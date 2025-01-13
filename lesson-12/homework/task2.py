import requests
import random




def get_genre_id(api_key):
    url = f'https://api.themoviedb.org/3/genre/movie/list?api_key={api_key}&language=en-US'

    response = requests.get(url)
    response.raise_for_status()
    genres=response.json()
    print("Available genres: ")
    for idx, genre in enumerate(genres['genres'], start=1):
       print(f"{idx}. {genre['name']}")
    
    try:
       id=int(input(("Enter the number of genre you want: ")))
       id_genre=genres['genres'][id-1]['id']
       return id_genre
    except(ValueError, IndexError):
       print("Invalid choice. Exiting.")
       exit()
if __name__=='__main__':
    api_key='350197450fe048563815fab9487eea01'
    
    id=get_genre_id(api_key)
    movies_url = f'https://api.themoviedb.org/3/discover/movie?api_key={api_key}&with_genres={id}&language=en-US'
    resp=requests.get(movies_url)
    resp.raise_for_status()
    movies=resp.json()
    if movies['results']:
       random_movie=random.choice(movies['results'])
       title = random_movie['title']
       overview = random_movie['overview']
       release_date = random_movie['release_date']
       print(f"\nWe recommend the movie: {title}")
       print(f"Release Date: {release_date}")
       print(f"Overview: {overview}")
    else:
        print("No movies found for the selected genre.")

    
