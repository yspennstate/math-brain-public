# Superseding supplement — prior B11 absorbs the first theorem; mixed-frame absolute-TT* barrier family is nevertheless paid by pair-log realignment

Run `20260924T034247Z-fleet01-B16-QFORM-auto11`.

**Status after fresh cross-check:** `ESSENTIAL_STEP_APPLIED / DUPLICATE ANALYTIC CLAIM CORRECTED / NEW LIVE-BRANCH CLOSURE / FULL QFORM OPEN`.

This supplement supersedes the novelty classification in `REPORT.md` while preserving that file immutably. The full QFORM conjecture remains OPEN, and continuity remains separate.

## 1. Correction: `QFORM-FRESH-HUB-CONDITIONAL-PAIRLOG-SQUARE-v1` is not a new analytic theorem

After the first report was committed, a broader repository search found the earlier fleet01/B11 theorem

`QFORM-OVERLAP-SAFE-SQUARE-LOG-v1`,

at

`proofnet24/QFORM-density/fleet-2026-09-22/fleet01/B11/20260923T101016Z-fleet01-B11-QFORM-auto11/REPORT.md`.

That result already allows an indefinite pair of independent cap-one source variables to be translated by an arbitrary function of the remainder, while the square smoother may be arbitrarily dependent on the same remainder. It gives

`||p_Q||_infinity
 <=8*2^(1/4) L^(1/2)(D kappa |d|)^(-1/4)`                        (1.1)

for a square statistic with marginal density cap `L`.

The first theorem in this run is therefore a scaled re-derivation/corollary, not a new analytic result. Indeed, in

`Y=gamma H+S`,
`aY^2+2 beta YU`

one may use the genuinely independent pair `(H,U)` directly and put the entire `S` dependence into the B11 translation. The dependence between `S` and the square variable `V` is exactly the overlap pattern already permitted by B11. The r38 `<14.901` estimate from the first report is valid but weaker than the B11 route and is not counted as new progress.

No mathematical claim from B11 is contradicted; the correction is solely about novelty/scope accounting.

## 2. Mechanism change: pay the newest mixed-Pluecker absolute-TT* barrier family by a different physical pair

The newest compatible fleet03/B16 result is

`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B16/20260924T025219Z-fleet03-B16-QFORM-r39/REPORT.md`.

It exhibits the strict target family

`Q_bar,theta
 = theta H^2 +2 sqrt(2) H L +2P^2+4LS`,                            (2.1)

with

`L=(X_1-X_3)/sqrt(2)`,
`S=(X_2+X_4)/sqrt(2)`,
`P=(X_1+X_3)/sqrt(2)`,                                            (2.2)

for five independent cap-one original variables. Its old absolute TT* kernel is infinite for interval laws even though the mixed Pluecker masses are exactly `1/2,1/2`. That is a genuine mechanism barrier, not a density counterexample.

The same family is in fact uniformly paid by a different source-preserving pair-log grouping.

Expand (2.1) in original coordinates and set

`X=X_1`, `Y=X_3`, `Z=X_2+X_4`.

Then

`Q_bar,theta
 =theta H^2 +(X+Y)^2 +2(H+Z)(X-Y).`                              (2.3)

Condition on the literal hub `H=h` and put

`W=h+Z`.                                                          (2.4)

Because `X_2,X_4` are independent cap-one variables,

`p_Z=f_2*f_4`, hence `||p_Z||_infinity<=1` by Young; translation gives

`||p_W||_infinity<=1`.                                           (2.5)

Conditional on `H=h`, the three scalar variables `X,Y,W` are mutually independent, each with density cap one.

Now choose the **indefinite pair `(X,W)`**, not the mixed-frame TT* coordinates. The conditional quadratic is

`F=(X+Y)^2+2W(X-Y)`.                                              (2.6)

In block form with pair vector `(X,W)` and remainder `Y`,

`B=[[1,1],[1,0]]`,
`C=[1,-1]^T`,
`D_0=1`.                                                         (2.7)

Here

`det B=-1`,
`kappa=sigma_min(B)=(sqrt(5)-1)/2`.                              (2.8)

Moreover

`B^(-1)C=[-1,2]^T`,                                              (2.9)

and the Schur complement is exactly

`D_0-C^T B^(-1)C=4`.                                             (2.10)

Therefore the exact completion is

`F = ((X,W)+(-Y,2Y))^T B ((X,W)+(-Y,2Y)) +4Y^2`.                 (2.11)

This is precisely the overlap-safe B11 theorem: the pair is an independent cap-one product pair, while its translation depends on the **same** scalar `Y` that generates the square remainder. No independence after any spectral rotation is used.

Substituting

`D=1`, `kappa=(sqrt(5)-1)/2`, `L=1`, `d=4`                       (2.12)

into (1.1) gives

`boxed:
 ||p_(Q_bar,theta)||_infinity
 <= 8 (sqrt(5)-1)^(-1/4)
 = 7.58716271595... <7.588
`                                                                    (2.13)

for **every real `theta`** and every collection of independent cap-one original input densities.

Thus fleet03/B16 r39's infinite absolute TT* kernel is rigorously a barrier to that particular frequency norm, not a surviving density-height stress family. A source-preserving physical-pair completion pays the same exact mixed-volume packet uniformly through every hub-square coefficient.

The r39 spectral check already gives at least three eigenvalues of modulus at least two for every `theta`, so (2.13) is an actual strict-target inequality.

## 3. General canonical compiler behind the r39 closure

The algebra above is not tied to unit coefficients. Suppose, conditional on an outside parameter, `X,Y,W` are mutually independent, `X,Y` have cap one and `W` has density cap `K`, and consider

`F=lambda (X+Y)^2+2 nu W(X-Y)`,                                   (3.1)

with `lambda nu !=0`.

Scale `W'=K W`, so `W'` has cap one. On the pair `(X,W')`,

`B_K=[[lambda,nu/K],[nu/K,0]]`,
`C_K=[lambda,-nu/K]^T`.                                          (3.2)

The exact identities are

`B_K^(-1) C_K =[-1, 2lambda K/nu]^T`,
`lambda-C_K^T B_K^(-1)C_K =4lambda`.                             (3.3)

Put

`kappa_K
 =(sqrt(lambda^2+4nu^2/K^2)-|lambda|)/2`.                     (3.4)

Then the overlap-safe pair-log theorem gives

`boxed:
 ||p_F||_infinity
 <=8 [K^2/(2 |lambda| nu^2 kappa_K)]^(1/4).
`                                                                    (3.5)

This is a new **structural compiler/application of the existing B11 analytic theorem**, not a new analytic estimate. It shows that the phase pattern `(X+Y)^2 + W(X-Y)` automatically contains a good indefinite physical pair plus an exact square Schur remainder. The mixed-volume absolute-TT* obstruction therefore has to survive after excluding this algebraic realignment, not merely after showing one chosen Fourier kernel is infinite.

## 4. Designated partner fleet02/B16 remains applied at an actual inequality

The newest completed designated-partner result used in this run remains fleet02/B16 commit

`390bf6a9ad30195ba4011927c8218245d0e014be`, theorem
`QFORM-PHYSICAL-HUB-DEFINITE-DISCRIMINANT-v1`.

For

`B_*=[[-1,1,0],[1,1,0],[0,0,1]]`,                               (4.1)

we have

`spec(B_*)={-sqrt(2),sqrt(2),1}`,
`det B_*=-2`, `a=-1`, `a det B_*=2>0`.                            (4.2)

Thus for a fresh cap-one hub and an orthonormal two-dimensional product projection `(U,V)` from a disjoint source block,

`boxed:
 ||p_(-H^2+2HU+U^2+V^2)||_infinity
 <=2sqrt(2pi)2^(-1/4)
 =4.2156294611... .
`                                                                    (4.3)

This partner application is independent of the duplication correction above.

## 5. Remaining B16 implication after the correction

Do **not** list the first report's conditional pair-log formula as a new claim. The substantive new live-state information from this run is instead:

- the r39 sharp mixed-Pluecker family with infinite old absolute TT* kernel is uniformly bounded by `<7.588` through a different physical pair;
- therefore total mixed volume plus failure of that absolute TT* norm does not characterize the hard endpoint;
- a surviving obstruction must also evade the phase-aligned completion (3.3), i.e. it must lack a source partition/orientation yielding an invertible physical/source pair with a quantitatively curved scalar Schur remainder.

The sharpened open implication is

`QFORM-PHASE-AWARE-MIXED-VOLUME-PAIR-OR-TTSTAR-v2`:

> In every generic majority-sign near-coloop survivor, either find a source-preserving orientation whose mixed phase realigns to a quantitatively good indefinite pair plus a scalar quadratic Schur remainder (hence pair-log smoothing pays it), or build a genuinely cancellation-preserving TT*/Hilbert receiver for the remaining mixed-volume packet. A mere lower bound on mixed Pluecker volume and a mere bounded projected joint density are both insufficient.

The unrestricted QFORM theorem and global continuity remain OPEN.
