import os
import random
import requests
from faker import Faker
from app import create_app
from app.extensions import db
from app.models import User, Post, Comment, Album, Photo

# Create Flask App instance
app = create_app(os.getenv('FLASK_ENV') or 'development')

# Context of the app to accede DB
with app.app_context():
    # Supprimez les tables existantes et créez de nouvelles tables
    db.drop_all()
    db.create_all()

    # Initialiser Faker pour générer des données aléatoires
    faker = Faker()

    # Récupérer les utilisateurs depuis JSONPlaceholder
    users_data = requests.get('https://jsonplaceholder.typicode.com/users').json()
    for user_data in users_data:
        user = User(
            username=user_data['username'],
            email=user_data['email']
        )
        user.set_password(faker.password())
        db.session.add(user)

    # Valider les utilisateurs
    db.session.commit()

    # Récupérer les posts depuis JSONPlaceholder
    posts_data = requests.get('https://jsonplaceholder.typicode.com/posts').json()
    for post_data in posts_data:
        user_id = post_data['userId']
        post = Post(
            title=post_data['title'],
            content=post_data['body'],
            user_id=user_id,
            liked=bool(random.getrandbits(1)),  # Randomly true or false
            numberOfLike=random.randint(0, 100)  # Nombre aléatoire entre 0 et 100
        )
        db.session.add(post)

    # Retrieve comments from JSONPlaceholder
    comments_data = requests.get('https://jsonplaceholder.typicode.com/comments').json()
    for comment_data in comments_data:
        comment = Comment(
            content=comment_data['body'],
            post_id=comment_data['postId'],
            user_id=random.randint(1, len(users_data))  # Associate comments to random users
        )
        db.session.add(comment)

    # Retrieve albums from JSONPlaceholder
    albums_data = requests.get('https://jsonplaceholder.typicode.com/albums').json()
    for album_data in albums_data:
        title = album_data['title']
        if title is None:
            title = "Untitled Album"  # Assign a default title

        album = Album(
            title=title,
            user_id=album_data['userId']
        )
        db.session.add(album)

    # Récupérer les photos depuis JSONPlaceholder
    photos_data = requests.get('https://jsonplaceholder.typicode.com/photos').json()
    for photo_data in photos_data:
        title = photo_data['title'],

        if title is None:
            title = "Untitled Photo"

        photo = Photo(
            title=title,
            url=photo_data['url'],
            thumbnailUrl=photo_data['thumbnailUrl'],
            album_id=photo_data['albumId'],
            liked=bool(random.getrandbits(1)),  # Randomly true or false
            numberOfLike=random.randint(0, 100)  # Random number between 0 and 100
        )
        db.session.add(photo)

    # Commit all changes
    db.session.commit()

    print("The database has been populated successfully!")
