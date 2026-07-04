# Contributing

First off, thank you for taking the time to contribute to Archive Flattener.

We welcome bug reports, feature requests, documentation improvements, and code contributions.

---

## Development Setup

Clone the repository:

```bash
git clone https://github.com/<username>/archive-flattener.git
cd archive-flattener
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it.

Windows:

```bash
.venv\Scripts\activate
```

Linux/macOS:

```bash
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Coding Standards

Please follow these guidelines:

- Follow PEP 8
- Write descriptive variable names
- Keep functions focused
- Add comments only where they improve readability
- Preserve backward compatibility whenever possible

---

## Commit Messages

Use Conventional Commits whenever possible.

Examples:

```
feat: add password-protected zip support

fix: prevent duplicate filename collision

docs: improve README examples

refactor: simplify archive detection
```

---

## Pull Requests

Before opening a PR:

- Ensure the code runs successfully.
- Update documentation if necessary.
- Keep pull requests focused on a single feature or fix.
- Test your changes.

Thank you for contributing.