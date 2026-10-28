SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account 01, slot B01, 2026-09-23T03:08:21Z.
attacking: aggregate star-wedge half-Riesz synthesis: combine a diffuse two-minor star with one-row random-slope decay so the total wedge energy is spent before selecting a tiny partner row.

# Aggregate star-wedge half-Riesz synthesis

Run: `20260923T030821Z-account01-B01-qform-auto11`  
Programme: `QFORM-DENSITY-3EIG-20260922`  
Role: account01/B01, Oscillatory replacement  
Status: **ESSENTIAL_STEP_APPLIED / FULL QFORM OPEN**  
Execution: `WITHOUT_VERIFIED_BRAIN`.

## 1. Exact target and correction boundary

The target remains open: for every dimension, independent real coordinates with densities bounded by one, and every real symmetric matrix with at least three eigenvalues of modulus at least one, prove a universal finite bound for the density of `Q=X^TAX`, or give a valid counterexample. Continuity is a separate requested conclusion.

No Gaussianity, moments, compact support, connected support, log-concavity, or independence after spectral rotation is used below. The phase-aligned scalar counterexample is retained: for a prescribed frequency `s`, one can choose a cap-one density supported on finitely many intervals contained in `{x:dist(sx^2,2pi Z)<=delta}`, of total measure one, and force `Re E exp(isX^2)>=cos(delta)`. Thus no law-uniform scalar pointwise power decay is used or asserted.


## 2. Dependencies actually used

### 2.1 B01 mixed-order determinant/Fourier theorem

Earlier account01/B01 report:

`yspennstate/math-open-problems@86f318f0826325e6df3504e1e8ec15f4316cc861`

`proofnet24/QFORM-density/fleet-2026-09-22/account01/B01/20260923T001242Z-b01-qform-auto11/REPORT.md`.

For disjoint original-coordinate sets `I,J`, with physical cross block `M=A[I,J]`, let `Omega` be a probability law on nonzero square minors `(S,T)` of possibly varying order. Put

`alpha_i=P(i in S)`, `beta_j=P(j in T)`, `kbar=E|S|`,

and

`K(Omega)=exp(E log det(M_ST)^2 + H(Omega))`.

If `alpha_i<=1/2` for every row coordinate, then the proof gives, for every `kbar>0`,

`|phi(t)| <= min(1, e^(kbar/4)(2pi)^(kbar/2) K(Omega)^(-1/4)|t|^(-kbar/2)).`       (2.1)

The earlier report used `kbar>2` only at the final L1 Fourier-inversion step. The determinant/BL proof of (2.1) itself does not require that inequality.

The same proof also allows the order-zero determinant term `(S,T)=(empty,empty)` with `det(empty)=1`: the diagonal-plus-PSD determinant expansion contains this positive term. In the application below every column marginal is `<1`, so its coefficient is nonzero. This extension changes no analytic step.

### 2.2 B01 row-aggregate random-slope theorem

Earlier account01/B01 report:

`yspennstate/math-open-problems@e398e885cc1902a2484e86973dd016a68721ec5c`

`proofnet24/QFORM-density/fleet-2026-09-22/account01/B01/20260922T183610Z-b01-qform-auto11/REPORT.md`.

For an arbitrary quadratic form `R=X^TSX`, one original coordinate `i`, and a disjoint original-coordinate bank `J`, write `r_i=S[i,J]` and `rho=||r_i||_2`. Then

`|phi_R(t)| <= min(1, sqrt(pi C_1/(rho |t|))),`                    (2.2)

where `C_1` is the universal one-dimensional product-projection density constant. The current projection source permits `C_1<=sqrt(2)`. The proof is Plancherel in the random *linear slope*, not scalar quadratic-phase decay, and permits arbitrary curvature on every retained block.

### 2.3 Designated partner account02/B01 r35

Latest completed partner report:

`yspennstate/math-open-problems@0bc769a70ba86df2c5bc5b73b5e5bbfe6021cfd8`

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B01/20260923T030247Z-account02-B01-qform-r35/REPORT.md`.

If two physical hub coordinates `X=(X1,X2)` and an independent leaf bank `Y` appear as

`S=X^T C X+2X^T(MY+c)+R(Y)`,

with arbitrary symmetric `C`, arbitrary measurable `R`, and rank-two `M`, and

`D=det(MM^T)>0`,

then

`H_(1/2)(S):=sup_s E|S-s|^(-1/2) <= 2^(11/4) D^(-1/8).`           (2.3)

Section 5 below applies this theorem at an actual inequality.

## 3. Fractional-Riesz form of the mixed-order theorem

The first new observation is that density inversion needs mean determinant order `>2`, but a fractional potential needs much less.

### Lemma 3.1 (mixed-order beta-Riesz compiler)

Assume (2.1), let `0<beta<1`, and suppose

`kbar>2 beta`.

Then

`H_beta(R):=sup_s E|R-s|^(-beta)`

obeys

`H_beta(R)
 <= [kbar/{beta(kbar-2beta) Gamma(beta) cos(pi beta/2)}]
    e^(beta/2)(2pi)^beta K(Omega)^(-beta/(2kbar)).`               (3.1)

In particular, at `beta=1/2`, every `kbar>1` gives

`boxed: H_(1/2)(R)
 <= 4 e^(1/4) [kbar/(kbar-1)] K(Omega)^(-1/(4kbar)).`             (3.2)

### Proof

Write

`a=kbar/2`,
`B=e^(kbar/4)(2pi)^(kbar/2)K(Omega)^(-1/4)`.

Then (2.1) is `|phi_R(t)|<=min(1,B|t|^-a)`. The Riesz representation

`|x|^-beta = [Gamma(beta)cos(pi beta/2)]^-1
              int_0^infinity cos(tx)t^(beta-1)dt`

and `a>beta` give

`H_beta(R)
 <= c_beta int_0^infinity t^(beta-1)min(1,Bt^-a)dt`
` = c_beta [a/{beta(a-beta)}] B^(beta/a)`,

where `c_beta=[Gamma(beta)cos(pi beta/2)]^-1`. Since

`B^(beta/a)=e^(beta/2)(2pi)^beta K(Omega)^(-beta/(2kbar))`,

this is (3.1). At `beta=1/2`, `c_beta=sqrt(2/pi)` and the constants simplify to (3.2). QED.

The important threshold is now

`kbar>1`,

not `kbar>2`.

## 4. Star geometry in a physical cross block

Fix a physical cross block `M=A[I,J]` and a row `i in I`, with row vectors `r_j`. Define the total pair-wedge energy through `i` by

`H_i := sum_(j!=i) ||r_i wedge r_j||^2`
`     = sum_(j!=i) sum_(|T|=2) det(M_{{i,j},T})^2.`                (4.1)

Assume `H_i>0`. Write

`W_j=||r_i wedge r_j||^2`,
`q_j=W_j/H_i`,
`rho=||r_i||_2`.

Thus `q` is a probability distribution on partner rows.

The natural order-two **star law** `omega_2` samples a physical minor `({i,j},T)` with probability

`det(M_{{i,j},T})^2/H_i`.

Its entropy-determinant currency is exactly

`K(omega_2)=H_i`,                                                   (4.2)

its row marginal at `i` is one, and the marginal at `j` is `q_j`.

## 5. Concentrated star: direct application of account02/B01 r35

Suppose first that some partner row `j` has

`q_j>1/2`, equivalently `W_j>H_i/2`.

Condition on all original coordinates in `I\{i,j}` and all coordinates outside `I union J`. The remaining quadratic polynomial in physical hubs `(X_i,X_j)` and leaf bank `X_J` has exactly the form required by the partner theorem (2.3); arbitrary conditioned affine shifts and the entire quadratic self-block on `J` are allowed. Its two-row slope Gram determinant is

`D=det(M_{{i,j},J} M_{{i,j},J}^T)=||r_i wedge r_j||^2=W_j`.

Therefore, literally applying the designated partner result,

`H_(1/2)(R)
 <= 2^(11/4) W_j^(-1/8)
 < 2^(23/8) H_i^(-1/8).`                                         (5.1)

Averaging the conditional estimate preserves the same uniform bound. Numerically `2^(23/8)=7.3360323456...`.

So a star concentrated on one partner is already paid; no reciprocal tiny entry or tiny `2x2` minor is selected.

## 6. Diffuse star: synthesize orders 2, 1 and 0

Assume now

`max_j q_j<=1/2`.                                                   (6.1)

The obstruction is that `omega_2` has row marginal one at the hub `i`. We dilute that marginal without discarding the aggregate wedge currency.

### 6.1 A self-matched order-one law

For every `j` with `q_j>0`, choose a column `c in J` with probability

`M_jc^2/||r_j||^2`.

Together with the outer choice `j~q`, this defines an order-one minor law `nu`. Its row marginals are exactly `q_j`. Its currency satisfies

`log K(nu)=H(q)+sum_j q_j log ||r_j||^2.`                           (6.2)

Since

`W_j<=||r_i||^2 ||r_j||^2=rho^2||r_j||^2`

and `W_j=q_j H_i`, one has

`||r_j||^2 >= q_j H_i/rho^2`.

Substituting into (6.2), the entropy cancels the `sum q_j log q_j` term and gives

`boxed: K(nu)>=H_i/rho^2.`                                        (6.3)

This is exactly the point where the whole star is spent before selecting a coordinate.

### 6.2 The 2+1+0 mixture

Let `delta_0` be the order-zero law on the empty minor, with determinant one, and define

`Omega=(1/2)omega_2+(1/4)nu+(1/4)delta_0.`                         (6.4)

Its hub row marginal is `1/2`. Every partner row marginal is

`(1/2+1/4)q_j=(3/4)q_j<=3/8`,

so the row-cap hypothesis of the mixed-order theorem holds. Its mean order is

`kbar=(1/2)2+(1/4)1=5/4.`                                         (6.5)

Because the three supports have distinct orders, the mixture entropy is exact, and

`K(Omega)=2sqrt(2) K(omega_2)^(1/2)K(nu)^(1/4)`
`        >=2sqrt(2) H_i^(3/4) rho^(-1/2).`                         (6.6)

Applying (2.1) gives

`|phi_R(t)|
 <= min(1,
        e^(5/16)(2pi)^(5/8)(2sqrt(2))^(-1/4)
        H_i^(-3/16)rho^(1/8)|t|^(-5/8)).`                          (6.7)

This estimate alone already has mean order `5/4>1`, enough for a half-Riesz potential. But combining it with the row-aggregate random-slope estimate eliminates the nuisance row norm completely.

## 7. Exact interpolation with random-slope decay

From (2.2), the same residual form also satisfies

`|phi_R(t)|<=min(1,(pi C_1)^(1/2)rho^(-1/2)|t|^(-1/2)).`          (7.1)

For positive `X,Y`, `min(X,Y)<=X^(1/5)Y^(4/5)`. Apply this with (7.1) carrying weight `1/5` and (6.7) carrying weight `4/5`. The powers of `rho` cancel exactly:

`-(1/5)(1/2)+(4/5)(1/8)=0`.

Hence

`boxed: |phi_R(t)|
 <= min(1,C_0 H_i^(-3/20)|t|^(-3/5)),`                            (7.2)

where

`C_0=e^(1/4)2^(1/5)pi^(3/5) C_1^(1/10).`                         (7.3)

This is the new oscillatory replacement. The exponent `3/5` is not supplied by any scalar quadratic phase. It appears only after combining (i) determinant-order averaging over the complete physical star and (ii) Plancherel averaging of its full linear slope.

The half-Riesz integral is explicit. If `D=C_0 H_i^(-3/20)`, then

`int_0^infinity t^(-1/2)min(1,D t^(-3/5))dt=12D^(5/6)`.

Multiplying by `sqrt(2/pi)` from the Riesz representation gives

`boxed: H_(1/2)(R)
 <= C_star H_i^(-1/8),`                                           (7.4)

with

`C_star=12*2^(2/3)*e^(5/24)*C_1^(1/12).`                          (7.5)

Using the current one-dimensional product-projection constant `C_1<=sqrt(2)`,

`C_star <=12*2^(17/24)e^(5/24)
        =24.1484268217...`.                                       (7.6)

Together with (5.1), (7.4) holds for **every** star `H_i>0`; the diffuse case is the larger constant.

## 8. Main corollary: unconditional pair-volume half-Riesz theorem

Let

`E_2:=e_2(M^T M)
    =sum_(|S|=|T|=2) det(M_ST)^2 >0.`                              (8.1)

For every row `i`, the natural order-two row marginal is

`h_i=H_i/E_2`,                                                     (8.2)

and `sum_i h_i=2`.

### Case A: all natural row marginals are diffuse

If `max_i h_i<=1/2`, apply Lemma 3.1 directly to the natural order-two law. Here `kbar=2`, `K=E_2`, so

`H_(1/2)(R)<=8e^(1/4)E_2^(-1/8).`                                 (8.3)

### Case B: a natural row marginal is heavy

If some `h_i>1/2`, then

`H_i>E_2/2`.

Apply the star theorem (7.4):

`H_(1/2)(R)
 <=2^(1/8)C_star E_2^(-1/8).`                                     (8.4)

Since (8.4) dominates (8.3) numerically, the two cases give the clean universal statement:

### Theorem 8.1 (`QFORM-PAIRVOLUME-HALF-RIESZ-UNCONDITIONAL-v1`)

For every quadratic form on independent cap-one physical coordinates, every disjoint original-coordinate cross block `M` with `E_2=e_2(M^TM)>0` satisfies

`boxed: sup_s E|R-s|^(-1/2)
 <= C_E2 E_2^(-1/8),`                                             (8.5)

where

`C_E2=2^(1/8)C_star
     =12*2^(19/24)e^(5/24) C_1^(1/12).`                           (8.6)

With `C_1<=sqrt(2)`, this simplifies to

`boxed: C_E2 <=12*2^(5/6)e^(5/24)
               =26.3340461808... .}`                              (8.7)

There is **no leverage condition, no natural-minor row-marginal condition, and no selected-minor lower bound** in (8.5). The complete second compound `E_2` is spent before any reciprocal payment.

Arbitrary within-bank self quadratic phases, arbitrary outside couplings, arbitrary signs, and arbitrary affine terms from conditioning are retained within the scope inherited from (2.1), (2.2), and the partner endpoint.

This theorem proves a half-Riesz potential bound, not a density bound for a bare rank-two packet; that distinction is essential because the opposite-sign rank-two density can have a logarithmic singularity.

## 9. Physical-square lift

Suppose one nonzero ORIGINAL physical pivot `a=A_00` is available. Completing the square only in that coordinate gives

`Q=a(X_0+ell(X_K))^2+R(X_K)`,                                     (9.1)

where `R` is the exact Schur residual. If, inside `R`, there are disjoint original-coordinate banks with cross block `M` and `E_2=e_2(M^TM)>0`, then the standard conditional square kernel gives

`p_Q(x)<=|a|^(-1/2) E|x-R|^(-1/2)`.

Therefore Theorem 8.1 yields

`boxed: ||p_Q||_infinity
 <= C_E2 |a|^(-1/2)E_2^(-1/8)
 <=26.335 |a|^(-1/2)E_2^(-1/8).`                                 (9.2)

Equivalently the analytic certificate costs only

`(|a|^4 E_2)^(-1/8)`.

This is an **essential-boundedness** conclusion. Continuity is not asserted from this square-peel step, because the square shift `ell(X_K)` is dependent on the residual variables.

## 10. What this closes and what remains

The previous B01 run left `QFORM-HEAVY-WEDGE-HUB-ROUTING-v1`: if the natural pair-volume law has a row carrying more than half of the total pair-wedge energy, spend that star without selecting a vanishing physical partner. Sections 5--8 close that **analytic** obstruction. A concentrated star is paid by the latest account02/B01 two-hub theorem; a diffuse star is paid by the new `2+1+0` determinant-order mixture and random-slope interpolation.

The first remaining structural implication is now sharper:

`QFORM-SPECTRAL-TO-PIVOT-E2-v1`:

starting only from the three-large-eigenvalue hypothesis, route every survivor of the already-paid null/ridge/grouped-square/mixed-hub branches to either

1. a nonzero physical pivot whose exact Schur residual has a disjoint physical cross block with dimension-free lower control on `|a|^4 e_2(M^TM)`, so (9.2) applies; or
2. an already-paid exact-null, grouped-coordinate, ridge, pair-log, rank-two-affine, or mixed-hub endpoint.

The bare spectral hypothesis has **not** been proved here to force such a pivot/E2 certificate, so the full QFORM conjecture remains OPEN. No full-proof candidate or two end-to-end reviews are claimed.

## 11. Phase-aligned counterexample remains preserved

Nothing in this report contradicts the scalar phase-alignment example. At a chosen frequency `s`, a fragmented cap-one scalar density can keep `|E e^{isX^2}|` bounded away from zero. The decay in (7.2) is instead a *joint* physical-coordinate estimate obtained after spending aggregate determinant entropy and a random projected slope. It is therefore exactly the type of averaged-in-frequency replacement demanded by the corrected problem statement.
