SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet02, slot B03, 2026-09-24T06:07:49Z.
attacking: the overlap-heavy third-exterior residue after the disjoint-E3 exit — test whether one can still force a single physical square/pair/triple, and if not isolate an aggregate rank-two crossing receiver with dependence-safe whole-copy time.

# fleet02/B03 — diffuse rank-two crossing obstruction and aggregate time closure

Programme: `QFORM-DENSITY-3EIG-20260922`  
Role: decoupled time integral / complementary constructions and source-valid counterexamples  
Status: **NEW SOURCE-VALID STRUCTURAL OBSTRUCTION / UNIFORM AGGREGATE RECEIVER ON THE STRESS FAMILY / FULL QFORM OPEN**  
Execution: `WITHOUT_VERIFIED_BRAIN`.

The unrestricted conjecture remains OPEN. Unrestricted continuity remains OPEN. No moment, compact-support, log-concavity, iid, Gaussian, diagonal-basis, or post-rotation independence hypothesis is introduced.

The first unpaid implication entering this run was the overlap-heavy residue left after the disjoint-third-volume exit and the previous B03 Schur-overlap ladder. The point proved here is that even after one rules out every rank-three physical cross cut, every bounded physical pair determinant, every bounded physical principal-triple scale, and every bounded single-square overlap-one currency, the target can still be uniformly paid by an **aggregate rank-two physical crossing**. Thus a global reduction must preserve that aggregate object before localizing to one physical edge or one physical anchor.

## 1. Sources actually consumed

The required pinned source was read at exactly

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`:

- `RESULTS.md` and `FOURIER_ROUTE_REPORT.md`: audited physical-cross decoupling/Fourier framework and the prohibition on post-rotation independence;
- `COUNTEREXAMPLE_SEARCH.md`: completed Theorem B, which for a form with at least three unit-scale eigenvalues gives

`||p_Q||_infinity <= 2 sqrt(2 pi) sum_i ||P e_i||`,                 (1.1)

with `P` the relevant large/range projection in that theorem.

I apply (1.1) to an actual family in Section 6. I also apply the pinned Theorem-D obstruction literally: every physical disjoint cross block in the family below has rank at most two, hence its third volume `e_3(MM^T)` is exactly zero.

The newest fleet03/B03 report read in this run is r49,

`yspennstate/math-open-problems@77db4c4d258bc99671c78d54d069830f80e2f752`,

including its later normalization supplement `ce3fecfe02212f5db3f9993cea2a0bea2f9cef3e`. Its near-coloop theorem is used in Section 8 to quantify why a single physical-edge localization has the wrong scale here. The **compatible aggregate receiver for the full stress family** is the earlier completed fleet03/B03 r46 theorem

`QFORM-ONE-LINEAR-BANK-R2-DENSITY-v1`,

`yspennstate/math-open-problems@3e4f3896cfaeeb04f1ae283d35848b55809a5d12`.

For an exact rank-two physical cross matrix with nonzero singular values `s_1,s_2`, one source bank entering only linearly, and arbitrary same-bank terms on the other source bank, r46 proves

`||p||_(infinity,ess) <= 2 sqrt(pi) (s_1 s_2)^(-1/2)`.             (1.2)

No singular-vector random coordinates are declared independent in that theorem.

## 2. The diffuse rank-two crossing family

Fix an even integer `n>=4`. Let `R={r_1,r_2}` be two original coordinates and let `C` be a disjoint original-coordinate bank of size `n`. Define two flat orthonormal vectors in `R^n` by

`v_1=n^(-1/2)(1,...,1)`,

`v_2=n^(-1/2)(1,...,1,-1,...,-1)`,                               (2.1)

with `n/2` plus signs and `n/2` minus signs. Let `M` be the `2 x n` matrix with rows `v_1^T,v_2^T`. Then

`M M^T=I_2`,

`s_1(M)=s_2(M)=1`,

`|M_(r,c)|=n^(-1/2)` for every physical entry.                    (2.2)

Let `S` be a third disjoint physical bank of size

`m=n^2`,

and put

`d=1/n`.                                                          (2.3)

On the original-coordinate decomposition `S union R union C`, set

`A_n = d I_S direct_sum [[0,M],[M^T,0]].`                          (2.4)

For independent cap-one coordinates the corresponding quadratic form is

`Q_n = d sum_(s in S) X_s^2 + 2 X_R^T M X_C`.                    (2.5)

The nonzero spectrum is

`{d (multiplicity n^2), +1,+1,-1,-1}`.                            (2.6)

Thus every `A_n` lies in the exact owner target, with four eigenvalues of modulus one.

## 3. Every physical disjoint crossing has rank at most two

This is the first exact obstruction.

Take any literal original-coordinate cut `I|J`. The diagonal `S` block contributes nothing to `A_n[I,J]`, because a diagonal entry can cross a cut only if the same coordinate lies on both sides, which is impossible.

Write

`I_R=I intersect R`, `J_R=J intersect R`,
`I_C=I intersect C`, `J_C=J intersect C`.

After row/column ordering the core cross block is

`[[0, M[I_R,J_C]],
  [M[I_C,J_R]^T, 0]].`                                           (3.1)

The two displayed rectangular pieces act on disjoint row and column supports, so

`rank A_n[I,J]
 = rank M[I_R,J_C] + rank M[I_C,J_R]
 <= |I_R|+|J_R|=2.`                                               (3.2)

Therefore

`boxed: e_3(A_n[I,J] A_n[I,J]^T)=0 for every physical cut I|J.`    (3.3)

In particular the required pinned Theorem D, every marginal-free physical-`E_3` extension, and every mechanism that first demands a rank-three literal crossing are identically unavailable on this target-valid family.

## 4. All bounded-size physical localization scales vanish

### 4.1 Physical pairs

A two-coordinate principal block is nonzero only in the following cases.

- Two coordinates of `S`: determinant `d^2=n^(-2)`.
- One `r in R` and one `c in C`: determinant `-M_rc^2=-n^(-1)`.

Hence

`boxed: max_(|K|=2) |det A_n[K,K]| = 1/n ->0.`                    (4.1)

Thus no fixed physical pair determinant stays quantitative.

### 4.2 Physical principal triples

A nonsingular triple is either three coordinates of `S`, with all singular values `d`, or a triple `{s,r,c}` with matrix

`diag(d, [[0,M_rc],[M_rc,0]])`                                    (4.2)

up to ordering. Therefore

`boxed: max_(|K|=3) sigma_min(A_n[K,K]) = 1/n,}`                  (4.3)

and

`boxed: max_(|K|=3) |det A_n[K,K]| = 1/n^2.}`                    (4.4)

Every other physical principal triple is singular. The pinned localized three-coordinate theorem consequently has a certificate of order at best `6 sqrt(pi) n` on this family, even though the true density will be uniformly bounded in Section 7.

### 4.3 The preceding B03 single-anchor overlap-one currency

Fix `s in S`. Because `A_n` is a direct sum across `S` and the core, every overlap-one third minor whose unique common coordinate is `s` factors as

`det A_n[{s} union P,{s} union Q] = d det B[P,Q]`,                (4.5)

where

`B=[[0,M],[M^T,0]]`                                               (4.6)

is the bipartite core and `P,Q` are disjoint physical two-sets in `R union C`.

The singular values of `B` are `1,1,1,1` and zeros, so

`e_2(B^2)=6`.                                                      (4.7)

For this explicit flat `2 x n` core the second-exterior overlap decomposition is

`E_0^(2)(B)=4-2/n`,
`E_1^(2)(B)=2`,
`E_2^(2)(B)=2/n`,                                                  (4.8)

whose sum is six. For completeness: `E_2^(2)=sum_(r,c) M_rc^4=2/n`; the overlap-one contribution is two by direct enumeration of the common-`R` and common-`C` cases; the disjoint value follows from (4.7).

Thus the exact one-anchor mass is

`mathcal E_(1,s)(A_n)=d^2(4-2/n)=(4-2/n)/n^2`.                   (4.9)

The scale used by the preceding theorem `QFORM-E1-ANCHOR-SQUARE-COMPILER-v1` is therefore

`Gamma_s=A_ss^2 mathcal E_(1,s)
        =(4-2/n)/n^4`.                                            (4.10)

Its right-hand side is

`8 sqrt(2) e^(1/4) Gamma_s^(-1/8)
 =8 sqrt(2) e^(1/4) (4-2/n)^(-1/8) n^(1/2),`                     (4.11)

which diverges. Hence choosing the best one physical square anchor cannot pay this family at universal scale.

Equations (3.3), (4.1), (4.3), and (4.10) together are the obstruction `QFORM-DIFFUSE-R2-NO-BOUNDED-LOCALIZER-v1`.

## 5. Why the obstruction is not a QFORM counterexample

The aggregate crossing `M` itself never degenerates:

`s_1(M)s_2(M)=1.`                                                 (5.1)

The key is to spend that product before selecting a physical edge. The `C` bank has zero quadratic self block, so conditional on the independent diagonal `S` bank, the core is exactly in the scope of the completed fleet03/B03 r46 one-linear-bank theorem. Applying (1.2) to the **whole physical matrix `M`**, not to singular-vector random coordinates, gives

`boxed: ||p_(2 X_R^T M X_C)||_(infinity,ess) <= 2 sqrt(pi).}`     (5.2)

The diagonal contribution

`T_n=d sum_(s in S) X_s^2`                                       (5.3)

is independent of the core. A mixture of translates of a density bounded by `H` is still bounded by `H`; therefore

`boxed: ||p_(Q_n)||_(infinity,ess) <= 2 sqrt(pi)}`                 (5.4)

for every even `n>=4` and every choice of independent cap-one input laws.

Consequently every interval `I` obeys the actual linear small-ball estimate

`boxed: P(Q_n in I) <= 2 sqrt(pi) |I|.`                            (5.5)

This is essential boundedness; no continuity assertion is promoted from r46.

## 6. Required pinned result applied to the same actual family

Condition on the whole `S` bank. The remaining core coefficient matrix is `B` from (4.6), with four nonzero eigenvalues `+1,+1,-1,-1`. Its range projection is the identity on the two `R` coordinates and the projection onto `span(v_1,v_2)` on the `C` bank. Therefore

`||P e_r||=1` for each `r in R`,

`||P e_c||=sqrt(v_1(c)^2+v_2(c)^2)=sqrt(2/n)` for each `c in C`.  (6.1)

The completed pinned `COUNTEREXAMPLE_SEARCH.md` Theorem B gives, uniformly in the conditioned diagonal shift,

`boxed:
 ||p_(Q_n)||_infinity
 <= 2 sqrt(2 pi) (2+sqrt(2n)).
}`                                                                  (6.2)

This is a valid equation-level use of the required `e5f71d79...` result. It also quantifies the obstruction: the fibre/projection-leverage certificate grows like `sqrt(n)`, while the aggregate rank-two receiver (5.4) stays at `2 sqrt(pi)`.

The pinned Theorem-D route is even more sharply obstructed here: by (3.3), its `Z_3` is exactly zero on every physical cut.

## 7. Assigned whole-copy decoupled-time estimate

Set

`H=2 sqrt(pi)`.                                                    (7.1)

From (5.4), the density of the whole scalar difference `Q_n-Q_n'` is bounded by the same `H`, since it is a convolution of `p_(Q_n)` with a reflected probability density. The elementary cap-to-half-Riesz calculation gives

`sup_a E|Q_n-Q_n'-a|^(-1/2) <= 2 sqrt(2H).`                       (7.2)

At `a=0`,

`boxed:
 E|Q_n-Q_n'|^(-1/2)
 <= 4 pi^(1/4)
 =5.32534145520... .
}`                                                                  (7.3)

Using only the **whole-output** identity

`|phi_(Q_n)(t)|^2=E exp(i t (Q_n-Q_n'))`                           (7.4)

and the positive regularized one-dimensional Riesz identity,

`boxed:
 int_R |t|^(-1/2)|phi_(Q_n)(t)|^2 dt
 <=4 sqrt(2) pi^(3/4)
 =13.3486514637... .
}`                                                                  (7.5)

No coordinatewise sum/difference pair is separated or declared independent. Also

`boxed: P(|Q_n-Q_n'|<=epsilon) <=4 sqrt(pi) epsilon.}`             (7.6)

Thus this stress family has the desired linear one-copy small-ball scale and the assigned dependence-safe weighted-time scale despite complete failure of rank-three physical crossing localization.

## 8. Newest fleet03/B03 r49 applied to the local-edge scale

The newest partner r49 is a near-coloop/physical-hyperbola receiver, not the correct aggregate closure for (2.4). Nevertheless it can be applied to an **actual physical edge subform**, and that application diagnoses exactly why edge localization is the wrong scale.

Fix any `r in R,c in C` and put

`beta=M_rc`, so `|beta|=n^(-1/2)`.                                (8.1)

Take the genuine physical coordinate `Z=X_r` (`q=1`) and `C_0=X_c`; pad the residual bank by two unused independent physical coordinates from `S` so that r49's orthonormal `(T,C,D)` notation is literal. For the scalar subform

`Y_(r,c)=2 beta Z C_0`,                                           (8.2)

r49 Theorem 4.1 gives

`boxed:
 H_(1/2)(Y_(r,c))
 <=2^(11/4)|beta|^(-1/2)
 =2^(11/4)n^(1/4).
}`                                                                  (8.3)

This is an actual equation-level application of the newest fleet03/B03 theorem. It is **not** used as a bound for the full `Q_n`; doing so would require deleting all other physical crossing terms, which is forbidden. Its purpose is diagnostic: every individual edge has the fractional scale `n^(1/4)`, while the complete rank-two matrix has singular product one and yields the uniform density (5.4). Aggregate-before-localize is therefore mathematically necessary on this family, not stylistic.

## 9. Structural consequence

The family (2.4) simultaneously has

- exact target spectrum with four eigenvalues of modulus one;
- zero third volume on every literal physical cut;
- `max |det A[K,K]| ->0` for every physical pair;
- every physical principal-three-coordinate spectral scale tending to zero;
- every single-square overlap-one currency `A_ss^2 E_(1,s)` tending to zero;
- yet a uniform full density bound `2 sqrt(pi)` from the aggregate physical rank-two crossing.

Therefore the overlap-heavy global reduction cannot require a bounded physical pair, a bounded physical triple, a bounded single square anchor, or a rank-three physical crossing before recognizing aggregate rank-two geometry.

The first unpaid B03 implication is now more precise: after the global third-compound funnel and the paid disjoint-`E_3`/single-anchor branches, a diffuse overlap-one/two survivor must be routed product-preservingly either to an aggregate rank-two one-linear-bank/projected-crossing receiver of the type used here, to the r49 near-coloop/physical-hyperbola receiver when a genuine physical pivot exists, or to another grouped-hub/finite-carrier mechanism. A bounded-size physical localizer is not an exhaustive bridge.

Full QFORM remains **OPEN**. Full-target continuity remains **OPEN**.
