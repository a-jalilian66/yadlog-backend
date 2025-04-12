# Yadlog Backend

A clean and production-ready Django backend project for building a blog-style platform with user authentication, post
creation, and admin capabilities. It uses Docker for full environment management, and supports separate configurations
for development, staging, and production.

---

## 📖 About the Project

This is a classic Django backend project, intended to be extended into a full-featured blog platform. The current
structure supports:

- Admin panel for managing content
- Blog post creation (in progress)
- Ready-to-integrate authentication system
- Docker-based setup for multiple environments
- Proper static/media handling and deployment support

---

## 🚀 Running the Project (Development)

To start the project locally for development:

```bash
docker-compose up --build
```

Admin interface:

```
http://localhost:8001/admin/
```

You can log in using credentials created manually or through the `CREATE_SUPERUSER` environment variable.

> Be sure to copy and adjust `.env.development` to a new `.env` file before running.

---

## ⚙️ Running the Project (Production - Locally)

```bash
docker-compose -f docker-compose.prod.yml up --build
```

Nginx and Gunicorn are used in the production setup:

```
http://127.0.0.1
```

This will serve static files properly and is the recommended way to test production before deploying to a server or
service like Liara.

---

## 📁 Project Structure

```
yadlog-backend/
├── core/                    # Django project code
├── scripts/                 # Entrypoint scripts per environment
├── nginx/                   # Nginx configuration
├── .env.example             # Sample environment variables
├── docker-compose.yml       # Development configuration
├── docker-compose.prod.yml  # Production configuration
├── Dockerfile               # Docker build config
├── README.md                # Documentation
```

---

## 🔐 Environment Configuration

Before running the app, ensure you have a `.env` file.

Start by copying:

```bash
cp env.example .env
```

Required variables include:

```
POSTGRES_DB=your_db
POSTGRES_USER=your_user
POSTGRES_PASSWORD=your_pass
DJANGO_ALLOWED_HOSTS=127.0.0.1,localhost
DJANGO_CSRF_TRUSTED_ORIGINS=http://127.0.0.1:8004,http://localhost:8004
```

---

## 📦 Deployment Notes

- The production image runs with Gunicorn and Nginx
- Static and media files are collected and served
- You can easily deploy to a platform like Liara or any Docker-based VPS

---

## ✅ Features

- [x] Admin setup with Django defaults
- [x] Docker environment (dev + prod)
- [x] Static/media configuration  
  _(More features are in progress and will be added in future updates.)_

---

## 👨‍💻 Developer Superuser (Optional)

You can auto-create a superuser in development mode using:

```
CREATE_SUPERUSER=true
```

---

## 🧪 Testing Static Serving in Production

After running production:

```
http://127.0.0.1/static/admin/css/base.css
```

This should load properly if Nginx and `collectstatic` worked.

---

## 🤝 Contributions

Feel free to fork this repo, add features, and open PRs! The project is just getting started and will grow over time 🚀
