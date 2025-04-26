
import { Card } from "@/components/ui/card";

const DemoSection = () => {
  return (
    <section className="flex items-center justify-center h-full px-6">
      <Card className="p-8 bg-white shadow-xl rounded-2xl max-w-4xl w-full">
        <h2 className="text-3xl font-bold text-center mb-8">
          See How It Works
        </h2>
        <div className="space-y-6">
          <div className="bg-purple-50 p-6 rounded-lg">
            <h3 className="text-xl font-semibold mb-4">Record your voice, and get instant feedback!</h3>
            <p className="text-gray-600">
              Our AI-powered speech recognition system will analyze your pronunciation
              and provide detailed feedback to help you improve.
            </p>
          </div>
          
          <div className="grid md:grid-cols-2 gap-6">
            <div className="bg-purple-50 p-6 rounded-lg">
              <h4 className="font-semibold mb-2">1. Record Your Voice</h4>
              <p className="text-gray-600">Speak the provided phrase into your microphone</p>
            </div>
            <div className="bg-purple-50 p-6 rounded-lg">
              <h4 className="font-semibold mb-2">2. Get Instant Feedback</h4>
              <p className="text-gray-600">Receive detailed analysis of your pronunciation</p>
            </div>
          </div>
        </div>
      </Card>
    </section>
  );
};

export default DemoSection;
