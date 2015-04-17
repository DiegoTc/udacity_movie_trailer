import fresh_tomatoes
import media

toy_story = media.Movie("Toy Story","A story of a boy and his toys that come to life","http://upload.wikimedia.org/wikipedia/commons/0/0a/Toy_Story_logo.svg","https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar = media.Movie("Avatar", "The story of a marine on a alien planet","http://www.rodandocine.com/wp-content/uploads/2009/11/avatar-carteles3.jpg", "https://www.youtube.com/watch?v=kbA9TfGphOI&")

starwars = media.Movie("Star Wars VII", "he Force Awakens is set approximately 30 years after the events of Return of the Jedi, and features three new leads alongside characters returning from previous Star Wars films","http://upload.wikimedia.org/wikipedia/commons/2/22/Star-wars-the-force-awakens-teaser-poster1-405x600.jpg","https://www.youtube.com/watch?v=OMOVFvcNfvE")

godfather = media.Movie("The Godfather","The Godfather is a 1972 American crime film directed by Francis Ford Coppola and produced by Albert S. Ruddy from a screenplay by Mario Puzo and Coppola. Starring Marlon Brando and Al Pacino as the leaders of a fictional New York crime family, the story spans the years 1945-55, concentrating on the transformation of Michael Corleone from reluctant family outsider to ruthless Mafia boss while chronicling the Corleones under the patriarch Vito.","http://upload.wikimedia.org/wikipedia/en/1/1c/Godfather_ver1.jpg","https://www.youtube.com/watch?v=sY1S34973zA")

oceantwelve = media.Movie("Ocean's Twelve","Ocean's Twelve is a 2004 American comedy heist film, which acts as the sequel to 2001's Ocean's Eleven. Like its predecessor, which was a remake of the 1960 heist film Ocean's 11, the film was directed by Steven Soderbergh and used an ensemble cast. ","http://upload.wikimedia.org/wikipedia/en/8/83/Ocean%27s12Poster1.gif","https://www.youtube.com/watch?v=Ze4WPu2kHus")

hunguergames = media.Movie("The Hunger Games","The Hunger Games is a 2012 American science fiction adventure film directed by Gary Ross and based on the novel of the same name by Suzanne Collins.","http://upload.wikimedia.org/wikipedia/en/thumb/4/42/HungerGamesPoster.jpg/220px-HungerGamesPoster.jpg","https://www.youtube.com/watch?v=4S9a5V9ODuY")

movies = [toy_story,avatar,starwars,godfather,oceantwelve,hunguergames]

fresh_tomatoes.open_movies_page(movies)
