
import math

movies = [
    {
        "title": "The Dune Chronicles",
        "year": 2021,
        "genres": {"sci-fi", "drama"},
        "rating": 8.6,
        "duration_min": 155,
        "actors": ["T. Chalamet", "R. Ferguson", "O. Isaac"],
    },
    {
        "title": "Kitchen Stories",
        "year": 2019,
        "genres": {"comedy", "drama"},
        "rating": 7.1,
        "duration_min": 98,
        "actors": ["A. Novak", "M. Ferguson"],
    },
    {
        "title": "silent hours",
        "year": 2016,
        "genres": {"thriller", "drama"},
        "rating": 6.4,
        "duration_min": 112,
        "actors": ["J. Bloom", "K. Lee"],
    },
    {
        "title": "Comet Racers",
        "year": 2023,
        "genres": {"sci-fi", "action"},
        "rating": 5.9,
        "duration_min": 101,
        "actors": ["O. Isaac", "P. Diaz"],
    },
    {
        "title": "The Last Bakery",
        "year": 2014,
        "genres": {"comedy"},
        "rating": 7.8,
        "duration_min": 89,
        "actors": ["A. Novak", "T. Chalamet"],
    },
    {
        "title": "midnight in oslo",
        "year": 2020,
        "genres": {"thriller", "mystery"},
        "rating": 8.9,
        "duration_min": 124,
        "actors": ["K. Lee", "R. Ferguson"],
    },
    {
        "title": "Garden of Static",
        "year": 2022,
        "genres": {"drama"},
        "rating": 4.8,
        "duration_min": 137,
        "actors": ["P. Diaz", "J. Bloom"],
    },
    {
        "title": "The Quiet Algorithm",
        "year": 2024,
        "genres": {"sci-fi", "drama"},
        "rating": 9.2,
        "duration_min": 118,
        "actors": ["M. Ferguson", "O. Isaac"],
    },
    {
        "title": "Two Left Shoes",
        "year": 2011,
        "genres": {"comedy"},
        "rating": 6.0,
        "duration_min": 95,
        "actors": ["A. Novak", "K. Lee"],
    },
    {
        "title": "Red Harbor",
        "year": 2018,
        "genres": {"action", "thriller"},
        "rating": 7.3,
        "duration_min": 129,
        "actors": ["P. Diaz", "T. Chalamet"],
    },
]





def average_rating(movies):
    total_rating = 0

    for movie in movies:
        total_rating += movie["rating"]

    average = total_rating / len(movies)

    return round(average, 1)


def catalog_age_stats(movies, current_year=2026):
    ages = []

    for movie in movies:
        age = current_year - movie["year"]
        ages.append(age)

    oldest = max(ages)
    newest = min(ages)

    total_age = sum(ages)
    average_age = total_age / len(ages)
    rounded_age = math.ceil(average_age)

    return oldest, newest, rounded_age


def duration_in_hours(minutes):
    hours = minutes // 60
    remaining_minutes = minutes % 60

    return f"{hours}ч {remaining_minutes}м"





def rating_tier(rating):
    if rating >= 9:
        return "шедевр"
    elif rating >= 7:
        return "хорошо"
    else:
        return "средне" if rating >= 5 else "слабо"


def decade_label(year):
    match year:
        case _ if year > 2020:
            return "новые"
        case _ if year >= 2015:
            return "недавние"
        case _:
            return "старые"




def find_first_masterpiece(movies):
    index = 0

    while index < len(movies):
        movie = movies[index]

        if movie["rating"] > 9.0:
            print("Найден фильм:", movie["title"])
            break

        index += 1

    else:
        print("Шедевров не найдено")


def count_long_movies(movies, threshold=120):
    count = 0

    for movie in movies:
        if movie["duration_min"] > threshold:
            count += 1

    return count




def normalize_title(title):
    words = title.split(" ")
    normalized_words = []

    for word in words:
        if word != "":
            first_letter = word[0].upper()
            other_letters = word[1:].lower()

            new_word = first_letter + other_letters
            normalized_words.append(new_word)

    result = " ".join(normalized_words)

    return result


def make_slug(title):
    normalized = normalize_title(title)
    slug = normalized.lower().replace(" ", "-")

    return slug


def format_report_line(movie):
    title = normalize_title(movie["title"])
    year = movie["year"]
    rating = movie["rating"]

    minutes = movie["duration_min"]
    duration = duration_in_hours(minutes)

    sorted_genres = sorted(movie["genres"])
    genres = ", ".join(sorted_genres)

    result = f'"{title}" ({year}) — {rating}/10, '
    result += f"{duration}, жанры: {genres}"

    return result





def get_movie_rating(movie):
    rating = movie["rating"]

    return rating


def titles_sorted_by_rating(movies):
    sorted_movies = sorted(
        movies,
        key=get_movie_rating,
        reverse=True,
    )

    titles = []

    for movie in sorted_movies:
        title = movie["title"]
        titles.append(title)

    return titles


def top_n_by_rating(movies, n=3):
    sorted_movies = sorted(
        movies,
        key=get_movie_rating,
        reverse=True,
    )

    top_movies = []

    for movie in sorted_movies[:n]:
        title = movie["title"]
        rating = movie["rating"]

        film = (title, rating)
        top_movies.append(film)

    return top_movies





def count_by_genre(movies):
    genre_counts = {}

    for movie in movies:
        for genre in movie["genres"]:
            count = genre_counts.get(genre, 0)
            genre_counts[genre] = count + 1

    return genre_counts


def actor_filmography(movies):
    filmography = {}

    for movie in movies:
        title = movie["title"]

        for actor in movie["actors"]:
            if actor not in filmography:
                filmography[actor] = []

            filmography[actor].append(title)

    return filmography



def movies_above_average(movies):
    average = average_rating(movies)

    result = {
        movie["title"]: movie["rating"]
        for movie in movies
        if movie["rating"] > average
    }

    return result





def all_genres(movies):
    genres = set()

    for movie in movies:
        genres.update(movie["genres"])

    return genres



def common_actors(movie1, movie2):
    actors1 = set(movie1["actors"])
    actors2 = set(movie2["actors"])

    common = actors1 & actors2

    return common


def genres_only_in_one(movies_a, movies_b):
    genres_a = all_genres(movies_a)
    genres_b = all_genres(movies_b)

    result = genres_a - genres_b

    return result



def iter_high_rated(movies, min_rating=8.0):
    for movie in movies:
        rating = movie["rating"]

        if rating >= min_rating:
            yield movie



def print_non_comedy_movies(movies):
    for movie in movies:
        if "comedy" in movie["genres"]:
            continue

        print(movie["title"])


def print_high_rated_movies(movies):
    for movie in iter_high_rated(movies):
        print(format_report_line(movie))


def total_duration_above_seven(movies):
    total = sum(
        movie["duration_min"]
        for movie in movies
        if movie["rating"] > 7
    )

    return total



def build_report(movies):
    print("ОТЧЕТ ПО КАТАЛОГУ")

    rating = average_rating(movies)
    print("Средний рейтинг:", rating)

    ages = catalog_age_stats(movies)
    average_age = ages[2]
    print("Средний возраст фильмов:", average_age, "лет")

    print("\nТоп-3 фильма:")

    sorted_movies = sorted(
        movies,
        key=get_movie_rating,
        reverse=True,
    )

    top_movies = sorted_movies[:3]

    for movie in top_movies:
        report_line = format_report_line(movie)
        print(report_line)

    print("\nФильмов по жанрам:")

    genre_counts = count_by_genre(movies)

    genre_names = sorted(genre_counts)

    genre_names = sorted(
        genre_names,
        key=genre_counts.get,
        reverse=True,
    )

    for genre in genre_names:
        count = genre_counts[genre]
        print(genre, "—", count)

    genres = all_genres(movies)
    sorted_genres = sorted(genres)
    genres_text = ", ".join(sorted_genres)

    print("\nВсе жанры каталога:", genres_text)



if __name__ == "__main__":
    build_report(movies)
