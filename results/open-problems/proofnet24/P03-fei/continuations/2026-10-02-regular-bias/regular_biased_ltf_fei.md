# Arbitrary-bias regular LTFs: a corollary of established results

Date: 2026-10-02. Status: **complete derivation from two established primary
results; research novelty unconfirmed**. This file does not resolve FEI for
all deterministic LTFs. In particular, it does not assert that regular LTF
FEI was previously an open problem. The point is to record a rigorous
arbitrary-bias consequence, correct an initially mistaken belief that its
relative noise estimate was unavailable, and make the remaining gap precise.

All spectral entropy is in bits. Natural logarithms are denoted \(\ln\).
For a Boolean LTF \(f:\{-1,1\}^n\to\{-1,1\}\), put

\[
 p=\min\{\Pr(f=1),\Pr(f=-1)\},\qquad L=\ln(1/p).
\]

The constant functions have \(H(f)=I(f)=0\), and are omitted from formulas
involving \(L\). Thus \(2^{-n}\le p\le1/2\) and
\(\ln2\le L\le n\ln2\).

## 1. Established relative noise bound

Theorem 18 of Klivans–O'Donnell–Servedio, *Learning Intersections and
Thresholds of Halfspaces*, JCSS 68 (2004), 808–840, states for every Boolean
halfspace and bit-flip noise \(0\le\varepsilon\le1/2\):

\[
 \operatorname{NS}_\varepsilon(f)
 \le\min\{2p,20.5p\sqrt{\varepsilon\ln(1/p)}\}.
\tag{1}
\]

Primary journal manuscript, Theorem 18 and proof in Section 3.3, pp. 9–11:
<https://www.cs.columbia.edu/~rocco/Public/focs02.pdf>.
The theorem applies on the Boolean cube, not only in Gaussian space.

An earlier checkpoint incorrectly treated the second term in (1) as a
missing lemma. The primary-source lookup resolves that obstacle; it must not
be presented as newly proved here. Keller–Klein's later noise-resistance
definition is different and is not the source of (1).

## 2. A self-contained bias-sensitive entropy bound

We prove directly from (1) that

\[
 \boxed{H(f)\le300p\sqrt{n\ln(1/p)}.}\tag{2}
\]

No Gaussian invariance or entropy-transfer theorem is used.

Let \(K\) be the spectral degree random variable:
\(\Pr(K=k)=W_k=\sum_{|S|=k}\widehat f(S)^2\). Let
\(F(t)=\Pr(K>t)\). Parseval and the constant coefficient give

\[
 q:=\Pr(K>0)=1-(1-2p)^2=4p(1-p)\le4p.
\]

For \(t\ge1\), use noise \(\varepsilon=1/(2t)\). Every integer \(k>t\)
satisfies \((1-1/t)^k\le e^{-1}\), with the obvious interpretation at
\(t=1\). The Fourier formula for bit-flip noise is

\[
 \operatorname{NS}_\varepsilon(f)
 =\frac12\sum_k W_k\bigl(1-(1-2\varepsilon)^k\bigr).
\]

Hence (1) gives

\[
 F(t)\le A p\sqrt{L/t},\qquad
 A=\frac{20.5\sqrt2}{1-e^{-1}}<46.
\tag{3}
\]

For \(0<t<1\), the same upper bound holds because \(F(t)=q\le4p\),
\(L\ge\ln2\), and \(A\sqrt{\ln2}>4\). Thus (3) holds for every
\(t>0\). A bound bigger than 1 causes no issue.

Conditioning the spectral set on its degree gives

\[
 H(f)\le H(K)+\sum_{k=1}^n W_k\log_2\binom nk.
\tag{4}
\]

For the within-level term, use \(\binom nk\le(en/k)^k\). The increasing
function \(\phi(t)=t\ln(en/t)\), with \(\phi(0)=0\), satisfies
\(\phi'(t)=\ln(n/t)\) on \((0,n]\). The tail integration identity and
(3) give

\[
 \begin{aligned}
 \sum_{k=1}^n W_k\log_2\binom nk
 &\le\frac1{\ln2}\mathbb E\phi(K)\\
 &=\frac1{\ln2}\int_0^n F(t)\ln(n/t)\,dt\\
 &\le\frac{4A}{\ln2}p\sqrt{nL}.
 \end{aligned}
\tag{5}
\]

The last integral is
\(\int_0^n t^{-1/2}\ln(n/t)\,dt=4\sqrt n\).

For the degree entropy, separate its zero/nonzero bit:

\[
 H(K)\le h_2(q)+q\log_2 n.
\]

Using \(h_2(q)\le q\log_2(1/q)+q\log_2 e\), \(p\le q\le4p\), and
the bounds on \(L\), we obtain

\[
 h_2(q)\le\frac4{\ln2}p(L+1)
 \le\frac4{\ln2}\left(\sqrt{\ln2}+\frac1{\sqrt{\ln2}}\right)
    p\sqrt{nL}.
\]

Also \(\log_2 n\le 2\sqrt n/(e\ln2)\) for \(n\ge1\), so

\[
 q\log_2n\le\frac8{e\ln2\sqrt{\ln2}}p\sqrt{nL}.
\]

The sum of the constants in (5) and the last two displays is less than 300
(indeed, less than 283). This proves (2), including \(n=1\).

## 3. Established degree-one and maximal-influence estimates

Normalize a representation \(f(x)=\operatorname{sgn}(\sum_i w_ix_i-\theta)\)
so \(\sum_iw_i^2=1\), and put \(\tau=\max_i|w_i|\). Sign changes of
coordinates and of the output preserve entropy and influences. They allow
us to work with a monotone indicator \(h=(f+1)/2\) of density \(p\le1/2\).

Theorems 1.1 and 1.4 of Keller–Klein, *Biased halfspaces, noise sensitivity,
and local Chernoff inequalities*, Discrete Analysis 2019:13, give absolute
positive constants \(c_W,C_M\) such that

\[
 W^1(h)\ge c_W p^2L,\qquad
 I_{\max}(h)\le C_M p\min\{1,\tau\sqrt L\}.
\tag{6}
\]

Primary text:
<https://arxiv.org/html/1710.07429v3>,
<https://arxiv.org/pdf/1710.07429v3>.
The paper defines indicator influence by physical bit flips, the same
influence as the corresponding \(\{-1,1\}\)-valued function.

For a monotone indicator,
\(\widehat h(\{i\})=I_i(h)/2\). Consequently

\[
 \sum_i I_i(f)^2=4W^1(h),\qquad
 I(f)\ge\frac{\sum_i I_i(f)^2}{I_{\max}(f)}.
\]

Set \(\kappa=4c_W/C_M>0\). Then (6) yields the concrete lower bound

\[
 \boxed{I(f)\ge\kappa\frac{pL}{\min\{1,\tau\sqrt L\}}.}\tag{7}
\]

In particular, if \(\tau\le B/\sqrt n\), where \(B\ge1\) is fixed,
then \(\min\{1,\tau\sqrt L\}\le B\sqrt{L/n}\), and

\[
 I(f)\ge\frac\kappa B p\sqrt{nL}.
\tag{8}
\]

This covers both the moderate-bias and very rare-event regimes in a single
inequality. It does not assume that every coordinate has influence
proportional to its weight; such an assumption would be false in general.

## 4. Regular arbitrary-bias FEI

Combining (2) and (8) proves

\[
 \boxed{H(f)\le\frac{300B}{\kappa}I(f)
 \quad\text{if}\quad
 \frac{\max_i|w_i|}{\sqrt{\sum_iw_i^2}}\le\frac B{\sqrt n}.}\tag{9}
\]

The bias \(\theta\) is arbitrary. More generally, (2) and (7) give

\[
 H(f)\le\frac{300}{\kappa}\tau\sqrt n\,I(f).
\tag{10}
\]

The constants in the Keller–Klein primary theorem are existential; no
explicit numerical universal constant is claimed for (9). The coefficient
300 in (2) is explicit and comes only from the stated noise bound and
elementary entropy inequalities.

For example, if the positive weights lie in \([c,2c]\), then
\(\tau\sqrt n\le2\), so (9) gives one universal FEI constant for that
whole class, regardless of the threshold. These weights need not be equal,
have a bounded number of distinct values, or have bounded total deviation
from a common weight. This is strictly broader as a hypothesis than the
fixed-L1-deviation corollary in `hamming_band_fei.md`.

There is also a complete \(\ell_2\)-nearuniform consequence. If
\(w_i=c(1+u_i)\), \(c>0\), and \(\sum_i u_i^2\le A^2\), then

\[
 \tau\sqrt n\le2(1+A).
\tag{11}
\]

Indeed, for \(n\ge4A^2\), the triangle inequality gives
\(\|w/c\|_2\ge\sqrt n-A\ge\sqrt n/2\), while
\(\max_i|w_i/c|\le1+A\). For \(n<4A^2\), the elementary bound
\(\tau\le1\) gives \(\tau\sqrt n<2A\). If all weights vanish, the
function is constant and is handled separately. Thus arbitrary-bias FEI
holds on this whole \(\ell_2\)-nearuniform class, with the bound

\[
 H(f)\le\frac{600(1+A)}\kappa I(f).
\tag{12}
\]

This resolves the proposed \(\ell_2\)-nearuniform subclass within the present
derivation. The earlier attempt to extend the physical Hamming-band estimate
to a soft band is unnecessary for that subclass. No novelty is asserted for
this consequence of the already-established input theorems.

## 5. Novelty and the remaining gap

All analytic input needed for this corollary predates this session. The
general relative noise estimate is Theorem 18 of KOS (2004), and the sharp
degree-one/maximal-influence estimates are Keller–Klein (2019). The direct
entropy tail calculation is elementary. This file establishes the corollary
without asserting that the corollary is new or previously open.

The existing random-LTF literature also proves FEI for random weight laws:
<https://arxiv.org/abs/1903.11635>. Its earlier author-hosted manuscript
<https://iuuk.mff.cuni.cz/~koucky/LBCAD/papers/random-ltf.pdf> states a
regular deterministic corollary too: Definition 9 normalizes
\(\sum_{i=0}^n w_i^2=1\), including the bias \(w_0\), and requires
\(|w_i|\le\tau\) for every \(0\le i\le n\). Corollary 10 then assumes
\(\tau\le c/\sqrt n\). That literal condition also bounds the bias.
In contrast, (9) above normalizes only the input weights and imposes no
condition on the bias. This establishes a difference between the stated
hypotheses, but does not certify novelty of this deterministic arbitrary-bias
consequence. A complete literature audit would be necessary before a
research claim.

The full deterministic-LTF gap is explicit in (10):
\(\tau\sqrt n\) can grow with \(n\). The relative noise bound controls
total degree, while the generic entropy estimate uses the number \(n\) of
coordinates to bound the number of coefficients at a degree. Removing that
dimension cost for highly unequal weights remains unresolved here. Low-degree
Gaussian invariance does not control the entire entropy tail.

Grouping coordinates by weight scale does not immediately repair the gap.
Physical restrictions on a regular group each obey (9), but the entropy of
the group's unconditional spectral marginal can exceed their average
entropy. For a group consisting of the first coordinate of \(\mathrm{AND}_n\),
the marginal is Bernoulli with parameter \(2^{1-n}\), whose entropy/influence
ratio grows linearly in \(n\); the rest of the function pays for that cost.
Thus an argument summing group FEI bounds needs an additional global
accounting step, which has not been supplied.

Earlier max-influence and separator induction obstructions remain valid.
Nothing in (9) supplies the missing adaptive split inequality for arbitrary
Boolean functions.
