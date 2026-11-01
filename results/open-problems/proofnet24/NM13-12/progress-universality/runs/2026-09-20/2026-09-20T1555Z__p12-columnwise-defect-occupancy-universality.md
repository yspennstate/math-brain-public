Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED.**

# NM13-12 — columnwise defect-occupancy universality for atomic near-lattice matrices

Repository / branch: private `yspennstate/math-open-problems` / `master`  
Worker: `NM13-12` / `proofnet24/NM13-12/progress-universality`  
Controlling policy: `operations/PROGRESS20_2026-09-20.md`, current LIVE20 mapping  
Primary applied parent: **P12 unresolved triangular/universality successor**  
T03 coordination: **NM13-03 / NM13-07 read for current boundary only; no lifted-RDT duplication**  
Status: **PARTIAL / NEW AUTHOR-SIDE COMPLETE RATE EXTENSION OF THE ATOMIC SUCCESSOR / INDEPENDENT REVIEW PENDING**

## 0. Compact handoff and route selection

The canonical P12 report remains

`proofnet24/P12-smooth-iid/runs/2026-09-17/2026-09-17T18-20-03Z__run-report.md`.

Its frozen theorem is unchanged. For `F in {R,C}`, let `A_m in F^{N_m x m}` have iid centered variance-one entries with density `f_m`. Assume one fixed integer `q>=1` and one uniform finite constant `M` satisfy

`sup_m ||f_m^{*q}||_infty <= M`,

and assume

`N_m/m -> gamma>1`, `k_m=r_m+1`, `k_m log m=o(m)`.

Then

`(k_m/m) log M^F_{m,r_m}(A_m) ->_P -h(gamma)/d_F`,

where `d_R=1`, `d_C=2` and

`h(gamma)=gamma log gamma-(gamma-1)log(gamma-1)`.

There is **no fourth-moment assumption and no positive-moment assumption above variance normalization** in that theorem. Its protocol-open items are audit/package gates rather than missing author-side mathematics. The mathematical successor remains universality for triangular laws outside every uniform finite-convolution density ceiling.

The immediate NM13-12 predecessor is

`2026-09-20T1454Z__p12-atomic-rare-dropout-codimension-universality.md`.

It treated the atomic model

`xi_m=(R+sigma_m B_m G)/sqrt(1+p_m sigma_m^2)`,

with `B_m~Bernoulli(p_m)`, `q_m=1-p_m`, under the strong global-defect condition

`N_m m q_m=o(k_m)`.

That proof used one global count `Dcal_m` for two logically different tasks: lower-extreme projected small balls and upper-extreme deletion of defective rows. This run separates the two scales. The lower extreme only cares about the **largest number of dropouts in one fresh column**, while the upper extreme only needs the **fraction of nonclean rows to vanish**. This yields a strict rate gain by factors that can diverge polynomially.

`POSTED.md` excludes the posted row-submatrix, mesoscopic-spike, kernel/ReLU and zero-margin/Ising results from duplicate research. The theorem below is different: the scalar laws are atomic, every fixed convolution retains atoms, and the quantitative novelty is a strictly larger dropout regime than the preceding unposted atomic theorem.

## 1. P12 predecessor used as the clean-row input

The earlier NM13-12 vanishing-noise theorem for

`tilde xi_m=(R+sigma_m G)/sqrt(1+sigma_m^2)`

has exact hypotheses

`(S1) m sigma_m^2/log(e/sigma_m) -> infinity`,

`(S2) k_m[log m+log(e/sigma_m)] = o(m)`,

together with `N_m/m->gamma>1`. Under these hypotheses,

`(k_m/m) log M^R_{m,r_m}(tilde A_m) ->_P -h(gamma)`.

This is the only nontrivial predecessor theorem invoked below. All new mask estimates are proved here.

## 2. New theorem — anisotropic dropout accounting

For each `m`, let

- `R` be Rademacher;
- `G~N(0,1)`;
- `B~Bernoulli(p_m)` with `p_m=1-q_m`;
- `(R,G,B)` independent;
- `0<sigma_m<=1`.

Put

`nu_m^2=1+p_m sigma_m^2`,

`xi_m=(R+sigma_m B G)/nu_m`,

and let `A_m in R^{N_m x m}` have iid entries with this law. Define

`mu_m := N_m q_m`.

For each column `j`, let

`D_{m,j}=# {i<=N_m: B_{ij}=0}`,

and let `D_m^*=max_{j<=m}D_{m,j}`.

### Theorem NM12-P12-COLUMN-OCCUPANCY

Assume

`N_m/m -> gamma>1`,

`k_m=r_m+1`,

`k_m log m=o(m)`,

and `(S1)--(S2)`. Suppose additionally

`(C1) mu_m=N_m q_m ->0`,

and there is an integer sequence `d_m>=1` such that

`(C2) d_m=o(k_m)`,

`(C3) m (e mu_m/d_m)^{d_m} ->0`.                         (2.1)

Then

`boxed:`

`(k_m/m) log M^R_{m,r_m}(A_m) ->_P -h(gamma)`.             (2.2)

The predecessor condition `N_m m q_m=o(k_m)` is **not** assumed.

### Explicit sufficient rate criterion

If

`k_m->infinity`, `mu_m->0`,

and

`log m / [k_m log(1/mu_m)] ->0`,                           (2.3)

then `(C2)--(C3)` hold. Indeed, once `mu_m<e^{-2}`, set

`L_m=log(1/(e mu_m))`

and

`d_m=ceil(3 log m/L_m)`.                                   (2.4)

Then `d_m=o(k_m)`, while

`m(e mu_m/d_m)^{d_m}`
` <= m(e mu_m)^{d_m}`
` <= m exp[-L_m d_m]`
` <= m^{-2}`.                                               (2.5)

Thus the theorem reaches masks much denser than the global-defect theorem whenever `k_m` grows.

## 3. Strict class separation from frozen P12

For every `m` with `q_m>0`,

`P{xi_m=+1/nu_m}=q_m/2`,

`P{xi_m=-1/nu_m}=q_m/2`.

For every fixed convolution depth `ell>=1`, the `ell`-fold convolution has an atom at `ell/nu_m` of mass at least

`(q_m/2)^ell>0`,                                             (3.1)

coming from all `ell` masks being off and all Rademachers being `+1`. Therefore no fixed convolution is absolutely continuous. In particular neither frozen P12 nor a bounded-density row-submatrix theorem applies.

The exact difference from the previous NM13-12 atomic theorem is quantitative, not cosmetic:

- predecessor: global number of dropped Gaussian coordinates had to satisfy `Dcal_m=o_P(k_m)`, enforced by `N_m m q_m=o(k_m)`;
- new theorem: the lower proof needs only `D_m^*=o_P(k_m)`, and the upper proof needs only an `o_P(m)` number of nonclean rows.

Those are strictly weaker requirements.

## 4. Column occupancy lemma

Each `D_{m,j}` is `Binomial(N_m,q_m)` with mean `mu_m`. For an integer `d>=mu_m`, the standard binomial tail estimate gives

`P{D_{m,j}>=d} <= (e mu_m/d)^d`.                            (4.1)

Hence by a union bound over the `m` columns,

`P{D_m^*>=d_m}`
` <= m(e mu_m/d_m)^{d_m}`
` ->0`                                                       (4.2)

by `(C3)`. Thus

`D_m^*/k_m ->_P 0`.                                        (4.3)

This replaces the predecessor's global estimate `Dcal_m/k_m->_P0`.

## 5. Lower extreme — only the fresh column's defects cost dimensions

Fix a mask realization with `D_m^*<=d_m`. Fix a candidate row set `T` with

`|T|=m+r_m=m+k_m-1`,

and a fresh column `C_j` of `(A_m)_T`. Freeze all other columns and write

`H_j=span{C_l:l!=j}`.

Since `H_j` is generated by at most `m-1` vectors in `R^{m+k_m-1}`,

`dim H_j^perp >= k_m`.                                     (5.1)

Choose measurably any `k_m`-dimensional subspace

`W_j subset H_j^perp`.

Let `I_j subset T` be the inactive coordinates of the fresh column. Because `T subset [N_m]`,

`|I_j| <= D_{m,j} <= D_m^* <= d_m`.                        (5.2)

Let

`E_j={x in R^T: x_i=0 for i in I_j}`.

Then

`U_j=W_j intersect E_j`

has dimension

`ell_j>=k_m-|I_j|>=k_m-d_m`.                               (5.3)

Let `Q_j` be orthogonal projection onto `U_j`. Conditional on the full mask, all other columns, and the fresh Rademacher coordinates, every coordinate that contributes to `U_j` has its Gaussian switched on. Therefore

`Q_j C_j=a_j+rho_m Z_j`,                                   (5.4)

where

`rho_m=sigma_m/nu_m`

and `Z_j` is standard Gaussian on the `ell_j`-dimensional space `U_j`.

For every `s>0`, Gaussian density times Euclidean ball volume yields

`P{||Q_j C_j||<=s | masks,other columns,fresh R}`
` <= (C s/rho_m)^{ell_j}`.                                 (5.5)

Since `U_j subset H_j^perp`,

`dist(C_j,H_j)<=s`

implies `||Q_j C_j||<=s`. At the exponentially small scales used below, `(S2)` gives `C s/rho_m<1`; hence by `(5.3)`

`boxed:`

`P{dist(C_j,H_j)<=s | masks,other columns}`
` <= (C s/rho_m)^{k_m-d_m}`.                               (5.6)

The important point is that **dropouts in every other column are irrelevant to this exponent**. Only the inactive coordinates of the current fresh column remove continuous dimensions.

## 6. Lower extreme — entropy still wins

For a tall candidate matrix `B` with `m` columns, the negative second-moment identity gives

`sum_i sigma_i(B)^(-2)=sum_j dist(C_j,H_j)^(-2)`.

Therefore

`sigma_min(B)<=t`

implies some fresh-column distance at most `sqrt(m)t`.

Condition on a mask realization with `D_m^*<=d_m`, union over all candidates and all `m` fresh columns, and use `(5.6)`:

`P{M_{m,r_m}(A_m)<=t | mask}`
` <= binom(N_m,m+r_m) m`
`    (C sqrt(m)t/rho_m)^{k_m-d_m}.                          (6.1)

Fix `epsilon>0` and set

`t_-=exp[-(h(gamma)+epsilon)m/k_m]`.                        (6.2)

Because `k_m log m=o(m)` and `r_m=k_m-1=o(m)`,

`log binom(N_m,m+r_m)=h(gamma)m+o(m)`.                      (6.3)

Also `1<=nu_m<=sqrt(2)`, so `(S2)` implies

`k_m[log m+log(e/rho_m)]=o(m)`.                            (6.4)

Using `d_m/k_m->0`, the logarithm of the right side of `(6.1)` at `t=t_-` is

`h(gamma)m`
` -(h(gamma)+epsilon)m(1-d_m/k_m)`
` +o(m)`
` =-epsilon m+o(m)`.                                       (6.5)

Together with `(4.2)`,

`P{(k_m/m)log M_{m,r_m}(A_m)<-h(gamma)-epsilon}->0`.       (6.6)

This proves the lower half of `(2.2)`.

## 7. Upper extreme — row thinning only needs o(m), not o(k)

Call a row clean if all of its `m` masks equal one. Let `R_m^def` be the number of nonclean rows. A union bound inside one row gives

`P{row nonclean}=1-(1-q_m)^m <=m q_m`.

Therefore

`E R_m^def <= N_m m q_m = m mu_m`.                         (7.1)

Set

`eta_m=sqrt(mu_m)->0`.

Markov's inequality gives

`P{R_m^def>eta_m m} <= sqrt(mu_m)->0`.                     (7.2)

This is where the predecessor was unnecessarily strong: there is no need for `R_m^def=o_P(k_m)`. Losing `o(m)` rows preserves the aspect ratio and hence the candidate entropy.

Define the deterministic row count

`N'_m=N_m-ceil(eta_m m)`.

Then

`N'_m/m->gamma`.                                            (7.3)

On the event in `(7.2)`, there are at least `N'_m` clean rows. Select the first `N'_m` clean rows by row index, obtaining `A_m^circ`. The selection depends only on the mask and is independent of all `R,G` variables. Conditional on the mask,

`A_m^circ=c_m tilde A_m`,                                  (7.4)

where `tilde A_m` has iid full-activation entries

`(R+sigma_m G)/sqrt(1+sigma_m^2)`

and

`c_m=sqrt(1+sigma_m^2)/sqrt(1+p_m sigma_m^2)`.             (7.5)

Since every row set available inside `A_m^circ` is also available in `A_m`,

`M_{m,r_m}(A_m)<=M_{m,r_m}(A_m^circ)`
`                 =c_m M_{m,r_m}(tilde A_m)`.              (7.6)

The predecessor vanishing-noise theorem applies to `tilde A_m` because `(7.3)` preserves `gamma` and `(S1)--(S2)` are unchanged. Hence

`(k_m/m)log M_{m,r_m}(tilde A_m)->_P-h(gamma)`.            (7.7)

Moreover `1<=c_m<=sqrt(2)`, so `k_m log c_m/m->0`. Together with `(7.2)`, `(7.6)--(7.7)` give

`P{(k_m/m)log M_{m,r_m}(A_m)>-h(gamma)+epsilon}->0`.       (7.8)

Combining `(6.6)` and `(7.8)` proves `(2.2)`. QED.

## 8. Concrete previously uncovered P12-successor application

Take

`gamma=2`,

`k_m=floor(sqrt(m))`,

`sigma_m=m^{-1/3}`,

and

`q_m=1/[m (log m)^2]`                                      (8.1)

for sufficiently large `m`.

Then

`mu_m=N_m q_m ~ 2/(log m)^2 ->0`.                          (8.2)

The sufficient occupancy choice `(2.4)` satisfies

`d_m=O(log m/log log m)=o(sqrt(m))`.                       (8.3)

Conditions `(S1)--(S2)` hold because

`m sigma_m^2/log(e/sigma_m)`
` =m^{1/3}/[1+(1/3)log m] ->infinity`,                     (8.4)

and

`sqrt(m)[log m+log(e m^{1/3})]/m->0`.                      (8.5)

But the predecessor global-defect hypothesis fails by a diverging factor:

`N_m m q_m/k_m`
` ~ 2 sqrt(m)/(log m)^2 ->infinity`.                       (8.6)

Indeed the expected total number of switched-off Gaussian coordinates is

`N_m m q_m ~ 2m/(log m)^2 ->infinity`,                    (8.7)

and is much larger than `k_m`; the expected number of nonclean rows is of the same order. Thus this is not an all-masks-active coupling and is not covered by the preceding atomic theorem.

Nevertheless Theorem NM12-P12-COLUMN-OCCUPANCY gives

`boxed:`

`(k_m/m) log M^R_{m,r_m}(A_m) ->_P -h(2)=-2log2+?`         (8.8)

More explicitly, `h(2)=2 log 2`, so the limit is

`boxed: -2 log 2`.                                         (8.9)

The scalar laws remain atomic for every `m`, and every fixed convolution depth retains an atom by `(3.1)`.

### Applied successor before / after

Before this run, the explicit family `(8.1)` was **UNKNOWN / uncovered** by both frozen P12 and NM13-12's atomic rare-dropout theorem, because frozen P12 requires an absolutely continuous fixed convolution and the atomic predecessor requires `(8.6)` to tend to zero.

After this run, the full row-submatrix exponent `(8.9)` is proved author-side, pending independent review.

### Demonstrated theory gain, separately

The quantitative mask condition improves from

`N_m m q_m=o(k_m)`

into the pair

- `N_m q_m->0` for entropy-stable row thinning;
- `D_m^*=o_P(k_m)` for the lower projected-small-ball exponent,

with the explicit deterministic sufficient condition `(2.3)`. For `k_m=sqrt(m)`, the theorem allows for example

`q_m=1/[m L_m]`

for very slowly diverging `L_m`, provided

`log m=o(sqrt(m) log L_m)`.

Thus the admissible dropout probability can be almost of order `1/m`, whereas the predecessor demanded `q_m=o(m^{-3/2})` in this surplus regime.

## 9. T03 coordination — parent reported separately

The newest complete NM13-03 report read in this run is

`proofnet24/NM13-03/progress-perceptron-theory/runs/2026-09-20/2026-09-20__t03-klfree-hinge-coupling-alpha123196344461908.md`.

It preserves the exact Gaussian `kappa=-1`, radius-`sqrt(N)` source model and moves the review-pending directed complete-second endpoint to

`12.3196344461908`.

Its complete-third application remains **CONDITIONAL** pending outward cell / Gaussian-moment enclosure.

The newest complete NM13-07 substantive report read here is

`proofnet24/NM13-07/progress-perceptron/runs/2026-09-20/2026-09-20__t03-pivoted-x-schur-cascade-alpha12319634446193.md`,

with endpoint `12.319634446193` and a conditional nested-Schur third-full route. Newer scalar-partition/Bregman checker/output artifacts appeared while this run was executing, but no newer completed substantive report was used as a promoted source claim.

Therefore this worker does not duplicate stationarity, Schur, Krawczyk, Gaussian-quadrature, entropy-cage or lifted-RDT calculations. The current T03 parent entering and leaving NM13-12 is

`[6.30297437506, 12.3196344461908]`

at the project's present review-pending upper-bound status. **NM13-12 causes no T03 movement in this run.**

## 10. Sanity checker and executed output

Executed checker:

`proofnet24/NM13-12/progress-universality/runs/2026-09-20/artifacts/2026-09-20T1555Z__columnwise_dropout_checker.py`

creation commit `aeab75c5056ecea119080283a6f013daf0919cd3`.

Archived executed output:

`proofnet24/NM13-12/progress-universality/runs/2026-09-20/artifacts/2026-09-20T1555Z__columnwise_dropout_checker.out`

creation commit `809eb099c67624bbfd2e704c14b4ad2862327a58`.

The checker verifies at `m=10^8,10^12,10^16,10^20` that the new column-occupancy union bound is already tiny, `d_m/k_m` decreases rapidly, the predecessor global-defect ratio is already large and increasing, the row-loss fraction bound tends down, `(S1)--(S2)` move in the correct directions, and the fixed-depth atom mass remains strictly positive. It ends

`ALL_COLUMNWISE_OCCUPANCY_CHECKS_PASS`.

The numerical checker is only a sanity test; the theorem is proved analytically in Sections 4--7.

## 11. Honest residual obstruction and next attack

The new theorem still requires `N_m q_m->0`, equivalently `m q_m->0` at fixed aspect ratio. The next genuinely different regime is

`q_m ~ c/m`, `c>0`,

where a positive fraction `1-e^{-c}` of rows contain at least one dropout. The lower-extreme column occupancy remains only logarithmic and is harmless for `k_m` much larger than `log m/loglog m`, but the clean-row deletion argument now removes a **linear** fraction of rows and changes the entropy from `h(gamma)` to `h(gamma e^{-c})`. Recovering the original exponent requires using partially defective rows constructively rather than discarding them.

A plausible but unproved next mechanism is a rowwise sparse-defect local-limit theorem: on the useful spread directions, `O_P(1)` missing Gaussian coordinates should perturb the continuous characteristic function by only `O(1/m)` per row while the Rademacher backbone prevents lattice concentration. That step is **UNKNOWN** here and is not claimed.

## 12. ledger_delta

- track: `NM13-12 / P12 successor`
- canonical_P12_theorem_changed: no
- canonical_P12_protocol_metric_changed: no
- predecessor_atomic_condition: `N_m m q_m=o(k_m)`
- new_atomic_conditions: `mu_m=N_m q_m->0` plus `m(e mu_m/d_m)^{d_m}->0` for some `d_m=o(k_m)`
- explicit_sufficient_condition: `k_m->infinity`, `mu_m->0`, `log m/[k_m log(1/mu_m)]->0`
- concrete_application: `gamma=2`, `k_m=floor(sqrt(m))`, `sigma_m=m^{-1/3}`, `q_m=1/[m(log m)^2]`
- application_before: `UNKNOWN / outside frozen P12 and outside atomic rare-dropout theorem`
- application_after: `row-submatrix exponent -h(2)=-2 log 2 proved author-side`
- strict_rate_gain: yes; predecessor defect ratio diverges in the concrete application
- distribution_still_atomic: yes; every fixed convolution retains an atom
- T03_before: `[6.30297437506,12.3196344461908]` at current project status
- T03_after: unchanged by NM13-12
- posted_row_submatrix_repackaged: no
- kernel_ReLU_zero_margin_repackaged: no
- independent_review: pending
- next_obstruction: `critical q_m~c/m; constructive use of partially defective rows`

# END NM13-12 COLUMNWISE DEFECT-OCCUPANCY REPORT
