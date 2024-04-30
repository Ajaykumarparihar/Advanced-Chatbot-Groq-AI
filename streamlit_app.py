import streamlit as st
from groq import Groq

# Initialize the Groq client
client = Groq(
    api_key=("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"),
)

def get_chat_response(system_message, user_message):
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": system_message,
            },
            {
                "role": "user",
                "content": user_message,
            }
        ],
        model="mixtral-8x7b-32768",
    )
    return chat_completion.choices[0].message.content

def main():
    st.title("Advanced Chatbot")
    
    # Input fields for system and user messages
    system_input = st.text_input("System Message:")
    user_input = st.text_input("User Message:")
    
    # Submit button
    if st.button("Submit"):
        response = get_chat_response(system_input, user_input)
        st.write(f"Bot: {response}")

if __name__ == "__main__":
    main()




# streamlit run stream.py
