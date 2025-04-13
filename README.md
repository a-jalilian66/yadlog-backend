# 📰 Yadlog Blog Backend

A modern, scalable, multi-language-ready Django backend for a blog system with production-ready Docker setup.

---

## 📁 Project Structure

```
yadlog-backend/
├── Dockerfile
├── docker-compose.yml
├── docker-compose.staging.yml
├── docker-compose.prod.yml
├── requirements/
│   ├── base.txt
│   ├── development.txt
│   └── production.txt
├── scripts/
│   ├── entrypoint.sh
│   ├── entrypoint.prod.sh
│   └── entrypoint.staging.sh
├── src/
│   ├── manage.py
│   ├── yadlog/          # Django project
│   │   ├── settings/
│   │   └── locale/
│   └── apps/
│       └── posts/       # Blog app
└── staticfiles/
```

---

## 🚀 Development Setup

```bash
docker-compose down -v
docker-compose up --build
```

- App: http://localhost:8001
- Admin: http://localhost:8001/admin/
- Default superuser: admin / admin (if `CREATE_SUPERUSER=true`)

---

## 📦 Features

### ✅ Blog App (`posts`)

- Models: Post, Category, Tag
- Multi-language support via `django-modeltranslation`
- Auto-generated translated slugs (with `TranslatedSlugMixin`)
- Tag & Category system
- MPTT support for nested categories

### ✅ Tech Stack

- Python 3.11
- Django 5+
- PostgreSQL
- Gunicorn + Nginx (in production)
- Docker / Docker Compose
- Static/media management with volumes

---

## ⚙️ Environments

- `docker-compose.yml` → Development
- `docker-compose.staging.yml` → Staging
- `docker-compose.prod.yml` → Production

---

## 🛠 Recommended Dev Setup

- Python interpreter from Docker
- `src/` marked as Sources Root (for clean imports like `from apps.posts...`)
- PyCharm Docker integration enabled

---

## ✅ Deployment

```bash
docker-compose -f docker-compose.prod.yml up --build
```

Or staging:

```bash
docker-compose -f docker-compose.staging.yml up --build
```

---