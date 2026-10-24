Runtime model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — this is not GPT-6 at maximum, and I do not claim otherwise. PROB10-05 metric MOVED: `W_{1/4}: 213/2500 = 0.0852 -> 8483/100000 = 0.08483`; source lower endpoint `103/625 = 0.1648 -> 16517/100000 = 0.16517`.**

# PROB10-05 bounded research iteration — equicorrelation/probit trace envelope

**Status: PARTIAL / source target OPEN.** This run keeps the exact HARD7-05 parent target and proves the stricter source-relevant bound

\[
\boxed{\theta_{2,1/4}>\frac{16517}{100000}=0.16517}.\tag{0.1}
\]

Together with the source-valid upper bound `theta_{2,1/4} <= 1/4`, the current certified bracket is

\[
\boxed{\frac{16517}{100000}<\theta_{2,1/4}\le\frac14},
\qquad
\boxed{W_{1/4}=\frac{8483}{100000}=0.08483}.\tag{0.2}
\]

This is a continuous-path persistence conclusion. It does **not** infer the continuous event from a finite simulation or a discretely sampled path.

## 1. Consumed state, exact model, source existence convention, ownership

This execution read/recovered the controlling `operations/PROB10_2026-09-20.md`, root `POSTED.md`, `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`, the canonical claim `operations/claims/MOLCHAN-2025-THETA2H.md`, current repository claim/alias searches, and the newest HARD7-05 chain through commit

`4f7031479268b0fb4cd2ffebbc6f82483e3001b2`.

The refocus does **not** change the mathematical target or owner. `PROB10-05` is the continuation of the HARD7-05 claim, so no competing claim was overwritten and no target-handoff is required. The old HARD7-05 files remain immutable history.

The frozen process is standard centered fractional Brownian motion `B_H` with

\[
\mathbb E B_H(t)B_H(s)=\frac12\bigl(t^{2H}+s^{2H}-|t-s|^{2H}\bigr),
\]

at `H=1/4`, and

\[
I_H(t)=\int_0^t B_H(u)\,du.
\]

The source event is the one-sided continuous event at a fixed positive level; here the level is frozen at 1:

\[
P_H(T)=\Pr\{I_H(t)\le 1\ \forall\,0\le t\le T\}
       =T^{-\theta_{2,H}+o(1)}.
\tag{1.1}
\]

Molchan's current source is G. Molchan, *Persistence probabilities for fractionally integrated fractional Brownian noise*, arXiv:2509.10265, current repository-verified version v11 revised 4 July 2026. The source treats the persistence exponent `e(a,H)` as the exponent determining the power-law asymptotic on the parameter domain `a>0`, `0<H<1`, `a+H>1`; the present integrated-fBM case is `a=2`, so `H=1/4` lies inside that domain. The current arXiv metadata again describes `e(a,H)` as determining the power-law asymptotic and explicitly calls the `e(2,H)` values problematic. It also records the duality

\[
e(a,H)=e(a+2H-1,1-H),
\]

which refutes the old general guess `e(2,H)=H(1-H)`. This run does not try to prove that obsolete formula and does not claim its refutation as fleet work.

The current source bounds recovered earlier from the full v11 PDF, printed p. 3 / equation (3), give at `H=1/4`

\[
\frac18\le\theta_{2,1/4}\le\frac14.
\tag{1.2}
\]

A separate current existence reference is N. D. Feldheim, O. N. Feldheim and S. Mukherjee, *Persistence and ball exponents for Gaussian stationary processes*, CPAM 78 (2025), 1949--2000, DOI 10.1002/cpa.22255: under positive spectral density at the origin their stationary persistence exponent exists, with continuity results including dense sampling under additional hypotheses. This is supporting literature, not a replacement for Molchan's model convention.

### Fresh literature check, 20 September 2026

Fresh searches for `2509.10265`, `theta_{2,H}`, exact `H=1/4`, and integrated-fBM persistence found Molchan's current source; Feldheim--Feldheim--Mukherjee's stationary persistence theory; Abundo--Pirozzi (2023), whose fractional-integration exponent work is explicitly numerical; and Zhang (arXiv:2604.01701, 2026) on Chung-type LIL/small-ball behavior of integrated fractional processes. I found no later theorem giving the exact one-sided continuous-time `theta_{2,1/4}`. This is a bounded dated negative search, not a worldwide novelty certificate.

## 2. Continuity with HARD7-05: what survives and what is superseded

The early HARD7-05 reports that asserted exact values such as `theta_{2,1/4}=1/8` are **not** part of the incoming state. Commit `c96cff22b0bb20895ac9d1d92e5cbf4b4ad318cd` and its report retracted those consequences after identifying the orientation error in the exact comparator-rate input. The finite covariance identities from those reports survive only in the scope they actually proved.

After that correction the track built an independent covariance/operator route. The source lower endpoint advanced through the certified chain including `0.1406`, `0.142`, `0.14235`, `0.1427`, `0.143066`, `0.146611`, `0.148`, `3/20`, `8071/50000`, `41/250`, `0.1647`, and finally

\[
L_{1/4}=\frac{103}{625}=0.1648
\]

at `4f703147...`. The only incoming value used as the source-level baseline here is that newest one.

The surviving machinery needed in this run is:

1. a Lamperti/sampling/Slepian reduction at
   \[
   r=\frac78,\qquad s=\frac{24861}{25000},
   \]
   with the all-lag covariance domination already proved in HARD7-05;
2. the corresponding self-adjoint killed operator `K=K_{r,s}` with Perron eigenvalue `lambda_1` and the continuous-path implication
   \[
   \theta_{2,1/4}\ge
   \frac{-\log\lambda_1}{4\log(8/7)};
   \tag{2.1}
   \]
3. the exact degree-18 quasimode bounds
   \[
   \frac{9116948312}{10^{10}}<\mu<\frac{9116948313}{10^{10}},
   \qquad
   \varepsilon^2<\frac{47004495}{10^{11}},
   \tag{2.2}
   \]
   for normalized trial vector `f`, where
   \[
   \mu=\langle f,Kf\rangle,
   \qquad \varepsilon^2=\|(K-\mu)f\|_2^2;
   \]
4. the exact Gaussian four-cycle trace representation
   \[
   \operatorname{tr}(K^4)
   =\frac1{1-r^4}
     \Pr(V_0<0,V_1<0,V_2<0,V_3<0).
   \tag{2.3}
   \]

For the standardized four-cycle variables the exact correlations are

\[
\rho_{\rm adj}=a=\frac{168557580}{170952323},
\qquad
\rho_{\rm opp}=b=\frac{167065920}{170952323},
\qquad 0<b<a<1.
\tag{2.4}
\]

The immediately preceding run bounded the four-orthant by a three-coordinate projection and obtained `tr(K^4)<1.10273`. This run replaces that projection loss.

## 3. New mathematics first: three materially different attacks

The preceding HARD7-05 iteration used B1/B4/B25. This run changed the route.

### Attack A — B14/B18: symmetry compression to an equicorrelated one-factor problem — SUCCESS

Dominate only the two opposite covariances `b` by the adjacent value `a`, turning the cyclic Gaussian covariance into the equicorrelation matrix. This preserves all variances and increases every off-diagonal covariance, so Slepian converts the difficult cyclic four-orthant into a one-factor equicorrelated four-orthant. Then translate the latter into a one-dimensional probit moment. This is the route proved below.

### Attack B — exact quadrivariate orthant formula — NOT USED

A direct Plackett/Childs-type quadrivariate orthant formula should retain both `a` and `b` and can only be sharper than Attack A. But using it rigorously would require a new outward-rounded integral/special-function enclosure. Since Attack A already moves the source metric by a visible amount, creating that machinery in this run would violate the 90/10 research rule. No floating-point quadrature is used as a theorem.

### Attack C — continuous-time interpolation/modulus route — AUXILIARY PROGRESS, NO SOURCE METRIC MOVEMENT

A deterministic interpolation estimate is proved in Section 7. It clarifies exactly which direction of the current comparison is already continuous-time valid and what extra modulus control a future reverse discrete-to-continuous bound would require. It is not used to manufacture a source-level upper bound.

The idea checkpoint for Attack A was written **before** its checker at

`artifacts/prob10_2026-09-20/PROB10-05/2026-09-20T0000Z__equicorrelation_probit_trace_idea.md`

commit `c49bd4fc5da9d35803d1a2af20591d3dd4ae9f5b`.

## 4. Equicorrelation domination of the four-cycle

Let `V=(V_0,V_1,V_2,V_3)` be the standardized Gaussian vector in (2.3). Its covariance matrix has adjacent entries `a` and opposite entries `b<a`.

Let `G=(G_0,G_1,G_2,G_3)` be centered, unit variance and equicorrelated with

\[
\operatorname{Cov}(G_i,G_j)=a\qquad(i\ne j).
\tag{4.1}
\]

This is positive definite because `0<a<1` (eigenvalues `1-a` with multiplicity three and `1+3a`). Its off-diagonal covariances dominate those of `V`. Slepian's inequality, applied to the maximum at threshold zero, gives

\[
\Pr(V_i<0\ \forall i)
\le
\Pr(G_i<0\ \forall i).
\tag{4.2}
\]

Thus it suffices to bound the equicorrelated orthant.

Use the exact one-factor representation

\[
G_i=\sqrt a\,Z+\sqrt{1-a}\,E_i,
\tag{4.3}
\]

where `Z,E_0,...,E_3` are independent standard normals. Put

\[
c=\sqrt{\frac{a}{1-a}},
\qquad
U=\Phi(-cZ).
\tag{4.4}
\]

Conditioning on `Z` gives

\[
\Pr(G_i<0\ \forall i)=M_4:=\mathbb E U^4.
\tag{4.5}
\]

Because `Z` is symmetric, `U` has the same law as `1-U`, so `M_1=1/2` and

\[
M_3=\frac32M_2-\frac14.
\tag{4.6}
\]

The bivariate Gaussian sign formula gives

\[
M_2=\Pr(G_0<0,G_1<0)
=\frac14+\frac{\arcsin a}{2\pi}.
\tag{4.7}
\]

Set `Q=U(1-U)`. Then

\[
\mathbb E Q^2=M_2-2M_3+M_4
=M_4-2M_2+\frac12,
\]
so

\[
M_4=2M_2-\frac12+\mathbb E Q^2.
\tag{4.8}
\]

The remaining problem is now one-dimensional.

## 5. A pointwise probit-product inequality

### Lemma
For every real `x`,

\[
\boxed{\Phi(x)\Phi(-x)\le\frac14 e^{-x^2/2}}.
\tag{5.1}
\]

### Proof
By symmetry take `x>=0` and write `y=x/sqrt(2)`. Since

\[
4\Phi(x)\Phi(-x)=1-\operatorname{erf}(y)^2,
\]
(5.1) is equivalent to

\[
F(y):=\operatorname{erf}(y)^2+e^{-y^2}-1\ge0.
\tag{5.2}
\]

Now `F(0)=0` and `F(y)->0` as `y->infinity`. Differentiation gives

\[
F'(y)=2e^{-y^2}
\left[\frac{2}{\sqrt\pi}\operatorname{erf}(y)-y\right].
\tag{5.3}
\]

Let

\[
g(y)=\frac{2}{\sqrt\pi}\operatorname{erf}(y)-y.
\]
Then

\[
g'(y)=\frac4\pi e^{-y^2}-1,
\qquad
 g''(y)=-\frac{8y}{\pi}e^{-y^2}<0\quad(y>0).
\tag{5.4}
\]

Thus `g'` is strictly decreasing, starts positive and eventually becomes negative. Hence `g` first increases from `g(0)=0`, then strictly decreases to `-infinity`, and has exactly one positive zero. Equation (5.3) therefore shows that `F` first increases and then decreases. Since both endpoint limits are zero, `F(y)>=0` for every `y>=0`. This proves (5.1). `QED`

Apply (5.1) with `x=cZ`. Then

\[
Q^2
=\Phi(cZ)^2\Phi(-cZ)^2
\le\frac1{16}e^{-c^2Z^2}.
\]
For standard normal `Z`,

\[
\mathbb E e^{-c^2Z^2}=\frac1{\sqrt{1+2c^2}}
=\sqrt{\frac{1-a}{1+a}}.
\tag{5.5}
\]

Combining (4.7), (4.8), and (5.5) yields the explicit four-orthant bound

\[
\boxed{
\Pr(G_i<0\ \forall i)
\le
\frac{\arcsin a}{\pi}
+rac1{16}\sqrt{\frac{1-a}{1+a}}.
}
\tag{5.6}
\]

This is the key new inequality of the run.

## 6. Rigorous trace cap and Temple step

By (2.3), (4.2), and (5.6),

\[
\operatorname{tr}(K^4)
\le
\frac1{1-r^4}
\left[
\frac{\arcsin a}{\pi}
+rac1{16}\sqrt{\frac{1-a}{1+a}}
\right].
\tag{6.1}
\]

The exact checker encloses `pi` using Machin's formula, `arcsin(a)` using alternating rational `arctan` bounds, and the square root by integer-square-root bracketing. It certifies

\[
\boxed{\operatorname{tr}(K^4)<\frac{273011}{250000}=1.092044}.
\tag{6.2}
\]

The outward-rounded numerical value of the right side of (6.1) is less than `1.0920432931825665`; the proof is the rational enclosure, not this decimal.

Now set

\[
\theta_*:=\frac{16517}{100000},
\qquad
x:=\frac{915557}{10^6},
\qquad
\beta:=\frac{98743}{125000}.
\tag{6.3}
\]

The exact checker proves

\[
x^{25000}<r^{16517},
\]
which is exactly

\[
x<r^{4\theta_*}.
\tag{6.4}
\]

Assume for contradiction that `lambda_1 >= r^(4 theta_*)`. Then `lambda_1>x>mu`. From the fourth trace,

\[
\sum_{j\ge2}\lambda_j^4
\le\operatorname{tr}(K^4)-\lambda_1^4
<\frac{273011}{250000}-x^4
<\beta^4.
\tag{6.5}
\]

Hence every non-Perron spectral value satisfies `|lambda_j|<beta`. Since the exact inputs also give `mu>beta`, the one-sided Kato--Temple bound applies:

\[
(\lambda_1-\mu)(\mu-\beta)\le\varepsilon^2.
\tag{6.6}
\]

But the archived rational inequalities give

\[
(x-\mu_{\rm hi})(\mu_{\rm lo}-\beta)
-\varepsilon^2_{\rm hi}
>1.77\times10^{-7}>0,
\tag{6.7}
\]

contradicting (6.6). Therefore

\[
\lambda_1<r^{4\theta_*}.
\tag{6.8}
\]

Insert (6.8) into the already established continuous-path reduction (2.1):

\[
\theta_{2,1/4}
\ge\frac{-\log\lambda_1}{4\log(8/7)}
>\frac{-4\theta_*\log r}{4\log(8/7)}
=\theta_*.
\]

This proves (0.1).

### Executed exact finite core

Checker:

`artifacts/prob10_2026-09-20/PROB10-05/2026-09-20T0004Z__equicorrelation_probit_trace_exact_check.py`

creation commit `ee9d71ef7967ae14d48705efc49a0bf0a7c3c1e7`.

Archived executed output:

`artifacts/prob10_2026-09-20/PROB10-05/2026-09-20T0004Z__equicorrelation_probit_trace_exact_check.out`

creation commit `c0e9d1e1cde8879287bf64dbb1432917914fe82c`.

The run ended with

`ALL_EXACT_CHECKS_PASS = True`.

The finite checker is a **self-check**, not an independent audit.

## 7. Continuous-time interpolation estimate

The source event is continuous, so it is useful to record exactly what sampling does and does not prove. Let

\[
0=t_0<t_1<\cdots<t_N=T,
\qquad
\Delta=\max_j(t_{j+1}-t_j).
\]

Because `I_H'(t)=B_H(t)` pathwise for continuous fBM paths, for `t in [t_j,t_{j+1}]`,

\[
I_H(t)
=I_H(t_j)+\int_{t_j}^t B_H(u)\,du
\le I_H(t_j)+\Delta\sup_{0\le u\le T}|B_H(u)|.
\]

Therefore, for every `eta>0`,

\[
\boxed{
\{\max_j I_H(t_j)\le1-\eta,\ 
  \sup_{u\le T}|B_H(u)|\le\eta/\Delta\}
\subseteq
\{\sup_{t\le T}I_H(t)\le1\}
\subseteq
\{\max_j I_H(t_j)\le1\}.
}
\tag{7.1}
\]

This is a deterministic continuous-time interpolation sandwich, not simulation.

It can be quantified probabilistically. Let

\[
m_H=\mathbb E\sup_{0\le t\le1}|B_H(t)|<\infty.
\]

Self-similarity and Borell--TIS applied to the centered Gaussian family `{+B_H(t),-B_H(t):0<=t<=1}` give, for `u>=0`,

\[
\Pr\left\{\sup_{t\le T}|B_H(t)|>
T^H(m_H+u)\right\}
\le e^{-u^2/2}.
\tag{7.2}
\]

Hence (7.1) becomes a rigorous reverse-interpolation estimate if one chooses a mesh/margin with

\[
\eta\ge\Delta T^H(m_H+u).
\tag{7.3}
\]

This explains the asymmetry cleanly. For the **lower bound on the exponent** in this run, only the right-hand inclusion in (7.1) is needed: the continuous persistence probability is at most the sampled persistence probability, so no unproved modulus interpolation enters (0.1). To derive a new **upper bound on the exponent** from a discrete grid, the left-hand inclusion plus a scale choice satisfying (7.3) would be required. This run does not claim such an upper-bound improvement.

## 8. Before/after and mechanism progress

Source-level metric, with assumptions frozen:

\[
L_{\rm before}=\frac{103}{625}=0.1648,
\qquad
U=\frac14,
\qquad
W_{\rm before}=\frac{213}{2500}=0.0852,
\]

and now

\[
L_{\rm after}=\frac{16517}{100000}=0.16517,
\qquad
U=\frac14,
\qquad
W_{\rm after}=\frac{8483}{100000}=0.08483.
\]

Thus

\[
\boxed{L\text{ improves by }37/100000=0.00037},
\qquad
\boxed{W\text{ shrinks by }37/100000=0.00037}.
\tag{8.1}
\]

Separate mechanism progress:

- four-cycle trace cap: `1.10273 -> 1.092044`;
- no change to `r`, `s`, source process, continuous event, or degree-18 quasimode;
- new analytic ingredient: the probit-product bound (5.1);
- new continuous-time interpolation inequality: (7.1)--(7.3), auxiliary only.

No simulation, finite-size fit, or sampled-path event is labeled as the continuous theorem.

## 9. Remaining gap and next nonexhausted routes

The exact value of `theta_{2,1/4}` remains unknown, and the certified source gap is still

\[
\frac{8483}{100000}=0.08483.
\]

The present equicorrelation replacement discards the strict difference `a-b` in the two opposite cycle correlations, so it is not expected to be optimal. The most promising next route is to retain the exact cyclic pair `(a,b)` in a rigorously enclosed quadrivariate orthant formula, or to move to a higher trace while preserving the exact `a,b` geometry. A second route is to improve the quasimode/residual rather than the trace. A third is to use (7.1)--(7.3) to build a genuine reverse dense-sampling comparison and attack the source upper endpoint. These are distinct from simply tightening the same rational decimals.

No source closure or independent validation is claimed. Status remains **PARTIAL / OPEN**.