import fresh_tomatoes
import media


big_lebowski = media.Movie("Big Lebowski",
                           "A flick bout a dude whose rug is stolen.",
                           "https://www.youtube.com/watch?v=cd-go0oBF4Y",
                           "http://www.imdb.com/title/tt0118715/?ref_=nv_sr_1")

the_game = media.Movie("The Game",
                       "A bored with life guy gets to play an interesting game.",
                       "https://www.youtube.com/watch?v=0kqQNBR09Rc",
                       "http://www.imdb.com/title/tt0119174/?ref_=fn_al_tt_1")

clean_shaven = media.Movie("Clean, Shaven",
                           "World from a schizophrenic POV",
                           "https://www.youtube.com/watch?v=6aInRjIwjpU",
                           "http://www.imdb.com/title/tt0106579/?ref_=nv_sr_1")

braindead = media.Movie("Braindead",
                        "Gore comedy classic from Peter Jackson.",
                        "https://www.youtube.com/watch?v=O8LIug1cP04",
                        "http://www.imdb.com/title/tt0103873/?ref_=fn_al_tt_1")

total_recall = media.Movie("Total Recall",
                           "Guy has a sweet tooth for exciting vacation.",
                           "https://www.youtube.com/watch?v=2DwNb-ZGVjE",
                           "http://www.imdb.com/title/tt0100802/?ref_=nv_sr_1")

a_scanner_darkly = media.Movie("A Scanner Darkly",
                               "Undercover operation against new and deadly drug.",
                               "https://www.youtube.com/watch?v=hkjDUERgCQw",
                               "http://www.imdb.com/title/tt0405296/?ref_=nv_sr_1")


movies = [big_lebowski, the_game, clean_shaven,
          braindead, total_recall, a_scanner_darkly]


# print big_lebowski.yt_trailer_id

sorted_movies = sorted(movies, key=lambda x: x.rating, reverse=True)


fresh_tomatoes.open_movies_page(sorted_movies)


# for movie in sorted_movies:
#   print movie.title + ' ' + str(movie.rating)
