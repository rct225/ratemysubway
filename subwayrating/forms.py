from django import forms
from django.contrib.comments.forms import CommentForm
from subwayrating.models import CommentWithRating

class CommentFormWithRating(CommentForm):
    rating = forms.CharField(max_length=300)

    def get_comment_model(self):
        # Use our custom comment model instead of the built-in one.
        return CommentWithRating

    def get_comment_create_data(self):
        # Use the data of the superclass, and add in the title field
        data = super(CommentFormWithRating, self).get_comment_create_data()
        data['rating'] = self.cleaned_data['rating']
        return data