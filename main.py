import os
import requests
from dotenv import load_dotenv

# Load Together.ai API key from .env file
load_dotenv()
api_key = os.getenv("TOGETHER_API_KEY")

# Together.ai API details
API_URL = "https://api.together.xyz/inference"
HEADERS = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}
MODEL_NAME = "mistralai/Mixtral-8x7B-Instruct-v0.1"

# Function to call Together API
def query_together(prompt: str, max_tokens: int = 300) -> str:
    response = requests.post(API_URL, headers=HEADERS, json={
        "model": MODEL_NAME,
        "prompt": prompt,
        "max_tokens": max_tokens,
        "temperature": 0.7,
        "top_p": 0.9,
        "stop": ["</s>"]
    })

    response.raise_for_status()  # show clear error if something fails
    return response.json()['choices'][0]['text'].strip()

# === Chat loop ===
print("Welcome to the Negotiation Coaching Chatbot!")
print("You are the SELLER. The AI will play the BUYER.")
print("Type 'exit' to quit.\n")

# Initial message from the buyer
buyer_message = "Hi, I’m interested in your product, but I was hoping to get a better price."

while True:
    print(f" Buyer: {buyer_message}")
    seller_message = input("You (Seller): ")

    if seller_message.lower() == "exit":
        break

    # --- AI Buyer responds ---
    buyer_prompt = f"""
You are a buyer in a negotiation. Here’s what the seller just said:

Seller: "{seller_message}"
Your previous message was: "{buyer_message}"

Respond as a realistic buyer who is trying to get a good deal. Keep your message short and human-like.
"""
    buyer_message = query_together(buyer_prompt)

    # --- AI Coach gives feedback ---
    coach_prompt = f"""
You are a negotiation coach helping a seller improve their responses.

Context:
Buyer just said: "{buyer_message}"
Seller replied: "{seller_message}"

Give constructive feedback on the seller’s reply, considering the buyer’s message.

Respond with:
- Feedback: ...
- Why it works or doesn’t work: ...
- How to improve: ...
- Suggested next seller message: ...
"""
    coach_feedback = query_together(coach_prompt)

    # Show AI Buyer reply and Coach feedback
    print(f"\nBuyer: {buyer_message}")
    print(f"\nCoach Feedback:\n{coach_feedback}")
    print("-" * 100)

# CODE 3 :
# import os
# import requests
# from dotenv import load_dotenv

# # Load Together.ai API key
# load_dotenv()
# api_key = os.getenv("TOGETHER_API_KEY")

# # ===== SHARED CONFIGURATION =====

# MODEL_NAME = "mistralai/Mixtral-8x7B-Instruct-v0.1"
# API_URL = "https://api.together.xyz/inference"

# HEADERS = {
#     "Authorization": f"Bearer {api_key}",
#     "Content-Type": "application/json"
# }


# def send_to_model(prompt: str, max_tokens: int = 500) -> str:
#     response = requests.post(
#         API_URL,
#         headers=HEADERS,
#         json={
#             "model": MODEL_NAME,
#             "prompt": prompt,
#             "max_tokens": max_tokens,
#             "temperature": 0.7,
#             "top_p": 0.9,
#             "stop": ["</s>"]
#         }
#     )
#     result = response.json()
#     return result['choices'][0]['text'].strip()


# # ===== OPTION 1: FULL TRANSCRIPT FEEDBACK =====

# def full_transcript_feedback():
#     # Load transcript from file
#     try:
#         with open("transcripts/sample_transcript.txt", "r") as file:
#             transcript = file.read()
#     except FileNotFoundError:
#         print("❌ Could not find 'sample_transcript.txt'. Please make sure it's in the 'transcripts/' folder.")
#         return

#     prompt = f"""
# You are a professional negotiation coach. Read the full negotiation transcript below and give categorized feedback.

# Include:
# - Tactical feedback
# - Strategic feedback
# - Behavioral feedback
# - Outcome-based feedback
# - Suggestions to improve

# Negotiation Transcript:
# {transcript}
# """

#     feedback = send_to_model(prompt)
#     print("=== FEEDBACK REPORT ===")
#     print(feedback)


# # ===== OPTION 2: CHATBOT COACHING MODE =====

# def coaching_chatbot():
#     SYSTEM_PROMPT = """
# You are a negotiation coach helping a seller improve their negotiation messages.

# The seller wants the buyer to agree to their offer. After each seller message, give:
# - Feedback (what they did well or should improve)
# - A short explanation
# - A suggested next message that would improve the buyer's chance of accepting

# Format:
# Feedback: ...
# Why: ...
# Suggested next message: ...
# """

#     print("\n📢 Coaching Chatbot Mode (Type 'exit' to quit)\n")

#     while True:
#         seller_input = input("🧑‍💼 You (Seller): ")
#         if seller_input.lower() == "exit":
#             break

#         prompt = f"{SYSTEM_PROMPT}\n\nSeller's message: {seller_input}"
#         feedback = send_to_model(prompt, max_tokens=300)
#         print("🤖 Coach:\n", feedback)
#         print("-" * 50)


# # ===== MAIN MENU =====

# def main():
#     print("🧠 Welcome to the AI Negotiation Feedback Agent!")
#     print("Choose a mode:")
#     print("1. Full Transcript Feedback")
#     print("2. Real-Time Coaching Chatbot\n")

#     choice = input("Enter 1 or 2: ")

#     if choice == "1":
#         full_transcript_feedback()
#     elif choice == "2":
#         coaching_chatbot()
#     else:
#         print("❌ Invalid choice. Please run again and enter 1 or 2.")

# if __name__ == "__main__":
#     main()


# CODE 2 BELOW:
# import os
# import requests
# from dotenv import load_dotenv

# # Load Together.ai API key
# load_dotenv()
# api_key = os.getenv("TOGETHER_API_KEY")

# # ===== SHARED CONFIGURATION =====

# MODEL_NAME = "mistralai/Mixtral-8x7B-Instruct-v0.1"
# API_URL = "https://api.together.xyz/inference"

# HEADERS = {
#     "Authorization": f"Bearer {api_key}",
#     "Content-Type": "application/json"
# }


# def send_to_model(prompt: str, max_tokens: int = 500) -> str:
#     response = requests.post(
#         API_URL,
#         headers=HEADERS,
#         json={
#             "model": MODEL_NAME,
#             "prompt": prompt,
#             "max_tokens": max_tokens,
#             "temperature": 0.7,
#             "top_p": 0.9,
#             "stop": ["</s>"]
#         }
#     )
#     result = response.json()
#     return result['choices'][0]['text'].strip()


# # ===== OPTION 1: FULL TRANSCRIPT FEEDBACK =====

# def full_transcript_feedback():
#     # Load transcript from file
#     try:
#         with open("transcripts/sample_transcript.txt", "r") as file:
#             transcript = file.read()
#     except FileNotFoundError:
#         print("❌ Could not find 'sample_transcript.txt'. Please make sure it's in the 'transcripts/' folder.")
#         return

#     prompt = f"""
# You are a professional negotiation coach. Read the full negotiation transcript below and give categorized feedback.

# Include:
# - Tactical feedback
# - Strategic feedback
# - Behavioral feedback
# - Outcome-based feedback
# - Suggestions to improve

# Negotiation Transcript:
# {transcript}
# """

#     feedback = send_to_model(prompt)
#     print("=== FEEDBACK REPORT ===")
#     print(feedback)


# # ===== OPTION 2: CHATBOT COACHING MODE =====

# def coaching_chatbot():
#     SYSTEM_PROMPT = """
# You are a negotiation coach helping a seller improve their negotiation messages.

# The seller wants the buyer to agree to their offer. After each seller message, give:
# - Feedback (what they did well or should improve)
# - A short explanation
# - A suggested next message that would improve the buyer's chance of accepting

# Format:
# Feedback: ...
# Why: ...
# Suggested next message: ...
# """

#     print("\n📢 Coaching Chatbot Mode (Type 'exit' to quit)\n")

#     while True:
#         seller_input = input("🧑‍💼 You (Seller): ")
#         if seller_input.lower() == "exit":
#             break

#         prompt = f"{SYSTEM_PROMPT}\n\nSeller's message: {seller_input}"
#         feedback = send_to_model(prompt, max_tokens=300)
#         print("🤖 Coach:\n", feedback)
#         print("-" * 50)


# # ===== MAIN MENU =====

# def main():
#     print("🧠 Welcome to the AI Negotiation Feedback Agent!")
#     print("Choose a mode:")
#     print("1. Full Transcript Feedback")
#     print("2. Real-Time Coaching Chatbot\n")

#     choice = input("Enter 1 or 2: ")

#     if choice == "1":
#         full_transcript_feedback()
#     elif choice == "2":
#         coaching_chatbot()
#     else:
#         print("❌ Invalid choice. Please run again and enter 1 or 2.")

# if __name__ == "__main__":
#     main()
# 2
# CODE 1 BELOW:
# import os
# import requests
# from dotenv import load_dotenv

# # Load API key
# load_dotenv()
# api_key = os.getenv("TOGETHER_API_KEY")

# # Load transcript
# with open("transcripts/sample_transcript.txt", "r") as file:
#     transcript = file.read()

# # Better prompt
# prompt = f"""
# You are a professional negotiation coach. Read the negotiation below and give categorized feedback to help the negotiator improve. Use bullet points.

# For each item, include:
# 1. [Feedback Type] - Tactical / Strategic / Outcome / Behavioral
# 2. Feedback message (concise and helpful)

# Negotiation Transcript:
# {transcript}
# """

# # Together.ai API call
# response = requests.post(
#     "https://api.together.xyz/inference",
#     headers={
#         "Authorization": f"Bearer {api_key}",
#         "Content-Type": "application/json"
#     },
#     json={
#         "model": "mistralai/Mixtral-8x7B-Instruct-v0.1",
#         "prompt": prompt,
#         "max_tokens": 500,
#         "temperature": 0.7,
#         "top_p": 0.9,
#         "stop": ["</s>"]
#     }
# )

# # Extract feedback
# result = response.json()
# feedback = result['choices'][0]['text'].strip()

# # Display result
# print("=== FEEDBACK REPORT ===")
# print(feedback)



