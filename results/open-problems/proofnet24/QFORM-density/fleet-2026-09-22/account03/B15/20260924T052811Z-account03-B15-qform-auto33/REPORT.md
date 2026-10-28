SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B15, 2026-09-24T05:28:11Z.
attacking: a countable rational-generic extremal skeleton for the full universal interval constant, followed by same-constant C0 closure.

# account03/B15 — countable rational skeleton at the exact QFORM constant

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `20260924T052811Z-account03-B15-qform-auto33`  
Status: `COUNTABLE_RATIONAL_CORE_EQUIVALENCE_PROVED / PARTNER_APPLIED / FULL_QFORM_OPEN`  
Execution: `WITHOUT_VERIFIED_BRAIN`.

## 1. Result

Let

\[
H(\mu):=\sup_{a<b}\frac{\mu((a,b))}{b-a}
\]

for a probability measure on the line. Let `C_all` be the supremum of `H` over the full owner target: arbitrary finite `n`, arbitrary independent one-dimensional probability densities `0<=f_i<=1`, and arbitrary real symmetric `A` having at least three eigenvalues of absolute value at least one.

Define the following **countable** subclass.

1. `F_Q`: densities `1_E`, where `E` is a finite union of bounded intervals with rational endpoints and total Lebesgue measure exactly one.
2. `A_(n,Q)^gen`: symmetric `n x n` matrices with rational entries, simple spectrum, every nonempty principal minor nonzero, and at least three eigenvalues of absolute value **strictly greater than one**.
3. `I_Q`: bounded open intervals with rational endpoints.

Set

\[
C_{\mathbb Q}:=
\sup_{\substack{n\ge1,\ A\in A_{n,\mathbb Q}^{gen},\\
 f_i\in F_{\mathbb Q},\ I\in I_{\mathbb Q}}}
\frac{\Pr\{X^TAX\in I\}}{|I|}.
\]

The main theorem of this run is

\[
\boxed{C_{all}=C_{\mathbb Q}.}
\tag{1.1}
\]

Consequently the full QFORM conjecture is equivalent, with **exactly the same optimal universal constant**, to the same interval estimate on a countable collection of rational, compactly supported, bang-bang product inputs and rational algebraically generic target matrices. If no finite universal constant exists, then for every `N` there is already a witness in this countable skeleton with interval ratio bigger than `N`.

No fragment-count bound is asserted. The number of interval components in the approximation below is allowed to tend to infinity, exactly as required by the live fixed-fragment correction.

## 2. One-dimensional rational chattering lemma

### Lemma 2.1

For every probability density `f` on `R` satisfying `0<=f<=1`, there exist sets `E_m`, each a finite union of bounded intervals with rational endpoints and `|E_m|=1`, such that

\[
1_{E_m}(x)\,dx \Rightarrow f(x)\,dx.
\tag{2.1}
\]

### Proof

Fix `eps_m downarrow 0`. Choose an integer `R_m -> infinity` so that

\[
\delta_m:=\int_{|x|>R_m}f(x)\,dx<\varepsilon_m.
\]

Choose a rational mesh `h_m>0` tending to zero and dividing `2R_m`. Partition `[-R_m,R_m]` into finitely many rational-endpoint cells `J_{m,k}` of length `h_m`; write their number as `N_m` and

\[
a_{m,k}:=\int_{J_{m,k}}f(x)\,dx\in[0,h_m].
\]

For each cell choose a rational number `q_{m,k}` such that

\[
0\le q_{m,k}\le a_{m,k},\qquad
0\le a_{m,k}-q_{m,k}<\varepsilon_m/N_m.
\tag{2.2}
\]

This is possible by density of the rationals; if `a_{m,k}=0`, take `q_{m,k}=0`. In each `J_{m,k}` take the left subinterval `L_{m,k}` of length `q_{m,k}`. Its endpoints are rational. Put

\[
s_m:=\sum_k(a_{m,k}-q_{m,k})<\varepsilon_m,
\qquad
d_m:=1-\sum_kq_{m,k}=\delta_m+s_m<2\varepsilon_m.
\tag{2.3}
\]

Because every `q_{m,k}` is rational, `d_m` is rational. Add one reserve interval

\[
D_m=[R_m+1,R_m+1+d_m]
\]

and define

\[
E_m=D_m\cup\bigcup_kL_{m,k}.
\]

Then `E_m` is a finite rational-endpoint union and, exactly,

\[
|E_m|=\sum_kq_{m,k}+d_m=1.
\]

It remains to prove weak convergence. Let `phi in C_c(R)`. For all sufficiently large `m`, the support of `phi` lies in `[-R_m,R_m]`, so the reserve interval contributes zero. Let `omega_phi(h)` be the modulus of continuity on the compact support enlarged by one cell, and choose one point `x_{m,k}` in each cell. Cellwise,

\[
\begin{aligned}
\left|\int_{L_{m,k}}\phi
-\int_{J_{m,k}}\phi f\right|
&\le |\phi(x_{m,k})|\,|q_{m,k}-a_{m,k}|\\
&\quad+\omega_\phi(h_m)(q_{m,k}+a_{m,k}).
\end{aligned}
\]

Summing and using `sum a_{m,k}<=1`, `sum q_{m,k}<=1`, gives

\[
\left|\int\phi 1_{E_m}-\int\phi f\right|
\le \|\phi\|_\infty s_m+2\omega_\phi(h_m)\to0.
\tag{2.4}
\]

Thus the probability measures `1_{E_m}dx` converge vaguely to the probability measure `f dx`; because all masses equal one and the limit has mass one, vague convergence is weak convergence. This proves (2.1).

Remarks:
- This is deliberately a weak, oscillatory/chattering approximation. In general `1_E` laws are **not** dense in `L^1` among all cap-one densities.
- The number of components is not controlled and may diverge. Therefore the lemma does not conflict with `QFORM-NO-UNIFORM-FRAGMENT-COUNT-BATHTUB-v1`.

## 3. Rational generic target matrices are dense from inside the target

For fixed `n`, define the polynomial on real symmetric matrices

\[
P(A)=\operatorname{Disc}(\chi_A)\prod_{\emptyset\ne S\subset\{1,\dots,n\}}\det A_{S,S}.
\tag{3.1}
\]

This is not the zero polynomial: a diagonal matrix with distinct nonzero diagonal entries makes every factor nonzero. Hence the set `P(A)!=0`, i.e. simple spectrum and all nonempty principal minors nonzero, is open dense. Because rational symmetric matrices are dense, rational points in this generic set are dense as well.

### Lemma 3.1

If `A` is any owner-target matrix, then there exists a sequence `A_m in A_(n,Q)^gen` with

\[
\|A_m-A\|_{op}\to0.
\tag{3.2}
\]

### Proof

Take `eta_m downarrow0` and first form

\[
B_m=(1+4\eta_m)A.
\]

Every eigenvalue of `A` with absolute value at least one is moved to absolute value at least `1+4 eta_m`. Choose a rational generic symmetric `A_m` with

\[
\|A_m-B_m\|_{op}<\eta_m.
\tag{3.3}
\]

Weyl's inequality preserves each positive eigenvalue originally at least one above `1+3 eta_m`, and each negative eigenvalue originally at most minus one below `-1-3 eta_m`. Thus `A_m` has at least three eigenvalues of absolute value strictly bigger than one. Also

\[
\|A_m-A\|_{op}
\le \eta_m+4\eta_m\|A\|_{op}\to0.
\]

This proves the lemma. No spectral-coordinate independence is used.

## 4. Simultaneous weak closure of product laws and matrices

Fix one arbitrary full target instance `(A,f_1,...,f_n)`. For each `i`, choose the rational bang-bang approximants `f_{i,m}=1_{E_{i,m}}` from Lemma 2.1, and choose `A_m` from Lemma 3.1. Since `n` is finite,

\[
\bigotimes_{i=1}^n f_{i,m}(x_i)dx_i
\Rightarrow
\bigotimes_{i=1}^n f_i(x_i)dx_i.
\tag{4.1}
\]

The maps

\[
q_m(x)=x^TA_mx
\]

converge to `q(x)=x^TAx` uniformly on every compact subset of `R^n`. Therefore the extended continuous-mapping theorem gives

\[
\mu_m:=\operatorname{Law}_{f_{1,m}\otimes\cdots\otimes f_{n,m}}(X^TA_mX)
\Rightarrow
\mu:=\operatorname{Law}_{f_1\otimes\cdots\otimes f_n}(X^TAX).
\tag{4.2}
\]

For completeness, this follows directly from tightness of the product laws: on a compact cube carrying all but arbitrarily small mass, `q_m->q` uniformly, and a bounded continuous test function is uniformly continuous on the corresponding bounded image.

## 5. Rational output intervals are enough

Assume first that `C_Q<infinity`. By definition, every rational-skeleton law `mu_m` satisfies

\[
\mu_m(J)\le C_{\mathbb Q}|J|
\tag{5.1}
\]

for every bounded open interval `J` with rational endpoints.

Let `I=(a,b)` be any bounded open interval, with arbitrary real endpoints. Choose rational outer intervals

\[
J_r=(a_r,b_r)\supset I,
\qquad |J_r|\downarrow|I|.
\]

Monotonicity and (5.1) give, for every fixed `m`,

\[
\mu_m(I)\le C_{\mathbb Q}|I|.
\tag{5.2}
\]

Applying Portmanteau to the open set `I` in (4.2),

\[
\mu(I)\le\liminf_m\mu_m(I)\le C_{\mathbb Q}|I|.
\tag{5.3}
\]

Thus every full target law obeys the same interval inequality, so

\[
C_{all}\le C_{\mathbb Q}.
\]

The reverse inequality is immediate because the rational skeleton is a subclass of the full target. Hence (1.1) follows when `C_Q<infinity`. If `C_Q=infinity`, the subclass inclusion already forces `C_all=infinity`, so (1.1) holds in all cases.

## 6. Countability and a canonical blow-up witness sequence

The skeleton is countable:

- `n` ranges over the positive integers;
- rational symmetric matrices form a countable set;
- a finite union of rational-endpoint intervals is specified by a finite rational tuple;
- finite products of countable sets are countable;
- rational output intervals are countable.

Therefore all interval ratios in the definition of `C_Q` can be enumerated as a sequence `(r_k)_{k>=1}` and

\[
C_{all}=C_{\mathbb Q}=\sup_{k\ge1}r_k.
\tag{6.1}
\]

In particular, if the universal conjecture is false, there is a **countable rational-generic witness sequence** with `r_{k_j}->infinity`; no uncountable or nonmeasurable pathology is required to witness failure.

Conversely, proving a single uniform bound on this enumerated rational skeleton proves the full owner theorem with exactly the same constant.

## 7. Peak formulation using completed fixed-instance regularity

The completed rank-at-least-three fixed-matrix theorem at

`yspennstate/math-open-problems@9b8bb7e84811978a2c46c7bb5ec50f2570dbc056`

path

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B15/20260922T200544Z-account02-B15-qform-r11/REPORT.md`

proves that every fixed rank-at-least-three cap-one product instance has a density in `C_0(R) cap L^infinity(R)`. Every rational-skeleton matrix has at least three eigenvalues of modulus bigger than one, hence rank at least three. Therefore each skeleton law has a canonical continuous density `p_theta` vanishing at infinity, and

\[
H(\mu_\theta)=\|p_\theta\|_\infty=\max_{t\in\mathbb R}p_\theta(t).
\tag{7.1}
\]

Consequently

\[
\boxed{
C_{all}=\sup_{\theta\in\mathscr S}\max_t p_\theta(t),
}
\tag{7.2}
\]

where `S` is countable. Since every `p_theta` is continuous, `max_t p_theta(t)=sup_{r in Q}p_theta(r)`, so even the peak-height formulation reduces to a countable set of evaluations once canonical representatives are fixed.

This is a logical/regularity reduction, not an algorithmic proof of a uniform bound.

## 8. Designated partner account04/B15 applied at an actual inequality

The completed account04/B15 theorem in

`yspennstate/math-open-problems@7b2b0f54db9acbd23a5f69f715178ab666e22d8e`

path

`proofnet24/QFORM-density/fleet-2026-09-22/account04/B15/20260923T221909Z-account04-B15-ruled-trace-c0-r8/REPORT.md`

states that, for every rank-at-least-three target/product instance, once an interval estimate

\[
\Pr\{Q\in I\}\le M|I|
\tag{8.1}
\]

has been separately established, the law has a canonical representative

\[
p_Q\in C_0(\mathbb R),\qquad \|p_Q\|_\infty\le M
\tag{8.2}
\]

with **no increase in the height constant**.

Apply that theorem to the actual transported inequality (5.3). If `C_Q<infinity`, every arbitrary owner-target instance satisfies

\[
\Pr\{X^TAX\in I\}\le C_{\mathbb Q}|I|.
\]

Hence account04/B15 gives

\[
\boxed{
p_{X^TAX}\in C_0(\mathbb R),\qquad
\|p_{X^TAX}\|_\infty\le C_{\mathbb Q}=C_{all}.
}
\tag{8.3}
\]

Thus the stronger continuity conclusion is again a zero-loss post-height closure. The hard universal problem is exactly the boundedness of the countable rational-skeleton ratios, not continuity.

## 9. Relation to live corrections

This proof uses none of the refuted interfaces:

- no law-uniform pointwise van-der-Corput decay;
- no independence after diagonalizing `A`;
- no arbitrary-joint coarea `L^infinity` theorem;
- no dimension-free fiber supremum;
- no bounded support diameter;
- no fixed fragment count.

The approximation explicitly permits the number of rational intervals to diverge. It also keeps original-coordinate product structure throughout.

## 10. What this does and does not solve

Proved here:

1. the optimal full universal interval constant equals the optimal constant on a **countable** rational-generic bang-bang skeleton;
2. if the conjecture fails, a blow-up sequence exists entirely in that skeleton;
3. if a uniform skeleton bound is proved, it transports to all rough laws and degenerate target matrices with zero constant loss;
4. account04/B15 then gives the requested `C_0` density with the same constant.

Not proved here:

- any finite numerical upper bound on `C_Q`;
- the unrestricted universal QFORM theorem;
- a fixed bound on the number of input fragments;
- any target-uniform modulus of continuity.

The remaining mathematical task is now equivalent to showing that the countable sequence of rational-skeleton interval ratios in (6.1) is bounded by one universal constant. Any aggregate-curvature, grouped-bank, Fourier, or small-ball proof may therefore work on rational generic matrices and finite rational interval inputs without losing generality, provided its constant is independent of the matrix genericity gaps, interval locations, support diameter, and number of fragments.

## 11. Source discipline


Completed fixed-instance regularity source actually read: `math-open-problems@9b8bb7e84811978a2c46c7bb5ec50f2570dbc056`.

Designated completed partner actually applied: account04/B15 at `math-open-problems@7b2b0f54db9acbd23a5f69f715178ab666e22d8e`.

Live correction retained: `QFORM-NO-UNIFORM-FRAGMENT-COUNT-BATHTUB-v1`; this report makes no fixed-fragment assertion.

Repository transport was authenticated; no authenticated native mathematical receiver ingestion/use was verified, so execution remains `WITHOUT_VERIFIED_BRAIN`.
