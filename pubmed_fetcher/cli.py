import click
from pubmed_fetcher.api import fetch_pubmed_ids, fetch_paper_details, save_to_csv

@click.command()
@click.argument("query")
@click.option("-d", "--debug", is_flag=True, help="Print debug information")
@click.option("-f", "--file", type=click.Path(), help="Save results to a CSV file")
def main(query, debug, file):
    """Fetch PubMed papers based on a query."""
    if debug:
        click.echo(f"Searching PubMed for: {query}")

    pubmed_ids = fetch_pubmed_ids(query)
    if debug:
        click.echo(f"Found PubMed IDs: {pubmed_ids}")

    papers = fetch_paper_details(pubmed_ids)
    
    if file:
        save_to_csv(papers, file)
        click.echo(f"Results saved to {file}")
    else:
        click.echo(papers)

if __name__ == "__main__":
    main()
