# fleet03/B17 — exact asymmetric arity-5 dyadic-spine exclusion

**Classification:** `ESSENTIAL_STEP_APPLIED / EXACT_FINITE_SLICE_CERTIFICATE`.  
**Full uniform-cube FEI:** **OPEN / NOT PROVED.**  
**Execution:** `WITHOUT_VERIFIED_BRAIN`; repository sources were read directly, but no authenticated installed-brain retrieval/context was used.  
**Publication priority:** `UNVERIFIED`; no novelty claim.

## 1. Exact candidate version and the missing implication attacked

The live all-gate target is
\[
D_\Gamma(G;p):=
\sum_i {\operatorname{It}_i(G;p)\over V_{p_i}}
       \bigl(\Gamma(p_i)+h_2(V_{p_i})\bigr)
-\Gamma(p_{\rm out})-\widetilde H_G(p)\ge0,
\qquad V_u=4u(1-u).
\tag{1.1}
\]
A finite-cap symmetric nonnegative \(\Gamma\) satisfying (1.1) for every Boolean gate and every product bias is equivalent to full FEI.

This run attacks the fixed current candidate `LIMIT-PRIME-GATE-LIFT-v1` from the exact other-account report

`fleet01/B18/20260922T0222Z-shared-graft-tail/REPORT.md`,
observed blob `7ea2c548afc0a5fc62f972f9c64df0578f7e0838`.

That report proves a finite cap for the recursive shared-graft obstruction and fixes
\[
C_*=6.5218512,\qquad
\Gamma_*(u)=\Gamma_{\rm RO}(u)+a_*u(1-u),
\qquad
a_*=0.2682048,
\tag{1.2}
\]
where \(\Gamma_{\rm RO}(1/2)=C_0=6.4548\).
Its remaining universal implication is
\[
D_{\Gamma_*}(P;p)\ge0
\tag{1.3}
\]
for every composition-prime Boolean gate \(P\), every arity, and every interior product bias.

I also consume and apply two exact cross-account structural results.

1. `fleet01/B13/20260922T002604Z-gate-composition-prime/REPORT.md` proves the cofactor criterion for composition-primality and the exact gate-slack composition law. The checker below implements that exact cofactor criterion, not the older AND/OR-only `READONCE` classifier.
2. `fleet04/B17/20260922T031352Z-biased-restriction-margin-cocycle/REPORT.md`, observed blob `d32321447c5f30282f243d9a2907ec719d483c92`, proves the exact biased one-coordinate restriction cocycle retaining the branch/KL and vertical-overlap credits. I apply it to choose a genuinely asymmetric physical-gluing slice rather than another uniform-bias search.

The old missing implication is therefore (1.3). The adversarial question in this report is whether it already fails at arity five on the first nonuniform dyadic input spine.

## 2. The asymmetric slice

Let \(G:\{0,1\}^5\to\{-1,1\}\), with the owner's convention that the \(-1\) event has probability \(p_{\rm out}\). Take
\[
p_1=p_2=p_3=p_4={1\over2},\qquad p_5={1\over4},\qquad p_{\rm out}={1\over8}.
\tag{2.1}
\]

Write \(A_b\subseteq Q_4\) for the negative points in the restriction \(x_5=b\), and put \(a_b=|A_b|\). Each point of \(A_0\) has product mass \(3/64\), while each point of \(A_1\) has mass \(1/64\). Thus (2.1) is equivalent to
\[
3a_0+a_1=8,
\tag{2.2}
\]
so the only cases are
\[
(a_0,a_1)=(0,8),(1,5),(2,2).
\tag{2.3}
\]
There are exactly
\[
\binom{16}{8}+16\binom{16}{5}+\binom{16}{2}^2=12,870+69,888+14,400=97,158
\tag{2.4}
\]
truth tables in this slice.

In the restriction-cocycle language of the consumed fleet04/B17 theorem, these are exactly the three output-bias pairs
\[
(r_0,r_1)=(0,1/2),\quad(1/16,5/16),\quad(1/8,1/8)
\tag{2.5}
\]
glued through the physical pivot \(p_5=1/4\). Thus the test keeps the actual asymmetric product bias and the source-valid restriction geometry.

## 3. Exact biased Walsh arithmetic

For a four-bit restriction \(f_b=(-1)^{G_b}\), define the unnormalised uniform Walsh integers
\[
U_b(S)=\sum_{x\in Q_4} f_b(x)(-1)^{S\cdot x},\qquad S\subseteq[4].
\tag{3.1}
\]
At \(p_5=1/4\), the biased orthonormal Fourier coefficients of the parent occur in exact pairs:
\[
\widehat f(S)={3U_0(S)+U_1(S)\over64},\qquad \widehat f(S\cup\{5\})={\sqrt3\,[U_1(S)-U_0(S)]\over64}.
\tag{3.2}
\]
Hence every squared spectral mass is an exact rational
\[
{n_S\over4096},\qquad n_S=(3U_0+U_1)^2\quad\hbox{or}\quad n_{S5}=3(U_1-U_0)^2,
\tag{3.3}
\]
and Parseval is exactly \(\sum_S(n_S+n_{S5})=4096\).

Let
\[
A=\sum_{i=1}^4\operatorname{It}_i,\qquad B=\operatorname{It}_5.
\tag{3.4}
\]
Both are exact rationals with denominator 4096. The exact dyadic AND-chain values of the source read-once potential are
\[
\Gamma_{\rm RO}(1/4)=C_0-2,
\qquad
\Gamma_{\rm RO}(1/8)={3\over4}C_0-H_3,
\qquad H_3=4-{9\over8}\log_2 3,
\tag{3.5}
\]
and \(h_2(3/4)=2-(3/4)\log_2 3\). Therefore
\[
\boxed{
D_{\Gamma_{\rm RO}}
=
C_0\!\left(A+{4\over3}B-{3\over4}\right)
-8
+{1\over4096}\sum_{n\in\mathcal N}n\log_2 n
-\left(B+{9\over8}\right)\log_2 3,
}
\tag{3.6}
\]
where \(\mathcal N\) is the multiset of nonzero integer mass numerators. The quadratic-lift currency is
\[
W_G={I(G)\over4}-{7\over64},\qquad I=A+B,
\tag{3.7}
\]
and \(D_{\Gamma_*}=D_{\Gamma_{\rm RO}}+0.2682048W_G\).

## 4. Main exact/computer-assisted theorem

For every one of the 97,158 Boolean gates satisfying (2.1),
\[
\boxed{D_{\Gamma_{\rm RO}}(G;p)\ge0.}
\tag{4.1}
\]
Equality occurs for exactly 40 truth tables, in exactly two geometric types: 8 cases with \(A_0=\varnothing\) and \(A_1\) a coordinate half-cube of \(Q_4\), and 32 cases with \(A_0=A_1\) an edge of \(Q_4\). Every base equality case is decomposable. Every other gate satisfies
\[
\boxed{D_{\Gamma_{\rm RO}}\ge0.05685.}
\tag{4.2}
\]
Consequently the lifted candidate has
\[
\boxed{D_{\Gamma_*}>0}
\tag{4.3}
\]
throughout the slice, with smallest certified lifted defect at least \(0.0125721\).

For the base potential, every gate in the slice that depends on all five inputs satisfies
\[
\boxed{c_G=-D_{\Gamma_{\rm RO}}/W_G\le-0.72768.}
\tag{4.4}
\]
Equality occurs for 192 essential truth tables. One representative has
\[
A_0=\varnothing,\qquad A_1=\{0,1,2,3,4,5,8,10\},
\tag{4.5}
\]
with influence vector \((1/16,1/16,1/8,1/8,3/8)\), \(W_G=5/64\), and
\[
D_{\Gamma_{\rm RO}}={C_0-6\over8}=0.05685.
\tag{4.6}
\]

Using the exact fleet01/B13 cofactor criterion gives a stronger statement on the actual unresolved prime class. Exactly 73,016 of the 97,158 gates are composition-prime. Every one satisfies
\[
\boxed{
c_G\le-\left({2387\over1250}+{9\over4}\log_2 3\right)=-5.475765626622601408\ldots .}
\tag{4.7}
\]
There are 2,000 tight prime truth tables. For their tight signature,
\[
W_G={1\over8},\qquad D_{\Gamma_{\rm RO}}={2387\over10000}+{9\over32}\log_2 3.
\tag{4.8}
\]
Thus the prime gates in this nonuniform slice have a large negative base margin rather than approaching the positive lift floor.

## 5. Rigorous finite certificate

The checker enumerates all truth tables in (2.3), computes (3.3) using integers, and collapses all 97,158 gates to only 73 exact spectral/influence signatures. There are 66 signatures among the 96,562 gates depending on all five inputs and 43 signatures among the 73,016 composition-prime gates.

No floating-point logarithm is used for a sign decision. For every positive integer \(n\), write \(n=2^k y\), \(1\le y<2\), and \(z=(y-1)/(y+1)\in[0,1/3]\). The checker encloses
\[
\ln y=2\sum_{j=0}^{m-1}{z^{2j+1}\over2j+1}+R_m,
\qquad
0\le R_m\le{2z^{2m+1}\over(2m+1)(1-z^2)},
\tag{5.1}
\]
and independently encloses \(\ln2\), giving exact rational intervals for every \(\log_2 n\). The two zero signatures are handled symbolically, as are the tight essential and tight prime signatures; all other decisions use strict rational interval lower bounds.

Recorded facts: 97,158 gates; 73 exact signatures; 96,562 all-five-input gates; 73,016 composition-prime gates; 40 base zero gates, all decomposable; minimum nonzero base defect lower bound \(0.056849999999999999\); largest essential base margin \(-0.72768\); largest composition-prime base margin (4.7); smallest lifted defect lower bound \(0.0125721\).

Checker SHA-256: `8d79ba1e13da77d10b78350bfdb46d3a96dbdd733f63b168e933a14db808942a`.

Captured PASS output SHA-256: `e6a66a60fc2da9065184d08876d0ceef841b89f2fdc4ef7d30f4d1e00d3c202c`.

## 6. Replacement obligation and full-FEI implication

No FEI candidate was refuted in this run. The stable scalar lift survives this genuinely nonuniform arity-five slice. The stronger adversarial hope that the first dyadic asymmetric pivot \(p_5=1/4\), at output mass \(1/8\), reveals a hidden prime obstruction is refuted on this exact slice.

Do not extrapolate this to all arity-five biases. The next decisive attack should leave this dyadic spine: either analyze the isolated four-input composition-prime class \(B_0=\{0,1,2,3,4,5,8,10\}\) at fully nonuniform interior product biases, or use a genuinely non-dyadic arity-five prime gate/bias vector. The first is preferable because the tight essential witness above is literally the \(B_0\) negative set gated by the fifth literal; this certificate shows that the tested dyadic gluing itself creates no positive margin.

**Consumed peer artifacts:** fleet01/B18 stable `LIMIT-PRIME-GATE-LIFT-v1`; fleet01/B13 composition-prime reduction; fleet04/B17 exact biased restriction cocycle.

**Next recipient:** fleet04/B17 for its B0 all-bias line and fleet01/B18 for the stable prime-gate chain.

**Old missing implication:** prove or refute \(D_{\Gamma_*}(P;p)\ge0\) for every composition-prime Boolean gate and every interior product bias.

**New proved inference:** it holds for every five-input gate with \((p_1,p_2,p_3,p_4,p_5)=(1/2,1/2,1/2,1/2,1/4)\) up to coordinate order and \(p_{\rm out}=1/8\), including all 73,016 composition-prime gates in that slice; in fact the base potential has the strict prime margin separation (4.7).

**Replacement obligation:** attack B0 or another composition-prime gate at genuinely non-dyadic interior biases; do not repeat the uniform central, uniform quarter-output, equal-bias EQ_d, or this 1/4-spine slice.

**Implication to full FEI:** positive but partial. One exact asymmetric product-bias slice of the universal prime-gate implication is closed. The all-arity/all-bias quantifier remains open.

**Full uniform-cube FEI remains OPEN / NOT PROVED.**
