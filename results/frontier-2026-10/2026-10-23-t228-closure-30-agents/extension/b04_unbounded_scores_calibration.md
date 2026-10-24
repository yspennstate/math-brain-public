# Unbounded score scales: exact calibration, label-noise bounds, and limit order

24 October 2026. B04. Extension work only; no frozen fullproof file is
modified.

**Results.** Relative coefficient delocalization gives a Gaussian
approximation after score normalization, uniformly over arbitrary score
magnitudes. This yields a strictly positive exact-calibration floor for
all standard-deviation scales above any fixed positive threshold,
including scales tending to infinity. At infinite scale, Gaussian CE and
signed overconfidence both tend to classification error, while logistic
risk diverges linearly.

A stronger late-time obstruction does not require delocalization or a
Gaussian score law: in the original Gaussian tanh RF model, every
coefficient vector above an explicit fixed norm threshold has a positive
calibration lower bound, simultaneously over all such vectors. The same
small-ball and label-noise argument gives a linear lower bound for
population logistic risk. This supplies the large-norm part of an
all-time stopping theorem without an all-time Gaussian approximation.

## 1. Setup and conventions

Let \(X\sim N(0,I_d)\), \(Z=\theta^\top X\), \(\|\theta\|=1\), and
\(Y\mid X\sim\operatorname{Bernoulli}(p(Z))\), with
\(p(z)=\sigma(\beta z)\) and fixed finite \(\beta\ge0\). Conditional
on a trained-model environment, a score is

\[
S_b(X)=b^\top\tanh(FX),\qquad b\in\mathbb R^m.
\tag{1.1}
\]

The fresh input is independent of that environment. All quantities below
are conditional population quantities unless an outer probability over
the environment is specified. Write

\[
Q_b=\mathbb E S_b^2,\qquad A_b=\mathbb E[ZS_b],\qquad
a_b=\sqrt{Q_b},\qquad r_b=A_b/a_b,
\qquad T_b=S_b/a_b
\tag{1.2}
\]

for \(b\ne0\). Thus \(a_b\) is the score standard deviation and
\(T_b\) has variance one. These symbols are distinct from the feature
Hermite coefficient \(a_1=\mathbb E[G\tanh G]\).

The exact calibration error and signed overconfidence are

\[
\operatorname{CE}(S)=
 \mathbb E\left|\mathbb E[Y\mid S]-\sigma(S)\right|,
\qquad
\operatorname{OC}(S)=
 \mathbb E[(\sigma(S)-Y)\operatorname{sign}S],
\tag{1.3}
\]

with \(\operatorname{sign}0=0\). The score-measurable witness bound is

\[
\operatorname{CE}(S)\ge
\left|\mathbb E[(\sigma(S)-p(Z))w(S)]\right|
\quad\text{for every measurable }|w|\le1.
\tag{1.4}
\]

Total variation uses the norm
\(\|\mu-\nu\|_{\rm TV}=\sup_{|f|\le1}|\mu f-\nu f|\), bounded by
two for probability measures.

For Gaussian RF rows \(W_j\sim N(0,I_d/d)\), with
\(m/d\to\gamma\in(0,\infty)\), there are fixed \(L<\infty\) and
\(s>0\) such that, with probability tending to one, simultaneously for
all coefficient vectors,

\[
\|F\|_{\rm op}\le L,\qquad
Q_b-A_b^2\ge s\|b\|_2^2.
\tag{1.5}
\]

One may use \(s=\nu/2\), where
\(\nu=\mathbb E\tanh^2G-a_1^2>0\), and a sufficiently large fixed
Gaussian-matrix norm bound \(L\). The exact Hermite decomposition in
`fullproof/b04_calibration_transfer.md`, equation (3.7), proves (1.5)
uniformly in data-dependent \(b\). Gaussian Poincare also gives

\[
s\|b\|_2^2\le Q_b\le L^2\|b\|_2^2,
\qquad
|r_b|\le r_*:=\sqrt{1-s/L^2}<1.
\tag{1.6}
\]

The large-norm small-ball argument in Section 5 only needs the weaker
condition \(Q_b\ge s\|b\|_2^2\), not the teacher-orthogonal bound in
(1.5).

## 2. Scale-free Gaussian approximation, uniform over readouts and times

**Theorem 2.1.** Fix \(L,s\) as in (1.5). There is a deterministic
modulus \(\omega_{L,s}(\eta)\downarrow0\) as \(\eta\downarrow0\)
such that every nonzero readout satisfying (1.5) obeys

\[
\left\|\mathcal L(Z,T_b)-N\!\left(0,
 \begin{pmatrix}1&r_b\\r_b&1\end{pmatrix}\right)\right\|_{\rm TV}
\le\omega_{L,s}\left(\frac{\|b\|_\infty}{\|b\|_2}\right).
\tag{2.1}
\]

The modulus is uniform over dimensions, feature matrices satisfying the
displayed bounds, coefficient norms, and training procedures.

**Proof.** Normalize the coefficient vector by \(\|b\|_2\). The
resulting odd function has gradient bounded by \(L\), Hessian
Hilbert--Schmidt norm bounded by \(2L^2\), Hessian operator norm bounded
by \(2L^2\|b\|_\infty/\|b\|_2\), and teacher-orthogonal variance
at least \(s\). The deterministic small-Hessian TV theorem in
`fullproof/b04_calibration_transfer.md`, Theorem 2.1, applies. Its proof
is dimension-free. Uniformity follows by contradiction: a sequence
violating a vanishing modulus would itself satisfy that theorem's fixed
derivative and variance bounds, with Hessian operator norm tending to
zero. Finally rescale the second coordinate by its positive standard
deviation. Total variation is unchanged under this invertible map.
\(\square\)

Let \(\mathcal I_d\) be any countable collection of times or
training-measurable readouts. Suppose

\[
\sup_{t\in\mathcal I_d}
 \frac{\|b_{t,d}\|_\infty}{\|b_{t,d}\|_2}\longrightarrow0
\quad\text{in probability},\qquad b_{t,d}\ne0,
\tag{2.2}
\]

and (1.5) holds with probability tending to one. Then (2.1) holds
uniformly over \(t\in\mathcal I_d\), in probability. No upper bound on
\(\sup_t\|b_{t,d}\|_2\) is required. A continuous-time family can be
handled through a countable dense set when its score laws and
coefficients have the relevant path continuity.

Condition (2.2) is a real additional hypothesis. Fixed-time coordinate
delocalization does not prove it over infinitely many times. The
large-norm theorem in Section 5 bypasses this hypothesis for a
calibration lower bound.

## 3. Gaussian calibration over the entire scale range

Let \((Z,T)\) be standard bivariate normal with correlation \(r\), and
put

\[
g_r(t)=\mathbb E_H\sigma\{\beta(r t+\sqrt{1-r^2}H)\}.
\]

For scale \(a>0\), define

\[
C_\beta(a,r)=\mathbb E_T|g_r(T)-\sigma(aT)|,
\]
\[
O_\beta(a,r)=
\mathbb E_T[(\sigma(aT)-g_r(T))\operatorname{sign}T].
\tag{3.1}
\]

Because the calibration functional is Lipschitz in joint TV with the
forecast link held fixed, (2.1) implies, uniformly in **all** scales,

\[
|\operatorname{CE}(S_b)-C_\beta(a_b,r_b)|
\le\omega_{L,s}(\|b\|_\infty/\|b\|_2),
\]
\[
|\operatorname{OC}(S_b)-O_\beta(a_b,r_b)|
\le\omega_{L,s}(\|b\|_\infty/\|b\|_2).
\tag{3.2}
\]

The test functions may depend on the environment through \(a_b\): the
TV norm already takes the supremum over all bounded measurable tests.
There is no forbidden substitution of a dimension-dependent witness
into a merely weak-convergence theorem.

### 3.1 Exact large-scale limits

Let \(e_\beta(r)\) be the error of the classifier
\(\mathbf1_{\{T>0\}}\):

\[
e_\beta(r)=\mathbb E[1-g_r(|T|)]
 =\tfrac12-\mathbb E[(p(Z)-\tfrac12)\operatorname{sign}T].
\tag{3.3}
\]

The irreducible Bayes error is

\[
e_{\rm B}=\mathbb E\sigma(-\beta|Z|)>0,
\qquad e_\beta(r)\ge e_{\rm B}\quad(-1\le r\le1).
\tag{3.4}
\]

Define the confidence deficit

\[
d(a)=\mathbb E\sigma(-a|T|).
\]

Symmetry gives the exact identity and bound

\[
\boxed{\quad
O_\beta(a,r)=e_\beta(r)-d(a),\qquad
|C_\beta(a,r)-e_\beta(r)|\le d(a).
\quad}
\tag{3.5}
\]

For the second inequality, replace \(\sigma(aT)\) by
\(\mathbf1_{\{T>0\}}\) inside the absolute value and use the reverse
triangle inequality. The replacement's expected error is exactly
\(d(a)\). Its folded-normal integral gives

\[
d(a)\le\frac{\sqrt{2/\pi}\log2}{a},
\qquad
a\,d(a)\longrightarrow\sqrt{2/\pi}\log2.
\tag{3.6}
\]

Hence, uniformly over every \(r\in[-1,1]\),

\[
C_\beta(a,r)\to e_\beta(r),\qquad
O_\beta(a,r)\to e_\beta(r)
\quad(a\to\infty).
\tag{3.7}
\]

In particular, if
\(a\ge2\sqrt{2/\pi}\log2/e_{\rm B}\), both CE and signed OC are at
least \(e_{\rm B}/2\). Signed OC need not be positive at smaller
scales; exact CE is the quantity with a positive all-scale floor below.

No continuity of conditional regression under the hard-prediction limit
is assumed. At finite \(a\), conditioning on the forecast retains the
whole value of \(T\); at \(a=\infty\), the forecast only retains its
sign. Inequality (3.5) directly controls CE despite this change of
sigma-field.

### 3.2 A uniform calibration floor on every interval \([a_0,\infty]\)

**Proposition 3.2.** For fixed \(a_0>0\), finite \(\beta\ge0\), and
\(r_*<1\),

\[
\boxed{\quad
c_*(\beta,a_0,r_*):=
\inf_{\substack{a\ge a_0\\|r|\le r_*}}C_\beta(a,r)>0.
\quad}
\tag{3.8}
\]

**Proof.** The function is continuous for finite \(a>0\) and
\(|r|<1\), by bounded convergence. It is strictly positive everywhere
on this domain. If \(\beta=0\) or \(r=0\), the regression is \(1/2\)
and the forecast is nonconstant. If \(\beta>0,r<0\), the regression
decreases and the forecast increases. If \(\beta>0,r>0\), perfect
calibration would imply, for all \(t\),
\(\mathbb E\sigma(\beta r t+\beta\sqrt{1-r^2}H)=\sigma(at)\).
As \(t\to+\infty\), comparison of the two tails first forces
\(a=\beta r\), then forces
\(\exp\{\beta^2(1-r^2)/2\}=1\), a contradiction.

Equations (3.5)--(3.6) extend \(C_\beta\) continuously to
\(a=\infty\), uniformly in \(r\), with the strictly positive value
\(e_\beta(r)\). The compactification of
\([a_0,\infty]\times[-r_*,r_*]\) is compact, so its minimum is
strictly positive. Equivalently, use the lower bound
\(e_{\rm B}/2\) beyond the explicit threshold following (3.7), and
the positive compact minimum below that threshold. \(\square\)

Combining (2.2), (3.2), and (3.8) proves an all-time CE floor whenever
\(\inf_t a_{t,d}\ge a_0\) with probability tending to one. There is
no upper-scale or upper-coefficient-norm restriction in this corollary.

### 3.3 Risk: a uniform slope limit, not automatically an absolute proxy

Let
\(\kappa=\mathbb E[Z\{p(Z)-1/2\}]\). The Gaussian population
logistic risk has the exact form

\[
\begin{aligned}
L_\beta(a,r)
 &=\mathbb E\log\{2\cosh(aT/2)\}-a\kappa r\\
 &=a\left(\frac1{\sqrt{2\pi}}-\kappa r\right)
       +j(a),\qquad
j(a)=\mathbb E\log(1+e^{-a|T|}).
\end{aligned}
\tag{3.9}
\]

The remainder is independent of \(r\), and

\[
0\le j(a)\le
 \frac{\sqrt{2/\pi}\,\pi^2}{12a},
\qquad
a\,j(a)\to\sqrt{2/\pi}\,\pi^2/12.
\tag{3.10}
\]

These follow by scaling the folded-normal integral and
\(\int_0^\infty\log(1+e^{-x})\,dx=\pi^2/12\).
For finite \(\beta\),

\[
\frac1{\sqrt{2\pi}}-\kappa
 =\mathbb E[|Z|\sigma(-\beta|Z|)]>0.
\tag{3.11}
\]

Thus risk diverges linearly as \(a\to\infty\), uniformly over
\(r\in[-1,1]\).

The normalized RF scores in (2.1) have uniformly bounded fourth moments:

\[
\mathbb E T_b^4\le5L^4/s^2.
\tag{3.12}
\]

If \(\epsilon\) denotes the TV error in (2.1), truncating at
\(|T|\le R\) shows, uniformly for \(a\ge a_0>0\),

\[
\left|\frac{L(S_b)}{a_b}
            -\frac{L_\beta(a_b,r_b)}{a_b}\right|
\le (R+\log2/a_0)\epsilon+\frac{C(L,s)}{R^3}.
\tag{3.13}
\]

Here the normalized loss is bounded by \(|T|+\log2/a_0\); its tail
has the stated bound from (3.12). The same standard-normal fourth-moment
bound controls the Gaussian tail. Choosing \(R\) of order
\(\epsilon^{-1/4}\) gives a vanishing bound of order
\(O(\epsilon^{3/4})\), with an additional \(O(\epsilon)\) term.
Consequently relative delocalization proves a **normalized-risk**
approximation uniformly over unbounded scales.

An absolute risk difference need not tend to zero when \(a_b\) diverges
arbitrarily rapidly: the bound is multiplied by \(a_b\). An absolute
proxy requires an additional rate condition. This distinction does not
affect CE or OC because they are bounded functionals.

## 4. What irreducible label noise proves without Gaussian score laws

All statements in this section apply to arbitrary measurable scores
\(S(X)\), with no RF or Gaussian-score assumption. At score zero use a
fair independent coin for the predicted class. Let \(e(S)\) be its
classification error and \(d(S)=\mathbb E\sigma(-|S|)\).

**Lemma 4.1 (confidence deficit).**

\[
\operatorname{OC}(S)=e(S)-d(S),\qquad
|\operatorname{CE}(S)-e(S)|\le d(S),
\]
\[
\boxed{\quad
\operatorname{CE}(S)\ge\operatorname{OC}(S)
\ge e_{\rm B}-\mathbb E\sigma(-|S|).
\quad}
\tag{4.1}
\]

**Proof.** On \(S\ne0\), the conditional error of the sign classifier
is \(p(Z)\) for \(S<0\) and \(1-p(Z)\) for \(S>0\). Subtracting
\(\sigma(-|S|)\) gives
\((\sigma(S)-p(Z))\operatorname{sign}S\). At zero the fair-coin
error and deficit both equal \(1/2\), so the identity still holds.
For CE, condition on \(S\) and compare the forecast with the appropriate
endpoint zero or one by the reverse triangle inequality. At zero the
same bound follows from \(0\le|\mathbb E[Y\mid S=0]-1/2|\le1/2\).
The witness (1.4) gives CE at least OC, and any classifier has error at
least the Bayes error. \(\square\)

If \(|S_k|\to\infty\) in probability under the test distribution,
then \(d(S_k)\to0\), by boundedness. Therefore

\[
\operatorname{CE}(S_k)-e(S_k)\to0,
\qquad \operatorname{OC}(S_k)-e(S_k)\to0,
\quad \liminf_k\operatorname{CE}(S_k)\ge e_{\rm B}.
\tag{4.2}
\]

If the classification errors converge to \(e_*\), both CE and OC
converge to \(e_*\). If the errors oscillate, noise alone does not
create an exact common limit.

There is also an exact loss identity:

\[
L(S)=\mathbb E\left[
 |S|\,e(X;\operatorname{sign}S)
 +\log(1+e^{-|S|})\right],
\tag{4.3}
\]

where the pointwise error is as above. It is at least
\(\sigma(-\beta|Z|)\). Thus \(|S_k|\to\infty\) in probability
implies \(L(S_k)\to\infty\). Indeed, for every \(\eta>0\), first
choose \(\zeta>0\) so that
\(\Pr\{\sigma(-\beta|Z|)\le\zeta\}<\eta\); then use divergence
of \(|S_k|\) to show their product diverges in probability. Truncation
from below at an arbitrary constant makes its expectation diverge.

### 4.1 Unbounded moments alone are insufficient

Let \(A_k\) be an event independent of \(Z\), of probability
\(\varepsilon_k=k^{-3}\), and set

\[
S_k=\begin{cases}
k^2,&A_k,\\
\beta Z,&A_k^c.
\end{cases}
\tag{4.4}
\]

For \(\beta>0\), the continuous score off \(A_k\) is exactly
calibrated. The atom at \(k^2\) has teacher mean \(1/2\), so

\[
\operatorname{CE}(S_k)
 =k^{-3}|\sigma(k^2)-1/2|\to0,
\quad \mathbb E S_k^2\sim k\to\infty.
\]

Moreover
\(L(S_k)\to\mathbb E\,h(\sigma(\beta Z))\), the Bayes logistic
risk, since the exceptional loss contributes only \(O(k^{-1})\).
For \(\beta=0\), replace the baseline by zero and the same example
works. Thus there is no noise-only calibration floor or population-risk
divergence conclusion from an unbounded \(L^2\) score norm alone.
Distributional spread or high confidence on a nonvanishing mass is
essential. This example is a limitation for arbitrary measurable scores,
not a construction in the fixed-proportional RF span.

## 5. A pathwise large-norm RF floor without delocalization

This argument was developed in coordination with B02/B06 and is supplied
here independently with explicit constants.

**Theorem 5.1 (all readouts above a fixed norm threshold).** Suppose

\[
\|F\|_{\rm op}\le L,\qquad
\mathbb E_X[h(X)h(X)^\top]\succeq s I_m,
\quad h(X)=\tanh(FX),
\tag{5.1}
\]

with fixed \(L,s>0\). Define

\[
\kappa_0=\sqrt{s/2},\qquad
p_0=\frac{s^2}{20L^4},\qquad
B_0=\sqrt{2\log(4/p_0)},\qquad
q_0=\sigma(-\beta B_0),
\]
\[
C_0=\log\frac4{q_0p_0},\qquad
R_0=C_0/\kappa_0,\qquad
\varepsilon_0=q_0p_0/4,\qquad
\ell_0=q_0\kappa_0p_0/2.
\tag{5.2}
\]

Then, simultaneously for every coefficient vector,

\[
\boxed{\quad
\|b\|_2\ge R_0\ \Longrightarrow\
\operatorname{CE}(S_b)\ge\varepsilon_0>0,
\quad}
\tag{5.3}
\]

and

\[
\boxed{\quad
\ell_0\|b\|_2\le L(S_b)
                       \le\log2+L\|b\|_2.
\quad}
\tag{5.4}
\]

There is no assumption on coefficient delocalization, coefficient upper
norm, training time, or how \(b\) was selected.

**Proof.** Oddness makes \(S_b\) centered. Poincare applied to its
square gives

\[
\mathbb E S_b^2\ge s\|b\|_2^2,
\qquad
\mathbb E S_b^4\le5L^4\|b\|_2^4.
\]

Paley--Zygmund applied to \(S_b^2\) therefore gives the uniform
small-ball inequality

\[
\Pr\{|S_b|\ge\kappa_0\|b\|_2\}\ge p_0.
\tag{5.5}
\]

The standard Gaussian tail bound gives
\(\Pr\{|Z|>B_0\}\le p_0/2\). No independence between \(S_b\) and
\(Z\) is needed: subtracting this exceptional mass leaves probability
at least \(p_0/2\) in the joint event
\(\{|S_b|\ge\kappa_0\|b\|_2,\ |Z|\le B_0\}\).

For \(\|b\|_2\ge R_0\), choose the score-measurable witness

\[
w(S)=\operatorname{sign}S\,
                       \mathbf1_{\{|S|\ge C_0\}}.
\]

Its expectation is a localized signed error, and (4.3)'s pointwise error
identity gives

\[
\begin{aligned}
\mathbb E[(\sigma(S_b)-p(Z))w(S_b)]
 &=\mathbb E[(e(X;\operatorname{sign}S_b)
            -\sigma(-|S_b|))\mathbf1_{\{|S_b|\ge C_0\}}]\\
 &\ge q_0\Pr\{|S_b|\ge C_0,\ |Z|\le B_0\}
                      -\sigma(-C_0)\\
 &\ge q_0p_0/2-q_0p_0/4=\varepsilon_0.
\end{aligned}
\tag{5.6}
\]

Use (1.4) to obtain (5.3). This is a calibration lower bound; it does
not assert positive **unlocalized** OC for every such coefficient
vector.

For risk, on the joint small-ball event above the conditional loss is at
least \(q_0|S_b|\), by (4.3). This proves the lower bound in (5.4).
The upper bound follows from \(L(S_b)\le\log2+\mathbb E|S_b|\) and
Poincare's \(\mathbb E S_b^2\le L^2\|b\|_2^2\). \(\square\)

For the original Gaussian tanh RF model, event (5.1) holds with
probability tending to one, for every fixed proportional width ratio.
Thus (5.3)--(5.4) hold on a **single feature event for the entire RF
span**. They apply simultaneously to all GD times, limiting readouts
when finite, and any training-measurable stopping rule whose coefficient
norm is at least \(R_0\).

Consequently, if another theorem proves that all GD iterates after a
deterministic time \(T_0\) have norm at least \(R_0\), with probability
tending to one, then the positive-time calibration floor consists of:

1. the finite collection of exact Gaussian CE limits at times
   \(1,\ldots,T_0\); and
2. the pathwise floor \(\varepsilon_0\) for the entire remaining tail.

This argument needs no relative delocalization over infinitely many
times. If the norms grow beyond every fixed threshold uniformly at late
times, (5.4) also forces population risk to diverge, despite empirical
training loss tending to zero in a separable sample. Any uniformly
risk-competitive stop must then occur in a bounded coefficient ball.

## 6. Dimension/time limits: what can and cannot be exchanged

### 6.1 Triangular late-time limits under uniform relative delocalization

Assume (1.5) and (2.2). For any training-measurable sequence of times
\(t_d\), if

\[
a_{t_d,d}\to\infty,\qquad r_{t_d,d}\to r_\infty
\quad\text{in probability},
\tag{6.1}
\]

then

\[
\operatorname{CE}_{t_d,d},\operatorname{OC}_{t_d,d}
 \longrightarrow e_\beta(r_\infty),
\qquad
\frac{L_{t_d,d}}{a_{t_d,d}}
 \longrightarrow\frac1{\sqrt{2\pi}}-\kappa r_\infty.
\tag{6.2}
\]

The CE/OC conclusions also hold in every finite \(L^p\), by
boundedness. Risk diverges in probability; an (L^1) divergence or a
normalized (L^p) statement requires the relevant outer uniform
integrability. If correlations do not converge, the uniform proxy still
holds with \(e_\beta(r_{t_d,d})\), but an exact deterministic limit
need not exist.

### 6.2 Dimension first, time second

The fixed-time state evolution in the fullproof files gives
deterministic \(a_t,r_t\) at each fixed time. If a separate late-time
argument shows \(a_t\to\infty\) and \(r_t\to r_\infty\), then

\[
\lim_{t\to\infty}\lim_{d\to\infty}\operatorname{CE}_{t,d}
 =e_\beta(r_\infty),
\]

with the analogous OC and normalized-risk statements. Fixed-time
convergence alone does not justify replacing these iterated limits by
an arbitrary triangular sequence \(t=t_d\to\infty\). Uniform
relative delocalization and uniform parameter control would justify
that replacement. For lower bounds only, Theorem 5.1 is sufficient and
strictly less demanding.

### 6.3 Time first in a fixed RF model

At fixed finite \(d,m\), suppose the feature covariance is positive
definite and a coefficient direction converges,

\[
\|b_t\|_2\to\infty,\qquad b_t/\|b_t\|_2\to u_*\ne0.
\tag{6.3}
\]

The nonzero analytic function \(u_*^\top\tanh(Fx)\) has a zero set of
Gaussian measure zero. Thus \(|S_{b_t}(X)|\to\infty\) in probability,
and its sign classifier converges almost surely away from that zero
set. Lemma 4.1 gives

\[
\lim_{t\to\infty}\operatorname{CE}_{t,d}
 =\lim_{t\to\infty}\operatorname{OC}_{t,d}
 =\Pr\{\operatorname{sign}(u_*^\top\tanh(FX))
                           \text{ misclassifies }Y\},
\tag{6.4}
\]

while risk diverges. This limit is the finite-model classifier's error;
identifying its subsequent high-dimensional limit requires information
about its direction. Uniform relative delocalization and correlation
convergence would identify it with (6.2). Without those hypotheses,
neither equality of the two iterated limits nor a Gaussian max-margin
law has been proved here.

Even without direction convergence, positive definite covariance plus
the analytic RF family yields a fixed-dimension uniform anti-concentration
statement

\[
\sup_{\|u\|_2=1}\Pr\{|u^\top\tanh(FX)|\le\epsilon\}
 \longrightarrow0\quad(\epsilon\downarrow0).
\tag{6.5}
\]

To prove it, a violating sequence has a convergent subsequence of unit
directions. Their scores converge pointwise to a nonzero analytic score,
whose zero set has measure zero, contradicting a persistent small-ball
mass at zero. Hence norm divergence alone at fixed dimension implies
confidence saturation, and CE/OC track possibly nonconvergent
classification errors. The constants in (6.5) need not be uniform in
dimension; Theorem 5.1 is the dimension-uniform lower-bound substitute.

## 7. Source search and scope

The requested literature search located the usual confidence-versus-
accuracy formulation in the primary paper by Chuan Guo, Geoff Pleiss,
Yu Sun, and Kilian Weinberger,
[*On Calibration of Modern Neural Networks*, ICML 2017](https://proceedings.mlr.press/v70/guo17a/guo17a.pdf),
Section 2. That paper is used only for context and terminology. It does
not supply the RF-span theorem proved above. Equations (4.1), (5.3), and
(5.4) are derived directly here; no inaccessible paper or absence of a
search result is used as a mathematical premise or a novelty claim.

The scale-free TV input is the fully proved deterministic Gaussian
smoothing theorem in `fullproof/b04_calibration_transfer.md`. Its
extension here is the removal of the coefficient upper-norm restriction
by normalization, together with uniform scale compactification and a
separate bounded-witness argument for large norms.

| Statement | Status |
|---|---|
| Uniform normalized TV for relatively delocalized readouts | Proved. |
| Uniform exact CE floor for all scales \(a\ge a_0\), including infinity | Proved under normalized Gaussian approximation; no norm upper bound. |
| Gaussian large-scale CE/OC limit and risk slope | Proved explicitly and uniformly in correlation. |
| Uniform relative delocalization of arbitrary all-time GD paths | Not assumed to follow from fixed-time bounds; remains a separate dynamical issue. |
| Large-norm CE floor for the entire original RF span | Proved without delocalization or Gaussian-score approximation. |
| Population logistic risk coercivity in coefficient norm | Proved on the same high-probability feature event. |
| Exact interchange of high-dimensional and late-time limits | Requires the stated uniform direction/correlation hypotheses; not inferred from fixed-time SE. |
| Calibration obstruction from arbitrary unbounded score moments alone | False; counterexample (4.4). |
