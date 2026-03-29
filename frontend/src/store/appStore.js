import { create } from 'zustand';

const useAppStore = create((set) => ({
    sessionId: null,
    fileName: null,
    columns: [],
    rowsCount: 0,
    chatHistory: [],
    datasetIssues: [],
    
    setSessionData: (data) => set({
        sessionId: data.session_id,
        fileName: data.filename,
        columns: data.columns,
        rowsCount: data.rows,
        datasetIssues: data.issues || []
    }),
    
    addChatMessage: (msg) => set((state) => ({
        chatHistory: [...state.chatHistory, msg]
    }))
}));

export default useAppStore;
