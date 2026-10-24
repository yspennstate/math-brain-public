# account01/B19 — exact latent-center global Schur carrier

Programme: `QFORM-DENSITY-3EIG-20260922`.

Status: **ESSENTIAL_STEP_APPLIED / FULL QFORM OPEN / FULL-TARGET CONTINUITY OPEN**.

This run uses only original-coordinate conditioning and deterministic coefficient algebra. No spectral rotation of the independent variables is used; no nonzero coefficient tail is discarded; no bounded support, moments, identical laws, or sign assumption is made.

## 1. Sources actually consumed

The designated partner account02/B19 exact two-hub/common-plane source is

- `yspennstate/math-open-problems@a12ea856984640d876168e74f6e0a2a3f4780029`, `proofnet24/QFORM-density/fleet-2026-09-22/account02/B19/B19-20260923T190836Z-r36/REPORT.md`.

Its live finite-core collar has literal hub pair `T={a,b}`, light bank `L`, physical cross matrix `M=A[T,L]` of rank two, and

`S=sqrt(det(M M^T)) > S0 := 1/(480 sqrt(7626)) = 2.3856699607287348e-5`.

In the exact no-coloop common-plane endpoint, after conditioning the remaining original H-bank coordinates, the light quadratic block has

`D_L = Delta + M^T K M`,

with `Delta` diagonal in the original light coordinates. The preceding account01/B19 receiver pays every nonzero normalized mismatch `K-B^{-1}` in the invertible-indefinite physical-pair chamber. Therefore the exact latent center is

`K=B^{-1}`, hence `D_L=Delta+M^T B^{-1}M`.

The latest designated partner handoff was also reread at `math-open-problems@e5ec25bafeced3d9060be919b2c37049fd53aea6`. It supplies the principal-minimal near-threshold obstruction and explicitly rules out any proof that demands a fixed base gap or fixed carrier norm; its three-Fresnel exit is retained as a paid branch. The present argument does not invoke a forbidden fixed-gap step.

The completed full-matrix physical-pair receiver used below is

- `yspennstate/math-open-problems@742ac943440e41925fe09db9a8c02a96cbd83dbc`, `proofnet24/QFORM-density/interactive/20260922T180015Z-pair-log/FULL_MATRIX_PAIR_EXTENSION.md`.

For an original invertible indefinite physical pair `B`, writing `D_B=|det B|`, `kappa=sigma_min(B)`, and assuming `s_3(A)>=s`, it gives

`||p_Q||_infty <= 3*400^(1/3)*(D_B^2 kappa s)^(-1/6)`

for arbitrary outside curvature/couplings and arbitrary cap-one product laws. This is an essential-boundedness theorem; continuity is not asserted there.

The completed orientation-free rank-two half-Riesz theorem is

- `yspennstate/math-open-problems@e542b1a6ef471b329e4e88a6553e1aacb45acc1a`, `proofnet24/QFORM-density/interactive/20260922T161801Z-rank-two-fusion/REPORT.md`.

It will also be used in Section 5 to record a universal physical three-coordinate receiver.

## 2. New theorem: exact latent center restores a unit global Schur carrier

### Theorem `QFORM-EXACT-LATENT-GLOBAL-SCHUR-CARRIER-v1`

Let the full symmetric coefficient matrix be partitioned in **original coordinates** as `T | R | L`, where `|T|=2`. Write

```
A = [ B    F      M
      F^T  A_RR   C
      M^T  C^T    D_L ].
```

Assume:

1. `B` is invertible (the density payment below uses the indefinite chamber);
2. the exact partner common-plane center holds on the conditioned `T union L` block,
   `D_L = Delta + M^T B^{-1}M`, with `Delta` physical diagonal;
3. `s_3(A)>=1`.

Set `E=[F,M]` and define the **full physical Schur remainder**

`Sglob := A[R union L,R union L] - E^T B^{-1}E`.

Then

```
Sglob = [ U     V
          V^T   Delta ],

U = A_RR - F^T B^{-1}F,
V = C - F^T B^{-1}M,
```

and necessarily

`||Sglob||_op >= 1`.                                                     (2.1)

#### Proof

Define the exact rank-two completion

`A0 = [[B,E],[E^T,E^T B^{-1}E]]`.

It factors as

`A0 = [I;E^T B^{-1}] B [I,B^{-1}E]`,

so `rank(A0)<=2`. Moreover

`A-A0 = diag(0_T,Sglob)`.

Eckart--Young for the third singular value gives

`1 <= s_3(A) <= ||A-A0||_op = ||Sglob||_op`.

The lower-right light block is exactly `Delta` because the partner identity makes

`D_L-M^T B^{-1}M=Delta`.

No random variable has been rotated and no coefficient has been suppressed. QED.

This is the missing exact equation behind the phrase “the third eigenvalue survives the latent rank-two collapse”: the third target-scale resource is not merely somewhere outside the latent plane; it is an **actual full physical Schur remainder of operator norm at least one** after the conditioned bank is restored.

## 3. Apply the completed pair theorem to the actual full matrix

In the invertible-indefinite chamber, the theorem from `FULL_MATRIX_PAIR_EXTENSION.md` applies directly to the same literal physical pair `T`, before any conditioning. Since `s_3(A)>=1`,

`||p_Q||_infty <= 3*400^(1/3)*(D_B^2 kappa)^(-1/6)`.                  (3.1)

Thus, for example, the fixed compound gate

`D_B^2 kappa >= 2^-40`

is fully paid by

`||p_Q||_infty < 2245.646`.                                             (3.2)

This is an actual application of completed peer mathematics to the full unconditioned target; arbitrary `A_RR`, `C`, affine terms, signs, degeneracies elsewhere, and extra spectrum are retained. Therefore the exact-latent-center debt may henceforth be restricted to the **weak physical-pair compound collar** `D_B^2 kappa<2^-40` (together with separately routed definite/singular-pair chambers).

The latest account02/B19 near-threshold obstruction explains why this collar cannot simply be removed by imposing a universal local pivot scale: principal-minimal examples can drive every fixed scalar/pair/triple local pivot scale to zero.

## 4. New carrier trichotomy under the live transverse collar

Let `Pi` denote the orthogonal projection in the light coordinate space onto `row(M)`. The account03/B19 finite-core compiler used by the partner gives in the unpaid transverse chamber

`||C(I-Pi)||_F < 1/64`.

Because `M(I-Pi)=0`, the full Schur cross block satisfies the exact identity

`V(I-Pi)=C(I-Pi)`,

hence

`||V(I-Pi)||_op < 1/64`.                                                (4.1)

For any symmetric two-bank block matrix,

`||[[U,V],[V^T,Delta]]||_op <= max(||U||_op,||Delta||_op)+||V||_op`.

Combining this with (2.1) yields the exhaustive physical carrier alternative

`max(||U||_op,||Delta||_op) >= 1/2`,                                   (4.2)

or

`||V||_op > 1/2`.

In the latter case, (4.1) gives

`||V Pi||_op >= ||V||_op-||V(I-Pi)||_op > 31/64`.                      (4.3)

Therefore the exact latent center with the full third target resource restored has one of three literal coefficient currencies:

1. a light physical diagonal carrier: `||Delta||_op>=1/2`;
2. a finite `R`-bank Schur carrier: `||U||_op>=1/2`;
3. a strong **aligned** Schur cross carrier: `||V Pi||_op>31/64`.

The third alternative is deliberately aligned with the same two-dimensional row space. This respects the partner stress construction: no source-disjoint or transverse third direction is being asserted. The small transverse component in (4.1) is retained in the matrix; it is used only to prove the deterministic inequality (4.3), not deleted as a random perturbation.

## 5. The latent rank-two core retains universal two-volume even when B is weak

The exact latent rank-two coefficient matrix on `T union L` is

`L2 = W B W^T`,

where

`W=[I_2; M^T B^{-1}]`.

Let `P2(L2)` be the product of the two nonzero singular values of `L2`. Since the nonzero eigenvalues of `W B W^T` and `B W^T W` have the same product,

`P2(L2)=D_B det(W^T W)`

`       =D_B det(I_2+B^{-1}G B^{-1})`,

where `G=MM^T` and `S=sqrt(det G)`. Put `H=B^{-1}G B^{-1}>=0`. Then

`det H = S^2/D_B^2`

and, for a positive semidefinite two-by-two matrix,

`det(I+H)=1+tr H+det H >= (1+sqrt(det H))^2`.

Therefore

`P2(L2) >= D_B(1+S/D_B)^2`

`         = D_B+2S+S^2/D_B`

`         >= 4S`.                                                       (5.1)

At the partner's live scale,

`P2(L2) > 4S0 = 9.542679842914939e-5`.                                 (5.2)

Thus degeneration of the literal hub pair does **not** annihilate the two-dimensional latent currency: the factors `B^{-1}M` compensate quantitatively. The remaining receiver should therefore be formulated as “robust rank-two latent volume + a unit full Schur carrier,” not as a proof that requires the hub pair itself to stay uniformly conditioned.

This is a deterministic coefficient statement only. It does not declare the latent coordinates independent.

## 6. Secondary completed receiver: every physical three-coordinate target is uniformly paid

### Theorem `QFORM-PHYSICAL-3X3-UNIFORM-RECEIVER-v1`

Let `A3` be any real symmetric `3x3` matrix with `sigma_min(A3)>=s>0`. Let the three variables be independent with densities bounded by one, and allow arbitrary affine terms coming from conditioning outside the three original coordinates. Then

`||p_Q||_infty <= 128*sqrt(2)/s < 181.020/s`.                          (6.1)

No sign or eigenvalue-multiplicity assumption is required.

#### Proof for s=1

If some physical diagonal satisfies `|a|>=1/4`, square-peel that original coordinate. Its two-dimensional Schur complement `S2` satisfies

`det A3 = a det S2`.

The orientation-free rank-two affine half-Riesz theorem gives

`H_{1/2}(S2) <=128 |det S2|^-1/4`.

The square peel therefore gives

`||p_Q||_infty <= |a|^-1/2 128|det S2|^-1/4`

`=128 |det A3|^-1/4 |a|^-1/4 <=128 sqrt(2)`,

because all three singular values are at least one, so `|det A3|>=1`.

Otherwise every diagonal has magnitude `<1/4`. For any column `i`, `||A3 e_i||>=1`, hence

`sum_{j!=i} A_{ji}^2 >15/16`.

Thus one physical off-diagonal entry has

`|A_ij|>sqrt(15/32)>1/2`,

while both corresponding diagonals have magnitude `<1/4`. The special physical-pair branch of the full-matrix pair theorem then gives `||p_Q||_infty<51`. Scaling by `s` proves (6.1). QED.

This theorem is useful whenever any compiler produces a literal original-coordinate three-variable principal block at a fixed minimum-singular-value scale; it avoids the forbidden step of treating spectral coordinates as independent.

Continuity is not asserted by (6.1); it is an essential-boundedness receiver.

## 7. Compact conditional proof graph after this run

A compact proof assembly now reads as follows.

1. The completed principal-minimal induction (account03/B19 r43) reduces the unrestricted theorem, with no constant loss, to original-coordinate principal-minimal targets; such targets have exactly three threshold-large eigenvalues or mixed-sign four.
2. Existing D/D5, physical E3, transverse-volume, ridge/window, triangle, Fresnel/H, and strong physical-pair exits pay the already-certified diffuse/nondegenerate branches.
3. The designated partner account02/B19 exact no-coloop compiler reduces the hard common-plane chamber to `D_L=Delta+M^T K M`; the preceding account01/B19 theorem pays every nonzero mismatch `K-B^{-1}` in the strong invertible-indefinite pair chamber.
4. At the remaining exact center `K=B^{-1}`, the present theorem restores the conditioned bank and proves the **exact unit Schur carrier** `||Sglob||>=1` in the full matrix. A strong pair compound is immediately paid by (3.1); the weak-pair residue still has latent two-volume bounded below by (5.2) and obeys the physical carrier trichotomy (4.2)--(4.3).
5. The latest account02/B19 construction rules out closing the remaining principal-minimal problem by demanding a fixed base gap, fixed collar, or fixed local pivot. Its three-Fresnel branch remains a paid exit whenever the near-threshold third mode is source-valid and sufficiently spread.

Hence the first sharpened local implication is

`QFORM-LATENT2-UNIT-SCHUR-CARRIER-COUPLED-RECEIVER-v1`:

> In the weak/singular-pair survivor, jointly spend the exact latent rank-two currency `P2(L2)>4S0` and the full physical Schur carrier `||Sglob||>=1`, using the explicit alternatives `||Delta||>=1/2`, `||U||>=1/2`, or `||V Pi||>31/64`, while retaining the nonzero transverse cross tail, arbitrary subthreshold spectrum, and original-product provenance.

The parallel principal-minimal rank-six/base-subcritical threshold-transfer debt from the latest partner remains global. Nothing in this report proves the unrestricted theorem.

## 8. Corrections preserved

The argument does not use: arbitrary-joint coarea; positive moments of conditional projection densities; law-uniform pointwise quadratic-phase decay; dimension-free fiber suprema; independence after a coefficient-space rotation; one-good-minor inversion; bounded support/moments/fragment count; or deletion of a small coefficient matrix as a small random error.

Continuity is tracked separately. The new latent-center theorem and the physical `3x3` receiver establish essential boundedness statements only; they do not add a full-target `C_0` conclusion.
