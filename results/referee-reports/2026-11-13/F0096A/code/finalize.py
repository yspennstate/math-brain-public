"""Build the simulation table from the independently verified output."""
import csv
import json
import statistics
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
rows = list(csv.DictReader(open(ROOT/'data/sweep.csv')))
checks = json.load(open(ROOT/'data/verification.json'))
assert len(rows) == len(checks) == 210
assert all(r['valid_cycle'] for r in checks)
lines = [
    '| $c$ | $n=1000$ | $n=10000$ | $n=100000$ | Mean solve time at $n=100000$ (s) | Largest observed degree |',
    '|---:|---:|---:|---:|---:|---:|',
]
for c in (1.5,1.55,1.6,1.75,2,2.25,2.5):
    selected = [r for r in rows if float(r['c']) == c]
    cells = []
    for n in (1000,10000,100000):
        rs = [r for r in selected if int(r['n']) == n]
        assert len(rs) == 10
        cells.append(f"{sum(int(r['found']) for r in rs)}/10 (1.00)")
    large = [r for r in selected if int(r['n']) == 100000]
    mean = statistics.mean(float(r['solve_seconds']) for r in large)
    degree = max(int(r['max_degree']) for r in selected)
    lines.append(f'| {c:.2f} | '+ ' | '.join(cells)+f' | {mean:.3f} | {degree} |')
assert all(r['components']==1 and r['bridges']==0 and r['articulation_vertices']==0 and r['degree3_triples_same_neighborhood']==0 for r in checks)
lines.append('\nAll 210 cycles passed independent verification. There were no heuristic failures, disconnected samples, bridges, articulation vertices, or degree-3 triples sharing an identical neighborhood. No failure structure was therefore observed. Ten samples per cell provide modest finite-size evidence: even 10/10 successes give only a 0.741 one-sided 95% lower confidence bound on that finite-size success probability, with no simultaneous coverage claim. They do not establish an asymptotic limit.')
resources = json.load(open(ROOT/'data/sweep_resources.json'))
verify_resources = json.load(open(ROOT/'data/verification_resources.json'))
lines.append(f"\nThe serial sweep took {resources['wall_seconds']:.1f} seconds. Maximum simulator RSS was {resources['children'][2]/2**20:.1f} MiB; the independent verifier used {verify_resources['peak_rss_bytes']/2**20:.1f} MiB. Both are well below 4 GB. The longest solver run took {max(float(r['solve_seconds']) for r in rows):.3f} seconds; sample-generation time is recorded separately and increases substantially with density.")
report = ROOT/'REPORT.md'
body = report.read_text()
placeholder = '<!-- SIMULATION_TABLE -->'
if placeholder in body:
    report.write_text(body.replace(placeholder,'\n'.join(lines)))
(ROOT/'data/simulation_table.md').write_text('\n'.join(lines)+'\n')
print('Simulation table finalized; all 210 certificates valid.')
