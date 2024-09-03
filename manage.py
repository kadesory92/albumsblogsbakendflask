import os

import click
from flask import Flask
from app import create_app, db
from flask_migrate import Migrate

# Create the application with the default configuration (or depending on the environment)
config_name = os.getenv('FLASK_CONFIG', 'development')
app = create_app(config_name)

# Configurer Flask-Migrate
migrate = Migrate(app, db)


# Commande personnalisée pour démarrer le serveur
@app.cli.command("runserver")
@click.option('--host', default='0.0.0.0', help='Adresse IP sur laquelle le serveur doit écouter.')
@click.option('--port', default=5000, help='Port sur lequel le serveur doit écouter.')
def runserver(host, port):
    """Démarrer le serveur Flask."""
    app.run(host=host, port=port)


# Commande personnalisée pour un shell interactif
@app.shell_context_processor
def make_shell_context():
    """Création d'un shell contextuel avec l'application et la base de données."""
    return dict(app=app, db=db)


if __name__ == '__main__':
    app.run()
