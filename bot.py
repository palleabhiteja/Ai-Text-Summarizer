

from transformers import pipeline


summarizer = pipeline("summarization")

def summarize_text(text, max_length=100, min_length=30):
    """
    Summarize the input text.
    
    :param text: The text to summarize
    :param max_length: Maximum length of summary
    :param min_length: Minimum length of summary
    :return: Summary string
    """
    summary = summarizer(text, max_length=max_length, min_length=min_length, do_sample=False)
    return summary[0]['summary_text']

if __name__ == "__main__":
    print("Enter your text (type 'exit' to quit):")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("Goodbye!")
            break
        summary = summarize_text(user_input)
        print("Summary:", summary)
