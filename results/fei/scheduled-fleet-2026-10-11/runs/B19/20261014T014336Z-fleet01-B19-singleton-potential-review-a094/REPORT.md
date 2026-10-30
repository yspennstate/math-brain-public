# B19 / A094 — independent review of B05 singleton-potential amortization

## Verdict

**THE FORMAL GU' TRANSFER THEOREM IS INDEPENDENTLY ACCEPTED.  A023 IS NOT YET COMPLETE.**

I reconstructed the proof of `B05-A023-SINGLETON-POTENTIAL-GU-v1` from the
original artifact at canonical commit
`b32a2ebfb4250805a722e9ab2839efcb2dfbe1f4`.  No repair is needed for the
formal theorem:

\[
G(F)\le\left(\max\{a,5\}+\frac8{\ln2(1-\ln2)}\right)I(F)+bU(F),
\qquad 0\le b<1,
\]

on the restriction closure generated from a restriction-closed base GU'
class by fresh fair half-activation and finite disjoint products of signed
point defects.  In particular the constants/parities base gives

\[
G(F)\le42.6126911532792\,I(F).
\]

The constant is uniform in dimension, syntax depth, defect ranks, sign
pattern, number of disjoint defect factors, and physical restrictions.

## Independent proof reconstruction

Define

\[
\phi(h)=2h^2\left(\log_2(1/h)+1/\ln2\right),\qquad
\Phi(f)=\sum_i\phi(|\widehat f(\{i\})|).
\]

The following four steps check.

1. From the displayed formula for `R''`,
   `-R''(t)<=2 log_2(1/|t|)`.  The triangular second-difference kernel then
   proves globally
   \[
   R(m)-\frac{R(m-h)+R(m+h)}2\le\phi(h).
   \]
   The endpoint and zero cases follow by continuity.

2. For Boolean `f`, `|fhat({i})|<=Inf_i(f)`.  Since `phi(h)<=Mh`,
   `M=2/ln2`, this gives `Phi(f)<=M I(f)`.  Under fresh activation,
   \[
   G(A(q))\le\tfrac12G(q)+R(Eq)+\Phi(q),
   \quad
   \Phi(A(q))\le\rho\Phi(q)+MJ,
   \]
   where `J=(1-Eq)/2` and `rho=(1+ln2)/4`.

3. With `lambda=4/(1-ln2)`,
   `1+lambda*rho-lambda/2=0`.  Consequently the current midpoint charge is
   funded by the decrease of the stored potential.  The remaining root term
   obeys `(1-b)R(t)<=5J`.

4. On disjoint variables, `G,U,I` are additive and
   `Phi(Bh)<=Phi(h)+M I(B)`.  The point-defect estimate `G(B)<=5I(B)` then
   propagates
   \[
   G+\lambda\Phi\le A_*I+bU,
   \quad A_*=\max\{a,5\}+\lambda M,
   \]
   through both products and activations.  The grammar is stable under every
   coordinate restriction, so the declared class really is
   restriction-closed.

## Required scope corrections

Two phrases must not be upgraded beyond the formal theorem.

- “Independent of activation probabilities” means independent of the dyadic
  rarity produced by arbitrarily many **fair half-activations**.  The proof
  does not cover a biased selector parameter.
- The potential gives a valid algebraic, generation-step amortization.  It
  does not yet provide A023's requested finite adaptive physical stopping
  rule or directly bound the complete expected
  `mu[log_2(1/mu)-D_2(nu||q)]` restriction-tree ledger plus terminal entropy.
  The same singleton account retains a contracted balance at descendants;
  the invariant proves no overspending, but it is not literally a
  first-physical-revelation stopping rule.

Accordingly the restricted GU' theorem is accepted, while packet A023 remains
in progress.  The result should be routed as a proved restricted theorem to
A064/A095, not recorded as completion of the universal rare-refund packet.

## Earlier positive-tower correction

The correction is also accepted.  For constant seed, the first balanced cap
has influence one, and after a positive rank-`r` defect step

\[
I(F_2)=\frac34+\frac{r+1/2}{2^r}<1\qquad(r\ge6).
\]

Thus the earlier implication using `I(F_d)>=1` is invalid.  Its additive
`G` recurrence and independent endpoint `U` theorem are unaffected.  The new
potential invariant supplies a valid replacement GU' transfer.

## Independent finite reproduction

`CHECK.py` independently passed:

- 600,256 scalar and point-defect checks;
- all 278 Boolean functions through three inputs;
- 3,892 activation/product identity checks;
- 834 invariant checks;
- 1,608 physical restriction checks; and
- 95 exact rational correction witnesses (`r=6,...,100`).

The maximum reconstructed activation-influence error was zero at displayed
precision.  These checks support, but do not replace, the analytic proof.

## Remaining universal gap

The immediate unpaid obligation is to convert the potential telescope into
the exact A023 physical restriction-tree stopping ledger.  After that, the
structural frontier is still shared-variable overlap: neither exact product
additivity nor `Phi(Bh)<=Phi(h)+MI(B)` survives automatically when a physical
coordinate is reused.  Full FEI remains **OPEN**.

