import React from 'react'
import './App.css'
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom'
import Home from './components/Home'
import Login from './components/Login'
import Register from './components/Register'
import DetailedView from './components/DetailedView'
function App() {
  // const [count, setCount] = useState()
  // useEffect(() => {
  //   const fetchdata=async()=>{
  //     const response=await fetch('http://localhost:8000/users/')
  //     const data=await response.json()
  //     setCount(data)
  //   }
  //   fetchdata()
  // },[]) //componentdidmount, componentdidupdate, componentwillunmount
  // console.log(count)
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/login" element={<Login />} />
        <Route path="/register" element={<Register />} />
        <Route path="*" element={<div>404 not found</div>} />

      </Routes>
    </Router>
  )
}

export default App
