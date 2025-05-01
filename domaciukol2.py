import csv
import json

movies = []

with open("netflix_titles.tsv", encoding="utf-8") as file:
    data = csv.DictReader(file, delimiter="\t")
    for row in data:
        # title
        title = row["PRIMARYTITLE"]

        # directors
        directors = []
        if row['DIRECTOR']:
            parts = row["DIRECTOR"].split(",")
            for dir in parts:
                directors.append(dir.strip())

        # cast
        cast = []
        if row["CAST"]:
            parts = row["CAST"].split(",")
            for ca in parts:
                cast.append(ca.strip())

        # genres
        genres = []
        if row["GENRES"]:
            parts = row["GENRES"].split(",")
            for gen in parts:
                genres.append(gen.strip())

        decade = None
        if row["STARTYEAR"] and row["STARTYEAR"].isdigit():
            year = int(row["STARTYEAR"])
            decade = (year // 10) * 10

        movie = {
            "title": title,
            "directors": directors,
            "cast": cast,
            "genres": genres,
            "decade": decade
        }
        movies.append(movie)

with open("hw02_output_Burdejova.json", "w", encoding="utf-8") as outputfile:
    json.dump(movies, outputfile, ensure_ascii=False, indent=2)
