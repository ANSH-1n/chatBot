# import os

# import streamlit as st
# from dotenv import load_dotenv
# import google.generativeai as gen_ai


# # Load environment variables
# load_dotenv()

# # Configure Streamlit page settings
# st.set_page_config(
#     page_title="Chat with Gemini-Pro!",
#     page_icon=":brain:",  # Favicon emoji
#     layout="centered",  # Page layout option
# )

# GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# # Set up Google Gemini-Pro AI model
# gen_ai.configure(api_key=GOOGLE_API_KEY)
# model = gen_ai.GenerativeModel('gemini-pro')


# # Function to translate roles between Gemini-Pro and Streamlit terminology
# def translate_role_for_streamlit(user_role):
#     if user_role == "model":
#         return "assistant"
#     else:
#         return user_role


# # Initialize chat session in Streamlit if not already present
# if "chat_session" not in st.session_state:
#     st.session_state.chat_session = model.start_chat(history=[])


# # Display the chatbot's title on the page
# st.title("🤖 Gemini Pro - ChatBot")

# # Display the chat history
# for message in st.session_state.chat_session.history:
#     with st.chat_message(translate_role_for_streamlit(message.role)):
#         st.markdown(message.parts[0].text)

# # Input field for user's message
# user_prompt = st.chat_input("Ask Gemini-Pro...")
# if user_prompt:
#     # Add user's message to chat and display it
#     st.chat_message("user").markdown(user_prompt)

#     # Send user's message to Gemini-Pro and get the response
#     gemini_response = st.session_state.chat_session.send_message(user_prompt)

#     # Display Gemini-Pro's response
#     with st.chat_message("assistant"):
#         st.markdown(gemini_response.text)











# import os

# import streamlit as st
# from dotenv import load_dotenv
# import google.generativeai as gen_ai


# # Load environment variables
# load_dotenv()

# # Configure Streamlit page settings
# st.set_page_config(
#     page_title="Chat with Gemini-Pro!",
#     page_icon=":brain:",
#     layout="centered",
# )

# # Set up Google Gemini-Pro AI model
# GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
# gen_ai.configure(api_key=GOOGLE_API_KEY)
# model = gen_ai.GenerativeModel('gemini-pro')


# # Function to translate roles between Gemini-Pro and Streamlit terminology
# def translate_role_for_streamlit(user_role):
#     if user_role == "model":
#         return "assistant"
#     else:
#         return user_role


# # Initialize chat session in Streamlit if not already present
# if "chat_session" not in st.session_state:
#     st.session_state.chat_session = model.start_chat(history=[])


# # Styling with custom CSS
# st.markdown(
#     """
#     <style>
#     /* General body styles */
#     body {
#         font-family: 'Arial', sans-serif;
#         background: linear-gradient(to right, #e0eafc, #cfdef3);
#         margin: 0;
#     }

#     /* Header styles */
#     .header {
#         text-align: center;
#         color: #4CAF50;
#         font-size: 2em;
#         font-weight: bold;
#         margin-bottom: 10px;
#     }

#     /* Chat history area */
#     .chat-history {
#         border: 1px solid #ddd;
#         border-radius: 10px;
#         padding: 10px;
#         height: 400px;
#         overflow-y: auto;
#         margin-bottom: 10px;
#         background-color: white;
#     }

#     /* Input box styling */
#     .user-input {
#         border: 1px solid #aaa;
#         border-radius: 8px;
#         padding: 10px;
#         width: 100%;
#         margin-bottom: 20px;
#         box-shadow: 0px 2px 4px rgba(0, 0, 0, 0.1);
#     }

#     /* Styled assistant message */
#     .assistant-msg {
#         background-color: #f0f8ff;
#         border-radius: 8px;
#         padding: 10px;
#         box-shadow: 1px 1px 5px rgba(0, 0, 0, 0.2);
#         margin-bottom: 5px;
#     }

#     /* User message bubble */
#     .user-msg {
#         background-color: #d1e7dd;
#         border-radius: 8px;
#         padding: 10px;
#         box-shadow: 1px 1px 5px rgba(0, 0, 0, 0.2);
#         margin-bottom: 5px;
#         text-align: right;
#     }
#     </style>
#     """,
#     unsafe_allow_html=True,
# )

# # Display the chatbot's styled header
# st.markdown('<div class="header">🤖 Gemini Pro - ChatBot</div>', unsafe_allow_html=True)

# # Display the chat history
# st.subheader("💬 Chat History")
# chat_container = st.container()
# with chat_container:
#     for message in st.session_state.chat_session.history:
#         with st.chat_message(translate_role_for_streamlit(message.role)):
#             st.markdown(
#                 f'<div class="{"assistant-msg" if message.role == "model" else "user-msg"}">{message.parts[0].text}</div>',
#                 unsafe_allow_html=True,
#             )

# # Input area with user-friendly design
# st.subheader("💭 Your Message")
# user_prompt = st.text_input(
#     "Type your message below:", 
#     key="user_input", 
#     placeholder="Type your thoughts here...",
#     label_visibility="visible",
# )

# # Handle user input & send it
# if user_prompt:
#     with st.chat_message("user"):
#         st.markdown(
#             f'<div class="user-msg">{user_prompt}</div>',
#             unsafe_allow_html=True,
#         )

#     # Send user's message and get a response
#     gemini_response = st.session_state.chat_session.send_message(user_prompt)

#     # Render the response from Gemini-Pro in a styled way
#     with st.chat_message("assistant"):
#         st.markdown(
#             f'<div class="assistant-msg">{gemini_response.text}</div>',
#             unsafe_allow_html=True,
#         )







# import os
# import streamlit as st
# from dotenv import load_dotenv
# import google.generativeai as gen_ai
# import pandas as pd
# import matplotlib.pyplot as plt
# import plotly.express as px


# # Load environment variables
# load_dotenv()

# # Configure Streamlit page settings
# st.set_page_config(
#     page_title="Chat with Gemini-Pro!",
#     page_icon=":brain:",
#     layout="centered",
# )

# # Set up Google Gemini-Pro AI model
# GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
# gen_ai.configure(api_key=GOOGLE_API_KEY)
# model = gen_ai.GenerativeModel('gemini-pro')


# # Function to translate roles between Gemini-Pro and Streamlit terminology
# def translate_role_for_streamlit(user_role):
#     if user_role == "model":
#         return "assistant"
#     else:
#         return user_role


# # Initialize chat session in Streamlit if not already present
# if "chat_session" not in st.session_state:
#     st.session_state.chat_session = model.start_chat(history=[])

# # Initialize DataFrame to log chat history
# if "user_logs" not in st.session_state:
#     st.session_state.user_logs = pd.DataFrame(columns=["timestamp", "user_input", "assistant_response"])


# # Styling with custom CSS
# st.markdown(
#     """
#     <style>
#     /* General body styles */
#     body {
#         font-family: 'Arial', sans-serif;
#         background: linear-gradient(to right, #e0eafc, #cfdef3);
#         margin: 0;
#     }

#     /* Header styles */
#     .header {
#         text-align: center;
#         color: #4CAF50;
#         font-size: 2em;
#         font-weight: bold;
#         margin-bottom: 10px;
#     }

#     /* Styled assistant message */
#     .assistant-msg {
#         background-color: #f0f8ff;
#         border-radius: 8px;
#         padding: 10px;
#         box-shadow: 1px 1px 5px rgba(0, 0, 0, 0.2);
#         margin-bottom: 5px;
#     }

#     /* User message bubble */
#     .user-msg {
#         background-color: #d1e7dd;
#         border-radius: 8px;
#         padding: 10px;
#         box-shadow: 1px 1px 5px rgba(0, 0, 0, 0.2);
#         margin-bottom: 5px;
#         text-align: right;
#     }
#     </style>
#     """,
#     unsafe_allow_html=True,
# )

# # Display the chatbot's styled header
# st.markdown('<div class="header">🤖 Gemini Pro - ChatBot</div>', unsafe_allow_html=True)

# # Display the chat history
# st.subheader("💬 Chat History")
# chat_container = st.container()
# with chat_container:
#     for message in st.session_state.chat_session.history:
#         with st.chat_message(translate_role_for_streamlit(message.role)):
#             st.markdown(
#                 f'<div class="{"assistant-msg" if message.role == "model" else "user-msg"}">{message.parts[0].text}</div>',
#                 unsafe_allow_html=True,
#             )

# # Input area with user-friendly design
# st.subheader("💭 Your Message")
# user_prompt = st.text_input(
#     "Type your message below:", 
#     key="user_input", 
#     placeholder="Type your thoughts here...",
# )

# # Handle user input & send it
# if user_prompt:
#     with st.chat_message("user"):
#         st.markdown(
#             f'<div class="user-msg">{user_prompt}</div>',
#             unsafe_allow_html=True,
#         )

#     # Send user's message and get a response
#     gemini_response = st.session_state.chat_session.send_message(user_prompt)

#     # Log user interaction into DataFrame
#     timestamp = pd.Timestamp.now()
#     new_log = pd.DataFrame({
#         "timestamp": [timestamp],
#         "user_input": [user_prompt],
#         "assistant_response": [gemini_response.text]
#     })
#     st.session_state.user_logs = pd.concat([st.session_state.user_logs, new_log], ignore_index=True)

#     # Render the response from Gemini-Pro in a styled way
#     with st.chat_message("assistant"):
#         st.markdown(
#             f'<div class="assistant-msg">{gemini_response.text}</div>',
#             unsafe_allow_html=True,
#         )


# # Data Visualization Section
# st.subheader("📊 Analytics & Logs")

# if len(st.session_state.user_logs) > 1:
#     # Display logs in a DataFrame for user insight
#     if st.button("Show User Logs"):
#         st.write("User logs for interactions:")
#         st.dataframe(st.session_state.user_logs)

#     # Generate Graphs using Plotly
#     user_logs_plot = st.session_state.user_logs.copy()
#     user_logs_plot["response_length"] = user_logs_plot["assistant_response"].apply(len)  # Calculate response length

#     fig = px.line(
#         user_logs_plot,
#         x="timestamp",
#         y="response_length",
#         title="Assistant Response Length Over Time",
#         labels={"response_length": "Response Length (characters)", "timestamp": "Timestamps"},
#         color_discrete_sequence=["blue"]
#     )

#     st.plotly_chart(fig)

# else:
#     st.write("Interact with the chatbot to generate logs and view insights!")

# # Allow users to download logs as CSV
# st.download_button(
#     label="Download Chat Logs as CSV",
#     data=st.session_state.user_logs.to_csv(index=False).encode('utf-8'),
#     file_name="user_logs.csv",
#     mime="text/csv",
# )






# import os
# import streamlit as st
# from dotenv import load_dotenv
# import google.generativeai as gen_ai
# import pandas as pd
# import matplotlib.pyplot as plt
# import plotly.express as px


# # Load environment variables
# load_dotenv()

# # Configure Streamlit page settings
# st.set_page_config(
#     page_title="Chat with Gemini-Pro!",
#     page_icon=":brain:",
#     layout="centered",
# )

# # Set up Google Gemini-Pro AI model safely
# GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# if not GOOGLE_API_KEY:
#     st.error("Google API key is missing. Please add it to secrets.toml or the environment.")
# else:
#     try:
#         gen_ai.configure(api_key=GOOGLE_API_KEY)
#         model = gen_ai.GenerativeModel('gemini-pro')
#     except Exception as e:
#         st.error(f"Failed to configure AI model with API key. Error: {e}")


# # Function to translate roles between Gemini-Pro and Streamlit terminology
# def translate_role_for_streamlit(user_role):
#     if user_role == "model":
#         return "assistant"
#     else:
#         return user_role


# # Initialize chat session in Streamlit if not already present
# if "chat_session" not in st.session_state:
#     try:
#         st.session_state.chat_session = model.start_chat(history=[])
#     except Exception as e:
#         st.error(f"Error initializing chat session: {e}")

# # Initialize DataFrame to log chat history
# if "user_logs" not in st.session_state:
#     st.session_state.user_logs = pd.DataFrame(columns=["timestamp", "user_input", "assistant_response"])

# # Styling with custom CSS
# st.markdown(
#     """
#     <style>
#     /* General body styles */
#     body {
#         font-family: 'Arial', sans-serif;
#         background: linear-gradient(to right, #e0eafc, #cfdef3);
#         margin: 0;
#     }

#     /* Header styles */
#     .header {
#         text-align: center;
#         color: #4CAF50;
#         font-size: 2em;
#         font-weight: bold;
#         margin-bottom: 10px;
#     }

#     /* Styled assistant message */
#     .assistant-msg {
#         background-color: #f0f8ff;
#         border-radius: 8px;
#         padding: 10px;
#         box-shadow: 1px 1px 5px rgba(0, 0, 0, 0.2);
#         margin-bottom: 5px;
#     }

#     /* User message bubble */
#     .user-msg {
#         background-color: #d1e7dd;
#         border-radius: 8px;
#         padding: 10px;
#         box-shadow: 1px 1px 5px rgba(0, 0, 0, 0.2);
#         margin-bottom: 5px;
#         text-align: right;
#     }
#     </style>
#     """,
#     unsafe_allow_html=True,
# )

# # Display the chatbot's styled header
# st.markdown('<div class="header">🤖 Gemini Pro - ChatBot</div>', unsafe_allow_html=True)

# # Display the chat history
# st.subheader("💬 Chat History")
# chat_container = st.container()
# with chat_container:
#     for message in st.session_state.chat_session.history:
#         role_class = "assistant-msg" if message.role == "model" else "user-msg"
#         st.markdown(
#             f'<div class="{role_class}">{message.parts[0].text}</div>',
#             unsafe_allow_html=True,
#         )

# # Input area with user-friendly design
# st.subheader("💭 Your Message")
# user_prompt = st.text_input(
#     "Type your message below:", 
#     key="user_input", 
#     placeholder="Type your thoughts here..."
# )

# # Handle user input & send it
# if user_prompt:
#     with st.chat_message("user"):
#         st.markdown(
#             f'<div class="user-msg">{user_prompt}</div>',
#             unsafe_allow_html=True,
#         )

#     try:
#         # Send user's message and get a response
#         gemini_response = st.session_state.chat_session.send_message(user_prompt)

#         # Log user interaction into DataFrame
#         timestamp = pd.Timestamp.now()
#         new_log = pd.DataFrame({
#             "timestamp": [timestamp],
#             "user_input": [user_prompt],
#             "assistant_response": [gemini_response.text]
#         })
#         st.session_state.user_logs = pd.concat([st.session_state.user_logs, new_log], ignore_index=True)

#         # Render the response from Gemini-Pro in a styled way
#         with st.chat_message("assistant"):
#             st.markdown(
#                 f'<div class="assistant-msg">{gemini_response.text}</div>',
#                 unsafe_allow_html=True,
#             )
#     except Exception as e:
#         st.error(f"Failed to send the message to the AI model: {e}")


# # Data Visualization Section
# st.subheader("📊 Analytics & Logs")
# if len(st.session_state.user_logs) > 0:
#     if st.button("Show User Logs"):
#         st.write("User logs for interactions:")
#         st.dataframe(st.session_state.user_logs)

#     # Generate Graphs using Plotly
#     user_logs_plot = st.session_state.user_logs.copy()
#     user_logs_plot["response_length"] = user_logs_plot["assistant_response"].apply(len)  # Log response length

#     fig = px.line(
#         user_logs_plot,
#         x="timestamp",
#         y="response_length",
#         title="Assistant Response Length Over Time",
#         labels={"response_length": "Response Length", "timestamp": "Timestamps"},
#         color_discrete_sequence=["blue"]
#     )

#     st.plotly_chart(fig)

# else:
#     st.write("Interact with the chatbot to generate logs and view insights!")

# # Allow users to download logs as CSV
# st.download_button(
#     label="Download Chat Logs as CSV",
#     data=st.session_state.user_logs.to_csv(index=False).encode('utf-8'),
#     file_name="user_logs.csv",
#     mime="text/csv",
# )





import os
import streamlit as st
from dotenv import load_dotenv
import google.generativeai as gen_ai
import pandas as pd
import plotly.express as px


# Load environment variables
load_dotenv()

# Configure Streamlit page settings
st.set_page_config(
    page_title="Chat with Gemini-Pro!",
    page_icon=":brain:",
    layout="centered",
)

# Set up Google Gemini-Pro AI model safely
GOOGLE_API_KEY = st.secrets.get("GOOGLE_API_KEY")  # Fetch from Streamlit secrets directly

if not GOOGLE_API_KEY:
    st.error("Google API key is missing from Streamlit secrets. Please add it there.")
    st.stop()  # Stop execution if key is missing
else:
    try:
        gen_ai.configure(api_key=GOOGLE_API_KEY)
        model = gen_ai.GenerativeModel("gemini-pro")
    except Exception as e:
        st.error(f"Failed to initialize AI model with provided API key: {e}")
        st.stop()


# Function to translate roles safely
def translate_role_for_streamlit(user_role):
    if user_role == "model":
        return "assistant"
    else:
        return user_role


# Initialize a safe chat session
if "chat_session" not in st.session_state:
    try:
        st.session_state.chat_session = model.start_chat(history=[])
    except Exception as e:
        st.error(f"Error initializing chat session: {e}")
        st.stop()


# Initialize logging structure if absent
if "user_logs" not in st.session_state:
    st.session_state.user_logs = pd.DataFrame(columns=["timestamp", "user_input", "assistant_response"])


# Display the chat history safely
st.subheader("💬 Chat History")
chat_container = st.container()
with chat_container:
    try:
        # Ensure chat history is only fetched if valid session is initialized
        if st.session_state.chat_session and st.session_state.chat_session.history:
            for message in st.session_state.chat_session.history:
                role_class = "assistant-msg" if message.role == "model" else "user-msg"
                st.markdown(
                    f'<div class="{role_class}">{message.parts[0].text}</div>',
                    unsafe_allow_html=True,
                )
        else:
            st.warning("No chat session history found.")
    except AttributeError as e:
        st.error(f"Error accessing history: {e}")


# Input area design
st.subheader("💭 Your Message")
user_prompt = st.text_input(
    "Type your message below:",
    key="user_input",
    placeholder="Type your thoughts here..."
)

# Process the user input safely
if user_prompt:
    with st.chat_message("user"):
        st.markdown(
            f'<div class="user-msg">{user_prompt}</div>',
            unsafe_allow_html=True,
        )

    try:
        # Send the user's prompt to the model safely
        gemini_response = st.session_state.chat_session.send_message(user_prompt)

        # Log response
        timestamp = pd.Timestamp.now()
        new_log = pd.DataFrame({
            "timestamp": [timestamp],
            "user_input": [user_prompt],
            "assistant_response": [gemini_response.text]
        })
        st.session_state.user_logs = pd.concat([st.session_state.user_logs, new_log], ignore_index=True)

        # Display assistant response safely
        with st.chat_message("assistant"):
            st.markdown(
                f'<div class="assistant-msg">{gemini_response.text}</div>',
                unsafe_allow_html=True,
            )
    except Exception as e:
        st.error(f"Failed to send message to AI model: {e}")

# Analytics Section
st.subheader("📊 Analytics & Logs")
if len(st.session_state.user_logs) > 0:
    if st.button("Show User Logs"):
        st.write("User logs for interactions:")
        st.dataframe(st.session_state.user_logs)

st.download_button(
    label="Download Chat Logs as CSV",
    data=st.session_state.user_logs.to_csv(index=False).encode('utf-8'),
    file_name="user_logs.csv",
    mime="text/csv",
)




