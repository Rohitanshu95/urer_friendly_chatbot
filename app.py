import streamlit as st
from gemini_api import get_gemini_response  # Your existing Gemini API integration
from PIL import Image
import io

# Page configuration
st.set_page_config(page_title="Gemini Chatbot", page_icon="🤖")

# Apply dark theme CSS
st.markdown(
    """
    <style>
        .stApp { background-color: #121212; color: white; }
        .chat-container { max-width: 700px; margin: auto; }
        .user-msg, .assistant-msg {
            padding: 12px; margin: 10px 0; border-radius: 15px;
            font-size: 16px; box-shadow: 0 0 10px rgba(255, 255, 255, 0.2);
        }
        .user-msg { background-color: #343a40; color: white; text-align: right; }
        .assistant-msg { background-color: #6c757d; color: white; }
        .stChatInput>div { background-color: #333 !important; color: white !important; border-radius: 10px; border: 1px solid #555; }
        .stSidebar { background-color: #1a1a1a; }
        ::-webkit-scrollbar { width: 6px; }
        ::-webkit-scrollbar-thumb { background: #ae2012; border-radius: 10px; }
    </style>
    """,
    unsafe_allow_html=True
)

# Sidebar with logo (Updated Path)
st.sidebar.image(r"C:\Users\ASUS\Downloads\images__1_-removebg-preview.png", 
                 caption="🤖 Gemini Chatbot", 
                 use_column_width=True)

st.title("🌙 Gemini Chatbot")

# Chat container
st.markdown('<div class="chat-container">', unsafe_allow_html=True)
if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    role_class = "user-msg" if message["role"] == "user" else "assistant-msg"
    prefix = "🧑‍💻 " if message["role"] == "user" else "🤖 "
    st.markdown(f'<div class="{role_class}">{prefix}{message["content"]}</div>', unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)

# File Upload Section
uploaded_file = st.sidebar.file_uploader("📂 Upload a file (TXT, PDF, CSV, etc.)", type=["txt", "pdf", "csv"])
if uploaded_file is not None:
    file_details = {"Filename": uploaded_file.name, "FileType": uploaded_file.type, "FileSize": uploaded_file.size}
    st.sidebar.write("✅ File uploaded successfully!", file_details)

    # Process text files
    if uploaded_file.type == "text/plain":
        file_content = str(uploaded_file.read(), "utf-8")
        st.sidebar.text_area("📄 File Content:", file_content, height=200)

# Image Upload Section
uploaded_image = st.sidebar.file_uploader("🖼️ Upload an Image (JPG, PNG)", type=["jpg", "png", "jpeg"])
if uploaded_image is not None:
    image = Image.open(uploaded_image)
    st.sidebar.image(image, caption="Uploaded Image", use_column_width=True)

# User input
if user_input := st.chat_input("Ask me something..."):
    st.session_state.messages.append({"role": "user", "content": user_input})
    st.markdown(f'<div class="user-msg">🧑‍💻 {user_input}</div>', unsafe_allow_html=True)

    # Get response from Gemini API
    response = get_gemini_response(user_input)

    # Store and display AI response
    st.session_state.messages.append({"role": "assistant", "content": response})
    st.markdown(f'<div class="assistant-msg">🤖 {response}</div>', unsafe_allow_html=True)
