import React, { useState } from 'react';

export const Navbar: React.FC = () => {
  const [isOpen, setIsOpen] = useState(false);

  const navLinks = ["Labs", "Studio", "Openings", "Shop"];

  return (
    <nav className="fixed top-0 left-0 w-full z-10 px-5 sm:px-8 py-4 sm:py-5 flex justify-between items-center">
      {/* Logo */}
      <div className="flex items-center gap-3 select-none cursor-pointer">
        <span className="text-[21px] sm:text-[26px] tracking-tight text-white font-heading">
          Mainframe®
        </span>
        <span className="text-[25px] sm:text-[30px] text-white select-none" style={{ letterSpacing: '-0.02em' }}>
          ✳︎
        </span>
      </div>

      {/* Desktop Nav */}
      <div className="hidden md:flex items-center gap-6 text-[23px] text-white">
        <div className="flex gap-2">
          {navLinks.map((link, index) => (
            <React.Fragment key={link}>
              <a href={`#${link.toLowerCase()}`} className="hover:opacity-60 transition-opacity">
                {link}
              </a>
              {index < navLinks.length - 1 && <span className="text-white">, </span>}
            </React.Fragment>
          ))}
        </div>
        <a href="https://yash-portfolio.streamlit.app/" target="_blank" className="underline underline-offset-2 hover:opacity-60 transition-opacity">
          Get in touch
        </a>
      </div>

      {/* Mobile Hamburger */}
      <button
        className="md:hidden flex flex-col justify-center items-center gap-[5px] w-10 h-10 z-20 relative"
        onClick={() => setIsOpen(!isOpen)}
      >
        <div className={`w-6 h-[2px] bg-white transition-all duration-300 ${isOpen ? 'rotate-45 translate-y-[7px]' : ''}`} />
        <div className={`w-6 h-[2px] bg-white transition-all duration-300 ${isOpen ? 'opacity-0' : ''}`} />
        <div className={`w-6 h-[2px] bg-white transition-all duration-300 ${isOpen ? '-rotate-45 -translate-y-[7px]' : ''}`} />
      </button>

      {/* Mobile Overlay */}
      <div className={`fixed inset-0 bg-black/90 backdrop-blur-md z-10 flex flex-col justify-center px-8 gap-8 transition-all duration-300 md:hidden ${isOpen ? 'opacity-100 pointer-events-auto' : 'opacity-0 pointer-events-none'}`}>
        {navLinks.map((link) => (
          <a
            key={link}
            href={`#${link.toLowerCase()}`}
            className="text-[32px] font-medium text-white"
            onClick={() => setIsOpen(false)}
          >
            {link}
          </a>
        ))}
        <a
          href="https://yash-portfolio.streamlit.app/"
          target="_blank"
          className="text-[32px] font-medium text-white underline underline-offset-2"
          onClick={() => setIsOpen(false)}
        >
          Get in touch
        </a>
      </div>
    </nav>
  );
};
