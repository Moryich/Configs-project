# Dotfiles Share

A REST API for sharing dotfiles and system configurations. Built with Django REST Framework, PostgreSQL, and JWT authentication.

## Tech Stack

- Python / Django / Django REST Framework
- PostgreSQL
- Docker
- JWT (via `djangorestframework-simplejwt`)
- `drf-spectacular` for Swagger UI

---

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/Moryich/Configs-project
cd Configs-project
```

### 2. Create and activate virtual environment

```bash
python3 -m venv venv
source venv/bin/activate.fish  # fish shell
# or
source venv/bin/activate       # bash/zsh
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Copy `.env.example` and fill in the values:

```bash
cp .env.example .env
```

`.env.example`:
```
SECRET_KEY=
DB_NAME=
DB_USER=
DB_PASSWORD=
```

### 5. Start the database

```bash
docker compose up -d
```

### 6. Apply migrations

```bash
python manage.py migrate
```

### 7. Run the server

```bash
python manage.py runserver
```

---

## API Documentation

Swagger UI is available at:

```
http://127.0.0.1:8000/api/v1/schema/swagger_ui/
```

---

## Endpoints

### Auth

| Method | URL | Description |
|--------|-----|-------------|
| POST | `/api/v1/auth/register/` | Register a new user |
| POST | `/api/v1/auth/login/` | Obtain JWT token pair |
| POST | `/api/v1/auth/refresh/` | Refresh access token |
| POST | `/api/v1/auth/verify/` | Verify token |

### Users

| Method | URL | Description | Auth required |
|--------|-----|-------------|---------------|
| GET | `/api/v1/users/` | List all users | No |
| GET | `/api/v1/users/{id}/` | Get user profile | No |
| GET | `/api/v1/users/me/` | Get own profile | Yes |
| PUT | `/api/v1/users/me/` | Update own profile | Yes |

### Configs

| Method | URL | Description | Auth required |
|--------|-----|-------------|---------------|
| GET | `/api/v1/configs/` | List all configs | No |
| POST | `/api/v1/configs/` | Upload a config | Yes |
| GET | `/api/v1/configs/{id}/` | Get config details | No |
| PUT | `/api/v1/configs/{id}/` | Update a config | Yes |
| DELETE | `/api/v1/configs/{id}/` | Delete a config | Yes |

---

## File Upload

Configs are uploaded as archives (`.zip`, `.tar.gz`, etc.) via `multipart/form-data`.

Example with curl:

```bash
curl -X POST http://127.0.0.1:8000/api/v1/configs/ \
  -H "Authorization: Bearer <your_token>" \
  -F "name=my bspwm config" \
  -F "description=daily driver" \
  -F "tags=WM" \
  -F "author_id=1" \
  -F "file=@/path/to/config.zip"
```

---

## Available Tags

`WM` `DE` `Shell` `Terminal` `NVim/Vim` `Emacs` `VSCode` `Bar` `Compositor` `Launcher` `Fetch` `Arch` `Debian` `NixOS` `Fedora` `Mint` `Gentoo` `Ubuntu`
