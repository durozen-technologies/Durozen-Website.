# DUROZEN Creative Portfolio - Admin Portal & FastAPI Backend

This document explains how to run, configure, and use the new **Admin Portal** and **FastAPI + PostgreSQL Backend** for managing live client demo websites on the DUROZEN portfolio.

---

## 🚀 Quick Start Guide

### 1. Start the FastAPI Backend

Open a terminal in the project root directory and run:

```bash
npm run backend
```
*Or double click:* `backend\start.bat`

The backend will start at:
- **API URL**: `http://localhost:8000`
- **Swagger Interactive API Docs**: `http://localhost:8000/docs`
- **Health Check**: `http://localhost:8000/api/health`

### 2. Start the Frontend Website

In a second terminal:

```bash
npm run dev
```

Visit:
- **Public Portfolio**: `http://localhost:3000`
- **Admin Portal**: `http://localhost:3000/admin`

---

## 🔐 Default Admin Credentials

- **Username**: `admin`
- **Password**: `durozenAdmin2026!`

*(You can customize these anytime in `backend/.env`)*

---

## 🐘 PostgreSQL Configuration

In `backend/.env`, configure your PostgreSQL connection string:

```env
DATABASE_URL=postgresql://postgres:postgres@localhost:5432/durozen_db
USE_SQLITE_FALLBACK=true
```

### Steps to create the local PostgreSQL database:
1. Open pgAdmin or `psql` shell:
   ```sql
   CREATE DATABASE durozen_db;
   ```
2. Put your PostgreSQL username and password in `backend/.env`.
3. Restart the backend (`npm run backend`). It will automatically connect and create the `projects` table!

> **Note on Zero-Downtime Fallback:**
> If your local PostgreSQL is not currently running, `USE_SQLITE_FALLBACK=true` allows the backend to automatically fall back to local storage (`durozen_local.db`) so development is never interrupted.

---

## 🛠️ Admin Portal Features

1. **Add New Demo Sites**:
   - Provide site name, Netlify/live demo URL, category, tagline, description, DUROZEN accent color, client name, and tags.
2. **Instant Live Preview**:
   - Test external links with one click or preview the live site inside an interactive modal.
3. **Edit Demo Sites**:
   - Update URLs, descriptions, or change categories.
4. **Delete Demo Sites**:
   - Remove demo sites with safety confirmation.
5. **Seed Default Sites**:
   - One-click restore to import the 10 original DUROZEN demo projects into PostgreSQL.
6. **Automatic Portfolio Sync**:
   - Any demo site added or modified in the Admin Portal automatically shows up live on the main DUROZEN portfolio home page!

