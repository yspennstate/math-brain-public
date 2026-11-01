Runtime model exposed by this run: **GPT-5.6 Sol**. Requested GPT-6/maximum is not a configurable/authenticated native selector here; reasoning-effort telemetry is **UNVERIFIED**.

# PROB10-03 — R14 bounded iteration: cancellation-free inner KL compiler for the third-full nested-Schur route

Repository / branch: private `yspennstate/math-open-problems` / `master`.  
Status: **OPEN / PARTIAL / NO R14 SOURCE-ENDPOINT MOVEMENT / NEW EXACT POSITIVE THERMODYNAMIC COMPILER**.

## 1. Contract, continuity, ownership, and consumed updates

I first read the controlling PROB10 contract, current posted-exclusion registry, the current Campbell--O'Rourke claim and immutable refocus handoff, the newest own R14 report, and the newest materially relevant T03 companion reports. The important consumed objects are:

- `operations/PROB10_2026-09-20.md`, blob `6f0fcee836d93371d43b84af1a55150fedc80779`;
- root `POSTED.md`, blob `affe1b5f31545bb15be9ba2580548e9e88095e1b`;
- `operations/claims/CAMPBELL-OROURKE-2022-Q1.8.md`, blob `d8fe3a276b9c59d4608a113c0d77ba5b5dc8717d`;
- immutable handoff `artifacts/prob10_2026-09-20/PROB10-03/20260919T2354Z_campbell_q18_r14_handoff.md`, blob `edaa787e384c28a4b5a658dbba80f664cde75882`, preserving Campbell--O'Rourke Q1.8, inherited metric `S=5`, and navigation point `3846db33296cfb6eea59ff7c488929087c7b62a2`;
- newest preceding own report `runs/prob10_2026-09-20/PROB10-03/20260920T1432Z_r14_parameter_face_overlap_cgmt_4c2a.md`, blob `fde6c4a24563cde2fa412b6c8489a51e550a05b9`;
- NM13-07 positive-gap all-moment compiler `proofnet24/NM13-07/progress-perceptron/runs/2026-09-20/2026-09-20__t03-posgap-dimensionless-allmoment-alpha12319634446195.md`, blob `4aef635b5bbb4c53972755f0c40fe43714cf0e68`;
- NM13-03 Schur branch-crossing report `proofnet24/NM13-03/progress-perceptron-theory/runs/2026-09-20/2026-09-20__t03-schur-branch-crossing-alpha12319634446194.md`, blob `bba5d3be7381c0a2437b0f75601236f74c10df7c`;
- a **concurrent update detected during this run**, NM13-07's stronger pivoted-x nested-Schur cascade `proofnet24/NM13-07/progress-perceptron/runs/2026-09-20/2026-09-20__t03-pivoted-x-schur-cascade-alpha12319634446193.md`, blob `e3062e200bf74d80e092432d3931a901a1017b58`.

The idea note for this run was written **before code**, as required:

`artifacts/prob10_2026-09-20/PROB10-03/20260920T1454Z_r14_piecewise_schur_idea.md`, creation commit `2194f5e9846c0b05e7a55316efc80d536a03d914`.

That note initially chose a piecewise three-dimensional Schur continuation as the primary route. While this run was in progress, NM13-07 independently committed the stronger pivoted-x nested-Schur cascade. I therefore do **not** claim the branch architecture as new R14 progress and do not overwrite any companion ownership. The present report pivots to a complementary missing ingredient of that cascade: a cancellation-free exact evaluation formula for its difficult inner KL term `D_H`.

No scheduler/cadence/enabled-state, canonical claim, workflow, permission, email, Drive object, public posting, or force push is changed.

## 2. Frozen source target and probability convention

For each fixed `alpha`, put

`M=floor(alpha N)`, `g_1,...,g_M iid N(0,I_N)`,

and ask for existence of `sigma` satisfying

`||sigma||_2=sqrt(N)`,

`<g_a,sigma> >= -sqrt(N)` for every `a<=M`.

A rigorous lower endpoint `alpha_L` means that for every fixed `alpha<alpha_L`, the satisfiability probability tends to one as `N->infinity`. A rigorous upper endpoint `alpha_U` means that for every fixed `alpha>alpha_U`, the satisfiability probability tends to zero. No boundary convention at equality is silently inferred.

The owner's posted Ising/zero-margin perceptron work is a different problem. A smaller-radius construction, ball relaxation, restricted ansatz, floating finite-lift root, algorithmic-class threshold, or replica/full-RSB numerical value is not promoted to an endpoint here.

### Source-scope refresh

The bounded current source check remains consistent with **OPEN / PARTIAL**:

1. El Alaoui--Sellke, `https://arxiv.org/abs/2010.15811`, use the same ambient spherical Gaussian model, but the negative-margin algorithm described there uses the conjectural FRSB/Parisi structure and outputs a feasible vector on radius `sqrt(qbar N)` with `qbar<1`; this is not the exact full-radius threshold theorem required here.
2. Stojnic, `https://arxiv.org/abs/1306.3980`, supplies rigorous negative-spherical-perceptron random-duality bounds/mechanisms, not an already closed exact `kappa=-1` threshold.
3. Stojnic, `https://arxiv.org/abs/2312.16531`, gives a fully lifted RDT characterization under the full stationarity system and explicitly notes the substantial numerical work needed to operationalize it. The repository therefore continues to require a directed root/stationarity certificate before treating a finite-level stationary value as an endpoint.
4. The retained later companion sources -- Montanari--Zhong--Zhou `https://arxiv.org/abs/2110.15824`, the full-RSB/jammed-Parisi calculations, and Huang--Sellke--Sun `https://arxiv.org/abs/2608.29416` -- do not by themselves supply unrestricted exact-radius closure at `kappa=-1`.

This is a dated bounded status check, not a worldwide priority certificate.

## 3. Source metric and concurrent attribution

At the beginning of the mathematical work, the newest consumed NM13-03 source endpoint was

`alpha_U=12.319634446194`.

During this run, the concurrent NM13-07 pivoted-x report moved the review-pending directed endpoint by another `10^-12` to

`alpha_U=12.319634446193`.

That movement belongs **entirely to NM13-07**, not R14. After consuming that update, the current repository-supported review-pending bracket is

`alpha_L = 6.30297437506`,

`alpha_U = 12.319634446193`,

`W = alpha_U-alpha_L = 6.016660071133`.

For **R14 attribution in this run**:

`source metric before = 6.016660071133`,

`source metric after  = 6.016660071133`.

Thus R14 source-level movement is **zero**. The progress below is mechanism progress toward the non-microscopic complete-third certificate and is kept separate.

## 4. Three materially different attacks and the required method change

Several recent R14 iterations have left the source bracket unchanged. This run therefore changes method rather than producing another renamed local bound.

### Attack A — piecewise 3D Schur continuation

The idea note proposed gluing short `m`-slabs, each with a certified three-dimensional branch, instead of demanding one large branch tube. Numerical scouts show that widening from `m0 +/- 0.001` to `m0 +/- 0.01`, `+/-0.02`, and `+/-0.04` greatly amplifies the final `RH` sign margin while retaining reasonable local conditioning.

However, before this could be claimed as the main new architecture, the concurrent NM13-07 worker committed the stronger **pivoted-x nested-Schur cascade**, which triangularizes the full inclusion more aggressively and puts the weak direction in the final scalar `x` crossing. I therefore treat this attack as consumed/superseded architecture and do not duplicate ownership.

### Attack B — generic entropy-cage-only certification

The matched-Gaussian/Stein/variance-deficit cages are mathematically valid, but I tested the negation of the hope that they alone resolve the final `RH` sign. They do not.

At the numerical-only positive-gap branch (`delta=10^-3`), the induced `RH` uncertainty from the generic `D_H` cage exceeds the scalar sign margin by factors approximately

- `328` and `353` on the two sides of the `m0 +/- 0.01` window;
- `158` and `183` on the two sides of `m0 +/- 0.02`;
- `72.8` and `97.6` on the two sides of `m0 +/- 0.04`.

So merely widening the crossing interval does not make a generic entropy cage into a sign certificate. This is the concrete obstruction required by the contract: the remaining proof needs either a direct rigorous `D_H` evaluation or a much more problem-specific inequality.

### Attack C — positive thermodynamic compiler for the inner hinge KL

This is the chosen and completed new route. It eliminates the subtractive log-partition expression for the inner KL entirely and replaces it by one compact scalar integral with an everywhere nonnegative explicit integrand.

This attack is complementary to the new nested-Schur cascade rather than duplicating it: the cascade isolates `RH` as its final scalar obligation, and `RH` contains exactly the `D_H` term for which cancellation-free outward control is needed.

## 5. Main exact theorem — positive inner-KL compiler

The dimensionless complete-third kernel has

`F_a(t)=E_H exp[-a(t+H)_+^2/2]`,

where `H~N(0,1)` and `a>0` (`a=xi-1` in the positive-gap compiler). Let `Y=t+H`, so the reference law is

`P_t=N(t,1)`.

Define the tilted law

`d rho_{t,a}/dP_t (y) = exp[-a y_+^2/2]/F_a(t)`.

Let

`K(t,a)=D(rho_{t,a} || P_t)`.

Translation identifies this with the inner `H`-KL used by the complete-third compiler.

For `s>=0`, write

`r_s=1+s`,

`A(t)=Phi(-t)`,

`B_s(t)=r_s^(-1/2) exp[-s t^2/(2r_s)] Phi(t/sqrt(r_s))`,

`F_s(t)=A(t)+B_s(t)`,

`q_s(t)=B_s(t)/F_s(t)`.

Conditional on `Y>0` under `rho_{t,s}`, the law is exactly

`N(mu_s,sigma_s^2) | {Y>0}`,

where

`mu_s=t/r_s`, `sigma_s^2=1/r_s`.

Let `M_k(s)=E[Y^k | Y>0]` under this truncated Gaussian. Put

`z_s=t/sqrt(r_s)`, `lambda_s=phi(z_s)/Phi(z_s)`.

Then

`M_1(s)=mu_s+sigma_s lambda_s`,

and for every `k>=2`,

`M_k(s)=mu_s M_{k-1}(s)+(k-1)sigma_s^2 M_{k-2}(s)`.          (5.1)

In particular `M_2,M_4` are explicit in elementary operations plus `Phi,phi`.

### Theorem R14-T03-POSITIVE-INNER-KL

For every `t in R` and `a>=0`,

`boxed:`

`K(t,a)`
` = (1/4) int_0^a s [ q_s(t) M_4(s) - q_s(t)^2 M_2(s)^2 ] ds`      (5.2)

` = (1/4) int_0^a s { q_s(t)[M_4(s)-M_2(s)^2]`
`                     + q_s(t)[1-q_s(t)] M_2(s)^2 } ds`.          (5.3)

Every term in the integrand of (5.3) is nonnegative. Hence

`K(t,a)>=0`,

`partial_a K(t,a)`
` = (a/4){q_a Var_+(Y^2)+q_a(1-q_a)M_2(a)^2} >=0`.             (5.4)

Moreover the KL has the exact sign-mixture decomposition

`K(t,a)=d_Ber(q_a(t)||Phi(t)) + q_a(t) K_+(t,a)`,               (5.5)

where `K_+(t,a)` is the KL from the positive-side tilted truncated Gaussian to the reference `N(t,1)|{Y>0}` and

`K_+(t,a)=(1/4) int_0^a s [M_4(s)-M_2(s)^2] ds`.                (5.6)

Thus the difficult inner KL is reducible to one positive compact integral with fully explicit truncated-normal moments, with no subtraction of a log partition from an energy expectation.

### Proof

Set

`V(Y)=Y_+^2/2`,

`Z(s)=E_{P_t} exp[-sV]=F_s(t)`.

The tilted law is `rho_{t,s}` and

`K(t,s)=D(rho_{t,s}||P_t)`
`      =-s E_s V-log Z(s)`.                                    (5.7)

Standard exponential-family differentiation is elementary here:

`(log Z)'(s)=-E_s V`,

`d/ds E_s V=-Var_s(V)`.

Differentiating (5.7), the two first-order expectation terms cancel and give

`dK/ds=s Var_s(V)`.                                            (5.8)

Since `K(t,0)=0`,

`K(t,a)=int_0^a s Var_s(V) ds`.                                (5.9)

It remains only to write the variance explicitly. The tilt is identically one on `Y<=0`; on `Y>0`, completing the square gives

`exp[-(y-t)^2/2-sy^2/2]`
` = exp[-s t^2/(2(1+s))]`
`   exp[-(1+s)(y-t/(1+s))^2/2]`.

Therefore the unnormalized positive mass is exactly `B_s(t)` above, the tilted sign probability is `q_s=B_s/(A+B_s)`, and the positive conditional law is the stated truncated `N(mu_s,sigma_s^2)`.

Because `V=0` on the negative side and `V=Y^2/2` on the positive side,

`E_s V = q_s M_2(s)/2`,

`E_s V^2 = q_s M_4(s)/4`.

Thus

`Var_s(V)`
` = [q_s M_4(s)-q_s^2 M_2(s)^2]/4`,                            (5.10)

which inserted into (5.9) proves (5.2). Splitting

`q M_4-q^2 M_2^2`
` = q(M_4-M_2^2)+q(1-q)M_2^2`

proves the manifestly positive form (5.3) and derivative statement (5.4).

For the moment recurrence, integrate the positive truncated Gaussian density by parts. The boundary term appears only for `k=1`, giving

`M_1=mu+sigma phi(mu/sigma)/Phi(mu/sigma)`.

For `k>=2`, the factor `y^{k-1}` kills the boundary at zero and yields (5.1).

Finally partition both reference and tilted laws by the sign event. On `Y<=0` the conditional laws coincide exactly. The KL chain rule therefore gives

`K=d_Ber(q||p)+qK_+`, `p=Phi(t)`,

which is (5.5). Conditional on `Y>0`, the same one-parameter exponential-tilt calculation uses `V_+(Y)=Y^2/2` and gives

`dK_+/ds=s Var_+(Y^2/2)`.

Integrating from zero proves (5.6). QED.

## 6. Why this directly attacks the lost uniform-control step

In the positive-gap complete-third system, the final c-sector quantity is

`D_H = m E_V < K(T,a) >_U`,

with `a=xi-1`, the `U` expectation taken under the already defined tilted outer law, and `V` Gaussian outside it.

Previously one evaluates the pointwise inner term as

`K(t,a)=-(a/2) E_{rho_{t,a}}Y_+^2 - log F_a(t)`,               (6.1)

which is correct but subtractive. Uniform outward interval arithmetic must then separately enclose an energy and a log partition and survive their cancellation.

Theorem (5.2)--(5.3) instead makes the innermost layer a compact `s in [0,a]` integral of an explicitly nonnegative function built only from

`q_s(t), M_2(s), M_4(s), Phi, phi`.

There are three concrete certification advantages:

1. **No inner KL cancellation.** Lower and upper interval sums can be accumulated directly from positive pieces; an outward lower bound cannot become spuriously negative because two large enclosures were subtracted.
2. **No hidden Gaussian H quadrature.** The entire `H` integration has been done analytically. Only the one-dimensional compact thermodynamic variable `s`, followed by the already existing `U,V` layers, remains.
3. **Direct derivative sign.** Equation (5.4) gives exact monotonicity in the hinge stiffness at fixed `t`, which can be used for parameter-face enclosure rather than differentiating a nested log-partition implementation.

This does not by itself certify the final nested-Schur crossing: the outer tilted `U,V` integrations, parameter dependence of `T`, and the branch boxes still need outward control. But it removes one of the principal cancellation mechanisms from the exact `RH` residual.

## 7. Executed tests and falsification results

The code/output preserved for this run are:

- `artifacts/prob10_2026-09-20/PROB10-03/20260920T1454Z_r14_piecewise_kl.py`;
- `artifacts/prob10_2026-09-20/PROB10-03/20260920T1454Z_r14_piecewise_kl.out`;
- `artifacts/prob10_2026-09-20/PROB10-03/20260920T1454Z_r14_global_positive_kl.py`;
- `artifacts/prob10_2026-09-20/PROB10-03/20260920T1454Z_r14_global_positive_kl.out`.

The first checker numerically scouts the three-dimensional `m` branch and quantifies the generic entropy-cage obstruction. It also checks the independent sign-mixture identity (5.5) and the positive-side path (5.6) over `t=-8,-4,-2,-1,0,1,2,4,8`. Its output ends

`ALL_NUMERICAL_SELF_CHECKS_PASS`.

The second checker directly compares the global positive path (5.2) with the independent sign-chain evaluation over the same grid at a representative positive-gap stiffness `a=2.526254483411193`. The maximum displayed discrepancy is `1.421e-14`; its output ends

`ALL_POSITIVE_KL_CHECKS_PASS`.

These are **self-checks**, not independent audits.

### Numerical-only branch scout

For context only, on the inherited `delta=10^-3` m-branch the GH80--GH200 signs remained stable on windows as wide as `m0 +/- 0.04`. For example at GH200:

- `m=m0-0.01`: `RH=-6.82479065e-6`, `alpha≈12.31719927663`;
- `m=m0+0.01`: `RH=+6.70362524e-6`, `alpha≈12.31567687204`;
- `m=m0-0.04`: `RH=-2.83022667e-5`, `alpha≈12.31957736371`;
- `m=m0+0.04`: `RH=+2.63011115e-5`, `alpha≈12.31344303374`.

No number in this paragraph is promoted to a source endpoint. The concurrent pivoted-x cascade is now the preferred branch architecture anyway.

### Negation test: generic cages are too wide

The same checker converts the existing generic `D_H` entropy-cage width into the corresponding `RH` uncertainty. Even on the widest tested m-window the cage is still roughly `73--98` times wider than the crossing sign. On the `+/-0.01` window it is roughly `328--353` times wider. Therefore the proposition

> “the existing generic entropy cage, by itself, is enough to certify the final scalar sign once the branch interval is widened”

is numerically falsified by large margins.

This is why the exact positive-path compiler is not cosmetic: a direct `D_H` evaluation layer is required unless a much sharper perceptron-specific inequality is found.

## 8. Auxiliary movement, source movement, and remaining full-scope gap

### Source movement attributable to R14

None:

`6.016660071133 -> 6.016660071133`.

The concurrent `10^-12` source microstep to `alpha_U=12.319634446193` is credited to NM13-07 and merely consumed here.

### Auxiliary mechanism movement

New exact facts established in this run:

1. the inner complete-third hinge KL has the explicit positive compiler (5.2)--(5.3);
2. its stiffness derivative is manifestly nonnegative by (5.4);
3. the sign-mixture identity (5.5) separates the Bernoulli sign-information cost from the positive-side truncated-Gaussian deformation;
4. the positive-side KL itself is a positive compact variance path (5.6);
5. the generic entropy-cage-only route is quantitatively too loose for the current scalar crossing, which forces a different certification method rather than another cage-only run.

### Remaining source gap

The full source problem remains **OPEN / PARTIAL**. To obtain a non-microscopic rigorous upper-endpoint move from the complete-third route, the next certificate must still:

1. outward certify the nested-Schur branch/cascade (currently strongest in the concurrent pivoted-x ordering);
2. outward enclose the `U,V` tilted moments and the Schur pivots on the entire branch boxes;
3. use the positive formula above, or an equivalently sharp direct method, to certify the final `RH` endpoint signs without the generic-cage slack;
4. outward bound the reconstructed source density on the certified branch;
5. recheck the exact source-matched stationarized complete-sfl implication at the certified root;
6. obtain the independent validations required by the repository closure standard.

The numerical third-full values near `12.3164` at prescribed positive gap and `12.28722` at zero objective remain conditional/numerical until those obligations are met. No ansatz or simulation is an endpoint.

## 9. Persistence and non-actions

This report is the single immutable R14 substantive report for this bounded iteration. Matching artifacts are create-only. Campbell--O'Rourke Q1.8 history remains preserved, including navigation commit `3846db33296cfb6eea59ff7c488929087c7b62a2`; no claim ownership file is overwritten.

No scheduler, cadence, enabled state, email, Drive object, public posting, workflow, repository permission, or force push was changed.
