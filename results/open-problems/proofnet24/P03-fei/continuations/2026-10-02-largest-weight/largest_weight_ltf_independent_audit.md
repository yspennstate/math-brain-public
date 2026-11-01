# Independent audit of the candidate largest-weight LTF proof

Date: 2026-10-02. Audited draft: `largest_weight_ltf_candidate.md`.

**Internal mathematical verdict: no error found after two independent
adversarial passes.** Under the stated KOS and Keller–Klein primary theorems,
the derivation is complete: it proves a uniform largest-weight split
increment inequality and hence FEI for every deterministic LTF by induction.
This is an internal audit of a candidate proof, not an external peer-review
certificate or a research-priority determination. It does not prove FEI for
all Boolean functions. The earlier restricted FEI corollaries do not depend
on this candidate.

I independently reconstructed the new slab-noise and dyadic-KL arguments
before reading the complete draft, then checked all displayed transitions
and constants in the complete file. I also wrote a separate finite stress
checker; the analytic verdict is not inferred from its output.

## 1. Established inputs, normalization, and endpoints

The primary-source checks are recorded in
`regular_biased_ltf_independent_audit.md`. In particular:

* KOS Theorem 18 applies to arbitrary Boolean cube halfspaces and uses bit
  flips, with the exact upper bound
  \(20.5p\sqrt{\varepsilon\ln(1/p)}\).
* Keller–Klein Theorem 1.4 applies to an input vector of squared norm 1,
  with unrestricted threshold, and gives the asserted maximal physical
  influence lower bound. Its logarithm is natural.
* For completeness, the hypercontractive input was checked in O'Donnell's
  [author-hosted *Analysis of Boolean Functions*](https://www.cs.cmu.edu/~odonnell/papers/Analysis-of-Boolean-Functions-by-Ryan-ODonnell.pdf),
  the two-function hypercontractivity theorem in Sections 9.4 and 10.1.
  Taking both functions to be an indicator of mean \(\alpha\), and the two
  norm parameters to be \(3/2\), gives
  \(\operatorname{Stab}_{1/2}(B)\le\alpha^{4/3}\), as used in the draft.

Coordinate flips and output complementation allow nonnegative weights and
rare positive output without changing the desired ratio. On the finite
cube one can move the threshold into the strict gap between negative and
positive attained scores, preserving the input weights. This avoids all
slab endpoint ties and preserves the largest-weight coordinate.

The asserted largest-weight/largest-influence implication is exact.
For \(w_i\ge w_j\), condition on the other coordinates; the difference of
the two singleton coefficients is one half of the difference between the
two mixed-sign function values. For a monotone \(\{-1,1\}\)-valued
function those singleton coefficients equal the physical influences.
The difference is nonnegative. The source maximal-influence lower bound
therefore applies to the chosen coordinate, not merely some coordinate.

With full input norm \(w\sqrt{R+1}\), Keller–Klein yields precisely
\(\alpha\ge cp\min\{1,\sqrt{L/(R+1)}\}\). The subsequent relation
\(p\sqrt L/\sqrt M\le\sqrt2\alpha/c\) is valid in both cases
\(L\le R+1\) and \(L>R+1\). The pivotal-slab bound
\(\alpha\le2p\) is also exact. Nonconstant functions have \(p>0\) and
\(\alpha>0\); all constant restrictions are handled separately in the
eventual induction.

## 2. New interval concentration and relative slab stability

The sinc-squared interval concentration proof is valid, including for
discrete atoms. For
\(K(u)=(\sin(u/(2w))/(u/(2w)))^2\), the triangular Fourier identity
\[
K(u)=w\int_{-1/w}^{1/w}(1-w|t|)e^{itu}\,dt
\]
has the correct coefficient and integration limits. At \(u=0\), the
right side equals 1, and direct integration gives the displayed identity
for all \(u\). On \(|u|\le w\),
\(K(u)\ge(23/24)^2>9/10\). For \(|b_jt|\le1\),
\(|\cos(b_jt)|\le e^{-b_j^2t^2/2}\): cosine is positive in this
range, and integrating \(\tan x\ge x\) proves the bound. Independence
then controls the characteristic function by \(e^{-vt^2/2}\).
The Gaussian integral gives
\((10/9)\sqrt{2\pi}\,w/\sqrt v<3w/\sqrt v\).
No Berry–Esseen approximation or nonatomic assumption remains implicit.

The resampling representation is the correct \(\rho\)-correlated cube
coupling. Conditional on the original \(X\) and on the mask, refreshed
coordinates are still independent uniform signs, even after multiplying
by \(B(X)\). Retained coordinates only translate the slab center.

The mask bad event is independent of \(X\). This fact is essential to
retain the factor \(\alpha\) in the error term; it is available here.
For the scaled random variance \(U=V_J/w^2\), exponential Markov gives
\[
\Pr(U<\mu/2)
\le e^{\mu/2}\mathbb E e^{-U}
\le \exp\{-[1-e^{-1}-1/2]\mu\}
\le e^{-\mu/8}.
\]
The convex chord inequality for \(e^{-u}\) on \([0,1]\) and the
independence of mask bits justify the middle estimate.

The good-mask bound is \(3\sqrt2/\sqrt\mu\). The bad-mask factor
is \(e^{-\mu/8}\), and
\(\sup_{u>0}\sqrt u e^{-u/8}=2e^{-1/2}\). Its addition to
\(3\sqrt2\) is less than 6. Together with the trivial
\(\operatorname{Stab}_\rho(B)\le\alpha\), this proves the stated
relative stability lemma for every \(R>0\) and \(0\le\rho<1\),
without a missing error depending on \(1/\alpha\).

## 3. Low-degree slab mass at both geometric and bias scales

For integer \(k\ge1\), \(\rho=1-1/(2k)\) satisfies
\(\rho^k\ge1/2\). Fourier positivity therefore gives
\(Q(K\le k)\le2\operatorname{Stab}_\rho(B)/\alpha\), resulting
in \(12\sqrt{2k/R}<18\sqrt{k/R}\). Replacing real \(k\ge1\) by
its floor leaves a valid inequality with the original, larger square root.

Hypercontractivity supplies the separate bound
\(Q(K\le k)\le2^k\alpha^{1/3}\). When \(L\ge2\ln2\),
\(\alpha\le2p\) implies \(\ln(1/\alpha)\ge L/2\).
For \(k\le L/(12\ln2)\), the exponential estimate in the draft is
\(e^{-L/12}\), and
\(\sup_{L>0}\sqrt L e^{-L/12}=\sqrt6e^{-1/2}<1.5\).
For larger \(k\), the constant 3 works since
\(\sqrt{12\ln2}<3\). The small-\(L\) case also obeys the trivial
bound with this constant. Thus there is no lost rare-event regime.

Choosing the appropriate bound according to the maximizing term in
\(M=\max\{1,R,L\}\) proves the stated
\(Q(K\le k)\le18\sqrt{k/M}\). This includes \(R=0\).
Degree zero is not being forced into this bound with \(k=0\): its mass
is exactly \(Q(K=0)=\alpha\), and it is treated separately later.

## 4. Tail comparison and dyadic KL separation

The split-pair law \(P\) is a probability law, since
\(A^2+B^2=1\). Its rest-coordinate degree is no larger than the full
degree of either associated Fourier coefficient. This verifies the
direction of the comparison with the full halfspace spectrum.
For full degrees at least real \(u\ge1\), bit-flip noise
\(1/(2u)\) attenuates by at least \(1-e^{-1}\). The same argument
works at \(u=1\). For \(0<u<1\), the nonzero full spectral mass is
at most \(4p\). The constant \(A_0\sqrt{\ln2}>4\) supplies the
small-\(u\) estimate. These facts prove the tail estimate for every
positive real lower bin endpoint, as required.

Combining it with the influence lower bound gives
\(P_j\le\Gamma\alpha2^{-j/2}\). For negative bins,
\(Q_j\le18\sqrt2\,2^{j/2}\), so
\(\sum_{j<0}|j|Q_j\) is uniformly bounded. Empty bins below degree
1 cause no exception. There is no need to assume a positive-bin tail
estimate for \(Q\).

The reference distribution, including the extra star atom, has total mass
1. The KL identity
\[
D(Q\|P)=D(Q\|R_{\mathrm{reference}})
+\sum_b Q_b\log_2(R_b/P_b)
\]
is valid on the coarse finite-support laws. Nonnegativity of its first
term yields the asserted lower bound. In positive-degree bins, the
reference-to-\(P\) log ratio is bounded below by
\[
\log_2(1/\alpha)-\log_2(2Z\Gamma)
+j/2-|j|/4.
\]
The last part is nonnegative for \(j\ge0\), and its negative-bin cost
is summable. The star contribution is at least \(-\alpha\), since
its reference mass is \(1/2\) and \(P_\star\le1\). This is a
clean way to include the zero-degree term without losing an unbounded
\(\alpha\log(1/\alpha)\) correction.

The final correction is bounded using
\(\alpha\log_2(1/\alpha)\le(\log_2e)/e\). Thus the displayed
absolute \(C_D\) proves
\(D(Q\|P)\ge\log_2(1/\alpha)-C_D\). No denominator can vanish
on the support of \(Q\), because \(P_S\ge\alpha Q_S\).
KL data processing increases this lower bound when one returns to the
individual subsets, so its use has the correct direction.

## 5. Conditional entropy, exact split identity, and induction

The included-coordinate part of conditional spectral-bit entropy is
exactly \(\alpha[\log_2(1/\alpha)-D(Q\|P)]\). The excluded part
is at most \(\alpha\log_2e\), by applying \(\ln(1+t)\le t\)
coefficient by coefficient to
\(a_S^2\ln(1+b_S^2/a_S^2)\). Terms with \(a_S=0\) are handled by
continuity. The bound follows after summing \(b_S^2\), not after
summing a number of coefficients depending on dimension.

The exact entropy increment identity has the additional term
\(1-h_2(r_S)\); it has not been omitted. Here
\(r_S(1-r_S)=1/4-q_S(1-q_S)\). The valid binary entropy bound
\(h_2(t)\ge4t(1-t)\) yields
\(1-h_2(r_S)\le4q_S(1-q_S)\le h_2(q_S)\).
Therefore \(\Delta_iH\le2\mathcal C\), with the stated factor two.

It follows that the largest-weight coordinate obeys
\(\Delta_iH\le2(C_D+\log_2e)I_i(f)\), with one absolute constant.
The restriction of an LTF remains an LTF, and physical influences satisfy
the exact restriction recursion. Applying the inductive hypothesis to
both restrictions and adding this increment gives
\[
H(f)\le C_*\tfrac12[I(f^+)+I(f^-)] + C_* I_i(f)=C_*I(f).
\]
Constant restrictions and the zero-dimensional base case have entropy
and influence zero. Thus the candidate has a complete implication to
deterministic-LTF FEI; the conclusion is not merely regular-LTF FEI.

## 6. Independent finite stress checks and limits of the audit

New code: `independent_largest_weight_probe.py`.
Output: `independent_largest_weight_probe_checks.json`.
It checks all threshold behaviors of sorted integer vectors with weights
in \(\{0,1,2,3\}\) through dimension 6, plus uniform, increasing,
superincreasing, heavy-coordinate, zero-coordinate, random, and two-scale
vectors through dimension 14. There were 1,642 nonconstant cases.

Integer Walsh coefficients and Fractions check spectral normalization,
\(Q_0=\alpha\), \(P\ge\alpha Q\), and physical pivot mass. Floating
point checks the entropy identity, factor-two inequality, and KL data
processing. Representative maxima were:

| Quantity | Maximum observed |
|---|---:|
| \(Q(K\le k)/\sqrt{k/M}\) | 1.20185043 |
| \(P(K\ge k)/(\alpha\sqrt{M/k})\) | 1.72736252 |
| \(\log_2(1/\alpha)-D(Q\|P)\), full subset law | 1.65593614 bits |
| Same deficit, coarsened bin law | 1.85875281 bits |
| Conditional spectral-bit entropy divided by \(\alpha\) | 2.69723723 |
| \(\Delta_iH/\alpha\) | 4.87222907 |

These observations neither prove a smaller universal constant nor exclude
an asymptotic counterexample; the analytic derivation above is what was
audited. Research novelty, literature priority, and external mathematical
acceptance are separate questions. The present internal audit found no
missing lemma or unjustified analytic extrapolation in the candidate file.
