from functools import lru_cache

@lru_cache
def load_llm():
    from transformers import pipeline
    return pipeline("text2text-generation", model="google/flan-t5-small")

def llm_insight(question, summary):
    llm = load_llm()
    prompt = f"{summary}\n\nQuestion: {question}"
    return llm(prompt, max_new_tokens=150)[0]["generated_text"]
