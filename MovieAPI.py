import requests, os

#example = https://api.themoviedb.org/3/movie/550?api_key=51a5043f9deab437ad0b47f82b3fa1a1
def get_movie_info(movie):
    #Connecting to API
    api_key = "51a5043f9deab437ad0b47f82b3fa1a1"
    api_base_url = "https://api.themoviedb.org/3"
    endpoint_path = f"/search/movie"
    endpoint = f"{api_base_url}{endpoint_path}?api_key={api_key}&query={movie}"

    #Sending HTTP request
    r = requests.get(endpoint)

    #Getiing data from API
    data = r.json()
    results = data['results']

    BASE_DIR = os.path.dirname(__file__)
    filename = os.path.basename(f"{movie}.txt")
    filepath = os.path.join(BASE_DIR, "Movie Files", filename)

    with open(filepath, 'w+') as f:
        for result in results:
            f.writelines("\n")
            info = {'Name':result['original_title'],
                    'Release Date' : result['release_date'],
                    'Popularity' : result['popularity'],
                    'Votes' : result['vote_count'],
                    'Overview': result['overview']}
            for i in info.keys():
                f.writelines(f"{i} : {info[i]}\n")

                