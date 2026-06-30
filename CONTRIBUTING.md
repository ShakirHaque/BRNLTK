# Contributing to brnltk

Contributions to **brnltk** are welcome. This includes bug reports, new
regional dialect mappings, additional linguistic rules, documentation
improvements, and code fixes.

## Reporting Issues

- Open an issue describing the bug or feature request.
- For bugs, include a minimal reproducible example, the expected behaviour,
  the actual behaviour, and your Python and operating system versions.

## Development Setup

1. Fork the repository and clone your fork:
   git clone https://github.com/ShakirHaque/BRNLTK.git
   cd BRNLTK
2. Create and activate a virtual environment:
   python -m venv venv
   source venv/bin/activate
3. Install the package in editable mode along with test dependencies:
   pip install -e .
   pip install pytest

## Running Tests

Before submitting any change, make sure all tests pass:

   pytest tests/ -v

If you add a new feature or fix a bug, please add or update a corresponding
test under the tests/ directory.

## Pull Request Process

1. Create a feature branch: git checkout -b feature/short-description
2. Make your changes and add tests for them.
3. Ensure all tests pass locally and the code follows PEP 8.
4. Commit with a clear message and push your branch.
5. Open a pull request describing the change and its motivation.

## Code Style

- Follow PEP 8 for Python code.
- Document public functions and classes with docstrings.

## License

By contributing, you agree that your contributions will be licensed under the
MIT License, the same license that covers this project.
