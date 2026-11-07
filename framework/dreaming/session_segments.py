"""session_segments.py - past sessions as recall notes, in an index of their own.

A question about an earlier session ("what did we decide yesterday about the index", "when did I ask for the
backup") is answered by a transcript, and the memory corpus holds none. This cuts session transcripts (Claude Code
.jsonl and Codex rollout .jsonl) into one provisional note per user prompt - the prompt whole, the assistant's text,
tool output cut to its error lines, system-reminder text dropped, a pasted document reduced to one line - drops any
note the secret scanner flags, writes one copy of a repeated body, and builds a bm25 index over the notes alone.

The notes get their own index on purpose: added to the memory index, sixteen thousand segments shift every query's
document frequencies and average length, and in the measurement behind this design best-in-5 on ordinary questions
fell by four while only two segments ever reached a top five. A separate index leaves the memory ranking as it was;
brain.py recall merges one segment into display slot 5 (see _segment_slot there).

    python session_segments.py build --root TRANSCRIPTS [--out DIR] [--sample N]
    python session_segments.py selftest

--out defaults to ~/.claude/brain_graph/segments_index (the folder brain.py reads; BRAIN_SEG_INDEX moves both).
The builder never writes inside the memory folder. Rebuild when transcripts accumulate; the build replaces the notes.
"""
import argparse
import hashlib
import json
import os
import random
import re
import shutil
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

DEFAULT_OUT = os.path.dirname(os.environ.get("BRAIN_SEG_INDEX") or os.path.join(
    os.path.expanduser("~"), ".claude", "brain_graph", "segments_index", "bm25_index.json.gz"))
SYSREM = re.compile(r"<system-reminder>.*?</system-reminder>", re.S)
PASTE = re.compile(r"<pasted_content[^>]*>(.*?)</pasted_content[^>]*>", re.S)
# an error REPORT, not any line holding the word (help text, source lines and grep hits got in otherwise)
ERRLINE = re.compile(r"^\s*(error\b|fatal:|traceback|[\w.]*(error|exception)\b:)"
                     r"|FullyQualifiedErrorId|exit(ed with)? code:? *[1-9]|command not found"
                     r"|no such file or directory|permission denied|access is denied", re.I)
HEADLESS = re.compile(r'"entrypoint"\s*:\s*"sdk-|"originator"\s*:\s*"codex_exec"|"source"\s*:\s*"exec"')
MAX_BODY = 6000


def _scan(text):
    try:
        from scan_secrets import scan
    except Exception:
        # transcripts carry pasted keys; without the scanner no note is written
        raise SystemExit("refused: scan_secrets.py is not importable beside this file")
    return scan(text)


def clean(s):
    s = SYSREM.sub("", s)
    s = PASTE.sub(lambda m: "[pasted document, %d chars]" % len(m.group(1)), s)
    return s.strip()


def text_of(content):
    if isinstance(content, str):
        return content
    if isinstance(content, list):
        return "\n".join(x.get("text", "") for x in content
                         if isinstance(x, dict) and x.get("type") in ("text", "input_text", "output_text"))
    return ""


def err_lines(s, k=3):
    return [ln.strip()[:300] for ln in str(s).splitlines() if ERRLINE.search(ln)][:k]


def events(path):
    """Yield (lineno, kind, text), kind in user / assistant / tool."""
    with open(path, encoding="utf-8", errors="replace") as h:
        for i, line in enumerate(h, 1):
            try:
                o = json.loads(line)
            except Exception:
                continue
            t = o.get("type")
            if t == "user" and not o.get("isMeta"):
                c = (o.get("message") or {}).get("content")
                if isinstance(c, list) and any(isinstance(x, dict) and x.get("type") == "tool_result" for x in c):
                    for x in c:
                        if isinstance(x, dict) and x.get("type") == "tool_result":
                            v = x.get("content")
                            yield i, "tool", v if isinstance(v, str) else text_of(v)
                    continue
                s = clean(text_of(c))
                if s and not s.startswith(("<local-command", "<command-", "Caveat:")):
                    yield i, "user", s
            elif t == "assistant":
                s = clean(text_of((o.get("message") or {}).get("content")))
                if s:
                    yield i, "assistant", s
            elif t == "event_msg":
                p = o.get("payload") or {}
                if p.get("type") == "user_message":
                    s = clean(p.get("message") or "")
                    if s:
                        yield i, "user", s
                elif p.get("type") == "agent_message":
                    s = clean(p.get("message") or "")
                    if s:
                        yield i, "assistant", s
            elif t == "response_item":
                p = o.get("payload") or {}
                if p.get("type") == "function_call_output":
                    yield i, "tool", str(p.get("output", ""))


def segments(path):
    cur = None
    for i, kind, s in events(path):
        if kind == "user":
            if cur:
                yield cur
            cur = {"start": i, "end": i, "prompt": s, "body": []}
        elif cur is not None:
            cur["end"] = i
            if kind == "assistant":
                cur["body"].append(s)
            else:
                cur["body"] += ["[tool error] " + e for e in err_lines(s)]
    if cur:
        yield cur


def is_headless(path):
    """A launched session (claude -p / sdk, codex exec): its opening prompt is a launcher's text, not a person's."""
    with open(path, encoding="utf-8", errors="replace") as h:
        return bool(HEADLESS.search(h.read(65536)))


def note(root, path, seg, headless=False):
    """(slug, full text, content) - content is everything after the frontmatter, the dedup key."""
    rel = os.path.relpath(path, root).replace("\\", "/")
    sid = hashlib.sha1(("%s:%s" % (rel, seg["start"])).encode()).hexdigest()[:12]
    slug = "transcript_segment_" + sid
    body = "\n\n".join(seg["body"])
    if len(body) > MAX_BODY:
        body = body[: MAX_BODY // 2] + "\n\n[... cut ...]\n\n" + body[-MAX_BODY // 2:]
    desc = re.sub(r"\s+", " ", seg["prompt"])[:150]
    label = "[PROVISIONAL] launch prompt: " if headless else "[PROVISIONAL] transcript: "
    fm = ["---", "name: " + slug, "description: " + json.dumps(label + desc, ensure_ascii=False),
          "metadata:", "  type: project", "status: provisional", "kind: transcript_segment",
          "speaker: " + ("launch" if headless else "user"),
          "source: " + json.dumps("%s:%s-%s" % (rel, seg["start"], seg["end"])), "---", ""]
    head = "Launch prompt (written by a launcher, not by a person):" if headless else "User prompt:"
    content = head + "\n\n" + seg["prompt"] + "\n\nWhat followed:\n\n" + body + "\n"
    return slug, "\n".join(fm) + content, content


def write_notes(root, mem, sample=0, seed=20261104):
    files = sorted(os.path.join(d, f) for d, _, fs in os.walk(root) for f in fs if f.endswith(".jsonl"))
    if sample:
        random.seed(seed)
        files = random.sample(files, min(sample, len(files)))
    st = dict(files=len(files), segments=0, written=0, secret_dropped=0, duplicates=0, launch=0)
    seen = {}       # sha1 of content -> note path; a repeated body is written once, its other sources appended
    for f in files:
        headless = is_headless(f)
        for seg in segments(f):
            st["segments"] += 1
            slug, text, content = note(root, f, seg, headless)
            if _scan(text):
                st["secret_dropped"] += 1
                continue
            key = hashlib.sha1(content.encode("utf-8")).hexdigest()
            if key in seen:
                with open(seen[key], "a", encoding="utf-8", newline="\n") as h:
                    h.write("\nAlso in: %s:%s-%s\n" % (os.path.relpath(f, root).replace("\\", "/"),
                                                       seg["start"], seg["end"]))
                st["duplicates"] += 1
                continue
            seen[key] = os.path.join(mem, slug + ".md")
            with open(seen[key], "w", encoding="utf-8", newline="\n") as h:
                h.write(text)
            st["written"] += 1
            st["launch"] += headless
    return st


def build(root, out, sample=0):
    """Cut `root`'s transcripts into OUT/memory and build OUT/bm25_index.json.gz over them. Returns the stats."""
    out = os.path.abspath(out)
    live_mem = os.path.normcase(os.path.abspath(os.environ.get("BRAIN_MEM_DIR") or os.path.join(
        os.path.expanduser("~"), ".claude", "projects")))
    if os.path.normcase(out).startswith(live_mem):
        raise SystemExit("refused: --out is inside the memory folder")
    mem = os.path.join(out, "memory")
    if os.path.isdir(mem):
        shutil.rmtree(mem)          # a rebuildable cache: the transcripts are the source
    os.makedirs(mem)
    st = write_notes(root, mem, sample)
    with open(os.path.join(mem, "MEMORY.md"), "w", encoding="utf-8", newline="\n") as fh:
        fh.write("# Memory Index (transcript segments only)\n")
    idx = os.path.join(out, "bm25_index.json.gz")
    # bm25 reads its paths at import: point this process at the segments folder before the import
    os.environ["BRAIN_MEM_DIR"], os.environ["BRAIN_BM25_INDEX"] = mem, idx
    import bm25
    t0 = time.time()
    bm25.build(mem, idx)
    try:
        bm25.maybe_build_postings(idx, force=True)
    except Exception:
        pass
    have = set(bm25._load_payload(idx)["dl"])
    names = [f[:-3] for f in os.listdir(mem) if f.endswith(".md") and f != "MEMORY.md"]
    st.update(index_docs=len(have), missing=len([s for s in names if s not in have]),
              build_s=round(time.time() - t0, 1), at=time.strftime("%Y-%m-%d %H:%M:%S"))
    with open(os.path.join(out, "MANIFEST.json"), "w", encoding="utf-8") as fh:
        json.dump(st, fh, indent=1)
    return st


def selftest():
    """Two fake sessions -> notes; the secret-bearing one is dropped; a repeat is written once."""
    import string
    import tempfile
    # a token-shaped string made at run time (the scanner passes repeated or sequential fillers as fakes)
    rng = random.Random(7)
    token = "gh" + "p_" + "".join(rng.choice(string.ascii_letters + string.digits) for _ in range(36))
    tmp = tempfile.mkdtemp(prefix="segtest_")
    try:
        root = os.path.join(tmp, "t")
        os.makedirs(root)
        rows = [{"type": "user", "message": {"content": "please rebuild the lexical index tonight"}},
                {"type": "assistant", "message": {"content": [{"type": "text", "text": "Rebuilt it, 512 docs."}]}},
                {"type": "user", "message": {"content": "my key is " + token}},
                {"type": "assistant", "message": {"content": "noted"}}]
        for name in ("a.jsonl", "b.jsonl"):
            with open(os.path.join(root, name), "w", encoding="utf-8") as fh:
                fh.write("\n".join(json.dumps(r) for r in rows) + "\n")
        mem = os.path.join(tmp, "m")
        os.makedirs(mem)
        st = write_notes(root, mem)
        ok = st["segments"] == 4 and st["written"] == 1 and st["duplicates"] == 1 and st["secret_dropped"] == 2
        print(("PASS" if ok else "FAIL") + "  selftest %s" % st)
        return 0 if ok else 1
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    sub = ap.add_subparsers(dest="cmd")
    b = sub.add_parser("build")
    b.add_argument("--root", required=True, help="folder of session .jsonl transcripts (walked recursively)")
    b.add_argument("--out", default=DEFAULT_OUT)
    b.add_argument("--sample", type=int, default=0)
    sub.add_parser("selftest")
    a = ap.parse_args()
    if a.cmd == "build":
        print(json.dumps(build(a.root, a.out, a.sample)))
    elif a.cmd == "selftest":
        sys.exit(selftest())
    else:
        ap.print_help()


if __name__ == "__main__":
    main()
