Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED. This is not GPT-6 at maximum.**

**NO SOURCE-LEVEL COEFFICIENT-METRIC MOVEMENT; NEW BIVARIATE RARE-EVENT CROSS-CHECK.** The saturated frontiers remain `c_LK^cert=a_LK^fine=b_LK^sqrt=0`; HARD recoveries remain `0/2`. This run uses fresh Section-B methods **#1 CHANGE THE CATEGORY, #7 TAKE THE LIMIT, #25 COUNT THE SAME THING TWICE**. The substantive advance is an exact bivariate Gamma/Poisson-arrival representation of Claim 299's one-defect term and a direct boundary-saddle expansion that independently recovers both `C_*` and `a_1`, without invoking Claim 299's one-dimensional Watson/Laplace `L_1` formula.

# P03 / P0456 run report — bivariate rare-event geometry and independent second-correction cross-check

Run timestamp: **2026-09-19T00:27:09Z**  
Track: **P03**  
Canonical target: **P0456**  
Repository / branch: `yspennstate/math-open-problems` / `master`  
Category: **HARD OUTSIDE**

---

## 1. Continuity, controls, source status, and audit-first screen

The exclusive assignment remains

`operations/claims/P0456.md`,

creation commit `9d9c9545783bf8ae09805830d72f5d935be9afb1`, blob `74b9c5ebda19b1ded526457c1c7ea12654419bcb`.

The newest complete P03 report entering this invocation was

`proofnet24/P03-fei/runs/2026-09-18/2026-09-18T23-31-30Z__p0456-second-correction-finite-reduction.md`,

creation commit `48897504e27eb996b34caf42b28f82598d482681`, blob `83d1c47e517643e86ad98f28583fbfc159ba4f29`; exact-commit readback recovered `**End of complete run report.**`.

I preserve Claims 274, 276, 278, 280, 282, 284, 286 and Claims 288--299.

This run reread/recovered the root `README.md`, `proofnet24/HOURLY_PROTOCOL_2026-09-15.md`, current `FLEET_RULES.md`, `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`, campaign `probability_campaign_2026_09/INDEX.md` and `RANKING.md`, root `POSTED.md` and `RESULTS.md`, the canonical P0456 claim, the full newest P03 report at its exact blob, current P26 evidence, and the current P04 directory. Large connector-rendered policy/root surfaces (`FLEET_RULES`, owner directive, `POSTED`, `RESULTS`) are truncated by the connector and are not represented here as byte-for-byte rereads; the exact mathematical dependencies below were recovered by exact path/blob reads.

### Fresh outside-audit screen

A new P26 report has appeared since the preceding P03 run:

`proofnet24/P26-proof-audit-recovery/runs/2026-09-19/2026-09-19_03-01-45__run-report.md`,

blob `a0977f328d9845b41217f82639dde1e2e334329a` on current `master`.

It independently audits **P04/I0101 Claim 12**, proves a stronger all-`t` alternating-projection convergence statement, and reconciles that P04 package. It does **not** audit P0456. Repository-wide searches for `P0456`, `PASS`, and audit terminology still recover no P26 or distinct OTHER-track full-chain P0456 audit. P04 has no `2026-09-19` run directory; its newest known terminal state remains the 2026-09-18 rotation-stop/readback sequence, with no new theorem for the directed P03->P04 duty.

Therefore the closure gate is unchanged:

`P0456_ACTIVE_AUDIT_PENDING / OUTSIDE_AUDITS_FOUND_0_OF_2`.

Self-audits never count. No source-closure label and no final paper package are created.

### Fresh primary-source / current-literature verification

The primary source remains Hossein Dabirian and Vijay Subramanian, *Connectivity of a family of bilateral preference random graphs*, *Journal of Applied Probability* 63(2) (June 2026), 552--579, DOI `10.1017/jpr.2025.10051`, published online 18 December 2025.

Fresh Cambridge HTML retrieval on 19 September 2026 again verifies the literal bilateral-preference model and Section 1.1's open band

`log n - 0.5 loglog n sqrt(log n) <= k <= log n + 0.5 loglog n sqrt(log n)`.

The source explicitly says connectivity in that band is not known and attributes the gap to analytically simpler sufficient conditions. Fresh reads also reverified Lemmas 10--14, including the source `O(k^3/n)` bad-interaction bound and pair conditional-independence mechanism, plus Theorem 3 (lower/disconnection side) and Theorem 6 (upper/connectivity side).

Fresh bounded searches for the exact title/DOI, `LK(n,k) Poisson isolated vertices`, bilateral-preference Poisson/connectivity updates, author updates, and the composite constant below found the Cambridge article and its earlier arXiv version but no later source-matching Poisson/critical-window/second-correction theorem. This is bounded dated negative evidence only; **publication novelty remains UNVERIFIED**.

---

## 2. Preserved chain and new claim

The source-matching chain remains:

- `P03-P0456-POISSON-CRITICAL-WINDOW-288 = PROVED / SOURCE-MATCHING-CANDIDATE-COMPLETE / AUDITS-PENDING / PUBLICATION-NOVELTY-UNVERIFIED`;
- `P03-P0456-UNIFORM-POISSON-INTERACTION-REPAIR-289 = PROVED / SELF-AUDIT-REPAIR / SOURCE-MATCHING-STRENGTHENING / AUDITS-PENDING / PUBLICATION-NOVELTY-UNVERIFIED`;
- Claim 290: marked isolated-vertex PPP;
- Claims 291--299: supporting P03 self-audit/strengthening kernels.

This run adds:

### Claim `P03-P0456-BIVARIATE-RARE-EVENT-CROSSCHECK-300`

**Status:** `PROVED / SELF-AUDIT-STRENGTHENING / SUPPORTING / AUDITS-PENDING / PUBLICATION-NOVELTY-UNVERIFIED`.

Let independently

`Y ~ Gamma(k,1)`, `W ~ Gamma(k+1,1)`,

and retain Claim 299's one-defect auxiliary term

`A_k := E[(k/W)(Y-k-W)_+]`.                                  (2.1)

Then exactly

`A_k
 = e^{-k}/Gamma(k)^2
   int_0^infinity int_0^infinity
   r w^(k-1)(k+w+r)^(k-1)e^{-2w-r} dr dw`.                   (2.2)

Put

`eta=sqrt(2)-1-log((1+sqrt(2))/2)`,

`C_*=(1+sqrt(2))/sqrt(2*pi*(2-sqrt(2)))`,

`a_1=-(332+235 sqrt(2))/96`.                                 (2.3)

A direct **two-coordinate boundary-saddle calculation** applied to (2.2), not the one-dimensional Watson/Laplace calculation of Claim 299, gives

`A_k
 = C_* k^(-1/2)e^{-eta k}
   {1+a_1/k+O(k^-2)}.`                                       (2.4)

Thus the leading prefactor and the full `1/k` coefficient in Claim 299 survive an independent local derivation. Claim 299 is **not downgraded**.

Moreover (2.2) has the exact finite expansion

`A_k=e^{-k} B_k^(2D)`,                                       (2.5)

where

`B_k^(2D)
 = sum_{b,c>=0; b+c<=k-1}
   (c+1)(k+b-1)! k^(k-1-b-c)
   /[(k-1)!(k-1-b-c)! b! 2^(k+b)].`                          (2.6)

This is an exact second evaluation of the same auxiliary correction and agrees identically with Claim 298's incomplete-gamma finite representation because both are derived exactly from (2.1) by different integration orders/expansions.

Claim 300 is a self-audit kernel only. It creates no new source-closure status and no new fixed-coefficient metric.

---

## 3. #1 CHANGE THE CATEGORY — from marked graph integral to a bivariate Poisson-arrival wedge

Claim 299's correction was presented as a one-dimensional marked saddle after integrating out the Gamma overshoot. Instead keep both Gamma coordinates visible.

The Gamma variables have the arrival-time interpretation

`Y = T_k^(1)`, `W = T_(k+1)^(2)`

for two independent rate-one Poisson processes. Also

`(Y-k-W)_+ = int_0^infinity 1{Y>k+W+r} dr`.                  (3.1)

Using the two Gamma densities and `Gamma(k+1)=k Gamma(k)`, the factor `k/W` cancels one power of `W`, giving exactly

`A_k
 = 1/Gamma(k)^2
   int_{w>0} int_{y>k+w}
   (y-k-w) y^(k-1)w^(k-1)e^{-(y+w)} dy dw`.                  (3.2)

Set `r=y-k-w`. This is (2.2).

At exponential scale write

`u=y/k`, `t=w/k`.

The rare-event region is the wedge

`u >= 1+t`.                                                   (3.3)

The independent Gamma Cramer rate is

`I(s)=s-1-log s`, `s>0`,                                     (3.4)

so the joint rate is

`J(u,t)=I(u)+I(t)`.                                           (3.5)

The constrained minimum lies on `u=1+t`; hence it reduces to

`F(t)=I(1+t)+I(t)
     =2t-1-log(t(1+t))`.                                     (3.6)

The Lagrange equations are

`I'(u)=Lambda`, `I'(t)=-Lambda`, `u=1+t`,                    (3.7)

or equivalently

`2-1/t-1/(1+t)=0`.                                            (3.8)

The unique solution is

`t_*=1/sqrt(2)`, `u_*=1+1/sqrt(2)`,                          (3.9)

with

`J(u_*,t_*)=eta`.                                             (3.10)

This changes the conceptual category: the correction is a weighted occupation of a **two-process rare-event wedge**, not merely an error term in a one-dimensional beta integral. The saddle `1/sqrt(2)` is the balance point between the two independent Gamma deviations.

---

## 4. #7 TAKE THE LIMIT — direct boundary Gaussian/exponential determinant

Now derive the prefactor in the two-dimensional picture.

Set `w=kt` and retain the normal overshoot `r=y-k-w` unscaled. Equation (2.2) becomes

`A_k
 = e^{-k} k^(2k-1)/Gamma(k)^2
   int_0^infinity int_0^infinity
   r t^(k-1)(1+t+r/k)^(k-1)e^{-2kt-r} dr dt`.                (4.1)

Stirling gives

`e^{-k} k^(2k-1)/Gamma(k)^2
 = e^k/(2pi){1-1/(6k)+O(k^-2)}.`                             (4.2)

Write

`q(t)=t/(1+t)`.                                               (4.3)

Uniformly for `t` in a fixed neighborhood of `t_*`, expansion of the exact integrand gives

`A_k
 = int int h(t,r)e^{-kF(t)}
   {1+c(t,r)/k+O((1+r^4)/k^2)} dr dt
   +O(e^{-(eta+rho)k})`,                                     (4.4)

for some fixed `rho>0`, where

`h(t,r)= r/[2pi t(1+t)] * e^{-q(t)r}`,                       (4.5)

`c(t,r)= -1/6-r/(1+t)-r^2/[2(1+t)^2]`.                      (4.6)

The remainder is uniform after splitting the exponentially small large-`r` tail; on the local region all Gamma/exponential moments are finite uniformly. Thus (4.4) is a direct two-coordinate expansion and does not import Claim 299's Watson boundary formula.

The constrained tangent direction to `u=1+t` is `(1,1)`. Since the Hessian of `J` is diagonal,

`H_J=diag(1/u^2,1/t^2)`,                                     (4.7)

the tangent quadratic curvature is

`(1,1) H_J(u_*,t_*) (1,1)^T
 =1/u_*^2+1/t_*^2
 =F''(t_*)
 =8-4sqrt(2).`                                                (4.8)

The normal overshoot has rate

`q_*=q(t_*)=sqrt(2)-1`.                                      (4.9)

Hence the local limiting product law has

- tangent fluctuation `X=sqrt(k)(t-t_*)` Gaussian with variance `1/F''(t_*)`;
- normal overshoot `R` with density proportional to `r e^{-q_*r}`, i.e. `Gamma(2,q_*)`.

The leading determinant is therefore

`[1/(2pi t_*(1+t_*))]
 * int_0^infinity r e^{-q_*r}dr
 * sqrt(2pi/F''(t_*))`                                       (4.10)

`= [1/(2pi t_*(1+t_*)q_*^2)]
   sqrt(2pi/F''(t_*))`                                       (4.11)

`= (1+sqrt(2))/sqrt(2pi(2-sqrt(2)))
 = C_*.`                                                      (4.12)

Thus the two-dimensional constrained saddle independently recovers both the exponent `eta` and Claim 298's prefactor `C_*`.

---

## 5. Direct bivariate recovery of the `1/k` coefficient

This is the main adversarial audit of Claim 299's sign/convention.

Let

`ell_1(t,r)=partial_t log h(t,r)
 = -1/t-1/(1+t)-r/(1+t)^2`.                                 (5.1)

At the saddle, under the normalized normal law

`R ~ Gamma(2,q_*)`,                                           (5.2)

we have

`E R=2/q_*`, `E R^2=6/q_*^2`.                               (5.3)

Direct differentiation and these moments give

`E[ell_1(t_*,R)] = 2-4sqrt(2)`,                              (5.4)

`E[h_tt(t_*,R)/h(t_*,R)] = 36-12sqrt(2)`,                    (5.5)

and from (4.6)

`E[c(t_*,R)] = -37/6-2sqrt(2)`.                              (5.6)

Also

`F_2:=F''(t_*)=8-4sqrt(2)`,

`F_3:=F'''(t_*)=-40+24sqrt(2)`,

`F_4:=F''''(t_*)=432-288sqrt(2)`.                            (5.7)

Under the normalized tangent Gaussian,

`E X^2=1/F_2`, `E X^4=3/F_2^2`, `E X^6=15/F_2^3`.           (5.8)

Expand (4.4) at `t=t_*+X/sqrt(k)`. Odd order `k^-1/2` terms integrate to zero. The relative `1/k` coefficient is the sum of five transparent bivariate contributions:

`a_1
 = E[c]
 + (1/2)E[h_tt/h] E[X^2]
 - (F_3/6)E[ell_1] E[X^4]
 - (F_4/24)E[X^4]
 + (F_3^2/72)E[X^6].`                                       (5.9)

Substitution of (5.4)--(5.8) yields exactly

`a_1
 = -83/24 - 235sqrt(2)/96
 = -(332+235sqrt(2))/96`.                                    (5.10)

This is Claim 299's coefficient, recovered without using its one-dimensional Laplace correction formula (5.16). In particular, the sign/convention of the old `L_1` term is independently validated.

Because `F` is analytic with a unique interior minimizer in `t`, the local `r` law has a uniform exponential moment, and the complement of the saddle neighborhood has a fixed rate gap, the standard Taylor/dominated-convergence bookkeeping in (4.4) continues one further order and gives the relative remainder `O(k^-2)` in the auxiliary Gamma model. Thus the previously flagged `O(k^-2)` Watson-expansion concern is bypassed and independently resolved at the level actually needed for `A_k`.

---

## 6. #25 COUNT THE SAME THING TWICE — exact finite identities

There are now two exact finite evaluations of `A_k` before asymptotics.

### 6.1 New two-dimensional polynomial expansion

Expand

`(k+w+r)^(k-1)
 = sum_{a+b+c=k-1}
   (k-1)!/(a!b!c!) k^a w^b r^c`.                             (6.1)

In (2.2), integrate termwise:

`int_0^infinity w^(k+b-1)e^{-2w}dw
 = (k+b-1)!/2^(k+b)`,                                        (6.2)

`int_0^infinity r^(c+1)e^{-r}dr
 = (c+1)!`.                                                   (6.3)

Since `a=k-1-b-c`, this gives exactly (2.5)--(2.6).

### 6.2 Claim 298's incomplete-gamma evaluation

Claim 298 independently evaluated the same expectation by first integrating the `Y` tail, obtaining

`A_k=e^{-k}B_k^(IG)`,                                        (6.4)

where

`B_k^(IG)
 =(k/k!)[
  1/(k-1)! sum_{ell=0}^k
  C(k,ell) k^(k-ell)(k+ell-1)!/2^(k+ell)
  -sum_{j=0}^{k-1} 1/j! sum_{ell=0}^j
   C(j,ell) k^(j-ell)(k+ell)!/2^(k+ell+1)]`.                 (6.5)

Equations (6.1)--(6.3) and the incomplete-gamma derivation are algebraically independent exact evaluations of the same positive double integral, so

`B_k^(2D)=B_k^(IG)`                                           (6.6)

for every integer `k>=1`. No floating-point assertion enters (6.6).

### 6.3 Relation to Claim 299's full finite beta coefficient formula

Claim 299 additionally proved the exact finite-`n` identity

`int_0^1 Q_k(x)^k(1-x)^(m-k-1)dx
 =(N+1)^(-k) sum_J a_J B(J+1,kN+m-J)`,                        (6.7)

with `[y^J]P_Nk(y)^k=a_J` and

`P_Nk(y)=sum_{j=k+1}^{N+1}(j-k)C(N+1,j)y^j`.

The coefficient representation (6.7) contains the complete beta model, whereas (6.4)/(6.6) is the critical-saddle one-defect Gamma limit. Claim 299's beta-to-Gamma transfer is uniform on the saddle neighborhood with relative error `O(poly(k)/n)=o(1/k)` at `k=log n+O(1)`. Therefore the exact finite beta representation cannot alter either `C_*` or `a_1`; its first-defect local limit is exactly the doubly-counted quantity above.

A negative result is worth stating plainly: direct steepest-descent extraction of `a_1` from the high-degree coefficient sum (6.7), without passing through its local Gamma scaling, remains less transparent than the bivariate saddle. Thus #25 gives an exact finite algebraic cross-check plus an independent asymptotic bivariate derivation, but not a third wholly separate coefficient-sum saddle calculation. There is no disagreement and hence no reason to downgrade Claim 299.

No new checker was manufactured: Claim 298 already archived an exact checker for (6.5), and Claim 299 archived an exact checker for (6.7). The new equality (6.6) is proved symbolically by two exact evaluations of (2.1), rather than asserted from finite numerical cases.

---

## 7. Adversarial audit of Claim 299's named weak points

### 7.1 Uniform second-order Watson expansion

The bivariate representation eliminates reliance on the one-dimensional Watson formula. The local expansion (4.4) is uniform because near `t_*`, `q(t)` is bounded away from zero and the normal variable has exponential tails. Taylor remainders are dominated by polynomial moments times an exponential. The nonlocal `t` region has fixed large-deviation gap. This independently reproduces `a_1` and supplies a relative `O(k^-2)` remainder for `A_k`.

### 7.2 Sign/convention of Claim 299's `L_1`

Resolved independently by (5.9)--(5.10). The same exact `a_1<0` emerges from the two-coordinate Gaussian/exponential expansion.

### 7.3 `o(1/k)` beta-to-Gamma transfer

Claim 299's local beta log-density error is `O(poly(k)/n)` on the fixed saddle neighborhood. With `k=log n+O(1)`, this is `o(1/k)`. The new bivariate derivation does not introduce any larger finite-`n` term. No gap found.

### 7.4 Component bounds at the `eps_n/k` scale

The Claim-299 decomposition remains valid under the literal bilateral-preference model: envelope failure `n^{-0.402585...+o(1)}`, sizes `2--12` at `n^{-1+o(1)}`, sizes `13--24` at worst `n^{-0.3+o(1)`, and sizes `>=25` totaling `n^{-0.25+o(1)`. Since

`eps_n/k=n^{-eta+o(1)}/(log n)^(3/2)`, `eta=0.225987...<0.25`,

every listed component contribution is `o(eps_n/k)`. No mean-degree inference is used.

### 7.5 Connectivity inference

The Palm/size-bias error is `n^{-1+o(1)}=o(eps_n/k)`. Claim 299's expansion of `e^{-mu_n}` is safe because `eps_n^2=o(eps_n/k)`. The event “disconnected with no isolated vertex” is contained in the nontrivial-component event above. Thus the second-correction connectivity inference survives this audit.

No contradiction to Claims 288, 289, 298, or 299 was found.

---

## 8. Source/prior-art record and novelty boundary

Fresh Cambridge retrieval on 19 September 2026 confirms:

- Section 1.1 still states the coefficient-`1/2` window as unresolved and says more exact sufficient conditions may close it;
- Lemma 10 gives the source `O(k^3/n)` bad-interaction bound;
- Lemmas 11--14 provide the source pair-isolation conditioning/second-moment chain;
- Theorem 3 gives the lower/disconnection result;
- Theorem 6 gives the upper/connectivity result.

The rate `I(s)=s-1-log s` is classical Gamma/Cramer/incomplete-gamma large-deviation machinery. Claim 300 identifies the P0456 correction as a boundary contraction of two such rates and makes the Poisson-arrival geometry explicit. Fresh bounded searches did not identify the composite constant

`min_t{I(t)+I(1+t)}`

or the corresponding P0456 correction theorem as a named current result. This absence is not a novelty certificate. **Publication novelty remains UNVERIFIED.**

---

## 9. Directed P03->P04 duty, metrics, and recovery state

The current P04 repository has no 2026-09-19 run directory and the newest recovered state remains rotation-stop/readback material. No genuinely new P04 successor theorem exists to audit, so I do not fabricate or recycle an audit.

All admitted P0456 coefficient metrics remain mathematically saturated:

- `c_LK^cert=0`;
- `a_LK^fine=0`;
- `b_LK^sqrt=0`.

They do not count as stuck/unchanged runs. HARD recoveries remain `0/2`. Claim 300 is an audit refinement, not a new fixed-coefficient metric.

---

## 10. Exact remaining obligations and next attack

Protocol closure remains blocked by independent outside audits and publication-novelty verification, not by lack of a candidate theorem.

Exact remaining obligations:

1. P26 must independently audit the full Claims 288/289 source-matching chain; Claims 291--300 are optional audit kernels, not outside receipts.
2. One distinct OTHER track must independently audit the same full implication chain.
3. Publication novelty remains UNVERIFIED; every current search miss is bounded negative evidence only.
4. Claim 299's two most delicate asymptotic constants now have an independent bivariate derivation. The remaining outside-audit emphasis should move to the all-fixed-root interaction theorem and the quantitative component decomposition, not spend another run recomputing `a_1`.
5. No final paper package until the two outside audits pass.

If no audit arrives next run, do **not** compute another formal `1/k` coefficient. A better next target is an outside-auditor-sized self-contained proof capsule for Claims 288/289 that minimizes dependencies: exact one-root marked integral, explicit fixed-`r` interaction graph, size-bias cross-check, and literal component elimination. Fresh methods should be chosen from Section B and must differ from #1/#7/#25.

---

## 11. `ledger_delta` for P26 only

```yaml
ledger_delta:
  track: P03
  target: P0456
  action: preserve_active_audit_pending
  metric:
    c_LK_cert: 0
    a_LK_fine: 0
    b_LK_sqrt: 0
    saturated: true
    unchanged_count_increment: 0
    recoveries_used: 0/2
  new_claim:
    id: P03-P0456-BIVARIATE-RARE-EVENT-CROSSCHECK-300
    status: PROVED / SELF-AUDIT-STRENGTHENING / SUPPORTING / AUDITS-PENDING / PUBLICATION-NOVELTY-UNVERIFIED
    statement: >-
      For A_k=E[(k/W)(Y-k-W)_+] with independent
      Y~Gamma(k,1), W~Gamma(k+1,1), there is the exact bivariate
      boundary-integral representation (2.2). A direct constrained
      two-coordinate saddle at (u_*,t_*)=(1+1/sqrt(2),1/sqrt(2))
      gives A_k=C_* k^-1/2 exp(-eta k){1+a_1/k+O(k^-2)},
      independently recovering Claim 299's C_* and
      a_1=-(332+235 sqrt(2))/96.
  exact_identity:
    statement: >-
      A_k=e^-k B_k^(2D), where B_k^(2D) is the finite double sum
      in (2.6); this equals Claim 298's exact incomplete-gamma
      representation because both are exact evaluations of A_k.
  preserved_claims:
    - P03-P0456-POISSON-CRITICAL-WINDOW-288
    - P03-P0456-UNIFORM-POISSON-INTERACTION-REPAIR-289
    - P03-P0456-MARKED-POISSON-CROSSCHECK-290
    - P03-P0456-PAIR-SMALLCOMP-AUDIT-KERNEL-291
    - P03-P0456-FINITE-PALM-INTERACTION-GRAPH-292
    - P03-P0456-LOCALBLOCK-SIZEBIAS-STEIN-293
    - P03-P0456-RANK-PALM-SUBLINEAR-WINDOW-294
    - P03-P0456-FIXED-FRACTION-POISSON-BAND-295
    - P03-P0456-OPTIMIZED-SADDLE-FRACTION-BAND-296
    - P03-P0456-DIRECT-TILT-ASYMMETRIC-POISSON-297
    - P03-P0456-FIRST-CORRECTION-LAPLACE-298
    - P03-P0456-SECOND-CORRECTION-FINITE-REDUCTION-299
  audit_gate:
    independent_passes_found: 0/2
    newest_p26_report: proofnet24/P26-proof-audit-recovery/runs/2026-09-19/2026-09-19_03-01-45__run-report.md
    newest_p26_target: P04/I0101 Claim 12, not P0456
    source_closed: false
  publication_novelty: UNVERIFIED
  next_state: P0456_ACTIVE_AUDIT_PENDING / CLAIM_300_BIVARIATE_CROSSCHECK_READY
```

**End of complete run report.**