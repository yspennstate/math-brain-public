Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — this was not GPT-6 at maximum, and I do not claim otherwise.** No authenticated runtime model/effort telemetry or binding selector was exposed.

# P0458 — ANOVA/group-action control of the dependence term and an alternate interior proof

Date: 2026-09-19 UTC  
Worker: `R7-03`  
Native ID: `6aabe7be74008191b526b109ee4e9e80`  
Canonical target: `P0458`  
Captured master for this research iteration: `67203151aae33f917c6b674b4f9e82bb68d783a8`  
Fresh master immediately before this artifact write: `e071c0a30ebe8f3a843555ec788a63df8be6208c`

Outside source: Hossein Dabirian and Vijay Subramanian, *Connectivity of a family of bilateral preference random graphs*, Journal of Applied Probability 63(2), 552–579 (2026), §1.1 open problems, DOI `10.1017/jpr.2025.10051`. The source asks for the limiting law of the standardized vertex degree in `LK(n,k)` and notes the dependence obstruction to computing the variance.

This artifact follows the recovery action selected in `research7_2026-09-17/R7-03/runs/2026-09-19/2026-09-19T113000Z__report.md`: build a structurally different proof of the interior dependence step, beginning with the balanced case, without importing the previous pointwise covariance estimate as a black box.

Methods used:

- **B1 — CHANGE THE CATEGORY:** replace a graph-by-graph dependence calculation by the ANOVA/Hoeffding decomposition of a symmetric statistic of the independent non-root edge array;
- **B11 — DUALIZE:** identify pair covariance with the squared `L^2` norm of the first projection onto the unique shared-edge sigma-field;
- **B14 — FIND THE GROUP ACTING:** use the `S_k` action on the root-selected neighbors to reduce the full conditional covariance matrix to its trivial and standard representation eigenspaces.

The main payoff is stronger than the balanced-case target: the total pair-covariance contribution has a **uniform finite-`n` expectation bound below `1/2` for every `2<=k<=n-2`**. This removes the previous good-event/bad-event lower-tail split from the interior proof.

---

## 1. Model and conditional representation

Give every edge of `K_n` an independent `Uniform(0,1)` score. Each vertex proposes its `k` smallest incident scores, and an edge is retained exactly when both endpoints propose it. Fix root `0`, write `D=D_{n,k}`, and define the degree deficit

\[
H:=k-D.
\]

Let `S` be the root's `k` proposed neighbors and let `X` be the `(k+1)`st smallest of the `n-1` root-edge scores. Conditional on `(X,S)`, the selected root scores `(U_i)_{i\in S}` are iid `Uniform(0,X)`, and all non-root edge scores remain independent uniforms.

For `i\in S`, let

\[
R_i:=\mathbf 1\{\text{endpoint }i\text{ rejects }(0,i)\}.
\]

Then

\[
H=\sum_{i\in S}R_i.
\]

Let `T` denote the `k`th smallest of `n-2` iid uniforms. Thus

\[
T\sim\operatorname{Beta}(k,n-k-1),
\]

with cdf `F_n`, and define

\[
q_n(x):=\frac1x\mathbb E[(x-T)_+].
\]

By symmetry,

\[
\mathbb E(R_i\mid X=x)=q_n(x),
\qquad
\mathbb E(H\mid X=x)=kq_n(x).
\tag{1.1}
\]

The earlier P0458 proof used a pointwise oscillation estimate for pair covariance followed by a lower-tail split for `X`. We now rederive the pair term as an exact ANOVA projection and integrate it exactly.

---

## 2. B11: exact shared-edge ANOVA identity

Fix distinct `i,j\in S` and let

\[
W:=U_{ij}
\]

be their unique shared non-root edge score. Conditional on `(X=x,W=w)`, the variables `R_i` and `R_j` depend on disjoint remaining edge sets and independent root scores. Hence they are conditionally independent, and the law of total covariance gives

\[
\operatorname{Cov}(R_i,R_j\mid X=x)
=
\operatorname{Var}(a_{n,x}(W)),
\tag{2.1}
\]

where

\[
a_{n,x}(w):=\mathbb P(R_i=1\mid X=x,W=w).
\]

This is precisely the first Hoeffding/ANOVA projection onto the shared-edge sigma-field: `a_{n,x}(W)-q_n(x)` is the projection of `R_i-q_n(x)` onto `sigma(W)`.

To compute it, condition further on `U_i=u`. Deleting the shared edge leaves `n-3` competitors, so if

\[
B_u\sim\operatorname{Bin}(n-3,u),
\]

then

\[
R_i=1\iff B_u+\mathbf 1_{\{w<u\}}\ge k.
\]

Therefore

\[
a_{n,x}(w)
=
\frac1x\int_0^x\mathbb P(B_u\ge k)\,du
+
\frac1x\int_0^x\mathbf 1_{\{w<u\}}\mathbb P(B_u=k-1)\,du.
\tag{2.2}
\]

Set

\[
c_{n,x}:=\frac1x\int_0^x\mathbb P(B_u\ge k)\,du.
\]

The beta-density identity

\[
(n-2)\,\mathbb P(B_u=k-1)
=
f_T(u)
\tag{2.3}
\]

holds exactly because

\[
f_T(u)
=\frac{u^{k-1}(1-u)^{n-k-2}}{B(k,n-k-1)}
=(n-2)\binom{n-3}{k-1}u^{k-1}(1-u)^{n-k-2}.
\]

Thus, with `F_n` the cdf of `T`,

\[
\boxed{
 a_{n,x}(w)
 =c_{n,x}+
 \frac{[F_n(x)-F_n(w)]_+}{x(n-2)}.
}
\tag{2.4}
\]

Combining (2.1) and (2.4), if `W\sim Uniform(0,1)`,

\[
\boxed{
 b_n(x):=\operatorname{Cov}(R_i,R_j\mid X=x)
 =
 \frac{1}{x^2(n-2)^2}
 \operatorname{Var}_W\!\left([F_n(x)-F_n(W)]_+\right).
}
\tag{2.5}
\]

This is an exact formula, not a bound. In particular `b_n(x)>=0`.

Since the bracketed random variable lies in `[0,1]`,

\[
\boxed{
0\le b_n(x)\le \frac{1}{4x^2(n-2)^2}.
}
\tag{2.6}
\]

The difference from the earlier proof is that (2.6) will now be integrated against the exact beta law of `X`; no good event and no Chernoff lower-tail patch are needed.

---

## 3. B14: the `S_k` covariance spectrum

Conditional on `X=x`, the vector `(R_i)_{i\in S}` is exchangeable under permutations of the selected-neighbor labels. Therefore its covariance matrix belongs to the two-dimensional commutant of the permutation representation:

\[
\Sigma_x=(a_n(x)-b_n(x))I_k+b_n(x)J_k,
\tag{3.1}
\]

where

\[
a_n(x)=q_n(x)(1-q_n(x)).
\]

The permutation representation decomposes as

\[
\mathbb R^k=\operatorname{span}\{\mathbf 1\}\oplus \mathbf 1^\perp.
\]

Accordingly, the two covariance eigenvalues are

\[
\lambda_{\mathrm{triv}}(x)
=a_n(x)+(k-1)b_n(x),
\tag{3.2}
\]

on the trivial representation and

\[
\lambda_{\mathrm{std}}(x)
=a_n(x)-b_n(x)
\tag{3.3}
\]

on the `(k-1)`-dimensional standard representation.

Since `H=\mathbf 1^T R`, only the trivial eigenspace contributes:

\[
\boxed{
\operatorname{Var}(H\mid X=x)
=k\lambda_{\mathrm{triv}}(x)
=kq_n(x)(1-q_n(x))+k(k-1)b_n(x).
}
\tag{3.4}
\]

Thus all conditional dependence relevant to the scalar degree deficit is compressed into one scalar ANOVA norm `b_n(x)`.

---

## 4. Exact global covariance budget

The root cutoff is

\[
X\sim\operatorname{Beta}(k+1,n-k-1).
\]

For `k>=2`, the inverse second moment is exact:

\[
\mathbb E[X^{-2}]
=
\frac{(n-1)(n-2)}{k(k-1)}.
\tag{4.1}
\]

Integrating (2.6) therefore gives

\[
\begin{aligned}
0
&\le
k(k-1)\,\mathbb E[b_n(X)]\\
&\le
\frac{k(k-1)}{4(n-2)^2}\mathbb E[X^{-2}]\\
&=
\boxed{\frac{n-1}{4(n-2)}}.
\end{aligned}
\tag{4.2}
\]

In particular, for every `n>=4` and `2<=k<=n-2`, the **entire ordered-pair covariance contribution is bounded by a universal constant below `1/2`**.

Combining (3.4), `q(1-q)<=q`, and the tower identity

\[
\mathbb E[kq_n(X)]=\mathbb EH,
\]

we obtain the finite-`n` inequality

\[
\boxed{
\mathbb E\operatorname{Var}(H\mid X)
\le
\mathbb EH+rac{n-1}{4(n-2)}.
}
\tag{4.3}
\]

This is the main proof-hardening identity of the run.

The exact finite-`n` beta-Gini formula proved in the preceding R7-03 run gives, with `r=n-1-k`,

\[
\mathbb EH
=
\frac{2B(n-1,n-1)}{B(k,k)B(r,r)}
\sim
\sqrt{\frac{kr}{\pi(k+r)}}
\tag{4.4}
\]

when `k,r->infinity`. Since

\[
s_n^2=\frac{k(n-k)}n=\frac{k(r+1)}{k+r+1}
\sim\frac{kr}{k+r},
\]

(4.4) says

\[
\mathbb EH\sim \frac{s_n}{\sqrt\pi}.
\tag{4.5}
\]

Therefore, throughout the complete interior regime `k->infinity`, `n-k->infinity`,

\[
\boxed{
\frac{\mathbb E\operatorname{Var}(H\mid X)}{s_n^2}
\le
\frac{1+o(1)}{\sqrt\pi\,s_n}+O(s_n^{-2})
\longrightarrow0.
}
\tag{4.6}
\]

Equivalently,

\[
\boxed{
\frac{H-\mathbb E(H\mid X)}{s_n}
\longrightarrow0
\quad\text{in }L^2.
}
\tag{4.7}
\]

This proves the conditional-noise negligibility needed for the interior limit **without** the former event `X>=k/(2n)`, without a Chernoff estimate for its complement, and without integrating `X^{-2}` by a tail split.

---

## 5. B1: alternate completion of the full interior limit

For completeness, the conditional mean can be handled exactly as in the order-statistic representation but independently of the old covariance argument. Put

\[
p_n:=\frac kn,
\qquad
\sigma_n:=\frac{s_n}{n},
\qquad
U_n:=\frac{X-p_n}{\sigma_n},
\qquad
V_n:=\frac{T-p_n}{\sigma_n}.
\]

Then

\[
\frac{kq_n(X)}{s_n}
=
\frac{k}{nX}\,g_n(U_n),
\qquad
 g_n(u):=\mathbb E[(u-V_n)_+].
\tag{5.1}
\]

If `k->infinity` and `n-k->infinity`, both beta shape parameters diverge, so

\[
U_n\Rightarrow Z,
\qquad
V_n\Rightarrow Z',
\]

with independent standard-normal limits. Uniform fourth-moment bounds imply `W_1(V_n,Z')->0`; because `v\mapsto(u-v)_+` is 1-Lipschitz uniformly in `u`,

\[
\sup_u|g_n(u)-g(u)|\to0,
\qquad
 g(u):=\phi(u)+u\Phi(u).
\tag{5.2}
\]

Also `k/(nX)=p_n/X->1` in probability. Hence

\[
\frac{\mathbb E(H\mid X)}{s_n}
=
\frac{kq_n(X)}{s_n}
\Rightarrow g(Z).
\tag{5.3}
\]

Together with the `L^2` noise estimate (4.7),

\[
\boxed{
\frac{H}{s_n}\Rightarrow g(Z).
}
\tag{5.4}
\]

For first-two-moment convergence, the conditional-mean term in (5.1) is uniformly square-integrable by the beta fourth-moment bounds on the central region and the exact beta inverse moments off it; alternatively one may combine the already proved exact mean formula with the standard beta fourth-moment estimate. Equation (4.6) then shows that the conditional-noise part has vanishing second moment on the `s_n` scale. Therefore

\[
\frac{\operatorname{Var}(H)}{s_n^2}\to
v:=\operatorname{Var}(g(Z))
=
\frac13+\frac{\sqrt3-2}{2\pi},
\tag{5.5}
\]

and the standardized degree limit follows exactly as in the existing P0458 theorem.

The point of this section is not to claim a new source endpoint — that was already reached — but to replace the most delicate dependence estimate by a shorter global identity.

---

## 6. Balanced-case local asymptotic: the projection constant is explicit

The recovery report singled out the balanced slice

\[
k_n=\left\lfloor\frac{n-1}{2}\right\rfloor.
\]

Here the ANOVA formula gives more than a bound. Let

\[
x_n(z):=p_n+\sigma_n z
\]

for fixed real `z`, and let `F_n` be the cdf of `T_n\sim Beta(k_n,n-k_n-1)`. In (2.5) define

\[
Y_{n,z}(W):=[F_n(x_n(z))-F_n(W)]_+.
\]

Since `T_n->1/2` in probability and the beta CLT gives

\[
F_n(x_n(z))\to\Phi(z),
\]

for Lebesgue-a.e. `w`,

\[
Y_{n,z}(w)	o \Phi(z)\mathbf 1_{\{w<1/2\}}.
\]

The variables are bounded by `1`, so dominated convergence in `L^2([0,1])` yields

\[
\operatorname{Var}_W(Y_{n,z}(W))
\to
\frac{\Phi(z)^2}{4}.
\tag{6.1}
\]

Since `x_n(z)->1/2`, (2.5) gives the explicit pair-covariance scaling

\[
\boxed{
n^2 b_n(x_n(z))\longrightarrow \Phi(z)^2.
}
\tag{6.2}
\]

Meanwhile (5.1) gives

\[
q_n(x_n(z))\sim\frac{g(z)}{\sqrt n},
\tag{6.3}
\]

because `s_n/k_n\sim n^{-1/2}`. Hence the two `S_k` covariance eigenvalues satisfy

\[
\lambda_{\mathrm{triv}}(x_n(z))
=q_n(1-q_n)+(k_n-1)b_n
\sim\frac{g(z)}{\sqrt n},
\tag{6.4}
\]

and

\[
\lambda_{\mathrm{std}}(x_n(z))
=q_n(1-q_n)-b_n
\sim\frac{g(z)}{\sqrt n}.
\tag{6.5}
\]

The pair dependence is one order smaller than the diagonal rare-rejection noise at the eigenvalue level. Consequently

\[
\boxed{
\frac{\operatorname{Var}(H\mid X=x_n(z))}{s_n}
\longrightarrow g(z).
}
\tag{6.6}
\]

This gives the balanced alternate mechanism requested by the stuck-recovery report: the root-cutoff fluctuation controls the order-`s_n` mean, while the entire non-root edge-array fluctuation has only order-`s_n^{1/2}` standard deviation and disappears after dividing by `s_n`.

---

## 7. What changed mathematically

The prior proof's fragile dependence step was

\[
\mathbb E[(H-kq_n(X))^2]/s_n^2\to0,
\]

proved by a pointwise covariance estimate plus a good-event/bad-event decomposition in `X`.

This run proves the stronger finite identity/bound

\[
\boxed{
\mathbb E\operatorname{Var}(H\mid X)
\le
\mathbb EH+rac{n-1}{4(n-2)},
}
\]

and obtains it from ANOVA plus the exact inverse beta moment. Thus the full dependence budget is `O(s_n)` in the entire interior regime, with the pair-covariance part itself `O(1)`.

This is a real proof simplification and a useful independent cross-check of the source solution. It does **not** count as either required independent audit because it is still owner-track work.

Frozen source metric remains

`R_unresolved: 0 -> 0` — **NO MOVEMENT**.

Mathematical source status remains **PROVED internally at source scope**. Protocol status remains **NOT CLOSED** until an actual P26 full-proof PASS and one distinct OTHER-track full-proof PASS exist.
