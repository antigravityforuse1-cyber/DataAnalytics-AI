import React, { useState, useEffect, useRef } from 'react';
import useAppStore from '../store/appStore';
import { askQuestion } from '../utils/api';
import ChartDisplay from './ChartDisplay';

export default function ChatWindow() {
    const { sessionId, chatHistory, addChatMessage } = useAppStore();
    const [query, setQuery] = useState('');
    const [loading, setLoading] = useState(false);
    const scrollRef = useRef(null);

    // Auto-scroll to bottom of chat
    useEffect(() => {
        if (scrollRef.current) {
            scrollRef.current.scrollTop = scrollRef.current.scrollHeight;
        }
    }, [chatHistory]);

    const handleSend = async () => {
        if (!query.trim() || !sessionId) return;
        
        const currentQuery = query.trim();
        setQuery('');
        
        // Add user message to UI
        addChatMessage({ role: 'user', content: currentQuery });
        setLoading(true);

        try {
            const resp = await askQuestion(sessionId, currentQuery);
            addChatMessage({ 
                role: 'assistant', 
                content: resp.reply, 
                visualizations: resp.visualizations,
                data: resp.data
            });
        } catch (error) {
            addChatMessage({ role: 'assistant', content: 'An error occurred while processing your request.' });
        } finally {
            setLoading(false);
        }
    };

    if (!sessionId) {
        return <div className="p-8 text-gray-500 text-center">No active session. Please upload a dataset first.</div>;
    }

    return (
        <div className="flex flex-col h-full">
            <div className="flex-1 overflow-y-auto p-4 flex flex-col gap-4" ref={scrollRef}>
                {chatHistory.map((msg, idx) => (
                    <div key={idx} className={`p-4 rounded-lg max-w-[80%] ${msg.role === 'user' ? 'bg-blue-100 self-end ml-auto' : 'bg-gray-100 self-start'}`}>
                        <div className="font-semibold mb-1 text-sm text-gray-700">{msg.role === 'user' ? 'You' : 'Assistant'}</div>
                        <div className="whitespace-pre-wrap">{msg.content}</div>
                        
                        {/* Render charts if requested */}
                        {msg.visualizations && msg.visualizations.length > 0 && (
                            <div className="mt-4 w-full h-64 bg-white p-2 border rounded">
                                {msg.visualizations.map((viz, vIdx) => (
                                    <ChartDisplay key={vIdx} spec={viz} />
                                ))}
                            </div>
                        )}
                        
                        {/* Render simple data previews if available */}
                        {msg.data && (
                            <pre className="mt-4 p-2 bg-gray-800 text-green-400 text-xs rounded overflow-x-auto">
                                {JSON.stringify(msg.data, null, 2)}
                            </pre>
                        )}
                    </div>
                ))}
                {loading && (
                    <div className="p-4 bg-gray-100 self-start text-xs rounded animate-pulse text-gray-500">Assistant is thinking...</div>
                )}
            </div>

            <div className="p-4 bg-gray-50 border-t flex gap-2">
                <input 
                    type="text" 
                    value={query}
                    onChange={(e) => setQuery(e.target.value)}
                    onKeyDown={(e) => e.key === 'Enter' && handleSend()}
                    placeholder="Ask about your data..."
                    className="flex-1 p-2 border rounded shadow-inner"
                    disabled={loading}
                />
                <button 
                    onClick={handleSend}
                    disabled={loading || !query.trim()}
                    className="px-6 py-2 bg-blue-600 text-white font-semibold rounded hover:bg-blue-700 disabled:opacity-50"
                >
                    Send
                </button>
            </div>
        </div>
    );
}
