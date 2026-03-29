import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import useAppStore from '../store/appStore';
import { uploadFile } from '../utils/api';
import ProgressBar from '../components/ProgressBar';

export default function Upload() {
    const [file, setFile] = useState(null);
    const [loading, setLoading] = useState(false);
    const navigate = useNavigate();
    const setSessionData = useAppStore(state => state.setSessionData);

    const handleUpload = async () => {
        if (!file) return;
        setLoading(true);
        try {
            const data = await uploadFile(file);
            setSessionData(data);
            navigate('/dashboard');
        } catch (error) {
            console.error(error);
            alert("Upload failed.");
        } finally {
            setLoading(false);
        }
    };

    return (
        <div className="flex flex-col items-center justify-center p-12 bg-white rounded shadow-sm border border-gray-100">
            <h1 className="text-2xl font-bold mb-4">Upload Dataset</h1>
            <p className="text-gray-500 mb-8">Supported formats: CSV, Excel</p>
            
            <input 
                type="file" 
                accept=".csv, .xlsx" 
                onChange={(e) => setFile(e.target.files[0])}
                className="mb-4"
            />
            {loading && <ProgressBar progress={50} />}
            <button 
                onClick={handleUpload}
                disabled={loading || !file}
                className="mt-4 px-6 py-2 bg-blue-600 text-white rounded hover:bg-blue-700 disabled:opacity-50"
            >
                {loading ? 'Uploading...' : 'Analyze Data'}
            </button>
        </div>
    );
}
