# fleet02/B19 — threshold-flexible terminal reduction and all-finite-K baseline barrier

**Run:** `20260922T111213Z-fleet02-B19-fei-threshold`  
**Programme:** `FEI-ALL-TEAM-20260922T095941Z` / control revision `2026-09-22.3`  
**Assignment:** Threshold-flexible terminal proof  
**Classification:** `ESSENTIAL_STEP_APPLIED / FULL_FEI_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`  
**Full uniform-cube FEI:** **OPEN / NOT PROVED.**

## 0. Exact scope and source state

This run follows the all-team owner reallocation and does no new POS3, installation, or benchmark work. The canonical state revision consumed is `FEI-20260922T1000Z-v1`; the live correction inbox was empty at the last pre-publication refresh. In particular the fixed-potential, raw-`U4`, unweighted-`L2`, and fixed-depth-KL routes remain retired at their exact corrected scopes.

Source-pinned premises actually used:

1. **TERMINAL_CORE** — `yspennstate/math-open-problems@85ffa60db26997421d980b1f86c03d82259504ca`, `proofnet24/P03-fei/fleet-2026-09-21/fleet02/B13/20260922T075416Z-all-block-terminal-core/REPORT.md`, blob `68e838a493671ed5c27a29468dfcce7bb621d860`. It supplies the physical all-block terminal compiler, the minimum-dimensional ratio core, tensor heredity of `(U_A,D_A)`, and the co-singleton phase tax.

2. **ROBUST_ROW** — `yspennstate/math-open-problems@fdbfbcc1beed0db4cb6d13c8d61fd92db53a8113`, `proofnet24/P03-fei/fleet-2026-09-21/fleet04/B12/20260922T081051Z-terminal-trigger-surplus/REPORT.md`, blob `d283c7b495316959312155f8ba68fb83569d9633`. It supplies the symbolic-`K` trigger-surplus and weighted-depth theorem.

3. **CURVATURE** — `yspennstate/math-open-problems@200e3fd37fe201f78d882ba8809414d201efb829`, `proofnet24/P03-fei/fleet-2026-09-22/fleet04/B18/20260922T091529Z-surplus-hidden-curvature/REPORT.md`, blob `468c55f8ab3d8c2864a91994b9cc07dbbbbf2be2`. It supplies the exact row law `4d_k=2R_k+Omega_k` and the fixed-cardinality visible-bank payment.

4. **COPAIR_BARRIER** — `yspennstate/math-open-problems@85ffa60db26997421d980b1f86c03d82259504ca`, `proofnet24/P03-fei/fleet-2026-09-21/fleet02/B13/20260922T093723Z-copair-terminal-tax/REPORT.md`, blob `000f6250c095d5a40870c6cfc3fabaf8f07c8d0e`. It supplies `omega_{i<-j}=4s_{ij}-2c_{i<-j}` and the exact tensor-orientation warning.

5. **Named partner actually consumed: fleet03/B19** — bundle commit `144ea823b604785a77b638b03b0c5d7909676d52`, `proofnet24/P03-fei/fleet-2026-09-22/fleet03/B19/20260922T103024Z-b19-fei-r11/REPORT.md`, report blob `c291157149243f0d2dcb73640be652db670ff393`. It proves the nonreused selected-pair I-projection inequality with the correct baseline `b_ij=(c/v)q_i q_j`.

The last source is applied explicitly in Section 4 below.

## 1. Setup and the exact symbolic terminal calculus

Use the source gauge

`q_i=Inf_i(f)<=1/2`, `J=sum_i q_i`, `j(q)=1-h2(1/2+sqrt(q(1-q)))`, `P=sum_i j(q_i)`, and `F=H-P`.

Let `g` be a genuine minimum-dimensional ratio core with `rho=F(g)/J(g)>K>2`. TERMINAL_CORE gives, for every nonempty physical block `A`, `U_A>=rho D_A>K D_A`. In particular, for every coordinate,

`h2(q_i)>K q_i`. (1.1)

Define the symbolic surplus `sigma_K(q)=h2(q)-Kq`. Let `a_K` be the unique root in `(0,1/2)` of

`h2(a_K)=K a_K`. (1.2)

Uniqueness follows because `d/dq [h2(q)/q]=log2(1-q)/q^2<0`. Hence (1.1) implies `q_i<a_K`.

### Lemma 1 — exact finite-threshold surplus coefficient

For every `K>2` and every coordinate of the ratio core,

`sigma_K(q_i) <= lambda_K [K+j'(q_i)]`, (1.3)

where

`lambda_K = log2(1+2^(-K)) / [K+j'(a_K)]`. (1.4)

**Proof.** `sigma_K` is concave and `sigma_K'(q)=log2((1-q)/q)-K`, so its maximum occurs at `q_*=1/(1+2^K)` and equals `log2(1+2^(-K))`. The source derivative formula gives `j''(q)<0` on `(0,1/2)`. Since `q_i<a_K`, `j'(q_i)>=j'(a_K)`. Divide the scalar maximum by this lower bound on `K+j'`. QED.

This is the symbolic replacement for the earlier `K=4` numerical coefficient. No raw-curvature payment has been assumed.

## 2. Symbolic weighted-depth reduction

Write the CURVATURE row quantities `R_k=sum_{i!=k} c_{k<-i}`, `Omega_k=sum_{i!=k} omega_{k<-i}`, so that

`4 d_k = 2 R_k + Omega_k`. (2.1)

The source fixed-cardinality theorem on a ratio-`rho` core gives

`sum_k [rho+j'(q_k)] R_k <= P-DTC(X)`. (2.2)

Since `rho>K`,

`sum_k [K+j'(q_k)] R_k <= P-DTC(X)`. (2.3)

Define the symbolic hidden bank

`U_K := sum_k [K+j'(q_k)] Omega_k`. (2.4)

Multiply (2.1) by `sigma_K(q_k)`, sum, and use Lemma 1 plus (2.3). This proves

`sum_k sigma_K(q_k)d_k <= (lambda_K/2)[P-DTC(X)] + (lambda_K/4) U_K`. (2.5)

Combining with ROBUST_ROW at `eta=1/16` gives the exact symbolic robust-row reduction

`sum_{i in R_1/16} q_i^2[K+j'(q_i)] <= (128 lambda_K/105)[P-DTC(X)] + (64 lambda_K/105)U_K`. (2.6)

Thus increasing `K` really does make the surviving hidden coefficient small. For example,

`K=8: a_8=0.0105621627280994..., lambda_8=0.000517684914618024...`,

and the two coefficients in (2.6) are `0.000631082562581972...` and `0.000315541281290986...`. If the terminal implication were later closed at `K=8`, TERMINAL_CORE would return the global FEI constant `8+2/ln2=10.8853900817779...`. This last sentence is conditional; no `K=8` FEI theorem is claimed.

## 3. All-finite-K Boolean barrier to paying the raw hidden bank

The small coefficient in (2.6) is **not** enough by itself. The following extends the source `K=4` tensor-orientation barrier to every finite threshold.

Fix any finite `K>2`. Choose an integer `d>=max(6,ceil(K+3))`, put `q=2^(1-d)`, and let `phi_d` be the `d`-bit one-point defect: `phi_d(0^d)=-1` and `phi_d(x)=+1` otherwise.

### Lemma 2 — `phi_d` is strictly all-block `K`-terminal

For a block `A` of size `a`, direct physical restriction gives:

- if `1<=a<=d-2`, `D_A=a q`, `U_A=a h2(q)`;
- if `a=d-1`, `D_A=d q`, `U_A=(d-1)h2(q)-q j'(q)`;
- if `a=d`, `D_A=d q`, `U_A=d h2(q)`.

Now `h2(q)>q log2(1/q)=(d-1)q`, while `j'(q)<2/ln2<3`. Therefore the ordinary/full blocks have `U_A/D_A>d-1>K`, and the co-singleton block has

`U_A/D_A > ((d-1)^2-3)/d > K`, (3.2)

because `d>=K+3` implies `d^2-(K+2)d-2>0`. Thus every nonempty block has a positive `K`-terminal margin. QED.

Let `F_{d,m}=prod_{r=1}^m phi_d(x^(r))`. The source tensor heredity of `(U_A,D_A)` makes `F_{d,m}` strictly all-block `K`-terminal for every `m`.

For coordinates in two different factors the exact tensor formula gives

`c_{i<-j}=0`, `s_ij=q^2`, `omega_{i<-j}=4q^2`. (3.4)

There are `m(m-1)d^2` directed cross-factor pairs. Hence

`U_K(F_{d,m})/J(F_{d,m}) >= 4[K+j'(q)] q d (m-1) -> infinity`. (3.5)

So for **every fixed finite threshold `K`**, all-block `K`-terminality alone does not make the raw hidden bank affordable. Since `lambda_K>0` is fixed once `K` is fixed, making `K` large cannot by itself turn the last term of (2.6) into `O(J)`.

### Lemma 3 — the same raw-bank divergence survives tensor primitivity

Let `N=dm`, `v=1^N`, and flip the single truth-table value at `v`, obtaining `G_{d,m}`.

Exactly as in the source surgery argument, every nontrivial coordinate partition has a multiplicative `2x2` rectangle of product `-1`: if the partition separates whole factors, use a rectangle with corner `v`; if it splits a factor, use the one-point-defect rectangle away from `v`. Hence `G_{d,m}` is tensor-primitive.

Let `delta_N=2^(1-N)`. A one-point flip changes each parent influence and each branch-averaged folded influence by at most `delta_N`, hence `D_A` by `O(N delta_N)`. For fixed `K,d`, the parent influences remain in a compact interval around the positive number `q`; `h2'`, `j'`, and `j''` are bounded there. Also the crossing functional is Lipschitz under this one-point perturbation. Consequently

`sup_A |(U_A-KD_A)(G_{d,m})-(U_A-KD_A)(F_{d,m})| = O_{K,d}(N 2^(-N))`. (3.7)

The tensor `F_{d,m}` has a fixed positive block margin from Lemma 2, so (3.7) proves that `G_{d,m}` is also strictly all-block `K`-terminal for all sufficiently large `m`.

For a fixed directed pair, the one-point flip changes derivative support disagreement `p_ij` at at most two quotient inputs, hence by at most `2^(2-N)`; the same bound holds for opposite-sign overlap, and singleton crossing changes by at most `2^(2-N)`. Therefore

`|Delta omega_{i<-j}| <= 7*2^(2-N)`. (3.8)

For all sufficiently large `m`, every cross-factor pair from (3.4) therefore still has `omega_{i<-j}(G_{d,m})>=2q^2`. Since the weights in `U_K` are at least `K`,

`U_K(G_{d,m})/J(G_{d,m}) -> infinity`. (3.9)

This is a genuine Boolean, tensor-primitive, all-block-terminal barrier for every fixed finite `K`. It is **not asserted to be ratio-critical**, so it does not refute the terminal-core programme. Instead it proves that the ratio-extremal hypothesis has to do real work.

## 4. Applying the named partner: the exact cross-factor obstruction is I-projection baseline

The partner theorem uses the lifted maximum-entropy nonempty I-projection. Let `pi` be the full squared-Fourier law of `F_{d,m}`, let `v=Pr_pi[X!=empty]`, and let `c` be the I-projection parameter. The partner's correct pair baseline is `b_ij=(c/v)q_i q_j`.

For the product, the empty Fourier mass of one factor is `(1-q)^2`; hence

`v=1-(1-q)^(2m)`, `N=dm`. (4.2)

All occurrence marginals equal `q`, and the nonzero I-projection root satisfies

`1-c=(1-cq/v)^N`. (4.3)

Define `f(t)=1-t-(1-tq/v)^N`. It is strictly concave, `f(0)=0`, and `f'(0)=Nq/v-1>0` for `d>=6`. At `t=v`,

`f(v)=(1-q)^(2m)-(1-q)^(dm)>=0` (4.4)

because `d>=2`. Therefore the unique positive root obeys `c>=v`. For every cross-factor pair,

`s_ij=q^2`, `b_ij=(c/v)q^2>=q^2`, `omega_{i<-j}=4q^2<=4b_ij`.

The partner's hidden-excess charge `Psi_b(omega)` is therefore exactly zero on the entire cross-factor bulk responsible for (3.5).

This applies the named other-account theorem exactly: the obstruction is not “unpaid KL above baseline.” It is the **conditional-product/I-projection baseline itself**. The partner theorem correctly refuses to pay it as irreducible occurrence dependence.

## 5. What changed, and the exact unpaid implication

Before this run, the active symbolic route had a `K=4` surplus reduction and a `K=4` raw-hidden-curvature no-go. After this run:

1. the terminal surplus/weighted-depth calculus is valid for **every finite `K>2`** with an explicit coefficient `lambda_K`;
2. the coefficient decays quickly (e.g. `lambda_8≈5.18e-4`), so finite-threshold flexibility genuinely improves every term already paid by `P-DTC`;
3. nevertheless, for **every fixed finite K**, there are exact all-block `K`-terminal Boolean tensors and tensor-primitive surgeries with `U_K/J -> infinity`;
4. applying fleet03/B19 shows that on the exact tensor bulk this divergence lies at or below the correct I-projection baseline, so the nonreused positive-excess selector charge is identically zero there.

Hence the finite-threshold strategy does **not** fail because `K=4` was numerically too small. The earliest source-valid obstruction is now:

> **RATIO-CRITICAL BASELINE ELIMINATION / SELECTOR.** Use the full minimum-dimensional ratio-extremal hypotheses (not terminality or qualitative primitivity alone) to prove that a genuine `rho>K` core cannot concentrate its unpaid terminal deficit in the conditional-product baseline. It must either create an affordable physical block / ratio descent, or force enough above-baseline pair excess under one realizable nonreused selector to pay the relevant terminal deficit. The small/nonrobust branch must be included in that same global selector/payment or closed separately; this report does not silently pay it.

Until that implication is proved, (2.6) is a reduction rather than FEI closure. This report therefore does not claim `ALL-BLOCK-TERMINAL(K)=>F<=KJ`, and does not claim the conditional `K=8` global constant as a theorem.

## 6. Executed regression

`CHECKER.py` is a standard-library numerical regression for the analytic formulas. It checks `a_K`, `lambda_K`, strict one-point-factor terminal ratios for `K=4,6,8,10,12`, the `K=8` coefficients, and the sign `c/v>=1` on representative tensor sizes. It terminates `THRESHOLD_FLEX_REGRESSION_PASS`.

Executed checker SHA-256: `263fff5316f415922d30b4d22993aa276901eeb345fcb8c093b298c2441b1a0f`.  
Captured output SHA-256: `735002dc0b48ac2281b59d1c0db5bb4fa5be046f3e1b2d17979cf19f8a2f6f81`.

The checker is not the proof; Sections 1–4 are analytic and arbitrary-dimensional.

## 7. Outcome

**Outcome:** `ESSENTIAL_STEP_APPLIED / FULL_FEI_OPEN`.

The exact threshold-flexible theorem and all-finite-K barrier are new run-level mathematics. The partner's selected-pair KL expression is consumed substantively and identifies the correct location of the remaining obstruction. No fixed potential, raw-`U4=O(J)`, unweighted convolution `L2`, or fixed-depth KL claim is revived.
