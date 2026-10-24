from pathlib import Path
import concurrent.futures
import hashlib
import json
import urllib.request
import zipfile
import io

root = Path(__file__).resolve().parent
pin = 'cd090736b8f5984d49926e80363910e7c6441a4f'
base = 'https://raw.githubusercontent.com/nitromannitol/percolation-after-anthropic/' + pin + '/'
queries = {
    'pinned_actual_tree': 'https://api.github.com/repos/nitromannitol/percolation-after-anthropic/git/trees/2a3d2c7bf05adf43607606504ab0911937d394ae?recursive=1',
    'pinned_comparator_archive': 'https://api.github.com/repos/nitromannitol/percolation-after-anthropic/actions/artifacts/11594280278/zip',
    'pinned_principal_receipt': base + 'verification/principal-statements.txt',
    'pinned_acceptance_receipt': base + 'verification/site-acceptance.txt',
    'pinned_build_receipt': base + 'verification/build.txt',
    'pinned_compiler_audit': base + 'scripts/Audit.lean',
}

def fetch(item):
    key, url = item
    record = {'date': '2026-10-11', 'request': key, 'url': url}
    try:
        with urllib.request.urlopen(urllib.request.Request(url, headers={'User-Agent': 'G0001-proof-audit/1.0'}), timeout=25) as response:
            data = response.read(8 * 1024 * 1024 + 1)
        if len(data) > 8 * 1024 * 1024:
            raise ValueError('8 MiB response cap exceeded')
        extension = '.zip' if key.endswith('archive') else '.txt'
        (root / (key + extension)).write_bytes(data)
        record.update(bytes=len(data), sha256=hashlib.sha256(data).hexdigest())
    except Exception as exc:
        record['error'] = str(exc)
    return record

with concurrent.futures.ThreadPoolExecutor(max_workers=6) as executor:
    for record in executor.map(fetch, queries.items()):
        with (root / 'pinned_request_log.jsonl').open('a', encoding='utf8') as output:
            output.write(json.dumps(record) + '\n')
        print(record, flush=True)

archive = root / 'pinned_comparator_archive.zip'
if archive.exists():
    data = archive.read_bytes()
    digest = hashlib.sha256(data).hexdigest()
    expected = '629af5a39b25d67a9ef8f536cb78ccba2628c9554a325fb825c91d4f2aa31def'
    print('Artifact SHA256 matches advertised digest:', digest == expected, flush=True)
    with zipfile.ZipFile(io.BytesIO(data)) as zipped:
        inventory = [{'name': info.filename, 'bytes': info.file_size} for info in zipped.infolist()]
        (root / 'pinned_artifact_inventory.json').write_text(json.dumps(inventory, indent=2), encoding='utf8')
        print('ARTIFACT INVENTORY', json.dumps(inventory), flush=True)
        # Read only the percolation comparator report, not arbitrary CI environment output.
        for info in zipped.infolist():
            name = info.filename.lower()
            if 'site' in name and info.file_size <= 2 * 1024 * 1024 and name.endswith(('.txt', '.log')):
                output_name = 'artifact_' + Path(info.filename).name
                (root / output_name).write_bytes(zipped.read(info))
                print('Saved site comparator report', output_name, flush=True)

if (root / 'pinned_actual_tree.txt').exists():
    tree = json.loads((root / 'pinned_actual_tree.txt').read_text())
    (root / 'pinned_tree_identity.json').write_text(json.dumps({
        'commit': pin, 'commit_declared_tree': '2a3d2c7bf05adf43607606504ab0911937d394ae',
        'actual_tree_response_sha': tree.get('sha'), 'entry_count': len(tree.get('tree', [])),
        'truncated': tree.get('truncated')}, indent=2), encoding='utf8')
    print('Actual pinned tree response:', tree.get('sha'), flush=True)
