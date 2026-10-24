SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B14, 2026-09-23T10:36:13Z.
attacking: collective kernel-leakage localization from an indefinite rank-two physical triple, keeping the full outside bank unconditioned until its aggregate slope has been paid.

# account03/B14 r33 — collective kernel leakage from an indefinite rank-two physical triple

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `20260923T103613Z-account03-B14-QFORM-r33`  
Assignment: translations and localization  
Status: `NEW SUPPORTING TARGET-LEVEL THEOREM / FULL QFORM OPEN / CONTINUITY SEPARATE`  
Execution: `WITHOUT_VERIFIED_BRAIN`

## 1. Scope and sources

The target remains the unrestricted statement: for independent original coordinates with probability densities bounded by one and every real symmetric matrix having at least three eigenvalues of modulus at least one, prove a dimension-free essential density bound for `X^T A X`, or give a genuine counterexample. No moment, bounded-support, connected-support, Gaussian, log-concavity, diagonal-basis-independence, or post-rotation-independence assumption is used below.

Fresh owner control was read from `yspennstate/math-research-brain` main. OWNER CONTROL remains revision `2026-09-22.15`, programme `QFORM-DENSITY-3EIG-20260922`. The live correction inbox was refreshed before publication. In particular, this proof does not use law-uniform pointwise quadratic-phase decay, an arbitrary-joint coarea estimate, a conditional projection-density supremum, a uniformly good physical minor, coefficient-to-output-law continuity, bounded-diameter localization, or a finite fragment-count restriction.

Two completed ingredients are used.

1. `account02/B14` random-slope localization, canonical report commit `9c77bae76f0d884fc60a2ffee86ad6269b79d690`, path `proofnet24/QFORM-density/fleet-2026-09-22/account02/B14/20260923T095834Z-account02-B14-QFORM-r33/REPORT.md`. If an invertible indefinite original-coordinate physical pair has `D=|det C|`, `kappa=sigma_min(C)`, and after exact completion its remainder is `Y=X S(V)+R(V)`, where `X` is an original cap-one coordinate independent of the original-coordinate bank `V`, `R` is arbitrary and may be maximally correlated with `S`, and the slope law has density cap `H`, then

   `||p_Q||_infinity <= 8 sqrt(H/kappa)+2 D^(-1/2)`.            (1.1)

2. The designated partner `account04/B14` kernel-leakage physical-enlargement theorem, canonical report commit `6442bbe9d4647a730b27b8e0786bc54b2546b7ec`, path `proofnet24/QFORM-density/fleet-2026-09-22/account04/B14/20260923T011517Z-account04-B14-kernel-leakage-core-r6/REPORT.md`. For a rank-two physical triple with nonzero singular values `nu_1>=nu_2>0`, unit kernel vector `k`, and an added physical coordinate `j` with coupling column `c_j`, it gives

   `||p_Q||_infinity <= C4 sqrt(s1(H_j)s2(H_j))/(|k^T c_j| sqrt(nu_1 nu_2)),` (1.2)

   where `C4=1000(8+log 4)` and `H_j` is the actual four-coordinate principal block.

I also use the standard product-projection estimate already source-pinned in the QFORM corpus: for independent cap-one original coordinates `V` and nonzero `a`,

`||p_(a^T V)||_infinity <= sqrt(2)/||a||_2`.                  (1.3)

The new point is to pay all kernel leakage through the whole vector in (1.3), before selecting any one outside coordinate or normalizing any fragment.

## 2. Matrix algebra for an indefinite rank-two physical triple

Let `S={i_1,i_2,i_3}` be three actual original coordinates and put `B=A[S,S]`. Assume `B` has rank exactly two and is indefinite. Write its two nonzero eigenvalues as `lambda_+>0>lambda_-`, let `nu_1=max(lambda_+,-lambda_-)`, `nu_2=min(lambda_+,-lambda_-)>0`, and let `k` be a unit vector spanning `Ker(B)`.

Let `V=X_{S^c}` denote every remaining original coordinate and define the collective kernel-leakage vector

`w=A[S^c,S] k`, `L=||w||_2`.                                  (2.1)

Assume `L>0`. Choose an index `i in S` with maximal `|k_i|`; then `|k_i|>=1/sqrt(3)`. Let `P=S\{i}` and `C=B[P,P]`.

### Lemma 2.1 — protected indefinite pair inside the rank-two triple

`C` is invertible indefinite and, with `D=|det C|`, `kappa=sigma_min(C)`,

`D=nu_1 nu_2 k_i^2`,                                             (2.2)
`kappa>=nu_2 k_i^2`.                                             (2.3)

Proof. For a symmetric rank-two `3 x 3` matrix with unit kernel vector `k`, spectral calculus gives `adj(B)=lambda_+ lambda_- k k^T`. Thus `det C=lambda_+ lambda_- k_i^2<0`, proving invertible indefiniteness and (2.2). Principal compression gives `sigma_max(C)<=||B||op=nu_1`; since the product of the two singular values of `C` is `D`, `kappa=D/sigma_max(C)>=nu_2 k_i^2`. QED.

Write the physical triple and all outside couplings in the order `(P,i,V)` as

`A = [[ C, b, F ], [ b^T, d, g^T ], [ F^T, g, E ]]`.          (2.4)

Since `det B=0` while `C` is invertible,

`d-b^T C^(-1)b=0`.                                               (2.5)

The kernel relation gives `C k_P+b k_i=0`, hence `k_P=-C^(-1)b k_i`. Define

`a=g-F^T C^(-1)b`.                                               (2.6)

Then the exact identity

`w=A[S^c,S]k=F^T k_P+g k_i=k_i a`                              (2.7)

holds, so `||a||_2=L/|k_i|`. No random coordinate has been rotated.

## 3. Main theorem: collective kernel-leakage localization

### Theorem 3.1 — `QFORM-INDEFINITE-RANK2-COLLECTIVE-KERNEL-LEAKAGE-v1`

Under Section 2, let every original coordinate be independent with probability density at most one. Allow an arbitrary affine perturbation `F_A(X)=X^T A X+eta^T X+c`. If `L=||A[S^c,S]k||_2>0`, then `F_A(X)` has an essentially bounded density and

`boxed: ||p_(F_A)||_infinity <= 8 (3/2)^(1/4)/sqrt(nu_2 L) + 2 sqrt(3)/sqrt(nu_1 nu_2).` (3.1)

A sharper coordinate-dependent form is

`boxed: ||p_(F_A)||_infinity <= 8/[2^(1/4) sqrt(nu_2 L |k_i|)] +2/[sqrt(nu_1 nu_2)|k_i|].` (3.2)

There is no dependence on outside dimension, outside quadratic block, outside support, fragment number or separation, translations, or moments.

Proof. Complete the square only in the two original coordinates `X_P` using the invertible indefinite physical block `C`. Formula (2.5) says the resulting Schur self-coefficient of the remaining original coordinate `X_i` is exactly zero. Formula (2.6) says its cross coupling to the untouched original-coordinate bank `V=X_{S^c}` is exactly `a`. Thus the exact remainder has the form

`Y = X_i [beta+2 a^T V] + R(V)`,                                (3.3)

where `beta` is arbitrary and `R(V)` is an arbitrary measurable quadratic-affine function of the entire outside bank. `R(V)` may be maximally correlated with the slope; the only independence used is that the original coordinate `X_i` is independent of `V`.

By (1.3), `||p_(a^T V)||_infinity <= sqrt(2)/||a||_2`. After scaling by two and translating by `beta`, the slope `S(V)=beta+2a^T V` has cap

`H<=1/(sqrt(2)||a||_2)=|k_i|/(sqrt(2)L)`.                       (3.4)

Apply (1.1) to (3.3). Equations (2.2)-(2.3) and (3.4) give

`||p_(F_A)||_infinity <=8/[2^(1/4) sqrt(nu_2 L |k_i|)] +2/[sqrt(nu_1 nu_2)|k_i|],`

which is (3.2). Finally `|k_i|>=1/sqrt(3)` gives (3.1). QED.

If additionally `nu_1>=1`, `nu_2>=1`, `L>=1`, then

`||p_(F_A)||_infinity <=8(3/2)^(1/4)+2sqrt(3)<12.318.`          (3.5)

This is a structural branch, not a claim that the bare global hypothesis `s_3(A)>=1` forces these three lower bounds for one physical triple.

## 4. Actual application of the designated partner theorem

For each outside coordinate `j`, let `c_j=A[S,j]`, `w_j=k^T c_j`, and `H_j=A[S union {j},S union {j}]`. The designated partner inequality (1.2) gives, whenever `w_j!=0`,

`||p_(F_A)||_infinity <= C4 sqrt(s1(H_j)s2(H_j))/(|w_j| sqrt(nu_1 nu_2)).` (4.1)

Combining (4.1) with Theorem 3.1 gives

`boxed: ||p_(F_A)||_infinity <= min { 8(3/2)^(1/4)/sqrt(nu_2 L)+2sqrt(3)/sqrt(nu_1 nu_2), inf_(j:w_j!=0) C4 sqrt(s1(H_j)s2(H_j))/(|w_j|sqrt(nu_1 nu_2)) }.` (4.2)

The partner wins when one leakage coordinate is strong; Theorem 3.1 is designed for diffuse leakage and pays the aggregate `L=(sum_j w_j^2)^(1/2)` before any reciprocal coordinate coefficient.

## 5. Diffuse-leakage stress family

For `m>=1`, take `B=diag(1,-1,0)`, `k=e_3`, and an outside bank of `m` original coordinates whose only coupling to the triple is `w_m=m^(-1/2)(1,...,1)` from the kernel coordinate; take the outside self block zero. The full matrix is the orthogonal direct sum of `1`, `-1`, and the star block `[[0,w_m^T],[w_m,0]]`. Since `||w_m||_2=1`, its spectrum is

`{1,-1,1,-1,0,...,0}`.                                         (5.1)

Thus every member is inside the original target. Here `nu_1=nu_2=L=1`, `|k_i|=1`, `D=kappa=1`, and (3.2) gives

`boxed: ||p_Q||_infinity <=8*2^(-1/4)+2<8.728,`                 (5.2)

uniformly in `m` and in all admissible product laws.

For every single outside coordinate `j`, `|w_j|=m^(-1/2)` and `H_j` has singular values `1,1,m^(-1/2),m^(-1/2)`. The designated partner bound (4.1) therefore gives `C4 sqrt(m)`, which diverges. This is not a defect in the partner theorem; it is exactly the regime where aggregate-before-inversion is necessary. The new theorem removes that one-coordinate reciprocal loss.

## 6. Localization, continuity, remaining debt

Theorem 3.1 is support-free. Arbitrary outside fragments are retained through the whole statistic `a^T V`, whose cap depends only on `||a||_2`. Affine shifts merely translate the slope or are absorbed into `R(V)`. A finite-fragment proof search may also use the completed affine-family finite-mixture compiler: total-variation approximation then transfers the same interval constant with no support-radius, fragment-count, separation, or translation tax. The correct proof order is to keep the entire leakage bank intact until its slope density has been paid.

Only essential boundedness is proved here. The random-slope / physical-pair logarithmic compiler does not by itself supply a continuous representative, so full-target continuity remains separate.

The unrestricted conjecture remains open. The bare condition `s_3(A)>=1` has not been shown to force an indefinite rank-two physical triple with both intrinsic scale `nu_2` and collective leakage `L` bounded below. When `L` is small, the third spectral resource may live in outside Schur self-curvature, cross-volume/ridge curvature, or a mixed-hub packet. The first remaining structural implication is therefore `QFORM-RANK2-COLLECTIVE-LEAKAGE-OR-VOLUME-EXIT-v1`: in each surviving N3/no-pivot state, extract either (i) a rank-two indefinite physical triple with controlled `nu_2 L` and `nu_1 nu_2`, now paid by Theorem 3.1; (ii) an existing volume/ridge/cross-bank/mixed-hub certificate; or (iii) an outside-curvature branch spending the third spectral resource without selecting one tiny leakage coefficient.

## 7. Integrity

- Full QFORM: `OPEN / NOT PROVED / NOT DISPROVED`.
- New theorem: `QFORM-INDEFINITE-RANK2-COLLECTIVE-KERNEL-LEAKAGE-v1`, (3.1)-(3.2).
- New exact identity: `A[S^c,S]k=k_i(g-F^T C^-1 b)`, (2.7).
- Designated partner account04/B14 actually applied at (4.1)-(4.2), source commit `6442bbe9d4647a730b27b8e0786bc54b2546b7ec`.
- Random-slope source applied at (3.3)-(3.4), source commit `9c77bae76f0d884fc60a2ffee86ad6269b79d690`.
- No moments, support restriction, finite fragment count, Gaussianity, log-concavity, rotated independence, coefficient-to-law continuity, or conditional-density supremum is used.
- Continuity: not proved on this branch; essential boundedness only.
- Native brain ingestion: not verified; repository transport remains `WITHOUT_VERIFIED_BRAIN`.
