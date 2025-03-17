# 📄 ai_summary_hf.py
from transformers import pipeline

# Load Hugging Face Summarization Model
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def generate_nlp_summary(report_text):
    # Split long text into chunks for processing
    max_length = 1024
    chunks = [report_text[i:i+max_length] for i in range(0, len(report_text), max_length)]
    
    summary = []
    for chunk in chunks:
        result = summarizer(chunk, max_length=200, min_length=50, do_sample=False)
        summary.append(result[0]['summary_text'])
    
    return " ".join(summary)
