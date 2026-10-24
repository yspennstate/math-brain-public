# Agent tools

These are the scripts agents call while they work. Each one reads a store built from `export/population/` with `tools/import_store.py`.

Set two variables first:

- `MATHBRAIN_STORE`: the path to the SQLite store;
- `MATHBRAIN_BUILD_SRC`: the path to this repository's `src/`.

The tools have no defaults that work outside the machine they were written on.

| Script | What it does |
|---|---|
| `math_recall.py` | Searches the store and returns the best current cards whole, with their ids and their linked ids. `--id CARD` prints a card and its links. `--or WORDS` adds a second wording. `--list` prints titles only. |
| `math_walk.py` | Gives a compact map of what lies around a card. `--toward WORDS` ranks the cards within two links by what you are looking for. |
| `math_strength.py` | Reports link strengths that grow from use. Two cards used together in one session within 30 minutes strengthen their link, and strengths fade by a power law. `--card`, `--top` and `--explain` are available. |
| `math_note.py` | Prints one complete current note. |
| `math_sense.py` | The hook. It runs on every prompt, decides whether the prompt is mathematical, and serves at most a few cards, each with a line saying how far to trust it. |
| `math_subagent_adapter.py`, `math_subagent_receipt.py` | Give a subagent the same recall and record what it was served. |
| `fastrecall.py` | Prepares, once per state of the store, the parsing and term tables a recall needs, so a call takes under two seconds instead of five or six. `MATH_RECALL_FAST=0` turns it off. |
| `query_embed.py`, `math_prefilter.py`, `property_order.py`, `brain_switch.py` | Helpers imported by the scripts above. |

`MATH_BRAIN_HOW_IT_WORKS.md` explains the ranking, the link types and the strengths in more detail.

## What the tools write, and the encoder

The tools write under your home directory. Recall and the link walk append one line per call to `~/.claude/brain_graph/live/math_couse.jsonl` (card ids, a session id and the time, never the words of a query), and `math_strength.py` folds that log into link strengths. The recall cache lives in `~/.claude/dreaming/cache/math_recall`; `MATH_RECALL_CACHE_DIR` moves it.

The meaning channel of recall embeds the query with BAAI/bge-small-en-v1.5, run through onnxruntime. The weights are not in this repository. Export the model to ONNX and put `model.onnx` and `tokenizer.json` in `agent_tools/models/bge-small-en-v1.5/`. Without them recall runs on words and links alone and says nothing about it.

## Wiring the hook

In Claude Code, `math_sense.py` runs as a `UserPromptSubmit` hook. In Codex it is listed in `hooks.json`. Codex accepts hook output only as JSON (`hookSpecificOutput.additionalContext`), and the script writes that form when it runs there.
