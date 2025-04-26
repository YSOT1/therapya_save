
import { Button } from "@/components/ui/button";
import { ArrowRight } from "lucide-react";

interface HeroProps {
  onTryNowClick: () => void;
}

const Hero = ({ onTryNowClick }: HeroProps) => {
  return (
    <section className="flex items-center justify-center h-full px-6 pt-16">
      <div className="max-w-6xl mx-auto text-center bg-white/50 backdrop-blur-sm rounded-2xl p-12">
        <h1 className="text-4xl md:text-6xl font-bold text-gray-900 mb-6 animate-fade-in">
          Therapya: Your Moroccan Dialect Speech Coach
        </h1>
        <p className="text-xl md:text-2xl text-gray-600 mb-8 max-w-2xl mx-auto animate-fade-in">
          Master pronunciation with AI feedback in seconds.
        </p>
        <div className="space-y-4 md:space-y-0 md:space-x-4 animate-fade-in">
          <Button
            onClick={onTryNowClick}
            size="lg"
            className="bg-purple-600 hover:bg-purple-700 text-white px-8 py-6 text-lg rounded-full shadow-lg hover:shadow-xl transition-all duration-300"
          >
            Try it Now <ArrowRight className="ml-2" />
          </Button>
        </div>
      </div>
    </section>
  );
};

export default Hero;
