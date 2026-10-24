Model actually run: GPT-5.6 Sol. Reasoning level: UNVERIFIED. This is not GPT-6 at maximum.

# P03 / D0043 — HARD recovery 1: frozen lattice Green kernel at the first exotic edge

**NO MOVEMENT: `k_exotic^cert: 0 -> 0`; D0043 consecutive unchanged count `3 -> 4`; HARD recovery episodes consumed `0/2 -> 1/2`.**

Methods used exactly as assigned: **B30 DO ONE PRIME / ONE SCALE / ONE DIRECTION AT A TIME; B11 DUALIZE; B7 TAKE THE LIMIT.**

Source target: Bálint Virág, *Operator limits of random matrices* (ICM 2014), Conjecture 5, with the precise nonregular-edge formulation in Krishnapur--Rider--Virág (KRV), Section 13 / Conjecture 45. The source asks for general-fixed-`beta` operator convergence at an analytic edge with density exponent `2k+1/2`, not merely beta=2 eigenvalue limits.

Status after this run: **PARTIAL / source still open on the bounded 2026-09-18 screen**. No claim of worldwide openness or publication novelty is made.

---

## 1. Continuity, ownership, and source/status gate

I continued from the newest complete P03 report

`proofnet24/P03-fei/runs/2026-09-18/2026-09-18T02-52-30Z__d0043-k1-critical-hessian-stuck.md`

creation commit `38e29fcec14c98d937ca2a5992840ab3301d67ec`, blob `7667a5d9866543206a3c65ab84ddc74eaacc667b`, whose exact-commit readback had recovered `**End of complete run report.**`.

The active create-only ownership file remains

`operations/claims/D0043.md`

creation commit `7578fb6bc235056f9d5b9f820d3087af9cc18c48`, blob `fa41e947fd62de7b036ea1a9a9e31c2642e1d18b`.

Before new mathematics I reread/recovered the root `README.md`, `proofnet24/HOURLY_PROTOCOL_2026-09-15.md`, current `FLEET_RULES.md`, `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`, `operations/FLEET_2026-09-16.md`, campaign `INDEX.md` and `RANKING.md`, root `POSTED.md`, current `RESULTS.md` and `QUEUE.md`, the D0043 claim, newest own report, and the D0043 attempt history including `D0043-A001`. Large root ledgers and intake surfaces are connector-truncated when requested wholesale; I recovered the exact current D0043 and relevant neighboring/history entries and do not claim a byte-for-byte manual rendering of every row.

Repository prior art is preserved rather than repaid:

- `D0043-A001` checked the formal exotic scaling balance and flagged the singular origin coefficient.
- `P03-D0043-ORIGIN-NOISE-SUBCRITICALITY-264` removed the origin-local continuum-form obstruction.
- `P03-D0043-GLOBAL-FORM-COMPACT-RESOLVENT-266` constructed the continuum exotic operator by forms, with compact resolvent, for every finite `k>=1`.
- `P03-D0043-K1-CRITICAL-HESSIAN-GATE-268` constructed the explicit source-admissible quartic below, found the `s^{-2/3}` local susceptibility, and proved that a uniform regular-edge covariance estimate cannot produce the exotic noise.

Fresh source checks on 2026-09-18:

1. Virág, arXiv:1804.06953 / ICM 2014, still states Conjecture 5 under the heading **Exotic edge operators**, and immediately distinguishes the beta=2 Riemann--Hilbert eigenvalue literature from the conjectured general-beta operator limit.
2. KRV, arXiv:1306.4832, Section 13, still states Conjecture 45 with `m_n ~ n^(1/(4k+3))` and the operator `S_{beta,k}`. The same section explicitly says their regular proof made essential use of uniform convexity and only supplies a conjectural framework for nonregular `V`.
3. Li--Valkó--Xu, arXiv:2607.08536 (2026-07-09), proves further ordinary Airy-beta soft-edge/operator limits for Laguerre beta ensembles; it is not a multicritical `k>=1` theorem.
4. A bounded current arXiv/web search did not recover a source-matching general-beta proof for exotic `k>=1`. This is a dated bounded search miss, not evidence that no such result exists worldwide.

PDF inspection note: the Virág PDF page containing Conjecture 5 was visually inspected successfully. The KRV Section-13 PDF text was recovered at exact page/line ranges, but the screenshot backend returned a cache miss for the relevant KRV pages; I therefore do not describe that failed screenshot as a visual readback.

---

## 2. Frozen metric and recovery state

Frozen metric:

`k_exotic^cert = largest K>=0 for which a source-matching rigorous operator-convergence theorem is known for every 0<=k<=K and every fixed beta>0 in the source setup.`

Before: `0`.
After: `0`.
Movement: **none**.

The `k=0` baseline is ordinary stochastic-Airy soft-edge convergence. A lattice-Hessian theorem for one explicit `k=1` potential is PARTIAL and does not move this metric.

The previous report was the formal three-unchanged HARD stuck trigger. This invocation executes its selected **recovery 1/2**. Since the metric remains zero, recovery 1 is now consumed. There is at most one further D0043 recovery before mandatory immutable handoff/rotation on another unchanged final-recovery run.

---

## 3. Recovery idea before calculation

The regular KRV proof says why its local-equilibrium algorithm works: the coefficients vary on scale `n`, the field mixes exponentially in logarithmically many sites, and blocks can be replaced by a nearly stationary Gaussian law before proving a functional CLT. The preceding D0043 report already proved that the constant Fourier mode loses its uniform spectral gap at the explicit `k=1` edge.

The recovery question is therefore sharper than another covariance estimate:

> **Does the full frozen lattice Hessian have a correlation length much smaller than the exotic edge window `m_n=n^(1/7)`, so a nonuniform local-equilibrium proof might still survive?**

I tried to refute that hope before attempting any CLT. The answer is no: the full soft symbol is quartic, its correlation length is exactly of order `u^{-1/2}`, and on the source edge window this is order `m_n` itself. Thus there is no mesoscopic local-stationarity scale inside the `k=1` window.

No checker was written. The new result is an analytic full-lattice theorem, not a finite enumeration, so the protocol's exact-artifact requirement is not triggered.

---

## 4. Explicit `k=1` source-admissible potential retained from Claim 268

Fix

`V_*(x) = (2/5)x^4 - (16/15)x^3 + (2/5)x^2 + (8/5)x.`

Claim 268 proved that its equilibrium density is

`rho_*(x) = (8/(5 pi)) (1-x)^2 sqrt(1-x^2) 1_{[-1,1]}(x),`

so the right edge has exponent `5/2 = 2*1 + 1/2` and is a genuine one-sided `k=1` exotic edge.

For the KRV frozen local Hamiltonian

`H_s = tr V_*(C) - (1-s) sum_j log b_j,`

write the right and left endpoint deficits of its constant minimizer as

`a+2b = 1-u`,
`a-2b = -1+v`.

The exact local critical equations from Claim 268 give

`v(u) = (5/32)u^3 - (5/128)u^4 + O(u^5),`

`s(u) = u^3 - (7/16)u^4 + O(u^5),`

and hence

`a(u)=(v-u)/2`, `b(u)=(2-u-v)/4`, `1-s=1-u^3+O(u^4)`.

In particular `u=s^(1/3)+O(s^(2/3))`.

---

## 5. B30 — exact full frozen lattice Hessian symbol

### Claim `P03-D0043-K1-FROZEN-GREEN-CRITICAL-WINDOW-270`

**Status: PROVED / STRUCTURAL-PARTIAL / SOURCE-ADMISSIBLE-EXAMPLE / PUBLICATION-NOVELTY-UNVERIFIED.**

Let `M_u(theta)` be the `2 x 2` Fourier symbol of the full bi-infinite frozen Hessian of the KRV Hamiltonian at the constant branch `(a(u),b(u))`. Put `c=1-s` and, before specializing to the branch, write

`M = [[A,C],[conj(C),B]]`, where

`A(theta) = (24/5)a^2 - (32/5)a + (32/5)b^2 + 4/5 + (16/5)b^2 cos(theta),`

`B(theta) = (48a^2 - 64a + 80b^2 + 8)/5 + c/b^2 + (64/5)b^2 cos(theta),`

`C(theta) = (16/5)b(3a-2)(1+exp(-i theta)).`

Then, with

`y = 1-cos(theta)`, `q=(1,2)^T`,

as `(u,y)->(0,0)` one has

`det M_u(theta) = (384/5)u^2 + (128/5)u y + (64/25)y^2 + O((u+y)^3),`

`tr M_u(theta) = 16 + 4u - 4y + O((u+y)^2),`

and

`q^* adj(M_u(theta)) q = 256/5 + O(u+y).`

Consequently the soft eigenvalue satisfies

`lambda_-(u,theta)
 = (24/5)u^2 + (8/5)u y + (4/25)y^2 + O((u+y)^3)`

and, in the critical Fourier scaling `theta=sqrt(u) xi`,

`lambda_-(u,sqrt(u)xi)
 = (u^2/25)(xi^4 + 20 xi^2 + 120) + o(u^2)`

locally uniformly in `xi`.

Equivalently, the soft dispersion is **quartic**:

`25 lambda_- = theta^4 + 20u theta^2 + 120u^2 + lower-order terms`

on the critical scale. There is no nonzero fixed `theta^2` stiffness at `u=0`; the quadratic stiffness itself collapses like `u`.

### Proof of the symbol

For a periodic Jacobi matrix `T=T(a_j,b_j)`, the identities

`tr T^2 = sum_j a_j^2 + 2 sum_j b_j^2`,

`tr T^3 = sum_j a_j^3 + 3 sum_j b_j^2(a_j+a_{j+1})`,

and, because `tr T^4 = ||T^2||_F^2`,

`tr T^4
 = sum_j (a_j^2+b_{j-1}^2+b_j^2)^2
 + 2 sum_j b_j^2(a_j+a_{j+1})^2
 + 2 sum_j b_j^2 b_{j+1}^2`

are exact. Substitute

`tr V_*(T) = (2/5)tr T^4 -(16/15)tr T^3 +(2/5)tr T^2 +(8/5)tr T`

and add the logarithmic Hessian from `-(1-s) sum log b_j`. Differentiating twice at the constant configuration and inserting a Fourier perturbation proportional to `exp(i j theta)` gives exactly the displayed `A,B,C`. At `theta=0` this symbol reduces to the `2 x 2` local Hessian used in Claim 268, providing an independent normalization check.

Now substitute

`a=(v-u)/2`, `b=(2-u-v)/4`, `c=1-s`

and the branch series for `v(u),s(u)`. Direct Taylor expansion gives the three displayed expansions. Since the hard eigenvalue tends to `16`, dividing the determinant by the hard eigenvalue yields the soft-eigenvalue expansion. Finally `1-cos(theta)=theta^2/2+O(theta^4)` gives the quartic scaled polynomial. QED.

---

## 6. B11 — dualize: the projected Green kernel has an exact critical limit

Define the projected frozen Green symbol

`Q_u(theta)=q^* M_u(theta)^(-1) q`

and its lattice kernel

`g_u(h)=(1/(2 pi)) int_{-pi}^{pi} exp(i h theta) Q_u(theta) dtheta.`

The adjugate formula and Claim 270 imply

`u^2 Q_u(sqrt(u) xi) -> 80/(xi^4+20xi^2+120)`

locally uniformly in `xi`.

For sufficiently small positive `u`, the only critical zero of the limiting `u=0` symbol is at `theta=0`. From the determinant expansion there are constants `c,C,delta>0` such that for `|theta|<=delta`,

`det M_u(theta) >= c (u^2 + u theta^2 + theta^4)`

while away from that neighborhood the determinant stays uniformly positive. The numerator `q^*adj(M)q` stays bounded. Hence after the substitution `theta=sqrt(u)xi`, the integrand is dominated by `C/(1+xi^2+xi^4)`. Dominated convergence therefore gives, for every fixed real `t`,

`u^(3/2) g_u(floor(t/sqrt(u))) -> K(t),`

where

`K(t)= (80/(2 pi)) int_R exp(i t xi)/(xi^4+20xi^2+120) dxi.`

This integral can be evaluated exactly. Set

`a_* = sqrt(sqrt(30)-5)`,
`b_* = sqrt(sqrt(30)+5)`.

Since `(b_* - i a_*)^2 = 10-2i sqrt(5)` and the conjugate factor gives the other quadratic root, residues yield

`K(t) = (2/sqrt(6)) exp(-b_* |t|)
        [ b_* sin(a_* |t|) + a_* cos(a_* |t|) ].`

Thus the projected frozen field has critical correlation scale

`|h| ~ u^(-1/2)`.

More precisely, after measuring distance in units `u^(-1/2)`, its limiting Green kernel has exponential envelope `exp(-b_* |t|)` with `b_*=sqrt(sqrt(30)+5)`.

This is the full-lattice answer; the previous report's constant-mode susceptibility `q^T H_s^(-1)q ~ (2/3)u^(-2)` is recovered as the zero-frequency value `Q_u(0)`, but it is not the pointwise lattice variance. The latter is an integral over all Fourier modes and scales like `u^(-3/2)`.

---

## 7. B7 — take the source critical limit: the correlation length is the whole edge window

For `k=1`, KRV predicts

`m_n ~ n^(1/7)`.

Write `m=m_n` and use `n=m^7` at the exponent level. At edge index

`j = x m`, with fixed `x>0`,

we have

`s=j/n = x m^(-6)`

and therefore

`u=s^(1/3)+O(s^(2/3)) = x^(1/3)m^(-2)+O(m^(-4)).`

The frozen correlation length in lattice sites is consequently

`u^(-1/2) = x^(-1/6)m (1+o(1)).`

Including the exponential constant from `K`, the Green-kernel envelope length is

`xi_corr(j) = [b_* x^(1/6)]^(-1) m (1+o(1)).`

So for every fixed macroscopic edge coordinate `x`, the frozen correlation length is **Theta(m_n)**, not `o(m_n)`.

The source's desired cutoff regime is `q_n=o(m_n)`. At such a cutoff,

`xi_corr(q_n)/m_n ~ (1/b_*) (m_n/q_n)^(1/6) -> infinity.`

There is therefore no choice of blocks satisfying simultaneously

`correlation length << block length << m_n`

uniformly from an admissible `q_n=o(m_n)` through a fixed positive fraction of the exotic edge window.

There is an equivalent adiabatic diagnostic. Since

`u(j)=(j/n)^(1/3)`, one has `u'(j)/u(j)=1/(3j)`. Over one correlation length at `j=xm`,

`Delta u / u ~ xi_corr(j)/(3j) = Theta(1)`.

Thus the local parameter itself changes by an order-one fraction across a single correlation length. The time-inhomogeneity cannot be frozen before mixing occurs.

This is exactly the regular-edge mechanism that fails: Virág's proof outline says the regular chain coefficients change on scale `n` while the chain mixes exponentially fast in logarithmically many sites. In this explicit exotic model, at source scaling, the correlation/mixing scale and the entire edge-window scale coincide.

---

## 8. The frozen Gaussian limit is colored, not Brownian

The preceding result can be stated as a clean Gaussian limit for the quadratic approximation, without claiming that the true nonlinear tridiagonal field is Gaussian.

Fix `r>0`. Let `u=r m^(-2)` and `n=m^7`, and let the stationary Gaussian quadratic field be defined by density proportional to

`exp[-(n beta/2) <delta, H_u delta>]`,

where `H_u` is the frozen full-lattice Hessian above. For the edge-direction fluctuation

`eta_j = delta a_j + 2 delta b_j`,

its covariance is `(n beta)^(-1) g_u(i-j)`.

Then the rescaled Gaussian field

`Z_m(t)=m^2 eta_floor(mt)`

has finite-dimensional distributions converging to a centered stationary Gaussian field with covariance

`Cov(Z(t),Z(t')) = beta^(-1) K_r(t-t')`,

where

`K_r(t)= (80/(2 pi)) int_R exp(i t xi)/(xi^4+20r xi^2+120r^2) dxi
       = r^(-3/2) K(sqrt(r)t).`

This follows immediately from the Green-kernel scaling; Gaussianity converts covariance convergence into finite-dimensional convergence.

Likewise, the frozen integrated process

`Y_m(L)=m sum_{j=1}^{floor(mL)} eta_j`

has limiting covariance

`beta^(-1) int_0^L int_0^{L'} K_r(t-s) dt ds.`

That covariance is not Brownian: its mixed second derivative is the continuous nonzero kernel `K_r(t-s)`, not a delta distribution.

**Interpretation / scope warning.** This does **not** refute KRV Conjecture 45 or Virág Conjecture 5. It refutes the specific proof idea of approximating the whole exotic edge window by rapidly mixing stationary Gaussian patches. The true field is nonhomogeneous on exactly the same scale as its correlations, and nonlinear corrections may also survive. Any source proof must therefore analyze the full inhomogeneous critical window as a single object.

---

## 9. Relation to the KRV variance heuristic

There is a useful consistency check. If a stationary block were much longer than its correlation length, then the block variance would be controlled by the zero-frequency susceptibility:

`Var(sum_{j=r}^{r+ell} eta_j)
 ~ (ell/(n beta)) Q_u(0)
 ~ (2 ell/(3 n beta)) u^(-2).`

Since `u=(j/n)^(1/3)`, summing this local variance density formally gives

`const * n^(-1/3) [ (r+ell)^(1/3) - r^(1/3) ],`

which is exactly the `k=1` shape of the KRV Section-13 difference-square heuristic.

So the exponent in the source heuristic is not the problem. The problem is the missing scale separation required to justify replacing the inhomogeneous field by stationary long blocks: inside `j=O(m_n)`, no block can be both much longer than the correlation length and much shorter than the edge window.

---

## 10. Exact blocker after recovery 1/2

The blocker is now more precise than in Claim 268.

The continuum operator exists (Claims 264/266). The explicit source-valid `k=1` local branch and susceptibility are known (Claim 268). The present Claim 270 gives the full frozen lattice Hessian and proves that its correlation length is order `m_n` throughout the source edge window.

What a source-matching proof must add is therefore:

1. the **nonhomogeneous full-window Hessian / Green operator** obtained when `u(j)~(j/n)^(1/3)` varies on the critical scale, rather than a frozen stationary Hessian;
2. control of the hard mode and a rigorous Schur-complement reduction to the soft critical mode;
3. a nonlinear concentration / finite-dimensional limit theorem on that nonuniformly convex field, with no local stationary replacement;
4. the KRV integrated-potential functional convergence and the global growth/oscillation estimates needed for operator convergence.

The simplest unproved case remains the same explicit quartic `V_*` and one fixed `beta>0`, but the relevant object is now the entire `n^(1/7)` critical window rather than a local block.

**Recovery 1/2 is consumed.** The metric did not move, but this recovery materially changed the blocker: rapid local mixing is not merely unproved; for the frozen linearized model it is impossible on an `o(m_n)` scale. A second/final recovery is warranted only by changing category to the nonhomogeneous critical-window operator.

Selected final-recovery action, if D0043 continues next run:

**derive the nonhomogeneous continuum Schur-complement Hessian on the full `k=1` window and decide whether its Gaussian critical field can possibly generate the KRV Brownian integrated potential before invoking nonlinear corrections.**

Recommended next Section-B triple: **B1 CHANGE THE CATEGORY, B18 SAY IT IN ANOTHER LANGUAGE, B23 DO WHAT THE PROPOSER DID NOT EXPECT.**

If that final recovery leaves `k_exotic^cert=0`, D0043 must be immutably handed off and P03 rotated; there is no third D0043 recovery.

---

## 11. Directed second audit: P04 / I0101

I independently audited a P04 theorem not previously audited by P03:

`P04-I0101-LOCAL-PATTERN-FOURIER-RIGIDITY-15`

from

`proofnet24/P04-closure-local-paley/runs/2026-09-17/2026-09-17T05-45-03Z__run-report.md`,

creation commit `534303105bce1394e989f1a228ffaf8637d0cbc1`, blob `7e00639496a5205478f5d4359a85d0b704325153`.

The report was fetched at that exact creation commit. This claim had a P11 audit in repository history, but no prior P03 audit was recovered by exact claim-name search, so it is new for P03's directed duty.

### Peer claim

Let `G=S3`. For every mask `E subset G`, let `b_E:G->R` satisfy `b_E(g)=1` for `g in E`. Define unnormalized Fourier data

`a_E = sum_g b_E(g)`,
`s_E = sum_g b_E(g) sgn(g)`,
`U_E = sum_g b_E(g) std(g)`,

and

`mu = 64^(-1) sum_E a_E`, `c=(mu-3)/3`.

The claim is

`64^(-1) sum_E [a_E^2+|s_E|^2+2||U_E||_F^2]
 = 18 + 2(mu-3)^2
   + (6/64) sum_E sum_{g notin E} (b_E(g)-c)^2.`

For `mu=0`, the unique minimizer is the conference-sign rule `b_E=+1` on the mask and `-1` off the mask, with minimum total Fourier energy `36`.

### Independent audit proof

Finite-group Plancherel for the unnormalized Fourier transform on `S3`, whose irreducible dimensions are `1,1,2`, gives for each mask

`a_E^2+|s_E|^2+2||U_E||_F^2 = 6 sum_g b_E(g)^2.`

Average over all 64 masks. Each of the six group elements lies in exactly 32 masks, so there are `64*3=192` fixed edge incidences and the same number of free incidences. Therefore the average fixed contribution to `sum_g b_E(g)^2` is exactly `3`, yielding the baseline `18` after multiplying by 6.

The average free-slot sum is `mu-3`. Since there are three free slots per mask on average, their global mean is `c=(mu-3)/3`. Completing the square gives

`64^(-1) sum_E sum_{g notin E} b_E(g)^2
 = 3c^2 + 64^(-1) sum_E sum_{g notin E}(b_E(g)-c)^2.`

Multiplication by 6 gives

`18 + 18c^2 + (6/64) sum squares
 = 18 + 2(mu-3)^2 + (6/64) sum squares,`

which is exactly the peer identity. If `mu=0`, then `c=-1`, the baseline is `18+18=36`, and equality is unique precisely when every free slot is `-1`. This is the conference-sign rule.

Verdict:

**`P03-AUDIT-P04-I0101-LOCAL-PATTERN-FOURIER-RIGIDITY-271 = PASS (CLAIM-SCOPED)`.**

Scope warning: this validates the exact local `S3` Fourier variational identity. It does not prove Randomstrasse Conjecture 27 or an eventual Paley-theta bound.

---

## 12. Prior-art / novelty discipline

The new D0043 result uses standard Fourier diagonalization of a translation-invariant Hessian and standard Green-kernel scaling. I did not find this explicit quartic symbol/correlation-length calculation stated in the bounded source/literature screen, but a search miss is not a novelty certificate. Status is therefore **PUBLICATION-NOVELTY-UNVERIFIED**.

The mathematical point claimed here is narrow and exact: for one source-admissible `k=1` potential, the full frozen Hessian has quartic soft dispersion and source-window correlation length `Theta(n^(1/7))`. It is not a general-beta exotic operator theorem.

---

## 13. Ledger delta for P26

```yaml
ledger_delta:
  task: P03
  target: D0043 / Virag ICM 2014 Conjecture 5 exotic edge operators
  metric: k_exotic^cert
  before: 0
  after: 0
  movement: none
  status: PARTIAL
  source_status: OPEN_ON_BOUNDED_2026_09_18_SCREEN
  unchanged_streak: 4
  stuck_protocol: ACTIVE
  recovery_episode_executed: 1_of_2
  section_B_moves: [30, 11, 7]
  new_claim: P03-D0043-K1-FROZEN-GREEN-CRITICAL-WINDOW-270
  new_claim_status: PROVED_STRUCTURAL_PARTIAL_SOURCE_ADMISSIBLE_EXAMPLE_PUBLICATION_NOVELTY_UNVERIFIED
  key_result: full frozen k1 Hessian has soft symbol proportional to theta^4+20u theta^2+120u^2 and correlation length Theta(u^-1/2)=Theta(n^(1/7)) across the source edge window
  next_blocker: nonhomogeneous full-window critical Hessian plus nonlinear field limit; no local stationary mixing scale
  next_recovery_if_continued: 2_of_2_FINAL
  next_moves: [1, 18, 23]
  peer_audit: P03-AUDIT-P04-I0101-LOCAL-PATTERN-FOURIER-RIGIDITY-271 PASS_CLAIM_SCOPED
  checker_created: false
```

**End of complete run report.**