import fresh_tomatoes
import media

#List of movies and their title, storyline, poster image, and trailer.
rocky_2 = media.Movie("Rocky 2",
                      "After an aspiring boxer, Rocky Balboa, lost the biggest fight of his newly-found career to the champion Apollo Creed, Rocky started getting national fame. Balboa faces the struggles of being a professional boxer as he prepares for the rematch of his life.",
                      "https://upload.wikimedia.org/wikipedia/en/b/bc/Rocky_ii_poster.jpg",
                      "https://www.youtube.com/watch?v=6PSSxAGSiCY")

dark_knight = media.Movie("The Dark Knight",
                          "As the city of Gotham has finally settled down, a new villian called by the name of Joker tries to ensue chaos on the citizens and Batman.",
                          "https://upload.wikimedia.org/wikipedia/en/8/8a/Dark_Knight.jpg",
                          "https://www.youtube.com/watch?v=EXeTwQWrcwY")

despicable_me = media.Movie("Despicable Me",
                            "When an intelligent super villian plans on stealing the moon with his yellow minions, three foster girls fight their way to save the world.",
                            "https://upload.wikimedia.org/wikipedia/en/thumb/d/db/Despicable_Me_Poster.jpg/220px-Despicable_Me_Poster.jpg",
                            "https://www.youtube.com/watch?v=sUkZFetWYY0")

breakfast_club = media.Movie("The Breakfast Club",
                             "Five students at New Trier High School share the same detention time. As time goes by, the differences from each person starts to reflect on eachother.",
                             "https://upload.wikimedia.org/wikipedia/en/thumb/5/50/The_Breakfast_Club.jpg/220px-The_Breakfast_Club.jpg",
                             "https://www.youtube.com/watch?v=ZXzlCpHK3-I")

the_warriors = media.Movie("The Warriors",
                           "As a local street gang gets falsley accused of killing the leader of the Gramercy Riffs, The Warriors flee to safety to their own turf from a horde of other gangs trying to get revenge.",
                           "https://upload.wikimedia.org/wikipedia/en/thumb/0/03/TheWarriors_1979_Movie_Poster.jpg/220px-TheWarriors_1979_Movie_Poster.jpg",
                           "https://www.youtube.com/watch?v=4GxSwUcm_XE")

gladiator = media.Movie("Gladiator",
                        "After being stabbed in the back by his brother for the throne of the Roman Empire, Maximus Meridius made his way from being a slave to fighting through gruesome battles in the Gladiator Arena to finally get revenge.",
                        "https://upload.wikimedia.org/wikipedia/en/thumb/8/8d/Gladiator_ver1.jpg/220px-Gladiator_ver1.jpg",
                        "https://www.youtube.com/watch?v=owK1qxDselE")
                                                      
movies = [rocky_2, dark_knight, despicable_me, breakfast_club, the_warriors, gladiator]
fresh_tomatoes.open_movies_page(movies)


