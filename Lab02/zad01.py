import re
from collections import Counter

stop_words = {'i', 'o', 'a', 'w', 'u', 'z'}

def zadanie1(text):
    count_paragraph = len([p for p in text.split('/n') if p.strip()])

    sentences = re.split(r'[.!?]', text)
    count_sentences = len([s for s in sentences if s.strip()])

    words = re.findall(r'\b\w+\b', text.lower())
    count_words = len(words)

    filtered_words = [word for word in words if word not in stop_words]
    word_freq = Counter(filtered_words)
    most_common_words = word_freq.most_common(10)

    wyniki = {
        "count_paragraph": count_paragraph,
        "count_sentences": count_sentences,
        "count_words": count_words,
        "most_common_words": most_common_words
    }
    return wyniki

text = """Przykład tekstu."""
wyniki = zadanie1(text)

print(f'Ilość akapitów: {wyniki["count_paragraph"]}')
print(f'Ilość zdań: {wyniki["count_sentences"]}')
print(f'Ilość słów: {wyniki["count_words"]}')
print(f'Najczęściej występujące słowa: {wyniki["most_common_words"]}')