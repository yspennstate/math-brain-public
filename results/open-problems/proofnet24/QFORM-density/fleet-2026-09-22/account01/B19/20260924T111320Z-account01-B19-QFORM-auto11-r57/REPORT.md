SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B19, 2026-09-24T11:13:20Z.
attacking: the retained-tail stability interface after diagonal-plus-finite-rank purification; remove unbounded physical-diagonal complexity by a finite-core argument, then identify the genuinely transverse light-light tail and apply account02/B19's latent pseudodeterminant theorem on the exact aligned endpoint.

# account01/B19 r57 — finite-diagonal purge, finite-hub carrier transfer, and aligned-tail Fresnel endpoint

Programme: `QFORM-DENSITY-3EIG-20260922`, owner revision `2026-09-22.5`.

Status: **ESSENTIAL_STEP_APPLIED / NEW STRUCTURAL COMPILER / DESIGNATED PARTNER APPLIED AT AN ACTUAL EQUATION / FULL QFORM OPEN / NOT PROVED / NOT DISPROVED**.

Execution: **WITHOUT_VERIFIED_BRAIN**. Repository retrieval and handoff transport are not native receiver ingestion.

Continuity: the finite-core payment below proves essential boundedness at its cited scope; I do not add a continuity claim there. The account02/B19 latent branch used in Section 5 does give a continuous `C_0` density. Full-target continuity remains OPEN separately.

All coordinates below are literal ORIGINAL coordinates. Orthogonal matrices occur only in deterministic coefficient-space factorizations. No random spectral coordinate is declared independent. No moment, support, iid, Gaussian, log-concavity, arbitrary-joint coarea, worst-fibre cap, pointwise law-uniform oscillatory decay, conditional-cap inheritance, coefficient-continuity, or deletion of a nonzero coefficient tail is used.

## 1. Fresh source frontier

Fresh protected control was resolved at

`yspennstate/math-research-brain@247191ebdc15533a53c6b44fc99f803525f956a1`

and reread immediately before the mathematical write at current main descendant

`yspennstate/math-research-brain@17d0485914975deb71a305f1241dd20bdc17b6e0`.

OWNER CONTROL remains revision `2026-09-22.15`, the sole research programme is QFORM, and the unrestricted theorem remains OPEN. The current corrections and CLAIMS retain all the known failures listed above.

The immediately preceding same-slot frontier is

`proofnet24/QFORM-density/fleet-2026-09-22/account01/B19/20260924T095039Z-account01-B19-QFORM-auto11-r56/REPORT.md`,

reconciled by the later same-slot r56 addendum. Its live anchored/no-large-star survivor is an exact coefficient decomposition

`A_light = D + K_r + F`,                                           (1.1)

where `D` is physical diagonal and either

`r<=12`, `||F||op < delta_12 := 3/16 + 2^-16
                         = 12289/65536
                         = 0.1875152587890625`,                    (1.2)

or on determinant collapse

`r<=11`, `||F||op < delta_11 := 3/16 + 2^-16 + 112*2^-20
                         = 1537/8192
                         = 0.1876220703125`.                       (1.3)

The nonzero `F` is retained. The prior first debt was

`QFORM-ANCHOR-REPURIFIED-R12/R11-SUBTARGET-TAIL-JOINT-ENDPOINT-v1`.

The fixed-dimensional physical principal-core theorem used below is the completed source recorded in account02/B20: if an `m x m` literal physical principal quadratic matrix has third absolute eigenvalue at least `c>0`, then, uniformly in all induced linear terms,

`||p||infinity <= 250 m (8+log m)/c`.                              (1.4)

Conditioning only outside ORIGINAL coordinates makes (1.4) an ambient receiver.

The designated partner consumed at equation level is account02/B19 r14,

`yspennstate/math-open-problems@02a537de4788fa8821d7986ef53fc5ad0a311003`,

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B19/20260924T083831Z-account02-B19-QFORM-auto11-r14/REPORT.md`.

Its theorem `QFORM-BL-RANKR-LATENT-PSEUDODET-ENDPOINT-v1` says that for an actual source block

`A[I,I]=D_I + W H W^T`, `W^T W=I`,                               (1.5)

with `D_I` physical diagonal, every row leverage `||W_i||^2<=1/2`, and `rank H=k>=3`, the FULL ambient law has a continuous `C_0` density and

`||p_Q||infinity <= [4k/(k-2)] |pdet H|^(-1/k)`.                  (1.6)

Arbitrary blocks touching `I^c`, curvature in `I^c`, affine terms, signatures and exact rank drops are retained. It does not authorize deleting a small nonzero latent mode or a nonseparable source tail.

## 2. New theorem: large physical diagonal coefficients force a bounded finite core

### Theorem 2.1 — `QFORM-SUBTARGET-TAIL-LARGEDIAG-FINITECORE-v1`

Let

`A=D+K+F`                                                         (2.1)

be a real symmetric matrix in original coordinates, where `D=diag(d_i)` is physical diagonal, `rank K<=r`, and `||F||op<=delta`. Fix `a>delta`. If there exist at least `r+3` physical coordinates with

`|d_i|>=a`,                                                       (2.2)

then for every independent cap-one product input law the complete ambient quadratic form has an essentially bounded density with

`boxed:
 ||p_Q||infinity
 <= 250 (r+3) [8+log(r+3)]/(a-delta).}`                           (2.3)

No sign assumption is made on `D,K,F`, and no bound is required on `||K||`.

### Proof

Choose any `S` of exactly `m=r+3` coordinates satisfying (2.2). Put

`B=D[S,S]+F[S,S]`.                                                (2.4)

Because every diagonal entry of `D[S,S]` has modulus at least `a`,

`s_m(D[S,S])>=a`.                                                 (2.5)

Compression cannot increase operator norm, so `||F[S,S]||<=delta`; singular-value Weyl gives

`s_m(B)>=a-delta`.                                                (2.6)

Now `rank K[S,S]<=r`. The standard rank-`r` singular-value interlacing inequality

`s_j(B+K[S,S]) >= s_{j+r}(B)`                                     (2.7)

with `j=3` gives

`boxed: s_3(A[S,S]) >= s_{r+3}(B) >= a-delta.}`                   (2.8)

Since `A[S,S]` is symmetric, this is its third largest absolute eigenvalue. Condition on every original coordinate outside `S`; all outside couplings become affine terms while the variables in `S` remain independent with their original density caps. Scale (1.4) by `a-delta` to obtain (2.3), uniformly in the conditioning value. Averaging finishes the proof. QED.

### Application to the live r56 tail

Take `a=1/2`.

For the rank-12 branch,

`a-delta_12 = 20479/65536 = 0.3124847412109375`,                   (2.9)

so fifteen large physical diagonals would give

`||p_Q||infinity < 128503`.                                       (2.10)

Therefore every still-unpaid rank-12 survivor satisfies

`boxed: #{i: |d_i|>=1/2} <=14.}`                                  (2.11)

For the rank-11 collapse branch,

`a-delta_11 = 2559/8192 = 0.3123779296875`,                        (2.12)

and fourteen large diagonals would give

`||p_Q||infinity <119205`.                                        (2.13)

Hence every still-unpaid rank-11 collapse survivor satisfies

`boxed: #{i: |d_i|>=1/2} <=13.}`                                  (2.14)

This is the first new simplification: the arbitrary diagonal in (1.1) is no longer an infinite-dimensional source of difficulty. Either it pays through a literal finite principal core, or all coefficients `|d_i|>=1/2` live on a fixed finite physical hub.

## 3. New finite-hub / light-carrier transfer

Let

`H={i: |d_i|>=1/2}`, `L=H^c`, `h=|H|`,                            (3.1)

so `h<=14` in the r12 branch and `h<=13` in the r11 branch. Write the actual block matrix

`A=[[A_HH,C],[C^T,A_LL]]`.                                        (3.2)

If `h>=3` and

`s_3(A_HH)>=1/64`,                                                (3.3)

then the fixed-dimensional theorem (1.4), conditioned on `L`, already pays the full law. In the r12 case its worst bound at `h=14` is

`64*250*14*(8+log 14) < 2,383,149`.                               (3.4)

Thus an unpaid state may assume `s_3(A_HH)<1/64` (with this understood trivially when `h<3`).

Define

`m_H := #{ singular values of A_HH that are >=3/4 }`.              (3.5)

Then `m_H<=2`.

### Theorem 3.1 — `QFORM-R57-FINITEHUB-LIGHTCARRIER-TRANSFER-v1`

Assume `s_3(A)>=1`, (3.1)-(3.5), and `||C||op<1/4`. Then

`boxed: s_(3-m_H)(A_LL) >=3/4.}`                                  (3.6)

Moreover, because

`A_LL=D_L+K_LL+F_LL`,                                              (3.7)

with `||D_L||op<1/2` and `||F_LL||op<=delta`,

`boxed:
 s_(3-m_H)(K_LL) >= kappa_delta := 1/4-delta.}`                    (3.8)

For the live two tails,

`kappa_12=4095/65536=0.0624847412109375`,                          (3.9)

`kappa_11=511/8192=0.0623779296875`.                              (3.10)

If instead `||C||op>=1/4` and `h>0`, then one literal hub coordinate `i in H` obeys

`boxed:
 ||A[i,L]||_2 >= 1/(4 sqrt(h)) >=1/(4 sqrt(14))
 =0.066815310478... .}`                                           (3.11)

Thus the failure of the small-coupling branch is itself a fixed-scale physical hub-star packet.

### Proof

Put

`A_0=diag(A_HH,A_LL)`.                                            (3.12)

Then

`A-A_0=[[0,C],[C^T,0]]`,                                         (3.13)

whose operator norm is exactly `||C||`. Hence singular-value Weyl and `s_3(A)>=1` give

`s_3(A_0)>=1-||C||>3/4`.                                         (3.14)

Therefore the block diagonal `A_0` has at least three singular values at least `3/4`. Exactly `m_H` of those can come from `A_HH`; by (3.5), `m_H<=2`. Hence `A_LL` contributes at least `3-m_H` singular values at least `3/4`, proving (3.6).

Next

`||D_L+F_LL||op <=1/2+delta`.                                     (3.15)

Applying Weyl to `A_LL=K_LL+(D_L+F_LL)` gives

`s_(3-m_H)(K_LL)
 >=3/4-(1/2+delta)
 =1/4-delta`,                                                     (3.16)

which is (3.8).

Finally, if `||C||op>=1/4`, then `||C||F>=1/4`. Since `C` has `h` physical rows,

`sum_(i in H)||A[i,L]||_2^2=||C||F^2>=1/16`,                     (3.17)

so one row has norm at least `1/(4 sqrt(h))`. QED.

### Interpretation

The rank-12/rank-11 tail problem is now split into finite, source-valid alternatives. Either a bounded physical principal hub pays, a fixed physical hub-star appears, or the untouched light bank contains one, two or three **finite-latent** directions at the fixed scales (3.9)-(3.10), depending on whether the finite hub itself carries two, one or zero `3/4`-scale singular directions.

In the particularly clean `m_H=0` branch,

`s_3(A_LL)>=3/4`, `s_3(K_LL)>=kappa_delta`.                        (3.18)

No coefficient of `F_LL` was erased to obtain this.

## 4. Exact aligned-tail endpoint and the designated account02/B19 theorem

Section 3 isolates what must be paid jointly with the genuine light-light tail. There is one important exact endpoint that can now be removed completely.

Assume `m_H=0`, `||C||op<1/4`, and suppose the retained light-light nonseparable part is **coefficient-range aligned** with the finite latent carrier, in the exact sense that there is a finite-dimensional physical frame `W` and symmetric `H_0` such that

`K_LL+F_LL = W H_0 W^T`, `W^T W=I_k`,                             (4.1)

with `k<=12` (or `k<=11` in the collapse branch) and

`max_(i in L)||W_i||_2^2<=1/2`.                                  (4.2)

This includes, for example, `F_LL=P_K F_LL P_K` where `P_K` projects onto the range of `K_LL`; importantly, `F_LL` is **absorbed exactly**, not discarded.

The actual light source block is then

`A_LL=D_L+W H_0 W^T`.                                             (4.3)

From (3.18) and `||D_L||<1/2`,

`boxed: s_3(H_0)=s_3(WH_0W^T) >=1/4.}`                            (4.4)

Indeed singular values are invariant under the isometric frame and Weyl gives `s_3(WH_0W^T)>=s_3(A_LL)-||D_L||>=1/4`.

Now condition on the finite original-coordinate hub `H`. Every `H-L` coupling becomes affine, while (4.3) is unchanged as the quadratic part on the independent light variables. This is exactly the hypothesis of the designated account02/B19 theorem (1.6). Therefore

`boxed:
 ||p_Q||infinity
 <= [4k/(k-2)] |pdet(H_0)|^(-1/k),
 p_Q in C_0(R).}`                                                 (4.5)

This is an actual equation-level application of the partner theorem to the live retained-tail compiler.

Two consequences are immediate.

**Exact rank three.** If `k=3`, then (4.4) gives

`|pdet(H_0)|>= (1/4)^3=1/64`,                                    (4.6)

and hence

`boxed: ||p_Q||infinity <=48, p_Q in C_0.}`                       (4.7)

**Higher aligned rank.** If `4<=k<=12` and

`|pdet(H_0)|>=2^-120`,                                            (4.8)

then, since `4k/(k-2)<=8` and `120/k<=30`,

`boxed: ||p_Q||infinity <=8*2^30=8,589,934,592, p_Q in C_0.}`      (4.9)

If (4.8) fails, write the nonzero singular values of `H_0` as `s_1>=...>=s_k>0`. Since

`|pdet(H_0)|=prod_(j=1)^k s_j >= s_k^k`,                          (4.10)

we obtain the deterministic near-rank-drop collar

`boxed: s_k(H_0)<2^(-120/k)<=2^-10.}`                             (4.11)

Equation (4.11) is **not** permission to remove that mode. It says only that after exact range alignment, every non-paid state is a quantitatively tiny nonzero finite-latent direction, precisely the correction-sensitive collar identified by account02/B19.

If (4.2) fails, the failure is also finite-dimensional localization: the rank-`k` coefficient range has a physical row with leverage `>1/2`; there are fewer than `2k` such rows by Parseval. No diffuse-source theorem is claimed on that branch.

## 5. Compact conditional proof assembly after r57

The proof graph relevant to this slot can now be compressed as follows.

1. Same-constant principal-minimal descent and the completed scalar, physical-pair, pair-log, physical-E3, D5, ridge/window, grouped-star, hub+square, null-coloop and rank-two fractional receivers pay their exact branches with arbitrary allowed outside curvature retained.
2. The robust-crossing / common-plane compilers and r56 direct repurification either pay by literal physical E3 or reduce the anchored no-large-star survivor to (1.1)-(1.3).
3. Theorem 2.1 above now pays every such survivor having `r+3` physical diagonal coefficients of modulus at least `1/2`. Thus the remaining large diagonal support has size at most fourteen (or thirteen in the collapse branch).
4. Theorem 3.1 then forces a fixed-scale physical hub-star, a paid finite principal hub, or `3-m_H` light latent directions at scale at least `kappa_12` / `kappa_11` while the genuine nonzero tail remains present.
5. In the three-light-carrier branch, if the light-light tail is exactly absorbed into the same finite coefficient range and that range is diffuse, account02/B19 r14 pays the full ambient law by (4.5). Exact rank three is bounded by `48`; higher rank is paid at the fixed pseudodeterminant gate, while pseudodeterminant failure produces the explicit nonzero near-rank-drop collar (4.11).

Accordingly the old undifferentiated tail debt can be sharpened to

`QFORM-R57-FINITEHUB-OR-TRANSVERSE-LIGHTTAIL-NEARRANKDROP-ENDPOINT-v1`:

> In the r12/r11 anchored survivor, after the finite-core diagonal purge, retain the finite hub `|H|<=14` (`<=13` on collapse), all hub-light couplings and the full nonzero light-light tail. If the finite hub has no target-scale third mode and the hub-light coupling is below `1/4`, the light finite-rank carrier is forced at the explicit scales (3.9)-(3.10). Close the remaining cases by either (i) spending the fixed physical hub-star / one- or two-hub plus light-carrier packet, (ii) routing a genuinely transverse component of `F_LL` to an already-paid physical/ridge receiver, or (iii) proving a uniform endpoint through the aligned but nonzero near-rank-drop collar (4.11), without coefficient deletion.

This is strictly narrower than `QFORM-ANCHOR-REPURIFIED-R12/R11-SUBTARGET-TAIL-JOINT-ENDPOINT-v1`: arbitrary large diagonal complexity and the exact diffuse aligned rank-three endpoint are now removed.

## 6. Corrections and regularity audit

- `F` is never dropped because its operator norm is `<0.188`.
- The finite-core proof conditions only original coordinates.
- The partner theorem is used only when the **actual** light self-block has the exact diagonal-plus-latent form (4.3).
- A small nonzero latent singular value in (4.11) remains an unpaid coefficient; exact rank drop is paid, near rank drop is not identified with exact rank drop.
- Signs are arbitrary throughout; singular values are used in the deterministic transfer, while the partner theorem handles every inertia.
- Full continuity is not inferred from the finite-core branch. It is recorded only on the partner branch where an `L^1` characteristic-function theorem supplies it.

The unrestricted target remains OPEN, and no end-to-end solution claim is made.
