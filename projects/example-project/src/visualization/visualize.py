"""
Script to create visualizations and reports.

This script should:
1. Load processed data and model results
2. Create exploratory data analysis plots
3. Generate model performance visualizations
4. Save figures for reports

Usage:
    python visualize.py
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path


def plot_data_distribution(df, target_column=None):
    """
    Create plots showing data distribution.
    
    Args:
        df: Input dataframe
        target_column: Target variable column name
    """
    fig, axes = plt.subplots(2, 2, figsize=(15, 10))
    
    # Distribution of numerical features
    numerical_cols = df.select_dtypes(include=['float64', 'int64']).columns
    if len(numerical_cols) > 0:
        df[numerical_cols].hist(bins=20, ax=axes[0, 0])
        axes[0, 0].set_title('Numerical Features Distribution')
    
    # Correlation heatmap
    if len(numerical_cols) > 1:
        corr_matrix = df[numerical_cols].corr()
        sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', ax=axes[0, 1])
        axes[0, 1].set_title('Correlation Matrix')
    
    # Target variable distribution (if provided)
    if target_column and target_column in df.columns:
        df[target_column].value_counts().plot(kind='bar', ax=axes[1, 0])
        axes[1, 0].set_title(f'{target_column} Distribution')
        axes[1, 0].tick_params(axis='x', rotation=45)
    
    plt.tight_layout()
    return fig


def plot_model_performance(y_true, y_pred, model_name="Model"):
    """
    Create model performance plots.
    
    Args:
        y_true: True labels
        y_pred: Predicted labels
        model_name: Name of the model
    """
    from sklearn.metrics import confusion_matrix, roc_curve, auc
    from sklearn.preprocessing import label_binarize
    import numpy as np
    
    fig, axes = plt.subplots(1, 2, figsize=(12, 5))
    
    # Confusion Matrix
    cm = confusion_matrix(y_true, y_pred)
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', ax=axes[0])
    axes[0].set_title(f'{model_name} - Confusion Matrix')
    axes[0].set_xlabel('Predicted')
    axes[0].set_ylabel('Actual')
    
    # ROC Curve (for binary classification)
    if len(np.unique(y_true)) == 2:
        fpr, tpr, _ = roc_curve(y_true, y_pred)
        roc_auc = auc(fpr, tpr)
        axes[1].plot(fpr, tpr, color='darkorange', lw=2, 
                    label=f'ROC curve (AUC = {roc_auc:.2f})')
        axes[1].plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--')
        axes[1].set_xlim([0.0, 1.0])
        axes[1].set_ylim([0.0, 1.05])
        axes[1].set_xlabel('False Positive Rate')
        axes[1].set_ylabel('True Positive Rate')
        axes[1].set_title(f'{model_name} - ROC Curve')
        axes[1].legend(loc="lower right")
    
    plt.tight_layout()
    return fig


def main():
    """Main function for creating visualizations."""
    project_dir = Path(__file__).resolve().parents[2]
    data_path = project_dir / 'data' / 'processed'
    figures_path = project_dir / 'reports' / 'figures'
    
    # Create figures directory if it doesn't exist
    figures_path.mkdir(parents=True, exist_ok=True)
    
    # Load your data here
    # df = pd.read_csv(data_path / 'your_data.csv')
    
    # Create and save data distribution plots
    # fig1 = plot_data_distribution(df, target_column='your_target')
    # fig1.savefig(figures_path / 'data_distribution.png', dpi=300, bbox_inches='tight')
    
    # Create and save model performance plots
    # y_true = ...  # Load true labels
    # y_pred = ...  # Load predictions
    # fig2 = plot_model_performance(y_true, y_pred)
    # fig2.savefig(figures_path / 'model_performance.png', dpi=300, bbox_inches='tight')
    
    # plt.show()  # Uncomment to display plots
    
    print("Visualizations created and saved!")


if __name__ == '__main__':
    main()