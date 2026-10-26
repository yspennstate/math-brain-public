"""Write one record into the store and add its line to the index.

    python new_record.py feedback "Clear music rights before picture lock" \
        --body "Clear every cue before the edit locks." \
        --why "A cue cleared after lock forced a re-edit of the harbour film." \
        --apply "At rough cut, list every cue and its licence; nothing locks with an open line." \
        --link project_harbour_film_cut_to_twelve_minutes_2026_03_10

    python new_record.py project "Harbour film ships at 12 minutes" --supersedes project_harbour_film_runs_eighteen_minutes_2026_02_20

Types: user, feedback, project, reference. The slug is built from the description and today's date. A new record
starts provisional unless --verified is given. --supersedes marks the old record superseded_by the new one (the
old record is kept: a reader who finds it must also find what replaced it). Standard library only.
"""
import argparse
import datetime as dt
import os
import re
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
TYPES = ("user", "feedback", "project", "reference")


def write_atomic(path, text):
    tmp = path + ".tmp"
    with open(tmp, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(text)
    os.replace(tmp, path)  # a crash mid-write leaves the old file whole


class IndexLock:
    """Hold memory/.index.lock while the index is read and rewritten. Without it, two agents writing records at the
    same moment each read the old index, each add their line, and the second write drops the first agent's line.
    A lock older than a minute is left by a crashed writer and is cleared."""

    def __init__(self, folder, wait=20.0, stale=60.0):
        self.path, self.wait, self.stale = os.path.join(folder, ".index.lock"), wait, stale

    def __enter__(self):
        end = time.time() + self.wait
        while True:
            try:
                os.close(os.open(self.path, os.O_CREAT | os.O_EXCL | os.O_WRONLY))
                return self
            except FileExistsError:
                try:
                    if time.time() - os.path.getmtime(self.path) > self.stale:
                        os.remove(self.path)
                        continue
                except OSError:
                    continue
                if time.time() > end:
                    sys.exit("the index is locked by another writer (%s); try again" % self.path)
                time.sleep(0.1)

    def __exit__(self, *exc):
        try:
            os.remove(self.path)
        except OSError:
            pass


def slugify(text, day):
    words = re.findall(r"[a-z0-9]+", text.lower())[:8]
    return "%s_%s" % ("_".join(words), day.strftime("%Y_%m_%d"))


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("type", choices=TYPES)
    ap.add_argument("description", help="one line that states the finding itself")
    ap.add_argument("--body", default="")
    ap.add_argument("--why", default="", help="the reason, for feedback records")
    ap.add_argument("--apply", default="", help="what to do next time, for feedback records")
    ap.add_argument("--link", action="append", default=[], help="slug of a related record (repeatable)")
    ap.add_argument("--supersedes", help="slug of the record this one replaces")
    ap.add_argument("--verified", action="store_true")
    ap.add_argument("--date", help="YYYY-MM-DD, default today")
    ap.add_argument("--dir", default=os.environ.get("BRAIN_MEM_DIR", os.path.join(HERE, "memory")))
    a = ap.parse_args()

    day = dt.date.fromisoformat(a.date) if a.date else dt.date.today()
    slug = slugify(a.description, day)
    path = os.path.join(a.dir, slug + ".md")
    if os.path.exists(path):
        sys.exit("exists: %s" % path)
    links = list(a.link) + ([a.supersedes] if a.supersedes else [])
    for s in links:
        if not os.path.exists(os.path.join(a.dir, s + ".md")):
            sys.exit("no record named %s" % s)

    status = "verified" if a.verified else "provisional"
    out = ["---", "name: " + slug, "description: " + a.description, "metadata:", "  type: " + a.type,
           "status: " + status, "---", "", a.body or a.description]
    if a.why:
        out += ["", "**Why:** " + a.why]
    if a.apply:
        out += ["**How to apply:** " + a.apply]
    if links:
        out += ["", "Related: " + ", ".join("[[%s]]" % s for s in links) + "."]
    open(path, "w", encoding="utf-8", newline="\n").write("\n".join(out) + "\n")
    with IndexLock(a.dir):
        update_old_and_index(a, slug)
    print("wrote", path)


def update_old_and_index(a, slug):
    if a.supersedes:
        old = os.path.join(a.dir, a.supersedes + ".md")
        text = open(old, encoding="utf-8").read()
        if "superseded_by:" in text:
            print("note: %s is already superseded; left as it is" % a.supersedes, file=sys.stderr)
        elif "\nstatus:" not in text:
            print("note: %s has no status line; add superseded_by: %s by hand" % (a.supersedes, slug), file=sys.stderr)
        else:
            text = text.replace("\nstatus:", "\nsuperseded_by: %s\nstatus:" % slug, 1)
            write_atomic(old, text)

    index = os.path.join(a.dir, "MEMORY.md")
    lines = open(index, encoding="utf-8").read().splitlines() if os.path.exists(index) else ["# Memory index"]
    tag = "[VERIFIED]" if a.verified else "[PROVISIONAL]"
    entry = "- [%s](%s.md) - %s %s" % (slug, slug, tag, a.description)
    at = next((i for i, l in enumerate(lines) if l.startswith("- ")), len(lines))
    lines.insert(at, entry)  # newest first
    write_atomic(index, "\n".join(lines) + "\n")


if __name__ == "__main__":
    main()
