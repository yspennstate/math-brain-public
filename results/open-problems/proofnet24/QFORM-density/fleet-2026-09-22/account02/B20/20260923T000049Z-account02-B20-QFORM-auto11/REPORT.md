# account02/B20 QFORM auto11 — no-pivot physical frontier and spike/dust obstruction

Run: `20260923T000049Z-account02-B20-QFORM-auto11`  
Programme: `QFORM-DENSITY-3EIG-20260922`  
Assignment: proof closure and keeper, SYNTHESIS  
Classification: **ESSENTIAL_STEP_APPLIED / N3-O0-PHYSICAL-FRONTIER-QUANTIZED / ROUTE-COUNTEREXAMPLE / FULL_TARGET_OPEN**  
Execution: `WITHOUT_VERIFIED_BRAIN` (`full_brain_connected=false`).

## 1. Exact target and correction boundary

For every finite `n`, every independent real `X_i` with probability densities `0<=f_i<=1`, and every real symmetric `A` with at least three eigenvalues of absolute value at least one, prove that `Q=X^T A X` has a density with one universal finite essential-supremum bound, or give a valid counterexample.

No Gaussian, log-concavity, moment, compact/connected-support, iid, diagonal-basis or post-rotation-independence assumption is used. Continuity is separate. I do not use law-uniform pointwise quadratic-phase decay, unrestricted spectral-fiber suprema, arbitrary-joint rank-three coarea, conditional projected-density caps, or an inference from the global spectrum to one uniformly good physical minor.

Fresh owner control remained QFORM-only at revision `2026-09-22.15` during the run. The newest completed designated partner consumed is account03/B20 r20, canonical mathematics

`yspennstate/math-open-problems@3e8641ff13d6bc9a08f6c5cbc4f0bd66edb53677`,

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B20/20260922T235039Z-account03-B20-QFORM-r20/REPORT.md`.

The newest interactive package actually used is the physical-cross-block fifth-volume theorem D5 from

`proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/FOURIER_ROUTE_REPORT.md`:

`||p_Q||_infinity <= 5 sqrt(2e) E_5(M)^(-1/10)`                         (1.1)

for an actual physical cross block `M`, retaining arbitrary same-side quadratic blocks and outside couplings.

I also use the newest Claude synthesis no-pivot equivalence: for any one fixed `tau in (0,1]`, it is enough to prove the full target on the class `N3(tau)` in which

`|A_ii|<tau`,  `|det A[{i,j},{i,j}]|<tau` for all `i!=j`.              (1.2)

Fix throughout

`tau_0=1/128`.                                                         (1.3)

Then every physical off-diagonal entry obeys

`|A_ij|^2 <= |A_ii A_jj|+|det A[{i,j},{i,j}]| < tau_0^2+tau_0 =129/16384`,

so with

`eta:=sqrt(129)/128`,                                                  (1.4)

we have `|A_ij|<eta`. The stronger observation `|A_ij|<1/8` was already recorded by account01/B09; it is not claimed as new here.

## 2. Exact use of the newest account03/B20 r20 result

The O0 two-anchor state gives an actual physical cross block, after physical permutations only,

`B=[[b,r^T],[c,D]]`,                                                   (2.1)

with common anchored third-minor mass `Z_ia>1/768`. Put

`delta:=1/sqrt(768)=1/(16 sqrt(3))`.                                 (2.2)

Partner r20 proves the following exact physical deshearing statements.

### Zero outer edge

If `b=0`, then

`Z_ia = ||c||^2 ||r||^2 ||P_(c^perp) D P_(r^perp)||_F^2`,             (2.3)

hence

`||c|| ||r|| ||P_(c^perp) D P_(r^perp)||_F > delta`.                 (2.4)

If `D` has `m` residual rows and `n` residual columns, the no-pivot entry cap gives

`||c||<=eta sqrt(m)`, `||r||<=eta sqrt(n)`, `||D||_F<=eta sqrt(mn)`.

Since orthogonal projections contract Frobenius norm, (2.4) implies

`mn > delta/eta^3 = 131072/(sqrt(3) 129^(3/2)) = 51.6493...`,         (2.5)

therefore

`boxed: mn>=52.`                                                       (2.6)

Thus the exact zero-edge obstruction cannot live in a bounded-size residual cross bank inside `N3(1/128)`.

### Nonzero outer edge

If `b!=0`, partner r20 proves that either

`P2: |b| sqrt(E_2(D)) > delta/2 =1/(32 sqrt(3))`,                    (2.7)

or both one-sided transverse star reserves exceed `delta/2`.

Inside `N3(1/128)`, `|b|<1/8`, so (2.7) gives the exact numerical implication

`sqrt(E_2(D))>1/(4 sqrt(3))`, hence

`boxed: E_2(D)>1/48.`                                                  (2.8)

On either star reserve, replacing the projected Frobenius norm by `||D||_F` gives

`eta^3 mn > delta/2`, hence

`boxed: mn>=26.`                                                       (2.9)

Equations (2.6), (2.8), (2.9) are a direct application of the newest designated-partner expression under the sufficient no-pivot reduction; no projected random coordinates are declared independent.

## 3. D5 pays the high fifth-volume part of P2

Apply (1.1) to the actual physical residual block `D`. If

`E_5(D)>=1/1024`,                                                      (3.1)

then

`||p_Q||_infinity <= 5 sqrt(2e) (1024)^(1/10)
                   =10 sqrt(2e)
                   <23.317.`                                          (3.2)

Thus every still-unpaid P2 state has

`E_2(D)>1/48`, `E_5(D)<1/1024`.                                      (3.3)

This is the exact D5 application required in the current continuation.

## 4. New theorem: low third-volume is either genuinely two-directional or a large rank-one spike

### Theorem `QFORM-R-SMALL-E3-SPIKE-OR-TWODIR-v1`

Let `D` be any real matrix with squared singular values

`lambda_1>=lambda_2>=...>=0`,

and suppose

`E_2(D)>1/48`, `E_3(D)<2^(-18)`.                                     (4.1)

Then at least one of the following holds:

**(A) two-direction packet**

`boxed: lambda_1 lambda_2 >1/96`, equivalently
`boxed: sigma_1(D) sigma_2(D)>1/sqrt(96).}`                           (4.2)

**(B) spike/dust packet**

`boxed: lambda_1 >16776973/1769472 =9.4813441523...}`,                (4.3)

so `sigma_1(D)>3.079179136...`. If in addition `D` is a physical subblock of an `N3(1/128)` matrix, with `m x n` entries, then necessarily

`boxed: mn>=1205.`                                                     (4.4)

### Proof

Let

`T:=sum_(r>=3) lambda_r = dist_F(D,{rank<=2})^2`.                     (4.5)

The exact elementary-symmetric identity

`3E_3=sum_(p<q)lambda_p lambda_q sum_(r!=p,q)lambda_r`                (4.6)

and the ordering of the `lambda` imply

`3E_3>=T E_2`.

Hence from (4.1)

`T < 3*2^(-18)/(1/48)=9/16384`.                                     (4.7)

Put `p=lambda_1 lambda_2`. Since the tail second elementary sum is at most `T^2/2`,

`E_2
 =p+(lambda_1+lambda_2)T+E_2(lambda_3,lambda_4,...)
 <=p+2 lambda_1 T+T^2/2`.                                            (4.8)

If `p>=E_2/2`, then `p>1/96`, proving (A). Otherwise `p<E_2/2`, and (4.8) yields

`lambda_1 > (E_2-T^2)/(4T)
          > (1/48-(9/16384)^2)/(4*(9/16384))
          =16776973/1769472`,                                        (4.9)

which proves (B).

For a physical `m x n` subblock in `N3(1/128)`, (1.4) gives

`lambda_1=sigma_1(D)^2 <= ||D||_F^2 < mn*(129/16384)`.               (4.10)

Combining (4.3) and (4.10),

`mn > (16776973/1769472)*(16384/129)
    =16776973/13932
    =1204.2042...`,                                                   (4.11)

so the integer product `mn` is at least `1205`. QED.

This theorem is deterministic and source-coordinate safe. It does not turn singular vectors into independent random variables.

## 5. A genuine target-level family refuting a free robust-two-direction inference

The spike/dust alternative is not an artifact of the proof. The following explicit target family shows that the numerical conditions

`N3(1/128) + s_3(A)>=1 + E_2(D)>1/48 + E_3(D)<2^(-18) + E_5(D)<1/1024`

do **not** force `sigma_1(D)sigma_2(D)` to be bounded below by a universal positive constant.

Take `M=2^k`, `k>=7`, put

`N=M^2`, `d=2M^2`, `t=1/(32M^3)`.                                   (5.1)

Let `U,V` be `d x d` normalized Sylvester-Hadamard orthogonal matrices, so every entry has modulus `d^(-1/2)`. Define

`D_M = U diag(sqrt(M), sqrt(t),...,sqrt(t),0,...,0) V^T`,             (5.2)

with exactly `N` copies of `sqrt(t)`. Its squared singular values are

`M, t (N times), 0,...`.

Therefore

`E_2(D_M)
 =1/32 +(M^2-1)/(2048 M^4)
 >1/48`,                                                             (5.3)

and

`E_3(D_M)
 =(M^2-1)/(2048 M^3)
 +(M^2-1)(M^2-2)/(196608 M^7)
 <1/(2048M)
 <=2^(-18)`                                                          (5.4)

for `M>=128`. Also

`E_5(D_M)
 =M*C(N,4)t^4+C(N,5)t^5
 <1/(24*32^4 M^3)+1/(120*32^5 M^5)
 <1/1024`.                                                           (5.5)

But

`boxed: sigma_1(D_M)sigma_2(D_M)=sqrt(Mt)=1/(4 sqrt(2) M) ->0.`       (5.6)

The physical entries remain tiny:

`max_(i,j)|(D_M)_ij|
 <=[sqrt(M)+N sqrt(t)]/d
 =(1+1/(4sqrt(2)))/(2M^(3/2))`.                                      (5.7)

Now add a disjoint 256-coordinate bank and let `w=(1/16,...,1/16)` there. On the physical coordinate decomposition `L disjoint_union R disjoint_union W`, define

`A_M = [[0,D_M,0],[D_M^T,0,0],[0,0,w w^T]].`                         (5.8)

The bipartite block contributes eigenvalues `+/-sigma_j(D_M)`, so in particular `+/-sqrt(M)`, while `w w^T` contributes the additional eigenvalue `+1`. Thus `A_M` has at least three eigenvalues of absolute value at least one.

Every diagonal is either zero or `1/256<1/128`. Principal physical `2x2` determinants inside the rank-one bank vanish; cross-bank determinants outside `L-R` vanish; an `L-R` pair has determinant `-(D_M)_ij^2`, whose magnitude is `<1/128` for `M>=128` by (5.7). Hence

`boxed: A_M belongs to N3(1/128) for every M>=128.}`                  (5.9)

This is **not a counterexample to QFORM**. It is a valid source-level counterexample to the proposed free implication that the low-`E_3` R invariants plus the full target spectrum must contain a uniformly robust second singular direction. Any closure of the spike/dust branch must spend grouped physical banks/hubs or another aggregate mechanism; it cannot simply promote (4.1) to `sigma_1 sigma_2 >=c`.

At `M=128`, for orientation, the exact formulas give

`E_2=0.0312500298005...`,
`E_3=3.8144668599e-6 <2^(-18)=3.814697265625e-6`,
`E_5=1.8941e-14`,
`sigma_1 sigma_2=0.00138107...`.

## 6. Strongest conditional end-to-end synthesis after this run

The current source-pinned chain is:

1. the newest Claude synthesis reduces the full theorem to one fixed no-pivot class; take `N3(1/128)`;
2. the O0 structural certificate supplies a physical two-anchor cross packet;
3. newest partner account03/B20 r20 converts that packet into only original-coordinate resources: exact doubly-transverse zero-edge mass, P2 physical second-compound mass, or one-sided transverse star reserves;
4. in `N3(1/128)`, P2 forces `E_2(D)>1/48`, while zero-edge/star packets require residual bank-size products at least `52`/`26`;
5. D5 pays P2 whenever `E_5(D)>=1/1024` by `<23.317`;
6. the completed third-volume split pays the substantial diffuse `E_3` branch (internally, at `<172.726` for the `theta=3/4` fractional-volume theorem), while concentrated volume marginals create a nested physical anchor packet;
7. the new theorem above reduces the low-`E_3` remainder to either a quantitatively genuine two-direction packet (4.2) or the high-dimensional spike/dust packet (4.3)-(4.4).

The fractional-volume `theta=3/4` theorem is a completed internal proof but has not yet received the two independent end-to-end reviews required for global closure, so it is used only as a conditional paid node here.

## 7. First unpaid universal implication

The earliest concrete unpaid implication inside this O0/no-pivot proof branch is now

`QFORM-N3-O0-GROUPED-DUST-PAYMENT-v1`:

under the original independent cap-one product source, arbitrary same-side blocks and all ambient couplings/spectrum, prove one universal linear small-ball/density estimate for each surviving source-realizable packet:

- the zero-edge doubly-transverse packet (2.4), now known to require `mn>=52`;
- the double-star packet from partner r20, now known to require `mn>=26`;
- the P2 low-`E_3` two-direction packet `sigma_1 sigma_2>1/sqrt(96)` without rotating the source;
- the P2 low-`E_3` spike/dust packet `sigma_1>3.079...`, `mn>=1205`;
- the substantial-`E_3` concentrated nested-anchor packet.

The explicit family (5.8) proves that the spike/dust bullet cannot be removed by a universal robust-second-direction lemma based only on the displayed R invariants. The next viable mechanism is therefore grouped original-coordinate hub/bank smoothing (including the proved two-hub mechanism when an actual zero hub block is obtained), or a volume/fractional-potential estimate that spends the dust collectively before any reciprocal local minor.

This is connected to the full target through the no-pivot equivalence and the O0 structural branch, but it does **not** by itself prove that every `N3(1/128)` matrix is already in this O0 packet. Any remaining upstream structural-exhaustion gate outside O0 remains part of the global proof graph.

## 8. Status

Full QFORM remains **OPEN / NOT PROVED / NOT DISPROVED**. The new target-family construction refutes only a proposed proof implication, not the conjecture. No new unrestricted continuity theorem is claimed.
