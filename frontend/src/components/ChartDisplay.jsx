import React from 'react';
import { LineChart, Line, BarChart, Bar, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer } from 'recharts';

export default function ChartDisplay({ spec }) {
    if (!spec || !spec.data || spec.data.length === 0 || spec.type === "none") {
        return <div className="text-gray-500 italic">No chart data available</div>;
    }

    if (spec.type === "bar") {
        return (
            <ResponsiveContainer width="100%" height="100%">
                <BarChart data={spec.data}>
                    <CartesianGrid strokeDasharray="3 3" />
                    <XAxis dataKey={spec.xAxis} />
                    <YAxis />
                    <Tooltip />
                    <Legend />
                    <Bar dataKey={spec.yAxis} fill="#8884d8" />
                </BarChart>
            </ResponsiveContainer>
        );
    }
    
    if (spec.type === "line") {
        return (
            <ResponsiveContainer width="100%" height="100%">
                <LineChart data={spec.data}>
                    <CartesianGrid strokeDasharray="3 3" />
                    <XAxis dataKey={spec.xAxis} />
                    <YAxis />
                    <Tooltip />
                    <Legend />
                    <Line type="monotone" dataKey={spec.yAxis} stroke="#82ca9d" />
                </LineChart>
            </ResponsiveContainer>
        );
    }

    return <div>Chart type {spec.type} not supported yet.</div>;
}
