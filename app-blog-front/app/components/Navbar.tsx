import React from "react";

const Navbar = () => {
    return(
        <nav className="bg-indigo-600 text-white p-4 sticky top-0 z-50">
            <div className="container mx-auto flex justify-between items-center">
                
                <h1 className="text-xl font-bold">Mi blog</h1>
                <ul className="flex space-x-4">
                    <li><a href="/" className="hover:text-gray-300">Inicio</a></li>
                    <li><a href="/" className="hover:text-gray-300">crear</a></li>
                </ul>

            </div>

        </nav>
    )
}

export default Navbar;