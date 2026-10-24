SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B19, 2026-09-23T13:07:09Z.
attacking: the first global low-leverage / extra-spectrum N3 gate by composing the proved spectral-window ridge receiver with a much smaller fixed no-pivot scale, so every ridge failure becomes a literal original-coordinate hub with a balanced star and a large leaf cross packet.

# account02/B19 auto11 — tiny-N3 spectral-window collapse to STAR4

Programme: `QFORM-DENSITY-3EIG-20260922`  
Role: Universal proof assembly / SYNTHESIS  
Status: **ESSENTIAL_STEP_APPLIED / GLOBAL LOW-LEVERAGE ANNULUS REMOVED / STAR4 FRONTIER / FULL QFORM OPEN**  
Execution: **WITHOUT_VERIFIED_BRAIN**

The unrestricted theorem remains OPEN. Nothing below assumes moments, compact or connected support, iid laws, log-concavity, diagonal-basis independence, or independence after any rotation/projection. Every probabilistic bank is a bank of ORIGINAL coordinates. No small quadratic random term is discarded. Continuity is asserted only on cited Fourier branches that prove it.

## 1. Fresh source graph and why the no-pivot scale may be changed

The owner-controlled geometric synthesis

`yspennstate/math-open-problems@472b70df7d1edbb3afac23269bc2e4368ae0e371`,
`proofnet24/QFORM-density/interactive/20260922T225732Z-claude-synthesis/GEOMETRIC_SYNTHESIS.md`, Theorem 5.1,

proves: for **any fixed** `tau in (0,1]`, a universal density theorem on the strict no-`tau`-pivot class implies the full QFORM conjecture. Thus a proof is free to choose one convenient universal `tau`; it is not necessary to stay at `1/64`.

I choose throughout

`tau := 2^-20 = 1/1048576`.                                      (1.1)

Hence the live no-pivot hypotheses are

`s_3(A)>=1`,
`|A_ii|<tau`,
`|A_ii A_jj-A_ij^2|<tau` for every `i!=j`.                       (1.2)

The pair condition implies the literal physical edge cap

`A_ij^2 < tau+tau^2 =: w`.                                      (1.3)

The newest compatible account01/B20 completed theorem used here is
`QFORM-SPECTRAL-WINDOW-1OVER16-v1`, canonical source

`yspennstate/math-open-problems@5593a06e6c0d8a346375176fc18181171fdc7ed9`,
`proofnet24/QFORM-density/fleet-2026-09-22/account01/B20/20260923T122603Z-account01-B20-QFORM-auto11/REPORT.md`.

Let

`P_16 := 1_{|A|>=1/16}`.                                        (1.4)

That theorem proves that if

`max_i (P_16)_ii <=1/50`,                                      (1.5)

then for arbitrary cap-one product inputs

`||p_Q||_infinity <= 5400 sqrt(e)/(29 sqrt(2))`
`                  =217.084094838352... <217.085`,              (1.6)

with a continuous `C_0` density. It retains the entire spectral tail below `1/16`; no random perturbation is deleted.

The owner-required newest-Claude package at

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`,
`proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/`,

was reread at `RESULTS.md`, `FOURIER_ROUTE_REPORT.md`, and `COUNTEREXAMPLE_SEARCH.md`. The completed `D_5` theorem from that package is applied below to an actual physical leaf cut.

## 2. New theorem: a failed `1/16` spectral window forces a strong literal star at tiny N3 scale

### Theorem `QFORM-N3-TINYTAU-WINDOW-STAR-v1`

Assume (1.2). If (1.5) fails, there is an ORIGINAL physical coordinate `h` such that

`(P_16)_hh>1/50`.                                                (2.1)

For that same physical coordinate,

`sum_(j!=h) A_hj^2 > 1/12800-tau^2`.                            (2.2)

Moreover the leaves can be partitioned into two disjoint ORIGINAL-coordinate banks

`h^c=J disjoint_union K`                                        (2.3)

such that simultaneously

`sum_(j in J) A_hj^2 > beta`,
`sum_(k in K) A_hk^2 > beta`,                                   (2.4)

where

`beta := (1/12800-tau-2tau^2)/2`
`      =1060634599/27487790694400`
`      =0.000038585661932302174...`.                             (2.5)

In particular `beta>40.45 tau`.

#### Proof

By spectral calculus,

`A^2 >= (1/16)^2 P_16 = (1/256)P_16`                             (2.6)

in positive-semidefinite order. Hence (2.1) gives

`(A^2)_hh >1/(256*50)=1/12800`.                                 (2.7)

Since `(A^2)_hh=A_hh^2+sum_(j!=h)A_hj^2` and `|A_hh|<tau`, (2.2) follows.

Write `w_j=A_hj^2`. By (1.3), every atom is `<w=tau+tau^2`. Sort the nonzero `w_j` decreasingly, append one zero if necessary, pair consecutive weights, and orient each pair one endpoint into `J` and the other into `K`. For every such orientation,

`|sum_J w_j-sum_K w_j| <=(w_1-w_2)+(w_3-w_4)+... <=w_1<w`.       (2.8)

Using total mass greater than `1/12800-tau^2`, each side is therefore strictly larger than

`[(1/12800-tau^2)-(tau+tau^2)]/2=beta`,                         (2.9)

which proves (2.4). No random input has been repartitioned or rotated; this is deterministic coefficient bookkeeping. QED.

### Stronger multi-bank form

The same numbers actually permit many banks. Since

`1/12800 = (2048/25)tau =81.92 tau`,                            (2.10)

a greedy minimal-mass construction gives **41 pairwise disjoint ORIGINAL leaf banks**, each with hub-star square mass at least `tau`: after 40 minimal banks, each of mass `<2tau+tau^2`, the remaining mass is still larger than

`(2048/25)tau-tau^2-40(2tau+tau^2)`
`=(48/25)tau-41tau^2>tau`.                                     (2.11)

The two-bank version is used below because it can be synchronized with a large leaf cross cut.

## 3. Synchronize the balanced star with an order-one physical leaf cross block

Let `T=h^c` and `B=A[T,T]`. Write `p` for the number of eigenvalues of `A` at least `1` and `q` for the number at most `-1`. Since `p+q>=3`, Cauchy interlacing after deleting one coordinate gives at least

`max(p-1,0)+max(q-1,0)>=1`                                     (3.1)

leaf-block eigenvalue of modulus at least one. Hence

`||B||_op>=1`.                                                  (3.2)

Put `D=diag(B)` and `Z=B-D`. From `||D||_op<tau`,

`||Z||_op>1-tau`,
`||Z||_F^2>(1-tau)^2`.                                         (3.3)

Return to the paired orientation proof of Section 2. For two leaves belonging to distinct predetermined pairs, the ordered event `j in J,k in K` has probability `1/4`; for leaves forming one predetermined pair it has probability `1/2`. Therefore every off-diagonal ordered coefficient contributes to

`E ||A[J,K]||_F^2`

with probability at least `1/4`, and

`E ||A[J,K]||_F^2 >= (1/4)||Z||_F^2
                       >(1-tau)^2/4.                            (3.4)

The star balance (2.4) holds for **every** pair orientation, so an orientation attaining the expectation in (3.4) simultaneously satisfies both conclusions. Thus there is one literal physical cut with

`boxed: ||A[J,K]||_F^2 > E0 :=(1-tau)^2/4}`                    (3.5)

and the two star masses (2.4).

Numerically

`E0=0.24999952316306917...`.                                    (3.6)

This step uses only interlacing, the strict N3 diagonal cap, and deterministic/randomized existence on physical indices.

## 4. Required newest-Claude result applied: D5 pays the diffuse part of that exact cut

Let `N=A[J,K]` be the cut in Section 3 and write

`x_r=s_r(N)^2`, `E=sum_r x_r=||N||_F^2`.                        (4.1)

Use the elementary occupancy lemma already proved in the account01/B20 compiler: if

`sum_(r=1)^4 x_r <=(1-eta)E`,                                   (4.2)

then

`e_5(x)>=eta^4 E^5/120`.                                        (4.3)

Indeed, after normalizing `p_r=x_r/E`, five iid draws are all distinct with probability `120e_5(p)`; while at most four distinct indices have appeared, the already-seen mass is at most the sum of the four largest `p_r`, so draws 2--5 are new with conditional probability at least `eta`.

Take `eta=1/64`. If

`sum_(r<=4)s_r(N)^2 <=(63/64)||N||_F^2`,                        (4.4)

then (3.5), (4.3), and the completed owner-required `D_5` theorem give at the **actual physical cross block** `N`

`||p_Q||_infinity`
` <=5 sqrt(2e) e_5(N^TN)^(-1/10)`
` <5 sqrt(2e)
`   [120/((1/64)^4 E0^5)]^(1/10)`
` =198.63362442792362... <198.634`.                             (4.5)

All same-bank quadratic terms, signs, outside couplings and affine terms remain present; this is exactly the stated scope of `D_5`.

Consequently every unpaid state after Sections 1--4 carries one physical hub/cut packet satisfying

`sum_(j in J)A_hj^2>beta`,
`sum_(k in K)A_hk^2>beta`,                                      (4.6)

`||N||_F^2>E0`, and

`boxed:
 sum_(r=1)^4 s_r(N)^2 >(63/64)||N||_F^2
                  >63(1-tau)^2/256.}`                          (4.7)

The final numerical lower bound is

`63(1-tau)^2/256=0.24609328061364621...`.                       (4.8)

Call this residual packet `STAR4(tau,beta,E0)`.

## 5. New rank-two versus relative-rank-one dichotomy inside STAR4

The four-direction concentration in (4.7) has a useful automatic refinement.

### Lemma `QFORM-STAR4-RANK2-OR-RELATIVE-RANK1-v1`

Let `s_1>=s_2>=...` be the singular values of `N` in a STAR4 packet.

Either

`boxed: s_2>s_1/16,}`                                           (5.1)

in which case

`boxed:
 s_1s_2 > rho_*:=63(1-tau)^2/16384
             =0.003845207509588222...;}`                        (5.2)

or

`boxed:
 (sum_(r>=2)s_r^2)^(1/2) <=s_1/6.}`                             (5.3)

Thus the second branch is an actual Frobenius-relative rank-one tube; no singular direction is deleted from the quadratic form.

#### Proof

From (4.7), `4s_1^2>=sum_(r<=4)s_r^2>63E/64>E0*63/64`, hence

`s_1^2>63(1-tau)^2/1024`.                                       (5.4)

If (5.1) holds, multiply by `s_1/16` to obtain (5.2).

Otherwise let `R=sum_(r>=2)s_r^2`. Then `s_2,s_3,s_4<=s_1/16`, while (4.7) says the tail after the first four singular directions is `<E/64=(s_1^2+R)/64`. Hence

`R <=3s_1^2/256+(s_1^2+R)/64`.                                 (5.5)

Rearranging gives

`(63/64)R <=7s_1^2/256`,

so exactly

`R<=s_1^2/36`,                                                  (5.6)

which is (5.3). QED.

This is the direct attack on the first new gap: every global N3 survivor is now either a **quantitative rank-two physical leaf cross packet** or a **relative rank-one physical leaf cross tube**, and in both cases the same literal hub has two quantitative disjoint star banks.

## 6. Current designated partner account03/B19 applied at equation level

The newest completed account03/B19 result found at the dependency refresh was r33,
`QFORM-TRIANGLE-PAIR-TRANSFER-RECONDITIONING-v1`, canonical source

`yspennstate/math-open-problems@f534d70a365f444c54234cd0c88f97c5201b27d6`,
`proofnet24/QFORM-density/fleet-2026-09-22/account03/B19/20260923T114327Z-account03-B19-QFORM-r33/REPORT.md`.

Its exact-rank-three TRIANGLE state has rank-two cross product `rho`, physical pair covariance determinant `d>377/1344`, and residual pair-complement determinant `r_T`. It proves

`||p_Q||_infinity
 <=C_* d^(-1/4) rho^(-3/8) r_T^(-3/16),`
`C_*=2^(15/4)3^(-3/8).`                                        (6.1)

At its live source constants

`rho>=sqrt(29/3072)`, `r_T>=1/64`,                              (6.2)

the actual inequality is

`||p_Q||_infinity<64.019<65`.                                   (6.3)

This splice remains valid inside the global proof graph whenever an exact-rank-three STAR4 descendant independently satisfies the partner's TRIANGLE hypotheses. I do **not** infer those hypotheses merely from (4.6)--(4.7), and I do not truncate a higher-rank cross block to manufacture them. The current designated partner therefore removes its genuine subbranch without being overextended.

## 7. Strongest source-pinned full proof graph after this run

1. **Full target -> `N3(2^-20)`.** By the owner-pinned Gaussian-padding / physical-pivot synthesis, proving one fixed `N3(tau)` suffices for any `tau in (0,1]`.
2. **Spectral-window diffuse exit.** If `max_i(P_16)_ii<=1/50`, account01/B20's completed ridge theorem gives (1.6), `<217.085` and continuous density.
3. **Every ridge failure -> one physical balanced star/cross cut.** Sections 2--3 give one literal hub `h` and physical leaves `J,K` with star energies `>beta` on both sides and `||A[J,K]||_F^2>E0`.
4. **Diffuse fifth-volume exit.** If the leaf cross energy is not `63/64` concentrated in its first four singular directions, the owner-required D5 theorem gives `<198.634`, continuously.
5. **Only remaining global packet: `STAR4`.** It has (4.6)--(4.7), and Section 5 splits it into a quantitative rank-two branch (5.1)--(5.2) or a relative-rank-one tube (5.3).
6. **Existing exact-rank-three TRIANGLE splice.** Whenever the independent r33 hypotheses hold, (6.1)--(6.3) pay that subbranch.

This composition removes the previously listed global `QFORM-N3-LOWLEVERAGE-EXTRASPECTRUM-PAYMENT-v1` / `[1/16,1)` annulus state as a separate debt: the small fixed no-pivot scale turns every failed spectral-window leverage test directly into a many-leaf physical star.

## 8. First unpaid implication now

The first global unpaid implication can be stated without spectral projections:

`QFORM-N3-TINYTAU-STAR4-PAYMENT-v1`:

> Let `tau=2^-20`. For arbitrary finite dimension, arbitrary independent cap-one product laws, and every symmetric `A in N3(tau)` carrying a literal physical hub/cut `h | J | K` with
> 
> `sum_(J)A_hj^2>beta`, `sum_(K)A_hk^2>beta`,
> 
> `||A[J,K]||_F^2>E0`, and
> 
> `sum_(r<=4)s_r(A[J,K])^2 >(63/64)||A[J,K]||_F^2`,
> 
> prove one universal linear interval/density bound, or descend source-preservingly to an already-paid grouped-square, mixed-hub, physical-pair, D/D'/D5, ridge, finite-core, or exact-rank-three TRIANGLE receiver.

The immediate subproblem is the Section 5 dichotomy: combine the **rank-two cross branch** with the same-side third spectral source, or absorb the **relative rank-one tube** without deleting its nonzero tail. The tail in (5.3) is only relatively small; arbitrary unbounded product inputs forbid treating it as a small random perturbation.

This frontier is strictly narrower than the prior low-leverage/annular extra-spectrum gate: it is entirely stated in literal physical coefficients and singular values of one actual leaf cross block.

## 9. Corrections and status

The construction does not infer independence of `P_16 X`, of singular-vector projections, or of any rotated coordinates. The MSS/ridge theorem is used only through its already-proved physical-cut conclusion. The randomized pair orientation is a deterministic existence proof on coefficient indices, not randomization of the input law. No worst-fiber supremum, arbitrary-joint coarea, pointwise quadratic-phase decay, one-good-minor selection, or coefficient-continuity argument is used.

No counterexample is produced. Full QFORM and full-target continuity remain OPEN. There are not two independent end-to-end reviews, so no full-proof claim is made.
