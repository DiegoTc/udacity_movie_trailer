import webbrowser

class Movie():
  """ This class provides a way yo store movie related information """
  VALID_RATINGS = ["G","PG","PG-13","R"]

  def __init__(self,movie_title,movie_storyline,poster_image_url,trailer_youtube):
    """This initialize the Movie class. It requieres the name and description of the movie.
       It's also needed the poster link and youtube triller link
    """
    self.title = movie_title
    self.storyline = movie_storyline
    self.poster_image_url = poster_image_url
    self.trailer_youtube_url = trailer_youtube

  def show_trailer(self):
    """ This functions opens the browser to a youtube video """
    webbrowser.open(self.trailer_youtube_url)
