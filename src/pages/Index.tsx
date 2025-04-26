
import { useRef } from "react";
import Hero from "@/components/Hero";
import RecordingSection from "@/components/RecordingSection";
import BetaSignup from "@/components/BetaSignup";
import Footer from "@/components/Footer";
import DemoSection from "@/components/DemoSection";
import Navbar from "@/components/Navbar";

const Index = () => {
  const recordingSectionRef = useRef<HTMLDivElement>(null);

  const scrollToRecording = () => {
    recordingSectionRef.current?.scrollIntoView({ behavior: "smooth" });
  };

  return (
    <div className="min-h-screen bg-gradient-to-b from-purple-50 to-white">
      <Navbar />
      <section id="home" className="h-screen">
        <Hero onTryNowClick={scrollToRecording} />
      </section>
      <section ref={recordingSectionRef} id="recording" className="h-screen">
        <RecordingSection />
      </section>
      <section id="demo" className="h-screen">
        <DemoSection />
      </section>
      <section id="beta" className="h-screen">
        <BetaSignup />
      </section>
      <section className="min-h-screen">
        <Footer />
      </section>
    </div>
  );
};

export default Index;
