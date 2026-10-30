# B01 / A003 — balanced half-activation logarithmic credit

**Run:** `20261013T170839Z-fleet01-B01-balanced-activation-credit-a003`  
**Packet:** A003, minimal target formulation  
**Stable gap:** `GU-ASYMMETRY-MISMATCH`  
**Status:** author-proved all-parameter one-step theorem, pending A086/A094
independent review.  Full FEI remains **OPEN**.

## Result

The previous mechanism had isolated a first-level logarithmic charge on odd
majority and showed that the scalar slack `H+I-G` cannot be passed through
fresh activation with bounded loss.  This run proves the exact general
pattern for **every balanced Boolean core**, not only majority.

For a balanced `g:{-1,1}^n->{-1,1}`, let

\[
 F(+1,x)=1,\qquad F(-1,x)=g(x),
\]

put `a_j=hat g({j})`,

\[
 L_1=\sum_ja_j^2\log_2(1/a_j^2),\qquad W_1=\sum_ja_j^2,
\]

and set `S=H+I-G`.  The complete signed activation charge is

\[
 S(F)-\tfrac12S(g)=\tfrac32-\tfrac12L_1-\sum_jD(a_j),
\]

where the explicit even scalar function `D` is given in `PROOF.md`.  It
satisfies

\[
 D(a)\le c_0a^2,
 \qquad c_0=\frac9{8\ln2}-\frac12=1.1230319210\ldots.
\]

Boolean physical-input accounting gives

\[
 L_1\le\frac{2}{e\ln2}I(g),\qquad W_1\le I(g).
\]

Therefore the rare logarithm has a dimension-independent one-step payment:

\[
 \boxed{G(F)\le\tfrac12G(g)+1+c_1I(g)},
 \qquad
 c_1=\frac9{8\ln2}-\frac12+\frac1{e\ln2}
 =1.6537697664\ldots.
\]

In particular, if `G(g)<=K I(g)`, then

\[
 G(F)\le(K+3.3075395329)I(F).
\]

This is an all-dimensions theorem with no dependence on address count or
core dimension.  It strictly extends the prior majority calculation to all
balanced cores under one fresh half-activation.

## Why it matters

The earlier majority asymptotic exposed an unpaid
`(1/2)L_1(Maj_n)=(1/pi)log_2 n+O(1)` term.  The new proof shows that this is
the exact universal first-level term for a balanced activation, and then
pays it by actual physical influence using
`|hat g({j})|<=Inf_j(g)`.  Thus the logarithm itself is no longer a
dimension-dependent obstruction at one node.

The result also identifies the precise hierarchy obstruction.  Applying the
one-step estimate independently at several ancestors can recharge the same
descendant influence.  Nothing here proves a single-use ownership telescope
for changing coherent cores, so universal GU and full FEI remain open.

## Exact class extension

- Previous proved scope: the logarithmic activation surcharge was derived
  asymptotically for balanced odd majority.
- New proved scope: the exact signed charge and a uniform influence payment
  hold for every balanced Boolean core in every finite dimension.
- Previous bound: `G(F)-G(g)/2=(1/pi)log_2 n+O(1)` on majority.
- New bound: `G(F)-G(g)/2<=1+c_1 I(g)` with absolute `c_1`, on all balanced
  cores.
- Parameter dependence removed: dimension, Fourier support size, and the
  number of nonzero singleton coefficients.
- Still unpaid: depth and overlap of repeated ownership in an arbitrary
  physical restriction hierarchy.

## Proof and validation

`PROOF.md` derives the exact identity from the source-pinned activation
formula, proves the sharp scalar estimate by differentiating `D`, and pays
`L_1` with the physical derivative inequality.

`CHECK_TWO_COMPONENT.py` independently reconstructs `H,I,G,L_1,W_1` from
truth tables.  It checks the exact identity (up to floating evaluation of
the displayed logarithms) on all 6,474 balanced functions modulo output
sign through four variables and 3,250 deterministic random balanced
functions in dimensions five through seven.  Maximum roundoff was
`3.331e-15`; the analytic bound had no negative numerical slack.  The
checker is corroboration only; the written calculus proof establishes the
all-parameter statement.

## Corrections and source scope

The independent A094 review at canonical commit
`da434787c48b70c8c0b957f58a9f55d82567cc08` was read and adopted: any
subsequent bent nullity-two statement requires exactly
`s=rank(M)=m-2`.  This run makes no broader bent-shield assertion.

Sources actually used:

- owner control revision `2026-10-12.1`, Brain control commit
  `40210272c19f43fed84f6a67653f9a04b0e11e28`, `ORDER.md` blob
  `7c5e21945adef435e6b587909603dd96794a1ebe`;
- A003 assignment blob `ac038a028831d59ad053dd56b2b527e2a71ffdee`;
- execution protocol blob `457358ff62cbf1141a72096bcabdf95bf18c1be2`;
- exact fresh-activation formula in B01 run
  `20261012T051555Z-fleet01-B01-majority-activation-no-go-a003`, package
  commit `8344aa4aa688790494e3ebd46bb94b13f659ce18`;
- A094 scope correction above, reviewing B01 package commit
  `92b9dd65273085c6cfa2c3ba69fa624b248e2959`.

No protected source, paid compute, public release, scheduler mutation, or
subagent was used.  Exposed model: Codex; reasoning-effort metadata was not
exposed.

## Persistence receipt

The complete nine-file package was committed and read back nonempty with
matching blob identities from both private routes:

- canonical package commit
  `62072d1b26e0cbbb18b71bfbc7bdaf2ce124b6b4`;
- Brain handoff package commit
  `0cd8b68cdc4ee67cd56a3033574555f6ca25277e`.

The delivery receipt is distinct from independent mathematical review or
downstream adoption.

## Next action

Freeze the weighted hierarchy claim that each physical coordinate's
`L_1+c_0W_1` credit is charged only at its first activating ancestor.  Test
it first on two-level balanced activations with a fresh balancing variable;
either prove the resulting telescope or preserve an exact coherent-core
counterexample.  Route this claim to B05/B18 and A086/A094.
