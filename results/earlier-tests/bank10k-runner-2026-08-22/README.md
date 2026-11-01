# bank10k three-arm runner

run_bank10k.py is the runner behind the bank10k tests: none, placebo and brain arms over a frozen stratified sample
of a 12,096-item bank of probability proofs with at most one planted fault. The replication result it produced is in
results/earlier-tests/bank10k-replication-2026-08-22. The two literature banks (plit-probability-bank-2026-09-06 and
mdlit-multidomain-bank-2026-09-06) import it for the same machinery.

What it does:

- `sample` freezes a subset stratified over the 50 reasoning cells (family, fault step, mechanism), with clean
  controls drawn in proportion, so a run is reproducible and its cost is known before it starts.
- `notes` builds the brain arm's notes from the math store and the placebo arm's notes by a deterministic
  derangement of the same notes, so placebo matches brain in length and form but not in relevance. Brain against
  placebo is the contrast that identifies the value of the content.
- `serve` runs one arm, resumable. Every solver call is sterile by default (no setting sources, so no hooks and no
  global instructions), and a verdict whose transcript shows an injected note is refused whatever the flags said.
  The prompt is checked to arrive whole before a run is spent on it.
- `grade` gives full credit on a faulted item only for the verdict "flawed" together with the exact fault step;
  clean items are the false-positive control.

Measured cost, recorded in the code: about 90 seconds and about four cents a call, three calls per sampled item.
Local paths read `<HOME>`. The bank's generator, items and keys are not included.
