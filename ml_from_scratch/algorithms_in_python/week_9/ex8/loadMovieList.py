def loadMovieList(filePath='movie_ids.txt'):
    """Reads the fixed movie list in movie.txt and returns a
    cell array of the words
       movieList = loadMovieList() reads the fixed movie list in movie.txt
       and returns a cell array of the words in movieList."""

    movieList = {}

    # Read the fixed movieulary list
    f = open(filePath, 'r')

    try:
        for idx, line in enumerate(f):
            tokens = line.split(' ')
            movieName = ' '.join(tokens[1:])
            movieList[idx] = movieName.strip()
    finally:
        f.close()

    return movieList
