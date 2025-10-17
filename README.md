# To-Do App

This is a simple to-do application built with FastAPI for the backend and Streamlit for the frontend.

## Requirements
- Python 3.7+
- FastAPI
- Uvicorn
- Streamlit

## Installation
1. Clone the repository.
2. Install the required packages:
   ```bash
   pip install fastapi uvicorn streamlit
   ```
3. Run the backend:
   ```bash
   uvicorn main:app --reload
   ```
4. Run the frontend:
   ```bash
   streamlit run frontend.py
   ```

## Usage
- Access the backend API at `http://127.0.0.1:8000`
- Access the frontend at `http://localhost:8501`.
