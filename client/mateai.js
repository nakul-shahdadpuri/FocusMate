import React, { useState } from 'react';
import { Card, CardContent } from '@/components/ui/card';
import { Button } from '@/components/ui/button';
import { Input } from '@/components/ui/input';
import { FiPaperclip, FiSend, FiMoon, FiSun, FiFolderPlus, FiFolder } from 'react-icons/fi';

const ChatApp = () => {
    const [messages, setMessages] = useState([]);
    const [newMessage, setNewMessage] = useState('');
    const [darkMode, setDarkMode] = useState(false);
    const [background, setBackground] = useState('https://source.unsplash.com/featured/?nature');
    const [directories, setDirectories] = useState([]);
    const [newDirectory, setNewDirectory] = useState('');

    const handleSendMessage = () => {
        if (newMessage.trim()) {
            setMessages([...messages, { text: newMessage, sender: 'You', timestamp: new Date().toLocaleTimeString() }]);
            setNewMessage('');
        }
    };

    const toggleDarkMode = () => {
        setDarkMode(!darkMode);
    };

    const addDirectory = () => {
        if (newDirectory.trim()) {
            setDirectories([...directories, newDirectory]);
            setNewDirectory('');
        }
    };

    return (
        <div className={`w-full h-screen p-4 flex flex-col ${darkMode ? 'bg-gray-900 text-white' : 'bg-gray-100 text-black'}`} style={{ backgroundImage: `url(${background})`, backgroundSize: 'cover' }}>
            <div className="flex justify-between items-center mb-2">
                <h2 className="text-2xl font-bold">MateAI</h2>
                <Button onClick={toggleDarkMode} className="rounded-full bg-blue-500 text-white p-2">
                    {darkMode ? <FiSun size={20} /> : <FiMoon size={20} />}
                </Button>
            </div>
            <div className="flex gap-4">
                <div className={`w-64 bg-gray-200 ${darkMode ? 'bg-gray-800' : 'bg-gray-300'} h-full p-4 rounded-lg shadow-md flex flex-col`}>
                    <div className="flex justify-between items-center mb-3">
                        <p className="text-sm font-semibold">Source Material</p>
                        <FiPaperclip size={18} className="text-gray-600" />
                    </div>
                    <div className="mb-4">
                        <label className="block text-xs font-medium mb-1">New Folder Name</label>
                        <div className="flex items-center gap-2">
                            <Input
                                type="text"
                                placeholder="e.g. Research Docs"
                                value={newDirectory}
                                onChange={(e) => setNewDirectory(e.target.value)}
                                className="flex-1 p-2 rounded border border-gray-300 focus:outline-none text-black"
                            />
                            <Button onClick={addDirectory} className="bg-blue-500 text-white p-2 rounded-full">
                                <FiFolderPlus size={16} />
                            </Button>
                        </div>
                    </div>
                    <div className="overflow-y-auto">
                        {directories.map((dir, index) => (
                            <div key={index} className="flex items-center gap-2 p-2 bg-gray-600 text-white rounded mb-1">
                                <FiFolder size={18} />
                                <span className="truncate">{dir}</span>
                            </div>
                        ))}
                    </div>
                </div>
                <Card className={`flex-1 mb-4 overflow-y-auto ${darkMode ? 'bg-gray-800 text-white' : 'bg-white text-black'} bg-opacity-70 rounded-2xl shadow-md`}>
                    <CardContent className="p-4">
                        {messages.map((message, index) => (
                            <div key={index} className={`mb-2 p-2 rounded-xl ${message.sender === 'You' ? (darkMode ? 'bg-blue-600 self-end text-white' : 'bg-green-300 self-end') : (darkMode ? 'bg-gray-700 self-start text-white' : 'bg-gray-200 self-start')} max-w-xs`}>
                                <p className="text-sm font-medium">{message.sender}</p>
                                <p className="text-base">{message.text}</p>
                                <p className="text-xs text-gray-500">{message.timestamp}</p>
                            </div>
                        ))}
                    </CardContent>
                </Card>
            </div>
            <div className="flex gap-2 items-center">
                <Input
                    type="text"
                    placeholder="Type a message..."
                    value={newMessage}
                    onChange={(e) => setNewMessage(e.target.value)}
                    className="flex-1 p-2 rounded-full border border-gray-300 focus:outline-none text-black"
                />
                <Button onClick={handleSendMessage} className="rounded-full bg-green-500 text-white p-2 flex items-center justify-center">
                    <FiSend size={20} />
                </Button>
            </div>
        </div>
    );
};

export default ChatApp;
