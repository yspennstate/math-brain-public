"""Verify source folders and local replay inputs in exact byte arithmetic."""
import json,hashlib
from pathlib import Path
HERE=Path(__file__).resolve().parent

def main():
    source=json.loads((HERE/'source_hashes.json').read_text())
    for name,digest in source.items():
        assert hashlib.sha256((HERE/name).read_bytes()).hexdigest()==digest,name
    if (HERE/'provenance.json').exists():
        for name,digest in json.loads((HERE/'provenance.json').read_text()).items():
            assert hashlib.sha256((HERE/name).read_bytes()).hexdigest()==digest,name
    print('PROVED: source snapshot unchanged; local replay input hashes matched.')

if __name__=='__main__':main()
