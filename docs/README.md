# Documentation

The pages in this folder, grouped by what you came to do.

## Build a brain for your own field

| page | what it covers |
|---|---|
| [build-your-own-brain.md](build-your-own-brain.md) | the five parts of a brain (store, recall, served notes, dreaming, coordination), where each lives here, and how to build each for a company, a studio or a lab |
| [brain-in-an-afternoon.md](brain-in-an-afternoon.md) | the short road: an empty folder at lunch, a brain agents search by evening, and a first measurement |
| [everything-is-a-node.md](everything-is-a-node.md) | what becomes a record and how records are linked, so requests, compactions, mistakes, files and code all land in the store |
| [prompts-as-nodes.md](prompts-as-nodes.md) | keeping the requests themselves, so the store records why work was done as well as what was found |
| [brain-building/compactions-as-brain-nodes.md](brain-building/compactions-as-brain-nodes.md) | keeping each compaction summary as a linked record, since it is the densest account a long session ever writes of what it was asked, did and left open |
| [brain-building/everything-to-brain-10-day-loop.md](brain-building/everything-to-brain-10-day-loop.md) | a prompt for an agent on a schedule: bring material in, link it, test recall, every ten minutes for ten days |
| [../examples/field_brain_starter/](../examples/field_brain_starter/README.md) | a complete small brain (a film studio's) with recall, hooks, a dream and a ten-question test; `new_field.py` turns it into an empty brain for any other field |
| [../framework/dreaming/README.md](../framework/dreaming/README.md) | the nightly pass in full: the agenda, the filing, connecting and nap dreams, and how to add a section for your field |

## Connect agents to a brain

| page | what it covers |
|---|---|
| [../AGENTS_GUIDE.md](../AGENTS_GUIDE.md) | the recall tools, the configuration for Claude Code and Codex, and what each choice was worth in the tests |
| [agency.md](agency.md) | the working habits that turn faster recall into finished work: a next-step note on disk, leases on shared state, an audit before each report, results written back |
| [codex-hooks-quickstart.md](codex-hooks-quickstart.md) | the hook files that put the brain in front of an agent at the right moment, for Codex and Claude Code |
| [brain-building/owner-words-reach-every-agent.md](brain-building/owner-words-reach-every-agent.md) | a hook that hands every session the person's own recent requests, repeated ones first, so an agent does not work from an out-of-date picture of what it was asked |
| [brain-building/task-checklist.md](brain-building/task-checklist.md) | one shared, dated checklist every agent writes to: who took which request, when it was done, and a seen mark only the person sets |
| [brain-building/keep-working-stop-hook.md](brain-building/keep-working-stop-hook.md) | stop hooks that send an agent back to its open work after a compaction or during a timed job, and the rules that keep them from looping |
| [cost.md](cost.md) | what the brain costs in tokens, each figure beside the accuracy it bought |

## What the tests measured

| page | what it covers |
|---|---|
| [../TESTS.md](../TESTS.md) | the three-arm tests (brain, documents only, model alone) and their results |
| [../results/earlier-tests/](../results/earlier-tests/README.md) | earlier tests, each with its design and aggregate scores |
| [evaluation-protocol.md](evaluation-protocol.md) | the paired protocol: one causal question, how arms are blinded and scored |
| [codex-runner.md](codex-runner.md), [attempt-ledger.md](attempt-ledger.md) | how a sealed evaluation is dispatched and how first attempts are recorded |
| [benchmark.md](benchmark.md), [benchmark-v4-10000-evidence.md](benchmark-v4-10000-evidence.md) | the deterministic 10,000-problem error-detection bank and its retained evidence |
| [challenge-bank.md](challenge-bank.md), [challenge-evaluation.md](challenge-evaluation.md) | the sealed challenge bank and the twenty-process comparison run on it |
| [research-status-ablation.md](research-status-ablation.md) | a tested diagnosis of research-status recall and the sealed study designed from it |

## The math store itself

| page | what it covers |
|---|---|
| [architecture.md](architecture.md) | the layers of the store, each auditable on its own |
| [design-brief.md](design-brief.md) | the brief the math store was built to |
| [retrieval-and-consolidation.md](retrieval-and-consolidation.md) | the safety contract for recall and for the reviews consolidation proposes |
| [nightly-pass.md](nightly-pass.md) | the store's own nightly pass: unreachable cards, claims with no evidence, proposed reviews |
| [formal-verification.md](formal-verification.md) | the pinned Lean toolchain and how machine-checked claims are kept |
| [store-findings-2026-09-13.md](store-findings-2026-09-13.md) | what a full read of the store found that the ingest checks had missed |
| [local-audit-protocol.md](local-audit-protocol.md) | how mathematical audits are run locally, apart from public corpus construction |
| [campaign-log.md](campaign-log.md) | the construction and audit log of the first hardening campaign |
| [cited-works.md](cited-works.md) | every work cited by the papers in this repository |
| [fpp_l2prime_ladder_20260829.md](fpp_l2prime_ladder_20260829.md) | a first-passage percolation measurement recorded with its tool, seed and the read fixed before the run |

## Publishing safely

| page | what it covers |
|---|---|
| [privacy-boundary.md](privacy-boundary.md) | the source gate and the publication gate, and why passing one does not pass the other |
| [threat-model.md](threat-model.md) | what must never enter the store or this repository, and the ways it could leak |
