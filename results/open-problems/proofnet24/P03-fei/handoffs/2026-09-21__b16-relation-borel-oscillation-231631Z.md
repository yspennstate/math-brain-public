# FEI joint interface-C handoff — fleet01/B16 relation-resolved Borel payment

**Run:** `20260921T230508Z-b16-fei-c11`  
**Full FEI:** OPEN / NOT PROVED.  
**Execution:** WITHOUT_VERIFIED_BRAIN.

## Named peer result consumed

Substantively used fleet03/B17

`proofnet24/P03-fei/fleet-2026-09-21/fleet03/B17/20260921T223248Z-relation-orientation-lift/REPORT.md`

(blob `ba900d4cc7cb6c7e2757b8983b3c1960577dea0e`). Its even-relation translation theorem gives, for the authentic relation vector `V_s`,

\[
\mathbb E\|V_s-\mathbb EV_s\|_2^2
\le J(f)N x\Pr[\mathrm{Bin}(N-1,x)\ge3],\quad x=\sin^2(s/N).
\]

Also used fleet04/B16's exact low/high/outside no-reuse Borel split and fleet02/B16's Hodge--Shapley ordered-flag gap.

## New proved result

For `N=2^n>=4`,

\[
\boxed{
4\int_0^\infty\frac{\mathbb E\|V_s-\mathbb EV_s\|_2^2}{s^3}\,ds
\le
C_NJ(f),
\qquad
C_N=\frac{2\log N+\frac83-\frac23\log6}{N}.
}
\]

Hence `C_N<=C_4=1.0611872690...` and `C_N=O((log N)/N)`.

Because the authentic Borel pieces satisfy

\[
w_L+w_H+w_O=4/s^3,
\]

the *sum* of the live-low, high-R16, and outside-live centered relation energies is paid once by the same `C_N J` bound. No terminal or negative R32 credit is spent.

The bound is stable under any relation-space operator `T_s` with uniform `l2` norm `M`:

\[
4\int\frac{\mathbb E\|T_s(V_s-\mathbb EV_s)\|_2^2}{s^3}ds
\le M^2C_NJ(f).
\]

## New exact mean identity

For a physical q-flip plaquette

\[
Q_{i,w}(x)=\{x,x+e_i,x+w,x+w+e_i\},\qquad w_i=0,
\]

its translated frustration bit satisfies

\[
\boxed{
\mathbb E_y\frac{1-\prod_{z\in Q_{i,w}(x)}f(y+z)}2=p_i(w)\le\kappa_i(w).
}
\]

Thus, once a compiler relation is authentically and nonreusingly identified with its ordered physical q-flip, its translation-invariant mean already has the correct physical sink.

## Obstruction / regression test

Centering alone is not a proof. For

\[
f(x)=(-1)^{x_1x_2}
\]

with arbitrary dummy coordinates and the `e_1,e_2` plaquette, the relation frustration is identically one under every physical translation, so the centered component is zero while the mean is one and `J(f)=1`. Any bridge that discards the relation means is false.

## Remaining implication

The Borel corridor is no longer the source-side obstruction on the centered relation subspace. The exact next interface-C task is:

1. prove the authentic refunded relation -> active-syndrome/Hodge-parent operator has dimension-free `l2` norm on `V_s-EV_s`;
2. prove fleet02/B16's compiler-authorized nonreusing Hodge cover maps the corresponding means to the ordered physical q-flips, so the identity above sends them to `p_i(w)<=kappa_i(w)`;
3. keep terminal Hodge defects, `0/4` and `2/2` square sectors, high/outside pieces and negative R32 credits co-located and nonreused.

If (1) fails, produce an admissible centered relation packet with operator amplification. If (2) fails, produce the smallest genuine doubled-parent syndrome whose source mean cannot be represented by its ordered parent flag.

## Artifact

Full report and checker:

`proofnet24/P03-fei/fleet-2026-09-21/fleet01/B16/20260921T231631Z-relation-borel-oscillation/`

Checker source SHA-256: `7067190827be0fefd6d3091f8b00b1be7f2113dae1097edec89fd68514df3cf2`  
Checker stdout SHA-256: `2d9ecea62c1035bc199bf0173123864e3bf27ab7541ff12a4b4a34c2ebccba0a`.
