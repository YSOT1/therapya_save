// src/pages/TestPronunciation.tsx

import { useState, useRef } from "react";
import { Button } from "@/components/ui/button";
import { Card, CardContent } from "@/components/ui/card";
import { toast } from "@/components/ui/use-toast";

interface Feedback {
  correct: boolean;
  mistakes: Array<{
    letter: string;
    tip: string;
  }>;
}

const TEST_SENTENCE = "Ana kanheb lmaghrib"; // Example Darija sentence

export default function TestPronunciation() {
  const [isRecording, setIsRecording] = useState(false);
  const [audioBlob, setAudioBlob] = useState<Blob | null>(null);
  const [feedback, setFeedback] = useState<Feedback | null>(null);
  const [practiceLetter, setPracticeLetter] = useState<string | null>(null);

  const mediaRecorderRef = useRef<MediaRecorder | null>(null);

  const startRecording = async () => {
    const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
    const mediaRecorder = new MediaRecorder(stream);
    const chunks: BlobPart[] = [];

    mediaRecorder.ondataavailable = (e) => {
      chunks.push(e.data);
    };

    mediaRecorder.onstop = () => {
      const blob = new Blob(chunks, { type: "audio/webm" });
      setAudioBlob(blob);
    };

    mediaRecorder.start();
    mediaRecorderRef.current = mediaRecorder;
    setIsRecording(true);
  };

  const stopRecording = () => {
    mediaRecorderRef.current?.stop();
    setIsRecording(false);
  };

  const uploadAndAnalyze = async () => {
    if (!audioBlob) return;

    toast({ title: "Uploading audio..." });

    const formData = new FormData();
    formData.append("file", audioBlob, "recording.webm");
    formData.append("expected_sentence", TEST_SENTENCE); // This is already in Latin.

    try {
      const response = await fetch("http://localhost:8000/analyze", {
        method: "POST",
        body: formData,
      });

      const data = await response.json();

      if (data.error) throw new Error(data.error);

      setFeedback(data.feedback);
      toast({ title: "Analysis complete!" });
    } catch (err) {
      toast({ title: "Error analyzing recording", description: String(err) });
    }
  };

  const handlePractice = (letter: string) => {
    setPracticeLetter(letter);
  };

  const resetTest = () => {
    setFeedback(null);
    setPracticeLetter(null);
    setAudioBlob(null);
  };

  return (
    <div className="p-6 flex flex-col items-center gap-6">
      <h1 className="text-3xl font-bold">Pronunciation Test</h1>

      {!feedback && (
        <Card className="p-6">
          <CardContent className="flex flex-col gap-4 items-center">
            <p className="text-lg">Repeat this sentence:</p>
            <p className="font-semibold text-xl">"{TEST_SENTENCE}"</p>

            {!isRecording && (
              <Button onClick={startRecording}>Start Recording</Button>
            )}
            {isRecording && (
              <Button variant="destructive" onClick={stopRecording}>
                Stop Recording
              </Button>
            )}

            {audioBlob && (
              <Button onClick={uploadAndAnalyze}>Analyze Pronunciation</Button>
            )}
          </CardContent>
        </Card>
      )}

      {feedback && (
        <Card className="p-6">
          <CardContent className="flex flex-col gap-4">
            <h2 className="text-2xl font-bold">Feedback:</h2>

            {feedback.correct ? (
              <p className="text-green-600">Great job! Your pronunciation is perfect!</p>
            ) : (
              <div className="flex flex-col gap-3">
                <p className="text-red-500">Issues detected in letters:</p>
                <ul className="list-disc ml-5">
                  {feedback.mistakes.map((m, idx) => (
                    <li key={idx}>
                      <strong>{m.letter}:</strong> {m.tip}
                      <Button size="sm" className="ml-3" onClick={() => handlePractice(m.letter)}>
                        Practice {m.letter}
                      </Button>
                    </li>
                  ))}
                </ul>
              </div>
            )}

            <Button variant="outline" onClick={resetTest}>Test Again</Button>
          </CardContent>
        </Card>
      )}

      {practiceLetter && (
        <Card className="p-6">
          <CardContent className="flex flex-col gap-4">
            <h2 className="text-xl font-semibold">Practice letter: {practiceLetter}</h2>
            <video controls src={`https://hpgzcjqykpnajdknhlij.supabase.co/storage/v1/object/public/practice-videos//${practiceLetter}.mp4`} className="rounded-lg shadow-lg" />
            <p>After practicing, try recording again!</p>
          </CardContent>
        </Card>
      )}
    </div>
  );
}
