SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account 03, slot B20, 2026-09-23T02:07:47Z.
attacking: the at-least-two-internal-rank-two O3 chamber by compressing any rank-one companion into a true product scalar and transporting the aggregate O3 determinant packet through its exact rank-two Schur pseudodeterminant.

# account03/B20 r23 — rank-one companion Schur-pseudodeterminant payment

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** proof closure and keeper  
**Owner control consumed:** revision `2026-09-22.15`  
**Status:** `ESSENTIAL_STEP_APPLIED / PROVED TARGET-LEVEL SUBBRANCH / FULL TARGET OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`, `full_brain_connected=false`.

## 1. Exact live debt and correction boundary

The unrestricted target remains open: for independent real original coordinates with marginal densities at most one and arbitrary real symmetric `A` with at least three eigenvalues of modulus at least one, prove one universal essential density bound for `X^TAX`, or give a target-valid counterexample. Global continuity remains separate.

Fresh account03/B19 r21 closes the O3 state with exactly one internally rank-two resource bank and two rank-one companions. Its first remaining exact-rank-three O3 chamber has at least two resource banks of internal spectral rank at least two. The first subcase is therefore: exactly two such banks and one rank-one companion. This report pays the non-small scalar coefficient part of that subcase without selecting any physical determinant atom.

No step uses post-rotation independence, the refuted arbitrary-joint rank-three coarea inequality, a positive conditional projection-density moment, law-uniform pointwise quadratic-phase decay, a worst-fiber supremum, or a fixed good physical minor.

## 2. O3 packet with one rank-one companion

Work in an exact-rank-three core

`A=R M R^T`, `R^T R=I_3`,                                      (2.1)

where `M=M^T` is invertible and `D=|det M|`. In the target exact-rank-three terminal one has `s_min(M)>=1`, hence `D>=1`.

Let `H,G_1,G_2` be disjoint original-coordinate resource banks from the O3 random-split packet. Assume `H` is spectral rank one: for a unit vector `v`,

`u_h=c_h v`, `h in H`,
`lambda=sum_(h in H)c_h^2>0`.                                   (2.2)

Let the cross-bank aggregate principal-triple determinant mass be

`mu=sum_(h in H,j in G_1,k in G_2) |det A[{h,j,k}]|`.            (2.3)

In the B10/B19 O3 packet, `mu>=1/512`.

Define the normalized original-product scalar

`S=lambda^(-1/2) sum_(h in H)c_h X_h`.                           (2.4)

Its coefficient vector has Euclidean norm one, so the scalar Rogozin--Ball projection theorem gives

`||p_S||_infinity <=sqrt(2)`.                                   (2.5)

Because `H` is disjoint from `G:=G_1 union G_2`, `S` is genuinely independent of all original coordinates in `G`. Condition on every original coordinate outside `H union G`; this contributes only a fixed spectral shift and therefore only affine/constant terms below.

Put

`m=v^T M v`, `a=lambda m`.                                      (2.6)

The theorem below treats `a!=0`.

## 3. Exact Schur pseudodeterminant identity

Let `P=I-vv^T`. Choose an orthonormal basis `E` of `v^perp`, and for every `j in G` put

`w_j=E^T u_j in R^2`.                                           (3.1)

Define

`Delta_G=sum_(j<k in G) det(w_j,w_k)^2
        =det(sum_(j in G) w_j w_j^T)`,                           (3.2)

and the mixed part

`Delta_12=sum_(j in G_1,k in G_2) det(w_j,w_k)^2`.               (3.3)

By exact-rank-three Cauchy--Binet,

`|det A[{h,j,k}]|=D c_h^2 det(v,u_j,u_k)^2`,                     (3.4)

hence

`mu=D lambda Delta_12 <=D lambda Delta_G`.                       (3.5)

In particular `Delta_G>0`.

Complete the square only in the true independent scalar `S`. The quadratic coefficient left on the `G` variables is the spectral Schur operator

`N=M-(Mv)(Mv)^T/m`.                                              (3.6)

In the orthogonal splitting `R v direct_sum v^perp`, write

`M=[[m,q^T],[q,C]]`.

Then

`N=[[0,0],[0,T]]`, `T=C-qq^T/m`,                                (3.7)

and the ordinary scalar Schur determinant identity gives

`|det T|=D/|m|`.                                                 (3.8)

Let `W` be the `|G| x 2` matrix with rows `w_j^T`. The physical residual quadratic matrix on the original coordinates in `G` is

`B_G=W T W^T`.                                                   (3.9)

It has exact rank two because `T` is invertible and `Delta_G=det(W^T W)>0`. Let `Pi` be the product of the absolute values of its two nonzero eigenvalues. The nonzero eigenvalues of `WTW^T` are those of `T W^T W`, so

`Pi=|det T| det(W^T W)=(D/|m|) Delta_G`.                         (3.10)

Multiplying by the scalar coefficient `|a|=lambda|m|` yields the central invariant

`boxed: |a| Pi =D lambda Delta_G >=mu.`                          (3.11)

This is the useful aggregate-before-inversion step: the entire O3 determinant bank becomes the product of the physical square strength and the rank-two Schur pseudodeterminant. No local triple is selected.

## 4. Analytic payment for a non-small companion scalar

After square completion the conditioned quadratic has the form

`Q=a(S+h(X_G))^2 + R_G(X_G)`,                                   (4.1)

where `R_G` has rank-two quadratic core `B_G` and an affine term lying in `range(W)`. The latter point follows directly from (3.6): the conditioned spectral shift enters as `2 R_G^T N y_0`, and `range(N)=v^perp`.

Orthogonalizing the two columns of `W` rewrites `R_G` as an invertible two-dimensional projected quadratic whose determinant is exactly `Pi`, with affine term in the same two-dimensional projection range. Therefore the completed orientation-free rank-two affine half-Riesz theorem applies in its sharper in-range form:

`sup_t E |R_G-t|^(-1/2) <=16 sqrt(30) Pi^(-1/4).`                (4.2)

Conditional on `X_G`, the translated scalar `S+h(X_G)` still has density cap `sqrt(2)`. The exact square-pushforward envelope therefore gives

`||p_Q||_infinity
 <=sqrt(2)|a|^(-1/2) sup_t E|R_G-t|^(-1/2)
 <=16 sqrt(60)|a|^(-1/2)Pi^(-1/4).`                             (4.3)

Using (3.11),

`boxed:
 ||p_Q||_infinity
 <=16 sqrt(60) mu^(-1/4)|a|^(-1/4).
`                                                                      (4.4)

### Theorem 4.1 — `QFORM-O3-RANKONE-COMPANION-SCHUR-PSEUDODET-v1`

In the exact-rank-three O3 packet above, if one resource bank is spectral rank one and its grouped scalar coefficient satisfies

`|a|>=1/24`,                                                      (4.5)

then for every admissible independent cap-one product law, arbitrary signs, and arbitrary affine terms induced by conditioning outside the three resource banks,

`boxed: ||p_Q||_infinity <1305`                                  (4.6)

whenever `mu>=1/512`.

Indeed,

`16 sqrt(60)(512*24)^(1/4)=1304.865980...<1305.`                (4.7)

This proves essential boundedness. Continuity is not claimed from the fractional-potential/square argument.

## 5. What the punctured near-null survivor must carry

The identity (3.11) is stronger than the threshold payment. If

`0<|a|<1/24`,                                                     (5.1)

then in the B10/B19 packet

`boxed: Pi >=mu/|a| >24/512=3/64.`                              (5.2)

Thus the remaining punctured near-null rank-one-companion state is not spectrally weak: after the exact scalar Schur completion, its physical residual has rank two and a uniformly positive nonzero-eigenvalue product `>3/64`. The only loss in (4.4) is the outer square coefficient tending to zero.

The exact endpoint `a=0` is not claimed here. It is qualitatively different because the scalar enters linearly rather than through a legitimate Schur square; replacing true scalar/pair independence by a conditional density cap is explicitly forbidden by the current counterexample ledger.

Consequently the B19 r21 chamber `at least two internal rank-two banks` is narrowed as follows:

- if exactly two banks have internal spectral rank at least two and the third is rank one, the entire `|a|>=1/24` region is paid by Theorem 4.1;
- a punctured survivor `0<|a|<1/24` carries the quantitative rank-two Schur resource `Pi>3/64`;
- the exact-null `a=0` endpoint and the all-three-internal-rank-two state remain separate;
- no perturbative deletion of a small rank-one companion is made.

## 6. Designated partner account04/B20 applied to an actual overlap

Fresh account04/B20 r4 proves `QFORM-PARTITIONED-NEAR-NULL-HYBRID-v1`. Apply it on its exact overlap with the present rank-one-companion state: suppose the exact-rank-three frame has a physical coordinate `h_0 in H` with leverage

`c=||u_(h_0)||^2>=1/2`,                                         (6.1)

all other rows of `H` are longitudinal along `v`, and all non-`H` rows are transverse in `v^perp`. This is precisely the partner's physical longitudinal/transverse partition with `e=v`. If

`|m|=|v^T Mv|<=1/2`,                                            (6.2)

then, because `D>=1`, the partner theorem gives directly

`boxed: ||p_Q||_infinity <105.463.`                             (6.3)

On the complementary part of the same overlap, `|m|>1/2`. Since `lambda>=c>=1/2`,

`|a|=lambda|m|>1/4>1/24`,                                      (6.4)

so Theorem 4.1 applies and gives `<1305` whenever the O3 packet has `mu>=1/512`.

Hence this concrete heavy-companion/exact-transverse-plane overlap is now fully paid for all values of `m`: the designated partner pays the near-null half and the new Schur-pseudodeterminant theorem pays the complementary half. No partner hypothesis is extended to mixed physical rows.

## 7. First remaining implication

The full conjecture remains `OPEN / NOT PROVED / NOT DISPROVED` and arbitrary-extra-spectrum descent remains open.

Inside the exact-rank-three O3 frontier, the first remaining implication is now

`QFORM-O3-RANKONE-COMPANION-NEARNULL-PAYMENT-v1`:

> In the rank-one-companion packet with `mu>=1/512`, pay `a=0` and the punctured range `0<|a|<1/24`, using the quantitative residual rank-two resource `Pi>3/64` in the punctured case, without replacing the grouped scalar by a conditionally capped effective variable and without selecting a vanishing physical minor; then route the all-three-internal-rank-two state separately.

The natural mechanisms are a true-independent-scalar cross-transverse estimate that retains hidden receiver curvature, or an aggregate linear-square/fractional-potential argument uniform as `a->0`.

## 8. Sources actually used

- fresh proof-assembly input: account03/B19 r21, `QFORM-O3-ROBUST-2PLUS1-GROUPED-PAYMENT-v1`, canonical path `proofnet24/QFORM-density/fleet-2026-09-22/account03/B19/20260923T010143Z-account03-B19-QFORM-r21/REPORT.md`;
- O3 aggregate/random-split source: account03/B19 r18 plus account03/B10 r19;
- rank-two affine half-Riesz theorem: `yspennstate/math-open-problems@e542b1a6ef471b329e4e88a6553e1aacb45acc1a`, `proofnet24/QFORM-density/interactive/20260922T161801Z-rank-two-fusion/REPORT.md`;
- designated partner actually applied: account04/B20 r4, `yspennstate/math-open-problems@f97aa31585b7b547a116d4580f898576af4e0842`, `proofnet24/QFORM-density/fleet-2026-09-22/account04/B20/20260923T011956Z-account04-B20-QFORM-r4/REPORT.md`.

`CHECK.py` and `CHECK_OUTPUT.txt` beside this report are arithmetic/algebra regression only; the proof is Sections 2--6.
