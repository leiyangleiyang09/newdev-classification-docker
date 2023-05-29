import re


def normalize_text(s: str) -> str:
    s = s.lower()
    s = re.sub(r'\s\W', ' ', s)
    s = re.sub(r'\W\s', ' ', s)
    s = re.sub(r'\s+', ' ', s)
    return s


def clean_data(doc: str) -> str:
    cleaned_text = ""
    for char in doc:
        if ord(char) >= 128 or ord(char) <= 31:
            cleaned_text = cleaned_text + " "
        else:
            cleaned_text = cleaned_text + char
    return cleaned_text


def clean_text(sentence_text: str) -> str:
    sentence_text = sentence_text.replace('\\\n', ' ')
    sentence_text = sentence_text.replace('\\\t', ' ')
    sentence_text = sentence_text.replace('\\\r', ' ')
    sentence_text = sentence_text.replace('\n', ' ')
    sentence_text = sentence_text.replace('\t', ' ')
    sentence_text = sentence_text.replace('\r', ' ')
    while '  ' in sentence_text:
        sentence_text = sentence_text.replace('  ', ' ')
    return sentence_text.strip()
