Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — GPT-6/maximum was requested, but no authenticated runtime metadata establishes that setting.**

# NM13-01 / LIVE20 T08 — growing automorphism-memory cutoff beyond LRE

**Status:** `PARTIAL / OPEN` for Salez Problem 2.3; `CANDIDATE_FULL` for the restricted transfer theorem and explicit degree-20 class below, pending later independent review. Publication novelty is `UNVERIFIED`.

Repository/branch: `yspennstate/math-open-problems` / `master`. Controlling policy: `operations/PROGRESS20_2026-09-20.md`. Prewrite master observed before this run's writes: `b9e0c9d5b870caaece23c2693a9bc25edd55e0f4`.

## 0. Short handoff and partner split

The preceding complete NM13-01 report was `2026-09-20T08-55-00Z__automorphism-memory-semidir-cutoff.md`. It proved the fixed-finite-hidden-state automorphism-memory transfer and explicitly left **growing/nonuniform memory** as a possible obstruction. It also corrected the earlier 08:02 semidirect strong-product toy as gauge-trivial.

The newest relevant P26 report read was `proofnet24/P26-progress-cutoff-transfer/runs/2026-09-20/2026-09-20_10-10-50__biregular-halved-green-transfer.md`. P26 is on the complementary NBRW Green/spherical/radial-clock route. This run stays on the transitivity/algebraic side: can a hidden automorphism memory whose cardinality diverges preserve a second likelihood phase through cutoff?

The answer is negative in a quantitative regime. The hidden state may grow polynomially and need not itself have a known cutoff theorem: a uniform hidden spectral gap plus enough vertical clock time kills the memory before the macroscopic cutoff front.

## 1. Source and current boundary

Salez, `arXiv:2508.21055v1`, uses the rate-one continuous-time convention

\[
P_t=e^{t(T-I)}=e^{-t}\sum_{k\ge0}\frac{t^kT^k}{k!},
\]

and Problem 2.3 asks exactly to prove cutoff for all bounded-degree vertex-transitive expander sequences.

The fresh primary boundary checked on 20 September 2026 remains Altschuler, `arXiv:2609.14945v1` (submitted 14 September 2026): cutoff for every fixed-degree **long-range expander** and the strict hierarchy

\[
\text{Ramanujan}\Longrightarrow\text{LRE}\Longrightarrow\text{spectral expansion},
\]

with neither converse. Thus LRE is not interchangeable with Salez's arbitrary spectral-expander hypothesis. Pedrotti--Salez, `arXiv:2607.05345`, gives another sufficient local-product/non-equilibrium-Poincare mechanism, not a derivation from transitivity plus a fixed ordinary spectral gap.

For the explicit family below I reuse Kaufman--Lubotzky, `arXiv:1108.2960`. Their Theorem 3 supplies, for `q=5` and all sufficiently large exponents `r`, 6-regular Ramanujan Cayley graphs on a group `G_r` of `PSL_2(5^r)`/`PGL_2(5^r)` type whose six generators form one orbit of a cyclic torus of order six. I retain the source's `PSL/PGL` alternative rather than force a branch that is unnecessary below.

Bounded searches for `semidirect product random walk cutoff expander`, `skew product Cayley cutoff`, and `growing fiber cutoff random walk` did not surface the exact theorem below. This is bounded negative evidence only; worldwide novelty remains `UNVERIFIED`. Root `POSTED.md` exclusions were respected, in particular the already-posted Salez Problem 2.4 Abelian-Cayley/product-condition result was not reopened.

## 2. Parent problem before / after

**Before:** Salez Problem 2.3 was `OPEN`. The newest NM13-01 semidirect theorem handled only a fixed finite hidden memory.

**After:** Salez Problem 2.3 remains `OPEN`, but the proved restricted scope strictly enlarges: a cutoff Cayley base may carry a hidden automorphism memory `K_n` with `|K_n| -> infinity`; if the hidden information budget is below the vertical spectral-dissipation budget at the base cutoff front, then the full bounded-degree semidirect Cayley graph has source-continuous-time cutoff with a quantitative window.

A concrete degree-20 family below has `|K_n|=n^{1/10+o(1)}`, gap at least `(3-sqrt(5))/10`, lies outside every fixed LRE constant, and cuts off at

\[
5\log_5 n=\frac{50}{11}\log_5N+O(1)
\]

with `O(sqrt(log N))` window.

## 3. General varying-memory transfer

Let

\[
G_n=\operatorname{Cay}(\Gamma_n,S_n),\qquad |S_n|=d,
\]

be connected `d`-regular Cayley graphs with `S_n=S_n^{-1}`. Let finite groups `K_n` act by automorphisms

\[
\rho_n:K_n\to\operatorname{Aut}(\Gamma_n),\qquad \rho_n(k)S_n=S_n.
\]

Let `F_n=Cay(K_n,T_n)` be connected `s`-regular Cayley graphs, with normalized SRW kernel `W_n` and gap `eta_n=1-lambda_2(W_n)>0`. Choose an involution `tau_n in K_n`, and on the semidirect product form

\[
H_n=\operatorname{Cay}(\Gamma_n\rtimes_{\rho_n}K_n,\Sigma_n),
\qquad
\Sigma_n=\{(u,\tau_n):u\in S_n\}\cup\{(e,t):t\in T_n\}.
\]

Put `D=d+s`, `a=d/D`, `b=s/D`, and `m_n=|K_n|`. The generating set is inverse-closed because `S_n,T_n` are symmetric, `tau_n^2=e`, and the action preserves `S_n`; connectedness follows from vertical generation of `(e,k)` and `(u,e)=(u,tau_n)(e,tau_n^{-1})`. Hence `H_n` is connected, `D`-regular and vertex-transitive.

### Theorem A — exact TV sandwich

For the source rate-one continuous-time walks,

\[
\boxed{
 d_{G_n}(at)\le d_{H_n}(t)
 \le d_{G_n}(at)+\frac12\sqrt{m_n-1}\,e^{-b\eta_nt}.
}
\tag{3.1}
\]

**Proof.** Split the rate-one Poisson clock into cross events of rate `a` and vertical events of rate `b`. At a cross event from `(g,k)`, the base increment is `rho_n(k)u` with `u` uniform on `S_n`. Since `rho_n(k)` permutes `S_n`, this increment is uniform even conditional on the complete hidden history. Thus the base coordinate is exactly rate-`a` continuous-time SRW on `G_n`; projection gives the lower bound.

For the upper bound, condition on the cross clock and all realized base increments. Those increments reveal no hidden-state information, because at every cross time `u -> rho_n(k)u` is a bijection of `S_n`. Under this conditioning, the hidden coordinate is an alternation of vertical pieces `exp(v b(W_n-I))` and deterministic right-permutations from the cross events. The permutations preserve uniform measure and are `L^2(u_{K_n})` isometries, while a vertical interval of length `v` contracts mean-zero `L^2` by `e^{-b eta_n v}`. The interval lengths sum to `t`; starting from a point mass gives

\[
\left\|\frac{\xi_t}{u_{K_n}}-1\right\|_2
\le \sqrt{m_n-1}\,e^{-b\eta_nt}.
\]

Cauchy--Schwarz yields the hidden TV error in (3.1). Replacing the conditioned hidden endpoint by uniform while keeping the base path fixed and then averaging gives `(delta_g e^{at(P_n-I)}) tensor u_{K_n}`. Triangle inequality proves (3.1). No cross/vertical commutation is used. `QED`

### Theorem B — gap transfer

If `gamma_n=1-lambda_2(P_n)` is the base normalized gap, then

\[
\boxed{\operatorname{gap}(H_n)\ge\min\{a\gamma_n,b\eta_n\}.}
\tag{3.2}
\]

**Proof.** For `f(g,k)`, write `bar f(g)=E_k f(g,k)`. Variance splits as `Var f=Var_g bar f+E_g Var_k f`. The vertical Dirichlet form is at least `eta_n E_g Var_k f`. Reparameterizing each cross generator by `v=rho_n(k)u` makes `v` uniform on `S_n`; Jensen over `k` then lower-bounds the cross form by the base Dirichlet form of `bar f`, hence by `gamma_n Var_g bar f`. Weighting by `a,b` gives (3.2). `QED`

## 4. Hidden information budget

Suppose `G_n` has cutoff at `T_n -> infinity` with window `w_n=o(T_n)`. Define

\[
I_n=\frac12\log m_n,
\qquad
D_n=\frac{b\eta_n}{a}T_n.
\]

At transferred time `T_n/a`, the hidden term in (3.1) is at most `(1/2)exp(I_n-D_n)`.

### Corollary C — subcritical growing memory is invisible

If for some fixed `delta>0`, eventually

\[
\boxed{I_n\le(1-\delta)D_n,}
\tag{4.1}
\]

and `eta_n T_n -> infinity`, then `H_n` has cutoff at

\[
\boxed{T_n^H=T_n/a}
\]

with window `O(w_n/a+1/(b eta_n))`. If `eta_n` is uniformly positive and the base has a limiting profile on a diverging window, that profile transfers after deterministic time rescaling.

Indeed, at `t=(T_n+z w_n)/a`, the exponent is at most `-delta D_n+o(D_n) -> -infinity`, uniformly for bounded `z`, while the lower term in (3.1) is exactly the base TV distance at `T_n+z w_n`.

For a fixed-degree Ramanujan/LRE base with

\[
T_n=\frac d{d-2}\log_{d-1}n,
\qquad w_n=O(\sqrt{\log n}),
\]

and `m_n=n^{alpha+o(1)}`, a uniform hidden gap `eta` gives the explicit sufficient condition

\[
\boxed{\alpha<\frac{2s\eta}{(d-2)\log(d-1)}.}
\tag{4.2}
\]

The hidden chain itself need not have a cutoff theorem; its spectral gap only has to dissipate the point-mass `L^2` information cost in time.

## 5. A growing skew hidden expander

Let

\[
K_j=C_6\times\Lambda_j,
\]

where `a` generates `C_6` and `L_j=Cay(Lambda_j,U_j)` is an `r`-regular Cayley spectral-expander family, `r>=3`, with normalized gap at least `gamma_L`. Use the symmetric skew vertical set

\[
T_j=\{(a,e),(a^{-1},e)\}
\cup\{(a,u),(a^{-1},u):u\in U_j\},
\tag{5.1}
\]

of degree `s=2(r+1)`. It is connected because `(e,u)=(a^{-1},e)(a,u)`. Every `Lambda_j` move in the displayed set simultaneously rotates the `C_6` coordinate.

### Proposition D — exact hidden spectral bound

Fourier-decompose along the six characters of `C_6`, with `chi(a)=e^{i theta}`. On the `theta` sector,

\[
W_\theta=\cos\theta\left(\frac1{r+1}I+\frac r{r+1}P_{L_j}\right).
\tag{5.2}
\]

For `theta=0`, the gap is at least `r gamma_L/(r+1)`. For a nontrivial `C_6` character, `cos theta` is in `{1/2,-1/2,-1}`. The bracket in (5.2) has spectrum in `[(1-r)/(r+1),1]`, so every nontrivial sector has top eigenvalue at most `(r-1)/(r+1)`. Therefore

\[
\boxed{
\eta_F\ge\min\left\{\frac r{r+1}\gamma_L,\frac2{r+1}\right\}.
}
\tag{5.3}
\]

Thus an arbitrary bounded-degree Cayley spectral expander may serve as a growing hidden memory; no cutoff assumption on that hidden family is required.

## 6. Explicit degree-20 polynomial-memory class outside LRE

For each sufficiently large exponent `r`, let `G_r` be the `q=5` Kaufman--Lubotzky output (with the source's appropriate `PSL_2(5^r)`/`PGL_2(5^r)` branch). Put

\[
\Gamma_j=G_{10j},\qquad \Lambda_j=G_j.
\]

Both have 6-element Ramanujan generating sets. Let the first `C_6` factor of `K_j=C_6 times Lambda_j` act on `Gamma_j` through the torus action permuting its six generators; let `Lambda_j` act trivially. Choose `tau=(a^3,e)` and use (5.1) with `r=6`, so the vertical degree is 14 and the output degree is

\[
D=6+14=20.
\]

The 6-regular Ramanujan bound gives `gamma_G,gamma_L >= 1-sqrt(5)/3`. Proposition D gives

\[
\eta_F\ge\frac{6-2\sqrt5}{7}.
\]

With `a=3/10` and `b=7/10`, Theorem B yields

\[
\boxed{\operatorname{gap}(H_j)\ge\frac{3-\sqrt5}{10}.}
\tag{6.1}
\]

For odd `Q`, the relevant `PSL_2(Q)` and `PGL_2(Q)` orders are `Q(Q^2-1)/2` and `Q(Q^2-1)`. Hence if `n_j=|Gamma_j|` and `m_j=|K_j|`,

\[
\log m_j=\frac1{10}\log n_j+O(1),
\qquad m_j=n_j^{1/10+o(1)}.
\tag{6.2}
\]

The 6-regular Ramanujan base has source-continuous-time cutoff at

\[
T_j^G=\frac32\log_5n_j
\]

with `O(sqrt(log n_j))` window. The transfer factor is `1/a=10/3`, so

\[
\boxed{T_j^H=5\log_5n_j}
\tag{6.3}
\]

with

\[
\boxed{O(\sqrt{\log n_j})=O(\sqrt{\log N_j})}
\tag{6.4}
\]

window. The hidden error at this front obeys

\[
\log\left(\sqrt{m_j}e^{-b\eta_FT_j^H}\right)
\le\left[\frac1{20}-\frac{3-\sqrt5}{\log5}\right]\log n_j+O(1)
=-0.4246576532\ldots\log n_j+O(1),
\]

so it is polynomially negligible throughout the square-root window. Since `N_j=n_jm_j=n_j^{11/10+o(1)}` and the exact group-order discrepancy is only `O(1)` on logarithmic scale,

\[
\boxed{T_j^H=\frac{50}{11}\log_5N_j+O(1).}
\tag{6.5}
\]

### Not long-range expanding

Each output step changes the base coordinate by at most one base edge, so

\[
|B_{H_j}(x,r)|\le m_j|B_{G_j}(\bar x,r)|\le C m_j5^r.
\tag{6.6}
\]

The output degree is 20, hence its LRE tree branching base is 19. Take

\[
r_j=\left\lfloor\frac12\log_{19}N_j\right\rfloor.
\]

Then

\[
\frac{|B_{H_j}(x,r_j)|}{19^{r_j}}
\le N_j^{-\beta+o(1)},
\qquad
\beta=\frac12\left(1-\frac{\log5}{\log19}\right)-\frac1{11}
=0.1357896242\ldots>0.
\tag{6.7}
\]

Positivity is certified exactly by

\[
\beta>0\iff 11\log5<9\log19\iff 5^{11}<19^9,
\]

and `48,828,125 < 322,687,697,779`. For any fixed LRE constant `c>0`, Altschuler's singleton expansion requirement at `r_j` would force `|B(x,r_j)| >= c 19^{r_j}` for all large `j` (the saturation term is not active because `19^{r_j}=O(sqrt(N_j))`). Equation (6.7) contradicts that. Hence this degree-20 cutoff family is a vertex-transitive spectral expander lying outside every fixed LRE constant.

## 7. Mechanism-level obstruction removed

The previous NM13-01 handoff left a concrete escape route for a hypothetical non-cutoff transitive expander: perhaps a **growing** hidden automorphism memory can preserve a second positive-mass likelihood phase through the macroscopic front. Theorems A--D remove the subcritical regime.

At transferred time `T_n/a`, the worst point-mass hidden `L^2` information costs

\[
I_n=\frac12\log|K_n|,
\]

whereas vertical spectral-gap dissipation supplies

\[
D_n=\frac{b\eta_n}{a}T_n.
\]

Whenever `I_n <= (1-delta)D_n`, the full law is `o(1)` in TV from `(base law at T_n) tensor uniform(K_n)`. Thus no hidden conditional phase of positive mass survives the cutoff front in this regime, even if the hidden expander itself has no known cutoff.

For the explicit degree-20 construction, `alpha=1/10` gives hidden-error decay `n^{-0.4246576532+o(1)}`. More generally with the same `d=r=6` parameters, the transfer tolerates

\[
\alpha<\frac{2(3-\sqrt5)}{\log5}=0.9493153\ldots,
\]

while the simple non-LRE ball proof works for

\[
\alpha<\frac{1-\log5/\log19}{1+\log5/\log19}=0.2931570\ldots.
\]

So a substantial polynomial-memory regime is simultaneously transitive, spectrally expanding, non-LRE, and cutoff.

The remaining obstruction is sharper: critical/supercritical hidden information `I_n approx D_n`, loss of a uniformly gapped hidden direction, or failure of an arbitrary vertex-transitive expander to expose any exact/approximate cutoff quotient. The next materially different attack is therefore critical-memory analysis plus approximate quotient extraction from stabilizer blocks, rather than another fixed-fiber example.

## 8. Executed sanity check and ledger delta

The executed checker `2026-09-20T09-13-06Z__growing-memory-checker.py` verifies all displayed degree-20 constants, including the exact non-LRE certificate `5^11<19^9`. On a 72-state noncommuting semidirect toy with base `V_4` and hidden `S_3 x C_3`, it checks exact one-step base lumping, the gap inequality and the continuous-time TV sandwich at seven times. The hidden cross/vertical commutator maximum is `0.25`; the archived output ends `ALL_CHECKS_PASS`. This finite computation is a sanity check, not the asymptotic proof.

Structured `ledger_delta` is saved alongside this report. Parent/source status is `PARTIAL / OPEN -> PARTIAL / OPEN`; the mathematical gain is the growing-memory theorem and explicit degree-20 non-LRE class, not a claim that Salez Problem 2.3 is solved.
