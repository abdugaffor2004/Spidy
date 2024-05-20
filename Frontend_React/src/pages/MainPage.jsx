import { Button } from "@/components/ui/button"
import { Input } from "@/components/ui/input"
import { Label } from "@/components/ui/label"
import { useState } from "react"
import { BsDash } from "react-icons/bs";
import { useNavigate } from "react-router-dom";

export const MainPage = () => {
    
    let [file, setFile] = useState(null)
    let [content, setContent] = useState({startPage: '', lastPage: '', questionAmount: ''})
    const navigate = useNavigate()
    const formData = new FormData();

    function handleSetFile(event) {
        const files = event.target.files;

        if (files?.length) {
            setFile(files[0]);
        }
    }

    function handleSubmit(e){
        e.preventDefault()
        console.log(file);
        console.log(content)

        if (!file) {
            return;
        }

        formData.append("file", file);
        Object.keys(content).forEach( (key) => formData.append(key, content[key]) );
        navigate("/result")
        
    }

    return(
        <div className="flex h-screen">
            `{/* <div className="w-2/3 flex flex-col items-center mt-10">
                <form className="grid  max-w-xs">
                    
                    <Label htmlFor="file">Нажмите сюда </Label>
                    <Input onChange={handleSetFile} accept=".pdf, .docx" id="file" type="file" className="max-w-72 mt-2 mb-4" />
                    <Button onClick={handleSubmit} type="submit">Отправить</Button>
                </form>
            </div>


            <div className="w-1/3 bg-green-600"></div> */}`


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
                    <Button onClick={handleSubmit} type="submit">Отправить</Button>
                </form>
            </div>



        </div>
    )
}