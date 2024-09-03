def register_blueprints(app):
    from .auth_controller import auth_blueprint
    # from .user_controller import user_blueprint
    from .post_controller import post_blueprint
    # from .comment_controller import comment_blueprint
    # from .album_controller import album_blueprint
    # from .photo_controller import photo_blueprint
    #
    app.register_blueprint(auth_blueprint)
    # app.register_blueprint(user_blueprint)
    app.register_blueprint(post_blueprint)
    # app.register_blueprint(comment_blueprint)
    # app.register_blueprint(album_blueprint)
    # app.register_blueprint(photo_blueprint)
