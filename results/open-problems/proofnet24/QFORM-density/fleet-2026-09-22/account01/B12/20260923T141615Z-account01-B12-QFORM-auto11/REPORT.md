SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B12, 2026-09-23T14:16:15Z.
attacking: polar-monotone cross-block stability — arbitrarily large signed spectral additions in the physical polar cone, plus adaptive reserve against hostile cross modes.

# account01/B12 — polar-cone absorption for additional eigenvalues

Programme: `QFORM-DENSITY-3EIG-20260922`  
Assignment: additional eigenvalue control  
Status: **PROVED SUPPORTING STABILITY THEOREM / DESIGNATED PARTNER RESULT APPLIED / D5 RECEIVER APPLIED / EXACT TARGET-CLASS FAMILY / FULL QFORM OPEN / NOT INDEPENDENTLY REVIEWED**  
Execution context: `WITHOUT_VERIFIED_BRAIN`.

## 1. Target and first unpaid implication

The full conjecture remains open: for independent real coordinates with one-dimensional densities at most one and real symmetric `A` with at least three eigenvalues of modulus at least one, prove a dimension-free bound for the density of `X^T A X`, or produce a valid counterexample.

This report proves a stability theorem for the assigned additional-eigenvalue problem. It does **not** derive its hypotheses from the bare spectral condition `s_3(A)>=1`. The remaining structural problem is still to force a product-preserving physical cut/core satisfying one of the completed volume/ridge/grouped-bank/Schur certificates.

The mechanism here differs from the preceding B12 threshold, footprint-rank, and nuclear-tail compilers. A full-rank, unbounded cross update is allowed for free when it lies in the positive cone determined by the **polar factor of the baseline physical cross block**. No commutation with the baseline singular values is required. Hostile residual directions are then handled by the adaptive singular-reserve theorem of the designated partner `account02/B12`.

## 2. Sources actually used

### Designated partner result

`account02/B12`, canonical report:

- repository: `yspennstate/math-open-problems`
- commit: `64268d2bee76cd374e2bf1a34868e0e6a1b7e84d`
- path: `proofnet24/QFORM-density/fleet-2026-09-22/account02/B12/20260923T115313Z-account02-B12-qform-r33/REPORT.md`

The proved adaptive reserve theorem used below is: for compatible rectangular matrices

`M_final=M_base+L+R+T`, `rank L<=r`, `||T||op<=delta`,

and `q+r<=d=min(rows,cols)`, one has

` s_q(M_final) >= max_{0<=p<=d-r-q}[s_{q+r+p}(M_base)-s_{p+1}(R)]-delta. `

The partner proof truncates `R` at rank `p`, spends `r+p` singular reserve directions, and restores the remaining tail by the exact operator-norm error `s_{p+1}(R)`.

### Density receiver

Pinned D5 theorem:

- repository: `yspennstate/math-open-problems`
- commit: `e5f71d79eff325201dd0274053d20268ce65b837`
- path: `proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/FOURIER_ROUTE_REPORT.md`

For an **actual original-coordinate** cross block `M=A[I,J]`, with `I,J` disjoint,

`Z_5=e_5(M^T M)` and `||p_Q||_infinity <= 5 sqrt(2e) Z_5^(-1/10)`.

Hence `s_5(M)>=gamma>0` implies

` ||p_Q||_infinity <= 5 sqrt(2e)/gamma. `

The proof gives an `L^1` characteristic function, so this branch yields a continuous density. Same-bank quadratic blocks, outside coordinates, outside couplings and affine terms are unrestricted.

## 3. Exact polar monotonicity identity

Let `M0` be a real `d x d` invertible matrix and write its right polar decomposition

` M0 = U S, `

where `U` is orthogonal and

` S=(M0^T M0)^(1/2) >0. `

Let `H=H^T>=0` be arbitrary. Define the polar-favourable cross update

` F = U H. `

There is **no** rank or norm restriction on `H`.

### Lemma 3.1 — polar-cone singular-value monotonicity

For every `j=1,...,d`,

` boxed: s_j(M0+F) >= s_j(M0). `

### Proof

Because `U` is orthogonal,

` M0+F = U(S+H). `

Therefore the singular values of `M0+F` are exactly the eigenvalues of the positive semidefinite matrix `S+H`:

` s_j(M0+F)=lambda_j(S+H). `

By Loewner monotonicity, `S+H >= S`, hence by the min-max principle

` lambda_j(S+H)>=lambda_j(S). `

Finally `lambda_j(S)=s_j(M0)`. This proves the claim. QED.

Two points are important.

1. `H` need not commute with `S`. The favourable cone is genuinely matrix-valued, not merely coordinatewise diagonal.
2. The argument is entirely deterministic and occurs in the original physical cross block. No rotation of the random vector is made.

Define the polar cone

` C_pol(M0) = { U H : H=H^T>=0 }. `

Every element of this cone is free for all singular-value lower bounds.

## 4. Main stability theorem — polar cone plus adaptive hostile reserve

Let `I,J` be disjoint original-coordinate banks of equal size `d`. Let `M0=A0[I,J]` be invertible with polar factorization `M0=US`. Suppose the final cross block is

` M = M0 + U H + L + R + T_IJ, `

where

- `H=H^T>=0` is arbitrary, with no rank or norm bound;
- `rank L<=r`, again with no norm bound;
- `R` is arbitrary;
- `T` is an arbitrary full symmetric matrix on the ambient space satisfying `||T||op<=delta`, so `||T_IJ||op<=delta`.

For `q+r<=d`, define

` Gamma_q^pol := max_{0<=p<=d-r-q}[ s_{q+r+p}(M0)-s_{p+1}(R) ] - delta. `

### Theorem 4.1 (`QFORM-POLAR-CONE-ADAPTIVE-RESERVE-v1`)

Under the preceding assumptions,

` boxed: s_q(M) >= Gamma_q^pol. `

In particular the entire favourable full-rank packet `UH` disappears from the bound.

### Proof

Set

` M_plus=M0+UH. `

By Lemma 3.1,

` s_j(M_plus)>=s_j(M0) `

for every `j`. Apply the completed `account02/B12` adaptive reserve theorem to the actual decomposition

` M=M_plus+L+R+T_IJ. `

It yields

` s_q(M) >= max_p [s_{q+r+p}(M_plus)-s_{p+1}(R)]-delta `

`          >= max_p [s_{q+r+p}(M0)-s_{p+1}(R)]-delta `

`          = Gamma_q^pol. `

QED.

This is the required concrete application of a completed designated-partner result to an actual inequality.

### Corollary 4.2 — D5 density compiler

If `q=5` and `Gamma_5^pol>0`, then the D5 theorem applied to the **actual final original-coordinate cross block** gives

` boxed: ||p_{X^T A X}||_infinity <= 5 sqrt(2e)/Gamma_5^pol. `

This branch has a continuous `C_0` density.

No probabilistic statement is made about the separate random variables `X^T(UH)X`, `X^T L X`, `X^T R X` or `X^T T X`. The matrices are combined first, a deterministic physical certificate is proved for the final matrix, and only then is the product-measure density theorem invoked.

## 5. Arbitrary same-bank additions are completely free

The D5 receiver depends on `A[I,J]`, not on `A[I,I]` or `A[J,J]`. Consequently Theorem 4.1 remains valid after adding arbitrary symmetric matrices `K_I` and `K_J` on the two banks, of arbitrary ranks, signs, multiplicities and norms, and after keeping all outside blocks/couplings arbitrary.

Thus a full symmetric added matrix may contain an unrestricted component

` E_free = [[K_I, U H],[H U^T, K_J]] `

with `K_I,K_J` arbitrary symmetric and `H>=0`, while the density bound is unchanged except for the separately declared hostile cross pieces `L,R,T`.

This is stronger than an operator-norm perturbation result: the free part may have unbounded norm and full rank.

## 6. Literal added-eigenvalue interpretation

Take first the pure off-diagonal favourable update

` E_H = [[0,UH],[H U^T,0]]. `

Because `U` is orthogonal, the singular values of `UH` are the eigenvalues of `H`. The standard symmetric-dilation identity therefore gives

` spec(E_H) = { +lambda_1(H),...,+lambda_d(H), -lambda_1(H),...,-lambda_d(H) }. `

Hence the theorem absorbs, with **zero loss**, arbitrarily many simultaneously added eigenvalues of both signs and arbitrarily large magnitudes. The magnitudes can cross any scale. The theorem is not based on assuming those spectral coordinates of `X` are independent.

The arbitrary same-bank matrices `K_I,K_J` add further unrestricted signed spectral content. Their interaction with `E_H` may change the eigenvectors and the final spectrum nontrivially; none of that affects the D5 cross-block certificate.

The `L` packet permits an additional `r` completely hostile cross directions of arbitrary magnitude. The `R` packet permits still more hostile directions: after choosing `p`, its largest `p` singular modes are paid only by consuming reserve directions, while only `s_{p+1}(R)` enters the numeric loss.

## 7. Exact target-class family with an explicit constant

Let `I,J` each contain 16 original coordinates and let

` M0=2 I_16. `

Thus `U=I_16`, `S=2I_16`. Consider **any** final real symmetric matrix whose `I x J` block is

` M = 2I_16 + H + L + R + T_IJ, `

where

- `H=H^T>=0` is completely arbitrary and can have unbounded full-rank spectrum;
- `rank L<=2` with no norm restriction;
- `R` is arbitrary subject only to `s_4(R)<=1/4`; its largest three singular values are completely unrestricted;
- `T` is any ambient symmetric matrix with `||T||op<=1/8`;
- the same-bank blocks `A[I,I]`, `A[J,J]`, every outside block and every outside coupling are arbitrary.

Apply Theorem 4.1 with

`q=5`, `r=2`, `p=3`, `d=16`.

Since

` s_{5+2+3}(M0)=s_10(2I_16)=2 `

and `s_4(R)<=1/4`, one gets the actual final-block inequality

` s_5(M) >= 2 - 1/4 - 1/8 = 13/8. `

Therefore

` Z_5(M)>= (13/8)^10 `

and D5 yields

` boxed: ||p_Q||_infinity <= 5 sqrt(2e)/(13/8) = 40 sqrt(2e)/13 `

`                                      = 7.174289174144998... . `

The density is continuous.

### Why every member is genuinely in the exact owner target class

For the full ambient symmetric matrix `A`, the cross block is the compression

` M=P_I A P_J. `

Singular values are monotone under left/right contractions, hence

` s_j(M)<=s_j(A) `

for every `j`. Since `s_5(M)>=13/8`,

` s_5(A)>=13/8>1. `

For symmetric `A`, its singular values are the absolute values of its eigenvalues. Therefore the final matrix actually has at least five eigenvalues of modulus at least `13/8`, regardless of the arbitrary self blocks and outside couplings. In particular it lies inside the exact target class requiring at least three eigenvalues of modulus at least one.

This family simultaneously allows:

- 16 favourable cross modes with arbitrarily large magnitude and arbitrary mixing inside the PSD matrix `H`;
- their global symmetric-dilation eigenvalues in both positive and negative signs;
- two further completely arbitrary hostile cross directions through `L`;
- three further arbitrarily large hostile singular directions inside `R`;
- an arbitrary full dense ambient tail of norm `1/8`;
- completely unrestricted same-bank and outside quadratic structure.

## 8. One-sided rectangular form

The square/invertible formulation is enough for the explicit theorem above. A rectangular version holds whenever the baseline cross block has full column rank. If `M0` is `m x d`, `m>=d`, write

`M0=US`, `U^T U=I_d`, `S>0`.

For `H>=0`, again

`M0+UH=U(S+H)`

and therefore all `d` singular values weakly increase. The same partner-reserve proof then applies verbatim.

If the baseline is rank deficient, one may restrict the polar-cone update to the initial space of the polar partial isometry; this report does not need that extension, so no stronger claim is made.

## 9. Scope and remaining gap

This theorem is a genuine additional-eigenvalue stability result, not a proof of the full conjecture.

What remains unpaid is structural: starting only from `s_3(A)>=1`, prove that some product-preserving original-coordinate cut admits a baseline cross block and decomposition in which either

1. a large component falls into a polar-favourable cone and the remaining hostile tail has enough singular reserve;
2. an already-completed D5/three-volume/ridge/grouped-bank/hub/localized-core/Schur certificate applies directly;
3. or another exhaustive aggregate mechanism controls the no-pivot survivor.

The known singleton-plus-two-bank and diffuse exact-rank-three examples rule out simply demanding one universally conditioned small principal block or one universal rank-three cross cut.

Continuity status: **proved in the stated D5 scope** because the receiver gives an integrable characteristic function. Continuity for the unrestricted full target remains open.

## 10. Correction audit

The live corrections were re-read before publication. This proof does not use:

- law-uniform pointwise van-der-Corput decay;
- independence after rotating into eigen-coordinates;
- arbitrary-joint coarea;
- positive moments of conditional projection density caps;
- a claim that small matrix norm makes `X^T T X` small;
- naive fiber-supremum integration;
- a universal good small principal minor or rank-three cross cut.

All random-variable conditioning remains inside the pinned D5 receiver on original coordinate banks.

Full target status: **OPEN / NOT PROVED / NOT DISPROVED**.
