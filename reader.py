"""HTML reader

ref: https://beomi.github.io/2017/01/20/HowToMakeWebCrawler/
"""

import sys

from bs4 import BeautifulSoup

def process_file(file_storage, target_selector=None):
    assert target_selector is not None

    soup = BeautifulSoup(file_storage, 'html.parser')
    contents = soup.select(target_selector) # 'div._4t5n > div'

    def print_tags(tags):
        result_string = ''
        for tag in tags:
            result_string += '{}'.format(tag)
        return result_string

    html_string = print_tags(soup)
    contents_string = print_tags(contents)
    reversed_string = print_tags(reversed(contents))
    
    html_string = html_string.replace(contents_string, reversed_string)
    return html_string

def main(argv):
    with open(argv[0]) as fp:
        print(process_file(fp, argv[1]))


if __name__ == "__main__":
    main(sys.argv[1:])
