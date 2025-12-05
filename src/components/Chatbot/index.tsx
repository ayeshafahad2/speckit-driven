import React from 'react';
import clsx from 'clsx';
import styles from './styles.module.css';

export default function Chatbot(): JSX.Element {
  return (
    <div className={clsx('card', styles.chatbotContainer)}>
      <div className="card__header">
        <h3>RAG Chatbot</h3>
      </div>
      <div className="card__body">
        <p>This is where the RAG chatbot interface will be integrated.</p>
        <p>Further development will include chat history, input field, and interaction logic.</p>
      </div>
      <div className="card__footer">
        <button className="button button--primary">Start Chat</button>
      </div>
    </div>
  );
}