SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B04, 2026-09-24T05:47:41Z.
attacking: sharpen the physical-triple determinant receiver by splicing the determinant-only physical-pair envelope with a square one-third-Riesz estimate, then spend it on the fresh exact-rank-three overlap-two Plucker branch.

# account03/B04 r51 — pair-envelope / square-Riesz sharpening of the physical-triple determinant receiver

Programme: `QFORM-DENSITY-3EIG-20260922`  
Assignment: Product Fourier rearrangement  
Status: **NEW QUANTITATIVE SHARPENING + FRESH EXACT-RANK-THREE E2 BRANCH CLOSED / FULL QFORM OPEN**  
Regularity: essential boundedness for the new determinant receiver; continuity is **not** asserted from this branch.  
Brain status: `WITHOUT_VERIFIED_BRAIN`.

The full target remains unchanged: independent ORIGINAL real coordinates with one-dimensional probability densities at most one; arbitrary real symmetric coefficient matrix; at least three eigenvalues of modulus at least one. No moment, compact-support, connected-support, Gaussian, log-concave, iid, spectral-coordinate-independence, or post-rotation-independence hypothesis is used.

## 1. Fresh source boundary and nonduplication check


A source-matching theorem already exists: account01/B06 proved `QFORM-PHYSICAL-TRIPLE-DET-ONLY-v1`, with

`||p_Q||_infinity <= 16*2^(1/4)*sqrt(30) |det M|^(-1/3)`

`=104.21688998922089... |det M|^(-1/3)`.

So this run does **not** claim first discovery of determinant-only physical-triple smoothing. The advance is a new product-space splice that improves the universal coefficient by a factor `0.4768815481...`, and then removes the anisotropy gate left open in the fresh account04/B03 exact-rank-three overlap-two reduction.

The analytic input is account01/B03 r40's completed determinant-only physical-pair envelope. For two ORIGINAL independent cap-one variables, every invertible symmetric physical pair `P`, every deterministic translation, and `D=|det P|`, its quadratic output `T` has

`p_T(t) <= C_pair D^(-1/3)|t|^(-1/3)` for a.e. `t!=0`,

where

`C_pair=2+2*pi=8.283185307179586...`.

No random-variable rotation is used in that theorem; its level curves are parameterized in coefficient space while the original product densities remain explicit.

## 2. New scalar lemma — translated square one-third Riesz

### Lemma `QFORM-SQUARE-ONE-THIRD-RIESZ-v1`

Let `Z` have a probability density bounded by one. For every `s!=0`, every `h,c,t in R`,

`boxed:
 E |t-[s(Z+h)^2+c]|^(-1/3) <= 6 |s|^(-1/3).`

### Proof

It is enough to set `W=Z+h`, divide by `|s|`, and bound uniformly in `a in R`

`E|W^2-a|^(-1/3)`.

For every `rho>0`, the Lebesgue measure of

`{w: |w^2-a|<rho}`

is at most `2 sqrt(2) sqrt(rho)`. For `a<0` this is immediate from a single centered interval; for `a>=0`, the exact length is

`2[sqrt(a+rho)-sqrt(max(a-rho,0))]`,

whose maximum over `a>=0` is attained at `a=rho` and equals `2 sqrt(2 rho)`.

Since the density of `W` is at most one,

`P(|W^2-a|<rho) <= min{1,H sqrt(rho)}`,
`H=2sqrt(2)`.

Layer cake at exponent `1/3`, split at `rho_0=H^(-2)`, gives

`E|W^2-a|^(-1/3)
 <= (1/3)H int_0^(H^-2) rho^(-5/6) d rho
    +(1/3)int_(H^-2)^infinity rho^(-4/3)d rho`

`=2H^(2/3)+H^(2/3)=3H^(2/3)=6`.

Rescaling restores `|s|^(-1/3)`. QED.

This is a direct decreasing-rearrangement/small-ball calculation and requires no moments or support geometry.

## 3. Main theorem — improved determinant-only physical triple

### Theorem `QFORM-PHYSICAL-TRIPLE-DET-ONE-THIRD-v2`

Let `X_1,X_2,X_3` be independent real variables with probability densities at most one. Let `M` be any invertible real symmetric `3x3` matrix, `ell in R^3`, and `c in R`. Then

`Q=X^T M X+2 ell^T X+c`

has an essentially bounded density satisfying

`boxed:
 ||p_Q||_infinity
 <= C_3,new |det M|^(-1/3),
 C_3,new=6(2+2pi)=12(1+pi)
          =49.69911184307752... .}`

Consequently, in an arbitrary ambient quadratic form, any ORIGINAL-coordinate principal triple `S` with `det A[S,S]!=0` gives the identical conditional bound

`boxed:
 ||p_(X^TAX)||_infinity
 <=12(1+pi)|det A[S,S]|^(-1/3).}`

### 3.1 Generic physical-pair pivot

First suppose some physical principal pair is invertible. Permute coordinates so

`M=[[P,r],[r^T,d]]`,

where `P` is invertible symmetric `2x2`. Put

`D=|det P|`,
`s=d-r^T P^(-1)r=det M/det P`.

Because `M` is invertible, `s!=0`.

Writing `u=(X_1,X_2)` and `z=X_3`, complete only the physical pair. All affine terms are retained exactly:

`Q=(u+h(z))^T P(u+h(z)) + s(z+z_0)^2+c_0`,

for deterministic affine `h(z)` and constants `z_0,c_0` depending on `M,ell,c`.

Condition on the ORIGINAL scalar `Z=z`. The two active variables remain independent cap-one variables. The completed account01/B03 pair theorem applies uniformly in the translation `h(z)`, hence for a.e. target value `y`,

`p_(Q|Z=z)(y)
 <= C_pair D^(-1/3)
    |y-[s(z+z_0)^2+c_0]|^(-1/3).`

Average over `Z` and use Lemma 2:

`p_Q(y)
 <=6 C_pair D^(-1/3)|s|^(-1/3)`

`=6 C_pair |det M|^(-1/3)`.

The physical-pair determinant cancels **exactly** before any reciprocal local scale is paid. This gives the claimed constant `12(1+pi)`.

### 3.2 Singular-pair edge case by coefficient perturbation

An invertible symmetric `3x3` matrix need not possess an invertible principal `2x2` pair; for example the stress matrix in Section 6 has all three principal pair determinants equal to zero. This cannot be ignored.

For arbitrary invertible `M`, choose a sequence `eps_k->0` avoiding the finitely many roots for which either `det(M+eps_k I)=0` or the selected principal-pair determinant vanishes. Put

`M_k=M+eps_k I`.

For every `k`, the generic-pair argument gives a density cap

`||p_(Q_k)||_infinity
 <=12(1+pi)|det M_k|^(-1/3)`,

where

`Q_k=X^T M_k X+2ell^T X+c`.

Every real-valued coordinate is finite almost surely, so `Q_k->Q` almost surely and hence weakly. For every nonnegative compactly supported continuous test function `phi`,

`int phi d law(Q)
 =lim_k int phi d law(Q_k)
 <=lim_k 12(1+pi)|det M_k|^(-1/3) int phi dx`

`=12(1+pi)|det M|^(-1/3) int phi dx`.

Therefore `law(Q)` is dominated by that constant times Lebesgue measure, proving absolute continuity and the same essential density cap. No moment or dominated-convergence hypothesis is needed.

### 3.3 Comparison with the existing theorem

The prior determinant-only coefficient was

`C_3,old=16*2^(1/4)*sqrt(30)=104.21688998922089...`.

The new coefficient is

`C_3,new=49.69911184307752...`,

so

`C_3,new/C_3,old=0.4768815481657328...`.

The gain comes from matching the pair envelope's `D^(-1/3)` homogeneity directly with the scalar Schur square's one-third Riesz cost `|s|^(-1/3)`. No threshold split between a large diagonal and a large off-diagonal coefficient is needed.

## 4. Fresh exact-rank-three overlap-two branch is now fully paid

The newest account04/B03 r4 Plucker theorem treats exact-rank-three matrices

`A=U Lambda U^T`, `Delta=|det Lambda|`,

and normalized overlap-two mass

`eta=E_2(A)/Delta^2`.

On the live sector `eta>=1/4`, it proves the dimension-free dichotomy

`either max_H J_2(H)>=E_2(A)^2/(18 Delta^2),`

`or max_(|S|=3)|det A[S,S]|>E_2(A)/(6Delta).`

For a target matrix with exactly three nonzero eigenvalues, all of modulus at least one, `Delta>=1`.

### Pair-star branch

If the first alternative fires, then

`J_2(H)>=1/288`.

The completed account01/B03 local overlap-two compiler gives

`||p_Q||_infinity
 <=129.924435862525374 * 288^(1/6)
 =333.879371828014... .`

### Dominant Plucker atom branch

The second alternative gives a physical principal triple with

`|det A[S,S]|>Delta/24>=1/24`.

The new theorem now gives, **without any spectral-anisotropy gate**,

`boxed:
 ||p_Q||_infinity
 <12(1+pi) 24^(1/3)
 =143.35704540067675... .}`

Therefore the whole exact-rank-three normalized overlap-two sector

`eta=E_2(A)/Delta^2>=1/4`

is paid by the universal bound

`boxed: ||p_Q||_infinity <333.880.}`

This removes precisely the unbounded-anisotropy debt left open in account04/B03 r4. It does **not** solve full QFORM or the other global overlap sectors.

## 5. Required designated-partner use: account04/B04

The newest completed designated partner result remains account04/B04 r2. On its double-anchor fourth-volume branch, a literal physical row pair `{a,b}` satisfies canonical pair inclusion mass

`eta_ab>2/75`.

Its exact pair packet is

`H_ab^(4)=eta_ab E_4(M)>(2/75)E_4(M)`.

Applying the completed account03/B04 pair-anchored E3 downshift at the actual inequality

`K_ab^2 >= 2 D_2 H_ab^(4) > (4/75)D_2E_4(M)`

gives

`boxed:
 ||p_Q||_infinity
 <6.824377206888847 [D_2E_4(M)]^(-1/12).}`

That branch has a continuous `C_0` density. This partner application is retained as an actual equation-level receiver; the new triple theorem above is a separate essential-boundedness mechanism.

## 6. Genuinely rotated indefinite stress matrix

Consider the physical `3x3` matrix

`B_*=[[1,1,1],
      [1,1,-1],
      [1,-1,1]].`

Every coefficient is nonzero. Direct algebra gives

`det B_*=-4`,
`spec(B_*)={2,2,-1}`.

Thus it is indefinite and satisfies the exact owner hypothesis with all three eigenvalues of modulus at least one. Yet every physical principal `2x2` determinant is **exactly zero**:

`det [[1,1],[1,1]]=0`,
`det [[1,1],[1,1]]=0`,
`det [[1,-1],[-1,1]]=0`.

So this matrix genuinely tests the perturbative edge case rather than the generic pair-pivot algebra.

For every admissible product input law, the new theorem gives

`boxed:
 ||p_(X^T B_* X)||_infinity
 <=12(1+pi) 4^(-1/3)
 =31.308478586086476... .}`

The previous determinant-only theorem gives about `65.65` on the same matrix. No Monte Carlo argument is used.

## 7. What remains

Full QFORM remains **OPEN**. Full-target continuity remains **OPEN** separately. This run settles a fresh structural debt only in the exact-rank-three overlap-two sector and improves the general physical-triple determinant receiver.

The next nonduplicate B04 implication is:

`QFORM-GENERALRANK-E2-AGGREGATE-TO-TRIPLEDET-OR-PAIRJ2-v1`:

replace the exact-rank-three Plucker rank-one factorization by a cancellation-safe positive/product-space decomposition for general rank, so that target-scale aggregate overlap-two mass produces either (i) a target-scale localized `J_2(H)`, already paid by account01/B03, or (ii) a target-scale physical principal triple determinant, now paid at coefficient `12(1+pi)`, without selecting from a dimension-growing unstructured sum.

Continuity should continue to be tracked independently: the new determinant-only receiver establishes essential boundedness but does not supply an `L^1` characteristic function.

## 8. Source pins

- owner/control read at the start from `yspennstate/math-research-brain@41dd3a35aa3ff248288ba0f08c7614ba11b5fd37`; later prepublication refresh recorded separately.
- prior physical-triple theorem: `proofnet24/QFORM-density/fleet-2026-09-22/account01/B06/20260923T130129Z-account01-B06-QFORM/ADDENDUM_TRIPLE_DET.md` (read on current master).
- determinant-only physical-pair envelope: `proofnet24/QFORM-density/fleet-2026-09-22/account01/B03/20260924T041651Z-account01-B03-QFORM-r40/REPORT.md`.
- local overlap-two compiler: account01/B03 r41, canonical theorem commit `7dc6d6841e318a88174fb41ddaa1c88e223aacf4` as source-pinned by account04/B03.
- fresh exact-rank-three Plucker localization: `proofnet24/QFORM-density/fleet-2026-09-22/account04/B03/20260924T051411Z-account04-B03-plucker-overlap2-r4/REPORT.md`.
- designated partner: account04/B04 r2, `yspennstate/math-open-problems@4a54666abf2316bb79b939cef3ea940605a0af57`, `proofnet24/QFORM-density/fleet-2026-09-22/account04/B04/20260924T001353Z-account04-B04-QFORM-r2/REPORT.md`.

No schedule, task identity, email/push notification, repository visibility, paid API/model, public-release, or cross-account-authentication state was changed.
