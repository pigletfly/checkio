import string

def checkio(text):
    return max(string.ascii_lowercase, key=lambda ch: text.lower().count(ch))

if __name__ == '__main__':
    assert checkio("Hello World!") == "l", "Hello test"
    assert checkio("How do you do?") == "o", "O is most wanted"
    assert checkio("One") == "e", "All letter only once."
