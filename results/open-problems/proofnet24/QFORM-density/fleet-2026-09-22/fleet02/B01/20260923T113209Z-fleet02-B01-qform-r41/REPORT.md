SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account 02, slot B01, 2026-09-23T11:32:09Z.
attacking: exact Schur cancellation of a strong overlapping rank-two bicore, and a product-preserving pre-Schur averaged-frequency exit before any residual determinant is inverted.

# fleet02/B01 r41 — complete rank-two Schur cancellation, with a pre-Schur Fresnel exit

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `20260923T113209Z-fleet02-B01-qform-r41`  
Classification: **EXPLICIT INTERMEDIATE STRUCTURAL OBSTRUCTION + SOURCE-VALID TARGET FAMILY PAID / FULL QFORM OPEN**  
Execution: **WITHOUT_VERIFIED_BRAIN**  
Continuity: proved for the paid family below; full-target continuity remains open.

## 1. Control and source boundary

Fresh owner control remained revision `2026-09-22.15`, QFORM-only, with no fleet02/B01 pause or stop at the pre-write refresh. The current programme still marks the unrestricted conjecture OPEN and preserves the phase-aligned-density refutation of every positive-power law-uniform scalar quadratic-phase decay estimate.

The required current compatible Claude/Fourier sources were read from

`proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/`

with current blobs `RESULTS.md=62e20ee976ddeb3f42d3ee5befd6ed49edc917a5`, `FOURIER_ROUTE_REPORT.md=9da148eed6cd43b1046a6f91d0f9329e12921cb4`, and `COUNTEREXAMPLE_SEARCH.md=ee721b237e206f31298b1871979faaab37a1bac2`. The initial Fourier/counterexample source commit is `e5f71d79eff325201dd0274053d20268ce65b837`.

The concrete source theorem used below is the rank-r Fresnel--Brascamp--Lieb bound from `FOURIER_ROUTE_REPORT.md`: for a product-law quadratic polynomial whose quadratic part is `D+R Lambda R^T`, with `D` diagonal, `R` having orthonormal columns and every physical row leverage at most `1/2`,

`|phi(t)| <= (4 pi)^(r/2) |t|^(-r/2) prod_k |lambda_k|^(-1/2)`,

and for `r>2`,

`||p||_infinity <= [4r/(r-2)] (prod_k |lambda_k|)^(-1/r)`.

Linear terms are allowed. Therefore the theorem may be applied after conditioning arbitrary disjoint ORIGINAL coordinates; no post-rotation independence is asserted.

A related earlier correction is fleet02/B07 r13, `math-open-problems@febf0c97f0f85e802b6bc2ab4a475c15109de013`, which records a family where a legitimate rank-two pair Schur correction annihilates one rank-one component of a pre-completion far core. The construction below strengthens that obstruction to **complete annihilation of a quantitatively strong rank-two bicore**, while also giving a uniform pre-Schur Fourier payment.

## 2. Exact construction

Let

`H0 = [[0,1],[1,0]]`.

Let `U,V` be `m x 2` matrices with orthonormal columns and flat row leverage

`||U_(i,*)||_2^2 = ||V_(j,*)||_2^2 = 2/m`.

Two flat Walsh columns give such frames for arbitrarily large even `m`. Fix

`sigma >= 1`, `eps > 0`, `c = sqrt(sigma eps)`.

Use ORIGINAL coordinate banks `P` of size two, `I` of size `m`, and `J` of size `m`. Define the symmetric physical-coordinate matrix

`A = [[eps H0,  c U^T,       c H0 V^T],
      [c U,     0,           sigma U V^T],
      [c V H0,  sigma V U^T, 0          ]].`                    (2.1)

All stochastic inputs remain arbitrary independent real variables with densities bounded by one.

The physical pair block on `P` is

`B = eps H0`, `B^(-1)=eps^(-1)H0`,

so it is invertible indefinite with

`|det B|=eps^2`, `sigma_min(B)=eps`.                               (2.2)

The original `I x J` bicore is

`K = sigma U V^T`,                                                  (2.3)

which has exactly two nonzero singular values `sigma,sigma`; hence its rank-two singular product is

`Delta_pre = sigma^2`.                                              (2.4)

Thus the pre-Schur bicore is quantitatively strong even when `eps` is arbitrarily small.

## 3. Complete Schur annihilation

Eliminate the actual physical pair `P`. The exact Schur cross block between the remaining ORIGINAL banks `I,J` is

`K_S = K - (cU) B^(-1) (c H0 V^T)`
`    = sigma U V^T - (c^2/eps) U H0^2 V^T`
`    = sigma U V^T - sigma U V^T`
`    = 0`.                                                          (3.1)

Therefore

`boxed: Delta_post = 0 while Delta_pre = sigma^2 >= 1.`             (3.2)

This proves the structural correction

**`QFORM-PRESCHUR-RANK2-NOT-SCHUR-STABLE-v1`.** There is no positive lower bound on the rank-two singular product of the post-pair Schur cross block in terms of the original rank-two bicore product and the nonzero pair invariants alone, when overlap couplings are unrestricted. It can vanish identically.

This does not contradict the earlier fleet02/B01 pair-plus-rank2-Schur theorem: that theorem correctly assumes a rank-two packet in the **actual Schur remainder**. The point here is that a routing argument may not substitute the pre-Schur `Delta_pre` for that hypothesis.

## 4. Exact spectrum: the obstruction lies inside the owner target

The matrix vanishes on the orthogonal complements of the columns of `U,V`. On the six-dimensional active space, simultaneous diagonalisation of `H0` is used only for deterministic spectrum computation, never to rotate the product probability law.

For `h in {+1,-1}` the corresponding three-dimensional coefficient block is

`M_h = [[eps h, c,   c h],
        [c,     0,   sigma],
        [c h,   sigma, 0]],`                                       (4.1)

with `c^2=sigma eps`. For `h=+1`,

`det(M_+ - lambda I)
 = (lambda+sigma)(eps lambda + eps sigma - lambda^2 + lambda sigma)`,

and the `h=-1` spectrum is its sign reflection. Put

`a = [sigma+eps + sqrt(sigma^2+6 sigma eps+eps^2)]/2`,
`b = [sqrt(sigma^2+6 sigma eps+eps^2) - (sigma+eps)]/2`.

Both are positive and `a>sigma`. The six nonzero eigenvalues of `A` are exactly

`{-a,-sigma,-b,b,sigma,a}`.                                        (4.2)

Hence every `sigma>=1` gives at least four eigenvalues of modulus at least one. The construction is therefore a genuine full-target family, not merely a certificate counterexample outside QFORM.

## 5. Required newest-source application: pay before Schur elimination

Condition on the two ORIGINAL coordinates `X_P`. This keeps all leaf coordinates independent. The conditional leaf quadratic part is exactly

`A_leaf = [[0, sigma U V^T],
           [sigma V U^T, 0]].`                                     (5.1)

The pair-to-leaf overlap in (2.1) becomes only a linear term after this conditioning.

The rank-four leaf block has eigenvalues

`+sigma,+sigma,-sigma,-sigma`.                                     (5.2)

An orthonormal eigenframe is generated by `(u_k,+v_k)/sqrt(2)` and `(u_k,-v_k)/sqrt(2)`, `k=1,2`. For every physical coordinate in either leaf bank, its leverage in this four-dimensional frame is exactly

`2/m`.                                                             (5.3)

Thus for `m>=4` the leverage is at most `1/2`. Apply the current rank-r Fresnel--Brascamp--Lieb theorem with `r=4`. Uniformly in the conditioned pair values,

`|phi_(Q|X_P)(t)|
 <= (4 pi)^2 sigma^(-2) |t|^(-2)`.                                (5.4)

Together with `|phi|<=1`, the same envelope holds after averaging over `X_P`. Since

`int_R min(1,16 pi^2 sigma^(-2)t^(-2)) dt = 16 pi/sigma`,

Fourier inversion gives

`boxed: ||p_(X^T A X)||_infinity <= 8/sigma <= 8.`                  (5.5)

The characteristic function is in `L1`, so this branch has a continuous `C_0(R)` density.

This is the required actual inequality from the newest averaged-frequency report. It is joint over four diffuse directions and never asserts the refuted scalar bound `|E exp(itX^2)|=O(|t|^(-1/2))` uniformly over cap-one laws.

## 6. Why the natural volume and Schur routes miss the same family

Consider the bank-respecting physical cut

`L={p_1} union I`, `R={p_2} union J`.

In orthonormal effective row/column bases `(p_1,u_1,u_2)` and `(p_2,v_1,v_2)`, its cross block is

`M = [[eps, 0, c],
      [0, sigma, 0],
      [c, 0, sigma]].`                                             (6.1)

The `2 x 2` corner has determinant `eps sigma-c^2=0`, so the nonzero singular values are exactly

`sigma+eps`, `sigma`,                                                (6.2)

and the cross block has rank two. Consequently

`e_3(M^T M)=0`, `e_5(M^T M)=0`.                                   (6.3)

Therefore the newest source's three-volume theorems D/D' and fifth-volume theorem D5 do not pay this natural cut at all. Simultaneously the exact pair Schur route loses the bicore completely by (3.1). The pre-Schur rank-four Fresnel packet is the correct currency here.

This is a concrete obstruction to a proof architecture that insists on Schur elimination before testing a diffuse spectral packet.

## 7. Strict-N3 realization

Set `sigma=1`. All physical diagonal entries of (2.1) are zero. Hence for every pair of physical coordinates `r!=s`,

`det A[{r,s},{r,s}] = -A_rs^2`.                                    (7.1)

The possible off-diagonal magnitudes are bounded by

`eps`, `sqrt(eps/m)`, `2/m`.                                       (7.2)

Given any fixed no-pivot threshold `tau>0`, choose `eps` and then `m` so that

`eps^2<tau`, `eps/m<tau`, `4/m^2<tau`.                             (7.3)

Then every physical diagonal has magnitude `<tau`, every physical `2 x 2` principal determinant has magnitude `<tau`, while the spectrum still contains `-1,+1` and a pair `+-a` with `a>1`. Thus the family lies in strict N3 and (5.5) gives the uniform all-law bound

`boxed: ||p_Q||_infinity <= 8.`                                    (7.4)

## 8. Latest designated-partner application

The newest completed fleet03/B01 result observed before publication is

`math-open-problems@ffbc3b5d921d1c8c391fe1ea3d8c1264697e8813`,

`QFORM-RANK1-BILINEAR-PLUS-SQUARE-LP-v1`. For disjoint ORIGINAL coordinate banks it proves, at `p=3`,

`||p_Q||_infinity <= 12 kappa^(-2/3) rho^(-1/3)`,                  (8.1)

where `kappa=|gamma| ||a||_2 ||b||_2` is the grouped rank-one bilinear strength and `rho=|lambda| ||z||_2^2` is the grouped-square strength. Its executed checker at commit `4efcb4696049e756215fbf29b60205a697809b07` records `K3=12` and target spectra exactly `{-1,1,1}` for its normalized flat-bank family.

Apply (8.1) to the actual strict-N3 family

`Q_partner = 2 (a^T X_I)(b^T X_J) + (z^T X_D)^2`,                  (8.2)

where `I,J,D` are disjoint equal-size ORIGINAL banks and `a,b,z` are flat unit vectors. Here

`kappa=1`, `rho=1`,                                                  (8.3)

so

`boxed: ||p_(Q_partner)||_infinity <= 12.`                          (8.4)

The coefficient matrix has the three nonzero eigenvalues `{-1,1,1}`. Its largest physical diagonal is `1/m` and every physical `2 x 2` principal determinant is `O(m^(-2))`; hence this too enters strict N3 as `m->infinity`. This is an actual use of the newest designated-partner theorem, not a summary.

The relevance to the present obstruction is structural: if a rank-two packet is destroyed or reduced during a legitimate elimination, a surviving source-disjoint rank-one bilinear direction plus grouped square is already a paid endpoint. One must not insist that all rank-two currency survive the Schur step.

## 9. What changed and what remains

The first unpaid implication is sharpened to

**`QFORM-N3-PRESCHUR-OR-SCHUR-ROUTING-v1`.** In arbitrary strict N3, before eliminating a small/indefinite physical pair, route the state quantitatively to at least one of:

1. a strong diffuse pre-Schur leaf packet, paid by Theorem F/MF;
2. a volume packet paid by D/D'/D5;
3. an actual rank-two packet in the post-pair Schur remainder, paid by fleet02/B01 r39;
4. a rank-one bilinear plus source-disjoint grouped square, paid by the newest fleet03/B01 theorem;
5. another already-paid hub/ridge/grouped-square/exact-null/physical-pair branch.

What is **not** allowed is to infer item 3 from a strong pre-Schur rank-two bicore: equations (2.4) and (3.1) show maximal destructive cancellation. The remaining difficult states are those in which overlap destroys the Schur packet while the pre-Schur spectral packet is high-leverage/non-Fresnel and no independent third-curvature packet is available. This is a structural routing debt, not an analytic pointwise-decay debt.

Full QFORM remains **OPEN / NOT PROVED / NOT DISPROVED**. No two independent end-to-end reviews are claimed.
