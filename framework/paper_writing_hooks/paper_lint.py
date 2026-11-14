# -*- coding: utf-8 -*-
"""paper_lint.py - the paper-writing checks W01..W38 by hand, on a .tex file or a paper folder.

  python paper_lint.py <file.tex | folder> [more ...]      every finding with its line; exit 1 when a MUST is found
  python paper_lint.py <file.tex> --json                   the same as JSON
  python paper_lint.py <new.tex> --against <old.tex> ...   sentences of <new> that stand word for word in <old>
  python paper_lint.py --build-index                       index the sentences of his earlier papers (own_papers.txt)
  python paper_lint.py --census <file or folder or glob>...  one line per paper: MUST and should counts
Engine pw_core.py, table pw_hooks.py (an agent, 12 Nov 2026).
"""
import glob
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import pw_core as C  # noqa: E402
import pw_hooks as H  # noqa: E402

for _s in (sys.stdout, sys.stderr):
    try:
        _s.reconfigure(encoding="utf-8", errors="replace")
    except Exception:  # noqa: BLE001
        pass


def tex_files(arg):
    arg = os.path.expanduser(arg)
    if os.path.isdir(arg):
        return C._main_tex(arg, 6) or sorted(glob.glob(os.path.join(arg, "*.tex")))[:6]
    if any(c in arg for c in "*?["):
        return sorted(f for f in glob.glob(arg, recursive=True) if f.lower().endswith(".tex"))
    return [arg]


def _head(path):
    try:
        with open(path, encoding="utf-8", errors="replace") as f:
            return f.read(6000)
    except OSError:
        return ""


def lint(path):
    d = C._read_doc(path)
    if d is None:
        return None, []
    if not d.whole:                       # a section file: lint the paper that includes it
        main = C.find_main(path)
        whole = C._read_doc(main) if main else None
        if whole is not None and whole.whole:
            d = whole
    out = []
    for h in H.TEXT:
        got = C.scan(h, [d])
        if got:
            out.append((h, got))
    return d, out


def against(new, olds):
    d = C._read_doc(new)
    if d is None:
        print("cannot read", new)
        return 2
    mine = C.sent_keys(d)
    units = C.unit_list(d)
    total = 0
    for old in olds:
        o = C._read_doc(old)
        if o is None:
            print("cannot read", old)
            continue
        theirs = {k: ln for ln, s, k in C.sent_keys(o)}
        hits = [(ln, s, theirs[k]) for ln, s, k in mine if k in theirs]
        total += len(hits)
        ou = C.unit_list(o)
        runs = {}
        for i, u in enumerate(ou):
            for k in u[3]:
                runs.setdefault(k, []).append(i)
        for (ln, env, lab, ks), i, c in C.unit_matches(units, lambda k: runs.get(k, ())):
            total += 5                    # one statement or proof printed again is a finding by itself
            print("the %s at l.%d%s stands, formulas included, in %s: the %s at l.%d%s (%d of %d runs of five tokens)" % (
                env, d.src(ln)[1], " (\\label{%s})" % lab if lab else "", old, ou[i][1], o.src(ou[i][0])[1],
                ", \\label{%s}" % ou[i][2] if ou[i][2] else "", c, len(ks)))
        print("%d of %d sentences of %s stand word for word in %s" % (len(hits), len(mine), os.path.basename(new), old))
        for ln, s, lo in hits[:60]:
            print("  l.%d (there l.%d): %s" % (ln, lo, C.excerpt(C.plain(s), 130)))
        if len(hits) > 60:
            print("  ... and %d more" % (len(hits) - 60))
    return 1 if total >= 5 else 0


def main(argv):
    if not argv or argv[0] in ("-h", "--help"):
        print(__doc__)
        return 0
    if argv[0] == "--build-index":
        idx = C.build_own_index()
        print("indexed %d sentences of %d papers -> %s" % (len(idx["keys"]), len(idx["sources"]), C.OWN_INDEX))
        for s in idx["sources"]:
            print("  ", s["path"])
        return 0
    if "--against" in argv:
        i = argv.index("--against")
        return against(argv[0], argv[i + 1:])
    if argv[0] == "--census":
        rows, done = [], set()
        for a in argv[1:]:
            for f in tex_files(a):
                main = f if "\\documentclass" in _head(f) else C.find_main(f) or f
                if C._key(main) in done:          # a section file of a paper already counted
                    continue
                done.add(C._key(main))
                d, found = lint(main)
                f = main
                if d is None or not d.whole:
                    continue
                m = sum(C.must_n(h, g) for h, g in found)
                s = sum(len(g) for h, g in found) - m
                rows.append((m, s, d.words, " ".join(h["id"] for h, g in found if C.must_n(h, g)), f))
        for m, s, w, ids, f in sorted(rows, reverse=True):
            print("MUST %3d  should %3d  words %6d  %-28s %s" % (m, s, w, ids, f.replace("\\", "/")))
        print("%d papers, %d with a MUST finding" % (len(rows), sum(1 for r in rows if r[0])))
        return 0
    as_json = "--json" in argv
    files = [f for a in argv if not a.startswith("--") for f in tex_files(a)]
    worst, report = 0, []
    for f in files:
        d, found = lint(f)
        if d is None:
            print("cannot read", f)
            worst = max(worst, 2)
            continue
        must = sum(C.must_n(h, g) for h, g in found)
        intro = sum(len(g) - C.must_n(h, g) for h, g in found if h["id"] in C.INTRO_GROUP)
        if must:
            worst = max(worst, 1)
        if as_json:
            report.append({"file": d.path, "asked": f, "files": d.files, "cut": d.cut, "words": d.words, "must": must,
                           "introduction": intro,
                           "findings": [{"id": h["id"], "must": C.must_n(h, g), "title": h["title"],
                                         "rule": h["rule"], "hits": [{"line": ln, "text": ex} for _, ln, ex in g]}
                                        for h, g in found]})
            continue
        shape = "whole document" if d.whole else "fragment: no main file that includes it was found, so the " \
                                                 "whole-paper checks did not run"
        if d.files > 1:
            shape += ", %d files read through \\input" % d.files
        print("%s  (%s, about %d words)" % (d.path, shape, d.words))
        if C._key(d.path) != C._key(f):
            print("  %s is part of this paper; the whole paper was read" % f.replace("\\", "/"))
        if d.cut:
            print("  longer than %d characters: only that much was read" % C.MAX_TEX)
        if d.unresolved:
            print("  %d \\input file(s) were not found: part of the paper was not read" % d.unresolved)
        if not found:
            print("  clean: none of the %d text checks found anything" % len(H.TEXT))
        found.sort(key=lambda x: (C.rank(*x), x[0]["id"]))
        for h, g in found:
            kind = "MUST" if C.must_n(h, g) else "introduction" if h["id"] in C.INTRO_GROUP else "should"
            print("  [%s %s] %s  (%d)" % (h["id"], kind, h["title"], len(g)))
            for _, ln, ex in g[:8]:
                print("      l.%-5s %s" % (ln if ln else "-", ex))
            if len(g) > 8:
                print("      ... and %d more" % (len(g) - 8))
            print("      -> " + h["rule"])
        print("  %d MUST findings, %d on the introduction (they count at the push gate), %d other; %d of %d checks fired" % (
            must, intro, sum(len(g) for h, g in found) - must - intro, len(found), len(H.TEXT)))
    if as_json:
        print(json.dumps(report, ensure_ascii=False, indent=1))
    return worst


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
