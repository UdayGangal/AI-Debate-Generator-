import os
from openai import OpenAI

# Initialize OpenAI Client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))  # or replace with your actual key (not recommended for prod)

def generate_argument(topic, participant_name, stance):
    """
    Generate a persuasive argument for a given topic, participant, and stance.
    """
    prompt = f"""You are participating in a formal debate.
Topic: {topic}
Your name: {participant_name}
Your stance: {stance}

Write a strong and persuasive argument from {participant_name}'s perspective in favor of their stance.
Be respectful, logical, and avoid repetition. Limit to 100 words.
"""
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=200,
            temperature=0.7,
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Error generating argument for {participant_name}: {str(e)}"

def generate_debate(topic, participants):
    """
    Generate a debate by alternating participant stances.
    """
    results = []
    for i, name in enumerate(participants):
        stance = "in favor" if i % 2 == 0 else "against"
        argument = generate_argument(topic, name, stance)
        results.append({
            "name": name,
            "stance": stance,
            "argument": argument
        })
    return results

# Example usage:
if __name__ == "__main__":
    topic = "Should AI be used in education?"
    participants = ["Alice", "Bob", "Charlie"]
    debate = generate_debate(topic, participants)

    for entry in debate:
        print(f"\n{entry['name']} ({entry['stance']}):\n{entry['argument']}")
