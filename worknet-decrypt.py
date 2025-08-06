#!/usr/bin/env python3
import sys

### Developed and maintained by wwwiesel (https://github.com/wwwiesel) 
### This tool is intended for educational purposes and authorized security assessments only.  Use it responsibly and only in environments you are authorized to test.

# Mapping
mapping = {
    # big to small
    'Q': 'a', 'W': 'b', 'E': 'c', 'R': 'd', 'T': 'e',
    'Z': 'f', 'U': 'g', 'I': 'h', 'O': 'i', 'P': 'j',
    'A': 'k', 'S': 'l', 'D': 'm', 'F': 'n', 'G': 'o',
    'H': 'p', 'J': 'q', 'V': 'w', 'L': 's', 'K': 'r',
    'Y': 't', 'X': 'u', 'C': 'w', 'B': 'x', 'N': 'y', 'M': 'z',

    # small to big
    'y': 'A', 'x': 'B', 'c': 'C', 'v': 'D', 'b': 'E',
    'n': 'F', 'm': 'G', 'l': 'H', 'k': 'I', 'j': 'J',
    'h': 'K', 'g': 'L', 'f': 'M', 'd': 'N', 's': 'O',
    'a': 'P', 'q': 'Q', 'w': 'R', 'e': 'S', 'r': 'T',
    't': 'U', 'z': 'V', 'u': 'W', 'i': 'X', 'o': 'Y', 'p': 'Z',

    # Special
    '0': '0', '1': '1', '2': '2', '3': '3', '4': '4',
    '5': '5', '6': '6', '7': '7', '8': '8', '9': '9',
    '$': '$', '!': '!', '§': '§', '%': '%', '/': '/', '-': '-',
    ')': ')', '=': '=', '_': '_', '(': '(', 'Ä': 'Ä', 'ä': 'ä', 'ü': 'ü'
}

def decrypt(text):
    return ''.join(mapping.get(c, c) for c in text)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("HowTo: python3 worknet2013-decrypt.py 'PASSWORD' (without'.')")
        sys.exit(1)

    input_text = sys.argv[1]
    print(decrypt(input_text))
