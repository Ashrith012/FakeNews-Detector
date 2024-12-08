# FakeNews-Detection using NLP

# Overview
This project implements a Fake News Detection System using Natural Language Processing (NLP) techniques and a Naive Bayes-based algorithm. The system analyzes news articles for patterns such as the presence of quotes, verbs, and named entities to classify them as either Real News or Fake News.

# Features
. Admin Login: Secure access for administrators to manage the system.
. News Document Upload: Upload news articles for evaluation.
. Fake News Detector Algorithm:
  . Extracts quotes, verbs, and named entities.
  . Applies a Naive Bayes algorithm to calculate a Fake Rank Score.
. Classification Results: Displays detection results with corresponding scores.

# Technologies Used
. Backend: Django
. NLP Libraries:
  . TextBlob
  . NLTK (Natural Language Toolkit)
. Frontend: HTML, CSS
. File Handling: Django's FileSystemStorage

# How It Works
1. Upload News Document: Users can upload a text document containing news articles.
2. Processing and Analysis:
    . Detects quotes, verbs, and named entities using NLP.
    . Calculates a Fake Rank Score for each article based on these features.
3. Classification:
    . Articles with a score > 0.90 are classified as "Real News."
    . Articles with a score ≤ 0.90 are classified as "Fake News."
4. Results Display: The analysis results are presented in a tabular format.
