import React, { useState, useEffect } from 'react';
import Layout from '@theme/Layout';
import ChatWindow from '../components/Chatbot/ChatWindow'; // Assuming ChatWindow is the main component
import { v4 as uuidv4 } from 'uuid'; // For generating a new session ID

export default function ChatbotPage(): JSX.Element {
  const [sessionId, setSessionId] = useState<string | null>(null);

  useEffect(() => {
    // In a real application, you'd make an API call to create a session
    // and get a real session ID. For now, simulate.
    const newSessionId = uuidv4();
    setSessionId(newSessionId);
    console.log(`Simulated new chat session created: ${newSessionId}`);
  }, []);

  if (!sessionId) {
    return (
      <Layout title="Chatbot">
        <main style={{ padding: '2rem', textAlign: 'center' }}>
          <h1>Loading Chatbot...</h1>
        </main>
      </Layout>
    );
  }

  return (
    <Layout title="Chatbot" description="Chat with the RAG chatbot about the book's content.">
      <main style={{ display: 'flex', justifyContent: 'center', alignItems: 'center', padding: '2rem' }}>
        <div style={{ width: '100%', maxWidth: '800px' }}>
          <ChatWindow sessionId={sessionId} />
        </div>
      </main>
    </Layout>
  );
}
