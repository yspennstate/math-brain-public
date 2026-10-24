# 100 random bank questions, ten subagents, brain against no brain

Registered before any verdict was served. The question, 2026-09-07: *"take 100 random questions
from the math test bank and test with 10 subagents on these questions, with and without the brain to see how they do."*

## The bank and the draw

`campaign_2026-09-06_prob_lit_bank/items/plit.jsonl`, 12,193 items. Each item is an arXiv math.PR theorem or lemma
with its proof rewritten as numbered steps; in a flawed item exactly one place of one step is altered by one of
thirteen operators. Truth lives in `<quarantined keys file>` and never appears in
anything a solver sees.

100 items drawn uniformly with seed 20260907 from the 11,867 items that have a key and are not among the 326 that
the defects registry flags as suspiciously paired. Composition (from the keys, hidden from every solver):
67 flawed / 33 clean; tier A 41, tier B 26; median 5 steps. Frozen in `SAMPLE.json`.

## The arms

Same model (claude-sonnet-5), same 100 items, same ten shards of ten, same task text. One difference:

- **none** - ten subagents, no brain. Told explicitly not to consult the brain, memories, or any store; the
  argument in front of them is all they get.
- **brain** - ten subagents with the brain available and told to use it: `ask_lit.py` over the proof-audit and
  literature store the lane serves from (243,287 nodes: the proof-audit knowledge layer, 53,355 arXiv math.PR
  statements, 13,701 abstracts, 176,450 Mathlib declarations) and `brain.py recall` over the memory brain. They
  query as much as they want before deciding.

This is an *agentic* brain arm, not the served-notes arm of `PROTOCOL_PLIT.md`. Stage 1 (07:3x today) served the
top-3 notes into the prompt of a tool-less solver and found nothing; the open question its own verdict named was
"a solver with tools". That is what this measures.

## The grade

`grade_plit.py` unchanged, the B12 rule: a flawed item is correct when the verdict is flawed **and** the reported
step equals the key's step; clean items feed only the false-positive guard.

- **Primary**: full credit on the 67 flawed items, brain against none, paired by item, exact McNemar.
- **Secondary, descriptive**: detection only (verdict flawed at any step); false positives on the 33 clean items;
  slices by tier and by operator family.

n = 67 flawed pairs. This detects only a large effect - roughly 15 points or more. A null here is a null with a
wide interval, not an equivalence, and will be reported as such.

## What would make the brain arm's win a false one

Leakage: the store contains the literature statements the bank was cut from, and the builder kept 12,178 nodes
whose text equals a bank claim (statement-level, answer-free - the *step* shingles were dropped). A brain agent
that retrieves the source paper's own statement learns the claim, not the altered step, so it should not by itself
reveal which step was changed. If the brain arm wins, the retrieved titles get read against the sampled papers
before the result is believed.

Both arms run under the same session hooks, so both receive the same ambient reflex injections on tool calls;
that is balanced across arms but is not zero.
