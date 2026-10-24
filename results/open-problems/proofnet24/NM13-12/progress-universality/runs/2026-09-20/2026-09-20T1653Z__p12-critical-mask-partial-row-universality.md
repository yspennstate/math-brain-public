Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED.**

# NM13-12 — critical-mask partial-row universality for atomic near-lattice matrices

Repository / branch: private `yspennstate/math-open-problems` / `master`  
Worker: `NM13-12` / `proofnet24/NM13-12/progress-universality`  
Controlling policy: `operations/PROGRESS20_2026-09-20.md`, current LIVE20 mapping  
Primary applied parent: **P12 unresolved triangular/universality successor**  
T03 coordination: **NM13-03 / NM13-07 read only for the current boundary; no lifted-RDT duplication**  
Status: **PARTIAL / NEW AUTHOR-SIDE COMPLETE RATE-AND-DISTRIBUTIONAL EXTENSION / INDEPENDENT REVIEW PENDING**

## 0. Compact handoff and materially different route

The canonical P12 report remains

`proofnet24/P12-smooth-iid/runs/2026-09-17/2026-09-17T18-20-03Z__run-report.md`.

Its frozen theorem is unchanged. For `F in {R,C}`, if `A_m in F^{N_m x m}` has iid centered variance-one entries with density `f_m`, one fixed integer `q>=1` and one uniform finite constant `M` satisfy

`sup_m ||f_m^{*q}||_infty <= M`,

and

`N_m/m -> gamma>1`, `k_m=r_m+1`, `k_m log m=o(m)`,

then

`(k_m/m) log M^F_{m,r_m}(A_m) ->_P -h(gamma)/d_F`,

where `d_R=1`, `d_C=2` and

`h(gamma)=gamma log gamma-(gamma-1)log(gamma-1)`.

There is **no fourth-moment assumption and no positive-moment assumption above variance normalization** in that frozen theorem. The remaining mathematical successor is triangular universality outside a uniform microscopic finite-convolution density ceiling. The frozen protocol/audit obligations are not reopened here.

The immediate NM13-12 predecessor is

`2026-09-20T1555Z__p12-columnwise-defect-occupancy-universality.md`.

It treated the atomic dropout law

`xi_m=(R+sigma_m B_m G)/sqrt(1+p_m sigma_m^2)`,

with `B_m~Bernoulli(p_m)`, `q_m=1-p_m`, and proved the P12 exponent under `mu_m=N_m q_m->0` plus a column-occupancy tail. Its upper extreme still deleted every row containing a dropout. The report explicitly named the next obstruction as the critical regime `q_m~c/m`: column defects stay logarithmic, but a positive fraction of rows are defective, so clean-row deletion changes the aspect ratio.

This run resolves that obstruction and in fact reaches

`m q_m = O(log m)`

provided `log m=o(k_m)`. The method is materially different: **no defective row is deleted**. The mask of each fresh row is absorbed as an `O(log m)` coordinate deletion inside the already proved P12/P13 robust-normal geometry, and the one- and two-normal microscopic estimates are re-proved conditionally on that mask.

`POSTED.md` forbids rediscovery of the already posted row-submatrix, kernel/ReLU, mesoscopic-spike and zero-margin/Ising claims. The theorem below is not one of those statements: every scalar law here is atomic, every fixed convolution retains an atom, and the new content is a quantitative partially-smoothed triangular-array extension beyond both frozen P12 and the latest unposted atomic predecessor. No publication novelty claim is made.

## 1. Model and theorem

For each `m`, let

- `R` be Rademacher;
- `G~N(0,1)`;
- `B~Bernoulli(p_m)`, with `q_m=1-p_m`;
- `(R,G,B)` independent;
- `0<sigma_m<=1`.

Set

`nu_m^2=1+p_m sigma_m^2`,

`xi_m=(R+sigma_m B G)/nu_m`,                             (1.1)

and let `A_m in R^{N_m x m}` have iid entries with this law. As usual,

`M^R_{m,r}(A)=min_{T subset [N_m], |T|=m+r} sigma_m(A_T)`.

Assume

`(H1) N_m/m -> gamma>1`,

`(H2) k_m=r_m+1`, `log m=o(k_m)`,

`(H3) m sigma_m^2/log(e/sigma_m) -> infinity`,

`(H4) k_m[log m+log(e/sigma_m)] = o(m)`,

and for one fixed finite `C_q`,

`(H5) m q_m <= C_q log m` for all sufficiently large `m`.  (1.2)

### Theorem NM12-P12-CRITICAL-MASK

Under `(H1)--(H5)`,

`boxed:`

`(k_m/m) log M^R_{m,r_m}(A_m) ->_P -h(gamma)`.             (1.3)

Thus the exact P12 exponent survives when the expected number of switched-off Gaussian coordinates in **each row** is as large as a constant multiple of `log m`. In particular it covers the previously named critical window `q_m~c/m` and an additional logarithmic factor beyond it.

This is not a global superset of the preceding theorem because `(H2)` adds `log m=o(k_m)`. It is a strict quantitative enlargement on every moderate-surplus sequence satisfying that condition, including the concrete `k_m=floor(sqrt(m))` application in Section 10.

## 2. Strict separation from frozen P12

For every `m` with `q_m>0`,

`P{xi_m=+1/nu_m}=q_m/2`,

`P{xi_m=-1/nu_m}=q_m/2`.

For every fixed convolution depth `ell>=1`, the `ell`-fold convolution has an atom at `ell/nu_m` of mass at least

`(q_m/2)^ell>0`,                                           (2.1)

coming from all masks off and all Rademachers `+1`. Therefore no fixed convolution is absolutely continuous, much less bounded by a Lebesgue density ceiling. Frozen P12 does not apply.

The difference from the immediate atomic predecessor is also strict. That theorem required `N_m q_m->0` in order to throw away an `o(m)` fraction of nonclean rows. Here `N_m q_m` may diverge like `Theta(log m)`, and Section 10 gives a law for which the number of clean rows is itself `o(m)`.

## 3. Global row-and-column mask occupancy

For row `i`, let

`R_i=#{j<=m:B_{ij}=0}`,

and for column `j`, let

`D_j=#{i<=N_m:B_{ij}=0}`.

Their means obey, for all large `m`,

`E R_i = m q_m <= C_q log m`,

`E D_j = N_m q_m <= 2 gamma C_q log m`.                     (3.1)

Put `C_*=2 max(1,gamma) C_q`. Choose a fixed `A>C_* e` so large that

`A log(A/(e C_*))>4`,                                      (3.2)

and set

`L_m=ceil(A log m)`.                                       (3.3)

For a binomial random variable of mean `mu<=C_*log m`, Chernoff gives

`P{X>=L_m} <= (e mu/L_m)^{L_m}`
`            <= m^{-A log(A/(e C_*))+o(1)}`.               (3.4)

There are `N_m+m=O(m)` rows and columns, hence

`P{ max_i R_i > L_m or max_j D_j > L_m } ->0`.             (3.5)

Call the event in (3.5)'s complement `E_m`. By `(H2)`,

`L_m/k_m ->0`,                                             (3.6)

while `L_m/m->0`.

This single event will serve both extremes, but unlike the predecessor it is never used to discard rows.

## 4. Uniform scalar anti-concentration and inherited geometry

The law (1.1) is centered and has variance one exactly. It also has a mask-uniform fixed scalar concentration gap.

### Lemma 4.1

For all `0<sigma_m<=1` and all `p_m in [0,1]`,

`Q_{xi_m}(1/2):=sup_z P{|xi_m-z|<=1/2} <= 3/4`.            (4.1)

### Proof

Condition on `R=+1` or `R=-1`. The two conditional laws are each mixtures of an atom and a Gaussian centered respectively at

`+1/nu_m`, `-1/nu_m`.

Their center separation is

`2/nu_m >= sqrt(2)>1`.                                     (4.2)

An interval of radius `1/2` has length one and contains at most one conditional center. The branch whose center it contains contributes at most one. For the other branch the interval lies entirely on one side of its center: its atom contributes zero and its centered Gaussian component contributes at most `1/2`. Averaging the two Rademacher branches gives at most `3/4`. QED.

The frozen P12/P13 geometry package records that its random-rounding / sparse-kernel / fresh-private-block useful-normal construction requires only this fixed scalar anti-concentration gap and the normalized second moment. It also proves robust adaptive two-plane geometry **before probability is applied to a genuinely fresh original row**, uniformly over coordinate subspaces generated by `O(log m)` deleted coordinates. In the weak tier its sequential-plane conclusion has scale `tau_m asymp m^{-1}`; strong ordinary pairs retain constant transversality. The family of all deletion sets of size `O(log m)` has cardinality `exp(O((log m)^2))`, already inside that tunable geometry proof.

Consequently the existing useful-normal and adaptive-pair geometry transfers to (1.1) on `E_m`; what remains to prove is the microscopic probability package after conditioning on each fresh row mask. Sections 6--8 do so.

## 5. Lower extreme: partial masks only cost `L_m` powers

Work on `E_m`. Fix a candidate row set `T` with

`|T|=m+r_m=m+k_m-1`,

fix a column `j`, freeze every other column of `(A_m)_T`, and write

`H_j=span{C_l:l!=j}`.

Because `H_j` is generated by at most `m-1` vectors in `R^{m+k_m-1}`,

`dim H_j^perp >= k_m`.                                     (5.1)

Choose a `k_m`-dimensional `W_j subset H_j^perp`. Let `I_j subset T` be the inactive coordinates of the fresh column. On `E_m`,

`|I_j|<=D_j<=L_m`.                                         (5.2)

Let

`E_j={x in R^T:x_i=0 for i in I_j}`,

`U_j=W_j intersect E_j`.

Then

`ell_j:=dim U_j >= k_m-L_m`.                               (5.3)

Conditional on the full mask, the other columns and the fresh Rademacher coordinates, every coordinate contributing to `U_j` has its Gaussian switched on. Thus the orthogonal projection `Q_j` onto `U_j` satisfies

`Q_j C_j = a_j + rho_m Z_j`,                               (5.4)

where

`rho_m=sigma_m/nu_m`

and `Z_j` is standard Gaussian in dimension `ell_j`. Hence for every `s>0`,

`P{dist(C_j,H_j)<=s | mask,other columns}`
` <= P{||Q_j C_j||<=s | mask,other columns}`
` <= (C s/rho_m)^{k_m-L_m}.                                (5.5)

The negative second-moment identity implies that if a candidate matrix has `sigma_min<=t`, some fresh-column distance is at most `sqrt(m)t`. Union over candidates and columns gives on `E_m`

`P{M_{m,r_m}(A_m)<=t | mask}`
` <= binom(N_m,m+r_m) m`
`    (C sqrt(m)t/rho_m)^{k_m-L_m}.                          (5.6)

Set

`t_-=exp[-(h(gamma)+epsilon)m/k_m]`.                        (5.7)

Since `r_m=o(m)`,

`log binom(N_m,m+r_m)=h(gamma)m+o(m)`,                     (5.8)

and `1<=nu_m<=sqrt(2)`, so `(H4)` gives

`k_m[log m+log(e/rho_m)]=o(m)`.                            (5.9)

Using `L_m/k_m->0`, the logarithm of the right side of (5.6) is

`h(gamma)m`
` -(h(gamma)+epsilon)m(1-L_m/k_m)`
` +o(m)`
` =-epsilon m+o(m)`.                                       (5.10)

Together with `P(E_m^c)->0`,

`P{(k_m/m)log M_{m,r_m}<-h(gamma)-epsilon}->0`.            (5.11)

This proves the lower half of (1.3).

## 6. New conditional-mask one-normal local limit theorem

The upper extreme cannot delete defective rows. Instead fix one fresh row mask. Let `I subset[m]` be its inactive coordinate set, `|I|<=L_m`, and let deterministic coefficients `a_j` satisfy

`v=sum_j a_j^2 in [v_0,1]`,

`max_j |a_j| <= C_0/sqrt(m)`.                              (6.1)

Put

`v_I=sum_{j notin I} a_j^2`.

Then

`v-v_I <= C_0^2 L_m/m=o(1)`,                              (6.2)

so `v_I>=v_0/2` for large `m`. Conditional on the mask, the linear form

`Y_I=sum_j a_j xi_j`

has characteristic function

`hat p_I(t)`
` = exp[-sigma_m^2 v_I t^2/(2 nu_m^2)]`
`   prod_j cos(a_j t/nu_m).                                (6.3)

Define

`w_I=(v+sigma_m^2 v_I)/nu_m^2`.                            (6.4)

Because `nu_m^2=1+p_m sigma_m^2`,

`|w_I-v|`
` = sigma_m^2 |v_I-p_m v|/nu_m^2`
` <= q_m + C L_m/m`
` = O(log m/m)=o(1).                                       (6.5)

### Lemma 6.1 — partial-mask local limit

Uniformly in all `I,a` obeying the conditions above,

`||p_I-phi_{w_I}||_infty`
` <= C/m + C sigma_m^{-1} exp(-c m sigma_m^2).              (6.6)

In particular, under `(H3)`, for every fixed `K<infinity`, for all large `m`,

`inf_{|x|<=K} p_I(x)>=c_K>0`,

`sup_x p_I(x)<=C`.                                         (6.7)

### Proof

Choose `eta>0` so that `|a_j t|/nu_m<=1/4` whenever `|t|<=eta sqrt(m)`. For `|x|<=1/4`,

`0<=-log cos x-x^2/2<=C x^4`.

Hence on the low-frequency region,

`hat p_I(t)=exp[-w_I t^2/2-R_I(t)]`,

`0<=R_I(t)<=C t^4 sum_j a_j^4<=C t^4/m`.                  (6.8)

Since `w_I>=v_0/2`,

`|hat p_I(t)-exp(-w_I t^2/2)|`
` <= (C t^4/m) exp(-c t^2)`,                               (6.9)

whose integral is `O(1/m)`.

For `|t|>eta sqrt(m)`, discard the cosine factors and use `v_I>=v_0/2`:

`|hat p_I(t)| <= exp(-c sigma_m^2 t^2)`.                   (6.10)

Its tail integral is at most

`C sigma_m^{-1} exp(-c m sigma_m^2)`.                      (6.11)

The Gaussian target tail is `O(e^{-cm})`. Fourier inversion proves (6.6). Condition `(H3)` makes the second error vanish, and (6.5) keeps `w_I` in a fixed compact subset of `(0,infinity)`, giving (6.7). QED.

Thus **every partially defective fresh row** supplies exactly the centered microscopic lower slab `c s` and upper slab `C s` required by the P12 survivor, with constants independent of its mask.

## 7. Two-normal estimates under a partial mask

Let `u,v` be two unit useful normals frozen before a fresh row is exposed, and put

`z_j=(u_j,v_j)^T`,

`G=sum_j z_j z_j^T`,

`G_I=sum_{j notin I} z_j z_j^T`.                            (7.1)

The existing adaptive-pair theorem is explicitly robust under every deletion set `I` of size `O(log m)`. We use its two tiers as follows.

### 7.1 Ordinary pairs: a two-dimensional conditional-mask local limit

For ordinary pairs, after any such deletion,

`G_I >= c_0 I_2`,                                          (7.2)

and useful-normal low leverage gives `max_j ||z_j||<=C_0/sqrt(m)` on the coordinates entering the microscopic theorem.

Conditional on the mask, the pair

`(<X,u>,<X,v>)`

has characteristic function

`hat p_I(theta)`
` = exp[-sigma_m^2 theta^T G_I theta/(2nu_m^2)]`
`   prod_j cos(theta^T z_j/nu_m).                           (7.3)

Its Gaussian quadratic covariance is

`Sigma_I=(G+sigma_m^2 G_I)/nu_m^2`.                        (7.4)

The same Taylor argument as Section 6, now in `R^2`, gives on `||theta||<=eta sqrt(m)` an `L^1` Fourier error `O(1/m)`. Above that radius, (7.2) gives

`|hat p_I(theta)|<=exp(-c sigma_m^2 ||theta||^2)`,

and therefore the two-dimensional tail integral is

`O(sigma_m^{-2} exp(-c m sigma_m^2))=o(1)`                 (7.5)

by `(H3)`. Since ordinary-pair `G` is uniformly nondegenerate, so is `Sigma_I`. Thus the joint density is uniformly bounded:

`||p_I^{(2)}||_infty<=C`.                                  (7.6)

Consequently an ordinary product slab of width `s` has probability at most

`C s^2`,                                                   (7.7)

which is exactly the canonical real ordinary-pair cost.

### 7.2 Medium pairs: use the active Gaussian directly

For the weak/medium tier the inherited sequential-plane theorem gives, after every `O(log m)` deletion, a retained plane Gram at least

`G_I >= c m^{-2} I_2`                                      (7.8)

(up to changing the inherited absolute constant; this is the `tau_m asymp m^{-1}` weak geometry).

Condition on the mask and Rademacher coordinates. The pair is then a translated Gaussian with covariance

`(sigma_m^2/nu_m^2) G_I`.

Its density is bounded by

`C sigma_m^{-2} (det G_I)^(-1/2)`
` <= C sigma_m^{-2} m^2`.                                  (7.9)

Condition `(H3)` implies `sigma_m^{-2}=o(m)`, hence for all large `m`,

`C sigma_m^{-2} m^2 <= C' m^3`.                            (7.10)

Therefore a medium product slab has probability at most

`C m^3 s^2`,                                               (7.11)

again exactly the canonical real medium-pair cost.

### 7.3 Bad / near-parallel pairs

The frozen survivor deliberately does not demand a two-dimensional gain for the near-parallel bad class. Lemma 6.1 supplies the one-normal upper bound

`P{|<X,u>-a|<=s}<=Cs`,                                     (7.12)

so the canonical bad-pair cost remains `Cs`.

Thus the full ordinary / medium / bad hierarchy

`boxed: Cs^2,  C m^3 s^2,  C s`                            (7.13)

survives despite the fact that every fresh row may contain `Theta(log m)` switched-off Gaussian coordinates.

## 8. Constructive upper extreme without row deletion

The frozen P12/P13 real three-tier survivor implication uses exactly the following distributional inputs after useful-normal/adaptive-pair geometry is frozen:

1. centered variance-one scalar law and a fixed scalar anti-concentration gap;
2. microscopic one-normal lower mass `>=c s` on the useful bounded target window;
3. one-normal upper mass `<=C s`;
4. ordinary / medium / bad pair costs `Cs^2`, `Cm^3s^2`, `Cs`;
5. tunably exponentially small geometry-failure probabilities;
6. probability is applied only to genuinely fresh original rows, never to projected coordinates treated as iid.

Item 1 is Lemma 4.1. Items 2--3 are Lemma 6.1. Item 4 is (7.13). Item 5 is the inherited robust-deletion geometry already valid uniformly over all `O(log m)` coordinate sets; its union class is only `exp(O((log m)^2))`. Item 6 is preserved because at each survivor stage the normals and prior rows are frozen first, then the next original row is exposed; conditioning further on that row's independent mask does not disturb freshness of its Rademacher/Gaussian coordinates.

On `E_m` every row mask belongs to the allowed deletion family, so **all original rows remain available**. There is no thinning factor and no aspect-ratio change.

Take the source marked-row scale

`t_+=exp[-(h(gamma)-epsilon)m/k_m]`,

`s=t_+/sqrt(k_m)`.                                         (8.1)

The deterministic overlap entropy and the three survivor invariants are unchanged. The ordinary/medium/bad probabilities are exactly no worse than the canonical real costs (7.13), while the one-normal lower constant is fixed. Hence the inherited marked-row second-moment/staging argument constructs, with probability tending to one, a row set of size `m+r_m` with least singular value at most `t_+` up to the same subexponential source normalization. Equivalently,

`P{(k_m/m)log M_{m,r_m}>-h(gamma)+epsilon}->0`.            (8.2)

No new `sigma_m^{-1}` penalty enters the ordinary pair or one-normal slab because the conditional-mask local limits converge to nondegenerate Gaussians. The only place a raw Gaussian density ceiling is used is the medium tier; (7.10) absorbs it into the already allowed polynomial `m^3` factor. Combining (8.2) with (5.11) proves Theorem (1.3). QED.

## 9. Why this actually crosses the previous obstruction

The preceding theorem's upper proof selected only fully active rows. If `q_m~c/m`, a row is clean with probability approaching `e^{-c}`, so such thinning changes the available aspect ratio from `gamma` to `gamma e^{-c}` and therefore changes the entropy exponent. At `m q_m` growing like `log m`, the clean fraction even tends to zero.

The present theorem never conditions on a row being clean. It conditions on its **actual** mask and proves that deleting `O(log m)` coordinates from the microscopic linear forms changes neither the one-normal local Gaussian law nor the robust two-normal survivor costs. This is the decisive new mechanism.

## 10. Concrete previously uncovered successor application

Take

`gamma=2`,

`k_m=floor(sqrt(m))`,

`sigma_m=m^{-1/3}`,                                        (10.1)

and

`q_m=log(m)/(4m)`.                                         (10.2)

Then

`m q_m=(1/4)log m`,

`N_m q_m~(1/2)log m`.                                      (10.3)

So the immediate predecessor hypothesis `N_m q_m->0` fails in the strongest possible direction: it diverges. The older global-defect condition fails even more strongly:

`N_m m q_m/k_m ~ (1/2) sqrt(m) log m -> infinity`.         (10.4)

Conditions `(H3)--(H4)` hold because

`m sigma_m^2/log(e/sigma_m)`
` = m^(1/3)/(1+(1/3)log m) -> infinity`,                   (10.5)

and

`k_m[log m+log(e/sigma_m)]/m`
` = O(log m/sqrt(m)) ->0`.                                 (10.6)

The clean-row mechanism fails decisively. A row is clean with probability

`(1-q_m)^m = exp[-(1/4)log m+o(1)]`
`            = m^{-1/4+o(1)}`,                             (10.7)

so the number of clean rows divided by `m` tends to zero in probability; eventually there are not even `m` clean rows with high probability. Nevertheless every row and column has only `O(log m)` defects with high probability, and the new partial-row theorem applies.

Therefore

`boxed:`

`(k_m/m) log M^R_{m,r_m}(A_m) ->_P -h(2)=-2 log 2`.        (10.8)

### Applied successor before / after

Before this run, the explicit law (10.1)--(10.2) was **UNKNOWN / uncovered in the project**:

- frozen P12 fails because every fixed convolution retains atoms;
- the rare-dropout theorem fails because its global defect count is enormous relative to `k_m`;
- the latest columnwise-occupancy theorem fails because `N_m q_m~(1/2)log m`, not `o(1)`;
- its clean-row upper proof cannot be salvaged because the clean-row aspect tends to zero.

After this run, (10.8) is proved author-side, pending later independent review.

This is the source-level application movement for NM13-12. The frozen canonical P12 theorem itself is unchanged.

## 11. T03 coordination and parent before / after

This run does not duplicate the Gaussian exact-sphere stationarity work owned by NM13-03 and NM13-07.

The latest NM13-07 substantive report on `master` during this run is

`proofnet24/NM13-07/progress-perceptron/runs/2026-09-20/2026-09-20__t03-double-semiconcavity-scalarQ-alpha123196344461907498.md`.

It moves the review-pending directed exact-sphere `kappa=-1` upper endpoint to

`12.3196344461907498`,

while its complete-third scalar-Q route remains conditional pending outward tube execution. It explicitly retires further complete-second decimal shaving as a substantive attack.

The latest NM13-03 substantive report is

`proofnet24/NM13-03/progress-perceptron-theory/runs/2026-09-20/2026-09-20__t03-outer-smoothing-selfbound-alpha12287222221600.md`.

It keeps the directed tier fixed and moves the stronger supported-CONDITIONAL third-full point to

`12.287222221600`,

still without directed outward four-dimensional enclosure.

Accordingly, the iid-Gaussian T03 parent before and after this NM13-12 run is unchanged:

`boxed: [6.30297437506, 12.3196344461907498]`.              (11.1)

The stronger `12.287222221600` value remains CONDITIONAL and is not promoted here.

## 12. Essential executed checker

Executed code:

`proofnet24/NM13-12/progress-universality/runs/2026-09-20/artifacts/2026-09-20T1653Z__critical_mask_partial_row_checker.py`

Archived actual output:

`proofnet24/NM13-12/progress-universality/runs/2026-09-20/artifacts/2026-09-20T1653Z__critical_mask_partial_row_checker.out`

The checker verifies at `m=10^6,10^9,10^12,10^18`:

- the explicit simultaneous row/column Chernoff union bound with `L=4 log m` decreases rapidly;
- `L/k_m->0`;
- `(H3)` increases and `(H4)` decreases in the expected direction;
- `N_m q_m~(1/2)log m` diverges, so the latest predecessor is genuinely inapplicable;
- the old global-defect ratio diverges;
- the clean-row aspect agrees with `2m^{-1/4}` and tends to zero;
- the two-dimensional high-frequency factor `sigma_m^{-2} exp(-c m sigma_m^2)` eventually decays decisively;
- fixed-depth convolution atoms remain strictly positive.

It ends

`ALL_CRITICAL_MASK_PARTIAL_ROW_CHECKS_PASS`.

The numerical checker is a sanity test only; the theorem proof is Sections 3--8.

## 13. Failure history and residual obstruction

The preceding row-deletion route is now retired for critical masks: it is mathematically incapable of preserving the entropy exponent once the clean fraction is nontrivial, and for the concrete application its clean fraction tends to zero.

The present proof deliberately stops at `m q_m=O(log m)` because the inherited adaptive two-plane theorem is certified uniformly for `O(log m)` coordinate deletions. Extending to

`m q_m >> log m`

without strengthening that geometry remains **UNKNOWN**. Two plausible but unproved routes are now sharply separated:

1. prove adaptive useful-normal/two-plane robustness after `o(k_m)` or even `o(m)` random coordinate deletion, which would immediately enlarge the mask rate through the conditional-mask local limits above;
2. when active Gaussian covariance becomes poorly conditioned, combine Gaussian small-ball powers on the active subspace with inverse-Littlewood-Offord/Rademacher powers on its kernel.

The second route is still needed for genuinely sparse activation or for fixed surplus where `O(log m)` lost dimensions are not negligible. No such claim is made here.

## 14. ledger_delta

- worker: `NM13-12`
- track: `progress-universality`
- canonical_parent: frozen P12 finite-convolution row-submatrix theorem
- canonical_parent_changed: `no`
- canonical_hypotheses: `centered variance-one iid; fixed q; uniform ||f_m^{*q}||_infty; N/m->gamma>1; k log m=o(m)`
- canonical_successor: `triangular laws without uniform microscopic finite-convolution smoothing`
- immediate_predecessor: `2026-09-20T1555Z__p12-columnwise-defect-occupancy-universality.md`
- predecessor_dropout_requirement: `N_m q_m -> 0 plus column occupancy`
- new_theorem: `critical-mask partial-row atomic universality`
- new_dropout_regime: `m q_m = O(log m)` with `log m=o(k_m)`
- mechanism_gain: `use partially defective rows directly via O(log m) coordinate-deletion robust geometry + conditional-mask 1D/2D local limits`
- row_deletion_used: `no`
- concrete_application: `gamma=2, k=floor(sqrt m), sigma=m^(-1/3), q=log(m)/(4m)`
- application_before: `UNKNOWN / outside frozen P12 and outside both prior atomic-dropout theorems`
- application_after: `row-submatrix exponent -h(2)=-2 log 2 proved author-side`
- clean_row_aspect_in_application: `2 m^(-1/4+o(1)) -> 0`
- fixed_convolution_absolute_continuity: `fails; every fixed convolution has an atom`
- T03_directed_before: `[6.30297437506, 12.3196344461907498]`
- T03_directed_after: `[6.30297437506, 12.3196344461907498]`
- T03_supported_conditional_peer_point: `12.287222221600`
- POSTED_repackaging: `no`
- independent_review: `pending`
- checker: `2026-09-20T1653Z__critical_mask_partial_row_checker.py`
- checker_output: `2026-09-20T1653Z__critical_mask_partial_row_checker.out`
- checker_verdict: `ALL_CRITICAL_MASK_PARTIAL_ROW_CHECKS_PASS`
- residual_obstruction: `m q_m >> log m / stronger random-deletion adaptive-plane robustness or hybrid discrete-continuous small ball`

# END NM13-12 CRITICAL-MASK PARTIAL-ROW REPORT
