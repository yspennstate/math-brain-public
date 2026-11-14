# -*- coding: utf-8 -*-
"""pw_run.py - runner of the paper-writing hooks W01..W56 (an agent, 12 Nov 2026).

Wired on PreToolUse (Bash, PowerShell, Edit, Write, MultiEdit, the browser tools) and UserPromptSubmit for Claude, and
with --codex for Codex (which takes a hook's words only as JSON additionalContext). Reads the hook payload on stdin and
prints the hooks that fired; prints nothing when the call has nothing to do with a paper. Never blocks.
  python pw_run.py --list        the hooks
  python pw_run.py --selftest    controls both ways (fires on a bad paper and on paper moments; quiet on a clean paper
                                 and on unrelated calls); touches no live state
"""
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
KEYS = (".tex", ".bib", "latex", "tectonic", "push", "zenodo", "researchgate", "arxiv", "paper", "submi", "sumbit",
        "referee", "reject", "regect", "manuscript", "preprint", "editorialmanager", "manuscriptcentral", "gh release",
        "reviewer", "declin", "scholarone", "springernature", "git commit", "readme")
# a bare `make` in a paper folder names no paper word: let it through when make stands as a command word
MAKE_CMD = re.compile(r'(?:&&|;|\|\||\(|"\s*:\s*"|\\n|"\s*,\s*")\s*make(?:\s|\\|"|$)')


def _out(text, codex, event):
    if not text:
        return
    if codex:
        sys.stdout.write(json.dumps({"hookSpecificOutput": {"hookEventName": event or "PreToolUse",
                                                            "additionalContext": text[:8500]}}))
    else:
        sys.stdout.write(text + "\n")


BAD = r"""\documentclass{amsart}
\title{Extreme least singular values with redundancy, radial ensembles, and quantitative stability of phase retrieval}
\begin{document}
\begin{abstract}
We prove three things: (i) a law; (ii) a bound; (iii) a rate \cite{a}.
\end{abstract}
\maketitle
\section{Introduction}
Random matrices have attracted considerable attention \cite{a,b,c,d,e,f,g}. It is well known that the smallest singular
value is of order one over the square root of the dimension.
The present paper does not use the $r=0$ theorem as a black box. The new ingredients are the rectangular hard-edge exponent
$d_F(r+1)$, a $k=r+1$ marked-row construction, a two-normal estimate for $k$ simultaneous marked constraints, and a
good-overlap/bad-overlap second-moment decomposition that remains uniform in the moderate range. These additions produce
the fixed-redundancy laws below and explain exactly how fixed redundancy changes the stability base.
Gaussianity is not the true source of the exponent! We found no later paper that draws the conclusion; the first version
of this paper presented the operator as new. This was re-derived line by line by Claude in a later session. To be clear,
we do not claim more. Remarkably, this sheds light on the problem, see Lemma~\ref{lem:missing}. TODO check the constant.
\section{The pair-normal proofs}
Short.
\section{Design rule for extra measurements}
Short too.
\end{document}
"""
GOOD = r"""\documentclass{amsart}
\title{The least singular value of a rectangular Gaussian matrix}
\begin{document}
\begin{abstract}
Let $A$ be an $(m+r)\times m$ real Gaussian matrix with $r$ fixed. We determine the limit law of the least singular value
of $A$ over a net of $N$ directions and show that the rate changes from $N^{-1}$ to $N^{-1/(r+1)}$.
\end{abstract}
\maketitle
\section{Introduction}
Let $A$ be an $n\times m$ matrix with independent standard Gaussian entries. Edelman \cite{edelman} computes the law of
the least singular value when $n=m$. Rudelson and Vershynin \cite{rv} prove the bound $s_m(A)\ge c(\sqrt n-\sqrt{m-1})$
with high probability for every $n\ge m$, but their argument does not give the limit law when $n-m$ stays bounded.
We prove that law. The square case is treated in \cite{prior}, where the second moment involves one constraint; here it
involves $r+1$ constraints at once, and the estimate that replaces it is Lemma~\ref{lem:two}.
\begin{theorem}\label{thm:main}
Let $r\ge 0$ be fixed. Then the least singular value satisfies the limit law stated in \eqref{eq:law}.
\end{theorem}
\begin{equation}\label{eq:law} \lim_{m\to\infty} P(m^{1/2} s_m(A) \le t) = 1-e^{-t^{r+1}}. \end{equation}
\begin{lemma}\label{lem:two}
For two independent uniform unit vectors $u,v$ in $R^m$ the angle between them has density proportional to
$\sin^{m-2}\theta$.
\end{lemma}
\begin{thebibliography}{9}
\bibitem{edelman} A. Edelman, Eigenvalues and condition numbers of random matrices, SIAM J. Matrix Anal. Appl. 9 (1988).
\bibitem{rv} M. Rudelson and R. Vershynin, Smallest singular value of a random rectangular matrix, CPAM 62 (2009).
\bibitem{prior} A. Author, The square case, preprint, 2026.
\end{thebibliography}
\end{document}
"""


def selftest():
    import tempfile
    sys.path.insert(0, HERE)
    import pw_core as C
    import pw_hooks as H
    hooks = H.load()
    fails = []

    def ok(name, cond, detail=""):
        print(("PASS " if cond else "FAIL ") + name + ((" - " + detail) if detail and not cond else ""))
        if not cond:
            fails.append(name)

    ok("56 hooks, ids W01..W56", sorted(h["id"] for h in hooks) == ["W%02d" % i for i in range(1, 57)])
    ok("43 text and 13 event hooks", len(H.TEXT) == 43 and len(H.EVENT) == 13)
    tmp = tempfile.mkdtemp(prefix="pwselftest_")
    bad, good = os.path.join(tmp, "bad", "main.tex"), os.path.join(tmp, "good", "main.tex")
    for fp, body in ((bad, BAD), (good, GOOD)):
        os.makedirs(os.path.dirname(fp))
        with open(fp, "w", encoding="utf-8") as f:
            f.write(body)

    def ids(p, state=None):
        fired, ch, text, ctx = C.decide(p, hooks, now=1000.0, state={} if state is None else state)
        return set(h["id"] for h, _ in fired), ch, fired, ctx

    # 1. a new bad paper written whole
    got, ch, fired, ctx = ids({"hook_event_name": "PreToolUse", "tool_name": "Write", "session_id": "t",
                               "tool_input": {"file_path": os.path.join(tmp, "new", "main.tex"), "content": BAD}})
    want = {"W01", "W02", "W03", "W04", "W05", "W06", "W07", "W08", "W09", "W11", "W12", "W13", "W15", "W16", "W17", "W20",
            "W22", "W23", "W24", "W26", "W34", "W39", "W40", "W41", "W50"}
    ok("FIRE bad paper written: the PTRF paragraph and the planted faults", want <= got, "missing %s" % sorted(want - got))
    ok("channels draft+start on a new \\documentclass file", ch == {"draft", "start"}, str(ch))
    out = C.render(fired, ch, ctx, len(hooks))
    ok("render names lines, MUST first, and stays under the cap",
       "l." in out and "black box" in out and " MUST |" in out and len(out) <= C.MAX_OUT and
       out.index(" MUST |") < min(x for x in (out.find(" introduction |"), out.find(" should |"), len(out)) if x >= 0),
       "%d chars" % len(out))
    w16 = [f for h, f in fired if h["id"] == "W16"]
    ok("W16 names the undefined labels of the PTRF paragraph", bool(w16) and "marked-row" in str(w16) and
       "two-normal" in str(w16), str(w16)[:300])
    w17 = [f for h, f in fired if h["id"] == "W17"]
    ok("W17 sees two-normal and pair-normal as one thing", bool(w17) and "pair-normal" in str(w17), str(w17)[:300])
    if "--show" in sys.argv:
        print(out)
    # 2. the clean paper is quiet on every text hook
    got, ch, fired, ctx = ids({"hook_event_name": "PreToolUse", "tool_name": "Write", "session_id": "t2",
                               "tool_input": {"file_path": good, "content": GOOD}})
    ok("QUIET clean paper: no text hook", not [i for i in got if int(i[1:]) <= 38], str(sorted(got)))
    # 3. an Edit that adds one self-referential sentence
    got, ch, _, _ = ids({"hook_event_name": "PreToolUse", "tool_name": "Edit", "session_id": "t3",
                         "tool_input": {"file_path": good, "old_string": "x",
                                        "new_string": "This paper is not intended to be a survey, and an earlier draft "
                                                      "of this paper has been revised."}})
    ok("FIRE edit adds self-narration (W01, W02)", {"W01", "W02"} <= got and ch == {"draft"}, str(sorted(got)))
    got, ch, _, _ = ids({"hook_event_name": "PreToolUse", "tool_name": "Edit", "session_id": "t3b",
                         "tool_input": {"file_path": good, "old_string": "\\end{document}",
                                        "new_string": "By Lemma~\\ref{lem:two} the angle has a density, which gives the bound."
                                                      "\n\\end{document}"}})
    ok("QUIET edit adds a plain mathematical sentence", not got, str(sorted(got)))
    # 4. compile, push, upload, submit, prompt moments
    got, ch, _, _ = ids({"hook_event_name": "PreToolUse", "tool_name": "Bash", "session_id": "t4", "cwd": os.path.dirname(bad),
                         "tool_input": {"command": "pdflatex -interaction=nonstopmode main.tex"}})
    ok("FIRE compile of the bad paper (W42 and text hooks)", "W42" in got and "W01" in got and ch == {"compile"},
       str(sorted(got)))
    got, ch, _, _ = ids({"hook_event_name": "PreToolUse", "tool_name": "Bash", "session_id": "t5", "cwd": os.path.dirname(bad),
                         "tool_input": {"command": "git add main.tex && git commit -m x && git push origin main"}})
    ok("FIRE push of a paper folder (W43 no audit, W49 MUST count, W45, W50)", {"W43", "W49", "W45", "W50"} <= got,
       str(sorted(got)))
    # the audit gate reads the verdict on record for the text as it stands, never the presence of a file
    note = os.path.join(os.path.dirname(good), "AUDIT_2026-11-12.md")
    with open(note, "w", encoding="utf-8") as f:
        f.write("audit")
    H.AUDIT_INDEX = os.path.join(tmp, "audit_index.json")
    gkey = os.path.abspath(good).replace("\\", "/").lower()

    def push_good(sid, rec):
        with open(H.AUDIT_INDEX, "w", encoding="utf-8") as f:
            json.dump({gkey: rec} if rec else {}, f)
        return ids({"hook_event_name": "PreToolUse", "tool_name": "Bash", "session_id": sid,
                    "cwd": os.path.dirname(good), "tool_input": {"command": "git push origin main"}})

    got, ch, _, _ = push_good("t6a", None)
    ok("FIRE W43 when a file named AUDIT lies beside the paper and no audit is on record", "W43" in got, str(sorted(got)))
    sha = C.paper_sha(good)
    got, ch, _, _ = push_good("t6b", {"report": note, "tex_sha": sha,
                                      "verdict": "VERDICT: NOT READY  |  MUST-FIX: 4  |  SHOULD-FIX: 9"})
    ok("FIRE W43 when the audit on record says NOT READY", "W43" in got, str(sorted(got)))
    got, ch, _, _ = push_good("t6c", {"report": note, "tex_sha": "0" * 64,
                                      "verdict": "VERDICT: SEND AS IS  |  MUST-FIX: 0  |  SHOULD-FIX: 1"})
    ok("FIRE W43 when the paper changed after its audit", "W43" in got, str(sorted(got)))
    got, ch, _, _ = push_good("t6", {"report": note, "tex_sha": sha,
                                     "verdict": "VERDICT: SEND AS IS  |  MUST-FIX: 0  |  SHOULD-FIX: 1"})
    ok("QUIET W43 and W49 on a clean paper whose audit says SEND AS IS for this text",
       "publish" in ch and not ({"W43", "W49"} & got), str(sorted(got)))
    got, ch, _, _ = ids({"hook_event_name": "PreToolUse", "tool_name": "Bash", "session_id": "t7", "cwd": tmp,
                         "tool_input": {"command": "git push origin main"}})
    ok("QUIET push from a folder with no paper", not ch and not got, str(ch))
    got, ch, _, _ = ids({"hook_event_name": "PreToolUse", "tool_name": "mcp__claude-in-chrome__navigate", "session_id": "t8",
                         "tool_input": {"url": "https://www.researchgate.net/publication/411189885_Extreme"}})
    ok("QUIET reading a ResearchGate page", not ch, str(ch))
    got, ch, _, _ = ids({"hook_event_name": "PreToolUse", "tool_name": "mcp__claude-in-chrome__navigate", "session_id": "t9",
                         "tool_input": {"url": "https://zenodo.org/uploads/new"}})
    ok("FIRE opening the Zenodo upload page", ch == {"publish"} and "W45" in got, str(sorted(got)))
    got, ch, _, _ = ids({"hook_event_name": "PreToolUse", "tool_name": "mcp__claude-in-chrome__navigate", "session_id": "t10",
                         "tool_input": {"url": "https://arxiv.org/submit/123/start"}})
    ok("FIRE arXiv submission page (W44 the journal is his)", "submit" in ch and "W44" in got, str(sorted(got)))
    got, ch, _, _ = ids({"hook_event_name": "UserPromptSubmit", "session_id": "t11",
                         "prompt": "take a look at the regection email i got today from a publication"})
    ok("FIRE his prompt about a rejection (W47)", ch == {"reject"} and got == {"W47"}, str(sorted(got)))
    got, ch, _, _ = ids({"hook_event_name": "UserPromptSubmit", "session_id": "t12",
                         "prompt": "write a paper on the new singular value result and post it"})
    ok("FIRE his prompt to write a paper (W39, W40, W41)", {"W39", "W40", "W41"} <= got, str(sorted(got)))
    for name, p in (
            ("a loop prompt", {"hook_event_name": "UserPromptSubmit", "prompt": "/loop fire this every 5 minutes; write papers"}),
            ("a continuation summary", {"hook_event_name": "UserPromptSubmit",
                                        "prompt": "This session is being continued from a previous conversation. referee paper"}),
            ("an unrelated prompt", {"hook_event_name": "UserPromptSubmit", "prompt": "check the rebalancing bots tonight"}),
            ("a brain memory about a paper", {"hook_event_name": "PreToolUse", "tool_name": "Bash", "tool_input": {
                "command": "python ~/.claude/dreaming/brain.py remember ptrf_rejection --desc \"referee rejected the paper\""}}),
            ("ls", {"hook_event_name": "PreToolUse", "tool_name": "Bash", "tool_input": {"command": "ls -la"}}),
            ("a Write of a python file", {"hook_event_name": "PreToolUse", "tool_name": "Write",
                                          "tool_input": {"file_path": "C:/x/y.py", "content": "This paper does not"}}),
            ("an edit of a hook file", {"hook_event_name": "PreToolUse", "tool_name": "Write", "tool_input": {
                "file_path": "~/.claude/dreaming/paper_writing_hooks/x.tex", "content": BAD}})):
        p["session_id"] = "q"
        got, ch, _, _ = ids(p)
        ok("QUIET " + name, not ch and not got, str(ch))
    # 5. cool-down, the runner's own path, the Codex form
    st = {}
    p = {"hook_event_name": "PreToolUse", "tool_name": "Edit", "session_id": "cd",
         "tool_input": {"file_path": good, "old_string": "x", "new_string": "This paper does not claim novelty."}}
    a, _, _, _ = ids(p, st)
    b, _, _, _ = ids(p, st)
    ok("cool-down: the same finding is not repeated at once", "W01" in a and "W01" not in b, "%s then %s" % (a, b))
    d = C.Doc(BAD, bad)
    n, mids, n2, iids = H.must_count([d])
    ok("the lint counts MUST findings on the bad paper", n >= 8 and "W01" in mids, "%d %s" % (n, mids))
    ok("the PTRF paragraph's labels are MUST on the first pages (W16)", "W16" in mids, "%s / %s" % (mids, iids))
    n, mids, n2, iids = H.must_count([C.Doc(GOOD, good)])
    ok("the lint is clean on the good paper", n == 0 and n2 == 0, "%d %s %d %s" % (n, mids, n2, iids))
    # 6. the audit of 12 Nov (F03-F06): a paper in several files, one lemma printed again, a long file, his own
    #    earlier paper in the references
    sp = os.path.join(tmp, "split")
    os.makedirs(os.path.join(sp, "sections"))
    with open(os.path.join(sp, "main.tex"), "w", encoding="utf-8") as f:
        f.write("\\documentclass{amsart}\n\\title{A split paper}\n\\begin{document}\n\\maketitle\n"
                "\\input{sections/intro}\n\\end{document}\n")
    with open(os.path.join(sp, "sections", "intro.tex"), "w", encoding="utf-8") as f:
        f.write("\\section{Introduction}\nThe present paper does not use the earlier theorem as a black box.\n")
    d = C._read_doc(os.path.join(sp, "main.tex"))
    got = C.scan(H.TEXT[0], [d])
    ok("a paper split over \\input files is read whole; the finding names the file and its line",
       d.files == 2 and bool(got) and got[0][1] == 2 and "intro.tex" in got[0][2], str(got)[:200])
    ok("the main file of a section file is found",
       (C.find_main(os.path.join(sp, "sections", "intro.tex")) or "").endswith("main.tex"))
    got, ch, _, _ = ids({"hook_event_name": "PreToolUse", "tool_name": "Bash", "session_id": "sp", "cwd": sp,
                         "tool_input": {"command": "git push origin main"}})
    ok("FIRE push of a split paper: the section file's sentence is seen (W01, W49)", {"W01", "W49"} <= got, str(sorted(got)))
    big = ("\\documentclass{amsart}\n\\begin{document}\nThe present paper does not use the earlier theorem as a black "
           "box.\n" + ("Let $x$ be a point of the set. " * 30 + "\n") * 800 + "\\end{document}\n")
    with open(os.path.join(tmp, "big.tex"), "w", encoding="utf-8") as f:
        f.write(big)
    d = C._read_doc(os.path.join(tmp, "big.tex"))
    ok("a file over 600,000 bytes is read", len(big) > 600000 and d is not None and bool(C.scan(H.TEXT[0], [d])),
       "%d bytes" % len(big))
    lem = ("\\begin{lemma}\\label{lem:slab}\nLet $u,v\\in S^{n-1}$ and $0<\\varepsilon<1$. Then\n\\[\n"
           "\\mathbb{P}\\bigl(|\\langle g,u\\rangle|\\le\\varepsilon,\\ |\\langle g,v\\rangle|\\le\\varepsilon\\bigr)"
           "\\le \\frac{C\\varepsilon^{2}}{\\sqrt{1-\\langle u,v\\rangle^{2}}}.\n\\]\n\\end{lemma}\n\\begin{proof}\n"
           "Write $v=\\langle u,v\\rangle u+\\sqrt{1-\\langle u,v\\rangle^{2}}\\,w$ with $w\\perp u$. The pair "
           "$(\\langle g,u\\rangle,\\langle g,w\\rangle)$ is standard Gaussian in $\\mathbb{R}^{2}$, and the event is "
           "contained in a parallelogram of area $4\\varepsilon^{2}/\\sqrt{1-\\langle u,v\\rangle^{2}}$.\n\\end{proof}\n")
    old = C.Doc("\\documentclass{amsart}\n\\begin{document}\n" + lem + "\\end{document}\n", "old.tex")
    new = C.Doc("\\documentclass{amsart}\n\\begin{document}\nSome text first.\n" + lem.replace("lem:slab", "lem:two")
                .replace("\\bigl", "\\left").replace("\\bigr", "\\right") + "\\end{document}\n", "new.tex")
    other = C.Doc("\\documentclass{amsart}\n\\begin{document}\n" + lem.replace("\\varepsilon", "\\delta")
                  .replace("\\langle g,u\\rangle", "X_1").replace("parallelogram", "strip") + "\\end{document}\n", "o.tex")
    ou, runs = C.unit_list(old), {}
    for i, u in enumerate(ou):
        for k in u[3]:
            runs.setdefault(k, []).append(i)
    m = C.unit_matches(C.unit_list(new), lambda k: runs.get(k, ()))
    ok("one lemma printed again, formulas included, is found (labels and \\left/\\bigl do not hide it)", len(m) == 2,
       "%d units of %d" % (len(m), len(C.unit_list(new))))
    m = C.unit_matches(C.unit_list(other), lambda k: runs.get(k, ()))
    ok("a lemma of the same shape with other formulas is not called a reprint", not m, str(len(m)))
    w19 = [h for h in H.TEXT if h["id"] == "W19"][0]
    own = ("\\documentclass{amsart}\n\\title{T}\n\\author{Jane Roe}\n\\begin{document}\n\\maketitle\n"
           "\\section{Introduction}\n" + "We study random matrices and their least singular values in some detail. " * 70 +
           "\n\\section{Proofs}\nText.\n\\begin{thebibliography}{9}\n\\bibitem{R1} J. Roe, The square case, 2025.\n"
           "\\bibitem{S} A. Smith, Another paper, 2020.\n\\end{thebibliography}\n\\end{document}\n")
    got = C.scan(w19, [C.Doc(own, "own.tex")])
    ok("W19 is a MUST when the author's own earlier paper is in the references and the introduction is silent on it",
       bool(got) and got[0][2].startswith(C.MUST_TAG) and "R1" in got[0][2] and "S)" not in got[0][2], str(got)[:200])
    own2 = own.replace("\n\\section{Proofs}", " The square case was proved in \\cite{R1}; that argument fails for "
                       "rectangular matrices.\n\\section{Proofs}")
    got = C.scan(w19, [C.Doc(own2, "own.tex")])
    ok("W19 is not a MUST once a sentence says what the earlier paper proved and where it stops",
       not any(x[2].startswith(C.MUST_TAG) for x in got), str(got)[:200])
    pat = "*** Begin Patch\n*** Update File: %s\n@@\n+The present paper does not use this as a black box.\n*** End Patch" % good
    got, ch, _, _ = ids({"hook_event_name": "PreToolUse", "tool_name": "apply_patch", "session_id": "cx",
                         "tool_input": {"input": pat}})
    ok("FIRE a Codex apply_patch that adds self-narration", "W01" in got and ch == {"draft"}, str(sorted(got)))
    got, ch, _, _ = ids({"hook_event_name": "PreToolUse", "tool_name": "apply_patch", "session_id": "cx2",
                         "tool_input": {"command": ["apply_patch", pat]}})
    ok("FIRE the same patch handed over as a list", "W01" in got and ch == {"draft"}, str(sorted(got)))
    # command shapes that printed nothing before (a bare make, a list command, a commit message)
    pdir = os.path.dirname(good).replace("\\", "/")
    for name, cmd in (("cd && make", "cd %s && make" % pdir),
                      ("a list command", ["bash", "-lc", "cd %s && latexmk -pdf main.tex" % pdir])):
        p = {"hook_event_name": "PreToolUse", "tool_name": "Bash", "session_id": "sh" + name[:2],
             "tool_input": {"command": cmd}}
        _, ch, _, _ = ids(p)
        low = json.dumps(p).lower()
        ok("compile channel on %s" % name, "compile" in ch, str(ch))
        ok("the runner lets %s through to the engine" % name, any(k in low for k in KEYS) or bool(MAKE_CMD.search(low)))
    ok("the runner stays shut on an unrelated command",
       not MAKE_CMD.search(json.dumps({"tool_input": {"command": "python build.py && echo makefile done"}}).lower()))
    got, ch, _, _ = ids({"hook_event_name": "PreToolUse", "tool_name": "Bash", "session_id": "cm1", "tool_input": {
        "command": "cd %s && git add main.tex && git commit -m \"Polish the introduction; fix AI tells; rerun audit\"" % pdir}})
    ok("FIRE W56 on a commit message that describes the editing", "W56" in got and "commit" in ch,
       "%s %s" % (sorted(got), ch))
    got, ch, _, _ = ids({"hook_event_name": "PreToolUse", "tool_name": "Bash", "session_id": "cm2", "tool_input": {
        "command": "cd %s && git add main.tex && git commit -m \"fix section heading\"" % pdir}})
    ok("QUIET W56 on a short plain commit message", "W56" not in got, str(sorted(got)))
    w51 = [h for h in H.TEXT if h["id"] == "W51"][0]
    got = C.scan(w51, [C.Doc(own, "own.tex")])
    ok("W51 is a MUST twice on a paper with no funding statement and no AI declaration",
       len([x for x in got if x[2].startswith(C.MUST_TAG)]) == 2, str(got)[:300])
    full = own.replace("\\begin{thebibliography}", "\\section*{Funding}\nThe author received no funding for this work.\n"
                       "\\section*{Use of AI tools}\nDrafts of the proofs were produced with Claude (Anthropic) and "
                       "checked by the author.\n\\begin{thebibliography}")
    got = C.scan(w51, [C.Doc(full, "own.tex")])
    ok("W51 has no MUST once both statements stand in the paper", not any(x[2].startswith(C.MUST_TAG) for x in got),
       str(got)[:300])
    own3 = own.replace("J. Roe, The square case, 2025.", "J. Roe, Supplementary code and data for this paper, 2026.")
    got = C.scan(w19, [C.Doc(own3, "own.tex")])
    ok("W19 leaves out the paper's own supplementary material", not any(x[2].startswith(C.MUST_TAG) for x in got),
       str(got)[:200])
    own4 = own.replace("\\begin{thebibliography}", "\\section*{Use of AI tools}\nThe proofs were drafted with the "
                       "system of \\cite{R1} and checked by the author.\n\\begin{thebibliography}")
    got = C.scan(w19, [C.Doc(own4, "own.tex")])
    ok("W19 leaves out an own entry cited only in the AI declaration", not any(x[2].startswith(C.MUST_TAG) for x in got),
       str(got)[:200])
    own5 = own4.replace("in some detail. ", "in some detail \\cite{R1}. ", 1)
    got = C.scan(w19, [C.Doc(own5, "own.tex")])
    ok("W19 still a MUST when that entry is also cited in the body without a comparison",
       bool(got) and got[0][2].startswith(C.MUST_TAG), str(got)[:200])
    # held-out rewordings written by the auditor and never read for patterns: how many hooks see anything in them
    held = os.environ.get("PW_HELDOUT_DIR") or ("~/brain-repo/12_cognitive_architecture/"
                                                "audits/reports/2026/11/12/paper_writing_hooks_audit/tests")
    for nm in ("t08_heldout_second_paraphrase.tex", "t10_heldout_third_paraphrase.tex"):
        fp = os.path.join(held, nm)
        if os.path.isfile(fp):
            try:
                doc = C._read_doc(fp)
                n = len([h for h in H.TEXT if C.scan(h, [doc])])
                print("info  held-out %s: %d of %d text hooks report something (a count, not a pass)" % (nm, n, len(H.TEXT)))
            except Exception as e:  # noqa: BLE001
                print("info  held-out %s: not read (%s)" % (nm, e))
    try:
        import shutil
        shutil.rmtree(tmp, ignore_errors=True)
    except Exception:  # noqa: BLE001
        pass
    print("ALL PASS" if not fails else "FAILED: %d (%s)" % (len(fails), "; ".join(fails)))
    return 0 if not fails else 1


def main(argv):
    for s in (sys.stdout, sys.stderr):
        try:
            s.reconfigure(encoding="utf-8", errors="replace")
        except Exception:  # noqa: BLE001
            pass
    if "--selftest" in argv:
        return selftest()
    if "--list" in argv:
        sys.path.insert(0, HERE)
        import pw_hooks as H
        for h in H.load():
            when = "+".join(h["on"]) if h["kind"] == "event" else ("text, whole paper" if h["kind"] == "doc" else "text")
            print("%s  %-6s %-18s %s" % (h["id"], "MUST" if h.get("must") else "", when, h["title"]))
        return 0
    try:
        src = getattr(sys.stdin, "buffer", None)  # the dispatcher's in-process stdin is text only
        raw = src.read().decode("utf-8", "replace") if src is not None else sys.stdin.read()
    except Exception:  # noqa: BLE001
        return 0
    low = raw.lower()
    if not any(k in low for k in KEYS) and not MAKE_CMD.search(low):
        return 0
    try:
        sys.path.insert(0, HERE)
        import pw_core as C
        import pw_hooks as H
        text, p = C.run_payload(raw, H.load)
        _out(text, "--codex" in argv, str(p.get("hook_event_name") or ""))
    except Exception as e:  # noqa: BLE001
        sys.stderr.write("[paper-writing hooks] error: %s\n" % e)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
