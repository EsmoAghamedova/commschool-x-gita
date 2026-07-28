# API Documentation

Base URL (local dev): `http://localhost:5000/api`

All protected routes require a header:

```
Authorization: Bearer <token>
```

---

## Authentication

### Register

`POST /api/auth/register`

**Auth required:** No

Request

```json
{
  "username": "alex",
  "email": "alex@example.com",
  "password": "supersecret"
}
```

Response `201`

```json
{
  "message": "User created successfully"
}
```

Response `400` (validation / duplicate email)

```json
{
  "error": "Email already registered"
}
```

---

### Login

`POST /api/auth/login`

**Auth required:** No

Request

```json
{
  "email": "alex@example.com",
  "password": "supersecret"
}
```

Response `200`

```json
{
  "token": "eyJhbGciOiJIUzI1NiIs...",
  "user": {
    "id": 1,
    "username": "alex",
    "email": "alex@example.com"
  }
}
```

Response `401`

```json
{
  "error": "Invalid email or password"
}
```

---

## Notes

### Get all notes

`GET /api/notes`

**Auth required:** Yes

Response `200`

```json
[
  {
    "id": 1,
    "title": "Python OOP",
    "content": "Classes and objects explanation...",
    "category": "Programming",
    "created_at": "2026-07-21T10:00:00Z"
  }
]
```

### Search notes

`GET /api/notes/search?q=python`

**Auth required:** Yes

Response `200` — same shape as "Get all notes", filtered.

### Create note

`POST /api/notes`

**Auth required:** Yes

Request

```json
{
  "title": "Python OOP",
  "content": "Classes and objects explanation...",
  "category": "Programming"
}
```

Response `201` — returns the created note object.

### Update note

`PUT /api/notes/<id>`

**Auth required:** Yes

Request — any subset of `title`, `content`, `category`.

Response `200` — returns the updated note object.

Response `404` if the note doesn't exist or doesn't belong to the user.

### Delete note

`DELETE /api/notes/<id>`

**Auth required:** Yes

Response `204` — no body.

---

## Study Sessions

### Create session

`POST /api/sessions`

**Auth required:** Yes

Request

```json
{
  "subject": "Python",
  "duration": 60
}
```

`duration` is in minutes. `created_at` is set by the server.

Response `201` — returns the created session object.

### Get sessions

`GET /api/sessions`

**Auth required:** Yes

Response `200`

```json
[
  {
    "id": 1,
    "subject": "Python",
    "duration": 60,
    "created_at": "2026-07-21T14:00:00Z"
  }
]
```

---

## Dashboard

### Get dashboard stats

`GET /api/dashboard`

**Auth required:** Yes

Response `200`

```json
{
  "total_minutes": 900,
  "current_streak_days": 7,
  "top_subject": "Python"
}
```

> Backend note: this can be computed on the fly from `sessions` for the MVP — no need for a separate stats table yet.

---

## Leaderboard

### Get ranking

`GET /api/leaderboard`

**Auth required:** Yes

Response `200`

```json
[
  { "rank": 1, "username": "alex", "total_minutes": 7200 },
  { "rank": 2, "username": "esmo", "total_minutes": 5880 },
  { "rank": 3, "username": "sarah", "total_minutes": 4500 }
]
```

---

## Error Format

All errors follow the same shape so the frontend can handle them generically:

```json
{
  "error": "Human-readable message here"
}
```

| Status | Meaning |
|---|---|
| 400 | Bad request / validation failed |
| 401 | Missing or invalid auth token |
| 403 | Authenticated, but not allowed to access this resource |
| 404 | Resource not found |
| 500 | Server error |