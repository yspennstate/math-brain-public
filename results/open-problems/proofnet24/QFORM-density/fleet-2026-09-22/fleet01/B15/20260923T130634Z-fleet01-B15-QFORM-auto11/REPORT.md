SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet01, slot B15, 2026-09-23T13:06:34.859269Z.
attacking: rough-law absolute-continuity/regularity at the original-coordinate pivot scale, and compiling the completed fleet02/B15 one-sheet/minority result into a quantitative heat-mode inequality.

# QFORM B15 — fractional trace regularity and minority-excess compiler

**Status:** `PROVED_SUPPORTING_LEMMAS / FULL_TARGET_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`  
**Central height target:** still OPEN.  
**Raw continuous-density conclusion:** still separate; not used to manufacture the height bound.

## 1. Scope and source control

The owner target is unchanged: for arbitrary independent real coordinates with probability densities `0<=f_i<=1`, and arbitrary real symmetric `A` with at least three eigenvalues of modulus at least one, prove

\[
\sup_t p_{X^TAX}(t)\le C
\]

in the essential sense for one universal finite `C`, or give a valid target counterexample.


Two completed sources are applied below rather than merely cited.

1. **Assigned partner fleet02/B15, newest completed run:** `yspennstate/math-open-problems@46c33d97490f78f8c3de0435f63d573958d81180`, `proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B15/20260923T130525Z-fleet02-B15-qform-auto11/REPORT.md`. It rechecks the rough original-coordinate ruled one-sheet submeasure bound and proves the weak-trace/normalized-trace separation inside the fixed target `A=I_3`. I use its zero-loss weak interval-trace closure in Section 5 and its ruled one-sheet payment in Section 6.
2. **Newest owner-required volume/tail result:** `yspennstate/math-open-problems@c2414ef633b9d4b7f04a83e1aeefbe713ed82bba`, `proofnet24/QFORM-density/interactive/20260923T002323Z-volume-stability/PEER_TAIL_EXTENSION.md`. Under its explicit original-coordinate projection/tail gate it gives
\[
\|p_Q\|_\infty\le {9\sqrt3e\over2}
 [s_1(M)^2s_2(M)^2T_2]^{-1/6}.
\tag{1.1}
\]
Section 5 supplies the rough-law closure interface for this exact inequality without using continuity.

## 2. Qualitative absolute continuity is much easier than the target

### Proposition 2.1
Let `A` be any nonzero real symmetric matrix and let the joint law of `X` be absolutely continuous on `R^n`. Then `Q=X^TAX` has an absolutely continuous law. Independence, the cap `f_i<=1`, and the three-large-eigenvalue hypothesis are not needed.

### Proof
For `q(x)=x^TAx`,

\[
\nabla q(x)=2Ax.
\]

The critical set is `ker A`, a proper linear subspace and hence Lebesgue-null. If `N subset R` is Lebesgue-null, the coarea formula gives

\[
\int_{q^{-1}(N)}|\nabla q(x)|\,dx
 =\int_N \mathcal H^{n-1}(q^{-1}(t))\,dt=0.
\]

Outside `ker A` the integrand is strictly positive, so `q^{-1}(N)\setminus ker A` is null; adding `ker A` preserves nullity. Any absolutely continuous input law therefore assigns zero probability to `q^{-1}(N)`. Hence `q_#\mu_X<<dt`. `square`

This is only qualitative. The owner target is the dimension- and law-uniform Radon--Nikodym height.

## 3. New original-coordinate fractional regularity theorem

The next result is quantitative, rough-law valid, and keeps all outside curvature and couplings. Constants are physical-entry dependent, so it is not the full target.

### Theorem 3.1 — nonzero diagonal pivot: weak `L^2` and fractional trace
Suppose `a=A_{ii}\ne0` for one original coordinate. Then for every measurable `E subset R` of finite length,

\[
\boxed{\Pr(Q\in E)\le2\sqrt{|E|/|a|}.}
\tag{3.1}
\]

Consequently the output density satisfies

\[
\boxed{|\{t:p_Q(t)>\lambda\}|\le {4\over |a|\lambda^2},}
\qquad
\boxed{\|p_Q\|_{L^{2,\infty}}\le {2\over\sqrt{|a|}}.}
\tag{3.2}
\]

For every `1<r<2`,

\[
\boxed{
\|p_Q\|_r^r
\le 2^{2r-2}|a|^{1-r}
\left({1\over1-r/2}+{1\over r-1}\right).
}
\tag{3.3}
\]

Most importantly for translation-uniform trace estimates, for every `0<beta<1/2`,

\[
\boxed{
\sup_t \mathbb E|Q-t|^{-\beta}
\le {8^\beta\over1-2\beta}|a|^{-\beta}.
}
\tag{3.4}
\]

### Proof
Condition on the other original coordinates `W=X_{-i}`. Since `X_i` remains independent of `W` with density cap one,

\[
Q=aX_i^2+2d(W)X_i+c(W)
 =a(X_i+d(W)/a)^2+C(W).
\tag{3.5}
\]

For `a>0`, the conditional output density is bounded by

\[
p_w(t)\le [a(t-C(w))]^{-1/2}\mathbf1_{t>C(w)},
\tag{3.6}
\]

because there are at most two inverse branches and each source density is at most one. For `a<0` reflect the output. For any set `E` of length `m`, rearrangement of the decreasing one-sided kernel yields

\[
\int_E(t-s)_+^{-1/2}dt\le\int_0^m u^{-1/2}du=2\sqrt m.
\tag{3.7}
\]

Average (3.6) in `W` to get (3.1). Taking `E={p_Q>lambda}` gives (3.2). The decreasing rearrangement obeys

\[
p_Q^*(s)\le\min\left({2\over\sqrt{|a|s}},{1\over s}\right),
\tag{3.8}
\]

whose `r`th power integrates to (3.3).

For (3.4), apply (3.1) to `(t-r,t+r)`:

\[
\Pr(|Q-t|<r)\le\min\{1,\sqrt{8r/|a|}\}.
\tag{3.9}
\]

The crossover is `r_0=|a|/8`; layer cake gives

\[
\begin{aligned}
\mathbb E|Q-t|^{-\beta}
&=\beta\int_0^\infty r^{-\beta-1}\Pr(|Q-t|<r)dr\\
&\le {8^\beta\over1-2\beta}|a|^{-\beta}.
\end{aligned}
\]

The endpoint `beta=1/2` is deliberately excluded: a single squared coordinate has the sharp square-root critical singularity. `square`

### Corollary 3.2 — fixed-scale smooth regularity
For every nonnegative kernel `k`, with decreasing rearrangement `k^*`,

\[
\sup_y\mathbb E k(Q-y)
\le {2\over\sqrt{|a|}}\int_0^\infty s^{-1/2}k^*(s)ds.
\tag{3.10}
\]

In particular, for the Gaussian kernel `gamma_epsilon`,

\[
\boxed{
\|\mu_Q*\gamma_\varepsilon\|_\infty
\le {2^{1/4}\Gamma(1/4)\over\sqrt\pi}
 {1\over\sqrt{|a|\varepsilon}}
< {2.433\over\sqrt{|a|\varepsilon}}.
}
\tag{3.11}
\]

For the Laplace kernel `ell_epsilon(u)=(2epsilon)^{-1}e^{-|u|/epsilon}`,

\[
\boxed{
\|\mu_Q*\ell_\varepsilon\|_\infty
\le {\sqrt{2\pi}\over\sqrt{|a|\varepsilon}}.
}
\tag{3.12}
\]

These are regularity estimates, not the target height theorem: they diverge as `epsilon downarrow0`.

### Theorem 3.3 — exact zero diagonal with an off-diagonal anchor
Suppose `A_ii=0` but `b=A_ij\ne0` for some original `j`. Then, with

\[
\Psi_b(m)=
\begin{cases}
{m\over|b|}\left(1+\log{|b|\over m}\right),&0<m<|b|,\\
1,&m\ge|b|,
\end{cases}
\]

one has for every measurable `E`,

\[
\boxed{\Pr(Q\in E)\le\Psi_b(|E|).}
\tag{3.13}
\]

Hence the output is absolutely continuous and, for every `0<beta<1`,

\[
\boxed{
\sup_t\mathbb E|Q-t|^{-\beta}
\le { (2/|b|)^\beta\over(1-\beta)^2}.
}
\tag{3.14}
\]

### Proof
Condition on all original coordinates except `X_i,X_j`, then also on `X_j=x`. As a function of `X_i`, `Q` is affine with slope

\[
2(bx+d(W)).
\]

Therefore the conditional `E`-probability is at most

\[
\min\left(1,{|E|\over2|b|\,|x-x_0(W)|}\right).
\tag{3.15}
\]

The density of `X_j` is at most one and has total mass one. The bathtub/rearrangement maximum of the radially decreasing right side is attained by filling a centered set of length one. If `m=|E|<|b|`, direct integration over `[-1/2,1/2]` gives

\[
{m\over|b|}\left(1+\log{|b|\over m}\right),
\]

and for `m>=|b|` the probability bound one suffices. This proves (3.13). Applying it to an interval of length `2r` and integrating the layer-cake identity gives exactly (3.14); the elementary integral simplifies to `(2/|b|)^beta/(1-beta)^2`. `square`

Thus every nonzero symmetric `A` under the product cap-one law has a completely explicit original-coordinate modulus of absolute continuity: a weak-`L^2` square-root modulus if some diagonal pivot is nonzero, and a logarithmic modulus if all diagonals vanish and some off-diagonal coefficient is nonzero. The constants need not be dimension-free under only the spectral hypothesis; the near-zero physical-pivot aggregation remains a genuine global obstruction.

## 4. Bounded density and continuity are logically different

For a finite Borel measure `mu` on the line, define

\[
D_\infty(\mu)=\inf\{C:\mu(E)\le C|E|\text{ for every Borel }E\}.
\]

Then `D_infinity(mu)<infinity` iff `mu=p dx` with `p in L^infinity`, and the value is exactly `||p||_infinity`. It is enough to test intervals. This is the central owner target.

Continuity requires strictly more. If `p in L^1 cap L^infinity`, then

\[
\boxed{
p\text{ has a }C_0(\mathbb R)\text{ representative}
\iff
\|\tau_h p-p\|_\infty\to0\quad(h\to0).
}
\tag{4.1}
\]

The forward implication is uniform continuity of a `C_0` function. Conversely, for a smooth compactly supported approximate identity `eta_delta`,

\[
\|p*\eta_\delta-p\|_\infty
\le\int\eta_\delta(h)\|\tau_hp-p\|_\infty dh\to0.
\tag{4.2}
\]

Each `p*eta_delta` lies in `C_0`; a uniform limit gives the desired representative.

So the universal `L^infinity` theorem asks only for interval domination. A continuity proof must additionally produce an `L^infinity` translation modulus (or an equivalent uniform desmoothing statement). The two conclusions must not be conflated.

## 5. Rough-law closure applied to the newest volume estimate

The newest fleet02/B15 theorem makes an important distinction: weak convergence gives uniform convergence of **unnormalized** interval masses for an atomless limit, and a pre-existing common interval estimate passes to the limit with zero loss; normalized shrinking-interval profiles need not converge even for `A=I_3`, smooth compact cap-one sources, continuous outputs and a common height bound.

That result supplies exactly the valid limiting interface needed here.

### Lemma 5.1 — zero-loss rough-source height closure
Fix a quadratic polynomial `q`. Suppose product laws `mu_m` converge weakly to a product law `mu`, and for every `m`

\[
(q_#\mu_m)(I)\le H|I|\qquad\text{for every interval }I,
\tag{5.1}
\]

with the same finite `H`. If the limit output is atomless (in particular, if `q` is nonconstant and `mu` is absolutely continuous), then

\[
\boxed{(q_#\mu)(I)\le H|I|\quad\forall I,}
\tag{5.2}
\]

hence `||p_{q(X)}||_infinity<=H`.

This is the assigned partner's completed weak-trace theorem applied to the actual height inequality (5.1); no convergence of densities is asserted or needed.

### Application to the owner-required collective-tail branch
Take the explicit original-coordinate cross-block gate in `PEER_TAIL_EXTENSION.md`: with row-space projection `P`, `max_i P_ii<=1/2` and

\[
\|(I-P)M\|_{op}\le\sqrt{T_2}/15,
\qquad T_2=\sum_{j\ge3}s_j(M)^2,
\]

the smooth-source Fourier estimate is

\[
H_{vol}={9\sqrt3e\over2}[s_1(M)^2s_2(M)^2T_2]^{-1/6}.
\tag{5.3}
\]

Mollify each original marginal: `f_i^(delta)=f_i*gamma_delta`. Then `0<=f_i^(delta)<=1`, each is a probability density, and `f_i^(delta)->f_i` in `L^1`, hence weakly. The matrix gate and `H_vol` are source-independent. Applying (5.1)-(5.2) gives, with **no continuity premise**,

\[
\boxed{
\|p_Q\|_\infty
\le {9\sqrt3e\over2}[s_1(M)^2s_2(M)^2T_2]^{-1/6}
}
\tag{5.4}
\]

for the rough cap-one product law whenever the stated matrix gate holds. If the original Fourier proof also establishes continuity directly, that is an additional conclusion; it is not needed for (5.4).

This application also explains why the partner's normalized-trace counterexample matters: the correct order is **prove a uniform interval inequality first, then pass it weakly**. One cannot infer (5.1) by taking a smooth limit of normalized local profiles.

## 6. Assigned-partner one-sheet result: excess height is necessarily minority weak-`L^2`

Now apply the other completed fleet02/B15 result at an actual inequality. Let `S` be an invertible indefinite original-coordinate physical three-block of signature `(2,1)` or `(1,2)`. The partner's rough ruled theorem gives a majority/one-sheet output submeasure

\[
\mu_G\le C_B\,dt,
\qquad
C_B\le {\pi\sqrt2\over\kappa},
\tag{6.1}
\]

where `kappa=sigma_min(A_SS)`. Arbitrary outside quadratic terms and couplings are retained because the conditioning is on original coordinates.

Write `mu_Q=mu_G+mu_-`. If, in addition, an original diagonal pivot `a=A_ii\ne0` is available anywhere in the full form, Theorem 3.1 applies to the full output and hence to the positive minority submeasure `mu_-<=mu_Q`. Since `p_G<=C_B`,

\[
(p_Q-C_B)_+\le p_-.
\]

Therefore

\[
\boxed{
|\{t:p_Q(t)>C_B+\lambda\}|
\le {4\over |a|\lambda^2}.
}
\tag{6.2}
\]

This is a precise regularity statement for the unpaid side: after the completed one-sheet payment, **all density above `C_B` is confined to a weak-`L^2` minority/two-sheet spike**. No X-ray-only estimate is being substituted for the missing minority payment.

At Gaussian scale `epsilon`, (3.11) similarly gives

\[
\boxed{
[(\mu_Q*\gamma_\varepsilon)(y)-C_B]_+
\le {2^{1/4}\Gamma(1/4)\over\sqrt\pi}
 {1\over\sqrt{|a|\varepsilon}}.
}
\tag{6.3}
\]

This is not yet uniform as `epsilon downarrow0`.

### Compatibility with the partner's two-sided minority packing
Use the completed two-sided packing inequality from the preceding fleet02/B15 run (and retained in the newest partner state). Let

\[
c_0=\sqrt{2e/\pi},\qquad
M=\max_y\mathbb E\gamma_\varepsilon(Q-y).
\]

If `M>c_0 C_B`, put

\[
u=\varepsilon(M/c_0-C_B)\in(0,1],
\qquad R=\log(2/u).
\tag{6.4}
\]

The partner theorem produces two disjoint minority intervals, each of length `R epsilon`, each carrying minority mass at least `u/2`. Their union `E` therefore satisfies

\[
\mu_-(E)\ge u,
\qquad |E|=2R\varepsilon.
\tag{6.5}
\]

Apply the new rough-law concentration (3.1) to this **actual partner-produced set**:

\[
\boxed{
u^2\le {8\varepsilon\over|a|}\log(2/u).}
\tag{6.6}
\]

Equivalently, with `W` the principal Lambert function,

\[
\boxed{
u^2\le {4\varepsilon\over|a|}
 W(|a|/\varepsilon).}
\tag{6.7}
\]

Since `M=c_0(C_B+u/epsilon)`, this yields

\[
\boxed{
M\le c_0 C_B
 +{2c_0\over\sqrt{|a|\varepsilon}}
 \sqrt{W(|a|/\varepsilon)}.
}
\tag{6.8}
\]

The numerical bound (6.8) is not advertised as the final height estimate; it still diverges at small scale. Its structural content is sharper: if `u>=delta>0`, then (6.6) forces

\[
\boxed{
{|a|\over\varepsilon}
\le {8\log(2/\delta)\over\delta^2}.
}
\tag{6.9}
\]

Thus a fixed normalized heat-mode excess above the already-paid majority side can occur only when every diagonal pivot used in this certificate is on the heat scale. In other words, the surviving branch is genuinely a **near-zero physical-pivot/minority-two-sheet branch**, not an arbitrary regularity defect.

At an exact zero diagonal, Theorem 3.3 gives the parallel compatibility condition

\[
\boxed{
u\le\Psi_b(2R\varepsilon)}
\tag{6.10}
\]

for any off-diagonal anchor `b=A_ij\ne0`. This is an exact-zero endpoint statement only; it does not treat a small nonzero quadratic pivot as a uniformly small perturbation.

## 7. What this changes and what remains unpaid

The regularity ledger is now precise.

- **Absolute continuity:** qualitative for every nonzero symmetric `A` under any absolutely continuous joint input; quantitatively, product cap-one laws satisfy (3.1) or (3.13) in original coordinates.
- **Fractional trace:** a nonzero physical diagonal gives translation-uniform exponent `beta<1/2`; an exact zero diagonal with an off-diagonal anchor gives every `beta<1`. These are rough-law statements with arbitrary outside couplings.
- **Bounded density:** still the substantive universal theorem. Weak convergence can preserve a uniform bound already proved, but cannot create it from continuity or normalized-profile convergence.
- **Continuous density:** equivalent, once a bounded density exists, to `L^infinity` translation continuity (4.1). This is a separate stronger obligation.
- **Assigned partner applied:** the newest weak-trace theorem transfers the current volume inequality to rough laws at zero loss, and the ruled one-sheet theorem plus minority packing combines with (3.1) in (6.2)-(6.9).

The first genuinely unpaid implication exposed by this run is now narrower. After the completed volume exits and one-sheet payment, a putative blow-up must lie in a product-sensitive minority/two-sheet regime in which useful physical diagonal pivots are simultaneously at the smoothing scale (or zero), while no existing collective-tail/ridge/grouped-coordinate certificate has fired. Closing that near-pivot structural branch must occur **before** paying reciprocal tiny minors; the live projection/X-ray correction forbids replacing it by a generic projected-density argument.

**Full QFORM status: OPEN / NOT PROVED / NOT DISPROVED.**
