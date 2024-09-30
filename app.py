# Getting answers on terminal 

from openai import OpenAI
import pyperclip
import time

# Set your OpenAI API key
api_key = "sk-ze3k1lRD1qZUqM_aqR4_BI_vcnwqsOsFfXvRewjsXRT3BlbkFJMVCtf1xRytzXHPRX_rlgs9pbqMNWfcBUtRhn363DUA"
client = OpenAI(api_key=api_key)
# Function to get answers from GPT-3.5-turbo
def get_answer(text):
    try:
        # Using 'gpt-3.5-turbo' instead of 'gpt-4'
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system",
                 "content": f"Provide atleast three points for given content:{text}"}
            ],
            max_tokens=150,
            temperature=0.7,
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error: {str(e)}"

def monitor_clipboard():
    recent_value = ""  # To store the last copied content
    print("Monitoring clipboard. Copy text to process it.")

    try:
        while True:
            # Get the current clipboard content
            clipboard_text = pyperclip.paste()

            # If clipboard content is not empty and it's new
            if clipboard_text and clipboard_text != recent_value:
                recent_value = clipboard_text  # Update the recent copied text
                print(f"New Text Detected: {recent_value}")

                # Get the answer from GPT-3.5-turbo
                answer = get_answer(recent_value)
                print(f"Answer: {answer}")

                # Copy the answer to the clipboard
                pyperclip.copy(answer)
                print("Answer copied to clipboard. You can paste it now!")

                # Wait for the clipboard to change before checking again
                while pyperclip.paste() == answer:
                    time.sleep(0.5)

            # Short sleep to reduce CPU usage
            time.sleep(0.1)

    except KeyboardInterrupt:
        print("\nClipboard monitoring stopped.")


if __name__ == "__main__":
    monitor_clipboard()