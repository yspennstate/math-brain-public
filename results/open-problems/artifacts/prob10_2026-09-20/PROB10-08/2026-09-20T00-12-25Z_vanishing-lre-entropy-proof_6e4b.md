# PROB10-08 artifact — vanishing-LRE endpoint entropy and continuous-time cutoff

Model actually run: **GPT-5.6 Sol**. Reasoning level: **UNVERIFIED**. GPT-6 maximum was requested in the owner prompt, but this runtime exposes no authenticated model/effort selector or attestation establishing GPT-6 maximum.

This is an analytic proof artifact, not an independent audit and not a novelty certificate.

Source target: Justin Salez, arXiv:2508.21055, Problem 2.3. Walk convention here is **rate-one continuous-time simple random walk** with semigroup `H_t = exp(t(P-I))` on a finite `d`-regular graph.

Primary proof lead read this run: Dylan J. Altschuler, arXiv:2609.14945v1, especially Lemmas 3.2–3.4 and the covering-tree proof of Theorem 1.12. The arXiv history checked this run still contains only v1, submitted 14 September 2026; a bounded correction/erratum search found no later correction. This artifact does not attribute the theorem below to Altschuler: it quantifies what happens when his fixed LRE constant is allowed to decay with `n` and adapts the final step to Salez's continuous-time convention.

## 1. Frozen notation

Fix `d>=3` and put

\[
q=d-1,\qquad L_n=\log_q n,\qquad v=\frac{d-2}{d}.
\]

Let `G_n` be connected `d`-regular graphs on `n` vertices, `P_n=A_n/d`, and assume the one-sided spectral gap

\[
1-\lambda_2(P_n)\ge \gamma>0
\tag{A1}
\]

uniformly in `n`.

For `c_n in (0,1/(16q)]`, assume the **vanishing long-range growth inequality**

\[
|B(S,r)|\ge \min\left\{\frac{3n}{4},\ c_n |S|q^r\right\}
\quad\text{for every nonempty }S\subseteq V(G_n),\ r\in\mathbb Z_{\ge0}.
\tag{A2}
\]

No transitivity is needed for the theorem below. When the graphs are vertex-transitive, they lie in Salez Problem 2.3's source class because (A1) is the expander hypothesis.

## 2. Quantitative transfer to the oriented-edge NBRW

Let

\[
\Omega=\{(u,v):u\sim v\},\qquad N=dn,
\]

and let `Q` be the oriented-edge nonbacktracking transition matrix

\[
Q((u,v),(v,w))=q^{-1}{\bf1}_{\{w\ne u\}}.
\]

For each `n`, set

\[
k_n:=\min\left\{k\ge1:q^{-k}\le \frac{c_n(q-1)}2\right\}.
\]

Repeating Altschuler's Lemma 3.2 with `c=c_n` gives the explicit directed growth constant

\[
a_n:=\frac{c_n}{2d q^{2k_n}}
\tag{2.1}
\]

such that

\[
|B_\Omega(F,r)|\ge a_n\min\{N,|F|q^r\}
\quad(F\ne\varnothing,r\ge0).
\tag{2.2}
\]

Here is the full dependence check. Let `C` be the terminal vertices of `B_\Omega(F,2k_n)` and `U` the vertices of `C` not reached at positive time up to `2k_n`. The same no-backtracking concatenation argument gives

\[
|U|\le q^{-k_n}|C|\le \frac{c_n(q-1)}2|C|.
\]

If `|C|q^ell<=n`, the graph growth (A2) and the geometric-series bound on exceptional endpoints give

\[
|B_\Omega(F,2k_n+\ell)|\ge \frac{c_n}{2}|C|q^\ell
\ge \frac{c_n}{2d}|F|q^\ell.
\]

At `ell=floor(log_q(n/|C|))` this is at least `c_n n/(2q)`, and larger radii follow by monotonicity. For radii below `2k_n`, use `|B_\Omega(F,r)|>=|F|`. These bounds imply (2.2) with (2.1).

Because `c_n<=1/(16q)`, the minimal `k_n` is in the regime where

\[
q^{-k_n}>\frac{c_n(q-1)}{2q}.
\]

Consequently

\[
a_n\ge A_d c_n^3,\qquad A_d:=\frac{(q-1)^2}{8dq^2}.
\tag{2.3}
\]

(The inequality is actually strict with this constant; the weak form is what is used.)

## 3. Endpoint entropy with a decaying expansion constant

Define

\[
\delta_n:=\frac{a_n(q-1)}{2q}.
\]

Choose

\[
C_{0,n}\ge \max\left\{1,\left\lceil\log_q\frac{2}{a_n(q-1)}\right\rceil,\ C_d^{(0)}\right\},
\]

where the fixed `C_d^(0)` is large enough that

\[
\lfloor\log_q(dn)\rfloor-C_{0,n}\le j_n-1,
\]

with `j_n` the least integer satisfying `d q^{j_n-1}>=n`.

Altschuler's forest induction in Lemma 3.3 is pointwise in `(a,q)` and therefore remains valid when `a=a_n` depends on `n`: for a walk on `Omega` started from one state and

\[
h_n:=\lfloor\log_q(dn)\rfloor-C_{0,n},
\]

we have

\[
H(Q^{h_n}(e,\cdot))\ge h_n\log q-\delta_n^{-1}\log(qh_n+1).
\]

Since `Q` is doubly stochastic, entropy is nondecreasing after `h_n`. Passing from the final oriented edge `(U,Y)` to its terminal vertex `Y` costs at most `log d`. Thus for the vertex-started NBRW endpoint law `K_j(x,.)`, uniformly in `x` and all `j>=j_n`,

\[
H(K_j(x,\cdot))\ge \log n-D_n,
\tag{3.1}
\]

where one may take

\[
D_n=(C_{0,n}+1)\log q+\delta_n^{-1}\log\big(q\lceil\log_q(dn)\rceil+1\big)+O_d(1).
\tag{3.2}
\]

By (2.3),

\[
D_n\le C_d\left(1+\log\frac1{c_n}+c_n^{-3}\log\log n\right)
\tag{3.3}
\]

for a constant depending only on `d`.

The exact place where fixed long-range expansion was used in arXiv:2609.14945 is therefore isolated: it ensures `a_n` and `delta_n` are constants. For cutoff, constancy is stronger than necessary; it is enough that `D_n=o(log n)`.

## 4. Continuous-time entropy-to-mixing lemma

Let `H_t=exp(t(P-I))` and let `mu_t=mu H_t`. Write `pi` for uniform measure and `f_t=mu_t/pi`. The relative entropy is

\[
\operatorname{Ent}_\pi(f_t)=\log n-H(\mu_t).
\]

For the symmetric kernel `P`, differentiation gives

\[
-\frac d{dt}\operatorname{Ent}_\pi(f_t)
=\mathcal E_P(f_t,\log f_t).
\]

Using

\[
(a-b)(\log a-\log b)\ge4(\sqrt a-\sqrt b)^2
\]

and the Poincare inequality from (A1),

\[
\mathcal E_P(f_t,\log f_t)
\ge4\mathcal E_P(\sqrt{f_t},\sqrt{f_t})
\ge4\gamma\operatorname{Var}_\pi(\sqrt{f_t}).
\]

Also

\[
\|\mu_t-\pi\|_{TV}^2\le \operatorname{Var}_\pi(\sqrt{f_t}),
\]

by Cauchy-Schwarz applied to `(sqrt(f)-1)(sqrt(f)+1)`. Since total variation decreases with time, integrating over `[0,s]` yields

\[
\boxed{
\|\mu H_s-\pi\|_{TV}
\le \sqrt{\frac{\log n-H(\mu)}{4\gamma s}}.
}
\tag{4.1}
\]

Thus every law satisfying (3.1) is within `epsilon/2` of stationarity after

\[
s_{n,\epsilon}:=\frac{D_n+1}{\gamma\epsilon^2}.
\tag{4.2}
\]

No lower spectral-edge assumption is needed in continuous time; an eigenvalue near `-1` decays rapidly under `exp(t(P-I))` rather than causing discrete-time periodicity.

## 5. Covering tree and cutoff

For rate-one continuous-time SRW on the infinite rooted `d`-regular tree, let `R_t` be distance from the root. Conditional on `R_t=j`, the projected endpoint law on `G_n` is `K_j(x,.)`. Hence

\[
H_t(x,\cdot)=\sum_{j\ge0}\Pr(R_t=j)K_j(x,\cdot).
\tag{5.1}
\]

Away from zero the jump increment is `+1` with probability `q/d` and `-1` with probability `1/d`, so its drift is `v=(d-2)/d`. The number of visits to zero is a.s. finite. Poissonization of the iid increment walk therefore gives

\[
\frac{R_t-vt}{\sqrt t}\Longrightarrow N(0,1).
\tag{5.2}
\]

(The compound-Poisson variance rate is `E[Z^2]=1`; the finite root correction is `O_P(1)`.)

Let

\[
T_n:=\frac{L_n}{v}=\frac d{d-2}\log_q n.
\]

For the upper bound, run for `t-s_{n,epsilon}` first and then for `s_{n,epsilon}`. From (5.1), (3.1), (4.1), and convexity of TV,

\[
\|H_t(x,\cdot)-\pi\|_{TV}
\le \Pr(R_{t-s_{n,\epsilon}}<j_n)+\epsilon/2.
\tag{5.3}
\]

By (5.2), for a constant `C_epsilon`, the probability in (5.3) is at most `epsilon/2` when

\[
t\ge T_n+C_\epsilon\sqrt{L_n}+s_{n,\epsilon}.
\]

For the lower bound, take `r_n=L_n-a\sqrt{L_n}`. The degree bound gives

\[
\pi(B(x,r_n))=O(q^{-a\sqrt{L_n}})=o(1).
\]

If `R_t<=r_n`, the projected walk lies in this ball. The radial CLT therefore gives, after choosing `C_epsilon`,

\[
\|H_t(x,\cdot)-\pi\|_{TV}\ge1-\epsilon-o(1)
\]

for

\[
t\le T_n-C_\epsilon\sqrt{L_n}.
\]

Combining the bounds proves:

### Theorem V-LRE

If (A1)–(A2) hold and

\[
D_n=O_d\left(1+\log(1/c_n)+c_n^{-3}\log\log n\right)=o(\log n),
\tag{5.4}
\]

then rate-one continuous-time SRW on `G_n` has total-variation cutoff at `T_n=d/(d-2) log_q n`. More quantitatively, for every fixed `epsilon in (0,1/2)`,

\[
|t_{mix}^{(n)}(\epsilon)-T_n|
\le C_{d,\gamma,\epsilon}\left(\sqrt{L_n}+D_n+1\right),
\tag{5.5}
\]

and therefore

\[
\frac{t_{mix}(\epsilon)-t_{mix}(1-\epsilon)}{t_{mix}(1/2)}
=O_{d,\gamma,\epsilon}\left(
L_n^{-1/2}+\frac{D_n}{L_n}
\right)=o(1).
\tag{5.6}
\]

A convenient sufficient condition is

\[
c_n^{-3}\log\log n=o(\log n).
\tag{5.7}
\]

This is a proved extension of the **fixed-constant hypothesis in the proof mechanism**. It is not a proof of Salez Problem 2.3, because arbitrary transitive spectral expanders need not satisfy (A2) with `c_n` in the range (5.7).

## 6. Auxiliary spectral corollary: tiny excess above the Ramanujan interval

This corollary is recorded as an auxiliary calculation because Salez's survey already lists `(near-)Ramanujan` positive results, so no novelty is claimed from the phrase “near-Ramanujan.”

Suppose every adjacency eigenvalue other than `d` and the possible bipartite eigenvalue `-d` satisfies

\[
|\lambda|\le2\sqrt q\cosh\theta_n.
\tag{6.1}
\]

Altschuler uses the Chebyshev polynomial

\[
F_r(x)=2q^{r/2}T_r(x/(2\sqrt q)),\qquad F_r(d)=q^r+1.
\]

Under (6.1),

\[
\max |F_r(\lambda)|\le2q^{r/2}e^{r\theta_n}.
\]

The same support plus Cauchy-Schwarz argument gives, in the nonbipartite case,

\[
|B(S,r)|\ge\min\left\{\frac{3n}{4},\frac1{16}e^{-2r\theta_n}|S|q^r\right\}.
\tag{6.2}
\]

In the bipartite case, using `(x+d)F_{r-1}(x)/(2d)` gives the uniform weaker form

\[
|B(S,r)|\ge\min\left\{\frac{3n}{4},\frac1{16q}e^{-2r\theta_n}|S|q^r\right\}.
\tag{6.3}
\]

For `r<=2L_n`, (6.3) implies (A2) with

\[
c_n=\frac1{16q}e^{-4\theta_nL_n}.
\tag{6.4}
\]

At `r=2L_n`, the second term in (6.3) already exceeds `3n/4` for large `n` whenever `theta_n L_n=O(log L_n)`; larger radii follow by monotonicity. Therefore (6.4) is valid for all radii.

If for some fixed `beta<1/12`,

\[
\theta_nL_n\le\beta\log L_n,
\tag{6.5}
\]

then

\[
D_n=O_d(L_n^{12\beta}\log L_n)
\]

and Theorem V-LRE gives

\[
\frac{w_n(\epsilon)}{t_{mix}(1/2)}
=O_{d,\epsilon}\left(L_n^{-1/2}+L_n^{12\beta-1}\log L_n\right)=o(1).
\tag{6.6}
\]

The spectral hypothesis (6.5) permits a vanishing excess over the Ramanujan edge of relative order `O((log L_n/L_n)^2)`. This calculation is **not counted as a prior-art-cleared new class** in the run ledger because existing literature already contains several “near-Ramanujan” cutoff results, and the bounded search in this run did not establish disjointness from all of them.

## 7. What this does and does not establish

- **Proved here:** Altschuler's endpoint-entropy mechanism tolerates a vanishing LRE constant as long as its induced entropy deficit is `o(log n)`, with the explicit cubic transfer loss `c_n -> a_n >= A_d c_n^3`, and the result works directly in Salez's continuous-time convention under a one-sided gap.
- **Complete class theorem:** vertex-transitive expander sequences satisfying (A2) and (5.7) exhibit cutoff with the window ratio (5.6). This is PARTIAL relative to the source.
- **Not proved:** every vertex-transitive spectral expander satisfies any WLRE estimate strong enough for (5.7). Altschuler's two-copy/matching construction shows fixed LRE cannot follow from spectral expansion alone.
- **Not claimed novel worldwide:** the bounded search did not locate this exact vanishing-LRE quantitative extension, but negative search is not a novelty certificate.
- **No finite checker:** the new core is analytic. No finite-enumeration claim was introduced, so manufacturing a checker would violate the 90/10 research contract.

## 8. Links to recovered history

- `operations/claims/I0112.md`
- `runs/R16/2026-09-16T18-48-00Z_i0112-product-varentropy.md`
- `runs/R16/2026-09-16T19-48-00Z_i0112-synchronous-tensor-cutoff.md`
- `runs/R16/2026-09-16T20-45-00Z_i0112-window-floor-gauge-obstruction.md`
- `runs/R16/2026-09-16T21-42-29Z_i0112-hecke-information-curvature-obstruction.md`
- `runs/R16/2026-09-16T22-43-00Z_i0112-stuck-recovery-1.md`
- `runs/R16/2026-09-16T23-44-54Z_i0112-stuck-recovery-2-tree-subcommutation-obstruction.md`
- `artifacts/prob10_2026-09-20/PROB10-08/2026-09-19T23-45-09Z_r16-h0002-handoff.md`
