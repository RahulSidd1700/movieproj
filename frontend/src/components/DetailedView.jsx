import React, { useEffect, useState, useContext } from "react";
import { useParams, Link } from "react-router-dom";
import "./DetailedView.css";

const DetailedView = () => {
  const { id } = useParams();
  const [movie, setMovie] = useState(null);


  useEffect(() => {
    fetch(`http://localhost:8000/api/movies/${id}/`)
      .then((res) => res.json())
      .then((data) => setMovie(data));
  }, [id]);

  if (!movie) return <p className="loading">Loading...</p>;


  return (
    <div className="detail-container">
      <Link to="/" className="back-button">← Back to Home</Link>
      <div className="detail-card">
        {movie.image_url && (
          <img src={movie.image_url} alt={movie.title} className="poster-img" />
        )}
        <div className="detail-info">
          <h2>{movie.title} ({movie.year})</h2>
          <p><strong>Genre:</strong> {movie.genre}</p>
          <p><strong>Rating:</strong> {movie.rating}/10</p>
          <p><strong>Review:</strong> {movie.review}</p>
          <p><strong>Watched Date:</strong> {movie.watched_date || "Not specified"}</p>
          {true ? (
            <button onClick={() => removeMovie(movie.id)} className="movie-button remove">Remove</button>
          ) : (
            <button onClick={() => addMovie(movie)} className="movie-button add">Add</button>
          )}
        </div>
      </div>
    </div>
  );
};

export default DetailedView;
