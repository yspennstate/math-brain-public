# B17 FEI new proof mechanisms — product spectra force Boolean dependence

**Run:** `B17-20260921T101035Z-r27`  
**Status:** PARTIAL; full Fourier entropy–influence (FEI) remains OPEN.  
**Brain label:** WITHOUT_VERIFIED_BRAIN.  
**Fresh source state:** `yspennstate/math-open-problems` master `e7217b10f3760736adfb1fa0542acbfb1f9c85ac`.  
**Live role:** FEI new proof mechanisms.  
**Creative moves used:** FLEET_RULES B2 (attack the negation first), B18 (say it in another language), B24 (find the extremal object).  
**Route:** APPROACHES #13 (Booleanity constraints on the spectral-sample profile), with a quantitative comparison to the product law.  
**Novelty:** no publication-priority claim. The flat-spectrum/bent-function endpoint is classical territory; the exact formulation and quantitative inequality below are recorded as a new-to-this-repository mechanism pending literature review.

## 1. Target obstruction

Let \(f:\{-1,1\}^n\to\{-1,1\}\), and let its spectral sample \(S\) have law
\[
\mu(A)=\widehat f(A)^2.
\]
Write
\[
p_i=\Pr_\mu(i\in S)=\operatorname{Inf}_i(f),\qquad
I(f)=\sum_i p_i.
\]
An arbitrary product law on subsets with many tiny marginals has entropy
\(\sum_i h_2(p_i)\), which can be much larger than a constant times
\(\sum_i p_i\).  Approach #13 asks what Booleanity forbids about such laws.

This run proves that *exact* product spectral laws are maximally rigid, and
derives a quantitative lower bound on how dependent a general Boolean spectral
sample must be when its matched product law is concentrated.

## 2. Exact theorem: an independent Boolean spectral sample has only fixed or fair coordinates

### Theorem

Assume the coordinates of the spectral sample are mutually independent:
\[
\widehat f(A)^2
 =\prod_{i\in A}p_i\prod_{i\notin A}(1-p_i)
 \qquad\text{for every }A\subseteq[n].
\]
Then
\[
p_i\in\{0,\tfrac12,1\}\qquad\text{for every }i.
\]
Consequently
\[
H(f)=H(\mu)\le 2I(f).
\]

More precisely, after deleting variables with \(p_i=0\) and factoring out the
character on the coordinates with \(p_i=1\), the remaining Boolean function has
a flat Fourier spectrum.  Hence the remaining active coordinates all have
\(p_i=1/2\); equivalently the residual function is a bent Boolean function
(on an even number of active coordinates, when nonconstant).

### Proof

Use the unnormalised Walsh coefficients
\[
W_A=\sum_x f(x)\chi_A(x)=2^n\widehat f(A)\in\mathbb Z.
\]

First remove boundary coordinates.  If \(p_i=0\), every Fourier coefficient
containing \(i\) vanishes, so \(f\) is independent of \(x_i\).  If \(p_i=1\),
every Fourier coefficient not containing \(i\) vanishes, so
\(f(x)=x_i g(x_{-i})\) for another Boolean function \(g\).  Independence of the
remaining spectral coordinates is preserved.  It is therefore enough to treat
the case
\[
0<p_i<1\quad\text{for all }i.
\]
Then every product probability is positive, hence every \(W_A\ne0\).

For any \(i\) and any \(A\not\ni i\), product structure gives
\[
\frac{p_i}{1-p_i}
 =\frac{W_{A\cup\{i\}}^2}{W_A^2}.
\]
Thus \(p_i/(1-p_i)\) is a square of a positive rational.  Write it in lowest
terms as
\[
\frac{p_i}{1-p_i}=\frac{a_i^2}{b_i^2},
\qquad
p_i=\frac{a_i^2}{a_i^2+b_i^2},
\]
where \(a_i,b_i\) are positive and coprime.  Put
\(D_i=a_i^2+b_i^2\) and \(D=\prod_iD_i\).  For every \(A\),
\[
W_A^2
 =4^n\,
   \frac{\prod_{i\in A}a_i^2\prod_{i\notin A}b_i^2}{D}.
\tag{1}
\]

Suppose an odd prime \(q\mid D\).  For every \(i\), choose one of
\(a_i,b_i\) that is not divisible by \(q\).  This is always possible because
\(\gcd(a_i,b_i)=1\); moreover, if \(q\mid D_i\), then in fact neither
\(a_i\) nor \(b_i\) is divisible by \(q\).  Choose \(A\) so that the numerator
in (1) uses the selected \(q\)-nondivisible factor for every coordinate.
Then the numerator, including \(4^n\), is not divisible by \(q\), while the
denominator is.  This contradicts the integrality of \(W_A^2\).
Therefore \(D\), and hence every \(D_i\), is a power of \(2\).

Because \(a_i,b_i\) are positive and coprime, they cannot have opposite parity:
then \(D_i\) would be an odd integer greater than \(1\), not a power of \(2\).
They cannot both be even.  Thus both are odd, and
\[
D_i=a_i^2+b_i^2\equiv2\pmod 8.
\]
The only power of \(2\) congruent to \(2\bmod8\) is \(2\).  Hence
\(D_i=2\) and \(a_i=b_i=1\).  Therefore \(p_i=1/2\).

Restoring the peeled coordinates proves
\(p_i\in\{0,1/2,1\}\).  Since an independent law has
\[
H(\mu)=\sum_i h_2(p_i)
\]
and \(I(f)=\sum_i p_i\), each allowed coordinate obeys
\(h_2(p_i)\le2p_i\), with equality only at \(p_i=1/2\).  Hence
\(H(f)\le2I(f)\).  ∎

## 3. A quantitative Booleanity-to-dependence inequality

The exact theorem suggests measuring the failure of independence rather than
trying to characterize all admissible profiles at once.

Let
\[
Q=\bigotimes_i\operatorname{Bernoulli}(p_i)
\]
be the product law with the same marginals as \(\mu\), and define the total
correlation
\[
\operatorname{TC}(\mu)
 =\sum_i h_2(p_i)-H(\mu)
 =D_{\rm KL}(\mu\|Q)\quad\text{(bits)}.
\]
For each \(i\), set
\[
m_i=\max_{A\subseteq[n]\setminus\{i\}}Q_{-i}(A)
   =\prod_{j\ne i}\max(p_j,1-p_j).
\]

### Proposition

Every Boolean spectral sample satisfies
\[
\boxed{\quad
\operatorname{TC}(\mu)
\ge
\frac1{\ln2}\,
\max_i
p_i(1-p_i)\,(2m_i-1)_+^2.
\quad}
\tag{2}
\]

### Proof

Choose signs \(\varepsilon_A\in\{-1,1\}\) for nonzero Fourier coefficients so
that
\(\widehat f(A)=\varepsilon_A\sqrt{\mu(A)}\), choosing arbitrary signs at zero
coefficients.  Booleanity \(f^2=1\) gives, for every nonempty \(T\),
\[
\sum_A\widehat f(A)\widehat f(A\triangle T)=0.
\]
For \(T=\{i\}\),
\[
\sum_A\varepsilon_A\varepsilon_{A\triangle\{i\}}
 \sqrt{\mu(A)\mu(A\triangle\{i\})}=0.
\tag{3}
\]

Put \(x_A=\varepsilon_A\sqrt{\mu(A)}\) and
\(y_A=\varepsilon_A\sqrt{Q(A)}\), and let
\[
\delta=\|x-y\|_2=\|\sqrt\mu-\sqrt Q\|_2.
\]
Comparing the left side of (3) with the corresponding expression for \(y\),
Cauchy–Schwarz gives
\[
\left|\sum_A y_Ay_{A\triangle\{i\}}\right|
\le 2\delta.
\tag{4}
\]
Indeed, expand \(yy'-xx'=(y-x)y'+x(y'-x')\) and use that the coordinate flip is
an \(\ell_2\)-isometry and both \(x,y\) have norm \(1\).

Group the product-law sum into pairs \(A=U\) and \(U\cup\{i\}\).  With
\(\sigma_i(U)=\varepsilon_U\varepsilon_{U\cup\{i\}}\),
\[
\sum_A y_Ay_{A\triangle\{i\}}
 =
2\sqrt{p_i(1-p_i)}\,
\mathbb E_{U\sim Q_{-i}}\sigma_i(U).
\tag{5}
\]
Any \(\{\pm1\}\)-valued function on a probability space whose largest atom has
mass \(m_i\) has mean of absolute value at least \((2m_i-1)_+\): the other
atoms have total mass only \(1-m_i\) and cannot cancel more than that.
Equations (4)–(5) therefore imply
\[
\delta\ge
\sqrt{p_i(1-p_i)}\,(2m_i-1)_+.
\tag{6}
\]

Finally, if \(A(\mu,Q)=\sum_A\sqrt{\mu(A)Q(A)}\) is Hellinger affinity, then
\(\delta^2=2(1-A)\).  Monotonicity of Rényi divergence gives
\[
D_{\rm KL}(\mu\|Q)_{\rm nats}
\ge -2\ln A
\ge \delta^2.
\]
Divide by \(\ln2\), use (6), and maximize over \(i\).  ∎

This is not strong enough by itself to prove FEI: it provides a maximum over
coordinates, whereas the entropy deficit can be a sum over many rare
coordinates.  But it is a dimension-free, genuinely Boolean lower bound on
spectral dependence, derived from the phase-cancellation equations rather than
from a generic entropy inequality.

## 4. Exact reformulation of the universal FEI gap

For any proposed constant \(C\),
\[
H(\mu)\le C\sum_i p_i
\]
is equivalent to
\[
\operatorname{TC}(\mu)
\ge
\sum_i\bigl(h_2(p_i)-Cp_i\bigr).
\tag{7}
\]
Since \(\operatorname{TC}\ge0\), only coordinates with
\(h_2(p_i)>Cp_i\) need positive dependence payment.  At Hod's numerical
constant
\[
C=\beta(1/2)\approx6.4547837,
\]
the nonzero solution of \(h_2(p)=Cp\) is
\[
p_\star\approx0.0305152008312.
\]
Thus the sharp-constant version of FEI can be read as:

> Booleanity must create enough dependence in the spectral sample to pay the
> entropy excess contributed by influence marginals below about \(3.05\%\).

Equation (2) is one concrete payment mechanism.  The next target is a
*tensorizable or multiscale strengthening* that pays a sum of rare-coordinate
deficits rather than only their maximum.

## 5. Adversarial dead route: raw sensitivity-set entropy cannot be the payment

Approach #3 proposes using the sensitivity set of a uniform input.  One natural
subroute would need a dimension-free inequality
\(H(\operatorname{Sens}(X))\le C I(f)\).  That subroute is false.

Take the one-point defect on \(n\ge2\) bits, equal to \(-1\) at one vertex and
\(+1\) elsewhere.  The sensitivity set is:
- all \(n\) coordinates at the defect vertex, probability \(2^{-n}\);
- the singleton \(\{i\}\) at the \(i\)-th neighbor, probability \(2^{-n}\)
  for each \(i\);
- empty everywhere else, probability
  \(q_0=1-(n+1)2^{-n}\).

Therefore
\[
I(f)=\mathbb E|\operatorname{Sens}(X)|=\frac{n}{2^{n-1}},
\]
while
\[
H(\operatorname{Sens}(X))
 =-q_0\log_2q_0+\frac{n(n+1)}{2^n}.
\]
Hence
\[
\frac{H(\operatorname{Sens}(X))}{I(f)}
 =
\frac{n+1}{2}
+\frac{2^{n-1}}{n}\bigl(-q_0\log_2q_0\bigr)
\to\infty.
\]
So sensitivity-set entropy cannot itself be bounded by a universal multiple of
influence.  A coupling-based route would need a subtler conditional or
relative-entropy payment, not this raw entropy bound.

## 6. Executed finite sanity checks

Two independent scripts were run in this invocation.

1. `verify_independent_spectral.py`: exhaustive Boolean functions through
   \(n=4\), quotienting global negation.  Counts checked:
   \(2,8,128,32768\) for \(n=1,2,3,4\).  Every function with an independent
   spectral sample had every marginal in \(\{0,1/2,1\}\), and every such case
   obeyed \(H\le2I\).  At \(n=4\), 560 of the 32768 representatives had
   independent spectral coordinates.  This is a sanity check, not the proof.

2. `verify_spectral_total_correlation.py`: on the same exhaustive range, checked
   inequality (2).  The minimum numerical margin
   `TC - lower_bound` was nonnegative at every dimension through \(4\).

Artifact SHA-256:
- `verify_independent_spectral.py`:
  `1d036843d46dd7909bba92ba8f59020d09c51a7cd10075a1151c37112fe8a8a3`
- `independent_spectral_verification.json`:
  `e96e28f5bc9a0d372955bd632a9c4f865cea850f0a130ca0d553165fa1be1160`
- `verify_spectral_total_correlation.py`:
  `07550f779977bdfe16451f56c6722f2d9e3a52b55a69d7a11f5c9ea513fd8874`
- `total_correlation_verification.json`:
  `07179b177128eb1358994ec3a9e6b9c7955934959190939e9a1f04f6cd76166c`

## 7. What moved and what remains

**Moved:** Approach #13 now has a rigorous obstruction to the most dangerous
exact product model and a quantitative dependence lower bound for every Boolean
spectral sample.

**Still open:** (2) pays only a maximum, not the sum in (7).  It does not prove
full FEI and should not be advertised as doing so.

**Next attack:** seek a chain-rule/tensorization version of the phase-cancellation
argument.  The concrete goal is to lower-bound total correlation by a sum over
rare coordinates, possibly after grouping coordinates into scales.  A useful
next lemma would make the singleton cancellation constraints survive a
conditional or block decomposition strongly enough to pay
\(\sum_{p_i<p_\star}(h_2(p_i)-\beta p_i)\).
