# Project Templates

This directory contains templates and boilerplate code for starting new data science projects.

## Available Templates

### `project-template/`
A standard data science project template with the following structure:

- **data/**: Store your datasets here
  - `raw/`: Original, immutable data
  - `interim/`: Intermediate data that has been transformed
  - `processed/`: Final, canonical datasets for modeling
  - `external/`: Data from third party sources

- **notebooks/**: Jupyter notebooks for exploration and prototyping
  - Number notebooks for easy ordering (e.g., `01-data-exploration.ipynb`)

- **src/**: Source code for production use
  - `data/`: Data processing scripts
  - `features/`: Feature engineering scripts
  - `models/`: Model training and prediction scripts
  - `visualization/`: Visualization utilities

- **tests/**: Unit tests for your code

- **docs/**: Documentation for your project

- **models/**: Trained and serialized models, model predictions, or model summaries

- **reports/**: Generated analysis as HTML, PDF, LaTeX, etc.
  - `figures/`: Generated graphics and figures to be used in reporting

## Usage

To create a new project:

1. Copy the `project-template` directory
2. Rename it to your project name
3. Update the README.md with project-specific information
4. Start coding!

```bash
cp -r templates/project-template/ projects/my-new-project/
cd projects/my-new-project/
# Update README.md and start working
```