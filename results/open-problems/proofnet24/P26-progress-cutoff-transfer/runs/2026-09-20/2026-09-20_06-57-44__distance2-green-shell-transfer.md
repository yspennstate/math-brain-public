Model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — GPT-6/maximum was requested, but authenticated runtime metadata does not establish that setting, so I do not claim otherwise.

# P26 / LIVE20 T08 — collision-Green shell transfer and exact-distance-two cutoff outside long-range expansion

**Status:** `CANDIDATE_FULL` for the restricted Green/shell transfer theorem and the exact-distance-two application proved below, pending later independent review; **PARTIAL / OPEN** for Salez Problem 2.3. Worldwide publication novelty is **UNVERIFIED**.

Repository/branch: `yspennstate/math-open-problems` / `master`.  
Controlling policy: `operations/PROGRESS20_2026-09-20.md`.  
Report root: `proofnet24/P26-progress-cutoff-transfer/runs/2026-09-20/`.

## 0. Compact handoff and division of labor with the historical C28 route

The preceding P26 runs established, in the exact rate-one continuous-time convention, cutoff transfer for line graphs, fixed finite fibers, ordinary graph squares, and then fixed same-vertex distance-set graphs `X_J(G)` under the hypothesis `1 in J`.  The newest P26 report is

`proofnet24/P26-progress-cutoff-transfer/runs/2026-09-20/2026-09-20_05-56-17__distance-set-shell-profile-transfer.md`.

It proved a shell-entropy Gaussian-profile criterion and applied it to `J={1,3}` on a degree-six LPS family.  The point of `1 in J` there was not shell geometry; it supplied the output spectral gap for free by Dirichlet-form domination from the base edges.

The live successor of historical C28 is `NM13-01`.  Its newest relevant report is

`proofnet24/NM13-01/progress-cutoff/runs/2026-09-20/2026-09-20T03-03-00Z__strong-product-nbrw-trace-cutoff.md`.

That report proves the exact vertex-transitive NBRW collision identity

\[
\chi^2(K_r(x,\cdot)\|\pi)
=
\sum_{i=2}^n p_r(\lambda_i)^2,
\tag{0.1}
\]

and a direct cutoff criterion for the original graph when this trace is polylogarithmic at the entropic radius.  It also proves a strong-product graph class.  I do not duplicate either class here.

The division of labor is now precise:

* `NM13-01` owns the **direct transitivity-to-NBRW-trace / empirical-spectrum route**;
* P26 owns **transfer of shell entropy/collision information through a different continuous-time walk**, with explicit radial clocks and output spectral-gap certification.

This run combines those two viewpoints only at the interface (0.1): it removes P26's old `1 in J` restriction by replacing edge containment with an exact distance-polynomial spectral calculation, and it applies the resulting Green/shell criterion to the **exact-distance-two graph**, not to a square, product, fiber, truncation, or strong product.

A neighboring PROB10-08 run has also produced a useful stress test: a source-admissible affine transitive expander whose actual continuous-time heat kernel has a polynomial `chi^2` excess at the tree/Ramanujan TV scale.  Thus a general proof of Salez 2.3 cannot simply demand heat-kernel `L^2` mixing at the TV cutoff scale.  The criterion below deliberately asks only for **NBRW shell collision/entropy**, which can be small even when unrelated global `L^2` modes are problematic.

## 1. Exact source convention and fresh scope boundary

Justin Salez, arXiv:2508.21055v1 (28 August 2025), defines continuous time by independent mean-one exponential holding times.  If `P` is the discrete transition matrix, the semigroup is exactly

\[
H_t=e^{t(P-I)}
=
e^{-t}\sum_{k\ge0}\frac{t^kP^k}{k!}.
\tag{1.1}
\]

Problem 2.3 in those notes is:

> Prove that all vertex-transitive expanders exhibit cutoff.

Here expanders have diverging size, uniformly bounded degree, and spectral gaps bounded away from zero.

Fresh scope checks on 20 September 2026 give the following boundary.

1. **Altschuler, arXiv:2609.14945v1, submitted 14 September 2026.**  Every fixed-degree long-range-expander sequence has cutoff with the tree/Ramanujan Gaussian profile.  The same paper proves the strict hierarchy
   \[
   \text{Ramanujan}\Longrightarrow\text{long-range expansion}
   \Longrightarrow\text{spectral expansion},
   \]
   with neither converse.  Long-range expansion is therefore not synonymous with Salez's spectral-expansion hypothesis.
2. **Pedrotti--Salez, arXiv:2607.05345, 6 July 2026.**  The local-product/non-equilibrium-Poincare method bounds cutoff windows in terms of their `gamma_*`; no checked theorem derives the required `gamma_*` control from vertex transitivity plus an ordinary spectral gap alone.
3. A bounded fresh search for `distance-two graph random walk cutoff`, `distance-2 Ramanujan cutoff`, and `exact distance graph cutoff` found distance-regular/distance-graph literature but no theorem matching the exact continuous-time result proved below.  This is negative search evidence only, not a novelty certificate.

The explicit input family below is classical Lubotzky--Phillips--Sarnak: fixed-degree Ramanujan Cayley graphs with logarithmically growing girth.  For degree six one may fix `p=5` and take a non-bipartite `PSL_2(F_\ell)` subfamily with `\ell` in an infinite admissible congruence class (for example primes `\ell=1 mod 20`).  Only the standard properties Ramanujan + non-bipartite + Cayley + girth tending to infinity are used.

## 2. Parent problem before / after

### Before

Salez Problem 2.3 was `OPEN`.  P26 already had several explicit spectral-but-not-long-range transitive cutoff classes, but its general same-vertex distance-set theorem required `1 in J` to transfer a spectral gap.  In particular it did **not** cover the pure exact-distance-two walk.

### After

Salez Problem 2.3 remains `OPEN`, but the proved source-compatible scope increases:

> **Exact-distance-two theorem.**  
> Let `(G_n)` be a fixed-degree, non-bipartite, vertex-transitive Ramanujan family with girth tending to infinity.  Let `Y_n` have the same vertex set, with two vertices adjacent iff their distance in `G_n` is exactly two.  Then the rate-one continuous-time SRW on `(Y_n)` is a bounded-degree vertex-transitive spectral-expander sequence with Gaussian total-variation cutoff in a `Theta(sqrt(log n))` window.  The sequence `(Y_n)` fails every fixed long-range-expansion constant.

For the degree-six LPS family the output degree is `30`, the cutoff center is

\[
\boxed{
T_n=\frac58\log_5 n+O(1),
}
\tag{2.1}
\]

and, for fixed `z`,

\[
\boxed{
d_{\rm TV}\!\left(
T_n+z\sqrt{\log_5 n}
\right)
\longrightarrow
\Phi\!\left(-z\sqrt{\frac{384}{325}}\right).
}
\tag{2.2}
\]

This is a parent-class theorem gain.  The exact checker below is only a sanity check and is not counted as movement.

## 3. A collision-Green shell transfer criterion

Let `G_n` be `d`-regular vertex-transitive graphs, `q=d-1`, with uniform stationary law `pi_n`.  Let `K_r(x,.)` be the endpoint law of length-`r` nonbacktracking walk started from `x` (uniform first edge, then uniform nonbacktracking choices).

Define the vertex-transitive collision statistic

\[
\mathcal C_{n,r}
:=
n\sum_y K_r(x,y)^2-1.
\tag{3.1}
\]

Vertex transitivity makes it independent of `x`.  It is a Green/collision quantity: if `Y_r,Y'_r` are independent NBRWs from the same start,

\[
1+\mathcal C_{n,r}
=
n\,\Pr(Y_r=Y'_r).
\tag{3.2}
\]

For any probability law `mu` on an `n`-point uniform space,

\[
D(\mu\|\pi)
\le
\log(1+\chi^2(\mu\|\pi)).
\tag{3.3}
\]

Thus

\[
D(K_r(x,\cdot)\|\pi_n)
\le
\log(1+\mathcal C_{n,r}).
\tag{3.4}
\]

Now let `X_n` be another regular vertex-transitive graph on the same state space, with rate-one continuous-time semigroup `H_t^X` and spectral gap at least `eta>0`.

### Theorem 3.1 — collision-Green shell/profile transfer

Assume there is a radial process `R_t` and radii `L_n -> infinity` such that, exactly,

\[
\delta_xH_t^X
=
\sum_r \Pr(R_t=r)K_r(x,\cdot)
\tag{3.5}
\]

for every `x,t`.  Assume further:

1. **Green/collision front.**  With
   \[
   g_n:=
   \sup_{r\ge L_n}\log(1+\mathcal C_{n,r}),
   \tag{3.6}
   \]
   we have
   \[
   g_n=o(\sqrt{L_n}).
   \tag{3.7}
   \]
2. **Radial CLT.**  For fixed constants `v>0`, `sigma^2>0`,
   \[
   \frac{R_t-vt}{\sqrt{\sigma^2 t}}
   \Longrightarrow N(0,1)
   \tag{3.8}
   \]
   uniformly for
   \[
   t=L_n/v+O(\sqrt{L_n}).
   \]
3. **Sub-front support is negligible.**  For every `h_n -> infinity` with
   `h_n=o(sqrt(L_n))`, the union of supports of `K_r(x,.)`, `r<=L_n-h_n`, has stationary mass `o(1)`.

Then, putting

\[
T_n=\frac{L_n}{v},
\qquad
\tau=\frac{\sqrt{\sigma^2}}{v^{3/2}},
\tag{3.9}
\]

one has, for every fixed real `z`,

\[
\boxed{
\left\|
\delta_xH_{T_n+z\sqrt{L_n}}^X-\pi_n
\right\|_{\rm TV}
\longrightarrow
\Phi(-z/\tau).
}
\tag{3.10}
\]

In particular `X_n` has cutoff with `Theta(sqrt(L_n))` window.

### Proof

The entropy-cleanup estimate is the exact continuous-time estimate already used by P26 and NM13-01.  For any initial law `mu` on `X_n`,

\[
\boxed{
\|\mu H_s^X-\pi_n\|_{\rm TV}
\le
\sqrt{
\frac{D(\mu\|\pi_n)}{4\eta s}
}.
}
\tag{3.11}
\]

Indeed, if `f_s=d(mu H_s^X)/d pi`, then entropy dissipation and
`(a-b)(log a-log b)>=4(sqrt a-sqrt b)^2` give

\[
-\frac d{ds}D(\mu H_s^X\|\pi)
\ge
4\eta\,\operatorname{Var}_\pi(\sqrt{f_s}),
\]

while `TV^2 <= Var_pi(sqrt(f_s))`; integrate and use monotonicity of TV.

Choose `s_n` so that

\[
g_n\ll s_n\ll\sqrt{L_n}.
\tag{3.12}
\]

At time `t-s_n`, use the exact mixture (3.5), split at `L_n`, and run `X_n` for the remaining `s_n`.  Equations (3.4), (3.11), and convexity of TV yield

\[
\|\delta_xH_t^X-\pi_n\|_{\rm TV}
\le
\Pr(R_{t-s_n}<L_n)
+
\sqrt{\frac{g_n}{4\eta s_n}}.
\tag{3.13}
\]

The second term is `o(1)` and `s_n=o(sqrt(L_n))`.  The radial CLT therefore gives

\[
\limsup_n d_n(T_n+z\sqrt{L_n})
\le
\Phi(-z/\tau).
\tag{3.14}
\]

For the reverse inequality choose `h_n -> infinity`, `h_n=o(sqrt(L_n))`, and let `A_n` be the union of the shell supports up to `L_n-h_n`.  By assumption 3,

\[
\pi_n(A_n)=o(1),
\]

whereas

\[
\delta_xH_t^X(A_n)
\ge
\Pr(R_t\le L_n-h_n).
\]

The CLT and the negligible `h_n` shift give

\[
\liminf_n d_n(T_n+z\sqrt{L_n})
\ge
\Phi(-z/\tau).
\tag{3.15}
\]

This proves (3.10). `QED`

The mechanism differs from a global heat-kernel `L^2` criterion: only collision of the **shell endpoint law** is used, and the final cleanup is allowed a vanishingly small fraction of the `sqrt(log n)` radial window.

## 4. Exact-distance-two graphs: removing the old `1 in J` hypothesis

Let `G` be `d`-regular with girth greater than four.  Write `A` for its adjacency matrix and `P=A/d`.  Define `Y=G^{[2]}` on the same vertices by

\[
x\sim_Y y
\iff
d_G(x,y)=2.
\tag{4.1}
\]

Because there are no triangles or four-cycles, every length-two nonbacktracking path has a unique endpoint at distance exactly two.  Therefore

\[
A_Y=A^2-dI
\tag{4.2}
\]

and

\[
D:=\deg(Y)=d(d-1)=dq.
\tag{4.3}
\]

The discrete SRW kernel on `Y` is exactly

\[
\boxed{
Q
=
\frac{A^2-dI}{d(d-1)}
=
\frac{dP^2-I}{d-1}.
}
\tag{4.4}
\]

This is where the present run departs from the previous distance-set theorem: `Y` contains **no base edges**, so Dirichlet domination by `P` is unavailable.  Instead we use the exact spectral image.

If `lambda` is a normalized eigenvalue of `P`, then the corresponding `Q` eigenvalue is

\[
\psi_2(\lambda)
=
\frac{d\lambda^2-1}{d-1}.
\tag{4.5}
\]

Suppose `G` is non-bipartite Ramanujan.  Every nontrivial normalized eigenvalue satisfies

\[
|\lambda|
\le
\rho_d:=\frac{2\sqrt{d-1}}d.
\tag{4.6}
\]

Hence

\[
\lambda_2(Q)
\le
\frac{d\rho_d^2-1}{d-1}
=
\frac{3d-4}{d(d-1)}
\tag{4.7}
\]

and so

\[
\boxed{
\operatorname{gap}(Y)
\ge
\frac{(d-2)^2}{d(d-1)}.
}
\tag{4.8}
\]

Also, `psi_2(lambda)=1` is equivalent to `lambda^2=1`.  Connectedness gives `lambda=1` simple and non-bipartiteness excludes `lambda=-1`, so `Y` is connected.

Vertex transitivity passes because every automorphism of `G` preserves graph distance.  If `G` is Cayley, `Y` is again Cayley, with generating set the exact word sphere of radius two.

Thus the missing spectral-gap transfer has been supplied without adding distance-one edges.

## 5. A direct Ramanujan bound for the NBRW collision front

The NM13-01 identity (0.1) reduces the shell collision to a polynomial spectral trace.  For completeness, the short transitivity argument is reproduced here.  The NBRW endpoint matrix is a polynomial `K_r=p_r(P)`, hence symmetric and automorphism-invariant.  Therefore `K_r^2` has constant diagonal on a vertex-transitive graph and

\[
n\sum_y K_r(x,y)^2
=
n(K_r^2)(x,x)
=
\operatorname{tr}(K_r^2).
\]

Diagonalizing `P` and using `p_r(1)=1` gives

\[
\boxed{
\mathcal C_{n,r}
=
\sum_{i=2}^n p_r(\lambda_i)^2.
}
\tag{5.0}
\]

For the present application, this trace can be bounded explicitly.

Let `M_r` be the matrix counting nonbacktracking paths of length `r`.  With `q=d-1`,

\[
M_0=I,\qquad M_1=A,\qquad M_2=A^2-dI,
\]

and for `r>=3`,

\[
M_r=AM_{r-1}-qM_{r-2}.
\tag{5.1}
\]

For `r>=1` the endpoint kernel is

\[
K_r=\frac{M_r}{dq^{r-1}}.
\tag{5.2}
\]

If `a` is an adjacency eigenvalue and `x=a/(2\sqrt q)`, the recurrence gives the exact Chebyshev formula

\[
M_r(a)
=
q^{r/2}
\left(
U_r(x)-q^{-1}U_{r-2}(x)
\right),
\tag{5.3}
\]

with the usual convention `U_{-1}=0`.

For a nontrivial Ramanujan eigenvalue, `|x|<=1` and

\[
|U_k(x)|\le k+1.
\]

Therefore the normalized NBRW multiplier satisfies

\[
\begin{aligned}
|p_r(\lambda)|
&=
\frac{|M_r(d\lambda)|}{dq^{r-1}}\\
&\le
\frac{
q^{r/2}\left((r+1)+q^{-1}(r-1)\right)
}{
(q+1)q^{r-1}
}\\
&\le
(r+1)q^{-r/2}.
\end{aligned}
\tag{5.4}
\]

By (5.0),

\[
\boxed{
\mathcal C_{n,r}
\le
(n-1)(r+1)^2q^{-r}.
}
\tag{5.5}
\]

Let

\[
j_n
:=
\min\{r\ge1:dq^{r-1}\ge n\}
=
\log_q n+O_d(1).
\tag{5.6}
\]

Since `nq^{-j_n}<=d/q`, and the factor `(r+1)^2q^{-(r-j_n)}` is uniformly `O((j_n+1)^2)` for `r>=j_n`,

\[
\sup_{r\ge j_n}\mathcal C_{n,r}
=
O_d((\log n)^2).
\tag{5.7}
\]

Consequently

\[
\boxed{
\sup_{r\ge j_n}
D(K_r(x,\cdot)\|\pi)
=
O(\log\log n).
}
\tag{5.8}
\]

This is the required collision-Green front.  Notice that no long-range expansion of the **output graph** has entered.

## 6. Exact shell representation and radial CLT for the distance-two walk

Let `T_d` be the `d`-regular tree.  Its exact-distance-two graph has two parity components; start in the even component at a root `o`.

For a high-girth base `G`, the universal covering map induces a graph covering from this component to `Y=G^{[2]}`.  Lift the rate-one continuous-time SRW on `Y` to the tree distance-two graph and set

\[
R_t=d_{T_d}(o,\widetilde X_t).
\tag{6.1}
\]

The root stabilizer of `T_d` acts transitively on every ordinary tree sphere and preserves the distance-two walk.  Conditional on `R_t=r`, the lifted endpoint is therefore uniform on the sphere of radius `r`.  Projecting that sphere to `G` is exactly the length-`r` NBRW endpoint law.  Hence

\[
\boxed{
\delta_xH_t^Y
=
\sum_{\substack{r\ge0\\ r\ {\rm even}}}
\Pr(R_t=r)K_r(x,\cdot).
}
\tag{6.2}
\]

This is the exact continuous-time shell transfer.

### 6.1 Interior radial increments

Suppose `R_t=r>=2`.  An exact-distance-two jump has `dq` possible destinations.  Relative to the root, their increment counts are

\[
\begin{array}{c|ccc}
\Delta R & -2 & 0 & +2\\ \hline
\#       & 1  & q-1 & q^2 .
\end{array}
\tag{6.3}
\]

Thus, away from the root,

\[
\Pr(\xi=2)=\frac qd,\qquad
\Pr(\xi=0)=\frac{q-1}{dq},\qquad
\Pr(\xi=-2)=\frac1{dq}.
\tag{6.4}
\]

The drift per rate-one Poisson event is

\[
\boxed{
v_2=\mathbb E\xi
=
\frac{2(q^2-1)}{dq}
=
\frac{2(d-2)}{d-1},
}
\tag{6.5}
\]

and the compound-Poisson variance rate is

\[
\boxed{
\sigma_2^2=\mathbb E\xi^2
=
\frac{4(q^2+1)}{dq}.
}
\tag{6.6}
\]

At the root the next jump goes deterministically to radius two.

### 6.2 Boundary correction is tight

Write `S=R/2`.  Away from zero the birth, hold and death probabilities are

\[
a=\frac qd,\qquad
b=\frac{q-1}{dq},\qquad
c=\frac1{dq}.
\]

Ignoring holds, the probability starting from `1` ever to hit `0` is

\[
\frac ca=\frac1{q^2}<1.
\tag{6.7}
\]

Hence the total number of returns to the root has a geometric tail.  The difference between `R_t` and the unconstrained compound-Poisson sum of iid increments (6.4) is therefore `O_P(1)`.

The ordinary compound-Poisson CLT now gives, uniformly for `t` in an `O(sqrt(L))` window about `L/v_2`,

\[
\boxed{
\frac{R_t-v_2t}{\sqrt{\sigma_2^2 t}}
\Longrightarrow N(0,1).
}
\tag{6.8}
\]

This supplies Theorem 3.1's radial input.

## 7. The distance-two cutoff theorem

Take a non-bipartite `d`-regular vertex-transitive Ramanujan family `(G_n)` with girth tending to infinity.  For all sufficiently large `n`, form `Y_n=G_n^{[2]}`.

Let `L_n` be the smallest even integer at least `j_n`.  Then

\[
L_n=\log_q n+O_d(1).
\tag{7.1}
\]

Sections 4--6 verify the hypotheses of Theorem 3.1:

* output gap at least `(d-2)^2/[d(d-1)]`;
* shell collision entropy `g_n=O(log log n)=o(sqrt(L_n))`;
* exact shell representation (6.2);
* radial CLT with `(v_2,sigma_2^2)`;
* lower support: a shell `K_r(x,.)` lies inside the base ball `B_G(x,r)`, so for `h_n->infinity`,
  \[
  \pi\!\left(B_G(x,L_n-h_n)\right)
  \le
  C_d\frac{q^{L_n-h_n}}n
  =o(1).
  \]

Therefore

\[
\boxed{
T_n
=
\frac{L_n}{v_2}
=
\frac{d-1}{2(d-2)}
\log_{d-1}n+O_d(1)
}
\tag{7.2}
\]

and, with

\[
\boxed{
\tau_2^2
=
\frac{\sigma_2^2}{v_2^3},
}
\tag{7.3}
\]

the exact rate-one continuous-time walk satisfies

\[
\boxed{
d_{\rm TV}\!\left(
T_n+z\sqrt{L_n}
\right)
\longrightarrow
\Phi(-z/\tau_2).
}
\tag{7.4}
\]

This proves cutoff with a `Theta(sqrt(log n))` window.

No discrete-time convention is substituted at any point: the radial variance in (6.6) is the **compound-Poisson variance rate**, and (3.11) is for the rate-one semigroup generated by `Q-I`.

## 8. Concrete new class: degree-30 Cayley expanders

Take the standard non-bipartite degree-six LPS Ramanujan Cayley family.  Here

\[
d=6,\qquad q=5,\qquad D=30.
\]

The output spectral gap from (4.8) is

\[
\boxed{\operatorname{gap}(Y_n)\ge\frac8{15}.}
\tag{8.1}
\]

The radial constants are

\[
\boxed{
v_2=\frac85,\qquad
\sigma_2^2=\frac{52}{15},\qquad
\tau_2^2=\frac{325}{384}.
}
\tag{8.2}
\]

Therefore

\[
\boxed{
T_n=\frac58\log_5 n+O(1),
}
\]

and

\[
\boxed{
d_{\rm TV}\!\left(
T_n+z\sqrt{\log_5 n}
\right)
\to
\Phi\!\left(-z\sqrt{\frac{384}{325}}\right).
}
\tag{8.3}
\]

The outputs are 30-regular vertex-transitive Cayley spectral expanders.  They are distinct from P26's degree-36 graph squares (`distances {1,2}`) and degree-156 `{1,3}` graphs: this walk has **only exact-distance-two moves**, so the previous `1 in J` theorem did not cover it.

### 8.1 The output is not long-range expanding

An output step moves at most two base edges, so

\[
B_{Y_n}(x,r)\subseteq B_{G_n}(x,2r).
\tag{8.4}
\]

The base tree bound yields

\[
|B_{Y_n}(x,r)|
\le
C_d q^{2r}.
\tag{8.5}
\]

For degree `D=dq`, the long-range tree benchmark is `(D-1)^r`.  But

\[
q^2=(d-1)^2<d(d-1)-1=D-1
\qquad(d\ge3).
\tag{8.6}
\]

Choose

\[
r_n=\left\lfloor\frac12\log_{D-1}n\right\rfloor.
\]

At this radius `(D-1)^{r_n}=Theta(sqrt n)`, safely below the macroscopic saturation term in the LRE definition, while

\[
\frac{|B_{Y_n}(x,r_n)|}{(D-1)^{r_n}}
\le
C_d
\left(
\frac{q^2}{D-1}
\right)^{r_n}
\longrightarrow0.
\tag{8.7}
\]

So no fixed positive long-range-expansion constant can hold.

For `d=6`, the strict branching ratio is

\[
\frac{25}{29}<1.
\]

Thus this application is explicitly **spectral but not long-range**, exactly separating Salez's source hypothesis from Altschuler's sufficient hypothesis.

A direct spectral sanity check also shows why this is not merely a degree-30 Ramanujan example: the transformed base Ramanujan edge tends to `7/15`, whereas the degree-30 Ramanujan edge is `sqrt(29)/15`, and `7^2>29`.

## 9. Essential exact sanity check

I executed one exact-arithmetic checker, not a certificate factory:

`proofnet24/P26-progress-cutoff-transfer/artifacts/2026-09-20/2026-09-20_06-57-44__distance2_green_transfer_exact.py`

with archived output

`proofnet24/P26-progress-cutoff-transfer/artifacts/2026-09-20/2026-09-20_06-57-44__distance2_green_transfer_exact.out`.

It verifies:

1. on the Petersen graph (girth five), `A_[2]=A^2-3I` is exactly the distance-two adjacency matrix, has degree six, is connected, and satisfies the normalized kernel identity (4.4);
2. for `3<=d<=50`, the algebraic gap identity
   \[
   1-\frac{3d-4}{d(d-1)}
   =
   \frac{(d-2)^2}{d(d-1)}
   \]
   and strict branching mismatch `(d-1)^2<d(d-1)-1`;
3. the degree-six constants
   \[
   8/15,\quad 8/5,\quad 52/15,\quad 325/384,\quad 5/8,\quad25/29;
   \]
4. the direct degree-30 non-Ramanujan edge separation `7^2>29`.

The executed output ends

`P26_T08_DISTANCE2_GREEN_TRANSFER_EXACT_PASS`.

The checker does not certify the asymptotic theorem; that proof is on the page above.

## 10. What was learned, what remains, and the next attack

### Mechanism-level advance

The previous P26 distance-set proof had a real structural restriction: `1 in J` was what supplied the spectral gap.  This run removes that restriction in a nontrivial source-valid case by combining:

1. an exact **distance-polynomial spectral image** for the output gap;
2. a **collision-Green shell criterion** requiring only
   \[
   \log(1+\mathcal C_{n,r})=o(\sqrt{\log n})
   \]
   at the radial front;
3. an explicit NBRW Chebyshev estimate giving `C_{n,r}=O((log n)^2)` on Ramanujan bases;
4. a new radial clock for exact-distance-two moves.

This is not an unchanged check or an auxiliary constant: it produces the degree-30 non-LRE transitive cutoff class with a full profile.

### Residual parent obstruction

The parent conjecture remains open because the Ramanujan bound (5.4) is far stronger than what an arbitrary transitive spectral expander is known to provide.  NM13-01 has reduced that missing step to empirical NBRW spectral mass, while the affine PROB10-08 stress test shows that a global heat-kernel `L^2` substitute can fail badly at the relevant TV scale.

The sharp remaining question for this route is therefore:

\[
\text{When does vertex transitivity + expansion force }
\sup_{r\ge j_n}
\log\!\left(
1+\sum_{i=2}^n p_r(\lambda_i)^2
\right)
=o(\sqrt{\log n})?
\tag{10.1}
\]

No claim here proves (10.1) in full generality.

### Next P26 attack

Stay complementary to NM13-01.  Rather than duplicate its attempt to prove (10.1) directly from the empirical spectrum, P26 should next seek a **Green-shell comparison under sparse local rewiring**: prove that if two transitive kernels have universal-cover radial chains coupled within `o(sqrt(log n))` displacement and their shell collision profiles differ by at most `exp(o(sqrt(log n)))`, then cutoff/profile transfers.  The first target should be a non-polynomial Cayley generating set obtained by replacing only a fixed fraction of exact-distance-two generators, where no exact distance polynomial diagonalization survives.

If that comparison cannot control shell collision after two honest routes, the route should be recorded as failed and T08 should switch method rather than accumulate graph-power variants.

## 11. `ledger_delta`

```yaml
ledger_delta:
  track: P26
  parent: T08
  source: "Salez arXiv:2508.21055v1, Problem 2.3"
  source_target: "all bounded-degree vertex-transitive expander sequences have TV cutoff"
  source_before: "OPEN / PARTIAL positive classes"
  source_after: "OPEN / PARTIAL positive classes strictly enlarged"
  parent_status_movement: "no closure"
  theorem_scope_movement:
    - "new collision-Green shell/profile transfer criterion with quantitative sqrt(log n) profile window"
    - "removes P26's previous 1-in-J spectral-gap restriction for pure exact-distance-two output"
    - "new 30-regular vertex-transitive Cayley spectral-expander class, provably non-LRE, with explicit Gaussian cutoff profile"
  explicit_application:
    base: "non-bipartite degree-6 LPS Ramanujan Cayley family"
    output: "exact-distance-two graph"
    degree: 30
    gap_lower_bound: "8/15"
    cutoff_center: "(5/8) log_5 n + O(1)"
    window: "Theta(sqrt(log n))"
    profile: "Phi(-z sqrt(384/325))"
    long_range_expansion: "fails every fixed positive constant"
  mechanism:
    collision_front: "C_{n,r}=n sum_y K_r(x,y)^2-1"
    transfer_requirement: "sup_{r>=L_n} log(1+C_{n,r})=o(sqrt(L_n))"
    ramanujan_bound: "C_{n,r}=O((log n)^2) for r at/after entropic radius"
    radial_speed: "2(d-2)/(d-1)"
    radial_variance_rate: "4((d-1)^2+1)/(d(d-1))"
  companion_coordination:
    NM13-01: "direct transitivity/NBRW empirical spectral-trace route and strong products"
    P26: "shell/Green transfer through distinct output walks"
  exact_check: "P26_T08_DISTANCE2_GREEN_TRANSFER_EXACT_PASS"
  mathematical_status: "CANDIDATE_FULL for restricted theorem/application; parent OPEN"
  publication_novelty: "UNVERIFIED"
  failed_or_avoided_routes:
    - "did not use global heat-kernel L2 as a TV surrogate; neighboring affine stress test shows that can be polynomially late"
    - "did not duplicate NM13-01 strong-product or direct empirical-spectrum proof route"
  next_attack: "Green-shell stability under sparse local rewiring without exact polynomial diagonalization"
```

**End of complete P26 substantive T08 report.**
