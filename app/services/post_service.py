from app.extensions import db
from app.models import Post


class PostService:

    @staticmethod
    def create_post(title, content, user_id):
        new_post = Post(title, content, user_id)
        db.session.add(new_post)
        db.session.commit()
        return new_post, True

    @staticmethod
    def update_post(post_id, title = None, content = None):
        post = Post.query.get(post_id)

        if post:
            if title:
                post.title = title
            if content:
                post.content = content

            db.session.commit()
            return post
        return None

    @staticmethod
    def get_post_by_user(user_id):
        return Post.query.filter_by(user_id=user_id)

    @staticmethod
    def get_post_by_id(post_id):
        return Post.query.get(post_id)

    @staticmethod
    def get_all_posts(page=1, per_page=10):
        return Post.query.paginate(page=page, per_page=per_page, error_out=False)

    @staticmethod
    def search_posts(query):
        search = f"%{query}%"
        return Post.query.filter(
            db.or_(Post.title.ilike(search), Post.content.ilike(search))
        ).all()

    @staticmethod
    def delete_post(post_id):
        post = Post.query.get(post_id)
        if not post:
            return
        db.session.delete(post)
        db.session.commit()

    @staticmethod
    def like_post(post_id):
        post = Post.query.get(post_id)
        if not post:
            return None

        post.liked = True
        post.numberOfLike += 1
        db.session.commit()
        return post

    @staticmethod
    def unlike_post(post_id):
        post = Post.query.get(post_id)
        if not post:
            return None

        post.liked = False
        post.numberOfLike -= 1
        db.session.commit()
        return post
