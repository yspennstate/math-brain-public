# -*- coding: utf-8 -*-
"""pw_run.py - runner of the paper-writing hooks W01..W73 (an agent, 12 Nov 2026).

Wired on PreToolUse (Bash, PowerShell, Edit, Write, MultiEdit, the browser tools) and UserPromptSubmit for Claude, and
with --codex for Codex (which takes a hook's words only as JSON additionalContext). Reads the hook payload on stdin and
prints the hooks that fired; prints nothing when the call has nothing to do with a paper.
Blocks in one case only: pdf_kind_gate.py beside this file (an optional reference-kind gate, not shipped here) runs first on
Bash/PowerShell/browser-upload calls, and with its LIVE file present a paper PDF that prints 'Theorem 2.1' for a
Lemma (or has no verdict, at a paper door) is denied: stdout is then ONE JSON object, the paper hooks' text folded
into the reason. Without LIVE it is a note and a row in would_deny.jsonl. A gate error or a missing gate file is
a note or nothing, never a deny. Codex only ever gets the note.
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



def _gate(raw):
    """The reference-kind gate's hookSpecificOutput dict, or None. Fails open: any error is a note, never a deny."""
    try:
        p = json.loads(raw or "{}")
    except Exception:  # noqa: BLE001
        return None
    if not isinstance(p, dict) or str(p.get("hook_event_name") or "PreToolUse") != "PreToolUse":
        return None
    tool = str(p.get("tool_name") or "")
    if tool not in ("Bash", "PowerShell") and not tool.endswith("file_upload"):
        return None
    if not os.path.isfile(os.path.join(HERE, "pdf_kind_gate.py")):
        return None
    try:
        if HERE not in sys.path:
            sys.path.insert(0, HERE)
        import pdf_kind_gate as G
        out, row = G.decide(p)
        if row:
            try:
                with open(G.LOG, "a", encoding="utf-8") as f:
                    f.write(json.dumps(row) + "\n")
            except OSError:
                pass
        return (out or {}).get("hookSpecificOutput") or None
    except Exception as e:  # noqa: BLE001
        return {"hookEventName": "PreToolUse", "additionalContext": "[pdf-kind-gate] the reference-kind gate failed "
                "(%s: %s), so NOTHING was checked; run tex_ship_gate.py --pdf on each PDF before posting." % (
                    type(e).__name__, str(e)[:200])}


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

    ok("73 hooks, ids W01..W73", sorted(h["id"] for h in hooks) == ["W%02d" % i for i in range(1, 74)])
    ok("50 text and 23 event hooks", len(H.TEXT) == 50 and len(H.EVENT) == 23, "%d %d" % (len(H.TEXT), len(H.EVENT)))
    tmp = tempfile.mkdtemp(prefix="pwselftest_")
    sub0 = os.path.join(tmp, "SUBS0.jsonl")               # the live record of submissions is not read by this test
    with open(sub0, "w", encoding="utf-8") as f:
        f.write(json.dumps({"rid": "S0001", "title": "An unrelated closed paper", "journal": "ALEA",
                            "status": "declined", "checked": "2099-01-01"}) + "\n")
    os.environ["PW_SUBMISSIONS"] = sub0
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
                         "prompt": "please read the regection letter that came back from the journal this morning"})
    ok("FIRE a prompt about a rejection, misspelled (W47, and W69 the answer is recorded)", ch == {"reject"} and
       got == {"W47", "W69"}, str(sorted(got)))
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
    # 24 Nov: a teaching or research statement may have AI as its subject; process words stay MUST; a paper is a paper
    w04 = [h for h in H.TEXT if h["id"] == "W04"][0]
    st = ("\\documentclass{article}\\begin{document}\\begin{center}Statement of teaching philosophy\\end{center}\n"
          "Students now have AI systems that will write a proof on request, and language models are part of the course.\n"
          "\\end{document}\n")
    ok("QUIET W04 on a teaching statement whose subject is AI", not C.scan(w04, [C.Doc(st, "ts/Teaching_Statement.tex")]),
       str(C.scan(w04, [C.Doc(st, "ts/Teaching_Statement.tex")]))[:200])
    st2 = st.replace("are part of the course.", "are part of the course. An audit agent found the error in a session.")
    ok("FIRE W04 MUST on process words in a statement", any(x[2].startswith(C.MUST_TAG) for x in
                                                            C.scan(w04, [C.Doc(st2, "ts/Teaching_Statement.tex")])), "")
    pap = ("\\documentclass{article}\\begin{document}\\section{Introduction}The bound was found by language models "
           "working through the problem.\n\\end{document}\n")
    ok("FIRE W04 MUST on a paper with no abstract in any folder", any(x[2].startswith(C.MUST_TAG) for x in
                                                                      C.scan(w04, [C.Doc(pap, "career/x/main.tex")])), "")
    ok("QUIET W51 on a long research statement", not C.scan(w51, [C.Doc(own.replace("\\begin{abstract}", "\\begin{quote}")
                                                                      .replace("\\end{abstract}", "\\end{quote}"),
                                                                      "rs/Research_Statement.tex")]), "")
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
    # W57..W66: "the author has read the paper" only in a paper he named (rule of 17 Nov)
    hk = dict((h["id"], h) for h in hooks)
    rdir = os.path.join(tmp, "rd")
    os.makedirs(rdir)
    rtex = os.path.join(rdir, "main.tex")
    filler = " ".join(["The chain mixes in time of order n squared on the path with n vertices."] * 90)

    def rdoc(sent):
        body = ("\\documentclass{article}\n\\title{A walk on the path}\n\\begin{document}\n\\begin{abstract}We bound the "
                "constant. %s\\end{abstract}\n\\section{Introduction}\n%s\n\\section*{Use of AI tools}\nThe proofs were "
                "found by Codex (OpenAI). %s\n\\end{document}\n" % (sent, filler, H.STANDING))
        with open(rtex, "w", encoding="utf-8") as f:
            f.write(body)
        return C.Doc(body, rtex)

    def fires(i, d):
        return bool(C.scan(hk[i], [d]))
    claim = "The author has read the paper and the proofs. "
    ok("FIRE W57 on the sentence in a paper he has not named", fires("W57", rdoc(claim)))
    ok("FIRE W57 on 'the author directed the work, read the paper and the proofs'",
       fires("W57", rdoc("The author directed the work, read the paper and the proofs, and takes responsibility. ")))
    ok("QUIET W57 and W58 on the standing sentence", not fires("W57", rdoc("")) and not fires("W58", rdoc("")))
    ok("QUIET W57 when a system did the reading",
       not fires("W57", rdoc("The author directed the work and Codex read the proofs a second time. ")))
    ok("QUIET W57 on an edit fragment that says nothing of it",
       not C.scan(hk["W57"], [C.Doc("Another agent has read it and adopted the corrections.", rtex, fragment=True)]))
    ok("FIRE W57 on an edit fragment that adds the sentence",
       bool(C.scan(hk["W57"], [C.Doc("The author has read the paper and the proofs.", rtex, fragment=True)])))
    ok("FIRE W58 on 'verified by the author'", fires("W58", rdoc("Every proof was verified by the author. ")))
    ok("FIRE W58 on 'the author checked every proof'", fires("W58", rdoc("The author checked every proof in the paper. ")))
    got58 = C.scan(hk["W58"], [rdoc("Every proof was verified by the author. ")])
    ok("W58 is a MUST on 'verified by the author'", bool(got58) and got58[0][2].startswith(C.MUST_TAG), str(got58)[:200])
    got58 = C.scan(hk["W58"], [rdoc("All claims and proofs were reviewed and edited by the author, who takes responsibility. ")])
    ok("W58 reports the template 'reviewed and edited by the author' and it is not a MUST",
       bool(got58) and not any(x[2].startswith(C.MUST_TAG) for x in got58), str(got58)[:200])
    # 18 Nov: the two shapes the census found (ipm-lowerbound, ising-perceptron-margin-release)
    ok("FIRE W58 on 'the author supervised the runs, reviewed the mathematics'",
       fires("W58", rdoc("The author supervised the runs, reviewed the mathematics, and accepts responsibility. ")))
    ok("QUIET W58 on 'verified' used as an adjective",
       not fires("W58", rdoc("The author set the objective of extending the verified capacity results to nonzero margin. ")))
    # 18 Nov held-out pass (150 files outside the census): two misses, one far verb, one "all of the above"
    ok("FIRE W58 on 'is responsible for all mathematical claims ... and has verified the arguments'",
       fires("W58", rdoc("The author is responsible for all mathematical claims, the selection of the problem and the "
                         "final form of the text, and has verified the arguments and references. ")))
    ok("FIRE W58 on 'the author reviewed all of the above'",
       fires("W58", rdoc("The author reviewed all of the above and takes full responsibility. ")))
    ok("QUIET W58 on 'the author thanks the referee, who checked the proofs'",
       not fires("W58", rdoc("The author thanks the referee, who checked the proofs with great care. ")))
    ok("QUIET W58 on another paper's authors ('the authors of [5] verified', 'the authors in [2] checked')",
       not fires("W58", rdoc("The authors of [5] verified the conjecture for small n and confirmed the results of [3]. "
                             "The authors in [2] checked the proofs of the main lemma. ")))
    ok("FIRE W58 on 'the author of this paper has verified the proofs'",
       fires("W58", rdoc("The author of this paper has verified the proofs. ")))
    ok("QUIET W58 on 'the author thanks J. Smith for having checked the proofs'",
       not fires("W58", rdoc("The author thanks J. Smith for having checked the proofs. ")))
    ok("QUIET W58 on 'the author thanks the reviewer that read the manuscript carefully'",
       not fires("W58", rdoc("The author thanks the reviewer that read the manuscript carefully. ")))
    ok("QUIET W58 on 'the author is grateful to J. Smith, who checked the proofs'",
       not fires("W58", rdoc("The author is grateful to J. Smith, who checked the proofs. ")))
    # W73: the Google Cloud education-credits sentence (rule of 18 Nov)
    cred = "Computational resources were provided in part by Google Cloud through its education credits program. "
    got73 = C.scan(hk["W73"], [rdoc(cred)])
    ok("FIRE W73 once on the credit sentence", len(got73) == 1, str(got73)[:200])
    ok("FIRE W73 on 'education credits programme' without the number",
       fires("W73", rdoc("Resources came from Google Cloud through its education credits programme. ")))
    ok("QUIET W73 on a plain grant line", not fires("W73", rdoc("Supported by a grant of the university credits program. ")))
    readme = os.path.join(rdir, "README.md")
    with open(readme, "w", encoding="utf-8") as f:
        f.write("# A walk on the path\nThe author has read the paper and the proofs.\n")
    ok("FIRE W62 on a README that says it", fires("W62", rdoc("")))
    os.remove(readme)
    ok("QUIET W62 with no such file beside the paper", not fires("W62", rdoc("")))
    ok("FIRE the W64 check on a posted paper that says it", bool(H.c64(set(), {}, {"docs": [rdoc(claim)]})))
    ok("QUIET the W64 check on the standing sentence", H.c64(set(), {}, {"docs": [rdoc("")]}) is None)
    ok("W65 asks for the sentence out or his word", "no AUTHOR_READ_OK" in (H.c65(set(), {}, {"docs": [rdoc(claim)]}) or ""))
    mk = os.path.join(rdir, "AUTHOR_READ_OK.txt")
    open(mk, "w").close()
    d = rdoc(claim)
    ok("an empty AUTHOR_READ_OK opens nothing: W57 and W59 both fire", fires("W57", d) and fires("W59", d))
    with open(mk, "w", encoding="utf-8") as f:
        f.write("2026-11-17 01:06, the author: \"make this paper ready for the journal, and say the author read "
                "everything\"\n")
    d = rdoc(claim)
    ok("QUIET W57 W58 W59 W60 W62 once the record holds the date and his words",
       not any(fires(i, d) for i in ("W57", "W58", "W59", "W60", "W62")))
    ok("W65 on a named paper says the sentence is made in his name", "in his name" in (H.c65(set(), {}, {"docs": [d]}) or ""))
    ok("FIRE W60 on a named paper with no such sentence", fires("W60", rdoc("")))
    d = rdoc(claim)
    now = os.path.getmtime(rtex)
    os.utime(mk, (now - 3 * 3600, now - 3 * 3600))
    ok("FIRE W61 when the .tex moved after the record", fires("W61", d))
    os.utime(mk, (now + 5, now + 5))
    ok("QUIET W61 when the record is the newer", not fires("W61", d))
    os.remove(mk)
    got, ch, _, _ = ids({"hook_event_name": "PreToolUse", "tool_name": "Write", "session_id": "rd1",
                         "tool_input": {"file_path": os.path.join(tmp, "rd2", "main.tex"), "content": rdoc(claim).raw}})
    ok("FIRE W57 through the engine on a paper written whole", "W57" in got, str(sorted(got)))
    # W67..W72: the private record of submissions (rule of 17 Nov)
    led = os.path.join(tmp, "SUBMISSIONS.jsonl")
    with open(led, "w", encoding="utf-8") as f:
        f.write(json.dumps({"rid": "S0001", "title": "A walk on the path", "journal": "J. Appl. Probab.", "ms_id": "JAP-1",
                            "submitted": "2026-11-01", "status": "under_review", "checked": "2026-09-01"}) + "\n")
        f.write(json.dumps({"rid": "S0002", "title": "Mixing of the lazy cycle", "journal": "ALEA", "ms_id": "",
                            "submitted": "2026-10-01", "status": "declined", "checked": "2026-11-01"}) + "\n")
        f.write(json.dumps({"rid": "S0003", "title": "Mixing of the lazy cycle", "journal": "Bernoulli", "ms_id": "",
                            "submitted": "2026-11-02", "status": "draft_started", "checked": "2026-11-16"}) + "\n")
    os.environ["PW_SUBMISSIONS"] = led
    try:
        r67 = H.c67(set(), {}, {"docs": [rdoc("")]}) or ""
        ok("W67 stops a paper whose row is open", r67.startswith("STOP") and "J. Appl. Probab." in r67, r67[:200])
        other = C.Doc(rdoc("").raw.replace("A walk on the path", "Cutoff for the riffle shuffle on trees"), rtex)
        r67 = H.c67(set(), {}, {"docs": [other]}) or ""
        ok("W67 calls an unlisted paper a first submission", "no row" in r67 and "STOP" not in r67, r67[:200])
        r67 = H.c67(set(), {}, {"docs": []}) or ""
        ok("W67 with no paper in the call lists what is open", "2 rows are open" in r67 and "check" in r67, r67[:200])
        ok("W70 names the unfinished draft", "S0003" in (H.c70(set(), {}, {}) or ""))
        r71 = H.c71(set(), {}, {}) or ""
        ok("W71 names the open row not looked at for a month and not the fresh one", "S0001" in r71 and "S0003" not in r71, r71[:200])
        got, ch, _, _ = ids({"hook_event_name": "PreToolUse", "tool_name": "mcp__claude-in-chrome__navigate", "session_id": "sb1",
                             "tool_input": {"url": "https://mc.manuscriptcentral.com/apjournals", "tabId": 1}})
        ok("FIRE W67 and W68 when a journal's submission site is opened", {"W67", "W68"} <= got and "submit" in ch,
           "%s %s" % (sorted(got), ch))
        got, ch, _, _ = ids({"hook_event_name": "UserPromptSubmit", "session_id": "sb2",
                             "prompt": "the journal rejected the paper, read the referee report and tell me what to do"})
        ok("FIRE W69 on a prompt about a rejection", "W69" in got, "%s %s" % (sorted(got), ch))
    finally:
        os.environ["PW_SUBMISSIONS"] = sub0
    pub = os.path.join(tmp, "pubrepo")
    os.makedirs(pub)
    open(os.path.join(pub, "SUBMISSIONS.md"), "w").close()
    ok("FIRE the W72 check on a record kept beside a paper", bool(H.c72(set(), {}, {"dir": pub})))
    ok("QUIET the W72 check on a folder without one", H.c72(set(), {}, {"dir": rdir}) is None)
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
    _gate_selftest(ok, C)
    print("ALL PASS" if not fails else "FAILED: %d (%s)" % (len(fails), "; ".join(fails)))
    return 0 if not fails else 1


def _gate_selftest(ok, C):
    """The reference-kind gate through main(): its paths moved to a scratch folder, the paper hooks' own run stubbed, so
    nothing live is read or written (18 Nov)."""
    import io
    import shutil
    import tempfile
    if not os.path.isfile(os.path.join(HERE, "pdf_kind_gate.py")):
        print("SKIP the reference-kind gate tests: pdf_kind_gate.py is optional and not installed")
        return
    import pdf_kind_gate as G
    keep = (G.LIVE, G.LOG, G.CACHE, G.decide, C.run_payload)
    tmp = tempfile.mkdtemp(prefix="pwgate_")
    G.LIVE, G.LOG, G.CACHE = (os.path.join(tmp, n) for n in ("LIVE", "would_deny.jsonl", "verdicts.json"))
    pdf = os.path.join(tmp, "main.pdf")
    with open(pdf, "wb") as f:
        f.write(b"%PDF-1.5\n% pdfTeX planted\n")
    C.run_payload = lambda raw, loader: ("[paper-writing hooks] W57 MUST stub text", {"hook_event_name": "PreToolUse"})

    def run(cmd, argv=(), tool="Bash", paths=None):
        ti = {"paths": paths} if paths is not None else {"command": cmd}
        payload = json.dumps({"hook_event_name": "PreToolUse", "tool_name": tool, "session_id": "gatetest",
                              "cwd": tmp, "tool_input": ti})
        si, so = sys.stdin, sys.stdout
        sys.stdin, sys.stdout = io.StringIO(payload), io.StringIO()
        try:
            rc = main(list(argv))
            return rc, sys.stdout.getvalue()
        finally:
            sys.stdin, sys.stdout = si, so

    def denies(out):
        try:
            o = json.loads(out)
        except ValueError:
            return False
        return o.get("hookSpecificOutput", {}).get("permissionDecision") == "deny"

    up = 'curl -F file=@%s "https://zenodo.org/api/deposit/depositions/1/files"' % pdf.replace("\\", "/")
    try:
        def verdict(kind):
            json.dump({G._key(pdf, []): {"kind": kind, "text": "main.pdf prints 1 reference(s) of the wrong kind: "
                                         "Theorem 2.1 -> Lemma 2.1" if kind == "wrong" else ""}},
                      open(G.CACHE, "w", encoding="utf-8"))
        rc, out = run("ls -la")
        ok("QUIET gate: an unrelated call prints nothing", rc == 0 and out == "", repr(out[:200]))
        verdict("clean")
        rc, out = run(up)
        ok("QUIET gate: a checked clean paper PDF to Zenodo, LIVE off", "[pdf-kind-gate]" not in out and not denies(out),
           out[:200])
        verdict("wrong")
        rc, out = run(up)
        ok("FIRE gate shadow: a wrong-kind PDF to Zenodo is a note, not a deny",
           "[pdf-kind-gate]" in out and "would deny" in out and not denies(out), out[:300])
        open(G.LIVE, "w").close()
        rc, out = run(up)
        ok("FIRE gate LIVE: the same call is denied, stdout one JSON object with the paper hooks' text inside",
           rc == 0 and denies(out) and "W57 MUST stub" in json.loads(out)["hookSpecificOutput"]["permissionDecisionReason"],
           out[:300])
        rc, out = run(up, argv=["--codex"])
        ok("QUIET gate for Codex: LIVE wrong-kind is advisory context, never a deny",
           not denies(out) and "[pdf-kind-gate]" in out and "additionalContext" in out, out[:300])
        rc, out = run("", tool="mcp__claude-in-chrome__file_upload", paths=[pdf])
        ok("FIRE gate LIVE: a browser upload of the wrong-kind PDF is denied", denies(out), out[:300])
        os.remove(G.CACHE)
        open(G.CACHE, "w").write("{not json")
        rc, out = run(up)
        ok("fail open: an unreadable verdict cache under LIVE gives a note, no deny", not denies(out), out[:300])
        verdict("wrong")
        G.decide = lambda p: 1 / 0
        rc, out = run(up)
        ok("fail open: a gate crash under LIVE is a loud note, no deny", rc == 0 and not denies(out) and
           "NOTHING was checked" in out, out[:300])
        G.decide = keep[3]
        sys.modules["pdf_kind_gate"] = None                 # import now raises: as if the file could not load
        rc, out = run(up)
        ok("fail open: a gate that cannot import gives the plain paper-hook text", not denies(out) and
           "W57 MUST stub" in out, out[:300])
        sys.modules["pdf_kind_gate"] = G
        verdict("wrong")
        rc, out = run('curl -s "https://zenodo.org/api/records/123"')
        ok("QUIET gate: a Zenodo read (GET) is not an upload", "[pdf-kind-gate]" not in out, out[:300])
        rc, out = run('curl -fsSL -o %s "https://zenodo.org/records/1/files/main.pdf"' % pdf.replace("\\", "/"))
        ok("QUIET gate LIVE: downloading the wrong-kind PDF from Zenodo is not denied", not denies(out) and
           "[pdf-kind-gate]" not in out, out[:300])
        up_py = os.path.join(tmp, "up_rows.py")
        with open(up_py, "w", encoding="utf-8") as f:
            f.write('import requests\nfor row in open("rows.txt"):\n'
                    '    requests.put("https://zenodo.org/api/files/" + row.split()[0], data=open(row.split()[1], "rb"))\n')
        rc, out = run("python %s" % up_py.replace("\\", "/"))
        ok("FIRE gate: a Zenodo upload script that names no PDF gets the 'NOTHING was checked' note, no deny",
           "[pdf-kind-gate]" in out and "NOTHING was checked" in out and not denies(out), out[:300])
        rc, out = run("grep -n requests.put %s; sed -n 1,5p %s" % (up_py.replace("\\", "/"), up_py.replace("\\", "/")))
        ok("QUIET gate: reading an upload script with grep or sed is not running it", "[pdf-kind-gate]" not in out,
           out[:300])
        msg_py = os.path.join(tmp, "send_note.py")
        with open(msg_py, "w", encoding="utf-8") as f:
            f.write('print("the zenodo upload of main.pdf waits for the audit")\n')
        rc, out = run("python -s -X utf8 %s" % msg_py.replace("\\", "/"))
        ok("QUIET gate: a script whose prose says zenodo upload is not an upload", "[pdf-kind-gate]" not in out, out[:300])
        gate_py = os.path.join(HERE, "pdf_kind_gate.py").replace("\\", "/")
        rc, out = run('python %s --check "%s" 2>&1 | tail -3' % (gate_py, pdf.replace("\\", "/")))
        ok("QUIET gate: the printed remedy (--check) is never denied, piped or not", not denies(out) and
           "[pdf-kind-gate]" not in out, out[:300])
        for sep in (" ; ", " && ", "\n"):                   # A01 18 Nov: a checker first must not hide an upload after
            rc, out = run("python %s --check x.pdf%s%s" % (gate_py, sep, up))
            ok("FIRE gate LIVE: an upload chained after the checker (%r) is still denied" % sep, denies(out), out[:300])
        # 18 Nov: an echoed 'python push_gate.py' line and a heredoc naming Zenodo were read as an upload.
        rc, out = run('echo "retry: python %s" >> NEXT.md && cat >> F.md <<\'EOF\'\nthe Zenodo upload waits; '
                      'curl -F file=@x.pdf https://zenodo.org/api/deposit/depositions/1/files\nEOF\npython -s %s'
                      % (up_py.replace("\\", "/"), msg_py.replace("\\", "/")))
        ok("QUIET gate: an echoed python line and a heredoc of prose naming Zenodo are not an upload",
           "[pdf-kind-gate]" not in out and not denies(out), out[:300])
        rc, out = run('python -s %s --body "the Zenodo upload of the paper waits for the audit"'
                      % up_py.replace("\\", "/"))
        ok("FIRE gate: running a real upload script still fires when its argument is prose",
           "[pdf-kind-gate]" in out, out[:300])
        rc, out = run('python -s %s send --body "note: Zenodo, ResearchGate and arXiv uploads are denied under LIVE"'
                      % msg_py.replace("\\", "/"))
        ok("QUIET gate: a mesh message whose quoted body names the doors is not an upload", "[pdf-kind-gate]" not in out,
           out[:300])
        rc, out = run('echo "retry python %s; keep spaced strings unless .pdf or -c body; Zenodo upload" >> NEXT.md'
                      % up_py.replace("\\", "/"))
        ok("QUIET gate: an echo whose prose says '.pdf' and names an upload script is not an upload",
           "[pdf-kind-gate]" not in out, out[:300])
        sp = os.path.join(tmp, "My Papers")
        os.makedirs(sp, exist_ok=True)
        shutil.copy(pdf, os.path.join(sp, "main.pdf"))
        rc, out = run('curl -F "file=@%s/main.pdf" "https://zenodo.org/api/deposit/depositions/1/files"'
                      % sp.replace("\\", "/"))
        ok("FIRE gate LIVE: a quoted PDF path with a space in it is read (unchecked at a strong door: denied)",
           denies(out), out[:300])
        rc, out = run("bash -c \"%s\"" % up.replace('"', ''))
        ok("FIRE gate LIVE: an upload inside bash -c \"...\" is still denied", denies(out), out[:300])
        rc, out = run("python <<'EOF'\nimport requests\nrequests.post('https://zenodo.org/api/deposit/depositions/1/files',"
                      " files={'file': open('%s', 'rb')})\nEOF" % pdf.replace("\\", "/"))
        ok("FIRE gate LIVE: a python heredoc that posts the wrong-kind PDF to Zenodo is denied", denies(out), out[:300])
        rc, out = run('curl -F "file=@%s" "https://zenodo.org/api/deposit/depositions/1/files"' % pdf.replace("\\", "/"))
        ok("FIRE gate LIVE: a quoted file=@ PDF path is still read", denies(out), out[:300])
        rows =open(G.LOG, encoding="utf-8").read().splitlines()
        ok("every posting call is logged to the scratch would_deny.jsonl", len(rows) >= 5, "%d rows" % len(rows))
    finally:
        G.LIVE, G.LOG, G.CACHE, G.decide, C.run_payload = keep
        sys.modules["pdf_kind_gate"] = G
        shutil.rmtree(tmp, ignore_errors=True)


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
    codex = "--codex" in argv
    gate = _gate(raw)                                     # before the KEYS filter: a curl upload names no paper word
    note = (gate or {}).get("permissionDecisionReason") or (gate or {}).get("additionalContext") or ""
    deny = bool(gate) and gate.get("permissionDecision") == "deny" and not codex
    low = raw.lower()
    text, event = "", "PreToolUse"
    if any(k in low for k in KEYS) or MAKE_CMD.search(low):
        try:
            sys.path.insert(0, HERE)
            import pw_core as C
            import pw_hooks as H
            text, p = C.run_payload(raw, H.load)
            event = str(p.get("hook_event_name") or "")
        except Exception as e:  # noqa: BLE001
            sys.stderr.write("[paper-writing hooks] error: %s\n" % e)
    if deny:                                              # ONE JSON object and nothing else, or the deny is lost
        reason = note + (("\n\n" + text) if text else "")
        sys.stdout.write(json.dumps({"hookSpecificOutput": {"hookEventName": "PreToolUse", "permissionDecision": "deny",
                                                            "permissionDecisionReason": reason[:9000]}}))
        return 0
    _out("\n".join(x for x in (note, text) if x), codex, event)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
