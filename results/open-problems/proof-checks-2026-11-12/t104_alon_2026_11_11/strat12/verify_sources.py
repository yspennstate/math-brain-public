"""Exact source fingerprints: no inherited source may change during this run."""
import hashlib,json
from pathlib import Path

HERE=Path(__file__).resolve().parent

def main():
    hashes=json.loads((HERE/'source_hashes.json').read_text())
    for name,digest in hashes.items():
        assert hashlib.sha256((HERE/name).read_bytes()).hexdigest()==digest,name
    actual={str(p.relative_to(HERE)) for folder in ('STRAT10','STRAT11')
            for p in (HERE/folder).rglob('*') if p.is_file()}
    assert actual==set(hashes),('Source file set changed',actual-set(hashes),set(hashes)-actual)
    print('PROVED (verify_sources.py): all',len(hashes),'inherited source files unchanged.')
    if (HERE/'provenance.json').exists():
        for name,digest in json.loads((HERE/'provenance.json').read_text()).items():
            assert hashlib.sha256((HERE/name).read_bytes()).hexdigest()==digest,name
        print('PROVED (verify_sources.py): STRAT12 proof code and certificate fingerprints matched.')

if __name__=='__main__':main()
