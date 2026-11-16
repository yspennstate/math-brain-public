# Checking an install

This folder tells you whether your copy of the math brain works the way ours does. It holds about 1,100 reference
cases and about 200 annotated logs, all made by running the public tools on the public store in a fresh clone of
this repository. Nothing in them comes from a private machine.

## Run the check

From the root of a checkout that has `src`, `tools`, `agent_tools`, `export`, `config`, `navigation` and
`conformance`:

```bash
git sparse-checkout add conformance          # if you cloned sparse, as the main README suggests
python tools/import_store.py --out local/population/brain.sqlite3
python conformance/verify_install.py         # 50 cases
python conformance/verify_install.py --all   # every case
```

Use Python 3.11 or newer (`python3` on macOS and Linux if that is the name of your 3.11). It runs the same on
Windows, macOS and Linux and uses the standard library only. It switches the tools' usage logs off; the one thing
it writes in your home directory is the hook's own note for each silent test prompt, in
`~/.claude/dreaming/mathbrain_silence_harness.tsv` (the folder is created if it is missing). The quick check runs
eight cases of each kind; its eight hook cases are four that should serve and four that should stay silent.

The first search on a new install builds the prepared fast-recall state. On a busy Windows laptop that took ten
minutes once; afterwards a search took one to twenty seconds and a walk a fraction of a second. On a quiet machine
the first search takes about a minute.

The last line says PASS or FAIL. PASS needs 95 percent of the cases. To have Claude Code or Codex check the whole
setup, including whether the prompt hook is wired into it and reaches it, paste the prompt in
[AGENT_CHECK.md](AGENT_CHECK.md); that page also has the hook entry for both runtimes.

## What is checked

| kind | how many | the call | passes when |
|---|---|---|---|
| search | 600 | `math_recall.py "<words of a card's title>"` | the reference's top card is in your top 3, and 3 of its top 5 are in your top 5 |
| fragment | 200 | `math_recall.py "<eight words from the middle of a card>"` | the same |
| negative | 50 | an everyday question the store cannot answer | WEAK MATCH printed exactly when the reference printed it |
| walk | 150 | `math_recall.py --id <card>` | same card, same link targets |
| hook | 100 | one `UserPromptSubmit` event into `math_sense.py` on stdin | served as the reference was with valid hook JSON and half its cards shared, or silent for the same reason the reference gave (a hook that crashes or is missing is silent with no reason, and fails) |
| nav | 40 | `navigation/nav_query.py "<question>"` | same first three card ids |

The STRICT count in the report is exact equality (same ids in the same order, same printed text). On the same
export and the same Python the reference runs twice gave byte-identical output, so strict differences point to a
different environment: another Python version, or the optional meaning channel (a sentence encoder) present on one
side and missing on the other.

Each case records what the reference printed, the seconds it took, and the export it ran against (the hash of
`export/population/MANIFEST.json`). When the export changes, regenerate the cases with `make_cases.py`; the
cases in this folder belong to the export they name.

## The logs

`logs/` holds about 200 transcripts, one call each, printed exactly as an agent sees them, with a header naming the
command, its time, and what to look for. `logs/INDEX.jsonl` lists them. They show the parts of the brain talking to
each other:

- a search, with the words that matched each card and the `--id` call that reads it whole;
- two wordings in one call, fused by rank (`found by wording 1 (rank 2), 2 (rank 1)`);
- a walk along a card's links, with each link's kind and stated reason;
- spreading activation through links (`--depth 2`), with the path that brought each card in;
- the WEAK MATCH hint on a question the store cannot answer;
- the prompt hook serving a block (the raw JSON, then the block as the agent reads it) or staying silent, with
  the reason the hook wrote for itself;
- the repository's own navigation brain answering "where is X".

If your agent's output differs from a log in form (no ids, no `matched` lines, no JSON from the hook), your agent
is not calling the tool you think it is.

## When it fails

- **Everything fails, search and walk alike.** The store did not import, or you imported a different export. Run
  `python tools/import_store.py --out local/population/brain.sqlite3` again and read its last lines: both digest
  counts must be 0.
- **Walk passes, search fails.** The store is right and the ranking differs. Check the Python version and whether
  `src/` is the one from this checkout (`MATHBRAIN_BUILD_SRC` overrides it). A few search failures with strict
  differences are normal across machines; many are not.
- **Hook cases fail with shape errors.** The hook printed something other than one JSON object, usually a Python
  warning or a traceback on stdout. Run one by hand:
  `echo '{"hook_event_name":"UserPromptSubmit","session_id":"t1","prompt":"spectral gap of a reversible Markov chain"}' | python agent_tools/math_sense.py`
- **The hook is silent in real sessions but the hook cases pass.** The check gives the hook ten minutes per prompt;
  a live session gives it 30 seconds to search and 60 seconds in all. On a loaded Windows laptop the reference hook
  took 72 to 87 seconds per prompt and, at the live settings, served nothing (its note says
  `budget_exhausted_before_ranking`). The report counts the hook cases slower than 30 seconds; if most are, raise
  `MATHBRAIN_TIME_BUDGET_S` and the hook entry's `timeout` together, or call `math_recall.py` yourself.
- **The hook is silent and its note says `integrity:read_failed_or_inconsistent`.** Your checkout predates commit
  0fe060548. Before it, the hook re-read each chosen card together with an artifact file under
  `local/population/objects/`, a folder the public export does not ship, so it failed on nine cards in ten and served
  nothing on any fresh install. Pull, and the hook cases pass.
- **Hook cases fail as silent where the reference served.** The hook cannot find the store or `src/`. It looks for
  `local/population/brain.sqlite3` beside `agent_tools/`; set `MATHBRAIN_STORE` if yours is elsewhere. The silence
  reason is written to `~/.claude/dreaming/mathbrain_silence_harness.tsv` for test session ids.
- **nav fails.** `navigation/` is missing from a sparse checkout.
- **Python too old.** macOS ships 3.9 as `/usr/bin/python3`; install 3.11 or newer.

## One finding the cases record

Four of the fifty everyday questions do not print WEAK MATCH on the reference (football standings, repotting an
orchid, renewing a passport, knitting a scarf): a word in each matches some card well enough to pass the threshold.
The hint is a hint; an agent still has to read the cards.

## Making the cases again

```bash
python conformance/make_cases.py      # writes cases/*.jsonl from the export in this checkout
python conformance/make_logs.py       # writes logs/ from those cases
```
