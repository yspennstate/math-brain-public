# Sharp variance accumulation, minimum affine influence, and a constant-four FEI class

19 September 2026. **Full Friedgut–Kalai FEI is not proved in this report.**

This continuation develops positive estimates after the scalar and full pivotal-resolvent pointwise proposals were disproved. The main results are: a sharp bound for variance over the entire multiplicative-derivative chain; exact tensorization and a closed formula on monotone functions for minimum affine influence; and a constant-four entropy–influence theorem preserved under arbitrary surjective affine mixing of a specified product class. The last statement is a genuine FEI bound, but only for its stated class. The universal accumulated allocation estimate remains unproved.

The proofs below are analytical. The accompanying executed rational checks are self-checks, not independent review or Lean verification. The basic seed results and standard Fourier composition are credited to earlier work; novelty of the combined statements has not been established.

## 1. Definitions and the exact current objective

All input spaces have the uniform measure. Write the cube as the additive vector space V=F_2^n, and let f:V->{-1,1}. Define

\[
\widehat f(s)=\mathbb E_x f(x)(-1)^{s\cdot x},\quad p_f(s)=\widehat f(s)^2,
\]
\[
H(f)=\sum_s p_f(s)\log_2\frac1{p_f(s)},\qquad
I_i(f)=\Pr[f(x)\ne f(x+e_i)],\quad I(f)=\sum_i I_i(f),
\]
\[
j_i(f)=\min\{I_i(f),1-I_i(f)\},\qquad J(f)=\sum_i j_i(f).
\]

Zero logarithmic terms are zero. The original conjecture asks for an absolute finite C such that H(f)<=C I(f) for all n and f. Multiplication by a character shifts the spectrum, preserves H, and can minimize I to J.

For independent uniform shifts Z_1,Z_2,..., let

\[
f_0=f,\qquad f_{k+1}(x)=f_k(x)f_k(x+Z_{k+1}).
\tag{1.1}
\]

Writing f=(-1)^P with its multilinear F_2 polynomial shows that each nonconstant multiplicative derivative lowers the algebraic degree. Thus f_k is constant once k>=n; zero shifts or other degeneracies may terminate earlier.

For independent spectral samples S,T with law p_f, let

\[
\mathfrak A(f)=H(S\mid S\triangle T,S\cap T),\qquad
\mathcal T(f)=\sum_{k\ge0}2^{-k}\mathbb E\mathfrak A(f_k).
\tag{1.2}
\]

The previous balanced-substitution report proves

\[
\tfrac12\mathcal T(f)\le H(f)
\le\mathcal T(f)+\left(5+\frac5{2\ln2}\right)J(f).
\tag{1.3}
\]

For the lower half, one needs only the elementary mixture identity. The average derivative spectrum is the XOR law of S and T. Thus, with a spectral sample V from the random derivative conditional on Z,

\[
D_\times(f)=2H(f)-\mathbb E_ZH(p_Z)
=H(S\mid S\triangle T)+I(Z;V)\ge\mathfrak A(f).
\]

The exact telescoping relation H(f)=(1/2)sum_k 2^{-k} E D_cross(f_k) then proves T<=2H. This elementary argument, not an unproved FEI estimate, is the part needed later for the class theorem. The upper half of (1.3) and its already stated hypotheses are retained from the predecessor. The universal bound T(f)<=C J(f) is still unproved here. In particular, the previously disproved pointwise estimates involving only R+Q or the full pivotal resolvent C+Q are not reused.

## 2. Sharp variance accumulation for every Boolean function

Define

\[
\mathcal V(f)=\sum_{k\ge0}2^{-k}\mathbb E\operatorname{Var}(f_k).
\tag{2.1}
\]

**Theorem 2.1.** For every Boolean function,

\[
\boxed{\mathcal V(f)\le2I(f).}
\tag{2.2}
\]

The constant two is optimal. No assumption about monotonicity, Fourier support, algebraic degree, or coordinate independence of the spectral sample is imposed.

### 2.1 A one-dimensional recursion bounds the full chain

Let mu=E f, and put

\[
b_k=\mathbb E\bigl[(\mathbb E_x f_k(x))^2\bigr].
\]

For a fixed Boolean g, the autocorrelation identity and Parseval give

\[
\mathbb E_z\left(\mathbb E_x g(x)g(x+z)\right)^2
=\sum_s\widehat g(s)^4\ge(\mathbb E g)^4.
\]

Conditioning on f_k and then applying Jensen therefore yields b_{k+1}>=b_k^2. Since b_0=mu^2,

\[
b_k\ge|\mu|^{2^{k+1}}.
\tag{2.3}
\]

Set delta=(1-|mu|)/2 in [0,1/2]. As f_k is Boolean, Var(f_k)=1-(E f_k)^2, so

\[
\mathcal V(f)\le W(\delta):=
\sum_{k\ge0}2^{-k}\left[1-(1-2\delta)^{2^{k+1}}\right].
\tag{2.4}
\]

The upper bound is an ordinary convergent infinite series, even though the actual chain sum is finite. It satisfies

\[
W(\delta)=4\delta(1-\delta)+\tfrac12W(2\delta(1-\delta)).
\tag{2.5}
\]

### 2.2 A sharp-order supersolution

Let w(delta)=4 delta log_2(1/delta), with w(0)=0. We claim

\[
w(\delta)\ge4\delta(1-\delta)+\tfrac12w(2\delta(1-\delta))
\quad(0\le\delta\le1/2).
\tag{2.6}
\]

After expanding the logarithm, the difference is

\[
4\delta\left[\delta\log_2(1/\delta)
 -(1-\delta)\log_2(1/(1-\delta))\right].
\]

The bracket is nonnegative. Indeed its natural-log version vanishes at zero and at 1/2, and its second derivative is (2delta-1)/(delta(1-delta))<=0. It is concave between its zero endpoints. Iterating (2.6), then letting the residual geometric factor tend to zero, proves

\[
W(\delta)\le4\delta\log_2(1/\delta).
\tag{2.7}
\]

This is a supersolution inequality, not an assertion that W=w for every delta.

### 2.3 Edge isoperimetry, including a short proof

The elementary cube edge-isoperimetric inequality is

\[
I(f)\ge2\delta\log_2(1/\delta)
\tag{2.8}
\]

for the smaller of the two level sets of f. Here is an induction proof with the present normalizations. For an arbitrary subset of density delta, let its two coordinate sections have densities a,b, with a<=b. The average within-section influence is at least a log_2(1/a)+b log_2(1/b) by induction; the crossing influence in the split coordinate is at least b-a. Put a+b=2delta and t=a/(a+b). The sum of these lower bounds is

\[
2\delta\left[\log_2(1/(2\delta))+h_2(t)+1-2t\right]
\ge2\delta\log_2(1/\delta),
\]

because h_2(t)>=2t on [0,1/2] by concavity. Constant sections and zero densities are interpreted by continuity. The zero-dimensional base is immediate. This proves (2.8) without a conjectural entropy estimate.

Combining (2.4), (2.7), and (2.8) proves Theorem 2.1.

### 2.4 Exact sharpness family

For r>=1, let w_r(x)=1-2*1_{x=0} on F_2^r. After k multiplicative derivatives, it is constant if the k shifts are linearly dependent. If they are independent, it equals -1 precisely on their k-dimensional span. The probability of independence is

\[
P_{r,k}=\prod_{j=0}^{k-1}(1-2^{j-r}).
\]

For k<r, the conditional variance is 4*2^{k-r}(1-2^{k-r}); for k=r it is zero. Thus

\[
\mathcal V(w_r)=4\,2^{-r}\sum_{\ell=1}^r P_{r,\ell},
\qquad I(w_r)=2r\,2^{-r},
\]
\[
\boxed{\frac{\mathcal V(w_r)}{I(w_r)}
=\frac2r\sum_{\ell=1}^rP_{r,\ell}\longrightarrow2.}
\tag{2.9}
\]

For example, 1-P_{r,ell}<=sum_{j<ell}2^{j-r}<2^{ell-r}; summing over ell bounds the total deficiency by two. This gives the explicit lower bound 2-4/r on the ratio, in addition to its upper bound two.

### 2.5 A cube-uniformity formulation

Expanding the square of the mean of f_k introduces one more independent cube direction. Hence

\[
\mathbb E(\mathbb E f_k)^2
=\mathbb E_{x,z_1,\ldots,z_{k+1}}
\prod_{\omega\in\{0,1\}^{k+1}}
 f(x+\omega_1z_1+\cdots+\omega_{k+1}z_{k+1}).
\tag{2.10}
\]

Equivalently, this is the (2^{k+1})st power of the usual Gowers U^{k+1} norm, including U^1=|E f|. Thus (2.2) also bounds the discounted sum of these cube-uniformity defects by 2I. Equation (2.10) is an exact expansion, not an independence approximation within a derivative.

## 3. Minimum affine influence and its rank representation

For any direction v in V, define

\[
\alpha_f(v)=\Pr[f(x)\ne f(x+v)],\quad
c_f(v)=1-2\alpha_f(v),\quad
j_f(v)=\tfrac12(1-|c_f(v)|).
\]

Let

\[
\boxed{\mathfrak I(f)=\min_{(v_1,\ldots,v_n)\text{ basis of }V}
\sum_i j_f(v_i).}
\tag{3.1}
\]

The minimum exists because the set of bases is finite. Choosing the standard basis proves Ifrak<=J<=I.

### 3.1 Why this is the exact extended-affine minimum

For an invertible linear map B whose columns are v_i, the coordinate influences of f(Bx) are alpha_f(v_i). A character multiplying f(Bx) can independently replace each of those influences by one minus itself. Indeed prescribe the character's values on the basis v_i, or equivalently prescribe its n coefficients in the new coordinates. Therefore

\[
\mathfrak I(f)=\min_{B\text{ invertible},\,a,b}
 I\bigl((-1)^{a\cdot x}f(Bx+b)\bigr).
\tag{3.2}
\]

The optional overall sign does not affect any quantity. Invertible input changes, translations, and output characters preserve H. Consequently a universal bound H<=C Ifrak would have exactly the same optimal universal constant as full FEI. This observation is only an equivalence; it proves no such bound for arbitrary f.

### 3.2 Integral of missing rank

Put

\[
L_t(f)=\operatorname{span}\{v:j_f(v)\le t\},\qquad0\le t\le1/2.
\]

The minimum-weight basis identity is

\[
\boxed{\mathfrak I(f)=\int_0^{1/2}
\bigl[n-\dim L_t(f)\bigr]\,dt.}
\tag{3.3}
\]

To prove it, any basis contains at most dim L_t vectors of weight at most t. Integrating its number of vectors with weight greater than t lower-bounds its cost by the right side. Conversely, greedily inspect all vectors by increasing weight, retaining each one that increases the span. At each threshold t the retained vectors span all vectors of weight at most t, so their count is exactly dim L_t. The greedy basis attains equality after integration. This is an elementary minimum-weight vector-matroid argument; the algorithmic principle is standard.

### 3.3 Exact tensorization

**Theorem 3.1.** For Boolean functions on disjoint input spaces,

\[
\boxed{\mathfrak I(f_1\otimes\cdots\otimes f_s)
=\sum_{j=1}^s\mathfrak I(f_j).}
\tag{3.4}
\]

Here tensor product denotes pointwise multiplication on the disjoint blocks. The autocorrelations factor, so

\[
j_{f\otimes g}(v,w)
=\tfrac12\bigl(1-|c_f(v)||c_g(w)|\bigr)
\ge\max\{j_f(v),j_g(w)\}.
\]

Every cheap vector of the product therefore lies in L_t(f) direct-sum L_t(g). The reverse span inclusion holds because the embedded vectors (v,0) and (0,w) keep their original costs. Thus

\[
L_t(f\otimes g)=L_t(f)\oplus L_t(g)
\]

at every t. Apply (3.3) and iterate. This exact rank equality, rather than just a bound on individual coordinate marginals, is what avoids losing a factor under later linear mixing.

### 3.4 Surjective affine lifts

If A:F_2^N->F_2^n is surjective, then

\[
H(f(Ax+b))=H(f),\qquad
\mathfrak I(f(Ax+b))=\mathfrak I(f).
\tag{3.5}
\]

The first identity follows because A^T injects the Fourier labels, changing their coefficients only by signs. For the second, alpha_{f\circ A}(v)=alpha_f(Av), and the cheap-vector span is precisely A^{-1}L_t(f). Its dimension is N-n+dim L_t(f), so (3.3) proves the identity. Output characters preserve both quantities.

Surjectivity is essential here. It is not permissible to identify dependent parameter forms and use (3.5) as though their joint law were still uniform on the full parameter cube.

## 4. An exact formula for every monotone Boolean function

Suppose f is increasing in its original coordinates. Write

\[
a_i=I_i(f),\qquad a_*=\max_i a_i,\qquad
q=1-\alpha_f(\mathbf1),
\]

where 1 is the vector flipping every input coordinate. For a constant or zero-dimensional function the conclusion is interpreted as Ifrak=0.

**Theorem 4.1.**

\[
\boxed{\mathfrak I(f)=I(f)-a_*+\min\{a_*,q\}.}
\tag{4.1}
\]

In particular, if f is also self-dual, f(x+1)=-f(x), then

\[
\boxed{\mathfrak I(f)=I(f)-\max_i I_i(f).}
\tag{4.2}
\]

The formula does not assert FEI for all monotone functions.

### 4.1 Directional influence increases under support inclusion

For monotone f,

\[
\operatorname{supp}(v)\subseteq\operatorname{supp}(w)
\quad\Longrightarrow\quad\alpha_f(v)\le\alpha_f(w).
\tag{4.3}
\]

It suffices to add one coordinate i not in v. Use sign-valued coordinates and write f(x_i,y)=a(y)+x_i b(y), with b(y)>=0 by monotonicity. Flipping the v coordinates in y gives

\[
c_f(v)=\mathbb E[a(y)a(y+v)+b(y)b(y+v)],
\]
\[
c_f(v+e_i)=\mathbb E[a(y)a(y+v)-b(y)b(y+v)].
\]

The difference is nonnegative, proving (4.3). In particular alpha_f(v)>=max_{i in supp(v)}a_i.

### 4.2 A direction omitting a coordinate cannot be almost antipodal too cheaply

If i is not in supp(v), then

\[
\boxed{\alpha_f(v)\le1-a_i.}
\tag{4.4}
\]

For a fixed y, the ordered pair (f(-1,y),f(+1,y)) is one of (--),(-+),(++). Let b_i(y) indicate the middle, pivotal case. For any two such ordered pairs, direct inspection of the nine possibilities gives

\[
\tfrac12\bigl[f(-1,y)f(-1,y')+f(+1,y)f(+1,y')\bigr]
\ge b_i(y)+b_i(y')-1.
\]

Take y'=y+v and average. This gives c_f(v)>=2a_i-1, equivalently (4.4). Taking v=e_j shows a_i+a_j<=1 for i!=j. Thus at most one coordinate influence exceeds 1/2.

### 4.3 The cheap-direction ranks

Fix 0<=t<1/2. Let the light coordinates be those with a_i<=t and the heavy ones their complement. Any vector with alpha_f(v)<=t is supported on the light coordinates by (4.3); all light unit vectors are indeed cheap.

A vector with alpha_f(v)>=1-t must contain every heavy coordinate, by (4.4). Thus, modulo the light-coordinate span, every such vector has the same image: the vector equal to one on all heavy coordinates. Such a vector exists exactly when alpha_f(1)>=1-t, by (4.3), that is, when q<=t. Consequently

\[
\dim L_t(f)=
\begin{cases}
\#\{i:a_i\le t\}+\mathbf1_{\{q\le t\}},&\text{if a heavy coordinate exists},\\
n,&\text{otherwise}.
\end{cases}
\tag{4.5}
\]

Integrating (4.5) yields

\[
\mathfrak I(f)=\sum_i\min(a_i,1/2)
-\bigl[\min(a_*,1/2)-q\bigr]_+.
\tag{4.6}
\]

If a_*<=1/2, this is (4.1). If a_*>1/2, it is the only such coordinate and q<=1-a_*<1/2, because alpha_f(1)>=a_*. Formula (4.6) is then I-a_*+q, again (4.1).

An optimal basis is also explicit. If q>=a_*, use the original coordinate basis. Otherwise replace a heaviest-influence unit vector by the all-ones vector, retaining the other unit vectors, and choose the output character to make the new directional cost q rather than 1-q. In the latter case all retained coordinate influences are at most 1/2. This construction attains (4.1).

### 4.4 Why the earlier basis obstruction is not contradicted

The previous signed-balance report shows that estimating entropy by the sum of marginal binary entropies after one fixed linear change loses a logarithm on a rare one-point defect. No such estimate is used here. Formula (4.1) determines the minimum *influence*, while entropy is computed separately on the seed functions. It does not control H by marginal entropy or establish a universal H/I bound.

## 5. A sharp constant-four FEI theorem stable under arbitrary surjective linear mixing

Consider the following seed types on their own parameter blocks:

- A one-point defect w_r(y)=1-2*1_{y=b}, with arbitrary r>=1 and b.
- An increasing read-once ternary-majority formula, with arbitrary tree shape and distinct variables at its leaves. A single variable is allowed.
- A quadratic phase (-1)^{Q(y)}, where Q is any polynomial over F_2 of degree at most two.

Translations, output signs, input sign reversals, and characters can be included by the affine invariances already proved.

Take any finite collection h_1,...,h_s of these seeds on disjoint parameter blocks, with total parameter dimension r, and let G=product_j h_j. Let A:F_2^N->F_2^r be **any surjective linear map**, b any translation, and chi any character. Define

\[
F(x)=\pm\chi(x)\prod_{j=1}^s h_j((Ax+b)^{(j)}).
\tag{5.1}
\]

The same physical input coordinate can occur in many parameter forms. The requirement is joint full row rank of all those forms, not disjointness of physical inputs.

**Theorem 5.1.** Every function (5.1) satisfies

\[
\boxed{H(F)\le4\mathfrak I(F)\le4J(F)\le4I(F).}
\tag{5.2}
\]

The constant four is optimal over this class. Moreover its *entire actual derivative chain* obeys

\[
\boxed{\mathcal T(F)\le8\mathfrak I(F)\le8J(F).}
\tag{5.3}
\]

The proof of (5.3) does not assume that derivatives remain in the seed class.

### 5.1 One-point seeds

For r>=2 put a=2^{1-r}. Every nonzero input direction changes w_r at exactly two points, so j_{w_r}(v)=a for v!=0. Therefore Ifrak(w_r)=r a. Its constant Fourier coefficient is 1-a and every nonempty coefficient has magnitude a. Hence

\[
H(w_r)=-2(1-a)^2\log_2(1-a)+(4a-2a^2)(r-1).
\tag{5.4}
\]

The elementary inequality -ln(1-a)<=a/(1-a) gives

\[
4ra-H(w_r)
\ge a\left[4-\frac{2(1-a)}{\ln2}\right]+2a^2(r-1)>0,
\]

using ln2>1/2. Thus H(w_r)<=4 Ifrak(w_r). For r=1 the function is a character, and both H and Ifrak vanish. Expanding (5.4) as r tends to infinity gives

\[
\frac{H(w_r)}{\mathfrak I(w_r)}\longrightarrow4.
\tag{5.5}
\]

This familiar monomial/one-point entropy computation is not claimed as a new seed theorem. It also proves sharpness of the constant in the larger class.

### 5.2 Unequal read-once ternary-majority formulas

Every such formula h is balanced, monotone, and self-dual. Its entropy and influence satisfy

\[
H(h)=4(I(h)-1).
\tag{5.6}
\]

Indeed a leaf has H=0,I=1. For a ternary-majority gate with balanced disjoint inputs g_1,g_2,g_3, its three singleton and one triple Fourier coefficients have squared weights 1/4. The standard Fourier composition expansion yields

\[
H(h)=2+\tfrac12\sum_j H(g_j),\qquad
I(h)=\tfrac12\sum_j I(g_j).
\]

These imply (5.6) by induction even when the three tree depths differ. By (4.2), Ifrak(h)=I(h)-a_* with a_*<=1. Thus H(h)=4(I-1)<=4 Ifrak(h).

Again, FEI for bounded-arity read-once formulas and the standard entropy composition mechanism predate this report. The role here is their exact compatibility with the affine minimum, which controls the new physical-coordinate influence after linear mixing.

### 5.3 Quadratic phases

Let B(v,w)=Q(v+w)+Q(v)+Q(w)+Q(0) be the alternating polar form, of rank rho. The derivative of (-1)^Q in direction v is a character. Its absolute autocorrelation is one for v in ker B and zero otherwise. Therefore j(v)=0 on ker B and 1/2 off it. Formula (3.3), or a basis extending ker B, gives

\[
\mathfrak I((-1)^Q)=\rho/2.
\]

The autocorrelation is a character on ker B and zero outside it. Fourier inversion shows that the squared spectrum is uniform on one affine coset of (ker B)^perp, of size 2^rho. Consequently

\[
H((-1)^Q)=\rho=2\mathfrak I((-1)^Q).
\tag{5.7}
\]

These elementary quadratic facts are established background, not a newly resolved quadratic FEI problem.

### 5.4 Combining the seeds

Disjoint products have product Fourier laws, so their entropies add. Theorem 3.1 proves that their minimum affine influences add exactly. Equation (3.5) and character invariance then give

\[
H(F)=\sum_jH(h_j)\le4\sum_j\mathfrak I(h_j)=4\mathfrak I(F).
\]

This proves (5.2). The lower half of the previously proved (1.3) says T(F)<=2H(F) for every F, and immediately gives (5.3). There is no circular appeal to unrestricted FEI and no need to differentiate within the class.

More generally, any collection of seeds satisfying H(h)<=C Ifrak(h) is closed under the same product-and-surjective-affine construction with the *same* constant C. The three seed types above provide one explicit sharp example of that principle.

### 5.5 Scope of the linear mixing

For example, one can replace the five independent parameters of w_2(y_1,y_2) Maj_3(y_3,y_4,y_5) by y_1=x_1 and y_j=x_1+x_j for j>=2. Then x_1 appears across all factors, but the parameter map is invertible, so (5.2) holds in the physical x coordinates. Arbitrary additional independent or redundant physical coordinates are allowed through a surjective map.

This does **not** permit arbitrary identifications among all parameter forms. In particular, a product of clauses on overlapping, linearly dependent parameter blocks is not automatically in (5.1). The previous coded perturbation uses dependencies of just this kind. Nor does the class include an arbitrary unbounded-arity outer majority or every NAND formula. Dropping these distinctions would silently replace the stated theorem by a much stronger unproved claim.

## 6. An affine-invariant version of the universal variance bound

Set

\[
\mathcal V_*(f)=1-\max_s p_f(s)
+\sum_{k\ge1}2^{-k}\mathbb E\operatorname{Var}(f_k).
\tag{6.1}
\]

Multiplying f by a character changes its first derivative only by a constant sign. All later variances are therefore unchanged, and minimizing the initial variance over characters gives exactly 1-max p. Invertible affine input changes preserve every variance in distribution; surjective lifts do so as well because projected uniform shifts remain independent and uniform. Thus V_* is invariant under the same transformations as H and Ifrak.

Apply Theorem 2.1 to an affine representative attaining (3.2), noting that its initial character need not simultaneously minimize the variance. This gives

\[
\boxed{\mathcal V_*(f)\le2\mathfrak I(f)\le2J(f).}
\tag{6.2}
\]

The constant two remains sharp, since on the one-point examples of sufficiently large dimension the constant Fourier coefficient is the largest one and V_*=V.

One must not replace V_* by V on the left of (6.2): a nonconstant character has V=1 but J=0. This is why the corrected initial term is necessary.

### 6.1 A rigorous limitation of variance as an entropy resource

The new variance budget alone cannot control all of H or all of T. For n=2s, take the nondegenerate quadratic phase

\[
f(x)=(-1)^{\sum_{i=1}^s x_{2i-1}x_{2i}}.
\]

Its squared Fourier law is uniform on all 2^n frequencies, so H=n and Ifrak=n/2. Every nonzero-shift derivative is a nonconstant character and the next derivative is constant. Therefore

\[
\boxed{\mathcal V_*(f)=\tfrac32(1-2^{-n}),\qquad H(f)=n.}
\tag{6.3}
\]

For the uniform spectral law, allocation entropy is E|S triangle T|=n/2, while every descendant character has zero allocation entropy. Hence T(f)=n/2 as well. Both H/V_* and T/V_* diverge. This is a limitation of using variance alone, not a counterexample to FEI.

The theorem in Section 5 handles these functions through their rank, not through a false entropy<=constant*variance assertion.

## 7. The shared-shift obstacle in a direct allocation transition argument

A tempting calculation would replace a derivative's spectral law by its averaged law and then draw two independent samples. This is not the actual descendant pair law. The exact correction can be written without discarding signs.

Let a_s=fhat(s), and for u,k in V define

\[
c_u(k)=\sum_s a_s a_{s+u}a_{s+k}a_{s+k+u}.
\]

The derivative spectral probabilities satisfy

\[
p_z(u)=\widehat{f f^z}(u)^2=\sum_k c_u(k)(-1)^{k\cdot z},
\qquad q(u)=\mathbb E_z p_z(u)=c_u(0)=(p_f*p_f)(u).
\tag{7.1}
\]

Here the equality follows by expanding the square and setting the difference between its two summation labels equal to k. For two spectral samples from the *same* random derivative, their joint averaged law is

\[
\boxed{\mathbb E_z[p_z(u)p_z(v)]
=q(u)q(v)+\sum_{k\ne0}c_u(k)c_v(k).}
\tag{7.2}
\]

Thus the correction is a positive-semidefinite covariance matrix, not generally zero. Also c_u(k)=c_k(u), and its nonzero-frequency columns sum to zero because sum_u p_z(u)=1. These exact identities are not a proof of a bound on the conditional allocation entropy under the shared-shift law.

For an explicit extreme illustration, a nondegenerate quadratic phase has uniform p_f. Every derivative is a character, so two descendant samples always agree. The actual joint averaged law is diagonal, while q times q is uniform on all ordered pairs. Treating those laws as equal would turn zero descendant allocation entropy into a positive quantity. This shows why an independence substitution cannot finish the current global argument.

A general concavity shortcut also fails. For an arbitrary probability law p=(a,b,c,d) on two spectral bits, elementary counting gives

\[
\mathfrak A(p)=1-\sum_i p_i^2+2(ad+bc)h_2\left(\frac{ad}{ad+bc}\right).
\]

Take p=(16/25,0,0,9/25), q=(14/25,7/50,7/50,4/25), and theta=4/5. The rational-log checker certifies

\[
\mathfrak A(\theta p+(1-\theta)q)
-\theta\mathfrak A(p)-(1-\theta)\mathfrak A(q)<-0.00116.
\]

These are arbitrary laws, **not** asserted to be squared spectra of Boolean functions. This only rules out a proof step invoking concavity on the entire probability simplex; it does not rule out an inequality that uses the additional exact Boolean constraints.

A preliminary numerical probe also considered minimum-affine-influence drift, 2 Ifrak(f)-E Ifrak(f_Z). It is nonnegative because a fixed optimal basis gives E j_{f_Z}(v)<=2 j_f(v)(1-j_f(v)), and Ifrak allows re-optimization. No universal inequality relating D_cross to this drift was proved. Its empirical behavior is not promoted to a new lemma or a near-completion claim. The final analytical conclusions of this report do not depend on that probe.

## 8. Executed checks

Run

```sh
python verify_affine_variance.py --part all --output verification.json
```

The standard-library dependency `prior_exact_entropy.py` is the **unchanged** checker from the preceding balanced-substitution continuation, reused for its exact Walsh transforms and rational linear forms in prime logarithms. Its original Git blob is `e867ba6b12e1a3e7588fd812eba6841319cd97b9`, and its SHA256 is `9600d6b961d26f9131277b830894c0e9497fefdaee2a9291507885cdf40326ab`. It is not a newly written independent implementation.

The actual current checks include:

- The 278 Boolean truth tables through dimension three, plus fixed-seed examples in dimensions four and five: 255 distinct canonical initial functions and 4,803 memoized derivative-chain states for the variance tests. All satisfy V<=2I and V_*<=2 Ifrak.
- One hundred rational arguments for the supersolution inequality; exact comparison of the one-point variance formula with full chains through dimension five; formula-based sharpness values through dimension 128.
- All 197 increasing functions in dimensions one through four, and 400 fixed-seed monotone examples in dimensions five through eight. The exact affine-minimum formula, the entire threshold-rank formula, and 5,643 instances each of the inclusion and omitted-coordinate inequalities pass. Greedy minima were also matched against 581 independently enumerated basis instances in dimensions at most three.
- 316 disjoint-product pairs, including 448 threshold-rank comparisons, for exact tensorization.
- Fifty surjective affine mixed examples from the explicit seed class, with exact entropy and minimum-influence preservation. Thirty-two of them also have their full allocation chains checked against T<=8 Ifrak.
- The exact shared-shift pair-law identity on all 278 truth tables through dimension three: 16,658 pair comparisons, with a nonzero covariance correction for 248 of those tables. An exact rational-law example separately refutes unrestricted concavity of allocation entropy.
- All eight quadratic homogeneous phases on three variables and four nondegenerate quadratic examples in dimensions 2,4,6,8; the latter verify the limitation (6.3). One-point entropy ratios through dimension 128 are enclosed using rational logarithm intervals and approach four.

Every accepted comparison in the final checker is integer/rational or uses outward rational logarithm enclosures. Numerical exploration scripts, when retained, are clearly separate and are not the justification for any universal theorem. The universal proofs above do not extrapolate from the tested finite dimensions.

## 9. Sources, reading coverage, and research delta

The latest FEI index was retrieved from current master at blob `8d45ee758aca61c7866e4e40432b324c133d28ad`. Its full-resolvent correction was retained. The mounted balanced-substitution report and checker were read; the checker hash was matched to its recorded remote blob. The universally quantified erasure reduction was also read directly from `solo-2026-09-17/ERASURE_REDUCTION.md`, blob `770f1fc8438b360549ed89480cb260768d839923`.

The earlier fixed-basis obstruction was read in full at `solo-2026-09-17/SIGNED_BALANCE_AND_LINEAR_BASIS_BARRIER_2026-09-18.md`, blob `6d886a56ad52de684f635cc124fb56110f67b8b2`. Section 4.4 explains why the present theorem does not contradict it. This session did not reread every page of the 1,506-page archive or every scheduled-worker report.

Primary-source comparisons checked during this continuation:

1. Ryan O'Donnell and Li-Yang Tan, *A composition theorem for the Fourier Entropy-Influence conjecture*, arXiv:1304.1347, 2013. Standard Fourier entropy/influence composition and bounded-arity read-once FEI predate this report.
2. Sugata Gangopadhyay and Pantelimon Stănică, *The Fourier Entropy-Influence conjecture holds for a log-density 1 class of cryptographic Boolean functions*, IACR ePrint 2014/054. Its abstract explicitly discusses monomial algebraic normal forms, direct sums, concatenations, and affine quadratic classes. The full text was not re-audited here, and no claim of priority over those constructions is made.
3. Nathan Keller and Noam Lifshitz, *Approximation of biased Boolean functions of small total influence by DNFs*, arXiv:1703.10116; Bulletin of the London Mathematical Society 50 (2018), 667–679, DOI 10.1112/blms.12167. This is a primary-source reference for the familiar edge-isoperimetric normalization; a complete elementary proof was included in Section 2.3.
4. María José González, Paul MacManus and María Cristina Pereyra, *Further evidence towards the Fourier Entropy-Influence conjecture*, arXiv:2606.00246, 2026. The earlier coordinate-restriction route remains distinct from the derivative-chain work here.

Searches for minimum influence under affine transformations, monotone directional influence, and affine FEI constructions did not establish a priority clearance. The new research delta is the collection of explicitly proved variance and affine-minimum statements and their use in the robust constant-four class, not a claim that their ingredients or all special cases were previously unknown.

## 10. Remaining full-scope gap and delivery status

The universal target remains to bound the accumulated allocation entropy T/J, or to establish another complete all-dimensional FEI proof. Section 2 controls an actual global variance cost. Section 5 controls the full allocation chain on a precise infinite class by a separate entropy proof. Neither provides a bound for arbitrary signed Fourier interactions.

In particular:

- Do not replace allocation entropy by variance; (6.3) disproves that simplification.
- Do not drop joint surjectivity in (5.1); dependent parameter forms can merge Fourier amplitudes coherently.
- Do not reuse either disproved pointwise resolvent inequality.
- Do not count a smaller auxiliary constant or a renamed equivalent target as a universal FEI solution.

At the time of preparing this package, the current GitHub connector exposed 48 read actions and no file-creation or commit action, including after complete discovery. A normal terminal Git request failed with `Could not resolve host: github.com`. The installed-plugin search found the same GitHub connector/CLI integration but did not expose another authorized write route. Therefore this session has **not** delivered these files to the repository. The accompanying patch adds a fresh continuation directory and a dated handoff, and inserts a short link section into the FEI index while preserving its existing text. It has not been remotely applied. This describes this session's delivery limitation, not a claim that scheduled workers or the account have lost write permission.
