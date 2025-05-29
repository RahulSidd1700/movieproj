import React,{useEffect,useState} from 'react'

const YourMoviesContext = () => {
  const userId = 14;  //USERID BRO
  const [movies, setMovies] = useState([]);
  

  useEffect(()=>{
    const fetchMovies= async()=>{
      const response = await fetch(`http://localhost:8000/api/wishlist/${userId}/`);
       const parsedResponse = await response.json();
      setMovies(parsedResponse.movies)
    }
    fetchMovies()
  },[])
const removeMovie = async (movieId) => {
  const response = await fetch(`http://localhost:8000/api/wishlist/${userId}/${movieId}/`, {
    method: "DELETE"
  });
  const parsedResponse = await response.json();
  alert(parsedResponse.message);
};

  return (
    <div>
      <div className="section">
        <h2>Your Movies</h2>
        <div className="movie-grid">
          {movies.length === 0 ? (
            <p className="empty-text">You have no movies added yet.</p>
          ) : (
            movies.map((movie,index) => (
              
              <div className="movie-card" key={index}>
                <img src={movie.image_url} alt={movie.title} />
                
                <h3>{movie.title}</h3>
                <div className="buttons">
                  <button onClick={() => removeMovie(movie.movie_id)} className="remove-btn">Remove</button>
                </div>
              </div>
            ))
          )}
        </div>
      </div>
    </div>
  )
}

export default YourMoviesContext
