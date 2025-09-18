# Data Science Project Guidelines

This document outlines the standards and best practices for all data science projects in this repository.

## Project Structure Standards

Every project must follow the template structure located in `/templates/project-template/`. This ensures consistency and makes it easier for team members to navigate and understand any project.

### Required Directories

- `data/` - All data files organized by processing stage
- `notebooks/` - Jupyter notebooks for exploration and analysis
- `src/` - Production-ready source code
- `tests/` - Unit tests for your code
- `docs/` - Project-specific documentation
- `models/` - Trained models and artifacts
- `reports/` - Generated reports and visualizations

### Required Files

- `README.md` - Project overview and instructions
- `requirements.txt` - Python dependencies
- `.gitignore` - Git ignore rules (inherit from repository root)

## Naming Conventions

### Projects
- Use lowercase letters with hyphens to separate words
- Be descriptive but concise
- Examples: `customer-churn-prediction`, `sales-forecasting`, `image-classification`

### Files and Directories
- Use lowercase for directories
- Use underscores for Python files (`snake_case`)
- Use hyphens for data files and reports
- Include version/date in data files when applicable

### Notebooks
- Number notebooks to indicate order: `01-`, `02-`, etc.
- Use descriptive names: `01-data-exploration.ipynb`
- Keep one main topic per notebook

## Code Quality Standards

### Python Style
- Follow PEP 8 style guidelines
- Use meaningful variable and function names
- Keep functions small and focused (< 50 lines preferred)
- Use type hints for function parameters and returns

### Documentation
- Write docstrings for all functions and classes
- Use Google-style docstrings
- Include examples in docstrings when helpful
- Keep inline comments concise and meaningful

### Testing
- Write unit tests for data processing functions
- Test edge cases and error conditions
- Aim for >80% code coverage
- Use pytest framework

## Data Management

### Data Organization
- **Raw data**: Never modify, keep original files immutable
- **Interim data**: Temporary files during processing
- **Processed data**: Final, clean datasets ready for modeling
- **External data**: Third-party data sources

### Data Documentation
- Create data dictionaries for all datasets
- Document data sources and collection methods
- Include data quality assessments
- Note any known limitations or biases

## Version Control

### Git Practices
- Make frequent, small commits
- Use descriptive commit messages
- Create feature branches for significant changes
- Don't commit large data files or models

### What Not to Commit
- Raw data files (> 10MB)
- Trained models (> 100MB)
- Personal configuration files
- Jupyter notebook outputs (clear before committing)

## Model Development

### Experimentation
- Use consistent evaluation metrics
- Document hyperparameters and model choices
- Track experiments with tools like MLflow when appropriate
- Create reproducible training scripts

### Model Documentation
- Document model architecture and parameters
- Include performance metrics on validation/test sets
- Explain feature importance and model interpretability
- Note any assumptions or limitations

## Reporting and Communication

### Jupyter Notebooks
- Clear narrative flow with markdown explanations
- Professional-quality visualizations
- Conclusions and next steps at the end
- Clear, reproducible code

### Reports
- Executive summary for non-technical stakeholders
- Technical methodology section
- Key findings with supporting evidence
- Actionable recommendations

### Presentations
- Focus on business impact
- Use clear, professional visualizations
- Include confidence intervals and limitations
- Prepare for Q&A about methodology

## Review Process

### Self-Review Checklist
- [ ] Code follows style guidelines
- [ ] All functions have docstrings
- [ ] Tests pass and coverage is adequate
- [ ] Notebooks have clear narrative flow
- [ ] README is complete and accurate
- [ ] No sensitive data or credentials committed

### Peer Review
- Review code for clarity and efficiency
- Verify reproducibility of results
- Check statistical methodology
- Ensure conclusions are supported by evidence