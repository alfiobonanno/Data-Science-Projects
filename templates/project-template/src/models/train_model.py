"""
Script to train machine learning models.

This script should:
1. Load feature-engineered data
2. Split data into train/validation/test sets
3. Train models with hyperparameter tuning
4. Save trained models

Usage:
    python train_model.py
"""

import pandas as pd
import joblib
from pathlib import Path
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report


def train_model(X_train, y_train, X_val, y_val):
    """
    Train a machine learning model.
    
    Args:
        X_train: Training features
        y_train: Training labels
        X_val: Validation features
        y_val: Validation labels
        
    Returns:
        Trained model
    """
    # Example with Random Forest
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    
    # Validate model
    y_pred = model.predict(X_val)
    accuracy = accuracy_score(y_val, y_pred)
    print(f"Validation Accuracy: {accuracy:.3f}")
    print("\nClassification Report:")
    print(classification_report(y_val, y_pred))
    
    return model


def main():
    """Main function for model training."""
    project_dir = Path(__file__).resolve().parents[2]
    data_path = project_dir / 'data' / 'processed'
    models_path = project_dir / 'models'
    
    # Create models directory if it doesn't exist
    models_path.mkdir(parents=True, exist_ok=True)
    
    # Load your data here
    # df = pd.read_csv(data_path / 'features.csv')
    # X = df.drop('target', axis=1)
    # y = df['target']
    
    # Split data
    # X_train, X_temp, y_train, y_temp = train_test_split(X, y, test_size=0.4, random_state=42)
    # X_val, X_test, y_val, y_test = train_test_split(X_temp, y_temp, test_size=0.5, random_state=42)
    
    # Train model
    # model = train_model(X_train, y_train, X_val, y_val)
    
    # Save model
    # joblib.dump(model, models_path / 'trained_model.pkl')
    
    print("Model training completed!")


if __name__ == '__main__':
    main()