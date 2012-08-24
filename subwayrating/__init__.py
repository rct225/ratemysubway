from subwayrating.models import CommentWithRating
from subwayrating.forms import CommentFormWithRating

def get_model():
    return CommentWithRating

def get_form():
    return CommentFormWithRating
