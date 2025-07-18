import cohere

co = cohere.Client("1YacVfW8ggBW2aLK7nS64JLc0CUchc6Da4TW0Qy4")  

def generate_argument(topic, participant_name, stance):
    prompt = f"""You are participating in a formal debate.
Topic: {topic}
Your name: {participant_name}
Your stance: {stance}

Write a strong and persuasive argument from {participant_name}'s perspective in favor of their stance.
Be respectful, logical, and avoid repetition. Limit to 100 words.
"""
    try:
        response = co.generate(
            model="command",
            prompt=prompt,
            max_tokens=150,
            temperature=0.7
        )
        return response.generations[0].text.strip()
    except Exception as e:
        return f"Error generating argument for {participant_name}: {str(e)}"

def generate_debate(topic, participants):
    debate_results = []
    for i, name in enumerate(participants):
        stance = "in favor" if i % 2 == 0 else "against"
        argument = generate_argument(topic, name, stance)
        debate_results.append((name, stance, argument))
    return debate_results