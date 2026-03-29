import React from 'react';
import { Link } from 'react-router-dom';

export default function NotFound() {
    return (
        <div className="flex flex-col items-center justify-center p-20 text-center">
            <h1 className="text-6xl font-bold mb-4">404</h1>
            <p className="text-xl text-gray-600 mb-8">Page not found</p>
            <Link to="/" className="text-blue-600 font-semibold underline">Go Home</Link>
        </div>
    );
}
