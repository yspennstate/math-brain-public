Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED. This is not GPT-6 at maximum.**

**NO SOURCE-LEVEL COEFFICIENT-METRIC MOVEMENT; NEW OPTIMIZED FIXED-FRACTION POISSON BAND.** The saturated frontiers remain `c_LK^cert=a_LK^fine=b_LK^sqrt=0`; HARD recoveries remain `0/2`. This run uses Section-B methods **#5 ADD A PARAMETER AND DIFFERENTIATE IN IT, #13 FIND WHAT ONLY INCREASES, #24 FIND THE EXTREMAL OBJECT**. The main advance is an optimized one-root saddle estimate whose exponential relative-error rate raises Claim 295's explicit `1%` Poisson band to every fixed symmetric fraction below an explicit proof-route constant `alpha_split=0.1097671059...`; in particular the clean `10%` band is rigorously certified.

# P03 / P0456 run report — optimized saddle exponent, monotone Palm envelope, and extremal witness count

Run timestamp: **2026-09-18T20:34:28Z**  
Track: **P03**  
Canonical target: **P0456**  
Repository / branch: `yspennstate/math-open-problems` / `master`  
Category: **HARD OUTSIDE**

---

## 1. Continuity, repository screen, source status, and audit gate

The exclusive assignment remains

`operations/claims/P0456.md`,

creation commit `9d9c9545783bf8ae09805830d72f5d935be9afb1`, blob `74b9c5ebda19b1ded526457c1c7ea12654419bcb`.

The newest complete P03 report entering this run was

`proofnet24/P03-fei/runs/2026-09-18/2026-09-18T19-32-54Z__p0456-fixed-fraction-poisson-band.md`,

creation commit `97e01cbd3899760f15cba9db4862c888012d21b7`, blob `ecbb2205becd2efc0c9f4f6aea66c3d619ac0ce5`; exact-commit readback recovered `**End of complete run report.**`.

I preserve Claims 274, 276, 278, 280, 282, 284, 286 and the candidate-complete/audit chain 288--295.

This invocation reread/recovered root `README.md`, `proofnet24/HOURLY_PROTOCOL_2026-09-15.md`, current `FLEET_RULES.md`, `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`, campaign `probability_campaign_2026_09/INDEX.md` and `RANKING.md`, root `POSTED.md`, root `RESULTS.md`, current `QUEUE.md`, the canonical P0456 claim, the complete newest P03 report, Claim 294's rank-Palm proof, the current P26 directory and newest P26 report, and neighboring P04 status only for the directed audit obligation. Large connector-rendered root/campaign surfaces can be truncated; I do **not** represent those as byte-for-byte rereads. Exact-path reads controlled every imported mathematical dependency used below.

P0457 remains the distinct diameter problem and is not resumed here.

### Fresh primary-source / prior-art verification

The primary source remains Hossein Dabirian and Vijay Subramanian, *Connectivity of a family of bilateral preference random graphs*, *Journal of Applied Probability* 63(2) (June 2026), 552--579, DOI `10.1017/jpr.2025.10051`, published online 18 December 2025.

Fresh Cambridge retrieval on 18 September 2026 again recovered Section 1.1's literal open band

`log n -(1/2) loglog n sqrt(log n) <= k <= log n +(1/2) loglog n sqrt(log n)`

and its statement that more elaborate or exact sufficient conditions could close the gap. The same primary PDF recovers Theorem 6: for `k >= log n+t' loglog n sqrt(log n)` with fixed `t'>1/2`, connectivity holds whp; in particular `k=floor(t log n)` is connected whp for every fixed `t>1`. The PDF text was accessible; screenshot retrieval was also attempted as required by the PDF-analysis protocol but the web screenshot cache missed in this invocation.

Fresh bounded searches for the exact title/DOI/authors, `LK(n,k) Poisson isolated vertices`, `LK(n,k) log n+c connectivity`, and bilateral-preference constant-window results again recovered the primary source and adjacent random-graph work but no later theorem matching Claims 288--295 or the strengthening below. This is dated bounded negative evidence only; **publication novelty remains UNVERIFIED**.

### Fresh outside-audit screen

The newest P26 report now present is

`proofnet24/P26-proof-audit-recovery/runs/2026-09-18/2026-09-18_23-00-00__run-report.md`,

blob `3ba1eb97d515be4bc47ee7035e45d2114a9851eb` on current `master`. It audits historical P04/I0101 Claim 43, not P0456. Repository search for P0456 plus audit/PASS still recovers no P26 or distinct OTHER-track full-chain audit of Claims 288/289. P04 remains rotation-stopped with no genuinely new theorem for the directed P03->P04 duty; no repeat audit is fabricated.

Therefore the closure gate remains

`P0456_ACTIVE_AUDIT_PENDING / OUTSIDE_AUDITS_FOUND_0_OF_2`.

Self-audits do not count. No final paper folder is created.

---

## 2. Preserved chain and new theorem

The candidate-complete source-matching chain remains:

- `P03-P0456-POISSON-CRITICAL-WINDOW-288 = PROVED / SOURCE-MATCHING-CANDIDATE-COMPLETE / AUDITS-PENDING / PUBLICATION-NOVELTY-UNVERIFIED`;
- `P03-P0456-UNIFORM-POISSON-INTERACTION-REPAIR-289 = PROVED / SELF-AUDIT-REPAIR / SOURCE-MATCHING-STRENGTHENING / AUDITS-PENDING / PUBLICATION-NOVELTY-UNVERIFIED`;
- Claim 290 is the marked isolated-vertex PPP cross-check;
- Claims 291--295 remain supporting P03 self-audit/strengthening kernels.

This run adds:

### Claim `P03-P0456-OPTIMIZED-SADDLE-FRACTION-BAND-296`

**Status:** `PROVED / SELF-AUDIT-STRENGTHENING / SUPPORTING / AUDITS-PENDING / PUBLICATION-NOVELTY-UNVERIFIED`.

Define, for `0<theta<1`,

`gamma(theta)=theta-log(1+theta)`,                            (2.1)

`delta(theta)=theta-1-log(theta)`,                            (2.2)

and

`eta_split=max_{0<theta<1} min(gamma(theta),delta(theta)).`    (2.3)

Then `gamma` is strictly increasing, `delta` is strictly decreasing, and the maximum occurs at the unique `theta_*` solving

`gamma(theta_*)=delta(theta_*)`.                              (2.4)

Numerically,

`theta_*=0.5819767068693264...`,
`eta_split=0.1233015614822445...`.                            (2.5)

Put

`alpha_split=eta_split/(1+eta_split)
             =0.1097671059226009...`.                         (2.6)

For every fixed `alpha` satisfying

`0<alpha<alpha_split`,                                        (2.7)

uniformly over all integers

`|k-log n| <= alpha log n`,                                   (2.8)

with `Z_n` the number of isolated vertices and

`lambda_n=n e^{-k}`,                                          (2.9)

we have

`d_TV(Law(Z_n),Poisson(lambda_n)) -> 0`,                      (2.10)

and

`P(LK(n,k) is connected)=exp(-lambda_n)+o(1)`.               (2.11)

The constant `alpha_split` is the optimized radius of the **specific two-region beta-saddle proof below**. It is not claimed to be a model threshold, a literature constant, or the maximal range of a different proof.

A clean rational corollary is the uniform **10% band**

`|k-log n| <= (1/10) log n`.                                 (2.12)

Indeed the rational split `theta=7/12` has

`gamma(7/12)=0.1238010039548931...`,
`delta(7/12)=0.1223298340660203...`,                           (2.13)

so the safe exponent `eta=3/25=0.12` is valid, and

`(3/25)(1-1/10)-1/10=1/125>0`.                               (2.14)

Thus Claim 295's explicit `1%` radius is materially enlarged to `10%`, while the parametric statement (2.7) records the full rigorously optimized range of this saddle split.

---

## 3. #5 ADD A PARAMETER AND DIFFERENTIATE — the sharp exponent of the two-region saddle proof

The clean one-root marked probability is, as in Claims 288/294/295,

`M_{k,k}=(m)_{k+1}/k! int_0^1 Q_k(x)^k(1-x)^(m-k-1) dx`,      (3.1)

where

`m=n+O(1)`, `N=n+O(k)`,
`Q_k(x)=E[(x-B_k)_+]`,
`B_k~Beta(k,N-k+1)`,
`beta=E B_k=k/(N+1)`.                                         (3.2)

The mean-replacement integral is exact:

`M_0=(1-beta)^m=e^{-k}(1+O(k^2/n))`.                          (3.3)

Instead of Claim 295's fixed split, put

`x_0=beta+theta k/N`, `0<theta<1`.                            (3.4)

### 3.1 Upper region — remove the old Cauchy--Schwarz half-exponent loss

Let `f` be the beta density. For `x>=x_0`, write

`R(x)=E[(B_k-x)_+]`,
`Q_k(x)=x-beta+R(x)`.                                         (3.5)

The beta density is

`f(b)=k C(N,k) b^(k-1)(1-b)^(N-k)`.                          (3.6)

Its log derivative is

`(log f)'(b)=(k-1)/b-(N-k)/(1-b)`.                            (3.7)

Since `Nx_0=(1+theta+o(1))k` and `k=O(log n)=o(N)`, for fixed `theta` there is `c_theta>0` such that, for all large `n`,

`(log f)'(b) <= -c_theta N` for all `b>=x_0`.                 (3.8)

Hence

`f(b)<=f(x_0) exp[-c_theta N(b-x_0)]`.                        (3.9)

Now let `X~Bin(N,x_0)`. The exact density/mass identity is

`f(x_0)=(k/x_0) P(X=k)`.                                     (3.10)

Also `P(X=k)<=P(X<=k)`, and the elementary binomial Chernoff bound gives

`P(X<=k)<=exp[-(gamma(theta)+o(1))k]`,                         (3.11)

because `E X=(1+theta+o(1))k` and

`gamma(theta)=theta-log(1+theta)`.                            (3.12)

Combining (3.9)--(3.11),

`R(x)
 <= int_x^1 (b-x) f(b) db
 <= C_theta N^(-1) exp[-(gamma(theta)+o(1))k]`                (3.13)

uniformly for `x>=x_0`. Since `x-beta>=theta k/N`,

`k R(x)/(x-beta)
 <= C_theta exp[-(gamma(theta)+o(1))k]`.                      (3.14)

Therefore

`Q_k(x)^k
 =(x-beta)^k[1+O_theta(exp(-(gamma(theta)-o(1))k))]`          (3.15)

throughout the upper region.

This is strictly stronger than Claim 295's Cauchy--Schwarz route, which lost a factor two in the exponent. The overshoot integral (3.13) exploits the monotone beta-density slope after the split and retains the full Chernoff rate `gamma(theta)`.

### 3.2 Lower region

Write

`t=(x-beta)N/k`.                                              (3.16)

For `k^(-1/4)<=t<=theta`,

`Q_k(x)
 <= (x-beta)+E|B_k-beta|
 = (k/N)(t+O(k^(-1/2)))`.                                     (3.17)

Relative to the mean-replacement saddle at `t=1`, the normalized log-integrand rate is

`log t+1-t+o(1)`.                                             (3.18)

It is strictly increasing on `0<t<1`, so on `t<=theta` the loss is at least

`delta(theta)=theta-1-log(theta)>0`.                          (3.19)

The region `t<k^(-1/4)` and the region `x<=beta` are superexponentially smaller because there

`Q_k(x)<=O(k^(3/4)/N)`                                       (3.20)

and the `k`th power loses `(1/4)k log k+O(k)` relative to the saddle. Consequently, for every fixed `eta<delta(theta)`, the entire lower region is `O(e^{-eta k})M_0`.

### 3.3 Relative saddle error and its optimization

Combining (3.3), (3.15), and the lower-region bound, for every fixed `theta in (0,1)` and every fixed

`eta<min(gamma(theta),delta(theta))`,                          (3.21)

we obtain, uniformly on any compact positive ratio band `c log n<=k<=C log n`,

`M_{k,k}
 =e^{-k}[1+O_theta(poly(k)e^{-eta k})+O(k^2/n)]`.             (3.22)

The sparse internal-edge correction of Claims 286/288/294/295 is uniform on such compact ratio bands, so exact isolation satisfies

`P(I_v)
 =e^{-k}[1+O_theta(poly(k)e^{-eta k})+n^{-1+o(1)}]`.          (3.23)

Now differentiate:

`gamma'(theta)=theta/(1+theta)>0`,                            (3.24)

`delta'(theta)=1-1/theta<0` for `0<theta<1`.                  (3.25)

As `theta downarrow 0`, `gamma(theta) downarrow 0` while `delta(theta) -> infinity`; as `theta uparrow 1`, `delta(theta) downarrow 0` while `gamma(theta)>0`. Hence the maximum of the minimum is attained at the unique crossing (2.4). This proves (2.5) and the definition of the optimized proof-route exponent `eta_split`.

No numerical optimization is needed for the theorem: `theta_*` is uniquely defined by (2.4). The decimals in (2.5)--(2.6) are orientation only.

---

## 4. From the optimized mean estimate to the fixed-fraction Poisson law

Fix `alpha<alpha_split`. By (2.6),

`alpha/(1-alpha)<eta_split`.                                  (4.1)

Choose `eta` and `theta` with

`alpha/(1-alpha)<eta<min(gamma(theta),delta(theta))`.          (4.2)

On the band (2.8), the largest explicit Poisson intensity occurs at the lower endpoint:

`lambda_n=n e^{-k}<=n^alpha`.                                (4.3)

Using (3.23),

`|nP(I_v)-lambda_n|
 <= n^{alpha-eta(1-alpha)+o(1)}+n^{alpha-1+o(1)}
 =o(1)`.                                                       (4.4)

The exact local-block Palm coupling of Claims 293--295 is unchanged. Claim 294's rank-witness proof and Claim 291's bounded-omission saddle are uniform on any fixed compact ratio band. Hence

`E|Z_n^s-(Z_n+1)|
 <= poly(k)e^{-k+o(k)}
 <= n^{-(1-alpha)+o(1)}
 =o(1)`.                                                       (4.5)

The standard size-bias Stein inequality therefore gives

`d_TV(Law(Z_n),Poisson(E Z_n))->0`.                           (4.6)

Together with

`d_TV(Poisson(E Z_n),Poisson(lambda_n))
 <= |E Z_n-lambda_n|`,                                       (4.7)

this proves (2.10).

For the clean `alpha=1/10` corollary, use `theta=7/12`, `eta=3/25`. Then the first term in (4.4) is at most

`n^{-1/125+o(1)}`,                                            (4.8)

while the Palm influence term is `n^{-9/10+o(1)}`.

---

## 5. Connectivity on the optimized band without extrapolating component envelopes

As in Claim 295, avoid extending any fixed-size component estimate beyond the range actually needed.

Split the band into three zones.

1. **Central zone:** `|k-log n| <= (log n)^(3/4)`. Claim 294 already gives the Poisson law and eliminates every nontrivial component whp via Claims 291, 280, and 278. Hence connectivity equals `P(Z_n=0)+o(1)=e^{-lambda_n}+o(1)`.

2. **Lower flank:** `k<log n-(log n)^(3/4)`. Then `lambda_n->infinity`. By (2.10), `P(Z_n=0)=e^{-lambda_n}+o(1)=o(1)`, and

`P(connected)<=P(Z_n=0)`.                                    (5.1)

Thus both sides of (2.11) tend to zero.

3. **Upper flank:** `k>log n+(log n)^(3/4)`. This is eventually above the published Theorem-6 sufficient window `log n+(1/2+epsilon)loglog n sqrt(log n)`, so the source gives connectivity whp. Simultaneously `lambda_n->0`, hence `e^{-lambda_n}->1`.

This proves (2.11) uniformly for every fixed `alpha<alpha_split` without a mean-degree argument.

---

## 6. #13 FIND WHAT ONLY INCREASES — a monotone Palm envelope exists

Claim 295 correctly showed that the **naive deterministic surgery that freezes the root star** cannot be Palm-exact: isolation reweights the root order vector. That does not rule out a joint monotone coupling. There is, in fact, a clean stochastic-order statement.

Fix the root `V` and its top-`k` label set `S`. Let

`D=(D_1,...,D_k)`                                             (6.1)

be the ordered root proposal weights, and for every nonroot competitor edge `e` appearing in the selected-neighbour stars put

`Y_e=1-W_e`,                                                  (6.2)

so larger `Y_e` means a lower competitor weight and therefore makes rejection of the root proposal easier.

Conditional on the label set `S`, the vector `D` has the law of the first `k` order statistics of iid uniforms; it is associated because every order statistic is a coordinatewise nondecreasing function of the underlying independent sample. The `Y_e` are independent of `D` and are mutually independent except that a selected-selected edge is represented once as the same coordinate in the two neighbour constraints. Products of associated systems remain associated.

The root-isolation indicator is coordinatewise increasing in the mixed order `(D,Y)`: increasing a root deadline can only make rejection at its selected neighbour easier, and increasing a competitor-lowness variable can only add a competitor below one or two relevant deadlines.

Therefore Harris association gives, for every bounded coordinatewise increasing `g`,

`E[g(D,Y) 1_{I_V} | S]
 >= E[g(D,Y)|S] P(I_V|S)`,                                   (6.3)

or equivalently

`E[g(D,Y)|S,I_V=1] >= E[g(D,Y)|S]`.                          (6.4)

Thus the isolated-root Palm local law **stochastically dominates** the ordinary local law in the mixed order “root deadlines larger / competitor weights lower.” By Strassen's theorem on this finite-dimensional closed partial order, an ordered randomized coupling exists.

This is a genuine monotone envelope that Claim 295 did not use. It does **not** prove the existence of a deterministic coordinatewise Monge map, and I do not claim one. The exact accept/reject sampler remains the constructive Palm realization; (6.4) is a structural domination statement that may support a future monotone coupling proof.

---

## 7. #24 FIND THE EXTREMAL OBJECT — the `O(k^2)` reciprocity candidate count is order-sharp

Could the Stein error be improved by replacing Claim 294's `O(k^2)` Type-R witness candidates by a smaller typical count? At the raw-witness level, no.

Fix an outside vertex `w` and ignore local edges into `A` until a Type-P witness occurs. Let

`D_1<...<D_k`                                                (7.1)

be the first `k` order statistics of the far edges from `w`, among `M=n-O(k)` candidates. Then exactly

`E D_j=j/(M+1)`.                                              (7.2)

For the `j`th far proposal endpoint `u_j`, each of the `|A|=k+1` raw edges from `u_j` into `A` is a potential reciprocity-rank witness if its weight lies below `D_j`. Hence in the ordinary copy the expected number of raw Type-R subdeadline pairs is

`(k+1) sum_{j=1}^k E D_j
 =(k+1) k(k+1)/(2(M+1))
 =(1/2+o(1)) k^3/n`.                                         (7.3)

Thus the `Theta(k^2)` candidate multiplicity and the resulting bare `Theta(k^3/n)` low-edge mass are not merely artifacts of a union bound: they are the correct order before the rare-isolation cost is imposed. Type R genuinely dominates Type P at this level.

Consequently, the present Stein proof is not bottlenecked by a removable factor `k` in the candidate enumeration. Any sharper absolute coupling rate must exploit cancellation, conditional isolation structure, or a finer coupling—not simply a smaller typical candidate set. The fixed-fraction range in Claim 296 is controlled by mean accuracy of the one-root saddle, not by the Palm influence estimate.

---

## 8. First-correction hunt and failure boundary

The improved saddle exponent also rechecks the possible first corrections.

- The exact mean-replacement factor `(1-beta)^m/e^{-k}=1+O(k^2/n)` contributes only `lambda_n O(k^2/n)=o(1)` throughout every fixed `alpha<alpha_split` band.
- The sparse-internal-edge correction remains `lambda_n n^{-1+o(1)}=o(1)`.
- The Palm interaction / joint-isolation correction remains smaller than the main intensity on this range.
- Fixed size-two and other nontrivial component probabilities vanish in the central zone; on the flanks the connectivity patch does not require a finer component expansion.

No nonzero `O(1)` correction coefficient is identified. The exact next correction to `P(I_v)` or to the connectivity law remains **OPEN**.

The first obstruction to pushing the symmetric fixed fraction farther by the present proof is now explicit: the optimized two-region saddle supplies at most `eta_split`, and absolute Poisson-mean accuracy requires

`alpha<eta_split(1-alpha)`.                                  (8.1)

At equality the current error estimate is only order one. This is a **proof-route boundary**, not evidence that the Poisson law itself fails there.

---

## 9. Metrics, status, audit duty, and exact remaining obligations

All admitted coefficient metrics remain saturated and are not used to manufacture stuck counts:

- `c_LK^cert=0` at `sqrt(log n) log log n`;
- `a_LK^fine=0` at `sqrt(log n log log n)`;
- `b_LK^sqrt=0` at `sqrt(log n)`.

There is no new frozen fleet metric in this run. The fixed-fraction radius is a supporting theorem parameter, not a newly admitted stuck-count quantity. HARD recoveries remain `0/2`.

Directed P03->P04 audit duty: the newest P04 state remains rotation-stop/administrative with no genuinely new mathematical theorem. I therefore perform no fabricated or repeated audit.

The source-matching result remains **audit pending**. The exact closure obligations are unchanged:

1. P26 must perform a genuine end-to-end outside audit of the 288/289 source-matching chain (Claims 291--296 are available audit kernels but do not replace that chain);
2. one distinct OTHER track must independently audit the same full implication chain;
3. any objection from either audit overrides strengthening work and must be repaired before closure;
4. publication novelty remains UNVERIFIED after the bounded current-literature miss;
5. only after two genuine outside PASS audits may P03 create the final source-matching paper folder and request shared-ledger closure through `ledger_delta`.

Current state:

`P0456_ACTIVE_AUDIT_PENDING / OUTSIDE_AUDITS_FOUND_0_OF_2 / CLAIM_296_OPTIMIZED_FRACTION_AUDIT_KERNEL_READY / RECOVERIES_USED=0/2`.

---

## 10. Next state

The next run must consume any incoming P26/OTHER-track audit first. If the audit gate is still empty, do not spend the run merely optimizing another decimal of `alpha_split`.

Fresh Section-B triple reserved for the next substantive attack:

- **#9 RANDOMIZE:** look for a direct change-of-measure or exponential-tilting proof of the exact one-root integral that bypasses the two-region split and might produce the true large-deviation rate rather than the current proof-route `eta_split`;
- **#12 FIND WHAT IS CONSERVED:** identify a likelihood-ratio / martingale invariant under revealing selected-neighbour stars that could control the Palm law without accumulating rank-witness errors;
- **#15 BREAK THE SYMMETRY ON PURPOSE:** treat lower and upper fixed-fraction offsets separately. The lower side is mean-accuracy limited; the upper side already has source connectivity and vanishing intensity, so a symmetric radius may be the wrong object.

A useful target is an **asymmetric** theorem: maximize the certified lower fraction `alpha_-` for the Poisson mean while allowing a separate upper fraction `alpha_+`, and prove or refute whether the optimized saddle rate is the actual obstruction. Any proposed extension must keep the literal LK dependence structure and must not infer connectivity from mean degree.

---

## 11. `ledger_delta` for P26

```text
P03/P0456:
  status: ACTIVE_AUDIT_PENDING
  source_claim: P03-P0456-POISSON-CRITICAL-WINDOW-288 (candidate complete; 0/2 outside audits found)
  new_supporting_claim: P03-P0456-OPTIMIZED-SADDLE-FRACTION-BAND-296 = PROVED / SELF-AUDIT-STRENGTHENING / SUPPORTING / AUDITS-PENDING / PUBLICATION-NOVELTY-UNVERIFIED
  theorem: for every fixed alpha < alpha_split, uniformly |k-log n|<=alpha log n, Z_n is TV-close to Poisson(n e^-k) and P(connectivity)=exp(-n e^-k)+o(1), where alpha_split=eta_split/(1+eta_split), eta_split=max_{0<theta<1} min(theta-log(1+theta), theta-1-log theta)=0.12330156148..., alpha_split=0.10976710592...
  clean_corollary: uniform 10% band |k-log n|<=0.1 log n, using theta=7/12 and eta=3/25
  structural_support: isolated-root Palm law stochastically dominates ordinary local law in the mixed order (larger root deadlines/lower competitor weights); Type-R raw witness mass is (1/2+o(1))k^3/n, so O(k^2) candidate enumeration is order-sharp
  saturated_metrics: c_LK^cert=0; a_LK^fine=0; b_LK^sqrt=0
  stuck_count: not applicable to saturated metrics
  recoveries: 0/2
  outside_audits: 0/2 (fresh P26 23:00 report audits P04/I0101, not P0456)
  publication_novelty: UNVERIFIED after bounded 2026-09-18 source/literature search
  next: consume outside audits first; otherwise pursue asymmetric lower/upper fraction and a direct tilted one-root saddle
```

No shared root ledger is edited by P03.

---

## 12. Model / interface honesty

Actual runtime available to this report identifies as **GPT-5.6 Sol**; reasoning level is **UNVERIFIED**. This is not GPT-6 at maximum. The exposed scheduling controls in this environment still provide timing/title/prompt controls but no model selector or reasoning-effort selector. GPT-6/maximum therefore remains prompt-only; changing that requires a product surface or owning/admin context that actually exposes those selectors. Permission denial, if encountered elsewhere, must be handled through the owning context/admin/support and never by duplicating tasks or bypassing permissions.

**End of complete run report.**