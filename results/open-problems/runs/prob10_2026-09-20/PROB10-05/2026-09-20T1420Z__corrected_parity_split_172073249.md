Runtime model/effort request: GPT-6 maximum. The platform exposes no authenticated model/effort telemetry to this run, so runtime model/effort is **UNVERIFIED**.

# PROB10-05 bounded substantive iteration — corrected four-cycle parity split

**Status: PARTIAL / source target OPEN / finite core self-certified / independent validation still required.** The exact persistence exponent is not determined. The obsolete formula `theta_{2,H}=H(1-H)` is not used and Molchan's refutation is prior work, not ours.

## 0. Valid before/after and an in-run correction

The newest relevant neighboring report was decisive:

`proofnet24/NM13-09/progress-persistence/runs/2026-09-20/2026-09-20T1312Z__corrected_mesh22_trace_17207285.md`

(blob `68b88f616c6569680d3eb81d67e2d7e2805bdfa2`). It shows that the recent PROB10 four-cycle calculations omitted the normalized cyclic AR variance factor

\[
G_0=\frac{1+r^4}{1-r^4}.
\]

Therefore the own-track caps `1.15053`, `1.13442` and the endpoints `0.172052`, `0.172096247...` are **not valid certified baselines**. Their immutable history is retained, but they are withdrawn from the source-model certificate chain. The valid incoming bound is the corrected peer result

\[
\theta_{2,1/4}>\frac{3441457}{20000000}=0.17207285.
\tag{0.1}
\]

This run first pursued the pre-correction normalization in the immutable checkpoint `2026-09-20T1342Z__hermite_ladder_idea.md` and checker `2026-09-20T1354Z__hermite100_exact_check.py`. After consuming the newer corrected peer report, that route was discarded rather than silently repaired or overwritten. **Failure count this run: 1 normalization-dependent route superseded.** The corrected idea was then frozen before new code in

`artifacts/prob10_2026-09-20/PROB10-05/2026-09-20T1402Z__corrected_cycle_parity_idea.md`.

The corrected route below proves the new repository candidate

\[
\boxed{\theta_{2,1/4}>\theta_*:=\frac{15664}{91031}
=0.17207324977205568\ldots .}
\tag{0.2}
\]

Thus the **valid** source-model candidate gap to the retained source upper endpoint `1/4` moves

\[
\frac{1558543}{20000000}=0.07792715
\quad\longrightarrow\quad
\boxed{\frac{28375}{364124}=0.07792675022794433\ldots},
\tag{0.3}
\]

an endpoint gain

\[
\theta_* - \frac{3441457}{20000000}
=\frac{727833}{1820620000000}
=3.9977205567\times10^{-7}.
\tag{0.4}
\]

The primary-literature bracket remains separately `1/8 <= theta_{2,1/4} <= 1/4`; (0.2) is a repository candidate pending independent validation.

## 1. Source statement, conventions, existence, literature, and ownership

Freeze centered standard fractional Brownian motion at `H=1/4`,

\[
\mathbb E[B_{1/4}(t)B_{1/4}(s)]
=\frac12\bigl(t^{1/2}+s^{1/2}-|t-s|^{1/2}\bigr),
\]

and ordinary integrated fBM

\[
I(t)=\int_0^t B_{1/4}(u)\,du.
\tag{1.1}
\]

The exact source event is continuous:

\[
p(T)=\Pr\{\sup_{0\le t\le T}I(t)\le1\}
=T^{-\theta_{2,1/4}+o(1)}.
\tag{1.2}
\]

The governing source remains G. Molchan, *Persistence probabilities for fractionally integrated fractional Brownian noise*, arXiv:2509.10265v11, revised 4 July 2026. Its Statement 1.2(a) gives existence and equality of the self-similar and Lamperti-dual persistence exponents in the parameter region containing `(alpha,H)=(2,1/4)`. The paper explicitly leaves the one-sided `alpha=2`, `H!=1/2` values unresolved and reports the old formula `theta_{2,H}=H(1-H)` refuted. At `H=1/4`, its displayed source bounds give

\[
\frac18\le\theta_{2,1/4}\le\frac14.
\tag{1.3}
\]

A bounded fresh literature check on 20 September 2026 rechecked Molchan v11 and newer adjacent work: Aurzada--Helmer, arXiv:2608.17463 (18 August 2026), on fractional Levy fields on manifolds; Molchan, arXiv:2608.26680 (27 August 2026), on multivariate-time fBM; and recent weighted-integrated fractional-process LIL/small-ball work. None of the retrieved results determines the present continuous one-sided integrated-fBM exponent at `H=1/4`. This is bounded negative evidence, not a worldwide novelty certificate.

Canonical claim ownership remains HARD7-05 through `operations/claims/MOLCHAN-2025-THETA2H.md` (blob `40b93171d1258596780a7746de1d96bd028a41d9`). The last pre-refocus HARD7-05 history remains linked at

`runs/hard7_2026-09-18/HARD7-05/2026-09-19T2250Z__triple_orthant_trace_164800.md`.

The refocus does not change the mathematical target or owner, so no ownership handoff is needed. No peer claim is overwritten.

## 2. Lamperti covariance comparison and the continuous direction

Direct integration gives `Var I(1)=2/5`, and `I` is self-similar of index `5/4`. Hence the unit-variance Lamperti dual is

\[
X(\tau)=\sqrt{\frac52}\,e^{-5\tau/4}I(e^\tau).
\tag{2.1}
\]

Writing `u=e^{-|t|/4}`, its covariance is

\[
R(u)=\frac{-2u^{10}+5u^6+5u^4+2(1-u^4)^{5/2}-2}{6u^5}.
\tag{2.2}
\]

Retain the corrected peer's comparator

\[
r=\frac{22}{25},\qquad
c=\frac{936901}{10^6},\qquad
s=\frac{936901}{940000},
\qquad c=s\frac{1+r}{2}.
\tag{2.3}
\]

For stationary standard Gaussian AR(1) states `(U_j)` with correlation `r` and iid standard Gaussian `(E_j)` independent of them, define

\[
Y_j=\frac{U_j+U_{j-1}}{\sqrt{2(1+r)}},\qquad
Z_j=\sqrt{s}\,Y_j+\sqrt{1-s}\,E_j.
\tag{2.4}
\]

Then

\[
\operatorname{Cov}(Z_0,Z_k)=c r^{k-1},\qquad k\ge1.
\tag{2.5}
\]

### Proposition 2.1 — all-lag comparison
For every integer `k>=1`,

\[
R(r^k)<c r^{k-1}.
\tag{2.6}
\]

### Proof
For `k=1,2`, substitute `u=r^k`, rearrange (2.2) to isolate the positive radical, and square. The exact checker obtains positive rational squared margins with decimal displays

`1.334296986263307e-4`, `2.3302146180526656e-7`.

For `k>=3`, Taylor's theorem gives

\[
(1-z)^{5/2}\le1-\frac52z+\frac{15}{8}z^2,
\]

hence

\[
R(u)\le\frac56u+\frac58u^3-\frac13u^5.
\tag{2.7}
\]

After division by `r^{k-1}`, the resulting polynomial quotient is increasing over `u^2<=r^6`, so `k=3` is worst. The exact endpoint margin is

`c-r(5/6+(5/8)r^6-(1/3)r^12)=0.011408957976493094...>0`.
QED.

Set the Lamperti mesh

\[
\Delta=-4\log r=4\log(25/22).
\tag{2.8}
\]

Continuity gives the literal inclusion

\[
\{X(t)<0\ \forall 0\le t\le n\Delta\}
\subseteq
\{X(j\Delta)<0,\ j=0,\dots,n\}.
\tag{2.9}
\]

Thus there is **no interpolation loss in the direction used for the lower exponent bound**. Slepian plus (2.6) bounds the sampled source survival by the comparator survival. If `lambda_1` is the Perron eigenvalue of the comparator's self-adjoint killed transfer operator, then

\[
\theta_{2,1/4}\ge\frac{-\log\lambda_1}{4\log(25/22)}.
\tag{2.10}
\]

A discrete path estimate is not used as a continuous lower-probability estimate; (2.9) is only the upper-probability direction needed for (2.10).

## 3. Correct cycle scale and inherited finite-operator data

For the transfer operator

\[
(Kf)(x)=\int p_r(x,dy)\,
\Phi\!\left(-\sqrt{\frac{s}{1-s}}\,
\frac{x+y}{\sqrt{2(1+r)}}\right)f(y),
\tag{3.1}
\]

retain the direct same-operator degree-56 certificate

\[
0.9155053441<\mu<0.9155053442,
\qquad
\varepsilon^2:=\|(K-\mu)f\|_2^2<2.70154\times10^{-5}.
\tag{3.2}
\]

These one-/two-step stationary Gaussian moment bounds are unaffected by the cyclic trace normalization error: they were computed directly under the stationary one-step and two-step laws, not under the normalized four-cycle trace measure. This is explicitly checked in the corrected neighboring report and checker.

For `tr K^4`, however, the normalized cyclic AR measure has vertex variance

\[
G_0=\frac{1+r^4}{1-r^4}
=\frac{624881}{156369}=3.9961948979\ldots .
\tag{3.3}
\]

With

\[
a=\frac{r+r^3}{1+r^4},\qquad b=\frac{2r^2}{1+r^4},
\]

the unit-scale adjacent/opposite formulas must first be multiplied by `G_0` before adding the independent softening noise. This yields the corrected correlations

\[
\rho_a=0.9911694036569575\ldots,
\qquad
\rho_o=0.9831256483522571\ldots .
\tag{3.4}
\]

Define

\[
q=\frac{2\rho_a}{1+\rho_o}
=0.9996032318784258\ldots,
\qquad
A=\frac{1+\rho_o}{1-\rho_o}
=117.5230722786\ldots .
\tag{3.5}
\]

The corrected opposite-pair reduction from the peer report gives

\[
\operatorname{tr}K^4=\frac{p(q)}{1-r^4},
\qquad
p(q)=\mathbb E[g_A(X)g_A(Y)],
\tag{3.6}
\]

where `(X,Y)` are standard Gaussian with correlation `q` and

\[
g_A(z)=\mathbf 1_{\{z>0\}}\bigl(2\Phi(\sqrt A\,z)-1\bigr).
\tag{3.7}
\]

## 4. New mathematics: exact odd-sector summation and O(K) even recurrence

Write probabilists' Hermite polynomials as `He_n` and set

\[
m=\mathbb E g_A(X),\qquad
d_n=\mathbb E[g_A(X)He_n(X)].
\]

Mehler's identity gives

\[
p(q)=m^2+\sum_{n\ge1}q^n\frac{d_n^2}{n!}.
\tag{4.1}
\]

The corrected peer checker truncated this full series at `M=500` and multiplied all unresolved Hermite energy by `q^{501}`. Here we exploit parity and the half-line support of `g_A`.

### Lemma 4.1 — exact parity masses
Let

\[
E_2=\mathbb E[g_A(X)^2].
\]

Then

\[
\sum_{n\text{ odd}}\frac{d_n^2}{n!}=\frac{E_2}{2},
\qquad
\sum_{\substack{n\ge2\\n\text{ even}}}\frac{d_n^2}{n!}
=\frac{E_2}{2}-m^2.
\tag{4.2}
\]

### Proof
Since `g_A(x)g_A(-x)=0` pointwise,

\[
0=\mathbb E[g_A(X)g_A(-X)]
=m^2+\sum_{n\ge1}(-1)^n\frac{d_n^2}{n!}.
\]

Also Parseval gives

\[
E_2=m^2+\sum_{n\ge1}\frac{d_n^2}{n!}.
\]

Adding and subtracting these identities gives (4.2). QED.

The same orthant integrals used by the corrected worker give

\[
m=\frac1\pi\arctan\sqrt A,
\qquad
E_2=\frac1\pi\arctan\frac{A}{\sqrt{1+2A}}.
\tag{4.3}
\]

### Lemma 4.2 — full odd sector in closed form
Put

\[
h=1+A,\qquad a_0=\frac{A}{1+A}.
\]

Then

\[
\boxed{
\sum_{j\ge0}q^{2j+1}\frac{d_{2j+1}^2}{(2j+1)!}
=\frac{1}{2\pi}\arcsin(q a_0).}
\tag{4.4}
\]

### Proof
A single Gaussian integration by parts gives, for `n>=1`,

\[
d_n=\frac{\sqrt A}{\pi}I_{n-1},
\qquad
I_k=\int_0^\infty He_k(x)e^{-h x^2/2}\,dx.
\tag{4.5}
\]

The generating function of the even `I_k` is elementary, or equivalently repeated integration gives

\[
I_{2j}=\sqrt{\frac{\pi}{2h}}\,
\frac{(2j)!}{j!}\left(-\frac{a_0}{2}\right)^j.
\tag{4.6}
\]

Substituting (4.6) into the odd part of (4.1) gives

\[
\frac{Aq}{2\pi h}
\sum_{j\ge0}\frac{\binom{2j}{j}}{4^j(2j+1)}(q^2a_0^2)^j.
\]

Using

\[
\sum_{j\ge0}\frac{\binom{2j}{j}}{4^j(2j+1)}z^{2j}
=\frac{\arcsin z}{z}
\]

and `A/(ha_0)=1` proves (4.4). QED.

### Lemma 4.3 — O(K) exact recurrence for the even sector
Let `J_j=I_{2j-1}`. Then

\[
J_j=(-1)^{j-1}\frac{(2j-3)!!}{h}P_j,
\]

where

\[
P_1=1,
\qquad
P_j=1+\frac{2j-2}{2j-3}a_0P_{j-1}.
\tag{4.7}
\]

Consequently, with

\[
D_1=\frac12,
\qquad
D_j=D_{j-1}\frac{(2j-3)^2}{(2j)(2j-1)},
\tag{4.8}
\]

the even Hermite mass is

\[
w_j:=\frac{d_{2j}^2}{(2j)!}
=\frac{A}{\pi^2h^2}D_jP_j^2.
\tag{4.9}
\]

### Proof
Differentiate `He_{n-1}(x)e^{-hx^2/2}` and integrate from zero to infinity. Using `He_n=xHe_{n-1}-(n-1)He_{n-2}` gives

\[
I_n=\frac{He_{n-1}(0)}{h}-(n-1)a_0 I_{n-2}.
\tag{4.10}
\]

For `n=2j-1`, `He_{2j-2}(0)=(-1)^{j-1}(2j-3)!!`; factoring this term yields (4.7). Squaring (4.5) and simplifying the double-factorial ratio gives (4.8)-(4.9). QED.

### Corollary 4.4 — finite rigorous trace upper bound
For any `K>=1`, positivity of the Hermite energies and (4.2) imply

\[
\begin{aligned}
p(q)\le{}&m^2+\frac{\arcsin(q a_0)}{2\pi}
+\sum_{j=1}^Kq^{2j}w_j\\
&+q^{2K+2}\left(\frac{E_2}{2}-m^2-\sum_{j=1}^K w_j\right).
\end{aligned}
\tag{4.11}
\]

The checker evaluates (4.11) at `K=1000` with outward rational bounds for `pi`, square roots, `atan`, and `asin`. It certifies

\[
p(q)<0.45775980172253834,
\]

and therefore

\[
\boxed{\operatorname{tr}K^4<\frac{1143529}{10^6}=1.143529.}
\tag{4.12}
\]

The exact outward trace value displayed by the checker is `1.1435285929299703`, leaving a positive cap margin `4.0707002960e-7`. The computed first 1000 even modes leave positive even Parseval mass `3.84101341216e-5`; no simulation is used in (4.12).

## 5. Kato--Temple synthesis

Set

\[
\theta_*:=\frac{15664}{91031},\qquad
x:=\frac{91577295}{10^8},\qquad
\beta:=\frac{81454563}{10^8}.
\tag{5.1}
\]

The exact positive-atanh-series comparison proves

\[
x<r^{4\theta_*}.
\tag{5.2}
\]

Assume for contradiction that `lambda_1>=r^{4 theta_*}>x`. From (4.12),

\[
\sum_{j\ge2}\lambda_j^4
<\frac{1143529}{10^6}-x^4.
\]

The checker proves

\[
\beta^4-\left(\frac{1143529}{10^6}-x^4\right)>0
\tag{5.3}
\]

with exact positive rational sign and decimal margin `2.8837863948e-9`. Hence every non-Perron spectral point lies in algebraic order below `beta`.

Since `mu>beta`, the spectral-measure Kato--Temple inequality gives

\[
\lambda_1\le\mu+\frac{\varepsilon^2}{\mu-\beta}.
\tag{5.4}
\]

Using only the outward data (3.2), the exact checker proves

\[
(x-\mu_+)(\mu_- -\beta)-\varepsilon_+^2>0,
\tag{5.5}
\]

with decimal margin `2.00505950178e-9`. Thus the right side of (5.4) is `<x`, contradicting the assumption. Therefore

\[
\lambda_1<r^{4\theta_*}.
\]

Substitution into (2.10) proves (0.2). QED.

## 6. A rigorous continuous-time interpolation estimate, and why it does not move the upper endpoint

The lower-endpoint proof needs only the zero-loss inclusion (2.9). For the opposite direction, the following finite-horizon estimate is rigorous and records exactly what remains missing.

Differentiate (2.1):

\[
X'(\tau)=\sqrt{\frac52}e^{-5\tau/4}
\left(e^\tau B_{1/4}(e^\tau)-\frac54 I(e^\tau)\right).
\tag{6.1}
\]

At `tau=0`,

\[
\operatorname{Var}I(1)=\frac25,
\qquad
\operatorname{Cov}(B_{1/4}(1),I(1))=\frac12,
\]

so stationarity gives the exact derivative variance

\[
\boxed{\operatorname{Var}X'(\tau)=\frac{15}{16}.}
\tag{6.2}
\]

Let `L>0`, mesh `delta>0`, `N=ceil(L/delta)`, and margin `eta>0`. Deterministically,

\[
\left\{\max_{0\le j\le N}X(j\delta)\le-\eta\right\}
\cap
\left\{\sup_{0\le t\le L}|X'(t)|\le\eta/\delta\right\}
\subseteq
\left\{\sup_{0\le t\le L}X(t)\le0\right\}.
\tag{6.3}
\]

Hence

\[
\Pr\{\sup_{[0,L]}X\le0\}
\ge
\Pr\{\max_jX(j\delta)\le-\eta\}
-\Pr\{\sup_{[0,L]}|X'|>\eta/\delta\}.
\tag{6.4}
\]

Let `M_1=E sup_{0<=t<=1}|X'(t)|<infinity`. Applying Borell--TIS to the signed derivative process on each unit block and union-bounding gives, for `u>0`,

\[
\Pr\{\sup_{[0,L]}|X'|>M_1+u\}
\le(\lceil L\rceil+1)\exp\left(-\frac{8u^2}{15}\right).
\tag{6.5}
\]

Thus (6.4)-(6.5) are a genuine continuous-time interpolation estimate. They still do **not** provide a source upper-exponent improvement: one needs a uniform lower bound for the negative-margin grid event, jointly with the shrinking-mesh/modulus requirement, at only subexponential cost. That conditional margin problem remains OPEN. No discretely sampled path is promoted to a continuous persistence bound.

## 7. Three attacks compared

1. **Corrected parity-split four-cycle trace — SUCCESS this run.** It consumes the peer's normalization repair, exactly sums the full odd Hermite sector, replaces the O(M^2)-style raw coefficient evaluation by an O(K) even recurrence, and moves the valid lower endpoint by `3.9977e-7`.

2. **Higher-degree same-operator Perron quasimode — NONEXHAUSTED.** The inherited residual `2.70154e-5` is now the larger controllable bottleneck. A degree >56 witness with full one-/two-step recertification is the highest-leverage next spectral attack.

3. **Reverse continuous interpolation — PARTIAL mechanism only.** Equations (6.3)-(6.5) are rigorous, but the long-survival margin cost is not controlled; no upper endpoint moves.

Because the valid source metric moved after an obstruction-triggered within-problem method correction, the unchanged-run counter resets rather than rotating away from PROB10-05.

## 8. Consumed updates, tests actually run, and artifact ledger

Consumed current state:

- `operations/PROB10_2026-09-20.md`;
- root `POSTED.md`;
- `operations/claims/MOLCHAN-2025-THETA2H.md`, blob `40b93171d1258596780a7746de1d96bd028a41d9`;
- prior own report `runs/prob10_2026-09-20/PROB10-05/2026-09-20T1304Z__even_block_hgr_172096247.md`, retained as history but its endpoint withdrawn after the scale correction;
- corrected peer report `proofnet24/NM13-09/progress-persistence/runs/2026-09-20/2026-09-20T1312Z__corrected_mesh22_trace_17207285.md`, blob `68b88f616c6569680d3eb81d67e2d7e2805bdfa2`;
- corrected peer checker blob `59751c663a495f9878f03e0158371ac503969688` and output blob `05349bddf015df1004cbb42b273e3b43e32d308f`;
- Molchan arXiv:2509.10265v11 full relevant statements/proof and bounded newer-literature search.

Idea-before-code artifacts:

- superseded wrong-scale checkpoint: `artifacts/prob10_2026-09-20/PROB10-05/2026-09-20T1342Z__hermite_ladder_idea.md`;
- corrected checkpoint: `artifacts/prob10_2026-09-20/PROB10-05/2026-09-20T1402Z__corrected_cycle_parity_idea.md`.

Authoritative corrected finite checker and archived executed output:

- `artifacts/prob10_2026-09-20/PROB10-05/2026-09-20T1412Z__corrected_parity_exact_check.py`;
- `artifacts/prob10_2026-09-20/PROB10-05/2026-09-20T1412Z__corrected_parity_exact_check.out`.

Tests actually run locally before upload:

- `python3 2026-09-20T1412Z__corrected_parity_exact_check.py`;
- `python3 -m py_compile` on the checker;
- exact rational all-lag covariance signs;
- outward `pi/sqrt/atan/asin` interval signs;
- exact parity-tail positivity;
- corrected trace cap;
- trace-separation and Kato--Temple signs;
- positive atanh log comparison.

The archived output ends

`ALL_EXACT_CHECKS_PASS = True`.

No Monte Carlo or discretely sampled-path experiment is used as theorem evidence. No schedule state, email, Drive item, public posting, or peer claim was modified.

## 9. Remaining gap and next target

The exact exponent remains **UNKNOWN**. The source-valid upper endpoint remains `1/4`, and the current self-certified repository candidate is

\[
\boxed{
\frac{15664}{91031}<\theta_{2,1/4}\le\frac14,
\qquad
W_{1/4}<\frac{28375}{364124}=0.07792675022794433\ldots .}
\]

Independent validation is still required before promotion beyond `PARTIAL / OPEN`. The next highest-leverage nonduplicating step is a new degree >56 Perron quasimode for the **same corrected `r=22/25` operator**, with complete direct one-/two-step moment recertification; further parity summation alone has diminishing leverage.