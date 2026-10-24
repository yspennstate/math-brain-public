# RS-2026-CL-A -> P08/P09 handoff — excess-contraction / diagram suppression

**Timestamp:** 2026-09-20T14:48:00Z  
**Ownership:** RS-2026-CL-A retains ownership of the low-degree source claim. This file shares only reusable analytic lemmas with P08 (Gaussian phase retrieval) and P09 (Gaussian tensor bounds). Do not relabel either role’s source problem or overwrite peer reports.

Primary RS report: `runs/2026-09-20/2026-09-20T14-48-00Z__report.md`.

## 1. Exact finite-state contraction lemma

Let `(S,mu)` be finite with `mu_* = min_s mu(s)>0`. Let `W:S x S -> R` be symmetric and let the integral operator

`(T_W f)(s)=sum_t mu(t)W(s,t)f(t)`

have operator norm `Lambda`.

For a connected graph `F`, write

`t(F,W)=E prod_{uv in E(F)} W(sigma_u,sigma_v)`,

with iid `sigma_v~mu`.

If `F` has minimum degree at least two, is not a cycle, has `e` edges and `v` vertices, and has excess

`r=e-v>=1`,

then

`|t(F,W)| <= Lambda^e mu_*^{-3r}`.                         (1.1)

Proof: suppress every maximal degree-two path. The resulting multigraph has at most `2r` branch vertices and `3r` branch edges. Conjugating by `diag(sqrt(mu))` gives for every path length `ell`

`|W^{(ell)}(s,t)| <= Lambda^ell / sqrt(mu(s)mu(t)) <= Lambda^ell/mu_*`.

Multiplying at most `3r` path-kernel losses proves (1.1).

The important structural point is that **long chains do not accumulate a separate combinatorial loss**. Every loss beyond the base factor `Lambda^e` is charged only to branch excess `r`.

## 2. Abstract diagram version

The same argument is basis-independent.

Suppose a connected contraction diagram has:

- `e` propagation edges;
- `v` internal diagram vertices;
- every degree-two chain represented by repeated application of an operator `A` with `||A||<=Lambda`;
- every endpoint evaluation / branch contraction bounded by a constant `K` after the chain is compressed.

If all nontrivial internal vertices have degree at least two and the diagram is not a pure cycle, put `r=e-v`. Suppressing degree-two chains leaves at most `2r` branch vertices and `3r` compressed chain edges. Consequently one obtains a bound of the schematic form

`|Amp(F)| <= Lambda^e K^{O(r)}`.                           (2.1)

The exact exponent on `K` depends on how many endpoint/branch norms are charged by the model, but the **number of charged objects is O(r), not O(e)**.

This is the part potentially reusable in Gaussian/Wick and tensor-chaos calculations.

## 3. Gaussian/Wick use

For a Gaussian chaos or Gaussian-process moment expansion, pairwise contractions often generate long chains of covariance or resolvent operators. If the normalized covariance propagation operator has norm at most `Lambda`, then every maximal degree-two Wick chain can be collapsed before applying Cauchy–Schwarz or Schatten bounds.

A useful proof template is therefore:

1. encode the moment as a contraction graph;
2. suppress all degree-two chains first;
3. use operator norm only along those chains;
4. pay dimension/Schatten/Christoffel losses only at the residual branch tensors;
5. enumerate diagrams by excess `r` rather than total order `e`.

This can prevent a dimension factor from being paid once per Wick edge when it should only be paid once per branching event.

## 4. P09 tensor implication

For P09’s unresolved tensor type-2 dimension loss, the lemma suggests separating two sources of loss:

- chain propagation, which should be controlled by the relevant injective/operator norm and need not cost extra powers of dimension;
- genuine branching contractions, whose count is bounded by the excess.

If P09 can show a branch tensor bound `K_d` and a chain bound `Lambda<=1`, then a diagram family with excess `r` contributes at most roughly `K_d^{C r}` before enumeration. Summing by excess may be materially sharper than bounding every tensor contraction independently.

This is not itself a solution to P09; it is a reusable bookkeeping lemma.

## 5. P08 phase-retrieval implication

For P08, correlated Gaussian minors or determinant expansions can also contain repeated covariance-propagation chains. If a minor-moment or bad-event expansion admits a diagram representation with a stable covariance operator, suppressing degree-two chains before applying determinant/Hadamard estimates may isolate the truly unstable branch configurations.

Again, no claim is made that the current P08 bottleneck already satisfies the needed uniform branch bound.

## 6. Limitation

The finite-state inequality (1.1) is proved exactly because point-evaluation of a finite kernel is controlled by `mu_*`. Infinite-dimensional Gaussian/Hermite systems do not have that pointwise finite-state bound automatically. In a Gaussian setting, the abstract version (2.1) requires a separately proved endpoint/branch contraction estimate, e.g. via Hilbert–Schmidt/Schatten norm, hypercontractivity, or a model-specific leverage bound.

So the transferable result is the **degree-two-chain suppression plus O(excess) branch count**, not an unjustified finite-state pointwise bound.