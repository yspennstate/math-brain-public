# T223–T322 whole-row triage and an actual phase-retrieval theorem

Prepared 23 October 2026 (America/New_York; host clock 24 October UTC). The source registry and all prior campaign/followup files were treated as frozen. This report does not count a new solved problem and does not claim literature novelty.

## Decision

**T321 is the strongest route found that stays inside an explicitly named original model.** The actual empirical quartic Gaussian phase-retrieval loss admits a direct, quantitative negative answer for sampling in raw parameter space: at a specified temperature that concentrates near the minimizers, its Poincaré constant is at least exponential in dimension, and Metropolis-adjusted Langevin has an exponential mixing lower bound from a specified 2-warm initialization. A truncated Metropolis-adjusted chain also has an explicit all-start time-to-accuracy upper bound with quantified target error. No toy double-well or categorical-data replacement is used.

This is a negative sampling result. It is not a lower bound for finding either sign of the phase-retrieval solution, for sampling on the sign quotient, for every initialization, or for every algorithm. The proof below is a full theorem for the original row's named phase-retrieval branch and the explicitly selected Metropolis-adjusted discretization. Whether that counts as the user's intended whole-row closure is a scope decision; whether it is a genuinely new open-problem closure is **not cleared**. The mechanism is classical metastability, explicitly anticipated by the cited source, even though the exact finite-sample theorem below was not located in the search.

Other serious candidates checked:

| Row | Reason considered | Source comparison / decision |
|---|---|---|
| T318 | Its original wording explicitly allows a high-dimensional random-features teacher with a mismatched inference prior, making exact posterior-temperature risk calculations plausible. | Wenzel et al. and Aitchison were opened. Baek–Berchuck–Mukherjee, *Asymptotics of Bayesian Uncertainty Estimation in Random Features Regression*, arXiv:2306.03783 (NeurIPS 2023), already treats asymptotic posterior predictive variance versus MAP risk. Two more directly titled 2024–25 reports were found, but their primary texts were not accessible. Novelty risk is substantial; no claim of closure here. |
| T268 | Its spectral-norm-only sample-complexity question initially looked susceptible to a short negative answer. | Vardi–Shamir–Srebro, NeurIPS 2022, Theorem 1, already proves a width-dependent fat-shattering lower bound in the **dimension-free** formulation, including ReLU. The dimension in that construction grows with width. Literal independence of depth/width while allowing arbitrary dependence on a fixed input dimension is different: anchored Lipschitz functions on a bounded domain have elementary metric-entropy bounds. The row does not pin this distinction down; it is not a clean genuinely unclosed target. |
| T321 | Explicit original Gaussian phase-retrieval model; symmetry creates a quantifiable barrier; no artificial loss needs to be invented. | Pursued below. Raginsky–Rakhlin–Telgarsky already identifies exponential inverse-temperature bottlenecks in multiwell losses. The phase-retrieval concentration and finite-sample statements below have not been located as a prior explicit theorem. Novelty remains unverified. |

## Exact original T321 statement

> Fix a model: (i) real phase retrieval, y_i = (a_i . x)^2 with Gaussian a_i, m = alpha d samples, the square loss of the amplitudes squared; or (ii) a two-layer network of width m with a planted teacher, Gaussian inputs, and weight decay lambda. Let pi_beta be proportional to exp(-beta L), with beta = beta(d, epsilon) chosen so that pi_beta gives probability at least 1 - delta to {L <= min L + epsilon}. Prove that pi_beta satisfies a Poincare inequality with constant polynomial in d and 1/epsilon (say separately whether a log-Sobolev inequality, which is stronger, also holds), or show the constant is exponential in d. Then bound the time for discretized Langevin dynamics from a stated initialization to reach total variation or W2 accuracy, including the discretization error. Raginsky, Rakhlin and Telgarsky give bounds exponential in d through the spectral gap; the mean-field limit (T223-T225) is a different question.

Source: `a03/registry422.jsonl`, problem_id `T321`, list `TOP200_DL`, version `2026-10-14`. The source is Raginsky–Rakhlin–Telgarsky, arXiv:1702.03849.

## Explicit theorem (no unproved landscape hypotheses)

Fix a deterministic unit vector \(v\in\mathbb R^d\). Let \(a_1,\ldots,a_m\) be independent \(N(0,I_d)\) vectors, \(y_i=(a_i^Tv)^2\), and define the actual empirical phase-retrieval loss

\[
 L(x)=\frac1{4m}\sum_{i=1}^m\big((a_i^Tx)^2-(a_i^Tv)^2\big)^2.
\]

Take \(m=10^6d\) and \(d\ge100\). Constants are deliberately loose. With probability at least \(1-10e^{-d/2}\) over the data, all conclusions below hold. More generally one can replace \(10^6\) by any sufficiently large fixed sampling ratio, with adjusted absolute constants.

Write

\[
a=\frac1{4096},\qquad b=\frac{9a}{16},\qquad
H=14+\frac12\log(1/a).
\]

For \(0<\epsilon\le b/2\), \(0<\delta\le1/2\), set

\[
\beta=\frac{2}{\epsilon}\left(Hd+\log\frac2\delta\right).
\]

Then \(\pi_\beta(dx)=Z_\beta^{-1}e^{-\beta L(x)}dx\) is a probability measure, its minimum loss is zero, and

\[
\pi_\beta\{L\le\epsilon\}\ge1-\delta.
\]

With the convention

\[
\operatorname{Var}_{\pi_\beta}(f)
\le C_P(\pi_\beta)\int\|\nabla f\|^2d\pi_\beta,
\]

the optimal Poincaré constant obeys

\[
C_P(\pi_\beta)\ge\frac1{16}e^{\beta b/4}.
\]

Both a finite Poincaré constant and a finite logarithmic Sobolev constant exist, as proved in Section 4a. Any logarithmic Sobolev constant under the convention
\(\operatorname{Ent}_{\pi_\beta}(f^2)\le2C_{LS}\int\|\nabla f\|^2d\pi_\beta\)
is at least \(C_P(\pi_\beta)\), so it has the same lower bound. For the physical-time Langevin generator \(\mathcal G=\beta^{-1}\Delta-\nabla L\cdot\nabla\), the relaxation time is \(\beta C_P\), not \(C_P\); this scaling distinction matters.

Consider **MALA**, not unadjusted Euler Langevin: propose

\[
Y=x-h\nabla L(x)+\sqrt{2h/\beta}\,G,\qquad G\sim N(0,I_d),
\]

and apply the ordinary Metropolis–Hastings acceptance ratio for target \(\pi_\beta\) and this Gaussian proposal density. If \(0<h\le(320d^2)^{-1}\), and

\[
\mu_0=\pi_\beta(\,\cdot\mid v^Tx>0),
\]

then for every integer \(k\ge0\),

\[
\|\mu_0P_h^k-\pi_\beta\|_{TV}
\ge\frac12-10k e^{-\beta b/4}.
\]

In particular, total variation distance remains at least \(1/4\) whenever
\(k\le e^{\beta b/4}/40\). The initialization is explicitly 2-warm. It is a lower-bound initialization, not an efficient prescription for constructing a conditional Gibbs sample. Metropolis correction gives exactly invariant \(\pi_\beta\), so there is **zero invariant-distribution discretization bias**. No diffusion-to-Euler error estimate or ULA convergence theorem is claimed. No geometric-ergodicity upper bound for the untruncated MALA chain is claimed.

There is also an explicit **time-to-accuracy upper bound** for a stated, practical modification: MALA with proposals outside a known ball rejected. Section 7 below proves it from any initialization in that ball, including the deterministic initialization \(X_0=0\). The only target error is a quantified truncation error; no unproved discretization estimate is used.

## Proof, including the high-probability data event

### 1. A uniform small-ball event at a fixed linear sample ratio

For unit \(u,w\), put

\[
C_{u,w}=\{z:|z^Tu|\ge1/4,\ |z^Tw|\ge1/4\}.
\]

The union bound and the standard Gaussian density bound give, regardless of the correlation between the two projections,

\[
\Pr\{a\in C_{u,w}\}\ge1-2\Pr\{|N(0,1)|<1/4\}
\ge1-1/\sqrt{2\pi}>0.60.
\]

The class of these sets is a Boolean combination of four affine halfspaces in \(\mathbb R^d\). Its growth function on \(N\ge d+1\) points is bounded by
\((eN/(d+1))^{4(d+1)}\): apply the halfspace growth bound to the four constituent halfspaces, then take their Boolean combination. The usual elementary symmetrization-and-Hoeffding VC inequality therefore yields

\[
\Pr\left\{\sup_{u,w}|P_m(C_{u,w})-P(C_{u,w})|>1/4\right\}
\le 8\left(\frac{2em}{d+1}\right)^{4(d+1)}e^{-m/512}.
\]

For \(m=10^6d,d\ge100\), this is at most \(8e^{-d}\). On its complement, at least \(m/4\) sample vectors simultaneously satisfy the two inequalities, for every pair \(u,w\). By homogeneity, for all \(p,q\in\mathbb R^d\),

\[
\frac1m\sum_i(a_i^Tp)^2(a_i^Tq)^2
\ge\frac1{1024}\|p\|^2\|q\|^2.
\tag{SB}
\]

Zero vectors are immediate. For nonzero vectors the factor is \((1/4)(1/4)^4=1/1024\). Taking \(p=x-v,q=x+v\) proves

\[
L(x)\ge aD(x),\qquad D(x)=\|x-v\|^2\|x+v\|^2.
\tag{1}
\]

This small-ball fact is also a coarse direct version of known stable Gaussian phase-retrieval bounds. Eldar–Mendelson, arXiv:1211.0872, proves such stability with \(O(d)\) measurements. The proof here does not assume a uniform quartic upper bound, which would be false at a constant sampling ratio.

### 2. Elementary Gaussian moment controls

Let \(S=m^{-1}\sum_i a_ia_i^T\). A \(1/8\)-net of the unit sphere has at most \(17^d\) elements. A chi-square Chernoff bound gives

\[
\Pr\{u^TSu>3/2\}\le
\exp[-m(1/2-\log(3/2))/2].
\]

The usual quadratic-form net inequality multiplies the maximum on that net by \((1-2/8)^{-1}=4/3\). Thus \(\|S\|_{op}\le2\) except on an event of probability at most \(e^{-d}\) at our sampling ratio. Also

\[
\Pr\{\max_i\|a_i\|^2>4d\}
\le m\exp[-(3-\log4)d/2]\le e^{-d/2}
\]

for \(d\ge100\). Consequently, simultaneously with (SB),

\[
A=\frac1m\sum_i(a_i^Tv)^2\|a_i\|^2\le8d,
\qquad
B=\frac1m\sum_i\|a_i\|^4\le8d^2.
\tag{2}
\]

Indeed use \(\max_i\|a_i\|^2\le4d\), \(v^TSv\le2\), and \(\operatorname{tr}S\le2d\). Summing the displayed exceptional probabilities is bounded by \(10e^{-d/2}\). All remaining arguments are deterministic on this data event.

### 3. Partition-function comparison without a false bounded-Hessian assumption

Let \(r(x)=\min(\|x-v\|,\|x+v\|)\). The larger of the two squared distances is
\(\|x\|^2+1+2|v^Tx|\ge1\), so (1) implies \(L\ge ar^2\). Hence

\[
Z_\gamma\le2\left(\frac\pi{a\gamma}\right)^{d/2}
\quad(\gamma>0).
\tag{3}
\]

For a lower bound, take \(q_\beta=N(v,I_d/\beta)\). Write \(x=v+z\), \(t_i=a_i^Tv\). The odd Gaussian moment is zero, and

\[
\mathbb E_{q_\beta}\big[(a_i^Tx)^2-t_i^2\big]^2
=\frac{4t_i^2\|a_i\|^2}{\beta}
 +\frac{3\|a_i\|^4}{\beta^2}.
\]

Thus
\(\beta\mathbb E_{q_\beta}L=A+3B/(4\beta)\le14d\)
when \(\beta\ge d\). Jensen applied to
\(Z_\beta=\mathbb E_{q_\beta}[e^{-\beta L}/q_\beta]\), together with the Gaussian entropy, gives

\[
Z_\beta\ge (2\pi e/\beta)^{d/2}
              e^{-\beta\mathbb E_{q_\beta}L}
\ge (2\pi/\beta)^{d/2}e^{-14d}.
\tag{4}
\]

Combining (3) at \(\gamma=\beta/2\) with (4),

\[
\frac{Z_{\beta/2}}{Z_\beta}\le2e^{Hd}.
\]

For every \(u>0\),

\[
\pi_\beta\{L\ge u\}
\le e^{-\beta u/2}\frac{Z_{\beta/2}}{Z_\beta}
\le2e^{Hd-\beta u/2}.
\tag{5}
\]

The specified \(\beta\) exceeds \(d\), and (5) at \(u=\epsilon\) gives the required \(\delta\) concentration.

### 4. A genuine barrier and the Poincaré lower bound

For \(s=v^Tx\), write \(\|x\|^2=s^2+\|x-sv\|^2\). Then

\[
D(x)=(\|x\|^2+1)^2-4s^2
\ge (s^2+1)^2-4s^2=(1-s^2)^2.
\]

On the strip \(B_0=\{|s|\le1/2\}\), this is at least \(9/16\), so \(L\ge b\). Also \(D\ge(\|x\|^2-1)^2\), so \(L\ge9a\ge b\) on \(B_\infty=\{\|x\|>2\}\). Since \(Hd\le\beta\epsilon/2\le\beta b/4\), (5) yields

\[
p:=\pi_\beta(B_0)\le2e^{-\beta b/4},
\qquad \pi_\beta(B_\infty)\le2e^{-\beta b/4}.
\tag{6}
\]

The loss and Gibbs law are invariant under \(x\mapsto-x\). The Lipschitz odd test function
\(f(x)=\max(-1,\min(1,2v^Tx))\)
has mean zero, variance at least \(1-p\), and Dirichlet energy at most \(4p\). It is admissible by smooth approximation (the density is smooth and positive). Therefore

\[
C_P\ge\frac{1-p}{4p}\ge\frac1{16}e^{\beta b/4},
\]

where \(p\le1/2\) holds by the stated parameter choices. The log-Sobolev implication follows by expanding its inequality at \(1+tf\) and taking \(t\to0\).

### 4a. Explicit finite Poincaré and log-Sobolev upper bounds

The original Gibbs measure also satisfies a logarithmic Sobolev inequality. This follows from an explicit bounded convexification, proposed by the parent and independently checked here. No globally Lipschitz gradient is assumed.

For every unit direction \(z\), (SB) gives

\[
z^T\nabla^2L(x)z
=\frac1m\sum_i\big(3(a_i^Tx)^2-(a_i^Tv)^2\big)(a_i^Tz)^2
\ge \frac3{1024}\|x\|^2-8d.
\]

Put

\[
c_0=3/1024,\qquad A_0=4d+\tfrac12,\qquad
R_0^2=\frac{8d+12A_0+1}{c_0}.
\]

Define a \(C^2\), nondecreasing function on \([0,\infty)\) by

\[
h(s)=\begin{cases}
s,&0\le s\le1,\\
1+t-t^3+\tfrac12t^4,&1\le s\le2,\quad t=s-1,\\
\tfrac32,&s\ge2.
\end{cases}
\]

In its middle interval, \(h'=(1-t)^2(1+2t)\ge0\) and \(h''=-6t(1-t)\ge-3/2\), and the derivatives through order two match at both joins. Set

\[
u(x)=A_0R_0^2h(\|x\|^2/R_0^2).
\]

Inside \(\|x\|\le R_0\), \(\nabla^2u=2A_0I\), which makes \(\nabla^2(L+u)\succeq I\). In the annulus \(R_0^2\le\|x\|^2\le2R_0^2\),

\[
\nabla^2u=2A_0h'I+\frac{4A_0}{R_0^2}h''xx^T\succeq-12A_0I,
\]

whereas \(\nabla^2L\succeq(c_0R_0^2-8d)I=(12A_0+1)I\). Outside the annulus \(u\) is constant and \(\nabla^2L\succeq I\). Thus \(L+u\) is globally 1-strongly convex.

By Bakry–Émery, the Gibbs law for \(\beta(L+u)\) has logarithmic Sobolev constant at most \(1/\beta\) in our convention. Since
\(0\le u\le\tfrac32A_0R_0^2\), the Holley–Stroock bounded-perturbation inequality gives

\[
C_P(\pi_\beta)\le C_{LS}(\pi_\beta)
\le\frac1\beta\exp\left(\frac32\beta A_0R_0^2\right)<\infty.
\tag{6a}
\]

Both standard criteria, with the needed normalization, are recorded as Theorems 3.1–3.2 of Menz–Schlichting, arXiv:1202.1510v4 (PDF pp. 22–23). No matching lower/upper exponential rate is asserted: the lower bound is \(e^{c\beta}\), while this upper bound is \(\beta^{-1}e^{C\beta d^2}\).

For well-posedness of the underlying diffusion, (SB) also yields
\(\langle x,\nabla L(x)\rangle\ge4a\|x\|^4-8d\|x\|^2\).
The polynomial drift is locally Lipschitz. Applying Itô's formula to the stopped squared norm and using this radial bound prevents finite-time explosion. Integration by parts against the smooth quartic-tailed density proves invariance of \(\pi_\beta\). None of these facts implies convergence of unadjusted Euler discretization.

### 5. The explicit MALA bottleneck bound

Let \(A_+=\{s>0\}\), so \(\pi_\beta(A_+)=1/2\). The exact MALA transition kernel satisfies detailed balance by construction. In particular, it preserves \(\pi_\beta\), and if a starting density is at most \(2\) with respect to \(\pi_\beta\), that remains true after every step.

For \(\|x\|\le2\), (2) implies

\[
\|\nabla L(x)\|
\le\frac1m\sum_i\big(\|a_i\|^2\|x\|^2+(a_i^Tv)^2\big)
                 \|a_i\|^2\|x\|
\le(2^3+2)B\le80d^2.
\]

For \(x\in A_+\setminus(B_0\cup B_\infty)\), therefore,
\(v^T(x-h\nabla L(x))\ge1/4\)
under the stated step bound. A one-dimensional Gaussian tail gives

\[
\Pr\{v^TY\le0\mid x\}\le e^{-\beta/(64h)}.
\]

Rejecting a proposal cannot create a sign crossing. For the stationary flow across the sign cut,

\[
Q(A_+,A_+^c)=\int_{A_+}\pi_\beta(dx)P_h(x,A_+^c)
\le4e^{-\beta b/4}+e^{-\beta/(64h)}
\le5e^{-\beta b/4}.
\tag{7}
\]

Starting from \(2\mathbf1_{A_+}\pi_\beta\), the probability of crossing from \(A_+\) to its complement by step \(k\) is at most \(2kQ(A_+,A_+^c)\): union bound over steps, using the preserved density upper bound. Therefore

\[
\mu_0P_h^k(A_+^c)\le10k e^{-\beta b/4},
\]

which proves the stated total-variation lower bound. This is a lower bound for the discrete algorithm itself; it neither accumulates an unaccounted diffusion discretization error nor assumes a Poincaré-to-MALA upper-bound theorem.

### 6. Near-minimizer concentration genuinely requires inverse temperature of order dimension

This additional argument prevents interpreting the exponential barrier merely as a consequence of voluntarily choosing an unnecessarily cold temperature. Let \(v_d\) be the volume of the unit ball and put

\[
c_* = a e^{-29}/16,\qquad
\epsilon_* = \min\left\{c_*,\frac{c_*b}{4H}\right\}.
\]

The numerical constants here are intentionally very conservative. For every \(0<\epsilon\le\epsilon_*\), if **any** inverse temperature \(\beta>0\) satisfies \(\pi_\beta\{L\le\epsilon\}\ge3/4\), then

\[
\beta\ge c_*d/\epsilon,
\qquad
C_P(\pi_\beta)\ge\frac1{16}\exp\left(\frac{c_*b\,d}{4\epsilon}\right).
\tag{8}
\]

To prove this, \(L\ge ar^2\) shows that the volume of the low-loss set is at most
\(2v_d(\epsilon/a)^{d/2}\). The standard bound
\(v_d\le(2\pi e/d)^{d/2}\)
and (4), when \(\beta\ge d\), give

\[
\pi_\beta\{L\le\epsilon\}
\le2\left(\frac{e^{29}\beta\epsilon}{ad}\right)^{d/2}.
\tag{9}
\]

If \(\beta<d\), repeat Jensen with \(q=N(v,I_d/d)\). Then
\(\beta\mathbb E_qL\le14d\), and (9) holds with \(\beta/d\) replaced by 1. When \(\epsilon\le c_*\), this upper bound is at most \(2(1/16)^{d/2}<3/4\). Hence concentration forces \(\beta\ge d\). If in addition \(\beta<c_*d/\epsilon\), the same contradiction follows from (9). This proves the necessary inverse-temperature bound.

For \(\epsilon\le c_*b/(4H)\), it also implies \(Hd\le\beta b/4\). Applying (5) to the strip and repeating the clipped-sign proof yields the second assertion in (8). Thus, for every fixed sufficiently small loss tolerance, **every** concentrating Gibbs temperature has an exponentially large raw-space Poincaré constant. This conclusion does not rely on the particular sufficient-temperature choice in the theorem.

### 7. A full explicit upper bound with controlled truncation and zero Metropolis bias

This section fixes the precise discretized algorithm rather than silently identifying ULA and MALA. For a requested total variation accuracy \(0<\zeta<1\), keep the original target \(\pi_\beta\) unchanged and choose

\[
R=\max\left\{2,\sqrt{1+\sqrt{\frac{2}{a\beta}\left(Hd+\log\frac4\zeta\right)}}\right\},
\qquad K=\{x:\|x\|\le R\}.
\]

Because \(L(x)\ge a(\|x\|^2-1)^2\), (5) gives

\[
\tau_R:=\pi_\beta(K^c)\le
2\exp\left[Hd-\frac{\beta a}{2}(R^2-1)^2\right]\le\zeta/2.
\tag{10}
\]

On \(K\), the same elementary data-event bounds give

\[
0\le L(x)\le M_R:=2d^2(R^2+1)^2,
\qquad \|\nabla L(x)\|\le G_R:=8d^2(R^3+R).
\]

Choose any \(h>0\); for consistency with the bottleneck lower bound one may take \(h\le1/(4G_R)\). Run the Gaussian Langevin proposal stated above, reject all proposals outside \(K\), and apply its usual Metropolis ratio to proposals inside \(K\). Its invariant law is exactly \(\pi_{\beta,K}=\pi_\beta(\cdot\mid K)\).

For all \(x,y\in K\), the proposal density is bounded below by

\[
q_{\min}=\left(\frac{\beta}{4\pi h}\right)^{d/2}
\exp\left[-\frac{\beta(2R+hG_R)^2}{4h}\right].
\]

The accepted continuous transition density is
\(\min\{q(x,y),e^{-\beta(L(y)-L(x))}q(y,x)\}\).
Since \(0\le L\le M_R\), this is at least \(e^{-\beta M_R}q_{\min}\). If \(\nu_K\) is uniform on \(K\), then

\[
P_{h,K}(x,\cdot)\ge\eta_K\nu_K(\cdot),\qquad
\eta_K=v_dR^d e^{-\beta M_R}q_{\min}>0.
\tag{11}
\]

The minorization itself ensures \(\eta_K\le1\). Splitting off this common component gives directly, without an external mixing theorem,

\[
\|\mu P_{h,K}^k-\pi_{\beta,K}\|_{TV}
\le(1-\eta_K)^k\le e^{-k\eta_K}
\]

for every starting law supported on \(K\), including \(\delta_0\). Moreover
\(\|\pi_{\beta,K}-\pi_\beta\|_{TV}=\tau_R\).
Consequently,

\[
k\ge \eta_K^{-1}\log(2/\zeta)
\quad\Longrightarrow\quad
\|\mu P_{h,K}^k-\pi_\beta\|_{TV}\le\zeta.
\tag{12}
\]

This is an explicit, deliberately loose time-to-accuracy upper bound for a specified discretized Langevin algorithm. Its error decomposition is exact: the Metropolis correction eliminates invariant-distribution time-discretization bias, and (10) bounds spatial truncation bias. No claim of an efficient bound is intended.

When \(R=2\), \(M_R=50d^2\), \(G_R=80d^2\), and \(h=(320d^2)^{-1}\), the same formula becomes

\[
\eta_K=v_d2^d\left(\frac{\beta}{4\pi h}\right)^{d/2}
\exp\left[-50\beta d^2-\frac{289\beta}{64h}\right].
\]

For fixed target accuracies and \(\beta=\Theta(d/\epsilon)\), its reciprocal is at most \(\exp[O(d^3/\epsilon+d|\log\epsilon|)]\). This does not match the lower exponential rate, and a matching rate is not claimed.

For the same truncated chain with \(R=2\), the exponential lower bound also holds from \(\pi_{\beta,K}(\cdot\mid v^Tx>0)\). Indeed \(\tau_2\le1/2\), so its strip mass is at most twice the original strip mass; there is no outside-ball contribution. The crossing-flow bound (7) is still at most \(5e^{-\beta b/4}\). The two warming and sign-symmetry arguments are unchanged. Thus one specified discrete chain has both a rigorously slow-start lower bound and a finite, quantified all-start upper bound.

## What remains to be cleared before claiming a new whole-row solution

1. **Novelty.** Raginsky et al., Section 4, already identifies generic exponential inverse-temperature metastability. The exact empirical phase-retrieval/data/temperature theorem is not located in the sources searched, but absence from search is not proof of novelty. Treat this as a new explicit derivation of a classical mechanism unless a deeper literature review clears more.
2. **Meaning of the requested discretization.** The theorem gives both lower and upper time bounds for explicitly truncated MALA, with quantified approximation to the original untruncated Gibbs target. If plain ULA or a matching exponential upper/lower rate was intended, those stronger obligations are not discharged. No such equivalence is asserted.
3. **Initialization.** The specified 2-warm conditional Gibbs start is a standard conductance lower-bound start, not an easily sampled generic initialization. The row says “stated initialization”; it does not require Gaussian initialization. This difference must remain visible.
4. **Raw signs.** This is a real obstruction to raw Gibbs mixing and a real lower bound for the row's explicitly named Poincaré constant. It disappears if an algorithm can make global sign flips or works on the quotient. It does not establish statistical or optimization hardness of phase retrieval.
5. **ULA.** The quartic loss is not globally gradient-Lipschitz, so the source's smoothness assumptions cannot be silently imported. Unadjusted Euler instability requires separate treatment, not a claim of zero bias.

## Primary sources actually inspected

The links below are retrieval locations; the passages and their roles are stated precisely enough to check independently.

- Raginsky, Rakhlin, Telgarsky, [arXiv:1702.03849v3, full text](https://arxiv.org/html/1702.03849v3), Section 2 and Section 4 “Uniform spectral gap,” especially Eq. (4.3), and Appendix B. The paper gives a general conservative inverse-gap upper estimate, explains exponential inverse-temperature dependence for multiwell landscapes, and asks for structurally favorable small inverse gaps. It does not state the empirical phase-retrieval theorem above. Retrieval refs: `turn176view1`, `turn178view2`.
- The same paper, Appendix A, Propositions A.1–A.2, also supplies alternative Lyapunov criteria for functional inequalities. Its separate M-smooth SGLD theorem is not applied here. A full-text search found no occurrence of “phase retrieval”: that branch is the original registry's concrete specialization, not a named phase-retrieval conjecture stated by Raginsky et al. Retrieval refs: `turn232view3`, `turn232view4`.
- Eldar and Mendelson, [Phase Retrieval: Stability and Recovery Guarantees](https://arxiv.org/pdf/1211.0872), Theorem 2.4 and its full-space specialization: stable recovery with linearly many Gaussian measurements. It supports the mathematical standardness of the small-ball ingredient, which is proved independently above. Retrieval ref: `turn195view0`.
- Roberts and Tweedie, [Exponential Convergence of Langevin Distributions and Their Discrete Approximations](https://www2.stat.duke.edu/~scs/Courses/Stat376/Papers/Langevin/RobertsTweedieBernoulli1996.pdf), Bernoulli 2(4), 341–363 (1996), Sections 3–4. This establishes that naive Euler and adjusted Langevin do not automatically inherit continuous-diffusion ergodicity, especially for lighter-than-Gaussian tails. It prevents an invalid ULA or geometric-MALA inference here. Retrieval ref: `turn195view1`.
- Wenzel et al., [arXiv:2002.02405v2, full text](https://arxiv.org/html/2002.02405v2), Sections 5.2 and 8. Empirical cold-posterior phenomenon; the authors do not resolve its mechanism. Retrieval refs: `turn176view0`, `turn178view3`.
- Aitchison, [arXiv:2008.05912v2](https://arxiv.org/pdf/2008.05912), Sections 2–3. Distinguishes posterior/likelihood tempering and develops a data-curation model. Retrieval ref: `turn193view2`.
- Baek, Berchuck, Mukherjee, [arXiv:2306.03783](https://arxiv.org/pdf/2306.03783), NeurIPS 2023. Relevant existing proportional random-features Bayesian uncertainty asymptotics; full PDF opened after initial triage. Retrieval refs: `turn195academia48`, `turn195search2`, `turn232view0`.
- Vardi, Shamir, Srebro, [The Sample Complexity of One-Hidden-Layer Neural Networks](https://proceedings.neurips.cc/paper_files/paper/2022/file/3baf4eeffad860ca9c54aeab632716b4-Paper-Conference.pdf), Theorem 1, PDF pp. 4–5, excludes **dimension-free** width-independent complexity under spectral-norm constraints for the relevant ReLU class. Its lower-bound input dimension grows with width; it does not exclude a bound with arbitrary dependence on fixed input dimension. Retrieval refs: `turn193view1`, `turn195view2`.
- Original T268 citations also opened: Golowich–Rakhlin–Shamir [arXiv:1712.06541v5](https://arxiv.org/pdf/1712.06541), and Bartlett–Foster–Telgarsky [arXiv:1706.08498](https://arxiv.org/pdf/1706.08498). Retrieval refs: `turn232view1`, `turn232view2`. The later Vardi–Shamir–Srebro fat-shattering result is the more direct obstacle to counting this row as unclosed.
- The Tien Mai, [Optimal sparse phase retrieval via a quasi-Bayesian approach](https://arxiv.org/html/2504.09509v1), 2025, theoretical Section 3 and algorithmic/numerical Section 4.1. This is a statistical contraction and empirical Langevin implementation paper for a different sparsity-prior/noise setting; no corresponding raw-sign mixing theorem was identified. Retrieval refs: `turn193view3`, `turn195view3`.

Searches included the exact combinations “phase retrieval” with “spectral gap,” “Gibbs,” “Poincare constant,” “Langevin,” “mixing time,” “Metropolis,” and “exponential,” including current search results. They retrieved generic metastability and phase-retrieval sampling work, but no exact deciding theorem for the specified empirical model. This is an evidence limit, not a novelty certification.

Additional primary-source checks after the initial proof:

- Menz and Schlichting, [arXiv:1202.1510v4](https://arxiv.org/pdf/1202.1510), Theorems 3.1–3.2, PDF pp. 22–23, state the Bakry–Émery and Holley–Stroock criteria used in Section 4a. Its Eyring–Kramers results also confirm the established nature of the metastability mechanism, but are not invoked to assert uniformity in growing dimension. Retrieval refs: `turn239view0`, `turn240view0`, `turn240view1`, `turn241view1`.
- Lytras, Makras, Sabanis, [The Tamed Subgradient Unadjusted Langevin Algorithm beyond Convexity, arXiv:2608.06283v1](https://arxiv.org/html/2608.06283v1), Theorem 1 and Section 8.2, treats a tamed Euler algorithm, gives explicit Wasserstein discretization/contraction bounds, and applies them to generalized **complex** phase retrieval with quartic least-squares potential. The source expressly distinguishes mode mixing from optimization. This is closely relevant 2026 upper-bound literature; no real-sign, high-probability, near-minimizer-temperature lower bound matching ours was found in the inspected section. Complex phase rotations form a connected symmetry orbit, so its geometry does not automatically give the discrete real-sign obstruction proved here. Retrieval refs: `turn239view1`, `turn240view2`, `turn241view0`.
