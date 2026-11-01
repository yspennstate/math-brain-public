# B05 / A023 — changing-overlap local swap fee is impossible

**Run:** `20261014T072934Z-fleet01-B05-changing-overlap-swap-a023`  
**Primary packet:** A023  
**Stable gap:** `GU-ASYMMETRY-MISMATCH`  
**Claim:** `B05-A023-CHANGING-OVERLAP-SWAP-NOGO-v1`  
**Status:** **PROVED PARAMETRIC ROUTE OBSTRUCTION, PENDING INDEPENDENT REVIEW**  
**Universal GU / full FEI:** **OPEN**

## Candidate and prior scope

The accepted fixed-block orbit potential is

\[
\widetilde\Lambda_X(f)=
\psi_{|X|}(E_X^f(\varnothing))+
\sum_{i\notin X}q(E_X^f(\{i\})),
\]

with (psi_k(t)=q(t)+tlog_2k).  It handles arbitrary reveal orders for
one fixed shared block.  The first changing-overlap candidate was an
absolute local transition fee:

\[
\widetilde\Lambda_{\{y,z\}}(f)
\le\widetilde\Lambda_{\{y,x\}}(f)
+C(\operatorname{Inf}_x(f)+\operatorname{Inf}_z(f)). \tag{Swap}
\]

If valid, this would let the first-revelation account follow the simplest
overlap change ({x,y}\to{y,z}) without reusing credit.

## Result

`Swap` is false for every finite (C).  Let (M_m) be odd majority and

\[
f_m(y,x,z,u)=x\quad(y=1),\qquad
f_m(y,x,z,u)=zM_m(u)\quad(y=-1).
\]

Writing

\[
a_m=\frac{\binom{m-1}{(m-1)/2}}{2^{m-1}},
\]

exact orbit accounting gives

\[
\widetilde\Lambda_{\{y,z\}}(f_m)
-\widetilde\Lambda_{\{y,x\}}(f_m)
=m q(a_m^2/2)-\frac12
=\frac1\pi\log_2m+O(1),
\]

while

\[
\operatorname{Inf}_x(f_m)=\operatorname{Inf}_z(f_m)=\frac12.
\]

Thus even one swap recharges an unbounded private singleton packet, although
the entering and leaving pivotal budgets stay constant.  All coordinates in
both blocks are genuinely active; this is not a dummy-variable artifact.

## Exact scope

This eliminates local nonnegative swap payments based only on the
symmetric-difference coordinates.  It does **not** eliminate payment by:

- the whole transported (z)-containing Fourier slice;
- total private-core influence, which is order (sqrt m) here;
- signed upper-set/KL cancellation;
- a globally chosen restriction tree.

Accordingly, the result is not a GU or FEI counterexample.  It sharpens the
remaining A023 obligation: a changing-core proof must assign ownership to
the private slice before it can become singleton mass; charging only the
coordinates by which successive overlap sets differ is impossible.

## Verification and next action

The checker passed five direct exact-Fraction Walsh cases and the closed
central-binomial formula through (m=2001).  The next mechanism should
transport the entire entering-coordinate slice and test whether its signed
(K_i-\Gamma_i) contribution can be charged to total private influence
without double spending across a second swap.

Fresh A087/A094 review is required.  No native ingestion is claimed.
