"""Bounded grep and context reads of only the packet's cached papers."""
import collections
import json
import pathlib
import re
import subprocess

ROOT = pathlib.Path('~/Downloads/Probability_1000_20h_20260906/sources')
HERE = pathlib.Path(__file__).resolve().parent
jobs = [
    ('beta_splitting_overview', r'Ansatz|harmonic descent|transition prob|q_n|q\(n|Problem 8', 24),
    ('lyons_determinantal_2014', r'commut|L1|L¹|1/3|d.bar|¯d', 16),
    ('free_unimodality_journal_2018', r'Problem 4.6|mode|ψt|vt\(|v_t|Theorem 3.2|Theorem 4.1', 23),
    ('biskup_dgff_extrema_2020', r'Problem 16.4|infinite mean|infinite expectation|infinite first|total mass|ρD', 19),
    ('randomstrasse_2025_v1', r'14.2|Conjecture 31|graph matr|overlap|Rademacher', 13),
    ('lyons_peres_20260819', r'Question 10.28|Tail Triviality|tail triviality|infinite orbit', 15),
]
out = []
for topic, expression, limit in jobs:
    path = ROOT / topic / 'text.txt'
    query = subprocess.run(['rg', '-n', '-i', '-e', expression, str(path)], capture_output=True, text=True, encoding='utf-8', errors='replace', timeout=30)
    matches = []
    for line in query.stdout.splitlines():
        number, sep, text = line.partition(':')
        if sep and number.isdigit():
            matches.append((int(number), text))
    if not matches:
        # STUCK: shell pattern searches twice returned no matches despite intact cached texts.
        # Fall back to a streaming regex grep; still read only matching context windows.
        pattern = re.compile(expression, re.IGNORECASE)
        with path.open(encoding='utf-8') as file:
            matches = [(i, line.rstrip()) for i, line in enumerate(file, 1) if pattern.search(line)]
    selected = matches[:limit]
    wanted = {j for i, _ in selected for j in range(max(1, i-4), i+7)}
    snippet = []
    with path.open(encoding='utf-8') as file:
        for i, line in enumerate(file, 1):
            if i in wanted:
                snippet.append(f'{i}: {line.rstrip()}')
            if wanted and i > max(wanted):
                break
    block = {'topic': topic, 'path': str(path), 'grep_match_count': len(matches), 'selected_match_count': len(selected), 'lines': snippet}
    out.append(block)
    print(json.dumps(block, ensure_ascii=False))
(HERE / 'source_excerpts.json').write_text(json.dumps(out, indent=2, ensure_ascii=False), encoding='utf-8')
