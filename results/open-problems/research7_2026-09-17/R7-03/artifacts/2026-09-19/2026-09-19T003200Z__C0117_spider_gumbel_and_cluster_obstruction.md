# C0117: spider Gumbel calibration and a clustered-late-set obstruction

Model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — this is **not GPT-6 at maximum**; no authenticated runtime model/effort telemetry or binding selector is exposed.

Target: Ding–Lee–Peres, *Cover times, blanket times, and majorizing measures*, Annals of Mathematics 175 (2012), Section 5, Question 5.2.  Frozen source-scale metric remains

\[
\beta_{\rm cert}:=\sup\Bigl\{\beta\in[1/2,1]:\ \operatorname{SD}(\tau_{\rm cov})\le C\,t_{\rm hit}^{\beta}t_{\rm cov}^{1-\beta}
\text{ has a written universal proof in source-compatible scope}\Bigr\}.
\]

This artifact is a mathematical research record, not a novelty claim. In particular, Higuchi–Ohwa–Shirai (2010), *Exact computation for the cover times of certain classes of trees*, already gives exact expectation/Laplace-transform formulae for spider graphs. The elementary spider derivation below is used as a sharp calibration for the DLP fluctuation question; bounded prior-art search has not established which precise asymptotic statements below are explicitly written in that paper.

## 1. B14: quotient the equal-arm spider by symmetry

Let `Sp(k,L)` be the tree made from `k>=2` disjoint paths of length `L>=1` whose initial vertices are identified to one centre `o`.  Write `(i,d)` for depth `d` on arm `i`, and `e_i=(i,L)` for its endpoint.  Simple random walk starts at the centre unless stated otherwise.

Covering the graph is equivalent to hitting every endpoint, because a walk that reaches `e_i` necessarily traverses every vertex of arm `i`.

### Proposition 1 (exact maximal hitting time)

For `Sp(k,L)`,

\[
\boxed{t_{\rm hit}=2kL^2.}
\]

**Proof.** The tree has `|E|=kL` edges.  For an endpoint `e_i`, the expected time to hit the centre is the standard one-dimensional value

\[
E_{e_i}T_o=L^2.
\]

The effective resistance between `o` and `e_i` is `L`, so the commute identity gives

\[
E_oT_{e_i}+E_{e_i}T_o=2|E|R_{\rm eff}(o,e_i)=2kL^2,
\]

hence `E_oT_{e_i}=(2k-1)L^2`.  For distinct endpoints, every path from `e_i` to `e_j` hits `o`, and therefore

\[
E_{e_i}T_{e_j}=L^2+(2k-1)L^2=2kL^2.
\]

For a target `(j,d)`, `1<=d<=L`, commute with the centre and the path hitting formula give

\[
E_{(j,d)}T_o=d(2L-d),
\]

\[
E_oT_{(j,d)}=2kLd-d(2L-d)=2(k-1)Ld+d^2.
\]

If source and target lie on different arms, add the source-to-centre term; the resulting expression is maximized at `d=L` at both ends and equals `2kL^2`.  If they lie on the same arm, the commute time is at most `2kL^2`, so either directed hitting time is at most this.  Thus distinct endpoints attain the maximum. ∎

### Excursion quotient

Each departure from `o` chooses an arm uniformly in `{1,...,k}`. Ignore the arm label and retain only radial depth. Between visits to `o` the radial walk is the simple walk on `{0,1,...,L}`, with `0` ending an excursion and `L` reflecting after it is reached. By gambler's ruin, an excursion hits depth `L` before returning to `0` with probability `1/L`.

Now group raw excursions into **success blocks**: one block starts at `o`, continues through as many failed excursions as necessary until an endpoint is hit, and ends upon the subsequent return to `o`. Let `Z` be its duration and `J` its successful arm label.

The radial process from `o` until first hit of depth `L` is the reflected-at-zero birth–death chain. Solving the elementary difference equation gives

\[
E_oT_L=L^2.
\]

From `L` back to `0` the mean is also `L^2`; therefore

\[
\boxed{EZ=2L^2.}
\]

Moreover there is a universal constant `C` with

\[
E Z^2\le C L^4. \tag{1}
\]

Indeed, for either one-dimensional hitting segment the maximal expected remaining hitting time is at most `L^2`; Markov's inequality followed by the strong Markov property gives

\[
P(T>2mL^2)\le 2^{-m},
\]

which implies a uniform `O(L^4)` second-moment bound. Apply `(A+B)^2<=2A^2+2B^2` to the two segments of `Z`.

The arm labels used on raw excursions are iid uniform and independent of all radial paths. Consequently the successful labels `J_1,J_2,...` are iid uniform on `{1,...,k}` and are independent of the iid success-block durations `Z_1,Z_2,...`.

Let `N_k` be the ordinary coupon-collector number of iid uniform labels needed to see all `k` labels. If `T^+` is the time at which the walk returns to the centre *after* the successful block that first completes all arms, then

\[
\boxed{T^+=\sum_{j=1}^{N_k}Z_j,\qquad N_k\perp (Z_j)_{j\ge1}.} \tag{2}
\]

The actual cover time `tau` ends at the first hit of the last new endpoint, not at the following return to the centre. Thus

\[
T^+-\tau=R,
\]

where, by the strong Markov property at that endpoint hit,

\[
ER=L^2,\qquad ER^2=O(L^4). \tag{3}
\]

### Proposition 2 (exact worst-start mean)

With centre start,

\[
\boxed{E_o\tau=2kL^2H_k-L^2.} \tag{4}
\]

Moreover the centre is the worst start. More exactly, if `x=(i,d)` has depth `d`, then

\[
\boxed{E_x\tau=E_o\tau-d^2.} \tag{5}
\]

Hence

\[
\boxed{t_{\rm cov}=2kL^2H_k-L^2=t_{\rm hit}\left(H_k-\frac1{2k}\right).} \tag{6}
\]

**Proof.** From (2), `EN_k=kH_k`, so `ET^+=2L^2 kH_k`; subtract `ER=L^2` from (3), proving (4).

For (5), before a walk started at depth `d` can cover any other arm it must hit the centre. The expected time to the centre is `d(2L-d)`. The probability of hitting the endpoint of its own arm before the centre is `d/L`. If that happens, one endpoint coupon is already collected on arrival at the centre; otherwise none is. From the centre, the expected remaining cover time when one prescribed endpoint is already collected is

\[
2kL^2H_{k-1}-L^2.
\]

Therefore, denoting the value in (4) by `C_k`,

\[
\begin{aligned}
E_x\tau
&=d(2L-d)+\frac dL\bigl(2kL^2H_{k-1}-L^2\bigr)+\left(1-\frac dL\right)C_k\\
&=C_k-d^2,
\end{aligned}
\]

because `C_k-(2kL^2H_{k-1}-L^2)=2L^2`. ∎

This exact identity simultaneously verifies the source centering convention on this family and generalizes the `L=1` star calculation.

### Proposition 3 (uniform-in-arm-length Gumbel fluctuation law)

Let `L=L_k` be **arbitrary**, possibly tending to infinity with `k`. For centre-start simple random walk on `Sp(k,L_k)`,

\[
\boxed{\frac{\tau-t_{\rm cov}}{t_{\rm hit}}\ \Rightarrow\ G-\gamma,} \tag{7}
\]

where `G` is the standard Gumbel law `P(G<=x)=exp(-e^{-x})` and `gamma` is Euler's constant. In particular,

\[
\boxed{\frac{\operatorname{SD}(\tau)}{t_{\rm hit}}\longrightarrow\frac{\pi}{\sqrt6}=1.282549830\ldots.} \tag{8}
\]

**Proof.** The coupon collector satisfies

\[
\frac{N_k-k\log k}{k}\Rightarrow G,
\]

\[
EN_k=kH_k,\qquad \operatorname{Var}N_k=k^2H_k^{(2)}-kH_k. \tag{9}
\]

Condition on `N_k` in (2). From `(1)` and `EZ=2L^2`,

\[
E\left[\left(\frac{T^+-2L^2N_k}{2kL^2}\right)^2\right]
=\frac{\operatorname{Var}(Z)EN_k}{4k^2L^4}
=O\left(\frac{\log k}{k}\right), \tag{10}
\]

uniformly in `L=L_k`. By (3),

\[
\frac{R-ER}{2kL^2}\to0
\]

in `L^2`, also uniformly in `L`. Therefore

\[
\frac{\tau-2kL^2\log k}{2kL^2}
-\frac{N_k-k\log k}{k}\to0
\]

in probability. Proposition 1 says the denominator is exactly `t_hit`; Proposition 2 and `H_k-\log k\to\gamma` shift the centre by `gamma`, proving (7).

For the variance, the independent random-sum identity gives

\[
\operatorname{Var}(T^+)=\operatorname{Var}(Z)EN_k+(EZ)^2\operatorname{Var}(N_k).
\]

Divide by `t_hit^2=4k^2L^4`. The first term is `O((\log k)/k)`, while the second equals

\[
\frac{\operatorname{Var}N_k}{k^2}=H_k^{(2)}-\frac{H_k}{k}\longrightarrow\frac{\pi^2}{6}.
\]

Equation (3) changes the centered `L^2` norm by only `O(L^2)`, which after division by `2kL^2` is `O(1/k)`. This proves (8). ∎

### Consequences for DLP Question 5.2

This family lies precisely in the qualitative concentration regime:

\[
\frac{t_{\rm cov}}{t_{\rm hit}}=H_k-\frac1{2k}\sim\log k\to\infty,
\]

while the fluctuations remain of exact order `t_hit`.

Thus any universal coefficient in a putative estimate

\[
\operatorname{SD}(\tau_{\rm cov})\le C t_{\rm hit}
\]

must satisfy

\[
\boxed{C\ge\pi/\sqrt6.} \tag{11}
\]

This strengthens the previous finite seven-vertex calibration `C>1.0433...`, but it does **not** prove or refute the existence of a finite universal `C`.

The upper tail of `G-gamma` is asymptotic to `e^{-x}`. Therefore a universal two-sided tail inequality with fixed prefactor and normalization exactly by `t_hit` cannot have exponential rate parameter strictly larger than `1`. DLP asks only for some positive universal rate, so this is a sharpness calibration, not closure.

## 2. B20: why the raw unvisited-vertex variance bridge fails

The preceding run proved that a bound of the form

\[
\operatorname{Var}(U_t)\le C\,E U_t,\qquad U_t:=\#\{v:T_v>t\}, \tag{12}
\]

near the cover threshold would imply the desired `t_hit`-scale tails. The next question is whether (12) is even universally plausible. It is not.

Let `D_r` be two copies `A,B` of `K_r` joined by a single bridge `a-b`, where `a in A`, `b in B`; start at a non-bridge vertex of `A`. Fix `alpha>0` and put `t_r=floor(alpha r^2)`.

### Proposition 4 (two-clique late-set clustering)

For `D_r`,

\[
\boxed{\frac{U_{t_r}}r\ \longrightarrow\ \operatorname{Bernoulli}(e^{-\alpha})\quad\text{in }L^2.} \tag{13}
\]

Consequently

\[
EU_{t_r}\sim r e^{-\alpha},\qquad
\operatorname{Var}(U_{t_r})\sim r^2e^{-\alpha}(1-e^{-\alpha}), \tag{14}
\]

and hence

\[
\boxed{\frac{\operatorname{Var}(U_{t_r})}{EU_{t_r}}\sim r(1-e^{-\alpha})\to\infty.} \tag{15}
\]

So the universal raw-vertex hypothesis (12) is false.

**Proof.** Until the bridge endpoint `b` is hit, the killed walk in `A` lumps to two states: `a` and `o=A\setminus\{a\}`. Its substochastic matrix is

\[
Q_r=\begin{pmatrix}
0&(r-1)/r\\
1/(r-1)&(r-2)/(r-1)
\end{pmatrix}.
\]

The dominant eigenvalue is

\[
\lambda_r=\frac12\left(\frac{r-2}{r-1}+\sqrt{\left(\frac{r-2}{r-1}\right)^2+\frac4r}\right)
=1-\frac1{r^2}+O(r^{-4}), \tag{16}
\]

while the second eigenvalue is `O(1/r)` in magnitude. The coefficient of `lambda_r^t` in the survival probability from `o` tends to `1`. Hence

\[
P(T_b>\lfloor\alpha r^2\rfloor)\to e^{-\alpha}. \tag{17}
\]

It remains to show that, apart from a vanishing event, the unvisited set has size `r+o(r)` when `T_b>t_r`, and size `o(r)` when `T_b<=t_r`.

First, conditional paths that remain in `A` have the same moves as `K_r` except that each departure from `a` pays an extra survival factor `(r-1)/r<=1`. Therefore, for any time `s`,

\[
P(T_b>s,\ A\text{ not covered by }s)
\le P_{K_r}(\tau_{\rm cov}>s).
\]

Since the complete-graph cover mean is `O(r\log r)`, taking `s=r^{3/2}` and Markov gives an `o(1)` bound. By (16), `P(T_b<=r^{3/2})=o(1)` and likewise the probability that `T_b` lies in the last `r^{3/2}` steps before `t_r` is `o(1)`.

After crossing to `b`, consider the next `M=r\log^2r` steps. If the bridge is suppressed, this is `K_r`; its expected cover time is `O(r\log r)`, so it fails to cover `B` by time `M` with probability `O(1/\log r)`. The probability of recrossing the bridge before this cover is also `o(1)`: at a visit to `b` the exit hazard is `1/r`, while the expected number of visits to `b` during the first `M` steps of `K_r` is at most `M/r+O(1)=O(\log^2r)`, hence the bridge-exit probability is `O(\log^2r/r)`. Since `M=o(r^{3/2})`, a crossing outside the two negligible endpoint windows therefore leaves enough time, with probability `1-o(1)`, for both cliques to be fully covered.

Thus

\[
\frac{U_{t_r}}r-\mathbf 1_{\{T_b>t_r\}}\to0
\]

in probability. Both terms are uniformly bounded by `2`, so convergence is in `L^2`; (13)–(15) follow from (17). ∎

This is a **route obstruction**, not a source counterexample. On `D_r`, both `t_hit` and `t_cov` are `Theta(r^2)`, so the ratio `t_cov/t_hit` stays bounded. The example says that raw vertices are the wrong units for a universal second-moment argument: a whole clique can survive as one late block.

## 3. B5: deform the spider bottleneck and watch the normalized law

The arm length `L` is a bottleneck parameter. Proposition 3 was deliberately proved uniformly for arbitrary `L=L_k`; therefore even making each late arm a macroscopically large cluster does **not** increase the cover fluctuation relative to `t_hit`:

\[
\frac{\operatorname{SD}(\tau)}{t_{\rm hit}}\to\frac{\pi}{\sqrt6}
\quad\text{for every sequence }L_k\ge1. \tag{18}
\]

At the same time

\[
\frac{t_{\rm cov}}{t_{\rm hit}}\sim\log k.
\]

So lengthening a symmetric bottleneck multiplies both the coupon-collection renewal time and the maximal hitting time by the same `L^2` factor; it does not manufacture an unbounded `SD/t_hit` ratio. The gluing obstruction is therefore not “large late clusters” by itself. What matters is whether the **number and geometry of effective late blocks** can create correlations more severe than coupon collection after time has been normalized by the maximal hitting scale.

This points to a corrected replacement for (12): count late *blocks* at a scale controlled by hitting geometry rather than late vertices. The spider quotient makes that replacement exact: the effective objects are the `k` endpoint labels, and their last-discovery law is ordinary coupon collection.

## 4. Literature/status check dated 2026-09-19

Primary source: Ding–Lee–Peres, Annals of Mathematics 175 (2012), Question 5.2, DOI `10.4007/annals.2012.175.3.8`, official page `https://annals.math.princeton.edu/2012/175-3/p08`.

Bounded fresh searches through 2026-09-19 recovered no paper claiming a source-matching universal `t_hit`-scale standard-deviation bound plus constant-rate exponential tail. This is negative evidence only.

Relevant known work checked:

1. David Aldous, *Threshold Limits for Cover Times*, J. Theoret. Probab. 4 (1991), proves qualitative threshold concentration for finite Markov chains when expected cover time dominates maximal hitting time. Its abstract covering theorem controls variance through the expected cover time of a terminal set; it does not supply the DLP `t_hit`-scale rate.
2. Jian Ding, *Asymptotics of cover times via Gaussian free fields: bounded-degree graphs and general trees*, Ann. Probab. 42 (2014), gives exponential concentration for general trees at the geometric-mean scale and asymptotic GFF formulae in the regime `t_hit=o(t_cov)`.
3. Alex Zhai, *Exponential concentration of cover times* (arXiv:1407.7617; EJP), gives general GFF-based exponential concentration, again with the generic geometric-mean contribution rather than the pure source scale.
4. Jonathan Hermon, *A Spectral Characterization for Concentration of the Cover Time*, J. Theoret. Probab. 33 (2020), characterizes asymptotic concentration for vertex-transitive graphs and a broader reversible class, not the universal DLP quantitative endpoint.
5. Yusuke Higuchi, Takuya Ohwa, Tomoyuki Shirai, *Exact computation for the cover times of certain classes of trees*, Journal of Math-for-Industry 2 (2010), computes expectation and Laplace-transform representations for spider graphs. Therefore no novelty is claimed for spider exact-cover formulae here; their role is to calibrate the still-unresolved source scale and to produce a self-contained quotient derivation.

A search miss is not an openness or novelty certificate.

## 5. Metric and research status

Frozen metric before: `beta_cert=1/2`.

Frozen metric after: `beta_cert=1/2`.

**NO MOVEMENT.** The run instead obtains two rigorous structural calibrations:

- sharp-family lower calibration `lim SD/t_hit = pi/sqrt(6)` in the divergent `t_cov/t_hit` regime;
- a complete counterexample to the raw universal late-vertex variance ansatz via two-clique metastable clustering.

The source-level `O(t_hit)` upper bound and universal exponential-tail clause remain unresolved. Mathematical status therefore remains **PARTIAL**.

## 6. Next mathematical obligation

The right object should quotient the late set into hitting-scale clusters. A useful next attack is to connect this to Aldous's terminal-set formalism: determine whether the terminal set's independent cover time admits a universal `O(t_hit)` or `O(t_hit^2/t_cov)` control after an intrinsic hitting-metric clustering, rather than raw vertex counting.
