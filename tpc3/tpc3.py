import re
import sys

def main ():
    sum = 0
    on = True
    regex_patterns = [
        r"(?P<integer>[+-]?\d+)",     # Pattern for capturing integers (positive or negative)
        r"(?P<on_state>on)",          # Pattern for capturing word 'on' (case insensitive)
        r"(?P<off_state>off)",        # Pattern for capturing word 'off' (case insensitive)
        r"(?P<sum>=)"                 # Pattern for capturing the equals sign
    ]

    all_patterns = re.compile('|'.join(regex_patterns), flags=re.I)
    for line in sys.stdin:
        matches_obtained = re.finditer(all_patterns, line)
        for unchecked_match in matches_obtained:
            if unchecked_match.lastgroup == 'integer':
                sum = sum + int(unchecked_match.group('integer')) if on else sum
            elif unchecked_match.lastgroup == 'on_state':
                on = True
            elif unchecked_match.lastgroup == 'off_state':
                on = False
            elif unchecked_match.lastgroup == 'sum':
                print("Soma = " + str(sum))


if __name__ == "__main__":
    main()