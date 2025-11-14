# `utils/` README — Core Utilities (Custom Exception & Logger)

This folder provides the **core utility modules** used throughout the **LLMOps FlipKart Product Recommender**.
It contains lightweight, reusable components for **error handling** and **logging**, ensuring that all project scripts and pipelines follow consistent debugging and traceability practices.

## 📁 Folder Overview

```text
utils/
├─ __init__.py          # Marks the directory as a package
├─ custom_exception.py  # Unified and detailed exception handling
└─ logger.py            # Centralised logging configuration
```

## ⚠️ `custom_exception.py` — Unified Error Handling

### Purpose

Defines a `CustomException` class that captures detailed debugging context whenever an error occurs — including the exact **file name**, **line number**, and **traceback**.

### Key Features

* Consistent formatting for all raised exceptions.
* Automatically detects the current exception via `sys.exc_info()` if not provided.
* Useful across any pipeline stage — data loading, preprocessing, or model inference.

### Example Usage

```python
from utils.custom_exception import CustomException
import sys

try:
    raise ValueError("Invalid input format.")
except Exception as e:
    raise CustomException("Pipeline execution error", sys) from e
```

### Output Example

```
Error in /llmops-flipkart-product-recommender/utils/example.py, line 8: Pipeline execution error
Traceback (most recent call last):
  File "/llmops-flipkart-product-recommender/utils/example.py", line 8, in <module>
    raise ValueError("Invalid input format.")
ValueError: Invalid input format.
```



## 🪵 `logger.py` — Centralised Logging

### Purpose

Provides a simple, centralised logging configuration used across the LLMOps project.
Each log entry is timestamped and written to a daily log file within a `logs/` directory.

### Log File Format

* Directory: `logs/`
* File name: `log_YYYY-MM-DD.log`
* Example: `logs/log_2025-11-10.log`

### Example Usage

```python
from utils.logger import get_logger

logger = get_logger(__name__)
logger.info("Initialising FlipKart Recommender pipeline.")
logger.warning("Missing entries detected in product metadata.")
logger.error("Model failed to load due to missing checkpoint.")
```

### Output Example

```
2025-11-10 19:42:01,120 - INFO - Initialising Anime Recommender pipeline.
2025-11-10 19:42:01,381 - WARNING - Missing entries detected in anime metadata.
2025-11-10 19:42:01,645 - ERROR - Model failed to load due to missing checkpoint.
```



## ✅ In Summary

* `custom_exception.py` — standardises how exceptions are reported across the codebase.
* `logger.py` — ensures consistent, timestamped logs for debugging and monitoring.
* Together with `__init__.py`, these modules provide the **core reliability utilities** supporting the **LLMOps FlipKart Product Recommender**.
  
