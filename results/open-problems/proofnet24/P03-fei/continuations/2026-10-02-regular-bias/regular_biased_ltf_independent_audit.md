# Independent audit: arbitrary-bias regular LTF FEI corollary

Date: 2026-10-02. Audited file: `regular_biased_ltf_fei.md`.

**Verdict: PASS as a derivation from established results.** I found no
mathematical error in the stated arbitrary-bias, input-weight-regular FEI
corollary, or its fixed-\(\ell_2\)-deviation consequence. The draft correctly
does not claim a solution of FEI for all LTFs, a solution of general FEI, or
research novelty. The source statements and the derivation were audited
independently of the draft's numerical checker. A new checker uses integer
Walsh transforms and exact rational identities.

The only representational detail worth making explicit is that, on the finite
cube, a threshold can be moved into a gap between attained input scores.
Thus output complementation can always be followed by a threshold-only
perturbation to obtain the strict halfspace convention used in Keller–Klein.
This leaves all input weights and their regularity ratio unchanged. This is
a routine justification of the draft's sign-change reduction, not a gap in
the result.

## 1. Primary-source verification

I opened the following primary documents, rather than relying on search
snippets or secondary summaries.

* Klivans–O'Donnell–Servedio, *Learning Intersections and Thresholds of
  Halfspaces*, [author-hosted journal manuscript](https://www.cs.columbia.edu/~rocco/Public/focs02.pdf),
  Theorem 18, PDF pp. 8–9 and proof through p. 11. The displayed estimate is
  \(\operatorname{NS}_{\varepsilon}(f)\le
  \min\{2p,20.5p\sqrt{\varepsilon\ln(1/p)}\}\), for Boolean cube halfspaces.
  Its noise operator independently flips each input bit with probability
  \(\varepsilon\); its Fourier noise formula has the factor \(1/2\) and
  multiplier \((1-2\varepsilon)^{|S|}\).
* Keller–Klein, *Biased halfspaces, noise sensitivity, and local Chernoff
  inequalities*, [arXiv v3 HTML](https://arxiv.org/html/1710.07429v3),
  Theorems 1.1 and 1.4 and Section 2 conventions. The normalization is of the
  input vector, \(\sum_i a_i^2=1\), with unrestricted threshold. The lower
  first-level Fourier weight and upper maximal influence estimates in the
  draft match these theorem statements. Their \(\log\) means natural
  logarithm. The introduction defines influence as the probability of a
  physical coordinate flip changing the output.
* Chakraborty–Karmalkar–Kundu–Lokam–Saurabh,
  *Fourier Entropy-Influence Conjecture for Random Linear Threshold Functions*,
  [author manuscript](https://iuuk.mff.cuni.cz/~koucky/LBCAD/papers/random-ltf.pdf)
  and [arXiv manuscript](https://arxiv.org/pdf/1903.11635), Section 2.2,
  Definition 9 and Corollary 10. Both include the bias \(w_0\) in
  \(\sum_{i=0}^n w_i^2=1\) and in \(\max_{0\le i\le n}|w_i|\le\tau\).
  Corollary 10 assumes \(\tau\le c/\sqrt n\). The draft's comparison of the
  literal hypotheses is accurate, including for the arXiv version rather
  than only the earlier author manuscript.

Some intermediate Keller–Klein proof displays identify indicator singleton
coefficients with influences without the factor two appearing in their
introductory physical-flip definition. The present derivation does not use
those intermediate identities: it uses their theorem statements, whose
constants are existential, and separately supplies the correct exact
identity \(\widehat h(\{i\})=I_i(h)/2\). Thus this convention issue does not
invalidate the result or justify an explicit numerical value of
\(\kappa\).

Targeted searches and the primary documents reviewed did not establish that
this arbitrary-bias deterministic corollary is new. The 2018/2019 regular
corollary already makes a broad claim of regular-LTF FEI, albeit with the
stated bias-inclusive normalization. A difference between written
hypotheses is not a priority result. The June 2026 primary paper
[*Further evidence towards the Fourier Entropy-Influence conjecture*](https://arxiv.org/html/2606.00246v2)
still formulates general FEI as a conjecture; it is not a comprehensive
survey certifying the current status of every LTF subclass. The draft's
novelty disclaimer is therefore appropriate.

## 2. Entropy-tail calculation

For \(t\ge1\), \(\varepsilon=1/(2t)\) is in the permitted range. If the
integer spectral degree \(k>t\), then
\((1-1/t)^k\le e^{-1}\), with the value zero at \(t=1\).
The Fourier formula therefore gives
\[
\frac{1-e^{-1}}2 F(t)\le\operatorname{NS}_{1/(2t)}(f)
 \le20.5p\sqrt{L/(2t)}.
\]
This produces precisely
\(A=20.5\sqrt2/(1-e^{-1})\), not half or twice that constant.
For \(0<t<1\), \(F(t)=q=4p(1-p)\le4p\), and the same bound follows
from \(A\sqrt{\ln2}>4\). No capping by 1 is necessary.

The entropy decomposition is valid: condition on the degree, then bound
conditional entropy by the logarithm of the number of sets at that degree.
The degree-zero layer has only one set and contributes no within-layer
entropy. Tail integration is justified because \(K\) has finite support:
\[
\mathbb E[K\ln(en/K)]
=\int_0^n F(t)\ln(n/t)\,dt.
\]
The integrable logarithmic singularity at zero causes no issue, and
\(\int_0^n t^{-1/2}\ln(n/t)\,dt=4\sqrt n\).

For degree entropy, \(H(K)\le h_2(q)+q\log_2 n\), including \(n=1\).
Since \(p\le q\le4p\),
\(q\ln(1/q)\le qL\le4pL\). The inequality
\(-(1-q)\ln(1-q)\le q\) is also valid at both endpoints by continuity.
The conversion of \(L+1\) to \(\sqrt{nL}\) uses both
\(L\le n\ln2\) and \(nL\ge\ln2\), correctly. Finally
\(\ln n\le2\sqrt n/e\) follows by maximizing \(\ln x/\sqrt x\)
over \(x\ge1\).

The independently evaluated constants are:

| Contribution | Value |
|---|---:|
| \(A\) | 45.86368474136502 |
| Within-level entropy | 264.66924213304856 |
| Binary zero/nonzero degree entropy | 11.73590300577307 |
| Conditional positive-degree entropy | 5.099848954629247 |
| Total coefficient of \(p\sqrt{nL}\) | 281.5049940934509 |

Thus 300 is a valid explicit coefficient; the claim that the computed
coefficient is below 283 is also correct. Constants and \(n=1\) are covered;
\(n=0\) is constant and trivial.

## 3. Influence conversion and arbitrary bias

Coordinate sign flips, coordinate permutations, and output complementation
preserve spectral entropy and physical influences. They allow positive
ordered input weights and indicator density \(p\le1/2\). Threshold ties can
be handled as described above without changing the weights.

For a monotone indicator \(h\), conditioning on all coordinates except
\(i\) gives
\(\mathbb E[x_i h(x)]=(h(x_i=1)-h(x_i=-1))/2\) on each fiber.
Consequently \(I_i(h)=2\widehat h(\{i\})\), while
\(I_i(2h-1)=I_i(h)\). The exact squared-influence identity used in the
draft is therefore
\(\sum_i I_i(f)^2=4W^1(h)\).
There is no factor four in physical indicator influence itself.

Since \(I_{\max}>0\) for a nonconstant function,
\[
I(f)\ge\frac{\sum_i I_i(f)^2}{I_{\max}(f)}
\ge\frac{4c_W}{C_M}\frac{pL}{\min\{1,\tau\sqrt L\}}.
\]
This exactly verifies the stated \(\kappa=4c_W/C_M\) and the lower bound.
Combining it with the entropy estimate yields first
\[
\frac{H(f)}{I(f)}\le
\frac{300}{\kappa}\sqrt{n/L}\min\{1,\tau\sqrt L\}
\le\frac{300}{\kappa}\tau\sqrt n.
\]
Thus the use of \(\tau\le B/\sqrt n\) is correct even in the rare-event
regime. No bound on the threshold is introduced at any stage.

Zero input coefficients can be deleted when applying source conventions
that require strict positivity; this leaves the nonzero vector norm,
maximal weight, Fourier entropy, and influence unchanged. The estimates
can then be expressed in the original dimension, which only enlarges the
entropy bound. All-zero input weights give a constant function.

## 4. Nearuniform consequences and remaining gap

Weights in \([c,2c]\) have norm at least \(c\sqrt n\) and maximum at most
\(2c\), giving \(\tau\sqrt n\le2\). This is a uniform arbitrary-threshold
class.

The \(\ell_2\)-nearuniform proof also allows negative or zero resulting
weights. For \(\sum_i u_i^2\le A^2\), the lower norm bound
\(\|(1+u_i)_i\|_2\ge\sqrt n-A\) and the upper maximum bound
\(\max_i|1+u_i|\le1+A\) are correct. If \(n\ge4A^2\), they give
\(\tau\sqrt n\le2(1+A)\). If \(n<4A^2\), the universal
\(\tau\le1\) gives the stronger \(\tau\sqrt n<2A\). The equality case,
\(A=0\), small dimensions, and cancellation of all coefficients are
handled. The claimed coefficient \(600(1+A)/\kappa\) follows.

The factor \(\tau\sqrt n\) remains unbounded for general representations,
so this calculation does not prove FEI for all LTFs. The AND example in the
draft's final discussion is also correct: each coordinate's spectral
membership marginal is Bernoulli with probability \(2^{1-n}\), which
equals its physical influence. Its marginal-entropy-to-influence ratio
grows on the order of \(n\), so summing entropies of independently treated
groups needs additional control.

## 5. Independent finite checks

New code: `independent_regular_biased_ltf_check.py`.
Results: `independent_regular_biased_ltf_checks.json`.

The checker exhausts every threshold behavior for nonzero nondecreasing
integer weight vectors in \(\{0,1,2,3\}^n\), \(1\le n\le6\). It also
checks selected thresholds, including extremely rare output events, for
uniform, increasing, superincreasing, single-heavy, zero-coordinate, and
random integer weights through \(n=12\).

There were 1,479 nonconstant threshold cases, 454 constant cases, 1,775
noise calculations, 15 sign/complement invariance checks, and 28
deterministic nearuniform vector checks. All passed. Parseval, spectral
variance, the physical/Fourier influence identity, and the factor-two
indicator singleton identity were checked with integers or Fractions.
Entropy and analytic-inequality displays used floating point and are
sanity checks rather than proof certificates.

The maximum observed \(H/(p\sqrt{nL})\) was approximately 9.384, well
below the proven 300. No numerical value of the universal Keller–Klein
constants or of \(\kappa\) is inferred from this finite sample.

**Final audit status:** valid corollary of old primary results, complete
within its stated scope; novelty unconfirmed; general deterministic-LTF
FEI and general FEI remain unproved by this file.
