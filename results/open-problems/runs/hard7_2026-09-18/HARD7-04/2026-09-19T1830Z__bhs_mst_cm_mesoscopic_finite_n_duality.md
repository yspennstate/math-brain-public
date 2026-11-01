Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — this is not GPT-6 at maximum, and I do not claim otherwise. NO MOVEMENT in the frozen source metric: `beta_MST^- >= eta -> beta_MST^- >= eta`, `eta=(tau-3)/(tau-1)`; fresh methods actually used: B3 PROVE SOMETHING STRONGER, B11 DUALIZE, B25 COUNT THE SAME THING TWICE.**

# HARD7-04 — finite-`n` Pareto duality through the mesoscopic postcritical window

Status: **PARTIAL / source target remains OPEN.** This run removes one analytic obstruction in the Bhamidi--Sen configuration-model MST route: for an explicit Pareto-quantile degree subclass, the extinction-dual deficit `tau-3` survives at finite `n` uniformly throughout every mesoscopic window `1 << lambda_n << n^eta`. It does **not** yet transfer through deletion of the actual principal component and therefore is not an MST upper bound or scaling-limit proof.

## 1. Continuity, ownership, and required repository reads

Canonical target remains `operations/claims/BHS-MST-CM-UNIV.md`, owned exclusively by `HARD7-04`; I read the claim back from current `master` before doing new mathematics. No competing BHS-MST owner appeared in the current claim/alias search. The neighboring heavy-tailed critical claim `operations/claims/P0150.md` is also owned by HARD7-04 but has a different source residual: weakest-assumption GHP convergence at criticality. I did not merge or overwrite those targets.

I resumed the newest own checkpoint

`runs/hard7_2026-09-18/HARD7-04/2026-09-19T1728Z__bhs_mst_cm_sharp_dual_collar.md`

rather than restarting admission. The earlier BHS run proved

`beta_MST^- >= eta`,

and the immediately preceding run proved, only at the limiting excess-law level,

`m_-(p)=1-(tau-3) epsilon+o(epsilon)`

and exposed the first-order collar barrier `delta_*=tau-3`. Its explicit remaining obligations were a triangular-array dual transfer and then a graph-level two-level conditioning/deletion argument. This run attacks the first of those two obligations.

At run start I re-read the HARD7 control, `operations/NEW_METHODS_2026-09-16.md`, `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`, campaign `INDEX.md` and `RANKING.md`, root `POSTED.md` and `RESULTS.md`, the current queue/I0049 disposition, the current claim, newest own reports, and neighboring HARD7/P0150 surfaces. I0049 remains `KNOWN / RESOLVED IN QUEUED SCOPE` and is not reopened. The root ledger remains coordinator/P26-managed, so I record only a `ledger_delta` below and do not overwrite shared state.

The idea was written before theorem bookkeeping at

`artifacts/hard7_2026-09-18/HARD7-04/2026-09-19T1830Z__bhs_mst_cm_mesoscopic_dual_transfer_idea.md`

creation commit `6d16e5e74a7a89f76779f0fcd92ff0bdb37bc3bb`, and read back successfully at that commit.

### Runtime capability honesty

The exposed scheduler interface still has no model selector, no reasoning-effort selector, and no guaranteed execution duration. GPT-6/maximum is prompt text only. This run identifies as GPT-5.6 Sol; reasoning telemetry is unavailable, hence `UNVERIFIED`. Changing that requires a platform interface which actually exposes model/reasoning controls. Historical `You cannot modify this task` failures (including P26 in one context) are authorization/context restrictions; the compliant workaround is an owning/authorized context or platform support, never a duplicate task or permission bypass. No automation was created, edited, disabled, re-enabled, or probed in this run.

## 2. Current-source/literature refresh — 19 September 2026

Primary target remains:

Shankar Bhamidi and Sanchayan Sen, *Geometry of the minimal spanning tree in the heavy-tailed regime: new universality classes*, PTRF 188 (2024), 729--804, arXiv:2009.10696, DOI `10.1007/s00440-024-01259-3`.

The source abstract still describes the `tau in (3,4)` strong-disorder MST distance scaling `n^((tau-3)/(tau-1))` as a well-known open problem for a broad class of random graphs, proves the rank-one inhomogeneous model, and proposes its limiting spaces as candidates for other heavy-tailed models. The already-admitted Section-8 configuration-model extension is therefore not replaced by a solved special case.

A fresh bounded web search on 19 September 2026 used the exact source title and the queries `configuration model minimum spanning tree heavy-tailed tau 3 4`, `configuration model minimal spanning tree power law heavy tailed`, and 2025/2026 variants. It recovered the Bhamidi--Sen paper, the Addario-Berry--Sen random 3-regular MST theorem, and ongoing configuration-model MST project descriptions, but no later source-matching theorem for the `tau in (3,4)` heavy-tailed configuration-model scaling limit. This is bounded negative evidence, not a worldwide novelty certificate.

Relevant URLs checked:

- https://arxiv.org/abs/2009.10696
- https://arxiv.org/abs/2005.02566
- https://arxiv.org/abs/1612.00650
- https://arxiv.org/abs/1810.03802
- https://www.thenetworkcenter.nl/Research-themes/Dynamics-on-networks/Developments-on-the-Configuration-Model-/

The last item is current-project evidence, not a primary theorem and not proof of openness.

## 3. Frozen metric and no-movement accounting

The fixed metric remains

`beta_MST^- := sup { beta>=0 : for every delta in (0,1) there is c_delta>0 with liminf_n P(diam(M_n)>=c_delta n^beta)>=1-delta }`.

Before this run:

`beta_MST^- >= eta`,  `eta=(tau-3)/(tau-1)`.

After this run:

`beta_MST^- >= eta`.

The trivial path-count upper bound remains `beta_MST^- <=1`, so the certified interval is still `eta <= beta_MST^- <=1`. **No movement** is claimed. This is the second consecutive no-movement run on the current BHS frozen metric, so the three-run Section-I trigger has not yet fired.

What changes is the proof route: the previous limiting-law dual calculation is upgraded to a finite-`n` mesoscopic theorem for a concrete Pareto-quantile subclass. I do not relabel that auxiliary theorem as movement of `beta_MST^-`.

## 4. Fresh 90% research moves: B3 / B11 / B25

The prior BHS runs used B1/B2/B19 and B6/B20/B30. None of this run's numbered moves was used previously on this target.

- **B3 — PROVE SOMETHING STRONGER.** Instead of another fixed-`epsilon`/limiting-law lemma, prove the dual deficit in a triangular array for every `epsilon_n=lambda_n n^{-eta}` with `lambda_n -> infinity` and `lambda_n=o(n^eta)`. **Successful for the explicit Pareto-quantile subclass below.**
- **B11 — DUALIZE.** Keep the exact extinction-root/secant identity at finite `n`. It converts the target into a ratio of endpoint derivative loss to its average. **Successful.**
- **B25 — COUNT THE SAME THING TWICE.** Express the derivative loss both through the excess pgf and through cumulative degree counts; summation by parts makes the integer-rounding error explicit. **Successful and identifies why the mesoscopic signal dominates the finite-`n` arithmetic roughness.**

Counterexample/failure stress was built into the route. It fails to certify fixed `lambda=O(1)` because the integer-tail error is itself of critical order `n^{-eta}`, and it fails at `lambda` of order `n^eta` because nearcriticality is gone. Most importantly, it does not survive actual giant deletion automatically; that is now the isolated graph-level obstruction.

## 5. Explicit finite-`n` Pareto-quantile subclass

Write

`r:=tau-1 in (2,3)`,

`a:=1/r`,

`beta:=tau-3=r-2 in (0,1)`,

`eta:=a beta=(tau-3)/(tau-1)`.

Fix `C>0`. Consider deterministic degree sequences with minimum degree at least three whose cumulative high-degree counts obey

`A_n(k):=#{v:d_v>=k}= C n k^{-r}+e_{n,k}`,        (5.1)

for `4<=k<=K_n`, where `|e_{n,k}|<=1`, `K_n=Theta(n^a)`, and there are no degrees above `K_n`; put all remaining mass at degree three and allow an `O(1)` parity correction. The literal construction `A_n(k)=floor(C n k^{-r})` until it reaches zero is the model example.

This is an explicit power-law degree family with exponent `tau-1=r`, `d_max=Theta(n^a)`, finite limiting second moment and divergent third-moment scale. Since all degrees are at least three its limiting branching factor is supercritical. I use it only as a concrete subclass/analytic test bed here; the theorem below is **not** promoted to the full retained degree-sequence class in the canonical claim.

Let

`ell_n:=sum_v d_v`,

`h_n(s):=(1/ell_n) sum_v d_v s^(d_v-1)`,

`nu_n:=h_n'(1)=(1/ell_n) sum_v d_v(d_v-1)`.

Thus `h_n` is the pgf of the size-biased excess degree. Tail summation gives

`ell_n = 3n + sum_{k>=4} A_n(k) = mu n+o(n)`                 (5.2)

for a finite `mu>0`. Similarly,

`sum_v d_v(d_v-1)=2 sum_{k>=2}(k-1)A_n(k)=Theta(n)`,         (5.3)

because `r>2`; the cumulative rounding error is `O(K_n^2)=o(n)` since `2a<1`. Hence

`nu_n -> nu in (1,infinity)`; in fact `nu>=2` from `d_v>=3`.

Define the derivative deficit

`g_n(y):=nu_n-h_n'(1-y)`                                   (5.4)

for `0<y<1`.

## 6. Finite-size Abelian lemma with explicit rounding scale

**Lemma 1 (mesoscopic derivative loss).** If

`y_n = z_n n^{-a}`,  `z_n -> infinity`,  `z_n=o(n^a)`,       (6.1)

then

`g_n(y_n)=K_0 y_n^beta(1+o(1))`

`        =K_0 n^{-eta} z_n^beta(1+o(1))`,                   (6.2)

where

`K_0=(C r/mu) I_r >0`,                                      (6.3)

`I_r:=int_0^infinity x^(1-r)(1-e^{-x}) dx`

`    =Gamma(3-r)/(r-2)`.                                    (6.4)

Moreover the error caused solely by the integer discrepancy `|e_{n,k}|<=1` is `O(n^{-eta})`, hence is smaller than the main term by `O(z_n^{-beta})`.

**Proof.** Let `N_n(k):=#{v:d_v=k}` and

`F_y(k):=k(k-1)[1-(1-y)^(k-2)]`.

From (5.4),

`ell_n g_n(y)=sum_{k>=3} N_n(k)F_y(k)`.                     (6.5)

The degree-three/bounded-degree contribution is `O(ny)`, hence `O(y)` after division by `ell_n`; because `0<beta<1` and `y->0`, this is `o(y^beta)`.

For the high-degree part, discrete summation by parts gives

`sum_{k=4}^{K_n} N_n(k)F_y(k)`

` = A_n(4)F_y(4)+sum_{k=5}^{K_n} A_n(k)[F_y(k)-F_y(k-1)]`.  (6.6)

Insert `A_n(k)=Cnk^{-r}+e_{n,k}`. The function `F_y(k)` is increasing in `k`, so the total contribution of the errors `e_{n,k}` is bounded in absolute value by a constant multiple of `F_y(K_n)+F_y(4)=O(K_n^2)`. Dividing by `ell_n~mu n` gives

`O(K_n^2/n)=O(n^(2a-1))=O(n^{-eta})`,                       (6.7)

because `2a-1=-(r-2)/r=-eta`.

It remains to evaluate the deterministic main sum

`C n [4^{-r}F_y(4)+sum_{k=5}^{K_n} k^{-r} Delta F_y(k)]`.   (6.8)

Set `t=yk`. Under (6.1), the lower endpoint `4y` tends to zero and the upper endpoint `yK_n` tends to infinity. After multiplication by `y^{-beta}`, (6.8) is a Riemann sum for

`C n y^beta * int_0^infinity t^{-r} d[t^2(1-e^{-t})]`.      (6.9)

The replacement `(1-y)^(k-2) -> e^{-yk}` is harmless in this scaling: for `0<y<1/2`, exponential upper/lower bounds obtained from `log(1-y)` squeeze it between the same profile with arguments `yk(1+o(1))`; the integrable envelopes are `t^(2-r)` at zero and `t^(1-r)` at infinity. Since `r in (2,3)`, both endpoints are integrable after the displayed Stieltjes derivative. Integration by parts yields

`int_0^infinity t^{-r} d[t^2(1-e^{-t})]`

` = r int_0^infinity t^(1-r)(1-e^{-t})dt = r I_r`.          (6.10)

The boundary terms vanish because near zero `t^2(1-e^{-t})=O(t^3)` and at infinity it is `O(t^2)`, while `2-r<0` and `3-r>0`. Finally,

`I_r=int_0^infinity t^{-1-beta}(1-e^{-t})dt`

`   =Gamma(1-beta)/beta=Gamma(3-r)/(r-2)`                   (6.11)

by one integration by parts. Divide (6.8) by `ell_n~mu n`. The rounding term (6.7) divided by the main scale `y^beta=n^{-eta}z_n^beta` is `O(z_n^{-beta})`, and the bounded-degree `O(y)` term is `o(y^beta)`. This proves (6.2)--(6.4). QED.

### Crude bound at the critical cutoff

We will also need that for each fixed `M`,

`sup_{0<y<=M n^{-a}} g_n(y)=O_M(n^{-eta})`.                 (6.12)

Indeed, `1-(1-y)^(d-2)<=y(d-2)` gives

`g_n(y) <= (y/ell_n) sum_v d_v(d_v-1)(d_v-2)`.              (6.13)

The truncated third factorial moment of (5.1) is `O(n K_n^(3-r))`; with `y<=M n^{-a}`, division by `ell_n=Theta(n)` gives

`O(M n^{-a} n^{a(3-r)})=O(M n^{-a(r-2)})=O_M(n^{-eta})`.    (6.14)

## 7. Average derivative loss

Define

`B_n(y):=(1/y) int_0^y g_n(t)dt`.                            (7.1)

**Lemma 2.** Whenever `y_n n^a -> infinity` and `y_n->0`,

`B_n(y_n)=K_0 y_n^beta/(beta+1) (1+o(1))`,                  (7.2)

and therefore

`g_n(y_n)/B_n(y_n) -> beta+1`.                              (7.3)

**Proof.** Put `z_n=y_n n^a`. For a fixed large `M`, split the integral at `M n^{-a}`. By (6.12), the first piece contributes at most

`(M/z_n) O_M(n^{-eta})`,                                    (7.4)

which divided by `y_n^beta=n^{-eta}z_n^beta` is `O_M(z_n^{-beta-1}) ->0`.

On `[M n^{-a},y_n]`, the proof of Lemma 1 is uniform once `M` is large: the same Riemann-sum comparison gives `g_n(t)=K_0 t^beta(1+o_M(1))`, with `o_M(1)->0` after `n->infinity` and then `M->infinity`. Hence

`(1/y_n) int_{M n^{-a}}^{y_n} g_n(t)dt`

` = K_0 y_n^beta/(beta+1)(1+o(1))`.                         (7.5)

Together with (7.4) this proves (7.2), and (7.3) follows from Lemma 1. QED.

## 8. Main theorem: finite-`n` extinction duality for `1 << lambda << n^eta`

**Theorem 3 (mesoscopic triangular-array dual transfer).** Let

`lambda_n -> infinity`,  `lambda_n=o(n^eta)`,                (8.1)

`epsilon_n:=lambda_n n^{-eta}`,                              (8.2)

`p_n:=(1+epsilon_n)/nu_n`.                                   (8.3)

For large `n`, `p_n<1`. Let `u_n<1` be the extinction probability of the bond-percolated excess Galton--Watson process with pgf

`phi_n(s)=h_n(1-p_n+p_n s)`,                                 (8.4)

and put

`q_n:=1-p_n+p_nu_n`,                                         (8.5)

`y_n:=1-q_n`,                                                (8.6)

`m_{n,-}:=phi_n'(u_n)=p_n h_n'(q_n)`.                        (8.7)

Then

`y_n n^a -> infinity`, `y_n->0`, and                         (8.8)

`(y_n n^a)^beta ~ ((beta+1)nu/K_0) lambda_n`.                (8.9)

Most importantly,

`1-m_{n,-}=(beta+o(1))epsilon_n`

`           =(tau-3+o(1)) lambda_n n^{-eta}`.                (8.10)

Thus the exact heavy-tail dual-deficit coefficient `tau-3` persists at finite `n` throughout every mesoscopic nearcritical scale (8.1) for this Pareto-quantile subclass.

**Proof.** The extinction equation `u_n=phi_n(u_n)` is equivalent, after `q_n=1-p_n+p_nu_n`, to

`q_n=1-p_n+p_n h_n(q_n)`.                                   (8.11)

With `y_n=1-q_n`,

`y_n=p_n[1-h_n(1-y_n)]`.                                    (8.12)

Divide by `y_n` and integrate `h_n'`:

`1/p_n=[1-h_n(1-y_n)]/y_n`

`     =(1/y_n)int_0^{y_n}h_n'(1-t)dt`

`     =nu_n-B_n(y_n)`.                                       (8.13)

Since `p_n nu_n=1+epsilon_n`, (8.13) gives the exact secant identity

`epsilon_n=p_n B_n(y_n)`.                                   (8.14)

First, `y_n->0`. Because every size-biased excess degree is at least two,

`h_n'(1-t)=E[X_n(1-t)^(X_n-1)] <= (1-t)E[X_n]=(1-t)nu_n`,    (8.15)

so `g_n(t)>=t nu_n` and therefore `B_n(y)>=nu_n y/2`. From (8.14),

`epsilon_n >= p_n nu_n y_n/2=(1+epsilon_n)y_n/2`,            (8.16)

hence `y_n<=2epsilon_n/(1+epsilon_n)->0`.

Next, `z_n:=y_n n^a -> infinity`. If a subsequence had `z_n<=M`, then `B_n(y_n)<=g_n(y_n)=O_M(n^{-eta})` by (6.12), and (8.14) would imply `epsilon_n=O(n^{-eta})`. But `epsilon_n=lambda_n n^{-eta}` with `lambda_n->infinity`, contradiction. Thus `z_n->infinity`. Since `y_n->0`, also `z_n=o(n^a)`, so Lemmas 1 and 2 apply.

Substitute (7.2) into (8.14):

`lambda_n n^{-eta}`

` = p_n [K_0/(beta+1)] n^{-eta} z_n^beta(1+o(1))`.           (8.17)

As `p_n->1/nu`, this is exactly (8.9).

Finally,

`1-m_{n,-}`

` = p_n[nu_n-h_n'(1-y_n)]-(p_nnu_n-1)`

` = p_n g_n(y_n)-epsilon_n`

` = p_n[g_n(y_n)-B_n(y_n)]`.                                (8.18)

Divide by (8.14):

`(1-m_{n,-})/epsilon_n = g_n(y_n)/B_n(y_n)-1 -> beta`        (8.19)

by (7.3). Since `beta=tau-3`, (8.10) follows. QED.

### Height consequence

Let `H_n` be the height of the Galton--Watson process conditioned on extinction. For generation size `Z_k`,

`P(H_n>=k)<=P(Z_k>=1)<=E Z_k=m_{n,-}^k`.                    (8.20)

For fixed `s>0`, take `k_n=floor(s n^eta/lambda_n)`. From (8.10),

`limsup_n P(H_n>=k_n) <= exp(-(tau-3)s)`.                    (8.21)

Thus the exact finite-`n` dual height scale in the mesoscopic regime is `n^eta/lambda_n`, matching the scale needed in a geometric Kruskal ladder.

## 9. Two-level collar consequence and the sharp allowable increment

Fix `delta in (0,tau-3)` and define

`p_{n,delta}:=[1+(1+delta)epsilon_n]/nu_n`.                   (9.1)

Keep the extinction tilt `q_n` generated at level `p_n`. Then

`p_{n,delta}/p_n`

` = [1+(1+delta)epsilon_n]/[1+epsilon_n]`

` =1+delta epsilon_n+O(epsilon_n^2)`.                        (9.2)

Using (8.10),

`p_{n,delta} h_n'(q_n)`

` =(p_{n,delta}/p_n)m_{n,-}`

` =1-(tau-3-delta+o(1))epsilon_n`.                           (9.3)

Consequently, for every fixed `c<tau-3-delta`,

`p_{n,delta} h_n'(q_n) <= 1-c lambda_n n^{-eta}`             (9.4)

for all sufficiently large `n`.

This makes the preceding run's collar barrier `delta_*=tau-3` finite-`n` and mesoscopic in this explicit subclass. It also shows exactly what cannot be demanded from this first-moment route: a fixed collar `delta>tau-3` makes the proxy supercritical to first order.

## 10. What is genuinely new here, and what remains missing

The result of this run is not the fixed limiting-law formula again. The substantive strengthening is:

> For an explicit integer-valued Pareto-quantile degree array, the heavy-tail extinction-dual coefficient `tau-3`, its extinction-root scale, and its `n^eta/lambda` height scale hold uniformly for every `lambda_n -> infinity` with `lambda_n=o(n^eta)`.

This matters because the Bhamidi--Sen rank-one MST proof uses a geometric sequence of growing nearcritical levels; a fixed-parameter asymptotic alone cannot justify that ladder.

However, the **actual source obstruction remains graph-level**. The theorem above uses the deterministic original half-edge law. Kruskal complement control needs a statement after conditioning on and deleting the random principal component. The next proof must show, uniformly along a geometric `lambda` ladder, that the residual paired half-edge profile has an effective offspring mean no larger than

`1-c lambda n^{-eta}`                                               (10.1)

for some `c>0`, while controlling without-replacement exploration and surplus edges. Equation (9.4) supplies the deterministic target margin, not the random transfer.

The failure modes are now precise:

1. **Fixed `lambda=O(1)`:** integer quantile rounding is of the same critical order `n^{-eta}` as the signal, so this mesoscopic proof alone does not certify the fixed-window endpoint. The published critical scaling theorem and the previous limiting-law analysis remain the appropriate tools there.
2. **`lambda` comparable with `n^eta`:** `epsilon_n` is no longer small; no nearcritical linear deficit is claimed.
3. **Random principal-component deletion:** degree depletion and pairing conditioning may destroy the deterministic profile unless a concentration/duality theorem controls them. This is the main remaining obligation.

A good next fresh triple, if the metric is still unchanged, is **B4 PROVE SOMETHING WEAKER COMPLETELY** (one actual deleted-profile scale), **B13 FIND WHAT ONLY INCREASES** (a depletion monotonicity for residual excess mean), and **B18 SAY IT IN ANOTHER LANGUAGE** (size-biased empirical measure / martingale formulation). Those numbers have not yet been used on the BHS target.

## 11. Verification and persistence

No exact-arithmetic checker was created: the new claim is an analytic asymptotic theorem and its proof is on the page; there is no finite exhaustive core to certify. This follows the owner's 90/10 rule rather than manufacturing another receipt-only checker.

Immutable idea artifact:

`artifacts/hard7_2026-09-18/HARD7-04/2026-09-19T1830Z__bhs_mst_cm_mesoscopic_dual_transfer_idea.md`

No root shared ledger was edited. Proposed coordinator delta:

`HARD7-04 | BHS-MST-CM-UNIV | beta_MST^-: >=eta -> >=eta (NO MOVEMENT); new finite-n theorem: Pareto-quantile dual deficit (tau-3+o(1)) lambda n^-eta uniformly for 1<<lambda<<n^eta | PARTIAL`

Closure is **not** claimed. No independent audit is requested or counted in this run; closure would still require the full source-matching scaling-limit proof, appropriate exact certificate for any finite core, prior-art reconciliation, and two independent other-track audits.