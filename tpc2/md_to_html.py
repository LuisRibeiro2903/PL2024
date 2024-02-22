import re
import sys



def header_check (line: str) -> str:
    regex = r"^ {0,3}(#+) "
    regex_match = re.match(regex, line)
    if regex_match:
        header_level = len(regex_match.group(1))
        _, upper_bound = regex_match.span()
        html_line = f"<h{header_level}>{line[upper_bound:]}</h{header_level}>\n"
    else:
        html_line = None
        
    return html_line
        
        
def italic_check(line: str) -> str:
    regex = r"\*(.+)\*"
    result = re.sub(regex, lambda match:f"<i>{match.group(1)}</i>", line)
    return result

def bold_check(line: str) -> str:
    regex = r"\*\*(.+)\*\*"
    matchssd = re.match(regex, line)
    result = re.sub(regex, lambda match:f"<b>{match.group(1)}</b>", line)
    return result


def handle_line(line: str) -> str:
    result = line
    tmp = header_check(result)
    if tmp:
        result = tmp
    result = bold_check(result)
    result = italic_check(result)
    return result
    



def main ():
    html = f""
    for line in sys.stdin:
        new_adition = handle_line(line.strip())
        html += new_adition
    
    file = open("result.html", "w" ,encoding="utf-8")
    file.write(html)
    file.close()


if __name__ == "__main__":
    main()