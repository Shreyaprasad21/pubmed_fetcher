import requests
import re
import pandas as pd
from typing import List, Dict, Optional

PUBMED_API_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
PUBMED_SUMMARY_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi"
PUBMED_FETCH_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi"

# Define heuristics for non-academic author detection
NON_ACADEMIC_KEYWORDS = ["pharma", "biotech", "inc", "corp", "gmbh", "ltd", "co.", "company"]

def fetch_pubmed_ids(query: str) -> List[str]:
    """Fetch PubMed IDs matching the query."""
    params = {
        "db": "pubmed",
        "term": query,
        "retmode": "json",
        "retmax": 10  # Fetch up to 10 results for testing
    }
    response = requests.get(PUBMED_API_URL, params=params)
    response.raise_for_status()
    return response.json()["esearchresult"]["idlist"]

def fetch_paper_details(pubmed_ids: List[str]) -> List[Dict[str, str]]:
    """Fetch detailed metadata for given PubMed IDs."""
    if not pubmed_ids:
        return []
    
    params = {
        "db": "pubmed",
        "id": ",".join(pubmed_ids),
        "retmode": "xml"
    }
    response = requests.get(PUBMED_FETCH_URL, params=params)
    response.raise_for_status()
    return parse_pubmed_xml(response.text)

def parse_pubmed_xml(xml_data: str) -> List[Dict[str, str]]:
    """Extract required details from PubMed XML data."""
    import xml.etree.ElementTree as ET
    
    root = ET.fromstring(xml_data)
    papers = []

    for article in root.findall(".//PubmedArticle"):
        pubmed_id = article.findtext(".//PMID")
        title = article.findtext(".//ArticleTitle")
        pub_date = article.findtext(".//PubDate/Year")
        authors = article.findall(".//Author")

        non_academic_authors = []
        company_affiliations = []
        corresponding_author_email = None

        for author in authors:
            last_name = author.findtext("LastName", default="Unknown")
            first_name = author.findtext("ForeName", default="")
            full_name = f"{first_name} {last_name}".strip()
            affiliation = author.findtext(".//Affiliation", default="")

            if any(kw in affiliation.lower() for kw in NON_ACADEMIC_KEYWORDS):
                non_academic_authors.append(full_name)
                company_affiliations.append(affiliation)

            if re.search(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b", affiliation):
                corresponding_author_email = re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}", affiliation)[0]

        papers.append({
            "PubmedID": pubmed_id,
            "Title": title,
            "Publication Date": pub_date,
            "Non-academic Author(s)": ", ".join(non_academic_authors),
            "Company Affiliation(s)": ", ".join(company_affiliations),
            "Corresponding Author Email": corresponding_author_email or "N/A"
        })

    return papers

def save_to_csv(papers: List[Dict[str, str]], filename: str):
    """Save results to a CSV file."""
    df = pd.DataFrame(papers)
    df.to_csv(filename, index=False)
