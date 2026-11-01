# ProofNet24 P16 — ReLU Contraction

**Run timestamp:** 2026-09-14 22:41:18 Asia/Jerusalem  
**Scope:** tied-weight Gaussian ReLU dynamics; independent-layer results are benchmarks only; **NO number theory**.

## Executive result

The tied model is
\[
W_{ij}\stackrel{\rm iid}{\sim}N(0,\alpha/N),\qquad
F_W(x)=\operatorname{ReLU}(Wx),\qquad
x_{t+1}=F_W(x_t),
\]
with the **same matrix \(W\) reused at every time**.

The strongest target remains
\[
\boxed{
\forall\alpha<2,\quad
P\{\exists C(W)<\infty,\rho(W)<1:
\|F_W^t(x)\|\le C(W)\rho(W)^t\|x\|
\ \forall x,t\}\to1.
}
\tag{MAIN}
\]

It is still OPEN for \(1/2\le\alpha<2\), including the original July normalization \(\alpha=1\). The fresh-input radial exponent is
\[
\chi_{\rm rad}(\alpha)=\frac12\log(\alpha/2).
\]

This run proves two deterministic theorems that identify the exact obstruction to `(MAIN)`.

### `P16-MAXLYAP-INVARIANT-10` — PROVED

Let
\[
K=S^{N-1}\cap\mathbb R_+^N,\qquad
g_W(u)=\|F_W(u)\|,
\]
and, when \(g_W(u)>0\),
\[
T_W(u)=F_W(u)/g_W(u).
\]
Define
\[
\Gamma_t(W)=\sup_{u\in K}\|F_W^t(u)\|.
\]
Positive homogeneity gives
\[
\Gamma_{s+t}\le\Gamma_s\Gamma_t,
\]
hence
\[
\boxed{
\lambda_{\max}(W)
=
\lim_{t\to\infty}t^{-1}\log\Gamma_t(W)
=
\inf_{t\ge1}t^{-1}\log\Gamma_t(W).
}
\tag{ML1}
\]

Let \(D_W=\{u:g_W(u)=0\}\), and let \(\mathcal I_W\) be the projective \(T_W\)-invariant probability measures assigning zero mass to \(D_W\). If \(\lambda_{\max}(W)>-\infty\), then
\[
\boxed{
\lambda_{\max}(W)
=
\sup_{\nu\in\mathcal I_W}
\int\log g_W(u)\,d\nu(u).
}
\tag{ML2}
\]

Consequently,
\[
\boxed{
\text{uniform all-start exponential contraction}
\iff
\lambda_{\max}(W)<0.
}
\tag{ML3}
\]

If \(\lambda_{\max}(W)<0\), then for every
\[
e^{\lambda_{\max}(W)}<\rho<1
\]
there is \(C(W,\rho)<\infty\) such that
\[
\|F_W^t(x)\|\le C(W,\rho)\rho^t\|x\|
\quad\forall x,\forall t.
\]
Conversely any such estimate forces \(\lambda_{\max}(W)\le\log\rho<0\).

A useful equivalent finite-block criterion is
\[
\boxed{
\lambda_{\max}(W)<0
\iff
\exists L\ge1:\Gamma_L(W)<1.
}
\tag{ML4}
\]

### `P16-RECURRENT-OBSTRUCTION-10` — PROVED

If
\[
\lambda_{\max}(W)\ge0,
\]
then there is an ergodic invariant \(\nu\in\mathcal I_W\) with
\[
\int\log g_W\,d\nu=\lambda_{\max}(W).
\]
For \(\nu\)-almost every \(u\),
\[
\lim_{t\to\infty}\frac1t\log\|F_W^t(u)\|
=
\lambda_{\max}(W)
\]
and \(u\) is recurrent for \(T_W\).

Therefore, for every \(\varepsilon>0\), there are arbitrarily large \(L\) and unit \(u\ge0\) such that
\[
\boxed{\|T_W^L(u)-u\|<\varepsilon}
\tag{RO1}
\]
and
\[
\boxed{\|F_W^L(u)\|\ge e^{-\varepsilon L}.}
\tag{RO2}
\]
Writing \(r_L=\|F_W^L(u)\|\),
\[
\boxed{
\|F_W^L(u)-r_Lu\|<\varepsilon r_L,\qquad
r_L^{1/L}\ge e^{-\varepsilon}.
}
\tag{RO3}
\]

Thus failure of `(MAIN)` cannot be a purely transient exceptional trajectory. It creates an arbitrarily long nearly closed projective orbit with noncontracting average radial multiplier. Exact rays and finite cycles are only special cases.

## Exact July source and normalization

The July source email is Gmail message `19f7fe2c44bd282c`, subject `Relu project`, dated 20 July 2026. It contains:

1. `ReLU_finite_horizon_Overleaf.pdf`;
2. `Deep_Gaussian_ReLU_Global_Stability_Overleaf.pdf`.

The fixed-matrix finite-horizon manuscript uses
\[
W_{ij}\sim N(0,1/N),\qquad x_{t+1}=(Wx_t)_+,
\]
with one \(W\) reused forever. For every fixed horizon \(T\), tolerance \(\delta>0\), and deterministic unit start,
\[
\boxed{
P_W\left\{
\max_{0\le t\le T}|2^t\|x_t\|^2-1|>\delta
\right\}
\le Ce^{-cN}.
}
\tag{JULY-FH}
\]
It also proves the same for a random start independent of \(W\), and an almost-every-input theorem: for any start measure \(\mu_N\) independent of \(W\), with probability at least \(1-Ce^{-cN/2}\), the \(\mu_N\)-mass of bad starts is at most \(e^{-cN/2}\).

The source explicitly does **not** claim all-time control, arbitrary growing horizon, or uniform control of every input chosen after observing \(W\). Its proof uses adaptive orthogonal Gaussian queries and Gram-Schmidt innovations.

The other July manuscript treats **independent matrices across layers**:
\[
(W_\ell)_{ij}\sim N(0,\alpha/n),\qquad W_1,\ldots,W_L\ \text{independent}.
\]
If \(K_{n,L}(\alpha)\) is the genuine global Euclidean Lipschitz constant and
\[
\alpha_L=\sup\{\alpha:P(K_{n,L}(\alpha)\le1)\to1\},
\]
then
\[
\boxed{\lim_{L\to\infty}\alpha_L=2}
\tag{JULY-LC}
\]
and
\[
\boxed{
\alpha_L\ge
2\exp\!\left[-(\sqrt{10}+o(1))\sqrt{\frac{\log L}{L}}\right].
}
\tag{JULY-LC-RATE}
\]
The order is: fix \(L\), send width \(n\to\infty\), then send \(L\to\infty\). This independent-layer theorem cannot be transferred by setting all \(W_\ell=W\).

For the tied scaled model write
\[
W=\sqrt\alpha\,A,\qquad A_{ij}\sim N(0,1/N).
\]
Positive homogeneity gives
\[
F_W=\sqrt\alpha\,F_A,\qquad T_W=T_A,
\]
so projective dynamics do not depend on \(\alpha\); only the radial cocycle does. For a deterministic unit input independent of fresh row randomness,
\[
E\|F_W(x)\|^2=\alpha/2.
\]

## Latest P16 state read

The complete prior report `2026-09-14_21-40-19__run-report.md` (Library id `file_00000000f92881f89c7fa2766f7ff96f`) was read in full.

Inherited proved results include: fixed/growing-horizon radial law for deterministic or \(W\)-independent starts; uniform all-start all-time contraction for \(\alpha<1/2\); failure of uniform one-step contraction above the positive-cone best-response threshold; no large ReLU eigenrays below the radial threshold; contraction of asymptotically projectively regular orbits for every fixed \(\alpha<2\); exclusion of disjoint-support exact two-cycles; support/overlap entropy exclusions; and the latest exact period-two reductions.

The immediately preceding claims are:

- `P16-CYCLE2-APPROXRAY-09`: any exact projective two-cycle
  \[
  (Au)_+=gv,\qquad (Av)_+=hu
  \]
  produces \(w=\sqrt h\,u+\sqrt g\,v\) with relative ReLU-ray defect at most \(\sqrt{1-\langle u,v\rangle^2}\).

- `P16-CYCLE2-EQUALSUPPORT-09`: equal-support exact two-cycles collapse to exact ReLU eigenrays and hence noncontracting ones are absent w.h.p. for every fixed \(\alpha<2\).

- `P16-CYCLE2-TYPE-SPECTRAL-09`: support entropy, outside-row orthant cost, overlap mass, and rectangular Gaussian spectral rarity jointly exclude a substantial region of noncontracting exact two-cycles without ever replacing reused blocks by independent ones.

The remaining exact two-cycle region is dense, support-mismatched, high-overlap, and spectrally atypical.

## OTHER reports read

The complete P15 report `P15_kernel_mean_correction_2026-09-14_22-23-36.md` (Library id `file_000000003f8c822f8d90f33b76523b46`) and the complete P13 report `P13_fourth_moment_RMT_2026-09-14_22-04-16.md` (Library id `file_000000005a1481f6adcdf1cca4cc241f`) were read.

P15's newest theorem is a prediction-relevant Schur-complement influence theorem. P13's weak-tail work reinforces the same dependence discipline needed here: preserve the actual reused/dependent object instead of substituting fictitious independent coordinates or layers.

## Proof of `P16-MAXLYAP-INVARIANT-10`

Positive homogeneity gives submultiplicativity directly. If \(F_W^t(u)\neq0\), normalize
\[
v=F_W^t(u)/\|F_W^t(u)\|\in K.
\]
Then
\[
F_W^{t+s}(u)
=
\|F_W^t(u)\|F_W^s(v),
\]
so \(\Gamma_{t+s}\le\Gamma_t\Gamma_s\). Fekete gives `(ML1)`.

If \(\lambda_{\max}<0\), choose \(e^{\lambda_{\max}}<\rho<1\). Some finite \(L\) satisfies \(\Gamma_L<\rho^L\). Writing \(t=kL+r\),
\[
\Gamma_t\le\Gamma_L^k\Gamma_r\le C_0\rho^t.
\]
After one step every orbit is nonnegative, and \(\|F_W(x)\|\le\|W\|\|x\|\), giving the full-space uniform estimate. The converse follows by restricting any uniform \(C\rho^t\) estimate to \(K\). This proves `(ML3)` and `(ML4)`.

For the variational formula, any invariant \(\nu\) with finite radial integral satisfies
\[
\log\|F_W^t(u)\|
=
\sum_{j=0}^{t-1}\log g_W(T_W^ju)
\]
almost surely. Integrating and using invariance,
\[
t\int\log g_W\,d\nu
\le\log\Gamma_t,
\]
hence every invariant exponent is at most \(\lambda_{\max}\).

For the reverse inequality, choose \(u_k\) attaining \(\Gamma_{t_k}\) with \(t_k\to\infty\), and average its surviving projective orbit:
\[
\nu_k=\frac1{t_k}\sum_{j=0}^{t_k-1}\delta_{T_W^ju_k}.
\]
A weakly convergent subsequence exists by compactness of \(K\).

The only issue is the dead set, where \(T_W\) is undefined. Let
\[
B=\max\{0,\log\|W\|\},\qquad
E_R=\{u:g_W(u)<e^{-R}\}.
\]
If \(p_{k,R}=\nu_k(E_R)\), then
\[
t_k^{-1}\log\Gamma_{t_k}
\le B-p_{k,R}(R+B),
\]
so
\[
p_{k,R}
\le
\frac{B-t_k^{-1}\log\Gamma_{t_k}}{R+B}.
\]
Since the left average tends to \(\lambda_{\max}>-\infty\), the limiting measure gives zero mass to the dead set as \(R\to\infty\).

To prove invariance, test against bounded continuous \(f\), insert a continuous cutoff that vanishes for \(g_W\le e^{-2R}\) and equals one for \(g_W\ge e^{-R}\), use the orbit telescoping identity, pass to the weak limit, then \(R\to\infty\). The \(O(R^{-1})\) dead-neighborhood frequency makes the cutoff error vanish.

Finally, the continuous truncations
\[
\phi_R(u)=\max\{\log g_W(u),-R\}
\]
satisfy
\[
\int\phi_R\,d\nu_k\ge t_k^{-1}\log\Gamma_{t_k}.
\]
Pass \(k\to\infty\), then \(R\to\infty\), to obtain an invariant \(\nu\) with exponent at least \(\lambda_{\max}\). The opposite inequality was already proved, giving `(ML2)`.

## Proof of `P16-RECURRENT-OBSTRUCTION-10`

When \(\lambda_{\max}\ge0\), a maximizing invariant measure has finite log-gain integral. Ergodic decomposition yields a maximizing ergodic component. Birkhoff gives the almost-sure radial exponent \(\lambda_{\max}\), and Poincare recurrence gives arbitrarily large \(L_k\) with
\[
T_W^{L_k}u\to u.
\]
At the same times, for every fixed \(\varepsilon>0\) eventually
\[
\|F_W^{L_k}(u)\|\ge e^{-\varepsilon L_k}.
\]
Since
\[
F_W^{L_k}(u)=r_kT_W^{L_k}u,
\]
the recurrence immediately yields `(RO3)`.

Hence a failure of uniform contraction always produces a recurrent invariant obstruction; it cannot be only transient.

## Consequence for proof strategy

The probabilistic tied theorem is now exactly
\[
\boxed{
P\{\lambda_{\max}(W)<0\}\to1
\quad(\alpha<2).
}
\]
Equivalently, with high probability every projective invariant measure must have negative radial exponent.

This proves that the previous target `P16-APPROXRAY-GAP-10`, although useful for high-overlap period two, is not logically sufficient for all time. A nonnegative invariant measure may produce approximate rays only for long iterates \(F_W^L\).

A true all-time analogue is:

### `P16-ITERATE-APPROXRAY-GAP-11` — OPEN

For fixed \(\alpha<2\), prove that w.h.p. there are \(L_0<\infty,\delta_\alpha,c_\alpha>0\) such that for every \(L\ge L_0\), every unit \(u\ge0\) with
\[
\|T_W^L(u)-u\|<\delta_\alpha
\]
satisfies
\[
\|F_W^L(u)\|\le e^{-c_\alpha L}.
\]
By the recurrent-obstruction theorem, this would imply `(MAIN)`.

## Peer audit

### `P16-AUDIT-P15-QUOTIENT-10` — PASS

Audited P15 claim `P15-QUOTIENT-HESSIAN-07`, source report `P15_kernel_mean_correction_2026-09-14_22-23-36.md`, Library id `file_000000003f8c822f8d90f33b76523b46`.

P15 assumes an exact secant Hessian
\[
\overline H=
\begin{pmatrix}A&B\\B^\top&C\end{pmatrix}\succeq0,
\qquad
\overline H\Delta=b.
\]
It defines
\[
S=A-BC^\dagger B^\top,\qquad
\widetilde b_R=b_R-BC^\dagger b_N.
\]
The only delicate point is singular \(C\). If \(v\in\ker C\), positivity of
\[
\left\langle (tu,v),\overline H(tu,v)\right\rangle
=
t^2\langle u,Au\rangle+2t\langle u,Bv\rangle
\]
for both signs of small \(t\) forces \(Bv=0\). Thus \(B\ker C=0\). From
\[
B^\top r+Cn=b_N
\]
one gets
\[
n=C^\dagger(b_N-B^\top r)+n_0,\qquad n_0\in\ker C,
\]
and the null component vanishes after multiplication by \(B\). Substitution gives
\[
Sr=\widetilde b_R.
\]
If \(S\succeq\mu I\), then
\[
r=S^{-1}\widetilde b_R.
\]
The prediction bound follows by integrating the prediction Jacobian along the actual deletion chord and using pathwise nuisance invariance.

Verdict:
\[
\boxed{\texttt{P15-QUOTIENT-HESSIAN-07: PROVED / PASS}.}
\]
This does not certify the empirical AdamW curvature hypotheses, which P15 correctly leaves open.

## Expectation / probability / uniformity distinctions

For a deterministic \(x\), or a start independent of \(W\),
\[
E\|F_W(x)\|^2=(\alpha/2)\|x\|^2.
\]
This is not uniform over \(W\)-dependent starts.

At \(\alpha=1\), the July theorem gives exponentially high-probability control over every **fixed** horizon for each deterministic start, and exponentially small exceptional start-measure for any start distribution independent of \(W\).

Uniform all-start all-time contraction is proved for \(\alpha<1/2\) and is still open for \(1/2\le\alpha<2\).

The new \(\lambda_{\max}(W)\) theorem is deterministic at fixed width and already takes \(t\to\infty\). The unresolved probability question is the width-asymptotic sign of that fixed-width infinite-time exponent.

## Failed-route graveyard

Expectation contraction does not imply uniform contraction. Uniform one-step contraction is false well below \(\alpha=2\). No expanding ray does not imply all trajectories decay. Independent-layer Lipschitz results cannot be transplanted to tied weights. Tiny finite-time norm does not guarantee later safety. Arbitrary-mask joint spectral radius is too pessimistic because most mask sequences are unrealizable. Disjoint-support and equal-support two-cycle obstructions have been eliminated, but dense recurrent motion remains. Reused Gaussian blocks cannot be treated as independent. This run additionally rejects the claim that one-step approximate-ray exclusion would by itself prove `(MAIN)`, and disproves the possibility that failure of `(MAIN)` is purely transient.

## Ledger

### PROVED

Inherited: exact July tied model; independent-layer benchmark; finite-horizon Gaussian innovations/state evolution; fixed-time angle synchronization; growing-horizon law for deterministic or \(W\)-independent starts; uniform all-start contraction for \(\alpha<1/2\); no-large-ray theorem; asymptotically regular-orbit contraction below \(2\); positive-cone best-response results; sparse-transition/cycle exclusions; disjoint-support two-cycle exclusion; period-two radial/entropy theorems; `P16-CYCLE2-APPROXRAY-09`; `P16-CYCLE2-EQUALSUPPORT-09`; `P16-CYCLE2-TYPE-SPECTRAL-09`.

New: `P16-MAXLYAP-INVARIANT-10`; finite-block criterion \(\lambda_{\max}<0\iff\exists L:\Gamma_L<1\); `P16-RECURRENT-OBSTRUCTION-10`; long-iterate approximate-ray corollary; `P16-AUDIT-P15-QUOTIENT-10`.

### CONDITIONAL / protocol-open

The period-two entropy/spectral claims still need additional OTHER-worker audits. A projective closing theorem would allow finite-period counting to attack the full invariant-measure obstruction. Any complete proof of `(MAIN)` needs two independent audits.

### DISPROVED / REJECTED

Expectation-to-uniform inference; one-step contraction throughout \(\alpha<2\); no-ray-to-global inference; independent-layer transfer; tiny-norm permanence; arbitrary-mask JSR as the realizable object; sparse recurrence as the only obstruction; surviving disjoint/equal-support cycles; independence of reused overlap blocks; one-step approximate-ray gap as a complete all-time proof; purely transient failure.

### OPEN

The main theorem for \(1/2\le\alpha<2\); \(P\{\lambda_{\max}(W)<0\}\to1\); negativity of every invariant-measure exponent; deterministic finite block \(L(\alpha)\) with \(\Gamma_L<1\) w.h.p.; `P16-APPROXRAY-GAP-10`; `P16-ITERATE-APPROXRAY-GAP-11`; dense intermediate-overlap cycles; period-\(k\) and nonperiodic recurrence; projective closing; exact positive-cone norm; multi-time adapted sign decoupling; reachable-mask entropy/Gaussian-width theorem; two independent audits of any complete solution.

## Highest-value next attack

### `P16-BLOCK-LYAP-GAP-11`

For every fixed \(\alpha<2\), find deterministic finite \(L=L(\alpha)\) and \(c_\alpha>0\) such that
\[
\boxed{
P\{\Gamma_L(W)\le e^{-c_\alpha L}\}\to1.
}
\tag{NEXT}
\]
Submultiplicativity would then prove `(MAIN)` immediately.

Three routes remain plausible: realizable tied-mask block entropy for a fixed \(L\) without introducing fresh matrices; direct invariant-measure entropy showing any near-zero exponent must spend mass in exponentially rare support/overlap configurations; and approximate recurrent-cycle counting via Kac-Rice/Gaussian width with a negative exponent per time step.

## Bottom line

The July tied theorem and independent-layer theorem are now cleanly separated. The tied all-start infinite-time statement is still open in the interval
\[
1/2\le\alpha<2.
\]
This run identifies its exact deterministic obstruction:
\[
\boxed{
\lambda_{\max}(W)
=
\sup_{\nu\in\mathcal I_W}\int\log\|F_W(u)\|\,d\nu(u).
}
\]
Uniform exponential contraction holds exactly when this number is negative. If it is nonnegative, there is an ergodic recurrent invariant obstruction and arbitrarily long near-cycles with near-noncontracting geometric-mean radial gain.

A complete proof below the conjectured threshold \(2\) must rule out that invariant-measure obstruction.

