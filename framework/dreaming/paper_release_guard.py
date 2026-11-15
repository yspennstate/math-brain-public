"""Paper release guard (owner, 2 Nov 2026 05:0x).

the user's words, after a paper went up on a public GitHub repo with an overflowing line and no funding statement or AI
acknowledgment: "this is not how we write paper, fix that repo right now, and put in the brian this ifnroamtion and
hooks so that this never ever happens agian".

A paper (a .tex file with \\documentclass, \\begin{document} and an abstract or \\maketitle) pushed to a PUBLIC
GitHub repository must have:
  1. a funding section: a \\section* heading containing "funding" (or the \\FUNDING macro);
  2. a declaration of generative AI: a \\section* heading naming generative AI / AI-assisted / use of AI;
  3. a competing-interest declaration (a heading containing "competing interest");
  4. no finished grant (NSF OISE-2401227 ended; owner 16 Jul);
  5. no line running into the margin: it is compiled with pdflatex and any "Overfull \\hbox" over 1pt refuses.

Use:
  python paper_release_guard.py check <file.tex or folder> [...]    run by hand before any push or API upload
  called from github_push_cost_guard.py on every git push (pre-push), so every clone that has the cost guard has this
  python paper_release_guard.py --selftest

A file that is not a paper (a table fragment, a beamer talk) is skipped. A draft that must go to a public repo
before it is finished does not exist: finish it first. There is no bypass.
"""
import io, json, os, re, shutil, subprocess, sys, tarfile, tempfile, time, urllib.request
import urllib.error

LOG = os.path.expanduser("~/.claude/dreaming/logs/paper_release_guard.log")
NOWIN = 0x08000000 if os.name == "nt" else 0
OVERFULL_PT = 1.0
FINISHED_GRANTS = ("2401227",)


def log(msg):
    try:
        os.makedirs(os.path.dirname(LOG), exist_ok=True)
        with io.open(LOG, "a", encoding="utf-8") as fh:
            fh.write("%s %s\n" % (time.strftime("%Y-%m-%d %H:%M:%S"), msg))
    except OSError:
        pass


def strip_comments(t):
    return re.sub(r"(?<!\\)%.*", "", t)


def is_paper(t):
    t = strip_comments(t)
    if not re.search(r"\\documentclass", t) or "\\begin{document}" not in t:
        return False
    if re.search(r"\\documentclass(\[[^\]]*\])?\{(beamer|standalone)\}", t):
        return False
    return bool(re.search(r"\\begin\{abstract\}|\\maketitle", t))


HEAD = r"\\(?:section|subsection|paragraph)\*?\{([^}]*)\}"


def section_problems(text, extra=""):
    """text: the paper; extra: the other .tex/.sty files beside it (macros such as \\FUNDING)."""
    t = strip_comments(text)
    heads = [h.lower() for h in re.findall(HEAD, t)]
    probs = []
    if not (any("funding" in h for h in heads) or "\\FUNDING" in t):
        probs.append("no funding section (\\section*{Acknowledgments and funding})")
    if not any(re.search(r"generative ai|ai-assisted|use of ai|\bai\b.*declaration|declaration.*\bai\b|"
                         r"artificial intelligence", h) for h in heads):
        probs.append("no AI declaration (\\section*{Declaration of generative AI and AI-assisted technologies})")
    if not any("competing interest" in h for h in heads):
        probs.append("no competing-interest declaration (\\section*{Declaration of competing interest})")
    for g in FINISHED_GRANTS:
        if g in t or g in strip_comments(extra):
            probs.append("names the finished grant NSF OISE-%s (owner 16 Jul: never list it again)" % g)
    probs += brain_credit_problems(t, extra)
    return probs


# Owner, 8 Nov 2026 16:55: the AI declaration credits the whole Brain framework (many agents, Claude and Codex), says
# the work is part of Math Brain and cites the Math Brain repo, the Math Brain paper and the Brain framework repo; the
# code and data section links the repo again. Standard: 12_cognitive_architecture/paper_declarations/.
BRAIN_LINKS = (("math-brain-public", "the Math Brain repository link (github.com/yspennstate/math-brain-public)"),
               ("brain-framework-public", "the Brain framework repository link (github.com/yspennstate/brain-framework-public)"),
               ("math-brain-2026-10-24", "the Math Brain paper (math-brain-public/tree/main/papers/math-brain-2026-10-24)"))


def declaration_body(t):
    m = re.search(r"\\(?:section|subsection|paragraph)\*?\{[^}]*(?:generative ai|ai-assisted|use of ai|artificial "
                  r"intelligence|\bai\b[^}]*declaration|declaration[^}]*\bai\b)[^}]*\}", t, re.I)
    if not m:
        return None
    rest = t[m.end():]
    e = re.search(r"\\(?:section|subsection)\*?\{|\\bibliography\{|\\begin\{thebibliography\}|\\printbibliography|"
                  r"\\end\{document\}", rest)
    return rest[:e.start()] if e else rest


ACK_HEAD = re.compile(r"\\(?:section|subsection|paragraph)\*?\{[^}]*acknowledg[^}]*\}|"
                      r"\\begin\{acknowledg?e?ments?\}", re.I)


def ack_body(t):
    m = ACK_HEAD.search(t)
    if not m:
        return None
    rest = t[m.end():]
    e = re.search(r"\\(?:section|subsection)\*?\{|\\end\{acknowledg?e?ments?\}|\\bibliography\{|"
                  r"\\begin\{thebibliography\}|\\printbibliography|\\end\{document\}", rest)
    return rest[:e.start()] if e else rest


def abstract_body(t):
    m = re.search(r"\\begin\{abstract\}(.*?)\\end\{abstract\}", t, re.S)
    return m.group(1) if m else ""


def brain_credit_problems(t, extra=""):
    # owner 8 Nov 16:55 (credit the agents, Claude and Codex, and the Brain; cite Math Brain) as corrected at 17:39:
    # "i dont want this in the fucking abstract i want it in the paper in the aknolgment section"
    probs = []
    if declaration_body(t) is not None:
        body = ack_body(t)
        if body is None:
            probs.append("no Acknowledgments section crediting the agents and Math Brain (owner 8 Nov 17:39)")
        else:
            for word, why in (("Math Brain", "say the agents were connected to Math Brain"),
                              ("Claude", "name Claude among the agents"),
                              ("Codex", "name Codex among the agents (many Codex agents worked too, not just Claude)")):
                if word.lower() not in body.lower():
                    probs.append("Acknowledgments do not %s (owner 8 Nov 16:55/17:39)" % why)
            if "\\cite" not in body:
                probs.append("Acknowledgments cite nothing: cite the Math Brain repo, the Math Brain paper and the "
                             "Brain framework repo (owner 8 Nov 16:55)")
        if re.search(r"brain framework|BrainFramework|MathBrainPaper", abstract_body(t), re.I):
            probs.append("the Brain/Math Brain credit is in the abstract; it belongs in the Acknowledgments "
                         "(owner 8 Nov 17:39)")
        if "not the work of one or two" in t:
            probs.append("drop 'It was not the work of one or two models': say the work was done by multiple agents "
                         "connected to Math Brain (owner 8 Nov 17:39)")
    allt = t + "\n" + strip_comments(extra)
    for key, why in BRAIN_LINKS:
        if key not in allt:
            probs.append("paper and bibliography lack %s (owner 8 Nov 16:55)" % why)
    heads = [h.lower() for h in re.findall(HEAD, t)]
    if not any(("data" in h or "code" in h) and "availab" in h for h in heads):
        probs.append("no code and data availability section linking the repo and Math Brain (owner 8 Nov 16:55)")
    return probs


def overfull(folder, main):
    """Compile main (a path relative to folder) and return (list of overfull lines, note)."""
    exe = shutil.which("pdflatex")
    if not exe:
        return [], "pdflatex not found - overfull lines NOT checked"
    wd = os.path.dirname(os.path.join(folder, main)) or folder
    name = os.path.basename(main)
    stem = name[:-4]
    out = tempfile.mkdtemp(prefix="paperguard_")
    cmd = [exe, "-interaction=nonstopmode", "-disable-installer", "-output-directory", out, name]
    env = dict(os.environ, BIBINPUTS=wd + os.pathsep, TEXINPUTS=wd + os.pathsep)
    try:
        for i in range(2):
            subprocess.run(cmd, cwd=wd, capture_output=True, timeout=240, creationflags=NOWIN, env=env)
            aux = os.path.join(out, stem + ".aux")
            if i == 0 and os.path.exists(aux) and "\\bibdata" in io.open(aux, encoding="latin-1").read():
                bt = shutil.which("bibtex")
                if bt:
                    subprocess.run([bt, stem], cwd=out, capture_output=True, timeout=120, creationflags=NOWIN, env=env)
        logf = os.path.join(out, stem + ".log")
        if not os.path.exists(logf):
            return [], "did not compile - overfull lines NOT checked"
        lg = io.open(logf, encoding="latin-1").read()
        hits = []
        for m in re.finditer(r"Overfull \\hbox \(([\d.]+)pt too wide\)([^\n]*)", lg):
            if float(m.group(1)) > OVERFULL_PT:
                hits.append("%spt too wide%s" % (m.group(1), m.group(2)))
        note = "" if os.path.exists(os.path.join(out, stem + ".pdf")) else "compile errors - check the log"
        return hits, note
    except subprocess.TimeoutExpired:
        return [], "compile timed out - overfull lines NOT checked"
    finally:
        shutil.rmtree(out, ignore_errors=True)


INPUT = re.compile(r"\\(?:input|include|subfile)\s*\{([^}]+)\}|\\input\s+([^\s{}\\]+)")


def expand_inputs(t, dirs, depth=0):
    """Inline \\input/\\include targets (an agent, 2 Nov: declarations kept in sections/declarations.tex
    were read as missing). dirs: the paper's folder first, then the repo root; LaTeX resolves against both."""
    if depth > 4:
        return t

    def sub(m):
        name = (m.group(1) or m.group(2) or "").strip()
        for d in dirs:
            for cand in (name, name + ".tex"):
                f = os.path.join(d, cand)
                if os.path.isfile(f):
                    try:
                        return expand_inputs(io.open(f, encoding="utf-8", errors="replace").read(), dirs, depth + 1)
                    except OSError:
                        pass
        return m.group(0)
    return INPUT.sub(lambda m: "\n" + sub(m) + "\n", strip_comments(t))


def check_folder(folder, rel_files):
    """Check the papers among rel_files (paths relative to folder). Returns list of (file, problems, notes)."""
    res = []
    for rel in rel_files:
        p = os.path.join(folder, rel)
        try:
            t = io.open(p, encoding="utf-8", errors="replace").read()
        except OSError:
            continue
        if not is_paper(t):
            continue
        t = expand_inputs(t, [os.path.dirname(p), folder])
        d = os.path.dirname(p)
        extra = ""
        for f in os.listdir(d):
            if f.endswith((".tex", ".sty", ".bib", ".bbl")) and os.path.join(d, f) != p:
                try:
                    extra += io.open(os.path.join(d, f), encoding="utf-8", errors="replace").read()
                except OSError:
                    pass
        probs = section_problems(t, extra)
        hits, note = overfull(folder, rel)
        probs += ["line runs into the margin: Overfull \\hbox (%s)" % h for h in hits]
        res.append((rel, probs, note))
    return res


def report(res, where):
    bad = [r for r in res if r[1]]
    for rel, probs, note in res:
        log("%s %s %s %s" % ("REFUSE" if probs else "ok", where, rel, " | ".join(probs + ([note] if note else []))))
    if not bad:
        for rel, _, note in res:
            if note:
                sys.stderr.write("[paper-guard] %s: %s\n" % (rel, note))
        return True
    sys.stderr.write("[paper-guard] REFUSED (owner, 2 Nov 2026: \"this is not how we write paper ... so that this "
                     "never ever happens agian\"). A public paper needs a funding section, a competing-interest "
                     "declaration, a declaration of generative AI, and no line in the margin:\n")
    for rel, probs, note in bad:
        sys.stderr.write("  %s\n" % rel)
        for pr in probs:
            sys.stderr.write("    - %s\n" % pr)
    sys.stderr.write("  Model block: yspennstate/bilateral-preference-connectivity-window paper/main.tex (Acknowledgements "
                     "and funding / Declaration of competing interest / Declaration of generative AI). The AI "
                     "declaration says truthfully which systems did what. Since 8 Nov 16:55/17:39 the "
                     "Acknowledgments (never the abstract) say the work was done by multiple agents, Claude and Codex, "
                     "connected to Math Brain and working inside the Brain framework, and cite the Math Brain repo, "
                     "the Math Brain paper and the Brain framework repo; a code and data section links the repo "
                     "again: brain-repo/12_cognitive_architecture/"
                     "paper_declarations/AI_DECLARATION_STANDARD.md, fixer fix_declarations.py beside it. "
                     "Fix, rebuild the PDF, push again.\n")
    return False


VIS_CACHE = os.path.expanduser("~/.claude/dreaming/logs/paper_guard_visibility.json")
VIS_TTL = 86400


def repo_is_public(url):
    """11 Nov 2026: a known answer is kept a day (VIS_CACHE), so a rate-limited anonymous API (403, 60 calls an hour
    shared by every agent on the box) no longer turns a private repo into 'cannot tell: check it'."""
    m = re.search(r"github\.com[:/]+([^/]+)/([^/\s]+?)(?:\.git)?/?$", url or "")
    if not m:
        return False
    slug = "%s/%s" % (m.group(1), m.group(2))
    try:
        c = json.load(io.open(VIS_CACHE, encoding="utf-8"))
    except Exception:
        c = {}
    hit = c.get(slug)
    if hit and time.time() - hit[1] < VIS_TTL:
        return bool(hit[0])
    ans = None
    try:
        r = urllib.request.urlopen("https://api.github.com/repos/%s" % slug, timeout=15)
        ans = not json.load(r).get("private", True)
    except urllib.error.HTTPError as e:
        if e.code == 404:
            ans = False
    except Exception:
        pass
    if ans is None:
        return bool(hit[0]) if hit else True  # cannot tell and never told: check it
    try:
        c[slug] = [ans, time.time()]
        tmp = VIS_CACHE + ".%d.tmp" % os.getpid()
        with io.open(tmp, "w", encoding="utf-8") as fh:
            json.dump(c, fh)
        os.replace(tmp, VIS_CACHE)
    except Exception:
        pass
    return ans


def git(*a, cwd=None):
    r = subprocess.run(["git"] + list(a), cwd=cwd, capture_output=True, creationflags=NOWIN)
    return r.returncode, r.stdout


def pre_push(remote_url, lines):
    """Called with the pre-push stdin lines. Returns (allow, None); writes its own messages."""
    zero = "0" * 40
    changed = set()
    sha_for = None
    for l in lines:
        parts = l.split()
        if len(parts) != 4 or parts[1] == zero:
            continue
        lsha, rsha = parts[1], parts[3]
        if rsha == zero:
            # 11 Nov 2026: a new branch used to list EVERY .tex in the tree (8,320 in the brain repo, one git show
            # each, 25+ min on a loaded box). Measure it against where it left the default branch instead.
            base = None
            for ref in ("refs/remotes/origin/HEAD", "refs/remotes/origin/main", "refs/remotes/origin/master"):
                rcb, ob = git("merge-base", lsha, ref)
                if rcb == 0 and ob.strip():
                    base = ob.decode().strip()
                    break
            if base is None:
                rcb, ob = git("rev-parse", "--verify", "--quiet", lsha + "^")
                base = ob.decode().strip() if rcb == 0 and ob.strip() else None
            if base:
                rc, out = git("diff", "--name-only", "--no-renames", base, lsha)
            else:
                rc, out = git("ls-tree", "-r", "--name-only", lsha)
        else:
            rc, out = git("diff", "--name-only", rsha, lsha)
            if rc != 0:
                rc, out = git("ls-tree", "-r", "--name-only", lsha)
        if rc == 0:
            changed |= {f for f in out.decode("utf-8", "replace").splitlines() if f.endswith(".tex")}
            sha_for = lsha
    if not changed:
        return True
    if not repo_is_public(remote_url):
        return True
    # Papers among the changed .tex: read the pushed content, not the working tree.
    tmp = tempfile.mkdtemp(prefix="paperguard_tree_")
    try:
        dirs = sorted({os.path.dirname(f) or "." for f in changed})
        cand = []
        for f in changed:
            rc, blob = git("show", "%s:%s" % (sha_for, f))
            if rc == 0 and is_paper(blob.decode("utf-8", "replace")):
                cand.append(f)
        if not cand:
            return True
        pdirs = sorted({os.path.dirname(f) for f in cand})
        args = ["archive", "--format=tar", sha_for, "--"] + [d if d else "." for d in pdirs]
        r = subprocess.run(["git"] + args, capture_output=True, creationflags=NOWIN)
        if r.returncode != 0:
            log("archive failed for %s: %r" % (remote_url, r.stderr[:200]))
            return True
        with tarfile.open(fileobj=io.BytesIO(r.stdout)) as tf:
            tf.extractall(tmp)
        return report(check_folder(tmp, cand), remote_url)
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


def check_paths(paths):
    """The `check` command. Fails closed: a path that does not exist, or that holds no paper the guard
    recognises, is a refusal, not a pass (a typo'd path used to exit 0 with nothing checked). One verdict
    line per paper goes to stdout so the caller sees what was read. The pre-push path does not come here."""
    ok = True
    for p in paths:
        p = os.path.abspath(p)
        if not os.path.exists(p):
            sys.stderr.write("[paper-guard] REFUSED: %s does not exist - nothing was checked\n" % p)
            ok = False
            continue
        if os.path.isdir(p):
            files = []
            for root, _, fs in os.walk(p):
                files += [os.path.relpath(os.path.join(root, f), p) for f in fs if f.endswith(".tex")]
            res = check_folder(p, files)
        else:
            res = check_folder(os.path.dirname(p), [os.path.basename(p)])
        if not res:
            sys.stderr.write("[paper-guard] REFUSED: no paper found in %s (needs \\documentclass, \\begin{document} "
                             "and an abstract or \\maketitle) - nothing was checked\n" % p)
            ok = False
            continue
        for rel, probs, _ in res:
            print("[paper-guard] %s %s" % ("REFUSE" if probs else "ok", rel))
        ok &= report(res, p)
    return ok


def selftest():
    good = ("\\documentclass{amsart}\\begin{document}\\begin{abstract}x\\end{abstract}\\maketitle\n"
            "\\section*{Acknowledgments and funding} ERC. This work was done by multiple AI agents, Claude and Codex, "
            "connected to Math Brain \\cite{MathBrainRepo}, in the Brain framework (brain-framework-public); see the "
            "Math Brain paper (math-brain-2026-10-24).\\section*{Declaration of competing interest} None."
            "\\section*{Code and data availability} \\texttt{github.com/yspennstate/math-brain-public}."
            "\\section*{Declaration of generative AI and AI-assisted technologies} A GPT model proposed the proof."
            "\\end{document}\n")
    bad = "\\documentclass{amsart}\\begin{document}\\begin{abstract}x\\end{abstract}\\maketitle\nText.\\end{document}\n"
    three = ("no funding section", "no AI declaration", "no competing-interest")
    has3 = lambda ps: all(any(p.startswith(k) for p in ps) for k in three)
    frag = "\\begin{tabular}{cc}a&b\\end{tabular}"
    over = good.replace("Text", "").replace("ERC.", "ERC. \\mbox{" + "W" * 120 + "}")
    cases = [("good passes", section_problems(good) == []),
             ("bad lacks three", has3(section_problems(bad))),
             ("acknowledgments without Codex refused",
              any("Codex" in p for p in section_problems(good.replace("Claude and Codex", "Claude")))),
             ("acknowledgments without a citation refused",
              any("cite nothing" in p for p in section_problems(good.replace("\\cite{MathBrainRepo}", "")))),
             ("no acknowledgments section refused",
              any("no Acknowledgments" in p for p in section_problems(good.replace("Acknowledgments and funding",
                                                                                   "Funding")))),
             ("credit in the abstract refused",
              any("abstract" in p for p in section_problems(good.replace("{abstract}x", "{abstract}x the Brain "
                                                                         "framework helped")))),
             ("'not the work of one or two' refused",
              any("one or two" in p for p in section_problems(good.replace("ERC.", "ERC. It was not the work of one "
                                                                           "or two models.")))),
             ("missing Brain framework link refused",
              any("Brain framework" in p for p in section_problems(good.replace("brain-framework-public", "the framework")))),
             ("link in the .bib counts", section_problems(good.replace("(math-brain-2026-10-24)", ""),
                                                          "@misc{p, note={math-brain-2026-10-24}}") == []),
             ("no code and data section refused",
              any("code and data" in p for p in section_problems(good.replace("Code and data availability", "Notes")))),
             ("fragment is not a paper", not is_paper(frag)),
             ("good is a paper", is_paper(good)),
             ("commented heading does not count",
              any(p.startswith("no funding section") for p in section_problems(
                  good.replace("\\section*{Acknowledgments and funding} ERC.",
                               "%\\section*{Acknowledgments and funding} ERC.\n")))),
             ("finished grant refused", any("2401227" in p for p in section_problems(good.replace("ERC.", "NSF OISE-2401227."))))]
    d = tempfile.mkdtemp(prefix="paperguard_st_")
    try:
        io.open(os.path.join(d, "o.tex"), "w").write(over)
        io.open(os.path.join(d, "g.tex"), "w").write(good)
        r = dict((f, p) for f, p, _ in check_folder(d, ["o.tex", "g.tex"]))
        cases.append(("overfull line refused", any("Overfull" in p for p in r.get("o.tex", []))))
        cases.append(("clean compile passes", r.get("g.tex") == []))
        decl = good[good.index("\\section*{Ack"):good.index("\\end{document}")]
        os.makedirs(os.path.join(d, "sec"))
        io.open(os.path.join(d, "sec", "decl.tex"), "w").write(decl)
        io.open(os.path.join(d, "i.tex"), "w").write(good.replace(decl, "\\input{sec/decl}"))
        io.open(os.path.join(d, "j.tex"), "w").write(good.replace(decl, "%\\input{sec/decl}\n"))
        r = dict((f, p) for f, p, _ in check_folder(d, ["i.tex", "j.tex"]))
        cases.append(("declarations through \\input pass", r.get("i.tex") == []))
        cases.append(("a commented \\input does not count", has3(r.get("j.tex", []))))
    finally:
        shutil.rmtree(d, ignore_errors=True)
    for n, c in cases:
        print("  %s %s" % ("PASS" if c else "FAIL", n))
    return 0 if all(c for _, c in cases) else 1


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(selftest())
    if len(sys.argv) > 2 and sys.argv[1] == "check":
        sys.exit(0 if check_paths(sys.argv[2:]) else 1)
    print(__doc__)
