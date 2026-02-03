# hello_python

Minimal Python "Hello World" project.

Run locally (macOS / Linux):

```bash
# from project root
python -m pip install --upgrade pip
python -m pip install -e .
python -m hello
```

Or without installing:

```bash
PYTHONPATH=src python -m hello
```

Run tests with `pytest`:

```bash
pip install pytest
PYTHONPATH=src pytest -q
```
