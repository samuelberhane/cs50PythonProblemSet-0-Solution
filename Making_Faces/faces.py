def convert(text):
    words = text.split()
    emojis = {
       ':)': '🙂',
       ':(': '🙁'
    }
    result = ""
    for word in words:
       result += emojis.get(word, word) + " "
    print(result)


def main():
    text = input('Enter a text: ')
    convert(text)

main()