from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import sys

try:
    model_name = "facebook/bart-large-cnn"
    print(f"Testing download for {model_name}...")
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    print("Tokenizer loaded.")
    model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
    print("Model loaded.")
except Exception as e:
    print(f"Error: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)
