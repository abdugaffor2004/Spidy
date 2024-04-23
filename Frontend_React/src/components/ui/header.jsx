import { Link } from "react-router-dom";



export function Header(){
    return(
        <header>
            <nav className="bg-orange-500 py-2 flex justify-center">
                <Link className="bg-green-500 mx-3 px-2 py-1 rounded" to={'/NotFound'}> NotFound </Link>
                <Link className="bg-green-500 mx-3 px-2 py-1 rounded" to={'/'}> Home </Link>
            </nav>
        </header>
    )
}