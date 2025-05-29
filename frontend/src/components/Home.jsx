// src/components/Home.jsx
import React, { useEffect, useState } from "react";
import { Link } from "react-router-dom";
import "./Home.css";
import YourMoviesContext from "./YourMoviesContext";
const Home = () => {
  const [allMovies, setAllMovies] = useState([]);
  const userId = 14; //USERID BRO

  useEffect(() => {
    fetch("http://localhost:8000/api/movies/all/")
      .then((res) => res.json())
      .then((data) => setAllMovies(data.movies));
  }, []);
// console.log(allMovies)
  const addMovie = async (movie)=>{
    const response= await fetch(`http://127.0.0.1:8000/api/wishlist/${userId}/${movie.id}/`, {
      method: "POST"
    })
    const parsedResponse = await response.json();
    alert(parsedResponse.message);

  }

  return (
    <div className="home-container">
      <h1 className="home-title"> Movies App</h1>
      <div className="section">
        <h2>All Movies</h2>
        <div className="movie-grid">
          {allMovies.map((movie) => (
            <div className="movie-card" key={movie.id}>
              <Link to={`/movie/${movie.id}`} ><img src={movie.image_url} alt={movie.title} /></Link>
              <h3>{movie.title}</h3>
              <div className="buttons">
                <Link to={`/movie/${movie.id}`} className="view-btn">View</Link>
                <button onClick={() => addMovie(movie)} className="add-btn">Add</button>

              </div>
            </div>
          ))}
        </div>
      </div>
      <YourMoviesContext />
    </div>
  );
};

export default Home;
