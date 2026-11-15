"""Check the pinned source artifact; this does not run Lean."""

import hashlib
import json
import os
from pathlib import Path
import re
import resource
import time


BASE = Path(__file__).resolve().parent
ROOT = BASE / "snapshot"
REVISION = "adc7f1241b42e322a6451854ab7e4b4c146bf78a"
ENTRY = "OAI.Probability.TraceReconstruction"
CHALLENGE = "ComparatorChallenges.TraceReconstruction"


def code_only(text):
    """Mask nested comments and string literals, retaining line positions.

    This is a small source scanner, not a Lean parser or elaborator.
    """
    out = []
    i = 0
    depth = 0
    in_string = False
    line_comment = False
    while i < len(text):
        c = text[i]
        pair = text[i:i + 2]
        if line_comment:
            if c == "\n":
                line_comment = False
            out.append("\n" if c == "\n" else " ")
            i += 1
        elif depth:
            if pair == "/-":
                depth += 1
                out.extend("  ")
                i += 2
            elif pair == "-/":
                depth -= 1
                out.extend("  ")
                i += 2
            else:
                out.append("\n" if c == "\n" else " ")
                i += 1
        elif in_string:
            if c == "\\":
                out.extend("  ")
                i += 2
            else:
                if c == '"':
                    in_string = False
                out.append("\n" if c == "\n" else " ")
                i += 1
        elif pair == "--":
            line_comment = True
            out.extend("  ")
            i += 2
        elif pair == "/-":
            depth = 1
            out.extend("  ")
            i += 2
        elif c == '"':
            in_string = True
            out.append(" ")
            i += 1
        else:
            out.append(c)
            i += 1
    assert depth == 0 and not in_string, "Unterminated comment/string"
    return "".join(out)


def imports(text):
    found = []
    for line in code_only(text).splitlines():
        if re.match(r"^\s*(public\s+)?import\s", line):
            found.extend(line.split("import", 1)[1].split())
    return found


def main():
    started = time.monotonic()
    manifest = json.loads((ROOT / "MANIFEST.json").read_text())
    assert manifest["revision"] == REVISION
    assert manifest["repository"] == "openai/math"
    entries = manifest["files"]
    paths = [e["path"] for e in entries]
    assert len(paths) == len(set(paths))
    assert sorted(paths) == sorted(
        str(p.relative_to(ROOT)) for p in ROOT.rglob("*")
        if p.is_file() and p.name != "MANIFEST.json"
    )
    byte_count = 0
    for e in entries:
        path = ROOT / e["path"]
        assert path.resolve().is_relative_to(ROOT.resolve())
        data = path.read_bytes()
        assert len(data) == path.stat().st_size == e["bytes"]
        header = b"blob " + str(len(data)).encode() + b"\0"
        assert hashlib.sha1(header + data).hexdigest() == e["sha"]
        assert hashlib.sha256(data).hexdigest() == e["sha256"]
        sha1, sha256 = hashlib.sha1(header), hashlib.sha256()
        with path.open("rb") as f:
            while chunk := f.read(8192):
                sha1.update(chunk)
                sha256.update(chunk)
        assert sha1.hexdigest() == e["sha"]
        assert sha256.hexdigest() == e["sha256"]
        assert f"/blob/{REVISION}/" in e["display_url"]
        byte_count += len(data)
    assert byte_count == sum((ROOT / p).stat().st_size for p in paths)

    graph, source = {}, {}
    for path in (ROOT / "lean/OAI").rglob("*.lean"):
        module = str(path.relative_to(ROOT / "lean"))[:-5].replace("/", ".")
        source[module] = path.read_text()
        graph[module] = imports(source[module])
    visited, todo, external = set(), [ENTRY], set()
    while todo:
        mod = todo.pop()
        if mod in visited:
            continue
        assert mod in graph, f"Missing OAI module: {mod}"
        visited.add(mod)
        for dep in graph[mod]:
            if dep.startswith("OAI."):
                todo.append(dep)
            else:
                external.add(dep)
    assert visited == set(graph), "Missing or extra OAI source files"

    # A second traversal starts with every disk module and follows parents.
    parents = {mod: set() for mod in graph}
    for mod, deps in graph.items():
        for dep in deps:
            if dep.startswith("OAI."):
                parents[dep].add(mod)
    for mod in graph:
        seen, queue = set(), [mod]
        while queue:
            v = queue.pop()
            if v not in seen:
                seen.add(v)
                queue.extend(parents[v])
        assert ENTRY in seen, f"File not reachable from entry: {mod}"

    tokens = ("sorry", "admit", "axiom", "opaque")
    hits = {token: [] for token in tokens}
    lines = 0
    for mod, text in source.items():
        lines += len(text.splitlines())
        for number, line in enumerate(code_only(text).splitlines(), 1):
            for token in tokens:
                if re.search(r"\b" + token + r"\b", line):
                    hits[token].append([mod, number])
    assert not any(hits.values()), hits

    config = json.loads((ROOT / "lean/ComparatorChallenges/TraceReconstruction.json").read_text())
    assert config["solution_module"] == ENTRY
    assert config["challenge_module"] == CHALLENGE
    assert set(config["permitted_axioms"]) == {"propext", "Quot.sound", "Classical.choice"}
    challenge = (ROOT / "lean/ComparatorChallenges/TraceReconstruction.lean").read_text()
    assert len(re.findall(r"\bsorry\b", code_only(challenge))) == 3
    assert all(not dep.startswith("OAI.") for dep in imports(challenge))
    packages = json.loads((ROOT / "lean/lake-manifest.json").read_text())["packages"]
    mathlib = next(p["rev"] for p in packages if p["name"] == "mathlib")
    summary = {
        "revision": REVISION,
        "files": len(entries),
        "bytes": byte_count,
        "oai_modules": len(visited),
        "oai_source_lines": lines,
        "external_import_boundary": sorted(external),
        "source_token_hits_after_comment_and_string_masking": hits,
        "challenge_sorry_count": 3,
        "toolchain": (ROOT / "lean/lean-toolchain").read_text().strip(),
        "mathlib_revision": mathlib,
        "effective_nice": os.getpriority(os.PRIO_PROCESS, 0),
        "elapsed_seconds": round(time.monotonic() - started, 3),
        "max_rss_bytes_macos": resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
        "lean_executed": False,
    }
    print(json.dumps(summary, indent=2))
    print("Snapshot checks: PASS (source audit only; no kernel acceptance claim)")


if __name__ == "__main__":
    main()
