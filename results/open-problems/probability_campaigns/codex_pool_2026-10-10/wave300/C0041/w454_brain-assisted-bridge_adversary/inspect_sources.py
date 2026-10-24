"""Targeted, read-only source inspection; all saved evidence stays in this folder."""
from pathlib import Path
import importlib.util
import json
import sqlite3
import subprocess
import urllib.request

ROOT = Path(__file__).resolve().parent
research = Path('~/<private-repo>/06_math_research')
evidence = {}
for directory in sorted(research.glob('probability_1000_intake_*')):
    for name in ('problems.jsonl', 'attempts.jsonl'):
        candidate = directory / name
        if not candidate.exists():
            continue
        found = subprocess.run(['rg', '-n', '"problem_id"\\s*:\\s*"C0041"', str(candidate)], capture_output=True, text=True, encoding='utf-8', timeout=30)
        if found.stdout.strip():
            evidence[str(candidate)] = found.stdout.strip().splitlines()
store_path = Path('~/math-brain-build/local/population/brain.sqlite3')
if store_path.exists():
    with sqlite3.connect(store_path.as_uri()+'?mode=ro', uri=True, timeout=3) as connection:
        tables = connection.execute("SELECT name FROM sqlite_master WHERE type='table' AND name NOT LIKE '%test%' AND name NOT LIKE '%eval%'").fetchall()
        evidence['store_tables'] = tables
        evidence['store_schema'] = {}
        for (table,) in tables:
            if table in ('entries', 'cards', 'nodes', 'sources', 'relations'):
                evidence['store_schema'][table] = connection.execute('PRAGMA table_info("'+table+'")').fetchall()
public_sources = {
    'new_preprint.pdf': 'https://raw.githubusercontent.com/openai/math/main/preprints/Directional-transience-implies-ballisticity-September-23-2026/paper.pdf',
    'DirectionalBallisticity.lean': 'https://raw.githubusercontent.com/openai/math/main/lean/ComparatorChallenges/DirectionalBallisticity.lean',
    'DirectionalBallisticity.json': 'https://raw.githubusercontent.com/openai/math/main/lean/ComparatorChallenges/DirectionalBallisticity.json',
}
for filename, url in public_sources.items():
    try:
        request = urllib.request.Request(url, headers={'User-Agent': 'C0041-source-review'})
        with urllib.request.urlopen(request, timeout=25) as response:
            data = response.read(2_000_000)
        (ROOT/filename).write_bytes(data)
        evidence[filename] = {'url': url, 'bytes': len(data)}
    except Exception as exc:
        evidence[filename] = {'url': url, 'error': type(exc).__name__+': '+str(exc)}
pdf_path = ROOT/'new_preprint.pdf'
if pdf_path.exists() and importlib.util.find_spec('fitz'):
    import fitz
    with fitz.open(pdf_path) as document:
        evidence['preprint_pages'] = len(document)
        selected = {}
        # Search first, then retain only exact statement / critical bridge pages.
        terms = ('Theorem 1.1', 'Theorem 1.2', 'Proposition 1.3', 'uniform integrability', 'finite mean', 'integrability')
        matches = []
        for number in range(len(document)):
            page_text = document[number].get_text()
            hits = [term for term in terms if term.lower() in page_text.lower()]
            if hits:
                matches.append({'page': number+1, 'terms': hits})
                if len(selected) < 5:
                    selected[str(number+1)] = page_text
        selected.setdefault('1', document[0].get_text())
        evidence['preprint_term_matches'] = matches
        (ROOT/'preprint_selected_pages.json').write_text(json.dumps(selected, ensure_ascii=False, indent=2), encoding='utf-8')
        evidence['selected_preprint_pages'] = sorted(selected, key=int)
(ROOT/'source_inspection.json').write_text(json.dumps(evidence, ensure_ascii=False, indent=2), encoding='utf-8')
print(json.dumps(evidence, ensure_ascii=False, indent=2))
