"""Sentences about the paper or about a computation, not about the mathematics (the house rule: a paper states mathematics,
not its own making). paper_lint passed one released source with 0 MUST while a first reader's audit found three:
"... is not treated here", "... is not proved here", "We took ... six draws". This looks for that shape.

    python -X utf8 process_lint.py paper/main.tex     report, one line per sentence with its line number
    python -X utf8 process_lint.py --selftest         controls

Flags, outside the AI declaration and the acknowledgments:
  scope-here  "not treated/proved/considered/discussed/pursued/addressed here" and "we do not treat/prove/consider ..."
  lab-diary   first person doing a computation: "we took/ran/drew/sampled/simulated/computed ... (draws|samples|runs|trials|seeds)"
  history     the paper narrating its versions: "earlier version", "first version", "previous draft", "was corrected"
A flag is a sentence to read, not a verdict: "we do not need X here" in a proof is mathematics.
"""
import io, re, sys

SKIP_SEC = re.compile(r"\\section\*?\{[^}]*(?:(?-i:\bAI\b)|artificial intelligence|generative|acknowledg|data availability|"
                      r"code availability)[^}]*\}", re.I)              # case-sensitive AI: 'thm:main' is not a declaration
VERB = (r"(?:treated|proved|proven|considered|discussed|pursued|addressed|studied|attempted|examined|investigated|settled|"
        r"resolved|answered|established|shown|determined|decided)")
PATTERNS = [
    ("scope-here", re.compile(r"\b(?:is|are|was|were|be|been)\s+not\s+" + VERB + r"\s+(?:in\s+this\s+(?:paper|note|work)|here)\b"
                              r"|\bnot\s+" + VERB + r"\s+here\b"
                              r"|\bwe\s+(?:do|did)\s+not\s+(?:treat|prove|consider|discuss|pursue|address|study|attempt)\b", re.I)),
    ("lab-diary", re.compile(r"\bwe\s+(?:took|ran|drew|sampled|simulated|computed|generated|used)\b[^.]{0,80}?"
                             r"\b(?:draws?|samples?|runs?|trials?|seeds?|replicates?|realizations?|realisations?)\b"
                             r"|\b(?:a|an|our|the)\s+(?:direct\s+|brute[- ]force\s+)?numerical\s+(?:check|minimi[sz]ation|"
                             r"maximi[sz]ation|computation|experiment|search|verification)\b[^.]{0,160}?\b(?:returns?|returned|"
                             r"gives?|gave|confirms?|confirmed|agrees?|agreed|matches|matched)\b", re.I)),
    ("search", re.compile(r"\bwe\s+(?:are|were)\s+not\s+aware\s+of\b|\bwe\s+(?:found|find)\s+no\b|\bwe\s+could\s+not\s+find\b"
                          r"|\bwe\s+did\s+not\s+find\b", re.I)),
    ("ai-in-body", re.compile(r"\b(?:AI\s+agents?|language\s+models?|Claude|Codex|ChatGPT|GPT-\d|Anthropic|OpenAI|Math\s+Brain)\b")),
    ("history", re.compile(r"\b(?:earlier|first|previous|prior|original)\s+(?:version|draft|record)s?\s+of\s+(?:this|the\s+present)"
                           r"|\bwas\s+corrected\b|\bin\s+an\s+earlier\s+version\b", re.I)),
]


def body(tex):
    """The document body with the AI declaration and acknowledgment sections blanked (line numbers kept)."""
    m = re.search(r"\\begin\{document\}", tex)
    start = m.end() if m else 0
    out = list(tex)
    for i in range(start):
        if out[i] != "\n":
            out[i] = " "
    for s in SKIP_SEC.finditer(tex):
        rest = tex[s.end():]
        e = re.search(r"\\section\*?\{|\\begin\{thebibliography\}|\\bibliography\{|\\end\{document\}", rest)
        stop = s.end() + (e.start() if e else len(rest))
        for i in range(s.start(), stop):
            if out[i] != "\n":
                out[i] = " "
    b = re.search(r"\\begin\{thebibliography\}", tex)
    if b:
        for i in range(b.start(), len(out)):
            if out[i] != "\n":
                out[i] = " "
    t = "".join(out)
    return re.sub(r"(?<!\\)%[^\n]*", lambda x: " " * len(x.group(0)), t)


ENV = re.compile(r"\\begin\{(lemma|proposition|corollary|claim|theorem)\}(.*?)\\end\{\1\}\s*\\begin\{proof\}(?:\[[^\]]*\])?"
                 r"(?=(.{0,300}))", re.S)                        # lookahead: the proof's start must not eat the next lemma
CITED = re.compile(r"\((?:see|cf\.|due\s+to|from)[^()]{0,40}?\\cite|\\cite[pt]?\*?(?:\[[^\]]*\])?\{[^}]*\}\s*\)|"
                   r"\b(?:due\s+to|proved\s+(?:by|in)|is\s+(?:the\s+)?(?:theorem|lemma|result)\s+of)\b[^.]{0,60}?\\cite", re.I)
KNOWN_PROOF = re.compile(r"\b(?:this|it)\s+is\s+(?:the|a)\s+(?:\w+\s+){0,2}(?:theorem|lemma|result|inequality|argument)\s+of\b"
                         r"|\bis\s+due\s+to\b|\bis\s+(?:well[- ]known|standard|classical)\b|\bfor\s+completeness\b"
                         r"|\bthe\s+argument\s+is\s+short\b|\bwe\s+(?:include|recall|give|reproduce|repeat)\s+(?:the|a|its)\s+"
                         r"(?:short\s+)?proof\b|\bwe\s+reprove\b|\bfollow(?:s|ing)?\s+(?:the\s+)?(?:proof|argument)\s+(?:of|in)\b", re.I)


def reproofs(t):
    """A statement credited to a citation, or a proof that opens by naming the result it repeats, followed by a full proof:
    the audit's 'known result reproved in full' (T325 R1, R2). Cite it at the statement and drop or shorten the proof,
    or say in one clause what the proof adds."""
    out = []
    for m in ENV.finditer(t):
        env, stmt, start = m.group(1), m.group(2), m.group(3)
        why = None
        if env != "theorem" and CITED.search(stmt):
            why = "statement credited to a citation, then proved"
        elif KNOWN_PROOF.search(start.split(".")[0] + "." + "".join(start.split(".")[1:2])):
            why = "proof opens by naming a known result"
        if why:
            ln = t.count("\n", 0, m.start()) + 1
            ctx = re.sub(r"\s+", " ", (stmt.strip()[:90] + " | proof: " + start.strip()[:90]))
            out.append((ln, "reproof", f"{env}: {why}: {ctx}"))
    return out


def repeats(tex, n=14, gap=40):
    """The same run of n words in two places at least gap words apart: a sentence written twice (T325 audit: the agents
    sentence in the acknowledgements and again in the AI declaration; Lemma 5.2 restating Theorem 2.1(ii)). Whole document
    from \\begin{document} to the bibliography, declarations included; a body sentence restated in the declarations (credits, by order) is skipped; math, citations and references are blanked."""
    sp = lambda x: re.sub(r"[^\n]", " ", x.group(0))                 # keep newlines: line numbers must not drift
    d = re.search(r"\\section\*\{\s*(Acknowledg|Declaration)", tex)
    decl = tex.count("\n", 0, d.start()) + 1 if d else 10 ** 9
    # the AI declaration credits the body's mathematicians by order (14 Nov): body -> declaration is not a repeat;
    # declaration -> declaration still is (T325: the agents sentence twice)
    stmt = set()                                                     # lines inside theorem-like statements
    for e in re.finditer(r"\\begin\{(theorem|lemma|proposition|corollary|claim)\*?\}.*?\\end\{\1\*?\}", tex, flags=re.S):
        a = tex.count("\n", 0, e.start()) + 1
        stmt.update(range(a, a + e.group(0).count("\n") + 1))
    tex = re.sub(r"\\begin\{(abstract|tabular\*?|array|verbatim|lstlisting)\}.*?\\end\{\1\}", sp, tex, flags=re.S)
    # an abstract restates by design; table cells repeat by design
    m = re.search(r"\\begin\{document\}", tex)
    t = list(tex)
    for i in range(m.end() if m else 0):
        if t[i] != "\n":
            t[i] = " "
    b = re.search(r"\\begin\{thebibliography\}|\\bibliography\{", tex)
    if b:
        for i in range(b.start(), len(t)):
            if t[i] != "\n":
                t[i] = " "
    t = "".join(t)
    t = re.sub(r"(?<!\\)%[^\n]*", sp, t)
    t = re.sub(r"\\(?:cite[pt]?|ref|eqref|label|url|href|includegraphics)\*?(?:\[[^\]]*\])?\{[^}]*\}", sp, t)
    t = re.sub(r"\$[^$]*\$|\\\[.*?\\\]|\\begin\{(equation|align|gather|multline)\*?\}.*?\\end\{\1\*?\}", sp, t, flags=re.S)
    t = re.sub(r"\\[a-zA-Z]+\*?", sp, t)
    sents = []                                                       # (line, word list, word-pair set)
    for s in re.finditer(r"[^.!?]+[.!?]", t):
        ws = [w.lower() for w in re.findall(r"[A-Za-z][A-Za-z'\-]*", s.group(0))]
        if len(ws) >= n:
            lead = len(s.group(0)) - len(s.group(0).lstrip())
            sents.append((t.count("\n", 0, s.start() + lead) + 1, ws, set(zip(ws, ws[1:]))))
    out = []
    for i in range(len(sents)):
        for j in range(i):
            (la, wa, pa), (lb, wb, pb) = sents[j], sents[i]
            if lb - la < 3 or la < decl <= lb:
                continue
            share = len(pa & pb) / min(len(pa), len(pb))
            if share >= 0.7:
                # overlap cannot tell a restatement (T325 l.80) from two parallel lemmas (T232 l.193/204), so name both
                what = ("two statements share their wording: if one restates the other, cite it by number; "
                        "if they differ, open with the difference; "
                        if la in stmt and lb in stmt else "")
                out.append((lb, "repeat", f"{what}{share:.0%} of its word pairs also in l.{la}: '{' '.join(wb[:12])} ...'"))
                break
    return out


KINDS = ("theorem", "lemma", "corollary", "proposition", "definition", "remark", "conjecture")
PREFIX = {"thm": "theorem", "theo": "theorem", "lem": "lemma", "cor": "corollary", "prop": "proposition",
          "def": "definition", "dfn": "definition", "rem": "remark", "conj": "conjecture"}


def refnames(t):
    """'Theorem~\\ref{lem:x}': a reference whose word names the wrong kind (house rule: lemmas and
    corollaries are never cited as theorems). The kind is the environment the label sits in, else the label's prefix."""
    kind = {}
    for e in re.finditer(r"\\begin\{(" + "|".join(KINDS) + r")\*?\}(.*?)\\end\{\1\*?\}", t, flags=re.S):
        for lab in re.findall(r"\\label\{([^}]*)\}", e.group(2)):
            kind[lab] = e.group(1)
    out = []
    for m in re.finditer(r"\b(" + "|".join(k.capitalize() for k in KINDS) + r")s?(?:~|\s+)\\ref\{([^}]*)\}", t):
        word, lab = m.group(1).lower(), m.group(2)
        real = kind.get(lab) or (PREFIX.get(lab.split(":", 1)[0].lower()) if ":" in lab else None)
        if real and real != word:
            out.append((t.count("\n", 0, m.start()) + 1, "refname",
                        f"'{m.group(0)}' points to a {real}: write {real.capitalize()}~\\ref{{{lab}}} or use \\cref"))
    return out


def scan(tex):
    t = body(tex)
    hits = reproofs(t) + repeats(tex) + refnames(t)
    for kind, rx in PATTERNS:
        for m in rx.finditer(t):
            ln = t.count("\n", 0, m.start()) + 1
            a = max(t.rfind(".", 0, m.start()), t.rfind("\n\n", 0, m.start())) + 1
            e = t.find(".", m.end())
            ctx = re.sub(r"\s+", " ", t[a:(e + 1 if e > 0 else m.end())]).strip()
            hits.append((ln, kind, ctx[:200]))
    return sorted(set(hits))


def selftest():
    tex = r"""\documentclass{article}\begin{document}
\section{Introduction}
The case $a_1\neq0$ is not treated here. We prove Theorem 1.
The edge is regular; universality at a soft edge is not proved here.
We took $N=2000$ and six draws of $W$ for Figure 1.
We do not need the bound here, since $f$ is bounded.
In an earlier version of this paper the constant was 3.
Whether $R_n$ converges is not settled here. We are not aware of a bound. The theorem was proved by AI agents (Claude).
A direct numerical minimization of the ratio for $n\le 8$ returns the same values. Numerical analysis of PDEs is classical.
\section{Proof of Theorem~\ref{thm:main}} We ran the chain; the bound is not proved here.
\section*{Declaration of generative AI}
We ran 40 trials with Codex. This was not treated here.
\begin{thebibliography}{9}\bibitem{x} We took six draws, \emph{T}, 2000.\end{thebibliography}
\end{document}"""
    h = scan(tex)
    kinds = [(ln, k) for ln, k, _ in h]
    checks = [("scope-here l.3", (3, "scope-here") in kinds),
              ("scope-here l.4", (4, "scope-here") in kinds),
              ("lab-diary l.5", (5, "lab-diary") in kinds),
              ("'we do not need' not flagged", not any(ln == 6 for ln, _ in kinds)),
              ("history l.7", (7, "history") in kinds),
              ("'not settled here' l.8", (8, "scope-here") in kinds),
              ("'we are not aware' l.8", (8, "search") in kinds),
              ("AI agents in the body l.8", (8, "ai-in-body") in kinds),
              ("numerical minimization returns l.9", (9, "lab-diary") in kinds),
              ("'numerical analysis is classical' not flagged", sum(1 for ln, _ in kinds if ln == 9) == 1),
              ("'we ran the chain' not flagged", not any(ln == 10 and k == "lab-diary" for ln, k, _ in h)),
              ("section titled thm:main is not skipped", (10, "scope-here") in kinds),
              ("AI declaration skipped", not any(ln == 12 for ln, _ in kinds)),
              ("bibliography skipped", not any(ln == 13 for ln, _ in kinds))]
    tex2 = r"""\begin{document}
\begin{lemma}\label{a} The zeros are positive (see~\cite{PS} for $n=2$).\end{lemma}
\begin{proof} By (2), the moments match.\end{proof}
\begin{lemma}\label{b} Every solution converges.\end{lemma}
\begin{proof} This is the theorem of \L{}ojasiewicz~\cite{CM}; the argument is short. By Lemma 1 the risk decreases.\end{proof}
\begin{lemma}\label{c} The map is proper.\end{lemma}
\begin{proof} By Lemma 2 the sublevel sets are bounded, as in the classical case.\end{proof}
\begin{theorem}\label{d} The flow converges, with $\mu$ as in~\cite{X}.\end{theorem}
\begin{proof} Combine the lemmas.\end{proof}
\end{document}"""
    r = [(ln, k) for ln, k, _ in scan(tex2) if k == "reproof"]
    checks += [("reproof: cited statement then proof l.2", (2, "reproof") in r),
               ("reproof: proof opens 'this is the theorem of' l.4", (4, "reproof") in r),
               ("reproof: plain lemma not flagged", (6, "reproof") not in r),
               ("reproof: main theorem citing a constant not flagged", (8, "reproof") not in r)]
    tex3 = r"""\begin{document}
\begin{abstract} This work was done by AI agents connected to Math Brain and working inside the Brain framework, a shared memory.\end{abstract}
\section*{Acknowledgements} This work was done by multiple AI agents connected to Math Brain and working together inside the Brain framework, a shared memory in which they record proofs.
The weather was mild and the river was calm on the day the survey of the northern bank began in earnest.
\begin{tabular}{l} a b c d e f g h i j k l m n o p \\ a b c d e f g h i j k l m n o p \end{tabular}

\begin{tabular}{l} a b c d e f g h i j k l m n o p \\ a b c d e f g h i j k l m n o p \end{tabular}
\section*{Declaration of generative AI} The work was done by AI agents connected to Math Brain and working inside the Brain framework, a shared memory in which they record proofs.
\end{document}"""
    r3 = [ln for ln, k, _ in scan(tex3) if k == "repeat"]
    checks += [("repeat: declaration repeats acknowledgements l.8", r3 == [8])]   # abstract and tables not counted
    tex4 = r"""\begin{document}
\section{Introduction} The quadratic form bound for polynomial random features is due to Fan and Wang, who proved it for every fixed degree.
Next we set notation.

\section*{Declaration of generative AI} The quadratic form bound for polynomial random features is due to Fan and Wang, who proved it for every degree.
\end{document}"""
    r4 = [ln for ln, k, _ in scan(tex4) if k == "repeat"]
    checks += [("repeat: body credit restated in the AI declaration is not flagged", r4 == [])]
    tex5 = r"""\begin{document}
\begin{lemma} Up to a null set, the set of initial points whose flow converges to a point with two vanishing products is null.\end{lemma}
Some words between the two.

\begin{lemma} Up to a null set, the set of initial points whose flow converges to a point with one vanishing layer is null.\end{lemma}
\end{document}"""
    r5 = [m for _, k, m in scan(tex5) if k == "repeat"]
    checks += [("repeat: two lemma statements carry the cite-or-differ label",
                len(r5) == 1 and r5[0].startswith("two statements share"))]
    tex6 = r"""\begin{document}
\begin{lemma}\label{key} A.\end{lemma}
\begin{corollary}\label{thm:odd} B.\end{corollary}
\begin{theorem}\label{thm:main} C.\end{theorem}
By Theorem~\ref{key} and Theorem \ref{thm:odd} and Theorem~\ref{thm:main}, and Lemma~\ref{key}, and Proposition~\ref{lem:gone}.
\end{document}"""
    r6 = sorted(m.split("'")[1] for _, k, m in scan(tex6) if k == "refname")
    checks += [("refname: env decides over prefix; right names and unknown labels pass, prefix used when no env",
                r6 == ["Proposition~\\ref{lem:gone}", "Theorem \\ref{thm:odd}", "Theorem~\\ref{key}"])]
    for n, ok in checks:
        print(("PASS " if ok else "FAIL ") + n)
    ok = all(c for _, c in checks)
    print(f"selftest {sum(c for _, c in checks)}/{len(checks)}", "ALL PASS" if ok else "FAIL")
    return 0 if ok else 1


if __name__ == "__main__":
    if sys.argv[1:] == ["--selftest"]:
        sys.exit(selftest())
    for p in sys.argv[1:]:
        hs = scan(io.open(p, encoding="utf-8", errors="replace").read())
        print(f"{p}: {len(hs)} process sentence(s)")
        for ln, k, c in hs:
            print(f"  l.{ln} [{k}] {c}")
