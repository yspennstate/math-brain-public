"""Bounded, read-only public certificate audit. Writes only in this problem folder."""
from pathlib import Path
import concurrent.futures
import hashlib
import json
import time
import urllib.request

ROOT = Path(__file__).resolve().parent
PIN = 'cd090736b8f5984d49926e80363910e7c6441a4f'
BASE = 'https://raw.githubusercontent.com/nitromannitol/percolation-after-anthropic/' + PIN + '/'
REQUESTS = {
    'pinned_commit': 'https://api.github.com/repos/nitromannitol/percolation-after-anthropic/git/commits/' + PIN,
    'pinned_tree': 'https://api.github.com/repos/nitromannitol/percolation-after-anthropic/git/trees/' + PIN + '?recursive=1',
    'pinned_artifacts': 'https://api.github.com/repos/nitromannitol/percolation-after-anthropic/actions/runs/37879691984/artifacts',
    'pinned_jobs': 'https://api.github.com/repos/nitromannitol/percolation-after-anthropic/actions/runs/37879691984/jobs',
    'pinned_releases': 'https://api.github.com/repos/nitromannitol/percolation-after-anthropic/releases?per_page=5',
}
FILES = {
    'pinned_final': 'Hypergraph/FinalCriticality.lean',
    'pinned_assembly': 'Hypergraph/ExactCommonQAssembly.lean',
    'pinned_endgame': 'Hypergraph/SiteEndgame.lean',
    'pinned_model': 'Hypergraph/SiteStatements.lean',
    'pinned_monotonicity': 'Hypergraph/SiteThetaMono.lean',
    'pinned_comparator_workflow': '.github/workflows/comparator.yml',
    'pinned_build_workflow': '.github/workflows/build.yml',
    'pinned_acceptance': 'scripts/acceptance.py',
    'pinned_audit_readme': 'PercolationAudit/README.md',
    'pinned_audit_bridge': 'PercolationAudit/Support/SiteCriticalityBridge.lean',
    'pinned_audit_solution_basic': 'PercolationAudit/SiteCriticality/SolutionBasic.lean',
    'pinned_audit_solution': 'PercolationAudit/SiteCriticality/Solution.lean',
    'pinned_audit_challenge': 'PercolationAudit/SiteCriticality/Challenge.lean',
}
REQUESTS.update({k: BASE + v for k, v in FILES.items()})

def fetch(item):
    key, url = item
    record = {'date': '2026-10-11', 'request': key, 'url': url}
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'G0001-proof-audit/1.0'})
        with urllib.request.urlopen(req, timeout=25) as response:
            data = response.read(8 * 1024 * 1024 + 1)
        if len(data) > 8 * 1024 * 1024:
            raise ValueError('Response exceeds 8 MiB audit cap')
        (ROOT / (key + '.txt')).write_bytes(data)
        record.update(bytes=len(data), sha256=hashlib.sha256(data).hexdigest())
    except Exception as exc:
        record['error'] = str(exc)
    return record

started = time.monotonic()
with concurrent.futures.ThreadPoolExecutor(max_workers=6) as executor:
    for record in executor.map(fetch, REQUESTS.items()):
        with (ROOT / 'pinned_request_log.jsonl').open('a', encoding='utf8') as output:
            output.write(json.dumps(record) + '\n')
        print(record, flush=True)

tree_path = ROOT / 'pinned_tree.txt'
if tree_path.exists():
    tree = json.loads(tree_path.read_text(encoding='utf8'))
    entries = {e['path']: e for e in tree.get('tree', [])}
    checks = []
    for key, path in FILES.items():
        local = ROOT / (key + '.txt')
        if path in entries and local.exists():
            data = local.read_bytes()
            actual = hashlib.sha1(b'blob ' + str(len(data)).encode() + b'\0' + data).hexdigest()
            checks.append({'file': path, 'expected_git_blob_sha': entries[path]['sha'],
                           'actual_git_blob_sha': actual, 'matches': actual == entries[path]['sha']})
    (ROOT / 'pinned_blob_checks.json').write_text(json.dumps(checks, indent=2), encoding='utf8')
    print('BLOB CHECKS', json.dumps(checks), flush=True)
    verification = [e for e in tree.get('tree', []) if e['path'].startswith('verification/')]
    (ROOT / 'pinned_verification_inventory.json').write_text(json.dumps(verification, indent=2), encoding='utf8')
    print('VERIFICATION FILES', '\n'.join(e['path'] for e in verification), flush=True)

print('Audit fetch elapsed seconds', time.monotonic() - started, flush=True)
