FROM python:3.10-slim

# Installer les dépendances système nécessaires à OpenCV
RUN apt-get update && apt-get install -y libglib2.0-0 libsm6 libxext6 libxrender-dev

# Créer un répertoire de travail
WORKDIR /app

# Copier les fichiers nécessaires
COPY requirements.txt requirements.txt
COPY app app

# Installer les dépendances Python
RUN pip install --no-cache-dir -r requirements.txt

# Exposer le port utilisé par FastAPI
EXPOSE 8000

# Commande pour démarrer l'application
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
