def convert(string):
    converted_string=string.replace(":)","🙂").replace(":(","🙁")
    return converted_string
def main():
    hello=input("say hello:")
    Emoji=convert(hello)
    print("converted string:",Emoji)
main()