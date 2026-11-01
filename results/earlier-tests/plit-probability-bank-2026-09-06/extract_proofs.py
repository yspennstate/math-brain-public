# -*- coding: utf-8 -*-
"""extract_proofs.py - theorem/proof pairs out of arXiv LaTeX sources, as numbered proof steps.

For every paper under arxiv_mathpr_sources/tex/<id>/: find the main file, inline \\input/\\include, strip
comments, expand the paper's own \\newcommand/\\def macros (best effort), map \\newtheorem names to kinds,
pair every proof environment with its statement (by the label named in "Proof of Theorem~\\ref{..}" when
present, else the nearest preceding statement), clean the text, and split the proof into sentence steps
(display math stays attached to its sentence). Writes proofs.jsonl; one row per accepted proof.

    python extract_proofs.py --out proofs.jsonl [--limit N] [--ids id1,id2]
    python extract_proofs.py --stats proofs.jsonl

Acceptance (recorded per row so the bank can re-filter): 3..25 steps, proof 250..6000 chars, statement
40..1800 chars, no figures/tikz/input in the proof, at most 3 references to things outside the pair,
at least a third of the steps carrying math.
"""
import argparse
import collections
import hashlib
import io
import json
import os
import re
import sys
import time

TEX = "<HOME>/arxiv_mathpr_sources/tex"
LISTING = "<HOME>/arxiv_mathpr_sources/listing.jsonl"

KIND_BY_NAME = {
    "theorem": "theorem", "lemma": "lemma", "proposition": "proposition", "corollary": "corollary",
    "claim": "claim", "fact": "fact", "observation": "observation",
}
DEFAULT_ENV = {
    "theorem": "theorem", "thm": "theorem", "theo": "theorem", "teo": "theorem", "mainthm": "theorem",
    "lemma": "lemma", "lem": "lemma", "lemm": "lemma",
    "proposition": "proposition", "prop": "proposition", "pro": "proposition",
    "corollary": "corollary", "cor": "corollary", "coro": "corollary",
    "claim": "claim", "fact": "fact", "observation": "observation", "obs": "observation",
}
MATH_ENVS = ("equation", "equation*", "align", "align*", "eqnarray", "eqnarray*", "gather", "gather*",
             "multline", "multline*", "alignat", "alignat*", "flalign", "flalign*", "displaymath", "split")


# ----------------------------------------------------------------------------- reading + inlining
def read_text(path):
    with open(path, "rb") as f:
        raw = f.read()
    for enc in ("utf-8", "latin-1"):
        try:
            return raw.decode(enc)
        except UnicodeDecodeError:
            continue
    return raw.decode("utf-8", errors="replace")


def strip_comments(s):
    s = re.sub(r"\\begin\{comment\}.*?\\end\{comment\}", "", s, flags=re.S)
    out = []
    for line in s.split("\n"):
        i, n = 0, len(line)
        buf = []
        while i < n:
            c = line[i]
            if c == "\\" and i + 1 < n:
                buf.append(line[i:i + 2])
                i += 2
                continue
            if c == "%":
                break
            buf.append(c)
            i += 1
        out.append("".join(buf))
    return "\n".join(out)


def find_main(d):
    files = [f for f in os.listdir(d) if f.lower().endswith((".tex", ".ltx"))]
    best, score = None, -1
    for f in files:
        try:
            t = read_text(os.path.join(d, f))
        except Exception:
            continue
        sc = 0
        if "\\begin{document}" in t:
            sc += 10
        if "\\documentclass" in t:
            sc += 5
        sc += min(5, t.count("\\begin{proof}"))
        if sc > score:
            best, score = f, sc
    return best


def inline_inputs(d, text, depth=0, seen=None):
    seen = seen if seen is not None else set()
    if depth > 6:
        return text

    def repl(m):
        name = m.group(2).strip()
        cands = [name, name + ".tex", name.replace("/", "__"), name.replace("/", "__") + ".tex",
                 name.replace("./", "").replace("/", "__") + ".tex"]
        for c in cands:
            p = os.path.join(d, c)
            if os.path.exists(p) and c not in seen:
                seen.add(c)
                try:
                    return "\n" + inline_inputs(d, strip_comments(read_text(p)), depth + 1, seen) + "\n"
                except Exception:
                    return ""
        return ""
    return re.sub(r"\\(input|include|subfile)\{([^}]+)\}", repl, text)


# ----------------------------------------------------------------------------- macros
def _balanced(s, i):
    """s[i] == '{'; return index just past the matching '}' or -1."""
    depth = 0
    n = len(s)
    j = i
    while j < n:
        c = s[j]
        if c == "\\":
            j += 2
            continue
        if c == "{":
            depth += 1
        elif c == "}":
            depth -= 1
            if depth == 0:
                return j + 1
        j += 1
    return -1


def collect_macros(text):
    """{name: (nargs, default_or_None, body)} from \\newcommand, \\renewcommand, \\providecommand, \\def,
    \\DeclareMathOperator. Best effort; complicated definitions are skipped."""
    macros = {}
    for m in re.finditer(r"\\(?:re)?newcommand\*?|\\providecommand\*?", text):
        i = m.end()
        # name: {\foo} or \foo
        mm = re.match(r"\s*\{?\\([A-Za-z@]+)\}?", text[i:i + 60])
        if not mm:
            continue
        name = mm.group(1)
        j = i + mm.end()
        nargs, default = 0, None
        mm2 = re.match(r"\s*\[(\d)\]", text[j:j + 10])
        if mm2:
            nargs = int(mm2.group(1))
            j += mm2.end()
            mm3 = re.match(r"\s*\[([^\]]*)\]", text[j:j + 200])
            if mm3:
                default = mm3.group(1)
                j += mm3.end()
        mm4 = re.match(r"\s*\{", text[j:j + 5])
        if not mm4:
            continue
        j += mm4.end() - 1
        k = _balanced(text, j)
        if k < 0 or k - j > 600:
            continue
        body = text[j + 1:k - 1]
        if "\\def" in body or "\\newcommand" in body:
            continue
        macros[name] = (nargs, default, body)
    for m in re.finditer(r"\\(?:e|g|x)?def\s*\\([A-Za-z@]+)\s*((?:#\d)*)\s*\{", text):
        name = m.group(1)
        nargs = len(re.findall(r"#\d", m.group(2)))
        j = m.end() - 1
        k = _balanced(text, j)
        if k < 0 or k - j > 600:
            continue
        body = text[j + 1:k - 1]
        if "\\def" in body:
            continue
        macros.setdefault(name, (nargs, None, body))
    for m in re.finditer(r"\\DeclareMathOperator\*?\s*\{?\\([A-Za-z@]+)\}?\s*\{", text):
        name = m.group(1)
        j = m.end() - 1
        k = _balanced(text, j)
        if k < 0:
            continue
        macros[name] = (0, None, "\\operatorname{" + text[j + 1:k - 1] + "}")
    # never expand these (structural or common LaTeX names)
    for bad in ("begin", "end", "label", "ref", "cite", "eqref", "section", "item", "proof", "left", "right",
                "frac", "sqrt", "sum", "int", "text", "mathbb", "mathcal", "mathrm", "operatorname", "le", "ge",
                "leq", "geq", "to", "cdot", "cdots", "ldots", "dots", "alpha", "beta", "gamma", "delta",
                "epsilon", "varepsilon", "lambda", "mu", "sigma", "tau", "omega", "Omega", "theta", "phi",
                "varphi", "psi", "rho", "xi", "eta", "kappa", "nu", "pi", "zeta", "chi", "infty", "in",
                "subset", "cup", "cap", "quad", "qquad", "limsup", "liminf", "lim", "sup", "inf", "max", "min",
                "log", "exp", "sin", "cos", "det", "tr", "var", "Var", "E", "P", "N", "R", "Z", "C", "Q"):
        macros.pop(bad, None)
    return macros


def expand_macros(text, macros, rounds=8):
    if not macros:
        return text, 0
    names = sorted(macros, key=len, reverse=True)
    pat = re.compile(r"\\(" + "|".join(re.escape(n) for n in names) + r")(?![A-Za-z@])")
    total = 0
    for _ in range(rounds):
        changed = 0
        out = []
        i = 0
        while True:
            m = pat.search(text, i)
            if not m:
                out.append(text[i:])
                break
            out.append(text[i:m.start()])
            name = m.group(1)
            nargs, default, body = macros[name]
            j = m.end()
            args = []
            ok = True
            if nargs:
                # optional first arg
                if default is not None:
                    mm = re.match(r"\s*\[([^\]]*)\]", text[j:j + 300])
                    if mm:
                        args.append(mm.group(1))
                        j += mm.end()
                    else:
                        args.append(default)
                while len(args) < nargs:
                    mm = re.match(r"\s*\{", text[j:j + 5])
                    if mm:
                        k = _balanced(text, j + mm.end() - 1)
                        if k < 0:
                            ok = False
                            break
                        args.append(text[j + mm.end():k - 1])
                        j = k
                    else:
                        mm = re.match(r"\s*(\\[A-Za-z]+|.)", text[j:j + 40], flags=re.S)
                        if not mm:
                            ok = False
                            break
                        args.append(mm.group(1))
                        j += mm.end()
            if not ok:
                out.append(m.group(0))
                i = m.end()
                continue
            rep = body
            for k, a in enumerate(args, 1):
                rep = rep.replace("#" + str(k), a)
            # a space after a control word if the expansion ends in a letter and the next char is a letter
            if rep and rep[-1].isalpha() and j < len(text) and text[j].isalpha():
                rep += " "
            out.append(rep)
            i = j
            changed += 1
        text = "".join(out)
        total += changed
        if not changed:
            break
    return text, total


# ----------------------------------------------------------------------------- environments
def theorem_env_map(text):
    env = dict(DEFAULT_ENV)
    for m in re.finditer(r"\\newtheorem\*?\s*\{([A-Za-z*]+)\}\s*(?:\[[^\]]*\])?\s*\{([^}]*)\}", text):
        name = m.group(1).strip("*")
        title = re.sub(r"[^a-z]", "", m.group(2).lower())
        for key, kind in KIND_BY_NAME.items():
            if title == key or title == key + "s":
                env[name] = kind
                break
        else:
            env.pop(name, None)   # definitions, remarks, examples, notation... are not statements
    return env


def find_envs(text, names):
    """[(start, end, envname, opt, inner)] for \\begin{name}[opt] ... \\end{name}, non-nested per name."""
    out = []
    for name in names:
        for m in re.finditer(r"\\begin\{" + re.escape(name) + r"\}(\[(?:[^\[\]]|\[[^\]]*\])*\])?", text):
            e = text.find("\\end{" + name + "}", m.end())
            if e < 0:
                continue
            inner = text[m.end():e]
            if len(inner) > 20000:
                continue
            out.append((m.start(), e + len(name) + 6, name, (m.group(1) or "")[1:-1], inner))
    out.sort()
    return out


LABEL_RE = re.compile(r"\\label\{([^}]*)\}")


def clean_text(s, local_labels, ext_counter):
    """LaTeX -> readable LaTeX: drop labels/spacing macros, number local equation refs, mark external ones."""
    s = re.sub(r"\\label\{[^}]*\}", "", s)

    def ref_repl(m):
        lab = m.group(2).strip()
        if lab in local_labels:
            return "(" + local_labels[lab] + ")"
        ext_counter[0] += 1
        return "(" + m.group(1) + " " + re.sub(r"[^A-Za-z0-9:._-]", "", lab) + ")"   # 13:1x: full label (Codex a21452b82)
    s = re.sub(r"\\(eqref|ref|cref|Cref|autoref)\{([^}]*)\}", ref_repl, s)
    s = re.sub(r"\\cite[tp]?\*?(?:\[[^\]]*\])?\{[^}]*\}", "[citation]", s)
    s = re.sub(r"\\(?:qedhere|qed|hfill|noindent|medskip|smallskip|bigskip|par|newline|linebreak|clearpage|newpage|allowdisplaybreaks|displaybreak|nonumber|notag|indent|centering)\b", " ", s)
    s = re.sub(r"\\vspace\*?\{[^}]*\}|\\hspace\*?\{[^}]*\}", " ", s)
    s = re.sub(r"\\(?:textit|textbf|emph|textsc|underline|textrm|textup)\{([^{}]*)\}", r"\1", s)
    s = re.sub(r"\\(?:it|bf|em|rm|sc)\b", "", s)
    s = re.sub(r"~", " ", s)
    s = re.sub(r"\\\\\s*(\[[^\]]*\])?", " \\\\ ", s)
    s = s.replace("\r", "")
    s = re.sub(r"[ \t]+", " ", s)
    s = re.sub(r"\n\s*\n+", "\n", s)
    return s.strip()


# ----------------------------------------------------------------------------- sentence steps
PLACE = "\u0001%d\u0002"


def protect_math(s):
    """Replace math spans with placeholders; returns (text, spans)."""
    spans = []

    def keep(m):
        spans.append(m.group(0))
        return PLACE % (len(spans) - 1)
    # display environments first
    for env in MATH_ENVS:
        s = re.sub(r"\\begin\{" + re.escape(env) + r"\}.*?\\end\{" + re.escape(env) + r"\}", keep, s, flags=re.S)
    s = re.sub(r"\\\[.*?\\\]", keep, s, flags=re.S)
    s = re.sub(r"\$\$.*?\$\$", keep, s, flags=re.S)
    s = re.sub(r"\\\(.*?\\\)", keep, s, flags=re.S)
    s = re.sub(r"\$(?:[^$\\]|\\.)+\$", keep, s, flags=re.S)
    return s, spans


def restore(s, spans):
    return re.sub("\u0001(\\d+)\u0002", lambda m: spans[int(m.group(1))], s)


ABBREV = ("i.e.", "e.g.", "cf.", "resp.", "w.r.t.", "a.s.", "a.e.", "vs.", "etc.", "Thm.", "Lem.", "Prop.",
          "Cor.", "Eq.", "Sec.", "Ch.", "Fig.", "no.", "St.", "Dr.", "Prof.", "s.t.", "i.i.d.", "w.l.o.g.",
          "W.l.o.g.", "r.v.", "p.d.f.", "c.d.f.", "resp.", "viz.", "approx.", "Ass.", "Def.", "Rem.")


def split_steps(proof_text):
    s, spans = protect_math(proof_text)
    s = s.replace("\n", " ")
    # sentence boundaries: '.', '?', '!' followed by space + uppercase/placeholder/quote, not after an abbreviation
    parts = []
    start = 0
    i = 0
    n = len(s)
    while i < n:
        c = s[i]
        if c in ".!?" and i + 1 < n:
            nxt = s[i + 1:i + 3]
            prev = s[max(0, i - 12):i + 1]
            is_abbrev = any(prev.endswith(a) for a in ABBREV)
            single_letter = re.search(r"(?:^|\s)[A-Za-z]\.$", prev) is not None
            if not is_abbrev and not single_letter and re.match(r"\s+(?:[A-Z\u0001(\"'\[]|\\\\)", s[i + 1:i + 4]):
                parts.append(s[start:i + 1])
                start = i + 1
        i += 1
    parts.append(s[start:])
    # a display placeholder at the very start of a part belongs to the previous sentence
    steps = []
    for p in parts:
        p = p.strip()
        if not p:
            continue
        if steps and (len(p) < 30 or re.match(r"^\u0001\d+\u0002\s*[.,;]?\s*$", p)):
            steps[-1] = steps[-1] + " " + p
        else:
            steps.append(p)
    return [restore(x, spans).strip() for x in steps]


def has_math(step):
    return bool(re.search(r"\$|\\\[|\\begin\{(?:equation|align|gather|multline|eqnarray)", step))


# ----------------------------------------------------------------------------- per paper
def process_paper(pid, meta):
    d = os.path.join(TEX, pid.replace("/", "_"))
    if not os.path.isdir(d):
        return [], "no_dir"
    main = find_main(d)
    if not main:
        return [], "no_main"
    text = strip_comments(read_text(os.path.join(d, main)))
    text = inline_inputs(d, text)
    macros = collect_macros(text)
    body_start = text.find("\\begin{document}")
    body = text[body_start:] if body_start >= 0 else text
    body, n_exp = expand_macros(body, macros)
    envmap = theorem_env_map(text)
    stmts = find_envs(body, list(envmap))
    proofs = find_envs(body, ["proof"])
    if not stmts or not proofs:
        return [], "no_pairs"
    label_to_stmt = {}
    for st in stmts:
        for lab in LABEL_RE.findall(st[4]):
            label_to_stmt[lab] = st
    rows = []
    used = set()
    # 2026-09-07 13:1x: labels named by ANY "Proof of ..." heading in the paper - a statement whose label is named
    # elsewhere has its proof elsewhere, so a headless proof right after it is somebody else's (the mispairing class
    # found in the checkpoint-E validity read: <item>, lemma ll20 of 2601.09880 paired with
    # a 15-step appendix proof of a theorem). Recorded per row as pair_rule / pair_gap_chars / stmt_named_elsewhere;
    # no new rejection yet - the rule is set from the recorded data, not guessed.
    named_elsewhere = set()
    for (_, _, _, popt2, _) in proofs:
        for lab in re.findall(r"\\(?:ref|cref|Cref|autoref)\{([^}]*)\}", popt2):
            named_elsewhere.add(lab)
    for (ps, pe, _, popt, pinner) in proofs:
        target = None
        pair_rule = "by_ref"
        labs = re.findall(r"\\(?:ref|cref|Cref|autoref)\{([^}]*)\}", popt)
        for lab in labs:
            if lab in label_to_stmt:
                target = label_to_stmt[lab]
                break
        if target is None and labs:
            continue   # names a theorem by label we cannot find: skip rather than mispair
        if target is None:
            if re.search(r"[Pp]roof of", popt):
                continue   # names a theorem by number: skip rather than mispair
            prev = [st for st in stmts if st[1] <= ps]
            if not prev:
                continue
            target = prev[-1]
            pair_rule = "nearest"
            # any other proof between the statement and this proof means this proof is not its proof
            if any(qs > target[1] and qs < ps for (qs, _, _, _, _) in proofs):
                continue
            if ps - target[1] > 2500:
                continue
        pair_gap = ps - target[1]
        stmt_named_elsewhere = any(lab in named_elsewhere for lab in LABEL_RE.findall(target[4]))
        key = (target[0], ps)
        if key in used:
            continue
        used.add(key)
        # local labels: equations inside the statement or the proof get local numbers
        local = {}
        for k, lab in enumerate(LABEL_RE.findall(target[4]) + LABEL_RE.findall(pinner), 1):
            local.setdefault(lab, "eq %d" % k)
        ext = [0]
        stmt_txt = clean_text(target[4], local, ext)
        proof_txt = clean_text(pinner, local, ext)
        if re.search(r"\\begin\{(figure|tikzpicture|table|tabular|itemize|enumerate)\}|\\includegraphics|\\input\{", proof_txt):
            continue
        steps = split_steps(proof_txt)
        row = {
            "paper": pid, "title": meta.get("title", ""), "published": meta.get("published", "")[:10],
            "primary_category": meta.get("primary_category", ""), "main_file": main,
            "kind": envmap.get(target[2], "theorem"), "env": target[2], "stmt_opt": target[3],
            "proof_opt": re.sub(r"\s+", " ", popt)[:200],
            "partial_heading": is_partial_heading(popt),   # judged on the FULL heading, before any display truncation
            "proof_heading": popt,   # the raw heading in full (Codex reviewer's regression test reads this name)
            "labels": LABEL_RE.findall(target[4])[:3],
            "pair_rule": pair_rule, "pair_gap_chars": pair_gap, "stmt_named_elsewhere": stmt_named_elsewhere,
            "statement": stmt_txt, "steps": steps, "n_steps": len(steps),
            "proof_chars": sum(len(x) for x in steps), "stmt_chars": len(stmt_txt),
            "external_refs": ext[0], "math_steps": sum(1 for x in steps if has_math(x)),
            "macros_expanded": n_exp,
        }
        row["digest"] = hashlib.sha256((re.sub(r"\s+", " ", stmt_txt + "|" + " ".join(steps))).encode("utf-8")).hexdigest()[:16]
        row["accept"], row["reject_reason"] = accept(row)
        rows.append(row)
    return rows, "ok"


# 2026-09-06 11:4x (Codex reviewer's negative row on <item>: "Proof of Theorem~\ref{thm:main1}, part (3)" was
# paired with the whole three-part statement and labelled a clean proof of it). A heading that names a part, a
# direction, a bound, a case, or a sketch is not a proof of the displayed statement.
PARTIAL_RE = re.compile(
    r"\bparts?\b|\bitems?\b|\bcases?\b|\bstep\b|\(\s*(?:i{1,3}|iv|v|vi|[a-h]|\d{1,2})\s*\)|"
    r"\b(?:first|second|third|fourth|last|upper|lower|easy|hard|remaining|other)\s+(?:part|bound|half|inequality|"
    r"assertion|statement|claim|direction|implication|inclusion|estimate|equality)\b|"
    r"\bonly if\b|\bif part\b|\bnecessity\b|\bsufficiency\b|\bconverse\b|\bdirection\b|\bimplication\b|"
    r"\\(?:Rightarrow|Leftarrow|Longrightarrow|Longleftarrow|implies|iff)\b|=>|<=|"
    r"\bsketch\b|\boutline\b|\bidea\b|\bheuristic\b|\bcontinued\b|\bcont\b|\bcompletion\b|\bconclusion of\b|"
    r"\b(?:lower|upper)\s+bound\b|\binequality\s*\(|\bequation\s*\(|\\eqref", re.I)


def is_partial_heading(popt):
    if not popt:
        return False
    t = re.sub(r"\\(?:ref|cref|Cref|autoref|label)\{[^}]*\}", " ", popt)
    return bool(PARTIAL_RE.search(t))


def accept(r):
    if r.get("partial_heading") or is_partial_heading(r.get("proof_opt", "")):
        return False, "partial_statement_proof"   # name aligned with the Codex reviewer's regression test (was partial_proof_heading in proofs_v2.jsonl rows before 13:1x)
    if not (3 <= r["n_steps"] <= 25):
        return False, "n_steps"
    if not (250 <= r["proof_chars"] <= 6000):
        return False, "proof_chars"
    if not (40 <= r["stmt_chars"] <= 1800):
        return False, "stmt_chars"
    if r["external_refs"] > 3:
        return False, "external_refs"
    if r["math_steps"] * 3 < r["n_steps"]:
        return False, "math_steps"
    if max(len(x) for x in r["steps"]) > 1500:
        return False, "step_too_long"
    if "\u0001" in " ".join(r["steps"]):
        return False, "placeholder_leak"
    if re.search(r"\\(?:begin|end)\{proof\}", " ".join(r["steps"])):
        return False, "nested_proof"
    joined = " ".join(r["steps"])
    if joined.count("[citation]") >= 3:
        return False, "citation_heavy"
    if re.search(r"same way as|similarly to the proof|analogous(?:ly)? to the proof|identical to the proof|"
                 r"mutatis mutandis|we omit|is omitted|left to the reader|proceeds (?:exactly )?as in|"
                 r"verbatim|word for word|follows (?:directly |immediately )?from \[citation\]|"
                 r"as in the proof of \[citation\]|standard and (?:is )?omitted|"
                 r"previous paragraphs?|preceding paragraphs?|described above|setup above|the above setup|"
                 r"notation (?:of|from|in) (?:the )?(?:previous|preceding)|same argument as", joined, flags=re.I):
        return False, "by_reference"
    if re.search(r"\\<|\\csname|\\makeatletter|\\@|\\newcommand|\\def\b|\\usepackage", joined + r["statement"]):
        return False, "raw_macro_residue"
    if r["statement"].count("[citation]") >= 2:
        return False, "stmt_citation_heavy"
    return True, ""


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default="proofs.jsonl")
    ap.add_argument("--limit", type=int, default=0)
    ap.add_argument("--ids", default="")
    ap.add_argument("--stats", default="")
    a = ap.parse_args()
    if a.stats:
        rows = [json.loads(l) for l in io.open(a.stats, encoding="utf-8") if l.strip()]
        acc = [r for r in rows if r["accept"]]
        print("rows", len(rows), "accepted", len(acc), "papers", len({r["paper"] for r in rows}),
              "papers_with_accepted", len({r["paper"] for r in acc}))
        print("reject reasons", collections.Counter(r["reject_reason"] for r in rows if not r["accept"]).most_common())
        print("kinds", collections.Counter(r["kind"] for r in acc).most_common())
        print("steps hist", sorted(collections.Counter(min(r["n_steps"], 25) for r in acc).items()))
        return
    meta = {}
    for ln in io.open(LISTING, encoding="utf-8"):
        try:
            r = json.loads(ln)
            meta[r["base_id"]] = r
        except Exception:
            pass
    done = set()
    if os.path.exists(a.out):
        for ln in io.open(a.out, encoding="utf-8"):
            try:
                done.add(json.loads(ln)["paper"])
            except Exception:
                pass
    if a.ids:
        ids = [x for x in a.ids.split(",") if x]
    else:
        # only papers whose download is COMPLETE (logged), never a tex dir the harvester is still writing
        dllog = os.path.join(os.path.dirname(TEX), "download_log.jsonl")
        ids = []
        if os.path.exists(dllog):
            for ln in io.open(dllog, encoding="utf-8"):
                try:
                    r = json.loads(ln)
                except Exception:
                    continue
                if r.get("kind") in ("tar", "single_tex") and r.get("n_tex", 0) > 0:
                    ids.append(r["base_id"])
        else:
            ids = sorted(p.replace("_", "/") if "_" in p and not p[0].isdigit() else p for p in os.listdir(TEX))
    ids = [i for i in ids if i not in done]
    if a.limit:
        ids = ids[:a.limit]
    t0 = time.time()
    n_rows = n_acc = 0
    status = collections.Counter()
    with io.open(a.out, "a", encoding="utf-8") as out:
        for k, pid in enumerate(ids, 1):
            try:
                rows, st = process_paper(pid, meta.get(pid, {}))
            except Exception as e:
                rows, st = [], "error:" + e.__class__.__name__
            status[st] += 1
            for r in rows:
                out.write(json.dumps(r, ensure_ascii=False) + "\n")
                n_rows += 1
                n_acc += int(r["accept"])
            if k % 100 == 0:
                out.flush()
                print("%d papers, %d rows, %d accepted, %.0fs" % (k, n_rows, n_acc, time.time() - t0), flush=True)
    print("done: %d papers, %d rows, %d accepted; status %s" % (len(ids), n_rows, n_acc, dict(status)))


if __name__ == "__main__":
    main()
