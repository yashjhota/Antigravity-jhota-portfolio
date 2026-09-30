import React from 'react';
import { BackgroundVideo } from './components/BackgroundVideo';
import { Navbar } from './components/Navbar';
import { Hero } from './components/Hero';

function App() {
  return (
    <div className="relative min-h-screen w-full overflow-hidden bg-black text-white">
      <BackgroundVideo />
      <Navbar />
      <Hero />
    </div>
  );
}

export default App;
