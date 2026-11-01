# Balanced substitution defeats the full pivotal-resolvent entropy bound

19 September 2026. **Full Friedgut–Kalai FEI: OPEN.**

This is a continuation of the exact next step proposed in the September 19 coded-budget report. Its main conclusion is negative and precise: the proposed inequality `D_cross <= K(C+Q_log)` is false for every finite universal K. The construction is balanced, monotone, and transitive on its input coordinates. It is not a counterexample to FEI. New positive results here are exact substitution identities and an unconditional entropy bound identifying the additional information that the failed budget discards. Novelty and independent review are not certified.

## 1. Main theorem and what must be corrected

Use the normalizations of the existing report. For Boolean f on the uniform cube, write H(f) for base-two Fourier entropy, I_i for coordinate influence, j_i=min(I_i,1-I_i), J=sum_i j_i, and

\[
D_\times(f)=2H(f)-\mathbb E_zH(f(x)f(x+z)),\qquad
Q(f)=\sum_i j_i^2\log_2(1/j_i).
\]

For u_i(x)=f(x)f(x+e_i), the proposed full pivotal resolvent is

\[
\mathcal C(f)=\sum_i\sum_{A\ne\varnothing}
\frac{\widehat u_i(A)^2}{1+|A|}.
\]

Zero logarithmic terms are zero. These conventions agree with `continuations/2026-09-19-coded-budget/REPORT.md`.

**Theorem 1 (failure of the proposed next step).** There is an explicit family F_m of balanced monotone Boolean functions, each invariant under a transitive permutation group on its coordinates, such that

\[
\mathcal C(F_m)\longrightarrow4,\qquad Q(F_m)\longrightarrow0,
\qquad D_\times(F_m)\longrightarrow\infty.
\tag{1}
\]

Consequently no finite dimension-free K satisfies

\[
D_\times(f)\le K[\mathcal C(f)+Q(f)]
\tag{2}
\]

for every Boolean f, even after restricting to balanced monotone transitive functions. Nevertheless,

\[
\frac{H(F_m)}{I(F_m)}\longrightarrow4.
\tag{3}
\]

The earlier discounted bounds for C and Q are not contradicted. The failed statement is the *pointwise* estimate (2). Its reported implication to FEI was conditional; that sufficient premise is now disproved. The earlier scalar-budget obstruction remains valid and is not being replaced by a claim to have refuted FEI.

## 2. The pivotal resolvent collapses to level mass on monotone functions

Work temporarily on {-1,+1}^n with the usual product characters. Let

\[
b_i(x_{-i})=\mathbf1_{\{f(1,x_{-i})\ne f(-1,x_{-i})\}}
\]

be the pivotal indicator. Then u_i=1-2b_i, and

\[
\mathcal C_i=4\sum_{A\ne\varnothing}\frac{\widehat b_i(A)^2}{1+|A|}.
\]

If f is increasing, its signed derivative `(f(1,x_-i)-f(-1,x_-i))/2` equals b_i. Therefore

\[
\widehat b_i(A)=\widehat f(A\cup\{i\}),\quad
\widehat f(\{i\})=I_i(f).
\]

Summing over i proves the exact identity

\[
\boxed{\mathcal C(f)=4\sum_{|S|\ge2}\widehat f(S)^2
=4\left(\operatorname{Var}(f)-\sum_i I_i(f)^2\right).}
\tag{4}
\]

The same identity holds for unate functions after reversing the required input signs. In particular C<=4 for every monotone Boolean function, regardless of its dimension or total influence. Equation (4) concerns the actual pivotal spectrum; it is not an approximation or an assumption of independent pivots.

For an arbitrary Boolean f, a related one-sided bound follows from the positive noise kernel: if phi_i is the signed derivative, then |phi_i|=b_i and `Stab_rho(phi_i)<=Stab_rho(b_i)` for 0<=rho<=1. Integrating and summing yields

\[
4\operatorname{Var}(f)\le\mathcal C(f)+4\sum_i I_i(f)^2.
\tag{5}
\]

The distinction between equality for monotone functions and inequality for arbitrary functions is essential.

## 3. Allocation information survives balanced block substitution

### 3.1 A quantity that the local budget misses

Let S,T be independent samples from p_f(A)=fhat(A)^2, and set

\[
U=S\triangle T,\qquad W=S\cap T.
\]

Define two conditional entropies

\[
L(f)=H(S\mid U),\qquad
\mathfrak A(f)=H(S\mid U,W).
\tag{6}
\]

The latter measures the uncertainty in assigning the exclusive elements U to the first or second sample when their common elements are already known. This report calls it *allocation entropy*; that is descriptive terminology, not a claim that the underlying conditional entropy is new.

Averaging derivative spectra gives the XOR convolution p_f*p_f. Indeed,

\[
\widehat{f f^z}(u)=\sum_s\widehat f(s)\widehat f(s+u)(-1)^{(s+u)\cdot z},
\]

and Parseval in z eliminates all unequal s cross terms. Consequently

\[
D_\times(f)=L(f)+I(Z;V)\ge L(f)\ge\mathfrak A(f),
\tag{7}
\]

where `(Z,V)` has uniform Z and conditional law `P(V=u|Z=z)=widehat{f f^z}(u)^2`. This mixture coupling is different from the independent-samples construction of S,T; only their u marginals are identified.

The additional standard Walsh uncertainty argument gives D_cross<=2L. To state it precisely, for each u of positive XOR mass q_u, normalize the real vector `a_s a_{s+u}/sqrt(q_u)`. Its squared-entry entropy is H(S|U=u); the entropy of its orthonormal Walsh transform is at least n-H(S|U=u), by the finite-dimensional entropic uncertainty inequality. Hence I(Z;V)<=L(f). This is the same uncertainty ingredient used in the September 13 archive, not a newly established uncertainty principle.

### 3.2 Exact substitution identities

Let h be a Boolean function on m coordinates. Let g_1,...,g_m be balanced Boolean functions on disjoint coordinate blocks. Put F=h(g_1,...,g_m). Since each inner constant Fourier coefficient is zero, a spectral sample of F is generated exactly by:

1. sampling an outer set A from hhat(A)^2;
2. for each i in A, independently sampling a nonempty inner set from g_i-hat squared;
3. taking their disjoint-block union.

The outer set is recoverable from the nonempty blocks of the final sample. Expanding the characters proves this rule directly. In particular the familiar composition identities are

\[
H(F)=H(h)+\sum_i I_i(h)H(g_i),\qquad
I(F)=\sum_i I_i(h)I(g_i).
\tag{8}
\]

These standard composition identities overlap the framework of O'Donnell–Tan (2013), which is credited below.

Take two independently generated samples S,T of F. Write A,B for their outer sets, Y=(A triangle B,A intersection B), and U,W for the fine-coordinate XOR and intersection. Then

\[
\boxed{L(F)=\mathfrak A(h)+\sum_i I_i(h)^2 L(g_i)+H(Y\mid U).}
\tag{9}
\]

Also

\[
\boxed{\mathfrak A(F)=\mathfrak A(h)+\sum_i I_i(h)^2\mathfrak A(g_i)
 +H(A\cap B\mid U,W).}
\tag{10}
\]

Both correction entropies are nonnegative. Thus D_cross(F)>=A(h), and even A(F)>=A(h), for every choice of balanced inner functions.

**Proof of (9).** Because every active inner spectral sample is nonempty, Y is a function of (S,U): recover T from S and U, then recover A and B from their nonempty blocks. The conditional chain rule gives
`H(S|U)=H(Y|U)+H(S|U,Y)`.
Given Y, the distribution of the observed fine XOR U is independent of the orientation allocating outer exclusive blocks to A or B. Each such block contains one inner sample with the same distribution whichever side it belongs to. Thus the orientation costs exactly A(h). Conditional on that orientation, the exclusive blocks of S are determined by U; each common block contributes L(g_i), and its occurrence probability is I_i(h)^2. This proves (9), including nonidentical inner functions.

**Proof of (10).** Use the same argument conditioned on (U,W). In an outer common block, the remaining uncertainty is A(g_i). The coarse union A union B is visible from the fine union U union W, so the conditional uncertainty in Y is exactly H(A intersection B|U,W). No independence between the different coordinates of A is assumed in either proof.

### 3.3 Exact closure for odd inner functions

A balanced function g is odd (self-dual) when g(-x)=-g(x). Its Fourier support then contains only sets of odd cardinality. If every inner g_i is odd, the correction in (10) vanishes identically:

\[
\boxed{\mathfrak A(h(g_1,\ldots,g_m))
=\mathfrak A(h)+\sum_i I_i(h)^2\mathfrak A(g_i).}
\tag{10a}
\]

Indeed, in a given block, a single active spectral sample has odd XOR cardinality, while two active samples have even XOR cardinality. If the fine union is empty the block is inactive. These observations determine the outer common set A intersection B from the fine XOR and intersection. This is why the conditional entropy in (10) is zero. The outer function h need not be monotone or odd for (10a).

## 4. Majority has unbounded allocation entropy

Let m=2r+1>=3 and h=Maj_m. Put

\[
b_s=4^{-s}\binom{2s}{s},\qquad b_0=1.
\]

Every coordinate influence is b_r. A spectral sample K=|S| is supported on odd sizes and has exact law

\[
q_s:=\Pr(K=2s+1)=\frac{m b_r b_s b_{r-s}}{2s+1},\quad 0\le s\le r.
\tag{11}
\]

For completeness, differentiate majority in one coordinate. The pivotal indicator is that the other 2r signs sum to zero. Conditional on that event, the expected product of 2s specified signs equals `(-1)^s binom(r,s)/binom(2r,2s)`, by taking coefficients in `(1-t^2)^r`. Therefore the coefficient at a set of size 2s+1 is `(-1)^s b_r binom(r,s)/binom(2r,2s)`. Squaring and multiplying by binom(m,2s+1), then cancelling factorials, gives (11). This exact level formula was also used in the preceding majority obstruction; it is reused here for a different conditional entropy.

For independent sizes K,K' and intersection size A0=|S intersection T|, exchangeability implies that, conditional on U,W,K,K', S minus W is uniform among the `(K-A0)`-subsets of U. Hence

\[
\mathfrak A(\operatorname{Maj}_m)
\ge\mathbb E\log_2\binom{K+K'-2A_0}{K-A_0}
\ge\mathbb E\min(K,K')-\mathbb E A_0.
\tag{12}
\]

The last inequality uses `binom(a+b,a)>=2^{min(a,b)}` for nonnegative integers: if a<=b, each factor `(b+j)/j` in the product for the binomial coefficient is at least two. Also E A0=m b_r^2. If `T_a=sum_{s=a}^r q_s`, the odd support of K gives

\[
\boxed{\mathfrak A(\operatorname{Maj}_m)
\ge B_m:=1+2\sum_{a=1}^{r}T_a^2-m b_r^2.}
\tag{13}
\]

B_m is an explicitly computable rational number; no logarithm evaluation is required for this lower bound.

A convenient all-dimensional estimate is

\[
\boxed{\mathfrak A(\operatorname{Maj}_{2r+1})
\ge\frac1{18}\sum_{a=1}^{r}\frac1a+\frac1{36}.}
\tag{14}
\]

**Proof.** The recurrence `b_{s+1}/b_s=(2s+1)/(2s+2)` proves

\[
\frac1{2\sqrt s}\le b_s\le\frac1{\sqrt{3s+1}}\quad(s\ge1).
\tag{15}
\]

For the lower inequality, start at s=1 and compare the squared recurrence with s/(s+1); their numerator difference is one. For the upper inequality compare it with `(3s+1)/(3s+4)`; after multiplication the right numerator exceeds the left by s. Both inductions are non-strict at s=1 and propagate in the required direction.

Since b_s decreases, `m b_r b_{r-s}>=m b_r^2>=1/2`. Thus for s>=1,

\[
q_s\ge\frac1{4\sqrt s(2s+1)}\ge\frac1{12s^{3/2}},
\]

and integration of the decreasing function x^(-3/2) gives

\[
T_a\ge\frac16\left(\frac1{\sqrt a}-\frac1{\sqrt{r+1}}\right).
\]

Consequently

\[
1+2\sum_{a=1}^rT_a^2
\ge1+\frac1{18}\left[\sum_{a=1}^r\frac1a
-\frac2{\sqrt{r+1}}\sum_{a=1}^r\frac1{\sqrt a}+\frac r{r+1}\right]
\ge\frac79+\frac1{18}\sum_{a=1}^r\frac1a.
\]

Here `sum a^(-1/2)<=2 sqrt(r)<=2 sqrt(r+1)`. By (15), `m b_r^2<=(2r+1)/(3r+1)<=3/4`. Subtracting this from the preceding display proves (14). The proof does not require the two spectral samples to be disjoint; it pays for their actual expected intersection.

## 5. The explicit balanced, monotone, transitive counterfamily

Let g_d be recursive ternary majority of depth d, with g_0(x)=x. It has 3^d inputs, is balanced and monotone, and its automorphism group is transitive on the leaves. Every coordinate influence is 2^(-d). These facts follow by induction from the corresponding facts for Maj_3. Its spectrum gives

\[
I(g_d)=(3/2)^d,\qquad H(g_d)=4[(3/2)^d-1].
\tag{16}
\]

Indeed Maj_3 has three singleton Fourier coefficients +1/2 and one triple coefficient -1/2; its entropy is two and its influence is 3/2. Formula (8) gives the entropy recursion `H_d=2+(3/2)H_{d-1}`, with H_0=0.

For every odd m>=3 set

\[
d=\lceil\log_2m\rceil,\qquad
F_m=\operatorname{Maj}_m(g_d(x^{(1)}),\ldots,g_d(x^{(m)})).
\tag{17}
\]

Its dimension is N_m=m 3^d. Permutations of the m blocks and the inner tree automorphisms act transitively on all N_m inputs. The function is balanced and monotone. Every influence equals

\[
j=b_r 2^{-d}<1/2,
\]

so J=I. Since all inner majorities are odd, (10a) also gives the exact strengthening

\[
\mathfrak A(F_m)=\mathfrak A(\operatorname{Maj}_m)+3m b_r^2[1-(3/4)^d].
\tag{17a}
\]

Here \(\mathfrak A(g_d)=3[1-(3/4)^d]\): \(\mathfrak A(\operatorname{Maj}_3)=3/4\), and (10a) gives the recursion \(A_d=3/4+(3/4)A_{d-1}\). The value 3/4 follows directly from the four equiprobable singleton/triple spectral sets: 12 of the 16 ordered sample pairs are distinct and have one bit of allocation uncertainty; the other four have none. Write

\[
V_m=N_m j^2=m b_r^2(3/4)^d.
\]

Equations (4) and the equal influences give the exact formulas

\[
\boxed{\mathcal C(F_m)=4(1-V_m),\qquad
Q(F_m)=V_m\left[d+\log_2(1/b_r)\right].}
\tag{18}
\]

Since m b_r^2<=3/4 and `log_2(1/b_r)<=(d+1)/2`,

\[
0\le Q(F_m)\le\frac38(3d+1)(3/4)^d\longrightarrow0.
\tag{19}
\]

Thus C(F_m)->4. On the other hand, (7), (10), and (14) imply

\[
\boxed{D_\times(F_m)\ge\frac{H_r^{\rm harm}}{18}+\frac1{36}
\longrightarrow\infty.}
\tag{20}
\]

This proves the first and main part of Theorem 1. It also proves at least logarithmic growth of the best constant for (2) along this family: N_m<=3 m^(1+log_2 3), whereas H_r^harm>=ln(r+1). In particular the obstruction is Omega(log N_m), not merely a violation of a small numerical constant.

Every fixed logarithmic-power replacement `Q_beta=sum_i j_i^2[log_2(1/j_i)]^beta`, beta>=0, also tends to zero on (17). Therefore `D_cross<=K(C+Q_beta)` fails for all finite K and every fixed finite beta. This statement concerns squared marginals with logarithmic powers, not every conceivable entropy budget.

### 5.1 Why this does not refute FEI

Let I_m=m b_r and H_m=H(Maj_m). Equations (8) and (16) give exactly

\[
\frac{H(F_m)}{I(F_m)}
=4+\left(\frac{H_m}{I_m}-4\right)(2/3)^d.
\tag{21}
\]

The elementary estimates H_m<=m and b_r>=1/(2 sqrt(r)) yield `H_m/I_m<=sqrt(2m)`. Also `(2/3)^d<=m^{-log_2(3/2)}`. Because log_2(3/2)>1/2, the correction in (21) tends to zero. This proves (3) without assuming FEI, including FEI for majority.

### 5.2 An explicit finite symbolic witness against K=8

One may take r=2^1024, m=2r+1 and d=1026 in (17). Since `H_r^harm>ln(r)>1024*(2/3)`, (20) gives `D_cross>4099/108`. Formula (19) gives Q<1/4: it is enough to verify `(3d+1)(3/4)^d<1/4` at d=20 and its monotone decrease thereafter; (19) is stronger still. Since C<=4,

\[
\frac{D_\times(F_m)}{\mathcal C(F_m)+Q(F_m)}
>\frac{4099}{459}>8.
\tag{22}
\]

This is a finite function given by an explicit recursive formula, not a practically enumerated truth table. The lower bound comes from the proof, with elementary finite rational comparisons checked in the verifier. The all-constant failure follows from (18)–(20), not from (22) alone.

## 6. A further positive identity: exact resolvent behavior under substitution

The collapse in (4) has a broader explanation. For any Boolean outer h and a *common* balanced monotone inner function g, put F=h(g,...,g) on disjoint blocks. Then

\[
\boxed{\mathcal C(F)+4\sum_{i,j} I_{ij}(F)^2
=\mathcal C(h)+4\sum_i I_i(h)^2.}
\tag{23}
\]

Equivalently, since `I_ij(F)=I_i(h)I_j(g)`,

\[
\mathcal C(F)=\mathcal C(h)+4\sum_i I_i(h)^2
\left[1-\sum_j I_j(g)^2\right].
\]

The common-inner-function hypothesis in (23) is deliberate; the proof must not silently extend a one-parameter substitution identity to arbitrary different inner functions.

**Proof.** Define the noise stability polynomial `s_g(rho)=sum_A ghat(A)^2 rho^|A|`. Its endpoints are s_g(0)=0 and s_g(1)=1. The pivotal indicator for coordinate (i,j) of F is
`b_i(h)(g(x^(l)):l!=i) b_j(g)(x^(i))`.
For a rho-correlated pair of inputs, the different blocks are independent; each balanced inner output pair has correlation s_g(rho). Therefore

\[
\operatorname{Stab}_\rho(b_{ij}(F))
=\operatorname{Stab}_{s_g(\rho)}(b_i(h))
\operatorname{Stab}_\rho(b_j(g)).
\]

Monotonicity of g implies `sum_j Stab_rho(b_j(g))=s'_g(rho)` by its signed derivative Fourier formula. Finally,

\[
\sum_i\int_0^1\operatorname{Stab}_\rho(b_i(f))d\rho
=\mathcal C(f)/4+\sum_i I_i(f)^2.
\]

Sum over i,j and substitute t=s_g(rho) in the polynomial integral to obtain (23). The proof uses no approximation, no independence among outer coordinates of the spectral sample, and no FEI assumption.

### 6.1 A positive pointwise theorem for read-once odd monotone formulas

For a balanced monotone gate h put

\[
\delta(h)=1-\sum_i I_i(h)^2=\mathcal C(h)/4.
\]

For a read-once composition F=h(g_1,...,g_m) of odd monotone functions on disjoint variable blocks, (10a) and the influence product formula yield the matched recursions

\[
\mathfrak A(F)=\mathfrak A(h)+\sum_i I_i(h)^2\mathfrak A(g_i),
\]
\[
\delta(F)=\delta(h)+\sum_i I_i(h)^2\delta(g_i).
\tag{23a}
\]

Therefore a gatewise bound A(h)<=kappa delta(h) is preserved, with the *same* kappa, under arbitrary read-once compositions of those gates. Gates of zero delta are dictators in this monotone balanced setting and have zero allocation entropy, so they cause no denominator problem.

In particular every read-once ternary-majority formula F, including unequal tree depths, satisfies exactly

\[
\boxed{\mathfrak A(F)=\tfrac34\mathcal C(F).}
\tag{23b}
\]

Indeed the ternary gate has A=3/4 and delta=1/4, so A=3 delta at every node; projections have both quantities zero. Combining with the universal estimate (25) below proves

\[
\boxed{D_\times(F)\le\tfrac32\mathcal C(F)+(4+2/\ln2)Q(F).}
\tag{23c}
\]

This is a genuine dimension-independent bound for the original pointwise target on a precisely specified infinite class. By additivity it extends to disjoint products and character multiples of those formulas. It does not settle the full target: the counterfamily uses outer majority gates of unbounded arity, whose ratio A(h)/delta(h) is unbounded by (14).

Nor can one apply (23c) to every later multiplicative derivative without proof: that derivative need not remain a read-once ternary-majority formula. FEI results for bounded-arity read-once formulas already exist in the composition literature. This is a pointwise resolvent/allocation result within the present program, not a claim to newly resolve FEI for a previously untouched broad class.

## 7. An unconditional entropy estimate and the genuinely global missing step

The elementary identity

\[
L(f)=\mathfrak A(f)+H(W\mid U)
\tag{24}
\]

follows because W is determined by S and U. Multiplication by a character preserves H,D,C,Q,L and A. For A, on a complemented spectral coordinate the pair (U_i,W_i) changes bijectively: W_i is complemented when U_i=0 and remains zero when U_i=1. Thus we may first choose a character making every spectral marginal equal to j_i<=1/2.

Conditional entropy subadditivity and coordinate independence between S and T give

\[
H(W\mid U)\le\sum_i H(W_i\mid U_i).
\]

For a marginal j, put q_0=j^2+(1-j)^2. Directly,

\[
H(W_i\mid U_i)=j^2\log_2(q_0/j^2)
 +(1-j)^2\log_2(q_0/(1-j)^2)
\le2j^2\log_2(1/j)+j^2/\ln2.
\]

Here q_0<=1 bounds the first term, and ln(1+x)<=x bounds the second. Since log_2(1/j)>=1,

\[
\boxed{\mathfrak A(f)\le D_\times(f)
\le2\mathfrak A(f)+(4+2/\ln2)Q(f).}
\tag{25}
\]

The upper bound uses D_cross<=2L from Section 3. The information represented by A is not controlled pointwise by C+Q, as Theorem 1 proves.

Let f_k be the independent uniform multiplicative-derivative chain from the preceding report. Define its accumulated allocation entropy

\[
\mathcal T(f)=\sum_{k\ge0}2^{-k}\mathbb E\mathfrak A(f_k).
\tag{26}
\]

The chain reaches a constant after at most n steps because each multiplicative derivative lowers the algebraic degree of the phase over F_2. Thus this is a finite quantity. The previously proved exact telescoping identity and Q-payment bound are

\[
H(f)=\tfrac12\sum_k2^{-k}\mathbb E D_\times(f_k),\qquad
\sum_k2^{-k}\mathbb E Q(f_k)\le\tfrac52 J(f).
\]

Using (25) gives the valid pointwise comparison

\[
\boxed{\tfrac12\mathcal T(f)\le H(f)
\le\mathcal T(f)+\left(5+\frac5{2\ln2}\right)J(f).}
\tag{27}
\]

The Q-payment is inherited from Section 7.4 of the coded-budget report; this continuation does not claim to have first proved it. Consequently a uniform bound `T(f)<=L J(f)` is equivalent, at the level of existence of universal constants, to FEI. If C_T=sup T/J and C_FEI=sup H/I, character minimization yields

\[
C_T/2\le C_{\rm FEI}\le C_T+5+5/(2\ln2).
\tag{28}
\]

**No finite universal bound on C_T is proved here.** Equations (27)–(28) identify a remaining global information cost; they are not a solution or evidence that the cost is easy to bound. Nor is there a justification for replacing T by its first-step A or by the failed first-step resolvent. The other correctly quantified erasure route remains available.

## 8. Verification and provenance

`verify_next_step.py` supplies actual finite self-checks and writes `verification.json`. The executed run passed 1,850 entropy comparisons over 370 distinct canonical functions, including all truth tables through dimension three and all 168 increasing functions on four variables. It also passed 128 common-inner substitution identities, ten exact conditional-entropy substitution identities, four unequal ternary-tree examples, eight non-odd monotone-inner examples, and a nonzero allocation-defect example. Exact majority level weights were matched against truth tables through eleven variables; rational lower bounds were evaluated through 1,025 outer coordinates. These are finite self-checks, not universal enumeration. Exact Walsh transforms, pivotal identities, probability-mass composition and rational inequalities use integers/Fractions. Entropy expressions are reduced to rational linear combinations of logarithms of primes; nonzero comparisons use outward rational logarithm intervals. Finite tests support the formulas but do not replace the proofs for all m.

The finite symbolic witness in Section 5.2 is checked from its analytic inequalities, not by creating its enormous truth table. Floating exploratory values, when included separately, are not accepted as proofs. No Lean compilation or independent expert audit is claimed.

Direct predecessor: `proofnet24/P03-fei/continuations/2026-09-19-coded-budget/REPORT.md`, Git blob `6bd3cef08192616a27053f01edb94863e7ad3720`, especially Sections 2, 7.1, 7.4, and 8. The current index was read from master, blob `82e045faae2753a2bf3cac12ee51c4c3a74abcab`. At initial inspection, `scheduled-continuation/` contained its README but no run report; that observation is not a claim about future executions.

The exact majority level weights and the Walsh uncertainty ingredient were already present in earlier FEI material. They are expressly reused. The proofs of the resolvent identities, the allocation substitution formulas, the harmonic lower bound and the counterfamily are the continuation recorded here. No exhaustive reread of the 1,506-page archive or global novelty search is asserted.

Outside primary-source comparison, checked 19 September 2026:

- Ryan O'Donnell and Li-Yang Tan, *A composition theorem for the Fourier Entropy-Influence conjecture*, arXiv:1304.1347 (2013). Balanced spectral sampling and entropy/influence composition are standard consequences within that framework; no novelty is claimed for (8).
- Hans Maassen and J. B. M. Uffink, *Generalized entropic uncertainty relations*, Physical Review Letters 60 (1988), 1103–1106, DOI 10.1103/PhysRevLett.60.1103. This supplies the standard orthonormal-Walsh entropy uncertainty used for the upper half of (25).
- María José González, Paul MacManus and María Cristina Pereyra, *Further evidence towards the Fourier Entropy-Influence conjecture*, arXiv:2606.00246 (2026). Their coordinate-restriction induction framework is distinct from the false multiplicative-derivative resolvent inequality refuted here. This report does not claim to settle their proposed inequalities.

## 9. Worker-facing correction

Do not continue attempting to prove `D_cross<=K(C+Q_log)` as a universal statement or merely enlarge K: Theorem 1 rules out every finite K. Do not call this a disproof of FEI. Keep the earlier valid packet and discounted-budget theorems, subject to their independent verification, and preserve their proofs and historical status.

Any new first-step entropy budget must retain the outer allocation uncertainty that survives balanced low-influence substitution. Equations (9), (10), and (23) are concrete tests for proposed replacements. An argument based only on the local resolvent and damped squared marginals fails them.

A genuinely useful next advance would establish a universal accumulated allocation bound, improve a full-scope hereditary erasure inequality, or supply a different global signed Fourier argument. Rephrasing (26) without bounding it is not closure. The source target remains OPEN. No unrelated task, source ownership, schedule, repository visibility, or existing mathematical file is changed by this report.
