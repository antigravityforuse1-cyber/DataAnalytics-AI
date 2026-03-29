import React from 'react';
import { useNavigate } from 'react-router-dom';
import useAppStore from '../store/appStore';

export default function Dashboard() {
    const { fileName, columns, rowsCount, datasetIssues } = useAppStore();
    const navigate = useNavigate();

    if (!fileName) {
        return (
            <div className="p-8 text-center">
                <p className="mb-4">No active session.</p>
                <button onClick={() => navigate('/upload')} className="text-blue-600 underline">Go Upload</button>
            </div>
        );
    }

    return (
        <div className="flex flex-col gap-6">
            <div className="bg-white p-6 rounded shadow border">
                <h2 className="text-xl font-semibold mb-2">Dataset Overview</h2>
                <p><strong>File:</strong> {fileName}</p>
                <p><strong>Rows:</strong> {rowsCount}</p>
                <p><strong>Columns:</strong> {columns.join(', ')}</p>
            </div>

            <div className="bg-white p-6 rounded shadow border">
                <h2 className="text-xl font-semibold mb-2 text-red-600">Detected Issues ({datasetIssues.length})</h2>
                {datasetIssues.length === 0 ? (
                    <p className="text-green-600">No issues detected! Your data looks clean.</p>
                ) : (
                    <ul className="list-disc ml-5">
                        {datasetIssues.map((i, idx) => (
                            <li key={idx} className="mb-2">
                                <strong>{i.type}</strong>: {i.description}
                            </li>
                        ))}
                    </ul>
                )}
            </div>

            <button 
                onClick={() => navigate('/analysis')}
                className="w-48 px-4 py-2 bg-green-600 text-white text-center rounded hover:bg-green-700"
            >
                Go to Analysis Chat
            </button>
        </div>
    );
}
