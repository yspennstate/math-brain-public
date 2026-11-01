"""Restore substantive recovered source files from a clone's Git objects."""
import argparse
import hashlib
import json
import subprocess
from pathlib import Path

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('destination', type=Path)
parser.add_argument('--repo', type=Path, default=Path.cwd())
args = parser.parse_args()
manifest = json.loads(Path(__file__).with_name('RECOVERY_MANIFEST.json').read_text())
if args.destination.exists():
    raise SystemExit('Use a new destination; existing files are never replaced.')
args.destination.mkdir(parents=True)
count = 0
for row in manifest['files']:
    if row['disposition'] == 'metadata_excluded':
        continue
    relative = Path(row['source'])
    if relative.is_absolute() or '..' in relative.parts:
        raise SystemExit('Unsafe manifest path')
    data = subprocess.run(['git', '-C', str(args.repo), 'cat-file', 'blob', row['git_blob']],
                          check=True, capture_output=True).stdout
    if len(data) != row['bytes'] or hashlib.sha256(data).hexdigest() != row['sha256']:
        raise SystemExit('Hash mismatch: ' + row['source'])
    target = args.destination / relative
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_bytes(data)
    count += 1
print(f'Restored and verified {count} substantive files to {args.destination}')
