# B01 / A003 — biased-balancer depth-uniform GU' transfer

## Outcome

**AUTHOR-PROVED RESTRICTED ALL-DEPTH THEOREM; INDEPENDENT REVIEW PENDING.**

The preceding parity-tower theorem required a fresh fair character before
every activation.  This run removes that exact balance after the first
level.  Every later level may instead use a fresh genuine Boolean AND
balancer of mean $-1/2$.

For an arbitrary Boolean base $P$, define

\[
F_1=A(wP),\qquad F_k=A(B_kF_{k-1})\quad(k\ge2),
\]

where $w$ is a fresh fair character, $B_k=(-1,-1,-1,1)$ is a fresh
two-bit AND sign, and $A$ is half-activation by a fresh fair selector.
Then

\[
\boxed{G(F_d)\le2^{-d}G(P)+24.}
\]

Therefore

\[
G(P)\le aI(P)+bU(P),\quad 0\le b<1
\Longrightarrow
\boxed{G(F_d)\le(a+24)I(F_d)+bU(F_d).}
\]

The coefficient $b$ is preserved exactly; the extra cost is independent
of dimension, depth, and terminal rarity $2^{-d}$.

If $U(P)\le cI(P)$ for $c\ge72/35$, then the same endpoint propagates and

\[
H(F_d)\le(2+2c)I(F_d).
\]

Thus a base satisfying $U(P)\le2I(P)$ generates an all-depth biased class
with $H(F_d)\le(214/35)I(F_d)$.

## Mechanism

For the scalar $R$ in `PROOF.md`, the exact activation identity is

\[
G(A(q))=\frac12G(q)+R(\mathbb Eq)
+\sum_i\left[R(\mathbb Eq)-\mathbb E R(\mathbb E(q|x_i))\right].
\]

The obstruction is the logarithmic cusp of $R''$ at zero.  The tower
geometry isolates that cusp to at most four explicit coordinates per
level.  Every other restriction mean lies in $[1/4,3/4]$, so after
multiplication by the mean $-1/2$ of the AND balancer, all three scalar
arguments lie in $[-3/8,-1/8]$.  On this interval

\[
-4<R''<0,
\]

and the full safe-coordinate charge is at most $W_1/2$.

Crucially, the inherited level-one Fourier mass obeys

\[
W_1(F_k)=\frac1{16}W_1(F_{k-1})
+\frac18(\mathbb EF_{k-1})^2
+\frac14(1+\mathbb EF_{k-1}/2)^2\le\frac12.
\]

This yields the depth-uniform recurrence

\[
G(F_k)\le\frac12G(F_{k-1})+12,
\]

rather than repeatedly charging the full inherited influence.

## Precise class extension

- Previous theorem: exact fair-character balancing at every level.
- New theorem: only the first level is exactly balanced; every subsequent
  level uses a nonflat, biased two-bit Boolean balancer with mean $-1/2$.
- Parameters controlled uniformly: base dimension, tower depth, and
  terminal rarity.
- Bias currently covered: the fixed nonzero balancer bias $-1/2$.
- Still unpaid: arbitrary bias, biased outer selectors, overlap, variable
  reuse, and arbitrary coherent-core changes.

The class remains proper and is not restriction-closed.  This is not full
FEI.

## Validation

`CHECK_BIASED_TOWER.py` reconstructs truth tables, Walsh coefficients,
$U$, $I$, $G$, means, and level-one mass without using the analytic proof.
It passed:

- 298 bases, including exhaustive Boolean functions through three
  variables, rare point defects through seven variables, and deterministic
  generic samples;
- 879 direct tower constructions;
- 2,324 exact mean/influence/$U$/level-one recurrences;
- 2,637 GU' transfer checks; and
- 879 endpoint-transfer checks.

The maximum recurrence error was $4.441\times10^{-16}$.  The largest
observed value of $G(F_d)-2^{-d}G(P)$ was $3.64554$, far below the proved
constant $24$; this finite observation is not used to improve the theorem.

## Status and next unpaid step

Claim `B01_A003_BIASED_BALANCER_TOWER_GU_TRANSFER_v1` is author-proved and
requires independent A086/A094 review.  The next mathematical move is to
replace the fixed AND balancer by a one-parameter Boolean family, track the
constant as its mean approaches $\pm1$, and determine whether activation
energy supplies the missing uniform credit.  A result whose constant
diverges with the bias would remain a proper-class theorem, not universal
GU'.

Full FEI remains **OPEN**.

## Source pins

- owner control revision `2026-10-12.1`, source commit
  `40210272c19f43fed84f6a67653f9a04b0e11e28`;
- preceding parity-tower package, canonical commit
  `51ef0d5565bbb807ba99e38815cbda4c2e32fe73`;
- preceding proof blob
  `ccdb3ea1dd743c459e03a2206c0879c36ae6392f`.
