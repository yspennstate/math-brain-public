SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B15, 2026-09-23T08:03:56Z.
attacking: zero-loss weak-limit closure of density height and a dense smooth/generic core; continuity kept separate; apply completed account02/B15 rough-source regularity to a concrete inequality.

# account01/B15 — zero-loss height closure and dense smooth/generic core

Programme: `QFORM-DENSITY-3EIG-20260922`  
Assignment: Absolute continuity and regularity  
Status: `ESSENTIAL_STEP_APPLIED / TARGET_LEVEL_HEIGHT_CLOSURE / FULL_TARGET_OPEN`  
Execution: `WITHOUT_VERIFIED_BRAIN`.

The full universal bound is still OPEN. This report proves a target-level closure theorem that removes rough source laws and algebraically nongeneric matrices from the HEIGHT problem at zero loss, while proving that continuity cannot be inferred from that closure alone. A completed account02/B15 quantitative regularity theorem is then applied to an actual live volume-branch inequality.

## 1. Three logically different regularity statements

Let `mu` be an absolutely continuous probability law on `R^n` and let `A` be real symmetric.

### 1.1 Absolute continuity: any nonzero A already suffices

Put `q(x)=x^T A x`. If `A!=0`, then `q#mu` is absolutely continuous. Product structure, rank three, and the cap-one assumption are not needed for this qualitative statement.

Proof. Let `N subset R` be Lebesgue-null. For

`E_k={x: |x|<=k, |grad q(x)|>=1/k}`,

coarea gives

`int_{E_k cap q^{-1}(N)} |grad q(x)| dx
 = int_N H^{n-1}(E_k cap q^{-1}(t)) dt =0`.

Hence `Leb(E_k cap q^{-1}(N))=0`. The complement of `union_k E_k`, up to a null set, lies in the critical set `ker A`, a proper linear subspace because `A!=0`. Therefore `Leb(q^{-1}(N))=0`, and absolute continuity of `mu` gives `mu(q^{-1}(N))=0`.

This proves existence of a density only; it gives no useful height bound.

### 1.2 Bounded density: encode it without assuming a density exists

For a finite Borel measure `nu` on `R`, define

`H(nu)=inf{C>=0: nu(E)<=C Leb(E) for every Borel E}`,

with `H(nu)=+infinity` if no finite `C` exists. Then

`H(nu)<infinity  <=>  nu=p dx for some p in L^infinity`,

and in that case `H(nu)=||p||_infinity` (essential supremum).

Moreover, if `I_Q` denotes the countable family of bounded open intervals with rational endpoints, then

`boxed{ H(nu)=sup_{I in I_Q} nu(I)/|I|. }`                         (1.1)

Indeed the inequality `<=` is immediate when `nu<=C dx`. Conversely, a bound on rational intervals passes to arbitrary open intervals by monotone approximation from inside, then to arbitrary open sets by disjoint interval decomposition, and finally to Borel sets by outer regularity.

### 1.3 Continuity is strictly stronger

A uniform height bound is closed under weak convergence, but continuity is not. For example, the smooth densities

`1_[0,1] * gamma_epsilon`

have height at most one and converge weakly to the Uniform[0,1] law, whose standard density representative is discontinuous at the endpoints. Thus any argument proving only the height by weak closure must not silently claim continuity.

The completed account02/B15 source `yspennstate/math-open-problems@9b8bb7e84811978a2c46c7bb5ec50f2570dbc056` reports the stronger fixed-matrix statement `rank(A)>=3 => p_Q in C_0(R)` with an instance-dependent bound. That is a separate regularity theorem; the universal-height conjecture is not a consequence because its constants can deteriorate with the matrix.

## 2. Main lemma: density height is weakly lower semicontinuous

### Theorem 2.1

If finite Borel measures `nu_m => nu` weakly, then

`boxed{ H(nu) <= liminf_m H(nu_m). }`                           (2.1)

Proof 1, directly from (1.1). For every open rational interval `I`, Portmanteau gives

`nu(I) <= liminf_m nu_m(I)`.

Therefore

`nu(I)/|I| <= liminf_m H(nu_m)`.

Take the supremum over the countable family `I_Q` and use (1.1).

Equivalently, along a subsequence realizing the liminf as `L<infinity`, every open interval satisfies `nu(I)<=L|I|`; hence every Borel set does, so `nu<=L dx`.

No Fourier envelope, moment bound, density continuity, or pointwise convergence of output densities is used.

## 3. Cap-preserving smooth compact approximation of every marginal

Let `f` be any probability density with `0<=f<=1`. There are `f_m in C_c^infinity(R)` with

`0<=f_m<=1`, `int f_m=1`, and `||f_m-f||_1 ->0`.                 (3.1)

Construction. Choose `R` so the tail mass

`eta_R=int_{|x|>R} f(x) dx`

is small. Choose a unit interval `J_R` disjoint from `[-R,R]` and set

`h_R=f 1_{[-R,R]} + eta_R 1_{J_R}`.

Then `0<=h_R<=1`, `int h_R=1`, and

`||h_R-f||_1 <=2 eta_R`.

Convolve with a nonnegative compactly supported mollifier `rho_epsilon` of mass one. Young gives

`||h_R*rho_epsilon||_infinity<=||h_R||_infinity<=1`;

it remains a probability density, is `C_c^infinity`, and converges to `h_R` in `L1` as `epsilon->0`. A diagonal choice gives (3.1).

For finitely many marginals, if

`F=prod_{i=1}^n f_i`, `F_m=prod_{i=1}^n f_{i,m}`,

then telescoping gives

`boxed{ ||F_m-F||_1 <= sum_i ||f_{i,m}-f_i||_1 ->0. }`           (3.2)

Thus the corresponding product probability laws converge even in total variation.

## 4. Generic rational matrices are a zero-loss dense core for HEIGHT

For fixed `n`, let `G_n` be the symmetric rational matrices satisfying:

1. `s_3(B)>1`, where `s_3` is the third largest singular value (equivalently third largest eigenvalue modulus for symmetric matrices);
2. the spectrum is simple;
3. every nonempty physical principal minor is nonzero.

### Lemma 4.1

For every target matrix `A` with `s_3(A)>=1`, there are `B_m in G_n` with `B_m->A` in operator norm.

Proof. First set `A^(m)=(1+1/m)A`, so `s_3(A^(m))>=1+1/m`. The bad matrices for conditions 2 and 3 form a finite union of proper real-algebraic hypersurfaces: the spectral discriminant and the principal-determinant polynomials. Their complement is open dense. Rational symmetric matrices are dense, so choose rational `B_m` outside all these hypersurfaces with

`||B_m-A^(m)||_op <1/(2m)`.

Weyl's singular-value inequality gives

`s_3(B_m)>=s_3(A^(m))-1/(2m)>1`,

and `B_m->A`.

This genericization is only a proof reduction. It does NOT produce a uniformly conditioned physical minor; the nonzero minors may tend to zero.

## 5. Simultaneous source-and-matrix convergence needs no moments

Let `F_m dx -> F dx` in total variation and `B_m->A` coefficientwise. Write

`q_m(x)=x^T B_m x`, `q(x)=x^T A x`,

and `nu_m=(q_m)#(F_m dx)`, `nu=q#(F dx)`.

For any bounded continuous test function `psi`,

`|int psi(q_m)F_m - int psi(q)F|
 <= ||psi||_infinity ||F_m-F||_1
    + int |psi(q_m(x))-psi(q(x))| F(x) dx`.

The second term tends to zero by dominated convergence because `q_m(x)->q(x)` pointwise. Hence

`boxed{ nu_m => nu weakly. }`                                    (5.1)

No moment assumption on the cap-one inputs is needed; in particular, small operator norm of `B_m-A` is never converted into an unjustified law-uniform estimate on `X^T(B_m-A)X`.

## 6. Exact dense-core equivalence for the full sharp HEIGHT constant

Define

`C_full = sup H((x^T A x)#(prod_i f_i dx))`,

where the supremum runs over every dimension, every independent cap-one product source, and every symmetric target matrix with `s_3(A)>=1`.

Define `C_core` by the same supremum but restricted to:

- `A in G_n` (rational, simple spectrum, all physical principal minors nonzero, `s_3(A)>1`), and
- every marginal `f_i in C_c^infinity(R)` with `0<=f_i<=1` and mass one.

Then, allowing the value `+infinity`,

`boxed{ C_full = C_core. }`                                      (6.1)

Proof. `C_core<=C_full` is immediate. Conversely fix arbitrary target data `(A,F)`. Choose the cap-preserving smooth product approximants of Section 3 and generic rational matrix approximants of Section 4. Section 5 gives weak convergence of the output laws. Theorem 2.1 therefore gives

`H(q_A#F) <= liminf_m H(q_{B_m}#F_m) <= C_core`.

Take the supremum over all target data.

This is a zero-loss reduction of the UNIVERSAL HEIGHT problem. It is stronger for this purpose than a common-Fourier-envelope approximation theorem: none is required. It also shows that exact zero physical pivots, repeated eigenvalues, singular principal minors, rough source discontinuities, and unbounded source support can all be removed from the proof of the universal height and restored afterward by closure. What remains hard is uniform control as those generic minors become arbitrarily small.

## 7. Actual application of the completed account02/B15 result

The latest completed assigned-partner result used here is account02/B15

`yspennstate/math-open-problems@beba6425b1130ce83dd870c447fc0e87bcc5bd58`,

which proves the following common-envelope stability inequality. If two product sources `F,G` for the same phase have

`Delta=||F-G||_1`

and both output characteristic functions satisfy

`|phi(t)|<=min(1,K|t|^{-b})`, `b>1`,

then

`boxed{
 ||p_F-p_G||_infinity
 <= [b/(pi(b-1))](2K)^(1/b) Delta^(1-1/b).
}`                                                               (7.1)

For the live `q=4/3` volume branch, `b=9/8` and `Z=e_3(M^T M)`, so the partner theorem gives the explicit actual inequality

`boxed{
 ||p_F-p_G||_infinity
 <= (9 sqrt(3)e/2) 2^(8/9) Z^(-1/6) Delta^(1/9)
 <39.233 Z^(-1/6) Delta^(1/9).
}`                                                               (7.2)

Apply (7.2) to the cap-preserving smooth approximants `F_m` of Section 3 for a FIXED matrix in this volume-certified branch. With `Delta_m=||F_m-F||_1`,

`boxed{
 | ||p_{F_m}||_infinity-||p_F||_infinity |
 <=39.233 Z^(-1/6) Delta_m^(1/9) ->0.
}`                                                               (7.3)

This is a genuine partner-to-equation application. In the volume branch the height passage is not merely lower semicontinuous: it is quantitatively continuous in source `L1`.

The same completed partner report gives, for `alpha=1/16`,

`boxed{
 [p_{F_m}-p_F]_{C^{0,1/16}}
 <=166.572 Z^(-17/96) Delta_m^(1/18) ->0.
}`                                                               (7.4)

Thus this certified branch passes BOTH height and continuity/Hölder regularity to rough sources. This is exactly the distinction required by the assignment:

- outside a common integrable Fourier envelope, Theorem 2.1 passes HEIGHT only;
- inside such a branch, (7.1)-(7.4) pass height and quantitative continuity.

No pointwise quadratic Fourier decay, rotated-coordinate independence, or projection-only shortcut is used.

## 8. Precise regularity ledger after this run

1. `A!=0` + absolutely continuous joint input => output is absolutely continuous. This is qualitative and much weaker than QFORM.
2. The universal bounded-density problem is exactly the finiteness of `C_full`, equivalently `C_core` by (6.1).
3. Therefore it is enough, with ZERO loss in the sharp constant, to prove the universal bound for smooth compactly supported cap-one product sources and algebraically generic rational matrices with strict `s_3>1` margin.
4. Weak closure alone does NOT imply continuous output densities.
5. On any branch carrying a common `L1` Fourier envelope, continuity follows separately, and account02/B15 supplies the explicit rough-source modulus (7.1)-(7.4).
6. The completed account02/B15 fixed-matrix theorem at `9b8bb7e...` reports `rank(A)>=3 => p_Q in C_0` with an instance-dependent constant. This is compatible with the ledger but is not the missing universal estimate.

## 9. First unpaid implication

The full target is reduced without loss to the smooth/generic core:

`sup_{n, B in G_n, f_i in C_c^infinity, 0<=f_i<=1}
 H((x^T B x)#(prod_i f_i dx)) < infinity.`                       (9.1)

Every matrix in this core has nonzero physical pivots/minors, but their magnitudes may be arbitrarily small. Hence the next structural step is NOT another genericization argument; it is to aggregate the original-coordinate product structure across banks/ridges/minority sheets before paying reciprocal near-singular minor costs. The live two-sheet X-ray and rotated-independence corrections remain binding.

Full QFORM remains OPEN.
