# Job board

[![Build Status](https://img.shields.io/endpoint.svg?url=https%3A%2F%2Factions-badge.atrox.dev%2Frombaks%2Fjob_board%2Fbadge%3Fref%3Ddevelop&style=flat)](https://actions-badge.atrox.dev/rombaks/job_board/goto?ref=develop)
[![Coverage Status](https://coveralls.io/repos/github/rombaks/job_board/badge.svg?branch=develop&kill_cache=1)](https://coveralls.io/github/rombaks/job_board?branch=develop)  
-----

### Project features

Project helps you to open job opportunity! It provides:

- post new jobs with descriptions;
- delete only jobs created by author;
- convenient search bar;
- documented API.

### Usage

-   Clone the repo.

```
git clone git@github.com:rombaks/job_board.git
```

-   Go to `backend` directory.

```
cd job_board/backend
```

-   Add your credentials to `.env` file for a local development

```
POSTGRES_USER=user
POSTGRES_PASSWORD=password
POSTGRES_SERVER=0.0.0.0
POSTGRES_PORT=5432
POSTGRES_DB=db

SECRET_KEY=better_use_bcrypt
```

-   Build docker-compose from backend directory

```
docker-compose build 
```

-   To run `bash` in created container

```
docker-compose run --rm api bash
```

-   To connect to `PostgreSQL` interactive terminal

```
docker-compose exec db psql -U postgres
```

-   Run app on http://localhost:8008 (set port in `docker-compose.yml` if necessary)

```
docker-compose up
```

---

### Additional info:

- API: FastAPI. Docs http://localhost:8008/docs/
- DateBase: PostrgeSQL 
- Dependency manager: Poetry
- Code style: Black, isort, flake8
- Typing: mypy, pydantic
- Tests: PyTest + Coveralls
- CI/CD: GitHub Actions
