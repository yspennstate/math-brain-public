Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED. This is not GPT-6 at maximum.** **NO SOURCE-LEVEL COEFFICIENT-METRIC MOVEMENT.** The saturated metrics remain `c_LK^cert=a_LK^fine=b_LK^sqrt=0`; no stuck count is manufactured from saturation, and HARD recoveries remain `0/2`. This run uses **#8 GO THE OTHER WAY AND DISCRETIZE, #12 FIND WHAT IS CONSERVED, #27 SWAP THE QUANTIFIERS**. The main result is a fully uniform replacement for Claim 301 Lemma 3.1(b): arbitrary bounded deadline omissions, including extreme ranks, preserve the `exp[-k+o(k)]` rejection cost with an explicit error bound.

# P03 / P0456 run report — exact bounded-omission discretization and uniform marked-saddle repair

Run-start timestamp: **2026-09-19T03:28:43Z**  
Track: **P03**  
Canonical target: **P0456**  
Repository / branch: `yspennstate/math-open-problems` / `master`  
Category: **HARD OUTSIDE**

---

## 1. Continuity, controls, audit-first screen, and source status

The exclusive assignment remains

`operations/claims/P0456.md`,

creation commit `9d9c9545783bf8ae09805830d72f5d935be9afb1`, blob `74b9c5ebda19b1ded526457c1c7ea12654419bcb`.

The newest complete P03 report entering this run was

`proofnet24/P03-fei/runs/2026-09-19/2026-09-19T02-32-51Z__p0456-defect-completeness-repair.md`,

creation commit `5a055a85d04533758c5eaf1126d22f9f6e1e9dbc`, blob `6a4ff314614ec27d942cde43056caf8a54346b6c`; its exact blob readback recovered `**End of complete run report.**`.

I preserve Claims 274, 276, 278, 280, 282, 284, 286 and 288--302. Claim 301 remains preserved only with Claim 302's minimum-deadline collision-block repair. This run adds Claim 303 below.

This run reread/recovered root `README.md`, `proofnet24/HOURLY_PROTOCOL_2026-09-15.md`, current `FLEET_RULES.md`, the current owner directive, campaign `probability_campaign_2026_09/INDEX.md` and `RANKING.md`, root `POSTED.md`, `RESULTS.md`, `QUEUE.md`, the canonical P0456 claim, the complete Claim-302 report at its exact creation commit, the source-capsule Lemma 3.1 and interaction proof, the current P26 run directory/newest P26 report, P04 rotation-stop state, and neighboring P0457 ownership only for nonduplication. `FLEET_RULES.md`, `OWNER_DIRECTIVE.md`, `POSTED.md`, `RESULTS.md`, and `QUEUE.md` are large connector-truncated surfaces, so this is not represented as a byte-for-byte whole-file reread; exact paths plus targeted reads/searches were used for the relevant controls and target state.

### 1.1 Incoming outside-audit screen

The newest complete P26 report recovered is

`proofnet24/P26-proof-audit-recovery/runs/2026-09-19/2026-09-19_05-00-09__run-report.md`,

creation commit `9d433d504a2cfb254fe061005a345b4e51ae25d9`.

It audits P04/I0101 Claim 38 at `p=4177`, not P0456. Fresh repository searches for `P0456` together with `AUDIT`, `PASS`, Claims 288/289/301/302, and P26 still recover no P26 or genuinely distinct OTHER-track full-chain P0456 audit. P04 has no `2026-09-19` run directory; its newest owner record remains the 2026-09-18 rotation-stop/disabled state, so there is no new P04 successor theorem for the directed P03->P04 duty. No repeated audit is fabricated.

Thus the closure gate remains

`P0456_ACTIVE_AUDIT_PENDING / OUTSIDE_AUDITS_FOUND_0_OF_2`.

Self-audits do not count. No source-CLOSED label and no final paper folder are created.

### 1.2 Fresh primary-source and current-literature screen

The primary source remains Hossein Dabirian and Vijay Subramanian, *Connectivity of a family of bilateral preference random graphs*, *Journal of Applied Probability* 63(2) (June 2026), 552--579, DOI `10.1017/jpr.2025.10051`, published online 18 December 2025.

Fresh Cambridge PDF retrieval on 19 September 2026 reverified Section 1.1 verbatim in substance: the authors still state that connectivity is unknown throughout

`log n - 0.5 loglog n sqrt(log n) <= k <= log n + 0.5 loglog n sqrt(log n)`,

and explicitly say the gap may come from analytically simpler sufficient conditions, including the no-intersection requirement in their isolated-vertex event. Lemma 10 still gives the pair bad-event estimate `P(B)=O(k^3/n)`; Lemma 14 is the pair second-moment comparison below coefficient `-1/2`; Theorem 3 is the lower disconnectedness result and Theorem 6 the upper connectivity result above coefficient `+1/2`.

Fresh bounded searches dated 19 September 2026 for the DOI/title/authors and for 2026 bilateral-preference connectivity/Poisson updates recovered the Cambridge article, journal/index mirrors, and author bibliographic entries but no later source-matching constant-window or isolated-vertex Poisson theorem. This is bounded negative evidence only. **Publication novelty remains UNVERIFIED.**

Neighboring `P0457` remains the distinct diameter open problem, canonically owned by NM13-04; it is not duplicated here.

---

## 2. Why Lemma 3.1(b) needed a cleaner proof surface

Claim 301 Lemma 3.1(b) asserted that deleting a bounded number of arbitrary proposal deadlines and lowering boundedly many competitor quotas leaves rejection cost `exp[-k+o(k)]`. Its proof reduced the event to an integral with an extra fixed power of the terminal order statistic and said that the same marked-saddle split controls it. That is plausible, but an outside auditor still had to check two hidden quantifiers:

1. the deleted ranks can be **any** ranks, including the very first or the terminal ranks;
2. the competitor quota can be lowered by a bounded amount at different retained deadlines, and the interaction skeleton can choose those deadlines adversarially.

Claim 302 repaired collision disjointization but did not make this analytic uniformity explicit. The purpose of this run is to remove that ambiguity completely.

---

## 3. #8 GO THE OTHER WAY AND DISCRETIZE — exact finite order-statistic representation

We first give an exact finite representation before taking any asymptotics.

Fix integers `m>=1` and `p<=m`. Let `U_1,...,U_m` be iid Uniform[0,1], with first `p` order statistics

`X_(1)<...<X_(p)`.

For each rank `i<=p`, let its outside-competitor block have size `N_i` and required quota `h_i`, and define

`q_i(x)=P(Bin(N_i,x)>=h_i)`.

Let `D subset {1,...,p}` be the set of omitted rejection deadlines. Conditional on the proposal order statistics, the disjointized outside competitor blocks are independent, so the exact rejection probability is

`P_{m,p}(D,h,N)`
` = (m)_p int_{0<x_1<...<x_p<1} (1-x_p)^(m-p) product_{i notin D} q_i(x_i) dx_1...dx_p`.       (3.1)

This is already a finite binomial/order-statistic expression and contains the omitted ranks exactly.

There is also an exact one-dimensional recursion. Put

`f_i(x)=1` if `i in D`, and `f_i(x)=q_i(x)` otherwise,

`F_0(x)=1`,

`F_i(x)=int_0^x F_{i-1}(u) f_i(u) du`.

Then

`P_{m,p}(D,h,N)=(m)_p int_0^1 F_{p-1}(t) f_p(t)(1-t)^(m-p)dt`.          (3.2)

Every `q_i` is the finite polynomial

`q_i(x)=sum_{j=h_i}^{N_i} C(N_i,j)x^j(1-x)^(N_i-j)`.                  (3.3)

Therefore (3.2) is an **exact finite rational coefficient algorithm** for every integer choice of `m,p,N_i,h_i,D`. No favorable-rank assumption appears anywhere.

For the asymptotic upper bound we can simplify further. If the largest retained rank is `ell`, all omitted ranks above `ell` can be discarded from the proposal exposure. Hence assume `ell` itself is retained. Let

`d=|D intersect {1,...,ell-1}|`, `s=ell-1-d`.

Let `N_+=max_i N_i`, `h_-=min_{i notin D} h_i`, and

`q(x)=P(Bin(N_+,x)>=h_-)`, `Q(t)=int_0^t q(x)dx`.

Since binomial upper tails increase with `N` and decrease with `h`, every retained `q_i<=q`.

Condition on `T=X_(ell)=t`. The first `ell-1` points are the order statistics of `ell-1` iid Uniform[0,t] variables. The product over the specified `s` retained ranks is one nonnegative term of the degree-`s` elementary symmetric polynomial of the `ell-1` values `q(U_j)`. Thus

`E[product retained q_i(X_(i)) | T=t]`
` <= C(ell-1,d) [Q(t)/t]^s`.                                  (3.4)

Dropping the terminal factor `q_ell(t)<=1` gives the exact uniform inequality

`P_{m,p}(D,h,N)`
` <= C(ell-1,d) (m)_ell/(ell-1)!`
`    * int_0^1 t^d Q(t)^s (1-t)^(m-ell) dt`.                 (3.5)

The omission **locations have disappeared**. Only their number `d<=|D|` remains. This is the key discretization fact.

---

## 4. #12 FIND WHAT IS CONSERVED — exact mean-replacement identity

Let

`B~Beta(h_-,N_+-h_-+1)`, `mu=E B=h_-/(N_++1)`.

Beta-binomial duality gives

`q(x)=P(B<=x)`, `Q(t)=E[(t-B)_+]`.                            (4.1)

Replace `B` by its mean, so `Q(t)` becomes

`L_mu(t)=(t-mu)_+`.

### 4.1 No omissions: exact conservation

When `d=0`, the right-hand side of (3.5) with `Q=L_mu` is exactly

`(m)_ell/(ell-1)! int_mu^1 (t-mu)^(ell-1)(1-t)^(m-ell)dt`
` = (1-mu)^m`.                                                (4.2)

This is **independent of `ell`**. In the clean mean-replacement model, exposing/requiring any initial number of proposal deadlines conserves the same total rejection mass.

### 4.2 Arbitrary bounded omissions: exact beta sum

For `d>=0`, with `s=ell-1-d`, define the mean-replacement upper integral

`J_d(mu)=C(ell-1,d)(m)_ell/(ell-1)!`
` * int_mu^1 t^d(t-mu)^s(1-t)^(m-ell)dt`.                    (4.3)

Expanding `t^d=[mu+(t-mu)]^d` and evaluating each beta integral gives the exact finite identity

`J_d(mu)`
` = sum_{j=0}^d`
`   [ m!(s+j)! / {s! j!(d-j)!(m-d+j)!} ]`
`   * mu^(d-j)(1-mu)^(m-d+j).                                (4.4)

This identity makes the conserved quantity precise. Factoring `(1-mu)^m`, every omitted rank only inserts a polynomial factor. For fixed `d<=M`, `ell=k+O_M(1)`, `m=n+O_r(1)`, `h_-=k+O_M(1)`, and `N_+=n+O_r(1)`, each term in (4.4) is at most

`C_{M,r} k^d (1-mu)^m`.                                      (4.5)

Moreover

`(1-mu)^m=exp[-h_-+O_{M,r}(k^2/n)]`.                         (4.6)

So **arbitrary omitted ranks do not change the exponential scale**. Their entire mean-replacement effect is at most `k^M`; quota shifts affect only `h_-=k-O(M)`.

---

## 5. #27 SWAP THE QUANTIFIERS — one simultaneous uniform bound

We now prove a single bound valid at once for every bounded offset, omission set, quota shift, and repaired fixed-root skeleton.

### Claim `P03-P0456-UNIFORM-BOUNDED-OMISSION-SADDLE-303`

**Status:** `PROVED / SELF-AUDIT-REPAIR / SUPPORTING / AUDITS-PENDING / PUBLICATION-NOVELTY-UNVERIFIED`.

Fix `C,M,r<infinity`. Uniformly over all integers satisfying

- `|k-log n|<=C`;
- `m=n+O_r(1)` and every competitor-block size `N_i<=n+O_r(1)`;
- `p=k+O_M(1)`;
- every omission set `D subset {1,...,p}` with `|D|<=M`;
- every retained quota `h_i` with `k-M<=h_i<=k+M`;
- every repaired fixed-`r` interaction skeleton of Claims 301--302 whose residual rejection blocks are disjoint;

the probability that all retained rejection constraints hold is at most

`exp[-k + O_{C,M,r}(k^(2/3)+log k)]`.                        (5.1)

In particular it is `exp[-k+o_C(k)]`, uniformly over **all** bounded omissions and shifts, including extreme omitted ranks.

### Proof

Use the domination and notation of (3.5), with `h_- >= k-M`. Put

`sigma=E|B-mu| <= sqrt(Var B) <= C_{C,M,r} sqrt(k)/n`.        (5.2)

Because `x -> (t-x)_+` is 1-Lipschitz,

`Q(t)<=L_mu(t)+sigma`.                                        (5.3)

Choose

`A=k^(1/3)`, `tau=mu+A sigma`.

#### Low region `0<=t<=tau`

Here

`Q(t)<=(A+1)sigma <= C k^(5/6)/n`.                            (5.4)

Using `s=ell-1-d=k+O_M(1)` in (3.5), Stirling's elementary factorial bounds give

`log[ C(ell-1,d)(m)_ell/(ell-1)! * (C k^(5/6)/n)^s ]`
` <= -(1/6)k log k + O_{C,M,r}(k)`.                          (5.5)

Thus the entire low region is `exp[-Omega(k log k)]`, uniformly in the omitted ranks.

#### High region `t>=tau`

Now `t-mu>=A sigma`, so (5.3) gives

`Q(t)<= (t-mu)(1+1/A)`.

Hence

`Q(t)^s <= exp(O(s/A))(t-mu)^s`
`          <= exp(O(k^(2/3)))(t-mu)^s`.                      (5.6)

Insert (5.6) into (3.5), and use the exact beta sum (4.4)--(4.6):

`P_high`
` <= exp(O(k^(2/3))) J_d(mu)`
` <= exp[-h_- + O_{C,M,r}(k^(2/3)+log k)]`
` <= exp[-k + O_{C,M,r}(k^(2/3)+log k)]`.                    (5.7)

Adding the superexponentially smaller low region proves (5.1). `square`

### 5.1 What can depend on the omitted set

The proof isolates every possible dependence:

1. the exact finite recursion (3.2) sees the actual omitted ranks;
2. the uniform upper bound (3.5) sees only `d=|D intersect {1,...,ell-1}|`;
3. the mean-replacement identity (4.4) sees only that integer `d`, contributing at most `k^d`;
4. the beta fluctuation error is independent of omission locations and contributes `exp[O(k^(2/3))]`;
5. quota shifts enter only through the worst quota `h_-=k-O(M)`.

There is therefore no extreme-rank obstruction hidden in Lemma 3.1(b).

---

## 6. Product step for repaired fixed-r skeletons

The last requested audit is whether one may multiply the per-root bounded-omission estimates after Claim 302's disjointization.

Fix a complete witness-labelled repaired skeleton. Temporarily remove root--root edges as in Claims 301--302.

1. **Root proposal arrays.** For different roots, the remaining incident root edges are disjoint raw edge sets, hence their ordered proposal values are independent. For each root, the ordered labels are independent of the ordered values by iid exchangeability. Conditioning on the cross-root label-equality partition therefore does not couple the proposal-value arrays.

2. **Active defects.** A selected--selected outside edge is disjoint from every root proposal array. A root-selected cross edge is a nonselected edge in the other root's star; conditional on that root's threshold and nonselection, its exact law is Uniform[`T`,1]. On the guard `G_L`, its prescribed early event has probability `O_L(k/n)` **pointwise in the proposal thresholds**. An early root--root edge likewise costs `O_L(k/n)` independently after temporary deletion. We first integrate these active-defect edges and pull out their uniform skeleton factors. They are not left inside the residual product.

3. **Residual rejection blocks.** By Claim 302, after minimum-deadline collision retention and the prescribed bounded omissions, every surviving competitor edge is `{u,x}` with `u` a distinct retained selected label and `x` in the external pool. Distinct retained labels have disjoint undirected edge families. Those raw edges are also disjoint from all root proposal arrays.

Therefore, conditional on the fixed label skeleton, after the active-defect factors are paid, the remaining rejection expectation factors exactly over roots into per-root functionals of the form covered by Claim 303. Thus for fixed `r`

`P(residual rejections | repaired skeleton,G_L)`
` <= exp[-rk + O_{C,M,r}(k^(2/3)+log k)].                    (6.1)

Combining (6.1) with the skeleton codimension `n^{-K+o(1)}` proves again that every positive-complexity skeleton contributes `o(e^{-rk})`. There is no silent multiplication of events sharing root order statistics.

Claim 303 therefore strengthens/replaces the proof of Claim 301 Lemma 3.1(b) without changing Claims 288/289/301/302.

---

## 7. Literal LK component elimination remains intact

This run did not infer connectivity from mean degree. The component side remains the self-contained Claim-301/302 argument under the literal bilateral rule:

- sizes `2--6`: delete all internal component edges before ordering external proposals, so the first `k-(r-1)` external proposals are unaffected by the spanning-tree weights; their rejection lists can be treated independently of the light tree edges;
- sizes `7--12`: on the single global threshold event with `a=5/32`, `b=32/5`, the component union bound has fixed-size exponent `1-5r/32`, already negative at `r=7`;
- sizes `13--floor(n/2)`: the same single global event yields the uniform geometric exponent beginning at `-1/64` when `r=13`;
- the two global threshold-tail Chernoff exponents are both strictly larger than one, and that global failure event is paid once.

Claim 302 rechecked these constants exactly. No new component gap appeared in the present analytic repair.

---

## 8. Methods used and failed variants

### #8 GO THE OTHER WAY AND DISCRETIZE — SUCCESS

The arbitrary-rank omission event now has the exact finite recursion (3.2) with finite binomial polynomials. This removed all ambiguity about whether an omitted rank was being treated favorably.

### #12 FIND WHAT IS CONSERVED — SUCCESS

The mean-replacement integral has exact mass `(1-mu)^m` with no omissions, independent of how many initial deadlines are retained. With `d` arbitrary omissions, the exact beta sum (4.4) shows that only a degree-`d` polynomial factor is lost. This is the invariant behind bounded omission.

### #27 SWAP THE QUANTIFIERS — SUCCESS

Rather than proving a separate `o(1)` for each fixed skeleton, Claim 303 gives one explicit bound uniform simultaneously over the bounded window, all omission sets of size at most `M`, all bounded quota shifts, and all repaired fixed-root skeletons.

### Failed/abandoned variants

1. Bounding every retained deadline by the terminal binomial tail `q(T)` is too crude: near the dominant terminal rank that bound can be order one and loses the `e^{-k}` scale.
2. Using only the additive estimate `Q(t)<=(t-mu)_+ + sigma` globally also loses the scale near `t=mu`; the low/high split at `mu+k^(1/3)sigma` is what makes the additive fluctuation harmless.
3. The exact recursion (3.2) is ideal for finite verification but opaque for asymptotics. The elementary-symmetric domination (3.4) is the bridge that removes omission locations before the saddle estimate.

---

## 9. Cumulative claim ledger delta

Preserved unchanged:

- `P03-P0456-POISSON-CRITICAL-WINDOW-288 = PROVED / SOURCE-MATCHING-CANDIDATE-COMPLETE / AUDITS-PENDING / PUBLICATION-NOVELTY-UNVERIFIED`.
- `P03-P0456-UNIFORM-POISSON-INTERACTION-REPAIR-289 = PROVED / SELF-AUDIT-REPAIR / SOURCE-MATCHING-STRENGTHENING / AUDITS-PENDING / PUBLICATION-NOVELTY-UNVERIFIED`.
- Claim 290 marked PPP and Claims 291--300 supporting self-audit/strengthening kernels.
- `P03-P0456-SOURCE-AUDIT-CAPSULE-301 = PROVED / SELF-AUDIT-CAPSULE / STEP-D-REPAIRED-BY-302 / LEMMA-3.1b-STRENGTHENED-BY-303 / SOURCE-MATCHING-SUPPORT / AUDITS-PENDING / PUBLICATION-NOVELTY-UNVERIFIED`.
- `P03-P0456-DEFECT-COMPLETENESS-DISJOINTIZATION-302 = PROVED / SELF-AUDIT-REPAIR / SUPPORTING / AUDITS-PENDING / PUBLICATION-NOVELTY-UNVERIFIED`.

New:

- `P03-P0456-UNIFORM-BOUNDED-OMISSION-SADDLE-303 = PROVED / SELF-AUDIT-REPAIR / SUPPORTING / AUDITS-PENDING / PUBLICATION-NOVELTY-UNVERIFIED`.

The source-matching theorem remains candidate-complete and audit-pending. Claim 303 is another P03 self-audit and does not move the independent-audit count.

All fixed coefficient metrics remain saturated at zero. HARD recoveries remain `0/2`.

---

## 10. Exact remaining obligations and `ledger_delta` for P26

The mathematical obligation for the source-matching chain is now primarily **independent verification**, not another self-strengthening:

1. P26 must independently audit the repaired chain Claims 288/289/301/302/303 end to end, including the arbitrary-rank bounded-omission quantifier and the Claim-302 minimum-deadline collision repair.
2. One genuinely distinct OTHER track must independently audit the same full source-matching chain. P03 self-checks never count.
3. Publication novelty remains unverified; repeat bounded current-literature checks do not become a novelty certificate.
4. Only after both outside PASS audits should a final source-matching paper folder be created and P26 asked to reconcile closure.

Suggested shared-ledger delta for P26 only:

```text
P03 / P0456:
  source_status: OPEN_IN_PRIMARY_SOURCE / SOURCE-MATCHING-CANDIDATE-COMPLETE_INTERNAL
  metrics: c_LK^cert=0, a_LK^fine=0, b_LK^sqrt=0 (SATURATED)
  new_claim: P03-P0456-UNIFORM-BOUNDED-OMISSION-SADDLE-303
  claim_301_status: PROVED / STEP-D-REPAIRED-BY-302 / LEMMA-3.1b-STRENGTHENED-BY-303 / AUDITS-PENDING
  outside_audits: 0/2
  closure: DO_NOT_CLOSE
  paper_package: DO_NOT_CREATE_YET
```

---

## 11. Next state

`P0456_ACTIVE_AUDIT_PENDING / OUTSIDE_AUDITS_FOUND_0_OF_2 / CLAIM_303_UNIFORM_OMISSION_REPAIR_READY`.

The next run should begin with incoming outside audits. If none exists, do **not** spend another run improving correction coefficients or coefficient windows. A useful fresh direction is to translate the repaired fixed-root proof into an outside-auditor lemma stack with no model-specific prose hidden between steps, and then attack the possibility of a direct Chen--Stein/dissociated-block certificate only if it genuinely shortens the source proof rather than duplicating factorial moments.

**End of complete run report.**