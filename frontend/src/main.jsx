import React from 'react'
import ReactDOM from 'react-dom/client'
import { BrowserRouter, Routes, Route } from 'react-router-dom'
import './styles/index.css'
import Nav from './components/Nav'
import Landing from './pages/Landing'
import Auth from './pages/Auth'
import DatasetManager from './pages/DatasetManager'
import TrainingLab from './pages/TrainingLab'
import RobustnessLab from './pages/RobustnessLab'
import Explainability from './pages/Explainability'
import Comparison from './pages/Comparison'
import Admin from './pages/Admin'

function App(){
  return <BrowserRouter><Nav/><Routes>
    <Route path='/' element={<Landing/>} />
    <Route path='/auth' element={<Auth/>} />
    <Route path='/datasets' element={<DatasetManager/>} />
    <Route path='/training' element={<TrainingLab/>} />
    <Route path='/robustness' element={<RobustnessLab/>} />
    <Route path='/explainability' element={<Explainability/>} />
    <Route path='/comparison' element={<Comparison/>} />
    <Route path='/admin' element={<Admin/>} />
  </Routes></BrowserRouter>
}

ReactDOM.createRoot(document.getElementById('root')).render(<App />)
