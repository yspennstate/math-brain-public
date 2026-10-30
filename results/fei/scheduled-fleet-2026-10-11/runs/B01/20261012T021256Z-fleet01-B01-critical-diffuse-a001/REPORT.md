# B01 / A001: critical–diffuse normal form

## Status

**AUTHOR-PROVED, PENDING INDEPENDENT A086/A094 REVIEW. Full FEI remains OPEN.**

This run advances the restriction-critical tensor-prime reduction from the
preceding A001 bundle. It proves that any high-ratio member of that residual
class must be exponentially diffuse in every coordinate. This is a genuine
structural narrowing and a restricted FEI endpoint; it is not a universal FEI
bound.

## Frozen objective and prior state

- Primary packet: **A001** (quantifier audit).
- Stable gap: **G-R-SELECT**.
- Attempt: **A001-CRITICAL-DIFFUSE-2**.
- Objective: starting from the source-pinned A001 critical-prime descent and
  the A003 exact restriction split, derive the strongest dimension-independent
  structural consequence of restriction-criticality, with every quantifier
  explicit, and test it against the mandatory sparse/prime controls.
- Prior status: A001 v1 proved, pending review, that every nonconstant Boolean
  function has a restriction-critical tensor-prime restriction descendant of
  no smaller Fourier entropy/influence ratio. The first unsupported line was
  still a finite universal good-coordinate bound on that class.

## Exact new theorem

Let (h:\{-1,1\}^m\to\{-1,1\}) be nonconstant, let
(R(h)=H(h)/I(h)), and put (alpha_i=I_i(h)). For a relevant coordinate,
write

\[
\Delta_iH=H(h)-\frac{H(h_{i=1})+H(h_{i=-1})}{2}.
\]

Assume (h) is **restriction-critical**, meaning
(Delta_iH\ge R(h)I_i(h)) for every relevant physical coordinate (i).
Then, for each such (i),

\[
R(h)\le G(\alpha_i):=
\frac{h_2(\alpha_i)}{\alpha_i}+
\frac{2}{\ln2}\frac{\min\{\alpha_i,1-\alpha_i\}}{\alpha_i}. \tag{1}
\]

Set (R_0=2+2/\ln2=4.8853900817\ldots). On (0<\alpha\le1/2),
(G) is strictly decreasing and maps that interval onto
([R_0,\infty)). Let (kappa) be its inverse. If (R(h)>R_0), then

\[
\boxed{\max_i I_i(h)\le\kappa(R(h))\le e^3 2^{-R(h)}.} \tag{2}
\]

The quantifiers in (1)–(2) are: every finite dimension, every genuine Boolean
sign, every restriction-critical nonconstant function, and every relevant
coordinate. No asymptotic or realizability assumption is used.

### Proof

For the spectral random set (S\sim\widehat h(S)^2), the A003 exact split is

\[
\Delta_iH=E_i+J_i,
\quad E_i=H(\mathbf1_{\{i\in S\}}\mid S\setminus\{i\}),
\]

where (J_i) is the Jensen–Shannon term of the two restriction spectra. The
two source-proved pointwise bounds are

\[
E_i\le h_2(\alpha_i),\qquad
J_i\le\frac2{\ln2}\min\{\alpha_i,1-\alpha_i\}.
\]

Combining these with criticality gives (1). For (0<\alpha\le1/2),

\[
\frac{d}{d\alpha}\frac{h_2(\alpha)}{\alpha}
=\frac{\log_2(1-\alpha)}{\alpha^2}<0.
\]

For (alpha\ge1/2), (G(\alpha)\le1/\alpha+2/\ln2\le R_0). Thus
(R>R_0) forces every (alpha_i<1/2) and
(alpha_i\le\kappa(R)). Finally,

\[
\frac{h_2(\alpha)}\alpha
=\log_2\frac1\alpha+
\frac{1-\alpha}{\alpha}\log_2\frac1{1-\alpha}
\le\log_2\frac1\alpha+\frac1{\ln2},
\]

using (-\ln(1-\alpha)\le\alpha/(1-\alpha)). Hence
(R\le G(\alpha_i)\le\log_2(1/\alpha_i)+3/\ln2), which rearranges to
(2).

## Consequences

### Critical–prime counterexample normal form

Combine (2) with the preceding A001 descent. For every nonconstant Boolean
(f) with (R(f)>R_0), there exists a restriction descendant (h),
tensor-prime after dummy variables and constant factors are deleted, such that

\[
R(h)\ge R(f),\qquad
\max_i I_i(h)\le\kappa(R(h))\le e^3 2^{-R(f)}.
\]

Thus, if FEI is false, a genuine Boolean counterfamily exists inside the much
narrower class

\[
\text{restriction-critical} + \text{tensor-prime} +
\text{all influences exponentially small in }H/I.
\]

This is an exact implication, not a counterexample construction.

### Restricted FEI endpoint

For every fixed (0<\delta\le1/2), every restriction-critical Boolean (h)
with (max_i I_i(h)\ge\delta) satisfies

\[
H(h)\le G(\delta)I(h).
\]

This is dimension-independent, but the fixed lower bound on one influence is a
real hypothesis. The low-influence embedding from A002 prevents treating it as
a universal endpoint.

### Relevant-dimension lower bound

For an (m)-variable Boolean function, each positive influence is a multiple
of (2^{1-m}). Hence every high-ratio critical (h) above satisfies

\[
m\ge R(h)+1-\frac3{\ln2}.
\]

This is weaker than FEI; it merely records the granularity forced by the
exponential diffusion estimate.

## Mandatory obstruction controls

- **Sparse one-point defects / rare restrictions:** the genuine prime gates
  (q_n) are restriction-critical, but (R(q_n)\to4<R_0). The new high-ratio
  clause correctly does not fire. Their rare logarithms remain visible.
- **Addressing and multiplexers:** their known bounded-ratio behavior is
  compatible with (1); the theorem does not charge selector entropy locally
  or re-propose the established fresh-selector endpoint.
- **Bent selector control:** a relevant coordinate near influence (1/2) in a
  restriction-critical function forces (R\le R_0), consistent with the
  accepted bent-selector obstruction.
- **Exact tensors:** removed by the source-pinned A001 factor descent. Near
  tensors are not removed and remain a live test.
- **Parity-zero erasure:** parity has zero spectral entropy and creates no
  contradiction. No claim is made that every coordinate supplies positive
  entropy decrement.
- **Shared-variable interference / activation equivalence:** not resolved.
  The proof uses only the exact single-coordinate restriction split and makes
  no composition transfer claim.
- **Boolean realizability:** every structural conclusion is stated only for
  genuine Boolean functions; the scalar envelope is not asserted sufficient
  for realizability.

## Validation

Command: `python3 verify_critical_diffuse.py`

The checker used exact `Fraction` Walsh masses and influences and a 90-digit
`Decimal` context for logarithms. It performed 36,890 assertions:

- exhaustive truth tables through (n=3);
- a deterministic, no-randomness sample of 4,105 (n=4) truth tables
  (4,096 multiplicative-permutation masks plus sparse/prime controls; duplicate
  masks are removed);
- 9,999 scalar envelope points on ((0,1/2));
- genuine one-point defects (q_n) for (2\le n\le60).

Result: **PASS**. There were no actual tested critical functions above
(R_0), so the all-ratio conclusion is certified by the analytic proof, not
by finite enumeration. The scalar pilot corroborates the monotonicity and
explicit inversion. The first attempt at exhaustive (n=4) checking was
terminated after exceeding the bounded 60-second pilot; it produced no result
and is not counted as evidence.

## Source pins and literature scope

- A001 critical-prime descent: `yspennstate/math-open-problems` commit
  `c8c6b995401f238e67317ab4d5b44aea6173a845`, run
  `20261012T011119Z-fleet01-B01-quantifier-audit-a001`, REPORT blob
  `662411dfae5b8d91d0b07e449c59274537492500`.
- A003 exact split and (2/\ln2) Jensen–Shannon cap:
  `yspennstate/math-open-problems` commit
  `87f7c6267e56e7a0eb5b8dfd572a6eaaecae6907`, run
  `20261011T210729Z-fleet01-B01-minimal-target-a003`.
- Owner-approved threshold manuscript: `yspennstate/fourier-entropy-threshold-functions`
  commit `b38ba0ab49618ccbe6d1518a34c141dcec9f247c`.

No literature-priority or novelty claim is made. This is a source-bound
campaign deduction from the two pinned identities.

## Exact remaining gap and next action

The tracked gap moves from an unrestricted critical-prime good-coordinate
problem to the following precise residual problem:

> Bound (R(h)) uniformly over genuine Boolean (h) that are simultaneously
> restriction-critical, tensor-prime, and satisfy
> (max_i I_i(h)\le e^3 2^{-R(h)}).

The theorem shows that every putative unbounded-ratio sequence must enter this
exponentially diffuse regime; it supplies no contradiction there. A next
attack should combine the diffuse bound with a genuinely nonlocal spectral
or restriction payment that survives rare activations, near tensors, and
shared-variable interference. Independent A086/A094 reconstruction is needed
before registry acceptance.

## Delivery distinctions

- Configuration: Codex model as exposed by this run; reasoning-effort selector
  not exposed; no subagents.
- Natural execution: one A001 attempt; no scheduler or graph mutation.
- Mathematical result: author-proved pending independent review.
- Independent review: not yet performed.
- Native Brain ingestion: not claimed.
- Full FEI: **OPEN**.
