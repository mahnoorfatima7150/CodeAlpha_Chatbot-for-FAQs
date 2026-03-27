import streamlit as st
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
st.title(" FAQ Chatbot")
questions = [
    "what is ai",
    "what is python",
    "what is machine learning",
    "what is deep learning",
    "who are you"
]
answers = [
    "AI stands for Artificial Intelligence.",
    "Python is a programming language.",
    "Machine learning is a subset of AI.",
    "Deep learning is a type of machine learning.",
    "I am your AI chatbot!"
]
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(questions)
user_input = st.text_input("Ask a question")
if st.button("Ask"):
    if user_input:
        user_vec = vectorizer.transform([user_input])
        similarity = cosine_similarity(user_vec, X)
        index = similarity.argmax()
        st.success(answers[index])
    else:
        st.warning("Please enter a question")