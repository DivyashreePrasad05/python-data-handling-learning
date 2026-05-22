"""
 Challenge:  Personal Movie Tracker with JSON

Create a Python CLI tool that lets users maintain their own personal movie database, like a mini IMDb.

Your program should:
1. Store all movie data in a `movies.json` file.
2. Each movie should have:
   - Title
   - Genre
   - Rating (out of 10)
3. Allow the user to:
   - Add a movie
   - View all movies
   - Search movies by title or genre
   - Exit the app

Bonus:
- Prevent duplicate titles from being added
- Format output in a clean table
- Use JSON for reading/writing structured data
"""

import os 
import json

FILE_NAME = "movies.json"

def load_movies():
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME , 'r' , encoding ="utf-8") as f:
     """load = json.load(f)  return load"""
    return json.load(f)     # read json file 

def save_movies(movies):
    #creates file
    with open(FILE_NAME , 'w' , encoding ="utf-8")as f :
        json.dump(movies , f , indent= 2)

def add_movies(movies):
    movie_title = input("Enter the name of the movie : ").strip().lower()

    #check for title
    if any(movie["title"].lower() == movie_title for movie in movies):
        print("The movie exixts already!...")
        return
    
    genre = input("Genre : ").strip().lower()

    try:
        rating = float(input("Enter rating(0-10)"))
        if not 0 <= rating >=10:
            raise ValueError
    except ValueError :
        print("Please enter the valid number between the range!")
        return

    movies.append({"title" :  movie_title , "genre": genre , "rating" : rating})
    save_movies(movies)
    print("Movie added successfully!")

def view_movies(movies):
    if not movies:
        print("No movies data in database")
        return

    print("-" * 30)
    for movie in movies:
             print(f"{movie["title"]} -- {movie["genre"]} -- {movie["rating"]}")
    print("-" * 30)
    

def search_movies(movies):
    term = input("Enter a movie name or genre : ").strip().lower()

    results = [
              movie for movie in movies
              if term in movie['title'].lower() or term in movie['genre'].lower()
    ]
    if not results:
        print("No found match result")
        return
        #search matched
    print(f"found {len(results)} results")

    for movie in results:
        print(f"{movie["title"]} -- {movie["genre"]} -- {movie["rating"]}")

def run_database():
   movies = load_movies()

   while True:
      print("\n🍿 MyMovieDB")
      print("1.Add a movie")
      print("2.View all movies")
      print("3.Search movies by title or genre")
      print("4.Exit the app") 

      choice = input("Choose an option (1-4): ").strip()
      match choice:
            case "1": add_movies(movies)
            case "2": view_movies(movies)
            case "3": search_movies(movies)
            case "4": break
            case _: print("Enter valid choice") 

if __name__ == "__main__":
    run_database()

    