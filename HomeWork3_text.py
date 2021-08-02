def main_function():
    length = int(input("enter the number of characters (min 35):\n"))

    def symbols_in_words(a):
        return len(" ".join(a))
    def format_string(words):
        left_whitespaces = length - sum(len(word) for word in words)
        while left_whitespaces > 0:
            if len(words) > 1:
                for i in range(len(words) - 1):
                    words[i] += " "
                    left_whitespaces -= 1
                    if left_whitespaces == 0:
                        break
            else:
                words[0] += " " * (length - len(words[0]))
                break
        final_string = "".join(words)
        return final_string + "\n"

    if length < 35:
        print("you entered a number less '35'")
        main_function()
    else:
        with open("text.txt", "r", encoding="utf-8") as z:
            text = z.read()
            words = text.split(" ")
            current_string = []
            new_text = ""

            while words:
                word = words[0]
                words = words[1:]

                if symbols_in_words(current_string + [word]) <= length:
                    if "\n" in word:
                        a, b = word.split("\n")
                        word = a
                        words = [b] + words
                        new_text += format_string(current_string + [word, "\n"])
                        current_string = []
                    else:
                        current_string += [word]
                else:
                    new_text += format_string(current_string)
                    current_string = [word]

            new_text += format_string(current_string)

        with open("new_text.txt", "w", encoding="utf-8") as writer:
            writer.write(new_text)

        print("text edited and saved 'new_text.txt'")

main_function()