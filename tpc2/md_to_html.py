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
    regex = r"\*(.+?)\*"
    result = re.sub(regex, lambda match:f"<i>{match.group(1)}</i>", line)
    return result

def bold_check(line: str) -> str:
    regex = r"\*\*(.+?)\*\*"
    result = re.sub(regex, lambda match:f"<b>{match.group(1)}</b>", line)
    return result

def url_check(line: str) -> str:
    regex = r"\[(?P<texto>[^\]]*)\]\((?P<url>[^\)]*)\)"
    result = re.sub(regex, lambda match:f"<a href=\'{match.group('url')}\'>{match.group('texto')}</a>", line)
    return result

def image_check(line: str) -> str:
    regex = r"\!\[(?P<alt>[^\]]*)\]\((?P<path>[^\)]*)\)"
    result = re.sub(regex, lambda match:f"<img src=\'{match.group('path')}\' alt=\'{match.group('alt')}\'/>", line)
    return result

def paragraph_check(line: str) -> str:
    if line == "":
        line = "<p>\n"
    return line


def ordered_lists_check(line: str, html: list[str]) -> str:
    regex = r"^ {0,3}\d+\. (?P<content>.*)$"
    match = re.match(regex, line)
    li_before = "<li>" in html[-1] if html else False
    if match:
        result = ""
        if not li_before:
            result += "<ol>\n"
        result += f"<li>{match.group('content')}</li>\n"
    elif li_before:
        result = "<ol>\n" + line
    else:
        result = None
    return result

def last_ol_tag(html: list[str]):
    if "<li>" in html[-1]:
        html[-1] += "</ol>"

def handle_line(line: str, html: list[str]):
    result = line
    result_header = header_check(result)
    if result_header:
        result = result_header
    result = bold_check(result)
    result = italic_check(result)
    result = image_check(result)
    result = url_check(result)
    result_ordered = ordered_lists_check(line, html)
    if result_ordered:
        result = result_ordered
    result = paragraph_check(result)
    html.append(result)
    

def write_html(html: list[str], filename: str):
    file = open(filename, "w" ,encoding="utf-8")
    for line in html:
        file.write(line)
    file.close()


def main (filename: str):
    html = []
    for line in sys.stdin:
        handle_line(line.strip(), html)
    last_ol_tag(html)
    write_html(html, filename)


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "result.html")