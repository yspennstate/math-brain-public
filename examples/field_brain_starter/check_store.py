"""Check that the store still holds together: every record indexed, every link and replacement pointing somewhere.

    python check_store.py                 # the starter's memory/ folder
    python check_store.py --dir path/to/memory
    python check_store.py --selftest      # break a copy of the store on purpose and show that each fault is caught

Records get written by hand, by new_record.py and by a dreaming agent at night. Any of them can leave a record out of
the index, a [[link]] to a slug that was never written, or a superseded_by: that names a record nobody kept. Recall
still runs on such a store; it just stops finding things, and nothing says so. This script says so.

ERRORS (exit 1): a record without a name, description or type; a name that differs from the file name; an index line
whose file is missing; a record with no index line; a [[link]] or superseded_by: that names no record; a record that
supersedes itself, or a chain of replacements that loops.
WARNINGS (exit 0): a record with no status line, or a status other than verified / provisional / superseded; the same
record indexed twice.

Run it after a dream and after editing records by hand. run_dream.py runs it and puts the result in the night's log.
Standard library only.
"""
import argparse
import os
import re
import shutil
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
STATUSES = ("verified", "provisional", "superseded")
LINK = re.compile(r"\[\[([^\]|#]+)")
INDEX_LINE = re.compile(r"^- \[([^\]]+)\]\(([^)]+)\)")


def read(path):
    with open(path, encoding="utf-8") as fh:
        return fh.read().replace("\r\n", "\n")


def front(text):
    """The frontmatter as a flat dict (nested keys such as 'metadata: type:' come out as 'type'), and the body."""
    m = re.match(r"^---\n(.*?)\n---\n?(.*)$", text, re.S)
    if not m:
        return None, text
    meta = {}
    for line in m.group(1).splitlines():
        k, _, v = line.strip().partition(":")
        if v.strip():
            meta[k.strip()] = v.strip()
    return meta, m.group(2)


def check(folder):
    errors, warnings = [], []
    files = sorted(n for n in os.listdir(folder) if n.endswith(".md"))
    records = {n[:-3]: read(os.path.join(folder, n)) for n in files if not n[:-3].isupper()}
    slugs = set(records)
    supersede = {}

    for slug, text in records.items():
        f = slug + ".md"
        meta, body = front(text)
        if meta is None:
            errors.append("%s: no frontmatter (a --- block with name, description and type)" % f)
            meta = {}
        for key in ("name", "description", "type"):
            if key in meta or meta == {}:
                continue
            errors.append("%s: frontmatter has no %s" % (f, key))
        if meta.get("name") and meta["name"] != slug:
            errors.append("%s: name is %s, not the file name" % (f, meta["name"]))
        status = meta.get("status")
        if meta and status is None:
            warnings.append("%s: no status line (verified, provisional or superseded)" % f)
        elif status and status not in STATUSES:
            warnings.append("%s: status %r is not one of %s" % (f, status, ", ".join(STATUSES)))
        new = meta.get("superseded_by")
        if new:
            if new == slug:
                errors.append("%s: superseded_by names itself" % f)
            elif new not in slugs:
                errors.append("%s: superseded_by %s, and no record has that name" % (f, new))
            else:
                supersede[slug] = new
        for target in sorted(set(LINK.findall(body))):
            if target.strip() not in slugs:
                errors.append("%s: links [[%s]], and no record has that name" % (f, target.strip()))

    for start in supersede:  # a loop of replacements leaves no current record to read
        seen, cur = [start], supersede[start]
        while cur in supersede and cur not in seen:
            seen.append(cur)
            cur = supersede[cur]
        if cur == start:
            errors.append("%s.md: superseded_by chain loops: %s" % (start, " -> ".join(seen + [start])))

    index_path = os.path.join(folder, "MEMORY.md")
    indexed = []
    if not os.path.exists(index_path):
        errors.append("MEMORY.md: missing; every record needs a line in the index")
    else:
        for n, line in enumerate(read(index_path).splitlines(), 1):
            m = INDEX_LINE.match(line)
            if not m:
                continue
            target = m.group(2)
            slug = target[:-3] if target.endswith(".md") else target
            if not os.path.exists(os.path.join(folder, target)):
                errors.append("MEMORY.md line %d: points to %s, which does not exist" % (n, target))
            indexed.append(slug)
        for slug in sorted(slugs - set(indexed)):
            errors.append("%s.md: no line in MEMORY.md, so an agent reading the index never learns it exists" % slug)
        for slug in sorted({s for s in indexed if indexed.count(s) > 1}):
            warnings.append("MEMORY.md: %s is indexed %d times" % (slug, indexed.count(slug)))

    mistakes = os.path.join(folder, "MISTAKES.md")
    if os.path.exists(mistakes):
        for n, line in enumerate(read(mistakes).splitlines(), 1):
            for target in LINK.findall(line):
                if target.strip() not in slugs:
                    errors.append("MISTAKES.md line %d: links [[%s]], and no record has that name" % (n, target.strip()))
    return errors, warnings, len(records)


def report(folder):
    errors, warnings, n = check(folder)
    for e in errors:
        print("ERROR   " + e)
    for w in warnings:
        print("warning " + w)
    print("%d records: %d error(s), %d warning(s)" % (n, len(errors), len(warnings)))
    return 1 if errors else 0


def selftest(folder):
    errors, _, n = check(folder)
    if errors:
        print("the store itself has errors; fix those first:")
        return report(folder)
    tmp = tempfile.mkdtemp(prefix="check_store_")
    try:
        mem = os.path.join(tmp, "memory")
        shutil.copytree(folder, mem)
        recs = sorted(s[:-3] for s in os.listdir(mem) if s.endswith(".md") and not s[:-3].isupper())
        a, b, c = recs[0], recs[1], recs[2]

        def edit(slug, change):
            p = os.path.join(mem, slug + ".md")
            text = change(read(p))
            with open(p, "w", encoding="utf-8", newline="\n") as fh:
                fh.write(text)

        edit(a, lambda t: t + "\nSee [[no_such_record_2026_01_01]].\n")
        edit(b, lambda t: t.replace("\nname: ", "\nsuperseded_by: %s\nname: " % b, 1))
        index = read(os.path.join(mem, "MEMORY.md"))
        kept = [ln for ln in index.splitlines() if "(%s.md)" % c not in ln]
        with open(os.path.join(mem, "MEMORY.md"), "w", encoding="utf-8", newline="\n") as fh:
            fh.write("\n".join(kept + ["- [gone_2026_01_01](gone_2026_01_01.md) - a record that was never written"]) + "\n")
        errs, _, _ = check(mem)
        wanted = {"broken link": "no_such_record_2026_01_01",
                  "self-supersede": "superseded_by names itself",
                  "unindexed record": "%s.md: no line in MEMORY.md" % c,
                  "index line to a missing file": "gone_2026_01_01.md, which does not exist"}
        ok = True
        for label, needle in wanted.items():
            hit = any(needle in e for e in errs)
            ok &= hit
            print("%-30s %s" % (label, "caught" if hit else "MISSED"))
        print("clean store: %d records, 0 errors; broken copy: %d errors" % (n, len(errs)))
        return 0 if ok else 1
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--dir", default=os.environ.get("BRAIN_MEM_DIR", os.path.join(HERE, "memory")))
    ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args()
    return selftest(a.dir) if a.selftest else report(a.dir)


if __name__ == "__main__":
    sys.exit(main())
