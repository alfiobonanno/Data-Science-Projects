"""
Common utility functions for data science projects.

This module contains reusable functions that can be used across multiple projects
to maintain consistency and reduce code duplication.
"""

import pandas as pd
import numpy as np
from typing import Tuple, List, Optional


def load_and_validate_data(file_path: str, expected_columns: List[str]) -> pd.DataFrame:
    """
    Load data from file and validate expected columns exist.
    
    Args:
        file_path: Path to the data file
        expected_columns: List of column names that should exist
        
    Returns:
        Loaded and validated DataFrame
        
    Raises:
        ValueError: If expected columns are missing
    """
    df = pd.read_csv(file_path)
    
    missing_columns = set(expected_columns) - set(df.columns)
    if missing_columns:
        raise ValueError(f"Missing expected columns: {missing_columns}")
    
    return df


def basic_data_info(df: pd.DataFrame) -> dict:
    """
    Get basic information about a DataFrame.
    
    Args:
        df: Input DataFrame
        
    Returns:
        Dictionary with basic statistics and info
    """
    return {
        'shape': df.shape,
        'memory_usage_mb': df.memory_usage(deep=True).sum() / 1024**2,
        'null_counts': df.isnull().sum().to_dict(),
        'dtypes': df.dtypes.to_dict(),
        'numeric_columns': df.select_dtypes(include=[np.number]).columns.tolist(),
        'categorical_columns': df.select_dtypes(include=['object']).columns.tolist()
    }


def split_features_target(df: pd.DataFrame, target_column: str) -> Tuple[pd.DataFrame, pd.Series]:
    """
    Split DataFrame into features and target.
    
    Args:
        df: Input DataFrame
        target_column: Name of the target column
        
    Returns:
        Tuple of (features DataFrame, target Series)
    """
    if target_column not in df.columns:
        raise ValueError(f"Target column '{target_column}' not found in DataFrame")
    
    X = df.drop(columns=[target_column])
    y = df[target_column]
    
    return X, y


def remove_outliers_iqr(df: pd.DataFrame, column: str, factor: float = 1.5) -> pd.DataFrame:
    """
    Remove outliers using the IQR method.
    
    Args:
        df: Input DataFrame
        column: Column name to check for outliers
        factor: IQR factor (1.5 is standard)
        
    Returns:
        DataFrame with outliers removed
    """
    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)
    IQR = Q3 - Q1
    
    lower_bound = Q1 - factor * IQR
    upper_bound = Q3 + factor * IQR
    
    return df[(df[column] >= lower_bound) & (df[column] <= upper_bound)]


def encode_categorical_features(df: pd.DataFrame, 
                               categorical_columns: Optional[List[str]] = None,
                               method: str = 'onehot') -> pd.DataFrame:
    """
    Encode categorical features.
    
    Args:
        df: Input DataFrame
        categorical_columns: List of categorical columns to encode
        method: Encoding method ('onehot' or 'label')
        
    Returns:
        DataFrame with encoded categorical features
    """
    df_encoded = df.copy()
    
    if categorical_columns is None:
        categorical_columns = df.select_dtypes(include=['object']).columns.tolist()
    
    if method == 'onehot':
        df_encoded = pd.get_dummies(df_encoded, columns=categorical_columns, prefix=categorical_columns)
    elif method == 'label':
        from sklearn.preprocessing import LabelEncoder
        for col in categorical_columns:
            le = LabelEncoder()
            df_encoded[col] = le.fit_transform(df_encoded[col])
    else:
        raise ValueError("Method must be 'onehot' or 'label'")
    
    return df_encoded


def create_project_structure(project_path: str) -> None:
    """
    Create standard project directory structure.
    
    Args:
        project_path: Path where the project should be created
    """
    import os
    
    directories = [
        'data/raw',
        'data/interim', 
        'data/processed',
        'data/external',
        'notebooks',
        'src/data',
        'src/features',
        'src/models',
        'src/visualization',
        'tests',
        'docs',
        'models',
        'reports/figures'
    ]
    
    for directory in directories:
        full_path = os.path.join(project_path, directory)
        os.makedirs(full_path, exist_ok=True)
    
    print(f"Project structure created at: {project_path}")


if __name__ == "__main__":
    # Example usage
    print("Data Science Utilities Module")
    print("Available functions:", [func for func in dir() if not func.startswith('_')])