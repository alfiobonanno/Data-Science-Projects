# Data Directory

This directory contains all data files for the project.

## Structure

- **raw/**: Original, immutable data dump. Never edit these files.
- **interim/**: Intermediate data that has been transformed but not yet final.
- **processed/**: The final, canonical data sets for modeling.
- **external/**: Data from third party sources.

## Data Management Guidelines

1. **Never edit raw data files** - they should be immutable
2. **Document data sources** - include metadata about where data comes from
3. **Use version control** for small data files (< 10MB)
4. **For large datasets**, consider using data versioning tools like DVC
5. **Include sample data** for others to test your code