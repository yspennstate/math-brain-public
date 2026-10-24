Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED.** GPT-6/maximum was requested only in prompt text; no authenticated reasoning-effort selector/telemetry is exposed here, so GPT-6/maximum is not claimed.

**SOURCE-WIDE STATUS: OPEN -> OPEN. SUBSTANTIVE MOVEMENT:** for the no-leaf family

`P(nu=2)=1-p, P(nu=3)=p`,

the rigorously certified high-mixture parent-bias endpoint improves from

`p>=3/4, lambda<=12/5=2.4`

to

`BOX: p>=3/4, lambda<=2587/1000=2.587`,

with the explicit new-strip certificate

`BOX: -ell'_lambda >= 4000/31214569 > 0`

for `12/5<=lambda<=2587/1000`.  The exact source conjecture remains **OPEN/PARTIAL**; the all-mixture `{2,3}` endpoint remains `1.85527`, and this restricted theorem has not received the independent audits required for closure.

# PROB10-06 — weighted branch-gap differentiation in logarithmic escape coordinates

## 1. Contract, handoff, intake, ownership, and consumed state

Controlling instruction:

- `operations/PROB10_2026-09-20.md`, blob `6f0fcee836d93371d43b84af1a55150fedc80779`.

Also consumed:

- root `POSTED.md`, blob `affe1b5f31545bb15be9ba2580548e9e88095e1b`;
- `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`, blob `38c2595db2f075aba6fa4ac241efdd14542f9f85`;
- intake ledger `probability_1000_intake_claude_20260907/RANKING_2026-09-07.md`, blob `49d4ef844baa293448c87d54cb02a5a9a08b4f1c`, whose current search entry still marks `P0066` `attempted_un` / attempted-unsolved.

The required immutable R02 handoff already exists and is preserved rather than duplicated:

- `runs/R02/20260920T0005Z_owner_refocus_handoff_I0095_to_PROB10-06_4d8c2a71.md`, blob `24734b748956373b8257a0b4f11f681f359b8afa`.

It hands off R02's actual former Randomstrasse/I0095 target, its `7/sqrt(17)` discrepancy witness and route exclusions. None of that work is relabelled as biased-walk research.

Historical P0066's old observation is also preserved rather than called new: at fixed local offspring `k`, the local radial drift `(k-lambda)/(k+lambda)` decreases with parent bias, but this does not control the `lambda`-dependent environment seen from the particle.

Immediate own predecessor and correction consumed:

- `runs/prob10_2026-09-20/PROB10-06/20260920T1350Z_branch_gap_logderivative_bridge_4e2c9a71.md`, blob `3fc9853c54f54a0007701490863678f2dd31271e`;
- `artifacts/prob10_2026-09-20/PROB10-06/20260920T1400Z_finite_depth_derivative_passage_correction.md`, blob `9354b9fa32d1a7433b6826f4f98b718d0ab2d036`.

That state proves, pending independent audit, `p>=3/4` through `lambda=12/5`, with the branch-gap identity `J=c_2-c_3`; its named next obligation was to keep the differentiated escape mass inside the two branch denominators rather than replacing both denominators by `lambda-1` before expectation. This run executes that obligation.

Current neighboring same-source work was re-read and kept disjoint:

- `proofnet24/P01-progress-speed/runs/2026-09-20/2026-09-20T13-20-00Z__run-report.md`, blob `9686722c7e1369a6f293986a2f76a45e161f44e9`, treats nonadjacent minimum-offspring-one laws below `lambda=1`;
- `proofnet24/NM13-05/progress-tree-speed/runs/2026-09-20/2026-09-20T13-45-00Z__harmonic-type-inverse-refinement.md`, blob `09fb24279ec083e487824d1e71a8b1f6be2b5dfc`, treats the distinct `{3,4}` family and crosses `lambda=3`;
- `probability_campaigns/progress_first_2026-09-20/P03/analytic/2026-09-20T0906Z__sharp-von-bahr-esseen-restores-all-mean-third-moment-terminal-theorem.md`, blob `3ed0bcbd0ccbfcd2d5f785e69779e6f5b66e56fd`, proves an existential terminal neighborhood under `E nu^3<infinity` but supplies no quantitative terminal width to splice to the present `{2,3}` interval.

The ownership-delimited route here is therefore: **the `{2,3}` family, high mixture `p>=3/4`, weighted branch-gap/log-coordinate differentiation.** It does not overwrite the P01 minimum-one, NM13-05 `{3,4}`, or P03 terminal-critical claims.

Idea-before-code artifact:

- `artifacts/prob10_2026-09-20/PROB10-06/20260920T1420Z_weighted_branchgap_idea_7b31c4d2.md`, creation/readback commit `f278a11dd2c3fa15fc63d3cde8f1443556cf5fdd`, blob `7357ff6ba6827ff78867af46708e695422fd8b31`.

Exact checker and archived output:

- `artifacts/prob10_2026-09-20/PROB10-06/20260920T1440Z_weighted_branchgap_check.py`, creation/readback commit `8bc510fe0cc10770511493cb742a09e16a73a507`, blob `85dfdc2dbe3cc6c3e1f83149336cfabce734b21a`;
- `artifacts/prob10_2026-09-20/PROB10-06/20260920T1440Z_weighted_branchgap_check.out`, creation/readback commit `dc7bf003ca88a9bab82cfe3786fbce2781a4b925`, blob `0028a26b575ced1550e69f872eb8f022d5690906`.

No scheduler, email, Drive, public-posting, permission, workflow, shared-root, or peer-file state was changed.

## 2. Exact source problem and convention

Let `nu` be the Galton--Watson offspring variable. The source assumptions recovered from Ben Arous--Fribergh--Sidoravicius are

`P(nu=0)=0`, `m=E nu in (1,infinity)`.

Thus there are **no leaves**.

In the original outward child-bias convention, at a vertex with `k` children,

`P_beta(parent)=1/(1+beta k)`,
`P_beta(each fixed child)=beta/(1+beta k)`.

Increasing `beta` pushes away from the root. The transient interval is

`beta>1/m`,

and the Lyons--Pemantle--Peres conjecture is that the limiting speed is increasing throughout this entire interval.

This report uses reciprocal **parent bias**

`lambda=1/beta`,

so

`P_lambda(parent)=lambda/(lambda+k)`,
`P_lambda(each fixed child)=1/(lambda+k)`.

Increasing `lambda` pushes toward the root. The equivalent conjectured sign is therefore

`ell'_lambda<=0` on `0<lambda<m`.

The restricted family here is

`P(nu=2)=1-p`, `P(nu=3)=p`, `p in [0,1]`,

with mean `m=2+p`. On `p>=3/4`, `m>=11/4=2.75`, so the new endpoint `2587/1000=2.587` lies strictly inside the source transient interval.

## 3. Primary-source/current-literature boundary

Primary navigation was refreshed on 20 September 2026.

1. Ben Arous--Fribergh--Sidoravicius, arXiv:1111.5865, proves the historical high-child-bias result `beta>=717` on Galton--Watson trees without leaves and states the LPP monotonicity conjecture in the outward-bias convention. This is baseline, not novelty.
2. Aidekon, arXiv:1111.4313, gives the exact speed formula from the invariant environment seen from the particle. The two-state coefficient reduction below is the already established specialization of that formula.
3. He--Wang--Xiang, arXiv:1610.08151 (published 2025), proves strict parent-bias decrease for minimum offspring `m1>=2` on

   `0<=lambda<=m1/(1+sqrt(1-1/m1))`,

   and records Aidekon's earlier general `lambda<=1/2` improvement. These are known baselines.
4. Bowditch--Tokushige, arXiv:1906.07913 and 2006.03433, provide differentiability/analyticity results in the ballistic regime; the proof below also supplies its own finite-depth domination/truncation passage on the compact strip used.

A bounded fresh arXiv search on 20 September 2026 found no checked source-wide resolution and no checked published theorem identical to the rectangle proved here. This is bounded negative evidence only, **not** a novelty certificate.

## 4. Before/after source metric and separate mechanism delta

### Full source problem

Before: **OPEN**.  
After: **OPEN**.

No arbitrary no-leaf offspring law is solved on its full transient interval.

### All-mixture `{2,3}` metric

Before: every `p in [0,1]` certified through `lambda=1.85527`.  
After: unchanged at `1.85527`.

### High-mixture restricted source metric

Before:

`p>=3/4 => ell'_lambda<0 through lambda=12/5=2.4`.

After:

`BOX: p>=3/4 => ell'_lambda<0 through lambda=2587/1000=2.587`.

Endpoint gain:

`2587/1000-12/5 = 187/1000 = 0.187`.

On the genuinely new strip

`p in [3/4,1]`, `lambda in [12/5,2587/1000]`,

`BOX: -ell'_lambda >= 4000/31214569`.

### Auxiliary mechanism delta

Before, differentiating the branch-addition gap gave

`-J' <= 2 eta mu/a^2 + 2 mu^2/a^3`, `a=lambda-1`,

which discarded every branch escape in the two denominators before expectation.

After, retain one branch in each denominator and use

`q=E[B/(a+B)]`, `r=E[B/(a+B)^2]`, `s=E[U/(a+B)]`, `U=-B'`.

The exact new estimate is

`BOX: -J' <= 2 q(s+r)`.

The weighted derivative `s` closes in the logarithmic escape coordinate with an exact annealed contraction

`BOX: rho_s<99/100`

on the larger strip. The same coordinate gives an explicit finite-depth truncation estimate

`BOX: E[B_N-B] <= (2587/1400)(99/100)^N`.

The favorable exact term in the branch-ratio derivative is also retained rather than discarded:

`Delta=(-J'-d h_2)/c_3`.

At the hard corner `(lambda,p)=(2.587,3/4)`, the checker shows the weighted estimate **without** this favorable term has product bound `0.999887580458478`, while retaining the term lowers it to `0.994297690358478`. Thus this cancellation is quantitatively active, not cosmetic.

## 5. Escape recursion and type-conditioned reciprocal denominator bounds

Let `B_N` be the depth-`N` escape approximation with terminal value `B_0=1`. If the current branch root has `k` children and child escapes `B_{N,i}`, then

`B_{N+1}=S_N/(lambda+S_N)`, `S_N=sum_i B_{N,i}`.                (5.1)

Then `B_N downarrow B`, the infinite-tree escape probability.

Put `Z=1/B`. For the infinite recursion,

`Z=1+lambda H_k(Z_1,...,Z_k)`,                                  (5.2)

where

`H_k(z_1,...,z_k)=1/(sum_i z_i^{-1})`.                          (5.3)

The harmonic sum is coordinatewise increasing and jointly concave. Indeed, with `H=H_k(z)`, for any vector `v`,

`v^T D^2H(z)v`
`=2H^2[H(sum_i v_i/z_i^2)^2-sum_i v_i^2/z_i^3]<=0`             (5.4)

by Cauchy.

Let `x_k=E[Z|nu=k]`, `k=2,3`. Conditional Jensen gives

`x_k <= T_{lambda,p,k}(x_2,x_3)`,                               (5.5)

with

`T_{lambda,p,k}(y_2,y_3)=1+lambda E_p H_k(y_{R_1},...,y_{R_k})`, (5.6)

where `P(R_i=3)=p`.

For a checker rectangle `lambda<=L`, `p>=P`, write

`a_P=(3-P)/6`, `M=(1-L a_P)^{-1}`,
`y_2^(0)=1+LM/2`, `y_3^(0)=1+LM/3`.                             (5.7)

Why this is a supersolution: `H_k(z)<=k^{-2}sum_i z_i`, and

`(1-P)y_2^(0)+P y_3^(0)=1+L M a_P=M`.                           (5.8)

Hence `T_{L,P,k}(y^(0))<=y_k^(0)`. Since `y_2>=y_3`, increasing `p` replaces a larger reciprocal input by a smaller one, while increasing `lambda` increases `T`; thus the `(L,P)` supersolution dominates the full rectangle.

At the global hard corner

`1-L(3-P)/6`
`=1-(2587/1000)(3/8)=239/8000>0`,                               (5.9)

so the construction is legitimate all the way to the new endpoint.

The checker performs 30 exact iterations of `T_{L,P}`, rounding each coordinate **up** to a `10^-9` rational grid only after verifying it remains below the preceding supersolution. Write the resulting bounds as `y_2,y_3`, and set

`d_k=1/y_k`.                                                     (5.10)

Then

`E[B|nu=k]=E[1/Z|nu=k]>=1/E[Z|nu=k]>=d_k`.                      (5.11)

Thus, with `mu=E B`,

`mu>=dbar:=(1-p)d_2+p d_3`.                                     (5.12)

No inverse-escape integrability is assumed before this finite-depth/supersolution argument.

Finally, because offspring is at most three, the essential supremum `u_B` of the infinite escape satisfies

`u_B<=3u_B/(lambda+3u_B)`,

and therefore on `lambda<3`

`BOX: 0<=B<=u:=(3-lambda)/3`.                                  (5.13)

## 6. New logarithmic coordinate and a finite-depth contraction

Set

`a=lambda-1>0`, `Q(b)=log(a+b)`.                                (6.1)

For the parent map `Phi(S)=S/(lambda+S)`, differentiate `Q(Phi)` with respect to a child log-coordinate `Q(B_i)`. If `T_i=sum_{j!=i}B_j`, put

`x=a+B_i`, `t=T_i`.

Using the exact identity

`a+Phi(S)=lambda(a+S)/(lambda+S)`,                               (6.2)

we obtain

`partial Q(Phi)/partial Q(B_i)`
`= (a+B_i)/[(lambda+S)(a+S)]`
`=:K(x,t)=x/[(x+t)(x+t+1)].                                    (6.3)

For fixed `x`, `K` decreases in `t`. For fixed `t`,

`sign partial_x K = sign[t(t+1)-x^2]`.                          (6.4)

On the new strip, `t` for at most two infinite siblings satisfies `t<=2u`. The checker verifies exactly

`a^2 >= 2u(2u+1)`                                               (6.5)

on every subbox. Therefore, if finite-depth child values are interpolated down to their infinite values, all sibling sums along the segment are at least the infinite sibling sum `T`, and all distinguished `x` values are at least `a`. Equations (6.3)--(6.5) give the pathwise comparison

`K(x,t) <= a/[(lambda+T)(a+T)].`                                (6.6)

Define sibling kernels

`R_j=E[1/((lambda+T_j)(a+T_j))]`, `j=1,2`,                     (6.7)

where `T_j` is a sum of `j` iid infinite branch escapes.

To bound `R_j`, write `Z_i=1/B_i` and

`H_j=(sum_i B_i)^(-1)=H_j(Z_1,...,Z_j)`.                        (6.8)

Then

`1/((lambda+T_j)(a+T_j))=G(H_j)`,                               (6.9)

where

`G(z)=z^2/((lambda z+1)(a z+1))`.                               (6.10)

Direct differentiation gives

`G'(z)=z((2lambda-1)z+2)/[(lambda z+1)^2(a z+1)^2]>0`,          (6.11)

and

`G''(z)=-2[lambda a((2lambda-1)z^3+3z^2)-1]`
`       /[(lambda z+1)^3(a z+1)^3`.                             (6.12)

Because `H_j>=1/(j u)>=1/(2u)`, the exact checker verifies

`lambda a[(2lambda-1)z^3+3z^2]>=1` for `z>=1/(2u)`,             (6.13)

so `G` is increasing and concave throughout the required range. Conditioning on sibling offspring types and using concavity of both `G` and `H_j`,

`E G(H_j(Z))`
`<=G(E H_j(Z))`
`<=G(H_j(E Z_1,...,E Z_j))`
`<=G(H_j(y_{R_1},...,y_{R_j})).`                                (6.14)

Averaging the finitely many type patterns gives exact rational upper bounds for `R_1,R_2`.

Define

`rho_s=a[(1-p)2R_1+p3R_2].`                                     (6.15)

The checker proves on the whole new rectangle

`BOX: rho_s<99/100`.                                            (6.16)

### Finite-depth truncation

Couple `B_N downarrow B` on the same tree. Apply the multivariate mean-value formula to `Q(B_N)-Q(B)`. The coefficients are bounded by (6.6), and the distinguished branch is independent of its siblings. Therefore

`L_{N+1}:=E[Q(B_{N+1})-Q(B)] <= rho_s L_N`.                      (6.17)

At depth zero,

`L_0<=log((a+1)/a)<=1/a<=5/7`,                                  (6.18)

because `a>=7/5` on the strip. Hence

`L_N <= (5/7)(99/100)^N`.                                       (6.19)

For `x>=y>0`, `x-y<=x log(x/y)`. Since `a+B_N<=a+1=lambda<=2587/1000`,

`BOX: E[B_N-B]`
`<= (2587/1000)(5/7)(99/100)^N`
`= (2587/1400)(99/100)^N`.                                      (6.20)

This is the required explicit truncation bound; it is not a simulation.

## 7. Differentiated recursion in the same coordinate

Let

`U_N=-partial_lambda B_N>=0`,                                   (7.1)

which follows inductively from differentiating (5.1) from terminal derivative zero. The exact derivative recursion is

`U=S/(lambda+S)^2 + lambda sum_i U_i/(lambda+S)^2`.              (7.2)

Define the weighted derivative

`W=U/(a+B)`.                                                     (7.3)

Using (6.2), (7.2) becomes exactly

`W = f(S)+sum_i K(a+B_i,T_i)W_i`,                               (7.4)

where

`f(s)=s/[lambda(lambda+s)(a+s)]`.                               (7.5)

The same comparison (6.6) controls the derivative coefficients at every finite depth by the infinite sibling kernels, hence by `rho_s<1`. A crude uniform source bound from (7.5) gives `sup_N E W_N<infinity`.

For completeness, derivative passage can be proved without assuming the desired speed sign. Subtract consecutive finite-depth recursions (7.4). On this compact strip `f` and `K` are Lipschitz in all branch variables. The crude differentiated recursion gives `U_N<=N/lambda`, hence `W_N<=N/(lambda a)`. Combining this polynomial bound with the geometric log-coordinate truncation (6.19)--(6.20) yields

`v_N:=E|W_N-W_{N-1}|`
`<=rho_s v_{N-1}+C N(99/100)^{N-1}`.                            (7.6)

Iteration gives `v_N<=C'(1+N^2)(99/100)^{N-1}`, so `sum_N v_N<infinity`. Thus `W_N` is Cauchy in `L^1`, and because `B_N->B` geometrically, `U_N=(a+B_N)W_N` converges in `L^1` to `U=-B'`. The standard uniform-derivative theorem then passes derivatives through every finite expectation defining the coefficients below. No sign of `ell'_lambda` has been assumed.

## 8. Sharp infinite weighted derivative bound

Let

`s=E[U/(a+B)]`, `mu=E B`.                                      (8.1)

The source function `f` in (7.5) is increasing and concave on the entire possible child-sum range. Indeed,

`sign f'(s)=sign(lambda a-s^2)`,                                (8.2)

and, up to a positive denominator,

`f''(s)` has numerator

`N(s)=s^3-3lambda a s-lambda a(2lambda-1)`.                     (8.3)

The checker verifies `(3u)^2<=lambda a`. Hence on `0<=s<=3u`, `N'(s)=3(s^2-lambda a)<=0` while `N(0)<0`, proving `f''<0` and `f'>=0`.

Conditional Jensen therefore gives, for current degree `k=2,3`,

`E[f(S_k)|nu=k] <= f(k mu)`.                                    (8.4)

Using `mu>=dbar`,

`f(kmu)/mu`
`=k/[lambda(lambda+kmu)(a+kmu)]`
`<=k/[lambda(lambda+k dbar)(a+k dbar)]`.                         (8.5)

Set

`C0=(1-p) 2/[lambda(lambda+2dbar)(a+2dbar)]`
`   +p 3/[lambda(lambda+3dbar)(a+3dbar)]`.                      (8.6)

The derivative part of (7.4) is at most `rho_s s`, hence

`s<=mu C0+rho_s s`.                                             (8.7)

Thus

`BOX: s<=mu Cs`, `Cs:=C0/(1-rho_s)`.                            (8.8)

This keeps the derivative mass paired with the branch denominator; it is the main new gain over the predecessor's global `eta=E U` estimate.

## 9. Weighted derivative of the exact branch-addition gap

For Aidekon coefficients, let iid branches `B_0,...` and put

`D_2=a+B_0+B_1+B_2`,
`D_3=D_2+B_3`,                                                   (9.1)

`c_2=E[B_0/D_2]`, `c_3=E[B_0/D_3]`.                             (9.2)

The exact branch-addition gap is

`J=c_2-c_3=E[B_0B_3/(D_2D_3)]`.                                (9.3)

Let

`h_k=-c'_k>=0`, `d=J/c_2`.                                      (9.4)

As in the predecessor,

`Delta:=h_2/c_2-h_3/c_3`
`=(log(c_3/c_2))'`
`=(-J'-d h_2)/c_3`.                                             (9.5)

The new point is to bound `-J'` before throwing away the branch variables in the denominators.

Write

`q=E[B/(a+B)]`,
`r=E[B/(a+B)^2]`,
`s=E[U/(a+B)]`.                                                 (9.6)

Differentiating the integrand in (9.3) gives

`-j'=(U_0B_3+B_0U_3)/(D_2D_3)`
` +B_0B_3 D'_2/(D_2^2D_3)`
` +B_0B_3 D'_3/(D_2D_3^2)`,                                    (9.7)

with

`D'_2=1-(U_0+U_1+U_2)<=1`,
`D'_3=1-(U_0+U_1+U_2+U_3)<=1`.                                 (9.8)

Because

`D_2>=a+B_0`, `D_3>=a+B_3`,                                    (9.9)

independence of branches 0 and 3 yields term by term

`E[(U_0B_3)/(D_2D_3)]<=sq`,
`E[(B_0U_3)/(D_2D_3)]<=qs`,
`E[B_0B_3/(D_2^2D_3)]<=rq`,
`E[B_0B_3/(D_2D_3^2)]<=qr`.                                    (9.10)

Therefore

`BOX: -J'<=2q(s+r)`.                                            (9.11)

Now `x/(a+x)` is increasing concave, while `x/(a+x)^2` is increasing concave on `0<=x<=u<a`. Hence Jensen, (5.12), and `mu>=dbar` give

`q<=mu/(a+mu)<=mu/(a+dbar)`,                                   (9.12)

`r<=mu/(a+mu)^2<=mu/(a+dbar)^2`.                               (9.13)

Combining with (8.8),

`-J'<=2mu^2/(a+dbar)[Cs+1/(a+dbar)^2]`.                         (9.14)

## 10. Retaining the favorable `-d h_2` term

The predecessor discarded `-d h_2` in (9.5). On the present strip it can be bounded explicitly.

From `B<=u`,

`D_2<=a+3u=2`,
`D_3<=2+u`.                                                      (10.1)

Thus

`J>=mu^2/[2(2+u)]`.                                             (10.2)

Also `c_2<=mu/a`, so

`d=J/c_2>=a mu/[2(2+u)]`.                                      (10.3)

The exact derivative score is

`h_2=E[(1/3)sum_{i=0}^2 (B_i+aU_i)/D_2^2]`.                    (10.4)

Since `D_2<=2` and `U_i>=0`,

`h_2>=mu/4`.                                                     (10.5)

Therefore

`BOX: d h_2>=a mu^2/[8(2+u)]`.                                 (10.6)

For the denominator of (9.5),

`D_3<=a+4u=:Dmax=(9-lambda)/3`,                                 (10.7)

hence

`c_3>=mu/Dmax`.                                                  (10.8)

Define

`C=2/(a+dbar)[Cs+1/(a+dbar)^2]-a/[8(2+u)]`.                    (10.9)

The checker verifies `C>=0` on every accepted box. Equations (9.5), (9.14), (10.6), and (10.8) give

`Delta<=Dmax mu C<=Dmax u C`.                                   (10.10)

This is the exact score bound interval-evaluated by the checker.

## 11. Aidekon speed derivative and certified sign

For the two-point family let

`Cmix=(1-p)c_2+p c_3`,
`theta=p c_3/Cmix`.                                             (11.1)

Then Aidekon's symmetrized formula is

`ell_lambda=(2+theta-lambda)/(2+theta+lambda)`.                  (11.2)

From (9.5),

`theta'=theta(1-theta)Delta`.                                   (11.3)

Thus exactly

`-ell'_lambda`
`=2(2+theta)/(2+theta+lambda)^2`
` *[1-lambda g(theta)Delta]`,                                  (11.4)

where

`g(theta)=theta(1-theta)/(2+theta)`.                            (11.5)

Adding one branch gives the inherited exact ratio lower bound

`c_3/c_2>=3/4`.                                                  (11.6)

Therefore

`theta>=3p/(4-p)`.                                               (11.7)

Since `g'` has the sign of `2-4theta-theta^2`, and at `p=3/4` the lower bound is `theta>=9/13>sqrt(6)-2`, `g` is decreasing throughout the allowed tilted range. Hence on a box whose lower mixture endpoint is `P`,

`g(theta)<=g(3P/(4-P))`.                                        (11.8)

The exact checker combines (5.7)--(5.12), (6.10)--(6.16), (8.6)--(8.8), (10.9)--(10.10), and (11.8). On

`lambda in [12/5,2587/1000]`, `p in [3/4,1]`,

it proves

`BOX: lambda g(theta)Delta <999/1000`,                          (11.9)
`BOX: rho_s<99/100`.                                            (11.10)

Substituting (11.9) into (11.4), using `2+theta>=2`, `theta<=1`, and `lambda<=2587/1000`,

`-ell'_lambda`
`>=4(1/1000)/(3+2587/1000)^2`
`=BOX: 4000/31214569>0`.                                        (11.11)

Together with the immediate predecessor's theorem through `12/5`, this proves the full restricted statement

`BOX: p>=3/4 => ell_lambda is strictly decreasing for 0<=lambda<=2587/1000`.

Every asserted point satisfies `lambda<m=2+p`.

## 12. Exact checker and actual output

The checker uses Python `fractions.Fraction` for every accepting comparison. Rectangle arithmetic is outward rational interval arithmetic. Each subbox computes its `(L,P)` reciprocal type-vector supersolution by 30 exact harmonic iterations with upward `10^-9` rational rounding, verifies the analytic shape inequalities for `f`, `K`, and `G`, evaluates `rho_s`, `Cs`, the weighted branch-gap coefficient (10.9), and the speed product (11.9), and bisects any box not immediately certified.

Archived actual output:

`WEIGHTED_BRANCHGAP_CHECK`

`RECT_PASS lambda=[12/5,2587/1000] p=[3/4,1]`

`visited=2615 accepted=1308 max_depth=28`

`speed_product_upper<999/1000`

`weighted_contraction_rho_s<99/100`

`worst_product_upper_float=0.998975869580471`

`worst_rho_s_upper_float=0.989481822302885`

`derivative_margin=4000/31214569`

`log_truncation=> E[B_N-B] <= (2587/1400)*(99/100)^N`

`HARD_CORNER_BASE_PRODUCT_float=0.999887580458478`

`HARD_CORNER_REFINED_PRODUCT_float=0.994297690358478`

`TYPE_VECTOR_CORNER_SLACK=239/8000`

`ROUNDING_GRID=1e-9 TYPE_VECTOR_ITERATIONS=30`

`ALL_EXACT_CHECKS_PASS`

The printed decimals are diagnostics only; all decisions are exact rational inequalities. This is a self-check, not an independent audit.

## 13. Three materially different attacks this run

The idea note was committed before code. The previous run used owner-directive moves #3, #2, and #12; this run deliberately uses different moves.

### Attack A — Move #18, SAY IT IN ANOTHER LANGUAGE: SUCCESS

Rewrite escape perturbations in the logarithmic coordinate `Q(B)=log(lambda-1+B)` and derivative mass as `W=U/(lambda-1+B)`. This reveals the exact kernel

`K=x/[(x+t)(x+t+1)]`

and makes the same annealed coefficient `rho_s` control both truncation and the differentiated recursion. Keeping branch factors inside `-J'` yields `-J'<=2q(s+r)`. This is the primary mechanism responsible for extending the endpoint past `2.4`.

### Attack B — Move #7, TAKE THE LIMIT: precise terminal-splice obstruction

The current P03 terminal theorem gives, for every finite-third-moment law, an existential interval `(m-epsilon,m)`. For `{2,3}` one can instantiate its leading coefficient exactly:

`f_2=E[nu(nu-1)]=2+4p`,

so

`ell_{m-delta}=[(m-1)/(2f_2)]delta+O_Lip(delta^2)`.              (13.1)

At the hardest present mixture `p=3/4`,

`m=11/4`, `f_2=5`, leading coefficient `=7/40`,                 (13.2)

while the still-uncovered distance from the new endpoint to criticality is

`11/4-2587/1000=163/1000`.                                      (13.3)

The P03 report's pairwise contraction has substantial critical slack, but the constants multiplying the `O_Lip(delta^2)` remainder in its equations (5.2), (5.5), and (6.8) are left existential. Therefore that report does **not** certify `epsilon>=163/1000`, and no splice is claimed. Turning those constants explicit is a genuinely different remaining route.

### Attack C — Move #24, FIND THE EXTREMAL OBJECT: SUCCESSFUL SECONDARY GAIN

Instead of discarding the favorable `-d h_2` in `Delta=(-J'-d h_2)/c_3`, use the extremal denominator identities

`D_2<=a+3u=2`, `D_3<=2+u`

to prove `d h_2>=a mu^2/[8(2+u)]`. The exact checker falsifies the idea that this term is negligible at the hard corner: omitting it gives the stronger-product bound `0.999887580458478>999/1000`, while retaining it gives `0.994297690358478<999/1000`. Thus it is needed for the clean uniform `999/1000` margin at the new endpoint.

## 14. Remaining full-scope gap and next obligation

The source-wide conjecture remains open. Even inside `{2,3}`:

- all mixtures still stop at `lambda=1.85527`;
- the high-mixture theorem now stops at `2.587`, while for `p=3/4` the critical endpoint is `m=2.75`;
- the reciprocal first-moment supersolution used here has corner slack `1-lambda E(1/nu)` and therefore approaches its own barrier at `lambda=8/3` when `p=3/4`; this route cannot simply be pushed to `m=11/4` by rerunning the same checker;
- smaller `p` values retain substantial intermediate gaps;
- P03's terminal theorem remains nonquantitative, so no overlap with `2.587` is certified.

The next nonduplicate mathematical attack should therefore do one of two things: (i) make the P03 terminal constants explicit for the bounded `{2,3}` law and test whether its terminal interval reaches below `2.587`; or (ii) replace the `E(1/B)` denominator control by a weaker weighted inverse moment tailored directly to the branch-gap/log kernel, so that the artificial `lambda E(1/nu)<1` barrier is removed. Another subdivision of the same reciprocal checker without a new inequality is not source progress.

Status: **PARTIAL / OPEN parent; restricted `{2,3}` theorem candidate pending independent validation.**