# 📄 ai_summary_hf.py
from transformers import pipeline

# Load Hugging Face Summarization Model
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def generate_nlp_summary(text):
    """Generates AI summary dynamically based on input length with better structuring."""
    if not text.strip():
        return "No meaningful data available for summarization."

    input_length = len(text.split())  # Count words
    max_length = min(150, int(input_length * 1.8))  # Dynamic length for better summaries

    # Ensure proper chunking for long inputs
    chunks = [text[i:i + 1024] for i in range(0, len(text), 1024)]
    summary = []

    for chunk in chunks:
        result = summarizer(chunk, max_length=max_length, min_length=50, do_sample=False)
        summary.append(result[0]['summary_text'])

    return " ".join(summary)
