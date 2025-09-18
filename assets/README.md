# Assets Directory

This directory contains shared resources and utilities that can be used across multiple projects.

## Contents

- **scripts/**: Utility scripts for common tasks
- **images/**: Shared images, logos, or graphics
- **templates/**: Additional templates (beyond project template)
- **configs/**: Configuration files and settings

## Purpose

Assets provide reusable components that help maintain consistency and avoid duplication across projects.

## Usage

Reference assets from your projects using relative paths:
```python
import sys
sys.path.append('../../assets/scripts')
from data_utils import common_preprocessing
```