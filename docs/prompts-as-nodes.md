# Requests as nodes

A research store holds what was found. It usually forgets what was asked. Months later nobody can say why a
card exists, whether a question was already put to the store, or whether an earlier answer was later refuted
and the question is open again. `math_brain.requests` keeps the requests.

## The model

Each request is a node in an append-only JSON-lines ledger (`requests.jsonl`, beside the store or wherever
`MATH_BRAIN_REQUESTS` points). Its id is `req_` plus twelve hex digits of the SHA-1 of the normalized text, so
the same question typed twice, with different case, spacing or punctuation, is one node with a count of two.

| field | meaning |
| --- | --- |
| `text` | the request, with e-mail addresses and home-directory paths removed before it is written |
| `role` | `researcher`, `agent` or `automation` |
| `first_asked`, `last_asked`, `times_asked` | when it was asked, and how often |
| `status` | `open`, `answered` or `dropped` |
| `links` | edges to store node ids or to other requests |

Four relations tie a request to the store:

- `asks_about`: the request concerns this card.
- `produced`: work on the request wrote this card.
- `answered_by`: this card answers the request. Adding the link marks the request answered.
- `follows`: the request continues an earlier request. A thread is everything reachable along `follows`.

The ledger is kept outside the SQLite store. The store's schema refuses node and edge kinds it does not know,
so a new kind inside it would stop older copies from opening the file. Requests and cards meet only through
ids in the links.

## Use

```
python -m math_brain.requests ask "Is the spectral gap of the Glauber dynamics bounded below at beta < 1?"
python -m math_brain.requests similar "spectral gap Glauber lower bound"
python -m math_brain.requests link req_3f0c9a1b2d4e claim_3d7e1176 produced
python -m math_brain.requests node claim_3d7e1176
python -m math_brain.requests open
python -m math_brain.requests show req_3f0c9a1b2d4e
```

`ask` prints the earlier requests that share most of their words with the new one. An agent should read those
before starting work: the question may already have an answer, or someone may be working on it.

## The nightly pass

`RequestLedger.consolidate(status_of=...)` is meant to run with the other consolidation steps. The status has
to be recomputed from authenticated evidence, so pass
`lambda node: recompute_current_status(store, node, verifier)` from `math_brain.verification`; the store's own
`current_status` refuses any claim that has verification events.

- an open request with a `produced` card that is now verified is marked answered by that card;
- an answered request whose answer is refuted, retracted or found to have a gap is reopened, with the reason in
  its note;
- a card whose status cannot be read is listed under `unresolved`, never counted as an answer;
- open requests untouched for fourteen days, and open requests asked more than once, are listed for a person.

Nothing is dropped automatically. Asking an answered request again reopens it, because a repeat means the
answer did not settle the question.

## At prompt time

`math_brain.request_hook` is a prompt hook for Claude Code and Codex. It reads the prompt, looks it up with
`similar`, and shows the agent at most three earlier requests with their status, how often they were asked and
the cards they produced, before the agent starts the work again:

```
MATH_BRAIN_REQUESTS=requests.jsonl python -m math_brain.request_hook          # Claude Code
MATH_BRAIN_REQUESTS=requests.jsonl python -m math_brain.request_hook --codex  # Codex wants a JSON envelope
```

It prints nothing when the ledger is not set, when nothing is similar enough, for prompts under four words, or
on any error. With `MATH_BRAIN_REQUESTS_RECORD=1` it also records the prompt, after the lookup, so a prompt never
matches itself.

## What it does not do

It does not decide that two differently worded requests mean the same thing. `similar` uses word overlap
(Jaccard on content words) and only proposes candidates; linking them with `follows` is a person's or an
agent's decision. It does not keep conversation transcripts, only the requests themselves.
