# The nightly pass

`consolidation.consolidate` reads the graph and proposes reviews: unreachable cards, claims with no
verification edge, negative edges that need resolving, reflexes to rehearse against the mistakes they came
from, and candidate associations. Called once, it forgets what it proposed. `math_brain.nightly` is the part
that runs it every night and remembers.

```
python -m math_brain.nightly run --store brain.sqlite --queue dream/queue.jsonl \
    --requests requests.jsonl --digest dream/DIGEST.md
python -m math_brain.nightly show --queue dream/queue.jsonl
python -m math_brain.nightly review --queue dream/queue.jsonl proposal_0a1b2c3d4e5f6a7b8c9d0e1f done --note "edge added"
```

A run opens the store read-only and appends to the queue, a JSON-lines log with three kinds of event:

- `new`: a proposal seen for the first time, with its hypothesis and review steps;
- `night`: the ids seen that night and a digest of the store's contents;
- `review`: a person or agent closed a proposal as `done` or `dismissed`.

From that log the queue knows how many nights each proposal has come back, which proposals vanished because
the graph changed (an orphan that gained an edge), and which are still open. When the store is unchanged since
the last run, nothing is appended, so a run on an idle store is free and the night counts mean real nights of
change. Mistake or reflex rows that fail their own integrity checks, and edge kinds this build does not know,
are reported in the digest rather than dropped in silence.

The proposals stay quarantined. The queue holds review work, not evidence; closing a proposal as `done` says
the review happened, and any change to a claim's status still goes through the verification gates.

With `--requests`, the same run consolidates the request ledger (see `prompts-as-nodes.md`) and lists stale
and repeated requests in the digest.
