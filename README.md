# FAQ Chatbot (Streamlit + Machine Learning)

An interactive FAQ chatbot built using **Streamlit** and **Machine Learning (TF-IDF + Cosine Similarity)**.
It answers user questions based on similarity matching.

---

## Features

* Simple and clean UI with Streamlit
* Uses TF-IDF for text vectorization
* Uses Cosine Similarity to find best match
* Fast and lightweight chatbot

---

## How It Works

* Predefined questions are converted into vectors using **TF-IDF**
* User input is also converted into a vector
* Cosine similarity is calculated
* The most similar question is selected
* Corresponding answer is displayed

---

## Project Structure

```
.
├── src/
│   └── chatbot.py
├── output/
│   └── Chatbot.mp4
├── requirements.txt
└── README.md
```

---

## Requirements

Install dependencies using:

```bash
pip install -r requirements.txt
```

---

## Run the App

```bash
streamlit run src/chatbot.py
```

---

## Demo

Check the demo video here:
`output/Chatbot.mp4`

---

## Technologies Used

* Python
* Streamlit
* Scikit-learn

---

## Author

Mahnoor Fatima
