# 📦 Changelog

All notable changes to this project will be documented in this file.

---

## [base-setup] - 2025-04-13

### Added

- Initialized blog system with `posts` app (Post, Category, Tag models)
- Setup multi-language support using `django-modeltranslation`
- Created `TranslatedSlugMixin` for multi-language slug generation
- Organized project using `src/` + `apps/` layout
- Added Docker support for development, staging, and production
- Added entrypoint scripts for different environments
- Initial Nginx configuration for static/media handling
- Configured environment-specific settings (dev, prod, staging)

---

## [Unreleased]

### In progress

- User authentication system
- Comments & interaction features
- API endpoints for public blog consumption