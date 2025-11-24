import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types

def main():
    try:
        prompt = sys.argv[1]
    except IndexError:
        print('input must include prompt')
        exit(1)
    
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    model_name = 'gemini-2.0-flash-001'

    client = genai.Client(api_key=api_key)
    
    messages = [
        types.Content(role="user", parts=[types.Part(text=prompt)])
    ]

    response = client.models.generate_content(model=model_name, contents=messages)

    output = response.text
    prompt_tokens = response.usage_metadata.prompt_token_count
    response_tokens = response.usage_metadata.candidates_token_count

    print(output)
    
    if '--verbose' in sys.argv[2:]:
        print(f'User prompt: {prompt}')
        print(f'Prompt tokens: {prompt_tokens}')
        print(f'Response tokens: {response_tokens}')
    
if __name__ == '__main__':
    main()