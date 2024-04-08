import { Link, Routes, Route } from 'react-router-dom'
import { Button } from './components/ui/button'
import { NotFound } from './pages/404'
import { MainPage } from './pages/MainPage'
import { Header } from './components/ui/header'

function App() {

  return (
    <>
    
      <Header />

      <Routes>
        <Route path='/' element={ <MainPage /> }></Route>
        <Route path="/NotFound" element={ <NotFound /> }/>
      </Routes>
    </>
  )
}

export default App
