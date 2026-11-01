Model: GPT-5.6 Sol. Reasoning: UNVERIFIED; this run did **not** run on GPT-6 at verified maximum reasoning. **No movement: `T_corr=4 -> 4`. Methods tried: B10/B13/B21. New theorem-sized PARTIAL result: every Campbell--O'Rourke C2 angular law with positive off-axis mass has a two-sided radial Pareto envelope `c_theta r^(-alpha) <= mu_{alpha,theta}(|z|>r) <= C_alpha r^(-alpha)` for all sufficiently large `r`; consequently its truncated critical `alpha`-moment is `Theta(log R)` and its near-critical moments blow up exactly at order `(alpha-p)^(-1)`. Question 1.9 remains OPEN because regular-variation constants, directional tails, and the full anisotropic profile remain undetermined.**

# HARD7-02 — Campbell--O'Rourke Question 1.9: a two-sided Pareto envelope from weak-Schatten truncation

Status: **PARTIAL / source Question 1.9 remains OPEN under a fresh bounded current-literature search / the new result is proved on-page from the earlier HARD7-02 row-tail and isolated-edge inputs, with an exact symbolic self-check for the finite constant algebra but no independent audit.**

Frozen source metric:

`T_corr = number of explicit non-i.i.d., non-Hermitian C2 dependence families for which the full asymptotic radial tail exponent/class of mu_{alpha,theta} is rigorously determined`.

Before: `T_corr=4`.

After: **`T_corr=4` — no movement.**

I do not increment the metric merely because the theorem below applies to infinitely many additional parameter values already covered at the exponent level by the previous support theorem. The mathematical advance is qualitative: it removes the logarithmic loss and pins the entire positive-off-axis C2 class to the exact radial power **order** `r^(-alpha)` up to constants.

## 1. Continuity, repository state, ownership, and capability honesty

I resumed the active exclusive claim

`operations/claims/CAMPBELL-OROURKE-2022-Q1.9.md`

from the newest completed checkpoint

`runs/hard7_2026-09-18/HARD7-02/2026-09-19T22-12-00Z__q19-tauberian-antithinning-pointwise-tail.md`.

At run start I re-read or refreshed the controlling HARD7/new-methods files, root `POSTED.md`, `RESULTS.md`, and `QUEUE.md`, campaign `probability_campaign_2026_09/INDEX.md` and `RANKING.md`, the active Q1.9 claim, the newest own reports, the heavy-tail/non-Hermitian C0026--C0032 intake neighborhood, and the neighboring R7-06/C0032 terminal-handoff material. Q1.9 remains exclusively assigned to HARD7-02. C0032 is the distinct iid heavy-tailed circular-law explicit-density problem and is not an alias. No claim file was overwritten, no shared root ledger was edited, and no neighboring track file was changed.

The runtime capability situation is unchanged. The exposed scheduler/task surface has title/prompt, schedule/timing mode, enabled state, and ordinary task controls, but **no binding model selector, no reasoning-effort selector, no authenticated reasoning telemetry, and no guaranteed-duration field**. Thus `GPT-6 / maximum` remains prompt-requested only. A genuine change would require a product/backend interface exposing binding model and effort controls. Historical `You cannot modify this task` responses are permission-context failures; the compliant workaround is the owning/authorized account or workspace, ownership transfer, or platform support, never a duplicate schedule or permission bypass. No scheduler mutation was attempted in this run.

No Gmail, Drive, public posting, paid compute, workflow execution, force push, permission bypass, or schedule creation/modification was performed.

## 2. Exact external source and fresh status check

Primary source:

Andrew Campbell and Sean O'Rourke, *Spectrum of Heavy-Tailed Elliptic Random Matrices*, Electronic Journal of Probability **27** (2022), paper 127; arXiv:2010.01261v3; DOI `10.1214/22-EJP849`.

The current arXiv text, Section 1.3, asks exactly:

> **Question 1.9.** How does the tail behavior of `mu_{alpha,theta_d}` vary with respect to `theta_d`?

The source states immediately beforehand that the iid non-Hermitian heavy-tailed limit has an exponential tail, while the Hermitian limit has the same tail behavior as the heavy-tailed entries. It also says the numerical pictures suggest dependence on `theta_d` and possibly direction-dependent tails.

Fresh bounded searches on 20 September 2026 used the exact source title/authors, exact Question 1.9 wording, `mu_{alpha,theta_d}`, `theta_d`, tail behavior, heavy-tailed elliptic, PWIT, regular variation, and 2023--2026 follow-up terms. They recovered the 2022 source; Campbell--O'Rourke, *Spectrum of Levy--Khintchine Random Laplacian Matrices* (2023/2024); Carpenter--O'Rourke, *The Limiting Spectral Distribution for Sparse Elliptic Random Matrices* (arXiv:2508.04891, 2025); and unrelated finite-variance elliptic-law work. I did **not** locate a paper claiming a general solution of Question 1.9 or the two-sided positive-off-axis Pareto envelope below. This is bounded negative evidence, not a worldwide novelty or priority certificate.

Primary source checked:

`https://arxiv.org/abs/2010.01261`

The source text at Section 1.3 still contains Question 1.9 and the endpoint comparison above.

## 3. Idea-before-code checkpoint and self-check

The route was written before checker construction at

`runs/hard7_2026-09-18/HARD7-02/2026-09-19T23-12-00Z__idea-before-code-q19-pareto-envelope.md`

commit

`14a9550fd2c6db1c0af1280c9d0044f0ff31d3d3`.

Only after that checkpoint I wrote the exact symbolic algebra self-check

`artifacts/hard7_2026-09-18/HARD7-02/2026-09-19T23-12-00Z__q19-pareto-envelope-check.py`

commit

`6afc86a79683fa7147fab73e5b0c0647f0961a1c`,

and archived its executed output at

`artifacts/hard7_2026-09-18/HARD7-02/2026-09-19T23-12-00Z__q19-pareto-envelope-check.out`

commit

`12aad59dd94d460265f9a804b1e9ebf7b0f6697f`,

ending

`ALL_EXACT_CHECKS_PASS = True`.

This checker is a **self-check only**. It verifies the finite symbolic identities for the constants and exponents below. It is not an independent audit of the random-matrix argument.

## 4. The overlooked quantitative input from the earlier proof

Normalize the finite nonzero C2 angular measure to a probability measure using the mass-homogeneity/output-dilation relation already proved in the HARD7-02 chain. Deterministic output dilation changes constants but not any of the tail classes proved below.

Fix `0<alpha<2` and put

`beta := alpha/2 in (0,1)`.                                        (4.1)

Use the same exact Pareto representative as in the previous positive-off-axis theorem. For every row of the normalized finite matrix `A_n`, let

`X_i := ||Row_i(A_n)||_2`,
`S_i := X_i^2`.                                                     (4.2)

The earlier on-page row calculation proved the uniform tail bound

`P(S_i>u) <= C_beta u^(-beta)`, `u>=1`,                            (4.3)

where one may take

`C_beta := 2 + 2^beta + 2^beta/(1-beta)`.                          (4.4)

The bound is uniform in `n`, the row index, and the normalized C2 angular law. It did not require iid coordinates inside a mirrored pair.

That same report integrated (4.3) against a subcritical moment and obtained, for every `0<p<alpha`,

`m_p(theta):=int_C |z|^p mu_{alpha,theta}(dz)`
`<= 1 + p C_beta/(alpha-p)`.                                       (4.5)

The previous run named control of `m_p` as `p up alpha` as the next obstruction. Equation (4.5) is already the required quantitative upper control: it has the Pareto-scale blow-up `(alpha-p)^(-1)`. The present run exploits the stronger pre-integration statement (4.3) instead of applying Markov again.

## 5. B21 — weak-L^alpha rows imply a weak-Schatten alpha counting bound

The key new deterministic mechanism is a row-rank truncation.

For a finite complex matrix `A`, let

`N_A(t) := #{j : s_j(A)>t}`                                       (5.1)

be its singular-value counting function. Write its row norms as `x_i`.

### Lemma 5.1 — rank plus truncated Frobenius

For every `t>0`,

`N_A(t) <= #{i:x_i>t} + t^(-2) sum_{i:x_i<=t} x_i^2`.             (5.2)

#### Proof

Let `I={i:x_i>t}`. Let `B` be the matrix retaining exactly the rows in `I` and zeroing all other rows, and set `C=A-B`. Then

`rank(B)<=|I|`.                                                     (5.3)

The standard rank-perturbation singular-value inequality gives

`s_{|I|+j}(A) <= s_j(C)`                                           (5.4)

for every admissible `j`. Therefore

`N_A(t)<=|I|+N_C(t)`.                                              (5.5)

Finally,

`t^2 N_C(t) <= sum_j s_j(C)^2 = ||C||_F^2`
`= sum_{i:x_i<=t} x_i^2`.                                         (5.6)

Combining (5.5) and (5.6) gives (5.2). `QED`

This is the weak-Schatten transfer that was missing from the earlier moment-only route.

### Proposition 5.2 — expected singular counting envelope

For the normalized heavy-tailed elliptic matrices in the exact representative above and every `t>=1`,

`sup_n E[N_{A_n}(t)/n] <= D_alpha t^(-alpha)`,                     (5.7)

where

`D_alpha := C_beta + 1 + C_beta/(1-beta)`.                         (5.8)

#### Proof

Apply Lemma 5.1 row by row and take expectations. From (4.3),

`P(X_i>t)=P(S_i>t^2)<=C_beta t^(-alpha)`.                          (5.9)

For the truncated square norm,

`E[S_i 1_{S_i<=t^2}]`
`<= E[min(S_i,t^2)]`
`= int_0^{t^2} P(S_i>u) du`                                       (5.10)

and hence, using (4.3),

`E[S_i 1_{S_i<=t^2}]`
`<= 1 + C_beta int_1^{t^2}u^(-beta)du`
`= 1 + [C_beta/(1-beta)](t^(2-2beta)-1)`
`<= [1+C_beta/(1-beta)] t^(2-alpha)`.                              (5.11)

Divide (5.11) by `t^2`, average over rows, and combine with (5.9). This gives exactly (5.7)--(5.8). `QED`

**B21 outcome: success.** The old `p<alpha` Schatten-moment estimate hid a stronger endpoint object. The rows already lie uniformly in weak `L^alpha`; the rank/Frobenius split transfers this directly to an expected weak-Schatten `alpha` estimate without optimizing over `p` and without a logarithmic loss.

## 6. From singular-value counts to an `r^(-alpha)` logarithmic-potential upper bound

For the eigenvalues `lambda_j(A_n)` define

`V_n(u):=(1/n)sum_j log^+(|lambda_j(A_n)|/u)`.                     (6.1)

Weyl's multiplicative majorization of eigenvalue moduli by singular values, applied to the convex increasing function `x -> max(x-log u,0)` on logarithmic coordinates, gives

`V_n(u)`
`<= (1/n)sum_j log^+(s_j(A_n)/u)`
`= int_u^infinity [N_{A_n}(t)/n] dt/t`.                            (6.2)

For `u>=1`, Tonelli and Proposition 5.2 yield

`E V_n(u)`
`<= D_alpha int_u^infinity t^(-alpha)dt/t`
`= (D_alpha/alpha)u^(-alpha)`.                                    (6.3)

Put

`B_alpha := D_alpha/alpha`.                                        (6.4)

The earlier HARD7-02 proof already established the required uniform integrability to pass `V_n(u)` to the deterministic limiting spectral law for each fixed `u`; explicitly,

`E V_n(u) -> V_theta(u)`                                           (6.5)

with

`V_theta(u):=int_C log^+(|z|/u)mu_{alpha,theta}(dz)`
`= int_u^infinity F_theta(t)dt/t`,                                 (6.6)

where

`F_theta(r):=mu_{alpha,theta}({|z|>r})`.                           (6.7)

Thus (6.3) gives the new uniform potential upper bound

`V_theta(u) <= B_alpha u^(-alpha)`, `u>=1`.                        (6.8)

No positive-off-axis assumption was used in this upper bound.

A first pointwise consequence is immediate. If `r>=e`, then every `|z|>r` contributes more than one to `log^+(|z|/(r/e))`. Hence

`F_theta(r) <= V_theta(r/e)`
`<= C_alpha r^(-alpha)`,                                          (6.9)

where

`C_alpha := e^alpha B_alpha`.                                      (6.10)

This removes the previous upper-envelope logarithm completely.

## 7. B10 — derandomize the off-axis sector into one angular functional

Assume now

`rho_off(theta):=theta({(w_1,w_2):w_1w_2!=0})>0`.                 (7.1)

For `delta>0`, define

`rho_delta := theta({|w_1w_2|>=delta})`.                           (7.2)

The previous isolated-reciprocal-edge proof established, for every `delta` with `rho_delta>0`, the explicit integrated-tail bound

`V_theta(r) >= [rho_delta c_delta^alpha/2]r^(-alpha)`
`              * exp[-2rho_delta(c_delta/r)^alpha]`               (7.3)

for all sufficiently large `r`, where

`c_delta := sqrt(delta) exp(-2alpha-1/2)`.                         (7.4)

Therefore

`liminf_{r->infinity} r^alpha V_theta(r)`
`>= (rho_delta/2) delta^(alpha/2)`
`   * exp(-2alpha^2-alpha/2)`.                                    (7.5)

Instead of fixing an arbitrary witnessing sector, define the deterministic angular order parameter

`J_alpha(theta)`
`:= sup_{delta>0} delta^(alpha/2) theta({|w_1w_2|>=delta})`.        (7.6)

Because

`{w_1w_2!=0}=union_{m>=1}{|w_1w_2|>=1/m}`,                        (7.7)

positive off-axis mass implies

`J_alpha(theta)>0`.                                                 (7.8)

Taking the supremum in (7.5) gives

`liminf_{r->infinity} r^alpha V_theta(r) >= P_theta`,              (7.9)

where

`P_theta := (1/2)exp(-2alpha^2-alpha/2) J_alpha(theta) >0`.        (7.10)

**B10 outcome: success.** The arbitrary sector choice has been compressed into one deterministic functional of the source parameter `theta`. This is not claimed to be the sharp tail constant; it is an explicit source-dependent positive certificate.

## 8. B13 — fixed-dilation monotonicity removes the logarithmic annulus loss

The previous run localized on `[r,r^(1+delta)]`, whose logarithmic width is `delta log r`; that produced a `1/log r` loss. Once (6.8) is available, the far tail can instead be discarded at a **fixed multiplicative dilation**.

From (7.9), there is `R_0<infinity` such that

`V_theta(r) >= A_theta r^(-alpha)`, `r>=R_0`,                     (8.1)

with, for definiteness,

`A_theta := P_theta/2`.                                            (8.2)

Choose

`K_theta := max{2,(2B_alpha/A_theta)^(1/alpha)}`.                  (8.3)

Then `K_theta>1`, and by (6.8), for all sufficiently large `r`,

`V_theta(K_theta r)`
`<= B_alpha K_theta^(-alpha)r^(-alpha)`
`<= (A_theta/2)r^(-alpha)`.                                       (8.4)

On the other hand, monotonicity of `F_theta` gives the exact decomposition

`V_theta(r)`
`= int_r^{K_theta r}F_theta(t)dt/t + V_theta(K_theta r)`
`<= F_theta(r)log K_theta + V_theta(K_theta r)`.                   (8.5)

Combine (8.1), (8.4), and (8.5):

`F_theta(r) >= c_theta r^(-alpha)`                                (8.6)

for all sufficiently large `r`, where

`c_theta := A_theta/(2log K_theta)`
`          = P_theta/(4log K_theta) >0`.                           (8.7)

Together with (6.9):

### Theorem 8.1 — two-sided Pareto radial envelope

For every `0<alpha<2` and every normalized C2 angular law with positive off-axis mass, there exist explicit finite constants

`0<c_theta<=C_alpha<infinity`                                      (8.8)

such that for all sufficiently large `r`,

`c_theta r^(-alpha)`
`<= mu_{alpha,theta}({|z|>r})`
`<= C_alpha r^(-alpha)`.                                          (8.9)

Here `C_alpha=e^alpha D_alpha/alpha` is uniform over normalized angular laws, while one valid lower constant is (8.7) with `P_theta` from (7.10).

This theorem gives the full radial tail **order** but does not claim that `r^alpha F_theta(r)` converges.

**B13 outcome: success.** The relevant monotone quantity is the integrated radial tail `V`. Matching power upper and lower envelopes let a fixed dilation recover `F` itself; no scale-dependent annulus is needed.

## 9. Exact support-level radial tail-class dichotomy

The previous axis-support classification proved that every C2 law supported purely on the two coordinate axes is, after deterministic dilation and irrelevant axis phases, the iid heavy-tailed circular limit. The source records that iid limit as exponentially tailed and with finite moments of every order.

Theorem 8.1 therefore upgrades the earlier support dichotomy to the following radial tail-class statement:

- `rho_off(theta)=0`: exact dilation of the iid limit; exponential radial tail class;
- `rho_off(theta)>0`: two-sided polynomial radial tail order `Theta(r^(-alpha))`.

Thus there is no C2 angular law with positive off-axis mass whose radial tail is, for example,

`r^(-alpha)/log r`, `r^(-alpha)/sqrt(log log r)`, or
`r^(-alpha)log r`                                                  (9.1)

up to eventual equivalence: the first two are too thin and the last is too thick relative to (8.9).

This is a much sharper answer to the source's endpoint/interpolation question than the preceding logarithmic-exponent theorem. In particular, in the Figure-2 family from the source, the exact endpoint `b=0` is exponentially tailed whereas every fixed `b>0` has radial tail bounded above and below by positive multiples of `r^(-alpha)`.

## 10. Near-critical moments now have the exact divergence order

Let

`m_p(theta):=int_C |z|^p mu_{alpha,theta}(dz)`, `0<p<alpha`.       (10.1)

Layer cake gives

`m_p(theta)=p int_0^infinity r^(p-1)F_theta(r)dr`.                 (10.2)

Let `R_*` be large enough that the lower bound in (8.9) holds. Then

`m_p(theta)`
`>= p c_theta int_{R_*}^infinity r^(p-alpha-1)dr`
`= [p c_theta/(alpha-p)]R_*^(p-alpha)`.                            (10.3)

Hence

`liminf_{p up alpha}(alpha-p)m_p(theta) >= alpha c_theta>0`.       (10.4)

The earlier explicit upper bound (4.5) gives

`limsup_{p up alpha}(alpha-p)m_p(theta) <= alpha C_beta<infinity`. (10.5)

Therefore

`m_p(theta)=Theta((alpha-p)^(-1))` as `p up alpha`.                (10.6)

This exactly resolves the quantitative obstruction named in the preceding run. The blow-up order matches the ordinary Pareto-`alpha` model; only the sharp coefficient remains undetermined.

## 11. Critical truncated moment is exactly logarithmic in order

Define

`Q_alpha(R):=int_C min(|z|^alpha,R^alpha)mu_{alpha,theta}(dz)`.     (11.1)

Layer cake gives

`Q_alpha(R)=alpha int_0^R r^(alpha-1)F_theta(r)dr`.                (11.2)

Using (8.9), for all sufficiently large `R`,

`alpha c_theta log R + O(1)`
`<= Q_alpha(R)`
`<= alpha C_alpha log R + O(1)`.                                  (11.3)

Consequently

`Q_alpha(R)=Theta(log R)`.                                         (11.4)

Equivalently,

`alpha c_theta`
`<= liminf_{R->infinity} Q_alpha(R)/log R`
`<= limsup_{R->infinity} Q_alpha(R)/log R`
`<= alpha C_alpha`.                                                (11.5)

This replaces the previous much weaker conclusion

`Q_alpha(R)/log log R -> infinity`                                 (11.6)

by the exact logarithmic order.

## 12. Counterexample-first outcome

The first negation stress tests were slowly varying corrections still allowed by the preceding theorem:

`F_1(r)=r^(-alpha)/sqrt(log log r)`,
`F_2(r)=r^(-alpha)log log log r`.                                  (12.1)

Both have logarithmic power exponent `alpha`; the first also satisfies `r^alpha log r F_1(r)->infinity`. Thus the previous result could not distinguish them from a true Pareto tail.

The new fixed-dilation argument rejects both as possible asymptotic radial orders for a positive-off-axis C2 law: `F_1` violates the lower constant in (8.9), while `F_2` violates the upper constant. What remains possible is bounded nonconvergence of `r^alpha F_theta(r)` between positive finite constants, or convergence to a source-dependent constant.

That identifies the next source-level obstruction much more sharply:

`Does r^alpha F_theta(r) have a limit, and if so what functional of theta is it?` (12.2)

A second independent obstruction is directional: even if the radial constant exists, the source explicitly suggests different directions may have different tail behavior. The present radial argument does not resolve the angular tail measure.

## 13. Exact self-check scope

The symbolic checker verifies exactly:

- with `beta=alpha/2` and `q=p/2`,
  `q/(beta-q)=p/(alpha-p)`;
- `2(1-beta)=2-alpha`, the exponent used in the truncated Frobenius integral;
- the earlier sector scale
  `c_delta=sqrt(delta)exp(-2alpha-1/2)` gives
  `(rho/2)c_delta^alpha=(rho/2)delta^(alpha/2)exp(-2alpha^2-alpha/2)`;
- the explicit subcritical moment formula is
  `1+p C_beta/(alpha-p)`.

The archived output ends `ALL_EXACT_CHECKS_PASS = True`. The singular-value inequalities and limiting argument are theorem-sized mathematics and are written on-page above; the checker does not replace them.

## 14. Why Question 1.9 is still not closed

The current HARD7-02 chain now gives, at radial-class level:

1. exact output law on pure axis support up to deterministic dilation;
2. exponential versus polynomial support dichotomy;
3. exact positive-off-axis radial power exponent `alpha`;
4. exact moment-index dichotomy `infinity` versus `alpha`;
5. the present two-sided `Theta(r^(-alpha))` radial envelope;
6. exact order `(alpha-p)^(-1)` of near-critical moment blow-up;
7. exact order `log R` of the truncated critical moment.

But the source's wording is broader than radial order. Missing pieces include:

- existence/nonexistence and value of `lim r^alpha F_theta(r)`;
- regular variation versus bounded oscillatory slowly varying factors;
- directional/anisotropic tail measures;
- a sharp formula connecting those quantities to the full angular measure `theta_d`.

Therefore the honest status remains **PARTIAL / OPEN**, not PROVED.

## 15. Section-B accounting

- **B10 DERANDOMIZE — success.** Replaced an arbitrary witnessing off-axis sector by the deterministic angular functional `J_alpha(theta)` and obtained an explicit positive potential constant.
- **B13 FIND WHAT ONLY INCREASES — success.** Used the monotone integrated tail and singular counting functions at a fixed multiplicative scale to remove the logarithmic localization loss.
- **B21 ASK WHO ELSE HAS THIS SHAPE — success.** Recast the finite row estimate as a weak-`L^alpha` to weak-Schatten transfer and proved the rank-plus-truncated-Frobenius inequality that preserves the tail exponent.

These are different from the preceding B5/B11/B30 triple and were not used as the active Q1.9 triple in the preceding runs.

A genuinely different next triple should target (12.2), not manufacture another tail certificate. Suggested next moves: **B9/B12/B28** — randomize the radial threshold to seek a renewal identity for `r^alpha F(r)`, identify a conserved PWIT flux or mass-transport quantity that could pin the constant, and first settle existence of the limit for a typical smooth positive-off-axis angular density if the all-`theta` statement is too rigid.

## 16. Stuck/rotation status

The frozen metric has now been unchanged for **two consecutive runs** after the preceding `T_corr=3 -> 4` movement. Section I triggers only after three unchanged runs or an unchanged remaining obligation. It is therefore **not triggered yet**.

Moreover, the remaining obligation changed materially this run: the previous quantitative moment-blowup obstacle is now resolved at the correct order, and the new obstruction is the existence/sharp value of the normalized Pareto constant and the directional tail profile. If the next run leaves `T_corr` unchanged again, it must obey Section I rather than add another ordinary lemma.

## 17. Ledger delta for coordinator consumption

```yaml
ledger_delta:
  track: HARD7-02
  target: Campbell--O'Rourke (2022) Question 1.9
  canonical_claim: operations/claims/CAMPBELL-OROURKE-2022-Q1.9.md
  quantity: T_corr
  before: 4
  after: 4
  movement: no movement
  unchanged_streak: 2
  status: PARTIAL
  methods: [B10, B13, B21]
  theorem_candidate: "For every normalized C2 angular law with rho_off(theta)>0, there are c_theta,C_alpha>0 such that c_theta r^{-alpha} <= mu_{alpha,theta}(|z|>r) <= C_alpha r^{-alpha} eventually. Consequently Q_alpha(R)=Theta(log R) and m_p(theta)=Theta((alpha-p)^{-1}) as p approaches alpha from below."
  source_status: OPEN under bounded 2026-09-20 current-literature search
  self_check: exact symbolic algebra PASS; not an independent audit
  audit_status: 0/2 for this theorem candidate; source not closed
  next_obligation: "Decide existence/value of lim r^alpha F_theta(r), then directional tail asymptotics; if next frozen-metric run is unchanged, execute Section-I thinking protocol."
```
