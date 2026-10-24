Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED. This is not GPT-6 at maximum.**

**NO SOURCE-LEVEL COEFFICIENT-METRIC MOVEMENT; NEW SECOND-CORRECTION THEOREM.** The saturated frontiers remain `c_LK^cert=a_LK^fine=b_LK^sqrt=0`; HARD recoveries remain `0/2`. This run uses fresh Section-B methods **#17 LOOK FOR YOUR NUMBERS SOMEWHERE ELSE, #14 EXACT FINITE REDUCTION, #3 PROVE SOMETHING STRONGER**. The substantive advance is a genuine `1/k` refinement of Claim 298's leading clean-saddle correction, together with an exact finite coefficient-extraction formula for the full clean marked integral (not merely the auxiliary Gamma model).

# P03 / P0456 run report — exact finite clean integral and second critical-window correction

Run timestamp: **2026-09-18T23:31:30Z**  
Track: **P03**  
Canonical target: **P0456**  
Repository / branch: `yspennstate/math-open-problems` / `master`  
Category: **HARD OUTSIDE**

---

## 1. Continuity, repository controls, source status, and audit gate

The exclusive assignment remains

`operations/claims/P0456.md`,

creation commit `9d9c9545783bf8ae09805830d72f5d935be9afb1`, blob `74b9c5ebda19b1ded526457c1c7ea12654419bcb`.

The newest complete P03 report entering this invocation was

`proofnet24/P03-fei/runs/2026-09-18/2026-09-18T22-28-49Z__p0456-first-correction-laplace.md`,

creation commit `a86b52b8c39a3509d0fa1cffcb24c2a23cebe81b`, blob `b50bf75945491d5fa26a07ce3410e9af6f5d6739`; exact-commit readback recovered `**End of complete run report.**`.

I preserve Claims 274, 276, 278, 280, 282, 284, 286 and the candidate-complete/supporting chain 288--298.

This invocation reread/recovered the root `README.md`, `proofnet24/HOURLY_PROTOCOL_2026-09-15.md`, current `FLEET_RULES.md`, `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`, campaign `probability_campaign_2026_09/INDEX.md` and `RANKING.md`, root `POSTED.md`, `RESULTS.md`, `QUEUE.md`, the canonical P0456 ownership claim, the newest complete P03 report, current P26 evidence, current P04 stop state, and P0457 references only for nonduplication. Large connector-rendered policy/root/campaign files are truncated by the connector and are not represented here as byte-for-byte rereads; exact-path reads controlled every mathematical dependency used below.

The canonical ownership claim still assigns P0456 exclusively to P03. The live ownership search continues to list P0456 among already-owned targets; no release or competing owner was found. P0457 remains a distinct diameter problem and is not resumed.

### Fresh primary-source verification

The primary source remains Hossein Dabirian and Vijay Subramanian, *Connectivity of a family of bilateral preference random graphs*, *Journal of Applied Probability* 63(2) (June 2026), 552--579, DOI `10.1017/jpr.2025.10051`, published online 18 December 2025.

Fresh Cambridge HTML retrieval on 18/19 September 2026 again verifies the literal model and Section 1.1. The paper states that, although Theorems 3 and 6 establish `k=log n` as the threshold, it is not known whether connectivity holds inside

`log n - 0.5 loglog n sqrt(log n) <= k <= log n + 0.5 loglog n sqrt(log n)`,

and explicitly says that more elaborate or exact sufficient conditions could close the gap. The same source gives the lower and upper window theorems used in the preserved chain and Lemma 10's `O(k^3/n)` bad-interaction estimate.

Fresh bounded searches for the exact title/DOI/authors, `LK(n,k) Poisson isolated vertices`, `LK(n,k) log n+c connectivity`, and variants involving the first-correction constant found the Cambridge paper and adjacent preference-graph material but no later source-matching Poisson/constant-window/first-correction theorem. This is dated bounded negative evidence only; **publication novelty remains UNVERIFIED**.

### Fresh outside-audit screen

No qualifying P0456 audit has arrived. Repository search for `P0456`, exact Claim-288/289/298 identifiers, `PASS`, and audit terminology still returns only P03's own P0456 material.

The newest concrete P26 report recovered is

`proofnet24/P26-proof-audit-recovery/runs/2026-09-19/2026-09-19_01-59-40__run-report.md`,

creation commit `910a3171b7f4126c9049856fc5543f37221d7b43`, blob `62b3427b406ff0bf23bd769ddd3eaa0c572653a9`. It audits the historical P04/I0101 split-conic Claim 11 and reconciles that P04 package; it does **not** audit P0456. P04 itself remains rotation-stopped, with newest known terminal record `proofnet24/P04-closure-local-paley/runs/2026-09-18/2026-09-18T13-49-33Z__rotation-stop-disabled.md`, creation commit `0bae9b472059407291083f04a1c494490337b924`, blob `348f9e0d08a29085964161377e66388357c0e1b9`, and no new theorem for the directed P03->P04 duty.

Therefore the closure gate remains

`P0456_ACTIVE_AUDIT_PENDING / OUTSIDE_AUDITS_FOUND_0_OF_2`.

Self-audits do not count. No source-closure label and no final paper folder are created.

---

## 2. Preserved chain and new theorem

The source-matching chain remains:

- `P03-P0456-POISSON-CRITICAL-WINDOW-288 = PROVED / SOURCE-MATCHING-CANDIDATE-COMPLETE / AUDITS-PENDING / PUBLICATION-NOVELTY-UNVERIFIED`;
- `P03-P0456-UNIFORM-POISSON-INTERACTION-REPAIR-289 = PROVED / SELF-AUDIT-REPAIR / SOURCE-MATCHING-STRENGTHENING / AUDITS-PENDING / PUBLICATION-NOVELTY-UNVERIFIED`;
- Claim 290: marked isolated-vertex PPP;
- Claims 291--298: supporting P03 self-audit/strengthening kernels.

This run adds:

### Claim `P03-P0456-SECOND-CORRECTION-FINITE-REDUCTION-299`

**Status:** `PROVED / SELF-AUDIT-STRENGTHENING / SUPPORTING / AUDITS-PENDING / PUBLICATION-NOVELTY-UNVERIFIED`.

Retain Claim 298's constants

`eta = sqrt(2)-1-log((1+sqrt(2))/2)`,

`C_* = (1+sqrt(2))/sqrt(2*pi*(2-sqrt(2)))`,

and put

`a_1 := -(332+235 sqrt(2))/96
      = -6.920210282892472...`.                               (2.1)

If integer `k-log n -> c in R`, define

`lambda_n=n e^{-k}`,

`eps_n=k^{-1/2} e^{-eta k}`.                                  (2.2)

Then for every fixed vertex `v`,

`P(I_v)
 = e^{-k}{1+C_* eps_n[1+a_1/k+o(1/k)]}.`                     (2.3)

Consequently

`mu_n:=E Z_n
 = lambda_n{1+C_* eps_n[1+a_1/k+o(1/k)]}.`                   (2.4)

The Palm/size-bias Poisson error and every nontrivial-component contribution are smaller than the new scale:

`d_TV(Law(Z_n),Poisson(mu_n))=o(eps_n/k)`,                    (2.5)

`P(exists a nontrivial component)=o(eps_n/k)`.               (2.6)

Hence

`P(LK(n,k) connected)
 = e^{-lambda_n}
   {1-lambda_n C_* eps_n
      -lambda_n C_* a_1 eps_n/k
      +o(eps_n/k)}.`                                         (2.7)

Because `a_1<0`, the explicit second correction in (2.7) is positive:

`-lambda_n C_* a_1 eps_n/k
 =lambda_n C_* (332+235 sqrt(2))/96 * eps_n/k.`               (2.8)

This is a second-order refinement of the supporting critical-window asymptotic. It is **not** source closure and makes no publication-priority claim.

The run also proves an exact finite representation of the full clean marked integral, in Section 4 below.

---

## 3. #17 LOOK FOR YOUR NUMBERS SOMEWHERE ELSE — the rate is classical, the contraction is composite

Claim 298's rate functions can be written using the standard Gamma/Cramer rate

`I(s)=s-1-log s`, `s>0`.                                     (3.1)

Indeed

`delta(t)=I(t)`,

`gamma(t)=I(1+t)`.                                            (3.2)

Therefore Claim 298's exponent is

`eta=min_{t>0}{I(t)+I(1+t)}`.                                (3.3)

This identifies the saddle as a contraction of **two simultaneous Gamma large deviations**: the normalized saddle variable pays `I(t)`, while the independent overshoot variable pays `I(1+t)`.

The individual rate in (3.1) is classical. Fresh NIST DLMF §8.12 retrieval states the large-parameter incomplete-gamma transformation through

`(1/2) eta_DLMF(lambda)^2=lambda-1-log lambda`,

and points to Temme's incomplete-gamma asymptotics. Fresh retrieval of N. M. Temme, *The Asymptotic Expansion of the Incomplete Gamma Functions*, SIAM J. Math. Anal. 10 (1979), DOI `10.1137/0510071`, confirms the standard asymptotic-expansion context. Thus the one-variable rates used here are not a new asymptotic principle.

Differentiating the composite rate gives

`d/dt[I(t)+I(1+t)]
 =2-1/t-1/(1+t)`,                                             (3.4)

whose unique positive zero is

`t_*=1/sqrt(2)`.                                              (3.5)

The bounded searches did not surface `eta=sqrt(2)-1-log((1+sqrt(2))/2)` or the saddle `1/sqrt(2)` as a named Bahadur--Rao/queueing/reliability constant. This is **not** a novelty certificate. The honest prior-art statement is: the component rates and sharp incomplete-gamma machinery are classical; the particular two-rate contraction arises from the P0456 clean marked integral and remains publication-novelty **UNVERIFIED**.

This perspective also explains why the two rate functions add in Claim 298 rather than compete: both deviations occur in the same one-defect expectation.

---

## 4. #14 EXACT FINITE REDUCTION — full clean marked integral

Claim 298 had an exact finite representation only for the auxiliary Gamma one-defect model. Here I reduce the **full beta clean integral** to a finite coefficient sum.

Recall

`B_k ~ Beta(k,N-k+1)`,

`q_k(x)=P(Bin(N,x)>=k)`,

`Q_k(x)=E[(x-B_k)_+]=int_0^x q_k(t)dt`,                       (4.1)

and

`M_{k,k}
 = C_{m,k} int_0^1 Q_k(x)^k(1-x)^(m-k-1)dx`,                 (4.2)

with

`C_{m,k}=(m)_{k+1}/k!`.                                      (4.3)

### 4.1 Exact stop-loss polynomial identity

Let `J_x~Bin(N+1,x)`. For `phi(j)=(j-k)_+`, the standard binomial derivative identity gives

`d/dx E phi(J_x)
 =(N+1) E[phi(K+1)-phi(K)]`,                                  (4.4)

where `K~Bin(N,x)`. Since

`phi(K+1)-phi(K)=1_{K>=k}`,                                  (4.5)

we obtain

`d/dx {E[(J_x-k)_+]/(N+1)}
 =P(Bin(N,x)>=k)=Q_k'(x)`.                                   (4.6)

Both sides vanish at `x=0`, so exactly

`Q_k(x)
 =1/(N+1) sum_{j=k+1}^{N+1}
   (j-k) C(N+1,j)x^j(1-x)^(N+1-j).`                          (4.7)

Define

`P_{N,k}(y)
 :=sum_{j=k+1}^{N+1}(j-k)C(N+1,j)y^j`.                       (4.8)

With `y=x/(1-x)`, equation (4.7) becomes

`Q_k(x)
 =(N+1)^(-1)(1-x)^(N+1) P_{N,k}(y).`                         (4.9)

### 4.2 Coefficient extraction

Write

`P_{N,k}(y)^k=sum_J a_J y^J`.                                (4.10)

Substituting (4.9) into the clean integral and using

`x=y/(1+y)`, `dx=dy/(1+y)^2`,                                (4.11)

we get exactly

`int_0^1 Q_k(x)^k(1-x)^(m-k-1)dx
 =(N+1)^(-k)
   sum_J a_J int_0^infinity y^J(1+y)^(-(kN+m+1))dy`           (4.12)

and hence

`= (N+1)^(-k)
   sum_J a_J B(J+1,kN+m-J).`                                 (4.13)

Equivalently, since the beta arguments are positive integers,

`B(J+1,kN+m-J)
 = J! (kN+m-J-1)!/(kN+m)!`.                                  (4.14)

Equations (4.8)--(4.14) are an **exact finite formula for the full clean marked integral**. No Gamma approximation or floating-point evaluation enters this identity.

### 4.3 Independent exact checker

I executed an exact `Fraction` checker that constructs the two sides independently:

1. direct side: expand the Bernstein polynomial (4.7) in `x`, raise it to the `k`th power, multiply by `(1-x)^(m-k-1)`, and integrate each monomial exactly;
2. transformed side: form `P_{N,k}(y)^k`, extract each exact integer coefficient, and evaluate (4.13) by factorials.

Artifact:

`proofnet24/P03-fei/artifacts/2026-09-18/2026-09-18T23-31-30Z__full_clean_coefficient_checker.py`

creation commit `5bc3fb85b27c8b284cb47ce4894dc8d1720655e3`, blob `430ddad3ba358d528d3be5e35f404cba952f81b2`.

Archived exact output:

`proofnet24/P03-fei/artifacts/2026-09-18/2026-09-18T23-31-30Z__full_clean_coefficient_checker.out`

creation commit `0d49114f36c96a4466344ff91bca2b8b0c14b8b7`, blob `a8f01f8829c7918cb12701a7745fde4bffb278d8`.

The output ends

`FULL_CLEAN_COEFFICIENT_IDENTITY_PASS`

and verifies five nontrivial exact cases, including `(N,m,k)=(8,11,3)`. This checker validates the finite identity only; it does not substitute for the asymptotic proof below.

A practical negative result from #14 is also worth recording: although (4.13) completely removes the continuous integral, direct saddle extraction from the very high-degree coefficient sum is not simpler than the beta/Gamma local analysis at `k~log n`. Its value is as an exact audit representation and a possible route to symbolic finite corrections, not as a replacement for Laplace asymptotics.

---

## 5. #3 PROVE SOMETHING STRONGER — the `1/k` correction to the one-defect saddle

Claim 298 reduced the leading clean defect to

`A_k=E[(k/W)(Y-k-W)_+]`,                                     (5.1)

where independently

`Y~Gamma(k,1)`, `W~Gamma(k+1,1)`.                            (5.2)

Write

`t=W/k`, `s=1+t`,

`gamma(t)=t-log(1+t)`,

`delta(t)=t-1-log t`,

`F(t)=gamma(t)+delta(t)`.                                     (5.3)

The unique minimizer remains

`t_*=1/sqrt(2)`,                                              (5.4)

with

`F(t_*)=eta`,

`F''(t_*)=8-4sqrt(2)=4(2-sqrt(2))`.                           (5.5)

The new task is to keep the first `1/k` term rather than stop at the leading Laplace prefactor.

### 5.1 Second-order boundary overshoot expansion

For fixed `t` in a compact neighborhood of `t_*`, put

`H_k(t)=E[(Y-sk)_+]`.                                         (5.6)

At the boundary, Stirling's expansion gives

`f_Y(sk)
 = e^{-k gamma(t)}
   /(s sqrt(2 pi k))
   [1-1/(12k)+O(k^-2)].`                                     (5.7)

For `z>=0`, let `q=t/s`. Uniformly for bounded `z` (and, after the usual `z<=k^(1/3)` / exponential-tail split, under the integral),

`f_Y(sk+z)/f_Y(sk)
 =e^{-qz}
  {1-[z/s+z^2/(2s^2)]/k+O((1+z^4)/k^2)}.`                   (5.8)

Because all polynomial moments against `z e^{-qz}` are finite uniformly on a compact `t`-set, integration yields

`H_k(t)
 = s/(t^2 sqrt(2 pi k)) e^{-k gamma(t)}
   {1+h_1(t)/k+O(k^-2)},`                                    (5.9)

where

`h_1(t)=-1/12-2/t-3/t^2`.                                   (5.10)

Indeed the two local-density correction integrals are

`[1/s int z^2 e^{-qz}dz
 +1/(2s^2) int z^3 e^{-qz}dz]
 /(int z e^{-qz}dz)
 =2/t+3/t^2`.                                                 (5.11)

### 5.2 Second-order saddle density

For `W~Gamma(k+1,1)`, the density of `t=W/k` is

`p_k(t)
 =sqrt(k/(2pi)) e^{-k delta(t)}
  [1-1/(12k)+O(k^-2)]`                                       (5.12)

uniformly on the same compact neighborhood.

Multiplying (5.9) by `k/W=1/t` and then by (5.12),

`A_k
 =int_0^infinity g(t)e^{-kF(t)}
   {1+b(t)/k+O(k^-2)}dt`,                                    (5.13)

with

`g(t)=(1+t)/(2pi t^3)`,                                      (5.14)

`b(t)=-1/6-2/t-3/t^2`.                                      (5.15)

The complement of a fixed neighborhood of `t_*` has rate at least `eta+rho` for some fixed `rho>0`. The very-small-`t` region is superexponentially small exactly as in Claim 298. Hence the local expansion controls the full integral to relative order `1/k`.

### 5.3 Laplace coefficient

For a one-dimensional nondegenerate minimum, the first Laplace correction from the amplitude `g` is

`L_1
 = g''/(2gF'')
   - g'F'''/(2g(F'')^2)
   - F''''/(8(F'')^2)
   + 5(F''')^2/(24(F'')^3)`,                                 (5.16)

all quantities evaluated at `t_*`.

At `t_*=1/sqrt(2)`, direct differentiation gives

`F''=8-4sqrt(2)`,

`F'''=-40+24sqrt(2)`,

`F''''=432-288sqrt(2)`,                                      (5.17)

`g'/g=2-4sqrt(2)`,

`g''/g=36-12sqrt(2)`.                                        (5.18)

Substituting into (5.16),

`L_1=65/24-43sqrt(2)/96`.                                    (5.19)

Meanwhile

`b(t_*)=-37/6-2sqrt(2)`.                                    (5.20)

Therefore the total relative `1/k` coefficient is

`a_1=b(t_*)+L_1
    =-83/24-235sqrt(2)/96
    =-(332+235sqrt(2))/96`,                                  (5.21)

exactly the constant in (2.1).

The leading Laplace factor is Claim 298's

`C_*=(1+sqrt(2))/sqrt(2pi(2-sqrt(2)))`.                       (5.22)

Thus

`A_k
 =C_* k^-1/2 e^{-eta k}
  {1+a_1/k+O(k^-2)}.`                                        (5.23)

This is the genuinely stronger asymptotic promised by #3.

---

## 6. Transfer from the Gamma auxiliary model to the exact clean beta integral

It remains to show that no finite-`n` approximation term contaminates the `eps_n/k` coefficient.

At `k=log n+O(1)`, the Claim-298 beta-to-Gamma scaling is needed only on a fixed neighborhood of the saddle `t_*`. On that neighborhood all beta arguments are `O(k/N)` and the log-density expansions have uniform error

`O(k^2/n)`.                                                   (6.1)

The scale and centering discrepancies (`N beta-k`, the difference between `N(1-beta)` and the beta denominator parameter, and the analogous `m,N` offsets) are also `O(poly(k)/n)`. Consequently the first-defect term satisfies the sharper relative comparison

`D_{1,n}
 =A_k{1+O(poly(k)/n)}
 =A_k{1+o(1/k)}.`                                             (6.2)

The mean-replacement beta integral obeys

`M_0=e^{-k}{1+O(k^2/n)}`,                                    (6.3)

and

`k^2/n=o(eps_n/k)`                                           (6.4)

at the critical window, because `eta<1`.

Claim 298 already separated all terms with at least two clean defects. Their exponential rate is

`eta_2=min_{t>0}{delta(t)+2gamma(t)}
       =delta(1/sqrt(3))+2gamma(1/sqrt(3))
       =0.3698641630... > eta`.                              (6.5)

Therefore even after any polynomial factor,

`multiple-clean-defect remainder=o(eps_n/k)`.                (6.6)

Combining (5.23), (6.2)--(6.6) with Claim 298's negligible `x<beta` region gives the exact clean integral expansion

`M_{k,k}
 =e^{-k}{1+C_* eps_n[1+a_1/k+o(1/k)]}.`                      (6.7)

The sparse internal selected-neighbor-edge correction from Claims 286/288/294 remains

`e^{-k} n^{-1+o(1)}`,                                        (6.8)

which is `o(e^{-k}eps_n/k)`. Hence exact vertex isolation has the same expansion, proving (2.3).

The exact finite representation (4.13) independently confirms that no continuum boundary term has been omitted; the asymptotic coefficient itself is obtained from the local beta/Gamma analysis above.

---

## 7. Poisson approximation and components at the second-correction scale

Claim 298 recorded, at `k=log n+O(1)`,

`d_TV(Law(Z_n),Poisson(mu_n))=n^{-1+o(1)}`.                  (7.1)

Since

`eps_n/k=k^-3/2 e^{-eta k}
          =n^{-eta+o(1)}/(log n)^(3/2)`                      (7.2)

and `eta<1`, (7.1) is `o(eps_n/k)`. This proves (2.5).

The quantitative component decomposition of Claim 298 is also strong enough without changing constants:

- threshold-envelope failure: `n^{-0.402585...+o(1)}`;
- component sizes `2--12`: `n^{-1+o(1)}`;
- sizes `13--24`: at worst `n^{-0.3+o(1)}`;
- sizes `>=25`: total `n^{-0.25+o(1)}`.

Because every exponent in this list is strictly larger than

`eta=0.225987...`,                                            (7.3)

each term is still `o(eps_n/k)` after the additional polylogarithmic factor in (7.2). Thus (2.6) holds. No mean-degree inference is used.

From (2.3),

`mu_n
 =lambda_n{1+C_*eps_n+C_*a_1 eps_n/k+o(eps_n/k)}.`           (7.4)

Then

`P(Z_n=0)=e^{-mu_n}+o(eps_n/k)`.                             (7.5)

The quadratic exponential term is negligible because

`eps_n^2/(eps_n/k)=k eps_n ->0`.                              (7.6)

Therefore

`e^{-mu_n}
 =e^{-lambda_n}
  {1-lambda_n C_*eps_n
    -lambda_n C_*a_1 eps_n/k
    +o(eps_n/k)}.`                                            (7.7)

Subtracting the `o(eps_n/k)` probability of a disconnected graph with no isolated vertices proves (2.7).

---

## 8. Correction hierarchy: one direction at a time

At `k=log n+c+o(1)`, the hierarchy now reads:

1. first clean one-defect term:
   `eps_n = k^-1/2 n^-eta e^{-eta c+o(1)}`;
2. second term from the **same one-defect saddle**:
   `eps_n/k = k^-3/2 n^-eta e^{-eta c+o(1)}`;
3. second-clean-defect exponential layer:
   `poly(k)e^{-eta_2 k}`, with `eta_2=0.369864...`;
4. component/interactions/internal-edge layer:
   `n^-1+o(1)` or the quantitative component exponents above.

Thus the second asymptotic term is not generated by pair dependence or a size-two component. It is the ordinary `1/k` Laplace/Watson correction to the same rare one-defect clean saddle.

This also resolves the main ambiguity left at the end of Claim 298: `eps_n/k` is much larger than both `e^{-eta_2 k}` and `n^{-1+o(1)}`.

---

## 9. Adversarial checks and failure modes

I explicitly checked the points most likely to falsify Claim 299.

### 9.1 Could finite-n beta corrections alter `a_1`?

No at the critical scale. Their relative log-density size on the saddle neighborhood is `O(poly(k)/n)=o(1/k)`. Thus they enter strictly after the displayed `a_1/k` term.

### 9.2 Could the `x<beta` clean-integral region compete?

No. Claim 298 bounds it by `exp[-(1/2+o(1))k log k]` relative to the main integral, superexponentially smaller than `eps_n/k` on the `k` scale.

### 9.3 Could the second clean defect beat the `1/k` term?

No. Its exponent `eta_2=0.369864...` is strictly larger than `eta=0.225987...`, while the new second term keeps exponent `eta` and loses only one factor `k`.

### 9.4 Could the expansion of `e^{-mu_n}` create a term at the same scale?

No. `eps_n^2=o(eps_n/k)` by (7.6).

### 9.5 Does the exact coefficient formula itself prove the asymptotic?

No. The coefficient identity is exact but the degree of `P_{N,k}^k` grows with `n,k`; direct asymptotic extraction from it was not simpler. I record this as a genuine route limitation rather than pretending #14 replaced the Laplace argument.

### 9.6 Prior-art honesty

The rate `s-1-log s` and incomplete-gamma asymptotic machinery are classical (DLMF/Temme). The bounded search did not identify the composite constant or the P0456 correction theorem elsewhere. That absence is not a publication-novelty certificate.

No contradiction to Claim 298 or the source-matching Claims 288/289 was found.

---

## 10. Directed peer-audit duty

The directed P03->P04 duty remains active in principle. The newest P04 state is still the rotation-stop record noted in Section 1 and creates no genuinely new theorem beyond packages P03 has already audited. I therefore do **not** fabricate a new peer audit or recycle a previous P04 claim.

---

## 11. Metric / stuck / recovery state

All admitted coefficient metrics remain at their mathematical minimum:

- `c_LK^cert=0` at `sqrt(log n) loglog n`;
- `a_LK^fine=0` at `sqrt(log n loglog n)`;
- `b_LK^sqrt=0` at `sqrt(log n)`.

They remain **SATURATED**, so none contributes an unchanged/stuck count. Claim 299 is an asymptotic refinement, not a new smaller fixed-coefficient metric. HARD recoveries remain `0/2`.

---

## 12. Exact remaining obligations and next attack

Protocol closure remains blocked by independent audits and publication-novelty verification of the source-matching chain, not by lack of a candidate mathematical answer.

Exact obligations:

1. P26 must independently audit the full Claims 288/289 source-matching chain; Claims 291--299 are optional audit kernels, not substitutes for an outside derivation.
2. One distinct OTHER track must independently audit the same full chain.
3. Publication novelty remains UNVERIFIED; current searches are bounded negative evidence only.
4. Claim 299's first outside-audit targets are: the uniform `O(k^-2)` Watson expansion in (5.8)--(5.10); the standard Laplace coefficient sign/convention in (5.16); the `o(1/k)` beta-to-Gamma transfer in (6.2); and the reuse of Claim 298's component exponents at scale `eps_n/k`.
5. The next mathematical correction beyond Claim 299 is open. It should **not** be pursued by merely computing another decimal. One must compare the `1/k^2` coefficient of the same saddle against all other mechanisms and keep the exact finite beta correction separate.

If no outside audit has arrived at the next invocation, use fresh Section-B methods **#1 CHANGE THE CATEGORY, #7 TAKE THE LIMIT, #25 COUNT THE SAME THING TWICE**. A useful target is to recast the one-defect correction as a two-dimensional conditioned-Poisson/Gamma rare-event problem and obtain the first two coefficients from a direct bivariate saddle; then compare that derivation against the one-dimensional Watson/Laplace expansion. Agreement would provide a genuinely independent self-check, while disagreement would expose the weak point.

---

## 13. `ledger_delta` for P26 only

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
    id: P03-P0456-SECOND-CORRECTION-FINITE-REDUCTION-299
    status: PROVED / SELF-AUDIT-STRENGTHENING / SUPPORTING / AUDITS-PENDING / PUBLICATION-NOVELTY-UNVERIFIED
    statement: >-
      If k-log n -> c, eta=sqrt(2)-1-log((1+sqrt(2))/2),
      C_*=(1+sqrt(2))/sqrt(2*pi*(2-sqrt(2))),
      a_1=-(332+235*sqrt(2))/96, and eps_n=k^-1/2 exp(-eta k), then
      P(I_v)=exp(-k){1+C_* eps_n[1+a_1/k+o(1/k)]};
      d_TV(Law(Z_n),Poisson(E Z_n))=o(eps_n/k); and
      P(connectivity)=exp(-lambda_n){1-lambda_n C_* eps_n
      -lambda_n C_* a_1 eps_n/k+o(eps_n/k)}.
  exact_finite_reduction:
    formula: >-
      With P_Nk(y)=sum_{j=k+1}^{N+1}(j-k)binom(N+1,j)y^j and
      [y^J]P_Nk(y)^k=a_J, the clean integral equals
      (N+1)^(-k) sum_J a_J B(J+1,kN+m-J).
    checker_creation_commit: 5bc3fb85b27c8b284cb47ce4894dc8d1720655e3
    checker_blob: 430ddad3ba358d528d3be5e35f404cba952f81b2
    output_creation_commit: 0d49114f36c96a4466344ff91bca2b8b0c14b8b7
    output_blob: a8f01f8829c7918cb12701a7745fde4bffb278d8
    output_terminal: FULL_CLEAN_COEFFICIENT_IDENTITY_PASS
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
  audit_gate:
    independent_passes_found: 0/2
    newest_p26_report: proofnet24/P26-proof-audit-recovery/runs/2026-09-19/2026-09-19_01-59-40__run-report.md
    newest_p26_target: P04/I0101 split-conic Claim 11, not P0456
    source_closed: false
  publication_novelty: UNVERIFIED
  next_state: P0456_ACTIVE_AUDIT_PENDING / CLAIM_299_SECOND_CORRECTION_AUDIT_KERNEL_READY
```

**End of complete run report.**