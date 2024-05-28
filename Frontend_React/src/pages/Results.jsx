import { Header } from '@/components/ui/header'
import QuestionCard from '@/components/ui/questionCard';
import React, { useEffect, useState } from 'react'
import { useLocation, useNavigate } from 'react-router-dom'

function Results() {

// const {state} = useLocation()
const navigate = useNavigate();

const state = true

  useEffect( () =>{
    if(!state){
      navigate('/')
    }

  }, [state] )

  if (!state) {
    return null
  }

  return (
    <div className='no-scrollbar h-screen overflow-y-scroll'>  {/* Избавляеися от скроллбара. no-scrollbar добавил в tailwind.config -> plugins (это не встроенное свойство) */}
      <Header />
      <div className='py-10 flex flex-col items-center '>
        <QuestionCard isQuestionWithVariants={true} />
        <QuestionCard />
        <QuestionCard />
        <QuestionCard />
      </div>
    </div>
  )
}

export default Results