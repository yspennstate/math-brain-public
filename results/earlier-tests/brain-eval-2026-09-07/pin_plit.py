"""Capture local PLIT source bytes without changing the experiment.

Private evidence; never add output to the code branch. Re-running refuses to
overwrite the evidence tree. SHA-256 is checked immediately after each copy.
"""
from pathlib import Path
import argparse
import hashlib
import json
from datetime import datetime, timezone


def main():
    p = argparse.ArgumentParser()
    p.add_argument('--campaign', type=Path, required=True)
    p.add_argument('--keys', type=Path, required=True)
    p.add_argument('--output', type=Path, required=True)
    a = p.parse_args()
    a.output.mkdir(parents=True, exist_ok=False)
    manifest = []
    def pin(src, rel):
        data = src.read_bytes()
        dst = a.output / rel
        dst.parent.mkdir(parents=True, exist_ok=True)
        with dst.open('xb') as f:
            f.write(data)
        digest = hashlib.sha256(data).hexdigest()
        if hashlib.sha256(dst.read_bytes()).hexdigest() != digest:
            raise RuntimeError('Snapshot copy mismatch')
        manifest.append({'subject': str(src.resolve()), 'evidence': str(dst.resolve()),
                         'sha256': digest, 'bytes': len(data),
                         'observed_at': datetime.now(timezone.utc).isoformat()})
    pin(a.keys, 'plit_keys.jsonl')
    for name in ('PROTOCOL_PLIT.md', 'STAGE1_SIZING.json', 'BUILD_REPORT.json',
                 'grade_plit.py', 'grade_plit_check.py', 'stage1.py', 'DEFECTS.json',
                 'VALIDITY_REVIEW.json', 'VALIDITY_REVIEW_C.json', 'VALIDITY_REVIEW_D.json',
                 'plit_notes_bm25.py', 'run_plit_wrapper.py', 'items/plit.jsonl'):
        pin(a.campaign / name, name)
    for name in ('run_plit_s1_haiku', 'run_plit_s1_opus', 'run_plit_haiku', 'run_plit_opus'):
        run = a.campaign / name
        pin(run / 'SAMPLE.json', name + '/SAMPLE.json')
        for src in sorted((run / 'verdicts').rglob('*.json')):
            pin(src, src.relative_to(a.campaign))
        if '_s1_' in name:
            for file in ('brain_notes.json', 'placebo_notes.json', 'results/STAGE1.json', 'results/STAGE1.md'):
                pin(run / file, name + '/' + file)
    (a.output / 'MANIFEST.json').write_text(json.dumps(manifest, indent=2) + '\n', encoding='utf-8')
    print(json.dumps({'files': len(manifest), 'bytes': sum(r['bytes'] for r in manifest),
                      'manifest_sha256': hashlib.sha256((a.output / 'MANIFEST.json').read_bytes()).hexdigest()}))


if __name__ == '__main__':
    main()
