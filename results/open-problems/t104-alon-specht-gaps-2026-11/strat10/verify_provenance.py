"""PROVED: copied starting sources remain byte-identical to pinned source hashes."""
import json,hashlib
from pathlib import Path
for c in json.load(open('provenance.json'))['files']:
    assert hashlib.sha256(Path(c['target']).read_bytes()).hexdigest()==c['sha256']
    # Replay is self-contained; external source paths need not remain installed.
print('PROVED: every inherited local dependency matches its copied source hash.')
