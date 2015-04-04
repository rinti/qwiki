import click
import requests

SEARCH_URL = 'http://en.wikipedia.org/w/api.php?continue=&action=query&titles={search}' +\
             '&prop=extracts&exintro=&explaintext=&format=json&redirects'


@click.command()
@click.argument('search')
def cli(search):
    s = requests.get(SEARCH_URL.format(search=search)).json()
    pages = s['query']['pages']
    page_id = pages.keys()[0]
    if int(page_id) > -1:
        click.echo(pages[page_id]['title'])
        click.echo(pages[page_id]['extract'])
    else:
        click.echo('Didn\'t find anything.')
