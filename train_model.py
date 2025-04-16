#!/usr/bin/env python
"""
Train and save the Framingham heart disease prediction model.
This script will train the model and save it as model1.pk1
"""

import os
import sys
from model import FraminghamModel

def train_and_save_model():
    """Train the model and save it as model1.pk1"""
    print("="*80)
    print("Training Framingham Heart Disease Prediction Model")
    print("="*80)
    
    # Initialize the model
    model = FraminghamModel()
    
    # Set custom path for the model
    model_path = 'model1.pk1'
    
    # Check if model already exists
    if os.path.exists(model_path):
        print(f"Model already exists at {model_path}")
        overwrite = input("Do you want to overwrite it? (y/n): ").lower()
        if overwrite != 'y':
            print("Exiting without training.")
            return False
    
    # Train the model
    print("\nTraining model...\n")
    success, metrics = model.train()
    
    if success:
        print("\nModel trained successfully!")
        print(f"Metrics: {metrics}")
        
        # Save to the specific filename
        model.save(model_path)
        print(f"\nModel saved to {model_path}")
        
        # Display model performance
        print("\nModel Performance:")
        print(f"  Accuracy:  {metrics['accuracy']:.4f}")
        print(f"  Precision: {metrics['precision']:.4f}")
        print(f"  Recall:    {metrics['recall']:.4f}")
        print(f"  F1 Score:  {metrics['f1']:.4f}")
        print(f"  AUC:       {metrics['auc']:.4f}")
        
        # Test prediction with sample data
        print("\nTesting model with sample data...")
        test_input = {
            'age': 55,
            'gender': True,  # Male
            'education': 2,
            'current_smoker': True,
            'cigs_per_day': 15,
            'bp_meds': False,
            'prevalent_stroke': False,
            'prevalent_hyp': True,
            'diabetes': False,
            'tot_chol': 240,
            'sys_bp': 150,
            'dia_bp': 95,
            'bmi': 30.5,
            'heart_rate': 80,
            'glucose': 95
        }
        
        result = model.predict(test_input)
        print(f"Sample prediction result: {result}")
        
        return True
    else:
        print("Failed to train model.")
        return False

if __name__ == "__main__":
    train_and_save_model() 