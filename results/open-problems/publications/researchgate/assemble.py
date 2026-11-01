#!/usr/bin/env python3
"""Reassemble a verbatim manuscript from readable source parts.
Usage: python publications/researchgate/assemble.py publications/researchgate/414266816-entropy-singularity
Python 3.9+; standard library only. Does not compile or modify an existing different main.tex.
"""
import argparse
import hashlib
import json
from pathlib import Path


def git_blob_sha(data: bytes) -> str:
    header = f'blob {len(data)}\0'.encode('ascii')
    return hashlib.sha1(header + data).hexdigest()


def assemble(folder: Path) -> Path:
    folder = folder.resolve(strict=True)
    manifest = json.loads((folder / 'source_manifest.json').read_text(encoding='utf-8'))
    chunks = []
    for part in manifest['parts']:
        path = (folder / part['path']).resolve(strict=True)
        if folder not in path.parents:
            raise ValueError('Manifest part escapes manuscript directory')
        data = path.read_bytes()
        if len(data) != part['bytes'] or git_blob_sha(data) != part['git_blob_sha']:
            raise ValueError(f'Part integrity check failed: {path.name}')
        chunks.append(data)
    data = b''.join(chunks)
    if (len(data) != manifest['total_bytes']
            or hashlib.sha256(data).hexdigest() != manifest['sha256']
            or git_blob_sha(data) != manifest['git_blob_sha']):
        raise ValueError('Assembled manuscript integrity check failed')
    output = folder / 'main.tex'
    if output.exists():
        if output.read_bytes() != data:
            raise FileExistsError(f'Refusing to overwrite different file: {output}')
    else:
        with output.open('xb') as stream:
            stream.write(data)
    return output


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('folder', type=Path)
    args = parser.parse_args()
    try:
        print(f'Verified complete source: {assemble(args.folder)}')
    except (OSError, ValueError, KeyError, TypeError) as exc:
        parser.exit(1, f'Assembly failed: {exc}\n')


if __name__ == '__main__':
    main()
