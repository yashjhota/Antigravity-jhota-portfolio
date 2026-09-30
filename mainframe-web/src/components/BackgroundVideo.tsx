import React, { useEffect, useRef } from 'react';

export const BackgroundVideo: React.FC = () => {
  const videoRef = useRef<HTMLVideoElement>(null);
  const targetTimeRef = useRef<number>(0);
  const isSeekingRef = useRef<boolean>(false);

  useEffect(() => {
    const handleMouseMove = (e: MouseEvent) => {
      const video = videoRef.current;
      if (!video) return;

      // Calculate time based on horizontal mouse position
      // Sensitivity: 0.8
      const sensitivity = 0.8;
      const progress = e.clientX / window.innerWidth;

      // Since the prompt asks for "delta = currentX - prevX", let's implement the delta approach
      // But for a hero page, a percentage-based scrub is usually smoother.
      // Let's follow the prompt's delta logic:
    };

    // Updated handleMouseMove based on precise prompt requirements
    let prevX = window.innerWidth / 2;
    const onMouseMove = (e: MouseEvent) => {
      const video = videoRef.current;
      if (!video || video.duration === 0) return;

      const currentX = e.clientX;
      const delta = currentX - prevX;
      prevX = currentX;

      const sensitivity = 0.8;
      const timeOffset = (delta / window.innerWidth) * sensitivity * video.duration;

      targetTimeRef.current = Math.max(0, Math.min(video.duration, video.currentTime + timeOffset));

      if (!isSeekingRef.current) {
        seekVideo();
      }
    };

    const seekVideo = async () => {
      const video = videoRef.current;
      if (!video) return;

      isSeekingRef.current = true;
      video.currentTime = targetTimeRef.current;
    };

    window.addEventListener('mousemove', onMouseMove);
    return () => window.removeEventListener('mousemove', onMouseMove);
  }, []);

  const onSeeked = () => {
    isSeekingRef.current = false;
    const video = videoRef.current;
    if (video && Math.abs(video.currentTime - targetTimeRef.current) > 0.1) {
      video.currentTime = targetTimeRef.current;
    }
  };

  return (
    <video
      ref={videoRef}
      onSeeked={onSeeked}
      muted
      playsInline
      preload="auto"
      className="fixed inset-0 z-0 w-full h-full object-cover object-[70%_center]"
      src="https://d8j0ntlcm91z4.cloudfront.net/user_38xzZboKViGWJOttwIXH07lWA1P/hf_20260826_041744_63efcd78-bf7d-4039-99e2-2461e8a61903.mp4"
    />
  );
};
