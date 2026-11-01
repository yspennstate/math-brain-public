# C0108 source/status reconciliation — quadratic Littlewood–Offord

## Scope and snapshot

- Worker: `R7-03`, native ID `6aabe7be74008191b526b109ee4e9e80`.
- Start-of-run master captured before screening: `c179a4caf72591ba4568c1f230dcbbb18240cc9b`.
- Fresh master before this create-only write: `0449a083183e11969b51307489f6531251f47c39`.
- Shard check: `sum(ord(c) for c in "C0108") = 268`, and `268 mod 7 = 2`.
- No `operations/claims/C0108.md` existed at the fresh check. This file is a source/status screen, **not** an ownership claim or admission record.

## 1. Exact outside source

Canonical intake `C0108` points to:

- Terence Tao and Van Vu, *From the Littlewood-Offord problem to the Circular Law: universality of the spectral distribution of random matrices*.
- arXiv:0810.2994, first posted 16 October 2008; Bulletin of the AMS publication in 2009.
- Exact locator: Section 6, “Open problems,” combinatorics paragraph (the repository intake calls this p. 21).

The source considers a quadratic form

\[
Q(\xi)=\sum_{1\le i,j\le n}c_{ij}\xi_i\xi_j
\]

in independent Rademacher variables and, under the stated nonzero-coefficient hypothesis, conjectures the sharp point-anticoncentration bound

\[
\sup_z \Pr(Q(\xi)=z)=O(n^{-1/2}).
\]

The source itself identifies sharpness via

\[
Q_0(\xi)=(\xi_1+\cdots+\xi_n)^2.
\]

It then separately remarks that the situation for higher-degree polynomials is much less clear. The intake row compressed both the explicit quadratic conjecture and that broader higher-degree research direction into one prose statement; these scopes must not be conflated.

For hypercube-valued inputs, a quadratic polynomial has the unique multilinear representation

\[
Q(\xi)=c+\sum_i b_i\xi_i+\sum_{i<j}a_{ij}\xi_i\xi_j,
\]

using \(\xi_i^2=1\). In the usual symmetric quadratic-form convention the source’s nonzero off-diagonal coefficients mean \(a_{ij}\ne0\) for every \(i<j\). If one starts from an ordered nonsymmetric coefficient array, it must first be symmetrized; the relevant coefficient is the effective coefficient \(a_{ij}=c_{ij}+c_{ji}\). This normalization prevents a fake counterexample produced only by cancellation between two representations of the same monomial.

## 2. Recovered repository attempt

The prior intake attempt `C0108-A001` used a two-block decoupling of the quadratic form and then linear Littlewood–Offord bounds. Its own record identified the remaining loss: exceptional coefficient-sum degeneracies and the row union/conditioning step retained logarithmic or subpolynomial losses. That attempt was substantive but did not reach the exact \(O(n^{-1/2})\) endpoint.

No new proof should now be built on the assumption that this quadratic endpoint is still open without first reconciling later literature.

## 3. Dated current literature check

Bounded primary/current literature review, 2026-09-18 UTC:

1. Matthew Kwan and Lisa Sauermann, *Resolution of the quadratic Littlewood–Offord problem*, arXiv:2312.13826 (first posted 21 December 2023), now Compositio Mathematica 161(12) (2025), 3089–3139; Cambridge lists online publication on 30 March 2026, DOI `10.1112/S0010437X25102789`.
2. Their Theorem 1.1 states: if a degree-at-most-two polynomial in independent Rademacher variables **robustly depends on at least \(m\) variables**, meaning its value cannot be pinned down by fixing any \(m-1\) variables, then

\[
\sup_{z\in\mathbb R}\Pr(Q(\xi)=z)\le \frac{C}{\sqrt m}
\]

for an absolute constant \(C\).
3. Current higher-degree follow-up work remains structurally nontrivial rather than supplying a blanket resolution of the source’s broad “higher degrees” direction. For example, Jin–Kwan–Sauermann–Wang (arXiv:2505.23335, 2025) studies algebraic structure in the polynomial Littlewood–Offord problem, and Grebennikov–Kwan (arXiv:2505.24699, 2025) proves the desired robust \(O(m^{-1/2})\) form for bounded Chow rank among other cases. These are evidence that the higher-degree programme should not be silently marked closed.

This status conclusion rests on a positive source-matching theorem, not on a negative search.

## 4. B2 — attack the negation: the exponent cannot be improved

Take

\[
Q_0(\xi)=\left(\sum_{i=1}^n\xi_i\right)^2
=n+2\sum_{i<j}\xi_i\xi_j.
\]

Every off-diagonal quadratic coefficient is nonzero. For even \(n\),

\[
\Pr(Q_0=0)
=2^{-n}\binom{n}{n/2}
\sim \sqrt{\frac{2}{\pi n}}.
\]

For odd \(n\),

\[
\Pr(Q_0=1)
=2\,2^{-n}\binom{n}{(n-1)/2}
=\Theta(n^{-1/2}).
\]

Therefore no uniform source theorem of order \(o(n^{-1/2})\) is possible. This is an exact obstruction to any attempted stronger endpoint and agrees with the source’s own sharpness example.

**B2 outcome:** the source exponent \(1/2\) is the correct endpoint; there is no hidden room to reinterpret the old conjecture as asking for a stronger power.

## 5. B6 — deform the solved robust-dependence theorem to the source hypothesis

### Lemma

Assume the unique multilinear form of \(Q\) has \(a_{ij}\ne0\) for all \(i<j\). Then \(Q(\xi)\) robustly depends on at least \(n-1\) variables in the sense of Kwan–Sauermann.

### Proof

Fix any set of at most \(n-2\) variables to arbitrary signs. Choose two unfixed coordinates \(u\ne v\). After all fixed coordinates are substituted, the resulting function of the remaining variables still contains the Fourier/Walsh monomial

\[
a_{uv}\xi_u\xi_v
\]

with coefficient \(a_{uv}\ne0\): substitution in other monomials cannot alter the coefficient of the distinct monomial \(\xi_u\xi_v\). A constant function on the remaining hypercube has all nonconstant Walsh coefficients equal to zero. Hence the restricted polynomial is not constant. Thus no assignment of any \(n-2\) variables pins down the value of \(Q\). This is precisely robust dependence on at least \(m=n-1\) variables. \(\square\)

Applying Kwan–Sauermann Theorem 1.1 gives

\[
\boxed{
\sup_z\Pr(Q(\xi)=z)
\le \frac{C}{\sqrt{n-1}}
=O(n^{-1/2}).
}
\]

This is exactly the explicit Tao–Vu quadratic endpoint.

**B6 outcome:** the 2023/2025 Kwan–Sauermann theorem strictly contains the source hypothesis and closes the source’s explicit quadratic conjecture.

## 6. B30 — localize the gluing failure in the canonical intake

The only remaining ambiguity is bookkeeping/scope, not the quadratic mathematics.

- **Explicit source endpoint:** the all-nonzero-coefficient quadratic conjecture \(O(n^{-1/2})\). This is **KNOWN / RESOLVED IN LITERATURE** by Kwan–Sauermann.
- **Broader sentence after it:** “the situation with higher degrees is much less clear.” This is a research direction, not the same fixed quadratic closure criterion. Current 2025 work still treats substantial higher-degree polynomial Littlewood–Offord structure questions.

The intake row `C0108` compressed these into one candidate. It is therefore unsafe either (i) to keep presenting the quadratic endpoint as open, or (ii) to declare every possible higher-degree version solved. The source-faithful reconciliation is:

```text
C0108 quadratic endpoint: KNOWN / RESOLVED_IN_LITERATURE_2023_2025;
residual general-degree direction: BROAD/HARD, not a fixed CLOSABLE endpoint for R7-03.
```

No invented replacement ID is created.

**B30 outcome:** the admission gluing failure is isolated exactly: the closable-looking quadratic clause is already solved, while the unsolved residue is too broad to be lawfully narrowed into a new R7-03 assignment.

## 7. Admission consequence

`C0108` passes the shard arithmetic but fails R7-03 admission:

1. the precise quadratic source endpoint is already known;
2. the surviving higher-degree direction is not an honest fixed CLOSABLE source target;
3. no canonical claim should be created for R7-03.

R7-03 therefore remains `PENDING_ADMISSION` rather than duplicating Kwan–Sauermann or manufacturing a narrower conjecture.

## 8. Metric

No successor target is admitted, so no target-specific metric or stagnation counter starts.

```text
metric: admission_baseline
before: UNKNOWN/UNMEASURED
after:  UNKNOWN/UNMEASURED
movement: none
stagnation count: N/A (no admitted target)
```

This screen advances the lawful source-status cursor; it is not a theorem-closure claim by R7-03.