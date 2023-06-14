import requests
from  bs4 import BeautifulSoup

def get_citations_needed_count(URL):
    response = requests.get(URL)
    soup = BeautifulSoup(response.content, 'html.parser')
    all_citation_needed = soup.find_all('sup', class_="noprint Inline-Template Template-Fact")
    print (len(all_citation_needed))
    return len(all_citation_needed)

get_citations_needed_count('https://en.wikipedia.org/wiki/Anglo-Iraqi_War')

def get_citations_needed_report(URL):
    response = requests.get(URL)
    soup = BeautifulSoup(response.text, 'html.parser')
    all_citation_needed = soup.find_all('sup', class_='noprint Inline-Template Template-Fact')
    report = ""
    for citation in all_citation_needed:
        parent_text = citation.find_parent('p').text.strip()
        report += f"Citation needed for: {parent_text}\n\n"
    print (report)
    return report

get_citations_needed_report('https://en.wikipedia.org/wiki/Anglo-Iraqi_War')