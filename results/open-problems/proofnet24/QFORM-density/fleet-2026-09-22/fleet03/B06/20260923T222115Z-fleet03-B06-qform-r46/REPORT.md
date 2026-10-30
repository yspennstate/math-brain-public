SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet03, slot B06, 2026-09-23T22:21:15Z.
attacking: QFORM-INDEFINITE-NEARNULL-OFFDIAGONAL-K-AGGREGATION-v1; aggregate the off-diagonal anchored Schur-curvature row before any curved-fiber maximum, and add a determinant-only physical four-coordinate receiver.

# fleet03/B06 r46 — projected anchored-K row receiver and four-coordinate determinant receiver

Programme: `QFORM-DENSITY-3EIG-20260922`  
Owner control: `2026-09-22.15`; programme revision `2026-09-22.5`  
Assignment: curved fiber integration / quantitative inequalities  
Status: `NEW SUPPORTING THEOREMS + ACTUAL PARTNER SPLICE / FULL QFORM OPEN`  
Execution: `WITHOUT_VERIFIED_BRAIN`.

The unrestricted owner target remains OPEN. No Gaussian, log-concavity, moment, compact-support, connected-support, iid, diagonal-basis, or post-rotation independence assumption is introduced. Every conditioning below is on literal original coordinates. The main new branch with the three-hub receiver gives a continuous `C_0` density; the determinant-only four-coordinate receiver establishes absolute continuity and an essential `L^infinity` bound but continuity is not asserted from that proof.

## 1. Fresh source state and corrections consumed


The immediate B06 predecessor is

`yspennstate/math-open-problems@b5d4a62bb80a7ad84db292cb8d886282a95e851b`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B06/20260923T211904Z-fleet03-B06-qform-r45/REPORT.md`.

It identified, around a literal physical two-hub block `H`, the anchored third-curvature matrix

`K_H = det(H) C - E^T adj(H) E`,                                  (1.1)

where

`A = [[H,E],[E^T,C]]`.                                           (1.2)

For every environment coordinate `k`, `(K_H)_{kk}` is exactly the determinant of the physical principal triple consisting of the two hubs and `k`. The r45 debt was the chamber in which all such diagonals are small but substantial off-diagonal/aggregate `K_H` curvature remains.

Three completed inputs are used at their proved scopes.

1. `QFORM-RANK2-AFFINE-HALF-RIESZ-v1`, source

`yspennstate/math-open-problems@e542b1a6ef471b329e4e88a6553e1aacb45acc1a`

`proofnet24/QFORM-density/interactive/20260922T161801Z-rank-two-fusion/REPORT.md`.

For two independent cap-one original coordinates and an invertible symmetric `2 x 2` matrix `S`, arbitrary affine terms satisfy

`sup_t E |Y^T S Y + ell^T Y + c-t|^(-1/2)
 <= 16 sqrt(30) |det S|^(-1/4)`.                                 (1.3)

2. `QFORM-PAIR-LOG-SMALLBALL-SMOOTHING-v1`, source

`yspennstate/math-open-problems@f7f0fedb2d93b46824f96cac1164af6f8a55626f`

`proofnet24/QFORM-density/interactive/20260922T180015Z-pair-log/PAIR_LOG_THEOREM.md`.

For an invertible indefinite physical pair `B`, with `D=|det B|`, `kappa=sigma_min(B)`, and a residual satisfying

`sup_t P(|R-t|<rho) <= H0 sqrt(rho)`,                             (1.4)

the full pair-plus-residual form has

`||p_Q||_infinity <=4 sqrt(2 H0) (D kappa)^(-1/4)`.              (1.5)

3. `QFORM-THREE-HUB-JOINT-PLANCHEREL-v1`, source

`yspennstate/math-open-problems@f98635ec90f47da9c38e40516896462bb423f3c6`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B01/20260923T140911Z-fleet02-B01-qform-r43/REPORT.md`.

For three ORIGINAL hub coordinates whose full hub-to-complement cross matrix is `B3` of rank three, arbitrary hub self-curvature, arbitrary complement self-curvature, and arbitrary affine terms are allowed, and

`||p_Q||_infinity <= 3 sqrt(2) Pi_3(B3)^(-1/3)`,                 (1.6)

where

`Pi_3(B3)=sqrt(det(B3 B3^T))`.                                   (1.7)

This branch has a continuous `C_0` density. The proof is joint three-dimensional Plancherel/product-projection, not a product of false scalar pointwise Fresnel bounds.

The designated partner theorem actually applied in Section 5 is fleet04/B06's `QFORM-BANKWISE-TRIPLE-CURVATURE-v1`, source

`yspennstate/math-open-problems@f24c8db8946d54f4da2d11898697913af766ad32`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B06/20260923T184145Z-fleet04-B06-QFORM-r1/REPORT.md`.

## 2. New theorem A: determinant-only physical four-coordinate receiver

### Theorem 2.1 — `QFORM-PHYSICAL-FOUR-DETERMINANT-RECEIVER-v1`

Let `Z_1,...,Z_4` be independent real random variables with probability densities bounded by one. Let `M=M^T` be any invertible real `4 x 4` matrix and `ell in R^4`, `c in R`. Then

`Q_4 = Z^T M Z + ell^T Z + c`                                    (2.1)

has an essentially bounded density satisfying

`boxed: ||p_(Q_4)||_infinity < 93 |det M|^(-1/4).`               (2.2)

No sign restriction is imposed on `M`.

### Proof

Normalize first to

`|det M|=1`.                                                      (2.3)

Set

`tau=1/4`, `m=1/2`.                                               (2.4)

We use two exhaustive cases.

#### Case A: a physical diagonal pivot has magnitude at least `1/4`

After permuting the four ORIGINAL coordinates, write

`M=[[a,v^T],[v,N]]`, `|a|>=1/4`,
`S=N-vv^T/a`.                                                     (2.5)

Then

`det S=det M/a`, hence `|det S|=1/|a|`.                          (2.6)

Completing only the literal scalar `Z_1`,

`Q_4=a[Z_1+psi(Y)]^2 + R(Y)`, `Y=(Z_2,Z_3,Z_4)`,                 (2.7)

where `R(Y)=Y^T S Y+beta^T Y+c0`. Because `Z_1` is independent of `Y` and its density is at most one, the translated-square pushforward gives for almost every `t`

`p_(Q_4)(t) <= |a|^(-1/2) E |R-t|^(-1/2)`.                      (2.8)

The r45 determinant-only three-coordinate theorem gives

`||p_R||_infinity <=102 |det S|^(-1/3)=102 |a|^(1/3)`.          (2.9)

For any probability density `p<=M0`, layer cake gives the sharp elementary estimate

`sup_t int |u-t|^(-1/2) p(u) du
 <= int_0^infinity min(1,2M0 s^(-2)) ds
 =2 sqrt(2M0)`.                                                  (2.10)

Therefore

`||p_(Q_4)||_infinity
 <=2 sqrt(204) |a|^(-1/2+1/6)
 =2 sqrt(204) |a|^(-1/3)
 <=2 sqrt(204) 4^(1/3)
 =45.3452440... <46`.                                            (2.11)

#### Case B: every physical diagonal has magnitude `<1/4`

Assume for contradiction that every off-diagonal entry also has magnitude at most `1/2`. Expand the determinant by permutations. Classifying permutations of four symbols by cycle type gives the absolute bound

`|det M|
 <= tau^4 + 6 m^2 tau^2 + 8 m^3 tau + 9 m^4
 =233/256 <1`,                                                   (2.12)

contradicting (2.3). Hence some off-diagonal entry, say `|M_12|`, is `>1/2`.

The literal physical pair

`B=[[M_11,M_12],[M_12,M_22]]`                                    (2.13)

is indefinite because

`M_12^2 >1/4 > |M_11 M_22|`.                                    (2.14)

Comparing with `[[0,M_12],[M_12,0]]`, the diagonal perturbation has operator norm `<1/4`, so

`kappa=sigma_min(B)>|M_12|-1/4>1/4`.                             (2.15)

Also

`D=|det B|=M_12^2-M_11 M_22 >1/4-1/16=3/16`.                   (2.16)

Complete this physical pair. Its residual is an invertible quadratic-plus-affine form in the other two ORIGINAL independent coordinates with Schur matrix `S2`, and

`|det S2|=|det M|/|det B|=1/D`.                                 (2.17)

By (1.3),

`sup_t E |R-t|^(-1/2)
 <=16 sqrt(30) D^(1/4)`.                                         (2.18)

Consequently Markov's inequality in the form

`1_{|R-t|<rho} <= sqrt(rho) |R-t|^(-1/2)`                       (2.19)

gives the pair-log hypothesis (1.4) with

`H0=16 sqrt(30) D^(1/4)`.                                        (2.20)

Insert (2.20) into (1.5):

`||p_(Q_4)||_infinity
 <=4 sqrt(32 sqrt(30)) D^(-1/8) kappa^(-1/4)`
` <4 sqrt(32 sqrt(30)) (16/3)^(1/8) 4^(1/4)`
` =92.32198487... <93`.                                          (2.21)

Cases A and B prove (2.2) under normalization (2.3). For general `M`, put `s=|det M|^(1/4)` and divide the entire polynomial by `s`. The normalized quadratic matrix has determinant modulus one and density rescales by `s^(-1)`, yielding (2.2). QED.

### Scope

This is a literal-original-coordinate theorem. Arbitrary coordinates outside the selected four may be conditioned on first, producing only affine terms in the four retained coordinates. Hence if an arbitrary ambient matrix contains a physical principal `4 x 4` block with determinant modulus at least `eta`, then the full ambient quadratic form satisfies

`||p_Q||_infinity <93 eta^(-1/4)`.                               (2.22)

Continuity is not claimed from this argument.

## 3. New theorem B: the whole off-diagonal anchored-K row is a three-hub cross-volume

Return to the physical two-hub decomposition (1.2), assume

`delta=det H !=0`,                                                (3.1)

and let `K=K_H` be (1.1). Fix one environment ORIGINAL coordinate `j`; write `J` for all other environment coordinates. Define

`E_J = E[:,J]`, `k_j = K[j,J]`.                                  (3.2)

The literal three-hub set is `{hub_1,hub_2,j}`. Its cross matrix to the complement `J` is

`B_j = [[E_J],[C[j,J]]]`,                                        (3.3)

viewed as a `3 x |J|` matrix.

### Theorem 3.1 — `QFORM-ANCHORED-K-PROJECTED-ROW-THREEHUB-v1`

If `E_J` has row rank two, then

`boxed:
 Pi_3(B_j)
 = |delta|^(-1)
   sqrt(det(E_J E_J^T))
   ||P_(ker E_J) k_j||_2.`                                       (3.4)

Equivalently, with

`Theta_j := sqrt(det(E_J E_J^T)) ||P_(ker E_J) K[j,J]||_2`,      (3.5)

one has the target-level continuous-density implication

`boxed:
 Theta_j>0
 => ||p_Q||_infinity
 <=3 sqrt(2) (|delta|/Theta_j)^(1/3).`                            (3.6)

This keeps the entire off-diagonal anchored-curvature row and the entire physical pair-shear plane before inversion. There is no individual-minor reciprocal and no curved-fiber supremum.

### Proof of the identity

Because

`H^(-1)=adj(H)/delta`,                                           (3.7)

the Schur complement of the physical pair is

`S=C-E^T H^(-1)E=K/delta`.                                       (3.8)

Apply to the three rows of `B_j` the determinant-one row operation

`L=[[I_2,0],[-E[:,j]^T H^(-1),1]]`.                              (3.9)

Then

`L B_j = [[E_J],[S[j,J]]]
        = [[E_J],[k_j/delta]]`.                                  (3.10)

Since `det L=1`, the three-dimensional row volume is unchanged:

`det(B_j B_j^T)=det((L B_j)(L B_j)^T)`.                          (3.11)

For any two-row matrix `F` of full row rank and any row vector `q`, the Gram determinant factorizes as

`det Gram(F_1,F_2,q)
 =det(F F^T) ||P_(ker F) q||_2^2`.                               (3.12)

Apply (3.12) with `F=E_J`, `q=k_j/delta`; taking square roots proves (3.4).

Now apply the completed three-original-hub theorem (1.6) to the literal hub set `{hub_1,hub_2,j}`. All hub self-curvature, all complement same-bank curvature, all outside couplings, and all affine terms are retained by that theorem. Substitution of (3.4) gives (3.6). QED.

### Interpretation

The new currency is not `max_k |K_jk|`. It is

`sqrt(det(E_J E_J^T)) * distance(K[j,J], rowspan(E_J))`.         (3.13)

Thus a large off-diagonal Frobenius norm of `K` is useful only to the extent that it survives projection away from the physical pair's two shear rows. This precisely identifies the missing weighted replacement: aggregate the curved Schur row jointly with the original-product shear geometry before taking a supremum.

The failure mode of (3.6) is now geometric and explicit:

1. the physical pair's cross shear has nearly zero two-area; or
2. the anchored-curvature row lies nearly in that shear plane.

Both are lower-dimensional / shear-flat states suitable for bankwise or grouped-square receivers.

## 4. Four-coordinate identity and a necessary warning about off-diagonal `K`

For two distinct environment coordinates `j,k`, let `M_{jk}` be the physical principal `4 x 4` block on the two hubs plus `j,k`. Schur determinant gives the exact identity

`boxed:
 det M_{jk}
 = det(K[{j,k},{j,k}]) / delta
 = [K_jj K_kk-K_jk^2]/delta.`                                   (4.1)

Therefore Theorem 2.1 gives

`boxed:
 K_jj K_kk != K_jk^2
 => ||p_Q||_infinity
 <93 [|delta|/|K_jj K_kk-K_jk^2|]^(1/4).`                       (4.2)

This is uniform through `delta ->0` whenever the `2 x 2` anchored exterior determinant stays fixed.

However, **off-diagonal Frobenius mass by itself cannot be converted to (4.2)**. In the exact rank-one model

`K=h h^T`,                                                       (4.3)

every anchored `2 x 2` determinant vanishes identically even though for the flat unit vector `h=(1,...,1)/sqrt(m)` one has

`sum_(j<k) K_jk^2=(1-1/m)/2`.                                   (4.4)

This configuration is realized algebraically by an exact-rank-three Schur remainder, e.g. `H=diag(1,-1)`, `E=0`, `C=-h h^T`, for which `delta=-1` and `K=h h^T`. Thus a proposed implication of the form "large off-diagonal Frobenius norm of `K` => one uniformly useful physical four-volume" is false. It does NOT refute QFORM; it shows why rank-one/grouped-square geometry must be retained rather than replaced by fixed-coordinate minor maxima.

The projected-row receiver (3.6) similarly vanishes in this shear-free stress example because `det(E_J E_J^T)=0`, correctly routing it to a grouped-square / rank-one mechanism rather than making a false curvature claim.

## 5. Actual designated-partner splice

The completed designated partner fleet04/B06 theorem gives, in its exact-rank-three chamber,

`D |lambda| >=1/4`,                                              (5.1)

and three disjoint original-coordinate banks with normal masses

`W_1 W_2 W_3 >61/1728`.                                         (5.2)

For any bank `b` with

`max_k ell_k <=1/2`, `det G_b >= W_b/64`,                        (5.3)

it proves

`||p_Q||_infinity
 <=12 [D |lambda| det G_b]^(-1/3)`.                              (5.4)

Choosing the maximal-normal-mass bank gives

`W_b >(61/1728)^(1/3)=0.3280414319...`;                          (5.5)

if (5.3) holds on that bank, then at the actual inequalities (5.1),(5.5)

`boxed: ||p_Q||_infinity <110.481`,                              (5.6)

with a continuous `C_0` density. This is an actual application of the designated partner theorem, not a restatement of its title.

The new projected-row identity sharpens a complementary physical-third-hub subbranch of the same partner geometry. In the exact-rank-three representation

`A=[[H,E],[E^T,E^T H^(-1)E+lambda h h^T]]`,                     (5.7)

put `g=H^(-1)E` and

`G^(-j)=sum_(k!=j) (g_1k,g_2k,h_k)^T(g_1k,g_2k,h_k)`.            (5.8)

The row-operation calculation in Section 3 specializes exactly to

`boxed:
 Pi_3(B_j)=D |lambda h_j| sqrt(det G^(-j)).`                     (5.9)

Hence, using (5.1), if one physical normal atom and the complementary three-frame obey

`h_j^2 >=1/64`, `det G^(-j)>=1/64`,                              (5.10)

then

`Pi_3(B_j)>= (1/4)(1/8)(1/8)=1/256`,                            (5.11)

and the three-hub receiver gives the much smaller bound

`boxed:
 ||p_Q||_infinity
 <=3 sqrt(2) 256^(1/3)
 =26.93908916... <26.940`,                                      (5.12)

again with a continuous `C_0` density and with arbitrary same-bank complement curvature retained.

Thus a heavy normal coordinate is no longer automatically routed to the much coarser physical-triple determinant bound from r45: if the complement retains genuine three-frame volume, it is paid at `<26.940`; if not, one obtains the precise near-coloop certificate `det G^(-j)<1/64`. This combines the actual partner lower bound `D|lambda|>=1/4` with the new aggregate off-diagonal/shear identity.

## 6. Exact arithmetic and finite sanity checks

The determinant expansion threshold in (2.12) is exact:

`(1/4)^4 +6(1/2)^2(1/4)^2 +8(1/2)^3(1/4)+9(1/2)^4
 =233/256`.                                                      (6.1)

The two normalized four-coordinate branch constants are

`2 sqrt(204) 4^(1/3)=45.3452440001...`,                          (6.2)

`4 sqrt(32 sqrt(30))(16/3)^(1/8)4^(1/4)
 =92.3219848692...`.                                             (6.3)

A 1000-instance Gaussian algebra sanity check was run for the exact identities (4.1) and (3.4). The maximum normalized discrepancies were approximately `9.2e-14` and `9.1e-10`, respectively. The second number is dominated by floating-point projection/conditioning of random Gram matrices. These checks are not the proof; Sections 3 and 4 give the exact Schur/Gram derivations.

## 7. What is now paid and what remains

Paid in this run:

1. every physical invertible `4 x 4` principal block by a determinant-only constant `<93 |det|^(-1/4)`;
2. every nonzero anchored `2 x 2` exterior determinant through (4.2);
3. every anchored off-diagonal row with nonzero projected currency `Theta_j` through the continuous-density bound (3.6);
4. the designated partner's transverse diffuse bank at `<110.481`;
5. in the partner exact-rank-three chamber, a heavy normal coordinate with complementary three-frame determinant at least `1/64` at `<26.940`.

The remaining r46 obstruction is therefore not "off-diagonal `K` is large". It is a structured **rank-one/shear-flat or near-coloop packet**: anchored curvature is close to the physical shear plane (or the shear plane itself has tiny area), its `2 x 2` anchored exterior determinants can all be tiny, and the product source must be aggregated across a bank rather than reduced to a single physical four-block.

The next precise B06 debt is

`QFORM-ANCHORED-K-RANKONE-SHEARFLAT-BANK-RECEIVER-v1`:

combine (3.6) with a quantitative decomposition of `K_H` into its projection onto `rowspan(E)` and its transverse part. If the transverse projected-row energy is large, pay it with a mixed-bank version of the three-hub Plancherel receiver before selecting coordinates. If it is small, use the resulting near-rank-one/shear-flat certificate to enter the fleet04/B06 bankwise triple-curvature theorem, the grouped-square receiver, or a finite heavy-shear-hub receiver, retaining the complete nonzero spectral tail.

The full QFORM conjecture remains OPEN / NOT PROVED / NOT DISPROVED. Global continuity remains OPEN. The three-hub paid branches above are continuous; the four-coordinate determinant theorem is asserted only as an essentially bounded density result.
