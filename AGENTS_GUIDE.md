# Giving an agent the store

This note says how to connect a coding agent (Claude Code, Codex, or any client that speaks MCP) to the store in this repository, what to tell it, and how it should search. The default workflow below is the operating procedure for agents using this store; its evidence and limits are stated alongside it. The tests themselves are in [TESTS.md](TESTS.md).

The short version: an agent with the store answers questions about past work faster and with less reading than an agent that has to search the same records as files, and its misses are mostly timeouts or abstentions rather than wrong answers. On 988 lookup and audit items with 600 seconds an item, Claude agents with the store answered 95.4 percent, agents with read access to the same repositories 82.0 percent, and the model alone 18.9 percent. Where both of the first two finished in time they were tied (99.3 against 99.4 percent on 806 items). The store's lead is speed: the agents with it took 120 seconds an item on average against 211, and timed out on 3.7 percent of items against 17.5. Codex agents, given 900 seconds an item, went the other way: the repository arm scored 97.0 percent of 394 items, the store arm 94.7 and the model alone 21.6; the gap between the first two is one the test does not settle. The store arm's misses there were mostly abstentions, on items that need several records found at once (section 4).

## Start here: the default recall workflow

**Use this workflow whenever an agent needs information from the store. It is the standard operating procedure, not a list of optional search tips.** A known card ID can go straight to whole-card reading; otherwise begin with a multi-wording search.

1. **Search deliberately with two or three alternative wordings in one call.** Name the object, theorem or method, symbol, or author that the answering card would use. These are alternative phrasings, not a three-word limit. The agent supplies them; the tool does not generate them.
2. **Read the relevant cards whole by ID, then follow useful linked IDs.** Check the statement, hypotheses, source and verification status before relying on a result. Do not answer from a title or snippet alone.
3. **Reword weak matches; stop when the evidence answers the question.** A hook note is a lead, not a verdict. After three unsuccessful rounds, report that the search did not find an answer; this does not prove the store contains none. Use authorized source-file search when appropriate, especially for numeric tables.
4. **Keep fast recall enabled and automatic spreading at depth 0 by default.** Multi-wording search improves query coverage; the prepared fast-recall state speeds up those same searches. Read linked cards deliberately rather than enabling deeper spreading without evidence. For newly added cards, refresh the prepared state or use the freshness controls in [the tool guide](agent_tools/README.md#fast-recall).
5. **Copy the full card ID when citing a result.** Read it from the whole-card output, preserve its source and status, and distinguish stored evidence from your own inference.

After the setup below, make one search call such as:

```bash
python agent_tools/math_recall.py "random transposition walk spectral gap" --or "Diaconis Shahshahani cutoff" --or "mixing time random transpositions"
```

Through MCP, send the same alternatives in the `wordings` array (up to three), then use `ids` to read the relevant cards.

**Evidence, not a universal guarantee:** on the reported 100-question held-out comparison, multiple wordings scored 86 versus 76 for one wording per call. Whole cards with IDs scored 83 versus 34 for titles and snippets. Reading cards and walking links preserved similar accuracy (82 versus 83) with about half the uncached input. These are separate comparisons, not additive gains. See [the agent guide](AGENTS_GUIDE.md#3-what-to-tell-the-agent) and [tests](TESTS.md).

## 1. Build the store

```
pip install -e .
python tools/import_store.py --out local/population/brain.sqlite3
export MATHBRAIN_STORE=$PWD/local/population/brain.sqlite3 MATHBRAIN_BUILD_SRC=$PWD/src
python agent_tools/math_recall.py spectral gap of the random transposition walk
```

If the last line prints cards with ids, the store works. The meaning channel needs an ONNX export of the encoder (see [agent_tools/README.md](agent_tools/README.md)); without it recall runs on words and links and is still usable.

## 2. Connect the agent

There are two ways, and either is enough.

**As a shell command.** An agent that has a shell can call `agent_tools/math_recall.py` directly. Put the commands in its instructions (section 3).

**As an MCP tool.** `agent_tools/mcp_math_recall.py` serves the same search as a tool named `math_recall`, with two inputs: `wordings` (one to three) and `ids`. The agent then needs no shell at all. This is how the brain arm of the three-arm test was connected, for both Claude and Codex.

For Claude Code, a `.mcp.json` in the project (or the same object passed with `--mcp-config`):

```json
{"mcpServers": {"mathbrain": {
  "command": "python",
  "args": ["-X", "utf8", "/path/to/repo/agent_tools/mcp_math_recall.py"],
  "env": {"MATHBRAIN_STORE": "/path/to/repo/local/population/brain.sqlite3",
          "MATHBRAIN_BUILD_SRC": "/path/to/repo/src"}}}}
```

The tool then appears to the agent as `mcp__mathbrain__math_recall`; allow it with `--allowedTools mcp__mathbrain__math_recall`.

For Codex, in `~/.codex/config.toml`:

```toml
[mcp_servers.mathbrain]
command = "python"
args = ["-X", "utf8", "/path/to/repo/agent_tools/mcp_math_recall.py"]
env = { MATHBRAIN_STORE = "/path/to/repo/local/population/brain.sqlite3", MATHBRAIN_BUILD_SRC = "/path/to/repo/src" }
```

`agent_tools/math_sense.py` is a prompt hook that serves a few cards when a prompt reads as mathematics. It is optional. In an earlier test it stayed silent on 85 of 100 recall questions, so it is a source of leads, not the way to search; the agent should still call recall. How much it carries depends on how many words a question shares with a card. In the three-arm test, whose questions name records in the store's own terms, Codex agents with the store answered 161 of 394 items without calling recall, 156 of them correctly, and on 158 of those 161 the hook had served notes.

## 3. What to tell the agent

The brain arm of the test gave every agent this note, word for word apart from the last sentence:

> You are connected to the math brain: the store of mathematical results, proofs, open problems, attempts and notes. Search it with the math_recall tool - give two or three wordings in one call (the object, the theorem or problem by name, the author), then pass card ids to read cards whole. Stop when a card answers; a WEAK MATCH line means reword. Notes from the brain may also appear with the question. A note is a hint, not a verdict: it can point right or wrong, so weigh it against the question in front of you.

Each clause is there for a reason measured on held-out recall questions (100 a configuration, Codex agents, 10 to 15 October 2026):

| Choice | Result |
|---|---|
| print whole cards with their ids, not titles and snippets | 83 of 100 against 34 |
| two or three wordings in one call, not one wording a call | 86 against 76 |
| word the search as the card would (the object, a theorem or method by name, a symbol, an author), not as the question is phrased | the main lever behind the row above |
| after the first search, read cards by id and follow their links instead of searching again | 82 against 83, at about half the uncached tokens |
| treat a WEAK MATCH line as a signal to reword | with that line showing, the answering card had been printed for 4 of 21 questions; without it, for 49 of 79 |
| leave spreading through the links (`--depth`) at 0 | 79 against 80, with 46 percent more tokens |

Apply these two instructions as part of the default workflow. First, after three rounds of wordings with nothing useful, the agent must say that its search did not find the answer rather than invent one; an unsuccessful search is not proof of absence. In the three-arm test this is what the agents with the store did: of the 19 items a Codex agent with the store lost to the repository arm, 16 were abstentions and 3 timeouts, and none a wrong value. Second, when the agent quotes a card's id in its answer, it should copy the full id from the card printed by `--id`, since search output shortens ids to a prefix.

## 4. Where search falls short

Recall ranks cards by the words they share with the query, by meaning, and by links. It does poorly on records made mostly of digits and punctuation, such as a table of walk counts, where words give it little to match. In the Codex runs the repository arm won nineteen items the store arm lost: ten asked for arithmetic on the page numbers of several ledger entries, seven for spreads or growth differences of walk counts and two for the odd source out. All nineteen need several records found at once; in sixteen the agent with the store gave up rather than answer, and in three it ran out of time. If an agent is likely to need such records, give it read access to `export/population/` as well, so it can fall back on a text search. We have not tested this combined setup.

The seventeen questions the store arm had lost by 28 October were asked again in three reruns, and it answered fifteen of them correctly in at least one. Most of its first misses came while the recall tool was rebuilding its prepared state, and once the harness checked that recall answered before each question, six of the eleven items that had timed out came back, all correct. So before a timed task, check that recall answers a probe query, and if it is slow, wait for it rather than give up.

The store also adds nothing to a task the model can do on its own. On proof audits, where the answer is stored nowhere, all three arms scored between 92 and 99 percent.

## 5. What it costs

Per Claude Sonnet session in the three-arm test, at list price: 0.053 USD with the store, 0.092 USD with the repositories, and 0.010 USD for the model alone. Counted per correct answer on a shard run with both time limits, the store cost 0.074 USD and the repositories 0.153. The agents with the store read about a quarter as many input tokens as those searching the repositories and wrote about two fifths as many output tokens. Most of an agent's input tokens are re-reads of the session on every turn, so fewer and better calls save more than shorter answers. [docs/cost.md](docs/cost.md) has the other cost measurements, including where a connected question's tokens go when the brain arrives as standing instructions and hooks rather than as a tool.

## 6. Writing back

The store grows from packets: a result, an attempt or a mistake written as a card with its links and its provenance, then checked and imported. The packets, cards, links and mistakes in `export/population/` show what an accepted contribution looks like, and the `PACKET_DELTA.json` files under `results/fei/` are packets as agents wrote them during a campaign. An agent that writes one should state how sure it is (verified or provisional) and what the claim rests on, so that the next agent reading the card knows how far to trust it.
