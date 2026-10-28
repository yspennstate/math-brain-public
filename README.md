# Math research brain

*Mathematical pseudo-Cognitive Dynamics*

A shared memory for agents that do mathematical research. The store holds about thirteen thousand cards (definitions, theorems, proof techniques, and the agents' own results: proofs, counterexamples, verified computations, corrected statements) joined by about nineteen thousand typed links. Around it are the tools agents use to search it, follow its links and write back to it while they work.

This repository contains the brain's code, a dated export of the store, the tools agents call, the records of the research campaigns that built it (among them a campaign on the Fourier entropy-influence conjecture), the papers that came out of that work, and the aggregate results of the tests that measure what the brain does for an agent.

Nothing in the method is specific to mathematics. To build a brain for a company, a film studio, a lab or a support desk, start with [examples/field_brain_starter/](examples/field_brain_starter/): twenty example records, a search tool, a prompt hook for Claude Code and Codex, a nightly dream with a runner for Linux, macOS and Windows, and a ten-question test that measures whether the records help. [docs/brain-in-an-afternoon.md](docs/brain-in-an-afternoon.md) takes a team from an empty copy of that folder to a measured brain in a day, [docs/build-your-own-brain.md](docs/build-your-own-brain.md) covers each part in full, [docs/everything-is-a-node.md](docs/everything-is-a-node.md) says what goes into the store and how it is linked, and [docs/agency.md](docs/agency.md) describes how agents should work with a brain so that better recall turns into progress on long tasks.

## How agents build on one another's work

Many agents use the brain at once: interactive Claude and Codex sessions, fleets of headless workers, and scheduled GPT tasks. None of them remembers anything from one session to the next. Their work adds up because every agent reads the store before it works and writes to it when it finds something, so each one starts where the others stopped. The agents that use the brain are the ones that build it, in the course of their research. The study of this loop, a memory that agents read, test and correct while they work, is what we call Mathematical pseudo-Cognitive Dynamics; the paper in `papers/pseudo-cognitive-dynamics-2026-09-23/` develops it.

The loop has five parts.

1. **Served cards.** A hook runs on every prompt, in Claude Code and in Codex, and puts a few cards from the store in front of the agent, each with a line saying how far to trust it. When nothing matches well it stays silent (`agent_tools/math_sense.py`).
2. **Deliberate recall.** When an agent needs something, it searches the store and gets whole cards back, with their ids and the ids of their links (`math_recall.py`). From any card it can step along the links (`math_recall.py --id`, `math_walk.py`). A link says how two results relate: one depends on, generalizes or is analogous to the other, or is easily confused with it (`distinct_from`).
3. **Links that grow with use.** When an agent uses two cards together, the link between them gets stronger, and strengths fade with time, so the links agents actually rely on rise in the ranking (`math_strength.py`).
4. **Writing back.** An agent writes its results as a packet: new cards and links with their sources, sealed with a hash. Before a packet lands, a held-out recall test runs on a copy of the store with the packet added, and a packet that costs an answer is held back. Packets land on the live store one at a time, each with an exact receipt. On 12 October 2026 nine packets landed this way; one more was held because its long titles pushed a correct answer out of first place, and four others are waiting for review. Wrong cards are never deleted: a corrected revision supersedes them and the supersession is recorded. Retracted links are kept in `edge_retractions` and known errors in `mistakes`.
5. **Shared work orders.** Scheduled tasks read a common board and a work order, such as the order that put every scheduled worker on the FEI conjecture, and commit their reports to a shared repository. Those records are in `results/`.

The store is exported to plain JSONL in `export/population/`. The public snapshot checked on 26 October 2026 contains 13,344 cards and 19,398 links, of which 231 are retracted (19,167 live). Its 16-table manifest and 56,733 rows pass the [release integrity check](papers/math-brain-2026-10-24/scripts/check_release.py). This is a dated publication snapshot, not a live mirror of the working store.

## What the tests show

In each test both arms use the same model, budget and questions, and the score is the number of correct answers. P values come from exact paired tests. The private questions and answer keys are withheld. After answer-bearing records are public, repeated tests are regression measurements; fresh held-out claims require unseen items and a new contamination audit. [TESTS.md](TESTS.md) describes each one.

**Does the brain help an agent answer?**

| Test | Without the brain | With the brain |
|---|---|---|
| 100 questions about results held in the store (Codex agents, 11 Oct 2026) | no tools: 0; text search over a copy of the store's files: 75 | recall tool: 83; hook, recall and link walk: 82 |
| 1,000 items whose answer must be recalled (13 Sep 2026) | 538 | 1,000 (462 helped, none harmed) |
| 61 reasoning and audit items (Claude agents, 5 and 6 Oct 2026) | tools only: 41 | full brain package: 52 (15 to 4, p = 0.019) |
| 80 questions about files kept in GitHub repositories (Codex agents, 12 Oct 2026) | git alone: 68 | git and the brain: 73 (9 to 4, p = 0.27) |
| 20 recall items, one Claude agent answering first without and then with the brain (23 Oct 2026) | 9 | 19 (10 to 0, p = 0.002) |
| 988 items, Claude agents at 600 seconds an item (23 and 24 Oct 2026) | model alone: 18.9%; the research repositories: 82.0% | 95.4% (146 to 13 against the repositories, p = 1.2e-29) |
| 383 items, Codex agents at 900 seconds an item (23 to 27 Oct 2026) | model alone: 21.7%; the research repositories: 96.9% | 94.8% (10 to 18, p = 0.19) |

The 1,000-item result holds where the answer has to be recalled; on items a strong solver can derive for itself, the brain changes nothing. On the 61 items the gain sits in the 26 that name a known result (22 against 13).

**What it costs.** On the 100 store questions the link walk left accuracy where it was (82 against 83) and cut the cost:

| | Recall tool alone | Hook, recall and link walk |
|---|---|---|
| Input tokens, all 100 questions | 186 million | 24.6 million (7.6 times fewer) |
| Uncached input tokens per question | 24 thousand | 13 thousand (1.8 times fewer) |
| Output tokens per question | 1.9 thousand | 0.4 thousand |
| Session-minutes | 666 | 78 |

How results are printed matters as much as how they are found: the same retrieval, printing titles and 700-character snippets without ids, scored 34 of 100.

**Is it getting better?** On 584 held-out questions the answer card was among the first eight results 298 times before the ranking changes of 12 October and 317 times after (p = 0.002); on six more question sets, pooled, the count went from 891 to 1,018 of 1,070. The gain comes from the ranking, BM25 with b = 0.4 and titles counted twice. Neither the meaning channel nor that day's new cards moved these counts.

**What it does not do.**

- The hook alone answers little: 7 of the 100 store questions. It was silent on 85 of them, including all 60 that were reworded so they share no words with their card.
- Spreading activation along links only re-ranks: 79 against 80, with 46 percent more input tokens.
- On new open problems it did not help. Fourteen Codex agents worked 13 problems on which the store held only a first attempt; graded blind, the brain arm scored 24 of 39 and the no-brain arm 26.
- An early version lost to plain documents: on a hard 300-item set it scored 238, against 264 for agents given the documents directly (14 to 40, p = 0.0005).

## Results posted since 13 October 2026

Twenty-five more problems from the literature were answered, fully or in part, between 13 and 23 October, each written up as a short paper with its verification code. Every paper is also copied into `papers/public/<name>/`. They are single-author write-ups checked by the agents' own audits; none has yet been refereed.

| Date | Repository | Result |
|---|---|---|
| 2026-10-13 | [gaussian-integer-spectra](https://github.com/yspennstate/gaussian-integer-spectra) | Gaussian-integer spectra of random sign matrices (Vu, Conjecture 9.5) |
| 2026-10-13 | [positive-cookie-ballisticity](https://github.com/yspennstate/positive-cookie-ballisticity) | Kosygina-Zerner Problem 5.3: speed of one-dimensional excited random walks with positive, possibly unbounded cookie stacks |
| 2026-10-13 | [sparse-allocation-poisson-limits](https://github.com/yspennstate/sparse-allocation-poisson-limits) | Poisson limits for large boxes in sparse random allocations |
| 2026-10-13 | [second-largest-degree-infinite-variance](https://github.com/yspennstate/second-largest-degree-infinite-variance) | The second largest outdegree of conditioned Galton-Watson trees with infinite variance |
| 2026-10-13 | [variation-threshold-stationary-times](https://github.com/yspennstate/variation-threshold-stationary-times) | The variation threshold, Kemeny's constant and stationary times of reversible Markov chains |
| 2026-10-13 | [relaxation-time-normal-approximation](https://github.com/yspennstate/relaxation-time-normal-approximation) | The relaxation time does not control the normal approximation of stationary additive functionals |
| 2026-10-13 | [nonergodic-galton-watson-flow-rule](https://github.com/yspennstate/nonergodic-galton-watson-flow-rule) | A nonergodic flow rule with Galton-Watson stationary measure |
| 2026-10-13 | [sandpile-holes-corner-angles](https://github.com/yspennstate/sandpile-holes-corner-angles) | Corner angles of sandpile aggregates on a background of holes (paper and computations) |
| 2026-10-14 | [bilateral-preference-degree-limits](https://github.com/yspennstate/bilateral-preference-degree-limits) | Degree fluctuations in bilateral preference random graphs: the limit laws of the root degree of LK(n,k) in every regime |
| 2026-10-14 | [supermodular-speed-ordering](https://github.com/yspennstate/supermodular-speed-ordering) | Supermodular ordering of speeded-up Markov chains without stochastic monotonicity (Leskelä's Problem 3) |
| 2026-10-14 | [beta-splitting-leaf-correlation](https://github.com/yspennstate/beta-splitting-leaf-correlation) | Correlation of leaf heights at distance r in the critical beta-splitting random tree (Aldous-Janson Open Problem 1) |
| 2026-10-16 | [drift-jump-leftmost-particles](https://github.com/yspennstate/drift-jump-leftmost-particles) | The stationary law of the leftmost particles in Aldous's drift-jump process |
| 2026-10-16 | [brownian-prefix-filling](https://github.com/yspennstate/brownian-prefix-filling) | A Brownian piece in front of a process absolutely continuous with respect to Brownian motion (Burdzy-Scheutzow Problem 7.5) |
| 2026-10-17 | [stable-unimodality-opposite-gaps](https://github.com/yspennstate/stable-unimodality-opposite-gaps) | Opposite gaps defeat large-time unimodality for one-sided stable processes (Hasebe-Ueda Conjecture 5.5) |
| 2026-10-18 | [hub-paths-barely-subcritical](https://github.com/yspennstate/hub-paths-barely-subcritical) | Hub paths and the largest component of the barely subcritical configuration model (van der Hofstad, Open Problem 4.13) |
| 2026-10-18 | [rrt-layer-tail](https://github.com/yspennstate/rrt-layer-tail) | The layer distribution of the random recursive tree (Stepanyants-Krapivsky-Hartle-Krioukov, Conjecture 1) |
| 2026-10-18 | [partition-qso-empty-body](https://github.com/yspennstate/partition-qso-empty-body) | Partition quadratic stochastic operators converge to the empty body (Ganikhodzhaev-Rozikov, Problem 10) |
| 2026-10-19 | [mmpp-stationary-order](https://github.com/yspennstate/mmpp-stationary-order) | The time-stationary and Palm inter-arrival times of a Markov-modulated Poisson process need not be ordered |
| 2026-10-20 | [shuffled-ablq-dominating-pair](https://github.com/yspennstate/shuffled-ablq-dominating-pair) | Counterexample to the conjectured dominating pair for DP-SGD with shuffled batches (Chua et al., Conjecture 3.2) |
| 2026-10-20 | [levy-drift-noncompact](https://github.com/yspennstate/levy-drift-noncompact) | A Levy random drift destroys compactness for every confining power (Shiozawa-Wang, Remark 5.3(ii)) |
| 2026-10-20 | [urn-euclidean-contractivity](https://github.com/yspennstate/urn-euclidean-contractivity) | On a contractivity question of Neri and Pinto for generalized Polya urns (arXiv:2607.07309, Remark 3.7) |
| 2026-10-20 | [cantor-harmonic-codings-singular](https://github.com/yspennstate/cantor-harmonic-codings-singular) | The binary and ternary harmonic measures of the Cantor set are mutually singular (Lyons-Peres Question 16.7) |
| 2026-10-21 | [bjorklund-star-quotient](https://github.com/yspennstate/bjorklund-star-quotient) | A homogeneous space G/H of infinite index with no nonconstant quasiharmonic functions (Bjorklund, Problem 2) |
| 2026-10-22 | [nonnormal-orbit-quotients](https://github.com/yspennstate/nonnormal-orbit-quotients) | A non-normal subgroup with a complete orbit quotient K_m that no normal quotient realizes (Grimmett-Li, Question 4.5) |
| 2026-10-23 | [arc-transitive-edge-heat](https://github.com/yspennstate/arc-transitive-edge-heat) | Edge monotonicity of the normalized heat kernel on arc-transitive and 1-walk-regular graphs (Aldous-Fill, Open Problem 7.30) |

Earlier papers from the same work, from July to 12 October, are in `papers/public/` as well.

## Repository map

| Path | Contents |
|---|---|
| `src/math_brain/` | the store, retrieval and ranking, triggers, ingestion, verification, Lean checking, the command line |
| `tools/` | export and import of the store, the Wikipedia and ProofWiki harvesters, maintenance scripts |
| `agent_tools/` | the scripts agents call while they work, and the hook |
| `export/population/` | the store as JSONL: cards, claims, links, retracted links, provenance, packets, evidence, mistakes; `MANIFEST.json` gives counts and SHA-256 digests |
| `tests/`, `docs/`, `config/`, `formal/`, `examples/` | unit tests, design notes, configuration, Lean files, examples |
| `results/fei/` | the Fourier entropy-influence campaign |
| `results/open-problems/` | attempts on open problems: proofs, counterexamples, verification code, papers in progress |
| `results/open-problems-codex-2026-10-11/` | thirty Codex agents on 112 open problems: 24 solved by their verdict (17 of them through two independent audits), 78 partial |
| `results/scheduled-tasks/` | mathematics campaigns run by scheduled tasks |
| `results/proofnet24-brain/` | work on a probability correlation problem, three collective rounds and a quadratic-form density problem |
| `papers/` | papers that came out of this work, and copies of their public repositories |
| `framework/` | the machinery around the store: shared memory and its nightly consolidation, the prompt hooks, the coordination layer that keeps agents from editing the same files, the supervised fleet |

## The FEI conjecture

The conjecture is open. The campaign proved that H ≤ 2(I − Var) + 2U for every Boolean function, where U = Σ_S p(S) log₂(π(S)/p(S)) compares each Fourier weight p(S) with the total weight π(S) on the supersets of S. So FEI is equivalent to a bound U ≤ C·I. The work now targets one inequality (GU): the restriction differences of U, summed over the coordinates, are at most a constant times the total influence. The largest ratio found is 3.09, which would give FEI with C ≤ 8.18. FEI itself is proved, with explicit constants, on several classes of functions. See [results/fei/README.md](results/fei/README.md).

## Using the store

```
pip install -e .
python tools/import_store.py --out local/population/brain.sqlite3
export MATHBRAIN_STORE=local/population/brain.sqlite3 MATHBRAIN_BUILD_SRC=src
python agent_tools/math_recall.py spectral gap of the random transposition walk
python agent_tools/math_recall.py --id <card id>
python agent_tools/math_walk.py <card id> --toward "mixing time lower bound"
```

Every row in the store carries a digest of its content, and the reader refuses a row that no longer matches its digest. In this copy a file path on the machine that built the store is replaced by an opaque identifier of the form `urn:mb-local:<hash>`, a link into a private repository by `urn:mb-private:<hash>`, and the name of a private repository by the words "a private repository". The digest of every row changed this way is recomputed, and every row that refers to it by digest is updated to match, so every row in `export/population/` reproduces its digest on any machine. Thirty-four cards and seven links did not match their stored digest in the working store either; their digests are recomputed from their content as it stands. A row's identifier is retained to preserve citations, but sanitization can change its content digest. This is a derived release snapshot and does not demonstrate an append-only revision repair in the private store.

[agent_tools/README.md](agent_tools/README.md) describes each tool, and [AGENTS_GUIDE.md](AGENTS_GUIDE.md) says how to connect an agent to the store and what each choice was worth in the tests. [docs/agency.md](docs/agency.md) describes the working habits that turn faster recall into progress on long tasks, and [docs/build-your-own-brain.md](docs/build-your-own-brain.md) explains how to build the same kind of store for another field with the code in [framework/](framework/).


## Sources

Each card names its origin in the `source_id` field of its metadata (`metadata_json` in `nodes.jsonl`). Cards from Wikipedia (`wikipedia:`) and ProofWiki (`proofwiki:`) are under CC BY-SA; cards from arXiv papers (`arxiv:`) state one result with its citation; the rest come from the work itself. [RIGHTS.md](RIGHTS.md) gives the counts and terms, and [LICENSE](LICENSE) covers the code.

## About this copy

This repository is a snapshot taken from the working repositories, not the repositories themselves. Outside the store export, paths into the home directory of the machine that ran the work are shortened to `~`, and the names of other private repositories become `<private-repo>`; the two repositories this copy was taken from are private as well. The author's own e-mail addresses are replaced by a placeholder except in the author blocks of papers. Spelling slips in the quoted prompts that directed the work are corrected. Zip archives were opened and treated the same way, member by member. A compiled PDF cannot be edited, so PDFs that show local paths or private repository names were left out, and the Markdown or LaTeX each was compiled from is kept. Third-party papers and their text extractions are not included. The store export is changed only in the way described above for its digests. A hash recorded in a run's manifest refers to its file as it was before these edits, so some of those hashes do not match the copy here.

## Open access and release review

Everyone may read and download this repository. Original project code and project-owned data are MIT-licensed; the [revised Math Brain paper](papers/math-brain-2026-10-24/math_brain.pdf) is additionally available under CC BY 4.0. Wikipedia and ProofWiki material retains its source licences. See [RIGHTS.md](RIGHTS.md) for attribution and third-party exceptions and the [26 October release review](papers/math-brain-2026-10-24/RELEASE_REVIEW.md) for the verified checks and remaining review boundaries.
