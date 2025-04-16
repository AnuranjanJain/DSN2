import pandas as pd
import numpy as np
import pickle
import os
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score
from config import MODEL_CONFIG

# Version information for the model
MODEL_VERSION = "1.0.0"
MODEL_NAME = "Framingham Heart Disease Prediction Model"
MODEL_DATE = "2024-04-16"

class FraminghamModel:
    """Model for Framingham heart disease prediction"""
    
    def __init__(self, model_path=None):
        """Initialize model"""
        self.model_path = model_path or MODEL_CONFIG['model_path']
        self.dataset_path = MODEL_CONFIG['dataset_path']
        self.feature_mapping = MODEL_CONFIG['feature_mapping']
        self.pipeline = None
        self.features = None
        self.categorical_cols = None
        self.numerical_cols = None
        self.metrics = None
        self.version = MODEL_VERSION
        
    def load(self):
        """Load the trained model"""
        try:
            # Create directory if it doesn't exist
            dirname = os.path.dirname(self.model_path)
            if dirname:
                os.makedirs(dirname, exist_ok=True)
            
            # Load the model if it exists
            if os.path.exists(self.model_path):
                with open(self.model_path, 'rb') as f:
                    model_data = pickle.load(f)
                    self.pipeline = model_data['pipeline']
                    self.features = model_data['features']
                    self.categorical_cols = model_data['categorical_cols']
                    self.numerical_cols = model_data['numerical_cols']
                    if 'metrics' in model_data:
                        self.metrics = model_data['metrics']
                    if 'version' in model_data:
                        self.version = model_data['version']
                print(f"Loaded {MODEL_NAME} version {self.version}")
                return True
            else:
                return False
        except Exception as e:
            print(f"Error loading model: {e}")
            return False
    
    def save(self, custom_path=None):
        """Save the model to a custom path or the default path"""
        if self.pipeline is None:
            raise ValueError("No model to save. Train or load a model first.")
        
        # Use custom path if provided, otherwise use default
        save_path = custom_path or self.model_path
        
        # Create directory if it doesn't exist and if there is a directory in the path
        dirname = os.path.dirname(save_path)
        if dirname:  # Only try to create directory if path has a directory component
            os.makedirs(dirname, exist_ok=True)
        
        # Prepare model data
        model_data = {
            'pipeline': self.pipeline,
            'features': self.features,
            'categorical_cols': self.categorical_cols,
            'numerical_cols': self.numerical_cols,
            'version': MODEL_VERSION,
            'date': MODEL_DATE,
            'name': MODEL_NAME
        }
        
        # Add metrics if available
        if self.metrics:
            model_data['metrics'] = self.metrics
        
        # Save the model
        with open(save_path, 'wb') as f:
            pickle.dump(model_data, f)
        
        print(f"Model saved to {save_path}")
        return True
    
    def train(self):
        """Train the model on the Framingham dataset"""
        try:
            # Load dataset
            df = pd.read_csv(self.dataset_path)
            
            # Rename columns using feature mapping
            renamed_df = df.rename(columns={
                orig: mapped for orig, mapped in self.feature_mapping.items()
            })
            
            # Define features and target
            X = renamed_df.drop(columns=['target'])
            y = renamed_df['target']
            
            # Define categorical and numerical columns
            self.categorical_cols = ['education', 'gender']
            self.numerical_cols = [
                'age', 'current_smoker', 'cigs_per_day', 'bp_meds', 
                'prevalent_stroke', 'prevalent_hyp', 'diabetes', 
                'tot_chol', 'sys_bp', 'dia_bp', 'bmi', 
                'heart_rate', 'glucose'
            ]
            
            # Keep only needed columns
            all_cols = self.categorical_cols + self.numerical_cols
            X = X[all_cols]
            
            # Store feature list
            self.features = all_cols
            
            # Split data
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
            
            # Create preprocessing pipelines
            numerical_transformer = Pipeline(steps=[
                ('imputer', SimpleImputer(strategy='median')),
                ('scaler', StandardScaler())
            ])
            
            categorical_transformer = Pipeline(steps=[
                ('imputer', SimpleImputer(strategy='most_frequent')),
                ('onehot', OneHotEncoder(handle_unknown='ignore'))
            ])
            
            # Combine preprocessing steps
            preprocessor = ColumnTransformer(
                transformers=[
                    ('num', numerical_transformer, self.numerical_cols),
                    ('cat', categorical_transformer, self.categorical_cols)
                ]
            )
            
            # Create and train model pipeline
            self.pipeline = Pipeline(steps=[
                ('preprocessor', preprocessor),
                ('classifier', RandomForestClassifier(n_estimators=100, random_state=42))
            ])
            
            # Train the model
            self.pipeline.fit(X_train, y_train)
            
            # Evaluate on test set
            y_pred = self.pipeline.predict(X_test)
            y_prob = self.pipeline.predict_proba(X_test)[:, 1]
            
            # Calculate metrics
            self.metrics = {
                'accuracy': float(accuracy_score(y_test, y_pred)),
                'precision': float(precision_score(y_test, y_pred)),
                'recall': float(recall_score(y_test, y_pred)),
                'f1': float(f1_score(y_test, y_pred)),
                'auc': float(roc_auc_score(y_test, y_prob))
            }
            
            # Save model
            model_data = {
                'pipeline': self.pipeline,
                'features': self.features,
                'categorical_cols': self.categorical_cols,
                'numerical_cols': self.numerical_cols,
                'metrics': self.metrics
            }
            
            # Create directory if it doesn't exist
            os.makedirs(os.path.dirname(self.model_path), exist_ok=True)
            
            # Save the model
            with open(self.model_path, 'wb') as f:
                pickle.dump(model_data, f)
            
            print(f"Model trained successfully. Metrics: {self.metrics}")
            return True, self.metrics
            
        except Exception as e:
            print(f"Error training model: {e}")
            return False, {}
    
    def predict(self, input_data):
        """Make prediction with the model"""
        if self.pipeline is None:
            raise ValueError("Model not loaded. Call load() or train() first.")
        
        # Ensure input data has all required features
        required_features = self.features
        
        # Check if input_data is a dictionary and convert to DataFrame
        if isinstance(input_data, dict):
            input_df = pd.DataFrame([input_data])
        elif isinstance(input_data, pd.DataFrame):
            input_df = input_data
        else:
            raise ValueError("Input data must be a dictionary or DataFrame")
        
        # Check for missing features and fill with default values
        for feature in required_features:
            if feature not in input_df.columns:
                # Default values based on feature type
                if feature in self.categorical_cols:
                    if feature == 'gender':
                        input_df[feature] = False  # Default to female
                    else:
                        input_df[feature] = 1  # Default education
                else:
                    input_df[feature] = 0  # Default numerical value
        
        # Make prediction
        risk_prob = self.pipeline.predict_proba(input_df)[0][1]
        risk_class = self.pipeline.predict(input_df)[0]
        
        # Determine risk level
        if risk_prob < 0.1:
            risk_level = 'Low'
        elif risk_prob < 0.2:
            risk_level = 'Medium'
        else:
            risk_level = 'High'
        
        return {
            'risk_score': float(risk_prob),
            'risk_class': int(risk_class),
            'risk_level': risk_level
        }

# Initialize and load or train the model when imported
model = FraminghamModel()
if not model.load():
    print("Model not found. Training new model...")
    success, metrics = model.train()
    if success:
        print(f"Model trained with metrics: {metrics}")
    else:
        print("Failed to train model.")

# Function to get model features
def get_model_features():
    """Get model features for form generation"""
    if model.features is None:
        model.load()
    
    return {
        'features': model.features,
        'categorical_cols': model.categorical_cols,
        'numerical_cols': model.numerical_cols
    }

# Function to make prediction
def predict(input_data):
    """Make a prediction"""
    return model.predict(input_data)

if __name__ == "__main__":
    # If run directly, train the model
    print("Training Framingham heart disease prediction model...")
    success, metrics = model.train()
    if success:
        print("Model trained successfully!")
        print(f"Metrics: {metrics}")
        
        # Save the model with specific filename 
        model.save('model1.pk1')
        
        # Test prediction
        test_input = {
            'age': 50,
            'gender': True,  # Male
            'education': 2,
            'current_smoker': False,
            'cigs_per_day': 0,
            'bp_meds': False,
            'prevalent_stroke': False,
            'prevalent_hyp': True,
            'diabetes': False,
            'tot_chol': 250,
            'sys_bp': 140,
            'dia_bp': 90,
            'bmi': 28.5,
            'heart_rate': 75,
            'glucose': 85
        }
        
        result = model.predict(test_input)
        print(f"Test prediction: {result}")
    else:
        print("Failed to train model.") 