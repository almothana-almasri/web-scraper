import requests
from bs4 import BeautifulSoup

def get_citations_needed_count(URL):
    """
    Retrieves the number of citations needed for a given Wikipedia page.

    Args:
        URL (str): The URL of the Wikipedia page.

    Returns:
        int: The count of citations needed.
    """
    response = requests.get(URL)
    soup = BeautifulSoup(response.content, 'html.parser')
    all_citation_needed = soup.find_all('sup', class_='noprint Inline-Template Template-Fact')
    number_of_citations = len(all_citation_needed)
    print(f"Number of citations needed in the History of Mexico page = {number_of_citations}\n")
    return len(all_citation_needed)

get_citations_needed_count('https://en.wikipedia.org/wiki/History_of_Mexico')

def get_citations_needed_report(URL):
    """
    Generates a report of the passages that require citations for a given Wikipedia page.

    Args:
        URL (str): The URL of the Wikipedia page.

    Returns:
        str: The report string containing the relevant passages.
    """
    response = requests.get(URL)
    soup = BeautifulSoup(response.text, 'html.parser')
    all_citation_needed = soup.find_all('sup', class_='noprint Inline-Template Template-Fact')
    report = ""
    for citation in all_citation_needed:
        parent_text = citation.find_parent('p').text.strip()
        report += f"Citation needed for: {parent_text}\n\n"
    print(report)
    return report

get_citations_needed_report('https://en.wikipedia.org/wiki/History_of_Mexico')