# group-h Music Recommendation App

Welcome to the group-h Music Recommendation App repository. This project is a full-stack application featuring separate frontend (FE) and backend (BE) components.

## Author

Jongwon Kang (<suta6034@gmail.com>)

## Table of Contents

- [Project Structure](#project-structure)
- [Frontend (FE)](#frontend-fe)
- [Backend (BE)](#backend-be)
- [Connecting FE and BE](#connecting-fe-and-be)
- [Global Development Guidelines](#global-development-guidelines)

---

## Project Structure

```
BE/                # Python Flask backend
    ├── app.py
    ├── requirements.txt
FE/                # Vue 3 frontend (Vite)
    └── music-app/
            ├── src/
            ├── package.json
            ├── .prettierrc.json
            ├── .editorconfig
            ├── .vscode/
            └── ...
.gitignore
README.md
```

---

## Frontend (FE)

**Location:** `FE/music-app`

**Tech Stack:**

- Vue 3
- Vite
- TypeScript
- Vuetify (UI & styling library)
- ESLint & Prettier

**Setup Instructions:**

1. Install dependencies:
   ```sh
   cd FE/music-app
   npm install
   ```
2. Start development server:
   ```sh
   npm run dev
   ```
3. Build for production(maybe not relevant for us):
   ```sh
   npm run build
   ```
4. Lint code:
   ```sh
   npm run lint
   ```

**Formatting & Linting:**

- Code style is enforced using Prettier and ESLint.
- VS Code users: Enable "Format on Save" and use the recommended extensions in `.vscode/extensions.json`.
- See `.prettierrc.json`, `.editorconfig`, and `eslint.config.ts` for configuration details.

---

## Backend (BE)

**Location:** `BE`

**Tech Stack:**

- Python 3
- Flask
- flask-cors

**Setup Instructions:**

> **Important:** Every developer must create and activate a Python virtual environment before installing dependencies. This keeps project dependencies isolated and avoids conflicts.

1. Create and activate a virtual environment:
   ```powershell
   cd BE
   python -m venv venv
   .\venv\Scripts\activate
   ```
2. Install dependencies:
   ```powershell
   pip install -r requirements.txt
   ```
3. Run the backend server:
   ```powershell
   python app.py
   ```

**Endpoints:**

- `/` : Returns a simple text message (for FE connection test)

---

## Connecting FE and BE

- The FE Vue app fetches data from the BE Flask server (e.g., from the `/` endpoint).
- Ensure the backend is running and CORS is enabled (`flask-cors` is installed and configured).
- Update FE code to fetch from the backend, e.g.:
  ```js
  fetch("http://localhost:5000/");
  ```

---

## Global Development Guidelines

- Use `.gitignore` in the root to exclude `venv/`, `__pycache__/`, `*.pyc`, `node_modules/`, `dist/`, and other build artifacts.
- All team members should use the recommended VS Code extensions and enable formatting on save.
- For questions or setup issues, refer to the individual `README.md` files in `FE/music-app` and this root file.

---
