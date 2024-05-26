import { getQuestions } from "@/api/api";
import { Button } from "@/components/ui/button"
import { Input } from "@/components/ui/input"
import Loader from "@/components/ui/loader";
import { useEffect, useState } from "react"
import { BsDash } from "react-icons/bs";
import { useQuery, useQueryClient } from "react-query";
import { useNavigate } from "react-router-dom";

export const MainPage = () => {
    
    let [file, setFile] = useState(null)
    let [content, setContent] = useState({startPage: '', lastPage: '', questionAmount: '', isQuestionsWithVariants: false})
    const navigate = useNavigate()
    const formData = new FormData();

    let {isLoading, isError, data, error, status , refetch, isSuccess} = useQuery(['questions', formData], () => getQuestions(formData), {enabled: false})
    let queryClient = useQueryClient()

    async function handleSetFile(event) {
        const files = event.target.files;

        if (files?.length) {
            setFile(files[0]);
        }
    }

    async function handleSubmit(e){
        e.preventDefault()
        console.log(file);
        console.log(content)

        if (!file) {
            return;
        }

        formData.append("file", file);
        Object.keys(content).forEach( (key) => formData.append(key, content[key]) );
        
        refetch()

    }
    
    useEffect(() => {
        if (status === "success") {
            navigate("/result", {state: data});
            queryClient.clear() // Сброс статуса react-query
        }
    }, [status, navigate]);
     // без useEffect будет ошибка: Cannot update a component (`BrowserRouter`) while rendering a different component (`MainPage`). To locate the bad setState() call inside `MainPage`, follow the stack trace as described


    if (isLoading) {
        return <Loader />
    }



    console.log(data)   

    return(
        <div className="flex h-screen">

            <div className="w-full flex flex-col items-center mt-10">
                <form className="grid max-w-xs">

                    <Input onChange={handleSetFile} accept=".pdf, .docx" id="file" type="file" className="max-w-72 mt-2 mb-4" />

                    {/* <Label htmlFor="pages"> Страницы </Label> */}
                    <div id="pages" className="flex justify-start">
                        <Input onChange={(e) => setContent({ ...content, startPage: e.target.value }) } placeholder='Начало' id="file" type="number" className="max-w-20 mt-2 mb-4 [&::-webkit-inner-spin-button]:appearance-none" />
                        <BsDash size={42} className="mt-2"/>
                        <Input onChange={(e) => setContent({ ...content, lastPage: e.target.value })} placeholder='Конец' id="file" type="number" className="max-w-20 mt-2 mb-4 [&::-webkit-inner-spin-button]:appearance-none" />
                        <Input onChange={(e) => setContent({ ...content, questionAmount: e.target.value })} placeholder='№' id="file" type="number" className="max-w-16 mt-2 mb-4 ml-5 [&::-webkit-inner-spin-button]:appearance-none" />
                    </div>

                    <div className="flex mt-3">
                        <input type="checkbox" onChange={(e) => setContent({...content, isQuestionsWithVariants: e.target.checked})} className="h-4 w-4 rounded-sm border border-primary ring-offset-background focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 disabled:cursor-not-allowed disabled:opacity-50 accent-slate-800"/>
                        <label htmlFor="questionsType" className="text-sm ml-2 font-medium leading-none peer-disabled:cursor-not-allowed peer-disabled:opacity-70"> Вопросы с вариантами ответов </label>
                    </div>

                    <p className="text-sm mt-2 mb-3 text-muted-foreground">
                        Значением по умолчанию является вопрос без вариантов ответа
                    </p>
                    

                    <Button onClick={handleSubmit} type="submit">Отправить</Button>
                </form>
            </div>



        </div>
    )
}