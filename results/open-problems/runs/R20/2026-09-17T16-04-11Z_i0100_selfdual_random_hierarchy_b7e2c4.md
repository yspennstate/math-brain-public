Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — GPT-6 / maximum was requested in prompt text, but the exposed runtime provides no authenticated applied-model or reasoning-effort receipt, so I do not claim GPT-6 / maximum. **NO MOVEMENT in the frozen exact-prime metric: `1213 -> 1213`; retained exact set `{5,13,17,29,41,181,241,317,421,541,601,661,1009,1021,1033,1049,1061,1093,1201,1213}`; unchanged count `0 -> 1`; status PARTIAL / SOURCE OPEN. Section-B moves: second-pass #8 GO THE OTHER WAY AND DISCRETIZE, #17 LOOK FOR YOUR NUMBERS SOMEWHERE ELSE, #28 REPLACE “FOR ALL” WITH “FOR TYPICAL”.**

# R20 / I0100 — a self-dual orthant threshold, the exact Gaussian random analogue, and an all-degree balanced-profile hierarchy

Repository / branch: `yspennstate/math-open-problems` / `master`.
Canonical claim: `operations/claims/I0100.md`.
Outside source: Afonso S. Bandeira et al., *Randomstrasse101: Open Problems of 2025*, Conjecture 26; stable compilation arXiv:2603.29571.

For `p = 1 mod 4`, put
\[
n=(p-1)/2.
\]
Let `Q` be the nonzero quadratic residues, choose a generator `alpha` of `Q`, and let
\[
S=\{d\in\mathbb Z_n\setminus\{0\}:\alpha^d-1\in Q\}.
\]
Then the one-localization is
\[
G_{p,1}=\operatorname{Cay}(\mathbb Z_n,S),
\]
and this track's source-normalized quantity is
\[
T_p:=\vartheta(\overline{G_{p,1}}).
\]
The source target is
\[
T_p\sim\sqrt{p/2}=\sqrt{n+1/2},
\]
which is equivalent to `T_p ~ sqrt(n)`.

## 1. Recovery, source gate, ownership, and current status

I continued from

`runs/R20/2026-09-17T15-10-00Z_i0100_p1213_quadratic_mellin_5e8c31.md`

rather than restarting. Before new mathematics I reread the campaign INDEX/RANKING, root POSTED/RESULTS/QUEUE, the operative follow-up implementation manifest, the canonical I0100 claim, and the newest neighboring Paley state available on `master`.

Ownership remains exact and non-overlapping:

- I0100 / Conjecture 26 / one-localization belongs to R20;
- P04 / I0101 is the distinct two-localization Conjecture 27; its newest located report keeps its exact domain at `{149,257,1009,4001,4013,4021}` and source status OPEN / PARTIAL;
- R12 exhausted its allowed stuck recoveries on I0102 / Conjecture 28 and handed that target off before rotating to I0060; nothing from the degree-four SoS scope is imported here;
- C28 / I0103 is the distinct Paley-ETF / Conjecture 29 scope.

Fresh source/literature check, 2026-09-17: the current public Jig #7 still labels the Conjecture-26 root **Open** and still asks whether the clique-bounding Lovasz theta of the Paley one-localization is asymptotic to `sqrt(p/2)`. I found no later source-matching resolution in the bounded current search. This is dated negative search evidence, not a worldwide novelty certificate.

The exact finite frontier entering and leaving this run is
\[
\boxed{p_{\max}=1213}
\]
with the full exact-certified set
\[
\boxed{\{5,13,17,29,41,181,241,317,421,541,601,661,1009,1021,1033,1049,1061,1093,1201,1213\}}.
\]
The preceding run moved the metric, so the post-movement unchanged count entering this run was `0`.

I did **not** spend this run manufacturing another prime certificate. The method work below produced a stronger structural target, and the only code written is explicitly discovery-only.

---

## 2. Idea before code

The previous reports had reduced Conjecture 26 to a one-sided Chebyshev / projected-simplex radial constant. For a real subspace `E` of
\[
H:=\mathbf 1^\perp\subset\mathbb R^n,
\]
let `P_E` denote orthogonal projection and define
\[
\boxed{
a_E:=\min_{\substack{r\in E\\r_0=1}}
\left(-\min_{i>0}r_i\right).
}
\tag{2.1}
\]
Equivalently, if `u_i=P_E e_i`, then
\[
\boxed{
a_E=\max\{a\ge0:-a u_0\in\operatorname{conv}(u_1,\ldots,u_{n-1})\}.
}
\tag{2.2}
\]
For the two complementary Paley Fourier halves, call these `a_N` and `a_S`. Earlier R20 work proved
\[
T_p=\frac{n a_N}{1+a_N}=1+\frac1{a_S}.
\tag{2.3}
\]

The new question I asked was: **what is the natural geometric threshold for (2.2) before inserting any Paley arithmetic?** That leads to a clean self-dual point, an orthant, and an exactly solvable random analogue.

In parallel I asked whether the previous quadratic balanced profile could be extended systematically rather than one degree at a time. That gives an exact all-degree hierarchy whose arithmetic data are just higher additive representation counts.

---

## 3. #8 DISCRETIZE — the exact all-degree balanced-profile hierarchy

Use the projected-simplex notation from the preceding reports. Let `Z=-Z` be a nonzero Fourier set in `Z_n`, `d=|Z|`, and
\[
A=n/d.
\]
Normalize the projected vertices by
\[
u_x=(d/n)^{-1/2}P_Ze_x,
\qquad
c_x=\langle u_0,u_x\rangle,
\qquad
z_x=u_x-c_xu_0.
\]
For coefficients `f_x`, the exact balancing projection is
\[
R_f=\sum_{x\ne0}f_xz_x,
\qquad
(\mathcal B_Zf)_x=f_x-\frac1A\langle R_f,z_x\rangle.
\tag{3.1}
\]
It kills the transverse moment and preserves both total mass and the radial moment `sum c_x f_x`.

For every integer `r>=1`, define the `r`-fold additive representation count
\[
m_r(k):=\#\{(a_1,\ldots,a_r)\in Z^r:a_1+\cdots+a_r=k\},
\]
and its mean on `Z`,
\[
\bar m_r:=\frac1{|Z|}\sum_{k\in Z}m_r(k).
\]
Also put
\[
R_r:=\sum_x c_x^r z_x,
\qquad
\rho_r(x):=\langle R_r,z_x\rangle.
\]
(`z_0=0`, so including `x=0` changes nothing.)

### Theorem R20-POLYHIER1 — exact all-degree correction formula

With the unnormalised discrete Fourier transform,
\[
\boxed{
\widehat{\rho_r}(k)
=\frac{A^{r+1}}{n^{r-1}}
\bigl(m_r(k)-\bar m_r\bigr)1_Z(k).
}
\tag{3.2}
\]
For a real polynomial
\[
P(t)=\sum_{r=0}^m b_rt^r,
\]
set `rho_0=0` and define
\[
\boxed{
F_P(x):=P(c_x)-\frac1A\sum_{r=0}^m b_r\rho_r(x).
}
\tag{3.3}
\]
Then `F_P = B_Z(P(c))` has exact transverse balance. If
\[
F_P(x)\ge0\qquad(x\ne0)
\tag{3.4}
\]
and its total mass is positive, then
\[
\boxed{
a_Z\ge
-\frac{\sum_{x\ne0}c_xP(c_x)}
       {\sum_{x\ne0}P(c_x)}.
}
\tag{3.5}
\]

#### Proof

Since
\[
\widehat c=A1_Z,
\]
the product-convolution rule gives
\[
\widehat{c^r}(k)
=\frac{A^r}{n^{r-1}}m_r(k).
\tag{3.6}
\]
Also
\[
\rho_r(x)
=\sum_yc_y^r\bigl(c_{x-y}-c_xc_y\bigr)
=(c^r*c)(x)-c_x\sum_yc_y^{r+1}.
\tag{3.7}
\]
The first term in (3.7) has transform
\[
\frac{A^{r+1}}{n^{r-1}}m_r(k)1_Z(k).
\]
At zero,
\[
\sum_yc_y^{r+1}
=(c^r*c)(0)
=\frac{A^{r+1}}{n^r}\sum_{k\in Z}m_r(k),
\]
so the transform of the second term in (3.7) is
\[
\frac{A^{r+1}}{n^{r-1}}\bar m_r\,1_Z(k).
\]
Subtracting proves (3.2).

Linearity of (3.1) now gives (3.3). By construction `F_P` is transversely balanced; the balancing projection preserves mass and radial moment, so
\[
\sum F_P=\sum P(c),
\qquad
\sum cF_P=\sum cP(c).
\]
If (3.4) holds, normalizing `F_P` to a probability vector gives an admissible point of the radial LP (2.2), proving (3.5). QED.

The previous quadratic Mellin formula is exactly the case `r=2`. Thus every fixed degree has a finite arithmetic description: degree `m` requires only the centered `r`-fold additive representation counts of the Paley Fourier half for `r<=m`.

### Discovery-only outcome

I executed a floating LP for this hierarchy at `p=1213`, explicitly marked `DISCOVERY_ONLY_NO_CERTIFICATE`. Using a scaled monomial basis, the best values of `sqrt(n) a_profile` through degree 15 were

- `N`: degree 1 `0.74747`, degree 5 `0.78019`, degree 10 `0.80709`, degree 15 `0.81581`;
- `S`: degree 1 `0.74995`, degree 5 `0.76595`, degree 10 `0.77345`, degree 15 `0.79239`.

The previous full floating radial LP at the same prime was about `1.05834` for `N` and `1.02660` for `S`. Therefore low fixed degree is still far from the true radial optimizer. This is numerical route selection only; no value here is an exact certificate.

The useful conclusion is structural: if the polynomial hierarchy is to solve the source, its degree must grow, or the proof must control the full Gibbs/extreme profile rather than any fixed low-degree truncation.

---

## 4. #17 LOOK FOR YOUR NUMBERS SOMEWHERE ELSE — complementary radial duality and the self-dual point

Let `E,F` be orthogonal complementary subspaces of `H=1^perp`. In the nondegenerate regime relevant here, both radial constants exceed the universal baseline `1/(n-1)`.

Define
\[
\mathfrak f(a):=\frac{1+a}{(n-1)a-1}.
\tag{4.1}
\]
It is decreasing and involutive on `a>1/(n-1)`:
\[
\mathfrak f(\mathfrak f(a))=a.
\]

### Theorem R20-COMP1 — exact complementary-subspace radial duality

\[
\boxed{a_F=\mathfrak f(a_E).}
\tag{4.2}
\]

#### Proof

The LP dual of (2.1) is the hull form
\[
a_E=\max\left\{a:
 y_i\ge0,\ \sum_{i>0}y_i=1,
\ P_E(y+a e_0)=0
\right\},
\tag{4.3}
\]
where `y_0=0`.

Take an optimal pair `(a,y)` in (4.3), and put
\[
w=y+a e_0,
\qquad
r=w-\frac{1+a}{n}\mathbf1.
\]
Because `P_Ew=0`, the centered vector `r` lies in `F`. Its coordinates satisfy
\[
r_0=\frac{(n-1)a-1}{n},
\qquad
r_i\ge-\frac{1+a}{n}\quad(i>0).
\]
After dividing by `r_0`, this is feasible for the primal problem defining `a_F`, hence
\[
a_F\le\mathfrak f(a_E).
\tag{4.4}
\]

For the reverse inequality, take a primal optimizer `r in F` for `a_F=b`, so `r_0=1` and `r_i>=-b`. Put `t=f(b)` and
\[
\alpha=\frac{(n-1)t-1}{n},
\qquad
\beta=\frac{1+t}{n}=\alpha b,
\qquad
w=\alpha r+\beta\mathbf1.
\]
Then `w_0=t`, every `w_i>=0` for `i>0`, and because `sum r=0`,
\[
\sum_{i>0}w_i=1.
\]
Moreover `w` is orthogonal to `E`. Thus `w=t e_0+y` gives a dual-feasible point in (4.3), proving
\[
a_E\ge\mathfrak f(a_F).
\]
Applying the decreasing involution `f` gives `f(a_E)<=a_F`; combine with (4.4). QED.

The unique positive fixed point of `f` is
\[
\boxed{a_*=\frac1{\sqrt n-1}.}
\tag{4.5}
\]
For the Paley halves, (4.2) recovers and conceptually explains the earlier relation between `a_N` and `a_S`. Using (2.3), the fixed point corresponds exactly to
\[
\boxed{T=\sqrt n.}
\tag{4.6}
\]
Thus the source asymptotic is a statement that the deterministic Paley complementary pair approaches the **self-dual radial point**.

### The critical cone becomes an orthant

For `a>1/(n-1)` and `i=1,...,n-1`, define the centered generators
\[
\boxed{
g_i(a)=e_i+a e_0-\frac{1+a}{n}\mathbf1\in H.
}
\tag{4.7}
\]
Because the ray in (2.2) always contains the baseline point `a=1/(n-1)`, convexity gives
\[
\boxed{
a_E\ge a
\iff
F\cap\operatorname{pos}\{g_1(a),\ldots,g_{n-1}(a)\}\ne\{0\}.
}
\tag{4.8}
\]
A direct inner-product calculation gives
\[
\boxed{
\langle g_i(a),g_j(a)\rangle
=\delta_{ij}+\tau(a),
\qquad
\tau(a)=\frac{(n-1)a^2-2a-1}{n}.
}
\tag{4.9}
\]
At the self-dual point (4.5), `tau(a_*)=0`. Therefore
\[
\boxed{g_1(a_*),\ldots,g_{n-1}(a_*)\text{ are an orthonormal basis of }H.}
\tag{4.10}
\]
So the source problem sits exactly at a deformation through a **positive orthant**.

There is an explicit orthogonal transform. Let
\[
u=n^{-1/2}\mathbf1,
\qquad
v=e_0-u.
\]
The orthogonal matrix whose first column is `u` and whose remaining columns are `g_i(a_*)` is the symmetric Householder reflection
\[
\boxed{
\mathcal H=I-2\frac{vv^T}{\|v\|^2},
\qquad
\mathcal H e_0=u.
}
\tag{4.11}
\]
Thus the critical Paley question is not an abstract projected-simplex event: after one explicit rank-one orthogonal change of coordinates it is an orthant-intersection question for a half-Fourier subspace.

Finally, if `T=n a/(1+a)`, then (4.9) simplifies to
\[
\boxed{
\tau(a)=\frac{T^2-n}{(n-T)^2}.
}
\tag{4.12}
\]
Hence
\[
\boxed{
T\sim\sqrt n
\iff
n\,\tau(a)\to0.
}
\tag{4.13}
\]
This is a sharper geometric normalization of the remaining asymptotic: the Paley subspace's cone-intersection threshold has to occur at pairwise generator correlation `o(1/n)` around the orthant.

---

## 5. The exact Gaussian/Haar random analogue is a known Gaussian-polytope absorption problem

The self-dual constant `1` is not merely numerically plausible. It is the exact critical constant for a random projection of a regular simplex.

Let `E` be Haar-random of dimension `d` in `H`, and define the random radial depth `A_{n,d}=a_E`.

A convenient self-contained realization is obtained from an `n x d` iid standard Gaussian matrix `X`. Let
\[
C=I-\frac1n\mathbf1\mathbf1^T,
\qquad
CX=QR
\]
be a thin QR factorization. Then `col(Q)` is Haar in `H`, and the row points of `Q` are an invertible linear image of the centered Gaussian sample
\[
X_i-\bar X.
\]
Since radial depth is invariant under invertible affine transformations, this is precisely the Baryshnikov--Vitale regular-simplex/Gaussian-sample correspondence in the statistic needed here.

Fix `a>=a_*`. For iid `X_0,...,X_{n-1}~N(0,I_d)`, put
\[
Y_a=(1+a)\bar X-aX_0,
\qquad
D_i=X_i-Y_a\quad(i>0).
\]
Then `A_{n,d}>=a` is exactly the event
\[
0\in\operatorname{conv}(D_1,\ldots,D_{n-1}).
\tag{5.1}
\]
The vectors `D_i` are jointly Gaussian and an exact covariance calculation gives
\[
\boxed{
\operatorname{Cov}(D_i,D_j)
=(\delta_{ij}+\tau(a))I_d,
}
\tag{5.2}
\]
with the same `tau(a)` from (4.9).

For `a>=a_*`, `tau(a)>=0`, so one may represent
\[
D_i=G_i+\sqrt{\tau(a)}\,G_0
\]
with `G_0,G_1,...,G_{n-1}` independent standard Gaussians. Therefore
\[
\boxed{
\mathbb P[A_{n,d}<a]
=p_{n-1,d}(\tau(a)),
\qquad a\ge a_*,
}
\tag{5.3}
\]
where `p_{N,d}(sigma^2)` is exactly the Kabluchko--Zaporozhets Gaussian-polytope non-absorption probability
\[
\mathbb P[\sigma G_0\notin\operatorname{conv}(G_1,\ldots,G_N)].
\]
Their 2020 theorem gives an explicit nonasymptotic formula for this function in terms of conic intrinsic volumes / regular spherical simplex angles.

### The self-dual point reduces exactly to Wendel

At `a=a_*`, `tau=0`, so the `D_i` become iid standard Gaussians. Wendel's theorem gives
\[
\boxed{
\mathbb P[A_{n,d}\ge a_*]
=1-2^{-(n-2)}\sum_{j=0}^{d-1}\binom{n-2}{j}.
}
\tag{5.4}
\]
For the two dimensions matching the Paley halves (with `n` even), let
\[
q_n=2^{-(n-2)}\binom{n-2}{(n-2)/2}.
\]
Then
\[
\boxed{
\mathbb P[A_{n,n/2}\ge a_*]
=\frac12-\frac{q_n}{2},
}
\tag{5.5}
\]
while
\[
\boxed{
\mathbb P[A_{n,n/2-1}\ge a_*]
=\frac12+\frac{q_n}{2}.
}
\tag{5.6}
\]
Since
\[
q_n\sim\sqrt{\frac{2}{\pi n}},
\qquad
\sqrt n\,a_*=\frac{\sqrt n}{\sqrt n-1}=1+O(n^{-1/2}),
\]
the conjectured constant `1` is exactly the random-projection self-dual threshold constant.

This is not a proof about the deterministic Paley subspace. It is, however, an exact solved comparison model, not a heuristic analogy.

The same framework gives the full random distribution: above the critical point use the explicit Kabluchko--Zaporozhets function in (5.3); below the critical point use the complementary-subspace involution (4.2) and the corresponding dimension `n-1-d`. Thus the random analogue is reduced completely to published Gaussian-polytope absorption probabilities.

---

## 6. #28 REPLACE “FOR ALL” WITH “FOR TYPICAL” — what worked, and why naive typicality is not enough

This move produced both a positive model and a precise warning.

**What worked.** The random/Haar analogue lands on the same constant `1` for an exact structural reason: at `a_*` the cone generators are orthonormal, the Gaussian differences decorrelate, and Wendel's formula sits exactly at the half-dimensional convex-hull threshold. This is a substantially better explanation for the constant than the earlier one-point Jacobi endpoint calculations.

**What fails.** At the exact critical point, the favorable random event has probability tending to `1/2`, not to `1`. Therefore a proof of the form “the Paley half-Fourier projection is typical enough that every high-probability Haar property transfers” cannot decide even the sign of `a_E-a_*` at criticality. Indeed the exact complementary duality forces the two halves to lie on opposite sides of the self-dual point unless equality occurs.

That is not a problem for the source conjecture: it needs both depths to be **within `o(1/sqrt(n))` of the self-dual point**, not to lie on one prescribed side. The right random comparison is therefore a **critical-window concentration/universality statement**, not a high-probability sign statement.

The current numerical hierarchy reinforces the same diagnosis. At `p=1213`, fixed-degree scalar profiles through degree 15 still reach only about `0.816` (`N`) and `0.792` (`S`) after multiplying by `sqrt(n)`, while the full floating radial optima are already near `1`. Matching finitely many low-degree additive/Jacobi statistics is therefore unlikely to be enough by itself.

The clean next mathematical target is now:

> Determine the high-dimensional critical window of `p_{n-1,d}(tau)` for `d=n/2+O(1)` and `tau=O(1/n)` from the Kabluchko--Zaporozhets formula, then identify a deterministic Paley statement strong enough to force the same `o(1/n)` cone-correlation crossing window.

Equivalently, with
\[
x=T_p/\sqrt n,
\]
(4.12) gives
\[
\tau=\frac{n(x^2-1)}{(n-\sqrt n\,x)^2}
=\frac{x^2-1}{n}+O(n^{-3/2})
\]
for bounded `x`. The source conjecture is precisely the statement that the Paley crossing occurs in the vanishing `x^2-1=o(1)` window around the random self-dual transition.

---

## 7. Prior-art boundary

Dated searches this run included variants of

- `Randomstrasse Conjecture 26 Paley one localization theta sqrt p/2`;
- `regular simplices Gaussian samples random projection`;
- `Wendel convex hull Gaussian formula`;
- `Gaussian polytope absorption sigma X convex hull`;
- `maximum barycentric coordinate Gaussian sample mean convex hull`;
- `1/(sqrt(n)-1) simplex projection convex hull Gaussian`.

Relevant established results recovered:

1. Y. Baryshnikov and R. Vitale, *Regular simplices and Gaussian samples*, Discrete Comput. Geom. 11 (1994), 141--147, DOI 10.1007/BF02574000: random projections of a regular simplex are affine-equivalent to Gaussian samples for affine-invariant statistics.
2. J. G. Wendel, *A Problem in Geometric Probability*, Math. Scand. 11 (1962), 109--112: exact probability that the origin is outside the convex hull of a centrally symmetric iid sample.
3. Z. Kabluchko and D. Zaporozhets, *Absorption probabilities for Gaussian polytopes and regular spherical simplices*, Adv. Appl. Probab. 52 (2020), 588--616, DOI 10.1017/apr.2020.7: exact non-absorption probability for `sigma X` in a Gaussian polytope, including Wendel at `sigma=0`.

I found no bounded-search source spelling out the particular R20 chain

`Paley Chebyshev radial depth -> complementary involution -> self-dual depth 1/(sqrt(n)-1) -> orthant/Householder transform -> Kabluchko--Zaporozhets parameter tau=(T^2-n)/(n-T)^2`.

That absence is **not** a novelty certificate. The Gaussian/simplex and Wendel/Kabluchko--Zaporozhets ingredients themselves are established prior art; only the application/synthesis here is being recorded as a self-check candidate mechanism pending a real prior-art audit.

---

## 8. Artifacts and validation budget

The only new code in this run is explicitly discovery-only:

- `artifacts/R20/i0100_random_projection_poly_discovery_20260917.py`
- `artifacts/R20/i0100_random_projection_poly_discovery_20260917.out`

The script says `DISCOVERY_ONLY_NO_CERTIFICATE` and uses floating FFT/LP/QR. It is **not** evidence for the exact prime metric and is not cited as proof of any finite theorem.

The theorem-sized claims `R20-POLYHIER1`, `R20-COMP1`, and the cone/random-distribution reduction have complete proofs on this page. Their audit state is **SELF_CHECK_ONLY**.

Existing independent finite-case audits are preserved:

- `R19-AUDIT-R20-I0100-P181-01 = PASS_EXACT_FINITE_CASE`;
- `P26-AUDIT-R20-I0100-P181-FOURIER-DUAL-ENDTOEND-18 = PASS_FULL_FINITE_PROOF / CLAIM_SCOPED / SOURCE_PARTIAL_OPEN`;
- `P26-RECONCILE-R20-I0100-P181-2OF2-18 = PASS`;
- `R19-AUDIT-R20-I0100-P241-02 = PASS_EXACT_FINITE_CASE`;
- `P26-AUDIT-R20-I0100-P241-FOURIER-DUAL-ENDTOEND-22 = PASS_FULL_FINITE_PROOF`;
- the corresponding P26 `p=241` reconciliation records the finite theorem as 2/2 outside-audited.

None of those audits establishes Conjecture 26, and none audits the new asymptotic mechanism in this report.

---

## 9. Structured ledger delta

```yaml
ledger_delta:
  track: R20
  source: "Afonso S. Bandeira et al., Randomstrasse101 (2025), Conjecture 26 / I0100"
  source_target: "theta(complement G_{p,1}) ~ sqrt(p/2)"
  graph_normalization: "G_{p,1}=Cay(Z_n,S), n=(p-1)/2, S={d != 0: alpha^d-1 is a nonzero square}"
  metric: "largest admissible prime with matching exact primal/dual source-normalized theta certificates"
  metric_before: 1213
  metric_after: 1213
  covered_primes: [5,13,17,29,41,181,241,317,421,541,601,661,1009,1021,1033,1049,1061,1093,1201,1213]
  status: PARTIAL
  source_status: OPEN
  unchanged_count_before: 0
  unchanged_count_after: 1
  tried_moves: [8,17,28]
  move_results:
    8: "R20-POLYHIER1: exact all-degree balanced polynomial hierarchy; degree r correction is the centered r-fold additive representation count on the Fourier half"
    17: "R20-COMP1 plus self-dual cone: a_F=(1+a_E)/((n-1)a_E-1); critical a*=1/(sqrt(n)-1) orthogonalizes the cone; random analogue reduces exactly to Gaussian-polytope absorption"
    28: "typical/Haar model explains constant 1 but critical event has probability ~1/2, so naive high-probability pseudorandom transfer cannot decide the Paley case"
  remaining_obligation: "prove the deterministic Paley complementary pair crosses the regular-cone family in an o(1/n) correlation window around the self-dual orthant; equivalently T_p/sqrt(n)->1"
  evidence:
    - "full written proofs R20-POLYHIER1 and R20-COMP1 on this report page"
    - "full written cone Gram/Householder and Gaussian covariance reductions on this report page"
    - "published Baryshnikov-Vitale / Wendel / Kabluchko-Zaporozhets results for the random comparison"
    - "discovery-only script/output, explicitly excluded from exact certificate evidence"
  audit_ids:
    - "R19-AUDIT-R20-I0100-P181-01=PASS_EXACT_FINITE_CASE"
    - "P26-AUDIT-R20-I0100-P181-FOURIER-DUAL-ENDTOEND-18=PASS_FULL_FINITE_PROOF"
    - "P26-RECONCILE-R20-I0100-P181-2OF2-18=PASS"
    - "R19-AUDIT-R20-I0100-P241-02=PASS_EXACT_FINITE_CASE"
    - "P26-AUDIT-R20-I0100-P241-FOURIER-DUAL-ENDTOEND-22=PASS_FULL_FINITE_PROOF"
  new_claim_audit_state: SELF_CHECK_ONLY
```

---

## 10. Next methods

The next run should not optimize another fixed-degree polynomial and should not chase another prime unless a new structural idea produces a candidate worth certifying.

Use second-pass methods:

- **#5 ADD A PARAMETER AND DIFFERENTIATE IN IT:** parameterize the regular cone by `tau` or `s=log(T/sqrt(n))`, where complementarity is `s -> -s`.
- **#7 TAKE THE LIMIT:** extract the `d=n/2+O(1)`, `tau=O(1/n)` critical-window asymptotic from the exact Kabluchko--Zaporozhets formula.
- **#10 DERANDOMIZE:** identify the weakest deterministic Fourier/character-sum statement that forces the Paley subspace to have the same near-orthant crossing window, without asking for full Paley RIP.

---

## 11. Model/scheduler control limitation

The limitation is still real in this run. The exposed scheduling surface provides prompt/title, schedule/timing, enabled state, and timing mode; it exposes **no native model-family selector, no reasoning-effort selector, no authenticated completed-run model-routing receipt, and no guaranteed hour-long execution field**. Thus GPT-6 / maximum remains prompt-only and actual reasoning metadata are UNVERIFIED.

The historical P26 scheduler ID that returned `You cannot modify this task` was an ownership/context boundary. Repository receipts show that another authorized context later updated P26 successfully. The legitimate workaround is therefore an authorized owning product/workspace context or a platform/API surface that actually exposes those controls, not a duplicate task or a permission bypass. No scheduler change was attempted here.

**NO CLOSURE CLAIM.**
