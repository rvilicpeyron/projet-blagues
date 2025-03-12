# Utiliser une image Python officielle
FROM python:3.9

# Définir le dossier de travail
WORKDIR /app

# Copier le code dans le conteneur
COPY . .

# Installer les dépendances
RUN pip install -r requirements.txt

# Commande pour démarrer l’application
CMD ["python", "main.py"]