import { Routes, Route } from 'react-router-dom'
import { NotFound } from './pages/404'
import { MainPage } from './pages/MainPage'

function App() {

  return (
    <>
      <Routes>
        <Route path='/' element={ <MainPage /> }></Route>
        <Route path="/NotFound" element={ <NotFound /> }/>
      </Routes>
    </>
  )
}

export default App
