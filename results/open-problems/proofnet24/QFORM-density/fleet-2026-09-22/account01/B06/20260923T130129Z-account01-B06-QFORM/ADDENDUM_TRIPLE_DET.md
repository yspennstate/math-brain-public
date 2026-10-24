# Addendum — determinant-only original-coordinate physical triple receiver

Run: `20260923T130129Z-account01-B06-QFORM`  
Status: `SUPPORTING_THEOREM_PROVED / FULL_TARGET_OPEN`  
Execution: `WITHOUT_VERIFIED_BRAIN`.

This addendum is downstream of `REPORT.md` in the same immutable run folder.  It uses the new quarter-Riesz indefinite-pair receiver proved there and the completed orientation-free rank-two half-Riesz theorem at

`yspennstate/math-open-problems@e542b1a6ef471b329e4e88a6553e1aacb45acc1a`

`proofnet24/QFORM-density/interactive/20260922T161801Z-rank-two-fusion/REPORT.md`.

The latter gives, when the active rank-two frame is the two ORIGINAL coordinates themselves (so every affine vector lies in its range),

`sup_t E |Y^T S Y + beta^T Y-t|^(-1/2) <=16sqrt(30)|det S|^(-1/4)`.

No rotation of the independent input law is used below.

## Theorem — `QFORM-PHYSICAL-TRIPLE-DET-ONLY-v1`

Let `X_1,X_2,X_3` be independent real random variables with probability densities at most one. Let `M` be any invertible real symmetric `3 x 3` matrix, let `ell in R^3`, and let `c in R`. Then

`Q=X^T M X+2 ell^T X+c`

has an essentially bounded density satisfying

`boxed: ||p_Q||_infinity <= C_3 |det M|^(-1/3),`

where one may take

`C_3=16*2^(1/4)*sqrt(30)=104.216889989... .`

Consequently, for an arbitrary ambient symmetric matrix `A`, if an ORIGINAL-coordinate principal triple `I` has `det A_(I,I) !=0`, then after conditioning all coordinates outside `I`,

`boxed: ||p_(X^T A X)||_infinity <= C_3 |det A_(I,I)|^(-1/3).`

This is a product-coordinate theorem.  It does not assert the false arbitrary-joint rank-three coarea lemma.

### Proof

Set

`mu=|det M|^(1/3)`.

Write

`M=[[a,b,d],[b,c,f],[d,f,e]].`

We split into two exhaustive physical-coordinate cases.

### Case 1: a physical diagonal has size at least `mu/2`

After a permutation suppose

`|a|>=mu/2`.

Write `Y=(X_2,X_3)` and block-decompose

`M=[[a,r^T],[r,N]]`.

Complete the first ORIGINAL coordinate, retaining all affine terms:

`Q=a(X_1+a^(-1)(r^T Y+ell_1))^2 + Y^T S Y+2 beta^T Y+c_0`,

where

`S=N-r r^T/a`.

Since `M` is invertible,

`det S=det M/a !=0`.

Conditional on `Y`, the translated scalar `X_1+a^(-1)(r^T Y+ell_1)` still has a density bounded by one.  The pushforward of its square term is dominated by the one-sided kernel

`|a|^(-1/2)|w|^(-1/2) 1_(sgn(a)w>0)`.

Therefore, for every `t`,

`p_Q(t)
 <= |a|^(-1/2)
    E |Y^T S Y+2 beta^T Y+c_0-t|^(-1/2).`

Apply the completed rank-two affine half-Riesz theorem to the two independent ORIGINAL coordinates in `Y`:

`p_Q(t)
 <=16sqrt(30)|a|^(-1/2)|det S|^(-1/4)`

`=16sqrt(30)|a|^(-1/4)|det M|^(-1/4)`.

Using `|a|>=mu/2` and `|det M|=mu^3`,

`boxed: ||p_Q||_infinity
 <=16*2^(1/4)*sqrt(30) mu^(-1).`                         (1)

### Case 2: all three physical diagonals are smaller than `mu/2`

Assume

`|a|,|c|,|e|<mu/2`.

We first force a quantitatively nondegenerate ORIGINAL-coordinate indefinite pair.  The determinant identity is

`det M=ace+2bdf-a f^2-c d^2-e b^2`.                    (2)

If all three off-diagonal coefficients obeyed

`|b|,|d|,|f|<=9mu/16`,

then (2) would give

`|det M|/mu^3
 < (1/2)^3 +2(9/16)^3 +3(1/2)(9/16)^2`

`=1957/2048 <1`,

contradicting `|det M|=mu^3`.  Hence, after a permutation,

`|b|>9mu/16`.                                             (3)

Take the physical pair

`B=[[a,b],[b,c]]`.

It is indefinite, because

`det B=ac-b^2 <mu^2/4-81mu^2/256=-17mu^2/256<0`.

Thus, with `D=|det B|`,

`boxed: D>17mu^2/256.`                                    (4)

Complete this ORIGINAL-coordinate pair against the third coordinate.  The scalar Schur remainder is

`R(z)=lambda z^2+gamma z+gamma_0`,

with the exact determinant identity

`|lambda|=|det M|/D`.                                      (5)

The pair theorem proved in `REPORT.md`, `QFORM-WEIGHTED-INDEFINITE-PAIR-RECEIVER-v1`, states

`||p_Q||_infinity
 <=2sqrt(3)D^(-3/8)
    sup_t E|t-R(X_3)|^(-1/4).`                            (6)

For a cap-one scalar input, a direct square small-ball estimate gives, for every `rho>0`,

`sup_t P(|R(X_3)-t|<rho)
 <=2sqrt(2) |lambda|^(-1/2) sqrt(rho).`                   (7)

Indeed, after completing the scalar square, the inverse image of an interval of length `2rho` under `lambda x^2` has total length at most `2sqrt(2rho/|lambda|)`.  Layer cake applied to (7) yields

`sup_t E|R(X_3)-t|^(-1/4)
 <=2^(7/4)|lambda|^(-1/4).`                               (8)

Substitute (5), (8) into (6):

`||p_Q||_infinity
 <=2^(11/4)sqrt(3) D^(-1/8)|det M|^(-1/4).`               (9)

Using (4) and `|det M|=mu^3`,

`||p_Q||_infinity
 <2^(11/4)sqrt(3)(256/17)^(1/8) mu^(-1)`

`<16.354 mu^(-1).`                                        (10)

This is much smaller than the Case 1 constant in (1), so (1) proves the theorem.

### Ambient conditioning

For a full `n x n` symmetric matrix `A`, condition all ORIGINAL coordinates outside a fixed triple `I`.  The three coordinates in `I` remain independent with the same density caps; outside values create only an affine vector and a constant.  Apply the theorem conditionally with `M=A_(I,I)` and average.  The bound is uniform in the conditioning.

QED.

## Scope and consequence for the fleet

This theorem completely pays every branch in which structural work produces one physical principal triple with determinant bounded below at the target scale.  In particular,

`|det A_(I,I)|>=delta*s^3`

implies

`||p_Q||_infinity <= C_3 delta^(-1/3)/s`.

It does **not** solve the full conjecture because the three-large-eigenvalue hypothesis does not force such a physical triple: diffuse exact-rank-three frames can have all individual principal `3 x 3` determinants tending to zero.  The remaining structural debt is therefore still aggregate-before-inversion: convert distributed third-compound mass into this determinant receiver without selecting a vanishing minor, or route the diffuse complement through the existing mixed-Fresnel/volume mechanisms.

Continuity is not asserted by this addendum; it proves essential boundedness in the stated scope.
