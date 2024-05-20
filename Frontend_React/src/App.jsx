import { Routes, Route } from 'react-router-dom'
import { MainPage } from './pages/MainPage'
import Results from './pages/Results'

function App() {

  return (
    <>
      <Routes>
        <Route path="/" element={ <MainPage /> }></Route>
        <Route path="/result" element={ <Results /> }/>
      </Routes>
    </>
  )
}

export default App
