# HARD7-01 route note before checking — mass/Radon sandwich

Target carried from STUCK2: for an origin-symmetric planar convex disk `M`, with `H=H_6(M)` the maximum area of an inscribed affine-regular hexagon,

\[
\Psi(M):=(3|M|-|H|)|M^\circ|\ge 18. \tag{C}
\]

If (C) holds, Chakerian's fixed-central-symmetral theorem gives

\[
(|B-B|+2|B|)|(B-B)^\circ|\ge 12 \tag{DF2}
\]

for every planar convex body `B`, not only the pentagon case that triggered STUCK2.

The direct monotonicity of `Psi` under Radonization is unnecessary. Combine two different published pieces of Langi's 2016 proof.

Let `P` be a maximum-area parallelogram in `M`. Affinely normalize `|P|=2`, so the standard maximum parallelogram has vertices `(+-1,0),(0,+-1)`. Write `A=|M|`, `Bpol=|M^circ|`, `h=|H|`.

1. **Mass inequality gives the missing hexagon/area coupling.** Choose a Chakerian minimum-area Reuleaux body `K` having central symmetral `M`, so `|K|=2A-(4/3)h`. Langi's Theorem 2.3 says `c_tr^m(K)>=6`, while formula (8) gives `c_tr^m(K)=2(|K|+2|P|)/|P|`. Hence

\[
6A-4h\ge 3|P|,
\]

and under `|P|=2`,

\[
h\le \frac32(A-1). \tag{R1}
\]

2. **Radon completion gives a polar-area lower envelope.** In Langi's proof of Theorem 2.2, the same normalization yields numbers `x_1,x_2 in [0,1/2]` with

\[
Bpol=A+2x_1+2x_2,
\]

and two Radon completions `M_i` with the same maximum parallelogram area `2` and areas `A+2x_i` (up to index swap). The sharp Radon bound used there gives `|M_i|>=3`. Thus when `2<=A<=3`, each `x_i >= (3-A)/2`, hence

\[
Bpol\ge 6-A. \tag{R2a}
\]

The basic inclusion of `M` in the quarter-turn of `M^circ` gives, for all `A`,

\[
Bpol\ge A. \tag{R2b}
\]

3. From (R1), `3A-h >= (3/2)(A+1)`. Since `P subset M`, `A>=2`.

- For `2<=A<=3`, (R2a) gives
  `Psi >= (3/2)(A+1)(6-A) = 18 + (3/2)(A-2)(3-A) >=18`.
- For `A>=3`, (R2b) gives
  `Psi >= (3/2)A(A+1) = 18 + (3/2)(A-3)(A+4) >=18`.

Thus (C) appears to follow globally from published ingredients without differentiating the nonsmooth maximizer `H_6`.

4. Chakerian then gives `|B|>=2A-(4/3)h`; therefore

\[
\left(A+\frac{|B|}{2}\right)|M^\circ|
\ge \frac23(3A-h)|M^\circ|\ge12,
\]

which is exactly (DF2) after `M=(B-B)/2`.

Methods for this recovery: **B8** (replace the continuum deformation by the exact two defect variables `x_1,x_2`), **B15** (keep the non-Radon asymmetry instead of assuming it away), **B27** (swap from controlling every maximizer trajectory of `H_6` to existential Radon completions plus a universal mass inequality, then eliminate the auxiliary quantities).

Before promotion: verify every constant against Langi 2016, check the algebra exactly, search the exact combined inequality for prior art, and keep `d_sym=3` because this does not prove dimension four.