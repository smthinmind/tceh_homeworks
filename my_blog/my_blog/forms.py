
from wtforms_alchemy import ModelForm

from my_blog.models import Post


# https://wtforms-alchemy.readthedocs.org/en/latest/introduction.html
class PostForm(ModelForm):
    class Meta:
        model = Post
        include = [
            'user_id',
        ]
