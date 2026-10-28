# What the brain costs

Four measurements, each on its own population. A cost is quoted only beside the accuracy of the
same runs. Prices are list prices, and the sessions themselves ran on subscription accounts.

## Where a connected question's tokens go (recall four-arm study, 25-27 September 2026)

There were 173 questions per arm, answered by Claude Opus sessions. The connected arm had the brain
wired in through recall, prompt hooks and standing instructions. One arm had plain file search,
and another had file search plus the recall command but no hooks and no standing context. Each API
call was counted once by its message id. Context here means cache reads plus cache writes plus
uncached input.

| arm | first-call context | calls per question | context tokens per question | share that is the opening context |
|---|---|---|---|---|
| connected | 105,748 | 12 | 1,522,187 | 0.85 |
| files and recall | 8,278 | 13 | 395,115 | 0.27 |
| files | 8,269 | 13 | 420,015 | 0.27 |

The first call's context is what a session opens with before it does any work: the system prompt,
tool definitions, instruction files, wake-up hooks and the question. In the connected arm that
opening is re-read on every call and makes up 85 percent of a question's tokens (quartiles 0.77 and
0.91). Subtract it, and the connected arm's own working context is a median 198,862 tokens a
question. That compares with 285,565 when recall is run by hand and 309,116 for plain file search.
So with the brain the work itself takes about a third fewer tokens. The extra cost is the context
the session carries, not the searching.

Writing a context costs forty times as much as re-reading it (cache write 8, cache read 0.20 and
output 20 dollars a million tokens, fitted to the client's own cost figures). A median connected
question came to 1.51 dollars: 1.06 in cache writes, 0.27 in re-reads and 0.17 in output. About
three quarters of that is the standing context. The largest single piece was a 39,000-token
instruction file, most of it rules for other projects that a math session never uses.

On the 142 questions that both arms ran cleanly, the connected arm and the files arm each answered
134, at 1.72 against 0.77 dollars a question. The recall-only arm against files only scored 131
against 128 of 137 (p = 0.25), at 0.75 against 0.74 dollars. Recall by itself costs nothing extra.
The cost sits in the hooks and the standing context.

What follows for anyone building one is simple. Keep the instructions every session loads short,
and hand domain rules to a session when it enters that domain. Each 10,000 tokens taken out of the
opening context saves about 0.10 dollars a question at twelve calls. That is a prediction about cost
only. Whether accuracy holds with a slim opening has not been measured.

## Teams (8-9 October 2026)

There were 20 items and four arms (brain single agent, brain team, single agent, team), run with
Codex. Every item where the arms disagreed went to the brain arm: 4 to 0, and 8 to 0 counting the
7 October teams run (the items are shared, so this is suggestive, not shown). The team with the
brain matched the single agent with the brain item for item. Without the brain, the team lost two
items to the single agent. A team used about three times the tokens, 56,000 to 61,000 an item
against 17,000 to 18,000. Run-to-run variation on this set is about three items in twenty.

## The three-arm test (23-25 October 2026)

The full figures are in [TESTS.md](../TESTS.md). With Claude, a brain-arm session read a quarter of
the repository arm's input, wrote two fifths of its output and cost 58 percent as much. The whole
test was 3,113 sessions, 198 session-hours and 107 million input tokens, at 125.69 dollars. This is
the opposite of the September result for a reason: the brain arm here received its notes through a
recall tool with no file tools, and carried no large standing instructions. The repository arm
paid for its searching.

## Reading the store

The recall rules in [CHANGES_2026-10-15](../framework/docs/CHANGES_2026-10-15.md) were chosen
partly on cost. Walking a card's links with `--id` reached the same answers as searching again, 82
against 83 of 100, on about half the uncached tokens. Spreading activation (`--depth`) added 46
percent more tokens for one answer fewer. A search prints about 3,500 tokens.

## One day of the open-problem campaign (10 October 2026)

Every Codex session recorded for 10 October was counted from its own log. The open-problem solvers
ran 464 sessions, 415 of them at maximum effort, and used 2.73 billion tokens in the day before the
account's usage ran out mid-morning.

That day solved no open problem. The solvers held 1,561 claims at the end of it, and every one
still listed a remaining gap. Among them were 442 independently checked proofs of special cases or
lemmas, 558 proved special cases, 361 sketches, 112 conjectures and 43 pieces of numerical evidence. The
campaign's results to that date were 22 answers from September, 15 of them full answers or
refutations and 7 reductions or partial answers. Spend at this scale buys checked partial results,
not solutions, and the referee pass in
[2026-10-10-two-agents-cross-family-referee](../results/frontier-2026-10/2026-10-10-two-agents-cross-family-referee/README.md)
is what sorted those claims.

## Building and testing the store (6-17 October 2026)

For twelve days headless Claude sessions built the store and ran its tests: 357 runs, 347 hours of
session time, 2.91 billion cache-read tokens, 171 million cache-write tokens and 28.3 million output
tokens, 18.5 million of them thinking. At list prices that is 2,495.52 dollars. Priced as if every
input token were uncached it would have been 12,705.81, so prompt caching took 80 percent off. The
runs went through subscriptions, so these are list-price equivalents, not bills.

142 of the runs ended flagged as errors, mostly at their turn cap or at an account limit, and they
carried 77 percent of the spend. A flagged run is not necessarily wasted, since the workers wrote to
disk as they went, but a turn cap set too low spends most of a run's tokens on context it then drops.

## What better recall bought

Most of the gain came from how the store prints, not from what it holds. The same retrieval scored
34 of 100 printed as snippets, 83 printed as whole cards with their identifiers and links, and 86 when
the agent gave two or three wordings in one call. On 64 questions about the agents' own past work the
answer came first for 24 in September and for 46 in October. On 1,000 items that each need a fact held
as a card, agents answered 538 without the brain and all 1,000 with it. Walking a card's links reached
the same answers as searching again on about half the uncached tokens, and in the three-arm test a
brain-arm session cost 58 percent of a repository-arm session. Section 9 of
[the paper](../papers/math-brain-2026-10-24) gives each test in full, the losses included.

## Long sessions

A long session re-reads its whole context on every call. One measured session on 9 October carried
about 663,000 tokens a turn. Another made 5,931 calls over two days and read 3.24 billion cache
tokens, opening at 141,460 tokens. [framework/docs/COMPACTION.md](../framework/docs/COMPACTION.md)
describes how sessions are compacted to keep that down.
