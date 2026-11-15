# Worker folders from the open-problem frontier, October 2026

These are the working folders of solver agents on rows of the open-problem list in
`results/open-problems/top200-probability-list-2026-10`. They are kept as the agents left them, so
the intermediate steps can be read:

- the routes tried;
- the claims and their versions;
- the audits one agent wrote of another's claim;
- the receipts that tie a claim to the exact file that was checked;
- the scripts that did the checking.

Nothing here is a finished paper. A claim counts only once an independent audit admits it, and many
claims here were never admitted.

## What a worker folder holds

Each solver followed the same rules (summarised below), so the folders share a layout:

- `STATUS.md` — where the worker stands, ending with a NEXT line naming the target it is on.
- `ROUTES.jsonl` — one line per route: the route in one sentence, live, dead or done, and for a dead
  route the precise reason and the failing step.
- `CLAIMS.jsonl` — one line per claim, with its kind and the target it serves. The kinds are:
  - moved: a step of the frontier argument now goes through;
  - narrowed: the statement is proved on a new part of its range;
  - special;
  - bound;
  - literature;
  - route-failure.
- `proofs/` — the proof text of each claim, versioned.
- `SELF_AUDIT.md`, `LITERATURE_AUDIT.md`, `AUDIT_QUEUE.md` — the worker's own checks, its literature
  pass and what it sent for review.
- `scripts/`, `logs/` — the code that checked each numerical step, and its output.

## The folders

- `w690_T233` — row T233, the linear width-depth band for Gaussian deep-linear initialization
  (Du and Hu; Shamir).
  - Claim C001 proves the loss stays in a fixed band on a logarithmic range of widths.
  - Claim C002 is an exact witness showing that the unchanged neighbourhood argument cannot reach the
    remaining strip.
  - The full target stays open.
- `w677` — row T127, recurrence and transience for one-sleeper models in dimensions three and four,
  which remain open.
  - The handoff `RESULT.md` records two independent placements of a self-similar threshold in
    (0.2648, 0.2649].
  - It records the lower-model constructions that passed review.
  - It gives frozen numerical means, labelled as evidence only.
- `recovery` — the review chain for four rows:
  - T039, plurality is stablest;
  - T067, tightness of the Kesten–Stigum bound for reconstruction on trees;
  - T170, the Eden model limit shape in low dimensions;
  - T186, the circumference of G(n, c/n).

  Each subfolder is one admission or review:
  - the claim reviewed;
  - the independent checker written from the proof text alone;
  - the receipt with the checked file's hash;
  - for T186, the reverse-route records and the coalesced-closure check.
- `c5693_t170_d12_replay` — an independent replay of the T170 dimension-12 certificate. It rebuilds
  every value from the stated recursion without reading the certifier's code.

## The rules the workers followed

A worker starts from the frontier paper and the exact point where its proof fails, not from earlier
attempts. Before starting any route it checks the row's record of settled facts and dead routes, and
it does not redo one without a written reason. It opens and closes every route in `ROUTES.jsonl`, so
a later worker inherits the failures as well as the successes. Among live routes it chooses by
Thompson sampling over every agent's recorded outcomes (`route_bandit.py` in the frontier tools).
That way a route that keeps stalling is tried less.

## Credit

The problems and the arguments these workers extend belong to the authors cited in each row of the
list and in each worker's `LITERATURE_AUDIT.md`. The checking discipline of a certificate rebuilt by
an independent program, from the proof text alone, follows long practice in computer-assisted proof.
