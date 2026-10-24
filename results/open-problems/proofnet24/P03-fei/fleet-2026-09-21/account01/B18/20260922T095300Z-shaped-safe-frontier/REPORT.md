# account01/B18 — near-sharp singleton-safe repair frontier after AND-margin refutation

**Run:** `20260922T095300Z-account01-B18-shaped-safe-frontier`  
**Primary classification:** `ESSENTIAL_STEP_APPLIED`  
**Inherited candidate status:** `OWNER-CG-EXTREMALITY-v1` is `CANDIDATE_REFUTED`.  
**Execution:** `WITHOUT_VERIFIED_BRAIN`; `full_brain_connected=false`.  
**Full unrestricted uniform-cube FEI:** **OPEN / NOT PROVED.**

## 0. Version/change summary

The live owner target offered two decisive alternatives for the read-once base potential `Gamma_0`: prove that the positive owner-normalized gate margin is extremized by AND/decomposable gates, or falsify that assertion by an actual Boolean gate and bias asking for a larger margin.

This run consumes and applies the exact completed **other-account** result account03/B12

`proofnet24/P03-fei/fleet-2026-09-21/account03/B12/20260922T094602Z-numaro-margin-refutation/REPORT.md`, scientific commit `274ff75dfbfcfe395207cbc8a4ff2211e6683fdc`.

It proves for the composition-prime 18-input Numaro gate at

\[
p_1={223\over456},\qquad p_2=\cdots=p_{18}=\frac12,
\qquad p_{\rm out}={1019\over2048},
\]
that

\[
c_G>0.4145908383477759\ldots,
\]
while the certified all-bias two-input AND theorem gives `c_AND<=0.01`. Thus the owner-normalized AND/decomposable extremality candidate is rigorously false by a large gap. This is a candidate refutation, not a refutation of FEI.

I therefore do not spend this run attempting to prove the now-false extremality statement. I apply the refutation to the first surviving replacement mechanism: the actual-original-coordinate singleton-restriction safe direction of account01/B14, and push that one-parameter family essentially to its source-valid safety boundary before rescaling it against the same strong Numaro witness.

The new immutable candidate/version is

`SHAPED-SAFE-FRONTIER-v1`.

## 1. Compact conditional end-to-end chain

For a symmetric potential `Gamma`, let

\[
D_\Gamma(G;p)=
\sum_i {\operatorname{It}_i(G;p)\over V_{p_i}}
\bigl(\Gamma(p_i)+h_2(V_{p_i})\bigr)
-\Gamma(p_{\rm out})-\widetilde H_G(p),
\qquad V_u=4u(1-u).
\]

The current smallest honest proof chain is:

1. **PROVED:** the all-gate potential theorem reduces full FEI to finding one finite symmetric nonnegative `Gamma` with `D_Gamma(G;p)>=0` for every finite Boolean gate and every product-bias vector, including boundary limits.
2. **REFUTED:** for the base `Gamma_0`, the claim that the worst positive repair margin is attained by AND/decomposable gates is false by the exact account03/B12 Numaro witness consumed above.
3. **PROVED:** account01/B14 supplied a literal singleton-restriction family of universally gate-safe perturbations. The present run proves universal safety for a substantially sharpened rational member of that family and proves it lies within `7.5e-17` of a rigorous necessary upper boundary coming from an actual two-input AND line.
4. **PROVED:** scaling this sharpened direction by the explicit rational coefficient below repairs the strongest currently source-certified Numaro witness while never decreasing any Boolean gate defect relative to `Gamma^dagger`.
5. **UNPAID / FIRST ESSENTIAL REMAINING IMPLICATION:** prove that the resulting candidate has nonnegative defect on every remaining composition-prime gate and bias, or construct an actual Boolean prime/bias counterexample to it. The balanced-uniform slice cannot be bypassed by potential shaping: for center `C=Gamma(1/2)`, its defect is `C[I(f)-1]-H(f)` on every balanced uniform Boolean `f`.
6. **CONDITIONAL:** universal nonnegativity in step 5 plus the existing decomposition/base/boundary reductions yields full FEI at the finite center displayed in Section 5.

No step below asserts step 5.

## 2. Sharpen the universal singleton-restriction direction

For a rational parameter `epsilon`, set

\[
\phi_\epsilon(m)=1-m^4-\epsilon(1-m^2)^3,
\qquad
\eta_\epsilon(p)=\phi_\epsilon(1-2p).
\]

Account01/B14 proved the universal-gate safety mechanism for the earlier value `epsilon=113009/5000000`: reveal one actual original coordinate `k`, let `t` be its product bias, let the two Boolean children have means `a,b`, and put

\[
\delta=\Pr(G_{k=0}\ne G_{k=1}),\qquad c=(1-t)a+tb.
\]

Actual Booleanity gives

\[
|a-b|\le 2\delta.
\]

Since `phi_epsilon>=0` for `0<=epsilon<1`, it is enough to prove the local inequality at `delta=|a-b|/2`:

\[
(1-t)\phi_\epsilon(a)+t\phi_\epsilon(b)
+{|a-b|\over2}\phi_\epsilon(1-2t)
-\phi_\epsilon(c)\ge0. \tag{2.1}
\]

Take `b>=a`, put `d=b-a`, and uniquely parameterize

\[
a=-1+u(2-d),\quad b=a+d,\quad c=-1+td+u(2-d),
\qquad 0\le d/2,t,u\le1.
\]

Exact algebra factors the left side of (2.1) as

\[
\boxed{
G_\epsilon(d,t,u)=d\,t(1-t)(2-d)R_\epsilon(d/2,t,u),
} \tag{2.2}
\]

where `R_epsilon` has degree at most four in each of its three variables and is affine in `epsilon`.

I choose

\[
\boxed{
\epsilon_*={56721646463783\over2500000000000000}
=0.0226886585855132.
} \tag{2.3}
\]

The attached exact-`Fraction` Bernstein checker converts the exact power coefficients of `R_{epsilon_*}` to the tensor Bernstein basis on `[0,1]^3` and recursively bisects only boxes whose Bernstein lower hull is not yet nonnegative. It terminates with

- `792` certified terminal boxes,
- `905` total boxes,
- maximum subdivision depth `27`,
- no unresolved boxes,
- minimum terminal Bernstein coefficient

\[
{43225860035202095786322675999861897145560250299268834991580273
\over
1028440348325753776346855739098344065614209916020987414592880640000000000000000}
>4.2030\times10^{-17}. \tag{2.4}
\]

Hence `R_{epsilon_*}>=0` on the full continuum, so (2.1) holds for every admissible physical reveal.

The same induction as the B14 source now gives, for **every** finite Boolean gate and **every** product-bias vector,

\[
\boxed{
\sum_i {\operatorname{It}_i(G;p)\over V_{p_i}}\eta_{\epsilon_*}(p_i)
-\eta_{\epsilon_*}(p_{\rm out})\ge0.
} \tag{2.5}
\]

Thus adding any nonnegative multiple of `eta_{epsilon_*}` can never decrease an all-gate defect. This is a continuum theorem from physical restrictions, not a finite gate sweep or an unsigned spectral relaxation.

## 3. A genuine Boolean upper obstruction nearly pins the family boundary

The improvement in (2.3) is not merely a numerical coefficient search. The same local inequality has a source-valid necessary upper restriction coming from an actual two-input AND/NAND line.

Take both input biases equal to

\[
r={8004417\over20000000}=0.40022085.
\]

Reveal one input of the `+1`-only-on-`(1,1)` AND gate. Then

\[
t=r,\qquad a=-1,\qquad b=-1+2r,\qquad \delta=r,\qquad c=-1+2r^2,
\]

which is exactly the parameter line `u=0`, `d/2=t=r` in (2.2). Solving its exact local gap for equality in `epsilon` gives the necessary threshold

\[
\epsilon\le
E(r):=
{2r^4+4r^3+2r^2-4r+1
\over
8r^2(r-1)(r^5+3r^4+3r^3+r^2-2)}.
\tag{3.1}
\]

At the rational `r` above,

\[
E(r)=
{87063976298056383004191692840000000000000000000000000000
\over
3837334674058112811005758660502687481768624593225620567041}
=0.022688658585513274\ldots .
\]

The exact gap is positive but tiny:

\[
0<E(r)-\epsilon_*
=7.42262963682054\ldots\times10^{-17}
<7.5\times10^{-17}. \tag{3.2}
\]

Therefore `epsilon_*` is rigorously within `7.5e-17` of a **necessary** upper bound for universal safety inside this one-parameter shaped family. Any `epsilon>E(r)` fails already on this concrete two-input Boolean gate at bias `r`. I do not claim that `E(r)` is the exact global optimum over all `r`; (3.2) is the precise proved near-frontier statement.

## 4. Apply the sharpened safe direction to the strong prime witness

For the strong composition-prime Numaro source used by account03/B12 and account02/B17,

\[
p_1={223\over456},\quad p_2=\cdots=p_{18}=\frac12,
\quad p_{\rm out}={1019\over2048},
\]

so the corresponding mean coordinates are

\[
m_1={5\over228},\qquad m_{\rm out}={5\over1024}.
\]

Its exact unit currency under the new safe direction is

\[
\boxed{
L_*={57\over256}\phi_{\epsilon_*}(5/228)
+{465\over256}\phi_{\epsilon_*}(0)
-\phi_{\epsilon_*}(5/1024)
}
\]

\[
=
{1761128465015772503763738147514586363332409
\over
1734259279166071833184174080000000000000000}
=1.0154931769271667\ldots . \tag{4.1}
\]

The source-certified strong-witness bracket gives

\[
D_{\Gamma^\dagger}>-0.038023735.
\tag{4.2}
\]

Choose

\[
\boxed{
\lambda_*={18721807228217\over500000000000000}
=0.037443614456434.
} \tag{4.3}
\]

Exact arithmetic yields

\[
\lambda_*L_*-0.038023735
=
{131483896411981860244390477594223695384753
\over
867129639583035916592087040000000000000000000000000000000}
>1.5163\times10^{-16}. \tag{4.4}
\]

Therefore the explicit replacement

\[
\boxed{
\Gamma_*(p)=\Gamma^\dagger(p)+\lambda_*\eta_{\epsilon_*}(p)
} \tag{4.5}
\]

has strictly positive defect on the strong Numaro witness. By (2.5), every Boolean gate/bias pair that was already nonnegative for `Gamma^dagger` remains nonnegative for `Gamma_*`.

This does **not** establish universal nonnegativity: an unknown prime gate may still be negative for `Gamma_*`.

## 5. Finite center of the new replacement

Since

\[
\eta_{\epsilon_*}(1/2)=1-\epsilon_*,
\]

the new center is exactly

\[
\boxed{
C_*:=\Gamma_*(1/2)
={8198056603839780478193093835089
\over
1250000000000000000000000000000}
=6.5584452830718245\ldots .
} \tag{5.1}
\]

This is lower than the executed account02/B17 shaped-repair center `6.55844529582746` by

\[
1.2755635617\ldots\times10^{-8},
\]

and lower than the completed quartic-Q4 center `6.558445589` by

\[
3.0592817562\ldots\times10^{-7}.
\]

These are candidate-center improvements inside proved universally safe repair directions. They are **not** FEI upper bounds until the universal gate obligation in step 5 of Section 1 is discharged.

## 6. Exact old/new missing implications and status

**Old missing implication:** `OWNER-CG-EXTREMALITY-v1`: no genuine gate/bias asks for a larger `Gamma_0` repair margin than AND/decomposable gates.

**Status of old implication:** `CANDIDATE_REFUTED`, applied here via account03/B12's exact Numaro margin `c_G>0.4145908383` versus certified `c_AND<=0.01`.

**New proved inference:** `SHAPED-SAFE-FRONTIER-v1`: the rational direction `eta_{epsilon_*}` in (2.3) is universally safe for every Boolean gate/product bias; it sits within `7.5e-17` of a rigorous source-valid upper boundary for that one-parameter family; and the explicit rational scale (4.3) repairs the strongest currently source-certified Numaro obstruction with finite center (5.1).

**New first essential missing implication:** either

\[
D_{\Gamma_*}(P;p)\ge0
\]

for every finite composition-prime Boolean gate `P` and every product bias `p`, with all boundary cases, or produce an actual Boolean prime/bias counterexample. Because the balanced-uniform slice is exactly `C_*[I(f)-1]-H(f)`, potential shaping alone cannot make that universal quantifier disappear.

**Implication to full FEI:** conditional only. If the new missing implication plus existing decomposition/base/boundary steps is proved, the all-gate theorem yields full FEI with finite constant `C_*`. No such universal proof is supplied here.

## 7. Verification and scope

`CHECKER.py` uses only Python standard-library exact `Fraction` arithmetic. It verifies the full tensor-Bernstein continuum certificate, the source-valid two-input upper obstruction, the strong Numaro repair currency, the positive repair slack, and the candidate-center comparisons. `CHECKER_OUTPUT.txt` records the accepted output.

Scoped privacy/secret review: this run contains only FEI mathematics, rational constants, logical account/slot labels, and repository-relative scientific references. It contains no credentials, scheduler identifiers, machine paths, unrelated private data, email/Drive material, public-posting action, paid/remote compute, workflow dispatch, permission changes, or benchmark gold.
