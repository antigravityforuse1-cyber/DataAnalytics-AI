import React from 'react';
import { NavLink } from 'react-router-dom';
import { Database, LayoutDashboard, BarChart2 } from 'lucide-react';

export default function Header() {
    return (
        <header className="bg-white border-b px-6 py-4 flex items-center justify-between">
            <div className="flex items-center gap-2">
                <Database className="text-blue-600" />
                <span className="text-xl font-bold text-gray-800">Data Assistant</span>
            </div>
            <nav className="flex items-center gap-6">
                <NavLink to="/upload" className={({isActive}) => isActive ? "text-blue-600 font-semibold" : "text-gray-500 hover:text-black"}>Upload</NavLink>
                <NavLink to="/dashboard" className={({isActive}) => isActive ? "text-blue-600 font-semibold" : "text-gray-500 hover:text-black"}>Dashboard</NavLink>
                <NavLink to="/analysis" className={({isActive}) => isActive ? "text-blue-600 font-semibold" : "text-gray-500 hover:text-black"}>Analysis</NavLink>
            </nav>
        </header>
    );
}
