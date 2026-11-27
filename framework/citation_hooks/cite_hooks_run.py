# -*- coding: utf-8 -*-
"""Runs the citation hooks C01..C62 on one hook payload (an agent, 11 Nov 2026; the credit hooks C17..C26,
14 Nov 2026).

Wired in hook_dispatch_list.json on UserPromptSubmit and PreToolUse (Bash, PowerShell, Write, Edit, MultiEdit and the
browser tools). Reads the payload from stdin and prints what fires. Warns, never blocks.

    python cite_hooks_run.py --list       every hook: id, channels, title
    python cite_hooks_run.py --selftest   fire and quiet controls plus the cool-down; no state written
"""
import json
import os
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
if HERE not in sys.path:
    sys.path.insert(0, HERE)
import cite_hook_core as C  # noqa: E402


def _pre(cmd, tool="Bash", cwd=None, **extra):
    ti = {"command": cmd}
    ti.update(extra)
    p = {"hook_event_name": "PreToolUse", "tool_name": tool, "tool_input": ti, "session_id": "selftest"}
    if cwd:
        p["cwd"] = cwd
    return p


def _tool(tool, ti):
    return {"hook_event_name": "PreToolUse", "tool_name": tool, "tool_input": ti, "session_id": "selftest"}


def _prompt(t):
    return {"hook_event_name": "UserPromptSubmit", "prompt": t, "session_id": "selftest"}


def selftest():
    tmp = tempfile.mkdtemp(prefix="cite_selftest_")
    paper = os.path.join(tmp, "p0072-ants").replace("\\", "/")
    plain = os.path.join(tmp, "notes").replace("\\", "/")
    os.makedirs(paper)
    os.makedirs(plain)
    with open(os.path.join(paper, "main.tex"), "w", encoding="utf-8") as f:
        f.write("\\documentclass{amsart}\n\\begin{document}\\end{document}\n")
    with open(os.path.join(plain, "README.md"), "w", encoding="utf-8") as f:
        f.write("notes\n")
    fire = [
        ("C01", _pre("cd " + paper + " && git push origin main")),
        ("C03", _pre("git push origin main", cwd=paper)),
        ("C16", _pre("cd ~/open-problems-repo && git add papers/p0072.tex && git push")),
        ("C01", _pre("gh release create v1 paper.pdf -R yspennstate/p0245-cover-time")),
        ("C14", _pre("curl -X POST https://zenodo.org/api/deposit/depositions -H 'Authorization: Bearer $Z'")),
        ("C14", _pre("python ~/papers/zenodo_upload.py --all")),
        ("C14", _tool("mcp__claude-in-chrome__navigate", {"url": "https://zenodo.org/uploads/new", "tabId": 3})),
        ("C15", _tool("mcp__claude-in-chrome__navigate", {"url": "https://www.researchgate.net/upload", "tabId": 3})),
        ("C05", _tool("mcp__claude-in-chrome__computer", {"action": "left_click", "text": "researchgate.net Publish"})),
        ("C08", _tool("Write", {"file_path": "C:/p/refs.bib", "content": "@article{a, title={x}}"})),
        ("C07", _tool("Edit", {"file_path": "C:/p/main.tex", "old_string": "a", "new_string": "as in \\cite{kms}"})),
        ("C01", _prompt("upload the two new preprints to zendo before the weekend")),
        ("C02", _prompt("publish the p0245 paper on github and researchgate")),
        ("C10", _prompt("post the new paper to zenodo")),
        # credit the mathematicians in development, writing and acknowledgment
        ("C17", _pre("python ~/.claude/dreaming/problem_recall.py P0072")),
        ("C19", _tool("Edit", {"file_path": "C:/p/main.tex", "old_string": "a",
                               "new_string": "\\begin{lemma}\\label{l1} x \\end{lemma}"})),
        ("C20", _tool("Write", {"file_path": "C:/p/main.tex", "content": "\\section{Introduction} The problem"})),
        ("C22", _tool("Edit", {"file_path": "C:/p/main.tex", "old_string": "a", "new_string": "\\begin{abstract} We"})),
        ("C24", _tool("Edit", {"file_path": "C:/p/main.tex", "old_string": "a",
                               "new_string": "\\section*{AI declaration} The proofs were drafted by"})),
        ("C25", _tool("Edit", {"file_path": "C:/p/main.tex", "old_string": "a",
                               "new_string": "\\section*{Acknowledgments} We thank"})),
        ("C26", _pre("cd " + paper + " && git push origin main")),
        ("C01", _pre("cd " + plain + " && cat > README.md <<'EOF'\nnotes\nEOF\ngit add main.tex README.md && git push")),
    ]
    quiet = [
        ("*", _pre("cd " + plain + " && git push origin main")),
        ("*", _pre("git push origin main", cwd=plain)),
        ("*", _pre("cat ~/papers/zenodo_upload.py")),
        ("*", _pre("grep -n zenodo ~/notes.md")),
        ("*", _pre("python ~/.claude/dreaming/brain.py remember zenodo_paper_x --desc 'posted the paper to zenodo'")),
        ("*", _pre("python ~/.claude/dreaming/citation_hooks/cite_hooks_run.py --selftest")),
        ("*", _tool("Write", {"file_path": "~/.claude/dreaming/citation_hooks/C99_x.py",
                              "content": "\\cite{x} zenodo researchgate"})),
        ("*", _tool("Write", {"file_path": "C:/p/main.tex", "content": "\\section{Intro} no references here"})),
        ("*", _tool("mcp__claude-in-chrome__navigate", {"url": "https://www.kaggle.com/competitions", "tabId": 3})),
        ("*", _prompt("keep working on the trading simulations")),
        ("*", _prompt("fire this every 3 minutes for the next week. ... water the plants, publish papers, read a good book")),
        ("*", _prompt("agents are working on improving the notes ... remove bugs, solve a puzzle, publish papers, enter "
                      "a contest, tidy the garden plan, and so on. record some videos")),
        ("*", _prompt("Stop hook feedback: post the paper to zenodo")),
        # a heredoc writing "papers" into a board row is not a paper being pushed
        ("*", _pre("cd " + plain + " && cat > s.py <<'EOF'\nrow = 'final papers 15 Jan'\nEOF\npython s.py && git push origin main")),
        ("C14", _pre("cd " + paper + " && git push origin main")),
        ("C15", _tool("mcp__claude-in-chrome__navigate", {"url": "https://zenodo.org/uploads/new", "tabId": 3})),
        ("C16", _tool("mcp__claude-in-chrome__navigate", {"url": "https://www.researchgate.net/upload", "tabId": 3})),
        ("C03", _tool("Write", {"file_path": "C:/p/refs.bib", "content": "@article{a, title={x}}"})),
        ("*", _tool("Write", {"file_path": "C:/p/notes.md", "content": "## Introduction \\begin{lemma} acknowledgments"})),
        ("C24", _tool("Edit", {"file_path": "C:/p/main.tex", "old_string": "a", "new_string": "\\section{Introduction} x"})),
        ("C17", _tool("Write", {"file_path": "C:/p/main.tex", "content": "\\section*{Acknowledgments} We thank"})),
        ("*", _pre("python ~/.claude/dreaming/math_recall.py 'spanning tree'")),
        ("*", _pre("cat > x.py <<'EOF'\nimport problem_recall\nEOF\necho problem_recall.py && grep problem_recall.py notes.md")),
        ("*", _pre("echo hi")),
        ("*", _prompt("hello")),
    ]
    hooks = C.load_hooks()
    ok = 10 <= len(hooks) <= 70
    print("loaded %d hooks %s" % (len(hooks), "ok" if ok else "WANT 10-70"))
    keep, C.BUDGET = C.BUDGET, 10 ** 9  # which hooks match, not how many fit
    for want, p in fire:
        got, ch, _ = C.decide(p, hooks, now=1000.0, state={})
        ids = [h["id"] for h in got]
        good = want in ids
        ok &= good
        print("FIRE  %s %s ch=%s got=%s  %s" % (want, "ok  " if good else "MISS", ",".join(sorted(ch)), ",".join(ids),
                                                json.dumps(p)[:70]))
    for notwant, p in quiet:
        got, ch, _ = C.decide(p, hooks, now=1000.0, state={})
        ids = [h["id"] for h in got]
        good = (not ids) if notwant == "*" else (notwant not in ids)
        ok &= good
        print("QUIET %s %s ch=%s got=%s  %s" % (notwant, "ok  " if good else "LOUD", ",".join(sorted(ch)), ",".join(ids),
                                                json.dumps(p)[:70]))
    C.BUDGET = keep
    st = {}
    batches = []
    for k in range(8):  # since 19 Nov a firing holds ~3.5k chars; the rest come at the next publish steps
        got, _, _ = C.decide(_pre("cd " + paper + " && git push"), hooks, now=1000.0 + 60 * k, state=st)
        if not got:
            break
        batches.append([h["id"] for h in got])
    flat = [x for b in batches for x in b]
    back, _, _ = C.decide(_pre("cd " + paper + " && git push"), hooks, now=1000.0 + 60 * len(batches) + 1900, state=st)
    cool = (2 <= len(batches) <= 6 and len(flat) == len(set(flat)) and len(flat) >= 10 and len(back) >= 5)
    print("COOLDOWN (overflow rotates over the next pushes, then silent, back after 30 min) %s  batches=%s back=%d"
          % ("ok" if cool else "FAIL", [len(b) for b in batches], len(back)))
    ok &= cool
    print("ALL PASS" if ok else "FAILED")
    return 0 if ok else 1


def main():
    if "--selftest" in sys.argv:
        sys.exit(selftest())
    if "--list" in sys.argv:
        for h in C.load_hooks():
            print("%s %-8s %-42s %s" % (h["id"], "MASSIVE" if h.get("massive") else "", ",".join(h["on"]), h["title"]))
        return
    raw = sys.stdin.read()
    out = C.run_payload(raw)
    if out:
        print(out)


if __name__ == "__main__":
    main()
