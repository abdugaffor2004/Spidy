import { Header } from '@/components/ui/header'
import React from 'react'
import { useLocation } from 'react-router-dom'

function Results() {

const {state} = useLocation()

  console.log(state)

  return (
    <div>
      <Header />
      {state.fileName}
    </div>
  )
}

export default Results