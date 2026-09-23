def count_words(text):
    words=text.split()

    counts={}

    for word in words:
        counts[word]=counts.get(word,0)+1
    return counts


paragraph = """
Python is a popular programming language.
Python is useful for data analysis.
Learning Python takes practice, and practice builds confidence.
"""

print(count_words(paragraph))
