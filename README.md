# Redkite

Python package for Redkite.

## Package names

- PyPI distribution name: `Redkite`
- Python import package: `redkite`

PyPI normalizes project names, so `Redkite`, `redkite`, and `red-kite` are treated as the same project name for registration and installation.

## Installation

After the first release is published to PyPI:

```bash
python -m pip install Redkite
```

Then import the package:

```python
import redkite

print(redkite.__version__)
```

## Local development

Create and activate a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate
```

Install the package in editable mode with packaging tools:

```bash
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

Build the source distribution and wheel:

```bash
python -m build
```

Validate the built distributions:

```bash
python -m twine check dist/*
```

## Publishing to PyPI

The project metadata lives in `pyproject.toml` and is configured for the PyPI package name `Redkite`.

Before the first publish:

1. Create or sign in to the PyPI account `InteralDigital`.
2. Enable two-factor authentication on the account.
3. Create an API token:
   - For the first upload, use an account-scoped token because the `Redkite` project does not exist on PyPI yet.
   - After the first release creates the project, replace it with a project-scoped token for `Redkite`.
4. Store the token locally in `~/.pypirc`, or provide it through your release automation secrets.

Example `~/.pypirc`:

```ini
[pypi]
username = __token__
password = pypi-your-api-token-here
```

### Recommended first publish flow

Test the package on TestPyPI first:

```bash
python -m build
python -m twine check dist/*
python -m twine upload --repository testpypi dist/*
```

Install from TestPyPI in a fresh environment:

```bash
python -m pip install --index-url https://test.pypi.org/simple/ --no-deps Redkite
python -m redkite
```

If the TestPyPI release looks correct, publish to production PyPI:

```bash
python -m twine upload dist/*
```

After upload, the package page should be available at:

https://pypi.org/project/Redkite/

### GitHub Actions publishing

This repository includes a GitHub Actions workflow at `.github/workflows/publish.yml`.

It runs when:

- a maintainer starts it manually from the Actions tab with `workflow_dispatch`
- a version tag matching `v*` is pushed, such as `v0.1.0`

Before running the workflow:

1. In GitHub, go to repository **Settings** > **Environments**.
2. Create an environment named `Redkite`.
3. Add an environment secret named `PYPI_TOKEN`.
4. Set `PYPI_TOKEN` to the PyPI API token for the `InteralDigital` account.

The publish job uses the `Redkite` environment and exposes that secret to Twine as the `PYPI_TOKEN` environment variable.

## Versioning releases

Before every release, update the version in `pyproject.toml`.

PyPI does not allow re-uploading the same version, even if a release file is deleted, so increment the version for each publish.
