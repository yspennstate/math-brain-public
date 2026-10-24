# E0092 paper package: deterministic Wilson generators

## Status

**PARTIAL / closure candidate. `E_WILSON_EXPLICIT = 0`.**

This folder assembles the current strongest E0092 candidate into one source-matching package. The package itself does **not** move the frozen metric. Repository closure still requires:

1. an actual P26 end-to-end PASS;
2. a distinct OTHER-track end-to-end PASS;
3. final source/prior-art/`explicit` reconciliation;
4. only then, coordinator/root-ledger reconciliation.

As of the package assembly run on 2026-09-18, repository searches did not find either required E0092 PASS audit. Search absence is not an audit.

## Outside source

Persi Diaconis, *Some things we've learned (about Markov chain Monte Carlo)*, Bernoulli 19 (2013), Section 5 Question 1 following Example 6, arXiv:1309.7754v1, DOI 10.3150/12-BEJSP09.

Literal question: item 2 of Wilson's theorem holds for almost all choices `V_1,...,V_N`; can an explicit set be found, for example when `N=2n`?

Wilson source: David B. Wilson, *Random random walks on Z_2^d*, Probability Theory and Related Fields 108 (1997), 441-457, DOI 10.1007/s004400050116.

For `N=2n`, Wilson's threshold is

```text
T_W(n,2n) = n * log(1/(1-2*H_2^{-1}(1/2))) ~= 0.24853 n.
```

Diaconis's displayed formula has a typographical inconsistency with the numerical value; this package follows Wilson's theorem and Diaconis's stated numerical constant.

## Source-clause to proof map

| Source/closure clause | Package location | Current state |
|---|---|---|
| One deterministic family, not `almost all` | `main.tex`, Sections 2-3; `ALGORITHM.md` | Candidate proof complete |
| Exactly `N=2n` labeled generators | `main.tex`, Theorem 1 and Sections 2, 6 | Candidate proof complete |
| Family chosen before epsilon | `ALGORITHM.md`; `main.tex`, Proposition 4 | Candidate proof complete |
| Wilson sharp threshold | `main.tex`, Sections 1 and 6 | Candidate proof complete |
| Every fixed epsilon, sufficiently large n | `main.tex`, Theorem 1 and Section 6 | Candidate proof complete |
| All integer times above the threshold | `main.tex`, Sections 6-7 | Candidate proof complete |
| Eventual irreducibility | `main.tex`, Section 7 | Deduced from TV `<1/2` |
| Eventual aperiodicity | `main.tex`, Section 7 | Deduced from TV `<1/2` |
| Exact finite construction algorithm | `ALGORITHM.md`; `main.tex`, Lemma 3 / Proposition 4 | Candidate proof complete |
| Collision normalization cross-check | `main.tex`, Sections 2 and 4 | Collision and Fourier forms agree |
| Known-vs-candidate-new boundary | `main.tex`, Sections 4 and 8 | Explicitly stated |
| P26 independent audit | external to this folder | **MISSING** |
| Distinct OTHER audit | external to this folder | **MISSING** |
| Final publication novelty/explicitness adjudication | external to this folder | **UNVERIFIED** |

## Files

- `main.tex` — self-contained theorem statement and proof, with prior-art/limitation section.
- `ALGORITHM.md` — canonical exact pseudocode/specification: seed indexing, bit order, tie rule, exact conditional expectation formula, and inherited evidence pointers.

No redundant checker was manufactured for this package run. Existing exact and formal evidence is referenced below.

## Reused exact/formal evidence

Historical E0092 support files:

- `prob1000_lean_20260908/ultracode_20260909/E0092/U_E0092.lean`
  - formalizes the collision-to-total-variation inequality `TV <= sqrt(Q)/2`;
  - this is a local algebraic core, not a formalization of the source theorem.
- `prob1000_lean_20260908/ultracode_20260909/E0092/check_identity.py`
  - checks on a small instance that the generator walk is the linear image of the `2n`-cube walk;
  - checks the collision formula in two forms and the shell TV bound.
- `prob1000_lean_20260908/ultracode_20260909/E0092/check_T.py`
  - historical Wilson-threshold numerical check.
- `block_search.py`, `check_block_lemma.py`, `check_product.py`
  - belong to the older block-Toeplitz route; retained for history but not required by the final global-Toeplitz proof.

The current global conditional-expectation construction is proved symbolically in `main.tex`; it has not been independently reimplemented or formally verified end to end.

## B19: canonical algorithm decisions

To prevent implementation ambiguity, `ALGORITHM.md` fixes:

1. Toeplitz seed indices `q=-(n-1),...,2n-1`;
2. row/column convention `M[r,c]=s[c-r]`;
3. ascending seed-bit decision order;
4. exact rational formula for every prefix conditional expectation;
5. Gaussian elimination over `F_2` for affine-system ranks/consistency;
6. tie rule `0` whenever the two conditional expectations are equal;
7. output order equal to matrix column order.

Therefore two exact implementations following the specification must output the same seed and the same labeled generator list.

## B25: shell energy counted twice

The package uses the same quantity in two independently normalized forms:

```text
Q_w(M) = 2^n * P(MZ=MZ') - 1
       = sum_{a != 0} (K_w(wt(M^T a))/binom(2n,w))^2.
```

The first form drives the Toeplitz conditional-expectation construction. The second is Parseval/Krawtchouk fixed-sphere smoothing. Their equality is written out in `main.tex`, Section 4, and is an important normalization cross-check.

The Fourier/Krawtchouk smoothing mechanism and the random-code entropy threshold are prior art; the package does not claim them as novel.

## B20: adversarial failure check performed during assembly

The package proof was checked specifically for these failure modes:

- **epsilon leakage:** the algorithm takes only `n`; epsilon appears only after the family is fixed;
- **strict-threshold integer issue:** the proof uses `k_0=floor((1+epsilon)T_W)+1`, the smallest integer strictly above the target threshold;
- **threshold factor:** for `N=2n`, the cube-coordinate parity mean uses `1-2/N = 1-1/n`, giving exactly Wilson's `n*t_*` scale;
- **nonuniform shell bound:** all `w=0,...,2n` are simultaneously controlled by the potential; only central shells are needed for mixing;
- **all-later-times scope:** handled by convolution contraction against uniform measure;
- **rank assumption:** full row rank is not assumed in the construction and is deduced eventually because a rank-deficient walk stays at TV at least `1/2`;
- **period assumption:** aperiodicity is similarly deduced; an irreducible period-two walk stays in one index-two coset at each time and has TV at least `1/2`;
- **small-case algebraic pattern:** not used; the earlier projection pattern fails at block size 9.

No fatal mathematical gap was found in this assembly self-check. This is still a worker self-check, not an independent audit.

## Dated prior-art/source check: 2026-09-18

Fresh web checks on 2026-09-18 found:

- Diaconis arXiv:1309.7754 still exposes the 2013 source and the same open-question context.
- Debris-Alazard, Ducas, Resch, Tillich, arXiv:2205.10552 / IEEE TIT 2023, explicitly studies spherically uniform noise and gives the optimal random-code smoothing threshold. This covers the Fourier/Krawtchouk/fixed-sphere mechanism at the heart of the analytic estimate.
- Pathegama-Barg, arXiv:2308.11009 / Entropy 2023, states explicit code families for Bernoulli and ball noise, not on the inspected statements the exact fixed-sphere deterministic family used here.
- Bounded searches for deterministic/explicit fixed-sphere smoothing and later work explicitly answering the Diaconis/Wilson `N=2n` question did not locate a matching source-level result.

These search misses are **bounded negative evidence only** and are not a novelty certificate.

## Explicitness caveat

The literal Diaconis question says `explicit set` but does not state polynomial time, closed formula, or algebraic-family requirements. The construction here is a deterministic finite algorithm using exact conditional expectations; a naive implementation is exponential-time.

This package therefore makes the narrow source-reading claim that the algorithm is a plausible literal explicit construction. It does **not** declare the intended semantic question settled. Both independent audits should explicitly say whether they accept this interpretation or require a stronger notion.

## Frozen metric

```yaml
metric: E_WILSON_EXPLICIT
value: 0
status: PARTIAL
candidate_source_theorem: packaged
p26_audit: missing
second_independent_audit: missing
publication_novelty: unverified
source_explicitness_intent: unresolved_pending_independent_audit
```