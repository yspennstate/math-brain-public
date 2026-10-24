# Giving an agent the brain

This note is for someone who wants their own agents to work from this store: a Claude Code or Codex session, a headless worker, a fleet of them. It says what the brain changes in an agent, how to connect it, and what to tell the agent so it uses the store well. Every claim about what helps comes from a test in [TESTS.md](../TESTS.md).

## What an agent gains

An agent with no memory starts every session from nothing. It can read files, but it does not know which files matter, so it reads many of them, and when the time runs out it stops with no answer. The brain changes three things.

**It reaches the record sooner.** In the three-arm test of October 2026, Claude agents with the recall tool answered 94.3 percent of 755 items, agents that could search the same repositories without the brain answered 78.1 percent, and agents with neither answered 21.7 percent. On the 593 items that both the brain arm and the repository arm finished in time they were level (99.2 against 99.3 percent). The difference was time: the repository arm timed out on a fifth of the items, the brain arm on one in twenty, and the brain arm took 136 seconds an item against 241.

**It reads less.** A brain-arm session read about a quarter of the input tokens of a repository-arm session and wrote two fifths of the output. With the link walk the cost falls further: on 100 store questions the hook, recall and walk together used 7.6 times fewer input tokens than recall alone, at the same accuracy (82 against 83).

**It knows when it does not know.** Every miss of the brain arm on the first 100 Codex items was an abstention, never a wrong value. Recall prints a WEAK MATCH line when its best score is low, and an agent told what that line means stops instead of guessing.

What the brain does not do: it does not prove new theorems for the agent. On 13 open problems where the store held only a first attempt, agents with the brain did no better than agents without it (24 against 26 of 39). It helps where the answer, or a piece of it, is already somewhere in the store.

## Setting it up

Build the store once, as in the [README](../README.md#using-the-store):

```
pip install -e .
python tools/import_store.py --out local/population/brain.sqlite3
export MATHBRAIN_STORE=$PWD/local/population/brain.sqlite3 MATHBRAIN_BUILD_SRC=$PWD/src
```

Then give the agent recall in one of two ways.

**As a tool (recommended).** `agent_tools/mcp_recall_server.py` is a small MCP server with one tool, `math_recall`, that takes one to three wordings or a list of card ids. It is the server the brain arm used in the three-arm test, and it needs no shell, so it works for agents that are not allowed one.

Claude Code:

```
claude mcp add mathbrain -e MATHBRAIN_STORE=$MATHBRAIN_STORE -e MATHBRAIN_BUILD_SRC=$MATHBRAIN_BUILD_SRC \
  -- python /path/to/agent_tools/mcp_recall_server.py
```

Codex, in `~/.codex/config.toml`:

```
[mcp_servers.mathbrain]
command = "python"
args = ["/path/to/agent_tools/mcp_recall_server.py"]
env = { MATHBRAIN_STORE = "/path/to/brain.sqlite3", MATHBRAIN_BUILD_SRC = "/path/to/src" }
```

**From a shell.** An agent with a shell can call the scripts directly:

```
python agent_tools/math_recall.py "first wording" --or "second wording" --or "third wording"
python agent_tools/math_recall.py --id <id> <id>
python agent_tools/math_walk.py <id> --toward "what you are looking for"
```

**The hook (optional).** `agent_tools/math_sense.py` runs on every prompt and puts a few cards in front of the agent when the prompt is mathematical and a card matches well. In Claude Code add it to `settings.json`:

```
{"hooks": {"UserPromptSubmit": [{"hooks": [{"type": "command", "command": "python /path/to/agent_tools/math_sense.py"}]}]}}
```

In Codex list it in `hooks.json`; the script writes the JSON form Codex expects. The hook is quiet by design (it stayed silent on 85 of the 100 store questions), so it is a prompt to look, not a substitute for recall.

## What to tell the agent

The way an agent searches matters as much as the store. These instructions come from measurements; put them in the agent's system prompt or its project instructions file.

1. Search before you answer, and before you say you do not know. Twice in the Codex runs an agent abstained without ever calling recall.
2. Give two or three wordings in one call, each phrased the way a card would put it: the object, the theorem or method by name, the symbol, the author. Not the wording of the question. With two or three wordings in one call agents answered 86 of 100 store questions, with one wording a call 76.
3. When a printed card looks close, read it and its neighbours whole with `--id`. Walking from a near card answered as many questions as searching again (82 against 83) on about half the uncached tokens.
4. Stop when a printed card answers. A WEAK MATCH line means reword. After three rounds of wordings with nothing, say the store does not have it.
5. Leave the spreading depth at 0. Spreading only re-orders cards the words already found, and it costs 46 percent more tokens.
6. Copy a card id in full from the `--id` printout when the id goes into an answer or a record; search output shortens ids.
7. A served card is a lead, not a verdict. Each card carries a line saying how far to trust it (verified, unreviewed, a harvested draft); check it before you build on it.

## Brain and files together

The three-arm test kept the brain arm away from the files, to measure each source alone. An agent you deploy should have both: recall first, then the files to confirm or to find what recall missed. The Codex runs show why. Three times a search missed a record that the repository arm found by reading files, and one of those records was mostly digits and punctuation, which word-based recall ranks poorly and a text search finds at once. If a record is a table, a list of numbers or a formula, search `export/population/*.jsonl` for it directly. We have not yet run a combined arm, so we cannot say by how much it beats the brain alone.

## Writing back

An agent that only reads the store gets faster; agents that also write to it make the next agent faster. Results go in as packets of cards and links with their sources, and a packet lands only if a held-out recall test on a copy of the store loses nothing with it added ([retrieval-and-consolidation.md](retrieval-and-consolidation.md)). Recall and the walk also record which cards were used together, and `math_strength.py` turns that into link strengths, so the links agents rely on rise in the ranking. Nothing an agent writes to its own copy reaches this repository; that copy is yours.

## Budget

At list price a Claude brain-arm session in the three-arm test cost about 5 cents, a repository-arm session about 9 cents and a session with no tools about 1 cent, and the brain arm used 58 percent of the repository arm's session-hours. The figures leave out sessions stopped at the time limit, which record no tokens, and most of those were in the repository arm.
