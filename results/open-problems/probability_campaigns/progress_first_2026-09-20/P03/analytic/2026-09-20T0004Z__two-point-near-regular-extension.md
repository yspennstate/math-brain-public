Model actually run: GPT-5.6 Sol; reasoning level UNVERIFIED. This was not GPT-6 at maximum, and I do not claim otherwise.

# P03-A analytic proof report — near-regular {2,3} offspring extension

**Status:** PROVED PARTIAL (new restricted theorem in this repository; not a full-source solution and not yet independently audited).

**Native role:** P03-A, `6aa7b398af30819181ca50ba3c4e6c33`, analytic recursive/derivative role under `operations/progress_first_2026-09-20/REGISTRY.md`.

**Captured master before write:** `7c8fc0bd163b33e5f1ea26632dbfc91c99aafabe`.

## 1. Source, convention, current range, and ownership continuity

The source problem is the Lyons–Pemantle–Peres monotonicity problem for biased random walk on a supercritical Galton–Watson tree without leaves. I use the **inward-bias convention** of He–Wang–Xiang / Aïdékon: if a vertex has `k` children, then for `lambda >= 0`

\[
P_\lambda(x,x^*)=\frac{\lambda}{\lambda+k},\qquad
P_\lambda(x,x_i)=\frac1{\lambda+k}.
\]

Thus larger `lambda` means stronger bias toward the root. If `nu` is the offspring variable, `m=E nu>1`, and `P(nu=0)=0`, the walk is transient for `0 <= lambda < m`. The conjecture asks whether the speed `ell_lambda` is nonincreasing on the whole interval `[0,m)`.

Primary / later sources checked this run:

* Lyons–Pemantle–Peres, *Biased random walks on Galton–Watson trees*, PTRF 106 (1996), and the 1997 unsolved-problems chapter.
* Ben Arous–Fribergh–Sidoravicius, *Lyons-Pemantle-Peres monotonicity problem for high biases*, CPAM 67 (2014), arXiv:1111.5865. Their outward-bias parameter is the reciprocal-style convention; in the inward `lambda` convention this is a small-`lambda` result.
* Aïdékon, *Speed of the biased random walk on a Galton–Watson tree*, PTRF 159 (2014), arXiv:1111.4313: exact speed representation used below.
* Ben Arous–Hu–Olla–Zeitouni, *Einstein relation for biased random walk on Galton–Watson trees*, AIHP 49 (2013), arXiv:1106.4387: monotonicity infinitesimally near the recurrent endpoint under its stated integrability hypotheses.
* He–Wang–Xiang, arXiv:1610.08151, published as *The speed of a biased walk on a Galton–Watson tree without leaves is monotonic for low values of bias*, J. Applied Probability 62 (2025), 1044–1052: if the minimum offspring is `m1 >= 2`, then `ell_lambda` is strictly decreasing for
  \[
  0\le \lambda\le \frac{m_1}{1+\sqrt{1-1/m_1}}.
  \]
* Bowditch–Tokushige, arXiv:1906.07913 (differentiability) and arXiv:2006.03433 (analyticity in the ballistic regime). Analyticity alone does not settle the sign of the derivative.

For the binary-minimum case `m1=2`, the strongest source-uniform low-bias interval recovered is
\[
[0,\lambda_*],\qquad \lambda_* = \frac{2}{1+1/\sqrt2}=4-2\sqrt2\approx1.171572875.
\]
A bounded literature search through the 2025 published monotonicity paper and the 2020 analyticity result found no full resolution of the interval between the low-bias theorem and the endpoint neighborhood. Failure to find a resolution is not a claim of exhaustive worldwide novelty.

**Full-source metric:** `R_full = 1` (full monotonicity on every no-leaf supercritical offspring law and every `lambda in [0,m)` remains unresolved); target is `0` only after a full proof or source-faithful refutation.

**Ownership check (performed once as directed):** no canonical `operations/claims/P0066.md` exists at the captured master. The owner registry explicitly assigns P03-A and P03-B as complementary non-exclusive roles on this source. The intended P03 report root did not yet contain a P03-B report at this snapshot, so there was no peer lemma to reuse in this first analytic iteration. Old D0047 history is untouched.

## 2. New exact reduction: speed is a regular-tree formula with an effective degree

Let
\[
\beta=\beta(\lambda)=P_e(\tau_{e^*}=\infty)
\]
be the escape probability from the artificial parent, and let `beta_i` be i.i.d. copies of `beta`, independent of `nu`. Aïdékon's speed formula (in this convention) is
\[
\ell_\lambda=
\frac{E\left[(\nu-\lambda)\,\beta_0/(\lambda-1+\sum_{i=0}^{\nu}\beta_i)\right]}
{E\left[(\nu+\lambda)\,\beta_0/(\lambda-1+\sum_{i=0}^{\nu}\beta_i)\right]}.
\tag{2.1}
\]

For each integer `k` in the support of `nu`, define
\[
D_k:=\lambda-1+\sum_{i=0}^{k}\beta_i,
\qquad
a_k(\lambda):=E\left[\frac{\beta_0}{D_k}\right].
\]
Set
\[
A(\lambda)=E[a_\nu(\lambda)],\qquad
B(\lambda)=E[\nu a_\nu(\lambda)],\qquad
M(\lambda)=\frac{B(\lambda)}{A(\lambda)}.
\]
Then (2.1) simplifies **exactly** to
\[
\boxed{\ \ell_\lambda=\frac{M(\lambda)-\lambda}{M(\lambda)+\lambda}\ }.
\tag{2.2}
\]
Indeed the numerator of (2.1) is `B-lambda A` and the denominator is `B+lambda A`.

Hence wherever differentiability holds,
\[
\boxed{\ \ell_\lambda'=
\frac{2(\lambda M'(\lambda)-M(\lambda))}{(M(\lambda)+\lambda)^2}.\ }
\tag{2.3}
\]
So the monotonicity problem becomes the single inequality
\[
\lambda M'(\lambda)<M(\lambda).
\tag{2.4}
\]
This is useful because for a nearly deterministic offspring law, `M` is a nearly constant effective degree even though the infinite random tree itself is never uniformly close to a regular tree.

## 3. Escape recursion and logarithmic derivative bound

For a vertex with children having escape probabilities `beta_1,...,beta_N`, the exact recursion is
\[
\beta=\frac{S}{\lambda+S},\qquad S=\sum_{j=1}^{N}\beta_j.
\tag{3.1}
\]
For offspring bounded below by 2 and `lambda<2`, comparison with the regular binary tree gives
\[
\beta\ge 1-\frac\lambda2.
\tag{3.2}
\]
(Equivalently, this is the `m1=2` case of the escape lower bound used by He–Wang–Xiang.)

Let
\[
q:=-\frac{\beta'}{\beta}.
\]
Differentiating (3.1) gives the exact smoothing identity
\[
q=
\frac1{\lambda+S}
+\frac{\lambda}{\lambda+S}
\sum_{j=1}^{N}\frac{\beta_j}{S}q_j.
\tag{3.3}
\]
Because (3.2) and `N>=2` imply `lambda+S>=2`, taking an essential supremum in (3.3) yields
\[
0\le q\le \frac1{2-\lambda},\qquad 0\le\lambda<2.
\tag{3.4}
\]
Differentiability is justified by the known derivative/analyticity results; (3.3) is also the finite-depth recursion behind the bound.

## 4. New restricted theorem

### Theorem (two-point near-binary monotonicity to `lambda=3/2`)

Let the offspring law be
\[
P(\nu=2)=1-p,\qquad P(\nu=3)=p,
\]
with
\[
0\le p<p_0,
\qquad
p_0:=\frac{4r}{5+4r}
=\frac{212-20\sqrt{43}}{867}
\approx0.0932540133,
\]
where
\[
r:=\frac{9-\sqrt{43}}{19}.
\]
Then the speed `ell_lambda` is **strictly decreasing for every**
\[
0\le \lambda\le \frac32.
\]
For every `p>0` in this range the tree is genuinely random, so this is not the regular-tree case.

For comparison, the source-uniform 2025 theorem with minimum offspring 2 reaches only
\[
\lambda_*=4-2\sqrt2\approx1.17157.
\]
Thus this proves a source-faithful monotonicity extension on the nonempty interval `(lambda_*,3/2]` for an explicit nontrivial offspring family.

### Proof

The known source-uniform theorem already proves strict decrease on `[0,lambda_*]`, and `lambda_*>1`. It therefore suffices to prove `ell'_lambda<0` on `[1,3/2]`.

For `k=2,3`, exchangeability gives
\[
(k+1)a_k
=E\left[\frac{S_{k+1}}{\lambda-1+S_{k+1}}\right],
\qquad S_{k+1}:=\sum_{i=0}^{k}\beta_i.
\tag{4.1}
\]
On `[1,3/2]`, (3.2) gives `beta_i >= 1-lambda/2`.

For `k=2`, since `s/(lambda-1+s)` is increasing in `s` when `lambda>=1`,
\[
a_2\ge
\frac{1-\lambda/2}{\lambda-1+3(1-\lambda/2)}
=\frac{2-\lambda}{4-\lambda}
\ge \frac15.
\tag{4.2}
\]
For `k=3`, the fraction in (4.1) is at most 1, so
\[
a_3\le\frac14.
\tag{4.3}
\]
Consequently
\[
\frac{a_3}{a_2}\le\frac54.
\tag{4.4}
\]

Now put
\[
f_k:=\frac{\beta_0}{D_k}.
\]
Using `beta_i'=-beta_i q_i`,
\[
\frac{f_k'}{f_k}
=-q_0-\frac{1-\sum_{i=0}^{k}\beta_i q_i}{D_k}.
\tag{4.5}
\]
On `[1,3/2]`, (3.4) gives `0<=q_i<=2`.

For `k=2`,
\[
D_2\ge \lambda-1+3(1-\lambda/2)=2-\lambda/2\ge\frac54.
\]
Also `0<=sum beta_i q_i<=6`, hence `|1-sum beta_i q_i|<=5`. Therefore
\[
\left|\frac{f_2'}{f_2}\right|\le 2+\frac5{5/4}=6,
\qquad
\left|\frac{a_2'}{a_2}\right|\le6.
\tag{4.6}
\]
(The second inequality follows by dominated differentiation and `|E f_2'|<=E|f_2'|`.)

For `k=3`,
\[
D_3\ge \lambda-1+4(1-\lambda/2)=3-\lambda\ge\frac32.
\]
Now `0<=sum beta_i q_i<=8`, so `|1-sum beta_i q_i|<=7`, and
\[
\left|\frac{a_3'}{a_3}\right|
\le 2+\frac7{3/2}
=\frac{20}{3}.
\tag{4.7}
\]
Hence
\[
\left|\frac{d}{d\lambda}\log\frac{a_3}{a_2}\right|
\le \frac{38}{3}.
\tag{4.8}
\]

For the two-point offspring law, the effective degree in (2.2) is
\[
M=\frac{2(1-p)a_2+3pa_3}{(1-p)a_2+pa_3}
=2+\theta,
\qquad
\theta:=\frac{pa_3}{(1-p)a_2+pa_3}.
\tag{4.9}
\]
The logistic derivative is exact:
\[
\theta'=\theta(1-\theta)
\frac{d}{d\lambda}\log\frac{a_3}{a_2}.
\tag{4.10}
\]
Therefore by (4.8),
\[
|M'|=|\theta'|
\le\frac{38}{3}\theta(1-\theta).
\tag{4.11}
\]
And from (4.4),
\[
\theta\le\frac{pa_3}{(1-p)a_2}
\le\frac{5p}{4(1-p)}.
\tag{4.12}
\]

Let
\[
r=\frac{9-\sqrt{43}}{19}.
\]
It is the smaller root of
\[
19t^2-18t+2=0.
\]
If `p<p0=4r/(5+4r)`, then (4.12) gives `theta<r`. Therefore
\[
19\theta(1-\theta)<2+\theta.
\tag{4.13}
\]
Combining `lambda<=3/2`, (4.11), (4.13), and `M=2+theta`,
\[
\lambda M'-M
\le \frac32|M'|-(2+\theta)
\le 19\theta(1-\theta)-(2+\theta)
<0.
\]
Equation (2.3) now yields `ell'_lambda<0` throughout `[1,3/2]`. Together with the source-uniform theorem on `[0,lambda_*]`, this proves strict decrease on `[0,3/2]`. QED.

## 5. Self-checks and why this is not the full conjecture

1. **Deterministic check.** At `p=0`, `M=2` and (2.2) gives the regular binary speed `(2-lambda)/(2+lambda)`, whose derivative is negative for `lambda<2`.
2. **Constant check.** `r=(9-sqrt(43))/19≈0.1285558671`, and solving `5p/[4(1-p)]<r` gives `p<(212-20sqrt(43))/867≈0.0932540133`.
3. **Denominator check.** On the new interval `[1,3/2]`, `D_2>=5/4` and `D_3>=3/2`, so differentiation under expectation has a uniform integrable bound once (3.4) is used.
4. **No metric substitution.** This restricted theorem does not change `R_full=1`; it closes only an intermediate family-specific obligation.
5. **No novelty overclaim.** A bounded 20 September 2026 literature check did not surface this exact `{2,3}` near-regular extension, but external novelty has not been exhaustively established.

## 6. Intermediate obligation ledger

* `O1` source convention and strongest recovered low-bias theorem: **DONE**.
* `O2` exact effective-degree reduction `ell=(M-lambda)/(M+lambda)`: **DONE**.
* `O3` explicit genuinely random family exceeding the universal cutoff: **DONE**, `{2,3}` with `p<p0`, monotone through `lambda=3/2`.
* `O4` remove the small-`p` restriction for `{2,3}`: **OPEN**.
* `O5` extend the effective-degree covariance control to arbitrary finite support with `min nu>=2`: **OPEN**.
* `O6` treat minimum offspring 1 and then all no-leaf laws: **OPEN**.
* `R_full`: **1 -> 1** (full LPP conjecture unresolved).

## 7. Exact remaining gap and next attack

The proof reduces the next bottleneck to controlling
\[
M'(\lambda)
=\operatorname{Cov}_{\pi_\lambda}\!\left(\nu,\frac{d}{d\lambda}\log a_\nu(\lambda)\right),
\qquad
\pi_\lambda(k)\propto P(\nu=k)a_k(\lambda),
\]
without paying the crude `theta << 1` factor. The most promising analytic next step is to prove a **one-sided** inequality, not an absolute-value bound:
\[
\frac{d}{d\lambda}\log a_{k+1}(\lambda)
-\frac{d}{d\lambda}\log a_k(\lambda)
\le C_k(\lambda)
\]
with `C_k` small or negative. The escape recursion (3.3) suggests conditioning on the extra `(k+2)`-nd branch and exploiting that adding a child raises `S`, lowers the coefficient `lambda/(lambda+S)`, and should damp the logarithmic sensitivity. If this yields monotonicity of `k -> (log a_k)'`, the covariance sign may become favorable and could remove the near-regular restriction entirely.

A second route is to generalize (4.9) from two points to finite support and bound `M'` by an Efron–Stein / conditional-covariance estimate under the tilted law `pi_lambda`. That is the next analytic attack; it is distinct from P03-B's coupling/regeneration role.
