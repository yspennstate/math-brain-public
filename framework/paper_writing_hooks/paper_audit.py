# -*- coding: utf-8 -*-
"""paper_audit.py - an editor's audit of a paper by a reader that did not write it.

His 12 Nov 2026 order after a journal declined a paper as "not thoroughly edited": "more editing, more auditing
... i want more agents working on audit, making sure that the million rules i have, including no self
introspection, are being followed".

  python paper_audit.py roster [N]          his papers, most lint findings first, with the state of their audit
  python paper_audit.py next [N]            the next N papers with no fresh audit (paths, one per line)
  pythonw paper_audit.py run <file.tex>     audit ONE paper: start a headless Claude session (Fable 5.2, --effort
                                            high, a pool account, no window, below-normal priority), wait for it,
                                            check the report, record it. Start it hidden and detached:
      Start-Process pythonw -ArgumentList '<this file>','run','<file.tex>' -WindowStyle Hidden
  python paper_audit.py status              runs in flight and the last ten finished

A run refuses to start when free memory is under 6 GB, when MAX_RUNNING audits are already in flight, when the
owner's hold on Claude agents is set, or when no pool account has room. The auditor never edits the paper; its
report goes to the audits home (12_cognitive_architecture/audits/reports/<date>/paper_audit_<slug>/REPORT.md) and
audit_index.json here records it, which is what hook W43 reads.  (an agent, 12 Nov 2026)
"""
import hashlib
import json
import os
import subprocess
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import pw_core as C  # noqa: E402
import pw_hooks as H  # noqa: E402

AUDITS = "~/brain-repo/12_cognitive_architecture/audits/reports"
INDEX = os.path.join(HERE, "audit_index.json")
RUNS = os.path.join(HERE, "audit_runs.jsonl")
STOP = os.path.join(HERE, "STOP_AUDITS")
MODEL = "claude-fable-5-2"
MAX_RUNNING = 2
MIN_FREE_GB = 6.0
TIMEOUT_S = 150 * 60  # 80 min cut two of three high-effort reads of a 1300-line paper (12 Nov)

for _s in (sys.stdout, sys.stderr):
    try:
        _s.reconfigure(encoding="utf-8", errors="replace")
    except Exception:  # noqa: BLE001
        pass


def key(tex):
    return os.path.abspath(tex).replace("\\", "/").lower()


def slug(tex):
    parts = [p for p in os.path.abspath(tex).replace("\\", "/").split("/") if p]
    name = "_".join(parts[-3:]).rsplit(".", 1)[0]
    name = "".join(c if c.isalnum() else "_" for c in name).strip("_")[:70]
    return name + "_" + hashlib.md5(key(tex).encode()).hexdigest()[:6]


def load_index():
    try:
        with open(INDEX, encoding="utf-8") as f:
            return json.load(f)
    except (OSError, ValueError):
        return {}


def save_index(idx):
    tmp = INDEX + ".%d.tmp" % os.getpid()
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump(idx, f, indent=1)
    os.replace(tmp, INDEX)


def log_run(row):
    row["at"] = time.strftime("%Y-%m-%dT%H:%M:%S")
    with open(RUNS, "a", encoding="utf-8") as f:
        f.write(json.dumps(row) + "\n")


def runs():
    out = []
    try:
        with open(RUNS, encoding="utf-8") as f:
            for ln in f:
                try:
                    out.append(json.loads(ln))
                except ValueError:
                    pass
    except OSError:
        pass
    return out


def in_flight():
    import psutil
    started, ended = {}, set()
    for r in runs():
        if r.get("event") == "start":
            started[r["run"]] = r
        elif r.get("event") in ("end", "refused"):
            ended.add(r.get("run"))
    live = []
    for rid, r in started.items():
        if rid in ended:
            continue
        try:
            p = psutil.Process(r["wrapper_pid"])
            if p.is_running() and "python" in p.name().lower():
                live.append(r)
        except Exception:  # noqa: BLE001
            pass
    return live


def state_of(tex, idx):
    rec = idx.get(key(tex))
    if not rec or not os.path.exists(rec.get("report", "")):
        return "none"
    try:
        if rec.get("tex_sha"):
            return "fresh" if rec["tex_sha"] == C.paper_sha(tex) else "stale"
        return "fresh" if rec.get("tex_mtime", 0) >= os.path.getmtime(tex) - 60 else "stale"
    except OSError:
        return "none"


def roster():
    idx = load_index()
    flying = {key(r["tex"]) for r in in_flight()}
    rows = []
    for fp in C.own_sources():
        d = C._read_doc(fp)
        if d is None or not d.whole or d.words < 800:
            continue
        must = should = 0
        for h in H.TEXT:
            g = C.scan(h, [d])
            m = C.must_n(h, g)
            must += m
            should += len(g) - m
        st = "running" if key(fp) in flying else state_of(fp, idx)
        rows.append((must, should, d.words, st, fp))
    rows.sort(key=lambda r: (-r[0], -r[1]))
    return rows


PROMPT = """You are the handling editor's first reader for a mathematics journal, and you did not write this paper.
Audit ONE paper. Its source: {tex}
(other .tex and .bib files in the same folder belong to it; a compiled PDF beside it may be read too.)

Why this audit exists. On 11 Nov 2026 a journal declined a paper of this author whose result its own editors called
significant, because (1) the introduction did not say what was new against the author's earlier paper, (2) a lemma
of the earlier paper was reprinted instead of cited, (3) the text "does not appear to have undergone a thorough
editing process": the one paragraph that said what was new was a list of labels the paper had coined and not yet
defined, opened by a sentence about the paper itself. The author's order the next morning: more editing, more
auditing, no self-introspection, every paper publishable as is.

Read first: ~/.claude/dreaming/paper_writing_hooks/PAPER_RULES.md (his rules, in his words).
Then run, and treat its output as leads to judge and not as the audit:
  python -X utf8 ~/.claude/dreaming/paper_writing_hooks/paper_lint.py "{tex}"

Then read the paper yourself, the first six pages twice, and write the report. What the report must contain:

1. THE EDITOR'S QUESTION. In your own three sentences, from the introduction alone: what was known before (with
   the citation), what fails when one tries to extend it, and the one new idea. If the introduction does not let
   you write these, say exactly which is missing and quote the passage that should have carried it. If the paper
   builds on an earlier paper of the same author, say whether a reader of that paper can tell from pages 1-2
   that this one is not routine.
2. SENTENCES ABOUT THE PAPER. Every sentence, anywhere outside the declaration section, whose subject is the
   paper, the draft, a version, the writing, a search, a check, a computation's "sanity", an agent or the author's
   care ("we are careful", "an honest account", "the present paper does not", "was corrected", "we found no").
   Line number, the sentence, and the replacement: either delete, or the mathematical statement it stands for.
3. NAMES. Every term coined in the paper: where it is first used, where it is defined, and whether the first use
   comes before the definition (abstract and introduction count). Every object that carries more than one name.
   Every symbol used before it is introduced or defined more than once.
4. REPRINTED MATERIAL. Statements or proofs that repeat an earlier paper (his or anyone's) where a citation would
   do. For his own earlier papers the lint's W21 lists word-for-word sentences; check what it found and look for
   the same lemma restated in other words.
5. CITATIONS. Brackets of several references with no word on what any of them does; a claim of novelty with the
   closest prior result not stated; references nobody can look up; a cited theorem used beyond its hypotheses.
6. STRUCTURE AND PROSE. Sections that exist only as outline (under a page, a conclusion repeating the abstract, a
   roadmap that lists section numbers), slogans in place of statements, promises the text does not keep, words
   that read as machine-written, runs of bold, colon-list abstracts, theorem statements with hidden hypotheses or
   unnamed constants.
7. WHAT IS MISSING ON THE PAGE. Name and affiliation, funding statement, declaration of AI use, code and data
   line pointing at a repository that exists, overfull lines or "??" in the log or PDF if present.
8. MATHEMATICS YOU CAN CHECK IN PASSING. You are not asked to re-prove the paper. But if while reading you see a
   step that does not follow, a statement contradicted elsewhere in the paper, or a constant that changes between
   statement and proof, record it with the line. Mark each as CERTAIN or SUSPECTED.
9. VERDICT. One of: SEND AS IS / MINOR EDIT (list) / REWRITE THE INTRODUCTION / NOT READY. Then the rewritten
   second paragraph of the introduction as you would have it (known / what fails / new idea, with the estimate
   displayed), using only mathematics that is in the paper.

Rules for you.
- You change nothing in the paper's folder: no edit, no compile into it, no git command there. You write ONLY in
  {out}/ : REPORT.md (append each section as you finish it, so a stop loses nothing) and STATUS.md with a NEXT
  line. Any text you propose for the paper follows his rules itself: plain declarative mathematics, no sentence
  about the writing, no word about how the text sounds.
- Every finding carries a line number of the source and the quoted words. A finding you could not confirm on the
  page is not a finding. Count nothing as clean that you did not read.
- Do not start other agents. Do not send email or messages. Do not push anything. Never pipe a program into
  `python -`; cap every command's output (| tail -40). Open no window.
- The first line of REPORT.md is exactly:  VERDICT: <one of the four>  |  MUST-FIX: <n>  |  SHOULD-FIX: <m>
"""


def run(tex):
    import psutil
    tex = os.path.abspath(tex)
    rid = "%s-%d" % (time.strftime("%Y%m%dT%H%M%S"), os.getpid())
    base = {"run": rid, "tex": tex.replace("\\", "/"), "wrapper_pid": os.getpid()}

    def refuse(why):
        log_run(dict(base, event="refused", why=why))
        return 3

    if not os.path.isfile(tex):
        return refuse("no such file")
    if os.path.exists(STOP):
        return refuse("STOP_AUDITS is set")
    free = psutil.virtual_memory().available / 2 ** 30
    if free < MIN_FREE_GB:
        return refuse("free memory %.1f GB is under %.0f GB" % (free, MIN_FREE_GB))
    flying = in_flight()
    if len(flying) >= MAX_RUNNING:
        return refuse("%d audits already in flight" % len(flying))
    if any(key(r["tex"]) == key(tex) for r in flying):
        return refuse("this paper is being audited now")
    sys.path.insert(0, "~/claude_pool")
    try:
        import claude_pool
        env, account = claude_pool.env_for("auto", fallback="main")   # pool accounts full -> his main login
        exe = claude_pool.claude_exe()
    except Exception as e:  # noqa: BLE001
        return refuse("no account: %s" % str(e)[:200])
    out = "%s/%s/paper_audit_%s" % (AUDITS, time.strftime("%Y/%m/%d"), slug(tex))
    os.makedirs(out, exist_ok=True)
    prompt = PROMPT.format(tex=tex.replace("\\", "/"), out=out)
    # The reader sees nothing of earlier reads, so items the author declined came back as new must-fix
    # items on every read (13 Nov, E0018: 5, 3, 4). An AUTHOR_RESPONSE.md in the audit folder is handed on.
    resp = os.path.join(out, "AUTHOR_RESPONSE.md")
    if os.path.isfile(resp):
        prompt += ("\n\nEarlier reads of this paper exist. The author's response to them, item by item, is in "
                   "%s. Read it first. For each item it declines, judge the stated reason: if the reason holds, "
                   "do not raise the item again; if it does not, say why in one line and keep the item.\n"
                   % resp.replace("\\", "/"))
    with open(os.path.join(out, "PROMPT.md"), "w", encoding="utf-8") as f:
        f.write(prompt)
    tex_mtime = os.path.getmtime(tex)
    tex_sha = C.paper_sha(tex)          # of the paper with its \input files, as the reader is about to see it
    # Normal priority on purpose: on a fully loaded box a below-normal claude -p starved before its first model call
    # (12 Nov 2026, 0.8 s CPU in 12 minutes, no connection; raised to normal it ran at once).
    flags = getattr(subprocess, "CREATE_NO_WINDOW", 0)
    t0 = time.time()
    with open(os.path.join(out, "PROMPT.md"), "rb") as fin, \
            open(os.path.join(out, "session.json"), "wb") as fout, \
            open(os.path.join(out, "session.err"), "wb") as ferr:
        p = subprocess.Popen([exe, "-p", "--output-format", "json", "--dangerously-skip-permissions",
                              "--model", MODEL, "--effort", "high", "--disallowedTools",
                              "Bash(taskkill:*)", "Bash(pkill:*)", "Bash(killall:*)", "Bash(wmic:*)",
                              "Bash(git push:*)", "Bash(git commit:*)", "Agent", "Task"],
                             stdin=fin, stdout=fout, stderr=ferr, env=env, creationflags=flags,
                             cwd=out)
        log_run(dict(base, event="start", out=out, account=account, claude_pid=p.pid))
        try:
            rc = p.wait(timeout=TIMEOUT_S)
        except subprocess.TimeoutExpired:
            p.kill()
            rc = -9
    served, session = "", ""
    try:
        with open(os.path.join(out, "session.json"), encoding="utf-8", errors="replace") as f:
            res = json.load(f)
        session = res.get("session_id", "")
        served = ",".join(sorted((res.get("modelUsage") or {}).keys()))
    except (OSError, ValueError):
        pass
    rep = os.path.join(out, "REPORT.md")
    # A REPORT.md left by an earlier run is not this run's report (12 Nov: a run killed at 80 min was
    # recorded with the previous read's verdict). Only a report written after this run started counts.
    ok = os.path.isfile(rep) and os.path.getsize(rep) > 1500 and os.path.getmtime(rep) >= t0
    first = ""
    if ok:
        with open(rep, encoding="utf-8", errors="replace") as f:
            first = f.readline().strip()[:200]
        ok = first.startswith("VERDICT:")
    if ok:
        idx = load_index()
        idx[key(tex)] = {"report": rep.replace("\\", "/"), "tex_mtime": tex_mtime, "tex_sha": tex_sha, "when": time.strftime("%Y-%m-%dT%H:%M:%S"),
                         "verdict": first, "session": session, "served": served}
        save_index(idx)
    log_run(dict(base, event="end", rc=rc, minutes=round((time.time() - t0) / 60, 1), report_ok=ok,
                 verdict=first, session=session, served=served, out=out))
    return 0 if ok else 1


def main(argv):
    if not argv or argv[0] in ("-h", "--help"):
        print(__doc__)
        return 0
    if argv[0] == "run":
        return run(argv[1])
    if argv[0] in ("roster", "next"):
        n = int(argv[1]) if len(argv) > 1 else (40 if argv[0] == "roster" else 3)
        rows = roster()
        if argv[0] == "next":
            for must, should, words, st, fp in [r for r in rows if r[3] in ("none", "stale")][:n]:
                print(fp)
            return 0
        for must, should, words, st, fp in rows[:n]:
            print("%-8s MUST %3d  should %3d  words %6d  %s" % (st, must, should, words, fp))
        print("%d papers: %d audited fresh, %d running" % (
            len(rows), sum(1 for r in rows if r[3] == "fresh"), sum(1 for r in rows if r[3] == "running")))
        return 0
    if argv[0] == "status":
        for r in in_flight():
            print("running since %s  %s  (account %s)" % (r["at"], r["tex"], r.get("account")))
        for r in [x for x in runs() if x.get("event") in ("end", "refused")][-10:]:
            print("%s %-7s %s  %s" % (r["at"], r["event"], r["tex"],
                                      r.get("verdict") or r.get("why") or ("rc %s, no report" % r.get("rc"))))
        return 0
    print(__doc__)
    return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
