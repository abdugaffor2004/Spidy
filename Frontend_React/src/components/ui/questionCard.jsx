import React from 'react'
import { Accordion, AccordionTrigger, AccordionItem, AccordionContent } from './accordion'

function QuestionCard({ question, answer, answer_variants ,isQuestionsWithVariants}) {
  return (
      
    // <div className='flex justify-around border-2 border-slate-900 rounded-sm w-[620px] h-fit '>
    //     <div className='py-2 pl-2'>
    //         <h2>Как историческая наука развивалась в Древней Греции и Древнем Риме?</h2>
    //     </div>
    //     <div className=' h-fit mt-0.5 '>
    //         <span className='text-xs align-top underline'>Ответ</span>
    //     </div>
    // </div>

    <Accordion type='single' collapsible className='w-[620px]'>
        <AccordionItem value="item-1">
            <AccordionTrigger className="text-start">
              {question}?

            </AccordionTrigger>

            {isQuestionsWithVariants && <div>{answer_variants}</div>}
            
            <AccordionContent>
                {answer}
            </AccordionContent>
        </AccordionItem>
    </Accordion>
    
  )
}

export default QuestionCard