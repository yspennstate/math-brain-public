SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet02, slot B06, 2026-09-24T05:26:46Z.
attacking: `QFORM-P1-OR-HUBDEGENERATE-MIXED-LAYER-COMPILER-v1`; aggregate the complete P1 one-tail/two-hub mixed-minor bank before any reciprocal physical-pair payment, then distinguish a genuine product-preserving pair receiver from a localized three-hub exit.

# fleet02/B06 r13 — P1 mixed-minor aggregation and triple-or-pair compiler

Programme: `QFORM-DENSITY-3EIG-20260922`  
Owner control at start: revision `2026-09-22.15`  
Assignment: Curved fiber integration / complementary constructions and source-valid counterexamples  
Designated partner used: fleet03/B06 r53, `yspennstate/math-open-problems@1ae51010a6c1eca20e0897902d67f9c169ad7997`  
Required pinned source used: `yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`, `RESULTS.md`, `FOURIER_ROUTE_REPORT.md`, `COUNTEREXAMPLE_SEARCH.md`  
Status: **NEW SUPPORTING THEOREM + TARGET-LEVEL CONDITIONAL PAYMENT + SOURCE-VALID STRUCTURAL COUNTEREXAMPLE / FULL QFORM OPEN**  
Execution: **WITHOUT_VERIFIED_BRAIN**

The unrestricted conjecture remains OPEN / NOT PROVED / NOT DISPROVED. No moment, support, Gaussian, log-concavity, iid, diagonal-basis, post-rotation independence, arbitrary-joint coarea cap, worst conditional-density supremum, or unrestricted curved-fiber supremum is used. Continuity is separate and is not asserted by the pair wrapper below.

## 1. Exact debt inherited from the designated partner

The newest designated partner fleet03/B06 r53 works in the literal three-hub normal form inherited from r52,

`A = F^T B F + D,        F=[I_3,Z],`                              (1.1)

where `B=B^T` is invertible, `Z` is `3 x m`, and `D` is an arbitrary diagonal matrix in the ORIGINAL coordinates. Put

`beta=det B`, `G=ZZ^T`, `K=B+D_H`,                               (1.2)

where `D_H` is the diagonal perturbation on the three physical hub coordinates. Partner r53/r52 uses the complete rank-three volume layers

`P_0=|beta|`, `P_1=|beta| e_1(G)`, `P_2=|beta| e_2(G)`, `P_3=|beta| det G`,
`P=P_0+P_1+P_2+P_3`,                                             (1.3)

and in the live low-Pluecker-disjoint branch proves

`max(P_0,P_1,P_2)>5P/16`.                                       (1.4)

r53 pays the P2 layer by aggregating every two-tail/one-hub mixed 3x3 minor before taking a scalar-pivot reciprocal. Its first remaining debt explicitly includes the P1-large branch and finite three-hub degenerations.

This run derives the exact P1 analogue and shows that its correct physical compiler is **localized triple OR two-hub pair**, not two-hub pair alone.

## 2. Complete P1 one-tail/two-hub mixed-minor identity

For each tail column `z_p` of `Z` and each hub `h in H={1,2,3}`, let `R_h(p)` be the oriented mixed 3x3 minor obtained by keeping the two hub columns in `H\{h}` and inserting tail column `p`. Equivalently, up to the fixed sign caused by restoring the natural column order,

`R_h(p)=det( K with column h replaced by B z_p )`.                (2.1)

Define

`N=B^{-1}K`.                                                     (2.2)

Because `B,K` are symmetric, `N=(K B^{-1})^T`, so `N` has exactly the same singular values as partner r53's matrix `M=K B^{-1}`.

### Theorem 2.1 — `QFORM-P1-MIXED-CROSSMINOR-AGGREGATE-v1`

For every tail column,

`boxed: R(p)=beta adj(N) z_p,`                                   (2.3)

where `R(p)=(R_1(p),R_2(p),R_3(p))^T`. Consequently the complete P1 mixed-minor energy is

`boxed:
 Lambda_1 := sum_p sum_h R_h(p)^2
           = beta^2 tr[ adj(N) G adj(N)^T ].`                    (2.4)

If `D_H=0`, then `N=I_3` and

`boxed: Lambda_1=beta^2 tr G = |beta| P_1.`                     (2.5)

Thus `P_1` is literally the complete one-tail/two-hub 3x3-minor energy before hub-diagonal cancellation, in exact parallel with r53's identity identifying P2 with the complete two-tail/one-hub bank.

### Proof

For any square matrix `K` and replacement vector `b`, the vector of determinants obtained by replacing column `h` of `K` by `b` is `adj(K)b`. Taking `b=Bz_p` gives

`R(p)=adj(K)Bz_p`.                                               (2.6)

Since `K=BN`, first suppose `N` invertible. Then

`adj(K)B
 = det(K)K^{-1}B
 = beta det(N) N^{-1}
 = beta adj(N).`                                                 (2.7)

Both sides of (2.7) are polynomial in the entries of `K`, so the identity extends to singular `N` by continuity/algebraic identity. This proves (2.3). Summing outer products `z_pz_p^T` gives `G`, hence

`sum_p |R(p)|^2
 =beta^2 sum_p z_p^T adj(N)^T adj(N)z_p
 =beta^2 tr[adj(N)Gadj(N)^T],`                                  (2.8)

which is (2.4). Equation (2.5) is immediate from `N=I`. QED.

This aggregation is exactly in the B06 spirit: no single favorable mixed minor is selected before the complete product-coordinate packet is summed.

## 3. Quantitative P1 survival unless the existing hub metric degenerates

Let

`mu=sigma_min(N)=sigma_min(KB^{-1}).`                            (3.1)

### Corollary 3.1 — `QFORM-P1-AGGREGATE-SURVIVAL-v1`

For every normal form (1.1),

`boxed: Lambda_1 >= |beta| mu^4 P_1.`                            (3.2)

Hence on the live partner branch `P_1>5P/16`,

`boxed: Lambda_1 > (5/16)|beta| mu^4 P.`                         (3.3)

### Proof

Let the singular values of `N` be `q_1>=q_2>=q_3=mu>=0`. For invertible `N`, the singular values of `adj(N)` are

`q_1q_2, q_1q_3, q_2q_3`,                                      (3.4)

so every singular value of `adj(N)` is at least `mu^2`. The same inequality remains true at `mu=0` trivially. Therefore

`tr[adj(N)Gadj(N)^T] >= mu^4 tr G`.                              (3.5)

Substitute (1.3) and (2.4):

`Lambda_1 >= beta^2 mu^4 trG
           = |beta| mu^4 P_1`.                                  (3.6)

This proves (3.2)-(3.3). QED.

This is the first useful compiler fact: **P1 cannot disappear through high-dimensional tail cancellation unless the same finite-dimensional hub metric `KB^{-1}` already degenerates.** Partner r53 had already isolated `mu ->0` as one of the P2 endpoint obstructions. No new dimension-dependent loss is created by the P1 layer.

## 4. Exact physical-pair meaning of each P1 row

Fix a hub `h` and put `J=H\{h}`. Let

`P_h=K[J,J]`                                                     (4.1)

be the literal original-coordinate 2x2 pair block. Suppose first that `P_h` is invertible. After exact completion of this physical pair, the Schur cross row from the remaining hub coordinate `h` to the complete tail bank is

`n_h=A[h,T]-A[h,J] P_h^{-1} A[J,T]`.                            (4.2)

### Lemma 4.1 — `QFORM-P1-PAIR-SCHUR-IDENTITY-v1`

For every tail column `p`,

`|R_h(p)|=|det P_h| |(n_h)_p|`,                                 (4.3)

and therefore

`boxed: ||R_h||_2=|det P_h| ||n_h||_2.`                          (4.4)

### Proof

Order the two columns indexed by `J` first and the tail column `p` last. The corresponding 3x3 mixed block has upper-left block `P_h`, so the scalar block determinant formula gives

`det = det(P_h) [A[h,p]-A[h,J]P_h^{-1}A[J,p]]`.                 (4.5)

The bracket is exactly `(n_h)_p`. Reordering columns back only changes sign. Summing squares proves (4.4). QED.

The key point is that the complete vector norm `||R_h||_2`, not an individual physical coefficient, is the invariant that survives the Schur completion.

## 5. Product-preserving pair payment and cancellation of the pair determinant

We now spend (4.4) through an actual bounded-density receiver.

The completed fleet03/B08 theorem `QFORM-RANK1-CROSSING-SQRT-SMALLBALL-v1`, source

`yspennstate/math-open-problems@cffe42e3fc7fd0745afa99d532a34428515d745e`,

states that an exact rank-one physical cross block of sole singular value `sigma>0` between two disjoint ORIGINAL-coordinate product banks, with arbitrary same-bank measurable functions retained, satisfies

`sup_s P(|R-s|<rho)
 <= H_1 sigma^(-1/2) sqrt(rho),`                                 (5.1)

where

`H_1=e^(1/2) 2^(1/4) Gamma(1/4)
   =7.108628442830306... .`                                      (5.2)

After completing an indefinite physical pair, the required pinned `e5f71d...` RESULTS package gives the pair-log receiver

`||p_Q||_infinity
 <=4 sqrt(2H) (|det P_h| sigma_min(P_h))^(-1/4)`                 (5.3)

whenever the remainder has the square-root small-ball coefficient `H`.

In the present setting the two disjoint banks are the single untouched original hub coordinate `X_h` and the entire original tail bank. Their post-pair cross block is the 1xm row `n_h`, hence its unique nonzero singular value is

`sigma=||n_h||_2`.                                               (5.4)

All scalar-hub curvature belongs to the first same-bank function, and **all tail diagonal curvature and all core-induced tail curvature** belong to the second same-bank function; none is deleted. Applying (5.1) then (5.3), and using (4.4), gives the determinant cancellation

`|det P_h| sigma = ||R_h||_2`.                                  (5.5)

### Theorem 5.1 — `QFORM-P1-INDEFINITE-PAIR-PAYMENT-v1`

If `P_h` is invertible indefinite and `R_h` is nonzero, then the full scalar quadratic form has an essentially bounded density satisfying

`boxed:
 ||p_Q||_infinity
 <= C_1 [sigma_min(P_h) ||R_h||_2]^(-1/4),`                      (5.6)

where

`C_1=4 sqrt(2H_1)=15.082311168072676... .`                       (5.7)

No conditional fiber supremum occurs; the actual product-law rank-one crossing is averaged first.

### Definite-pair endpoint

If instead `P_h` is definite, condition on every remaining original coordinate. Completing the square translates the two physical pair coordinates. Their joint density is at most one. The linear map `y=|P_h|^{1/2}(x-x_0)` gives a two-dimensional density cap `|det P_h|^{-1/2}`, and radial coarea for `|y|^2` gives

`boxed: ||p_Q||_infinity <= pi / sqrt(|det P_h|).`                (5.8)

This uses only the product density cap in the two original coordinates; it does not rotate a product law and then claim independence.

## 6. Aggregate P1 payment under a finite pair gate

Since

`Lambda_1=sum_h ||R_h||_2^2`,                                   (6.1)

some hub `h_*` satisfies

`||R_h*||_2 >= sqrt(Lambda_1/3).`                                (6.2)

Assume the three literal pair blocks obey

`sigma_min(P_h)>=kappa>0, h=1,2,3.`                              (6.3)

Choose `h_*` from (6.2). If `P_h*` is definite, (5.8) and `|det P_h*|>=kappa^2` give `pi/kappa`. If it is indefinite, (5.6) gives the other branch.

### Corollary 6.1 — `QFORM-P1-PAIR-GATE-PAYMENT-v1`

Under (6.3),

`boxed:
 ||p_Q||_infinity
 <= max{
      pi/kappa,
      C_1 [kappa^2 Lambda_1/3]^(-1/8)
    }.`                                                         (6.4)

Combining (3.3) with (6.4), on the actual partner branch `P_1>5P/16` and `mu>0`,

`boxed:
 ||p_Q||_infinity
 < max{
      pi/kappa,
      C_1 [5 kappa^2 |beta| mu^4 P / 48]^(-1/8)
    }.`                                                         (6.5)

Thus the whole P1 tail packet is paid whenever the finite hub metric `mu` and the literal physical-pair conditioning `kappa` are quantitative. Every tail coefficient remains present.

## 7. A source-valid obstruction to the stronger `P1 => good physical pair` claim

The pair gate (6.3) is not automatic, even when P1 is large and the ambient matrix is an exact QFORM target.

Take

`B = [[1,1,1],
      [1,1,-1],
      [1,-1,1]],`                                               (7.1)

`D=0`, and a one-coordinate tail with

`Z=e_1`.                                                        (7.2)

Then

`spec(B)={2,2,-1}`, `beta=-4`, `G=diag(1,0,0)`.                 (7.3)

Hence

`P_0=4, P_1=4, P_2=P_3=0, P=8`,                                (7.4)

so in particular

`P_1=4>5P/16=5/2`.                                              (7.5)

Because `D_H=0`, (2.5) gives

`Lambda_1=16`.                                                   (7.6)

Indeed the three mixed vectors are concentrated completely in one hub index:

`R_1=-4, R_2=R_3=0`.                                           (7.7)

But every physical 2x2 hub principal block is singular:

`det [[1,-1],[-1,1]]=0`,
`det [[1,1],[1,1]]=0`.                                         (7.8)

Therefore **large complete P1 mixed-minor energy does not force even one invertible physical two-hub pair.** Any compiler that tries to extract such a pair from P1 alone is false.

The full ambient 4x4 matrix is

`A_* = [[1,1,1,1],
        [1,1,-1,1],
        [1,-1,1,1],
        [1,1,1,1]].`                                           (7.9)

Its spectrum is

`{1+sqrt(5), 2, 1-sqrt(5), 0}`.                                (7.10)

Thus it has three eigenvalues of modulus at least one and is a genuine exact-target family, not a two-eigenvalue route counterexample.

Crucially, the obstruction is already paid by the **other arm of the compiler**. Its literal three-hub principal block is `B`, whose three eigenvalues have modulus at least one. The completed required pinned `COUNTEREXAMPLE_SEARCH.md` Theorem A at

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`

states that a physical 3x3 principal block with all eigenvalue magnitudes at least `c` gives, after conditioning all other original coordinates,

`||p_Q||_infinity <= 6 sqrt(pi)/c`.                              (7.11)

Here `c=1`, so the actual target obstruction satisfies

`boxed: ||p_{X^T A_* X}||_infinity <= 6 sqrt(pi)
       =10.634723105433096... .`                                 (7.12)

This is the required real application of a completed `e5f71d...` result to an actual inequality. It also proves that the correct structural statement is **localized three-hub block OR product-preserving physical-pair receiver**, not physical-pair extraction alone.

## 8. Finite-hub compiler now available

Let

`c=sigma_min(K)`                                                 (8.1)

(the minimum absolute hub eigenvalue, because `K` is symmetric), and let `kappa=min_h sigma_min(P_h)`.

The preceding results give a clean conditional compiler for the P1-large branch:

- if `c` is quantitative, the pinned localized Theorem A pays the full ambient form by `6 sqrt(pi)/c`;
- if `c` is small but `mu` and `kappa` are quantitative, (6.5) pays the whole P1 packet by a product-preserving two-hub/rank-one-cross receiver;
- otherwise the only remaining obstruction is finite-dimensional: `mu=sigma_min(KB^{-1})` is small and/or one of the three literal physical pair blocks has small `sigma_min`.

No high-dimensional fiber maximum remains in this reduction.

This is intentionally not promoted to a universal bound because the bare three-large-eigenvalue hypothesis has not yet supplied uniform lower bounds on `c`, `mu`, `kappa`, or the combined volume currency in (6.5). The obstruction (7.1)-(7.10) proves that `kappa` cannot be forced merely from large P1.

## 9. Exact first unpaid implication after this run

The next B06 debt is

`QFORM-P1-FINITE-HUB-DEGENERATION-ROUTING-v1`:

> In partner r53's low-disjoint three-hub packet, assume `P_1>5P/16` and the localized hub triple is not quantitative. Use the identities
> `Lambda_1=beta^2 tr(adj(B^{-1}K) G adj(B^{-1}K)^T)` and
> `Lambda_1>=|beta| mu^4 P_1`
> together with the actual finite hub degeneracy (`mu` small and/or one or more physical 2x2 pair blocks nearly singular) to expose either r53's same-bank normal curved-section channel or an at-most-five heavy-tail-coordinate receiver. The proof must retain the complete diagonal tail and every nonzero spectral term. It may not assert that P1 itself forces an invertible pair, because Section 7 is an exact counterexample.

The new aggregate identity suggests the correct order: first spend all P1 Pluecker mass; only after the sum is fixed should one decide whether the finite hub geometry is a localized triple, an indefinite pair plus rank-one crossing, or a near-singular hub configuration requiring the same-bank normal theorem.

## 10. Deterministic algebra check and corrections retained

A fixed-seed algebra check on 1000 random invertible symmetric `B`, random diagonal `D_H`, and random `3 x 5` matrices `Z` verified (2.4) to maximum normalized discrepancy below `8e-15`. The check is only a sanity test; Sections 2-6 contain the proofs.

The structural example was evaluated exactly: `det B=-4`, `spec(B)={2,2,-1}`, all three 2x2 principal determinants vanish, and `spec(A_*)={1+sqrt(5),2,1-sqrt(5),0}`.

Binding corrections retained: law-uniform pointwise quadratic phase decay is false; arbitrary projected joint-density coarea does not solve the problem; worst spectral-fiber suprema lose dimension; conditional projection-density moments may diverge; rotations do not preserve coordinate independence; a uniformly good single physical minor or universal rank-three cross cut is not available. None of those corrections is contradicted by the present aggregate argument.

No scheduler, identity, cadence, enabled-state, notification, email, permission, account, public-release, paid-call, or remote-workflow state is changed by this report.
