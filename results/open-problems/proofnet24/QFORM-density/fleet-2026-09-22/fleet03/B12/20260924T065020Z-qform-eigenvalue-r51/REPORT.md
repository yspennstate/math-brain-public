SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet03, slot B12, 2026-09-24T06:50:20.972579Z.
attacking: transverse-angle spectral shielding: arbitrary signed added modes at a positive principal angle from a protected physical carrier cannot cancel its square energy; allow a finite-rank resonant packet and a small dense tail.

# fleet03/B12 — transverse-angle spectral shielding with a finite resonant budget

Programme: `QFORM-DENSITY-3EIG-20260922`  
Role: Additional eigenvalue control  
Run: `20260924T065020Z-qform-eigenvalue-r51`  
Status: **NEW SUPPORTING STABILITY THEOREM / FULL QFORM OPEN**  
Brain status: `WITHOUT_VERIFIED_BRAIN`

## 1. Scope and source boundary

The owner target remains open: for independent ORIGINAL coordinates with arbitrary scalar densities bounded by one and an arbitrary real symmetric matrix with at least three eigenvalues of absolute value at least one, prove a universal density bound or produce a valid counterexample. No Gaussianity, log-concavity, moment, compact-support, connected-support, iid, diagonal-basis, or post-rotation independence assumption is used below.

This run changes mechanism from the recent relative-resonance/destructive-projection sequence. The new quantity is an **angle between deterministic carrier-action subspaces**, not a norm of the added matrix and not an independence claim about the added quadratic form.

Source-valid inputs actually used:

1. fleet04/B12 r8, `yspennstate/math-open-problems@bcb9fd2641440a89d6e4967781d755618e163001`, `proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B12/20260924T002154Z-fleet04-B12-multihub-shear-r8/REPORT.md`. For an ORIGINAL-coordinate carrier `H`, its multidimensional hub shear theorem gives

   `s_(p+ell)(P_H A_*) >= gamma(||Lambda^(-1)W^T||) min{s_p(Lambda),s_ell(R)}`,

   with `gamma(t)=(sqrt(t^2+4)-t)/2`.

2. fleet03/B12 r47, `yspennstate/math-open-problems@7fa8e2a00f932cb7ed6e68da9dbd07725c24d0f1`, `proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B12/20260924T031535Z-qform-eigenvalue-r47/REPORT.md`. If an `m>=5` ORIGINAL-coordinate carrier satisfies

   `lambda_5((A^2)[H,H]) >= g^2>0`,

   then

   `||p_(X^T A X)||_infinity <= sqrt(24*pi*m+K_3^2)/g`,

   `K_3=3*2^(4/3)*exp(1/3)=10.550168831164775...`,

   and the output density has a representative in `C_0(R)`.

The current correction inbox was consumed. In particular, no arbitrary-joint coarea gate, conditional-density cap/moment gate, pointwise quadratic van-der-Corput decay, bounded-diameter localization, or treatment of a coefficient tail as an independent random convolution factor is used.

## 2. One-packet angle shield

Let `H` be `m` ORIGINAL coordinates and let

`P:R^m -> R^n`

be their coordinate embedding. Let `A_*` be symmetric and put

`M=A_* P`.

Assume `M` has full column rank and

`g=s_m(M)>0`.

Let `G=G^T` be an arbitrary signed addition. No bound is imposed on `rank(G)`, `||G||`, its eigenvalue signs, or their magnitudes. Put

`N=G P`,

let `Pi_M` and `Pi_N` be the orthogonal projections onto `Ran(M)` and `Ran(N)`, and define the carrier-action coherence

`c = ||Pi_M Pi_N||_op in [0,1]`.

### Theorem 2.1 — `QFORM-TRANSVERSE-ANGLE-SHIELD-v1`

If `c<1`, then

`boxed: s_m((A_*+G)P) >= g sqrt(1-c^2).`                 (2.1)

Equivalently,

`boxed: lambda_m(((A_*+G)^2)[H,H]) >= g^2(1-c^2).`       (2.2)

This is completely magnitude-free in the added spectrum.

### Proof

Fix `x in R^m`. Set

`u=Mx in Ran(M)`, `v=Nx in Ran(N)`.

By the definition of principal-subspace coherence,

`|<u,v>| <= c ||u|| ||v||`.

Therefore

`||(M+N)x||^2`
` = ||u||^2+||v||^2+2<u,v>`
` >= ||u||^2+||v||^2-2c||u||||v||`
` = (||v||-c||u||)^2 + (1-c^2)||u||^2`
` >= (1-c^2)g^2||x||^2`.

Taking the infimum over unit `x` proves (2.1). Since `A_*+G` is symmetric,

`((A_*+G)P)^T((A_*+G)P)=P^T(A_*+G)^2P`,

which is exactly the ORIGINAL-coordinate compression `((A_*+G)^2)[H,H]`; hence (2.2). QED.

### Sharpness

The factor `sqrt(1-c^2)` is sharp even for a symmetric addition. Take `m=1,n=2`, `P=e_1`,

`M=g e_1`,

`w=c e_1+sqrt(1-c^2)e_2`,

and choose a symmetric `G` with first column

`G e_1=-gc w`;

for example

`G=[[-gc^2,-gc sqrt(1-c^2)],[-gc sqrt(1-c^2),0]]`.

Then `Ran(GP)=span(w)` has coherence `c` with `Ran(M)`, while

`||(M+GP)|| = g sqrt(1-c^2)`.

At the endpoint `c=1`, no positive norm-free stability statement is possible: taking `G=-A_*` cancels the carrier exactly. Thus the angle obstruction is genuine rather than a proof artifact.

## 3. Spectral interpretation: arbitrary eigenvalues of either sign

Write an arbitrary symmetric packet spectrally as

`G=sum_a theta_a v_a v_a^T`.

Then

`GP=sum_a theta_a v_a(P^T v_a)^T`,

so

`Ran(GP) subset span{v_a : P^T v_a != 0}`.                 (3.1)

Consequently, if all eigenvectors of the added packet that actually touch the physical carrier lie in a global subspace `S` satisfying

`||Pi_(Ran M) Pi_S||_op <= c<1`,                           (3.2)

then (2.1) holds **for arbitrary values of every `theta_a`**. There may be arbitrarily many positive or negative eigenvalues, arbitrarily small or arbitrarily large, and arbitrary multiplicities inside `S`. Their magnitudes never enter the estimate.

This is the requested dependence-safe additional-eigenvalue control: the entire signed packet stays inside the final quadratic form. The theorem is only a deterministic coefficient inequality; it never asserts that `X^T G X` is independent of the baseline quadratic form.

## 4. Add a completely uncontrolled resonant packet and a dense local tail

The angle shield remains useful even when finitely many carrier directions are allowed to be totally hostile.

Let

`A=A_*+G+R+T`,

where all four matrices are real symmetric. Assume:

- `g=s_m(A_*P)>0`;
- with `S=Ran(GP)`, the coherence `c=||Pi_(Ran(A_*P)) Pi_S||_op<1`;
- `rank(RP)<=q` (in particular, `rank R<=q` is sufficient), with no bound on the size or signs of `R`;
- `epsilon=||TP||_op`, with no restriction on the complement-only action of `T`.

### Theorem 4.1 — `QFORM-ANGLE-SHIELD-RANK-TAIL-STABILITY-v1`

For every `k` with `k+q<=m`,

`boxed:
 sqrt(lambda_k((A^2)[H,H]))
 = s_k(AP)
 >= [g sqrt(1-c^2)-epsilon]_+ .`                        (4.1)

### Proof

Set

`X=(A_*+G)P`.

Theorem 2.1 gives

`s_m(X)>=g sqrt(1-c^2)`,

so every singular value of `X` is at least this quantity. Put `Y=RP`. Since `rank(Y)<=q`, apply the standard singular-value rank interlacing to

`X=(X+Y)-Y`:

`s_(k+q)(X) <= s_k(X+Y)+s_(q+1)(Y)=s_k(X+Y)`.

Therefore

`s_k((A_*+G+R)P)>=g sqrt(1-c^2)`.

Finally singular-value Weyl for the local tail `TP` gives

`s_k(AP)>=s_k((A_*+G+R)P)-||TP||_op`,

which proves (4.1). QED.

### Five-mode density corollary

If `m>=5`, `q<=m-5`, and

`g_5=g sqrt(1-c^2)-epsilon>0`,                         (4.2)

then (4.1) at `k=5` gives

`lambda_5((A^2)[H,H])>=g_5^2`.

The completed five-square-mode compiler therefore yields

`boxed:
 ||p_(X^T A X)||_infinity
 <= sqrt(24*pi*m+K_3^2)/g_5.`                          (4.3)

Moreover the density is continuous and vanishes at infinity.

Thus an `m`-coordinate protected carrier tolerates simultaneously:

- an unlimited-rank packet `G` with completely arbitrary signed eigenvalue magnitudes, provided its carrier-action image stays at a positive principal angle from the protected carrier image;
- `m-5` completely uncontrolled resonant carrier directions through `R`;
- a fully nonseparable dense remainder `T`, charged only by its deterministic local action `||TP||`;
- arbitrary complement spectrum and couplings not seen by `TP`.

No random remainder is discarded and no eigen-coordinate independence is invoked.

## 5. Required fleet04/B12 equation-level application

Use the completed fleet04/B12 r8 multihub theorem. Take an ORIGINAL carrier `H` of size

`m=11`,

with hub dimension `p=2` and transverse dimension `ell=9`. Assume its final aligned-packet aggregates satisfy

`s_2(Lambda)>=4`,

`s_9(R)>=2`,

`||Lambda^(-1)W^T||_op<=1`.

The partner inequality gives, at an actual equation,

`s_11(P_H A_*)`
` >= gamma(1) min{4,2}`
` = ((sqrt(5)-1)/2)*2`
` = sqrt(5)-1`
` = 1.2360679774997898... .`                              (5.1)

Transpose symmetry gives the same lower bound for

`M=A_*P_H^T`.

Now add three further signed pieces:

1. `G`, of arbitrary rank and arbitrary eigenvalue signs/magnitudes, satisfying only

   `||Pi_(Ran M) Pi_(Ran(GP_H^T))||_op <= 1/2`;             (5.2)

2. `R_0`, any symmetric packet with

   `rank(R_0 P_H^T)<=6`,                                    (5.3)

   again with unrestricted signs and magnitude;

3. `T`, any symmetric dense addition satisfying only

   `||T P_H^T||_op<=1/20`.                                  (5.4)

Theorem 4.1 with `k=5,q=6,c=1/2` gives

`sqrt(lambda_5((A^2)[H,H]))`
` >= (sqrt(5)-1)*sqrt(3)/2 - 1/20`
` = 1.0204662693192699... >1.`                              (5.5)

This is an actual final-matrix square-energy statement. In particular `s_5(A)>1`, so the family lies inside the owner target class.

Applying (4.3) with `m=11` gives

`boxed:
 ||p_Q||_infinity
 <= sqrt(264*pi+K_3^2) /
    ((sqrt(5)-1)*sqrt(3)/2-1/20)
 = 30.0554895996032... <30.056.`                             (5.6)

The density has a representative in `C_0(R)`.

This application is materially different from the preceding B12 relative-resonance results. Here the unlimited-rank packet `G` may have arbitrarily large action **partly overlapping** the protected image; no small relative map or small destructive-projection norm is assumed. Only the principal angle is charged. Six additional resonant directions may then be completely uncontrolled, and a dense local tail remains.

## 6. Deterministic computation

A seeded checker tested 10,000 random rectangular carrier problems with `n=30,m=11`.

For each instance it constructed:

- a full-column-rank baseline `M`;
- an arbitrary-scale packet `N_G` whose range had a prescribed coherence `c in [0,0.8]` with `Ran(M)`;
- a rank-`q` hostile packet with `0<=q<=6` and arbitrary scale;
- a dense tail normalized to a known operator norm `epsilon<=0.08`.

It checked both

`s_m(M+N_G)>=s_m(M)sqrt(1-c^2)`

and

`s_5(M+N_G+N_R+N_T)>=s_m(M)sqrt(1-c^2)-epsilon`.

There were zero violations. The minimum observed angle-only margin was

`0.002592818226651805`,

and the minimum observed rank-tail margin was

`0.3050693301679356`.

The same checker includes the exact two-dimensional sharpness example with `c=0.6,g=2`, for which both sides equal `1.6` to machine precision. These computations are sanity checks only; the proof is the elementary principal-angle inequality plus singular-value interlacing.

## 7. Exact remaining gap

The full conjecture remains **OPEN / NOT PROVED / NOT DISPROVED**.

The present result removes a large class of arbitrary smaller and larger signed eigenvalues from the obstruction list: eigenmodes whose physical carrier action is uniformly transverse to a protected image are harmless regardless of magnitude, and finitely many resonant directions can be spent as a rank budget.

What is still missing from the bare hypothesis `s_3(A)>=1` is a structural extraction theorem. One must force either:

1. a bounded ORIGINAL-coordinate carrier with five protected square-energy modes after spending the resonant directions and transverse-angle packet above; or
2. enough failure of transversality/reserve to create one of the already-paid physical pair, projected-crossing, grouped-bank, ridge, hub/common-plane, Schur, or Pluecker-volume exits.

Exact cancellation at coherence one shows why some resonance/alignment statistic is unavoidable in any fixed-carrier stability theorem. This is not a counterexample to QFORM; it identifies the geometric obstruction that a full proof must route elsewhere.
