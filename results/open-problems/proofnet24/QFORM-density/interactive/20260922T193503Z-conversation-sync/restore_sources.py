"""Restore the 33 text members from an existing local repository, without network.

Usage: python restore_sources.py --repo-root /path/to/math-open-problems --output ./restored
The compiled PDF and original ZIP bytes are not present in this source archive.
No mathematical checker, compiler, workflow, or remote command is executed.
"""
from __future__ import annotations
import argparse
import hashlib
import json
from pathlib import Path, PurePosixPath
import re
import subprocess
import sys


def blob_sha(data: bytes) -> str:
    return hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()


def safe_relative(value: str) -> Path:
    p = PurePosixPath(value)
    if p.is_absolute() or ".." in p.parts or "\\" in value or not p.parts:
        raise ValueError(f"Unsafe relative path: {value!r}")
    return Path(*p.parts)


def restore(manifest: dict, repo: Path, output: Path) -> int:
    repo, output = repo.resolve(), output.resolve()

    def read_source(spec: str) -> bytes:
        key, name = spec.split(":", 1)
        path = safe_relative(name)
        commit = manifest["commits"][key]
        if not re.fullmatch(r"[0-9a-f]{40}", commit):
            raise ValueError("Invalid source commit")
        # A checked-out source suffices; final blob hashes are verified below.
        local = (repo / path).resolve()
        if not local.is_relative_to(repo):
            raise ValueError("Source path escapes the repository")
        if local.is_file():
            return local.read_bytes()
        proc = subprocess.run(
            ["git", "-C", str(repo), "show", f"{commit}:{path.as_posix()}"],
            check=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=30,
        )
        if proc.returncode:
            raise RuntimeError(f"Missing local source {commit}:{name}; use a clone containing the pinned history")
        return proc.stdout

    planned = []
    for package, member, source, expected in manifest["files"]:
        if source == "patch:regularized":
            patch = manifest["patch"]
            data = read_source(patch["base_source"])
            if blob_sha(data) != patch["base_git_blob_sha"]:
                raise ValueError("Canonical report hash mismatch before whitespace patch")
            text = data.decode("utf-8")
            for old, new in patch["replacements"]:
                if text.count(old) != 1:
                    raise ValueError("Whitespace patch context is not unique")
                text = text.replace(old, new, 1)
            data = text.encode("utf-8")
        else:
            data = read_source(source)
        if blob_sha(data) != expected:
            raise ValueError(f"Source hash mismatch: {package}/{member}")
        data.decode("utf-8")
        stem = Path(manifest["packages"][package]["filename"]).stem
        dest = (output / safe_relative(stem) / safe_relative(member)).resolve()
        if not dest.is_relative_to(output):
            raise ValueError("Destination escapes the output directory")
        if dest.exists() and (not dest.is_file() or dest.read_bytes() != data):
            raise FileExistsError(f"Refusing to overwrite different content: {dest}")
        planned.append((dest, data))
    # Validate the whole package before writing any output.
    for dest, data in planned:
        dest.parent.mkdir(parents=True, exist_ok=True)
        if not dest.exists():
            with dest.open("xb") as out:
                out.write(data)
    return len(planned)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--manifest", type=Path, default=Path(__file__).with_name("MANIFEST.json"))
    args = parser.parse_args()
    try:
        manifest = json.loads(args.manifest.read_text(encoding="utf-8"))
        if manifest.get("schema_version") != 1:
            raise ValueError("Unsupported manifest version")
        count = restore(manifest, args.repo_root, args.output)
    except (OSError, ValueError, KeyError, RuntimeError, subprocess.TimeoutExpired) as exc:
        print(f"Restoration failed: {exc}", file=sys.stderr)
        return 1
    print(f"Restored and hash-verified {count} text files. Compiled PDF and original ZIP bytes were not archived.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
