class Movie:
    movie = "Cinema"

    @staticmethod
    def static():
        return Movie.movie

    def __init__(self, name="", graduation_year=0, genre="", duration=0, number_of_reviews=0, imdb_rating=0.0):
        self.name = name
        self.graduation_year = graduation_year
        self.genre = genre
        self.duration = duration
        self.number_of_reviews = number_of_reviews
        self.imdb_rating = imdb_rating

    def __str__(self):
        return "Name: " + str(self.name) + \
               "\nGraduation year: " + str(self.graduation_year) + \
               "\nGenre: " + str(self.genre) + \
               "\nDuration: " + str(self.duration) + "minutes" + \
               "\nNumber of reviews: " + str(self.number_of_reviews) + \
               "\nIMDb Rating: " + str(self.imdb_rating)

    def __del__(self):
        pass


def main():
    the_godfather = Movie("'The Godfather'", 1972, "Crime", 175, 4255, 9.2)
    nice_guys = Movie("'Nice guys'", 1990, "Biographical drama", 146, 1398, 8.7)
    back_to_the_future = Movie("'Back to the future'", 1985, "Adventure comedy, fantasy", 175, 4255, 8.5)

    print(the_godfather.__str__(), "\n", "\n", nice_guys.__str__(), "\n", "\n", back_to_the_future.__str__())
    print(Movie.movie)
    Movie.static()


if __name__ == '__main__':
    main()
