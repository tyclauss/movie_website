# coding=utf-8
"""
Module that uses the content of media.py to define class movie
"""

import fresh_tomatoes
import media

# various instances of class Movie created and populated with data
baby_driver = media.Movie(
    "Baby Driver",
    "A story of a baby that drives cars",
    "https://images-na.ssl-images-amazon.com/images/M/MV5BMDA0N2U0OTUtN2U3My00NDg4LTgwNTctZmMyOWExMDdjMjE0XkEyXkFqcGdeQXVyMDc2NTEzMw@@._V1_SY1000_SX675_AL_.jpg",  # noqa
    "https://www.youtube.com/watch?v=z2z857RSfhk")

horrible_bosses = media.Movie(
    "Horrible Bosses",
    "Three guys that hate their bosses",
    "https://images-na.ssl-images-amazon.com/images/M/MV5BNzYxNDI5Njc5NF5BMl5BanBnXkFtZTcwMDUxODE1NQ@@._V1_UY1200_CR90,0,630,1200_AL_.jpg",  # noqa
    "https://www.youtube.com/watch?v=VpUeQV8sdOc")

the_big_lebowski = media.Movie(
    "The Big Lebowski",
    "A story about nothing",
    "https://s-media-cache-ak0.pinimg.com/736x/63/9a/41/639a4130e36855d4000e3a39bd7ce469--all-movies-the-big-lebowski.jpg",  # noqa
    "https://www.youtube.com/watch?v=cd-go0oBF4Y")

# list to store instances created
lstMovies = [baby_driver, horrible_bosses, the_big_lebowski]

# calls on fresh tomatoes file for html, css,
# and javascript to open the webpage
fresh_tomatoes.open_movies_page(lstMovies)
