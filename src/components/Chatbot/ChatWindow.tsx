import React, { useState, useEffect, useRef } from 'react';
import clsx from 'clsx';
import styles from './styles.module.css'; // Assuming common styles

interface Message {
  id: string;
  sender: 'user' | 'chatbot';
  content: string;
  timestamp: string;
}

interface ChatWindowProps {
  sessionId: string;
  // Other props like userId, chapterId can be passed or derived
}

const ChatWindow: React.FC<ChatWindowProps> = ({ sessionId }) => {
  const [messages, setMessages] = useState<Message[]>([]);
  const [inputMessage, setInputMessage] = useState('');
  const messagesEndRef = useRef<HTMLDivElement>(null);

  // Simulate fetching initial messages for the session
  useEffect(() => {
    // In a real app, this would fetch messages from the backend
    setMessages([
      { id: '1', sender: 'chatbot', content: 'Hello! How can I help you with the book today?', timestamp: new Date().toISOString() },
    ]);
  }, [sessionId]);

  useEffect(() => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  }, [messages]);

  const handleSendMessage = async () => {
    if (inputMessage.trim() === '') return;

    const newMessage: Message = {
      id: String(messages.length + 1),
      sender: 'user',
      content: inputMessage,
      timestamp: new Date().toISOString(),
    };

    setMessages((prevMessages) => [...prevMessages, newMessage]);
    setInputMessage('');

    // Simulate sending message to backend and getting a response
    // This will be replaced by actual API calls in later tasks
    setTimeout(() => {
      const botResponse: Message = {
        id: String(messages.length + 2),
        sender: 'chatbot',
        content: `You asked: "${newMessage.content}". I'm still learning how to answer!`,
        timestamp: new Date().toISOString(),
      };
      setMessages((prevMessages) => [...prevMessages, botResponse]);
    }, 1000);
  };

  return (
    <div className={clsx(styles.chatWindow, 'card')}>
      <div className={clsx('card__header', styles.chatHeader)}>
        <h4>Chat Session: {sessionId.substring(0, 8)}...</h4>
      </div>
      <div className={clsx('card__body', styles.chatBody)}>
        <div className={styles.messagesContainer}>
          {messages.map((msg) => (
            <div key={msg.id} className={clsx(styles.message, styles[msg.sender])}>
              <div className={styles.messageContent}>{msg.content}</div>
              <div className={styles.messageTimestamp}>
                {new Date(msg.timestamp).toLocaleTimeString()}
              </div>
            </div>
          ))}
          <div ref={messagesEndRef} />
        </div>
      </div>
      <div className={clsx('card__footer', styles.chatInputContainer)}>
        <input
          type="text"
          className={clsx('input', styles.chatInput)}
          placeholder="Ask me anything about the book..."
          value={inputMessage}
          onChange={(e) => setInputMessage(e.target.value)}
          onKeyPress={(e) => {
            if (e.key === 'Enter') {
              handleSendMessage();
            }
          }}
        />
        <button className="button button--primary" onClick={handleSendMessage}>
          Send
        </button>
      </div>
    </div>
  );
};

export default ChatWindow;