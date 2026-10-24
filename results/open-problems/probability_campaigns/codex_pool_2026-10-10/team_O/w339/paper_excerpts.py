import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SOURCE_GROUPS = [
    (Path('~/Downloads/Probability_1000_20h_20260906'), {
        'agresti_veraar_spde_journal_2025': ['Theorem 6.4', 'Problem 5.', 'Assumption 6.1'],
        'tree_automata_2019': ['randomiz', 'endogen'],
        'queues_computing_frontiers_2021': ['7.3', 'provision'],
        'grimmett_2022_selected': ['Question 6.1', 'diffus'],
        'lyons_peres_20260819': ['Conjecture 4.10'],
    }),
    (Path('~/Downloads/Probability_1000_intake_claude_20260907'), {
        'bordenave_chafai_circular_2012': ['6.6.', 'almost surely'],
        'kosygina_zerner_erw_2012': ['Theorem 5.2', 'Problem 5.3', '(POS1)'],
        'drewitz_ramirez_rwre_2014': ['Corollary 2.15', 'Open question 2.19'],
        'heydenreich_hofstad_highd_2017': ['Open Problem 15.5'],
        'chatterjee_chaos_2008': ['without the nonneg', 'non-negative', 'second moment'],
    }),
]
ledger_roots = [SOURCE_GROUPS[0][0], Path('~/<private-repo>/06_math_research/probability_1000_intake_claude_20260907')]
sections = []
for (cache, patterns), ledger_root in zip(SOURCE_GROUPS, ledger_roots):
    rows = {}
    path = ledger_root / 'sources.jsonl'
    with path.open(encoding='utf-8') as stream:
        for line in stream:
            item = json.loads(line)
            if item.get('source_id') in patterns:
                rows[item['source_id']] = item
    for sid, needles in patterns.items():
        row = rows.get(sid)
        if row is None:
            sections.append(f'## {sid}\nSOURCE LEDGER ROW NOT FOUND\n')
            continue
        rel = row.get('text_relative_to_downloads') or row.get('text_path') or row.get('extracted_path')
        if rel:
            textpath = Path(rel)
            if not textpath.is_absolute():
                textpath = cache / rel
        else:
            textpath = cache / 'sources' / sid / 'text.txt'
        sections.append(f'## {sid}\n{json.dumps(row,ensure_ascii=False)}\nTEXT: {textpath}\n')
        if not textpath.exists():
            sections.append('TEXT NOT FOUND\n')
            continue
        lines = textpath.read_text(encoding='utf-8',errors='replace').splitlines()
        for needle in needles:
            hits = [i for i,line in enumerate(lines) if needle.casefold() in line.casefold()]
            if needle in ('almost surely', 'randomiz', 'endogen', 'diffus', 'second moment', 'non-negative'):
                hits = hits[-2:]
            else:
                hits = hits[:2]
            if not hits:
                sections.append(f'NO LITERAL MATCH: {needle}\n')
            for index in hits:
                fragment = '\n'.join(f'{i+1}: {lines[i]}' for i in range(max(0,index-4),min(len(lines),index+23)))
                sections.append(f'MATCH {needle}\n{fragment}\n')
report = '\n'.join(sections)
ROOT.joinpath('source_excerpt_report.md').write_text(report,encoding='utf-8')
print(report)
