Model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — no separately authenticated maximum-effort metadata is exposed.

# P26 / LIVE20 T08 — finite-orbit Green transfer and cutoff on edge-Cayley line graphs of Ramanujan bigraphs

**Parent status:** `PARTIAL / OPEN` for Salez Problem 2.3 before this run; `PARTIAL / OPEN` after this run.

**Restricted theorem status:** `CANDIDATE_FULL` for Theorems A–D below, pending later independent review.

**Publication novelty:** `UNVERIFIED`. A bounded web search for combinations of `line graph`, `biregular`, `Ramanujan bigraph`, `cutoff`, and `(9,3)` did not recover a matching ordinary-SRW cutoff theorem. This is negative evidence only, not a priority certificate.

Repository/branch: `yspennstate/math-open-problems` / `master`.
Controlling policy: `operations/PROGRESS20_2026-09-20.md`.
Run root: `proofnet24/P26-progress-cutoff-transfer/runs/2026-09-20/`.

## 0. Compact handoff, failed-route preservation, and C28/NM13-01 split

The newest own substantive report read before this run was

`2026-09-20_14-00-00__tauberian-parity-green-transfer.md`.

It proved a positive averaged-shell Green criterion and applied the two-shell filter `(1/2,1/2)` to odd-distance walks on bipartite Ramanujan Cayley graphs, where every individual shell retains a permanent parity mode. Its recorded next obstruction was the positive exceptional NBRW sector, which cannot in general be cancelled by a positive scalar shell filter.

That obstruction is preserved. So are two earlier failed/unproved routes: the Ihara/first-repeated-directed-edge tangle decomposition is not promoted to a theorem, and a global point-mass heat-kernel `L^2` criterion remains too strong for the parent problem.

The newest relevant historical-C28 successor report read was NM13-01's

`2026-09-20T10-30-00Z__normalizing-voltage-two-front-cutoff.md`.

NM13-01 owns an algebraic hidden-coordinate route: normalizing voltage lifts, exact TV factor transfer, and two macroscopic mixing fronts. P26 remains complementary: covering-space shells, Green functions, spherical/edge spectra, and radial clocks. The present run is not another graph-distance polynomial. It moves to a quasi-homogeneous universal cover whose line-graph spheres have **two stabilizer orbits**, requiring a finite-orbit Green transfer and a Markov-additive radial CLT.

There is no three-unchanged-run trigger: the preceding run changed the transfer mechanism to Tauberian shell averaging, while this run changes both the shell geometry (one orbit -> two orbits) and the radial clock (i.i.d.-like radial increments -> a two-state Markov additive process).

The root `POSTED.md` exclusion registry was read. In particular, nothing below reopens the posted Salez Problem 2.4 / Abelian Cayley product-condition result.

## 1. Exact source convention and current exact boundary

Justin Salez, `arXiv:2508.21055v1` (28 August 2025), inserts independent mean-one exponential waiting times between discrete transitions. If `P` is the discrete transition matrix, the exact convention is

\[
H_t=e^{t(P-I)}=e^{-t}\sum_{j\ge 0}\frac{t^jP^j}{j!}.
\tag{1.1}
\]

Problem 2.3 is exactly

> Prove that all vertex-transitive expanders exhibit cutoff.

There an expander sequence has diverging size, uniformly bounded degree, and one-sided spectral gap bounded away from zero.

The freshly checked September 2026 boundary remains strictly narrower.

* Dylan J. Altschuler, `arXiv:2609.14945v1`, submitted 14 September 2026, proves Gaussian-profile cutoff for every fixed-degree **long-range expander** sequence. The same paper proves the strict hierarchy `Ramanujan => long-range => spectral`, with neither converse. Its long-range hypothesis is therefore not synonymous with the spectral-expander hypothesis in Salez Problem 2.3.
* Francesco Pedrotti--Justin Salez, `arXiv:2607.05345`, submitted 6 July 2026, prove a local-product / non-equilibrium-Poincare criterion with window `O(1/gamma_*)`; the checked statement does not derive the required `gamma_*` estimate from vertex transitivity plus an ordinary fixed spectral gap.
* Shai Evra--Brooke Feigon--Kathrin Maurischat--Ori Parzanchevski (EFMP), `arXiv:2312.06507v3`, revised 6 April 2026, construct fully Ramanujan and adj-Ramanujan biregular Cayley bigraphs and prove sharp NBRW mixing estimates. Their Corollary 4.12 is the Green input used below. Their Theorem 8.7 gives an Eisenstein `p=2` congruence subgroup acting simply transitively on the **edges** of the `(9,3)` Bruhat--Tits tree, and its proof invokes their Theorem 7.3(1) for the Ramanujan property.

## 2. Parent before/after and mechanism-level movement

### Parent before

Salez Problem 2.3 was open. P26 had already proved several transitive spectral-but-not-long-range classes using one-orbit endpoint shells: regular line graphs, finite-fiber closures, regular graph powers/distance sets, biregular halves/exact even distances, and the preceding parity-smoothed odd-distance class.

### Parent after

Salez Problem 2.3 remains open. The proved source-valid scope is enlarged to a new class:

> **ordinary rate-one continuous-time SRW on line graphs of suitable edge-regular fully Ramanujan `(9,3)` arithmetic bigraphs has an explicit Gaussian cutoff profile.**

The outputs are `10`-regular vertex-transitive Cayley spectral expanders, have a fixed one-sided gap at least

\[
\frac35-\frac{3\sqrt3}{10}>0.08038,
\tag{2.1}
\]

and fail every fixed long-range-expansion constant. Their cutoff center is

\[
\boxed{\,4\log_4 n+O(1)=2\log_2 n+O(1)\,}
\tag{2.2}
\]

with a `Theta(sqrt(log n))` Gaussian window.

This class is not covered by the earlier regular-ancestor line-graph theorem: the ancestor is genuinely biregular, its line-tree spheres split into two orbits, and the radial clock has persistent two-state memory.

### Mechanism-level advance

The reusable new theorem is a **finite-orbit shell Green transfer**. It removes the assumption that the root stabilizer acts transitively on each lifted sphere. A bounded number of shell types is allowed, with uniform late-shell Green control over all types. This is exactly what the biregular line graph needs.

The second reusable calculation is the exact two-state Markov-additive radial clock on `L(T_{K+1,k+1})`, including closed formulas for its speed and continuous-time variance rate.

## 3. Theorem A — finite-orbit shell Green transfer

Let `Y_n` be a finite transitive regular graph with uniform stationary law `pi_n`, and let its rate-one continuous-time SRW satisfy the exact decomposition

\[
\delta_xH_t
=\sum_{r\ge0}\sum_{\sigma\in\Sigma}p_{n,t}(r,\sigma)\nu_{n,r,\sigma}^{x},
\tag{3.1}
\]

where `Sigma` is a fixed finite type set; at radii where a type is absent its mass is zero. Put

\[
R_t=r\quad\text{on the summand }(r,\sigma).
\]

Assume that for every `h>=0`,

\[
\sup_x\sup_{\sigma\in\Sigma}\sup_{r\ge\ell_n+h}
\chi^2(\nu_{n,r,\sigma}^{x}\Vert\pi_n)
\le G_n(h),
\tag{3.2}
\]

and that all shell supports with `r<=ell_n-h`, over all types, lie in a set `A_{n,x}(ell_n-h)` satisfying

\[
\sup_x\pi_n(A_{n,x}(\ell_n-h))\le L_n(h).
\tag{3.3}
\]

Then

\[
\boxed{
\Pr(R_t\le\ell_n-h)-L_n(h)
\le d_n(t)
\le \Pr(R_t<\ell_n+h)+\frac12\sqrt{G_n(h)}.
}
\tag{3.4}
\]

Here `d_n(t)` is worst-start TV distance; transitivity makes the displayed start immaterial.

### Proof

For the lower bound let `A=A_{n,x}(ell_n-h)`. By (3.1) and the support hypothesis,

\[
\delta_xH_t(A)\ge\Pr(R_t\le\ell_n-h),
\]

while `pi_n(A)<=L_n(h)`. Testing total variation against `A` gives the left inequality.

For the upper bound write `q=Pr(R_t<ell_n+h)`. The early mixture contributes at most `q` to TV. Conditional on the late event, the law is a convex combination of shells with `r>=ell_n+h`. For every such shell, Cauchy--Schwarz gives

\[
\|\nu_{n,r,\sigma}^{x}-\pi_n\|_{TV}
\le\frac12\sqrt{\chi^2(\nu_{n,r,\sigma}^{x}\Vert\pi_n)}
\le\frac12\sqrt{G_n(h)}.
\]

TV is convex, so the late mixture obeys the same bound. This proves (3.4). `QED`

### Quantitative profile corollary

Suppose `w_n -> infinity`, `h_n=o(w_n)`, `G_n(h_n)+L_n(h_n)=o(1)`, and

\[
\Pr(R_{T_n+zw_n}<\ell_n+o(w_n))\to F(z)
\tag{3.5}
\]

for every fixed `z`. Then (3.4) yields

\[
\boxed{d_n(T_n+zw_n)\to F(z).}
\tag{3.6}
\]

Thus the number of universal-cover shell orbits is irrelevant as long as it stays bounded and all types have the same late Green front.

## 4. The line graph of a biregular tree: exact two-orbit shell structure

Let

\[
X=(L\sqcup R,E)
\]

be a finite connected `(K+1,k+1)`-biregular simple graph, `K>k>=2`, and let

\[
Y=L(X)
\]

be its line graph. A vertex of `Y` is an edge of `X`; two such vertices are adjacent when the corresponding edges of `X` share an endpoint. Therefore `Y` is

\[
\boxed{D=K+k}
\tag{4.1}
\]

regular.

Let `T=T_{K+1,k+1}` be the universal covering tree of `X`. The covering `T->X` induces a graph covering

\[
L(T)\longrightarrow L(X),
\tag{4.2}
\]

because the incident edges at each endpoint are carried bijectively to the corresponding incident edges downstairs.

Fix a root edge `e_0` of `T`. For an edge `e` at line-graph distance `r>=1` from `e_0`, the unique edge-geodesic from `e_0` to `e` in `T` has a distinguished far endpoint. There are two types:

* `A`: the far endpoint lies in `R`;
* `B`: the far endpoint lies in `L`.

The stabilizer of `e_0` in `Aut(T)` is transitive on each `(r,A)` and `(r,B)` orbit. Hence rate-one SRW on `L(T)`, started at `e_0`, is uniform conditional on `(R_t=r,S_t=sigma)`.

More concretely, the two orbit laws are ordinary directed-edge NBRW laws on `X`. To obtain type `A`, orient the root edge toward its `R` endpoint and run NBRW for `r` transitions; to obtain type `B`, orient it toward `L`. On a tree, a directed nonbacktracking edge path is exactly a line-graph geodesic. Forgetting the terminal orientation is a bijection on the relevant orientation class. Consequently the projected finite-graph walk has the exact shell representation

\[
\boxed{
\delta_{e_0}e^{t(Q_Y-I)}
=\sum_{r,\sigma}\Pr(R_t=r,S_t=\sigma)\nu_{r,\sigma},
}
\tag{4.3}
\]

with each `nu_{r,sigma}` an `r`-step NBRW edge-endpoint law.

No discrete-time substitution or lazification has occurred: the outer clock in (4.3) is exactly Salez's rate-one Poisson clock.

The universal-cover line spheres have exact sizes, writing `S=Kk`,

\[
|\mathcal S_{2m}|=2S^m\quad(m\ge1),
\qquad
|\mathcal S_{2m+1}|=D S^m\quad(m\ge0).
\tag{4.4}
\]

Indeed, a two-step outward move multiplies either branch by `Kk`. Thus

\[
|B_{L(T)}(e_0,r)|\le C_{K,k}(\sqrt{Kk})^r.
\tag{4.5}
\]

For `n=|E(X)|=|V(Y)|`, the entropic radius is therefore

\[
\boxed{\ell_n=\log_{\sqrt{Kk}}n+O(1).}
\tag{4.6}
\]

The early support term in Theorem A obeys

\[
\boxed{L_n(h)\le C_{K,k}(Kk)^{-h/2}.}
\tag{4.7}
\]

## 5. Theorem B — a Ramanujan NBRW Green front supplies both shell types

Assume now that `X` is a fully Ramanujan `(K+1,k+1)` bigraph. EFMP Corollary 4.12 gives, for the nonbacktracking adjacency `B` and every integer `t>=1`,

\[
\left\|B^{2t}|_{L_0^2(E)}\right\|_2
\le t\sqrt{2(Kk)^{t+1}}.
\tag{5.1}
\]

After normalizing `B^{2t}` by `(Kk)^t`, their proof of Theorem 4.13 yields from any oriented edge `e`

\[
\|p_e^{2t}-u\|_2
\le t\sqrt{2Kk}\,(Kk)^{-t/2},
\tag{5.2}
\]

where `u` is uniform on the corresponding orientation class. If that class has `n` states (up to the harmless fixed orientation convention),

\[
\boxed{
\chi^2(p_e^{2t}\Vert u)
\le 2(Kk)n t^2(Kk)^{-t}.
}
\tag{5.3}
\]

One NBRW step between the two orientation classes is doubly stochastic: every row and every column has the same number of allowed nonbacktracking continuations. Therefore chi-square contracts at odd times as well.

Combining (4.3), data processing under forgetting orientation, and (5.3), there is a constant `C=C(K,k)` such that for all sufficiently large `n` and all `h>=2`,

\[
\boxed{
G_n(h)
\le C(\ell_n+h+2)^2(Kk)^{-h/2}.
}
\tag{5.4}
\]

To see the exponent, at an even shell `r=2t>=ell_n+h`,

\[
t\ge\log_{Kk}n+h/2+O(1),
\]

so `n(Kk)^{-t}<=C(Kk)^{-h/2}`; the function `t^2(Kk)^{-t}` is decreasing beyond a fixed constant. Odd shells follow by contraction.

Taking for example

\[
h_n=8\log_{Kk}\ell_n,
\tag{5.5}
\]

we obtain

\[
G_n(h_n)+L_n(h_n)=o(1),
\qquad
h_n=O(\log\log n)=o(\sqrt{\log n}).
\tag{5.6}
\]

This is the promised quantitative Green transfer: the shell cleanup costs only `O(log log n)` radial layers, far below the radial `sqrt(log n)` front.

## 6. Theorem C — exact two-state radial speed and continuous-time variance

Away from the root, the line-radius/type pair is a Markov additive chain. From type `A` (far endpoint in `R`), a line-graph SRW step has

\[
\begin{array}{c|ccc}
\Delta R&-1&0&+1\\ \hline
\#&1&K-1&k,
\end{array}
\tag{6.1}
\]

while from type `B`,

\[
\begin{array}{c|ccc}
\Delta R&-1&0&+1\\ \hline
\#&1&k-1&K.
\end{array}
\tag{6.2}
\]

Each row totals `D=K+k`. The type transition matrix is

\[
P_{\rm typ}=\frac1D
\begin{pmatrix}
K-1&k+1\\
K+1&k-1
\end{pmatrix},
\tag{6.3}
\]

with stationary law

\[
\boxed{
\pi_A=\frac{K+1}{D+2},
\qquad
\pi_B=\frac{k+1}{D+2}.
}
\tag{6.4}
\]

The conditional drifts are `(k-1)/D` and `(K-1)/D`, so the asymptotic radial speed is

\[
\boxed{
v=\frac{2(Kk-1)}{D(D+2)}.
}
\tag{6.5}
\]

For the exact continuous-time variance, introduce the tilted one-jump matrix

\[
M_\theta=\frac1D
\begin{pmatrix}
K-1&e^{-\theta}+ke^{\theta}\\
e^{-\theta}+Ke^{\theta}&k-1
\end{pmatrix}.
\tag{6.6}
\]

Its Perron eigenvalue is

\[
\lambda(\theta)=
\frac{D-2+\sqrt{(K-k)^2+4(e^{-\theta}+ke^{\theta})(e^{-\theta}+Ke^{\theta})}}{2D}.
\tag{6.7}
\]

A rate-one Poisson clock changes the tilted generator to `M_theta-I`, so the cumulant rate is `lambda(theta)-1`. Direct differentiation at zero gives

\[
\lambda'(0)=v
\tag{6.8}
\]

and

\[
\boxed{
\sigma^2:=\lambda''(0)
=
\frac{4\left[(Kk+1)(D+2)^2-2(Kk-1)^2\right]}
{D(D+2)^3}.
}
\tag{6.9}
\]

The root is a negligible boundary perturbation. Since `k>=2`, both conditional interior drifts in (6.1)--(6.2) are positive. For sufficiently small `alpha>0`, uniformly over the two types,

\[
\mathbb E[e^{-\alpha\Delta R}\mid S_t]\le1-c\alpha<1.
\tag{6.10}
\]

Optional stopping before a return to zero gives a return probability from radius one strictly below one. Successive excursions therefore make a geometric number of root visits; the continuous holding times add only `O_P(1)` boundary time and displacement. Standard Perron--Frobenius perturbation of the finite matrix (6.6), or equivalently the Markov-additive CLT, yields

\[
\boxed{
\frac{R_t-vt}{\sqrt{\sigma^2t}}\Longrightarrow N(0,1).
}
\tag{6.11}
\]

Combining (3.4), (5.6), and (6.11), for

\[
T_n=\frac{\ell_n}{v},
\qquad
\tau^2=\frac{\sigma^2}{v^3},
\tag{6.12}
\]

we obtain the full profile

\[
\boxed{
 d_Y\left(T_n+z\sqrt{\ell_n}\right)
\longrightarrow
\Phi\left(-\frac z\tau\right).
}
\tag{6.13}
\]

In particular the TV cutoff window is `Theta(sqrt(log n))`.

## 7. Spectral transfer from a biregular ancestor to its line graph

Let `C` be the unsigned vertex-edge incidence matrix of `X`, and let `M` be the `L x R` biadjacency matrix. Then

\[
C^TC=2I+A_Y,
\qquad
CC^T=
\begin{pmatrix}
(K+1)I&M\\
M^T&(k+1)I
\end{pmatrix}.
\tag{7.1}
\]

If `s` is a singular value of `M`, the corresponding nonzero eigenvalues of `CC^T` solve

\[
(K+1-\theta)(k+1-\theta)-s^2=0,
\]

hence

\[
\theta_\pm(s)=
\frac{K+k+2\pm\sqrt{(K-k)^2+4s^2}}2.
\tag{7.2}
\]

The normalized line-walk eigenvalues are

\[
q_\pm(s)=\frac{\theta_\pm(s)-2}{K+k}.
\tag{7.3}
\]

There is also the usual flat line-graph band `-2/(K+k)` from `ker C`. The Perron singular value `sqrt((K+1)(k+1))` gives `q_+=1`; its zero partner belongs to `ker C^T` and does not create another edge eigenvalue.

For a `(9,3)` adj-Ramanujan ancestor (`K=8,k=2`), every nontrivial squared singular value satisfies

\[
s^2=0
\quad\text{or}\quad
2\le s^2\le18.
\tag{7.4}
\]

Now `D=10`, and

\[
q_+(s)=\frac25+\frac1{20}\sqrt{36+4s^2}
\]

is increasing. Therefore the largest nonconstant line eigenvalue is

\[
q_{\max}=q_+(\sqrt{18})
=\frac25+\frac{3\sqrt3}{10}.
\tag{7.5}
\]

The zero singular sector gives only `7/10` and `1/10`, while the flat band is `-1/5`. Hence

\[
\boxed{
\operatorname{gap}(Y)
\ge1-q_{\max}
=\frac35-\frac{3\sqrt3}{10}
>0.08038.
}
\tag{7.6}
\]

So the line outputs are genuine fixed-degree spectral expanders.

## 8. Theorem D — explicit degree-10 edge-Cayley class

We now supply the required proved application, not merely the framework.

EFMP Theorem 8.7 treats the Eisenstein group at `p=2`. In their notation,

\[
\Delta_{\mathscr E}^{2}=C\ltimes\Lambda_{\mathscr E}^{2}
\]

is a congruence subgroup and acts **simply transitively on the edges** of the `(9,3)` Bruhat--Tits tree. Their proof also states that the relevant Ramanujan property follows from Theorem 7.3(1); in the Eisenstein case Corollary 7.4 records that retaining the full level at the ramified prime `3` suffices.

Take a sequence `N_j` of sufficiently deep finite-index normal principal congruence subgroups of `Delta_E^2`, imposed at auxiliary primes away from `2,3`, and let

\[
X_j=N_j\backslash T_{9,3}.
\tag{8.1}
\]

Passing to a sufficiently deep subsequence removes the finitely many short stabilizers, so the quotients are finite simple bigraphs and `n_j:=|E(X_j)|->infinity`. Because `Delta_E^2` acts freely and transitively on tree edges and `N_j` is normal,

\[
\Delta_E^2/N_j
\]

acts freely and transitively on `E(X_j)`. Therefore

\[
Y_j:=L(X_j)
\tag{8.2}
\]

is a Cayley graph: the ten generators are the unique group elements taking a fundamental edge to its ten adjacent edges. In particular `Y_j` is vertex-transitive and `10`-regular.

The deeper auxiliary level leaves the `3`-adic component containing an Iwahori, so EFMP Theorem 7.3(1) applies at every level: `X_j` is fully Ramanujan. Thus Sections 5--7 apply without any extra girth hypothesis.

For `K=8,k=2`,

\[
D=10,\qquad Kk=16,\qquad \ell_n=\log_4 n+O(1).
\tag{8.3}
\]

The radial counts are exactly

\[
A:\ {-1:1,\ 0:7,\ +1:2},
\qquad
B:\ {-1:1,\ 0:1,\ +1:8}.
\tag{8.4}
\]

Equations (6.5) and (6.9) give

\[
\boxed{v=\frac14,}
\qquad
\boxed{\sigma^2=\frac{37}{80},}
\qquad
\boxed{\tau^2=\frac{148}{5}.}
\tag{8.5}
\]

Therefore ordinary SRW in Salez's exact rate-one convention has

\[
\boxed{
T_n=4\log_4n+O(1)=2\log_2n+O(1)
}
\tag{8.6}
\]

and the Gaussian profile

\[
\boxed{
 d_{Y_j}\left(4\log_4n_j+z\sqrt{\log_4n_j}\right)
\longrightarrow
\Phi\left(-z\sqrt{\frac5{148}}\right).
}
\tag{8.7}
\]

This is a new output walk, not EFMP's NBRW restated: EFMP supplies the edge-shell Green estimate, while (4.3) and the two-state radial clock transfer it to ordinary rate-one SRW on a different regular Cayley graph.

## 9. These outputs are not long-range expanders

For the `(9,3)` tree line graph, (4.5) gives

\[
|B_{Y_j}(e,r)|\le C4^r
\tag{9.1}
\]

for every quotient ball. But a `10`-regular long-range expander requires the singleton growth benchmark `9^r` up to macroscopic saturation. Take for example

\[
r_j=\left\lfloor\frac12\log_9n_j\right\rfloor.
\]

Then `9^{r_j}=O(sqrt(n_j))`, so the saturation branch in the long-range minimum is inactive for large `j`, while

\[
\frac{|B_{Y_j}(e,r_j)|}{9^{r_j}}
\le C\left(\frac49\right)^{r_j}\longrightarrow0.
\tag{9.2}
\]

Thus no fixed positive long-range-expansion constant can hold. The class is genuinely

\[
\boxed{\text{vertex-transitive spectral expander but not long-range expander}.}
\]

Altschuler's theorem therefore does not apply directly to the output sequence.

## 10. Exact checks executed in this run

The exact checker

`2026-09-20_14-57-03__biregular-line-green-check.py`

was executed before archival. It verifies:

1. the biregular incidence spectral transform and the exact `(9,3)` line-gap lower bound;
2. both radial multiplicity rows;
3. the stationary type law `(3/4,1/4)`;
4. `v=1/4` from both stationary averaging and the tilted eigenvalue;
5. the exact continuous-time variance rate `sigma^2=37/80`;
6. `tau^2=148/5`;
7. the branching mismatch `4<9`.

Its terminal output is

`P26_T08_BIGRAPH_LINE_GREEN_EXACT_PASS`.

Checker creation commit: `3499fa0f343ef9268c30c76635abfd7748090d95`.
Archived output creation commit: `589c6b0ea18735ff3779fe886e04c3576f7be1ee`.

## 11. Residual obstruction and next attack

The parent obstruction is not the finite number of local shell types: Theorem A removes that issue. Nor is a biregular/Markov-additive radial clock an obstruction: its profile can be computed exactly.

What remains is the production of a sufficiently small **late shell Green defect** from arbitrary vertex transitivity plus an ordinary spectral gap. In the present class that input still comes from the full Ramanujan NBRW operator estimate.

The preceding run showed that short positive scalar filters can cancel negative oscillatory exceptional modes but not genuinely slow positive modes. The new finite-orbit theorem suggests the next attack: replace scalar filters by a **positive matrix-valued filter on shell types**. For a finite-type universal-cover decomposition, allow

\[
\bar\nu_{r,a}=\sum_{j\le J}\sum_b A_j(a,b)\nu_{r+j,b},
\qquad A_j(a,b)\ge0,
\]

with row sums one. The objective is to use type switching to attenuate exceptional positive scalar modes through their nontrivial eigenvectors across shell types, while paying only `J=o(sqrt(log n))` radial smoothing. This is distinct from NM13-01's voltage/hidden-coordinate TV route and is a plausible way to attack the positive exceptional sector left by the scalar Tauberian theorem.

If that matrix-filter route fails twice, preserve the failure and switch to another unproved T01--T10 scope as required by LIVE20; no such switch is triggered in this run.

## 12. ledger_delta

```yaml
ledger_delta:
  parent: T08 Salez arXiv:2508.21055 Problem 2.3
  parent_before: OPEN/PARTIAL
  parent_after: OPEN/PARTIAL
  source_convention: "rate-one continuous time H_t = exp(t(P-I))"
  restricted_status: CANDIDATE_FULL_pending_independent_review
  publication_novelty: UNVERIFIED
  substantive_advances:
    - "finite-orbit shell Green-to-TV squeeze, allowing boundedly many stabilizer shell types"
    - "exact two-type Markov-additive radial clock on line graphs of biregular trees"
    - "closed speed v=2(Kk-1)/((K+k)(K+k+2)) and continuous-time variance formula"
    - "biregular incidence spectral transform for regular line outputs"
    - "proved degree-10 edge-Cayley arithmetic class with Gaussian cutoff"
    - "proved output gap >= 3/5-3sqrt(3)/10 and proved non-LRE by branching 4<9"
  concrete_application:
    ancestor: "deep congruence quotients of EFMP Theorem 8.7 edge-simply-transitive Ramanujan (9,3) tree action"
    output: "10-regular Cayley line graphs"
    cutoff_center: "4 log_4 n + O(1) = 2 log_2 n + O(1)"
    window: "Theta(sqrt(log n))"
    profile_variance_parameter: "tau^2 = 148/5 when window is sqrt(log_4 n)"
  c28_coordination:
    live_successor: NM13-01
    nm_route: "normalizing voltage lifts / hidden-coordinate TV / two macroscopic fronts"
    p26_route: "finite-orbit shell Green / edge spectra / Markov-additive radial clocks"
  preserved_failures:
    - "Ihara first-repeat tangle bound remains unproved"
    - "global point-mass heat-kernel L2 remains too stringent"
    - "positive exceptional shell modes remain the main scalar-filter obstruction"
  not_counted_as_advances:
    - source recovery
    - literature receipts
    - repeated exact checks
    - commit hashes
  next_attack: "positive matrix-valued shell filters across finite shell types to damp the positive exceptional sector"
  checker_commit: 3499fa0f343ef9268c30c76635abfd7748090d95
  checker_output_commit: 589c6b0ea18735ff3779fe886e04c3576f7be1ee
```

End of complete P26 substantive T08 report.
