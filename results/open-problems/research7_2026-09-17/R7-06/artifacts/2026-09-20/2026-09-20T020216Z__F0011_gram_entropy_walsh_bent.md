Model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — this is **not GPT-6 at maximum**; no authenticated binding model/effort selector or runtime telemetry is exposed.

# F0011 — exact Gram-type entropy bounds and a Walsh/bent-function reduction of the max-volume fixed-spectrum core

Date: 2026-09-20 UTC  
Role: C05 / R7-06 Random Matrix Spectral Entropy  
Native ID: `6aabe827777c8191a43330b4a87d481d`  
Canonical source: Van H. Vu, *Recent progress in combinatorial random matrix theory*, Probability Surveys 18 (2021), Conjecture 9.4, arXiv:2005.02797, DOI 10.1214/20-PS346.  
Source target: for the symmetric Rademacher matrix `M_n^sym`,
\[
\Pr(\operatorname{Spec}(M_n^{\rm sym})\subset\mathbb Z)
=2^{-(1/2+o(1))n^2}.
\]
Status below: **PROVED PARTIAL**, pending later independent review. None of the results below proves the full source conjecture.

## 1. Inherited bridge and what is attacked here

The preceding R7-06 work reduced the difficult two-eigenvalue boundary
\[
H=H^T\in\{\pm1\}^{N\times N},\qquad H^2=NI
\]
to balanced half-completions
\[
H=\begin{pmatrix}P&C\\ C^T&D\end{pmatrix},\qquad N=2r.
\]
It proved that one may choose a balanced cut with `corank(C)<=sqrt(N)` and that singular cross-block completions reduce to positive-definite sign-Gram fibers at only `2^{O(N^{3/2})}=2^{o(N^2)}` additional conditioned entropy. Thus the singular/corank endpoint is not discarded in this note.

For an invertible cross block,
\[
K:=CC^T=2rI-P^2>0,
\qquad
D=-C^{-1}PC.
\tag{1.1}
\]
The previous run also proved
\[
\log\frac{r^r}{\det K}
\ge \frac{\|P^2-rI\|_F^2}{4r^2},
\tag{1.2}
\]
so the maximum-volume point `K=rI` recursively forces `P^2=rI`.

This note attacks two remaining bridges:

1. obtain an all-dimensions entropy theorem for **every** positive sign-Gram fiber, using only exact orbit/type information rather than a small-`r` census;
2. analyze the exact max-volume point `K=rI` in a canonical hard class of cross Hadamards, namely the Sylvester/Walsh equivalence class, and turn the completion problem into a constrained bent-function count.

## 2. Exact two-row entropy inside a positive sign-Gram fiber

For a positive definite integer Gram matrix `K` with diagonal `r`, define
\[
\mathcal R(K)
:=\{C\in\{\pm1\}^{r\times r}:CC^T=K\}.
\]
Let `C` be uniform on `mathcal R(K)`, and write its rows as `R_1,...,R_r`.

The fiber is invariant under right multiplication by an arbitrary signed permutation matrix. This elementary symmetry already fixes every two-row marginal exactly.

### Lemma 2.1 (exact pair marginal)

For `i<j`, put
\[
w_{ij}:=\frac{r+K_{ij}}2.
\]
Then
\[
\boxed{
H_2(R_i,R_j)
=r+\log_2\binom r{w_{ij}}.
}
\tag{2.1}
\]

### Proof

Let
\[
Z:=R_i\circ R_j\in\{\pm1\}^r.
\]
Since `sum_l Z_l=K_{ij}`, exactly `w_{ij}` coordinates of `Z` are `+1`.

Column permutations act transitively on all sign vectors with this prescribed number of `+1` coordinates and preserve the uniform measure on the fiber, so `Z` is uniform on that Hamming type. Hence
\[
H_2(Z)=\log_2\binom r{w_{ij}}.
\]

Conditioned on `Z`, independent column sign flips preserve `Z` and act freely and transitively on the possible first row `R_i`. Therefore `R_i` is conditionally uniform on `\{\pm1\}^r`, and `R_j=R_i\circ Z`. Thus
\[
H_2(R_i,R_j)=H_2(Z)+H_2(R_i\mid Z)
=\log_2\binom r{w_{ij}}+r.
\]
QED.

### Theorem 2.2 (correlation-energy entropy deficit)

Every nonempty positive fiber satisfies
\[
\boxed{
\log_2|\mathcal R(K)|
\le
r^2-
\frac{\|K-rI\|_F^2}{4r(r-1)\ln2}.
}
\tag{2.2}
\]

In particular, for an inherited half-completion `K=2rI-P^2`,
\[
\boxed{
\log_2|\mathcal R(2rI-P^2)|
\le
r^2-
\frac{\|P^2-rI\|_F^2}{4r(r-1)\ln2}.
}
\tag{2.3}
\]

### Proof

Shearer's inequality applied to the family of all row pairs gives
\[
H_2(R_1,\ldots,R_r)
\le
\frac1{r-1}\sum_{i<j}H_2(R_i,R_j).
\tag{2.4}
\]
For `rho=K_{ij}/r`, the standard binary-entropy bound
\[
h_2\!\left(\frac{1+\rho}{2}\right)
\le1-\frac{\rho^2}{2\ln2}
\tag{2.5}
\]
implies
\[
\log_2\binom r{(r+K_{ij})/2}
\le
r-\frac{K_{ij}^2}{2r\ln2}.
\tag{2.6}
\]
Using Lemma 2.1 in (2.4),
\[
\log_2|\mathcal R(K)|
\le
r^2-
\frac1{2r(r-1)\ln2}\sum_{i<j}K_{ij}^2.
\]
Since `diag(K)=r`,
\[
\|K-rI\|_F^2=2\sum_{i<j}K_{ij}^2,
\]
which proves (2.2). Equation (2.3) follows from
\[
K-rI=rI-P^2=-(P^2-rI).
\]
QED.

This is a direct seed/fiber coupling: a strongly non-Hadamard seed with
\[
\|P^2-rI\|_F^2\ge\varepsilon r^4
\]
forces a `Theta(r^2)` loss in the cross-Gram fiber entropy. The near-Hadamard regime remains the difficult one.

## 3. A uniform four-row theorem: every positive Gram fiber loses at least `(5/8) r log r` bits

The pair estimate can be weak near `K=rI`. A higher marginal gives a uniform saving even there.

Fix four distinct row indices `i,j,k,l`. Relative to row `i`, define
\[
Z_2=R_i\circ R_j,\quad
Z_3=R_i\circ R_k,\quad
Z_4=R_i\circ R_l.
\]
For `a,b,c in {+-1}`, let `n_{abc}` be the number of coordinates with
\[
(Z_2,Z_3,Z_4)=(a,b,c).
\]
The Gram entries determine every Fourier coefficient of this eight-cell histogram of degree at most two:
\[
\sum 1=r,
\]
\[
\sum Z_2=K_{ij},\quad \sum Z_3=K_{ik},\quad \sum Z_4=K_{il},
\]
\[
\sum Z_2Z_3=K_{jk},\quad
\sum Z_2Z_4=K_{jl},\quad
\sum Z_3Z_4=K_{kl}.
\]
Only the cubic coefficient
\[
T_{ijkl}:=\sum_{s=1}^r R_{i,s}R_{j,s}R_{k,s}R_{l,s}
\tag{3.1}
\]
remains undetermined. Given `T=T_{ijkl}`, Fourier inversion gives the histogram exactly:
\[
\boxed{
 n_{abc}(T)=\frac18\Big(
 r+aK_{ij}+bK_{ik}+cK_{il}
 +abK_{jk}+acK_{jl}+bcK_{kl}+abcT
 \Big).
}
\tag{3.2}
\]

### Lemma 3.1 (four-row entropy bound)

Uniformly over every nonempty positive Gram fiber and every four distinct rows,
\[
\boxed{
H_2(R_i,R_j,R_k,R_l)
\le
4r-\frac52\log_2 r+O(1).
}
\tag{3.3}
\]

### Proof

The statistic `T` is invariant under signed column flips and column permutations, and it has at most `r+1` possible values. Conditioned on `T`, equation (3.2) fixes the eight pattern counts.

Column permutations act transitively on all pattern sequences with those counts, while independent column sign flips make the reference row `R_i` conditionally uniform on `\{\pm1\}^r`. Therefore
\[
H_2(R_i,R_j,R_k,R_l\mid T)
=
 r+\log_2\frac{r!}{\prod_{a,b,c} n_{abc}(T)!}.
\tag{3.4}
\]
The largest eight-cell multinomial coefficient satisfies, by Stirling uniformly in `r`,
\[
\max_{n_1+\cdots+n_8=r}
\frac{r!}{n_1!\cdots n_8!}
\le C\,8^r r^{-7/2}
\tag{3.5}
\]
for an absolute constant `C`. Hence
\[
H_2(R_i,R_j,R_k,R_l)
\le
\log_2(r+1)+r+3r-\frac72\log_2r+O(1),
\]
which is (3.3). QED.

### Theorem 3.2 (uniform positive-fiber entropy bound)

For every positive definite sign Gram matrix `K`,
\[
\boxed{
\log_2|\mathcal R(K)|
\le
r^2-\frac58 r\log_2r+O(r).
}
\tag{3.6}
\]
Consequently, if `mathcal B(K)` denotes the `r`-element sign-class support representations used in the preceding R7-06 work, so that
\[
|\mathcal R(K)|=2^r r!\,|\mathcal B(K)|,
\]
then
\[
\boxed{
\log_2|\mathcal B(K)|
\le
r^2-\frac{13}{8}r\log_2r+O(r).
}
\tag{3.7}
\]

### Proof

Apply Shearer's inequality to all four-row subsets. Each row occurs in `binom(r-1,3)` such subsets, while
\[
\frac{\binom r4}{\binom{r-1}3}=\frac r4.
\]
Lemma 3.1 gives
\[
\begin{aligned}
\log_2|\mathcal R(K)|
&\le
\frac1{\binom{r-1}3}
\sum_{|S|=4}H_2((R_i)_{i\in S})\\
&\le
\frac r4\left(4r-\frac52\log_2r+O(1)\right)\\
&=r^2-\frac58r\log_2r+O(r).
\end{aligned}
\]
Subtracting `r+log_2(r!)=r log_2 r+O(r)` gives (3.7). QED.

This is not yet the desired `2^{o(r^2)}` fiber theorem, but it is an arbitrary-size, all-positive-fibers entropy loss independent of determinant or spectral nondegeneracy.

## 4. The exact maximum-volume point and a Walsh/bent-function bridge

At `K=rI`, the inherited determinant theorem forces
\[
P^2=rI,
\qquad
CC^T=rI.
\tag{4.1}
\]
Thus both principal seed and cross block are Hadamard matrices. We now solve a canonical equivalence class of the cross block much more sharply.

Let
\[
r=2^m,\qquad G=\mathbb F_2^m,
\]
and let `W` be the Sylvester/Walsh matrix
\[
W_{x,y}=(-1)^{x\cdot y},\qquad x,y\in G.
\]
Then
\[
W=W^T,\qquad W^2=rI.
\]
Fix the normalized cross block `C=W`. The off-diagonal block equation gives
\[
\boxed{
D=-\frac1r W P W.
}
\tag{4.2}
\]

Write
\[
P_{x,y}=(-1)^{f(x,y)}
\]
for a Boolean function `f:G x G -> F_2`.

### Theorem 4.1 (Walsh completion equals swap-symmetric bentness plus the seed Hadamard condition)

For `C=W`, the requirement that the forced matrix `D` in (4.2) be a sign matrix is equivalent to `f` being bent on `2m` variables. Moreover,
\[
P=P^T
\iff
f(x,y)=f(y,x)\quad\forall x,y.
\tag{4.3}
\]
Therefore every max-volume completion with Walsh cross block is represented by a **swap-symmetric bent function**, with the additional inherited condition `P^2=rI`.

### Proof

The `(u,v)` entry of `W P W` is
\[
\sum_{x,y\in G}(-1)^{f(x,y)+u\cdot x+v\cdot y},
\]
which is exactly the unnormalized Walsh transform of `f` at frequency `(u,v)`. A Boolean function on `2m` variables is bent precisely when every such transform has absolute value
\[
2^{(2m)/2}=2^m=r.
\]
Thus `(1/r)WPW` is entrywise `+-1` exactly when `f` is bent. Symmetry is visibly equivalent to (4.3). QED.

Note that this is an upper-reduction: swap-symmetric bentness by itself need not imply `P^2=rI`, but every actual max-volume completion lies in this class.

Also, because `C` is invertible,
\[
D=-C^{-1}PC
\]
implies `tr D=-tr P`; hence every such completion has `tr H=0`. Therefore its two eigenvalues have equal multiplicity `r`. On the integral-spectrum branch, if `N=2r=2^{m+1}`, one must additionally have `m` odd so that `sqrt(N)` is integral. The fixed spectrum is then
\[
\{+\sqrt N\}^{r}\cup\{-\sqrt N\}^{r}.
\]

## 5. Swap symmetry plus Rothaus degree gives a quadratic entropy saving

A classical theorem of Rothaus says that a bent Boolean function on `2m>2` variables has algebraic normal form degree at most `m`.

The monomials in variables `(x_1,...,x_m,y_1,...,y_m)` are indexed by ordered pairs `(A,B)` of subsets of `[m]`, with total degree `|A|+|B|`. Swap symmetry sends `(A,B)` to `(B,A)`. Hence a swap-symmetric Boolean function of degree at most `m` is specified by one coefficient per orbit of this involution among the low-degree monomials.

Let
\[
M_m:=\sum_{d=0}^{m}\binom{2m}{d}
=2^{2m-1}+\frac12\binom{2m}{m},
\tag{5.1}
\]
and let
\[
F_m:=\sum_{j=0}^{\lfloor m/2\rfloor}\binom mj,
\tag{5.2}
\]
the number of fixed monomials `A=B` with `2|A|<=m`. The number of swap-orbits is exactly
\[
\boxed{
O_m=\frac{M_m+F_m}{2}.
}
\tag{5.3}
\]
Since `r=2^m`, the central-binomial estimate gives
\[
\boxed{
O_m=\left(\frac14+O(m^{-1/2})\right)r^2.
}
\tag{5.4}
\]
For the integral branch `m` is odd, and in fact `F_m=2^{m-1}=r/2` exactly.

### Theorem 5.1 (fixed Walsh cross-block completion count)

For `r=2^m`, the number of symmetric sign matrices `P` that can occur in a max-volume two-eigenvalue completion with normalized cross block `C=W` is at most
\[
\boxed{
2^{O_m}
=2^{(1/4+O(m^{-1/2}))r^2}.
}
\tag{5.5}
\]
The same upper bound holds after restricting to any fixed trace/spectrum slice.

### Proof

By Theorem 4.1 every such `P` gives a swap-symmetric bent function `f`. Rothaus's degree theorem puts `f` in the vector space of degree-at-most-`m` Boolean functions. Swap symmetry makes its ANF coefficients constant on the involution orbits counted by (5.3). Hence there are at most `2^{O_m}` possibilities. The additional condition `P^2=rI`, or any fixed-trace condition, only decreases this number. QED.

### Corollary 5.2 (Sylvester-equivalence-class fixed-spectrum bound)

Suppose the max-volume cross block `C` is Hadamard-equivalent to `W`. There are at most
\[
(2^r r!)^2=2^{O(r\log r)}
\]
labelled cross blocks in this equivalence orbit. Block-diagonal signed-permutation conjugation normalizes each such `C` to `W` while preserving sign entries, symmetry and spectrum. Consequently the entire labelled max-volume branch with cross block in the Sylvester equivalence class has size
\[
\boxed{
2^{(1/4+o(1))r^2}
=2^{(1/16+o(1))N^2},
\qquad N=2r.
}
\tag{5.6}
\]
On the integral branch this applies along the odd-`m` powers `N=2^{m+1}` and concerns the fixed equal-multiplicity spectrum `+-sqrt(N)`.

This is still not `2^{o(N^2)}`, so it does not close even this restricted branch, but it is a leading-quadratic entropy improvement at a canonical exact maximum-volume point.

For comparison, Potapov's general upper bound for all `2m`-variable bent functions has logarithm below `(11/32+o(1))2^{2m}`. The elementary swap-symmetric degree-orbit argument above gives the smaller coefficient `1/4` because it uses the matrix symmetry specific to this F0011 reduction.

## 6. The obvious huge bent family collapses under matrix symmetry

The standard Maiorana-McFarland family consists of
\[
f(x,y)=x\cdot\pi(y)+g(y),
\tag{6.1}
\]
where `pi` is a permutation of `F_2^m` and `g` is arbitrary; every such `f` is bent.

The raw family is enormous, so it is a natural candidate for producing a high-entropy counterfamily to the Walsh reduction. Swap symmetry destroys that freedom almost completely.

### Theorem 6.1 (exact swap-symmetric Maiorana-McFarland classification)

A function of the form (6.1) satisfies
\[
f(x,y)=f(y,x)\quad\forall x,y
\]
if and only if there exist

- an invertible symmetric matrix `A in GL(m,2)`,
- a vector `c in F_2^m`, and
- a bit `c_0 in F_2`,

such that
\[
\boxed{
\pi(y)=Ay+c,
\qquad
g(y)=c\cdot y+c_0.
}
\tag{6.2}
\]
Consequently the number of swap-symmetric functions in the raw Maiorana-McFarland class is exactly
\[
\#\{A=A^T\in GL(m,2)\}\,2^{m+1}
\le
\boxed{2^{m(m+1)/2+m+1}}.
\tag{6.3}
\]
In `r=2^m` notation this is only
\[
2^{O((\log r)^2)}.
\]

### Proof

Let `c=pi(0)` and `c_0=g(0)`. Setting `x=0` in swap symmetry gives
\[
g(y)=y\cdot c+c_0.
\tag{6.4}
\]
Put
\[
\phi(y):=\pi(y)+c.
\]
Substitution of (6.4) into the symmetry identity cancels the affine terms and leaves
\[
\boxed{x\cdot\phi(y)=y\cdot\phi(x)\quad\forall x,y.}
\tag{6.5}
\]
Taking `x=e_i` shows
\[
\phi_i(y)=y\cdot\phi(e_i),
\]
so every coordinate of `phi` is linear. Hence `phi(y)=Ay` for some matrix `A`. Equation (6.5) is exactly `A=A^T`. Since translation by `c` preserves bijectivity, `pi` is a permutation exactly when `A` is invertible. This proves necessity, and direct substitution proves sufficiency. Counting all symmetric `A` gives (6.3). QED.

Every function in Theorem 6.1 is bent and its sign matrix `P` is a Hadamard matrix (it is a column-signed/permuted character table); swap symmetry makes `P=P^T`, hence `P^2=rI`. Therefore these parameters give genuine max-volume Walsh-cross-block completions. They form a very small explicit valid family, rather than a quadratic-entropy obstruction.

This statement concerns the **raw** Maiorana-McFarland representation (6.1), not its completed affine-equivalence closure.

## 7. What this does and does not prove

### New proved partial statements

1. Every positive sign-Gram fiber obeys the exact pair-energy bound (2.2), directly coupling the cross-fiber entropy loss to the inherited seed energy.
2. Every positive sign-Gram fiber, including the orthogonal/Hadamard point, obeys the uniform all-dimensions estimate
   \[
   \log_2|\mathcal R(K)|
   \le r^2-\frac58r\log_2r+O(r).
   \]
3. At the exact max-volume point with a Sylvester/Walsh cross block, the completion problem injects into swap-symmetric bent functions.
4. Rothaus's degree theorem plus swap symmetry gives
   \[
   2^{(1/4+o(1))r^2}
   \]
   completions for this normalized branch, and the same leading exponent after allowing the entire Sylvester Hadamard equivalence orbit.
5. The raw Maiorana-McFarland construction cannot generate a large counterfamily after imposing the required swap symmetry: it collapses to affine permutations with symmetric invertible linear part and has only `2^{O(m^2)}` members.

### What remains open

The full F0011 source asks for `2^{o(N^2)}` total integral-spectrum matrices. The present results do not establish that.

The two-eigenvalue bottleneck is now split more sharply:

- **singular balanced cuts:** already reduced to the positive-fiber problem with only `2^{O(N^{3/2})}` overhead;
- **positive non-near-Hadamard fibers:** (2.3) gives a quadratic entropy loss when the seed correlation energy is `Omega(r^4)`;
- **positive near-Hadamard fibers:** the uniform four-row theorem gives a subleading `Omega(r log r)` loss, but not a vanishing quadratic exponent;
- **exact maximum volume, Sylvester cross block:** reduced to swap-symmetric bent functions and bounded by `2^{(1/4+o(1))r^2}`;
- **exact maximum volume, arbitrary Hadamard cross block:** still lacks an analogue of the Walsh/bent degree restriction.

The previous proposed implication
\[
\log(r^r/\det K)\ge\eta r
\Longrightarrow
|\mathcal B(K)|=2^{o(r^2)}
\]
remains **unproved**. Determinant deficit alone need not force a comparably large Frobenius/correlation-energy deficit; a small number of very small eigenvalues can carry substantial log-determinant loss. The present pair-energy theorem therefore does not justify that implication by itself.

## 8. Next attack

The highest-value next step is not another small-order census. It is one of the following arbitrary-size bridges:

1. **arbitrary-Hadamard flat-transform theorem:** for a fixed Hadamard `C`, bound symmetric Hadamard sign matrices `P` for which `C^TPC/r` is again sign. The Walsh case above says that a character table turns this into swap-symmetric bentness; the goal is an invariant replacement for algebraic degree that works for every Hadamard equivalence class;
2. **high-multiplicity inverse theorem:** prove that a positive Gram fiber with `2^{Omega(r^2)}` roots must carry character-table/group-like structure, after which a bent-function-type argument can be applied;
3. **counterexample route:** construct an arbitrary-size positive Gram family with definite volume deficit and `2^{Omega(r^2)}` roots. Such a family would refute the proposed volume-deficit route and force a different global invariant.

The singular endpoint should continue to be attached through the inherited `corank<=sqrt(N)` reduction rather than reopened as a separate case.

## 9. Literature boundary checked for this run

The following external facts were used only at their stated scope.

- Vu's Conjecture 9.4 remains the exact outside target.
- Ferber-Jain-Zhao prove a constant quadratic-exponent improvement for the number of Hadamard matrices and explicitly note that even `2^{o(n^2)}` Hadamard counting would require important new ideas.
- Rothaus's classical degree bound says a bent function on `2m>2` variables has algebraic degree at most `m`.
- Vladimir Potapov, *Upper bounds on the numbers of binary plateaued and bent functions*, Cryptography and Communications 16 (2024), gives the general bent-count upper exponent `11/32`.
- Jan Kristian Haugland, *A lower bound on the number of bent squares*, arXiv:2508.14605 (2025), emphasizes the still-large gap in general bent enumeration and the matrix/bent-square viewpoint.
- The Maiorana-McFarland form used in Section 6 is classical; the symmetry-collapse theorem is a project deduction from that representation and is not asserted externally novel.

A bounded 20 September 2026 search did not surface a proof of Vu's full asymptotic or an existing theorem identical to the swap-symmetric completion count above. Search failure is **not** an openness or novelty certificate.
