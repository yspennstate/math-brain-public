# P0257 route note — shape-dependent capsule guard inside the non-C4 chain family

This note is written **before checker code**. It records the mathematical route, not a proved claim by itself.

Planned Section-B methods for this run: **#6 DEFORM TO A POINT YOU CAN SOLVE, #21 ASK WHO ELSE HAS THIS SHAPE, #29 ADD THE POINTS AT INFINITY**.

The predecessor certified an additive non-C4 size-4 sink-SCC correction over the normalized shape box

- `p1=(0,0)`, `p2=(1,0)`;
- `71/40 <= x3 <= 89/40`, `-1/2 <= y3 <= 1/2`;
- `111/40 <= x4 <= 129/40`, `-1/2 <= y4 <= 1/2`;

using one uniform external guard radius `H=57/20` around all four vertices. Its guard-union area was upper-bounded by the `H`-parallel body of the whole `129/40 by 1` rectangle, giving `Q_old=147939/2800`.

The new idea is to deform only a positive-measure central subfamily, retain the predecessor certificate on the complement, and give the subfamily **vertex-wise guard radii** adapted to the local second-neighbor ranks.

Take the central subfamily

`|y3|,|y4| <= a := 36/125`.

Keep the predecessor's exact internal topology bounds, but use the sharper per-vertex second-neighbor upper bounds

`U1=U4=229/100`, `U2=133/100`, `U3=177/100`.

Give every possible path-boundary crossing the same positive surplus `delta=1/2` by taking

`R1=R4=279/100`, `R2=183/100`, `R3=227/100`.

The key geometric compression is that the two smaller middle guard disks are contained in the capsule around the endpoint segment `[p1,p4]` with radius `R=279/100`.

For `p2`, the point `(1,y4/x4)` lies on `[p1,p4]`, so

`dist(p2,[p1,p4]) <= |y4|/x4 <= (36/125)/(111/40) = 96/925 < 24/25 = R-R2`.

For `p3`, the point `(x3,(x3/x4)y4)` lies on `[p1,p4]`, and

`dist(p3,[p1,p4]) <= |y3| + (x3/x4)|y4| <= (36/125)(1+89/111) = 96/185 < 13/25 = R-R3`,

with exact slack `1/925`.

Thus the whole unequal-radius guard union is contained in `[p1,p4] + B_R`.

On the same central subfamily,

`|p1-p4|^2 <= (129/40)^2 + (36/125)^2 < (81/25)^2`,

so the capsule area is at most

`2 R (81/25) + pi R^2`.

Using only `pi < 22/7` gives the exact coefficient

`Q_cap = 1489023/35000 = 42.5435142857...`,

strictly smaller than `Q_old=52.8353571428...`.

The central subfamily has normalized shape volume

`V_cap=(9/20)^2(72/125)^2 = 26244/390625`,

which is the fraction `5184/15625` of the predecessor chain box.

The same sink-SCC Hamiltonian-boundary lemma gives `L`-side surplus at least `delta*s = s/2` per non-endpoint component. The exact-binomial / Campbell-Mecke transfer therefore gives

`Delta_cap >= (5*pi^(3/2)/64) * V_cap * (1/2) * Q_cap^(-7/2)`.

The intended certificate uses `pi^(3/2)>51/10` and `sqrt(Q_cap)<261/40`; preliminary exact arithmetic gives a central correction around `2.664e-8`, versus about `1.398e-8` from the predecessor's uniform-guard certificate on exactly the same central shapes. The complement keeps its predecessor certificate, so any verified difference is genuine movement without double counting.

Method #21 literature target: compare this unequal-radius capsule/parallel-body compression with standard continuum nearest-neighbor component geometry; use prior art only for context, not as a substitute for the source-valid finite-binomial transfer. Method #29: the scale integral is kept over `s in (0,infinity)` with the same fixed-cutoff-then-limit argument, so the compactified tail remains explicit rather than simulated.
