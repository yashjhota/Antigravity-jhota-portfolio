import React, { useState, useEffect } from 'react';
import { useTypewriter } from '../hooks/useTypewriter';

export const Hero: React.FC = () => {
  const [visible, setVisible] = useState(false);
  const text = "Glad you stopped in. Good taste tends to find us. Now, what are we building?";
  const { displayed, done } = useTypewriter(text);

  useEffect(() => {
    const timer = setTimeout(() => setVisible(true), 400);
    return () => clearTimeout(timer);
  }, []);

  const copyEmail = async () => {
    try {
      await navigator.clipboard.writeText('hello@mainframe.co');
      alert('Email copied to clipboard!');
    } catch (err) {
      console.error('Failed to copy!', err);
    }
  };

  return (
    <div className="relative z-10 h-screen flex flex-col justify-end pb-12 md:justify-center md:pb-0 px-5 sm:px-8 md:px-10 overflow-hidden">
      <div className="max-w-xl relative z-10">
        {/* Blurred Intro */}
        <div className="pointer-events-none select-none mb-5 sm:mb-6 text-white blur-[4px] font-normal leading-[1.3]"
             style={{ fontSize: 'clamp(18px, 4vw, 26px)' }}>
          Hey there, meet A.R.I.A,<br />
          Mainframe's Adaptive Response Interface Agent
        </div>

        {/* Typewriter Text */}
        <p className="text-white mb-5 sm:mb-6 font-normal leading-[1.35] min-h-[54px]"
           style={{ fontSize: 'clamp(18px, 4vw, 26px)' }}>
          {displayed}
          {!done && <span className="inline-block w-[2px] h-[1.1em] bg-white align-middle ml-[2px] animate-blink" />}
        </p>

        {/* Action Buttons */}
        <div className={`flex flex-wrap gap-y-1 transition-all duration-400 ease-out ${visible ? 'opacity-100 translate-y-0' : 'opacity-0 translate-y-2'}`}>
          <button className="inline-flex items-center justify-center bg-white text-black border border-black/10 rounded-full text-[13px] sm:text-[15px] px-4 sm:px-5 py-[0.3em] mx-[0.2em] mb-[0.4em] whitespace-nowrap hover:bg-black hover:text-white transition-colors duration-200">
            Pitch us an idea
          </button>
          <button className="inline-flex items-center justify-center bg-white text-black border border-black/10 rounded-full text-[13px] sm:text-[15px] px-4 sm:px-5 py-[0.3em] mx-[0.2em] mb-[0.4em] whitespace-nowrap hover:bg-black hover:text-white transition-colors duration-200">
            Come work here
          </button>
          <button className="inline-flex items-center justify-center bg-white text-black border border-black/10 rounded-full text-[13px] sm:text-[15px] px-4 sm:px-5 py-[0.3em] mx-[0.2em] mb-[0.4em] whitespace-nowrap hover:bg-black hover:text-white transition-colors duration-200">
            Send a brief hello
          </button>
          <button className="inline-flex items-center justify-center bg-white text-black border border-black/10 rounded-full text-[13px] sm:text-[15px] px-4 sm:px-5 py-[0.3em] mx-[0.2em] mb-[0.4em] whitespace-nowrap hover:bg-black hover:text-white transition-colors duration-200">
            See how we operate
          </button>
          <button
            onClick={copyEmail}
            className="inline-flex items-center justify-center text-white bg-transparent border border-white rounded-full text-[13px] sm:text-[15px] px-4 sm:px-5 py-[0.3em] mx-[0.2em] mb-[0.4em] whitespace-nowrap gap-2 sm:gap-3 hover:bg-white hover:text-black transition-colors duration-200"
          >
            <span>Reach us: <span className="underline underline-offset-1">hello@mainframe.co</span></span>
            <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
              <rect x="9" y="9" width="13" height="13" rx="2" ry="2"></rect>
              <path d="M5 15H4a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"></path>
            </svg>
          </button>
        </div>
      </div>
    </div>
  );
};
