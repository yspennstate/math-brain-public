Model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — GPT-6/maximum was requested, but no authenticated runtime metadata establishes that model/effort setting, so I do not claim it.

# P26 / LIVE20 T08 — Ramanujan spherical-set transfer without base edges; a distance-{2,3} cutoff class outside long-range expansion

**Status:** `CANDIDATE_FULL` for the restricted spherical-set transfer theorem and the concrete distance-{2,3} application below, pending later independent review; **PARTIAL / OPEN** for Salez Problem 2.3. Worldwide publication novelty is **UNVERIFIED**.

Repository/branch: `yspennstate/math-open-problems` / `master`.  
Controlling policy: `operations/PROGRESS20_2026-09-20.md`.  
Report root: `proofnet24/P26-progress-cutoff-transfer/runs/2026-09-20/`.

## 0. Compact handoff and division of labor with the historical C28 route

The newest P26 report before this run is

`proofnet24/P26-progress-cutoff-transfer/runs/2026-09-20/2026-09-20_06-57-44__distance2-green-shell-transfer.md`.

It proved a collision-Green shell/profile criterion in the exact rate-one continuous-time convention and applied it to the pure exact-distance-two graph of a non-bipartite Ramanujan base. Earlier P26 runs covered line graphs, fixed finite fibers, graph squares and distance-set graphs containing distance one.

The live successor of historical C28 is `NM13-01`. The newest relevant report available in this run is

`proofnet24/NM13-01/progress-cutoff/runs/2026-09-20/2026-09-20T04-22-00Z__incidence-strong-product-trace-obstruction.md`.

That report makes an important route correction: a raw NBRW spectral-trace condition for the **output graph** can fail polynomially on an explicit transitive spectral-expander sequence that nevertheless has cutoff. Thus one should not try to deduce a universal output-NBRW `L^2` trace bound from transitivity plus spectral expansion.

The complementary split used here is therefore:

* `NM13-01` owns the direct transitivity/product/empirical-spectrum route and the diagnosis of when raw output-NBRW trace is too strong;
* P26 owns shell entropy/Green transfer through a different continuous-time walk, using a base shell law when the output has an exact spherical representation.

This run strictly enlarges P26's same-vertex class. It removes the old requirement that distance one be present, not just for the isolated case `J={2}`, but for **arbitrary fixed spherical distance sets whose Ramanujan spectral transform is separated from one**. The proved application is the new set `J={2,3}`.

No stagnation trigger applies: each of the recent P26 T08 runs enlarged theorem scope, so this run continues T08 rather than rotating.

## 1. Exact source convention and current scope boundary

Justin Salez, arXiv:2508.21055v1 (submitted 28 August 2025), defines continuous time by independent mean-one exponential holding times. If `P` is the one-step transition matrix, the semigroup is exactly

\[
H_t=e^{t(P-I)}
=e^{-t}\sum_{k\ge0}\frac{t^kP^k}{k!}.
\tag{1.1}
\]

Problem 2.3 is exactly:

> Prove that all vertex-transitive expanders exhibit cutoff.

Here an expander sequence has diverging size, uniformly bounded degree and a one-sided spectral gap bounded away from zero.

The newer exact-scope boundary checked on 20 September 2026 is unchanged in the crucial sense.

1. **Dylan J. Altschuler, arXiv:2609.14945v1, submitted 14 September 2026.** Every fixed-degree long-range-expander sequence has cutoff with an explicit Gaussian profile. The paper proves the strict hierarchy
   \[
   \text{Ramanujan}\Longrightarrow\text{long-range expansion}
   \Longrightarrow\text{spectral expansion},
   \]
   with neither converse. Long-range expansion is therefore not synonymous with Salez's hypothesis.
2. **Francesco Pedrotti--Justin Salez, arXiv:2607.05345, submitted 6 July 2026.** Their local-product/non-equilibrium-Poincare criterion gives a cutoff-window bound in terms of `gamma_*`; no checked theorem derives the needed `gamma_*` lower bound from vertex transitivity plus an ordinary spectral gap alone.
3. **Classical Ramanujan input.** Lubotzky--Phillips--Sarnak give fixed-degree Cayley Ramanujan families with logarithmically growing girth; a non-bipartite degree-six subfamily is enough for the concrete application here.
4. A bounded fresh search for fixed spherical/distance-{2,3} continuous-time cutoff theorems found Ramanujan SRW/NBRW results and collision-free operators on Ramanujan complexes, but no theorem matching the finite-range reversible distance-{2,3} walk below. This is negative evidence only, not a worldwide novelty certificate.

The root `POSTED.md` exclusions were checked. The posted Cayley product-condition manuscript concerns Salez Problem 2.4 and is not reopened here; no posted T08 distance-{2,3} claim was found.

## 2. Parent problem before / after

### Before

Salez Problem 2.3 was `OPEN`. P26 had proved cutoff for several non-long-range transitive output classes, including the pure exact-distance-two graph. The general distance-set theorem, however, obtained its output spectral gap from the presence of distance-one edges, and the later repair handled only `J={2}` separately.

### After

Salez Problem 2.3 remains `OPEN`, but the proved source-compatible scope is strictly larger:

> **Ramanujan spherical-set theorem.** Fix `d>=3`, put `q=d-1`, and fix a nonempty finite set `J subset {1,...,m}`. Let `(G_n)` be a non-bipartite, `d`-regular, vertex-transitive Ramanujan sequence with `girth(G_n)>2m` for all sufficiently large `n`. Let `X_{J,n}` join two vertices iff their distance in `G_n` belongs to `J`. Define the spherical spectral transform `F_J` below. If
> \[
> \beta_{d,J}:=\sup_{|\lambda|\le 2\sqrt q/d}|F_J(\lambda)|<1
> \]
> and the associated tree radial drift `v_J` is positive, then the exact rate-one continuous-time SRW on `(X_{J,n})` has Gaussian total-variation cutoff at
> \[
> T_n=\frac{\log_q |V(G_n)|}{v_J}+O(1)
> \]
> with a `Theta(sqrt(log n))` window and an explicit Gaussian profile.

This theorem does **not** require `1 in J`.

The concrete new application takes a degree-six LPS Ramanujan base and

\[
\boxed{J=\{2,3\}}.
\]

The output is a **180-regular vertex-transitive Cayley spectral-expander sequence**, contains no base edges, is not the pure distance-two graph, and fails every fixed long-range-expansion constant. Its cutoff center is

\[
\boxed{
T_n=\frac{45}{109}\log_5 n+O(1),
}
\tag{2.1}
\]

and, for fixed real `z`,

\[
\boxed{
 d_{\rm TV}\!\left(T_n+z\sqrt{\log_5 n}\right)
 \longrightarrow
 \Phi\!\left(-z\sqrt{\frac{2590058}{1277775}}\right).
}
\tag{2.2}
\]

This theorem-class enlargement, not the checker receipt, is the substantive movement of the run.

## 3. Spherical distance kernels as NBRW polynomials

Let `G` be `d`-regular, `q=d-1`, with normalized adjacency/SRW kernel `P=A/d`. For `j>=0`, let `K_j` denote the endpoint kernel of length-`j` nonbacktracking walk started from a vertex, with `K_0=I`.

Because `K_j` counts nonbacktracking paths, it is a polynomial in `P`:

\[
K_j=p_j(P),
\tag{3.1}
\]

where

\[
p_0(x)=1,\qquad p_1(x)=x,
\tag{3.2}
\]

and

\[
\boxed{
p_{j+1}(x)=\frac d q x p_j(x)-\frac1q p_{j-1}(x)
}
\qquad(j\ge1).
\tag{3.3}
\]

Indeed, if `B_j` is the matrix counting nonbacktracking paths of length `j`, then `B_0=I`, `B_1=A`, `B_2=A^2-dI`, and `B_{j+1}=AB_j-qB_{j-1}`; dividing by the row sum `d q^{j-1}` gives (3.3).

Now assume `girth(G)>2m`. Then for each `1<=j<=m`, every pair at distance `j` is joined by a unique geodesic of length `j`. Hence the exact-distance-`j` graph has degree

\[
D_j=dq^{j-1}
\tag{3.4}
\]

and its SRW kernel is exactly `K_j`.

For a fixed nonempty set `J subset {1,...,m}`, set

\[
D_J:=\sum_{j\in J}D_j,
\qquad
w_j:=\frac{D_j}{D_J}.
\tag{3.5}
\]

The graph `X_J` obtained by taking the union of those exact-distance shells is simple, `D_J`-regular and vertex-transitive, and its discrete SRW kernel is

\[
\boxed{
Q_J=\sum_{j\in J}w_jK_j=F_J(P),
\qquad
F_J(x):=\sum_{j\in J}w_jp_j(x).
}
\tag{3.6}
\]

For a Cayley base, `X_J` is itself Cayley: its generating set is the union of the word spheres of radii in `J`.

## 4. Spectral transfer without distance-one edges

Suppose `G` is non-bipartite Ramanujan. Then every nontrivial normalized eigenvalue of `P` lies in

\[
[-\rho_d,\rho_d],
\qquad
\rho_d:=\frac{2\sqrt q}{d}<1.
\tag{4.1}
\]

By (3.6), every nontrivial eigenvalue of `Q_J` is `F_J(lambda)` for such a `lambda`. Therefore

\[
\boxed{
\max_{i\ge2}|\lambda_i(Q_J)|\le\beta_{d,J}:=
\sup_{|x|\le\rho_d}|F_J(x)|.
}
\tag{4.2}
\]

Consequently, whenever `beta_{d,J}<1`,

\[
\boxed{
\operatorname{gap}(X_J)\ge1-\beta_{d,J}>0.
}
\tag{4.3}
\]

This is the key repair of the old `1 in J` mechanism. The output spectral gap is obtained from the **spherical transform of the Ramanujan interval**, not by retaining any base edge.

The argument also gives connectedness automatically: the eigenvalue `1=F_J(1)` is simple because all nontrivial eigenvalues have modulus at most `beta_{d,J}<1`.

## 5. The collision-Green front is automatic on a transitive Ramanujan base

For a vertex-transitive `G_n`, define

\[
\mathcal C_{n,r}:=
 n\sum_y K_r(x,y)^2-1.
\tag{5.1}
\]

Transitivity makes this independent of `x`. Since `K_r=p_r(P)` is symmetric,

\[
\boxed{
\mathcal C_{n,r}
=\operatorname{tr}(K_r^2)-1
=\sum_{i=2}^n p_r(\lambda_i)^2.
}
\tag{5.2}
\]

This is the exact shell Green/collision quantity: `1+C_{n,r}` equals `n` times the meeting probability of two independent length-`r` NBRWs from the same start.

For `lambda=(2 sqrt(q)/d) cos theta`, the standard Chebyshev form of the spherical polynomial is

\[
p_r(\lambda)
=
\frac{q^{1-r/2}}{d}
\left(
U_r(\cos\theta)-q^{-1}U_{r-2}(\cos\theta)
\right),
\tag{5.3}
\]

with the second term absent when `r=1`. Since `|U_k(cos theta)|<=k+1`, there is a constant `C_d` such that

\[
|p_r(\lambda)|
\le C_d(r+1)q^{-r/2}
\tag{5.4}
\]

throughout the Ramanujan interval. Hence

\[
\mathcal C_{n,r}
\le C_d^2 n(r+1)^2q^{-r}.
\tag{5.5}
\]

Put

\[
L_n:=\lceil\log_q n\rceil.
\tag{5.6}
\]

For `r>=L_n`, the right-hand side is at most a constant times
`(r+1)^2 q^{L_n-r}`, whose supremum is `O_d(L_n^2)`. Therefore

\[
\boxed{
\sup_{r\ge L_n}
\log(1+\mathcal C_{n,r})
=O_d(\log\log n)
=o(\sqrt{L_n}).
}
\tag{5.7}
\]

Finally, for any law `mu` on an `n`-point uniform space,

\[
D(\mu\|\pi)\le\log(1+\chi^2(\mu\|\pi)),
\tag{5.8}
\]

so (5.7) is exactly the entropy input needed for the shell cleanup argument.

## 6. Exact continuous-time shell representation for `X_J`

Consider the rate-one continuous-time SRW on `X_J`, with semigroup

\[
H_t^{(J)}=e^{t(Q_J-I)}.
\tag{6.1}
\]

Lift it to the infinite `d`-regular tree rooted at `o`. At each Poisson jump, choose `j in J` with probability `w_j` and then choose uniformly a vertex at tree distance exactly `j` from the current vertex. Let `R_t` be the distance of the lifted endpoint from `o`.

The root stabilizer of the tree acts transitively on every sphere and leaves the lifted dynamics invariant. Therefore, conditional on `R_t=r`, the tree endpoint is uniform on the sphere `S(o,r)`. Projection to `G` sends that uniform sphere law exactly to the length-`r` NBRW endpoint law `K_r(x,.)`.

Thus, for every `x,t`, one has the exact identity

\[
\boxed{
\delta_xH_t^{(J)}
=
\sum_{r\ge0}\Pr(R_t=r)K_r(x,\cdot).
}
\tag{6.2}
\]

This is an exact statement in Salez's continuous-time convention; no lazy-time substitution or discrete-time approximation is used.

## 7. Radial CLT and explicit profile

Let `m=max J`. Whenever `R_t>=m`, one jump has an increment distribution independent of the current radius. Conditional on choosing a shell length `j`, the count of endpoints producing radial increment `j-2a` is

\[
N_{j,0}=q^j,
\tag{7.1}
\]

\[
N_{j,a}=(q-1)q^{j-a-1}
\qquad(1\le a<j),
\tag{7.2}
\]

and

\[
N_{j,j}=1.
\tag{7.3}
\]

These counts sum to `d q^{j-1}=D_j`, as required.

Let `xi_J` denote the resulting increment after mixing the shell lengths with weights `w_j`, and set

\[
v_J:=\mathbb E\xi_J,
\qquad
M_{2,J}:=\mathbb E\xi_J^2.
\tag{7.4}
\]

Assume `v_J>0`. The boundary region `{0,...,m-1}` creates only an `O_P(1)` correction. A short proof is as follows. Since `E xi_J>0`, for sufficiently small `s>0`,

\[
\mathbb E e^{-s\xi_J}<1.
\tag{7.5}
\]

Thus `e^{-sR}` is a strict supermartingale whenever the radius is at least `m`, up to the next entrance into the boundary region. Optional stopping gives a return probability strictly below one from radius `m`; by the strong Markov property the number of boundary returns has a geometric tail. Since jumps are bounded, the total discrepancy from the unrestricted compound-Poisson sum is `O_P(1)`.

If `N_t~Pois(t)`, the unrestricted sum `S_t=sum_{k<=N_t} xi_k` has mean `v_J t` and variance `M_{2,J}t`. Hence

\[
\boxed{
\frac{R_t-v_Jt}{\sqrt{M_{2,J}t}}
\Longrightarrow N(0,1).
}
\tag{7.6}
\]

uniformly for `t=L_n/v_J+O(sqrt(L_n))`.

## 8. Quantitative Green/entropy-to-TV transfer

Let

\[
\eta_J:=1-\beta_{d,J}>0.
\tag{8.1}
\]

For any initial law `mu` on `X_J`, entropy dissipation plus Poincare gives the exact continuous-time cleanup bound

\[
\boxed{
\|\mu H_s^{(J)}-\pi\|_{TV}
\le
\sqrt{\frac{D(\mu\|\pi)}{4\eta_J s}}.
}
\tag{8.2}
\]

Indeed,
`-d/ds D(mu H_s||pi) >= 4 eta_J Var_pi(sqrt(f_s))`, while
`TV^2 <= Var_pi(sqrt(f_s))`; integrate and use monotonicity of TV.

Write

\[
g_n:=\sup_{r\ge L_n}\log(1+\mathcal C_{n,r})
=O(\log\log n).
\tag{8.3}
\]

Choose `s_n` with

\[
g_n\ll s_n\ll\sqrt{L_n}.
\tag{8.4}
\]

At time `t-s_n`, use (6.2), split shells at `L_n`, and apply (8.2) to every shell with `r>=L_n`. Convexity of TV gives

\[
 d_n(t)
\le
\Pr(R_{t-s_n}<L_n)
+
\sqrt{\frac{g_n}{4\eta_Js_n}}.
\tag{8.5}
\]

The second term is `o(1)`, and the `s_n` shift is negligible on the `sqrt(L_n)` scale.

For the reverse inequality choose `h_n->infinity` with `h_n=o(sqrt(L_n))`. The support of every `K_r(x,.)` with `r<=L_n-h_n` lies in the base ball `B_G(x,L_n-h_n)`, whose size is at most

\[
1+d\sum_{k<L_n-h_n}q^k
=O_d(q^{L_n-h_n})
=o(n).
\tag{8.6}
\]

Therefore that ball is a TV witness, and

\[
 d_n(t)
\ge
\Pr(R_t\le L_n-h_n)-o(1).
\tag{8.7}
\]

Combining (7.6), (8.5) and (8.7), for

\[
T_n=\frac{L_n}{v_J},
\qquad
\tau_J^2:=\frac{M_{2,J}}{v_J^3},
\tag{8.8}
\]

one obtains for each fixed real `z`

\[
\boxed{
 d_n(T_n+z\sqrt{L_n})
\longrightarrow
\Phi(-z/\tau_J).
}
\tag{8.9}
\]

This proves the Ramanujan spherical-set theorem stated in Section 2.

## 9. New application: the distance-{2,3} graph of degree-six LPS graphs

Take a non-bipartite degree-six LPS Ramanujan Cayley family `(G_n)`. Then

\[
d=6,\qquad q=5,
\qquad J=\{2,3\}.
\]

Its girth tends to infinity, so `girth(G_n)>6` eventually.

### 9.1 Degree and exact spectral polynomial

The two shell degrees are

\[
D_2=6\cdot5=30,
\qquad
D_3=6\cdot25=150,
\]

so

\[
\boxed{D_J=180},
\qquad
w_2=\frac16,
\qquad
w_3=\frac56.
\tag{9.1}
\]

From (3.3),

\[
p_2(x)=\frac{6x^2-1}{5},
\qquad
p_3(x)=\frac{36x^3-11x}{25}.
\tag{9.2}
\]

Therefore

\[
\boxed{
F(x)=\frac{36x^3+6x^2-11x-1}{30}.
}
\tag{9.3}
\]

The Ramanujan interval is

\[
|x|\le\frac{\sqrt5}{3}.
\tag{9.4}
\]

The derivative satisfies

\[
F'(x)=0
\iff
x=\frac{-1\pm\sqrt{34}}{18}.
\tag{9.5}
\]

Evaluating `F` at those two critical points and at the two endpoints of (9.4) gives the exact maximum absolute value

\[
\boxed{
\beta_{6,\{2,3\}}
=F(\sqrt5/3)
=\frac7{90}+\frac{\sqrt5}{10}
<1.
}
\tag{9.6}
\]

Hence the new 180-regular output family has the uniform spectral-gap bound

\[
\boxed{
\operatorname{gap}(X_n)
\ge
\frac{83}{90}-\frac{\sqrt5}{10}
>0.698.
}
\tag{9.7}
\]

This is a genuine no-base-edge application of the spherical spectral transfer.

### 9.2 Exact radial law

A uniform output neighbor gives the following interior radial increment counts on the six-regular tree:

\[
\begin{array}{c|rrrrrrr}
\Delta R&-3&-2&-1&0&1&2&3\\ \hline
\#&1&1&4&4&20&25&125.
\end{array}
\tag{9.8}
\]

The counts sum to `180`. Therefore

\[
\boxed{
v=\mathbb E\xi=\frac{109}{45}}
\tag{9.9}
\]

and

\[
\boxed{
M_2=\mathbb E\xi^2=\frac{631}{90}}.
\tag{9.10}
\]

Thus

\[
\boxed{
T_n=\frac{45}{109}\log_5 n+O(1)
}
\tag{9.11}
\]

and

\[
\boxed{
\tau^2=\frac{M_2}{v^3}
=\frac{1277775}{2590058}.
}
\tag{9.12}
\]

Equations (2.1)--(2.2) follow.

### 9.3 The output is not a long-range expander

The output degree is `180`, so its tree branching base would be

\[
179.
\]

But one output step changes base distance by at most three. Hence

\[
B_{X_n}(x,r)\subseteq B_{G_n}(x,3r),
\]

and the elementary degree bound on the six-regular base gives

\[
|B_{X_n}(x,r)|\le C\,5^{3r}=C\,125^r.
\tag{9.13}
\]

Long-range expansion for a 180-regular sequence would require, for a fixed `c>0`,

\[
|B_{X_n}(x,r)|
\ge
\min\{3n/4,c\,179^r\}
\tag{9.14}
\]

for all `r`. Take

\[
r_n=\left\lfloor\frac12\log_{179}n\right\rfloor.
\]

Then the second term in (9.14) is still below `3n/4` for large `n`, while

\[
\frac{|B_{X_n}(x,r_n)|}{179^{r_n}}
\le
C\left(\frac{125}{179}\right)^{r_n}
\longrightarrow0.
\tag{9.15}
\]

Thus no fixed long-range-expansion constant can hold.

This explicitly separates the result from Altschuler's theorem: the **input** is Ramanujan/LRE, but the **output sequence to which Salez's conjecture applies** is spectral and vertex-transitive while provably not LRE.

## 10. Essential exact sanity check

I executed an exact symbolic/rational checker, not counted as theorem progress:

`proofnet24/P26-progress-cutoff-transfer/artifacts/2026-09-20/2026-09-20_07-58-10__distance23_spherical_exact.py`

creation commit

`8072380b84cc6822f02cfe92c7c47b58bdf0d9bc`.

Its archived output is

`proofnet24/P26-progress-cutoff-transfer/artifacts/2026-09-20/2026-09-20_07-58-10__distance23_spherical_exact.out`

creation commit

`80c16692cf3c9590c8e16459d320e1cab2a5d15e`.

The checker independently verifies:

* the exact NBRW polynomials `p_2,p_3` and their weighted transform;
* the exact critical points and maximum absolute spectral transform on the Ramanujan interval;
* the exact gap lower bound;
* all seven radial increment counts;
* `v=109/45`, `M_2=631/90`, and `tau^2=1277775/2590058`;
* the strict long-range branching mismatch `125<179`.

The archived output ends

`P26_T08_DISTANCE23_SPHERICAL_EXACT_PASS`.

## 11. What this changes mechanistically

The previous route had two separate spectral mechanisms:

1. keep base edges (`1 in J`) and inherit a gap by Dirichlet domination; or
2. handle pure distance two by a one-off polynomial calculation.

The new theorem replaces both by one reusable object:

\[
F_J(P)=\sum_{j\in J}w_jp_j(P).
\]

The only spectral question for any fixed shell set is whether the spherical transform stays below one on the Ramanujan interval. Once it does, the collision-Green front of the **base** automatically supplies the entropy cleanup, and the output's entire cutoff profile is read from a one-dimensional finite-range radial process.

Thus the demonstrated transfer chain is now

\[
\text{Ramanujan shell collision}
\Longrightarrow
O(\log\log n)\text{ shell entropy deficit}
\Longrightarrow
\text{spherical output gap}
\Longrightarrow
\text{Gaussian TV cutoff profile}.
\]

This is stronger than another isolated graph operation and remains complementary to NM13-01's direct output-spectrum program.

## 12. Residual obstruction and next attack

The parent obstruction is unchanged in kind but sharper in location. The proof still receives its near-maximal shell entropy from the Ramanujan spectral interval. General vertex-transitive spectral expanders can have substantial spectral mass outside that interval, and NM13-01 has shown that demanding a small raw output-NBRW `L^2` trace is too strong in general.

The next P26 attack will therefore **not** try to prove a universal raw trace bound. The next target is a trimmed Green/entropy criterion that tolerates a controlled exceptional spectral subspace:

\[
\sum_{i\notin E_n}p_r(\lambda_i)^2\le \operatorname{polylog}(n),
\qquad
\dim E_n=o(\sqrt{\log n})\text{ in an entropy-weighted sense},
\]

with a direct entropy estimate showing that exceptional low-dimensional modes cost only `o(sqrt(log n))` information even when their `L^2` contribution is polynomial. A successful version would survive the type of product obstruction exhibited by NM13-01 and would move the criterion closer to ordinary transitivity plus spectral expansion.

No failed recovery route is charged this run; the spherical-set route succeeded and enlarged source-valid scope.

## 13. `ledger_delta`

```text
parent = T08 / Salez arXiv:2508.21055 Problem 2.3
parent_before = OPEN / PARTIAL
parent_after = OPEN / PARTIAL
parent_status_changed = no

mechanism_before = collision-Green shell transfer + isolated exact-distance-two spectral repair
mechanism_after = general spherical-set spectral transform F_J(P) + Green-shell Gaussian-profile transfer for fixed J without requiring distance one
mechanism_advance = yes

new_proved_application = degree-180 distance-{2,3} Cayley graphs of degree-six non-bipartite LPS Ramanujan bases
new_application_vertex_transitive = yes
new_application_spectral_expander = yes; gap >= 83/90 - sqrt(5)/10
new_application_long_range = no; 125^r versus required 179^r singleton growth
new_cutoff_center = (45/109) log_5 n + O(1)
new_window = Theta(sqrt(log n))
new_profile = Phi(-z sqrt(2590058/1277775)) under time shift z sqrt(log_5 n)

runtime_model = GPT-5.6 Sol
runtime_reasoning = UNVERIFIED
source_scope = exact rate-one continuous time H_t = exp(t(Q-I))
review_status = CANDIDATE_FULL pending later independent review
publication_novelty = UNVERIFIED
posted_conflict = none found; Salez 2.4 posted Cayley product-condition claim remains excluded
companion = NM13-01 / historical C28 successor
companion_split = NM13-01 direct transitivity/output-spectrum; P26 base-shell Green transfer through spherical output kernels
stagnation_trigger = no
next_attack = trimmed Green/entropy criterion tolerating exceptional spectral modes
```

End of complete P26 substantive T08 report.
