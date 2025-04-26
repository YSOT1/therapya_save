
import { useState } from "react";
import { Button } from "@/components/ui/button";
import { Card } from "@/components/ui/card";
import { useToast } from "@/hooks/use-toast";
import { Mic } from "lucide-react";

const RecordingSection = () => {
  const [isRecording, setIsRecording] = useState(false);
  const [feedback, setFeedback] = useState("");
  const { toast } = useToast();
  const targetPhrase = "The quick brown fox jumps over the lazy dog"; // This will be dynamic later

  const startRecording = () => {
    setIsRecording(true);
    toast({
      title: "Recording started",
      description: "Please pronounce the phrase shown above",
    });
    // Recording logic will be implemented later
  };

  const stopRecording = () => {
    setIsRecording(false);
    setFeedback(
      "Pronunciation Analysis:\n" +
      "- Word Accuracy: 85%\n" +
      "- Areas to improve:\n" +
      "  • 'quick' - try emphasizing the 'k' sound\n" +
      "  • 'jumps' - elongate the 'm' sound\n" +
      "- Overall clarity: Good"
    );
    // Feedback logic will be implemented later
  };

  return (
    <section className="py-20 px-6 max-w-4xl mx-auto" aria-label="Speech Practice Area">
      <Card className="p-8 bg-white shadow-xl rounded-2xl">
        <h2 className="text-2xl font-bold text-center mb-8">
          Practice Your Pronunciation
        </h2>
        
        <div className="flex flex-col items-center gap-6">
          <div className="text-center space-y-4">
            <p className="text-gray-600 mb-2">Please pronounce this phrase:</p>
            <div className="p-4 bg-purple-50 rounded-lg">
              <p className="text-lg font-medium text-purple-900">{targetPhrase}</p>
            </div>
          </div>
          
          <Button
            onClick={isRecording ? stopRecording : startRecording}
            aria-label={isRecording ? "Stop Recording" : "Start Recording"}
            className={`w-32 h-32 rounded-full transition-all duration-300 ${
              isRecording
                ? "bg-red-500 hover:bg-red-600 animate-pulse"
                : "bg-purple-600 hover:bg-purple-700"
            }`}
          >
            <Mic className="w-8 h-8" />
          </Button>
          
          {feedback && (
            <div className="mt-8 p-6 bg-purple-50 rounded-lg w-full text-gray-800 animate-fade-in">
              <pre className="whitespace-pre-wrap font-sans">{feedback}</pre>
            </div>
          )}
        </div>
      </Card>
    </section>
  );
};

export default RecordingSection;

