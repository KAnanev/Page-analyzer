# Page Analyzer

[![hexlet-check](https://github.com/KAnanev/Page-analyzer/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/KAnanev/Page-analyzer/actions/workflows/hexlet-check.yml)
[![Maintainability](https://api.codeclimate.com/v1/badges/da7e58734b9be8cb3a0a/maintainability)](https://codeclimate.com/github/KAnanev/Page-analyzer/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/da7e58734b9be8cb3a0a/test_coverage)](https://codeclimate.com/github/KAnanev/Page-analyzer/test_coverage)

**Page Analyzer** is a Flask web application for checking websites and storing page analysis history.

The application allows users to add URLs, run page checks and save the result in PostgreSQL. For every checked page it stores the HTTP status code, `<h1>`, `<title>` and meta description.

---

## Features

- Add and validate URLs
- Store checked URLs in PostgreSQL
- Run page checks on demand
- Parse HTML page metadata
- Save check history for each URL
- Display all added URLs and their latest checks
- Flash messages for validation and check results
- Production startup with Gunicorn
- Development workflow through Poetry and Makefile

---

## Tech stack

- Python 3.10
- Flask
- PostgreSQL
- psycopg / psycopg2-binary
- requests
- BeautifulSoup4
- validators
- Pydantic
- Poetry
- Gunicorn
- Pytest
- Flake8

---

## How it works

1. User submits a URL.
2. The application validates and normalizes it.
3. URL is stored in the `urls` table.
4. User starts a page check.
5. The app performs an HTTP request to the target page.
6. HTML is parsed with BeautifulSoup.
7. Status code, `h1`, `title` and description are saved in `url_checks`.
8. The check history is displayed on the URL page.

---

## Database schema

The project uses two PostgreSQL tables:

```text
urls
├── id
├── name
└── created_at

url_checks
├── id
├── url_id
├── status_code
├── h1
├── title
├── description
└── created_at
```

---

## Environment variables

Create a `.env` file in the project root:

```env
SECRET_KEY=change_me
DATABASE_URL=postgresql://user:password@localhost:5432/page_analyzer
```

`DATABASE_URL` is required for database connection.

---

## Installation

Clone the repository:

```bash
git clone https://github.com/KAnanev/Page-analyzer.git
cd Page-analyzer
```

Install dependencies:

```bash
make install
```

or directly with Poetry:

```bash
poetry install
```

---

## Database initialization

Create a PostgreSQL database and set `DATABASE_URL` in `.env`.

Then initialize tables:

```bash
make init_db
```

This command runs Flask CLI command `init-db` and creates the required tables.

---

## Local development

Run the development server:

```bash
make dev
```

The application will be available at:

```text
http://127.0.0.1:5000
```

---

## Production start

The project includes a Gunicorn startup command:

```bash
make start
```

By default, it uses port `8000`. You can override it:

```bash
PORT=8080 make start
```

---

## Tests and quality checks

Run tests:

```bash
make test
```

Run linter:

```bash
make lint
```

Run full check:

```bash
make check
```

Generate test coverage:

```bash
make test-coverage
```

---

## Project structure

```text
Page-analyzer/
├── page_analyzer/
│   ├── services/         # URL, database and page-checking services
│   ├── templates/        # HTML templates
│   ├── __init__.py       # Flask app factory
│   ├── db.py             # Database connection and init command
│   ├── database.sql      # SQL schema
│   └── views.py          # Flask routes
├── tests/                # Test suite
├── Makefile              # Common development commands
├── pyproject.toml        # Poetry dependencies and tool config
└── README.md
```

---

## Author

[KAnanev](https://github.com/KAnanev)
