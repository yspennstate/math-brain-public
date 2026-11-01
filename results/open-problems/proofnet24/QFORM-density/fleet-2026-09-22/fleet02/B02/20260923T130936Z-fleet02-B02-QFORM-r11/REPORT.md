SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account 02, slot B02, 2026-09-23T13:09:36Z.
attacking: the partner r29 tiny-Schur-tail / two-sided high-leverage collar by retaining the actual rank-four cross block and converting exact-rank-three base leverage into an incident-volume L1 receiver.

# fleet02/B02 r11 — high-leverage compound stability and dominant-pivot incident transport

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** Integrated Fourier estimate  
**Status:** `ESSENTIAL_STEP_APPLIED / FULL_TARGET_OPEN`  
**Execution context:** authenticated repository retrieval plus actual receiver-memory use in this run; this is not a claim of native learned-memory population.  
**Continuity:** proved on the new Fourier-L1 branches below; unrestricted continuity remains open.  
**Target-wide universal unweighted Fourier L1:** `OPEN_NOT_REFUTED`.

The exact target remains the arbitrary product-law statement: every original coordinate has an arbitrary real probability density bounded by one; no moments, bounded support, log-concavity, iid hypothesis, diagonal-basis independence, or post-rotation independence is assumed. The real symmetric matrix may have arbitrary additional spectrum and only has to possess three eigenvalues of modulus at least one.

## 1. Current source map and the live debt

Fresh owner control remained QFORM-only, revision `2026-09-22.15`, with the proof-first/newest-Claude continuation active and no later stop observed before this report.

The required Claude source was read at

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`,

`proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/{RESULTS.md,FOURIER_ROUTE_REPORT.md,COUNTEREXAMPLE_SEARCH.md}`.

I use its physical-cross-block D'/D5 route only through source-valid product-coordinate statements. The q-dependent sharp Hausdorff--Young refinement is taken from

`yspennstate/math-open-problems@c2414ef633b9d4b7f04a83e1aeefbe713ed82bba`,

`proofnet24/QFORM-density/interactive/20260923T002323Z-volume-stability/REPORT.md`.

For an actual physical cross block `M`, if its third-volume row marginals satisfy `alpha_i<=q/2`, `1<=q<3/2`, then

`||p_Q||inf <= [3e/((3-2q)sqrt(q))] E3(M)^(-1/6)`              (1.1)

and the proof gives a genuine unweighted `L1_t` characteristic-function estimate. The degree-five sharp-HY exit is

`||p_Q||inf <=(5e/sqrt(2)) E5(M)^(-1/10)`.                    (1.2)

The newest compatible designated partner is `fleet03/B02` r29,

`yspennstate/math-open-problems@e28bdce394cdb3d096de191390ea5cca0b3cdef9`,

`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B02/20260923T120105Z-fleet03-B02-qform-r29/REPORT.md`.

Its exact remaining collar starts from an ORIGINAL-coordinate physical cross block

`N=[[P,R],[C,M]]`,                                              (1.3)

where `P` is an invertible physical `2x2` pivot, `D=|det P|`, and

`D^2>=theta E2(N)`, `0<theta<=1`.                              (1.4)

Put `S=M-CP^(-1)R`. On the exact-rank-two Schur collar, write

`S=S1+T`, `rank(S1)=rank(T)=1`, `||T||op=s2(S)`,                (1.5)

where `S1` is the top singular term. The partner defines

`N0=[[P,R],[C,CP^(-1)R+S1]]`,                                  (1.6)

`q_theta=sqrt(theta^(-1)-1)`,
`kappa_theta=(1+q_theta)^2`,
`m*=min(sigma_min(P),s1(S))`,
`a=m*/kappa_theta`.                                             (1.7)

Its deterministic shear lemma proves

`rank(N0)=3`, `s3(N0)>=a`, `N-N0=E`, `rank(E)=1`,               (1.8)

and on the tiny-tail branch

`||E||op=s2(S)<=a/16`.                                         (1.9)

The partner paid (1.9) whenever one exact-base range projection has maximum physical leverage at most `1/2`; its remaining state had two-sided high leverage. This run sharpens that collar and converts it into an actual incident determinant packet.

The previous fleet02/B02 transport theorem used below is

`QFORM-INCIDENT32-DISJOINT-TRANSPORT-L1-v1`,

canonical report

`yspennstate/math-open-problems@6f408fc6a3726d1dc6ea86f7ef322ca291c85e12`,

`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B02/20260923T100819Z-fleet02-B02-qform-r11/REPORT.md`.

For incident third-volume mass `J3`, a residual `2x2` minor family of squared mass `H_F`, and tilted determinant laws admitting a row- or column-disjoint coupling with KL costs `D3,D2`, it gives

`||p_Q||inf
 <=5e 2^(-1/5) exp((D3+D2)/10)(J3 H_F)^(-1/10)`,              (1.10)

again by a genuine `L1_t` estimate.

No refuted pointwise quadratic-phase envelope, conditional density cap, arbitrary-joint coarea theorem, post-rotation independence, or deletion of a small random quadratic error is used.

## 2. First live use of D' and D5

Let

`kappa=s3(N)`.

From (1.8)-(1.9), singular-value perturbation gives

`kappa>=15a/16`.                                                (2.1)

Let `P_L` be the orthogonal projection onto `range(N0)` and `P_R` the projection onto `range(N0^T)`, and put

`ell_L=max_i (P_L)_ii`, `ell_R=max_j(P_R)_jj`.                 (2.2)

The volume-stability estimate applied to `P_L` gives for every actual third-volume row marginal of `N`

`sqrt(alpha_i)
 <=sqrt((P_L)_ii)+(sqrt(3)||E||op/kappa)sqrt(1-(P_L)_ii)`
`<=sqrt((P_L)_ii)+(sqrt(3)/15)sqrt(1-(P_L)_ii)`.               (2.3)

The same holds after transposing `N`.

Take the explicit threshold

`h0=3/5`,
`A0=(sqrt(3/5)+(sqrt(3)/15)sqrt(2/5))^2
   =0.718470418323181... <3/4`,                                (2.4)

and

`q0=2A0=1.436940836646362... <3/2`.                            (2.5)

If `min(ell_L,ell_R)<=3/5`, orient the better side as the row side and apply (1.1) to the ACTUAL block `N`. Since `E3(N)>=kappa^6`,

`||p_Q||inf
 <= C0/kappa
 <= (16 C0)/(15a)
 <57.536948/a`,                                                (2.6)

where

`C0=3e/[(3-2q0)sqrt(q0)]=53.940888151446...`.                  (2.7)

Moreover

`integral_R |phi_Q(t)|dt <2pi*57.536948/a`.                    (2.8)

Thus D' pays the entire tiny-tail collar unless BOTH exact-base range projections have a physical leverage greater than `3/5`, a strictly sharper obstruction than the partner's previous `>1/2` state.

D5 is also checked on the live block rather than omitted. Gaussian block elimination preserves rank and gives

`rank(N)=rank(P)+rank(S)=2+2=4`.                               (2.9)

Hence

`E5(N)=0`.                                                      (2.10)

So the ungated D5 estimate is genuinely unavailable on this exact-rank-two Schur collar. This is why the mechanism now changes from fifth-volume smoothing to incident third-volume transport.

## 3. Rank-one perturbations have dimension-free third-compound stability

For a matrix `M`, let `C3(M)=wedge^3 M`, with Frobenius norm

`||C3(M)||F^2=E3(M)`.                                          (3.1)

### Lemma 3.1 — `QFORM-RANK1-COMPOUND3-STABILITY-v1`

If `M0` has rank three and `E=p q^T` has rank one, then

`boxed:
 ||C3(M0+E)-C3(M0)||F
 <=||E||op sqrt(E2(M0)).
}`                                                               (3.2)

### Proof

Because two copies of the rank-one map `E` wedge to zero, the third exterior power has no terms quadratic or cubic in `E`. On decomposable three-vectors the linear term is

`Ex wedge M0 y wedge M0 z
 +M0 x wedge Ey wedge M0 z
 +M0 x wedge M0 y wedge Ez`.

For `E=p q^T` this is exactly the operator factorization

`C3(M0+E)-C3(M0)
 =(p wedge) o (wedge^2 M0) o i_q`,                              (3.3)

where `i_q` is contraction by `q`. Both `p wedge` and `i_q` have operator norms `||p||` and `||q||`. Therefore

`||C3(M0+E)-C3(M0)||F
 <=||p||||q|| ||wedge^2 M0||F
 =||E||op sqrt(E2(M0))`.                                       (3.4)

QED.

Apply the lemma to (1.8)-(1.9). If the three nonzero singular values of `N0` are `s1>=s2>=s3>=a`, then

`E2(N0)/E3(N0)
 =s1^(-2)+s2^(-2)+s3^(-2)
 <=3/a^2`.                                                      (3.5)

Consequently, with

`delta=sqrt(3)/16=0.1082531754730548...`,                      (3.6)

we have

`boxed:
 ||C3(N)-C3(N0)||F
 <=delta sqrt(E3(N0)).
}`                                                               (3.7)

This is the key stability estimate: it depends on the smallest nonzero singular scale `a`, but not on the condition number `s1/s3`, dimension, support, or moments.

## 4. Two-sided high leverage forces a large ACTUAL row-column third-volume star

Assume now the complement of (2.6):

`ell_L>3/5`, `ell_R>3/5`.                                      (4.1)

Take physical indices `i,j` attaining these maxima. Write a thin SVD

`N0=U Sigma V^T`,                                               (4.2)

and let

`ell_i=||U_i||^2>3/5`, `r_j=||V_j||^2>3/5`.                   (4.3)

For exact rank three,

`det N0[S,T]^2
 =det(Sigma)^2 det(U_S)^2 det(V_T)^2`                          (4.4)

for every row triple `S` and column triple `T`. Cauchy--Binet gives

`sum_S det(U_S)^2=sum_T det(V_T)^2=1`,                         (4.5)

and the inclusion identities

`sum_(S contains i) det(U_S)^2=ell_i`,
`sum_(T contains j) det(V_T)^2=r_j`.                            (4.6)

Thus the exact-base row-column incident star has squared compound norm

`J_ij(N0)
 :=sum_(S contains i,T contains j) det N0[S,T]^2
 =ell_i r_j E3(N0)`.                                           (4.7)

Restricting (3.7) to the same coordinate subvector of the compound matrix and applying the reverse triangle inequality gives

`sqrt(J_ij(N))
 >=sqrt(J_ij(N0))-||C3(N)-C3(N0)||F
 >(3/5-delta)sqrt(E3(N0))`.                                    (4.8)

Hence the ACTUAL physical cross block satisfies

`boxed:
 J_ij(N)
 >=c_star E3(N0)
 >=c_star a^6,
}`                                                               (4.9)

where

`c_star=(3/5-sqrt(3)/16)^2
       =0.2418149394323342...`.                                (4.10)

There is also a relative statement. From (3.7),

`sqrt(E3(N))<=(1+delta)sqrt(E3(N0))`,                           (4.11)

so

`boxed:
 J_ij(N)/E3(N)
 >=((3/5-delta)/(1+delta))^2
 =0.1968816133508936....
}`                                                               (4.12)

Thus failure of the sharp-HY diffuse receiver forces one literal physical row-column star to carry at least `19.68%` of the ACTUAL third exterior volume, even after restoring the small nonzero transverse Schur direction. This is not a fixed-minor inference: the whole incident determinant packet is retained.

## 5. Apply the previous incident-(3+2) L1 theorem to the partner's dominant pivot

Let `H_P` be the two physical row indices and `K_P` the two physical column indices of the partner's pivot `P`.

First suppose

`i notin H_P`, `j notin K_P`,                                  (5.1)

so the pivot itself is a residual `2x2` minor after deleting the heavy outer row `i` and column `j`.

Normalize the squared incident minors in (4.9) to a probability law `mu_3` on residual row pairs `R` and residual column pairs `T`. Define

`delta_R=mu_3(R cap H_P=empty)`,
`delta_C=mu_3(T cap K_P=empty)`.                               (5.2)

Take the residual two-minor family `F={P}`. Its squared mass is

`H_F=D^2`,                                                      (5.3)

and its determinant law is a point mass at `(H_P,K_P)`.

If `delta_R>0`, condition `mu_3` on `R cap H_P=empty`. This tilted law has KL cost exactly `log(1/delta_R)`, and its row-pair marginal is automatically disjoint from the deterministic row pair of `P`. Therefore the proved transport theorem (1.10) gives

`||p_Q||inf
 <=5e 2^(-1/5) delta_R^(-1/10)
   (J_ij(N)D^2)^(-1/10)`.                                      (5.4)

The identical inequality with `delta_C` follows by transposing the physical cross block.

Using (4.9),

`||p_Q||inf
 <=5e 2^(-1/5) delta_*^(-1/10)c_star^(-1/10)
   a^(-3/5)D^(-1/5)`,                                         (5.5)

where `delta_*=max(delta_R,delta_C)` and the better orientation is used.

The partner's dominant-minor hypothesis now pays the remaining pivot scale. Since

`E2(N)>=s1(N)^2s2(N)^2>=s3(N)^4=kappa^4`,                     (5.6)

(1.4) and (2.1) imply

`D>=sqrt(theta) kappa^2
 >=sqrt(theta)(15a/16)^2`.                                     (5.7)

Therefore, whenever

`delta_*>=1/4`,                                                 (5.8)

we obtain the genuine integrated-Fourier estimate

`boxed:
 ||p_Q||inf
 <=C_theta/a,
}`                                                               (5.9)

where

`C_theta
 =5e 2^(-1/5)4^(1/10)c_star^(-1/10)
   theta^(-1/10)(16/15)^(2/5)`.                               (5.10)

The characteristic function lies in `L1`, with

`integral |phi_Q| <=2pi C_theta/a`.                            (5.11)

For the live nested endpoint `theta=7/64`,

`C_theta=20.0556090985...`,                                    (5.12)

so

`boxed:
 ||p_Q||inf <20.055610/a
            =20.055610 kappa_theta/m*
            <297.825706/m*.
}`                                                               (5.13)

This is an equation-level application of the completed fleet03/B02 r29 result: its dominant-pivot inequality (1.4), its rank-one perturbative representation (1.8)-(1.9), and its lower bound (2.1) are all used in the new L1 estimate. On this high-leverage/transverse-transport branch, (5.13) is also numerically smaller than the partner's `<335.600555/m*` diffuse-side coefficient.

## 6. Exact classification when the transport exit fails

Continue to assume the pivot is disjoint from the heavy outer anchors, (5.1). If (5.8) fails, then

`delta_R<1/4`, `delta_C<1/4`.                                  (6.1)

Thus more than `3/4` of the incident determinant law has its residual row pair meeting the two pivot rows, and more than `3/4` has its residual column pair meeting the two pivot columns. By the union bound, more than `1/2` of the same incident law satisfies BOTH conditions. Hence

`boxed:
 sum_{S contains i, T contains j,
      (S\{i}) cap H_P !=empty,
      (T\{j}) cap K_P !=empty}
      det N[S,T]^2
 > (1/2)J_ij(N)
 >=(c_star/2)a^6.
}`                                                               (6.2)

Numerically

`c_star/2=0.1209074697161671...`.                              (6.3)

If instead the pivot overlaps the heavy row or heavy column,

`i in H_P` or `j in K_P`,                                      (6.4)

the configuration is already a literal pivot-anchor overlap and is recorded separately rather than forcing the residual transport theorem outside its hypotheses.

Therefore the formerly vague two-sided high-leverage collar has become an explicit trichotomy:

1. one base range side has leverage at most `3/5`: paid by sharp-HY D' with (2.6)-(2.8);
2. both sides are heavy, the dominant pivot is disjoint, and at least one incident law has `>=1/4` avoidance mass: paid by incident-(3+2) transport with (5.9)-(5.13);
3. otherwise either a heavy anchor lies in the dominant `2x2` pivot, or at least `12.09% * a^6` of actual third-volume mass lies in the concrete two-sided pivot-star collar (6.2).

The live block has rank four, so D5 is exactly zero on this collar. The next mechanism should therefore spend the finite pivot-anchor / pivot-star geometry directly, not repeat a fifth-volume attempt or delete the nonzero transverse tail.

## 7. Deterministic constant check

The scalar constants used above are

`delta=sqrt(3)/16=0.10825317547305482`,
`c_star=(3/5-delta)^2=0.2418149394323342`,
`((3/5-delta)/(1+delta))^2=0.19688161335089358`,
`A0=0.718470418323181`,
`q0=1.436940836646362`,
`C0=53.94088815144618`,
`(16/15)C0=57.536947361542595`.

At `theta=7/64`,

`q_theta=sqrt(57/7)=2.8535691936340255`,
`kappa_theta=(1+sqrt(57/7))^2=14.849995530125193`,
`C_theta=20.055609098516616`,
`C_theta*kappa_theta=297.8257054669099`.

These are scalar checks only. The proof is the exterior-power identity (3.3), exact-rank-three Pluecker factorization (4.4), sharp-HY volume theorem, and the source-pinned incident-transport theorem.

## 8. Correction boundary and first unpaid implication

Every current correction remains respected:

- no law-uniform pointwise oscillatory decay;
- no independence after spectral rotation or bankwise shear;
- no arbitrary-joint coarea density theorem;
- no worst conditional projection-density cap;
- no fixed-minor-alone inference;
- no replacement of an exact-zero hypothesis by a merely small coefficient;
- no law-uniform deletion of a small matrix perturbation on unbounded inputs.

The small transverse direction is retained in the ACTUAL matrix `N`; only its effect on the deterministic third compound is bounded by (3.7), and every Fourier estimate is then applied to the actual form.

The first unpaid implication is now

`QFORM-DOMINANT2-PIVOTSTAR-MIXEDHUB-RECEIVER-v1`:

pay either the literal overlap (6.4), or the two-sided pivot-star concentration (6.2), by a grouped mixed-hub / physical-pair / ridge receiver while preserving arbitrary same-bank curvature and the nonzero transverse Schur direction. The surviving packet already contains a fixed dominant physical `2x2` pivot and a fixed heavy outer row-column anchor; at least one additional row and column may still roam, so it is not yet a bounded-dimensional principal block.

No exact-target counterexample to the stronger target-wide statement

`integral_R |E exp(it X^T A X)| dt <= C`

was found. The universal unweighted Fourier-L1 criterion therefore remains `OPEN_NOT_REFUTED`, and so does the unrestricted QFORM conjecture.
