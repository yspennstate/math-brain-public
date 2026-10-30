SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet02, slot B20, 2026-09-24T04:37:14Z.
attacking: the r44/r46 global rank-two separator by locating the third target spectral resource with signed Weyl bookkeeping, then strengthening the genuinely two-cross-mode survivor by an E3 tail gate.

# fleet02/B20 r45 — signed spectral peel for the global rank-two separator

Programme: `QFORM-DENSITY-3EIG-20260922`  
Status: **ESSENTIAL STEP APPLIED / SIGNATURE-ROUTED GLOBAL R2 SEPARATOR / STRONG-R2 TAIL TIGHTENED / FULL QFORM OPEN**.  
Execution: `WITHOUT_VERIFIED_BRAIN` (authenticated repository retrieval occurred; no actual native learned-memory receiver ingestion was exposed).

The owner target is unchanged: for every dimension, every independent real product input with coordinate densities bounded by one, and every real symmetric coefficient matrix with at least three eigenvalues of modulus at least one, prove one universal finite essential density bound for `X^T A X`, or give a valid counterexample. No Gaussian/log-concave/moment/support hypothesis, no post-rotation independence, no arbitrary-joint coarea bound, no worst-fibre supremum, and no deletion of a small coefficient tail is used below. Continuity remains separate.

## 1. Fresh source-pinned inputs

The newest compatible designated partner is fleet03/B20 r46 at

`yspennstate/math-open-problems@9ae7023224386e95ab2bd7f088347db8750c7b06`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B20/20260924T034736Z-fleet03-B20-QFORM-auto11-r46/REPORT.md`.

Its strong-carrier chamber starts from disjoint ORIGINAL-coordinate banks `R,C` with

    N=A[R,C],
    dist_F(N,rank<=2)<2^-16,
    s2(N)>=1/64,
    s1(N)s2(N)>28159/(4194304 sqrt(2)).

Its heavy second-singular-vector alternative gives one literal original coordinate `j` with

    ||A[R,j]||_2 >= 1/128                                      (1.1)

(or the transpose-symmetric version). Its proved one-singular E3 inequality is

    E3(M) >= (1/3) s1(M)^2 dist_F(M,rank<=2)^4                 (1.2)

for every real matrix `M`, and it uses the completed full-ambient physical-E3 receiver

    ||p_Q||_infinity <= C_E3 E3(M)^(-1/6),
    C_E3=8.4530212255281768747049... .                          (1.3)

The preceding fleet02/B20 r44 globalized the heavy arm. With

    O=(R union C)^c,
    L=R union (C\{j}),
    J={j} union O,
    W=A[L,J],                                                   (1.4)

`L|J` is a partition of ALL original coordinates and

    s1(W)>=1/128.                                               (1.5)

Unless the full law is already paid by `<13098`, r44 gives

    dist_F(W,rank<=2)<2^-12.                                   (1.6)

The required owner-pinned source

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`

`proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/`

was read through `RESULTS.md`, `FOURIER_ROUTE_REPORT.md`, and `COUNTEREXAMPLE_SEARCH.md`. Its unrestricted D5 theorem says for every literal physical cross block `M`, with no volume-marginal hypothesis,

    ||p_Q||_infinity <= 5 sqrt(2e) e5(M^T M)^(-1/10).           (1.7)

Applied to the actual global `W` in (1.4),

    e5(W^T W)>=1/1024
       => ||p_Q||_infinity <=10 sqrt(2e)<23.317.                (1.8)

Hence every still-unpaid heavy-arm state may retain the exact additional gate

    e5(W^T W)<1/1024.                                          (1.9)

This is an equation-level use of the required pinned source on the current frontier.

## 2. New theorem: signed spectral peel across any physical cut

Let a real symmetric matrix be written in an ORIGINAL-coordinate partition `L|J` as

    A = [[B,W],[W^T,C]],
    D = diag(B,C).                                              (2.1)

Write the singular values of `W` as

    s1>=s2>=...>=0.                                             (2.2)

Let

    p = #{eigenvalues of A >= 1},
    q = #{eigenvalues of A <= -1}.                              (2.3)

Thus the owner target says `p+q>=3`.

### Theorem 2.1 — `QFORM-CROSS-SVD-SIGNATURE-PEEL-v1`

For every integer `r>=0`, put `sigma=s_{r+1}(W)` (zero if the index is beyond the rank). Then the block-diagonal physical matrix `D` has

    at least max(p-r,0) eigenvalues >= 1-sigma,                 (2.4)

and

    at least max(q-r,0) eigenvalues <= -(1-sigma).              (2.5)

No random-variable rotation occurs in this statement. It is deterministic coefficient geometry, and `D` is literally the direct sum of the two original-coordinate principal blocks.

### Proof

Take an SVD

    W=sum_i s_i u_i v_i^T

and truncate it after `r` terms:

    W_r=sum_{i<=r}s_i u_i v_i^T.

Let

    K_r=[[0,W_r],[W_r^T,0]].                                   (2.6)

The nonzero eigenvalues of `K_r` are exactly

    +s1,...,+sr,-sr,...,-s1,                                   (2.7)

so its `(r+1)`-st largest eigenvalue is zero. Put

    R=A-K_r.

Weyl's eigenvalue inequality gives, for every `k` with `k+r<=n`,

    lambda_{k+r}(A)
       <= lambda_k(R)+lambda_{r+1}(K_r)
       =  lambda_k(R).                                         (2.8)

If `k<=p-r`, the left side is at least one, hence

    lambda_k(R)>=1.                                            (2.9)

Apply the same argument to `-A=(-R)+(-K_r)`. Since `-K_r` has the same positive eigenvalues `s1,...,sr`, `-R` has at least `max(q-r,0)` eigenvalues at least one. Equivalently, `R` has at least that many eigenvalues at most `-1`.

Finally

    R=D+E_r,
    E_r=[[0,W-W_r],[(W-W_r)^T,0]],                              (2.10)

and

    ||E_r||_op=s_{r+1}(W)=sigma.                               (2.11)

A final Weyl perturbation from `R` to `D` gives (2.4)-(2.5). QED.

### Immediate target corollary (`r=1`)

For every physical cut,

    s2(W)<theta<1                                               (2.12)

forces `D` to contain at least `p-1` positive eigenvalues `>=1-theta` and at least `q-1` negative eigenvalues `<=-(1-theta)`. Since `p+q>=3`, at least one actual same-side principal-block spectral resource of modulus `>=1-theta` survives. If the three target eigenvalues have the same sign, at least two same-side resources survive.

The cruder but useful scalar consequence is

    s3(A) <= max{||B||op,||C||op}+s2(W).                        (2.13)

Indeed it is also obtained by taking the best rank-one crossing mode, whose symmetric extension has rank two.

## 3. Apply the theorem to the live r46/r44 global separator

Take `W` from (1.4), and choose the fixed threshold

    theta=1/2.                                                  (3.1)

There are now two exhaustive possibilities.

### Branch S: side-spectrum branch

If

    s2(W)<1/2,                                                  (3.2)

Theorem 2.1 with `r=1` says the literal block-diagonal matrix

    D=diag(A[L,L],A[J,J])                                      (3.3)

contains at least `p-1` eigenvalues `>=1/2` and at least `q-1` eigenvalues `<=-1/2`. In particular it contains at least one eigenvalue of modulus `>=1/2`; if `(p,q)` is `(3,0)` or `(0,3)`, it contains at least two with the target sign.

This identifies the missing third resource without asserting that its spectral coordinate is an independent random variable. Because `D` is block diagonal, every such resource lies in one of the two ORIGINAL source-side principal blocks.

### Branch C: genuine two-cross-mode branch

If

    s2(W)>=1/2,                                                 (3.4)

then automatically

    s1(W)>=s2(W)>=1/2.                                         (3.5)

Thus r44's weak arm lower bound `1/128` upgrades, on this branch, to two order-one singular directions of the GLOBAL physical cut. The remaining nonzero cross tail is still present.

We can now tighten that tail substantially using the already-completed E3 receiver.

Let

    T2=sum_{i>=3}s_i(W)^2
      =dist_F(W,rank<=2)^2.                                    (3.6)

By the definition of the third elementary symmetric polynomial in the squared singular values,

    E3(W)
      >= s1(W)^2 s2(W)^2 T2
      >= (1/16) T2.                                            (3.7)

Therefore, if

    dist_F(W,rank<=2)>=2^-16,                                  (3.8)

then

    E3(W)>=2^-36.                                              (3.9)

The physical-E3 receiver (1.3) applies to this ACTUAL global cut and gives

    ||p_Q||_infinity
       <= C_E3 (2^-36)^(-1/6)
       =64 C_E3
       =540.9933584338033...
       <541.                                                    (3.10)

Hence every still-unpaid Branch C state satisfies the stronger tube

    boxed:
    s1(W)>=1/2,
    s2(W)>=1/2,
    dist_F(W,rank<=2)<2^-16,
    e5(W^T W)<1/1024.                                          (3.11)

This is strictly sharper than r44's `2^-12` global rank-two tube on the genuinely two-mode branch. Crucially, (3.11) is a coefficient statement only: the tail `W-W_2` remains in the random quadratic form and is not discarded.

## 4. Sharpness / obstruction checks inside the exact target

The signed peel cannot force the side-spectrum branch universally.

Take two two-dimensional original banks and

    A_cross=[[0,I_2],[I_2,0]].                                 (4.1)

Then

    spec(A_cross)={1,1,-1,-1},                                 (4.2)

so the owner target holds strongly, while `D=0` and `s2(W)=1`. Thus all target spectrum can genuinely be carried by two crossing singular directions. This is Branch C, not Branch S.

Conversely the count in Theorem 2.1 is sharp. Let `L` have dimension three, `J` dimension one, take

    D=diag(1,1,0,0),
    W=s e_3 f^T,
    s>=1.                                                       (4.3)

Then

    spec(A)={s,1,1,-s},                                        (4.4)

so `(p,q)=(3,1)`, while `s2(W)=0`; `D` has exactly the `p-1=2` positive unit eigenvalues guaranteed by the theorem and no stronger universal count follows.

Neither construction is a QFORM counterexample. Both are finite-dimensional full-rank target matrices (for `s>=1` in (4.3)); the pinned `COUNTEREXAMPLE_SEARCH.md` Theorem A supplies a finite universal bound at fixed `n=4` and spectral scale one. Their purpose is only to show that the two branches of the new resource-routing theorem are genuinely necessary.

A second, analytic warning comes from the fresh fleet02/B19 curved-rank-two stress family: a fixed-strength rank-two physical crossing with aligned arbitrary same-bank curvature can have an **unbounded two-bank partial density**, even though the full target law is bounded after a genuine third source is spent jointly. Therefore Branch C cannot be closed by first scalarizing the curved two-bank core and then convolving a third source; the third target resource must remain inside the smoothing argument.

## 5. Strongest source-pinned conditional closure after this run

The r46 heavy-arm branch is no longer merely

    `one arm + global rank-two tube`.

It is now exhausted by the following source-preserving funnel:

1. **Paid physical-volume exits.** If the strengthened E3 tail gate (3.8) fires, the full ambient law is continuously bounded by `<541`. If the pinned D5 gate (1.8) fires, it is continuously bounded by `<23.317`.

2. **Strong global two-mode survivor.** Otherwise (3.11) holds: a literal partition of all original coordinates has two singular values at least `1/2`, rank-two Frobenius tail below `2^-16`, and fifth volume below `1/1024`. Arbitrary same-side quadratic blocks remain untouched.

3. **Side-spectrum survivor.** If `s2(W)<1/2`, then the literal principal blocks on the two source sides collectively retain `p-1` positive target modes at scale `1/2` and `q-1` negative target modes at scale `1/2`; at least one such mode always exists, and two exist in the same-sign-three case.

The fully diffuse r46 alternative remains separately source-pinned as

    A[H,H]=diag(A_1,A_2,A_3,A_4)+K+E_H,
    rank K<=12,
    ||E_H||op<33/131072,                                       (5.1)

with arbitrary same-bank blocks retained and all three balanced cuts rank-two thin unless already paid by E3.

Accordingly the first current unpaid implication is sharpened to

`QFORM-R46-STRONG-R2-OR-SIDEBLOCK-SIGNATURE-OR-FOURBANK-R12-JOINT-PAYMENT-v1`:

> Under the full original cap-one product hypotheses and target spectrum, pay either the global strong two-cross-mode tube (3.11), the side-spectrum branch (3.2)-(3.3) with its signed retained principal-block resources, or the r46 four-bank rank-at-most-twelve carrier (5.1), while retaining all same-bank curvature and nonzero tails. In Branch C the third resource must be spent jointly rather than after a two-bank density supremum.

This is a real reduction of the first unpaid edge: the former global separator branch has been split by a sharp signed spectral identity, and its genuinely two-mode half has a four-orders-of-two tighter Frobenius tail (`2^-16` rather than `2^-12`) at the explicit universal payment cost `<541`.

## 6. Status and correction guard

The unrestricted QFORM conjecture remains **OPEN / NOT PROVED / NOT DISPROVED**. No valid counterexample to the owner target was found. Full-target continuity remains separately OPEN.

The proof uses no law-uniform pointwise quadratic-phase decay, no fiber supremum, no conditional density-cap inheritance, no post-rotation independence, no arbitrary-joint coarea estimate, and no claim that an operator-small coefficient tail is a small random perturbation. SVD/eigenvectors occur only in deterministic coefficient algebra. All probabilistic receivers are applied on literal original-coordinate banks.
