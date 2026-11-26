# -*- coding: utf-8 -*-
"""Self-test for pw1k.py (author an agent, 12 Nov 2026).  `python pw1k.py selftest` -> 0 when every check passes.

It touches nothing live: the hook state and the fire log go to a temporary folder for the run.
"""
import json
import os
import re
import shutil
import sys
import tempfile

BAD = r"""\documentclass{amsart}
\usepackage{amsmath}
\usepackage{amsmath}
\newtheorem{theorem}{Theorem}
\newtheorem{lemma}{Theorem}
\newtheorem{proposition}{Proposition}
\newcommand{\RR}{\mathbb{R}}
\title{A paper with every fault}
\author{A. Author}
\begin{document}
\begin{abstract}
We study the window of a chain.
\end{abstract}
\maketitle
\section{Introduction}
The window $W$ is a set of states and the window $W$ is finite. Later the band $W$ is used again, the band $W$ is long, and the block $W$ once more.
The time-step is small and the timestep is fixed. We use the window and the band of the chain throughout.
Each window has a width and each band has a width.
We write $Q_\ell$ and $Q_\ell$ again with $\mathbb{R}$ and $\RR$.
\begin{lemma}\label{lem:a}
For all $n$ we have $n\ge 0$.
\end{lemma}
\begin{theorem}\label{lem:a}
For all $n$ we have $n\ge 1$.
\end{theorem}
By Theorem~\ref{prop:b} the claim follows.
\begin{proposition}\label{prop:b}
The window is finite.
\end{proposition}
\section{Results}
The band is finite.
\end{document}
"""

CLEAN = r"""\documentclass{amsart}
\usepackage{amsmath}
\newtheorem{theorem}{Theorem}[section]
\newtheorem{lemma}[theorem]{Lemma}
\title{Occupation sums of a descent chain}
\author{A. Author}
\subjclass{60J10}
\keywords{Markov chain}
\begin{document}
\begin{abstract}
We bound the number of visits of a descent chain to a set of states.
\end{abstract}
\maketitle
\section{Introduction}\label{sec:intro}
Let $n$ be a positive integer and let $h_n$ denote the $n$th harmonic number. The chain starts at $n$ and moves down.
Theorem~\ref{thm:main} gives the bound, and Lemma~\ref{lem:step} is the step used in its proof.
\begin{theorem}\label{thm:main}
For every positive integer $n$ the expected number of visits is at most $h_n$.
\end{theorem}
\section{Proof}\label{sec:proof}
\begin{lemma}\label{lem:step}
For every positive integer $n$ we have $h_n \ge 1$.
\end{lemma}
\begin{proof}
The first term of the sum defining $h_n$ equals one, and the other terms are positive.
\end{proof}
\begin{proof}[Proof of Theorem~\ref{thm:main}]
Apply Lemma~\ref{lem:step} at each step of the chain and add the bounds.
\end{proof}
\end{document}
"""

BIB = r"""@article{a1,
  author = {A. Author},
  title = {A title of some length here},
  journal = {Ann. Probab.},
  year = {2020},
}
@article{a2,
  author = {B. Author},
  title = {Another title of some length},
  journal = {Journal of Something},
}
"""


def run():
    import pw1k as E
    import pw1k_detect as D
    import pw1k_rules as Rm
    fails, notes = [], []

    def check(name, ok, detail=""):
        (notes if ok else fails).append("%s %s %s" % ("ok  " if ok else "FAIL", name, detail))

    R = E.rules()
    kinds = {}
    for r in R:
        kinds[r["kind"]] = kinds.get(r["kind"], 0) + 1
    check("count", len(R) >= 1000, "%d rules (%s)" % (len(R), ", ".join("%s %d" % kv for kv in sorted(kinds.items()))))
    ids = [r["id"] for r in R]
    check("ids unique", len(set(ids)) == len(ids))
    check("ids in order", ids == ["P%04d" % (i + 1) for i in range(len(ids))], "first %s last %s" % (ids[0], ids[-1]))
    texts = [r["text"] for r in R if r["kind"] != "cluster"]
    dup = sorted(set(t for t in texts if texts.count(t) > 1))
    check("texts unique", not dup, "%d repeated: %s" % (len(dup), "; ".join(d[:50] for d in dup[:3])) if dup else "")
    check("texts short", all(len(t) <= 300 for t in texts), "longest %d" % max(len(t) for t in texts))
    missing = [name for name, _, _, _ in Rm.FN if not callable(getattr(D, name, None))]
    check("detectors exist", not missing, ", ".join(missing[:6]))
    extra = [n for n in dir(D) if n.startswith("fn_") and n not in set(x[0] for x in Rm.FN)]
    check("no orphan detectors", not extra, ", ".join(extra[:6]))
    chans = set(c for c, _ in Rm.EVENTS)
    check("event channels", chans <= {"draft", "bib", "compile", "publish"}, ",".join(sorted(chans)))

    docs = {"bad": E.Doc(text=BAD, name="bad.tex"), "clean": E.Doc(text=CLEAN, name="clean.tex"),
            "bib": E.Doc(text=BIB, name="refs.bib"), "empty": E.Doc(text="", name="empty.tex"),
            "frag": E.Doc(text="Some loose text with $x$ and no preamble.\n", name="frag.tex")}
    raised = []
    for dn, doc in docs.items():
        for r in R:
            try:
                if r["kind"] == "cluster":
                    E.run_cluster(r, doc)
                elif r["kind"] == "rx":
                    E.run_rx(r, doc)
                elif r["kind"] == "gloss":
                    E.run_gloss(r, doc)
                elif r["kind"] == "fn":
                    h = getattr(D, r["fn"])(doc)
                    if h is not None and not (isinstance(h, tuple) and len(h) == 2 and isinstance(h[0], int)):
                        raised.append("%s on %s returned %r" % (r["fn"], dn, h))
            except Exception as e:
                raised.append("%s on %s: %r" % (r.get("fn") or r["id"], dn, e))
    check("no rule raises", not raised, "%d: %s" % (len(raised), " | ".join(raised[:5])) if raised else "5 documents x %d rules" % len(R))

    F = E.lint(docs["bad"])
    fired_fn = set(r["fn"] for r in R if r["kind"] == "fn" and r["id"] in set(f[2] for f in F))
    for want in ("fn_object_names", "fn_label_duplicate", "fn_ref_kind", "fn_env_prints_other_kind", "fn_pkg_twice",
                 "fn_hyphen_compound_mixed", "fn_macro_bypass", "fn_theorem_counters"):
        check("bad sample fires " + want, want in fired_fn)
    check("bad sample fires a word cluster", any(f[3] == "terms" and f[2] in set(r["id"] for r in R if r["kind"] == "cluster") for f in F),
          "%d findings" % len(F))
    check("findings sorted by weight", [f[0] for f in F] == sorted([f[0] for f in F], reverse=True))
    check("offsets resolve to lines", all(re.match(r"(l\.\d+|\S+:\d+)$", docs["bad"].line(f[1])) for f in F))

    C = E.lint(docs["clean"])
    cl = [f for f in C if f[2] in set(r["id"] for r in R if r["kind"] == "cluster")]
    check("clean sample fires no word cluster", not cl, "; ".join("%s %s" % (f[2], f[4][:60]) for f in cl[:3]))
    heavy = [f for f in C if f[0] >= 7]
    check("clean sample fires nothing heavy", not heavy, "; ".join("%s %s" % (f[2], f[4][:70]) for f in heavy[:4]))
    check("clean sample is quiet", len(C) <= 6, "%d findings: %s" % (len(C), "; ".join("%s %s" % (f[2], f[4][:50]) for f in C[:8])))
    check("empty and fragment are quiet", len(E.lint(docs["empty"])) == 0 and len(E.lint(docs["frag"])) <= 2,
          "%d and %d" % (len(E.lint(docs["empty"])), len(E.lint(docs["frag"]))))

    tmp = tempfile.mkdtemp(prefix="pw1k_selftest_")
    keep = (E.STATE_DIR, E.FIRES)
    try:
        E.STATE_DIR, E.FIRES = tmp, os.path.join(tmp, "fires.jsonl")
        pay = {"hook_event_name": "PreToolUse", "tool_name": "Write", "session_id": "selftest", "cwd": tmp,
               "tool_input": {"file_path": os.path.join(tmp, "bad.tex"), "content": BAD}}
        out = E.hook(json.dumps(pay), now=1000000.0)
        check("hook speaks on a paper", out.startswith("[paper-1k]"), out[:60].replace("\n", " "))
        check("hook output is short", 0 < len(out) <= E.MAX_OUT, "%d chars" % len(out))
        out2 = E.hook(json.dumps(pay), now=1000060.0)
        ids1, ids2 = set(re.findall(r"\bP\d{4}\b", out)), set(re.findall(r"\bP\d{4}\b", out2))
        check("hook does not repeat a rule inside the cooldown", not (ids1 & ids2), "%d repeated" % len(ids1 & ids2))
        pay["session_id"] = "selftest-codex"
        oc = E.hook(json.dumps(pay), codex=True, now=1000000.0)
        try:
            j = json.loads(oc)
            okc = j["hookSpecificOutput"]["additionalContext"].startswith("[paper-1k]") and j["hookSpecificOutput"]["hookEventName"] == "PreToolUse"
        except Exception:
            okc = False
        check("codex output is the JSON shape", okc)
        quiet = {"hook_event_name": "PreToolUse", "tool_name": "Write", "session_id": "selftest",
                 "tool_input": {"file_path": os.path.join(tmp, "notes.py"), "content": "x = 1\n"}}
        check("hook is silent off a paper", E.hook(json.dumps(quiet), now=1000000.0) == "")
        quiet["tool_input"] = {"command": "git status"}
        quiet["tool_name"] = "Bash"
        check("hook is silent on an ordinary command", E.hook(json.dumps(quiet), now=1000000.0) == "")
        check("hook survives junk input", E.hook("not json", now=1.0) == "" and E.hook("", now=1.0) == "")
        comp = {"hook_event_name": "PreToolUse", "tool_name": "Bash", "session_id": "selftest-c", "cwd": tmp,
                "tool_input": {"command": "pdflatex -interaction=nonstopmode main.tex"}}
        oe = E.hook(json.dumps(comp), now=1000000.0)
        check("compile event line", oe.startswith("[paper-1k]") and len(oe) <= E.MAX_OUT, oe[:50].replace("\n", " "))
    except Exception as e:
        check("hook runs", False, repr(e))
    finally:
        E.STATE_DIR, E.FIRES = keep
        shutil.rmtree(tmp, ignore_errors=True)

    ws = E._prose_ws(r"a (?: b| c)? [ x] d ?e(?<!x y)")
    w1 = E._WS1
    check("prose space becomes whitespace", ws == "a" + w1 + "(?:" + w1 + "b|" + w1 + "c)?" + w1 + "[ x]" + w1 + r"d\s?e(?<!x\sy)", ws)
    check("prose space stops at a paragraph break", re.fullmatch(w1, " \n  ") and not re.fullmatch(w1, "\n\n"))
    bad_rx = []
    for r in R:
        if r["kind"] == "rx" and r["scope"].islower():
            try:
                re.compile(E._prose_ws(r["rx"]))
            except re.error as e:
                bad_rx.append("%s %s" % (r["id"], e))
    check("every widened prose rule compiles", not bad_rx, "; ".join(bad_rx[:4]))
    p813 = [r for r in R if r["id"] == "P0813"]
    if p813:
        brk = E.Doc(text="\\documentclass{article}\\begin{document}\nThe bound (see\nbelow) holds.\n\\end{document}\n",
                    name="brk.tex")
        check("prose rule matches across a line break", E.run_rx(p813[0], brk) is not None)

    # 24 Nov: a research statement is not a paper - no roadmap / notation appendix / theorem-in-intro demand on it;
    # the same text with an abstract, or named like a paper, still gets them.
    secs = "".join("\\section{Part %s}\nThe argument in this part is about random matrices.\n" % c for c in "BCDEF")
    stmt = ("\\documentclass{article}\\newtheorem{theorem}{Theorem}\\title{Research Statement}\\begin{document}\\maketitle\n"
            "\\section{Introduction}\nMy work is on random matrices and the stability of fixed points.\n" + secs.replace(
                "Part B}\n", "Part B}\n\\begin{theorem}Every orbit converges.\\end{theorem}\n", 1) + "\\end{document}\n")
    want = {"fn_roadmap", "fn_intro_no_statement"}

    def _fns(doc):
        return {r.get("fn") for r in R if r["id"] in {f[2] for f in E.lint(doc)}} & want
    sd = E.Doc(text=stmt, name="main.tex")
    check("statement is an application doc", E.application_doc(sd))
    check("statement gets no paper-structure rules", not _fns(sd), ",".join(sorted(_fns(sd))))
    pd = E.Doc(text=stmt.replace("Research Statement", "Fixed points of random maps").replace(
        "\\maketitle", "\\maketitle\\begin{abstract}We prove a bound.\\end{abstract}"), name="main.tex")
    check("paper with an abstract is not an application doc", not E.application_doc(pd))
    check("the same text as a paper gets them (control)", _fns(pd) == want, ",".join(sorted(_fns(pd))))
    pp = E.Doc(text=stmt.replace("Research Statement", "Fixed points of random maps"), name="paper.tex")
    check("paper without an abstract is not an application doc", not E.application_doc(pp))

    rows = E.notation_rows(docs["clean"])
    check("notation rows", any(r[1] == "h" for r in rows), "%d rows: %s" % (len(rows), ", ".join(r[1] for r in rows[:6])))

    for line in notes + fails:
        print(line)
    print("pw1k selftest: %d passed, %d failed, %d rules" % (len(notes), len(fails), len(R)))
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(run())
