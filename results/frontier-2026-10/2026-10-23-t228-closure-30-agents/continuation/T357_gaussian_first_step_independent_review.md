# Independent proof audit: Gaussian tanh random features after one GD step

23 October 2026. A28. No subagents. This review concerns actual one-step output-layer gradient descent, not a ridge-path substitution or a generic random-feature Gaussian-equivalence assertion.

**Verdict: PASS for the first-step CLT, replica extension, and stated calibration lower bound in the final version pinned below.** I independently obtain the proposed signal and all three variance contributions. The covariance quadratic form, the radial-coefficient correction in the population mean, and the conditional training CLT can be justified by direct finite-dimensional Gaussian calculations. No missing finite-width term or normalization error was found.

An independent two-test-point argument below also proves convergence in probability of the realized network's conditional test law, and convergence in `L¹` of its population logistic risk. Fixed continuous witnesses transfer the limiting calibration error as a lower bound in probability. This strengthens an annealed statement, but still does not establish an exact limit of unbinned conditional calibration error, more than one GD step, or an early-stopping theorem.

The final author file audited is `followup/T357_gaussian_first_step_attempt.md`, SHA256 **`1469aad3c34b902a363fe66d32eff199c451adc28d2ae5ae4de6cbb716fd630b`**, 24,848 bytes. I first reconstructed the annealed proof from version `c1947b7b3c5c66aa381ea8d7b523fa9c1f10b0625620ebd22c00e94c74bba0e1`, then checked the substantive replica and calibration-witness revision `9e6647ba2ed3e8246f2dd54fd8709dc3dd179c4b61e2b16cecc1eaf53cbd28c5`. The final revision clarifies status, fresh-label notation, independent Gaussian names, and sigmoid-inverse measurability; these clarifications were checked against the accepted derivation.

## 1. Normalization and result

Let `F` be the `m×d` matrix with independent rows `W_j∼N(0,I_d/d)`. Inputs `X_i∼N(0,I_d)` are independent of the features and each other. Set `Z_i=θᵀX_i` for a deterministic unit vector `θ`, and draw labels conditionally independently with success probability `σ(βZ_i)`, for fixed `β≥0`. Write `R_i=Y_i−1/2` and

\[
h_j(x)=\tanh(W_j^\top x),\qquad
K_m(x,x')=m^{-1}h(x)^\top h(x').
\]

The exact first-step score under review is

\[
S_d=\frac{cd}{n}\sum_{i=1}^nR_iK_m(X_0,X_i),
\qquad n/d\to\alpha>0,\quad m/d\to\gamma>0,
\tag{1}
\]

where `c>0` is fixed. For readout `m^{-1/2}aᵀh` and mean logistic loss, (1) is precisely GD from zero with step `cd`. For unnormalized readout `aᵀh`, it is mean-loss GD with step `cd/m→c/γ`. These are different parameterizations of the same score update; no extra factor of `m`, `d`, or `n` is missing.

Define

\[
a=\mathbb E[G\tanh G]=\mathbb E\operatorname{sech}^2G,
\quad b=\mathbb E\tanh^2G,
\quad \mu=\mathbb E[G(\sigma(\beta G)-1/2)].
\]

Thus `a=1−b>0`. The result is

\[
(Z_0,S_d)\Rightarrow
\left(Z,\;ca^2\mu Z+c\tau G\right),
\qquad Z\perp G,\quad Z,G\sim N(0,1),
\]

\[
\boxed{\tau^2=\frac{\mu^2a^2b}{\gamma}
+\frac{a^4+b^2/\gamma}{4\alpha}.}
\tag{2}
\]

The quantity `b` is the full feature second moment, not `b−a²`. That distinction is essential to both finite-width contributions.

## 2. Gaussian estimates used here

For orthonormal Hermite polynomials, correlated standard normals satisfy
`E[H_k(G)H_l(G')]=1_{k=l}ρ^k`. One direct proof expands the identity

\[
\mathbb E\left[e^{sG-s^2/2}e^{tG'-t^2/2}\right]=e^{\rho st}
\]

in powers of `s,t`, and then extends by `L²` approximation. Odd functions have only odd degrees. Hence removing their degree-one covariance leaves an absolute remainder at most `|ρ|³` times their `L²` norms.

Gaussian Poincaré gives `Var g(G)≤E||∇g(G)||²`. In Hermite coordinates, the right side is the coefficient sum weighted by total degree and therefore dominates the nonconstant coefficient sum on the left. In particular, for centered `L`-Lipschitz `g`,

\[
\mathbb Eg^2\le L^2,\qquad
\mathbb Eg^4\le4L^2\mathbb Eg^2+(\mathbb Eg^2)^2\le5L^4.
\tag{3}
\]

The second inequality applies Poincaré to `g²`; our functions are smooth and bounded, so all applications are justified directly.

The elementary Gaussian matrix estimates needed below are `||F||op=O_P(1)`, bounded fixed moments of that norm, and `max_j| ||W_j||²−1 |→0` in probability. A fixed-radius sphere net and Gaussian tails prove the first two when `m/d` stays bounded; a chi-square Chernoff bound and union bound over `m=O(d)` rows prove the third. No sharp spectral-edge theorem is needed.

For two independent uniform directions on the unit sphere, their inner product `ρ` satisfies

\[
\mathbb E\rho^6=\frac{15}{d(d+2)(d+4)}.
\tag{4}
\]

Indeed, a Gaussian vector is the product of its independent length and direction: `15=E G_1^6=E||G||^6 E U_1^6`, and `E||G||^6=d(d+2)(d+4)`.

For primary documentation of the general Gaussian tools, I independently read Guangqu Zheng's author-hosted [*Gaussian analysis with applications*, Boston University, Fall 2025 notes](https://sites.bu.edu/gzheng90/files/2025/10/MA884_notes_updating-2.pdf): Lemma 1.6, printed p. 5, gives integration by parts; Proposition 1.14, p. 10, gives the Hermite proof of Poincaré; Proposition 2.3, p. 17, gives multivariate chaos expansion; Proposition 2.9, p. 21, gives Mehler's formula. The model-specific calculations below are derived here rather than imported from those notes.

## 3. Covariance operator: the row-norm dependence is controlled

Set

\[
\Sigma_F=\mathbb E_X h(X)h(X)^\top,\quad
q_j=\|W_j\|^2,\quad
A(q)=\mathbb E\operatorname{sech}^2(\sqrt qG),\quad
B(q)=\mathbb E\tanh^2(\sqrt qG).
\]

Let `D_A=diag(A(q_j))`. Exact Hermite separation gives

\[
\Sigma_F=D_AFF^\top D_A
+\operatorname{diag}\{B(q_j)-q_jA(q_j)^2\}+E_F,
\tag{5}
\]

where `E_F` has zero diagonal and, for `j≠k`,

\[
|(E_F)_{jk}|\le|\rho_{jk}|^3,
\qquad \rho_{jk}=\frac{W_j^\top W_k}{\|W_j\|\|W_k\|}.
\]

All row norms are positive almost surely. The coefficients of the first Hermite component are `√q_j A(q_j)`, which explains the precise first matrix in (5). Ignoring this row-dependent coefficient without a bound would be a gap.

Here it is harmless: uniform row-norm concentration and continuity imply `||D_A−aI||op→0` and uniform convergence of the diagonal in (5) to `b−a²`. Also, (4) gives the direct expectation bound

\[
\mathbb E\|E_F\|_F^2
\le\frac{15m(m-1)}{d(d+2)(d+4)}=O(d^{-1}).
\]

Thus the higher odd-Hermite remainder vanishes in operator norm, without a maximum-correlation bound or exceptional row-norm event. Combining this with `||F||op=O_P(1)` yields

\[
\|\Sigma_F-[a^2FF^\top+(b-a^2)I_m]\|_{\rm op}
\longrightarrow0\quad\text{in probability}.
\tag{6}
\]

This verifies the author's Lemma 1 and supplies a slightly cleaner remainder estimate. Oddness matters: the same Frobenius argument would not make an arbitrary quadratic Hermite term vanish.

## 4. The dependent test-feature quadratic form

The test feature vector `h=h(X_0)` depends on `F`; treating it as an independent isotropic vector would be unjustified. Conditioning on `X_0=x` resolves this exactly.

Put `r=||x||/√d`, `u=x/||x||`. The feature rows decompose as

\[
W_j=d^{-1/2}(G_ju+V_j),
\qquad h_j=\tanh(rG_j),
\]

where `G_j` are iid standard normals and `V_j` are independent standard Gaussians on the orthogonal subspace, independent of all the `G_j`. Conditional on `x,G_1,…,G_m`,

\[
\|F^\top h\|^2
\overset{\rm law}=\frac1d\left(\sum_jG_jh_j\right)^2
+\frac1d\left(\sum_jh_j^2\right)\chi^2_{d-1},
\tag{7}
\]

with independent chi-square variable. Conditional scalar laws of large numbers, boundedness of tanh, and `r→1` imply

\[
\frac d{m^2}\|F^\top h\|^2\to a^2+b/\gamma,
\qquad
\frac d{m^2}\|h\|^2\to b/\gamma.
\]

For example, the variance of `m^{-1}ΣG_j tanh(rG_j)` is at most `1/m`, uniformly in `r`; its mean tends to `a`. Thus the random conditioning radius causes no LLN gap.

Since `||h||²≤m`, (6) has `o_P(1)` effect after multiplication by `d/m²`. Hence

\[
Q_d:=\frac d{m^2}h^\top\Sigma_Fh
\to a^2(a^2+b/\gamma)+(b-a^2)b/\gamma
=a^4+b^2/\gamma.
\tag{8}
\]

This proves the requested quadratic-form concentration, including its finite-width constant.

## 5. Population mean: cubic and radial errors vanish in L²

Write `t=θᵀW`, `q=||W||²`, `τ(z)=σ(βz)−1/2`, and

\[
u(W)=\mathbb E_X[\tau(\theta^\top X)\tanh(W^\top X)].
\]

The exact population mean conditional on `F,X_0` is

\[
M_d=\mathbb E[S_d\mid F,X_0]
=\frac{cd}{m}\sum_jh_j(X_0)u(W_j).
\]

The odd Hermite expansion gives, without a lower bound on `q`,

\[
u(W)=\mu A(q)t+e(W),\qquad
|e(W)|\le\tfrac12|t/\sqrt q|^3.
\tag{9}
\]

The factor `1/2` follows from `||τ||₂≤1/2`, while `||tanh||₂≤1`. By (4), Cauchy–Schwarz for the feature average, and `|h_j|≤1`,

\[
\mathbb E\left|\frac d m\sum_jh_je(W_j)\right|^2
\le\frac{d^2}4\mathbb E|t/\sqrt q|^6=O(d^{-1}).
\tag{10}
\]

Thus no informal exceptional-event truncation is needed to justify this `L²` remainder.

The radial term requires more care. Define

\[
J_d=\frac d m\sum_j h_jt_j[A(q_j)-a].
\]

A bound by the maximum radial error followed by absolute summation is not sufficient at this scale. Instead, variance differentiation gives `A'(q)=(1/2)E[tanh'''(√qG)]`, uniformly bounded for `q≥0`. Consequently `A` is globally Lipschitz. Rotating `θ` to the first coordinate gives the exact moment

\[
\mathbb E[t^2(q-1)^2]=\frac{2d+8}{d^3}=O(d^{-2}):
\tag{11}
\]

expand `q−1=d^{-1}Σ_l(G_l²−1)` and use `E G_1²(G_1²−1)²=10` and `Var Σ_{l>1}(G_l²−1)=2(d−1)`.

Conditional on `X_0=x`, the summands are iid over features and have second moment `O(d^{-2})`, uniformly in `x`. Gaussian integration by parts, with `z=θᵀx`, yields exactly

\[
\mathbb E_W[t(A(q)-a)\tanh(W^\top x)]
=\frac1d\mathbb E_W\left[
2tA'(q)\tanh(W^\top x)
+z(A(q)-a)\operatorname{sech}^2(W^\top x)
\right].
\tag{12}
\]

Its absolute value is at most `C(1+|z|)d^{-3/2}`: use `E|t|=O(d^{-1/2})` and `E|q−1|≤√(2/d)`. Therefore

\[
\mathbb E\operatorname{Var}(J_d\mid X_0)=O(m^{-1}),
\qquad
\mathbb E|\mathbb E[J_d\mid X_0]|^2=O(d^{-1}),
\]

and `J_d→0` in `L²`. Combining (9)–(12),

\[
M_d=c\mu aT_d+o_{L^2}(1),
\qquad T_d=\frac d m\sum_j t_j\tanh(W_j^\top X_0).
\tag{13}
\]

This independently verifies the population-mean reduction, including the cancellation that a uniform norm approximation alone would miss.

## 6. Exact conditional Gaussian fluctuation of the population mean

Conditional on `X_0=x`, let `z=θᵀx`, `r=||x||/√d`. The same orthogonal decomposition as in (7) gives iid standard normals `G_j,H_j`, independent of each other, such that

\[
T_d=\frac z r\frac1m\sum_jG_j\tanh(rG_j)
+\frac{\sqrt d}{m}\sqrt{1-z^2/\|x\|^2}
\sum_jH_j\tanh(rG_j).
\tag{14}
\]

Conditional on `x,G_1,…,G_m`, the second term is exactly centered Gaussian, with variance tending in probability to `b/γ`. The first term tends to `aZ_0`. Conditional characteristic functions therefore give

\[
(Z_0,M_d)\Rightarrow
\left(Z,\;ca^2\mu Z+c\mu a\sqrt{b/\gamma}\,G_w\right),
\tag{15}
\]

where `G_w` is independent of `Z`. The sign of `μ` is immaterial for the variance; at `β=0`, `μ=0` and this fluctuation is absent.

There is also a direct moment bound: conditional on `x`, `Var T_d≤d/m`, and integration by parts gives `|E[T_d|x]|≤|z|`. Thus `sup_d E T_d²<∞`; (13) implies the same for `M_d`.

## 7. Conditional training CLT and independent variance addition

Conditional on `F,X_0`, let

\[
\xi_i=R_iK_m(X_0,X_i)-\mathbb E[R_iK_m(X_0,X_i)\mid F,X_0].
\]

These variables are iid and centered. Although the teacher is informative, `R_i²=1/4` identically. Therefore

\[
\operatorname{Var}(S_d-M_d\mid F,X_0)
=\frac{c^2d}{4n}Q_d-\frac{M_d^2}{n}
\to\frac{c^2}{4\alpha}(a^4+b^2/\gamma).
\tag{16}
\]

The subtracted term vanishes because `M_d=O_P(1)`. Replacing `R²` by a conditional Bernoulli variance would be incorrect here and would lose part of the sampling fluctuation.

For a Gaussian training input, `K(X)=m^{-1}h(X_0)ᵀtanh(FX)` is odd, hence centered, and has Lipschitz constant at most `||F||op/√m`. Equation (3) gives

\[
\mathbb E[K(X)^4\mid F,X_0]\le5\|F\|_{\rm op}^4/m^2.
\]

If `A=RK`, then `E|A−EA|⁴≤16E|A|⁴=EK⁴`. Consequently

\[
\sum_{i=1}^n\mathbb E\left[\left|\frac{cd}{n}\xi_i\right|^4
\middle|F,X_0\right]
\le\frac{5c^4d^4\|F\|_{\rm op}^4}{n^3m^2}
=O_P(d^{-1})\to0.
\tag{17}
\]

The triangular-array CLT applied conditionally gives convergence of the conditional characteristic function to the Gaussian characteristic function with the deterministic variance in (16), in probability. A formal justification is to take any subsequence, extract a further subsequence along which the conditional variance and Lyapunov remainder converge almost surely, and apply the deterministic triangular-array theorem on those conditioning realizations. This proves convergence in probability for the original sequence.

Conditional characteristic functions have modulus at most one, so this convergence is also in `L¹`. Multiplication by `exp(iuZ_0+ivM_d)` now proves that the training Gaussian is asymptotically independent of the pair in (15). Adding its variance to the width variance proves (2).

The conditional training variance has uniformly bounded expectation by Poincaré and bounded `E||F||op²`. Together with the `L²` population-mean bound, this yields `sup_d E S_d²<∞`. Logistic loss is bounded by `log 2+|S_d|`, so its annealed expectation converges. A fresh Bernoulli label can be added by conditioning on `Z_0`, since its success probability is a bounded continuous function of that coordinate.

## 8. Two independent test inputs: conditional test-law concentration

Let `X,X'` be fresh independent test inputs for the same feature matrix and training sample. The following independent extension verifies the proposed route to a realized-network statement.

First, condition on `F`. Since `E_X h(X)h(X)ᵀ=Σ_F`,

\[
\mathbb E_{X,X'}\left[
\left(\frac d{m^2}h(X)^\top\Sigma_Fh(X')\right)^2
\middle|F\right]
=\frac{d^2}{m^4}\operatorname{tr}(\Sigma_F^4).
\tag{18}
\]

Equation (6) implies `||Σ_F||op=O_P(1)`. On each event `||Σ_F||op≤C`, the right side is at most `C⁴d²/m³=O(d^{-1})`. Conditional Markov inequality and tightness of this norm give cross-quadratic-form convergence to zero in probability. Thus the two conditional training noises have vanishing cross covariance. Cramér–Wold and the same fourth-moment estimate apply to every fixed linear combination of their kernels.

For the population means, (13) holds jointly for the two tests. Conditional on `x,x'`, the feature rows are iid. Write `U=√d θᵀW`. The three Gaussian coordinates `(U,Wᵀx,Wᵀx')` have variances tending to one and pairwise covariances

\[
\operatorname{Cov}(U,W^\top x)=\frac{\theta^\top x}{\sqrt d},\quad
\operatorname{Cov}(U,W^\top x')=\frac{\theta^\top x'}{\sqrt d},\quad
\operatorname{Cov}(W^\top x,W^\top x')=\frac{x^\top x'}d,
\]

all tending to zero in probability. Therefore the two per-row centered variables `U tanh(Wᵀx)` and `U tanh(Wᵀx')` have limiting variances `b` and covariance zero. The Gaussian `U` supplies bounded fourth moments because tanh is bounded, so Gaussian continuity plus uniform integrability justifies the moment limits. Conditional Cramér–Wold proves independent width noises. The conditional means tend to `aθᵀx` and `aθᵀx'` by integration by parts. The independent standard-normal teacher coordinates remain independent of both width noises in the limit.

The conditional training characteristic functions then show that

\[
((Z,S_d),(Z',S_d'))\Rightarrow((Z,S),(\widetilde Z,\widetilde S)),
\tag{19}
\]

where the two limiting pairs are independent and each has law (2).

Let `\mathcal E_d` be the realized features and training data, and let `g` be any bounded continuous function of a teacher coordinate and a score. Define

\[
Q_d(g)=\mathbb E[g(Z,S_d)\mid\mathcal E_d].
\]

Single-test convergence gives `EQ_d(g)→E g(Z,S)`, and (19) gives `E Q_d(g)²→(E g(Z,S))²`. Hence

\[
Q_d(g)\longrightarrow\mathbb E g(Z,S)\quad\text{in }L^2.
\tag{20}
\]

A countable convergence-determining class yields weak convergence in probability of the conditional fresh-test law to the deterministic law (2). This is a precise quenched-in-probability statement. It is not almost-sure convergence for every realized sequence of trained networks.

The same second-moment proof applies to a fixed bounded measurable observable whose discontinuity set has zero probability under the limiting test law, by the corresponding bounded almost-everywhere-continuous form of weak convergence. It also applies after adding fresh labels, which are conditionally independent given their teacher coordinates.

The conditional population logistic risk in fact converges in `L¹`. Apply (20) first to the bounded continuous truncation `min(ell,B)`, where `ell` is logistic loss. The annealed second-moment bound gives `sup_d E[ell 1_{ell>B}]=O(B^{-1})`, and the limiting loss has the same tail control. The `L¹` distance between conditional risk and limiting risk is bounded by the two expected tails plus the `L¹` distance for the truncated observable, which tends to zero at fixed `B`. Then let `B→∞`. This proves the stronger risk statement in the author's replica revision.

## 9. Calibration lower bound without an exact calibration-error limit

Let `g(s)=E[Y|S=s]` for the Gaussian limit (2), and write `p(s)=σ(s)`. Gaussian conditioning gives the continuous function

\[
g(s)=\mathbb E_H\sigma\!\left(\beta\left[
\frac{A}{Q}s+\sqrt{1-A^2/Q}\,H\right]\right),
\quad A=ca^2\mu,\quad Q=A^2+c^2\tau^2>0.
\]

For the realized network, define

\[
\mathrm{CE}_d=\mathbb E\left[
|\mathbb E[Y\mid\sigma(S_d),\mathcal E_d]-\sigma(S_d)|
\middle|\mathcal E_d\right].
\]

Because sigmoid is one-to-one, any fixed bounded witness `w(S_d)` with `|w|≤1` is measurable with respect to the predicted probability. Conditional expectation and the triangle inequality give

\[
\mathrm{CE}_d\ge
\left|\mathbb E[(Y-\sigma(S_d))w(S_d)\mid\mathcal E_d]\right|.
\]

Choose the continuous bounded witnesses `w_k(s)=tanh(k[g(s)−p(s)])`. At each fixed `k`, the replica theorem makes the right-hand conditional expectation converge in `L²` to

\[
\mathbb E[(g(S)-p(S))\tanh(k[g(S)-p(S)])].
\]

This is nonnegative and tends, by dominated convergence, to `CE_infinity=E|g(S)−p(S)|`. Given `ε>0`, first choose a fixed `k` whose limiting expectation exceeds `CE_infinity−ε/2`, then let `d→∞`. It follows that

\[
\Pr\{\mathrm{CE}_d\ge\mathrm{CE}_{\infty}-\varepsilon\}\to1.
\]

The quantifier order is valid and does not require uniformity over a changing sequence of witnesses. This verifies the author's §9 extension. It is a lower bound only; weak conditional test-law convergence supplies no matching upper bound for the unbinned calibration functional.

## 10. Acceptance boundary

| Statement | Audit finding |
|---|---|
| Exact first GD-step normalization (1) | Verified. |
| Odd-Hermite covariance operator approximation | Verified, including random row norms and an `O(d^{-1})` squared-Frobenius remainder bound. |
| Dependent test-feature quadratic form | Verified by exact orthogonal Gaussian decomposition. |
| Population mean and finite-width fluctuation | Verified; cubic and radial errors vanish in `L²`. |
| Conditional training CLT and independent variance addition | Verified with an explicit Lyapunov bound. |
| Annealed logistic-risk limit | Verified by uniform integrability. |
| Conditional test-law concentration and population risk | Verified in the replica revision: bounded observables converge in `L²`; risk converges in `L¹`. |
| Limiting Gaussian model's conditional calibration curve | Follows by Gaussian conditioning once (2) is proved. |
| `CE_d≥CE_infinity−ε` with probability tending to one | Verified using a fixed continuous witness first, then the dimension limit. |
| Convergence of finite-network unbinned calibration error or conditional regression curves | Does not follow from weak test-law convergence, even in probability; not certified. |
| Full finite-time GD trajectory, early-stopping optimum, or publication novelty | Not established by this first-step theorem. |

The proof does not rely on numerical agreement. The identities `a=1−b` and `μ=a/2` at `β=2`, the exact moments (4) and (11), and the formal infinite-width/pure-noise reductions provide independent algebraic checks of the constants. No conclusion about later GD iterates is obtained by repeating the conditional iid argument, because the later coefficients depend on the same training sample nonlinearly.
