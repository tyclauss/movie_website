import webbrowser

# coding=utf-8
"""
Module to display movie object, attributes and instances
"""

class Movie():
    """
    Class object stores information about a movie
    """
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube_url):
        """
        initializes instance of class Movie
        """
        
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube_url

    # function that opens a movie trailer following a link
    def play_trailer(self):
        """
        initializing instance for opening youtube video
        """
        webbrowser.open(self.trailer_youtube_url)
