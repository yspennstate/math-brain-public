# B07 / A031 — sharp payment of the Boolean root KL rows

**Status:** PROVED sharpening; fresh independent review required. Universal
GU and full FEI remain OPEN.

## Frozen candidate and prior bound

Primary packet: **A031**. Stable gap: `G-GU-SIGNED-KL`. Claim version:
`B07-A031-SHARP-ROOT-KL-v2`.

The exact Boolean restriction identity is

\[
\Delta_iU=B_i-\Gamma_i+K_i.
\]

The preceding theorem paid the empty upper-set row by
`sum_i K_i^(0) <= 4 I`; point defects showed only that the best coefficient
was at least `2/ln 2`.  This run freezes the scalar root term and closes
that constant gap.

## New theorem

Boolean convolution gives `C_(i,empty)=0`.  Writing
`a=fhat(empty)`, `d=fhat({i})`, and `m=a^2+d^2`,

\[
K_i^{(0)}=m\left[1-h_2\left(\frac{1+2ad/m}{2}\right)\right].
\]

The sharp scalar bound

\[
1-h_2\left(\frac{1+x}{2}\right)
\le\frac{1-\sqrt{1-x^2}}{\ln2}
\]

implies

\[
\boxed{
K_i^{(0)}\le\frac{2\min(a^2,d^2)}{\ln2}
\le\frac{2d^2}{\ln2}.}
\]

Therefore

\[
\boxed{
\sum_iK_i^{(0)}
\le\frac2{\ln2}\sum_i\widehat f(\{i\})^2
\le\frac2{\ln2}I(f).}
\]

The coefficient is optimal for this scalar component: point defects tend
to `2/ln 2 = 2.885390081777...`.

## Complete GU implication

Let `c0=2/ln 2`.  For any `a>=c0` and `0<=b<1`, it is now sufficient to
prove on tensor-prime Boolean functions that

\[
\boxed{
\sum_iK_i^{(+)}
\le(a-c_0)I+bU+\sum_i(\Gamma_i-B_i).}
\]

The exact tensor additivity of `G,I,U` then gives universal
`G<=aI+bU`, and the source-reviewed reduction gives

\[
H(f)\le\left(2+\frac{2a}{1-b}\right)I(f).
\]

This strictly shrinks the unpaid coefficient floor from `4` to the optimal
root value `2/ln 2`; it does not control any nonempty row.

## Verification

An independent checker reconstructs `U` from upper-set masses, computes
both physical children, and verifies the full identity
`Delta_i U=B_i-Gamma_i+K_i`.  It does not import the earlier checker.
It passed all 65,812 Boolean truth tables through dimension four with
834,966 assertions.  The maximum identity error was `4.441e-16`; the
maximum excess above the new sharp root bound was zero.  Point defects
through dimension 27 converge to the proved sharp constant.  The finite
checks are diagnostic; the scalar derivative proof is all-dimensional.

## Exact remaining gap

Only

\[
\sum_iK_i^{(+)}-sum_i(\Gamma_i-B_i)
\]

remains.  It must be paid once, with a fixed `b<1`, while retaining signed
upper-set correlations and avoiding repeated influence under physical
restriction.  A failed sharper estimate for that remainder would not
disprove GU or FEI.

Because this run materially sharpens the original theorem, it is a
contribution rather than an independent acceptance of v2.  Fresh review is
requested from A088/A090 and A094.

## Configuration and delivery

- Model: Codex; exact model and reasoning-effort metadata not exposed.
- Subagents: none.
- No scheduler, graph, deployment, email, publication, or protected-source action.

