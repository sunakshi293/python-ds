# Sample movie data
movies = [
    {"name": "Forrest Gump", "year": 1994, "duration": 142, "genres": ["Drama", "Romance"]},
    {"name": "Avengers: Endgame", "year": 2019, "duration": 181, "genres": ["Action", "Adventure", "Drama"]},
    {"name": "Back to the Future", "year": 1985, "duration": 114, "genres": ["Adventure", "Comedy", "Sci-Fi"]}
]

def print_welcome_message():
    print("Welcome to the Movie Admin CLI!")

def list_movies():
    if not movies:
        print("No movies found.")
    else:
        for index, movie in enumerate(movies, start=1):
            print(f"{index}. {movie['name']} ({movie['year']}) - {movie['duration']} min - Genres: {', '.join(movie['genres'])}")

def add_movie():
    name = input("Enter movie name: ")
    year = int(input("Enter the year: "))
    duration = int(input("Enter duration (in minutes): "))
    genres = input("Enter genres : ")
    genres = [genre.strip() for genre in genres]  
    movies.append({"name": name, "year": year, "duration": duration, "genres": genres})
    print(f"Movie '{name}' added successfully.")

def search_movie():
    name = input("Enter movie name to search: ")
    found_movies=[movie for movie in movies if name.lower() in movie['name'].lower()]
    if found_movies:
        for movie in found_movies:
            print(f"{movie['name']} ({movie['year']}) - {movie['duration']} min - Genres: {(movie['genres'])}")
    else:
        print("No movies found with that name.")

def view_movie():
    name = input("Enter movie name to view: ")
    for movie in movies:
        if movie['name'].lower() == name.lower():
            print(f"Name: {movie['name']}\nYear: {movie['year']}Duration: {movie['duration']} min Genres: {', '.join(movie['genres'])}")
            return
    print("Movie not found.")

def delete_movie():
    name = input("Enter movie name to delete: ")
    global movies
    movies = [movie for movie in movies if movie['name'].lower() != name.lower()]
    print(f"Movie '{name}' deleted successfully." if any(movie['name'].lower() == name.lower() for movie in movies) else "Movie not found.")

def main():
    print_welcome_message()
    while True:
        choice = input("Choose [a]dd, [l]ist, [s]earch, [v]iew, [d]elete or [q]uit: ").lower()
        if choice == 'a':
            add_movie()
        elif choice == 'l':
            list_movies()
        elif choice == 's':
            search_movie()
        elif choice == 'v':
            view_movie()
        elif choice == 'd':
            delete_movie()
        elif choice == 'q':
            print("Goodbye!")
            break
        else:
            print("Invalid choice")
            


    

