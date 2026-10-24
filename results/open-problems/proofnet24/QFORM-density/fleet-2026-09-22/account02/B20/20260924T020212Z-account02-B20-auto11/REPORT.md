# account02/B20 — r44 finite-carrier collapse to a physical full cut and re-entry compiler

Programme: `QFORM-DENSITY-3EIG-20260922`  
Role: Proof closure and keeper / SYNTHESIS  
Run: `20260924T020212Z-account02-B20-auto11`  
Status: **ESSENTIAL_STEP_APPLIED / R44-R9-CARRIER-PHYSICAL-CUT / FULL-CUT-REENTRY / FULL-QFORM-OPEN**  
Execution: `WITHOUT_VERIFIED_BRAIN`. Full-target continuity remains separate and OPEN.

## 1. Scope and source boundary

The target is unchanged: for every finite `n`, independent ORIGINAL real random variables with probability densities `0<=f_i<=1`, and every real symmetric matrix `A` with at least three eigenvalues of absolute value at least one, prove that `Q=X^TAX` has a density with one universal finite essential-supremum bound, or give a valid target counterexample.

No Gaussianity, log-concavity, moments, bounded/connected support, iid hypothesis, diagonal-basis independence, post-rotation independence, or deletion of a small nonzero coefficient tail is used below. Every cut is a partition of original source coordinates. Spectral/SVD language is used only for deterministic coefficient geometry.

Fresh owner control remained revision `2026-09-22.15`, QFORM-only. The live corrections remain in force: no law-uniform pointwise quadratic-phase decay, no dimension-free worst-fibre projected-density shortcut, no arbitrary-joint three-dimensional coarea cap, no post-rotation independence, no one-good-minor inference from aggregate volume, and no probabilistic deletion of a small nonzero coefficient tail.

The newest compatible completed designated partner actually consumed is account03/B20 r44:

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B20/20260924T014735Z-account03-B20-QFORM-r44/REPORT.md`.

Its two relevant conclusions are:

1. on the giant-near-rank-one/exterior branch, either the full law is already paid by `<462.275` or there is a literal physical cross block `W` with

`||W||_F^2 > c_B:=3025/65536 = 0.0461578369140625`;               (1.1)

2. on the r46 star-aligned rank-two collar, either the full law is already paid by `<301.954`, there is a literal physical self-bank cross block with energy `>0.1081845659397438`, or there is a symmetric skeleton `S` satisfying

`rank(S)<=9,  s_3(S)>=1/4`,                                      (1.2)

and an exact decomposition

`A=S+T+R_0`,                                                      (1.3)

where `T=diag(0_H,A[R,R],A[C,C])`, `|H|=2`, `S[R,R]=S[C,C]=0`, `S[H,H]=A[H,H]`, all hub-leaf coefficients are retained in `S`, and `R_0` is the symmetric embedding of the actual cross tail `E` with

`||E||_F < eps_0:=(9*2^-18)^(1/4)=0.07654655446197431... .`       (1.4)

The live chamber also has

`max_i |A_ii|<1/64`.                                              (1.5)

The required pinned source is

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`,
`proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/`.

Its unrestricted physical fifth-volume theorem is used quantitatively below:

`||p_Q||_infinity <=5 sqrt(2e) e_5(M^T M)^(-1/10)`               (1.6)

for every literal physical cross block `M`, without a row-marginal gate and with arbitrary same-bank curvature/outside couplings retained.

## 2. The r44 finite-rank carrier always contains a fixed-energy physical full cut

The finite-rank label in (1.2) is not itself a new probabilistic debt. Its third singular mode, together with the small physical diagonal and the retained-tail scale, forces a literal original-coordinate cross cut.

Let

`Off(B):=B-diag(B)`.

Since `s_3(S)>=1/4`,

`||S||_F^2 >= s_1(S)^2+s_2(S)^2+s_3(S)^2 >=3/16`.                (2.1)

Only the two physical hub coordinates can contribute to `diag(S)`, and by (1.5),

`||diag(S)||_F^2 <2/4096=1/2048`.                                (2.2)

Therefore

`||Off(S)||_F^2 >3/16-1/2048=383/2048`.                          (2.3)

The symmetric embedding `R_0` of `E` has

`||R_0||_F=sqrt(2)||E||_F <sqrt(2) eps_0=sqrt(3)/16`.             (2.4)

The off-diagonal support of `T` lies only in the `R-R` and `C-C` blocks, whereas `Off(S)+R_0` is supported on `H-H`, `H-R`, `H-C`, and `R-C`. These supports are Frobenius-orthogonal. Thus

`||Off(A)||_F^2
 =||Off(S)+R_0||_F^2+||Off(T)||_F^2
 >=(||Off(S)||_F-||R_0||_F)^2`.                                  (2.5)

Combining (2.3)-(2.5),

`||Off(A)||_F
 > sqrt(383/2048)-sqrt(3)/16
 = (sqrt(766)-4sqrt(3))/64
 =: gamma_0
 =0.3241953402487592... .`                                       (2.6)

Now independently two-colour all ORIGINAL coordinates. For a symmetric zero-diagonal matrix, the expected squared Frobenius norm of the rectangular cut is exactly one quarter of the full squared Frobenius norm. Hence some deterministic full physical bipartition `P sqcup P^c=[n]` satisfies

`boxed:
 ||A[P,P^c]||_F^2 > c_0:=gamma_0^2/4
 = (sqrt(766)-4sqrt(3))^2/16384
 =0.026275654659752182... .}`                                     (2.7)

### Theorem 2.1 — `QFORM-R44-R9-CARRIER-TO-PHYSICAL-CUT-v1`

Under the exact r44 finite-carrier hypotheses (1.2)-(1.5), there is a literal original-coordinate **full cut** `P|P^c` satisfying (2.7). No coordinate rotation is applied to the random vector, and the actual tail `E` remains in the coefficient matrix; only its Frobenius norm is used in the deterministic lower bound.

Notice that the rank upper bound `rank(S)<=9` is not needed for the extraction once `s_3(S)>=1/4` is known. The theorem is therefore stronger than merely saying that a bounded-rank skeleton exists.

## 3. Every r44 physical packet re-enters one common full-cut compiler

The two strong physical packets from r44 also re-enter (2.7). If `W=A[U,V]` is any literal physical cross block with `||W||_F^2>c_B` or `>0.1081845`, extend one side, say `U`, to the full cut `U|U^c`. Its full cross block contains `W` on a disjoint column subbank, so its energy is at least that of `W`, and in particular exceeds `c_0`.

Thus every unpaid r44 rank-nine/strong-packet state admits a literal full cut

`M=A[P,P^c]`, `E:=||M||_F^2>c_0`.                                (3.1)

Set `tau=1/64` and `S_4(M)=sum_{j=1}^4 s_j(M)^2`.

### 3A. Failure of strong-top-four is fully paid

The completed cross-cut volume inequality used by r44/account04-B20 r10 gives, if

`S_4(M) <= (63/64)E`,                                             (3.2)

then

`e_5(M^T M) >= (1/64)^4 E^5/120`.                                (3.3)

Apply the pinned unrestricted D5 theorem (1.6) to this **actual full physical cut**. Since `E>c_0`,

`boxed:
 ||p_Q||_infinity
 < 5sqrt(2e)[120/((1/64)^4 c_0^5)]^(1/10)
 =612.696761291... <612.697.}`                                    (3.4)

This is the required pinned-source payment at an actual inequality in the current r44 branch. Same-bank quadratic blocks, the original r44 coefficient tail, outside couplings, affine terms, signs, and extra spectrum remain present.

Hence every unpaid descendant may assume

`S_4(M)>(63/64)E`.                                                (3.5)

### 3B. A third crossing singular direction is fully paid

Assume (3.5) and `s_3(M)>=tau`. Then

`s_1(M)^2 >= S_4(M)/4 >(63/256)E >(63/256)c_0`,                   (3.6)

and `s_2,s_3>=1/64`. Consequently

`Delta_3:=s_1s_2s_3
 > sqrt((63/256)c_0)/4096
 =1.9632116237736183e-5`.                                         (3.7)

The completed grouped physical cross-rank-three receiver gives

`boxed: ||p_Q||_infinity <3e Delta_3^(-1/3)<302.293.`             (3.8)

Thus every unpaid state may further assume

`s_3(M)<1/64`.                                                     (3.9)

### 3C. A genuine second direction re-enters the E2 cascade

Assume (3.5), (3.9), and `s_2(M)>=tau`. Writing `x_i=s_i^2`, the same strong-top-four calculation as in the earlier B20 compiler yields

`e_2(M^T M)
 > tau^2[(63/64)E-3tau^2]
 > z_0`,                                                          (3.10)

where

`boxed:
 z_0:= (1/4096)[(63/64)c_0-3/4096]
 =6.135907148606825e-6.}`                                         (3.11)

Thus this branch is not a new r44 category: it is a fixed-positive-`E2` packet and re-enters the already source-valid determinant-law / half-Riesz / physical-pair / anchored-cofactor cascade. The half-Riesz output is **not** promoted by itself to `L^infinity`.

### 3D. The remaining rank-one tube self-replicates with the same floor

It remains to consider

`S_4(M)>(63/64)E`, `s_2(M)<1/64`, `E>c_0`.                        (3.12)

Let `M_1=s_1uv^T` be the top singular component and use its symmetric embedding as a deterministic rank-at-most-two matrix. Since `s_3(A)>=1` and the residual crossing has operator norm `s_2(M)<1/64`, the previous source-valid Eckart--Young argument gives

`max(||A[P,P]||_op,||A[P^c,P^c]||_op)>63/64`.                    (3.13)

Choose a side `C` attaining (3.13). Remove its physical diagonal using (1.5), then two-colour the original coordinates of `C`. Some split `C=P_1 sqcup Q_1` satisfies

`||A[P_1,Q_1]||_F^2>961/4096`.                                   (3.14)

Relabel the colours so that `P_1` carries at least half the squared mass of the relevant top singular vector. Since in (3.12) `s_2,s_3,s_4<1/64`,

`s_1(M)^2>(63/64)E-3/4096`.                                      (3.15)

Writing `R_1=C^c`, the new full cut `P_1|P_1^c=P_1|(Q_1 union R_1)` therefore has energy

`E' > 961/4096 + (1/2)[(63/64)E-3/4096]
    =1919/8192+(63/128)E
    =:F(E).`                                                       (3.16)

The fixed point of `F` is `1919/4160=0.461298...`, while `c_0` is smaller. Hence for every `E>c_0`,

`F(E)>c_0` if `E<=1919/4160`, and `F(E)>=1919/4160>c_0` otherwise. (3.17)

So the floor `E>c_0` is invariant under every unpaid rank-one reproduction. A same-side continuation strictly decreases the cardinality of the active original-coordinate bank, and a singleton cannot satisfy (3.13) in the all-small-diagonal chamber. Therefore after finitely many reproductions an unpaid chain must undergo the already-defined curvature flip.

At that flip, for a physical partition `[n]=P_1 sqcup Q_1 sqcup R_1`, one has

`||A[P_1 union Q_1,P_1 union Q_1]||_op>63/64`,                    (3.18)
`||A[Q_1 union R_1,Q_1 union R_1]||_op>63/64`,                    (3.19)
`||A[P_1,Q_1]||_F^2>961/4096`,                                   (3.20)

and the retained arm obeys the fixed lower bound

`||A[P_1,R_1]||_op^2
 > (1/2)[(63/64)c_0-3/4096]
 =0.012566337840346777...`,                                      (3.21)

so

`boxed: ||A[P_1,R_1]||_op>0.1120996781.`                          (3.22)

The current cut also remains a strong-top-four absolute-rank-one tube with energy `>c_0`; no coefficient has been removed from the actual law.

### Theorem 3.1 — `QFORM-R44-FULLCUT-REENTRY-v1`

Every r44 state lying in either the finite-carrier branch or either new strong-physical-packet branch is, source-preservingly, in exactly one of the following classes:

1. a full-law D5 payment `<612.697`;
2. a grouped physical rank-three payment `<302.293`;
3. a fixed-positive E2 packet with `e_2(M^TM)>z_0=6.1359e-6`, entering the existing determinant-law/anchor cascade; or
4. a finite curvature-flip packet satisfying (3.18)-(3.22).

In particular the r44 `rank<=9, s_3>=1/4` skeleton and the r44 fixed-energy strong-top-four packets no longer need to appear as independent frontier categories.

## 4. Exact use of the newest designated partner

The newest completed account03/B20 r44 is used at its exact expressions, not merely cited:

- its skeleton inequality `s_3(S)>=1/4` and retained-tail scale `||E||_F<eps_0` are substituted into (2.1)-(2.7), producing the new explicit physical cut floor `c_0`;
- its giant-R1 block floor `3025/65536` and aligned-collar self-bank floor `0.1081845659...` are extended to full physical cuts and routed through Theorem 3.1.

This directly removes two of the three new structural categories in r44's stated frontier.

## 5. Current first unpaid implication

The fresh first unpaid full-target implication is now

`QFORM-R44-E2/ONEANCHOR-OR-CURVATURE-FLIP-PAYMENT-v1`:

> Under the original independent cap-one source law, the all-small-diagonal target chamber `s_3(A)>=1`, and after the completed scalar, principal-triple, E3, D5, grouped-rank-three, and r44 exits, prove a universal linear small-ball / essential-density payment for the surviving fixed-positive E2 / multiplicative-rank-two / inherited one-anchor packets or for the finite curvature-flip packet (3.18)-(3.22), while retaining arbitrary same-bank curvature, every nonzero coefficient tail, all outside couplings, signs, affine terms, fragmented/unbounded laws, and arbitrary extra spectrum.

The multiplicative-rank-two packet from the preceding B20 theorem is already an E2 packet (`E_2>4/9`) and should be attacked through the same determinant-aggregate/anchor interface rather than treated as a separate spectral category. The r44 rank-nine carrier and its strong-top-four physical packets have been collapsed into the re-entry theorem above.

## 6. Correction audit and review

Review A (algebra/support): the only possible Frobenius cancellation in Section 2 is between the `R-C` portions of `S` and `R_0`; it is paid by the exact triangle loss `||R_0||_F<sqrt(3)/16`. The arbitrary same-bank block `T` lives on disjoint off-diagonal matrix positions and therefore cannot cancel this lower bound.

Review B (probabilistic provenance): every smoothing theorem is applied only to literal original-coordinate cuts. The singular vectors of `S` and `M` are used solely to derive deterministic coefficient inequalities. No projected random vector is declared independent, no conditional cap-one density is assumed, and no small nonzero random quadratic term is discarded.

This is not a full candidate, so the owner's two independent end-to-end reviews for a complete proof are not claimed.

## 7. Status

Full unrestricted QFORM: **OPEN / NOT PROVED / NOT DISPROVED**.  
No valid target counterexample was found.  
Full-target continuity: **OPEN**.  
The new D5 payment (3.4) is asserted only as essential boundedness at the pinned source's scope; no continuity upgrade is inferred beyond source-backed statements.
