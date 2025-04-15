import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
import pickle
import sys
import traceback

try:
    # Load dataset
    print("Loading dataset...")
    data = pd.read_csv('cleaned_heart_disease_dataset.csv')

    # Print dataset info
    print(f"Dataset shape: {data.shape}")
    print(f"Columns: {data.columns.tolist()}")
    
    # Check data types and identify categorical columns
    print("\nData types:")
    print(data.dtypes)
    
    # Separate features and target
    X = data.drop('heart_disease', axis=1)
    y = data['heart_disease']
    
    # Identify categorical columns that need encoding
    categorical_cols = X.select_dtypes(include=['object']).columns.tolist()
    numerical_cols = X.select_dtypes(exclude=['object']).columns.tolist()
    
    print(f"\nCategorical columns: {categorical_cols}")
    print(f"Numerical columns: {numerical_cols}")
    
    # Preprocessing for categorical data
    categorical_transformer = OneHotEncoder(drop='first', sparse_output=False, handle_unknown='ignore')
    
    # Preprocessing for numerical data
    numerical_transformer = StandardScaler()
    
    # Combine preprocessing steps
    preprocessor = ColumnTransformer(
        transformers=[
            ('num', numerical_transformer, numerical_cols),
            ('cat', categorical_transformer, categorical_cols)
        ])
    
    # Create and train the pipeline
    print("\nCreating and training pipeline...")
    model_pipeline = Pipeline(steps=[
        ('preprocessor', preprocessor),
        ('classifier', RandomForestClassifier(n_estimators=100, random_state=42))
    ])
    
    # Split the data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Train the model pipeline
    model_pipeline.fit(X_train, y_train)
    
    # Evaluate the model
    train_score = model_pipeline.score(X_train, y_train)
    test_score = model_pipeline.score(X_test, y_test)
    print(f"Training accuracy: {train_score:.4f}")
    print(f"Testing accuracy: {test_score:.4f}")
    
    # Extract feature importance
    # Note: Feature names will be different due to one-hot encoding
    feature_importances = model_pipeline.named_steps['classifier'].feature_importances_
    
    # Create a dictionary to map feature indices to feature names
    preprocessor = model_pipeline.named_steps['preprocessor']
    feature_names = []
    
    # Get the feature names for numerical features
    feature_names.extend([f"{col}" for col in numerical_cols])
    
    # Get the feature names for categorical features (with one-hot encoding)
    if categorical_cols:
        ohe = preprocessor.named_transformers_['cat']
        cat_feature_names = ohe.get_feature_names_out(categorical_cols).tolist()
        feature_names.extend(cat_feature_names)
    
    # Create feature importance DataFrame
    feature_importance = pd.DataFrame({
        'Feature': feature_names,
        'Importance': feature_importances
    }).sort_values('Importance', ascending=False)
    
    print("\nFeature Importance:")
    print(feature_importance.head(10))
    
    # Save the entire pipeline (which includes the preprocessor and model)
    print("\nSaving model pipeline...")
    with open('model1.pk1', 'wb') as f:
        pickle.dump({
            'pipeline': model_pipeline, 
            'features': X.columns.tolist(),
            'categorical_cols': categorical_cols,
            'numerical_cols': numerical_cols
        }, f)
    
    print("Model saved as model1.pk1")

except Exception as e:
    print("Error occurred:")
    print(str(e))
    traceback.print_exc() 