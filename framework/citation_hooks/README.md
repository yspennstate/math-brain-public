# Citation and credit hooks

Sixty-two short checks that run while an agent develops, writes and posts a mathematics paper. Each one
looks at a single hook event (a prompt, a shell command about to run, a file just written) and, when the
event belongs to its phase, prints a reminder of one rule. None of them blocks anything. They exist
because the failures they describe kept happening in practice: a reference that did not exist, a partial
result by someone else that went uncited, an introduction that left a reader unsure which statements were
known and which were new.

C01-C16 cover citation itself: checking each reference against its source, searching beyond the first
hits, citing where the problem was posed and every earlier partial result, sources for borrowed lemmas,
software and data, and making the posted records (the repository, Zenodo, ResearchGate) carry the same
bibliography as the PDF.

C17-C26 cover credit. The people whose work carries a result should be named and their contribution
stated plainly, in three places that must agree:

- the introduction, near its start, names the mathematicians whose work the paper rests on, with
  citations, and says what existed before, what is new, and how each new idea relates to an old one;
- the AI declaration names the same people and says that those results are theirs;
- the abstract claims no more novelty than the introduction does.

The credit work starts when the attack on a problem starts, not when the paper is written: C17 asks for a
`CREDITS.md` in the paper's folder recording who posed the problem, whose results are used, the citation
key for each and how it is used, with every statement marked known, adapted or new (C19). Attribution in
the body stays one neutral clause in the present tense ("The operator W was introduced by A [4], who
determined its two fixed points"); C13 checks that the paper never narrates its own history.

C27-C62 read the paper's source itself. When a tool call names a `.tex` file (or a `main.tex` sits in the
working folder), they look for the things a referee or an expert in the area would object to: a result
called classical with no citation, a novelty claim made before a forward-literature search, a displayed
theorem that is not new but carries no source, an introduction without a paragraph on what was known, an
AI declaration that does not name the people the results rest on, a construction from the literature
that is not named after its author, an in-preparation or personal-communication entry with no year or
no place it is cited. C55-C57 are a final reread before posting, and C58-C62 keep the public copies (the
GitHub README, Zenodo, ResearchGate) in line with the corrected PDF, holding a new posting until every
point an expert has raised is answered in it. `cite_tex_scan.py` and `cite_tex_scan2.py` hold the shared
text helpers.

## Running them

    python cite_hooks_run.py --list       every hook with its channels and title
    python cite_hooks_run.py --selftest   fire and quiet controls and the cool-down; writes no state

`cite_hooks_run.py` reads one hook payload on standard input, the way Claude Code and Codex deliver
them, runs the hooks whose phase matches, and applies a cool-down so a rule is not repeated on every
command. To wire it, add it as a `UserPromptSubmit`, `PreToolUse` and `PostToolUse` command in the
agent's hook settings. It prints plain text, which Claude Code passes to the model; Codex reads only a
JSON `hookSpecificOutput` object, so a Codex install needs a small wrapper.

`../paper_writing_hooks/` holds the companion rule set for the writing itself (one name per object,
notation tables, no workshop vocabulary in a paper, the funding paragraph) with its own selftest:
`python pw1k_selftest.py`.
