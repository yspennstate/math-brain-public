Model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — this is **not GPT-6 at maximum**; GPT-6 / maximum reasoning was requested, but no authenticated runtime model/effort telemetry or binding selector is exposed.

# F0003 — rowwise Cramér tilting, localized congruence theta sums, and the `1/4` singularity exponent

Date: 2026-09-18 UTC.  
Slot: `R7-07 Hard Problem New Methods`, native ID `6aabe8413f60819197825dd81ca138ae`.  
Outside target: Van H. Vu, *Recent progress in combinatorial random matrix theory*, arXiv:2005.02797 / *Probability Surveys* 18 (2021), Section 5 immediately after Theorem 5.2.  
Primary undirected framework: Jiaoyang Huang, *Invertibility of adjacency matrices for random d-regular graphs*, arXiv:1807.06465.  
Imported one-row inverse input: Hoi H. Nguyen and Amanda Pan, *A note on the singularity probability of random directed d-regular graphs*, arXiv:2308.06461 / *European Journal of Combinatorics* (2024). Only their inverse characteristic-function mechanism for the same `U_{d,p}` walk is used; no directed global independence or directed singularity theorem is transferred.

Frozen metric:

\[
a_3:=\sup\{a\ge0:\Pr(A_{n,3}\text{ singular})\le n^{-a+o(1)}\}.
\]

Cumulative evidenced value before this artifact: **`a_3 >= 1/5`**.  
Value after the theorem below: **`a_3 >= 1/4` — MOVEMENT.**

Methods in this iteration: **B1 CHANGE THE CATEGORY / B15 BREAK THE SYMMETRY ON PURPOSE / B30 LOCALIZE.** The immediately preceding mathematical triple was B5/B12/B24.

The full source endpoint remains `a_3=1` and, for every fixed `d>=3`, exponent `d-2`. The result below is therefore **PARTIAL**, not source closure.

---

## 1. Cumulative interfaces reused without restarting

The previous R7-07 theorem proved

\[
\Pr(A_{n,d}\text{ singular over }\mathbb R)
\le O_d(n^{2-d})+n^{-1/5+o(1)}.
\tag{1.1}
\]

Its central analysis established the following facts in Huang's undirected symmetric-type representation.

Let `M=(m_ij)` be a symmetric edge-count type, let

\[
A_{ij}=\frac{m_{ij}}{dn}-\frac1{p^2},\qquad r=A\mathbf 1,
\]

and decompose

\[
A=H+\frac{r\mathbf1^T+\mathbf1r^T}{p},\qquad H\mathbf1=0.
\]

The exact quadratic exponent is

\[
Q(A)=\frac{dnp^2}{4}\|H\|_F^2+\frac{np}{2}\|r\|_2^2.
\tag{1.2}
\]

With

\[
u_{ij}=pA_{ij}-r_i,\qquad
X=\sqrt n\,pH,\qquad Y=\sqrt{np}\,r,\qquad Z=\sqrt n\,u,
\]

one has

\[
Z_{ij}=X_{ij}+\frac{Y_j}{\sqrt p},
\qquad
Q=\frac d4\|X\|_F^2+\frac12\|Y\|_2^2.
\tag{1.3}
\]

The previous run proved, after averaging rather than maximizing the corrections, that on the equidistributed sector

* the combined Stirling and local cubic perturbations have normalized variance `O_d(p^4/n)`;
* the complete fourth-order correction costs `O_d(p^4 log n/n)`;
* the exact row-denominator correction costs `O_d(p^3/n)`;
* every one of these perturbations is `o(Q)` on the broad equidistributed ball whenever `p^2 sqrt(log n/n)=o(1)`.

Hence **none of the central cumulant terms forces the old `p^5` restriction**. The two surviving restrictions were:

1. a one-row Fourier outer bound `exp(-c n/p^3)` was compared with a *global* `p^2`-dimensional type count;
2. the same `exp(-c n/p^3)` character separation was accompanied by a crude `exp(Cp^2 log n)` packing allowance in the congruence theta sum.

The purpose of this artifact is to remove both global payments. The resulting common condition is

\[
\boxed{p^4(\log n)^C=o(n)}
\tag{1.4}
\]

for a fixed finite `C`; logarithmic slack will be chosen at the end.

The field-independent sparse-support sieve from the earlier R7-07 work is also retained:

\[
\Pr(\exists\,0\ne x\in\ker_{\mathbb F_p}A,\ 3\le |\operatorname{supp}x|\le\delta_dn)
=o(n^{2-d}),
\tag{1.5}
\]

uniformly in the field, while support two is exactly the nonadjacent-twin event and has probability `O_d(n^{2-d})` in the simple graph model.

---

# 2. B1 — change category: tilt each row to its own target before Fourier analysis

The `1/5` proof used the inverse characteristic-function estimate at the original uniform `U_{d,p}` law. This makes the outer integral target-independent, whereas the central saddle can be exponentially small for an atypical row. Taking a ratio then appears to cost the largest possible row energy.

The correct category is an **exponential family**: for each row target, first perform the exact Cramér tilt that makes that target the mean. The large-deviation rate then factors out of both the central and outer pieces, so the inverse-characteristic estimate becomes genuinely relative.

## 2.1 One-row setup

For a symmetric type `M`, write

\[
n_i:=\frac1d\sum_jm_{ij},\qquad
q_{ij}:=\frac{m_{ij}}{dn_i}.
\]

Thus `q_i=(q_{i0},...,q_{i,p-1})` is a probability vector. Huang's row factor is the probability that `N_i:=n_i` iid copies of the same `U_{d,p}` count walk have total vector `m_i=(m_{i0},...,m_{i,p-1})`.

Put

\[
t_{ij}=q_{ij}-\frac1p.
\]

From the definitions,

\[
q_{ij}-\frac1p
=\frac{u_{ij}}{1+pr_i}.
\tag{2.1}
\]

On Huang's broad equidistributed ball, (1.2)-(1.3) imply

\[
\sum_i\|u_i\|_2^2\le C\frac{p^2\log n}{n},
\qquad
\max_i|pr_i|=o(1)
\tag{2.2}
\]

through the scale considered here. Hence, uniformly in the row,

\[
\|t_i\|_2\le C\,p\sqrt{\frac{\log n}{n}}.
\tag{2.3}
\]

Also `N_i=(1+o(1))n/p` uniformly.

Let `X` denote one uniform `U_{d,p}` step and `mu=E X=(d/p)1`. For `eta in 1^perp`, define the exponential tilt

\[
\Pr_\eta(X=x)=\frac{e^{\langle\eta,x\rangle}}{M(\eta)}\Pr_0(X=x),
\qquad M(\eta)=E_0e^{\langle\eta,X\rangle}.
\tag{2.4}
\]

At `eta=0`, the covariance on `1^perp` has all eigenvalues comparable to `1/p`, with constants depending only on fixed `d`. For `||eta||_infty<=o(1)`, the tilted weights are uniformly `e^{o(1)}`-comparable to the uniform weights, so the same covariance bounds hold. The inverse-function theorem, made quantitative by integrating the Hessian of `log M`, therefore gives a unique small `eta_i` satisfying

\[
E_{\eta_i}X=dq_i,
\tag{2.5}
\]

and

\[
\|\eta_i\|_2\le C_dp\|t_i\|_2
\le C_dp^2\sqrt{\frac{\log n}{n}}.
\tag{2.6}
\]

If `p=n^{1/4}/(log n)^K` with any fixed `K>1/4`, the final quantity in (2.6) tends to zero. In particular `||eta_i||_infty=o(1)` uniformly over all rows and all broad equidistributed symmetric types.

## 2.2 Exact rate factorization

Let

\[
I_i=\langle\eta_i,dq_i\rangle-\log M(\eta_i).
\]

Because `m_i=N_i d q_i`, the Radon-Nikodym identity gives **exactly**

\[
\Pr_0\Big(\sum_{a=1}^{N_i}X_a=m_i\Big)
=e^{-N_iI_i}
\Pr_{\eta_i}\Big(\sum_{a=1}^{N_i}(X_a-dq_i)=0\Big).
\tag{2.7}
\]

Thus every target-dependent exponential penalty has been factored out before the Fourier domain is divided into central and outer pieces.

This identity is the central change of category in the run.

---

## 3. A robust inverse theorem under the small Cramér tilt

Nguyen--Pan's inverse theorem for the uniform `U_{d,p}` walk says, in contraposed form, that outside the union of the `p` structured neighborhoods there is a fixed `c_d>0` with

\[
|\phi_0(s)|\le1-\frac{c_d}{p^2}.
\tag{3.1}
\]

A naive total-variation perturbation would be useless, because the gap itself is only order `p^{-2}`. The right quantity is the **phase energy**, which is multiplicatively stable under comparable weights.

### Lemma 3.1 — inverse gap survives every `o(1)` exponential tilt

Let `eta` satisfy `||eta||_infty=o(1)`. Uniformly outside the same structured neighborhoods,

\[
\boxed{|\phi_\eta(s)|\le1-\frac{c'_d}{p^2}}
\tag{3.2}
\]

for all sufficiently large `n`.

### Proof

For any probability law `rho` on the finite step space and independent `X,Y~rho`,

\[
1-|E_\rho e^{i\langle s,X\rangle}|^2
=E_{\rho\otimes\rho}
\big[1-\cos\langle s,X-Y\rangle\big].
\tag{3.3}
\]

Every `U_{d,p}` step has total mass `d`. Hence from (2.4)

\[
e^{-2d\|\eta\|_\infty}
\le
\frac{d\Pr_\eta}{d\Pr_0}(x)
\le
e^{2d\|\eta\|_\infty}
\tag{3.4}
\]

(after absorbing the normalizing factor, which lies between the same extrema). Applying (3.4) twice in the nonnegative expectation (3.3) yields

\[
1-|\phi_\eta(s)|^2
\ge e^{-O_d(\|\eta\|_\infty)}
\big(1-|\phi_0(s)|^2\big).
\tag{3.5}
\]

Outside the structured neighborhoods, (3.1) implies the right side is at least `c_d/p^2`. Therefore (3.2) follows, after decreasing the constant. QED.

The important point is that we never subtract an `O(||eta||)` error from a `p^{-2}` gap; we compare the positive phase energies multiplicatively.

---

## 4. Centered tilted local mass and the relative outer error

The exact centered probability in (2.7) has Fourier representation on the `(p-1)`-dimensional torus. Split it into the union `C` of the `p` structured neighborhoods and its complement `O`.

### Lemma 4.1 — uniform centered lower bound

Assume

\[
p^3(\log N)^C=o(N)
\tag{4.1}
\]

for a sufficiently large fixed `C`, `N\asymp n/p`, and `||eta||_infty=o(1)`. For every lattice-allowed centered target,

\[
\Pr_\eta\Big(\sum_{a=1}^N(X_a-E_\eta X)=0\Big)
\ge \exp[-C_dp\log N].
\tag{4.2}
\]

Moreover the Fourier integral over `O` has absolute value at most

\[
\exp[-c_dN/p^2].
\tag{4.3}
\]

### Proof

The outer estimate is immediate from Lemma 3.1:

\[
|\phi_\eta(s)|^N\le(1-c_d/p^2)^N
\le e^{-c_dN/p^2}.
\]

For the lower bound, repeat the central part of the Nguyen--Pan local Fourier calculation with `N` in place of their sample size. The needed estimates are uniform under the present tilt because the tilted weights differ from the uniform `U_{d,p}` weights by `e^{o(1)}` and every step has bounded total mass `d`.

Concretely, on `1^perp`, the tilted covariance eigenvalues remain in `[c_d/p,C_d/p]`. On the Fourier scale

\[
\|s\|_2=O\!\left(\frac{p}{\sqrt N}\sqrt{\log N}\right),
\]

Taylor expansion of the centered logarithmic characteristic function gives the Gaussian quadratic plus cubic and fourth-order remainders. The same `U_{d,p}` moment identities used in the directed proof give aggregate cubic size `O_d(p^{3/2}/\sqrt N)` on the Gaussian core and aggregate fourth-order size `O_d(p^3/N)`, up to fixed powers of `log N`. Under (4.1) both are `o(1)`. The complement inside a structured neighborhood is Gaussian-small, and Lemma 3.1 handles the region outside all structured neighborhoods.

The resulting central integral is bounded below by a constant-to-the-`p` multiple of the Gaussian determinant factor

\[
(\det(N\Sigma_\eta|_{1^\perp}))^{-1/2}
\asymp_d \left(\frac pN\right)^{(p-1)/2},
\]

up to the fixed lattice-periodicity factor. Its logarithm is `-O_d(p log N)`, proving (4.2). QED.

For our row size `N_i\asymp n/p`, condition (4.1) is exactly

\[
p^4(\log n)^C=o(n).
\tag{4.4}
\]

Combining (4.2)-(4.3), the ratio between a row's outer Fourier piece and its centered structured piece is therefore at most

\[
\epsilon_{row}
\le
\exp\left[-c_d\frac{n}{p^3}+C_dp\log n\right].
\tag{4.5}
\]

Crucially, **the Cramér rate `e^{-N_i I_i}` cancels from this ratio** by (2.7). Thus (4.5) is uniform even for a row that carries much more than average target energy.

---

# 5. B15 — break symmetry on one exceptional row: no global `p^2` type entropy is paid

The previous proof compared the one-row outer suppression with the number of possible symmetric types, producing

\[
e^{-cn/p^3}\quad\text{versus}\quad e^{O(p^2\log n)}.
\]

That is not the correct comparison. For a **fixed** symmetric type `M`, Huang's exact formula already factors the row probabilities. Apply (2.7) and the central/outer decomposition row by row before summing over `M`.

Write

\[
P_i(M)=C_i(M)+R_i(M)
\]

where `C_i` is the rate-factored structured-neighborhood contribution and `R_i` is the rate-factored outer contribution. By Lemma 4.1, after choosing the structured union invariant under complex conjugation, `C_i>0` for all sufficiently large `n` and

\[
|R_i|\le\epsilon_{row}C_i.
\tag{5.1}
\]

Therefore, pointwise in the symmetric type,

\[
\left|\prod_{i=0}^{p-1}P_i-\prod_{i=0}^{p-1}C_i\right|
\le
\big[(1+\epsilon_{row})^p-1\big]\prod_iC_i
\le 2p\epsilon_{row}\prod_iC_i
\tag{5.2}
\]

once `p epsilon_row=o(1)`.

But by (4.5),

\[
p\epsilon_{row}
\le
\exp\left[-c_d\frac n{p^3}+C_dp\log n+\log p\right]=o(1)
\tag{5.3}
\]

under `p^4 log n=o(n)`.

Equation (5.2) is the sought compatibility calculation for an exceptional row. A single row may carry an atypically large target displacement, but after rowwise Cramér tilting its rate penalty is present in both `C_i` and `R_i`; the only remaining ratio is the centered Fourier ratio (4.5). Hence **there is no union bound over `exp(O(p^2 log n))` symmetric types at this stage**. The positive sum over `M` can be taken only after the multiplicative row approximation has been established.

This removes the first `1/5` bottleneck.

---

# 6. B30 — localize the congruence theta sum before paying dimension

The second `1/5` bottleneck came from attaching a crude `Cp^2 log n` packing term to the *same* shifted-character exponent `-cn/p^3`. The correct localization separates two geometrically different effects:

1. the nearest shifted dual point, whose distance is `Theta(p^{-1/2})` and gives `e^{-cn/p^3}`;
2. all *other* dual points, which are a fixed positive distance away and therefore receive the much stronger `e^{-cn/p^2}` suppression.

## 6.1 The base count lattice has a dimension-free dual spacing

Use independent count coordinates consisting of `m_ij` for `i<j` and `m_ii/2` on the diagonal. After fixing total edge count, the difference lattice is a bounded diagonal rescaling of

\[
A_{D-1}=\{z\in\mathbb Z^D:\sum_a z_a=0\},
\qquad D=\frac{p(p+1)}2.
\]

Its dual in the total-sum-zero subspace is the projected integer lattice and has shortest nonzero vector of norm bounded below by an absolute positive constant. The diagonal factor two changes this only by an absolute constant. Thus there is `lambda_0>0`, independent of `p`, such that distinct points of the ordinary dual lattice are at Euclidean distance at least `lambda_0`.

In these count coordinates the quadratic precision inherited from (1.2) has eigenvalues between

\[
c_d\frac{p^2}{n}\quad\text{and}\quad C_d\frac{p^2}{n}.
\tag{6.1}
\]

## 6.2 Nontrivial finite characters

The previous B24 support lemma is retained exactly: every nonzero weighted-row mod-`p` character acts nontrivially on at least `p-1` independent upper-triangular count coordinates. Since `gcd(p,d)=1`, a nonzero `a/p` phase cannot be cancelled modulo integers by a mod-`d` phase. Consequently, modulo the ordinary dual lattice,

\[
\operatorname{dist}(u_\chi,L^*)^2\ge\frac{c_d}{p}
\tag{6.2}
\]

for every character with nontrivial mod-`p` part. Purely mod-`d` nontrivial characters have a stronger constant lower bound.

The finite character group has size

\[
|G|=d^{p-1}p^p=\exp[O_d(p\log p)].
\tag{6.3}
\]

## 6.3 Shifted theta lemma

Let `Theta_chi` be the Gaussian theta sum after inserting a finite character and `Theta_0` the unshifted one. Poisson summation gives, after cancellation of the common determinant factor,

\[
\frac{|\Theta_\chi|}{\Theta_0}
\le
\sum_{\ell\in L^*+u_\chi}
\exp\left[-c_d\frac n{p^2}\|\ell\|^2\right],
\tag{6.4}
\]

because the unshifted dual zero term alone lower-bounds the denominator.

Choose a nearest shifted dual point. If its distance is at most `lambda_0/4`, then every other shifted dual point is at distance at least `3lambda_0/4`. If the nearest distance is larger, *every* point already has constant distance. In either case, (6.2) and a standard shell-packing bound in dimension `D=O(p^2)` give

\[
\boxed{
\frac{|\Theta_\chi|}{\Theta_0}
\le
\exp\left[-c_d\frac n{p^3}\right]
+
\exp\left[C_dp^2\log n-c_d\frac n{p^2}\right].
}
\tag{6.5}
\]

The key difference from the previous estimate is structural: the `Cp^2 log n` packing term is attached only to the **constant-distance tail**, whose exponent is `-cn/p^2`, not to the nearest shifted point with exponent `-cn/p^3`.

Summing (6.5) over (6.3) yields

\[
\sum_{\chi\ne1}\frac{|\Theta_\chi|}{\Theta_0}=o(1)
\tag{6.6}
\]

provided

\[
\frac n{p^3}\gg p\log p
\quad\text{and}\quad
\frac n{p^2}\gg p^2\log n.
\]

Both are implied by

\[
\boxed{p^4\log n=o(n).}
\tag{6.7}
\]

Hence the exact congruence Gaussian mass is `(1+o(1))/|G|` of the unconstrained Gaussian mass through the quarter-power scale.

The same argument may be differentiated a fixed number of times. Polynomial factors in the dual variable and in `n,p` do not affect either exponential separation in (6.5). Therefore every degree-at-most-six Gaussian moment used in the cumulative B5/B12 cubic, quartic, and denominator estimates agrees on the exact congruence lattice with its continuous centered Gaussian counterpart up to `o(1)`. In particular the odd-cubic cancellation is legitimate on the exact arithmetic class at the new scale.

This removes the second `1/5` bottleneck.

---

# 7. Central equidistributed contribution through `p=n^{1/4-o(1)}`

We now combine the two new localizations with the already-proved central estimates.

Choose `p` satisfying `p^4 (log n)^C=o(n)` with enough fixed logarithmic slack. Then:

1. **Row outer regions.** B1/B15 give the pointwise-in-`M` multiplicative error `1+o(1)` from (5.2)-(5.3), so no global type entropy is paid.

2. **Exact congruences.** B30 gives the correct `1/|G|` theta fraction with relative error `o(1)`, and differentiated Poisson summation transfers all fixed-degree Gaussian moments.

3. **Stirling and local cubics.** The cumulative averaged error is

\[
O_d(p^4/n)=o(1).
\]

4. **Fourth order.** The cumulative normalized cost is

\[
O_d(p^4\log n/n)=o(1).
\]

5. **Exact row denominators.** The cumulative normalized cost is

\[
O_d(p^3/n)=o(1).
\]

6. **Broad-ball domination.** The ratio of every retained nonquadratic perturbation to the quadratic form is bounded by

\[
O_d\left(p^2\sqrt{\frac{\log n}{n}}\right)=o(1),
\]

so Gaussian complements remain negligible.

It follows, by the same exact Huang symmetric-type normalization used in the previous theorem, that the expected number `N_ns` of nonzero finite-field kernel vectors in the equidistributed/non-sparse sector is

\[
E N_{ns}=O_d(1)
\tag{7.1}
\]

uniformly for primes satisfying (1.4).

No directed global factorization has been imported. The only directed-paper ingredient is the one-row inverse phase-energy statement for the same `U_{d,p}` step law, and Section 3 proves that this input survives the rowwise tilt needed in the undirected symmetric calculation.

---

# 8. Non-equidistributed classes at the same scale

The earlier R7-07 source inspection localized Huang's non-equidistributed estimates as follows.

* The near-zero corner class is `exp[-b c p^2 log n+O(p^2 log n)]` and is killed by choosing the source constant `b` large.
* The far class is

\[
\exp[-c n/p^2+O(p^2\log n)],
\]

which is `o(1)` precisely under the second inequality in (6.7).
* The sparse third class is no longer counted value-by-value. By the field-independent support sieve (1.5), it has event probability `O_d(n^{2-d})` whenever its support cutoff `O(p^3 log n)` is `o(n)`. This condition has a large margin at the quarter-power scale.

Thus no non-equidistributed class introduces a stricter condition than `p^4 log n=o(n)`.

Conditioning the configuration model on simplicity costs only a fixed `d`-dependent constant, because the probability of simplicity is bounded away from zero for fixed `d`.

---

# 9. Finite-field inequality and the quarter-power theorem

Outside the sparse event, if the simple adjacency matrix is singular over `F_p`, its nonzero kernel contains at least `p-1` nonzero vectors, all counted by `N_ns`. Therefore

\[
(p-1)\mathbf1_{\{A\text{ singular mod }p\}\cap E_{sp}^c}
\le N_{ns}.
\]

Taking expectations and using (1.5), (7.1), and simplicity conditioning gives

\[
\Pr(A_{n,d}\text{ singular over }\mathbb F_p)
\le O_d(n^{2-d})+O_d(1/p).
\tag{9.1}
\]

Because an integer matrix singular over `R` has determinant exactly zero, real singularity implies singularity modulo every prime. Hence (9.1) is also an upper bound for real singularity.

Set, for example,

\[
x_n=\frac{n^{1/4}}{(\log n)^{10}}.
\]

By Bertrand's postulate choose a prime `p_n in [x_n,2x_n]`. For fixed `d`, eventually `p_n>d`, so `gcd(p_n,d)=1`. All displayed polynomial/logarithmic conditions above hold, and

\[
\frac1{p_n}=n^{-1/4+o(1)}.
\]

We obtain the theorem

\[
\boxed{
\Pr(A_{n,d}\text{ singular over }\mathbb R)
\le O_d(n^{2-d})+n^{-1/4+o(1)}
}
\tag{9.2}
\]

for every fixed `d>=3`. In particular,

\[
\boxed{a_3\ge\frac14.}
\tag{9.3}
\]

This is strict movement from the previous `a_3>=1/5` theorem. It is still far from the source-predicted cubic endpoint `a_3=1`.

---

# 10. What is genuinely new and what remains open

The new mechanism is not another higher-order Edgeworth calculation. It is a change in where the large-deviation cost is paid:

* **B1:** rowwise exponential tilting factors the exact target rate out before Fourier localization;
* **B15:** this makes one exceptional row no worse than a typical row in *relative* outer error, so the outer estimate is multiplied rowwise before the symmetric type sum and never pays `exp(O(p^2 log n))`;
* **B30:** the congruence theta sum is split into its single nearest shifted dual point and its constant-distance tail, attaching the dimension packing loss only to the stronger `exp(-cn/p^2)` tail.

The common new barrier is now

\[
\boxed{e^{-cn/p^3}\quad\text{versus only}\quad e^{O(p\log p)},}
\]

together with ordinary lattice discretization

\[
\boxed{e^{-cn/p^2+O(p^2\log n)}}.
\]

Both meet at `p^4 log n=o(n)`.

No finite checker is appropriate: the result is an asymptotic analytic theorem. The exact finite/combinatorial ingredient reused here is the previously proved character-support lemma; its hypotheses are unchanged. The present proof does **not** claim the quarter-power barrier is intrinsic. To move beyond `1/4`, one must exploit more than a row-by-row inverse gap, because an undirected row contains only `N_i\asymp n/p` iid `U_{d,p}` steps. The natural next question is whether symmetry couples the row Fourier variables strongly enough to recover an `n`-sample suppression in collective directions, or whether one can classify the few row phases that simultaneously approach their structured neighborhoods.

Full source closure is absent. Independent P26 and distinct OTHER-track audits are absent, and no source-level paper package is claimed.

---

# 11. Source and prior-art status checked 2026-09-18

Vu's source still asks for the sharp exponent after Huang's polynomial bound. Huang's paper treats both directed and undirected models and supplies the undirected symmetric-type/local-CLT framework used here. Nguyen--Pan's paper is explicitly titled and stated as a directed-model result; it proves the directed `n^{-1/3+o(1)}` bound and extends the one-row `U_{d,p}` local Fourier treatment to `p<=n^{1/3-o(1)}` in that directed setting. This artifact imports only the identical one-row inverse mechanism and proves the additional tilted stability needed here.

A bounded fresh search on 2026-09-18 also found He--Huang's September 2026 *The oriented Kesten--McKay law for random regular digraphs*, which concerns directed spectral density / hard-edge estimates, and Huang--McKenzie--Yau's fixed-degree edge-universality work. Neither search result states the sharp undirected atom-at-zero exponent `d-2`. No later source-matching resolution was found in the bounded search. That is negative evidence only: worldwide openness and publication novelty remain **UNVERIFIED**.

---

# 12. Next nonrepeating attack

The next run must not repeat B1/B15/B30. Use:

1. **B14 — exploit the symmetry group:** classify simultaneous structured row phases under the symmetric `S_p` action and determine the dimension of the genuinely dangerous collective frequency manifold;
2. **B21 — import an analogous technique:** compare the resulting collective phase manifold with inverse Littlewood--Offord / inverse-Kneser stability, looking for an `n/p^2` or stronger suppression in nontrivial symmetric directions;
3. **B27 — compress the proof:** formulate a block-Fourier transfer operator in which the `p` row neighborhoods are one orbit, so that entropy is charged by orbit dimension rather than row count.

Frozen metric objective remains `a_3`; any next movement must improve the exponent beyond `1/4` without changing its definition.
