"""Read-only target-card discovery and short paper locators, not whole stores."""
import json
from pathlib import Path
import sqlite3

HERE = Path(__file__).resolve().parents[1]
store = Path('~/math-brain-build/local/population/brain.sqlite3')
if store.is_file():
    with sqlite3.connect(store.as_uri() + '?mode=ro', uri=True) as db:
        db.execute('PRAGMA query_only=ON')
        tables = db.execute("SELECT name FROM sqlite_master WHERE type='table'").fetchall()
        schema = {}
        for (name,) in tables:
            if name in ('nodes', 'cards', 'theorems', 'sources', 'statements'):
                schema[name] = [dict(zip(('cid','name','type','notnull','default','pk'), row))
                                for row in db.execute('PRAGMA table_info(' + name + ')')]
        print(json.dumps({'read_only_store': str(store), 'candidate_schemas': schema}, indent=2))

try:
    import pypdf
except ImportError:
    print('PYPDF_UNAVAILABLE: mathematical preprint stays unverified')
else:
    pdf = HERE / 'sources' / 'claimed_resolution.pdf'
    if pdf.is_file():
        reader = pypdf.PdfReader(str(pdf))
        locators = []
        for number, page in enumerate(reader.pages, 1):
            text = page.extract_text() or ''
            lines = text.splitlines()
            matches = []
            for index, line in enumerate(lines):
                if any(term in line.lower() for term in ('theorem 1.', 'operator surgery', 'contraction', 'coerciv', 'lemma 4.', 'lemma 5.', 'lemma 6.')):
                    matches.append({'line': index + 1, 'text': ' '.join(lines[max(0,index-1):index+2])[:450]})
            if matches:
                locators.append({'page': number, 'matches': matches[:8]})
        (HERE / 'PREPRINT_LOCATORS.json').write_text(json.dumps({'pages': len(reader.pages), 'locators': locators}, indent=2), encoding='utf-8')
        print(json.dumps({'preprint_pages': len(reader.pages), 'locators': locators}, indent=2))
