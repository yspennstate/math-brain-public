# account03/B17 — balanced arity-six Gibbs collar and a 2,029-profile threat chamber

**Classification:** `ESSENTIAL_STEP_APPLIED / BALANCED6_ANALYTIC_COLLAR + FINITE_CENTROID_REDUCTION`.  
**Full unrestricted uniform-cube FEI:** **OPEN / NOT PROVED**.  
**Execution:** `WITHOUT_VERIFIED_BRAIN`. Authenticated repository controls and mathematical artifacts were read directly; no authenticated cognitive-brain retrieval/context was used.

## 0. Live target and method change

The current owner-level target is the all-gate reformulation `D_Gamma(G;p)>=0` for every Boolean gate and every product bias, with the current stable scalar-lift candidate

\[
C_*=6.5218512,\qquad
\Gamma_*(u)=\Gamma_{\rm RO}(u)+0.2682048\,u(1-u).
\]

At the balanced uniform point this becomes simply

\[
\boxed{H(G)\le C_*[I(G)-1].}\tag{0.1}
\]

The complete five-input uniform slice is already closed by account01/B17 (`20260922T043923Z-arity5-uniform-c001`). I therefore do **not** repeat an arity-five sweep. I move one dimension up and attack the first balanced arity-six chamber analytically.

The named compatible **other-account** result consumed and applied is account04/B17,

`proofnet24/P03-fei/fleet-2026-09-21/account04/B17/20260922T031352Z-biased-restriction-margin-cocycle/REPORT.md`,

which proves the exact restriction identities. At a uniform pivot `j` they give

\[
I(G)=\frac{I(G_0)+I(G_1)}2+\delta_j,
\qquad
\delta_j=\Pr[G_0\ne G_1].\tag{0.2}
\]

I also retain account03/B13's proved `BAL6-ZERO-L1` theorem: if a balanced six-bit gate has a zero singleton Fourier coefficient, then (0.1) already holds. The new work below treats the nonzero-singleton chamber by a different mechanism: a one-fixed-atom spectral Gibbs envelope plus exact cube isoperimetry.

## 1. Exact pivot data for a balanced six-bit gate

Let `G:{0,1}^6->{-1,1}` be balanced under uniform measure. Fix a coordinate `j`. Its two five-bit restrictions have complementary negative-set sizes. After swapping the two branches if necessary, write

\[
|A_0|=m,\qquad |A_1|=32-m,\qquad 1\le m\le16.
\]

Put

\[
\mu_m:=1-\frac m{16}.
\]

The pivot singleton coefficient is exact:

\[
\boxed{|\widehat G(\{j\})|=\mu_m.}\tag{1.1}
\]

Hence the parent spectral law contains a fixed level-one atom of mass

\[
\boxed{a_m=\mu_m^2.}\tag{1.2}
\]

The branch disagreement obeys

\[
\delta_j\ge |\Pr[A_0]-\Pr[A_1]|=\mu_m.\tag{1.3}
\]

Let `beta_5(m)` be the minimum edge boundary of an `m`-set in `Q_5`. Coordinate compression gives the exact recursion

\[
\beta_n(m)=\min_{a+b=m}
\bigl(\beta_{n-1}(a)+\beta_{n-1}(b)+|a-b|\bigr),\tag{1.4}
\]

which yields for `m=1,...,16`

\[
(5,8,11,12,15,16,17,16,19,20,21,20,21,20,19,16).\tag{1.5}
\]

Each five-bit child's total influence is therefore at least `beta_5(m)/16`. Applying the consumed account04/B17 identity (0.2) and (1.3) gives

\[
\boxed{I(G)\ge I_{\rm floor}(m):=\frac{\beta_5(m)}{16}+\mu_m.}\tag{1.6}
\]

This is a physical Boolean restriction bound, not a free spectral-law relaxation.

## 2. A fixed-singleton Gibbs envelope

Because `G` is balanced, its empty Fourier mass is zero. Remove the known singleton atom of mass `a=a_m`; the remaining mass is `R=1-a`.

Among the remaining 62 nonempty subsets of `[6]`, the multiplicities by degree are `5,15,20,15,6,1` at degrees `1,...,6`. For any `lambda>=0`, define

\[
Z_\lambda=
5\,2^{-\lambda}+15\,2^{-2\lambda}+20\,2^{-3\lambda}
+15\,2^{-4\lambda}+6\,2^{-5\lambda}+2^{-6\lambda}.\tag{2.1}
\]

For the remaining spectral masses `(q_S)`, nonnegativity of relative entropy against the Gibbs law proportional to `2^{-lambda |S|}` gives

\[
\sum_{S\ne\{j\}}\phi(q_S)
-\lambda\sum_{S\ne\{j\}}|S|q_S
\le R\log_2\frac{Z_\lambda}{R},\qquad
\phi(x)=x\log_2(1/x).\tag{2.2}
\]

Therefore, if `lambda<C_*` and `I(G)>=T`,

\[
H(G)-C_*[I(G)-1]
\le U_m(T,\lambda),\tag{2.3}
\]

where

\[
U_m(T,\lambda)=C_*+\phi(a_m)-\lambda a_m
+R\log_2\frac{Z_\lambda}{R}
-(C_*-\lambda)T.\tag{2.4}
\]

This is the key replacement mechanism. It uses an actual Boolean singleton atom forced by the physical restriction, rather than maximizing over all 63 spectral atoms as if the parent spectrum were unconstrained.

For the only multipliers needed below,

\[
Z_0=62,\qquad Z_1=\frac{633}{64},\qquad Z_2=\frac{10505}{4096}.\tag{2.5}
\]

Thus every sign below is certified with rational logarithm intervals.

## 3. PROVED: an exact influence collar for every nonzero pivot type

The adjacent checker evaluates (2.4) with exact `Fraction` arithmetic and outward atanh-series logarithm bounds. It proves:

| `m` | `beta_5(m)` | `I_floor(m)` | safe whenever `I>=T_m` | `lambda` | certified `U_m` upper |
|---:|---:|---:|---:|---:|---:|
|1|5|1.2500|1.2500|0|-0.376950175093099|
|2|8|1.3750|1.3750|1|-0.275900699286685|
|3|11|1.5000|1.5000|1|-0.372868341758839|
|4|12|1.5000|1.5625|1|-0.233439902586603|
|5|15|1.6250|1.6250|1|-0.182540707965867|
|6|16|1.6250|1.6875|1|-0.207064659254539|
|7|17|1.6250|1.7500|1|-0.297361052946689|
|8|16|1.5000|1.7500|1|-0.100564008469611|
|9|19|1.6250|1.8125|1|-0.300245556454449|
|10|20|1.6250|1.8125|2|-0.201671904234604|
|11|21|1.6250|1.8125|2|-0.181700507074309|
|12|20|1.5000|1.8125|2|-0.187849775670103|
|13|21|1.5000|1.8125|2|-0.213673090035060|
|14|20|1.3750|1.8125|2|-0.251581554096703|
|15|19|1.2500|1.7500|2|-0.008845619926190|

Hence:

> **Theorem 3.1 (balanced-six Gibbs collar).** If a balanced six-bit Boolean gate has a coordinate whose minority restriction size is `m in {1,...,15}` and its total influence satisfies `I(G)>=T_m` from the table, then `H(G)<6.5218512[I(G)-1]`.

The smallest certified margin is still strictly negative by more than `8e-3`; none of these are floating sign ties.

Immediate consequences:

* pivot types `m=1,2,3,5` are impossible in a falsifier at any influence, because `T_m=I_floor(m)`;
* account03/B13 already excludes `m=16` (zero singleton);
* every surviving pivot type has `T_m<=29/16`.

## 4. New finite threat chamber: only five influence levels and 2,029 centroid profiles

For a balanced parent, each pivot disagreement count is even, so every coordinate influence is a multiple of `1/16`; therefore

\[
I(G)=K/16\tag{4.1}
\]

for an integer `K`.

A hypothetical falsifier must satisfy `I<T_m` for every coordinate. Since `m=16` is already closed and `T_m<=29/16` for all `m<=15`, any balanced six-bit falsifier must obey

\[
\boxed{I(G)\le 28/16=7/4.}\tag{4.2}
\]

Now write

\[
j_i:=16-m_i,\qquad |\widehat G(\{i\})|=j_i/16.
\]

Two universal Boolean/Fourier constraints sharpen the chamber further. First, coordinatewise `Inf_i(G)>=|hat G({i})|`, so

\[
\boxed{\sum_i j_i\le K.}\tag{4.3}
\]

Second, if `W_1=sum_i hat G({i})^2`, balanced Parseval gives

\[
I-1=\sum_{|S|\ge2}(|S|-1)\widehat G(S)^2\ge1-W_1,
\]

hence

\[
\boxed{W_1\ge2-I,\qquad
\sum_i j_i^2\ge16(32-K).}\tag{4.4}
\]

Parseval also gives `sum_i j_i^2<=256`.

For each integer `K=16,...,28`, the checker enumerates only sorted singleton-magnitude profiles. It retains `j_i` only if its pivot type `m_i=16-j_i` satisfies

\[
I_{\rm floor}(m_i)\le K/16<T_{m_i},\tag{4.5}
\]

and then imposes (4.3)-(4.4). The result is exact:

| `K` | `I=K/16` | surviving sorted centroid profiles |
|---:|---:|---:|
|16–23|1.0000–1.4375|0|
|24|1.5000|40|
|25|1.5625|26|
|26|1.6250|795|
|27|1.6875|915|
|28|1.7500|253|

Thus any hypothetical balanced six-bit falsifier must have

\[
\boxed{I(G)\in\left\{\frac32,\frac{25}{16},\frac{13}{8},\frac{27}{16},\frac74\right\}}\tag{4.6}
\]

and, after coordinate permutation/input negations, its singleton-magnitude vector must belong to one of exactly

\[
\boxed{2029}
\]

arithmetic profiles. In particular (4.2) forces

\[
\boxed{W_1\ge1/4.}\tag{4.7}
\]

The 2,029 profiles are only necessary profiles; many may not be realizable by a Boolean truth table. No finite-profile statement here is promoted to full arity-six closure.

## 5. Exact old/new implication

**Exact candidate version attacked:** `LIMIT-PRIME-GATE-LIFT-v1` at balanced center `C_*=6.5218512`.

**Old missing implication:** prove `D_{Gamma_*}(P;p)>=0` for every composition-prime gate and every product bias, or produce a gate/bias falsifier. The complete five-input uniform slice was already closed, while balanced arity six remained open outside the zero-singleton child-slack theorem.

**New proved inference:** every nonzero pivot type has the analytic influence collar in Theorem 3.1. Combining those collars with the already-proved zero-singleton theorem collapses the entire balanced arity-six threat to five total-influence levels and exactly 2,029 sorted singleton-magnitude profiles.

**What is not proved:** the 2,029 necessary profiles have not all been shown unrealizable or safe; nonuniform product bias and arity greater than six are untouched. Full FEI is therefore still OPEN.

**Replacement obligation:** do not rerun a generic six-bit truth-table search. Use the five-bit layer-pair machinery from account01/B17 to attack only boundary sizes `48,50,52,54,56` and only the 2,029 centroid profiles above. Either eliminate all realizable profiles by exact child-spectrum/edge-boundary inequalities or return the first actual Boolean gate with `H>C_*(I-1)`.

**Consumed peer artifact:** account04/B17 `20260922T031352Z-biased-restriction-margin-cocycle/REPORT.md`, applied in (0.2)/(1.6).  
**Next recipient:** `account01/B17` (five-bit layer enumerator / exact arity-five comparator machinery), with `account01/B18` as stable-candidate integrator.

## 6. Reproduction boundary

`CHECKER.py` verifies the cube boundary recursion, every row of the Gibbs collar with outward rational logarithm intervals, and the exact 2,029-profile count. `CHECK_OUTPUT.txt` is the captured PASS output.

No external model/API, paid compute, workflow dispatch, email, Drive action, public posting, credential, scheduler mutation, machine path or unrelated private transcript is used or recorded.
