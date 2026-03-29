import React from 'react';

export default function ProgressBar({ progress }) {
    return (
        <div className="w-full h-2 bg-gray-200 rounded-full overflow-hidden">
            <div 
                className="h-full bg-blue-600 transition-all duration-300"
                style={{ width: `${progress}%` }}
            ></div>
        </div>
    );
}
