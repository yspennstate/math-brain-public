# B19 / A094 — independent review of the half-packet GU invariant

**Target:** `B05-A023-HALF-PACKET-INVARIANT-v1`  
**Producer:** fleet01/B05, canonical commit
`38fd5ddccc0e53d26f8cf68165fb3080257fe225`  
**Stable gap:** `GU-ASYMMETRY-MISMATCH`  
**Verdict:** **ACCEPTED AT DECLARED SCOPE; CONSTANT STRENGTHENED**  
**Universal GU / full FEI:** **OPEN**

## Audited candidate and implication

The target proves for every Boolean core, every bias, and `0<eta<=1`

\[
P(m,a)\le\frac12q(a^2),
\]

and uses it to contract `L+2Phi` under fresh fair activation.  Together
with disjoint-product subadditivity and structural restriction closure,
this yields a dimension- and depth-independent GU bound on the generated
fresh/disjoint class.

## Independent verdict

The proof is correct at that scope.

- The coupled scalar lemma includes `a->0`, `m->+-1`, and `r=m/a->infinity`;
  no compactness or finite-grid assumption is hidden.
- The identity for `Phi(Af)` retains the selector singleton, core
  singletons, and the full `W_1/2` correction.
- `L` is exactly additive under disjoint products and `Phi` is
  subadditive; no packet is reused across product factors.
- The generated class is genuinely restriction-closed.  Selector
  restrictions return the core or a constant, while data restrictions act
  recursively.
- The base signed characters pay their singleton potential because
  `c>4/ln2`.

The term “sharp half-packet” is not an optimality theorem: the proof
establishes the sufficient coefficient `1/2`, but does not prove it is the
smallest possible universal coefficient.

## Stronger constant

The producer separately bounded `W_1<=4J` and `q(J^2)<=2J/ln2`.  Retaining
their common selector parameter gives

\[
W_1+2q(J^2)
\le J\left(4(1-J)+4J\log_2(1/J)+\frac{4J}{\ln2}\right).
\]

The bracket has derivative `4(log2(1/J)-1)` and maximum
`4+2/ln2` at `J=1/2`.  Therefore

\[
c_\dagger=\frac{29}{2}+\frac2{\ln2}=17.3853900817\ldots
\]

suffices, improving the producer's
`29/2+4/ln2=20.2707801635...`.  On the same restriction-closed class,

\[
\boxed{G(F)\le\left(\frac{33}{2}+\frac2{\ln2}\right)I(F)
<19.385391I(F),}
\]

and

\[
\boxed{H(F)\le\left(35+\frac4{\ln2}\right)I(F)
<40.770781I(F).}
\]

This strengthening is reviewer-contributed and needs fresh A085/A090
review before registry acceptance.

## Independent reproduction

The independently written checker passed:

- 721,650 scalar half-packet tests and 83 explicit rare/boundary probes;
- 399,998 analytic derivative-sign evaluations;
- 1,000,000 selector-reserve evaluations, attaining its maximum at
  `J=1/2`;
- 534 Boolean cores, 2,670 activation/eta tests, and 534 independent
  singleton-identity tests;
- all 256 disjoint two-bit product pairs; and
- 180 generated construction nodes and 1,612 physical restrictions.

All tested contraction and generated-class residuals were nonpositive at
the recorded precision.  The acceptance rests on the analytic
reconstruction in `REVIEW_PROOF.md`, not the finite tests.

## Remaining gap

Fresh selectors and disjoint private blocks are still hypotheses.  A
shared/reused coordinate changes the singleton packet into an orbit packet;
the accepted overlap and rare-majority families rule out a memoryless
positive charge.  The next unpaid step is an augmented **signed orbit**
contraction retaining opening refunds and terminal `Theta`.

Model: Codex. Reasoning-effort metadata: UNKNOWN.

