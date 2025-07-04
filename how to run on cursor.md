
## ⚙️ Getting Started — Run FastAPI App in Cursor

Follow the steps below to set up and run the FastAPI application inside **Cursor (VS Code alternative)**:

---

### 🖥️ A. Open Terminal in Cursor

* Open the terminal either from the bottom pane or by using the shortcut:
  `Ctrl + Backtick` <kbd>Ctrl</kbd> + <kbd>\`</kbd>

---

### 🐍 B. Create Virtual Environment (only once)

```bash
python -m venv venv
```

This will create a new virtual environment named `venv` in your project folder.

---

### 🔋 C. Activate the Virtual Environment

```bash
.\venv\Scripts\activate
```

> ✅ You'll know it's activated when the terminal shows `(venv)` before your command prompt.

---

### 📦 D. Install Required Packages

```bash
pip install fastapi uvicorn python-multipart
```

This installs the necessary packages for the FastAPI app to run.

---

### 🚀 E. Run the FastAPI App

```bash
python -m uvicorn main:app --reload
```

> ✅ If successful, you’ll see a message similar to:

```
Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
```

---

### 🔍 Access Swagger UI (API Playground)

* Open your browser and go to:

```bash
http://127.0.0.1:8000/docs
```

This opens the **Swagger UI**, where you can test and interact with all available API endpoints visually.
