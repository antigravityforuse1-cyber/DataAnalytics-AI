import axios from 'axios';

// The URL will point to Render automatically during the GitHub Actions build
const API_BASE_URL = process.env.REACT_APP_API_URL || 'http://localhost:8000/api';

const api = axios.create({
    baseURL: API_BASE_URL
});

export const uploadFile = async (file) => {
    const formData = new FormData();
    formData.append('file', file);
    const response = await api.post('/analysis/upload', formData, {
        headers: { 'Content-Type': 'multipart/form-data' }
    });
    return response.data;
};

export const askQuestion = async (sessionId, query) => {
    const response = await api.post('/analysis/ask', {
        session_id: sessionId,
        action: query
    });
    return response.data;
};

export default api;
