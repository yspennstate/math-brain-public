SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B07, 2026-09-24T04:06:07Z.
attacking: the exact-singular low-pivot h=2 survivor; cancel the vanishing pair scale against the forced third cross-E2 resource, then select one physical cut carrying both the diffuse determinant star and a constant tau-weighted E2 packet.

# account01/B07 r41 — tau-cancelled same-cut E2 localization on the exact-singular h=2 branch

Programme: `QFORM-DENSITY-3EIG-20260922`  
Role: coordinate minor selection  
Status: `NEW SUPPORTING THEOREM / DESIGNATED PARTNER APPLIED / FULL QFORM OPEN`  
Continuity: not proved by the new theorem; full-target continuity remains OPEN.  
Execution: `WITHOUT_VERIFIED_BRAIN`.

## 1. Source boundary


The immediate predecessor is account01/B07 r40b,

`yspennstate/math-open-problems@91fa874bd38adeb9a45c969ebf1de219816a9892`,

`proofnet24/QFORM-density/fleet-2026-09-22/account01/B07/20260924T033250Z-account01-B07-qform-auto11-r40b/REPORT.md`.

Its exact-singular low-pivot h=2 branch gives one literal physical pair `H={h_1,h_2}`. Put `O=H^c`,

`B=A[H,H]=tau ell ell^T`, `tau!=0`, `||ell||=1`,

let `k` be a unit vector perpendicular to `ell`, set

`U=A[O,H]`, `q=Uk`, `s=||q||_2`,

and let `D_H(r,c)=det A[(H,r),(H,c)]` be the full bordered-minor matrix. Then r40b proves the exact original-coordinate identities and inequalities

`D_H=-tau q q^T`,                                                (1.1)

`L:=||D_H||_op=|tau|s^2 >=7/96`,                               (1.2)

`|tau|<1/32`,                                                     (1.3)

`max_r q_r^2/s^2 <1/7`.                                         (1.4)

It also spends the global owner hypothesis `s_3(A)>=1` before any reciprocal pair selection and obtains the third-resource fork

`s_2(U)>31/64`                                                    (1.5)

or

`||A[O,O]||_op>31/64`.                                          (1.6)

The present run treats (1.5). The residual-curvature branch (1.6) was already routed in r40b to a physical square or a simultaneous residual crossing plus determinant-star cut.

The latest completed designated partner account02/B07 consumed here is

`yspennstate/math-open-problems@ec29bb4321feffe020e5cb0185d148f2f6de847e`,

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B07/20260924T013622Z-account02-B07-qform-auto11/REPORT.md`.

Its theorem `QFORM-E2-BOUNDED-SUPPORT-BALANCE-v1` states, for a physical block `K` of rank `r>=2`,

`E2(K):=e_2(KK^T) <=(r-1)s_2(K)^2 ||K||_F^2`,                  (1.7)

with the bounded-entry consequence

`s_2(K) >= [E2(K)/((r-1)pqL_0^2)]^(1/2)`                        (1.8)

for a `p x q` block whose entries have modulus at most `L_0`. The partner correctly records that diffuse E2 need not force a dimension-free balanced second singular direction without a support/balance input.

## 2. The vanishing pair scale cancels against the forced cross-E2 packet

Assume the cross-E2 branch (1.5). Because `k` is a unit vector,

`s_1(U)>=||Uk||=s`.                                               (2.1)

Since `U` has exactly two columns,

`E2(U)=s_1(U)^2 s_2(U)^2`.                                       (2.2)

Combining (1.2), (1.5), (2.1), and (2.2) gives the central scale cancellation

`|tau| E2(U)
 >= |tau|s^2 s_2(U)^2
 > (7/96)(31/64)^2
 =6727/393216`.                                                   (2.3)

Numerically,

`6727/393216 = 0.0171076456705729...`.                            (2.4)

This is already qualitatively different from the r40b bound `E2(U)>0.055`: as `|tau|->0`, the complete physical two-minor packet of the pair-to-residual block must grow at least like `1/|tau|`. Thus the small exact-singular core cannot simultaneously make its kernel-star large and leave only a fixed-size transverse E2 resource.

No coordinate rotation is used in (2.3). Although the proof uses the kernel direction `k` to estimate `s_1(U)`, `E2(U)` is the original-coordinate Cauchy--Binet sum

`E2(U)=sum_{r<c in O} det A[{r,c},H]^2`.                          (2.5)

The two columns are the literal physical pair `H`.

## 3. Main theorem: one physical cut carries both currencies

Define the normalized kernel-star coordinate law

`p_r=q_r^2/s^2`, `sum_r p_r=1`.                                  (3.1)

By (1.4), `max_r p_r<1/7`. For a physical cut `O=R union S`, define

`P_R=sum_{r in R}p_r`,                                           (3.2)

and the cross-cut physical E2 packet

`E_RS=sum_{r in R,c in S} det A[{r,c},H]^2`.                     (3.3)

### Theorem — `QFORM-EXACTSINGULAR-TAU-CANCELLED-SAMECUT-E2-v1`

Under (1.1)--(1.5), there exists a literal original-coordinate partition `O=R union S` such that

`1/10 < P_R < 9/10`,                                             (3.4)

`E_RS > (31/112)E2(U)`,                                          (3.5)

and consequently

`boxed: |tau| E_RS > 29791/6291456 >0.0047351519.`               (3.6)

On the same cut the overlap-two bordered-minor star obeys

`boxed: ||D_H[R,S]||_op >7/320 =0.021875.`                        (3.7)

Finally, one of the two literal physical hub coordinates `h in H` has

`|A_hh|>=|tau|/2`,                                                (3.8)

and therefore the same cut satisfies the entirely source-coordinate product currency

`boxed:
 |A_hh| E_RS
 >29791/12582912
 =0.0023675759633382... .
}`                                                               (3.9)

Thus the small-`|tau|` exact-singular collar has been converted into a constant physical scalar-coefficient times physical cross-E2 packet, while retaining a constant piece of the exact bordered determinant star on the SAME residual partition. No tiny minor is selected or inverted.

### Proof

Choose a uniformly random independent Bernoulli cut of the residual coordinates. Each unordered pair `{r,c}` is separated with probability `1/2`, so

`E E_RS = (1/2)E2(U)`.                                           (3.10)

Also

`E P_R=1/2`,

`Var(P_R)=(1/4)sum_r p_r^2 <1/28`,                               (3.11)

using `sum p_r^2 <=(max p_r)sum p_r<1/7`. Therefore Chebyshev gives

`P{|P_R-1/2|>=2/5}< (1/28)/(4/25)=25/112`.                       (3.12)

Call the complement of this event `G`; on `G`, (3.4) holds. Since always `0<=E_RS<=E2(U)`,

`E[E_RS 1_G]
 >= E E_RS-E2(U)P(G^c)
 > (1/2-25/112)E2(U)
 = (31/112)E2(U)`.                                                (3.13)

Hence at least one good physical cut obeys (3.5). Multiplying by (2.3) gives

`|tau|E_RS
 > (31/112)(6727/393216)
 =29791/6291456`,                                                 (3.14)

which is (3.6).

For that same cut, (1.1) gives

`||D_H[R,S]||_op
 =|tau| ||q_R|| ||q_S||
 =L sqrt(P_R(1-P_R))`.                                           (3.15)

Under (3.4), `P_R(1-P_R)>9/100`; hence

`||D_H[R,S]||_op >(3/10)L >=7/320`,                              (3.16)

proving (3.7). This sharpens r40b's safe but nonsharp `L/10` lower bound on any cut already known to lie in the interval `(1/10,9/10)`.

Finally `B=tau ell ell^T`, so its literal diagonal entries are `tau ell_1^2,tau ell_2^2`. Since `max(ell_1^2,ell_2^2)>=1/2`, some `h in H` obeys (3.8); combine with (3.6) to obtain (3.9). QED.

## 4. Designated partner account02/B07 applied to the new packet

Apply the completed partner inequality (1.7) directly to the actual physical block `U=A[O,H]`, whose rank is two on the present branch. From (2.3),

`|tau| s_2(U)^2 ||U||_F^2
 >= |tau|E2(U)
 >6727/393216`.                                                  (4.1)

Hence

`boxed:
 sqrt(|tau|) s_2(U)||U||_F
 > sqrt(6727/393216)
 =0.130796198991304... .
}`                                                               (4.2)

This is an equation-level use of the newest completed designated-partner theorem. It shows that the tiny-`tau` collar cannot hide the regenerated E2 packet in a simultaneously small product of second singular scale and total physical cross energy.

The bounded-support version is also explicit. If a literal row core `J subset O` of cardinality `m` carries at least half of `E2(U)` and

`max_{r in J,h in H}|A_rh|<=L_0`,                                (4.3)

then the partner's bounded-entry consequence (1.8), with `p=m,q=2,r=2`, gives

`boxed:
 s_2(U[J,H])
 > sqrt(6727/393216)/(2 sqrt(m|tau|) L_0)
 =0.0653980994956522.../(sqrt(m|tau|)L_0).
}`                                                               (4.4)

Thus bounded physical support becomes increasingly balanced as `|tau|->0`; if no such core exists, the determinant currency is genuinely support-diffuse, exactly the alternative identified by the partner stress theorem.

## 5. What this does and does not close

This run does NOT prove the full conjecture and does not prove continuity on the exact-singular survivor. The existing exact rank-one-pair receiver

`yspennstate/math-open-problems@9c6683c03c8b0dbd635314109854871448343055`,

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B09/20260924T021301Z-account02-B09-QFORM-r16/REPORT.md`,

still gives only

`||p_Q||_infinity <=2^(5/2)(|tau| ||q||)^(-1/2)`,                (5.1)

which deteriorates like `|tau|^(-1/4)` after (1.2). Its own target-valid example proves that this worst-slice half-Riesz interface cannot simply be perturbed across a near-rank-one pair.

The new theorem identifies the correct missing analytic interface more sharply: on the hard exact-singular cross-E2 branch there is now ONE literal partition carrying simultaneously

1. a diffuse zero-kernel determinant-star crossing `||D_H[R,S]||_op>7/320`;
2. a physical two-minor packet with `|tau|E_RS>29791/6291456`;
3. one literal hub diagonal with `|A_hh|E_RS>29791/12582912`.

The remaining receiver must spend these currencies jointly while retaining arbitrary residual same-bank curvature. It may not condition the third resource away before the half-Riesz step.

I record the next B07 obligation as

`QFORM-SAMECUT-STAR-PLUS-TAU-E2-DEPENDENCE-SAFE-RECEIVER-v1`.

The residual-curvature alternative from r40b is also slightly sharpened by (3.16): whenever its simultaneous cut has `1/10<P_R<9/10`, the retained determinant-star operator norm is `>7/320`, not merely `>7/960`.

## 6. Regression checks

A deterministic finite checker was run on 100 random exact-singular coefficient packets with 12 residual coordinates, normalized so that (1.2), (1.4), and (1.5) hold. Exhaustive enumeration of all physical cuts found zero violations of (2.3), (3.5), or (3.7). The smallest observed best-good-cut ratio `E_RS/E2(U)` was about `0.724`, well above the proved `31/112`. These checks are regression evidence only; the proof is Sections 2--4.

## 7. Status

Supporting theorem proved: `QFORM-EXACTSINGULAR-TAU-CANCELLED-SAMECUT-E2-v1`.

Full QFORM: **OPEN / not proved / not disproved**.  
Full-target continuity: **OPEN**.  
Native brain ingestion: **not verified**; retain `WITHOUT_VERIFIED_BRAIN`.
