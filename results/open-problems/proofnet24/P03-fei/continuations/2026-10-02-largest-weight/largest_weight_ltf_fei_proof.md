# Fourier entropy–influence bound for every linear threshold function

Date: 2026-10-02. **Complete proof, internally audited.**

The proof below establishes the uniform-cube Fourier entropy–influence bound
for every Boolean linear threshold function, with arbitrary real input
weights and arbitrary threshold (output bias). Four independent internal
analytic audits found no gap in the preceding candidate version. That is not
external peer review, and the research-priority search has not certified
novelty. The general FEI conjecture for all Boolean functions remains open;
this proof also makes no claim for nonuniform product input distributions.

The [earlier candidate draft](largest_weight_ltf_candidate.md) is preserved
separately. The argument combines
two established biased-halfspace estimates with an elementary interval-noise
bound, hypercontractivity, and a dyadic relative-entropy comparison.

All entropy and KL divergence below use base-2 logarithms; \(\ln\) is natural.
The uniform cube convention is \(\widehat f(S)=\mathbb E f\chi_S\).

## Theorem and constants

Let \(f:\{-1,1\}^n\to\{-1,1\}\) be an LTF under the uniform input
measure. Define
\[
 H(f)=\sum_S\widehat f(S)^2\log_2\frac1{\widehat f(S)^2},\qquad
 I(f)=\sum_i\Pr[f(X)\ne f(X^{\oplus i})].
\]
There is a universal \(C_*<\infty\) such that
\[
 \boxed{H(f)\le C_*I(f).}
\tag{T}
\]
More strongly, every nonconstant Boolean LTF split on a coordinate of
largest absolute input weight satisfies

\[
 \Delta_iH(f):=H(f)-\tfrac12[H(f^{+})+H(f^{-})]
 \le C_* I_i(f).
\tag{1}
\]

No weight regularity assumption is made. Here is an explicit expression for
the constant in terms of an established universal constant. Let \(0<c\le1\)
be a lower-bound constant in Keller–Klein's Theorem 1.4, with physical
bit-flip influences and input-weight Euclidean normalization. Set
\[
 \begin{gathered}
 A_0=\frac{20.5\sqrt2}{1-e^{-1}},\qquad
 \Gamma=\max\{1,\sqrt2A_0/c\},\\
 r=2^{-1/4},\quad Z=\frac{1+r}{1-r},\quad
 s=2^{-1/2},\quad C_-=18\sqrt2\frac{s}{(1-s)^2},\\
 C_D=\log_2(2Z\Gamma)+\tfrac34C_-+1+\frac{\log_2e}{e},\qquad
 C_*=2(C_D+\log_2e).
 \end{gathered}
\]
All these constants are universal. The primary Keller–Klein theorem supplies
an existential constant; no unsupported numerical value for \(c\) is assigned
here. Constants and zero-variable functions have \(H=I=0\).

## 1. Established inputs and normalization

Delete zero-weight coordinates; this preserves entropy and influence.
Coordinate sign changes and an output sign change preserve every quantity
in (1), and preserve the LTF class. Thus take a monotone LTF with positive
input weights and positive output density \(0<p\le1/2\). Ties at the threshold can be removed by moving
the threshold slightly inside the finite gap between the largest negative
and smallest positive score; the Boolean function is unchanged.

Let coordinate \(i\) have largest weight \(w>0\). Let the remaining weights
be \(a_j\in[0,w]\), with
\(\sigma^2=\sum_j a_j^2\), and put

\[
 R=\sigma^2/w^2,\quad L=\ln(1/p),\quad M=\max\{1,R,L\}.
\]

Write the split as

\[
 f(x,z)=A(x)+zB(x),\qquad
 B(x)=\mathbbm1\{|\sum_j a_jx_j-\theta|<w\}.
\tag{2}
\]

The open slab notation is valid after the threshold perturbation. Its values
at endpoints otherwise use the corresponding half-open interval; all
concentration arguments also apply to closed intervals. Put
\(\alpha=\mathbb E B=I_i(f)\).

A coordinate of largest weight also has largest influence. Indeed, for
\(w_i\ge w_j\), monotonicity gives \(I_i=\widehat f(\{i\})\), and after
conditioning on other coordinates,

\[
 I_i-I_j=\tfrac12\mathbb E\bigl[
 f(T+w_i-w_j)-f(T-w_i+w_j)\bigr]\ge0.
\]

Keller–Klein (2019), Theorem 1.4, gives an absolute \(c>0\) with

\[
 \alpha\ge c p\min\{1,\sqrt{L/(R+1)}\}.
\tag{3}
\]

In particular, \(\alpha>0\) for a nonconstant LTF. Therefore

\[
 \frac{p\sqrt L}{\sqrt M}\le\frac{\sqrt2}{c}\alpha.
\tag{4}
\]

For \(L\le R+1\), use \(R+1\le2M\); for \(L>R+1\), \(M=L\).
Also \(\alpha\le2p\), since the pivotal slab accounts for an edge joining
the rare output to the other output, and the rare endpoint has probability
\(\alpha/2\) in the full cube.

Klivans–O'Donnell–Servedio (2004), Theorem 18, gives, for
\(0<\varepsilon\le1/2\),

\[
 \operatorname{NS}_\varepsilon(f)\le20.5p\sqrt{\varepsilon L}.
\tag{5}
\]

These are established primary results, not newly proved here. Sources:
<https://arxiv.org/html/1710.07429v3>;
<https://www.cs.columbia.edu/~rocco/Public/focs02.pdf>.

## 2. Slab-noise lemma, with an elementary proof

**Lemma.** For \(B\) in (2), \(R>0\), and \(0\le\rho<1\),

\[
 \operatorname{Stab}_\rho(B)
 \le\alpha\min\left\{1,\frac6{\sqrt{(1-\rho)R}}\right\}.
\tag{6}
\]

Here stability is \(\mathbb E B(X)B(Y)\), without centering.

### A bounded-weight interval concentration estimate

If \(Z=\sum_j b_jX_j\), independent unbiased signs, \(|b_j|\le w\), and
\(v=\sum_j b_j^2>0\), then for every center \(t\),

\[
 \Pr(|Z-t|\le w)\le\min\{1,3w/\sqrt v\}.
\tag{7}
\]

For a direct Fourier proof, use
\(K(u)=(\sin(u/(2w))/(u/(2w)))^2\). On \(|u|\le w\), \(K(u)>9/10\),
because \(\sin s/s\ge1-s^2/6\ge23/24\) on \(|s|\le1/2\). The identity

\[
 K(u)=w\int_{-1/w}^{1/w}(1-w|t|)e^{itu}\,dt
\]

follows by integrating the triangular kernel. For \(|t|\le1/w\), each
\(|b_jt|\le1\), and \(|\cos(b_jt)|\le e^{-b_j^2t^2/2}\). Hence

\[
 \begin{aligned}
 \Pr(|Z-t_0|\le w)
 &\le\tfrac{10}{9}\mathbb E K(Z-t_0)\\
 &\le\tfrac{10}{9}w\int_{-1/w}^{1/w}
        |\mathbb E e^{itZ}|\,dt\\
 &\le\tfrac{10}{9}w\int_{\mathbb R}e^{-vt^2/2}\,dt
 <3w/\sqrt v.
 \end{aligned}
\]

The bound is uniform in the center and permits atoms and endpoint ties.

### Apply concentration after a random resampling mask

To produce \(\rho\)-correlated \(X,Y\), independently keep each coordinate
of \(X\) with probability \(\rho\); otherwise resample a fresh unbiased
sign. Let \(J\) be the set of resampled coordinates and
\(V_J=\sum_{j\in J}a_j^2\). Conditional on \((J,X)\), the retained
coordinates only change the slab center. Its half-width stays \(w\), so (7)
gives

\[
 \Pr(B(Y)=1\mid J,X)\le\min\{1,3w/\sqrt{V_J}\},
\]

with upper bound 1 when \(V_J=0\).

Put \(\varepsilon=1-\rho\) and \(\mu=\varepsilon R\). A weighted
Bernoulli Chernoff bound gives

\[
 \Pr(V_J<\varepsilon\sigma^2/2)\le e^{-\mu/8}.
\tag{8}
\]

For completeness, scale summands by \(w^2\), so they lie in \([0,1]\).
For \(u\in[0,1]\), \(e^{-u}\le1-(1-e^{-1})u\). Exponential Markov with
parameter 1 yields an upper bound
\(\exp[-((1-e^{-1})-1/2)\mu]\le e^{-\mu/8}\).

On the good-mask event, conditional slab probability is at most
\(3\sqrt2/\sqrt\mu\). Crucially, \(J\) is independent of \(X\), and
the good/bad condition depends only on \(J\). Thus

\[
 \begin{aligned}
 \operatorname{Stab}_\rho(B)
 &=\mathbb E_{J,X}\left[B(X)\Pr(B(Y)=1\mid J,X)\right]\\
 &\le\alpha\left[\frac{3\sqrt2}{\sqrt\mu}+e^{-\mu/8}\right]
 \le\frac{6\alpha}{\sqrt\mu}.
 \end{aligned}
\]

The final inequality uses
\(\sup_{u>0}\sqrt u e^{-u/8}=2e^{-1/2}\), whose addition to
\(3\sqrt2\) is less than 6. The trivial stability bound is \(\alpha\).
This proves (6). For \(R=0\) we use only the trivial bound
\(\operatorname{Stab}_\rho(B)\le\alpha\).

## 3. Low-degree mass for the normalized slab spectrum

Let \(Q_S=\widehat B(S)^2/\alpha\), a probability law. Write \(K=|S|\)
under this law. We shall prove

\[
 \boxed{Q(K\le k)\le18\sqrt{k/M}\quad(k\ge1).}\tag{9}
\]

First suppose \(R>0\). Choose \(\rho=1-1/(2k)\). For integer \(k\ge1\),
\(\rho^k\ge1/2\), so (6) implies

\[
 Q(K\le k)\le2\operatorname{Stab}_\rho(B)/\alpha
 \le12\sqrt{2k/R}<18\sqrt{k/R}.
\tag{10}
\]

For real \(k\ge1\), replace it by \(\lfloor k\rfloor\).

Independently, Bonami–Beckner hypercontractivity gives the standard small-set
expansion bound \(\operatorname{Stab}_\rho(B)\le\alpha^{2/(1+\rho)}\).
Indeed, at \(\rho=1/2\),
\[
 \operatorname{Stab}_{1/2}(B)=\|T_{1/\sqrt2}B\|_2^2
 \le\|B\|_{3/2}^2=\alpha^{4/3}.
\]
This precise uniform-cube inequality is stated and proved in O'Donnell's
2021 book edition, Section 9.5, Small-Set Expansion Theorem (printed
page 264). Consequently

\[
 Q(K\le k)\le2^k\alpha^{1/3}.
\tag{11}
\]

If \(L\ge2\ln2\), then \(\ln(1/\alpha)\ge L-\ln2\ge L/2\). For
\(1\le k\le L/(12\ln2)\), (11) is at most \(e^{-L/12}\), hence at
most \(1.5\sqrt{k/L}\) because
\(\sup_{L>0}\sqrt L e^{-L/12}=\sqrt6 e^{-1/2}<1.5\).
For \(k>L/(12\ln2)\), the trivial bound 1 is at most
\(3\sqrt{k/L}\). For \(L<2\ln2\) the same trivial bound works for all
\(k\ge1\). Therefore

\[
 Q(K\le k)\le3\sqrt{k/L}.
\tag{12}
\]

If \(M=R\), use (10); if \(M=L\), use (12); if \(M=1\), the trivial
bound is enough. This proves (9), including \(R=0\). The zero-degree mass
is known exactly:

\[
 Q(K=0)=\widehat B(\varnothing)^2/\alpha=\alpha.
\tag{13}
\]

## 4. Degree tails for the full split-pair spectrum

Let \(P_S=\widehat A(S)^2+\widehat B(S)^2\). The pointwise identity
\(A^2+B^2=1\) gives \(\sum_S P_S=1\). Its degree is the degree in the
remaining coordinates. For each \(S\), the two full-function spectral
coefficients are \(\widehat A(S)\) at \(S\), and \(\widehat B(S)\) at
\(S\cup\{i\}\). Hence

\[
 P(|S|\ge u)\le\Pr_{\widehat f^2}(|T|\ge u).
\]

The noise-tail calculation from (5) gives for every real \(u>0\)

\[
 P(|S|\ge u)\le A_0p\sqrt{L/u},\qquad
 A_0=\frac{20.5\sqrt2}{1-e^{-1}}<46.
\tag{14}
\]

For \(u\ge1\), take \(\varepsilon=1/(2u)\), so
\[
 2\operatorname{NS}_\varepsilon(f)
 =\sum_T\widehat f(T)^2[1-(1-2\varepsilon)^{|T|}].
\]
Every contributing full degree at least \(u\) has the bracket at least
\(1-e^{-1}\), since \((1-1/u)^u\le e^{-1}\). Applying (5) then yields
(14). For \(u<1\), the full
nonconstant mass is \(4p(1-p)\le4p\), and
\(A_0\sqrt{\ln2}>4\). Thus the estimate includes small \(u\) without
discarding the zero-degree exception improperly.

Combining (14) and (4) gives

\[
 P(|S|\ge u)\le\Gamma\alpha\sqrt{M/u},\qquad
 \Gamma=\max\{1,\sqrt2 A_0/c\}.
\tag{15}
\]

## 5. Dyadic coarse-graining forces KL separation

Both laws below have finite support. We use \(0\log(0/p)=0\) and omit
zero-mass summands. Keep degree zero as a special atom \(\star\).
For every positive degree,
define \(J=\lfloor\log_2(K/M)\rfloor\in\mathbb Z\). Let \(Q_j,P_j\)
be the probabilities of this bin under the slab law and split-pair law.

The lower endpoint of bin \(j\) is \(M2^j\), so (15) gives

\[
 P_j\le\Gamma\alpha2^{-j/2}\quad(j\in\mathbb Z).
\tag{16}
\]

For \(j<0\), the upper endpoint is \(M2^{j+1}\). If this is less than 1,
the positive-degree bin is empty. Otherwise (9) implies

\[
 Q_j\le18\sqrt2\,2^{j/2}.
\]

Therefore

\[
 \mathbb E_Q[|J|\mathbbm1_{J<0}]
 \le C_-:=18\sqrt2\sum_{m=1}^\infty m2^{-m/2}<\infty.
\tag{17}
\]

There is no required upper-tail bound on \(Q\).

Set \(r=2^{-1/4}\), \(Z=\sum_{j\in\mathbb Z}2^{-|j|/4}=(1+r)/(1-r)\),
and choose the reference law

\[
 R^{\rm ref}_\star=\tfrac12,\qquad
 R^{\rm ref}_j=\frac{2^{-|j|/4}}{2Z}.
\]

In this paragraph \(Q^{\rm bin},P^{\rm bin}\) are the coarse bin laws, and
\(R^{\rm ref}\) is the reference law just defined. Nonnegativity of
\(D(Q^{\rm bin}\|R^{\rm ref})\) gives

\[
 D(Q^{\rm bin}\|P^{\rm bin})\ge\sum_{j\in\mathbb Z\cup\{\star\}}
     Q_j\log\frac{R^{\rm ref}_j}{P_j}.
\tag{18}
\]

For positive-degree bins, (16) gives

\[
 \log\frac{R^{\rm ref}_j}{P_j}
 \ge\log\frac1\alpha-\log(2Z\Gamma)
      +\tfrac12j-\tfrac14|j|.
\]

The last two terms are nonnegative for \(j\ge0\) and equal \(3j/4\) for
\(j<0\). Also \(Q_\star=\alpha\), \(P_\star\le1\), so its contribution
to (18) is at least \(-\alpha\). Therefore

\[
 D(Q^{\rm bin}\|P^{\rm bin})\ge(1-\alpha)\log\frac1\alpha
             -\log(2Z\Gamma)-\tfrac34 C_- -\alpha.
\]

Since \(\alpha\log_2(1/\alpha)\le(\log_2e)/e\), this proves

\[
 \boxed{D(Q^{\rm bin}\|P^{\rm bin})\ge\log_2(1/\alpha)-C_D,}\tag{19}
\]

The constant \(C_D\) is the one defined with the theorem. By the log-sum
inequality (KL data processing), the individual-subset laws satisfy
\[
 D(Q\|P)\ge D(Q^{\rm bin}\|P^{\rm bin})
 \ge\log_2(1/\alpha)-C_D.
\]
Thus coarse-graining supplies the required lower bound, in the correct
direction, without claiming an individual-degree lower mass bound.
There is no division
by a vanishing \(P_j\) on the support of \(Q_j\), since pointwise
\(P_S\ge\widehat B(S)^2=\alpha Q_S\).

## 6. Conditional spectral-bit entropy and the split increment

Let \(q_S=\widehat B(S)^2/P_S\). The conditional entropy of inclusion of
coordinate \(i\), given the other spectral coordinates, is

\[
 \mathcal C=\sum_S P_Sh_2(q_S).
\]

The contribution where \(i\) is included is exactly

\[
 \sum_S\widehat B(S)^2\log\frac{P_S}{\widehat B(S)^2}
 =\alpha\left[\log\frac1\alpha-D(Q\|P)\right].
\]

The other contribution is at most \(\alpha\log_2e\), by
\(\ln(1+t)\le t\). Thus (19) gives

\[
 \mathcal C\le\alpha(C_D+\log_2e).
\tag{20}
\]

For completeness, derive the split identity one coefficient pair at a time.
Fix \(S\) and write \(a=\widehat A(S)\), \(b=\widehat B(S)\),
\(P=a^2+b^2\). Its two full-function spectral masses are \(a^2,b^2\),
so their entropy contribution is \(-P\log_2P+Ph_2(q)\), with
\(q=b^2/P\). The two restricted coefficients are \(a+b,a-b\);
their average entropy contribution is
\(-P\log_2(2P)+Ph_2(r)\), with \(r=(a+b)^2/(2P)\).
Subtracting and summing gives

\[
 \Delta_iH(f)=\sum_S P_S[1+h_2(q_S)-h_2(r_S)],\qquad
 r_S=\frac{(\widehat A(S)+\widehat B(S))^2}{2P_S}.
\]

Since \(r_S(1-r_S)=(1-2q_S)^2/4\), the elementary inequality
\(h_2(t)\ge4t(1-t)\) implies
\(1-h_2(r_S)\le4q_S(1-q_S)\le h_2(q_S)\). Hence

\[
 \Delta_iH(f)\le2\mathcal C
 \le2(C_D+\log_2e)\alpha.
\tag{21}
\]

To verify that binary-entropy inequality, expand
\[
 1-h_2((1+x)/2)=\frac1{\ln2}\sum_{m\ge1}
 \frac{x^{2m}}{(2m)(2m-1)}.
\]
The coefficients are positive and sum to 1 (evaluate at \(x=1\)). Since
\(x^{2m}\le x^2\) on \([-1,1]\), the series is at most \(x^2\),
which is equivalent to the claimed inequality. Boundary values follow by
continuity.

This proves the split theorem (1) with the universal \(C_*\) given above.

## 7. Dimension induction

Proceed by induction on \(n\). A zero-variable function is constant and has
\(H=I=0\); a constant in any dimension has the same values. Suppose the
theorem holds in all smaller dimensions and \(f\) is nonconstant. Delete
zero-weight coordinates and choose any largest absolute input-weight
coordinate \(i\). Both restrictions \(f^+,f^-\) are LTFs in \(n-1\)
variables, including when a restriction is constant. The inductive
hypotheses and (1) imply
\[
 \begin{aligned}
 H(f)
 &\le C_*I_i(f)+\tfrac12[H(f^+)+H(f^-)]\\
 &\le C_*\left(I_i(f)+\tfrac12[I(f^+)+I(f^-)]\right)\\
 &=C_*I(f).
 \end{aligned}
\]
The last identity follows by conditioning each other coordinate's physical
flip influence on the value of \(x_i\). The constant is uniform in dimension,
weights, and threshold, so it applies anew at each restriction. This proves
(T) for every Boolean LTF under uniform input.

If one splits on an unused coordinate instead, \(\alpha=0\), the restrictions
coincide, and the split increment is exactly zero. The proof never defines
\(Q\) when \(\alpha=0\). On a largest nonzero weight of a nonconstant
function, \(\alpha>0\) follows from (3).

## 8. Source and scope record

The only established non-elementary inputs are the following.

* Nathan Keller and Ohad Klein, *Biased halfspaces, noise sensitivity, and
  local Chernoff inequalities*, Discrete Analysis 2019:13, Theorem 1.4:
  <https://arxiv.org/html/1710.07429v3>. Input weights, excluding the bias,
  are normalized by their Euclidean norm. Their influence is explicitly
  the physical flip probability, equal for the indicator halfspace and
  its \(\{-1,1\}\)-valued version. We use its lower bound only.
* Adam Klivans, Ryan O'Donnell, and Rocco Servedio, *Learning intersections
  and thresholds of halfspaces*, Journal of Computer and System Sciences
  68 (2004), 808–840, Theorem 18, available in the authors' full manuscript:
  <https://www.cs.columbia.edu/~rocco/Public/focs02.pdf>. We use its
  minority-density noise-sensitivity upper bound with independent bit
  flips of probability \(\varepsilon\).
* Ryan O'Donnell, *Analysis of Boolean Functions*, May 2021 arXiv edition,
  Section 9.5, Small-Set Expansion Theorem, printed page 264:
  <https://www.cs.cmu.edu/~odonnell/papers/Analysis-of-Boolean-Functions-by-Ryan-ODonnell.pdf>.
  We use the uniform-cube indicator stability estimate at \(\rho=1/2\).

The argument developed here is the largest-weight pivotal-slab concentration/stability
estimate and the dyadic relative-entropy separation that converts the
conditional spectral inclusion entropy to \(O(I_i)\). Its proof is complete
above. Internal independent analytic audits and finite stress tests are
recorded in companion files. Those checks do not establish research priority
or replace external mathematical review. The unrestricted Boolean FEI
conjecture and nonuniform input versions are outside the proved theorem.

Companion audit records are the [root audit](largest_weight_ltf_root_audit.md),
[independent adversarial audit](largest_weight_ltf_independent_audit.md),
[heat/entropy audit](largest_weight_ltf_heat_audit.md), and
[probability audit](largest_weight_ltf_probability_audit.md).
The [prior-art checkpoint](largest_weight_ltf_prior_art_checkpoint.md)
records the literature search and its limits.

The separate [stress checker](verify_largest_weight_ltf.py) and
[results](largest_weight_ltf_verification.json) check 1,632 LTF truth tables
through dimension 16, including exact threshold atoms, zero remaining
weights, very unequal weights, and minority densities down to \(2^{-16}\).
They check 13,056 slab stability inequalities, 18,022 low-degree inequalities,
22,814 pair-spectrum tail inequalities, and the dyadic KL and exact split
identities. The maximum split-identity numerical error was below
\(2\times10^{-14}\). All tested weights are integers and their score sums are
exactly represented, so threshold atoms do not create spurious non-LTF truth
tables through floating-point summation. An additional independently written
[probe](independent_largest_weight_probe.py) checks 1,642 examples.
