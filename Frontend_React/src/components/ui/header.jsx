import { Link } from "react-router-dom";



export function Header(){
    return(
        <header>
            <nav className="py-5 pr-3 flex justify-end">
                <Link className=" bg-slate-900 text-white mx-3 px-2 py-1 rounded" to={'/'}> Форма </Link>
            </nav>
        </header>
    )
}