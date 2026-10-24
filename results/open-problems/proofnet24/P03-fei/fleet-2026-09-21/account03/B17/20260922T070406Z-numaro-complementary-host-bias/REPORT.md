# account03/B17 — exact complementary host-bias spine of the Numaro gate

**Classification:** `ESSENTIAL_STEP_APPLIED / NUMARO_COMPLEMENTARY_HOST_BIAS_SPINE / FULL_FEI_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`  
**Full unrestricted uniform-cube FEI:** **OPEN / NOT PROVED**.

## 0. Exact candidate, full conditional chain, and the old missing implication

The live all-gate candidate remains `LIMIT-PRIME-GATE-LIFT-v1`,

\[
C^\dagger=6.521851214,\qquad C_0=6.4548,
\qquad a^\dagger=4(C^\dagger-C_0)=0.268204856,
\]
\[
\Gamma^\dagger(p)=\Gamma_0(p)+a^\dagger p(1-p),
\]
where \(\Gamma_0\) is the committed h96 read-once value-iteration potential.  For a Boolean gate \(G\) at product bias \(p\), write

\[
D_\Gamma(G;p)=
\sum_i\frac{\operatorname{It}_i(G;p)}{V_{p_i}}
\bigl(\Gamma(p_i)+h_2(V_{p_i})\bigr)
-\Gamma(p_{\rm out})-\widetilde H_G(p),
\qquad V_u=4u(1-u).
\tag{0.1}
\]

The exact gate reformulation and composition cocycle reduce full FEI for this fixed candidate to

\[
D_{\Gamma^\dagger}(P;p)\ge0
\quad\text{for every finite composition-prime Boolean gate }P
\text{ and every interior product-bias vector }p.
\tag{0.2}
\]

That universal implication is still open.  The current run attacks it on the explicit balanced 18-input Numaro obstruction itself, but in a genuinely nonuniform product-bias direction rather than by another truth-table swap or physical restriction.

The source gate is accepted only after reconstruction gives truth-table SHA-256

`f8a7bb2c738d86368305111633376b1a3a83d8ee1f1abcc9a37d841b0f9c7839`.

At the unbiased center it has \(I=261/128\), and the already-certified entropy gives the base margin

\[
c_0(1/2^{18})\approx0.2681828436921863,
\]
so the current lift has only about \(2.20\times10^{-5}\) coefficient reserve there.  This makes nonuniform biasing of this same gate a natural adversarial test.

## 1. Named cross-account theorem consumed and applied

This run substantively consumes account04/B17,

`proofnet24/P03-fei/fleet-2026-09-21/account04/B17/20260922T004252Z-gate-margin-repair/REPORT.md`, report blob

`cf92d6d1219b6ba4ee048b90205024c8075b41df`.

That report proves the exact quadratic-lift law

\[
D_G(\Gamma_0+c\,p(1-p))=D_G(\Gamma_0)+cW_G,
\qquad
W_G:=\frac{I(G;p)}4-p_{\rm out}(1-p_{\rm out})\ge0,
\tag{1.1}
\]
so for \(W_G>0\) the base required margin is

\[
c_G^{(0)}=-\frac{D_G(\Gamma_0)}{W_G}
=a^\dagger-\frac{D_G(\Gamma^\dagger)}{W_G}.
\tag{1.2}
\]

Thus the adversarial question is source-exact: find a product bias on the Numaro gate with \(c_G^{(0)}>a^\dagger\), or prove a family stays below the lift.  The calculations below use (1.1)-(1.2) directly.

The current candidate and its nonnegativity/source normalization are also consistent with account01/B18 `20260922T0325Z-addressing-star-cdagger`, which fixes the same \(C^\dagger,a^\dagger,\Gamma^\dagger\) and proves the already-certified binary AND constraints survive because \(a^\dagger>0.01\).

## 2. Exact host-edge representation of the 18-input source

Split the variables into nine core bits \(c\in\{0,1\}^9\) and nine auxiliary bits \(z_1,\ldots,z_9\).  The recovered source has nine disjoint two-point host sets \(H_j\subset\{0,1\}^9\).  Exact reconstruction shows that these are coordinate edges, one in every core direction; in the source ordering their directions are

\[
(0,3,8,4,1,7,5,2,6).
\tag{2.1}
\]

If \(f_0(c)\in\{\pm1\}\) is the base core function, then every host point has \(f_0(c)=+1\), the hosts are disjoint, and the full gate is exactly

\[
\boxed{
 f(c,z)=f_0(c)-2\sum_{j=1}^9 1_{H_j}(c)z_j.
}
\tag{2.2}
\]

This identity is useful because at each core point at most one auxiliary variable can matter.

Let \(r_j=\Pr[z_j=1]\), \(u_j=r_j(1-r_j)\), and use the normalized biased character

\[
\psi_j(z_j)=\frac{z_j-r_j}{\sqrt{u_j}}.
\]
Then

\[
z_j=r_j+\sqrt{u_j}\,\psi_j(z_j),
\]
so (2.2) becomes

\[
f(c,z)=g_r(c)+\sum_j b_j(c)\psi_j(z_j),
\tag{2.3}
\]
with

\[
g_r(c)=f_0(c)-2\sum_jr_j1_{H_j}(c),
\qquad
b_j(c)=-2\sqrt{u_j}\,1_{H_j}(c).
\tag{2.4}
\]

Therefore **there are no Fourier atoms containing two or more auxiliary coordinates**.  This is an exact structural reduction, not a numerical observation.

For a coordinate edge \(H_j=\{x,x\oplus e_{\pi(j)}\}\), its uniform core Fourier transform has magnitude \(1/256\) on exactly the 256 subsets not containing \(\pi(j)\), and vanishes on the other 256.  Hence the entire auxiliary-\(j\) packet has 256 equal masses

\[
\boxed{\frac{u_j}{16384}},
\tag{2.5}
\]
its auxiliary influence is \(u_j/64=V_{r_j}/256\), and its contribution to core influence is \(u_j/16\).

## 3. Complementary two-host deformation collapses to one scalar

Choose any two distinct auxiliaries \(j\ne k\), put

\[
r_j=r,\qquad r_k=1-r,\qquad r_\ell=\frac12\quad(\ell\ne j,k),
\qquad 0<r\le\frac12.
\tag{3.1}
\]

All nine core bits remain unbiased.  Because the two displaced biases sum to one, the output remains exactly balanced:

\[
\boxed{p_{\rm out}=1/2.}
\tag{3.2}
\]

Let \(u=r(1-r)\).  The exact integer-Walsh checker proves two source-specific algebraic facts.

First, for every ordered pair \((j,k)\), the squared zero-auxiliary core Fourier coefficients have the same 47 polynomial classes in \(r\); after adjoining core Fourier level, the same 54 weighted classes occur.  Thus entropy and influence on (3.1) are independent of which distinct pair is chosen.

Second, the total influence carried by the nine core coordinates is independent of \(r\):

\[
\boxed{I_{\rm core}(r)=\frac{513}{256}.}
\tag{3.3}
\]

The checker proves (3.3) coefficient-by-coefficient as a polynomial identity.  Writing each zero-auxiliary core Walsh numerator as \(z_S(r)=z_S(0)+b_Sr\), its weighted quadratic coefficients cancel exactly against the packet term \(7/64+(r-r^2)/8\).

The seven untouched auxiliary coordinates contribute \(7/256\) influence and the complementary pair contributes \(u/32\).  Therefore

\[
\boxed{
I(r)=\frac{65}{32}+\frac{u}{32},
\qquad
W(r)=\frac{I(r)-1}{4}=\frac{33+u}{128}.
}
\tag{3.4}
\]

For entropy, let \(H_{\rm core}(r)\) denote the entropy of the zero-auxiliary core packet.  Seven unbiased auxiliary packets contribute \(7/16\), while the two biased packets contribute

\[
2\cdot256\frac{u}{16384}\log_2\frac{16384}{u}
=\frac{u}{32}\log_2\frac{16384}{u}.
\]
Hence

\[
\boxed{
H(r)=H_{\rm core}(r)+\frac7{16}
+rac{u}{32}\log_2\frac{16384}{u}.
}
\tag{3.5}
\]

Finally, the core coordinates are unbiased and each displaced auxiliary has
\(\operatorname{It}/V=1/256\).  Substitution into (0.1) gives the exact one-variable defect

\[
\boxed{
D_{\Gamma^\dagger}(r)
=rac{33}{32}C^\dagger
+rac{\Gamma^\dagger(r)+h_2(4u)}{128}
-H(r).
}
\tag{3.6}
\]

Equations (3.4)-(3.6) reduce a genuinely 18-input nonuniform adversary to one scalar while keeping the original Boolean gate and actual normalization.

## 4. A continuous extreme-bias theorem independent of the detailed potential shape

At the boundary \(r=0\), the two displaced auxiliary packets vanish.  Rational logarithm enclosures give

\[
H(0)=6.710059141705122\ldots
\]
with enclosure width below \(1.2\times10^{-79}\).  Since the last term in (3.6) is the only negative term after the fixed center and \(\Gamma^\dagger,h_2\ge0\),

\[
D_{\Gamma^\dagger}(0)
\ge \frac{33}{32}C^\dagger-H(0)
>0.015599922732378.
\tag{4.1}
\]

We now control the whole nearby continuum, not merely a grid.  For a representative complementary pair, the exact core numerator perturbation has

\[
\sum_S2|z_S(0)b_S|=49248,
\qquad
\sum_Sb_S^2=8192.
\]
After division by \(512^2\), the \(\ell_1\) change of the zero-auxiliary spectral masses is at most

\[
\frac{1539}{8192}r+rac1{32}r^2.
\]
The two newly appearing auxiliary packets have total mass \(u/32\le r/32\).  Hence the total-variation distance from the \(r=0\) spectral law obeys

\[
\boxed{
T(r)\le\frac{1795}{16384}r+rac{r^2}{64}.
}
\tag{4.2}
\]

For \(0\le r\le1/512\),

\[
T(r)\le\frac{3591}{16777216}=0.0002140402793884\ldots .
\]
The Audenaert--Fannes inequality on at most \(2^{18}\) spectral atoms gives

\[
|H(r)-H(0)|
\le T\log_2(2^{18}-1)+h_2(T).
\]
Using \(\log_2(2^{18}-1)<18\) and
\(h_2(T)\le T(\log_2(1/T)+1/\ln2)\), with the rationally verified bound \(1/\ln2<1.443\), the checker obtains

\[
|H(r)-H(0)|<0.006770699784389.
\tag{4.3}
\]

Combining (3.6), nonnegativity of \(\Gamma^\dagger,h_2\), (4.1), and (4.3):

\[
\boxed{
D_{\Gamma^\dagger}(r)>0.008829222947989
\qquad (0\le r\le1/512).
}
\tag{4.4}
\]

Thus the exact Numaro obstruction is **repelled from the extreme complementary host-bias boundary on a genuine continuous interval**, without using the fine shape of the h96 potential.

## 5. Infinite dyadic complementary spine is rigorously safe

At \(r=2^{-m}\), the committed read-once source normalization gives the dyadic AND-chain value

\[
\Gamma_0(2^{-m})=C_0 I(\mathrm{AND}_m)-H(\mathrm{AND}_m),
\qquad
I(\mathrm{AND}_m)=m\,2^{1-m}.
\tag{5.1}
\]

For \(m=2,\ldots,8\), the checker evaluates (3.5)-(3.6) with rational masses and rigorous atanh-series logarithm enclosures.  For \(m\ge9\), (4.4) applies automatically because \(2^{-m}\le1/512\).

The finite front of the infinite spine is:

| \(m\) | \(r=2^{-m}\) | certified \(D_{\Gamma^\dagger}\) lower bound | certified \(c_G^{(0)}\) upper bound |
|---:|---:|---:|---:|
|2|0.25|0.0046429580655842|0.250297552575676|
|3|0.125|0.0107185075773770|0.226767378853293|
|4|0.0625|0.0142687905050681|0.212957340075379|
|5|0.03125|0.0157532321525392|0.207157413588103|
|6|0.015625|0.0161666319908139|0.205527133042987|
|7|0.0078125|0.0161520536207094|0.205569178872680|
|8|0.00390625|0.0160172067887170|0.206084832954786|

For the analytic tail \(m\ge9\), (4.4) also gives

\[
c_G^{(0)}<0.233960195882612.
\]

Therefore for **every** choice of two distinct source auxiliaries and every dyadic complementary bias \(r=2^{-m},1-r\) with \(m\ge2\),

\[
\boxed{
D_{\Gamma^\dagger}>0,
\qquad
c_G^{(0)}<0.250297552575676<a^\dagger.
}
\tag{5.2}
\]

The coefficient reserve is at least

\[
\boxed{
a^\dagger-c_G^{(0)}>0.017907303424324.}
\tag{5.3}
\]

This is an infinite exact asymmetric family.  It is not a finite bias grid, and all variables remain interior for every finite \(m\).

## 6. Refutation attempt, what changed, and the replacement obligation

**Exact candidate version:** `LIMIT-PRIME-GATE-LIFT-v1`, \(C^\dagger=6.521851214\), \(a^\dagger=0.268204856\).

**Old missing implication:** prove the live gate inequality for every composition-prime Boolean gate at every interior product bias, or find a genuine counterexample.  The Numaro seed is one of the closest known center obstructions, so asymmetric product biases of this same gate are a high-value adversarial direction.

**Stronger adversarial claim tested:** complementary biasing of two source hosts can increase the Numaro gate's required base margin beyond the live lift.

**New proved inference / refutation:** that claim is false on the entire dyadic complementary spine \(r=2^{-m}\), \(m\ge2\), for every ordered host pair, and on the full continuous extreme-bias collar \(0<r\le1/512\).  The source-specific Fourier packet decomposition gives the exact scalar defect (3.6), rather than relying on sampled biases.

**Not proved:** the intermediate non-dyadic interval \(1/512<r<1/2\) is not closed by this report.  In particular, (5.2) must not be promoted to an all-bias theorem.  Nor does this result cover simultaneous deformation of several host pairs or nonuniform core-coordinate biases.

**Replacement obligation:** attack the still-open intermediate complementary interval with the actual h96 source envelope, or move one dimension outward to simultaneous host-pair/core-bias deformation.  Re-running auxiliary physical restrictions is now redundant: the present attack keeps the original 18-input gate and changes the product measure instead.

**Consumed peer artifact:** account04/B17 `20260922T004252Z-gate-margin-repair`, blob `cf92d6d1219b6ba4ee048b90205024c8075b41df`.

**Applied to claim:** exact base-margin comparison for the nonuniform Numaro host-bias family through the quadratic-lift identity (1.1)-(1.2).

**Next recipients:** account03/B18 for fixed-candidate integration; account04/B17 for the remaining non-dyadic margin interval / cocycle comparison.

**Implication to full FEI:** one infinite nonuniform family around a known hard composition-prime obstruction is removed, but the universal prime-gate/all-bias implication remains open.  Therefore full FEI remains **OPEN / NOT PROVED**.

## 7. Verification and scope

`CHECKER.py` reconstructs the exact source truth table and refuses any hash mismatch; verifies all nine host directions, pair-independent polynomial classes, the exact influence identities, the continuous total-variation bound, and rational logarithm enclosures; then certifies the dyadic front and the analytic tail.  It uses no randomized search.

Scoped privacy review: this package contains only FEI mathematics, the public/source-bound Boolean construction already present in the research repository, and deterministic verification code/output.  It contains no credentials, scheduler identifiers, machine paths, unrelated private transcripts, email/Drive actions, public-posting actions, paid model/API/Codex calls, workflows, or permission changes.
