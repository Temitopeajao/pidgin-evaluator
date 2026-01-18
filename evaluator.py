import os
import json
from openai import OpenAI

# PROJECT: Low-Resource Language Alignment Evaluator
# AUTHOR: Temitope Ajao
# PURPOSE: To automate the grading of English -> Nigerian Pidgin translations
# using LLM-as-a-Judge methodology.

class PidginEvaluator:
    def __init__(self, api_key):
        """
        Initialize with API key for the Judge Model.
        """
        self.client = OpenAI(api_key=api_key)

    def generate_translation(self, english_text):
        """
        Simulates the target model we are training (e.g., Llama-3 Fine-tuned).
        In a real production pipeline, this would call your specific model endpoint.
        """
        response = self.client.chat.completions.create(
            model="gpt-4o-mini", # Simulating the base student model
            messages=[
                {"role": "system", "content": "You are a fluent speaker of Nigerian Pidgin. Translate the user's input accurately, maintaining local Lagos context."},
                {"role": "user", "content": english_text}
            ]
        )
        return response.choices[0].message.content

    def evaluate_quality(self, original, translation):
        """
        The 'Critic' Model that scores the output based on grammar and tone.
        This automates the RLHF (Reinforcement Learning from Human Feedback) loop.
        """
        rubric = """
        Score 1-5 based on:
        1. Lexical Accuracy (Is it real Pidgin or just broken English?)
        2. Tone (Does it sound natural to a Lagos local?)
        3. Grammar (Correct syntax for Pidgin).
        """
        
        # We use a Chain-of-Thought prompt to get the reasoning before the score
        prompt = f"""
        Act as a linguistic expert in West African languages. Evaluate this translation:
        
        Original (English): "{original}"
        Candidate (Pidgin): "{translation}"
        
        {rubric}
        
        Return JSON format: {{ "score": int, "reasoning": "string" }}
        """

        evaluation = self.client.chat.completions.create(
            model="gpt-4o", # The stronger 'Judge' model (GPT-4)
            messages=[{"role": "user", "content": prompt}],
            response_format={"type": "json_object"}
        )
        return json.loads(evaluation.choices[0].message.content)

# --- EXECUTION ---
if __name__ == "__main__":
    # Test Case: A phrase that requires cultural context, not just literal translation
    input_text = "I was very surprised by what happened yesterday."
    
    # 1. Setup - Ensure you have your key exported in your terminal
    # Command: export OPENAI_API_KEY="sk-..."
    api_key = os.getenv("OPENAI_API_KEY")
    
    if not api_key:
        print("❌ Error: OPENAI_API_KEY not found. Please set it in your environment.")
    else:
        bot = PidginEvaluator(api_key=api_key)
        
        print(f"--- INPUT ---\n{input_text}\n")
        
        # 2. Generate Translation
        pidgin_output = bot.generate_translation(input_text)
        print(f"--- MODEL OUTPUT ---\n{pidgin_output}\n")
        
        # 3. Evaluate Quality
        score_data = bot.evaluate_quality(input_text, pidgin_output)
        print(f"--- AI JUDGE VERDICT ---\nScore: {score_data['score']}/5\nReasoning: {score_data['reasoning']}")
