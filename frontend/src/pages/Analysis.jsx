import React from 'react';
import ChatWindow from '../components/ChatWindow';

export default function Analysis() {
    return (
        <div className="h-[80vh] flex flex-col bg-white rounded shadow border relative">
            <div className="p-4 border-b">
                <h2 className="text-xl font-semibold">Conversational Analysis</h2>
                <p className="text-sm text-gray-500">Ask questions, filter data, or request charts.</p>
            </div>
            <div className="flex-1 overflow-hidden">
                <ChatWindow />
            </div>
        </div>
    );
}
