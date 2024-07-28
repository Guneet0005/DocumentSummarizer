import React from 'react';
import './App.css';
import axios from 'axios'
import { useEffect, useState } from 'react'

function App() {
  const [products, setProducts] = useState([])

  useEffect(() => {
    ;(async() => {
      const response = await axios.get('http://127.0.0.1:8000/upload-file')
      console.log(response.data);
    })()
    })


  return (
    <div>
      <h1>Upload File</h1>
      <input type ="file" name ="img" />
    </div>
  );
}

export default App;
