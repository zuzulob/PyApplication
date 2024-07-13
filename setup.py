
**`setup.py`**

```python
from setuptools import setup, find_packages

setup(
    name="hello-world-python",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        'pytest',
    ],
    entry_points={
        "console_scripts": [
            "hello-world-python=src.main:main",
        ],
    },
)
