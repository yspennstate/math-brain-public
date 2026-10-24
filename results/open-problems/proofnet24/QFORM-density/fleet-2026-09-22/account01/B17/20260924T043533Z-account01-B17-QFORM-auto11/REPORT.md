SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B17, 2026-09-24T04:35:33Z.
attacking: close the symmetric six-variable Householder cone-tip integral in exact elementary form, then apply the newest completed account02/B17 zero-pivot theorem to a concrete target-valid inequality.

# QFORM-EXACT-SYMMETRIC-HOUSEHOLDER-SIX-v1

Programme: `QFORM-DENSITY-3EIG-20260922`, revision `2026-09-22.5`.  
Worker: `account01/B17`.  
Run: `20260924T043533Z-account01-B17-QFORM-auto11`.  
Status: **PROVED SUPPORTING SHARP-WITNESS THEOREM / FULL TARGET OPEN**.  
Execution: `WITHOUT_VERIFIED_BRAIN`.

The unrestricted theorem remains **OPEN / NOT PROVED / NOT DISPROVED**. Full-target continuity remains separate. The strongest source-valid universal lower obstruction remains `3 sqrt(2)`. The new result here is different: an exact elementary closed form for the finite six-variable rotated witness previously only enclosed numerically, plus a new actual-matrix application of account02/B17's completed generic zero-pivot theorem.

Fresh owner control and the live correction inbox were consumed before publication. In particular, no post-rotation independence, arbitrary-joint coarea cap, conditional-cap-as-independence step, or law-uniform pointwise stationary-phase bound is used.

## 1. Exact six-variable target witness

Let `X_1,...,X_6` be independent `Unif[-1/2,1/2]` and define the three disjoint bank sums

\[
Y_1={X_1+X_2\over\sqrt2},\qquad
Y_2={X_3+X_4\over\sqrt2},\qquad
Y_3={X_5+X_6\over\sqrt2}.
\tag{1.1}
\]

The `Y_j` are independent with common triangular density

\[
g(y)=\sqrt2(1-\sqrt2|y|)_+.
\tag{1.2}
\]

Put

\[
n={1\over\sqrt3}(1,1,1)^T,
\qquad
B=I_3-2nn^T
={1\over3}
\begin{pmatrix}
1&-2&-2\\
-2&1&-2\\
-2&-2&1
\end{pmatrix}.
\tag{1.3}
\]

If `R` is the `6 x 3` bank matrix with two rows `e_j/sqrt(2)` for each `j`, then `R^T R=I_3`, `Y=R^T X`, and `A=RBR^T` is

\[
\boxed{
A=
\begin{pmatrix}
1/6&1/6&-1/3&-1/3&-1/3&-1/3\\
1/6&1/6&-1/3&-1/3&-1/3&-1/3\\
-1/3&-1/3&1/6&1/6&-1/3&-1/3\\
-1/3&-1/3&1/6&1/6&-1/3&-1/3\\
-1/3&-1/3&-1/3&-1/3&1/6&1/6\\
-1/3&-1/3&-1/3&-1/3&1/6&1/6
\end{pmatrix}.
}
\tag{1.4}
\]

All 36 physical entries are nonzero and

\[
\boxed{\operatorname{spec}(A)=\{1,1,-1,0,0,0\}.}
\tag{1.5}
\]

Moreover, every original-coordinate `3 x 3` principal block is either singular or, when one coordinate is chosen from each bank, equals `B/2` and has spectral magnitudes `1/2`. Thus the three target-scale eigenvalues exist only after genuine bank aggregation.

The preceding B17 run proved the exact cone-tip small-ball formula

\[
I_*:=\lim_{h\downarrow0}{\Pr(|X^TAX|\le h)\over2h}
=\sqrt2\int_0^{2\pi}P(|\omega(\theta)|)\,d\theta,
\tag{1.6}
\]

where one null-circle sheet is

\[
\omega(\theta)
={n+\cos\theta\,e_1+\sin\theta\,e_2\over\sqrt2},
\quad
e_1={1\over\sqrt2}(1,-1,0),
\quad
e_2={1\over\sqrt6}(1,1,-2),
\tag{1.7}
\]

and, for `a_j>=0`, `m=max_j a_j`,

\[
P(a)=\int_0^\infty\prod_{j=1}^3(1-ta_j)_+dt
={1\over m}-{s_1\over2m^2}+{s_2\over3m^3}-{s_3\over4m^4}.
\tag{1.8}
\]

For any essentially bounded output density, `||p_Q||_infty >= I_*`; thus `I_*` is a valid universal-constant obstruction without choosing an arbitrary pointwise representative of a density.

Source dependency for (1.6)--(1.8): `yspennstate/math-open-problems@e68c07e9490090e0e27f33cd478b41ce42aad2f9`, `proofnet24/QFORM-density/fleet-2026-09-22/account01/B17/20260924T033844Z-account01-B17-QFORM-auto11/REPORT.md`.

## 2. Symmetry reduces the cone integral to two elementary pieces

Shift the angular variable by setting `x=theta-pi/6`. The three cone coordinates become

\[
\begin{aligned}
w_1(x)&={1\over\sqrt6}+{\cos x\over\sqrt3},\\
w_2(x)&={1\over\sqrt6}+{\cos(x-2\pi/3)\over\sqrt3},\\
w_3(x)&={1\over\sqrt6}+{\cos(x+2\pi/3)\over\sqrt3}.
\end{aligned}
\tag{2.1}
\]

Because `P` is symmetric in the absolute coordinates, the integrand has period `2pi/3` and is even in `x` (the reflection `x -> -x` swaps `w_2,w_3`). Therefore

\[
\boxed{I_*=6\sqrt2\int_0^{\pi/3}P(|w(x)|)\,dx.}
\tag{2.2}
\]

On `0<=x<=pi/3`, `w_1=max_j |w_j|`; `w_2>0`; and `w_3` changes sign exactly at `x=pi/12`. Put

\[
S=w_1+w_2+w_3=\sqrt{3/2}.
\tag{2.3}
\]

The elementary identities

\[
w_2w_3=w_1^2-Sw_1+{1\over4},
\qquad
w_2-w_3=\sin x
\tag{2.4}
\]

then give the exact piecewise integrand

\[
\boxed{
P_+(x)
={3\over4w_1}-{S\over4w_1^2}+{1\over48w_1^3},
\qquad 0\le x\le {\pi\over12},
}
\tag{2.5}
\]

and

\[
\boxed{
P_-(x)
={5\over12w_1}+{S-2\sin x\over12w_1^2}-{1\over48w_1^3},
\qquad {\pi\over12}\le x\le {\pi\over3}.
}
\tag{2.6}
\]

This is the step that makes the previously numerical cone integral exactly elementary.

## 3. Closed-form antiderivatives

Write

\[
w_1(x)={1\over\sqrt6}(1+\sqrt2\cos x),
\qquad
z={\tan(x/2)\over1+\sqrt2}.
\tag{3.1}
\]

Define

\[
J_1(z)=2\sqrt6\,\operatorname{artanh}z,
\tag{3.2}
\]

\[
J_2(z)=12\left({\sqrt2 z\over1-z^2}-\operatorname{artanh}z\right),
\tag{3.3}
\]

and

\[
J_3(z)=24\sqrt6\left({z\over(1-z^2)^2}+\operatorname{artanh}z\right)
-12\sqrt6(1+2\sqrt2){z\over1-z^2}.
\tag{3.4}
\]

Then `dJ_k/dx=w_1^{-k}` for `k=1,2,3`. The remaining sine term is also exact:

\[
\int {\sin x\over w_1(x)^2}dx={\sqrt3\over w_1(x)}.
\tag{3.5}
\]

At the two breakpoints,

\[
z_1=z(\pi/12)=4+3\sqrt3-3\sqrt2-2\sqrt6,
\qquad
z_2=z(\pi/3)={\sqrt6-\sqrt3\over3},
\tag{3.6}
\]

and

\[
w_1(\pi/12)={\sqrt6+\sqrt2\over4},
\qquad
w_1(\pi/3)={\sqrt6+\sqrt3\over6}.
\tag{3.7}
\]

Substituting (2.5)--(2.6) into (2.2) gives, before simplification,

\[
\begin{aligned}
I_*=6\sqrt2\Big[&{1\over3}J_1(z_1)+{5\over12}J_1(z_2)
-{S\over3}J_2(z_1)+{S\over12}J_2(z_2)\\
&+{1\over24}J_3(z_1)-{1\over48}J_3(z_2)
-{\sqrt3\over6}\{w_1(\pi/3)^{-1}-w_1(\pi/12)^{-1}\}\Big].
\end{aligned}
\tag{3.8}
\]

All rational-algebraic terms collapse, yielding the exact value

\[
\boxed{
\begin{aligned}
I_*={}&44\sqrt3\,\operatorname{artanh}\!\left(4+3\sqrt3-3\sqrt2-2\sqrt6\right)\\
&-2\sqrt3\,\operatorname{artanh}\!\left({\sqrt6-\sqrt3\over3}\right)
-{165\over4}+12\sqrt3+15\sqrt2.
\end{aligned}
}
\tag{3.9}
\]

The committed symbolic checker verifies the characteristic polynomial of `B`, the three rationalized `z`-coordinate antiderivative identities, and a rigorous interval evaluation of (3.9). It returns

\[
\boxed{
I_*\in
[4.063070616806037260125484422593499956752965346061772324,
4.063070616806037260125484422593499956752965346066262569].
}
\tag{3.10}
\]

Hence the exact finite target witness satisfies

\[
\boxed{\|p_{X^TAX}\|_\infty>4.063.}
\tag{3.11}
\]

This improves the preceding certified `>4.0625` bound and, more importantly, eliminates numerical quadrature from the mathematical value. It does **not** improve the strongest unrestricted lower obstruction

\[
\boxed{C_{\rm univ}\ge3\sqrt2=4.242640687119\ldots,}
\tag{3.12}
\]

which still comes from the diffuse three-bank limit. The gap between that obstruction and the exact finite-six witness is about `0.179570070313248`.

## 4. Newest account02/B17 theorem applied to an actual target inequality

The latest completed designated-partner result consumed here is

`yspennstate/math-open-problems@f6c1d85bd32a1bf5e70264d4327806d128481131`,
`proofnet24/QFORM-density/fleet-2026-09-22/account02/B17/20260924T034414Z-account02-B17-qform-auto11-r46/REPORT.md`.

It proves the following global product-law theorem. If a real symmetric `3 x 3` matrix has all three eigenvalue magnitudes at least one and has a zero physical diagonal entry, then for arbitrary independent cap-one marginals

\[
\|p_Q\|_\infty
\le \sqrt2\left[2+\log\left(\sqrt2+{1\over3}\right)\right]
=3.617859563383761\ldots<3\sqrt2.
\tag{4.1}
\]

More precisely, choosing the zero physical pivot and writing its two incident edges as `a,b`,

\[
L=\sqrt{a^2+b^2},
\qquad
|\det A|=L^2|\kappa|,
\tag{4.2}
\]

the partner result gives, when `K=|kappa|/L < 3/sqrt(2)`,

\[
\boxed{
\|p_Q\|_\infty
\le {\sqrt2\over L}
\left[2+\log\left({\sqrt2L\over|\kappa|}+{1\over3}\right)\right].
}
\tag{4.3}
\]

Apply (4.3) to the concrete fully coupled target matrix

\[
A_p=
\begin{pmatrix}
1&1&-1\\
1&0&1\\
-1&1&0
\end{pmatrix}.
\tag{4.4}
\]

Its characteristic polynomial is

\[
(\lambda-1)(\lambda^2-3),
\tag{4.5}
\]

so

\[
\boxed{\operatorname{spec}(A_p)=\{1,\sqrt3,-\sqrt3\}.}
\tag{4.6}
\]

Thus it is target-valid. Using the second coordinate as the zero pivot,

\[
L=\sqrt2,
\qquad
|\kappa|={|\det A_p|\over L^2}={3\over2},
\qquad
K={3\over2\sqrt2}<{3\over\sqrt2}.
\tag{4.7}
\]

Therefore the completed partner theorem gives the actual arbitrary-law inequality

\[
\boxed{
\left\|p_{X^2+2XY-2XZ+2YZ}\right\|_\infty
\le 2+\log{5\over3}
=2.5108256237659906832\ldots
}
\tag{4.8}
\]

for every independent `X,Y,Z` with one-dimensional densities bounded by one. This is an actual application of account02/B17's completed theorem to a fresh target-valid matrix, not a citation-only dependency.

The partner's correction file was also read; it changes only an informal label for an account03 dependency and leaves the zero-pivot formulas unchanged.

## 5. Constraint on any proposed sharp proof

The comparison is now unusually clean. A target-valid **single physical zero-pivot triple** is globally bounded by at most `3.61786` by account02/B17, and the explicit matrix (4.4) is bounded by only `2.51083`. By contrast, the six-variable grouped Householder witness has a rigorously exact cone-tip obstruction `I_*=4.063070616806...`, even though **no original-coordinate principal triple has three eigenvalues at the target scale**.

Therefore a sharp proof cannot safely collapse grouped-coordinate geometry to a single target-valid zero-pivot physical triple while pretending concentration is preserved. The spectral threshold must be paid after aggregation or by a genuinely product-preserving grouped-coordinate/ridge mechanism. This is consistent with the live full-proof gap: the bare target hypothesis does not automatically supply a uniformly good physical minor.

The witness remains below `3sqrt(2)`, so it does not disprove the candidate sharp constant. It does show that finite, order-one, entrywise-dense physical coupling plus grouped independent banks already generates concentration significantly above all currently closed three-variable zero-pivot architectures.

## 6. Checks, provenance, and scope

Authoritative checker: `CHECK.py`.  
Authoritative numerical/symbolic output: `CHECK_OUTPUT.txt`, containing `QFORM_B17_EXACT_SIX_HOUSEHOLDER_CHECK_PASS`.

Mathematical scope:
- exact finite `n=6` lower witness for iid physical unit-interval laws;
- exact nonzero spectrum `{1,1,-1}` and entrywise-dense physical matrix;
- exact elementary expression for its centered cone-tip small-ball derivative;
- no claim that this orientation is globally optimal at `n=6`;
- no claim that the unrestricted sharp constant equals `3sqrt(2)`;
- full arbitrary-law/full-dimension QFORM remains open;
- unrestricted continuity remains separate.

Control refreshed during the run to `yspennstate/math-research-brain@aa2367e22ada13d982748057e4a0788e0e61adfe`; no later B17 stop or target change was present. Schedule, enabled/quiet state, email/push state, identity, permissions, visibility, and public-release state were not changed.
