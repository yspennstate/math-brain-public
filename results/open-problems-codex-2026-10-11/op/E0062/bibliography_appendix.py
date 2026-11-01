import pathlib,json
R=pathlib.Path(__file__).resolve().parent
items={}
for p in list(R.glob('openalex*.response'))+list(R.glob('citing*.response'))+list(R.glob('target_openalex*.response')):
    for w in json.loads(p.read_text(encoding='utf-8')).get('results',[]):
        t=(w.get('title') or '').lower()
        if ('quadratic stochastic' in t and any(s in t for s in ['volterra','ergod','regularity'])) or ('lotka' in t and any(s in t for s in ['operator','mapping','degenerate'])):
            items[w['id']]=w
with (R/'LITERATURE.md').open('a',encoding='utf-8') as f:
    f.write('\n## Additional on-topic bibliographic leads from API results\n\n')
    f.write('The following are metadata leads, not full-text theorem verifications. Duplicated versions can have distinct API identifiers. None is classified as a literature solution.\n\n')
    for w in sorted(items.values(),key=lambda w:(w['publication_year'],w['title'])):
        authors='; '.join(a['author']['display_name'] for a in w.get('authorships',[]))
        f.write(f"- {authors}. *{w['title']}* ({w['publication_year']}). {w.get('doi') or w['id']}.\n")
print('Bibliographic metadata leads appended:',len(items))
