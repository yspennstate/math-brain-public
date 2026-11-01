"""Bring a folder of existing documents into the store as provisional reference records, one record per file.

    python import_docs.py ../handbook --dry-run        # list what would be written, write nothing
    python import_docs.py ../handbook                  # write the records and their index lines
    python import_docs.py --selftest                   # import two documents into a scratch store and check it

new_record.py is for the lessons a team writes one at a time. A team that already has a few hundred pages (a
handbook, incident reviews, delivery specs, old design notes) should not retype them. This script reads every .md
and .txt file under the folder you name, and writes for each one a record of type reference: the description is the
document's first heading or first line, the body is its opening text (--chars, default 1500) followed by the path it
came from, and the date is the file's own modification date. Every record starts provisional, because nobody has
checked yet that the document is still true; promote the ones you have checked by changing status: to verified.

Only the folder you name is read: ingestion is deny by default, so point it at the pages the team has decided belong
in the brain, not at a whole drive. A file whose record already exists is skipped, so the script can be run again
after new documents are added. Run check_store.py afterwards. Standard library only.
"""
import argparse
import datetime as dt
import os
import re
import shutil
import subprocess
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from new_record import IndexLock, slugify, write_atomic  # noqa: E402

EXTENSIONS = (".md", ".txt")


def documents(folder):
    for root, dirs, files in os.walk(folder):
        dirs[:] = sorted(d for d in dirs if not d.startswith("."))
        for name in sorted(files):
            if name.lower().endswith(EXTENSIONS) and not name.startswith("."):
                yield os.path.join(root, name)


def strip_frontmatter(text):
    m = re.match(r"^---\n.*?\n---\n?", text, re.S)
    return text[m.end():] if m else text


def describe(text, fallback):
    """The first heading, or else the first non-empty line, as one line of at most 150 characters."""
    lines = [l.strip() for l in text.splitlines() if l.strip()]
    heading = next((l for l in lines if l.startswith("#")), None)
    line = (heading or (lines[0] if lines else fallback)).lstrip("#").strip()
    line = re.sub(r"\s+", " ", line).replace("[[", "[").replace("]]", "]")
    return (line[:147] + "...") if len(line) > 150 else (line or fallback)


def record_for(path, folder, chars):
    with open(path, encoding="utf-8", errors="replace") as fh:
        text = strip_frontmatter(fh.read().replace("\r\n", "\n"))
    rel = os.path.relpath(path, folder).replace(os.sep, "/")
    description = describe(text, os.path.splitext(os.path.basename(path))[0].replace("_", " "))
    day = dt.date.fromtimestamp(os.path.getmtime(path))
    body = text.strip()
    if len(body) > chars:
        body = body[:chars].rsplit(" ", 1)[0] + " ..."
    body = body.replace("[[", "[ [")  # a [[...]] in a document is not a link to a record
    slug = slugify(description, day)
    lines = ["---", "name: " + slug, "description: " + description, "metadata:", "  type: reference",
             "status: provisional", "---", "", body, "", "Source: `%s`, imported %s." % (rel, dt.date.today())]
    return slug, description, "\n".join(lines) + "\n"


def run(folder, mem, chars, dry_run, out=sys.stdout):
    if not os.path.isdir(folder):
        sys.exit("no folder %s" % folder)
    os.makedirs(mem, exist_ok=True)
    new, skipped = [], 0
    seen = set()
    for path in documents(folder):
        slug, description, text = record_for(path, folder, chars)
        if slug in seen or os.path.exists(os.path.join(mem, slug + ".md")):
            skipped += 1
            continue
        seen.add(slug)
        new.append((slug, description, text))
        print("%s %s" % ("would write" if dry_run else "write", slug), file=out)
    if not dry_run and new:
        for slug, _, text in new:
            write_atomic(os.path.join(mem, slug + ".md"), text)
        with IndexLock(mem):
            index = os.path.join(mem, "MEMORY.md")
            lines = open(index, encoding="utf-8").read().splitlines() if os.path.exists(index) else ["# Memory index"]
            at = next((i for i, l in enumerate(lines) if l.startswith("- ")), len(lines))
            lines[at:at] = ["- [%s](%s.md) - [PROVISIONAL] %s" % (s, s, d) for s, d, _ in new]
            write_atomic(index, "\n".join(lines) + "\n")
    print("%d %s, %d already in the store" % (len(new), "to write" if dry_run else "written", skipped), file=out)
    return len(new)


def selftest():
    work = tempfile.mkdtemp(prefix="import_docs_")
    try:
        docs, mem = os.path.join(work, "docs"), os.path.join(work, "memory")
        os.makedirs(os.path.join(docs, "reviews"))
        open(os.path.join(docs, "delivery.md"), "w", encoding="utf-8").write(
            "---\ntitle: x\n---\n# Festival delivery spec\n\nStereo and 5.1 go as separate files. See [[old wiki]].\n")
        open(os.path.join(docs, "reviews", "outage.txt"), "w", encoding="utf-8").write(
            "\n\nThe March outage came from a certificate nobody renewed.\nRenewals now have an owner.\n")
        open(os.path.join(docs, "notes.pdf"), "w").write("not a text document")
        os.makedirs(mem)
        quiet = open(os.devnull, "w")
        checks = []
        checks.append(("dry run writes nothing", run(docs, mem, 1500, True, quiet) == 2 and not os.listdir(mem)))
        checks.append(("two documents become two records", run(docs, mem, 1500, False, quiet) == 2))
        names = sorted(n for n in os.listdir(mem) if n != "MEMORY.md")
        index = open(os.path.join(mem, "MEMORY.md"), encoding="utf-8").read()
        checks.append(("the heading names the first record", any(n.startswith("festival_delivery_spec_") for n in names)))
        checks.append(("the first line names the second", any(n.startswith("the_march_outage_came_from") for n in names)))
        checks.append(("both are in the index", all("(%s)" % n in index for n in names)))
        body = open(os.path.join(mem, [n for n in names if n.startswith("festival")][0]), encoding="utf-8").read()
        checks.append(("frontmatter of the document is dropped", "title: x" not in body))
        checks.append(("the source path is kept", "Source: `delivery.md`" in body))
        checks.append(("a [[...]] in a document is not left as a link", "[[" not in body.split("---", 2)[2]))
        checks.append(("a second run adds nothing", run(docs, mem, 1500, False, quiet) == 0))
        res = subprocess.run([sys.executable, os.path.join(HERE, "check_store.py"), "--dir", mem],
                             capture_output=True, text=True)
        checks.append(("check_store.py passes the imported store", res.returncode == 0))
        quiet.close()
        for name, ok in checks:
            print("%s  %s" % ("ok  " if ok else "FAIL", name))
        bad = sum(1 for _, ok in checks if not ok)
        print("%d of %d checks pass" % (len(checks) - bad, len(checks)))
        return 1 if bad else 0
    finally:
        shutil.rmtree(work, ignore_errors=True)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("folder", nargs="?")
    ap.add_argument("--dir", default=os.environ.get("BRAIN_MEM_DIR", os.path.join(HERE, "memory")),
                    help="the store's memory folder")
    ap.add_argument("--chars", type=int, default=1500, help="how much of each document goes into its record")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args()
    if a.selftest:
        return selftest()
    if not a.folder:
        ap.error("name the folder of documents to import")
    run(a.folder, a.dir, a.chars, a.dry_run)
    return 0


if __name__ == "__main__":
    sys.exit(main())
