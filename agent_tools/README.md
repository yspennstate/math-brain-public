# Agent tools

These are the scripts agents call while they work. Each one reads a store built from `export/population/` with `tools/import_store.py`.

## Start here: the default recall workflow

**Use this workflow whenever an agent needs information from the store. It is the standard operating procedure, not a list of optional search tips.** A known card ID can go straight to whole-card reading; otherwise begin with a multi-wording search.

1. **Search deliberately with two or three alternative wordings in one call.** Name the object, theorem or method, symbol, or author that the answering card would use. These are alternative phrasings, not a three-word limit. The agent supplies them; the tool does not generate them.
2. **Read the relevant cards whole by ID, then follow useful linked IDs.** Check the statement, hypotheses, source and verification status before relying on a result. Do not answer from a title or snippet alone.
3. **Reword weak matches; stop when the evidence answers the question.** A hook note is a lead, not a verdict. After three unsuccessful rounds, report that the search did not find an answer; this does not prove the store contains none. Use authorized source-file search when appropriate, especially for numeric tables.
4. **Keep fast recall enabled and automatic spreading at depth 0 by default.** Multi-wording search improves query coverage; the prepared fast-recall state speeds up those same searches. Read linked cards deliberately rather than enabling deeper spreading without evidence. For newly added cards, refresh the prepared state or use the freshness controls in [the tool guide](#fast-recall).
5. **Copy the full card ID when citing a result.** Read it from the whole-card output, preserve its source and status, and distinguish stored evidence from your own inference.

After the setup below, make one search call such as:

```bash
python agent_tools/math_recall.py "random transposition walk spectral gap" --or "Diaconis Shahshahani cutoff" --or "mixing time random transpositions"
```

Through MCP, send the same alternatives in the `wordings` array (up to three), then use `ids` to read the relevant cards.

**Evidence, not a universal guarantee:** on the reported 100-question held-out comparison, multiple wordings scored 86 versus 76 for one wording per call. Whole cards with IDs scored 83 versus 34 for titles and snippets. Reading cards and walking links preserved similar accuracy (82 versus 83) with about half the uncached input. These are separate comparisons, not additive gains. See [the agent guide](../AGENTS_GUIDE.md#3-what-to-tell-the-agent) and [tests](../TESTS.md).

Set two variables first:

- `MATHBRAIN_STORE`: the path to the SQLite store;
- `MATHBRAIN_BUILD_SRC`: the path to this repository's `src/`.

`math_recall.py`, `math_walk.py`, `math_sense.py` and `frontier_digest.py` fall back to `src/` and `local/population/brain.sqlite3` in this checkout when the variables are unset, so after the import in the top-level README they run from the repository root as they are. The other tools need both variables.

## Fast recall

`fastrecall.py` is on by default; nothing has to be installed or run to use it. The first search against a store builds a prepared state (the parsed cards, the term tables and the link maps, about 70 MB for this store) in the recall cache, and every later search loads it instead of reading the store again. On a fresh clone of this repository, on a busy laptop, the first search took 27 seconds, each later one 5 to 6 seconds with two wordings, and the same search with `MATH_RECALL_FAST=0` took 25 seconds every time. The results are the same either way.

- The state is keyed to the store, the recall code and the dials, so a changed store or a new version of `math_recall.py` builds a new one on its next search.
- A search may answer from a state up to 45 minutes behind the store while the new one is built, so that a store being written to does not rebuild on every call. Cards added in that window are not found until the rebuild. After you re-import or add cards and want them found at once, set `MATH_RECALL_FAST_STALE_S=0` for the next call, or run `python agent_tools/math_recall_prebuild.py`, which builds the state ahead of time with the same paths and environment a search would use, so the next search finds it ready (a scheduled run every few minutes keeps the first search after a change fast; a run against an unchanged store stops at once). It writes its lock and log under `agent_tools/cache/math_recall/`; `--status` prints them. The copy under `framework/dreaming/` belongs to the general framework and warms that folder's own `math_recall.py`, not this one.
- `MATH_RECALL_CACHE_DIR` moves the cache. Old states are not removed automatically; delete the directory's older `recall_*.m` files when the store has moved on.

## How to search

Follow this default workflow on every store lookup; [AGENTS_GUIDE.md](../AGENTS_GUIDE.md) gives the numbers.

```
python agent_tools/math_recall.py "random transposition walk spectral gap" --or "Diaconis Shahshahani cutoff"
python agent_tools/math_recall.py --id claim_03ca421f claim_7e623698
```

- Give two or three wordings in one call, each after its own `--or`, worded the way a card would say it: the object, the theorem or method by name, a symbol, an author.
- Then read the cards it printed with `--id` and follow their links, rather than searching again.
- Stop when a card answers. A `WEAK MATCH` line means reword. After three unsuccessful rounds, report that the search did not find an answer, not that the store necessarily contains none.
- Leave `--depth` at 0.
- Search output shortens ids to a unique prefix. When an id goes into an answer or a record, copy the full id from the `--id` card.

| Script | What it does |
|---|---|
| `math_recall.py` | Searches the store and returns the best current cards whole, with their ids and their linked ids. `--id CARD` prints a card and its links. `--or WORDS` adds a second wording. `--list` prints titles only. |
| `math_walk.py` | Gives a compact map of what lies around a card. `--toward WORDS` ranks the cards within two links by what you are looking for. |
| `math_strength.py` | Reports link strengths that grow from use. Two cards used together in one session within 30 minutes strengthen their link, and strengths fade by a power law. `--card`, `--top` and `--explain` are available. |
| `math_note.py` | Prints one complete current note. |
| `frontier_digest.py` | The frontier of one research program: the store's results on it, newest first, each tagged literature or unrefereed house result, then what was withdrawn and the failed routes. `--digest PROGRAM [--at TIME]`, `--delta PROGRAM --since TIME`. |
| `math_sense.py` | The hook. It runs on every prompt, decides whether the prompt is mathematical, and serves at most a few cards, each with a line saying how far to trust it. |
| `math_subagent_adapter.py`, `math_subagent_receipt.py` | Give a subagent the same recall and record what it was served. |
| `mcp_math_recall.py` | Serves `math_recall.py` to an agent as an MCP tool over stdio, so the agent needs no shell. This is how the brain arm of the three-arm test was connected. |
| `fastrecall.py` | Prepares, once per state of the store, the parsing and term tables a recall needs, so a call takes under two seconds instead of five or six. `MATH_RECALL_FAST=0` turns it off. |
| `query_embed.py`, `math_prefilter.py`, `property_order.py`, `brain_switch.py` | Helpers imported by the scripts above. |

`MATH_BRAIN_HOW_IT_WORKS.md` explains the ranking, the link types and the strengths in more detail.

## What the tools write, and the encoder

The tools write under your home directory. Recall and the link walk append one line per call to `~/.claude/brain_graph/live/math_couse.jsonl` (card ids, a session id and the time, never the words of a query), and `math_strength.py` folds that log into link strengths. The recall cache lives in `~/.claude/dreaming/cache/math_recall`; `MATH_RECALL_CACHE_DIR` moves it.

The meaning channel of recall embeds the query with BAAI/bge-small-en-v1.5, run through onnxruntime. The weights are not in this repository. Export the model to ONNX and put `model.onnx` and `tokenizer.json` in `agent_tools/models/bge-small-en-v1.5/`. Without them recall runs on words and links alone and says nothing about it.

## Wiring the hook

In Claude Code, `math_sense.py` runs as a `UserPromptSubmit` hook. In Codex it is listed in `hooks.json`. Codex accepts hook output only as JSON (`hookSpecificOutput.additionalContext`), and the script writes that form when it runs there.
