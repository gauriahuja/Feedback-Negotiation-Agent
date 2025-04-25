# Feedback-Negotiation-Agent
This project simulates an AI-powered negotiation environment where a **seller** negotiates with a **buyer agent** (AI) and receives **coaching feedback** in real-time.

Built using the **Together.ai** API and the **Mixtral-8x7B-Instruct** model, this tool generates realistic negotiation dialogues and provides categorized coaching feedback to help improve negotiation strategy.


##  Features

- **Buyer Simulation:**
  - AI acts as a buyer and responds realistically to the seller's negotiation attempts.

- **Coaching Feedback:**
  - AI coach evaluates each seller response.
  - Provides:
    - Feedback
    - Explanation
    - Suggested improved response

- **Transcript Analysis Mode:**
  - Analyze complete negotiation transcripts for:
    - Tactical
    - Strategic
    - Behavioral
    - Outcome-based feedback

## Technologies Used

- Python 3.9+
- [Together.ai API](https://www.together.ai/)
- Mixtral-8x7B-Instruct-v0.1 model
- LangChain
- python-dotenv

## Project Structure
.
├── main.py                # Main script with chat and transcript analysis modes
├── .env                   # Contains Together.ai API key
├── requirements.txt       # List of required Python packages
├── feedback_prompt.txt    # Prompt template for transcript feedback
├── sample_transcript.txt  # Example transcript for demo/test

## Installation

1. Install the required Python packages:
   ```bash
   pip install -r requirements.txt

Create a `.env` file and add your Together.ai API key:

```env
TOGETHER_API_KEY=your_api_key_here

## How to Use

### Option 1: Chat Coaching Mode
Run the chatbot to simulate live negotiation:

python main.py

Follow the prompts:
- AI plays the buyer.
- After your message, the AI coach gives feedback.

### Option 2: Transcript Feedback Mode
- Upload or modify `sample_transcript.txt`.
- Switch to transcript mode in `main.py`.
- Receive categorized, structured feedback.

## 🔍 Example Output

Buyer: That’s too expensive. I can do $350.
Seller: I can lower it slightly to $580.

Coach Feedback:
- Feedback: Good attempt to show flexibility.
- Why: You anchored the price but may still seem rigid.
- Suggested next message: I can offer $580 and include an accessory to add more value.

## License
This project is intended for academic and research purposes at the University of Florida.

## Author
Gauri Ahuja  
M.S. in Computer Science, University of Florida  
[LinkedIn](https://linkedin.com/in/gauri777) | [Email](mailto:ahujagauri@ufl.edu)

## Acknowledgements
- Built as part of ongoing research in AI-driven feedback systems.
- Inspired by real-world negotiation training needs and agentic AI applications.

##  Don't forget to star the repo if you find it useful!
