# Behave-pytest

Small utility package to integrate pytest asserts into Behave project.

## Quick start


Installation:

```bash
$ pip install behave-pytest
```

Add before_all hook into your project. like this (features/environment.py):

```python

from behave_pytest.hook import install_pytest_asserts

def before_all(context):
    install_pytest_asserts()
```

That's it. When running test you will see standard pytest assertion details:

![Behave + Pytest](pytest.png)
