Model actually ran: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — requested GPT-6 maximum is prompt-only in this runtime, and I do not claim otherwise. SOURCE-WIDE STATUS: OPEN -> OPEN (no universal no-leaf closure). AUXILIARY MOVEMENT: for the nondegenerate offspring family `nu in {2,3}`, the rigorously covered parent-bias endpoint advances from the published all-offspring `m1=2` endpoint `4-2 sqrt(2)=1.171572875...` to `theta_2 in (1.811,1.812)`, with the explicit certified bound `-ell'(lambda) >= 1085/101376` on `1 <= lambda <= 9/5`. Three attacks: (A) two-support escape-derivative cancellation — SUCCESS; (B) finite-depth escape/derivative truncation with explicit contraction — SUCCESS on a subrectangle; (C) port the common super-regeneration coupling — BLOCKED for the new interval because `lambda>1` means child-bias `beta=1/lambda<1`.**

# PROB10-06 — bounded substantive iteration: a two-point offspring derivative bridge

Status: **PARTIAL / OPEN**. This report proves a restricted-family theorem and an adjacent-two-point extension criterion. It does **not** settle the source-wide Lyons–Pemantle–Peres conjecture, and it has not received an independent other-track audit. Novelty is **UNVERIFIED**; the bounded literature search described below is not a priority certificate.

## 1. Owner refocus and preserved R02 handoff

The controlling assignment is `operations/PROB10_2026-09-20.md`, which assigns PROB10-06 to native slot R02 and expressly replaces R02's preceding Randomstrasse/I0095 target.

Before doing new mathematics I wrote and read back the immutable handoff

`runs/R02/20260920T0005Z_owner_refocus_handoff_I0095_to_PROB10-06_4d8c2a71.md`

at commit

`0439a90108047760ebd8d94ffd7d5b76463666da`.

That handoff preserves the actual prior R02 state: I0095 was `PENDING_ADMISSION, not READY`, operationally retired/handoff, with retained explicit sign-matrix certificate `7/sqrt(17)` at order 17 and all older `artifacts/R02/` left intact. Nothing from that target is relabeled as PROB10-06 progress.

## 2. Source statement, assumptions, and bias convention

Primary source navigation used in this run:

- Ben Arous–Fribergh–Sidoravicius, arXiv:1111.5865v1, *A proof of the Lyons-Pemantle-Peres monotonicity conjecture for high biases*;
- He–Wang–Xiang, arXiv:1610.08151v1, later published in *Journal of Applied Probability* 62 (2025), 1044–1052;
- Aïdékon, arXiv:1111.4313 / PTRF 159 (2014), for the speed formula used by He–Wang–Xiang.

The exact source setting is a supercritical Galton–Watson tree whose offspring variable `nu` satisfies

`P(nu=0)=0`, `m=E nu > 1`.

Thus there are **no leaves**. In the parent-bias convention of He–Wang–Xiang, at a non-root vertex with `nu` children,

- parent transition probability is `lambda/(lambda+nu)`;
- each child transition probability is `1/(lambda+nu)`.

The source conjecture is that the limiting speed `ell_lambda` is monotonic nonincreasing for

`0 <= lambda < m`.

The reciprocal child-bias convention is `beta=1/lambda` for `lambda>0`: each child has weight `beta` relative to parent weight 1. Increasing `beta` increases drift **away** from the root, so the equivalent conjectural direction is that `v(beta)` is nondecreasing for `beta>1/m`. I do not interchange these directions below.

Known baselines, not new claims:

- arXiv:1111.5865v1 proves increasing child-bias speed for `beta>=717`, and `beta>=717/d` at minimal degree `d`;
- Aïdékon improved the parent-bias range to `lambda<=1/2`;
- He–Wang–Xiang prove strict decrease for

`0 <= lambda <= m1/(1+sqrt(1-1/m1))`, `m1=min{k>=1:P(nu=k)>0}>=2`;

- Einstein-relation work gives monotonicity in a neighborhood of the recurrence edge `lambda=m`.

A bounded fresh search through 20 September 2026 found the 2025 journal publication of the He–Wang–Xiang low-bias theorem, Bowditch–Tokushige differentiability/analyticity papers, the old high-bias/progeny-distribution papers, and a 2026 regular-tree spectral-radius paper, but no source-wide resolution and no hit for the exact two-point-support calculation below. This is negative search evidence only.

## 3. Repository intake / prior attempt / ownership reconciliation

Intake `P0066` is already marked `attempted_un` / attempted-unsolved in the probability-1000 ledgers. The prior campaign catalog records the following real obstruction, which I therefore do **not** claim as new: for fixed local offspring number `D`, the pointwise radial drift `(D-lambda)/(D+lambda)` decreases with parent bias, but the stationary law of the environment seen by the walk also varies with `lambda`; the previous attempt did not control that measure-change term and did not produce a speed coupling.

I searched for `operations/claims/P0066.md`; that exact canonical claim path is absent on current master, and a repository search found no separate P0066 claim owner. The current owner directive nevertheless explicitly assigns native slot R02 to PROB10-06. I therefore take only the following delimited route: **Aïdékon/He–Wang–Xiang escape-probability differentiation specialized to two adjacent offspring values**, complementary to the older stationary-environment drift attempt. No other claim file is overwritten and no old attempt is called new.

`POSTED.md` was also consumed; it contains no posted solution of P0066 and instructs workers not to treat restricted results as source closure.

## 4. New idea before code

The pre-code mathematical note is

`artifacts/prob10_2026-09-20/PROB10-06/20260920T0012Z_two_point_escape_derivative_idea.md`

created before the checker. The central observation is that for a two-point offspring law, the four expectation terms in the He–Wang–Xiang derivative criterion collapse to one cross-difference. That creates a factor `p(1-p)` and allows an AM–GM gain that is absent from the general minimal-degree argument.

## 5. First unresolved finite-support family

Fix

`P(nu=2)=1-p`, `P(nu=3)=p`, `0<p<1`.

Then `m=2+p`, `m1=2`, `m2=3`; the tree is supercritical, bounded-support, and has no leaves. The general 2025 theorem only guarantees strict speed decrease through

`lambda_0 = 2/(1+sqrt(1/2)) = 4-2sqrt(2) = 1.171572875...`.

I work on `1<=lambda<2`, which overlaps the known interval but extends beyond it.

Let `B=beta(e,lambda)` denote the quenched escape probability from a vertex before its parent, and let

`U=-dB/dlambda`.

He–Wang–Xiang Lemmas 2.3–2.4 give, almost surely for `1<=lambda<2`,

`1-lambda/2 <= B <= 1-lambda/3`,

`0 < U <= B/(2-lambda)`.

Let `B_0,...,B_k` be iid copies of `B`, with corresponding `U_i`, and define

`S_k = sum_{i=0}^k B_i`,

`D_k = lambda-1+S_k`,

`c_k = E[(1/(k+1))*S_k/D_k]`,

`h_k = E[(1/(k+1))*sum_{i=0}^k (B_i+(lambda-1)U_i)/D_k^2]`.

Because `B_i'= -U_i`, the numerator in `h_k` is exactly `B_i+(1-lambda)B_i'` from criterion (2.8).

Set

`A=(1-p)*2*c_2+p*3*c_3`,

`C=(1-p)*c_2+p*c_3`,

`H1=(1-p)*h_2+p*h_3`,

`Hnu=(1-p)*2*h_2+p*3*h_3`.

The symmetrized Aïdékon formula is

`ell_lambda = (A-lambda*C)/(A+lambda*C)`.

### Lemma 1 — exact two-support cancellation

`A*H1-C*Hnu = p(1-p)(c_3*h_2-c_2*h_3)`.

**Proof.** Expand both products. The `(1-p)^2` terms are both `2 c_2 h_2`; the `p^2` terms are both `3 c_3 h_3`. The mixed coefficient is

`2 c_2 h_3+3 c_3 h_2 - 3 c_2 h_3-2 c_3 h_2 = c_3 h_2-c_2 h_3`.

Multiplication by `p(1-p)` gives the identity. ∎

This is the mechanism absent from the previous repository attempt: the environment-measure correction is not discarded; for two offspring values it is algebraically isolated.

### Lemma 2 — one-sided bounds on the two branch terms

Put

`Q=(2-lambda)(2-lambda/2)`,

`V=3-lambda/3`.

Then for `1<=lambda<2`,

`h_2 <= c_2/Q`,

`h_3 >= c_3/V`.

**Proof.** Since `U_i<=B_i/(2-lambda)`,

`B_i+(lambda-1)U_i <= B_i*(1+(lambda-1)/(2-lambda)) = B_i/(2-lambda)`.

For `k=2`, the lower escape bound gives

`D_2 >= lambda-1+3(1-lambda/2)=2-lambda/2`.

Therefore pointwise

`(1/3)*sum(B_i+(lambda-1)U_i)/D_2^2`

`<= (1/(2-lambda))*(1/D_2)*(1/3)*S_2/D_2`

`<= (1/Q)*(1/3)*S_2/D_2`.

Taking expectations proves `h_2<=c_2/Q`.

For `k=3`, `U_i>0` and `lambda>=1`, so `B_i+(lambda-1)U_i>=B_i`. The upper escape bound gives `B_i<=1-lambda/3`, hence

`D_3 <= lambda-1+4(1-lambda/3)=3-lambda/3=V`.

Thus `1/D_3>=1/V`, and

`(1/4)*sum(B_i+(lambda-1)U_i)/D_3^2 >= (1/V)*(1/4)*S_3/D_3`.

Taking expectations proves `h_3>=c_3/V`. ∎

### Lemma 3 — derivative identity and quantitative lower bound

Let

`a(lambda)=1/Q-1/V`.

Then for every `0<p<1` and `1<=lambda<2`,

`-ell_lambda' >= [4-(lambda/2)*a(lambda)]/(3+lambda)^2`.

In particular `ell_lambda'<0` whenever

`F(lambda):=2/lambda-(1/4)*a(lambda)>0`.

**Proof.** First note `Q<V`: because `lambda>=1`,

`Q=((2-lambda)(2-lambda/2)) <= 2-lambda/2 < 3-lambda/3=V`,

so `a(lambda)>0`.

Let `x=(1-p)c_2` and `y=p c_3`. Then `C=x+y`, and by Lemmas 1–2,

`A H1-C Hnu <= p(1-p)c_2 c_3 a(lambda)=x y a(lambda)`.

AM–GM gives `xy<=(x+y)^2/4=C^2/4`. Also `2C<=A<=3C`.

Differentiate `c_k`. Since `S_k'= -sum U_i` and `D_k'=1+S_k'`,

`d/dlambda (S_k/D_k) = -[S_k+(lambda-1)sum U_i]/D_k^2`,

so `c_k'=-h_k`. Consequently

`A'=-Hnu`, `C'=-H1`,

and

`A'C-AC' = A H1-C Hnu`.

Differentiating

`ell=(A-lambda C)/(A+lambda C)`

gives the exact identity

`-ell' = 2 lambda * [A C/lambda-(A H1-C Hnu)]/(A+lambda C)^2`.

The preceding estimates imply

`A C/lambda-(A H1-C Hnu)`

`>= C^2[2/lambda-a(lambda)/4]`.

Finally `A+lambda C <= (3+lambda)C`, hence

`-ell' >= 2 lambda [2/lambda-a/4]/(3+lambda)^2`

`= [4-(lambda/2)a]/(3+lambda)^2`.

If `F(lambda)>0`, the right-hand side is strictly positive. ∎

## 6. Explicit new covered interval for `{2,3}`

For `d=2`, clearing positive denominators shows that `F(lambda)>0` on the interval from 1 up to the first zero in `(1,2)` of

`P(lambda)=-5 lambda^3+104 lambda^2-490 lambda+576`.

On `[1,2]`, `P''(lambda)=-30lambda+208>0`, while `P'(2)=-134<0`; hence `P'<0` throughout `[1,2]`, so there is at most one root. Exact arithmetic gives

`P(1811/1000)=622069/200000000 >0`,

`P(1812/1000)=-497877/3125000 <0`.

Thus there is a unique

`theta_2 in (1.811,1.812)`

(numerically `1.811019...`) such that the new derivative argument proves

`ell_lambda'<0` for `1<=lambda<theta_2`.

Combining with the published low-bias theorem yields the complete rigorously covered interval for this nondegenerate family:

`0 <= lambda < theta_2`.

This advances the family-specific endpoint from `4-2sqrt(2)=1.171572875...` to `theta_2>1.811`.

### Certified sign lower bound on a closed interval

On `1<=lambda<=9/5`,

`Q=(2-lambda)(2-lambda/2) >= 11/50`,

and because `lambda>=1`, `V=3-lambda/3<=8/3`, so `1/V>=3/8`. Hence

`a(lambda)<=50/11-3/8=367/88`.

Also `lambda/2<=9/10` and `(3+lambda)^2<= (24/5)^2=576/25`. Lemma 3 therefore gives the fully explicit uniform bound

`-ell_lambda' >= [4-(9/10)(367/88)]/(576/25)`

`= 1085/101376`

`= 0.01070... >0`.

This is the run's requested certified sign lower bound. It is not inferred from simulation.

## 7. Extension of the same mechanism to adjacent two-point offspring laws

The cancellation is not specific to `{2,3}`. Fix integer `d>=2` and

`P(nu=d)=1-p`, `P(nu=d+1)=p`, `0<p<1`.

For `1<=lambda<d`, the published escape/derivative bounds give

`1-lambda/d <= B <= 1-lambda/(d+1)`,

`0<U<=B/(d-lambda)`.

Define `c_d,h_d,c_{d+1},h_{d+1}` exactly as above. The same expansion gives

`A H1-C Hnu=p(1-p)(c_{d+1}h_d-c_d h_{d+1})`.

Now put

`delta_d=d-lambda/d`,

`Q_d=(d-lambda)*delta_d/(d-1)`,

`V_d=d+1-lambda/(d+1)`.

The degree-`d` lower denominator and derivative upper bound imply `h_d<=c_d/Q_d`; the degree-`d+1` upper denominator and `U>=0` imply `h_{d+1}>=c_{d+1}/V_d`. Since `lambda>=1`, `d-lambda<=d-1`, so

`Q_d <= d-lambda/d < d+1-lambda/(d+1)=V_d`,

and `a_d:=1/Q_d-1/V_d>0`.

Repeating Lemma 3 but using `dC<=A<=(d+1)C` yields the explicit sufficient condition and quantitative bound

`-ell_lambda' >= [2d-(lambda/2)a_d]/(d+1+lambda)^2`,

whenever

`d/lambda - a_d/4 > 0`.

This is a rigorously proved adjacent-two-point extension criterion. I have not found it in the bounded search, but **novelty remains UNVERIFIED**.

## 8. Second attack — explicit finite-depth truncation, not an assumed derivative sign

The proof above legitimately imports the published infinite-tree differentiability lemma. To address the owner priority directly, I also bounded truncation error for the escape recursion itself on a concrete rectangle.

Restrict temporarily to

`0<p<=1/4`, `1<=lambda<=9/5`.

Let `B_n` be the level-`n` approximation with boundary value 1 and `B` the infinite escape probability, coupled on the same tree. The recursion is

`f(S)=S/(lambda+S)`.

Because `B_n>=B>=1-lambda/2`, a degree-2 node has total child Lipschitz constant at most

`L_2=2lambda/(lambda+2(1-lambda/2))^2=lambda/2<=9/10`.

A degree-3 node has total child Lipschitz constant at most

`L_3=3lambda/(lambda+3(1-lambda/2))^2`

`<= (27/5)/(21/10)^2=60/49`.

Thus, with `e_n=E|B_n-B|`,

`e_n <= rho e_{n-1}`,

where, because `p<=1/4`,

`rho <= (3/4)(9/10)+(1/4)(60/49)=1923/1960<1`.

Since `e_0<=1`,

`E|B_n-B| <= (1923/1960)^n`.

For the derivative, write `U_n=-B_n'` and `U=-B'`. The differentiated recursion is

`U_n = lambda/(lambda+S_n)^2 * sum U_{n-1,i} + S_n/(lambda+S_n)^2`.

The published finite-depth bound gives `U_n,U<=1/(2-lambda)<=5`. Comparing the two recursions and differentiating the two coefficient functions in `S`, using `lambda+S>=2`, `2-lambda>=1/5`, and degree at most 3, gives the conservative one-step estimate

`f_n <= rho f_{n-1}+21 e_{n-1}`,

where `f_n=E|U_n-U|`. Since `f_0<=5` and `e_{j}<=rho^j`, induction yields

`E|U_n-U| <= 5 rho^n + 21 n rho^(n-1)`.

Moreover, throughout this rectangle the speed-formula denominators are uniformly bounded away from zero: for degree 2,

`D_2>=2-lambda/2>=11/10`,

and for degree 3,

`D_3>=3-lambda>=6/5`.

Therefore finite-depth expectations and their first derivatives converge with an explicit error and no hidden small denominator on this subrectangle. This is auxiliary mechanism control; it is not required to label the source solved.

## 9. Third attack — regeneration coupling and exact obstruction

I also tried to port the common super-regeneration method of arXiv:1111.5865 to the new interval. That paper explicitly fixes **child bias `beta>1`** and builds the common regeneration structure from a one-dimensional `beta`-biased walk whose regeneration probability contains a factor proportional to `beta-1`.

Our new region is **parent bias `lambda>1`**, hence reciprocal child bias

`beta=1/lambda<1`.

Thus the exact one-dimensional reference walk used by the high-child-bias coupling has the wrong drift direction and its stated super-regeneration construction does not cover this interval. This is a precise obstruction, not a claim that no regeneration proof can exist. A successful regeneration attack here would need a different reference process or a different common renewal event.

## 10. Exact checker and actual output

Only after writing the mathematical idea did I create and execute the exact checker:

- `artifacts/prob10_2026-09-20/PROB10-06/20260920T0012Z_two_point_escape_derivative_check.py`
- `artifacts/prob10_2026-09-20/PROB10-06/20260920T0012Z_two_point_escape_derivative_check.out`

The executed output is `PASS` and records exactly:

- `Q(9/5)=11/50`;
- `V(9/5)=12/5`;
- `a(9/5)=545/132`;
- derivative-criterion margin at `9/5`: `125/1584>0`;
- uniform derivative lower bound on `[1,9/5]`: `1085/101376>0`;
- exact root bracket `theta_2 in [1811/1000,1812/1000]` via opposite polynomial signs;
- truncation contraction cap `rho=1923/1960<1`.

This is a **self-check**, not an independent audit.

## 11. Metrics: source-level and auxiliary kept separate

### Source-wide metric

Target: prove monotonicity for **every** supercritical no-leaf Galton–Watson offspring law throughout `0<=lambda<m`.

Before: OPEN / known partial low-bias and near-critical regimes.

After: **OPEN / unchanged at source-wide scope**. This run does not add an all-offspring interval beyond the published theorem and does not close the conjecture.

### Auxiliary mechanism metric

Frozen family: `P(nu=2)=1-p`, `P(nu=3)=p`, `0<p<1`.

Before family-specific rigorously covered endpoint inherited from the all-offspring theorem:

`lambda_0=4-2sqrt(2)=1.171572875...`.

After:

`theta_2`, unique root in `(1.811,1.812)` of `-5 lambda^3+104 lambda^2-490 lambda+576=0`.

Certified sign margin:

`-ell'(lambda)>=1085/101376` for every `0<p<1` and `1<=lambda<=9/5`.

Auxiliary truncation rectangle:

`0<p<=1/4`, `1<=lambda<=9/5`, with

`E|B_n-B| <= rho^n`,

`E|U_n-U| <= 5 rho^n+21 n rho^(n-1)`,

`rho=1923/1960`.

## 12. Remaining full-scope gap

Even for the first family `{2,3}`, this run leaves the interval

`theta_2 <= lambda < 2+p`

unsettled except for the separately known qualitative neighborhood of `m=2+p`. The present escape-derivative bound itself stops before `lambda=2` because the imported estimate `U<=B/(2-lambda)` degenerates there. Bridging `lambda>=2` requires a new lower escape estimate / derivative control adapted to the actual two-point law rather than the minimal-degree comparison.

For general no-leaf offspring laws, the two-support cancellation disappears and the original environment-measure term remains a genuine multi-direction covariance problem. That is the main source-wide gap.

A promising next iteration inside this parent problem is therefore not another simulation. It is one of:

1. keep `{2,3}` but replace the `m1=2` derivative bound near `lambda=2` by a distribution-sensitive regeneration/escape estimate;
2. exploit the adjacent-support formula quantitatively for `{d,d+1}` and identify a denominator/derivative estimate that remains nondegenerate through `lambda=d`;
3. seek a covariance ordering that decomposes a finite-support law into adjacent two-point transfers while controlling the cross-terms.

## 13. Consumed repository state and delivery discipline

Consumed/reconciled in this bounded run:

- `operations/PROB10_2026-09-20.md`;
- current `POSTED.md`;
- prior P0066 intake/rank entries and `probability_campaign_2026_09/report_2026-09-12/chapters/catalog_01_codex_P0001_P0150.md` attempt summary;
- missing exact path `operations/claims/P0066.md` plus repository ownership search;
- newest pre-refocus R02 report `runs/R02/20260919T2210Z_successor_gate_linear_dim6_priorart_cutoff_17_22_30_8a6f2c4d.md`;
- immutable I0095 handoff at commit `0439a90108047760ebd8d94ffd7d5b76463666da`;
- current master after artifact writes: `139e9ea4e1647792ddb1545ab5d583e7710ec46b`.

No scheduler state, notification state, email, Drive, public posting, workflow, permission, purchase, peer file, shared ledger, or force push was used or changed.

## 14. Structured ledger delta

```yaml
ledger_delta:
  worker: R02
  target: PROB10-06
  intake: P0066
  source_status_before: OPEN_PARTIAL
  source_status_after: OPEN_PARTIAL
  source_wide_closure: false
  actual_model: GPT-5.6 Sol
  reasoning_level: UNVERIFIED
  requested_model: GPT-6 maximum
  requested_model_verified: false
  bias_convention: parent_lambda_increases_drift_to_root__child_beta_equals_1_over_lambda_increases_drift_away
  no_leaves: true
  first_family: "P(nu=2)=1-p, P(nu=3)=p, 0<p<1"
  family_endpoint_before: "4-2*sqrt(2) ~= 1.171572875"
  family_endpoint_after: "theta_2 in (1.811,1.812), P(theta_2)=0"
  threshold_polynomial: "-5*l^3+104*l^2-490*l+576"
  certified_closed_interval: "1 <= lambda <= 9/5"
  certified_sign_lower_bound: "-ell'(lambda) >= 1085/101376"
  adjacent_two_point_extension: true
  truncation_subrectangle: "0<p<=1/4, 1<=lambda<=9/5"
  truncation_rho: "1923/1960"
  finite_escape_error: "E|B_n-B| <= rho^n"
  finite_derivative_error: "E|U_n-U| <= 5*rho^n+21*n*rho^(n-1)"
  approaches:
    - two_support_escape_derivative_cancellation_SUCCESS
    - finite_depth_denominator_and_truncation_SUCCESS_SUBRECTANGLE
    - common_super_regeneration_port_BLOCKED_WRONG_DRIFT_FOR_beta_lt_1
  self_check: PASS
  independent_audit: NONE_THIS_RUN
  novelty: UNVERIFIED
  old_R02_target_handoff_commit: 0439a90108047760ebd8d94ffd7d5b76463666da
  scheduler_changed: false
  email_or_drive_used: false
  public_posting: false
```
