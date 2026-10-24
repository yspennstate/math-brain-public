Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum.**

# PROB10-04 — entropy stabilization pays arbitrary inner rescue-aggregate drift

This note is a theorem-level continuation of the already-proved iid-priority one-rescue compiler.  It does **not** certify a new random-3-SAT threshold endpoint.  Its purpose is to remove the principal inner-optimization failure in the preceding six-scalar conditional dual: the adversary can no longer erase the rescue correction for free by sending `Q`, `B`, or `E` to zero.

## 1. Setup

Fix the Díaz light cutoff `M`, the degree masses `\widehat\delta_{i,j}`, syntactic clause masses `\widehat\gamma_k`, and a copy macrostate

\[
u=\ell_{ps},\qquad v=\ell_{ns1},\qquad w=\ell_{ns2},
\qquad N=\lambda_n-v-w.
\]

For the theorem first assume `u,v,N>0`; the zero-mass boundary is obtained by continuity, with the rescue term set to zero whenever its corresponding source pool is empty.

Write

\[
\delta_i=\widehat\delta_{i,1},\qquad
D_1=\sum_{i=1}^M\delta_i,
\]

and for a feasible type

\[
E=\sum_i f_{i,1,1},\qquad
Q=Q_{safe},\qquad B=B_{can}.
\]

Thus `0<=E<=v`, `0<=Q<=u`, `0<=B<=N`.  The inherited iid-priority rescue factor has exponential rate

\[
R(x)=\prod_{i=1}^M
\left(1-\frac12\frac BN\left(\frac Qu\right)^i\frac Ev\right)^{t_i},
\qquad t_i=t_{i,1},
\tag{1.1}
\]

where `t_i+f_i=delta_i` and `f_i=f_{i,1,1}`.

Fix arbitrary positive source multipliers

\[
\nu=(\nu_{ps},\nu_{ns1},\nu_{ns2}),
\qquad
\mu=(\mu_{ps},\mu_{ns1},\mu_{ns2}).
\]

Let `D_0(u,v,w;nu,mu)` denote the ordinary **unrescued conditional Díaz dual** obtained by applying the source log-sum inequalities while keeping `(u,v,w)` fixed:

\[
\begin{aligned}
D_0=\;&C_\ell(u,v,w)+h_{ps}\log\nu_{ps}
+\sum_{i,j}\widehat\delta_{i,j}
 \log\frac{\Psi_{i,j}(\nu)}{\widehat\delta_{i,j}}\\
&+h_{ns}\log\frac{\nu_{ns1}+\nu_{ns2}}{h_{ns}}
+\sum_{k=0}^3\widehat\gamma_k
 \log\frac{\Psi_k(\mu)}{\widehat\gamma_k}\\
&-u\log(\nu_{ps}\mu_{ps})
-v\log(\nu_{ns1}\mu_{ns1})
-w\log(\nu_{ns2}\mu_{ns2}),
\end{aligned}
\tag{1.2}
\]

with zero fixed masses omitted.  Here `Psi_{i,j}` and `Psi_k` are exactly the source partitions.  Because `(u,v,w)` are fixed, the positive copy-entropy term `C_ell` is a constant and the wrong-curvature obstruction isolated in run 9 is absent.

## 2. Gibbs reference aggregates

For `j=1`,

\[
\Psi_{i,1}=\nu_{ps}^i+\nu_{ns1}.
\]

Let

\[
p_i^*=\frac{\nu_{ns1}}{\nu_{ps}^i+\nu_{ns1}},
\qquad
E_*=\sum_i\delta_i p_i^*.
\tag{2.1}
\]

For an extended clause type `alpha=(ps,ns,pu,nu)` define

\[
b(\alpha)=\mathbf1\{ps=0,ns=1,nu\ge1\},
\tag{2.2}
\]

and

\[
q(\alpha)=ps\,\mathbf1\{ps+ns\ge2\}.
\tag{2.3}
\]

For each syntactic positive-literal count `k=ps+pu`, let

\[
a_\alpha=\frac{2}{w(\alpha)!}
\mu_{ps}^{ps}\mu_{ns1}^{ns1(\alpha)}\mu_{ns2}^{ns2(\alpha)},
\qquad
r_{k,\alpha}=\frac{a_\alpha}{\Psi_k(\mu)}.
\tag{2.4}
\]

Then define the Gibbs clause aggregates

\[
B_*=\sum_k\widehat\gamma_k\sum_{\alpha:p(\alpha)=k}
r_{k,\alpha}b(\alpha),
\tag{2.5}
\]

\[
Q_*=\sum_k\widehat\gamma_k\sum_{\alpha:p(\alpha)=k}
r_{k,\alpha}q(\alpha).
\tag{2.6}
\]

The exact within-`k` ranges are

\[
\operatorname{range}_k b=(1,1,0,0),
\qquad
\operatorname{range}_k q=(0,1,2,3),
\tag{2.7}
\]

for `k=0,1,2,3`.  Hence put

\[
G_B=\widehat\gamma_0+\widehat\gamma_1,
\qquad
G_Q=\widehat\gamma_1+4\widehat\gamma_2+9\widehat\gamma_3.
\tag{2.8}
\]

## 3. Exact KL remainder for the log-sum inequalities

The source proof uses

\[
\sum_r x_r\log\frac{a_r}{x_r}
\le X\log\frac{\sum_r a_r}{X}.
\]

The difference between the right and left sides is exactly

\[
X D_{KL}(p\|r),
\qquad p_r=x_r/X,
\quad r_r=a_r/\sum_s a_s.
\tag{3.1}
\]

Therefore the ordinary conditional source dual is not merely an upper bound: after dropping only nonnegative remainders from blocks irrelevant below,

\[
\log F(x)
\le D_0-K_{var}-K_{clause},
\tag{3.2}
\]

where

\[
K_{var}=\sum_i\delta_i
D_{KL}\!\left(
\left(1-\frac{f_i}{\delta_i},\frac{f_i}{\delta_i}\right)
\Big\|
(1-p_i^*,p_i^*)
\right),
\tag{3.3}
\]

and

\[
K_{clause}=\sum_k\widehat\gamma_k D_{KL}(p_k\|r_k).
\tag{3.4}
\]

All logarithms are natural.

## 4. Three aggregate stability inequalities

### Lemma 4.1 — the leaf aggregate

\[
\boxed{K_{var}\ge \frac{2(E-E_*)^2}{D_1}.}
\tag{4.1}
\]

**Proof.** Pinsker with natural logarithms gives, for each Bernoulli block,

\[
D_{KL}(p\|r)\ge2|p-r|^2.
\]

Hence

\[
K_{var}\ge2\sum_i\delta_i
\left(\frac{f_i}{\delta_i}-p_i^*\right)^2.
\]

Cauchy--Schwarz yields

\[
\sum_i\delta_i z_i^2\ge
\frac{(\sum_i\delta_i z_i)^2}{\sum_i\delta_i},
\]

and `sum delta_i z_i=E-E_*`. QED.

### Lemma 4.2 — simultaneous blocker and safe-slot aggregates

\[
\boxed{
K_{clause}
\ge \frac{(B-B_*)^2}{G_B}
+\frac{(Q-Q_*)^2}{G_Q}.
}
\tag{4.2}
\]

**Proof.** Split each clause KL term into two equal halves.  Pinsker gives

\[
\frac12\widehat\gamma_kD_{KL}(p_k\|r_k)
\ge \widehat\gamma_k\operatorname{TV}(p_k,r_k)^2.
\tag{4.3}
\]

If a statistic `h` has range `R_k` in block `k`, then

\[
|\Delta H_k|
=\widehat\gamma_k|E_{p_k}h-E_{r_k}h|
\le\widehat\gamma_kR_k\operatorname{TV}(p_k,r_k).
\]

Thus the half-KL is at least

\[
\frac{\Delta H_k^2}{\widehat\gamma_kR_k^2}
\]

whenever `R_k>0`.  Summing and applying Cauchy in the form

\[
\sum_k\frac{x_k^2}{a_k}\ge
\frac{(\sum_kx_k)^2}{\sum_ka_k}
\]

gives the `B` bound from one half using ranges `(1,1,0,0)` and the `Q` bound from the other half using `(0,1,2,3)`.  Adding them proves (4.2). QED.

The finite enumeration of the 16 admissible 3-clause types and both range vectors is executed in the companion diagnostic.

## 5. Fractional-knapsack lower envelope for the true centers

For `0<=s<=1` and `0<=E<=D_1`, define

\[
A_{min}(s,E)=
\min\left\{
\sum_{i=1}^M(\delta_i-f_i)s^i:
0\le f_i\le\delta_i,\ \sum_i f_i=E
\right\}.
\tag{5.1}
\]

### Lemma 5.1 — exact greedy formula

The minimizer in (5.1) places false mass into degree classes in the order

\[
i=1,2,\ldots,M.
\tag{5.2}
\]

Equivalently, if `r` is the unique index such that

\[
\sum_{i<r}\delta_i\le E\le\sum_{i\le r}\delta_i,
\]

then

\[
\boxed{
A_{min}(s,E)=
\left(\sum_{i>r}\delta_i s^i\right)
+\left(\delta_r-E+\sum_{i<r}\delta_i\right)s^r.
}
\tag{5.3}
\]

Moreover `A_min` is nondecreasing in `s` and nonincreasing in `E`.

**Proof.** Minimizing the true-center sum is equivalent to maximizing `sum f_i s^i`.  Since `s^i` is nonincreasing in `i`, the standard exchange argument says that if `i<j`, `f_i<delta_i`, and `f_j>0`, moving any common admissible mass from `j` to `i` cannot decrease the objective.  Iteration gives the greedy form.  Formula (5.3) follows.  The monotonicities follow either directly from (5.1), viewed as a minimum of nondecreasing functions of `s`, and from the greedy form in `E`, or by the same exchange argument. QED.

## 6. Main theorem — entropy-stabilized rescue defect

### Theorem 6.1

For every feasible type at the fixed copy macrostate and every positive multipliers `nu,mu`, the inherited rescued exponential objective satisfies

\[
\boxed{
\log F_R(x)
\le
D_0(u,v,w;\nu,\mu)-\mathcal P(Q,B,E),
}
\tag{6.1}
\]

where

\[
\boxed{
\begin{aligned}
\mathcal P(Q,B,E)=\;&
\frac{2(E-E_*)^2}{D_1}
+\frac{(B-B_*)^2}{G_B}
+\frac{(Q-Q_*)^2}{G_Q}\\
&+\frac{BE}{2Nv}
A_{min}\!\left(\frac Qu,E\right).
\end{aligned}}
\tag{6.2}
\]

On a zero-mass boundary the final term is defined by the continuous convention inherited from the rescue factor; in particular it is zero whenever `B=0`, `E=0`, or `Q=0`.

**Proof.** Combine (3.2), Lemma 4.1, and Lemma 4.2.  It remains only to control the rescue factor.  Put

\[
x_i=\frac12\frac BN\left(\frac Qu\right)^i\frac Ev.
\]

The inherited construction has `0<=x_i<=1/2`, and `log(1-x)<=-x`. Therefore

\[
\log R(x)
\le-\frac{BE}{2Nv}
\sum_i t_i\left(\frac Qu\right)^i.
\tag{6.3}
\]

Because `t_i=delta_i-f_i` and `sum f_i=E`, Lemma 5.1 gives

\[
\sum_i t_i(Q/u)^i\ge A_{min}(Q/u,E).
\tag{6.4}
\]

Substitution into (3.2) proves (6.1)--(6.2). QED.

### Corollary 6.2 — aggregate collapse has a strictly positive price

Suppose

\[
B_*>0,\quad Q_*>0,\quad 0<E_*<D_1,
\quad u,v,N>0.
\]

Then over the compact feasible box

\[
0\le B\le N,\quad 0\le Q\le u,\quad0\le E\le\min(v,D_1),
\]

\[
\boxed{\inf\mathcal P(Q,B,E)>0.}
\tag{6.5}
\]

Indeed the three quadratic terms vanish simultaneously only at `(B_*,Q_*,E_*)`, where the rescue term is strictly positive.  Continuity and compactness then give (6.5).

Thus the adversary in run 9's six-scalar relaxation cannot turn the rescue correction off for free.  This is the main mathematical advance of the present run.

## 7. Explicit four-case lower bound

For practical certification choose radii

\[
0<r_B,r_Q,r_E<1,
\qquad (1+r_E)E_*<D_1.
\]

If any of

\[
|B-B_*|\ge r_BB_*,\quad
|Q-Q_*|\ge r_QQ_*,\quad
|E-E_*|\ge r_EE_*
\]

holds, one quadratic term pays respectively

\[
L_B=\frac{r_B^2B_*^2}{G_B},\qquad
L_Q=\frac{r_Q^2Q_*^2}{G_Q},\qquad
L_E=\frac{2r_E^2E_*^2}{D_1}.
\tag{7.1}
\]

Otherwise monotonicity of `A_min` gives

\[
L_R=
\frac{(1-r_B)B_*(1-r_E)E_*}{2Nv}
A_{min}\!\left(\frac{(1-r_Q)Q_*}{u},(1+r_E)E_*\right).
\tag{7.2}
\]

Therefore

\[
\boxed{
\inf\mathcal P
\ge\min\{L_B,L_Q,L_E,L_R\}.
}
\tag{7.3}
\]

This converts the qualitative compactness statement into a directly interval-certifiable scalar defect.

## 8. Separate deterministic clause-capacity floor

A different attack in this run gives an exact but insufficient structural constraint.  Let `gamma_b=sum_k hat_gamma_k` be the core clause density.  A `ps` copy is unsafe exactly when it is the sole satisfied literal of its clause.  Hence the number of singleton-`ps` clauses is `u-Q`; the number of singleton negative-satisfied blockers is `v`.  The remaining

\[
R=\gamma_b-(u-Q)-v
\]

clauses have two or three satisfied literals, and their satisfied-copy count is `Q+w`.  Thus

\[
Q+w\le3R,
\]

which rearranges to

\[
\boxed{
Q\ge \frac{[3u+3v+w-3\gamma_b]_+}{2}.
}
\tag{8.1}
\]

At the rounded source saddle this gives `Q>=3.4560642...`, i.e. `Q/u>=0.5901075...`.  It is useful for future outer boxes, but it does not solve the aggregate-collapse problem because no analogous positive feasibility floor for `B` holds globally.

## 9. Rounded-source diagnostic only

Using the rounded multipliers printed by Díaz et al. and the same source saddle formulas used in preceding PROB10-04 diagnostics gives approximately

\[
B_*=0.4578196811,\qquad
Q_*=4.3807111082,\qquad
E_*=0.001116323755,
\]

\[
D_1=0.01615197730,
\quad G_B=1.5276072859,
\quad G_Q=18.0512009826.
\]

Choose the simple radii

\[
r_B=0.0016,\qquad r_Q=0.0006,\qquad r_E=0.05.
\]

The executed companion diagnostic gives

\[
L_B=3.51250669925\times10^{-7},
\]

\[
L_Q=3.82723938403\times10^{-7},
\]

\[
L_E=3.85766616189\times10^{-7},
\]

and

\[
L_R=2.94688866148\times10^{-7}.
\]

Hence, **for the rounded-source surrogate only**, the complete inner reallocation of `Q,B,E` pays at least

\[
\boxed{2.94688866148\times10^{-7}.}
\tag{9.1}
\]

This is about `84.20` times the source's printed rounded final log margin and retains about `83.89%` of run 8's fixed-outer scalarized rescue correction.  The companion output explicitly labels these as high-precision rounded-multiplier diagnostics, not outward intervals and not a new threshold endpoint.

## 10. What remains

The source metric is still the verified external bracket `[3.52,4.4898]`.  The present theorem pays **all inner `Q,B,E` drift at each fixed copy macrostate**, but the three copy masses `(u,v,w)` can still move.  The next full-scope obligation is therefore sharply reduced:

> certify the outer three-dimensional `(u,v,w)` maximization, with multipliers chosen boxwise if needed, and show a negative uniform log margin at some `alpha<4.4898`.

A safe implementation can combine (7.3), the deterministic floor (8.1), and the source's existing three-dimensional copy-count polytope.  Until that outer interval calculation is done, status remains **PARTIAL / source OPEN**.