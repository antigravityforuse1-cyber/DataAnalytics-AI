import React from 'react';
import { HashRouter, Routes, Route, Navigate } from 'react-router-dom';
import Upload from './pages/Upload';
import Dashboard from './pages/Dashboard';
import Analysis from './pages/Analysis';
import NotFound from './pages/NotFound';
import Header from './components/Header';

function App() {
  return (
    <HashRouter>
      <div className="min-h-screen bg-gray-50 flex flex-col">
        <Header />
        <main className="flex-1 p-4 w-full max-w-7xl mx-auto">
          <Routes>
            <Route path="/" element={<Navigate to="/upload" />} />
            <Route path="/upload" element={<Upload />} />
            <Route path="/dashboard" element={<Dashboard />} />
            <Route path="/analysis" element={<Analysis />} />
            <Route path="*" element={<NotFound />} />
          </Routes>
        </main>
      </div>
    </HashRouter>
  );
}

export default App;
