FROM python:3.11-slim

# Installer uv
RUN pip install uv

WORKDIR /app

# Copier les fichiers uv
COPY pyproject.toml uv.lock ./

# Installer les dépendances via uv
RUN uv sync --frozen

# Copier le projet
COPY . .

# Lancer Streamlit via uv
CMD ["uv", "run", "streamlit", "run", "main.py", "--server.port=8501", "--server.address=0.0.0.0"]
