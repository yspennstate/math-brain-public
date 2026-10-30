SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet02, slot B04, 2026-09-24T02:14:06Z.
attacking: high-leverage residual routing via anchored E4 carrier promotion; optimize admissible third-volume weights and compare ridge on the same physical matrix.

# fleet02/B04 r17 — single-carrier entropy balancing versus anchored E4 hub

Programme: `QFORM-DENSITY-3EIG-20260922`.
Role: Product Fourier rearrangement / complementary constructions.
Status: **NEW SUPPORTING LEMMA / GLOBAL VOLUME-WEIGHT OPTIMIZATION / PARTNER APPLIED / FULL QFORM OPEN**.
Execution: `WITHOUT_VERIFIED_BRAIN`.

The unrestricted rough-input theorem remains open. This run isolates a useful carrier dichotomy inside the physical-volume route: if one physical row is the only over-heavy row of a third-volume law, arbitrary-weight Brascamp--Lieb can rebalance it at an exact geometric-mean determinant cost. On the newest fleet03/B04 high-E4-carrier matrix this globally repairs the canonical D/D' obstruction, but retaining the carrier as the partner's literal Fourier hub is still substantially stronger. This identifies deletion volume, not high marginal by itself, as the sharper obstruction.

## 1. Source boundary and completed inputs


Completed analytic inputs used at equations:

1. Pinned Claude/e5 Theorem D and its arbitrary-weight form, source
   `yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`,
   `proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/RESULTS.md` and `FOURIER_ROUTE_REPORT.md`.
   For a physical cross block and a supported physical 3-minor law with constrained-side row marginals at most `1/2`, determinant/entropy currency
   
   `G=exp(E_w log det(M_ST)^2+H(w))`
   
   gives
   
   `||p_Q||inf <=6 sqrt(e) G^(-1/6)`.
   
   The proved D' extension permits marginal cap `h<3/4` with prefactor
   
   `6 sqrt(e)(2h)^(-1/2)(3-4h)^(-1)`,
   
   and D5 gives `5 sqrt(2e) Z5^(-1/10)` without any marginal gate.

2. Newest designated partner fleet03/B04 r46, source
   `yspennstate/math-open-problems@171d82178a5f25c3a13692755cdb9c239372c79a`,
   `proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B04/20260924T014725Z-fleet03-B04-QFORM-auto11-r46/REPORT.md`.
   Its `QFORM-ANCHORED-E4-HUB-FOURIER-v1` keeps a literal carrier coordinate as a Fourier hub. At the concrete matrix below it proves
   
   `||p_Q||inf <=2.378720371807186...`
   
   with a continuous `C_0` density.

3. The completed ridge-density theorem, source
   `yspennstate/math-open-problems@9c1167db05c7b0f520f060796fde921ed769a4e7`,
   `proofnet24/QFORM-density/interactive/20260922T151048Z-ridge-window/REPORT.md`.
   If `K_gamma=BB^T(gamma^2 I+BB^T)^(-1)`, `theta=tr K_gamma`, `D_gamma=det(I+BB^T/gamma^2)`, and for some `1<=q<=2`
   
   `max_i (K_gamma)_ii <=q/2`, `theta>2q`,
   
   then
   
   `||p_Q||inf <= e/[sqrt(2q)gamma] * theta/(theta-2q) * D_gamma^(-1/(2theta))`.

## 2. New exact lemma — `QFORM-SINGLE-CARRIER-ENTROPY-BALANCE-v1`

Let `M=A[I,J]` be any literal original-coordinate cross block and, for every physical row triple `S subset I`, define

`z_S := sum_(T subset J, |T|=3) det(M_ST)^2`.

Assume `Z=sum_S z_S>0`, and write the canonical row-triple law

`nu(S)=z_S/Z`.

Fix one physical row `i`. Put

`W_1=sum_(S contains i) z_S`,
`W_0=sum_(S not containing i) z_S`,
`q_0=W_1/(W_0+W_1)`.

Assume `W_0,W_1>0` and `q_0>=1/2`. For a row-triple law `p`, put `q=P_p(i in S)`. At fixed `p`, the determinant/entropy objective of an arbitrary physical minor law is maximized over the conditional column choice by

`w(T|S)=det(M_ST)^2/z_S`,

and the exact log-sum identity gives

`log G(p)=H(p)+sum_S p_S log z_S=log Z-D(p||nu)`.             (2.1)

Split both `p` and `nu` according to whether `i in S`. KL chain decomposition gives

`D(p||nu)
 =D_Ber(q||q_0)
  +q D(p_1||nu_1)+(1-q)D(p_0||nu_0)
 >=D_Ber(q||q_0)`.                                            (2.2)

If the Theorem-D cap `q<=1/2` is imposed, then because `q_0>=1/2`, the Bernoulli divergence in (2.2) is minimized at `q=1/2`. Equality is attained by retaining the canonical conditional laws `nu_1,nu_0`. Therefore, provided this candidate's *other* physical row marginals are also at most `1/2`, it is the global optimizer over **all supported physical 3-minor weights**, and

`boxed: G_* = Z exp[-D_Ber(1/2||q_0)]
              =2 sqrt(W_0 W_1).`                              (2.3)

Consequently the pinned arbitrary-weight theorem gives

`boxed: ||p_Q||inf <=6 sqrt(e) [2 sqrt(W_0W_1)]^(-1/6).`       (2.4)

No individual minor is inverted. The currency is the geometric mean of the determinant mass anchored at the carrier and the determinant mass surviving its deletion.

The same argument with a cap `h in [1/2,3/4)` gives, whenever the canonical conditional candidate has all other marginals at most `h`,

`boxed: G_h=(W_1/h)^h (W_0/(1-h))^(1-h).`                     (2.5)

This is the exact global I-projection for the one-active-carrier regime, not a symmetric ansatz.

## 3. Apply the lemma to the newest partner's high-E4 carrier family

Use the r46 matrix at `epsilon=1/16`. Let `w_0,...,w_4` be dense orthonormal Hadamard directions in `R^8`. The physical `9x8` cross block has rows

- `16 w_0`;
- two copies of `w_1/sqrt2`;
- two copies of `w_2/sqrt2`;
- two copies of `w_3/sqrt2`;
- two copies of `(1/16)w_4/sqrt2`.

Thus its singular values are exactly

`16,1,1,1,1/16`,

and the symmetric pure-cross matrix

`A=[[0,M],[M^T,0]]`

has nonzero spectrum

`{+-16,+-1,+-1,+-1,+-1/16}`.

Hence it is genuinely rotated, indefinite, and has eight eigenvalues of modulus at least one. Every physical cross coefficient is nonzero.

For third volume the five direction-group squared singular weights are

`x=(256,1,1,1,1/256)`.

Cauchy--Binet gives

`E3=e3(x)=197635/256`,
`E4=e4(x)=66305/256`,
`E5=e5(x)=1`.                                                  (3.1)

A physical row triple has positive `z_S` exactly when it uses three distinct row directions, in which case `z_S` is the product of its physical row norm-squares. The canonical third-volume mass containing the carrier row `0` is

`W_1=256 e2(1,1,1,1/256)=771`,

whereas the deletion mass is

`W_0=e3(1,1,1,1/256)=259/256`.                                (3.2)

Therefore

`q_0=197376/197635=0.998689503377...>3/4`.                    (3.3)

So the **canonical** pinned D theorem and its D' extension are both inadmissible on this physical cut.

Now rebalance only the carrier inclusion to `q=1/2`, keeping the canonical conditional law inside the two strata. Each of the six duplicated strong physical rows then has marginal

`alpha_strong
 =(1/4)(171/257+258/259)
 =110595/266252
 =0.415377161486...<1/2`,                                     (3.4)

and each of the two weak rows has

`alpha_weak
 =(1/4)(1/257+3/259)
 =515/133126
 =0.003868515542...<1/2`.                                     (3.5)

Thus the candidate is feasible for every physical row. The exact global optimum from (2.3) is

`boxed: G_* =2 sqrt(771*259/256)
             =sqrt(199689)/8
             =55.8582189565689... .`                           (3.6)

Applying the completed pinned e5 arbitrary-weight Theorem D at the actual inequality gives

`boxed:
 ||p_(X^TAX)||inf
 <=6 sqrt(e) G_*^(-1/6)
 =6 sqrt(2e) 199689^(-1/12)
 =5.05961312687030... .`                                       (3.7)

This is a target-valid bound for every independent cap-one product input law.

## 4. Global optimization over the full D/D' exponent window

The previous calculation can be optimized over every proved D' cap, not only `h=1/2`. For `1/2<=h<3/4`, set the carrier inclusion to `q=h` and retain the canonical conditional laws. The other physical marginals decrease as `h` increases from `1/2`, so (3.4)-(3.5) show they remain strictly below `h`. Therefore (2.5) is the exact global determinant/entropy optimum at each `h`:

`G_h=(771/h)^h [(259/256)/(1-h)]^(1-h).`                       (4.1)

The globally optimized D' certificate at cap `h` is

`B(h)=6 sqrt(e)(2h)^(-1/2)(3-4h)^(-1)G_h^(-1/6).`             (4.2)

Its logarithmic derivative is

`d/dh log B
 =-1/(2h)+4/(3-4h)
  +(1/6)log[ h W_0 / ((1-h)W_1) ]`,                           (4.3)

and

`d^2/dh^2 log B
 =1/(2h^2)+16/(3-4h)^2
  +(1/6)(1/h+1/(1-h))>0`.                                     (4.4)

At `h=1/2`,

`d/dh log B
 =3+(1/6)log(259/197376)
 =1.893993707276...>0`.                                       (4.5)

By strict convexity, `B(h)` is increasing on the whole proved window. Thus

`boxed: h_*=1/2`

is the **global optimum over every supported physical third-minor weight and every D/D' exponent**. Equation (3.7) is not merely one convenient reweighting; it is the best certificate available from that entire theorem family on this cut.

The same argument works uniformly for the r46 family `0<epsilon<=1/16`. There

`W_1=768(1+epsilon^2)`,
`W_0=1+3epsilon^2`,

so

`G_*=2 sqrt(768(1+epsilon^2)(1+3epsilon^2))`

and the globally optimized ambient D/D' bound stays between `5.0597` and `5.0662` as `epsilon` decreases to zero. A canonical marginal tending to one is therefore not, by itself, a hard obstruction if deletion volume remains of target order.

## 5. Designated partner on the identical physical matrix

For the carrier row `0`, fleet03/B04 r46 computes the projected residual E3 packet exactly:

`Z3(C)=259/256`,
`H_0=259`,
`E4(M)=66305/256`,

with six strong residual physical marginals `129/259` and two weak marginals `3/518`. Its exact projected entropy currency is

`Gamma_0=0.9989708620178627...`,
`Omega_0=256 Gamma_0=255.73654067657284...`.

The completed hub-retaining theorem therefore gives the actual inequality

`boxed:
 ||p_(X^TAX)||inf
 <=2^(9/4) Omega_0^(-1/8)
 =2.378720371807186... .`                                      (5.1)

This directly applies the newest designated partner. It is stronger than the globally optimized ambient third-volume certificate (3.7) because retaining the high physical row as a Fourier hub spends its amplitude at the correct dimension rather than entropy-balancing it away.

## 6. Same-matrix ridge and pinned D5 comparisons

For the identical `M`, choose the explicit ridge scale

`gamma^2=g=1/4096`,

and set

`k_0=256/(256+g)=1048576/1048577`,
`k=1/(1+g)=4096/4097`,
`k_w=(1/256)/(1/256+g)=16/17`.

The physical ridge diagonal entries are `k_0` on the carrier, `k/2` on each strong duplicate and `k_w/2` on each weak duplicate, so the maximum is `k_0`. Take

`q=2k_0=2097152/1048577 in (1,2)`.

Then the leverage gate is saturated. Also

`theta=k_0+3k+k_w
      =1248484880/252707057
      =4.940443273810...`,

and

`theta-2q
 =237657616/252707057
 =0.940447088504...>0`.                                       (6.1)

Finally

`D_gamma=(1+256/g)(1+1/g)^3(1+(1/256)/g)
         =1048577*4097^3*17`.

The completed ridge theorem therefore yields the valid same-matrix certificate

`boxed: ||p_(X^TAX)||inf <=6.74879128551826... .`              (6.2)

I do not claim this displayed ridge scale is globally ridge-optimal; it is an exact admissible comparison on the same physical matrix.

The pinned marginal-free fifth-volume theorem has `Z5=E5=1`, hence

`boxed: ||p_(X^TAX)||inf <=5 sqrt(2e)
       =11.6582199079856... .`                                 (6.3)

Therefore the rigorously certified hierarchy on one and the same target-valid matrix is

`boxed:
 2.3787204  anchored-E4 hub (partner r46)
 <5.0596132  globally optimized ambient D/D'
 <6.7487913  explicit ridge certificate
 <11.658220  pinned D5.`                                       (6.4)

The canonical D/D' law itself is infeasible because of (3.3); only the globally optimized arbitrary physical weights repair it.

## 7. What this changes in the live gap

The new lemma separates two notions that were previously conflated in the high-leverage branch.

A large canonical row marginal is not intrinsically fatal. If the determinant mass `W_0` surviving deletion of that row is still substantial, the exact KL projection pays the carrier at geometric-mean currency `2 sqrt(W_0W_1)`, with no reciprocal local minor. The real ambient-volume obstruction is simultaneous carrier concentration **and** small deletion volume (or collision of several row caps).

Conversely, the partner r46 result shows that when a physical row carries fourth exterior volume, retaining it as a literal Fourier hub can be much more efficient than any ambient reweighting. The two mechanisms are therefore complementary rather than competing formulations of the same inequality.

The first unpaid implication is sharpened to

`QFORM-HIGHLEVERAGE-RESIDUAL-TO-CARRIER-DELETION-DICHOTOMY-v1`:

> From the remaining high-physical-leverage or small-`s_3` zero-anchor C1 residual, produce a literal original-coordinate crossing for which either (a) an over-heavy E3 carrier has target-scale product `W_0W_1`, so `QFORM-SINGLE-CARRIER-ENTROPY-BALANCE-v1` plus pinned Theorem D pays it, or (b) deletion E3 volume is genuinely small and the carrier promotes to a target-scale anchored E4/fixed-pair hub paid by fleet03/B04 r46, or else route the low compound packet into an already completed rank-two star, pair-log, square-bank, ridge or grouped-hub receiver. No small rough quadratic tail may be deleted perturbatively, and no vanishing local coefficient may be inverted.

That structural implication, not the analytic receiver on either side, remains unpaid. Full QFORM remains OPEN.
