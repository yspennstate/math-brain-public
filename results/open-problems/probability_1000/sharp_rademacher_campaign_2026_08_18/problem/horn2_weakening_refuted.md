# I tried to weaken my own horn-2 chain and the weakening is false — with the object it hands us instead

Author: main session c53c1d50, 2026-08-19 ~03:2x. This records a **refuted self-correction**, kept because the refutation produced the campaign's first candidate class member.

## 1. The correction I attempted

Working the unified G2/horn-2 question of `g2_sharpened.md` §6, I argued that the horn-2 chain's step 3 — *large stars dissolve under arm decomposition* — **fails for class members by definition**, on this reasoning:

> The k-arm star decomposes because its arms meet only at the homogenizer `q`, so `q` is a cut vertex. The residual class consists of strongly connected components. **A strongly connected object has no such cut.** So a class member cannot have separable arms, and the arm decomposition is unavailable exactly where the chain needs it.

I wrote it up, concluded horn 2 was at the same `log n` wall as horn 1, and was about to propagate that into `STATE_OF_THE_PROOF.md` §3 and §6, `STATE.md` and `LOG.md`.

## 2. The bolded step is false

Strong connectivity is a property of a *directed* graph; a cut vertex is a property of the *underlying undirected* graph. Nothing links them. The witness is the **directed bowtie** — two directed cycles sharing one vertex:

```
1 → 2 → 3 → 1        strongly connected : True
3 → 4 → 5 → 3        cut vertices       : [3]
```

Strongly connected (everything reaches everything through 3), and removing 3 splits `{1,2}` from `{4,5}`.

Worse for the correction, the natural generalization is exactly the object I had just declared impossible. The **k-arm star-of-cycles** — hub `0`, arm `i` the cycle `0 → a_i → b_i → 0` — is strongly connected **for every k**, with the hub the unique cut vertex:

| k | strongly connected | cut vertices |
|---|---|---|
| 2 | True | [0] |
| 3 | True | [0] |
| 4 | True | [0] |
| 5 | True | [0] |

Controls, run in the same pass, behave as they must: a plain directed cycle `C₃/C₄/C₆` is strongly connected with **no** cut vertex, and a path `P₄` is **not** strongly connected and has two. Sampling 200,000 random digraphs on 5 vertices, 5,776 of the 71,495 strongly connected ones (8.1%) carry a cut vertex — strong-with-a-cut is common, not a curiosity. Script: `scratchpad/bowtie_check.py`.

## 3. So the correction is withdrawn, and the original labelling stands

The chain's step 3 is **unproved**, exactly as `horn2_closes_modulo_admissibility.md` labelled it in the first place. My attempt to show it *fails* is refuted by explicit counterexample. Both the "closes" and the "fails by definition" readings are unsupported; the honest status is the one already on the books, and **no change to `STATE_OF_THE_PROOF.md` or the claim ledger is warranted.** The chain was right to be labelled CONDITIONAL and stays there.

Note the direction of the error: the refutation pushes *toward* the original chain, not away. Strong connectivity does not block the arm decomposition, so the structural objection I raised against step 3 simply is not there.

## 4. What this hands us: a candidate class member

The campaign's standing weakness is stated in `STATE_OF_THE_PROOF.md` §7 — **no explicit member of the residual class**, so every number computed all campaign is a measurement on a known non-member. The star-of-cycles is the first shape that is simultaneously:

- **class-shaped** — strongly connected, so it survives condensation as a single block rather than decomposing, which is what the class assertion demands; and
- **high-multiplicity** — a star core with `k` arms gives boundary multiplicity `D = k`, unbounded, which is the regime horn 2's step 3 is about.

Every previous object failed one of these. The pure k-arm star has `D = k` but is not strongly connected. The NAE path and cycle are strongly connected but have `D = O(1)`. The star-of-cycles has both, and it has them for every `k`.

That makes it the first object worth testing as an actual sign fibre: build it, compute `d_cb`, `μ`, `λ`, and see whether it is a genuine class member and whether its arms dissolve. If they dissolve, step 3 gains its first evidence *inside* the class rather than outside it. If they do not, we have the counterexample that settles the chain the other way. **Either outcome moves a question that has been definitional all campaign onto measurable ground** — which is the first time that has been true for horn 2.

## 5. The methodological point

The failed argument reasoned about the *star* (a known non-member) and the *class definition* in the same breath, and let a graph-theoretic word — "connected" — carry between a directed and an undirected meaning without checking. Two minutes of computation refuted what half an hour of prose had built, and it refuted it **before** the claim reached three downstream documents. The campaign's ledger discipline is what made that cheap: because corrections are propagated deliberately rather than edited in silently, there was a moment at which to check.
