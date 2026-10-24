Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED.**

# NM13-12 — atomic rare-dropout codimension universality

Repository / branch: private `yspennstate/math-open-problems` / `master`  
Worker: `NM13-12` / `proofnet24/NM13-12/progress-universality`  
Controlling policy: `operations/PROGRESS20_2026-09-20.md`, current LIVE20 mapping  
Primary applied parent: **P12 unresolved triangular/universality successor**  
T03 coordination: **NM13-03 / NM13-07 read for current boundary only; no lifted-RDT duplication**  
Status: **PARTIAL / NEW AUTHOR-SIDE COMPLETE ATOMIC RANDOM-MATRIX EXTENSION / INDEPENDENT REVIEW PENDING**

## 0. Compact handoff and route selection

The latest canonical P12 report remains

`proofnet24/P12-smooth-iid/runs/2026-09-17/2026-09-17T18-20-03Z__run-report.md`.

Its frozen theorem is unchanged. For `F in {R,C}`, let `A_m in F^{N_m x m}` have iid centered variance-one entries with density `f_m`. Assume one fixed integer `q>=1` and one uniform finite constant `M` satisfy

`sup_m ||f_m^{*q}||_infty <= M`,

and assume

`N_m/m -> gamma>1`, `k_m=r_m+1`, `k_m log m=o(m)`.

Then

`(k_m/m) log M^F_{m,r_m}(A_m) ->_P -h(gamma)/d_F`,

where `d_R=1`, `d_C=2` and

`h(gamma)=gamma log gamma-(gamma-1)log(gamma-1)`.

There is **no fourth-moment assumption and no positive-moment assumption above variance normalization** in that frozen theorem. Its remaining canonical obligations are audit/package gates, not missing author-side mathematics. The mathematical successor relevant here remains universality for triangular laws outside every uniform finite-convolution density ceiling.

The latest NM13-12 report before this run was

`proofnet24/NM13-12/progress-universality/runs/2026-09-20/2026-09-20T1354Z__p12-vanishing-moment-gap-universality.md`.

It pushed the smooth positive-floor near-lattice class down to a vanishing `2+delta_m` moment gap. Its recorded next obstruction was the loss of the deterministic positive smoothing floor, especially Bernoulli--Gaussian masks with `P(S_m=0)>0`: a mask can annihilate part of a projected Gaussian covariance, so the old full `t^{k_m}` continuous small-ball power is not available by conditioning alone.

This run attacks exactly that obstruction by a different mechanism. It does **not** try to force a positive covariance floor. Instead it proves that if the total number of dropped Gaussian coordinates is `o_P(k_m)`, then every fresh-column projection loses at most `o_P(k_m)` continuous dimensions. The lost exponent is then `o(m)` at the row-submatrix extreme scale. On the constructive side, all rows containing a dropout are discarded; there are only `o_P(k_m)` such rows, so the candidate entropy remains `h(gamma)m+o(m)`. This permits genuinely atomic entry laws and even a diverging total number of atomic defects.

`POSTED.md` excludes rediscovery/repackaging of the posted bounded-density row-submatrix papers, mesoscopic-spike work, kernel/ReLU work and zero-margin/Ising perceptron results. The result below is distinct: every entry law has atoms, every fixed convolution retains atoms, and the concrete matrix has a number of dropped continuous coordinates tending to infinity in probability.

## 1. Current T03 companion state, preserved rather than duplicated

The newest complete NM13-03 report on current `master` is

`proofnet24/NM13-03/progress-perceptron-theory/runs/2026-09-20/2026-09-20__t03-schur-branch-crossing-alpha12319634446194.md`.

It proves an exact Schur branch-crossing lemma, reduces the positive-gap complete-third root problem to a uniformly invertible 3D branch plus a scalar sign crossing, and moves the review-pending exact-sphere source endpoint to

`12.319634446194`.

Its third-full application remains **CONDITIONAL** pending outward enclosure of the 3D tube / Gaussian moments.

The newest NM13-07 report is

`proofnet24/NM13-07/progress-perceptron/runs/2026-09-20/2026-09-20__t03-pivoted-x-schur-cascade-alpha12319634446193.md`.

It further triangularizes the positive-gap system by a pivoted nested-Schur cascade and moves the current review-pending exact-sphere source endpoint by another exact `10^-12` to

`12.319634446193`.

Its positive-gap third-full waypoint remains conditional pending outward moment/root enclosure. No stationarity, Krawczyk, Schur, c-sector, Gaussian quadrature or lifted-RDT calculation is duplicated here.

Thus the T03 parent entering and leaving this NM13-12 run is

`[6.30297437506, 12.319634446193]`.

There is **no T03 source movement from this worker in this run**.

## 2. New atomic dropout model

For each `m`, let

- `R` be Rademacher;
- `G~N(0,1)`;
- `B~Bernoulli(p_m)` with `p_m=1-q_m`;
- `(R,G,B)` independent;
- `0<sigma_m<=1`.

Set

`nu_m^2 = 1+p_m sigma_m^2`,

and define the centered variance-one entry

`xi_m = (R + sigma_m B G)/nu_m`.                         (2.1)

Indeed

`E xi_m=0`,

and

`E xi_m^2=(1+p_m sigma_m^2)/nu_m^2=1`.

Let `A_m in R^{N_m x m}` have iid entries with law `xi_m`, and let

`M_{m,r}(A)=min_{T subset [N_m], |T|=m+r} sigma_m(A_T)`,

with `k_m=r_m+1`.

For comparison define the full-activation Gaussian-smoothed Rademacher law

`tilde xi_m=(R+sigma_m G)/sqrt(1+sigma_m^2)`.              (2.2)

The earlier NM13-12 vanishing-noise theorem proves the row-submatrix exponent for `(2.2)` under

`(S1) m sigma_m^2 / log(e/sigma_m) -> infinity`,

`(S2) k_m[log m + log(e/sigma_m)] = o(m)`,

plus `N_m/m->gamma>1`.

The present theorem transfers that result to `(2.1)` even though `(2.1)` is not absolutely continuous.

## 3. Main theorem — rare-dropout codimension universality

### Theorem NM12-P12-ATOMIC-DROPOUT

Assume

`N_m/m -> gamma>1`,

`k_m=r_m+1`,

`k_m log m=o(m)`,

`0<sigma_m<=1`,

and `(S1)--(S2)` above. Suppose in addition

`(D1) N_m m q_m = o(k_m)`.                                (3.1)

Then for iid real entries `(2.1)`,

`boxed:`

`(k_m/m) log M^R_{m,r_m}(A_m) ->_P -h(gamma)`.             (3.2)

The theorem removes the deterministic positive smoothing floor completely. Condition `(D1)` is quantitative: it permits a **diverging** number of dropped Gaussian coordinates provided that number is `o_P(k_m)`.

### Strict class separation

For every `m` with `q_m>0`, the law `(2.1)` has two atoms:

`P{xi_m=+1/nu_m} >= q_m/2`,

`P{xi_m=-1/nu_m} >= q_m/2`.

For every fixed convolution depth `ell>=1`, the `ell`-fold convolution has an atom at `ell/nu_m` of mass at least

`(q_m/2)^ell >0`,                                           (3.3)

coming from all `ell` masks being off and all `ell` Rademachers being `+1`. Hence no fixed convolution is even absolutely continuous. In particular neither the frozen P12 finite-convolution theorem nor any of the preceding positive-floor smooth NM13-12 theorems applies.

## 4. Dropout count and the correct small parameter

Let

`Dcal_m = # {(i,j): B_ij=0, 1<=i<=N_m, 1<=j<=m}`.

Then

`E Dcal_m = mu_m := N_m m q_m`.                            (4.1)

By `(D1)`, `mu_m/k_m ->0`, hence

`Dcal_m/k_m ->_P 0`.                                       (4.2)

A convenient explicit deterministic envelope is

`eta_m = sqrt(mu_m/k_m) ->0`.                              (4.3)

Markov gives

`P{Dcal_m > eta_m k_m}`
` <= mu_m/(eta_m k_m)`
` = eta_m ->0`.                                            (4.4)

Write

`G_m={Dcal_m <= eta_m k_m}`.

All estimates below are uniform over mask realizations in `G_m`.

## 5. New lower-extreme lemma — each dropout costs at most one continuous dimension

Fix one mask realization, one candidate row set `T` with

`|T|=m+r_m=m+k_m-1`,

and one fresh column `C_j` of `(A_m)_T`. Freeze all other columns. Let

`H_j=span{C_l:l!=j}`.

Because `H_j` is generated by at most `m-1` vectors in `R^{m+k_m-1}`,

`dim H_j^perp >= k_m`.                                     (5.1)

Choose any measurable `k_m`-dimensional subspace

`W_j subset H_j^perp`.

Let `I_j subset T` be the rows in which the fresh column mask is off. Then

`|I_j| <= Dcal_m`.                                         (5.2)

Define the active-coordinate subspace

`E_j={x in R^T: x_i=0 for every i in I_j}`.

By the dimension inequality,

`U_j:=W_j intersect E_j`

satisfies

`ell_j:=dim U_j >= k_m-|I_j| >= k_m-Dcal_m`.               (5.3)

Let `Q_j` be orthogonal projection onto `U_j`. Conditional on the mask, all other columns, and the fresh Rademacher coordinates, the projected fresh column is a translated isotropic Gaussian on `U_j`:

`Q_j C_j = a_j + rho_m Z_j`,

where `Z_j~N(0,I_{ell_j})` and

`rho_m = sigma_m/nu_m`.                                    (5.4)

The point is exact: vectors in `U_j` vanish on every inactive coordinate, so every coordinate contributing to `U_j` has an active Gaussian with the same variance `sigma_m^2/nu_m^2`.

Therefore, for every `s>0`, Gaussian density times ball volume gives

`P{||Q_j C_j||_2 <= s | masks, other columns, fresh Rademachers}`
` <= (C s/rho_m)^{ell_j}`.                                 (5.5)

For the exponentially small radii below, `C s/rho_m<1` for all large `m` by `(S2)`. Using `(5.3)`,

`boxed:`

`P{dist(C_j,H_j)<=s | masks, other columns}`
` <= (C s/rho_m)^{k_m-Dcal_m}`.                            (5.6)

This is the new mechanism. The old positive-floor argument gave a full `k_m` power. A mask with `Dcal_m` dropped coordinates loses at most `Dcal_m` powers, regardless of where those defects occur and regardless of the adaptive subspace `H_j^perp`.

## 6. Lower extreme: the lost powers cost only o(m)

The standard negative second-moment identity used in P12 gives, for a candidate matrix `B` with `m` columns,

`sum_i sigma_i(B)^(-2)=sum_j dist(C_j,H_j)^(-2)`.

Consequently

`sigma_min(B)<=t`

forces at least one fresh-column distance

`dist(C_j,H_j)<=sqrt(m) t`.                                (6.1)

Conditional on a mask realization in `G_m`, union over all candidates and all `m` fresh columns and apply `(5.6)`:

`P{M_{m,r_m}(A_m)<=t | masks}`
` <= binom(N_m,m+r_m) m`
`    (C sqrt(m) t/rho_m)^{k_m-Dcal_m}.                     (6.2)

Fix `epsilon>0` and take

`t_- = exp[-(h(gamma)+epsilon)m/k_m]`.                     (6.3)

Since `k_m=o(m)` and `N_m/m->gamma`,

`log binom(N_m,m+r_m)=h(gamma)m+o(m)`.                     (6.4)

Also `(S2)` implies

`k_m[log m+log(e/rho_m)]=o(m)`,                            (6.5)

because `nu_m` is uniformly bounded between `1` and `sqrt(2)`.

On `G_m`, `Dcal_m/k_m<=eta_m->0`. Taking logarithms in `(6.2)` and using `(6.3)--(6.5)` gives

`log P`
` <= h(gamma)m`
`    -(h(gamma)+epsilon)m(1-Dcal_m/k_m)`
`    +o(m)`
` = -epsilon m`
`   +(h(gamma)+epsilon)m Dcal_m/k_m`
`   +o(m)`
` = -epsilon m+o(m)`.                                      (6.6)

Thus

`P{M_{m,r_m}(A_m)<=t_- , G_m}->0`.

Together with `P(G_m^c)->0`,

`P{(k_m/m)log M_{m,r_m}(A_m)<-h(gamma)-epsilon}->0`.       (6.7)

This proves the required lower bound on the normalized logarithm.

## 7. Constructive upper extreme by deleting defective rows

A row is called clean if all of its `m` masks equal one. Every nonclean row contains at least one dropout, so on `G_m` the number of nonclean rows is at most

`Dcal_m <= eta_m k_m=o(k_m)`.                              (7.1)

Set the deterministic row count

`N'_m=N_m-ceil(eta_m k_m)`.

For all large `m`,

`N'_m/m -> gamma`,                                         (7.2)

and on `G_m` there are at least `N'_m` clean rows. Select the first `N'_m` clean rows according to row index and call the resulting matrix `A_m^circ`.

The selection uses only the Bernoulli mask and is independent of all `R,G` variables. Therefore, conditional on the mask, the selected `R,G` entries remain iid. Since every selected mask equals one,

`A_m^circ = c_m tilde A_m`,                                (7.3)

where `tilde A_m` has iid entries `(2.2)` and

`c_m = sqrt(1+sigma_m^2)/sqrt(1+p_m sigma_m^2)`.           (7.4)

Because `A_m` contains every candidate row set available inside `A_m^circ`,

`M_{m,r_m}(A_m) <= M_{m,r_m}(A_m^circ)`
`                  = c_m M_{m,r_m}(tilde A_m)`.            (7.5)

The predecessor vanishing-noise theorem applies to `tilde A_m` with row count `N'_m`, because `(7.2)` preserves the aspect ratio and `(S1)--(S2)` are unchanged. Hence

`(k_m/m)log M_{m,r_m}(tilde A_m) ->_P -h(gamma)`.          (7.6)

Moreover `1<=c_m<=sqrt(2)` because `sigma_m<=1`, while `k_m/m->0`. Thus

`(k_m/m)log c_m ->0`.                                      (7.7)

Combining `(7.5)--(7.7)` and `P(G_m^c)->0` yields, for every `epsilon>0`,

`P{(k_m/m)log M_{m,r_m}(A_m)>-h(gamma)+epsilon}->0`.       (7.8)

Together with `(6.7)`, this proves `(3.2)`. QED.

## 8. Concrete unresolved application with a diverging number of atoms/defects

Take

`k_m=floor(sqrt(m))`,

`sigma_m=m^(-1/3)`,

`q_m = m^(-3/2)/log m`,                                    (8.1)

and `N_m/m->gamma>1`.

Then

`m sigma_m^2/log(e/sigma_m)`
` ~ m^(1/3)/[(1/3)log m] -> infinity`,                     (8.2)

and

`k_m[log m+log(e/sigma_m)]/m`
` = O(log m/sqrt(m)) ->0`.                                 (8.3)

The expected total number of dropped Gaussian coordinates is

`mu_m=N_m m q_m`
` ~ gamma sqrt(m)/log m -> infinity`,                      (8.4)

but

`mu_m/k_m ~ gamma/log m ->0`.                              (8.5)

Hence `(D1)` holds although the matrix contains a diverging number of dropped coordinates. In fact `Var(Dcal_m)<=mu_m`, so `(8.4)` implies

`Dcal_m/mu_m ->_P 1`,                                      (8.6)

and therefore `P{Dcal_m=0}->0`. The theorem is **not** a disguised coupling on an event where the whole matrix is fully smoothed.

At the same time each scalar entry has atoms of mass at least

`q_m/2 = 1/[2 m^(3/2) log m]`,                             (8.7)

and every fixed convolution retains a nonzero atom by `(3.3)`. Thus:

- frozen P12 does not apply because there is no convolution density at any fixed depth;
- the microscopic-jitter transfer does not apply because its required concentration inequality at the exponentially small jitter scale is violated by the polynomial atom `(8.7)`;
- the preceding positive-floor NM13-12 near-lattice theorems do not apply because the Gaussian scale equals zero with probability `q_m`.

Nevertheless the new theorem proves

`boxed:`

`(k_m/m) log M^R_{m,r_m}(A_m) ->_P -h(gamma)`.             (8.8)

### Applied parent claim: before / after

**Before:** the explicit atomic triangular family `(8.1)` was **UNKNOWN / uncovered** by frozen P12 and by the preceding NM13-12 positive-floor smooth extensions.

**After:** `(8.8)` is proved author-side, pending independent review.

The frozen canonical P12 theorem itself is unchanged.

## 9. Demonstrated theory gain, separately from parent movement

The mechanism-level gain is the exact replacement

`full rank-k continuous projected Gaussian smoothing`

by

`rank at least k-Dcal_m continuous smoothing`,             (9.1)

where `Dcal_m` is the global number of missing continuous coordinates. The resulting loss in the logarithmic lower-extreme calculation is

`(h(gamma)+epsilon)m Dcal_m/k_m = o_P(m)`.                 (9.2)

On the constructive side the same defect count deletes only `o_P(k_m)` rows, which changes the candidate entropy by `o(m)` and leaves `N'_m/m->gamma`.

Thus the theorem allows total dropout intensity all the way up to

`N_m m q_m = o(k_m)`,                                      (9.3)

not merely `o(1)`. When `k_m->infinity`, `(9.3)` permits a diverging number of atomic defects. This is a quantitative dimension-regime gain as well as a distributional-class gain.

## 10. Exact distinction from posted/public row-submatrix results

The August 7, 2026 Yang--Wen--Shmalo public theorem assumes one fixed centered real subgaussian law with a bounded Lebesgue density and treats square row candidates. The frozen private P12 theorem replaces bounded density by a fixed finite-convolution density ceiling and permits moderate surplus.

The present law `(2.1)` is different from both:

1. it is triangular;
2. it has genuine atoms for every `m`;
3. every fixed convolution retains atoms and therefore has no Lebesgue density;
4. the concrete application has a diverging number of mask defects in the whole matrix;
5. the proof uses a new codimension-loss small-ball estimate plus clean-row entropy stability, not the posted bounded-density local-CLT theorem as a restatement.

A bounded fresh search on 20 September 2026 surfaced the Yang--Wen--Shmalo bounded-density theorem and the earlier Gaussian row-submatrix theorem, but no matching atomic rare-dropout moderate-surplus result. This is dated negative evidence only, not a novelty certificate.

## 11. Essential sanity checker — executed code and actual output

The following checker was executed in this run. It verifies the concrete asymptotic balances, a finite benchmark of the lower-tail exponent, and persistence of convolution atoms.

```python
import math

gamma = 2.0
eps = 1.0

def h(g):
    return g*math.log(g) - (g-1.0)*math.log(g-1.0)

print("RARE_DROPOUT_ATOMIC_UNIVERSALITY_CHECK")
print(f"h(2)={h(gamma):.12f}")
for m in (10**6, 10**9, 10**12, 10**18):
    k = math.sqrt(m)
    sigma = m**(-1.0/3.0)
    q = m**(-1.5) / math.log(m)
    p = 1.0 - q
    N = gamma*m
    mu = N*m*q
    eta = math.sqrt(mu/k)
    Dnorm = math.sqrt(1.0 + p*sigma*sigma)
    rho = sigma/Dnorm

    smoothing = m*rho*rho / math.log(math.e/rho)
    mod_penalty = k*(math.log(m)+math.log(math.e/rho))/m
    defect_ratio_mean = mu/k
    atom_mass = q/2.0
    main_per_m = h(gamma) - (h(gamma)+eps)*(1.0-eta)

    print(
        f"m={m:.0e}  mu={mu:.6g}  mu/k={defect_ratio_mean:.6g}  "
        f"eta={eta:.6g}  smoothing={smoothing:.6g}  "
        f"moderate_penalty={mod_penalty:.6g}  atom={atom_mass:.6g}  "
        f"lower_main_per_m={main_per_m:.6g}"
    )
    assert smoothing > 1.0
    assert mod_penalty < 0.1
    assert defect_ratio_mean < 0.2
    assert main_per_m < 0.0

for m in (10**6, 10**9, 10**12):
    k = math.sqrt(m)
    q = m**(-1.5) / math.log(m)
    mu = gamma*m*m*q
    assert abs((mu/k)*math.log(m) - gamma) < 1e-10

m = 10**9
sigma = m**(-1/3)
q = m**(-1.5)/math.log(m)
for ell in (1,2,3,5):
    atomic_lower = (q/2.0)**ell
    assert atomic_lower > 0.0
    print(f"ell={ell} convolution_atom_lower={atomic_lower:.6e}")

print("ASYMPTOTICS: mu~2*sqrt(m)/log(m)->infinity; mu/k=2/log(m)->0")
print("ASYMPTOTICS: m*rho^2/log(e/rho)->infinity; k[log m+log(e/rho)]/m->0")
print("ALL_RARE_DROPOUT_CODIMENSION_CHECKS_PASS")
```

Actual stdout:

```text
RARE_DROPOUT_ATOMIC_UNIVERSALITY_CHECK
h(2)=1.386294361120
m=1e+06  mu=144.765  mu/k=0.144765  eta=0.38048  smoothing=17.8387  moderate_penalty=0.0194207  atom=3.61912e-11  lower_main_per_m=-0.0920634
m=1e+09  mu=3051.91  mu/k=0.0965099  eta=0.31066  smoothing=126.458  moderate_penalty=0.000905392  atom=7.62978e-16  lower_main_per_m=-0.258673
m=1e+12  mu=72382.4  mu/k=0.0723824  eta=0.26904  smoothing=979.399  moderate_penalty=3.78414e-05  atom=1.80956e-20  lower_main_per_m=-0.357992
m=1e+18  mu=4.82549e+07  mu/k=0.0482549  eta=0.21967  smoothing=67496.8  moderate_penalty=5.6262e-08  atom=1.20637e-29  lower_main_per_m=-0.475803
ell=1 convolution_atom_lower=7.629776e-16
ell=2 convolution_atom_lower=5.821349e-31
ell=3 convolution_atom_lower=4.441559e-46
ell=5 convolution_atom_lower=2.585586e-76
ASYMPTOTICS: mu~2*sqrt(m)/log(m)->infinity; mu/k=2/log(m)->0
ASYMPTOTICS: m*rho^2/log(e/rho)->infinity; k[log m+log(e/rho)]/m->0
ALL_RARE_DROPOUT_CODIMENSION_CHECKS_PASS
```

The numerical benchmark is only a sanity check; theorem `(3.2)` is proved analytically in Sections 4--7.

## 12. Failed-route history and residual obstruction

Preserved failed route from the predecessor: trying to condition on a Bernoulli mask and demand a uniform positive projected covariance fails, because sparse adaptive directions can lie in inactive coordinates and make the conditional covariance singular.

The present theorem avoids that failure by paying one continuous dimension per dropout. It therefore handles only regimes where the total number of dropouts is `o_P(k_m)`.

The next genuine obstruction is the **extensive-mask regime**

`N_m m q_m comparable to k_m` or larger.

There the exponent loss in `(9.2)` is order `m` and cannot be discarded. A further theorem would need to recover some of the missing powers from the Rademacher component itself, i.e. a hybrid discrete/continuous projected small-ball estimate on the kernel of the active Gaussian mask. That is materially different from another Fourier-tail or positive-floor refinement.

No claim is made here for constant dropout probability, for the unsmoothed Rademacher endpoint, or for arbitrary atomic triangular arrays. Those remain **UNKNOWN**.

## 13. ledger_delta

- track: `NM13-12 / P12 successor universality`
- canonical_P12_theorem: unchanged
- canonical_P12_hypotheses: iid centered variance one; fixed `q`; uniform `||f_m^{*q}||_infty`; `N_m/m->gamma>1`; `k_m log m=o(m)`
- canonical_P12_audit_status: unchanged / protocol-open
- previous_NM12_obstruction: Bernoulli Gaussian mask can destroy the positive projected covariance floor
- new_theorem: `NM12-P12-ATOMIC-DROPOUT`
- new_assumption_gain: deterministic positive scale floor removed; atoms allowed
- quantitative_dropout_regime: `N_m m q_m=o(k_m)`
- new_mechanism: projected continuous rank `>=k_m-Dcal_m` plus deletion of at most `Dcal_m` defective rows
- concrete_family: `k_m=floor(sqrt(m))`, `sigma_m=m^(-1/3)`, `q_m=m^(-3/2)/log m`
- concrete_before: UNKNOWN / uncovered
- concrete_after: exponent `-h(gamma)` proved author-side
- concrete_total_dropouts: diverges like `gamma sqrt(m)/log m`
- fixed_convolution_density: none; every fixed convolution has atoms
- T03_before: `[6.30297437506, 12.319634446193]`
- T03_after: same
- NM13-03_coordination: Schur branch-crossing / endpoint `12.319634446194`; third-full route conditional
- NM13-07_coordination: pivoted nested-Schur cascade / endpoint `12.319634446193`; third-full route conditional
- posted_claim_repackaged: no
- checker_status: `ALL_RARE_DROPOUT_CODIMENSION_CHECKS_PASS`
- independent_review: pending
- next_attack: hybrid discrete/continuous projected small ball when `Dcal_m` is order `k_m`
