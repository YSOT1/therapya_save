
import { useState } from "react";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Card } from "@/components/ui/card";
import { useToast } from "@/components/ui/use-toast";

const BetaSignup = () => {
  const [email, setEmail] = useState("");
  const { toast } = useToast();

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    toast({
      title: "Thanks for signing up!",
      description: "We'll notify you when early access is available.",
    });
    setEmail("");
  };

  return (
    <section className="py-20 px-6 bg-purple-50">
      <Card className="max-w-xl mx-auto p-8 border-none shadow-lg">
        <h2 className="text-3xl font-bold mb-4 text-center">Join Our Beta Program</h2>
        <p className="text-gray-600 mb-8 text-center">
          Be among the first to try our AI-powered speech therapy assistant
        </p>
        <form onSubmit={handleSubmit} className="flex flex-col sm:flex-row gap-4">
          <Input
            type="email"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            placeholder="Enter your email"
            className="flex-grow"
            required
          />
          <Button type="submit" className="bg-purple-600 hover:bg-purple-700 whitespace-nowrap">
            Join Beta
          </Button>
        </form>
      </Card>
    </section>
  );
};

export default BetaSignup;

