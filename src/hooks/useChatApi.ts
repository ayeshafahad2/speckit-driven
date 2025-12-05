import { useState, useCallback } from 'react';

const BACKEND_API_URL = process.env.REACT_APP_BACKEND_API_URL || 'http://localhost:8000';

interface ChatSession {
  session_id: string;
  user_id?: string;
  start_time: string;
  end_time?: string;
  is_active: boolean;
  current_context_chapter_id?: string;
}

interface ChatMessage {
  message_id: string;
  session_id: string;
  sender_type: 'user' | 'chatbot' | 'agent';
  content: string;
  timestamp: string;
  context_selected_text?: string;
  retrieved_sources?: any[];
}

interface CreateChatSessionRequest {
  initial_message?: string;
  chapter_id?: string;
}

export function useChatApi() {
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const callApi = useCallback(async <T>(
    endpoint: string,
    method: string = 'GET',
    body?: any,
    headers: Record<string, string> = {}
  ): Promise<T | null> => {
    setLoading(true);
    setError(null);
    try {
      const response = await fetch(`${BACKEND_API_URL}${endpoint}`, {
        method,
        headers: {
          'Content-Type': 'application/json',
          ...headers,
        },
        body: body ? JSON.stringify(body) : undefined,
      });

      if (!response.ok) {
        const errorData = await response.json();
        throw new Error(errorData.detail || 'API call failed');
      }

      return await response.json();
    } catch (err: any) {
      setError(err.message);
      return null;
    } finally {
      setLoading(false);
    }
  }, []);

  const createSession = useCallback(async (
    requestBody?: CreateChatSessionRequest,
    token?: string
  ): Promise<ChatSession | null> => {
    const headers: Record<string, string> = {};
    if (token) headers['Authorization'] = `Bearer ${token}`;
    return callApi<ChatSession>('/chat/session', 'POST', requestBody, headers);
  }, [callApi]);

  const getSession = useCallback(async (
    sessionId: string,
    token?: string
  ): Promise<ChatSession | null> => {
    const headers: Record<string, string> = {};
    if (token) headers['Authorization'] = `Bearer ${token}`;
    return callApi<ChatSession>(`/chat/session/${sessionId}`, 'GET', undefined, headers);
  }, [callApi]);

  const endSession = useCallback(async (
    sessionId: string,
    token?: string
  ): Promise<ChatSession | null> => {
    const headers: Record<string, string> = {};
    if (token) headers['Authorization'] = `Bearer ${token}`;
    return callApi<ChatSession>(`/chat/session/${sessionId}/end`, 'POST', undefined, headers);
  }, [callApi]);

  // Placeholder for sending messages, will be updated in US2
  const sendMessage = useCallback(async (
    sessionId: string,
    userMessage: string,
    selectedText?: string,
    token?: string
  ): Promise<{ chatbot_response: string, sources: any[] } | null> => {
    const headers: Record<string, string> = {};
    if (token) headers['Authorization'] = `Bearer ${token}`;
    const body = { user_message: userMessage, selected_text: selectedText };
    // Simulate API call
    console.log(`Simulating sending message to /chat/session/${sessionId}/message:`, body);
    return Promise.resolve({
      chatbot_response: `Simulated response to "${userMessage}"`,
      sources: []
    });
    // return callApi<{ chatbot_response: string, sources: any[] }>(`/chat/session/${sessionId}/message`, 'POST', body, headers);
  }, [callApi]);

  return { loading, error, createSession, getSession, endSession, sendMessage };
}
