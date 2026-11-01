SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet02, slot B04, 2026-09-23T20:55:06Z.
attacking: the zero-diagonal C1-overlap branch via an exact rank-two bipartite rearrangement receiver; optimize the physical two-volume law and compare the e5 volume and direct ridge gates on the same target-valid matrix.

# fleet02/B04 r14 — zero-pivot C1 factorization and a 2xm product-rearrangement receiver

Programme: `QFORM-DENSITY-3EIG-20260922`.
Role: Product Fourier rearrangement / complementary constructions and source-valid counterexamples.
Status: `ESSENTIAL_STEP_APPLIED / SUPPORTING THEOREM / ROUTE SEPARATION / FULL TARGET OPEN`.
Execution context: `WITHOUT_VERIFIED_BRAIN`.
Continuity: not asserted by the new receiver; the full continuous-density question stays separate.

## 0. First unpaid implication

The first unpaid B04 implication after this run is

`QFORM-ZEROPIVOT-C1-TO-2XM-OR-GROUPED-RECEIVER-v1`:

> Starting from target-scale overlap-one third-compound mass `C1(A)` carried by zero or near-zero physical diagonal anchors, prove that either conditioning/grouping a bounded number of ORIGINAL coordinates exposes a clean `2 x m` bilinear packet with target-scale `det(MM^T)`, or the same overlap mass quantitatively enters an already-paid `C2`, pair/hyperbolic, projected-crossing, grouped-hub, or ridge endpoint. The reduction must not manufacture a scalar square, rotate the independent inputs, or invert a vanishing physical minor.

The analytic `2 x m` zero-pivot endpoint itself is paid below. What remains is structural extraction from a general matrix.

## 1. Sources actually applied

The pinned Claude/e5 source is

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`

under `proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/`.

I used the completed product-projection/Ball-Rogozin fact underlying `COUNTEREXAMPLE_SEARCH.md` and, as an explicit obstruction, the proved cross-volume theorems `D`, `D'`, and `D5` from `RESULTS.md` / `FOURIER_ROUTE_REPORT.md`. In particular, `D/D'` require positive physical cross 3-volume and `D5` requires positive physical cross 5-volume.

The newest completed designated partner result observed before publication is fleet03/B04 r40, source-pinned at

`yspennstate/math-open-problems@d795290dd6280b18d6cd02e29e6f7fe06e4c65c2`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B04/20260923T195244Z-fleet03-B04-auto11-r40/REPORT.md`.

Its row-marginal-free critical two-volume theorem says that for

`R=F(X_I)+2 X_I^T B X_J+G(X_J)`, `Z2=e2(BB^T)>0`,

`|phi_R(t)| <= min{1, pi 2^(7/4) Z2^(-1/4)|t|^(-1)}`,

`||p_R||_2^2 <= 2^(11/4) Z2^(-1/4)`,

and

`sup_s E|R-s|^(-1/2) <= 8 2^(3/8) Z2^(-1/8)`.

Its scalar-pivot overlap receiver needs `A_hh != 0`; the family below has `A_hh=0` at every coordinate, so this is exactly the partner's stated zero-pivot survivor rather than a duplicate of its paid branch.

## 2. A rearrangement theorem for a clean physical 2xm bilinear packet

### Theorem 2.1 — `QFORM-PHYSICAL-2XM-BILINEAR-REARRANGEMENT-v1`

Let `X=(X1,X2)` and `Y=(Y1,...,Ym)` be two disjoint ORIGINAL-coordinate banks, all scalar coordinates independent and each with probability density at most one. Let `M` be a real `2 x m` matrix of row rank two, with singular values `s1>=s2>0`. Put

`Q=2 X^T M Y + F(X)`,

where `F` is an arbitrary measurable function of the two-coordinate bank (in particular an arbitrary quadratic-plus-affine self term). Then `Q` has an essentially bounded density and

`boxed: ||p_Q||_infinity <= sqrt(2 pi) (s1 s2)^(-1/2)
                              = sqrt(2 pi) det(MM^T)^(-1/4).`                    (2.1)

No moment, support, log-concavity, connectedness, centering, or post-rotation independence assumption is used.

#### Proof

Fix `x`. Conditional on `X=x`, the random part involving `Y` is the linear form

`2 <M^T x,Y>`

plus the deterministic shift `F(x)`. The sharp one-dimensional product projection estimate (Ball/Rogozin, the same cap used in the pinned e5 source) gives

`||p_{2<M^T x,Y>}||_infinity <= sqrt(2)/(2||M^T x||_2)
                              = 1/(sqrt(2)||M^T x||_2)`                         (2.2)

whenever `x!=0`; the exceptional point has zero probability because `(X1,X2)` has an absolutely continuous joint law.

Therefore, for a.e. output level `t`,

`p_Q(t) <= (1/sqrt(2)) E[ ||M^T X||_2^(-1) ].`                                 (2.3)

Let

`B=(MM^T)^(1/2)`.

Then `||M^T x||_2=||Bx||_2` and `det B=s1 s2`. Since `X1,X2` are ORIGINAL independent variables with scalar density caps one, their two-dimensional joint density satisfies

`f_X(x)=f_1(x_1)f_2(x_2)<=1`.                                                    (2.4)

After the deterministic coefficient change `z=Bx`, the pushforward density `g` has

`0<=g(z)<=K:=1/(s1 s2)`, `integral g=1`.                                       (2.5)

The decreasing rearrangement/bathtub principle for the radial decreasing kernel `|z|^(-1)` gives

`integral g(z)|z|^(-1) dz
 <= K integral_{|z|<=R}|z|^(-1) dz`, `K pi R^2=1`.

Hence

`E ||M^T X||_2^(-1) <= 2 sqrt(pi/(s1 s2)).`                                     (2.6)

Combining (2.3) and (2.6) proves (2.1). The proof never declares the coefficient-space singular vectors to be independent random coordinates. QED.

### Corollary 2.2 — a complete target class

For

`A=[[0_2,M],[M^T,0_m]]`

one has

`spec(A)={+s1,+s2,-s2,-s1,0,...,0}`.                                           (2.7)

Thus if `s2>=1`, `A` already has four eigenvalues of modulus at least one, and every admissible product law satisfies

`boxed: ||p_{X^TAX}||_infinity <= sqrt(2 pi).}`                                  (2.8)

This is a clean zero-diagonal, indefinite, nonseparable target branch. Essential boundedness is proved; continuity is not promoted here.

## 3. Exact zero-pivot C1 factorization for a 2xm bipartite block

The same geometry gives a useful compound identity that explains why the partner's scalar-pivot `C1` receiver can fail while a lower-order product packet remains large.

Let the left physical bank be `L={1,2}`, the right bank be `R`, and

`A=[[0_2,M],[M^T,0]]`.                                                          (3.1)

For a right coordinate `j`, define

`Z2^(-j)=sum_{V subset R\{j}, |V|=2} det(M[:,V])^2`.                            (3.2)

For the overlap-one third-compound mass anchored at the left coordinate `i`, one has the exact identity

`boxed: C_{1,i}(A)=2 sum_{j in R} M_{ij}^2 Z2^(-j),    i=1,2,`                   (3.3)

while every right-coordinate anchor has `C_{1,j}(A)=0`.

#### Proof

A nonzero `3 x 3` minor of a bipartite matrix must balance left rows against right columns. Because the left bank has only two coordinates, an overlap-one pair of triples is necessarily, up to reversing row/column triples,

`S=L union {j}`, `T={i} union V`,

where `i in L`, `|V|=2`, and overlap exactly one means `j notin V`. In the ordered bases `(L,j)` and `(i,V)`, expansion along the unique right-row/left-column entry gives

`|det A[S,T]| = |M_{ij}| |det M[:,V]|`.                                         (3.4)

Summing squares over `V`, `j`, and the reversed orientation gives (3.3). The common coordinate is always the left coordinate `i`, proving the right-anchor assertion. QED.

Thus zero-diagonal `C1` is not intrinsically a third-volume object in this geometry: it is exactly a physical coefficient squared times a complementary two-volume, aggregated before any reciprocal minor is chosen.

## 4. A fully explicit rotated-indefinite stress family

For `L>2`, set

`U=(1/sqrt(2))*[[1,1],[1,-1]]`,

`V=(1/3)*[[2,1],[2,-2],[1,2]]`,

so `U^T U=I_2` and `V^T V=I_2`, and define

`M_L=U diag(L,1) V^T`

`    =(sqrt(2)/6)*[[2L+1, 2L-2, L+2],
                    [2L-1, 2L+2, L-2]].`                                       (4.1)

Every one of its six physical coefficients is nonzero for `L>2`, and its singular values are exactly `L,1`. Embed it as

`A_L=[[0_2,M_L],[M_L^T,0_3]].`                                                  (4.2)

Then

`spec(A_L)={L,1,0,-1,-L}`.                                                      (4.3)

Hence `A_L` is genuinely rotated in the original product coordinates, indefinite, all five physical diagonal entries vanish, and four eigenvalues satisfy `|lambda|>=1`.

Theorem 2.1 yields the explicit target-level estimate

`boxed: ||p_{X^T A_L X}||_infinity <= sqrt(2 pi) L^(-1/2).}`                    (4.4)

This tends to zero as the strong singular value grows, despite the complete failure of every scalar-pivot square receiver.

## 5. Global optimization of the physical two-volume weights

There is only one left row pair. The three physical `2 x 2` minors have determinants

`Delta_12= 2L/3`, `Delta_13=-L/3`, `Delta_23=-2L/3`,                             (5.1)

so their squared sizes are

`L^2*(4/9,1/9,4/9)`,                                                            (5.2)

and

`Z2=e2(M_L M_L^T)=L^2`.                                                         (5.3)

Let `w` be any probability weight on the three nonzero minors and let

`nu=(4/9,1/9,4/9)`                                                              (5.4)

be the canonical squared-volume law. Its determinant-entropy currency is

`G2(w)=exp(sum_T w_T log Delta_T^2 + H(w))
     =Z2 exp(-KL(w||nu)) <= L^2`,                                               (5.5)

with equality uniquely at `w=nu`. Thus (5.4) is the GLOBAL optimizer over all supported physical two-volume weights.

But every supported two-minor uses both physical left rows, so for every possible weight,

`alpha_1=alpha_2=1`.                                                            (5.6)

Therefore every earlier fractional two-volume compiler that requires `alpha_i<=q/2` with `q<2` has an empty feasible set on this matrix. This is not poor optimization: the globally optimal volume law itself sits at the critical marginal boundary. The newest partner r40 theorem is exactly what survives that boundary.

Applying fleet03/B04 r40 at `Z2=L^2` gives the actual same-matrix inequalities

`|phi_Q(t)| <= min{1, pi 2^(7/4) L^(-1/2)|t|^(-1)},`                            (5.7)

`||p_Q||_2^2 <=2^(11/4)L^(-1/2),`                                               (5.8)

and

`sup_s E|Q-s|^(-1/2) <=8 2^(3/8)L^(-1/4).`                                     (5.9)

The critical Fourier envelope (5.7) is not `L^1`, so by itself it does not yield an `L^infinity` density. Theorem 2.1 changes mechanism: it conditions one original bank linearly and spends the same exact pair determinant through a two-dimensional decreasing rearrangement, obtaining the stronger `L^infinity` estimate (4.4).

## 6. The pinned e5 volume theorems give an exact obstruction on every physical cut

This family applies the pinned e5 results to an actual obstruction, not merely a citation.

There are only five original coordinates. For every disjoint physical cut `I,J`, after conditioning any remaining coordinates,

`min(|I|,|J|)<=2`,                                                              (6.1)

so

`rank A_L[I,J] <=2`.                                                            (6.2)

Consequently every physical cross 3-volume and 5-volume vanishes:

`e3(A_L[I,J]^T A_L[I,J])=0`,

`e5(A_L[I,J]^T A_L[I,J])=0`.                                                    (6.3)

Thus the completed e5 Theorem D, its relaxed D' extension, and the marginal-free D5 theorem produce no finite certificate on ANY physical cut of this target-valid matrix. No entropy reweighting can repair this because there is no supported physical third or fifth minor to weight.

This is a source-valid obstruction to the ambient higher-volume route, not a counterexample to QFORM: (4.4) pays the matrix uniformly.

## 7. Direct ridge also has no certificate on any physical cut

For every physical cut, the regularized crossing matrix has rank at most two. Hence for every positive regularization scale,

`theta_gamma=tr K_gamma < 2`.                                                    (7.1)

The completed direct ridge theorem requires `q>=1` and

`theta_gamma>2q>=2`.                                                            (7.2)

Equations (7.1)-(7.2) are incompatible. Therefore the direct ridge family has no certificate on any physical cut of `A_L`.

On the natural `2 x 3` cut this is visible more sharply: `K_gamma` has the two nonzero eigenvalues

`L^2/(L^2+gamma^2)`, `1/(1+gamma^2)`,                                            (7.3)

and its trace is always strictly below two.

The matrix also has no original scalar square pivot because `A_{ii}=0` for all five physical coordinates. I do not claim that every pair/hyperbolic/grouped mechanism fails; indeed the point of this example is that the correct lower-order product mechanism succeeds.

## 8. Exact compound location of the obstruction

For this five-coordinate family, two triples cannot be disjoint, so

`C0(A_L)=0`.                                                                     (8.1)

Every odd principal minor of the zero-diagonal bipartite matrix vanishes, so

`C3(A_L)=0`.                                                                     (8.2)

Using (3.3) and the minors (5.1), direct expansion gives

`boxed: C1(A_L)=(16/27)L^2(L^2+1),`                                              (8.3)

with anchored masses

`C_{1,1}=(8/27)L^2(L^2+L+1)`,

`C_{1,2}=(8/27)L^2(L^2-L+1)`,                                                    (8.4)

and all three right anchors zero. Yet every diagonal-weighted partner currency is exactly zero:

`A_{hh}^2 C_{1,h}=0`.                                                            (8.5)

Since `A_L^2` has eigenvalues `L^2,L^2,1,1,0`,

`e3(A_L^2)=2L^2(L^2+1)`.                                                        (8.6)

Therefore the remaining compound class is

`C2(A_L)=(38/27)L^2(L^2+1)`.                                                     (8.7)

So this is a precise target-valid inhabitant of the partner's unpaid zero-pivot `C1` branch, and it shows that trying to manufacture a scalar square there is unnecessary: the overlap-one packet is already a coefficient-times-two-volume object, and the product rearrangement receiver pays it.

## 9. Concrete stress value L=9

For `L=9`,

`M_9=(sqrt(2)/6)*[[19,16,11],[17,20,7]]`.                                       (9.1)

Its physical pair-minor squares are `(36,9,36)`, so the globally optimized volume law is `(4/9,1/9,4/9)` and `Z2=81`.

The new bounded-density receiver gives

`boxed: ||p_Q||_infinity <= sqrt(2 pi)/3
                              =0.8355427582103334... .}`                          (9.2)

The partner r40 same-matrix critical certificates are

`pi 2^(7/4)/3=3.522338667454749...` for the `|t|^-1` Fourier coefficient,

`||p_Q||_2^2 <=2.242390440676572...`,

`sup_s E|Q-s|^-1/2 <=5.989845327788119...`.                                     (9.3)

The exact overlap masses are

`C1=3936`, `C2=9348`, `C_{1,1}=2184`, `C_{1,2}=1752`,                            (9.4)

while every e5 third/fifth-volume certificate and every direct ridge certificate is absent for the structural reasons in Sections 6-7.

## 10. Mathematical conclusion

This run changes mechanism from the previous ambient-volume/ridge comparisons. A target-valid matrix can simultaneously have:

1. zero physical diagonal pivots at every coordinate;
2. target-scale (indeed growing) overlap-one compound mass;
3. no physical cut with nonzero third or fifth cross volume;
4. no direct ridge certificate on any physical cut;
5. a globally optimized pair-volume law pinned at the forbidden critical marginal `alpha=1`;

and nevertheless satisfy the uniform product-law estimate

`||p_Q||_infinity <= sqrt(2 pi) det(MM^T)^(-1/4)`.

The correct currency is a lower-order physical packet spent through product rearrangement before any reciprocal scalar pivot or higher-volume certificate is demanded. The full QFORM conjecture remains OPEN; the structural extraction step in Section 0 is the next unpaid implication.

No moments, support bounds, log-concavity, diagonal-basis independence, or post-rotation independence were used. No continuity conclusion for the unrestricted target is claimed.
