import { Button } from "@/components/ui/button"
import { Input } from "@/components/ui/input"
import { Label } from "@/components/ui/label"
import { useState } from "react"

export const MainPage = () => {
    
    let [file, setFile] = useState(null)

    function handleSetFile(event) {
        const files = event.target.files;

        if (files?.length) {
            setFile(files[0]);
        }
    }

    function handleSubmit(e){
        e.preventDefault()
        console.log(file)

        if (!file) {
            return;
        }

        const formData = new FormData();
        formData.append("file", file);
    }

    return(
        <div className="flex h-screen">
            <div className="w-2/3 flex flex-col items-center mt-10">
                <form className="grid  max-w-xs">
                    
                    <Label htmlFor="file">Нажмите сюда </Label>
                    <Input onChange={handleSetFile} accept=".pdf, .docx" id="file" type="file" className="max-w-72 mt-2 mb-4" />
                    <Button onClick={handleSubmit} type="submit">Отправить</Button>
                </form>
            </div>


            <div className="w-1/3 bg-green-600"></div>
        </div>
    )
}