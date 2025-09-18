# Models Directory

This directory contains trained models, model artifacts, and predictions.

## Structure

- **trained/**: Serialized trained models (pickle, joblib, h5, etc.)
- **predictions/**: Model predictions on test/validation sets
- **checkpoints/**: Model checkpoints during training
- **summaries/**: Model performance summaries and metrics

## Best Practices

1. **Version your models** - Include timestamps or version numbers
2. **Document model metadata** - Training date, parameters, performance
3. **Save preprocessing steps** - Include scalers, encoders, etc.
4. **Track experiments** - Use tools like MLflow or Weights & Biases