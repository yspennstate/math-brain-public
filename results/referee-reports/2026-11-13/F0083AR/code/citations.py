"""Independent forward-citation metadata query, preserving provenance."""
import datetime
import json
import pathlib
import urllib.parse
import urllib.request

ROOT = pathlib.Path(__file__).resolve().parents[1]
def get(url):
    request = urllib.request.Request(url, headers={'User-Agent': 'Mathematical independent referee literature check'})
    with urllib.request.urlopen(request, timeout=60) as response:
        return json.load(response)

target = get('https://api.openalex.org/works/https://doi.org/10.1214/009117906000000098')
identifier = target['id'].rsplit('/', 1)[-1]
cursor = '*'
records = []
urls = []
while cursor:
    query = urllib.parse.urlencode({'filter': f'cites:{identifier},from_publication_date:2006-01-01,to_publication_date:2026-11-13', 'per-page':200, 'cursor':cursor})
    url = 'https://api.openalex.org/works?'+query
    urls.append(url)
    page = get(url)
    records.extend(page['results'])
    cursor = page['meta'].get('next_cursor') if page['results'] else None
result = {'queried_at':datetime.datetime.now().astimezone().isoformat(), 'target':target, 'query_urls':urls, 'records':records}
(ROOT/'data'/'independent_citations.json').write_text(json.dumps(result, indent=2)+'\n')
lines = [f'Queried {result["queried_at"]}', f'Target: {target["id"]} {target["display_name"]}', *urls, f'Records: {len(records)}', '']
for item in sorted(records, key=lambda item:(item['publication_year'], item['display_name'])):
    lines.extend([f'{item["publication_year"]}: {item["display_name"]}', '; '.join(author['author']['display_name'] for author in item['authorships']), str(item.get('doi')), str(item.get('best_oa_location'))])
    abstract = item.get('abstract_inverted_index')
    if abstract:
        positions = {position:word for word, indices in abstract.items() for position in indices}
        lines.append('ABSTRACT: '+' '.join(positions[i] for i in sorted(positions)))
    lines.append('')
(ROOT/'sources'/'independent_forward_citations.txt').write_text('\n'.join(lines)+'\n')
print(f'{len(records)} records, {sum(bool(x.get("abstract_inverted_index")) for x in records)} abstracts')
