Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — no authenticated runtime metadata establishes GPT-6 or a maximum-effort setting.**

# P26 / LIVE20 T08 — all fixed exact-distance spherical Green transfer on non-Ramanujan Cayley bigraphs

**Parent status:** `PARTIAL / OPEN` for Salez Problem 2.3 before this run; `PARTIAL / OPEN` after this run.

**Restricted theorem status:** `CANDIDATE_FULL` for Theorems A--C below, pending later independent review.

**Publication novelty:** `UNVERIFIED`. A bounded repository search found no prior T08 `distance-eight cutoff` result, and bounded web searches for `exact distance eight graph random walk cutoff`, `distance-eight Cayley cutoff`, and variants did not recover a matching ordinary-SRW theorem. This is negative evidence only, not a priority certificate.

Repository/branch: `yspennstate/math-open-problems` / `master`.
Controlling policy: `operations/PROGRESS20_2026-09-20.md`.
Run root: `proofnet24/P26-progress-cutoff-transfer/runs/2026-09-20/`.

## 0. Compact handoff and complementary C28/NM13-01 split

The controlling LIVE20 policy replaces P26's former audit-first duties by direct T08 work. The newest own substantive report before this run was

`2026-09-20_11-57-39__weighted-exception-distance6-transfer.md`.

That report proved a weighted exceptional Green-to-TV criterion and applied the EFMP Sarnak--Xue shell estimate to the exact bigraph-distance-six left graph of the non-Ramanujan Eisenstein `(9,3)` Cayley bigraphs, producing a 4608-regular spectral-but-not-long-range cutoff class. Its next speculative route was an Ihara/first-repeated-directed-edge tangle decomposition. That tangle route remains unproved and is preserved as failed/unresolved history; it is not counted as progress here.

The newest relevant live historical-C28 successor report read this run is NM13-01's

`2026-09-20T09-13-06Z__growing-automorphism-memory-cutoff.md`.

NM13-01 has moved to growing hidden automorphism memory in semidirect Cayley graphs, proving a quantitative transfer for polynomially growing memory and an explicit degree-20 non-LRE class. P26 therefore stays on the complementary shell-Green / spherical-spectrum / radial-clock route. There is no three-run unchanged trigger: the preceding P26 runs enlarged theorem scope and changed the mechanism from crude exceptional counts to weighted entropic-radius Green mass.

## 1. Exact source convention and current exact scope

Justin Salez, `arXiv:2508.21055`, defines the continuous-time chain by inserting independent mean-one exponential waiting times between discrete jumps. Thus, if `P` is the discrete SRW kernel,

\[
H_t=e^{t(P-I)}=e^{-t}\sum_{j\ge0}\frac{t^jP^j}{j!}.
\tag{1.1}
\]

Problem 2.3 in those notes is exactly: prove that all vertex-transitive expanders exhibit cutoff. There `expander` means diverging size, uniformly bounded degree, and ordinary spectral gap bounded away from zero.

The current checked boundary on 20 September 2026 is materially narrower than this conjecture:

* Dylan J. Altschuler, `arXiv:2609.14945`, submitted 14 September 2026, proves an explicit Gaussian-profile cutoff theorem for every fixed-degree **long-range expander** sequence and establishes the strict hierarchy Ramanujan => long-range => spectral, with neither converse. Long-range expansion is therefore not synonymous with the hypothesis of Salez Problem 2.3.
* Francesco Pedrotti and Justin Salez, `arXiv:2607.05345`, submitted 6 July 2026, prove a universal window bound `O(1/gamma_*)` in terms of a non-equilibrium Poincare quantity. The checked result does not derive a positive `gamma_*` bound from vertex transitivity plus the ordinary spectral gap alone.
* Shai Evra, Brooke Feigon, Kathrin Maurischat and Ori Parzanchevski, `arXiv:2312.06507`, construct `(p^3+1,p+1)` arithmetic Cayley bigraphs, including explicit examples which are genuinely non-Ramanujan for NBRW but satisfy a Sarnak--Xue density theorem and bounded-window NBRW cutoff. Their weighted shell Green estimate is the external input used below.

The repository's POSTED exclusions, including the Salez Problem 2.4 Abelian-Cayley result, remain untouched.

## 2. Parent before/after and mechanism-level movement

### Parent problem before

Salez Problem 2.3 was `OPEN / PARTIAL`. P26 had individual exact-distance-four and exact-distance-six biregular output classes, but no theorem controlling the entire fixed exact-distance hierarchy.

### Parent problem after

Salez Problem 2.3 remains `OPEN / PARTIAL`; no general transitivity-plus-gap implication is claimed.

The proved source-compatible subclass is strictly enlarged: for **every fixed integer `m>=4`**, ordinary rate-one continuous-time SRW on the left exact-bigraph-distance-`2m` graph of the EFMP `p=2` Eisenstein family has an explicit Gaussian cutoff profile. Every output is a bounded-degree vertex-transitive Cayley spectral expander and fails every fixed long-range-expansion constant.

The first genuinely new concrete member is `m=4`, exact ancestor distance eight. It is 73728-regular, has normalized spectral gap at least `15/16`, and cuts off at

\[
\frac{24576}{93935}\log_{16}n+O(1)
\]

with a `Theta(sqrt(log n))` Gaussian window.

### Mechanism-level movement

The substantive mechanism advance is an **all-distance spherical/Chebyshev transfer**. The exact-distance operators satisfy a second-order recurrence, and on the adjacency-Ramanujan bulk this recurrence can be solved with Chebyshev polynomials. For the concrete `(9,3)` parameters this yields the uniform bound

\[
|\lambda(Q_m)|\le 2^{-m}\qquad(m\ge4)
\]

on every nonconstant output mode. This removes the need for a fresh one-off spectral optimization at each distance. In parallel, the radial clock admits closed formulas for its drift and variance for all `m`, so the entire hierarchy has explicit cutoff centers and profiles.

The Green criterion itself is restated and proved below because it is the transfer bridge demanded by T08; it was already developed in previous P26 runs and is not separately counted as a new ledger advance here.

## 3. Theorem A — quantitative Green-shell profile transfer

Let `X_n` be a transitive finite chain with uniform stationary law `pi_n`, in the exact rate-one convention. Suppose that from every start `x` there is an exact shell representation

\[
\delta_xH_t^{(n)}=\sum_{r\ge0}\Pr(R_t=r)\nu_{n,r}^x.
\tag{3.1}
\]

Let `ell_n` be an entropic radius. Assume that for `h>=0`

\[
\sup_x\sup_{r\ge ell_n+h}
\chi^2(\nu_{n,r}^x\Vert\pi_n)\le G_n(h),
\tag{3.2}
\]

and that all shells of radius at most `ell_n-h` are supported in sets `A_{n,x}(ell_n-h)` with

\[
\sup_x\pi_n(A_{n,x}(ell_n-h))\le L_n(h).
\tag{3.3}
\]

Then for every `t,h>=0`,

\[
\boxed{
\Pr(R_t\le ell_n-h)-L_n(h)
\le d_n(t)
\le
\Pr(R_t<ell_n+h)+\frac12\sqrt{G_n(h)}.
}
\tag{3.4}
\]

Here transitivity identifies worst-start TV with the point-start value.

### Proof

For the upper bound, split (3.1) at `ell_n+h`. Early shells cost at most their total mass. For every late shell, Cauchy--Schwarz gives

\[
\|\nu-\pi_n\|_{TV}
\le\frac12\sqrt{\chi^2(\nu\Vert\pi_n)}
\le\frac12\sqrt{G_n(h)}.
\]

Convexity of TV under mixing gives the right side of (3.4). For the lower bound, test TV against `A_{n,x}(ell_n-h)`. Every shell with radius at most `ell_n-h` lies in that set, while stationarity assigns it mass at most `L_n(h)`. This proves the left side. `QED`

### Quantitative window consequence

If, uniformly in `n`,

\[
G_n(h)\le C e^{-c h},\qquad L_n(h)\le C e^{-c h},
\tag{3.5}
\]

then fixed TV accuracy `epsilon` costs only

\[
h_\epsilon=O_c(\log(C/\epsilon))
\tag{3.6}
\]

radial layers. Consequently, if

\[
\frac{R_t-vt}{\sqrt{M_2t}}\Longrightarrow N(0,1),
\qquad v>0,\ M_2>0,
\tag{3.7}
\]

and `ell_n -> infinity`, then choosing any `h_n -> infinity` with `h_n=o(sqrt(ell_n))` and applying (3.4) at

\[
t=\frac{ell_n}{v}+z\sqrt{ell_n}
\]

gives

\[
\boxed{
 d_n\!\left(\frac{ell_n}{v}+z\sqrt{ell_n}\right)
 \longrightarrow
 \Phi\!\left(-\frac{z}{\tau}\right),
 \qquad
 \tau^2=\frac{M_2}{v^3}.
}
\tag{3.8}
\]

In particular

\[
t_{mix}(\epsilon)
=\frac{ell_n}{v}
+\tau\,\Phi^{-1}(1-\epsilon)\sqrt{ell_n}
+o(\sqrt{ell_n}).
\tag{3.9}
\]

This is the quantitative Green-function transfer criterion used below.

## 4. Exact-distance operators on a biregular tree quotient

Let

\[
X=(L\sqcup R,E)
\]

be connected, left-transitive and `(K+1,k+1)`-biregular. For a fixed integer `m>=1`, suppose the girth is greater than `4m`. Define `Y_m` on `L` by

\[
x\sim_{Y_m}y
\quad\Longleftrightarrow\quad
\operatorname{dist}_X(x,y)=2m.
\tag{4.1}
\]

The girth assumption implies uniqueness of every relevant `2m`-geodesic: two distinct such geodesics with the same endpoints would create a cycle of length at most `4m`. Therefore `Y_m` is simple and regular of degree

\[
\boxed{D_m=(K+1)k(Kk)^{m-1}.}
\tag{4.2}
\]

Every left automorphism preserves distance, so `Y_m` is vertex-transitive; for a Cayley bigraph the left regular action makes `Y_m` a Cayley graph.

Let `M` be the `|L| x |R|` incidence matrix, put

\[
B=MM^T,
\]

and let `A_m` be the adjacency matrix of `Y_m`. Since

\[
A_1=B-(K+1)I,
\tag{4.3}
\]

tree intersection counting gives

\[
A_1^2=A_2+(k-1)A_1+(K+1)kI
\tag{4.4}
\]

and, for `m>=2`,

\[
\boxed{
A_1A_m=A_{m+1}+(k-1)A_m+KkA_{m-1}.
}
\tag{4.5}
\]

The girth condition transports these tree identities exactly to the finite quotient through the required radius.

## 5. Theorem B — all fixed distances for `(K,k)=(8,2)`

Specialize to the EFMP `p=2` parameters

\[
(K+1,k+1)=(9,3),\qquad K=8,\quad k=2,\quad Kk=16.
\]

Write

\[
A_m=f_m(B).
\]

Equations (4.3)--(4.5) become

\[
f_1(x)=x-9,
\qquad
f_2(x)=x^2-19x+72,
\tag{5.1}
\]

and

\[
\boxed{
f_{m+1}(x)=(x-10)f_m(x)-16f_{m-1}(x),\qquad m\ge2.
}
\tag{5.2}
\]

The degree is

\[
D_m=18\,16^{m-1}.
\tag{5.3}
\]

### Chebyshev solution on the adjacency-Ramanujan bulk

For `x in [2,18]`, set

\[
z=\frac{x-10}{8}\in[-1,1].
\]

Let `U_j` be the Chebyshev polynomial of the second kind, with `U_{-1}=0`. Solving (5.2) gives, for `m>=2`,

\[
\boxed{
f_m(x)=4^{m-2}\left[f_2(x)U_{m-2}(z)-4f_1(x)U_{m-3}(z)\right].}
\tag{5.4}
\]

This follows immediately from `U_{j+1}(z)=2zU_j(z)-U_{j-1}(z)` and the initial cases `m=2,3`.

On `[-1,1]`, `|U_j(z)|<=j+1`. Also on `[2,18]`,

\[
|f_1(x)|\le9,
\qquad
|f_2(x)|\le54.
\]

Hence

\[
|f_m(x)|
\le4^{m-2}\{54(m-1)+36(m-2)\}
=4^{m-2}(90m-126).
\tag{5.5}
\]

After dividing by (5.3), the normalized exact-distance kernel

\[
Q_m=A_m/D_m
\]
satisfies

\[
\boxed{
|q_m(x)|\le\frac{5m-7}{4^m},\qquad x\in[2,18].
}
\tag{5.6}
\]

At a zero mode, the recurrence gives an exact closed value. Indeed direct induction from (5.1)--(5.2) yields

\[
\boxed{q_m(0)=(-1/2)^m.}
\tag{5.7}
\]

For every `m>=4`,

\[
5m-7\le2^m,
\tag{5.8}
\]

starting from `13<=16` at `m=4` and propagating by induction. Thus

\[
\frac{5m-7}{4^m}\le2^{-m}.
\tag{5.9}
\]

An adjacency-Ramanujan `(9,3)` bigraph has nontrivial nonzero `B`-spectrum in

\[
[(\sqrt8-\sqrt2)^2,(\sqrt8+\sqrt2)^2]=[2,18],
\tag{5.10}
\]

with zero modes allowed, while the Perron mode is `27`. Since `q_m(27)=1` by the row sum, (5.6)--(5.9) prove

\[
\boxed{
\max_{\lambda\ne1}|\lambda(Q_m)|\le2^{-m},
\qquad
\operatorname{gap}(Y_m)\ge1-2^{-m},
\qquad m\ge4.
}
\tag{5.11}
\]

This is the all-distance spectral transfer promised above.

## 6. Exact shell representation for rate-one SRW

Lift rate-one continuous-time SRW on `Y_m` to the exact-distance-`2m` left graph of the universal `(9,3)`-biregular tree. Let

\[
R_t=\frac12\operatorname{dist}(o,Z_t)
\]

be the half-radius. The root stabilizer is transitive on every left sphere. Therefore, conditional on `R_t=r`, the lifted endpoint is uniform on the left sphere of bigraph radius `2r`. Projecting to the finite bigraph gives exactly the left endpoint law `nu_r^x` of a uniformly chosen nonbacktracking path of length `2r`.

Consequently, with **no lazification and no time rescaling**,

\[
\boxed{
\delta_x e^{t(Q_m-I)}
=
\sum_{r\ge0}\Pr(R_t=r)\nu_r^x.
}
\tag{6.1}
\]

This is exactly Salez's source convention (1.1).

The EFMP Sarnak--Xue estimate used in the preceding P26 report gives, with

\[
ell_n=\log_{16}|L_n|+O(1),
\]

\[
\boxed{
\sup_x\chi^2(\nu_{ell_n+h}^x\Vert\pi_{L_n})
\le C(4^{-h}+16^{-h}),\qquad h\ge0.
}
\tag{6.2}
\]

The left half-ball of radius `ell_n-h` has stationary mass `O(16^{-h})`, so Theorem A applies with exponentially small upper and lower Green errors. Crucially, the shell law in (6.2) does not depend on `m`; changing `m` changes only the radial clock.

## 7. Theorem C — closed radial moments for every fixed `m`

Assume the current half-radius is at least `m`. A `2m`-edge output geodesic may follow the unique inward ancestor ray for `s` initial edges before turning. Then

\[
\Delta R=m-s.
\]

For `(K,k)=(8,2)`, the exact multiplicities are:

\[
\begin{aligned}
s=0 &: &&16^m,\\
s=2a+1,\quad 0\le a\le m-1 &: &&16^{m-a-1},\\
s=2a,\quad 1\le a\le m-1 &: &&14\,16^{m-a-1},\\
s=2m &: &&1.
\end{aligned}
\tag{7.1}
\]

They sum to `D_m=18*16^{m-1}`. Evaluating the resulting finite geometric sums gives

\[
\boxed{
\mathbb E s=\frac8{45}(1-16^{-m})
}
\tag{7.2}
\]

and

\[
\boxed{
\mathbb E s^2
=\frac8{675}\left(29-(60m+29)16^{-m}\right).
}
\tag{7.3}
\]

Therefore the interior drift is

\[
\boxed{
v_m
=m-\frac8{45}(1-16^{-m})>0
}
\tag{7.4}
\]

and the raw second-moment rate for the exact rate-one compound-Poisson clock is

\[
\boxed{
M_{2,m}
=\frac{675m^2-240m+232}{675}
-\frac{240m+232}{675\,16^m}.
}
\tag{7.5}
\]

The boundary region `{0,1,...,m-1}` is finite. Since `v_m>0`, for sufficiently small `theta>0` the interior increment `xi_m` obeys

\[
\mathbb E e^{-\theta\xi_m}<1.
\]

The usual exponential-supermartingale argument then gives a geometric tail for the number of returns to the boundary region. Hence the number of boundary-modified jumps is `O_P(1)`. Coupling with the unrestricted rate-one compound-Poisson sum yields

\[
\boxed{
\frac{R_t-v_mt}{\sqrt{M_{2,m}t}}\Longrightarrow N(0,1).
}
\tag{7.6}
\]

Combining (6.1)--(6.2), the half-ball lower bound and Theorem A proves, for every fixed `m>=4`,

\[
\boxed{
T_{n,m}=\frac{\ell_n}{v_m}
}
\tag{7.7}
\]

and

\[
\boxed{
 d_{TV}\left(T_{n,m}+z\sqrt{\ell_n}\right)
 \longrightarrow
 \Phi\left(-\frac z{\tau_m}\right),
 \qquad
 \tau_m^2=\frac{M_{2,m}}{v_m^3}.
}
\tag{7.8}
\]

Thus the window is `Theta(sqrt(log n))`, while Green cleanup for fixed accuracy costs only `O(log(1/epsilon))` radial layers.

## 8. Concrete new class: exact bigraph-distance eight

Take `m=4`. Then

\[
D_4=18\cdot16^3=73728.
\]

The recurrence gives

\[
\boxed{
f_4(x)=x^4-39x^3+520x^2-2732x+4608.}
\tag{8.1}
\]

On the Ramanujan bulk, (5.6) gives

\[
|q_4(x)|\le\frac{13}{256}<\frac1{16},
\]

while `q_4(0)=1/16`. Hence

\[
\boxed{\operatorname{gap}(Y_4)\ge15/16.}
\tag{8.2}
\]

The interior radial increment counts are

\[
\begin{array}{c|rrrrrrrrr}
\Delta R&-4&-3&-2&-1&0&1&2&3&4\\ \hline
\#&1&1&14&16&224&256&3584&4096&65536.
\end{array}
\tag{8.3}
\]

They give

\[
\boxed{v_4=\frac{93935}{24576}},
\qquad
\boxed{M_{2,4}=\frac{1100129}{73728}},
\tag{8.4}
\]

and

\[
\boxed{
\tau_4^2=
\frac{221485222330368}{828862171175375}.
}
\tag{8.5}
\]

Therefore, writing `n=|L_n|`, the ordinary simple random walk in Salez's exact continuous-time convention has

\[
\boxed{
T_n=\frac{24576}{93935}\log_{16}n+O(1)
}
\tag{8.6}
\]

and

\[
\boxed{
 d_{TV}\left(T_n+z\sqrt{\log_{16}n}\right)
 \longrightarrow
 \Phi\left(-z/\tau_4\right).
}
\tag{8.7}
\]

The EFMP family has logarithmically growing girth, so for this fixed `m=4` the required girth `>16` holds eventually.

## 9. Every output in the hierarchy is spectral but not long-range

One output step in `Y_m` changes the ancestor half-radius by at most `m`. A left half-ball of radius `s` in the `(9,3)` universal tree has size `O(16^s)`. Thus

\[
|B_{Y_m}(x,r)|\le C_m16^{mr}.
\tag{9.1}
\]

But the output degree is

\[
D_m=18\,16^{m-1},
\]

so

\[
16^m<D_m-1=18\,16^{m-1}-1.
\tag{9.2}
\]

A degree-`D_m` long-range expander must, in particular, satisfy the singleton tree-branching lower bound on the `(D_m-1)^r` scale through a fixed positive logarithmic range. Taking

\[
r_n=\left\lfloor\frac12\log_{D_m-1}n\right\rfloor
\]

gives

\[
\frac{|B_{Y_m}(x,r_n)|}{(D_m-1)^{r_n}}
\le C_m\left(\frac{16^m}{D_m-1}\right)^{r_n}
\longrightarrow0.
\tag{9.3}
\]

Hence every fixed-`m` output fails every fixed long-range-expansion constant while (5.11) gives a uniform spectral gap. For `m=4`, the incompatible branching bases are

\[
65536<73727.
\]

Thus these are genuine spectral-but-not-long-range cutoff examples; Altschuler's output hypothesis does not apply to them.

## 10. Exact calculation executed and archived

The executed exact-arithmetic checker is

`2026-09-20_13-00-56__distance-allm-green-checker.py`

with archived output

`2026-09-20_13-00-56__distance-allm-green-checker.out`.

It verifies:

* the recurrence through `m=9` and `f_m(27)=D_m`;
* the exact zero-mode identity `q_m(0)=(-1/2)^m`;
* the exact `m=4` polynomial (8.1);
* the Chebyshev bound `13/256<1/16` and the elementary all-`m` inequality `5m-7<=2^m`;
* the radial multiplicities and degree identity for `m=1,...,8`;
* the closed drift and second-moment formulas (7.4)--(7.5) on those test values;
* `v_4=93935/24576`, `M_{2,4}=1100129/73728`, and the exact profile constant (8.5);
* the strict `m=4` branching mismatch `65536<73727`.

Its terminal marker is `ALL_CHECKS_PASS`. The checker certifies finite algebra/arithmetic only; the probability and asymptotic arguments are written above.

## 11. Residual obstruction, failed-route history, and next attack

### Residual obstruction

The parent conjecture still lacks a way to create the required near-entropic shell Green front from **arbitrary bounded-degree vertex transitivity plus ordinary spectral expansion**. In the theorem above, the shell front is inherited from EFMP's arithmetic Sarnak--Xue density result. The all-distance Chebyshev theorem shows that once a shell front exists, a large family of highly non-LRE radial clocks can use it, but it does not manufacture that front in a general transitive graph.

### Failed/unresolved route history preserved

The following earlier routes remain explicitly unresolved or ruled out as universal criteria:

* maximal tree-rate / long-range ball growth is not forced by transitivity plus spectral gap;
* raw global heat-kernel or NBRW `L^2` control can be polynomially large at the TV scale even on transitive cutoff examples;
* crude exceptional-mode counting is too expensive in the presence of polynomial exceptional sectors;
* the proposed Ihara/first-repeated-directed-edge tangle decomposition from the preceding P26 report is still unproved. It is not silently promoted here.

### Next P26 attack

The next attack should return to the parent mechanism rather than continue increasing the exact distance. Use the all-distance recurrence as a test family for a **Tauberian shell-Green criterion**: replace pointwise control of a single NBRW shell by control of a short positive average

\[
\sum_{j=0}^{J}a_j\,\chi^2(\nu_{\ell_n+j}\Vert\pi),
\qquad a_j\ge0,\quad \sum_j a_j=1,
\]

with `J=o(sqrt(log n))`, and prove that such averaged Green control still transfers the same TV profile. The spectral side can then exploit cancellation/averaging across the nonbacktracking polynomial family without requiring every exceptional mode to be small at the same radius. This stays complementary to NM13-01's growing hidden-memory / root-stabilizer likelihood route and attacks the remaining general-transitivity obstruction rather than producing another one-off graph operation.

## 12. ledger_delta

```yaml
slot: P26
parent: T08
source: Salez arXiv:2508.21055 Problem 2.3
runtime_model: GPT-5.6 Sol
runtime_reasoning: UNVERIFIED
parent_status_before: PARTIAL / OPEN
parent_status_after: PARTIAL / OPEN
source_level_advance: >-
  Strictly enlarges the proved source-compatible cutoff subclasses from individual
  biregular distances to every fixed exact bigraph distance 2m, m>=4, on the p=2
  EFMP Eisenstein Cayley bigraph family.
mechanism_advance: >-
  All-distance spherical/Chebyshev transfer: exact-distance operators obey a common
  recurrence, yielding |lambda_nontrivial(Q_m)| <= 2^{-m} for every fixed m>=4,
  together with closed radial drift/variance formulas and hence explicit Gaussian profiles.
transfer_criterion: >-
  Exact Green-shell TV squeeze with exponential shell cleanup; fixed epsilon costs
  O(log(1/epsilon)) radial layers and does not widen the sqrt(log n) radial window.
new_class: exact bigraph-distance-eight left graphs of EFMP p=2 Eisenstein Cayley bigraphs
new_class_degree: 73728
new_class_vertex_transitive: true
new_class_cayley: true
new_class_spectral_gap_lower: 15/16
new_class_long_range_expander: false
new_class_center: (24576/93935) log_16 n + O(1)
new_class_window: Theta(sqrt(log n))
new_class_profile_tau_squared: 221485222330368/828862171175375
all_m_scope: every fixed m>=4, degree 18*16^(m-1), gap >= 1-2^(-m)
proof_status: CANDIDATE_FULL pending later independent review
publication_novelty: UNVERIFIED
companion_split: >-
  NM13-01 owns growing automorphism-memory / semidirect / root-stabilizer likelihood routes;
  P26 owns shell Green / spherical-spectrum / radial-clock transfer.
checker: 2026-09-20_13-00-56__distance-allm-green-checker.py
checker_output: 2026-09-20_13-00-56__distance-allm-green-checker.out
checker_result: ALL_CHECKS_PASS
residual_obstruction: >-
  Derive near-entropic shell Green control directly from arbitrary bounded-degree vertex
  transitivity plus ordinary spectral expansion, without arithmetic Sarnak-Xue input.
next_attack: >-
  Prove a short-radius averaged/Tauberian Green-shell transfer and use spectral averaging
  across the NBRW polynomial family to dilute exceptional modes, with averaging length
  o(sqrt(log n)).
```

End of complete P26 substantive T08 report.
