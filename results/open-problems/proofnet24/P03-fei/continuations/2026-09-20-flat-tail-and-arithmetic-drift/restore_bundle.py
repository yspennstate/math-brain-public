#!/usr/bin/env python3
"""Verify and restore the exact FEI scientific source bundle; standard library only.

Run from a checkout: python restore_bundle.py --output /path/to/new/directory
Use --verify-only to check the capsule without writing any scientific files.
The destination must not exist. Nothing in the repository is overwritten.
"""
from __future__ import annotations
import argparse
import base64
import hashlib
import json
import lzma
from pathlib import Path, PurePosixPath


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def safe_name(name: str) -> PurePosixPath:
    if not isinstance(name, str) or not name or '\\' in name:
        raise ValueError(f'Invalid source path: {name!r}')
    path = PurePosixPath(name)
    if path.is_absolute() or '..' in path.parts or str(path) != name:
        raise ValueError(f'Unsafe or noncanonical source path: {name!r}')
    return path


def verified_sources(root: Path) -> dict[str, bytes]:
    manifest = json.loads((root / 'BUNDLE_MANIFEST.json').read_text(encoding='utf-8'))
    encoded = []
    for part in manifest['parts']:
        path = root.joinpath(*safe_name(part['path']).parts)
        data = path.read_bytes()
        if len(data) != part['bytes'] or sha256(data) != part['sha256']:
            raise ValueError(f'Part hash/size mismatch: {part["path"]}')
        git = hashlib.sha1(b'blob ' + str(len(data)).encode('ascii') + b'\0' + data).hexdigest()
        if git != part['git_blob_sha']:
            raise ValueError(f'Git blob mismatch: {part["path"]}')
        encoded.append(b''.join(data.split()))
    compressed = base64.b64decode(b''.join(encoded), validate=True)
    if len(compressed) != manifest['compressed_bytes'] or sha256(compressed) != manifest['compressed_sha256']:
        raise ValueError('Compressed source hash/size mismatch')
    decoder = lzma.LZMADecompressor(memlimit=256 * 1024 * 1024)
    raw = decoder.decompress(compressed, max_length=10 * 1024 * 1024)
    if not decoder.eof or decoder.unused_data:
        raise ValueError('Oversized, incomplete, or concatenated source capsule')
    text_sources = json.loads(raw.decode('utf-8'))
    if not isinstance(text_sources, dict) or len(text_sources) != manifest['source_files']:
        raise ValueError('Unexpected source count/format')
    sources: dict[str, bytes] = {}
    for name, text in text_sources.items():
        safe_name(name)
        if not isinstance(text, str):
            raise ValueError(f'Nontext source: {name}')
        sources[name] = text.encode('utf-8')
    scientific = json.loads(sources['SCIENCE_MANIFEST.json'].decode('utf-8'))
    entries = scientific['files']
    expected = {entry['path'] for entry in entries}
    if len(expected) != len(entries) or set(sources) != expected | {'SCIENCE_MANIFEST.json'}:
        raise ValueError('Scientific manifest does not enumerate the exact source set')
    for entry in entries:
        data = sources[entry['path']]
        if len(data) != entry['bytes'] or sha256(data) != entry['sha256']:
            raise ValueError(f'Scientific source hash/size mismatch: {entry["path"]}')
    return sources


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, help='New destination directory (must not exist)')
    parser.add_argument('--verify-only', action='store_true')
    args = parser.parse_args()
    root = Path(__file__).resolve().parent
    sources = verified_sources(root)
    if args.verify_only:
        print(json.dumps({'status': 'PASS', 'verified_source_files': len(sources), 'written': False}, indent=2))
        return
    target = (args.output or (root / 'restored_sources')).absolute()
    if target.exists() or target.is_symlink():
        raise FileExistsError(f'Refusing existing destination: {target}')
    target.mkdir(parents=True, exist_ok=False)
    for name, data in sources.items():
        dest = target.joinpath(*safe_name(name).parts)
        dest.parent.mkdir(parents=True, exist_ok=True)
        with dest.open('xb') as handle:
            handle.write(data)
    print(json.dumps({'status': 'PASS', 'verified_source_files': len(sources), 'output': str(target)}, indent=2))


if __name__ == '__main__':
    main()
