Model actually run: **GPT-5.6 Sol. Reasoning effort: UNVERIFIED — no authenticated applied-effort selector or GPT-6 receipt is exposed.**

# P20 T10 — weighted projective correctors and delayed Richardson exactification

Date: 2026-09-20 UTC.  
Repository / branch: private `yspennstate/math-open-problems` / `master`.  
Controlling directive: `operations/PROGRESS20_2026-09-20.md`.  
Canonical parent: `operations/claims/PROB10-10.md`.  
Model: undirected nearest-neighbor FPP on `Z^2` with iid physical-edge weights `Exp(1)`.  
Status: **PARTIAL / OPEN** for the source problem. The new theorem arguments below are **CANDIDATE_PROVED pending later independent review**. No certification, novelty, or priority claim is made.

## 1. Exact source and frozen source-facing metric

The exact source remains Auffinger--Damron--Hanson, *50 years of first passage percolation*, arXiv:1511.03262, Question 4: show that if the passage-time distribution is continuous then the limit shape is strictly convex. Section 2.8 explicitly treats strict convexity as conjectural. The repository freezes the iid `Exp(1)`, undirected nearest-neighbor `Z^2` specialization.

Let `mu` be the time-constant norm and

`Delta_12 := 2 mu(e1)-mu(1,1) >= 0`.

The retained rigorous axis certificate is

`mu(e1) >= b := 3002823/10000000 = 0.3002823`,

so it is enough for this first checkpoint to prove

`mu(1,1) < 2b = 3002823/5000000 = 0.6005646`.

Tracked original-problem quantity:

- **before:** largest proved `c_*` with `Delta_12 >= c_*` is `0`;
- **after:** `c_*=0`.

Thus this run does **not** prove the axis/diagonal strict triangle inequality and does not close full strict convexity.

A bounded fresh primary-source search on 20 September 2026 again found no source-matching unconditional resolution. Jacquet's pattern theorems remain relevant to true-geodesic geometry but do not imply this same-quadrant triangle defect; directed/integrable models remain different models. This is a bounded literature check, not an exhaustive novelty certificate.

## 2. Essential dependencies and failures preserved

I used only the dependencies needed for this attack:

1. `operations/PROGRESS20_2026-09-20.md` and LIVE20, pairing P20 with P04 on T10;
2. `operations/claims/PROB10-10.md`, including the R07/R08 failure history;
3. P20's preceding report `proofnet24/P20-progress-fpp/runs/2026-09-20/2026-09-20T13-10-00Z__upper-corner-bellman-box-certificate.md`;
4. the current canonical owner's asynchronous-carry / exact-Richardson report at commit `4a4a81c6078e76f6096efe0f681e7298f7b12457`;
5. P04's physical-edge slab machinery, with the latest T10 report found under its designated progress root `proofnet24/P04-progress-curvature/runs/2026-09-20/2026-09-20T09-47-23Z__width7-undirected-cone1362.md`;
6. the displaced P20 cyclic-interval proof and its existing P26 audit state.

The binding failures are unchanged and are not overwritten:

- shared bypasses invalidate multiplication of independent local-surgery savings;
- pointwise finite-scale strict saving is false on positive-probability cylinder events;
- old fixed-corner exact blocks missed the needed diagonal threshold;
- weighted-SAW/Chernoff first-moment bounds have a diagonal barrier already exposed by monotone E/N paths;
- reflected-cone strict inequalities are compatible with the `l1` diamond and are not source-facing progress on `Delta_12`;
- the Jacquet/Busemann true-geodesic route forces backtracking but under flatness can collapse to near-co-calibration, leaving a global rigidity obstruction;
- sampled carry values below `0.6005646` remain screens only.

The preceding P20 run reduced the continuous-state Bellman verification to upper-corner expectations of one scalar functional, but still lacked a rigorous evaluator at asynchronous upper-corner profiles and had a large unresolved compact profile core. This run addresses those two bottlenecks.

## 3. Min-plus block notation

Fix one fresh finite diagonal band with input and output boundaries indexed by

`D={0,1,...,M-1}`, with `M=W+1` in the canonical even-width parametrization.

For realized block environment `omega`, let `d_omega(i,j)` be its internal passage metric and, for a finite normalized arrival profile `y` with `min y=0`, put

`F_omega(y)_j = min_i {y_i+d_omega(i,j)}`,

`g_omega(y)=min_j F_omega(y)_j`,

`Phi_omega(y)=F_omega(y)-g_omega(y) 1`.

Write

`t_first=g_omega(y)`, `t_last=max_j F_omega(y)_j`.

The preceding report proved the pointwise anchor estimate `E g<=2L`, output-span reset `E span(Phi)<=2W`, projective compactification, and a central-coordinate corrector. The new step is to replace the single central coordinate by an arbitrary positive linear profile functional.

## 4. P20-FPP-WEIGHTED-PROFILE-CORRECTOR-42 — CANDIDATE_PROVED

Let `alpha=(alpha_0,...,alpha_{M-1})` with `alpha_j>=0` and total mass

`A := sum_j alpha_j`.

Let `kappa>=0` and assume

`kappa+A <= 1`.

Define the projective corrector

`h_{kappa,alpha}(y) := kappa span(y)+sum_j alpha_j y_j`.

Then the exact one-block scalar is

`g+h(Phi)`
` = (1-kappa-A)t_first + kappa t_last + sum_j alpha_j F_j`          (4.1)

and is coordinatewise nondecreasing in the incoming profile `y`.

Let the fixed output-boundary chain have link costs `Z_0,...,Z_{M-2}`. In the lattice band each link uses two distinct physical Exp(1) edges, hence the `Z_l` are iid `Gamma(2,1)` with mean `2` and variance `2`. For a chain vertex `k`, set

`H_k := sum_j alpha_j d_chain(k,j)`.

If `k` is an output minimizer of `F`, then samplewise

`sum_j alpha_j Phi_j <= H_k <= max(H_0,H_{M-1}).`                    (4.2)

Write cumulative masses `A_l=sum_{j<=l}alpha_j` and

`c_l := A-2A_l`, `0<=l<=M-2`.

Then

`H_0+H_{M-1}=A sum_l Z_l`,

`H_0-H_{M-1}=sum_l c_l Z_l`.                                       (4.3)

Consequently

`E max(H_0,H_{M-1})`
` <= C(alpha)`
` := A W + (1/2) sqrt( 4(sum_l c_l)^2 + 2 sum_l c_l^2 ).`          (4.4)

Therefore the Bellman residual

`B_{kappa,alpha}(y)`
` := E[g+h(Phi)]-h(y)`

obeys the global coercive inequality

`B_{kappa,alpha}(y)`
` <= 2L + 2 kappa W + C(alpha)`
`    - kappa span(y) - alpha dot y.`                                (4.5)

### Proof

Identity (4.1) follows from `span(Phi)=t_last-t_first` and `Phi_j=F_j-t_first`. The coefficients are nonnegative under `kappa+A<=1`; every `F_j`, their minimum, and their maximum are coordinatewise nondecreasing, proving monotonicity.

For (4.2), choose an output minimizer `k`. Along the fixed output chain,

`Phi_j=F_j-F_k <= d_chain(k,j)`

by the triangle inequality for block passage times. Multiplying by `alpha_j` and summing gives the first inequality.

It remains to show that the maximum of `H_k` is at an endpoint. Crossing link `k` gives

`H_{k+1}-H_k = Z_k(2A_k-A)`.                                      (4.6)

Because `A_k` is nondecreasing and `Z_k>=0`, the signs in (4.6) can change at most once, from nonpositive to nonnegative. Thus `H_k` first decreases and then increases, so its maximum is one of the endpoints. Expanding chain distances gives (4.3).

Now

`max(H_0,H_R)=(H_0+H_R+|H_0-H_R|)/2`.

The first term has expectation `AW`, because there are `W=M-1` links of mean two. For `D=sum c_l Z_l`,

`E D=2 sum c_l`, `Var(D)=2 sum c_l^2`.

Cauchy--Schwarz gives

`E|D| <= sqrt(E D^2)`
` = sqrt(4(sum c_l)^2+2 sum c_l^2)`,

which proves (4.4). Finally combine `E g<=2L`, `E span(Phi)<=2W`, and (4.4), then subtract `h(y)`, to obtain (4.5). QED.

This theorem is deterministic/analytic except for exact first and second moments of the fixed boundary-chain Gamma variables. It is not sampled curvature.

## 5. Uniform-profile corollary and quantitative compact-core shrinkage

Take uniform weights

`alpha_j = eta/M`, `0<=eta<=1`,

so `A=eta`. Symmetry gives `sum c_l=0`, and an exact finite sum yields

`sum_{l=0}^{W-1} (1-2(l+1)/(W+1))^2`
` = W(W-1)/(3(W+1)).`

Hence per unit `eta`,

`C_unif(W)`
` = W + sqrt( W(W-1)/(6(W+1)) ).`                                 (5.1)

For `W=48`,

`C_unif(48)=48+2 sqrt(94)/7`
`              =50.7701027756664737...`.                          (5.2)

This is smaller than the preceding single-central-coordinate reset constant

`M_48=51.89865430250223...`,

but the larger structural gain is that the coercive penalty is now the **whole average profile**, not one designated coordinate.

For the pure uniform corrector `kappa=0, eta=1`, `L=4`, and source-facing block threshold

`lambda_* = 4*0.6005646 = 3002823/1250000 = 2.4022584`,

equation (4.5) certifies every normalized profile satisfying

`bar y := (1/49) sum_j y_j`
` >= 8 + C_unif(48)-lambda_*`
` = 66997177/1250000 + 2 sqrt(94)/7`
` = 56.3678443756664737...`.                                      (5.3)

In the difficult branch where one anchored coordinate is zero and each of the other 48 coordinates is at least `r`, (5.3) holds as soon as

`r >= (49/48)(8+C_unif(48)-lambda_*)`
` = 3282861673/60000000 + 7 sqrt(94)/24`
` = 57.5421744668261919...`.                                      (5.4)

The preceding pure-span compactification at `kappa=1` only removed this branch once

`span(y) >= 8+96-lambda_*`
` = 126997177/1250000`
` = 101.5977416`.                                                  (5.5)

Thus for the one-low/many-high sector the analytic unresolved threshold drops from `101.5977416` to `57.5421744668...`, roughly a 43 percent reduction. This is a **mechanism/certificate-domain gain only**; it does not change `c_*`.

More generally, if at most `q` of the 49 coordinates lie below `r`, the uniform corrector certifies whenever

`((49-q)/49) r >= 56.367844375666...`.

This is useful for adaptive branch-and-bound because broad boxes with only a few low coordinates can now be discarded without evaluating any stochastic block expectation.

## 6. Continuous-box upper-corner compiler with weighted correctors

Let a normalized profile box have lower and upper corners `ell<=u` and a fixed zero anchor. By monotonicity of (4.1), every `y` in the box satisfies

`B_{kappa,alpha}(y)`
` <= E Q_{kappa,alpha}(u)`
`    - kappa max_i ell_i - alpha dot ell,`                           (6.1)

where

`Q_{kappa,alpha}(u)`
` =(1-kappa-A)t_first(u)+kappa t_last(u)+sum_j alpha_j F_j(u).`     (6.2)

Thus one may first use the analytic drift bound (4.5). Only boxes not eliminated by that bound require a rigorous upper enclosure of the single scalar expectation in (6.2). There is no tensor-net interpolation loss and no requirement to know the full transition kernel.

The remaining question from the preceding run was how to obtain that enclosure for genuinely asynchronous upper-corner profiles. The next theorem supplies an exact finite-state recursion specialized to Exp(1).

## 7. P20-FPP-DELAYED-RICHARDSON-REWARD-43 — CANDIDATE_PROVED

Let `G=(V,E)` be a finite graph with iid Exp(1) physical-edge passage times. Let input/source vertices `s_i` have deterministic activation times `u_i>=0`. Their induced arrival times are

`F(v)=min_i {u_i+T_G(s_i,v)}`.                                    (7.1)

Let `O` be the output set. Fix `kappa,alpha` as above and define

`Q=(1-kappa-A) min_{j in O}F(j)`
`   +kappa max_{j in O}F(j)`
`   +sum_{j in O} alpha_j F(j).`                                  (7.2)

Define the infection set `S_t={v:F(v)<=t}` and the nonnegative state reward

`w(S)`
` =(1-kappa-A) 1{S cap O is empty}`
`  +kappa 1{O is not a subset of S}`
`  +sum_{j in O} alpha_j 1{j notin S}.`                            (7.3)

Then samplewise

`Q = integral_0^infinity w(S_t) dt.`                              (7.4)

Moreover this expectation can be evaluated by a finite delayed Richardson recursion.

For an infected set `S`, let

`b(S)=#{edges with exactly one endpoint in S}`,

`m_S(v)=#{x in S:{x,v} in E}` for `v notin S`.                    (7.5)

Consider one phase with time `delta>=0` until the next deterministic source-activation event, whose activation set is `A_next`. Let `V^+(S)` denote the expected future reward immediately after that deterministic event and all later phases. Let `U_S(delta)` be the expected reward from now through that future continuation, starting in infected set `S` with `delta` time remaining to the event. If `b=b(S)>0`, then

`U_S(delta)`
` = w(S)(1-e^{-b delta})/b`
`   + sum_{v notin S} m_S(v) int_0^delta e^{-b s}`
`       U_{S union {v}}(delta-s) ds`
`   + e^{-b delta} V^+(S union A_next).`                           (7.6)

If `b(S)=0`,

`U_S(delta)=w(S)delta+V^+(S union A_next).`                        (7.7)

After the final deterministic source activation, the recursion becomes time-homogeneous and triangular:

`U(S)=0` whenever `w(S)=0`, and otherwise, for `b(S)>0`,

`U(S)= w(S)/b(S)`
`      +sum_{v notin S} [m_S(v)/b(S)] U(S union {v}).`             (7.8)

For rational activation times, repeated use of (7.6)--(7.8) produces a finite exponential-polynomial expression with rational coefficients, integer exponential rates, and polynomial factors in the activation gaps. Hence it admits fully rigorous interval evaluation using one-sided enclosures of finitely many exponentials. No Monte Carlo is required.

### Proof

For each nonnegative random time `X`, `X=int_0^infinity 1{X>t}dt`. Applying this separately to the three nonnegative terms in (7.2) gives (7.4): `min F_j>t` iff no output has been infected; `max F_j>t` iff not all outputs are infected; and `F_j>t` iff output `j` is uninfected.

Now condition on the present infected set during a phase with no deterministic source activation. Every live boundary edge has an independent rate-one exponential residual clock. This is exactly where the Exp(1) law is used: conditioning on survival to the present time leaves an independent Exp(1) residual by memorylessness. Therefore the next infection event has total rate `b(S)`, and vertex `v` is infected at hazard `m_S(v)`.

The expected reward accumulated before the first of a random infection event and the deterministic activation time is

`w(S) int_0^delta e^{-b s} ds`
` =w(S)(1-e^{-b delta})/b`.

The density that `v` is the next infected vertex at elapsed time `s` is `m_S(v)e^{-b s}`; conditioning on this event gives the integral term in (7.6). If no infection event occurs by `delta`, which has probability `e^{-b delta}`, the deterministic activation occurs and the infected set becomes `S union A_next`, giving the last term. This proves (7.6). Equation (7.7) is immediate when there is no live boundary edge.

After the last deterministic activation, the holding time in state `S` has mean `1/b(S)` and the next vertex is `v` with probability `m_S(v)/b(S)`, yielding (7.8). Every stochastic transition strictly enlarges `S`, so the final recursion is triangular in `|S|`; the phase recursion is then solved backwards over the finite list of deterministic activation times. Integrals of exponential-polynomials remain exponential-polynomials, including the usual polynomial factors when rates coincide. QED.

### Why this is new relative to the current canonical exact recursion

The canonical owner already proved the ordinary Richardson recursion for a single source activated at time zero and terminal hitting. That theorem is not re-claimed here. The new point is the **delayed multi-source occupation-reward recursion** (7.6), which evaluates exactly the asynchronous upper-corner functional needed by P20's continuous-profile Bellman boxes, including first-output, last-output, and weighted output labels simultaneously.

## 8. P20-FPP-SPARSE-UPPER-CERTIFICATE-44 — CANDIDATE_PROVED

The delayed recursion has two monotone one-sided simplifications suitable for P04/certificate work.

1. **Edge deletion.** If `H` is a connected edge-deleted subgraph of `G` containing the relevant sources and outputs, then every arrival time in `H` is at least its counterpart in `G`. Since every coefficient in (7.2) is nonnegative,

`E Q_G(u) <= E Q_H(u).`                                            (8.1)

Thus a tractable sparse `H` supplies a rigorous upper certificate for the full block.

2. **Source delay/deletion.** Raising an input activation time, or replacing a source by activation time `+infinity`, can only increase every output arrival and hence `Q`. Therefore late/high sources can be removed when seeking an upper bound:

`u<=u' coordinatewise  ==> E Q(u)<=E Q(u').`                       (8.2)

These operations are deliberately one-sided. They can enlarge the computed cost but cannot create a false source-facing upper bound.

Combining (6.1), (8.1), and (8.2), an unresolved continuous box can be certified by evaluating a sparse delayed-Richardson problem at a source-pruned upper corner. This is the concrete P04 handoff.

## 9. Finite-to-infinite transfer and exact source compiler

The canonical asynchronous carry theorem already pays the dependence and interface error correctly: physical edge sets are disjoint band-to-band; the normalized boundary profile is carried rather than synchronized; a Bellman supersolution telescopes; and the final fresh staircase correction is `O(W/N)`.

Therefore if a finite cover of the post-first-band profile core is certified at some common `lambda` using weighted correctors and (6.1), while the analytic outer drift (4.5) handles the complement, then

`mu(1,1) <= lambda/L`.                                             (9.1)

With the retained axis lower certificate,

`Delta_12 >= 0.6005646-lambda/L`.                                 (9.2)

Hence any rigorous certificate with

`lambda/L < 0.6005646`                                            (9.3)

would make the first source-facing defect strictly positive.

For `L=4`, this means `lambda<2.4022584`. The existing sampled carry value below this threshold remains nonrigorous and is not used in (9.1)--(9.3).

The demonstrated gain of this run is that the outer/core decomposition is now significantly smaller in broad high-average sectors and the remaining scalar upper-corner expectations have an exact Exp-specific delayed finite-state recursion. No claim is made that the width-48 finite cover has already been completed.

## 10. Executed exact sanity checks

I executed an exact-rational / symbolic sanity checker and archived both code and output:

- code: `proofnet24/P20-progress-fpp/artifacts/2026-09-20/2026-09-20T14-10-00Z__weighted-corrector-delayed-richardson-sanity.py`, creation commit `4aa77a6b0361f84ce5edab4648b79cd07ed5fe32`;
- output: `proofnet24/P20-progress-fpp/artifacts/2026-09-20/2026-09-20T14-10-00Z__weighted-corrector-delayed-richardson-sanity.out`, creation commit `0bc6d439b792d0f4fb5bc53cfa07b18b94143b23`.

It verifies:

- the exact uniform-chain variance and `C_unif(48)=48+2sqrt(94)/7`;
- the exact branch thresholds (5.3)--(5.5);
- the endpoint-max property for weighted chain distance on an exact rational example;
- the delayed two-source/one-output star identity `E min(E_0,a+E_1)=1-e^{-a}/2` from the phase recursion;
- an exact two-output weighted-reward identity.

The archived output ends

`P20-T10-WEIGHTED-CORRECTOR-DELAYED-RICHARDSON-SANITY: ALL_EXACT_CHECKS_PASS`.

This is supplementary sanity evidence only. It is not sampled curvature and not an asymptotic proof.

## 11. Honest residual obstruction and failure report

The source metric did not move. The unresolved task is now a finite but still potentially large certification problem.

The naive delayed-Richardson state space is exponential in the number of block vertices. At widths near the encouraging screen regime, brute-force enumeration of all infected subsets is not realistic. The new analytic uniform corrector removes large high-average portions of profile space, and edge/source deletion can simplify each remaining upper corner, but I have **not** yet constructed a finite sparse family whose exact interval bounds all lie below the `2.4022584` block threshold.

So the present obstruction is precise:

> Build a pathwidth-/frontier-compressed delayed-Richardson interval evaluator, and combine it with adaptive weighted-profile correctors, so that every unresolved continuous profile box is either eliminated analytically or gets a one-sided scalar expectation bound strong enough for (9.3).

If the best tractable sparse upper bounds remain above threshold, that is an honest quantitative failure of this route, not evidence that `Delta_12=0`.

## 12. Next attack

The next P20/P04-compatible attack should not return to sampled curvature or local-surgery multiplication. It should implement the proof obligation created here:

1. represent the delayed Richardson recursion by a frontier/pathwidth state rather than arbitrary infected subsets;
2. use edge deletion to choose a sparse band graph whose frontier remains small but whose one-sided cost is still competitive;
3. for each profile box, optimize `alpha` (under `alpha>=0`, `kappa+sum alpha<=1`) to maximize the analytic lower-corner penalty before any stochastic evaluation;
4. evaluate only the residual upper corners, with rigorous exponential intervals;
5. first certify one nontrivial whole box below `lambda_*`, then enlarge to a finite cover and invoke the already-proved asynchronous finite-to-infinite compiler.

This is a materially different exactification step from the prior box geometry run, not another audit or another sampled screen.

## 13. Short cyclic-interval handoff

The displaced P20 cyclic-interval work remains preserved and untouched. The source-literal proof candidate `P20-FOKAM-BITJOKA-CI241-SEMICIRCLE-MAJORITY-01` remains on record with its finite sanity artifact. P26's full-proof/source-quantifier audit remains PASS. The last recovered independent-audit state remains one distinct audit out of the desired two. No certification closure is claimed, and no research time in this run was spent waiting for the second audit.

## 14. ledger_delta

`original_problem`:

- `Delta_12` lower-bound metric: `c_*=0 -> 0`;
- full strict convexity: OPEN;
- no source-level certification or novelty claim.

`mechanism_gain`:

- `P20-FPP-WEIGHTED-PROFILE-CORRECTOR-42 = CANDIDATE_PROVED`;
- uniform-profile analytic reset `C_unif(48)=48+2sqrt(94)/7`;
- one-low/many-high profile-sector outer threshold reduced from `101.5977416` (pure span) to `57.5421744668...` (uniform corrector), without stochastic sampling;
- `P20-FPP-DELAYED-RICHARDSON-REWARD-43 = CANDIDATE_PROVED`, giving an exact asynchronous Exp(1) recursion for the required upper-corner scalar;
- `P20-FPP-SPARSE-UPPER-CERTIFICATE-44 = CANDIDATE_PROVED`, allowing edge/source deletion as safe one-sided simplifications;
- exact sanity code/output executed and archived at commits `4aa77a6b0361f84ce5edab4648b79cd07ed5fe32` and `0bc6d439b792d0f4fb5bc53cfa07b18b94143b23`.

`residual_obstruction`:

- rigorous frontier-compressed interval evaluation and finite profile-box cover at `lambda/L<0.6005646` are not yet completed.

`next_attack`:

- pathwidth/frontier delayed-Richardson interval recursion plus adaptive weighted-corrector branch-and-bound, beginning with a single whole-box source-valid certificate.

END OF P20 FPP RUN REPORT
