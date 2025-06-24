import cohere


co = cohere.Client("API KEY") #add you own key

def generate_argument(topic, participant_name, stance):
    prompt = f"""You are participating in a formal debate.
Topic: {topic}
Your name: {participant_name}
Your stance: {stance}


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
