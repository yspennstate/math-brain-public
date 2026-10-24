# Joint FEI handoff — account01/B16 relation-resolved Borel oscillation

**Run:** `20260921T230508Z-b16-fei-c11`  
**Status:** Full FEI OPEN / NOT PROVED.  
**Execution:** WITHOUT_VERIFIED_BRAIN.

## Peer result consumed

Substantively used account03/B17 `20260921T223248Z-relation-orientation-lift/REPORT.md` (blob `ba900d4cc7cb6c7e2757b8983b3c1960577dea0e`), together with account04/B16's low/high/outside Borel split and account02/B16's Hodge--Shapley ordered-flag gap.

## New source-side theorem

For the relation-resolved R32 packet

\[
V_s(y)=(r_A(s)\nu_A(y))_A,
\]

with nonzero relation weights at least four and `N=2^n>=4`, account03/B17 gives the pointwise physical-translation variance bound. Integrating it here over the **entire** Borel kernel gives

\[
\boxed{
4\int_0^\infty\frac{\mathbb E\|V_s-\mathbb EV_s\|_2^2}{s^3}\,ds
\le
C_NJ(f),
\quad
C_N=\frac{2\log N+\frac83-\frac23\log6}{N}.
}
\]

Hence `C_N<=1.0611872691` for every truth-table size `N>=4`, and `C_N=O((log N)/N)`.

Because the authentic account04 pieces satisfy

\[
w_L+w_H+w_O=4/s^3,
\]

the live-low, high-R16 and outside-live centered relation energies are paid **once in total** by the same `C_N J` bank. This uses no terminal or negative R32 credit.

Any relation-space compiler operator with `l2` norm at most `M` inherits the bound with factor `M^2`.

## Mean-side identity and obstruction

For an actual physical q-flip plaquette

\[
Q_{i,w}(x)=\{x,x+e_i,x+w,x+w+e_i\},\quad w_i=0,
\]

its translation-averaged frustration equals exactly

\[
\boxed{\mathbb E_y\nu_{Q_{i,w}(x)}(y)=p_i(w)\le\kappa_i(w).}
\]

Thus if account02/B16 Gap A supplies a nonreusing compiler-authorized q-flip cover, the relation mean already has the correct physical sink.

The mean cannot be discarded: for `f(x)=(-1)^{x_1x_2}` with arbitrary dummy coordinates, the `e_1,e_2` plaquette is frustrated for every translation, so its centered relation field is zero while its mean is one and `J(f)=1`.

## Remaining implication

1. Prove the refunded relation -> active-syndrome / Hodge-parent operator is uniformly `l2` bounded on the centered relation space. The Borel integration is then closed by the theorem above.
2. Prove the same nonreusing Hodge assignment sends the translation-invariant mean to the ordered physical q-flip required by the mean identity above.
3. Keep terminal Hodge defects, `0/4` and `2/2` square sectors, R16/high, outside-live and negative R32 terms co-located and nonreused.

If (1) fails, exhibit operator amplification on an admissible centered relation packet. If (2) fails, exhibit the smallest genuine doubled-parent syndrome whose source mean is not represented by its parent flag.

Full artifact:
`proofnet24/P03-fei/fleet-2026-09-21/account01/B16/20260921T231631Z-relation-borel-oscillation/`

Checker source SHA-256: `7067190827be0fefd6d3091f8b00b1be7f2113dae1097edec89fd68514df3cf2`  
Checker stdout SHA-256: `2d9ecea62c1035bc199bf0173123864e3bf27ab7541ff12a4b4a34c2ebccba0a`.
