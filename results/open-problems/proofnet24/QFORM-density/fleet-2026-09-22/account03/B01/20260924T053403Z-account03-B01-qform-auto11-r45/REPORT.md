SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B01, 2026-09-24T05:34:03Z.
attacking: simultaneous hub-and-bank hyperbolic entanglement; complete the physical pair first, double-decouple the Schur critical value, and average the logarithmic pair singularity.

# account03/B01 — post-pair-completion cross smoothing for simultaneous H/Y entanglement

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `20260924T053403Z-account03-B01-qform-auto11-r45`  
Assignment: oscillatory replacement / quantitative inequalities and rigorous computations  
Execution: `WITHOUT_VERIFIED_BRAIN`  
Status: **NEW AVERAGED-FREQUENCY L^r THEOREM + NEW ESSENTIALLY-BOUNDED DENSITY BRANCH / FULL QFORM OPEN**

## 1. Exact scope and correction boundary

Let all random coordinates below be mutually source-disjoint groups of the original independent coordinates, each scalar coordinate having a probability density bounded by one. No Gaussian, moment, compact-support, connected-support, log-concavity, iid, or post-rotation independence assumption is used.

The full target remains open: for arbitrary real symmetric `A` with `s_3(A)>=1`, prove one universal bound on the density of `X^T A X`, or give a valid counterexample. The present result is a supporting theorem for the mixed two-hub/hyperbolic interface isolated in the preceding account03/B01 run.

The phase-aligned fragmented-support obstruction is retained throughout. No pointwise law-uniform quadratic-phase decay estimate is used or claimed. We also do not use the refuted arbitrary-joint coarea theorem, conditional projected-density caps, naive fiber suprema, or independence after spectral rotation.

## 2. Designated partner result actually applied

Source: `yspennstate/math-open-problems@f7e82d169badc671968036252d351b8533cdd425`,
`proofnet24/QFORM-density/fleet-2026-09-22/account04/B01/20260924T012155Z-account04-B01-lr-residual-r1/REPORT.md`.

For independent cap-one `U,V`, every `c!=0`, every `1<r<=2`, and arbitrary real affine coefficients,

`Z=2cUV+beta U+gamma V+delta`,

account04/B01 proves, with `alpha=(r-1)/r`,

`||p_Z||_r <= 2^alpha |c|^-alpha`.                            (2.1)

This source result will be applied pointwise after fixing all other original-coordinate groups. The coefficients of `U,V` are then deterministic even when they depend simultaneously on both hub and slope banks.

## 3. Arbitrarily entangled hyperbolic pair still gives a global L^r law

### Theorem 3.1 — `QFORM-HYPERBOLIC-PAIR-ENTANGLED-GLOBAL-LR-v1`

Let `Z_0` be any random element independent of cap-one `U,V`. Let `A(Z_0),B(Z_0),D(Z_0)` be arbitrary measurable real functions. Put

`Q=2cUV+A(Z_0)U+B(Z_0)V+D(Z_0)`, `c!=0`.                       (3.1)

Then for every `1<r<=2`, with `alpha=(r-1)/r`, `Q` has a density and

`boxed: ||p_Q||_r <= 2^alpha |c|^-alpha.`                      (3.2)

In particular,

`||p_Q||_2 <= sqrt(2)|c|^-1/2`.                                (3.3)

#### Proof

For almost every fixed `Z_0=z`, (2.1) applies to the conditional law and gives

`||p_(Q|Z_0=z)||_r <= 2^alpha |c|^-alpha`.                      (3.4)

The unconditional density is the probability mixture

`p_Q(x)=E[p_(Q|Z_0)(x)]`.                                      (3.5)

Minkowski's integral inequality yields

`||p_Q||_r <= E ||p_(Q|Z_0)||_r <=2^alpha |c|^-alpha`.          (3.6)

No conditional density cap for a rotated coordinate is asserted; only the completed partner theorem for the two original coordinates `U,V` is used. QED.

### Averaged-frequency consequence

With Fourier convention `phi_Q(t)=E exp(itQ)`, Hausdorff--Young gives

`||phi_Q||_(r') <= (2pi)^alpha 2^alpha |c|^-alpha`,             (3.7)

where `r'=r/(r-1)`. At `r=2`, Plancherel sharpens this to

`boxed: int_R |phi_Q(t)|^2 dt <= 4pi/|c|.`                     (3.8)

Thus simultaneous arbitrary entanglement of the two pair coefficients with all other source-disjoint coordinates admits a uniform **integrated-frequency** estimate even though pointwise quadratic-phase decay is false.

For the signed triangular average

`D_T mu(y)=(1/(2pi)) int_{-T}^T (1-|t|/T) Re(e^{-ity}phi_Q(t))dt`,

Cauchy--Schwarz and (3.8) give the explicit bound

`boxed: sup_y |D_T law(Q)(y)| <= sqrt(2T/(3pi|c|)).`            (3.9)

This is a direct averaged-frequency replacement on the previously entangled pair interface.

## 4. The simultaneous hub-and-bank interface

Let

- `H=(H_1,H_2)` be two independent original cap-one hub coordinates;
- `Y=(Y_1,...,Y_m)` be a source-disjoint product bank;
- `U,V` be two further independent original cap-one coordinates;
- `F(H)` and `G(Y)` be arbitrary measurable real same-bank phases;
- `B` be a deterministic `2 x m` matrix;
- `a,b in R^2`, `ell,mvec in R^m`, `beta,gamma in R`;
- `c!=0`.

Consider

`Q = F(H)+2 H^T B Y+G(Y)+2cUV`
`    +[2a^T H+ell^T Y+beta]U`
`    +[2b^T H+mvec^T Y+gamma]V`.                               (4.1)

This is exactly the preceding B01 obstruction: the same hyperbolic pair shifts both hubs and has affine coefficients depending simultaneously on both the hub and slope banks.

Set

`A_u=2a^T H+ell^T Y+beta`,
`A_v=2b^T H+mvec^T Y+gamma`.                                   (4.2)

The physical pair matrix in `(U,V)` is

`P=[[0,c],[c,0]]`,                                              (4.3)

so completing that pair changes the critical value by

`A_u A_v/(2c)`.                                                 (4.4)

Therefore the completed critical remainder is

`T(H,Y)=F(H)+2H^TBY+G(Y)-A_u A_v/(2c)`.                         (4.5)

The crucial algebraic observation is that it remains a two-bank phase with one explicit physical cross block:

`T(H,Y)=F_*(H)+2H^T B_*Y+G_*(Y)`,                              (4.6)

where

`boxed: B_* = B-(a mvec^T+b ell^T)/(2c).`                      (4.7)

All terms depending only on `H` are absorbed into `F_*`; all terms depending only on `Y` are absorbed into `G_*`. This identity is exact and does not require those same-bank terms to be quadratic.

## 5. Product-preserving concentration of the completed critical value

We use the previously proved account03/B01 double-decoupling theorem from

`yspennstate/math-open-problems@0993b0d6fcaadedcc7873bf89d99c5eedf630dc0`,
`proofnet24/QFORM-density/fleet-2026-09-22/account03/B01/account03-B01-20260924T002941Z-auto11/REPORT.md`.

For arbitrary measurable `F_*(H),G_*(Y)` and physical cross block `B_*`, two original-coordinate Cauchy--Schwarz differences give

`P(T in I)^4 <= P(|(H-H')^T B_* (Y-Y')|<=|I|)`.                (5.1)

The one-singular-direction bilinear estimate then gives, with

`sigma=||B_*||_op>0`,

`sup_(|I|=h) P(T in I) <= K_0 (h/sigma)^(1/8)`,                 (5.2)

where

`K_0=[4 sqrt(2/e)]^(1/4)=1.36099627655494...`.                 (5.3)

For symmetric intervals of radius `rho`, this becomes

`sup_t P(|T-t|<rho) <= H sigma^(-1/8) rho^(1/8)`,               (5.4)

with

`H_0=2^(3/4)e^(-1/8)=1.48417696371179...`,
`H=H_0 sigma^(-1/8)`.                                          (5.5)

Every difference is still in original coordinates and retains coordinatewise density cap one. No rotated random coordinate is treated as independent.

## 6. Averaging the moving logarithmic pair singularity

Use the completed logarithmic physical-pair theorem

`yspennstate/math-open-problems@f7f0fedb2d93b46824f96cac1164af6f8a55626f`,
`proofnet24/QFORM-density/interactive/20260922T180015Z-pair-log/PAIR_LOG_THEOREM.md`.

For an invertible indefinite physical pair matrix `P`, with

`D=|det P|`, `kappa=sigma_min(P)`,

and completed critical remainder `T`, it proves for every cutoff `r_0>0`

`p_Q(t) <= 2sqrt(2)/r_0`
`          +D^(-1/2) E log_+(2r_0^2/(kappa|t-T|)).`             (6.1)

For (4.3),

`D=c^2`, `kappa=|c|`.                                          (6.2)

More generally, if

`P(|T-t|<rho)<=H rho^alpha`, `0<alpha<1`,                       (6.3)

then layer cake gives, for every `A>0`,

`E log_+(A/|t-T|)`
` = int_0^infinity P(|t-T|<A e^{-v})dv`
` <= (H/alpha) A^alpha`.                                       (6.4)

Apply (5.4) with `alpha=1/8`. Substituting (6.2)--(6.4) into (6.1) gives

`p_Q(t) <= 2sqrt(2) r_0^-1`
` +(H/alpha)2^alpha |c|^(-1-alpha) r_0^(2alpha)`.               (6.5)

This is finite uniformly in `t` for every `r_0>0`.

## 7. Main new density theorem

### Theorem 7.1 — `QFORM-TWO-HUB-BOTH-SIDES-ENTANGLED-POSTPAIR-CROSS-v1`

Under (4.1), suppose

`sigma=||B-(a mvec^T+b ell^T)/(2c)||_op>0`.                    (7.1)

Then `Q` has an essentially bounded density and

`boxed:
 ||p_Q||_infinity
 <= C_mix |c|^(-9/10) sigma^(-1/10),
 C_mix=5*2^(9/5)*e^(-1/10)
      =15.7541344792523... .
}`                                                               (7.2)

#### Proof

In (6.5), let `alpha=1/8`, `A_0=2sqrt(2)` and

`B_0=(H/alpha)2^alpha |c|^(-1-alpha)`.                          (7.3)

The right side is `A_0/r_0+B_0 r_0^(2alpha)`. Its optimizer obeys

`r_0^(2alpha+1)=A_0/(2alpha B_0)`.                              (7.4)

At the optimizer,

`min = A_0(2alpha+1)/(2alpha)`
`      * (2alpha B_0/A_0)^(1/(2alpha+1)).`                      (7.5)

For `alpha=1/8`, substituting `H=H_0 sigma^-1/8` and (5.5) simplifies exactly to

`5*2^(9/5)e^(-1/10)|c|^-9/10 sigma^-1/10`,                     (7.6)

which is (7.2). QED.

The homogeneity is exact: under scaling of the whole quadratic form by `lambda`, both `c` and `sigma` scale by `|lambda|`, and `9/10+1/10=1`, so the right side scales by `|lambda|^-1`, as a density bound must.

### Signed-Fejer consequence

The designated account04/B01 signed-Fejer theorem at

`yspennstate/math-open-problems@a3693ed6d50e8e4143b2f33bf997c5de2cb52d79`

proves that for a bounded density,

`||p_Q||_infinity=sup_(T>0,y) D_T law(Q)(y)`.                  (7.7)

Hence (7.2) also yields

`boxed:
 sup_(T>0,y) D_T law(Q)(y)
 <=15.754135 |c|^-9/10 sigma^-1/10.
}`                                                               (7.8)

This is the desired bounded averaged-frequency endpoint in the noncollapsed post-pair-cross branch.

## 8. Concrete target-valid stress check

Take six original coordinates ordered as `(H1,H2,Y1,Y2,U,V)` and choose

`B=I_2`,
`a=(0.4,0.1)`, `b=(0.1,-0.3)`,
`ell=(0.3,-0.2)`, `mvec=(-0.1,0.4)`, `c=0.7`,

with zero same-bank diagonal terms for the finite check. The symmetric coefficient matrix has eigenvalues approximately

`-1.24694520, -1.02836910, -0.50487628,`
` 0.55832543,  1.00459605,  1.21726910`.                        (8.1)

Thus four eigenvalues have absolute value at least one. The post-completion block is

`B_*=[[1.007142857,-0.1],[0.071428571,0.928571429]]`,           (8.2)

with

`sigma=1.01344769611609`.                                      (8.3)

The theorem gives

`||p_Q||_infinity <=21.6883332811`.                             (8.4)

This finite spectrum check is only a stress test of the scope; it is not evidence for the unrestricted theorem.

## 9. Preserved pointwise counterexample

Fix any `s!=0` and `eta in (0,pi/2)`. The set

`E={x:dist(sx^2,2pi Z)<=eta}`

has infinite Lebesgue measure. Choose a finite union `E_0 subset E` of total measure one and take `f=1_(E_0)`. Then `f` is an admissible probability density and

`Re E exp(isX^2)>=cos(eta)`.                                   (9.1)

Thus no positive law-uniform pointwise power decay in `|s|` can be restored. The present mechanism instead uses (i) the partner's global conditional `L^r` budget and (ii) product-preserving concentration of the moving pair critical value before averaging the logarithmic singularity.

## 10. Exact remaining interface

The previous mixed H/Y affine-entanglement obstruction is now paid whenever the completed critical value retains a nonzero physical H--Y cross block `B_*`.

The first remaining local interface is

`QFORM-PAIR-COMPLETION-CROSS-COLLAPSE-v1`,                     (10.1)

namely the exact or quantitatively near-collapsed case

`B-(a mvec^T+b ell^T)/(2c) approx 0`.                           (10.2)

In the exact case, completing `(U,V)` removes the H--Y bilinear cross term from the critical value, leaving `F_*(H)+G_*(Y)`. The partner theorem still supplies the global `L^r` / integrated-frequency estimate (3.2)--(3.9), but this run does not prove a universal `L^infinity` upgrade there. The next structural task is to use the three-large-eigenvalue condition to show that this cross collapse forces a separately payable same-bank curvature/grouped-square/ridge currency, or to find a counterexample to that structural implication. No such forcing statement is claimed here.

## 11. Continuity and proof status

- Theorem 3.1 gives absolute continuity and `L^r` control, but not continuity by itself.
- Theorem 7.1 gives an essentially bounded density. The pair-log proof used here does **not** establish a continuous representative, so continuity is not claimed for this new branch.
- Full QFORM remains **OPEN**.
- Two independent end-to-end reviews would still be required before any full candidate proof could be promoted.

## 12. Deterministic checks

Sibling `checks.py` verifies the completion identity on 1000 deterministic pseudo-random parameter choices, the optimizer and exact constant, scaling, and the target-valid six-coordinate spectrum. Sibling `CHECKS.txt` records the numerical output and ends `STATUS=PASS`.
