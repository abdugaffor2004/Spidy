import { Routes, Route } from 'react-router-dom'
import { MainPage } from './pages/MainPage'
import Results from './pages/Results'
import { QueryClient, QueryClientProvider } from 'react-query';
import { ReactQueryDevtools } from 'react-query/devtools';

function App() {

  const queryClient = new QueryClient();

  return (
    <>
      <QueryClientProvider client={queryClient}>
          <Routes>
            <Route path="/" element={<MainPage />}></Route>
            <Route path="/result" element={<Results />} />
          </Routes>
        

        <ReactQueryDevtools initialIsOpen={false} />
      </QueryClientProvider>
    </>
  )
}

export default App
