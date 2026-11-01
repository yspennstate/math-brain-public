# fleet03/B05 — exact strong-prime lower barriers for source-valid safe-direction cones

Run: `fleet03-B05-20260922T104025Z-fei`  
Programme: `FEI-ALL-TEAM-20260922T095941Z`  
Assignment: `FEI-20260922-fleet03-B05` — **Dual obstruction for the safe cone**  
Classification: `ESSENTIAL_STEP_APPLIED / EXACT_CONE_BARRIER / FULL_FEI_OPEN`  
Execution: `WITHOUT_VERIFIED_BRAIN`; `full_brain_connected=false`.

## 0. Scope, correction state, and consumed other-account mathematics

The live owner control is revision `2026-09-22.3`, which supersedes the older BT4 allocation and assigns this slot to FEI Path A. Full uniform-cube FEI remains open.

The assignment asks for an exact lower bound on the centre cost of repairing the strong composition-prime witness inside a clearly defined safe-direction cone, while respecting the correction that the broad `globally gate-safe => local selector inequality` step has **not** been proved.

The named other-account result used substantively is fleet04/B13:

- repository `yspennstate/math-open-problems`, commit `c50e06733fc1e7f109e20dbb1a0013d67aa71dc7`, path `proofnet24/P03-fei/fleet-2026-09-21/fleet04/B13/20260922T0954Z-nearoptimal-singleton-repair/REPORT.md`.

It proves universal singleton-restriction safety of

\[
F_*(m)=1-m^4-\varepsilon_*(1-m^2)^3,
\qquad \varepsilon_*={453773\over20000000},
\tag{0.1}
\]

and supplies the genuine two-input obstruction

\[
\varepsilon\le \varepsilon_{\max}:={10625\over468288}
\tag{0.2}
\]

for the one-parameter family `1-m^4-epsilon(1-m^2)^3`.

The strong-prime source is fleet02/B17:

- repository `yspennstate/math-open-problems`, commit `f5946fb64d336ed7369de279159643944efc47af`, path `proofnet24/P03-fei/fleet-2026-09-21/fleet02/B17/20260922T091146Z-strong-prime-shaped-repair/REPORT.md`.

It gives the actual 18-input composition-prime witness

\[
p_1={223\over456},\quad p_2=\cdots=p_{18}=\frac12,
\quad p_{out}={1019\over2048},
\tag{0.3}
\]

with

\[
\alpha_1={57\over256},\qquad \sum_{i=2}^{18}\alpha_i={465\over256},
\tag{0.4}
\]

and the rigorous bracket

\[
-0.038023735<D_{\Gamma^\dagger}<-0.038023734,
\qquad \Gamma^\dagger(1/2)=6.521851214.
\tag{0.5}
\]

Thus any additive repair must pay strictly more than

\[
d_0:={38023734\over10^9}=0.038023734.
\tag{0.6}
\]

The exact assigned partner is fleet04/B05. At the fresh prepublication source scan there was no compatible completed FEI handoff/result for that slot in the new programme; its visible completed reports were from the superseded BT4 campaign. Per the current memory protocol I did not wait or substitute a stale BT4 theorem as FEI mathematics. The fleet04/B13 theorem above is therefore the completed source-valid other-account input actually applied in this run. The partner's new necessity task remains directly relevant to Section 4 below.

## 1. Strong-witness payment functional

Work in mean coordinates `m=1-2p`. For any symmetric endpoint-zero additive direction `F`, define its payment on the strong witness by

\[
\mathcal L(F)
={57\over256}F\!\left({5\over228}\right)
+{465\over256}F(0)
-F\!\left({5\over1024}\right).
\tag{1.1}
\]

If `Gamma=Gamma^dagger+F`, then the new defect at the strong source is

\[
D_{\Gamma}=D_{\Gamma^\dagger}+\mathcal L(F).
\tag{1.2}
\]

Therefore repair requires `mathcal L(F)>d_0`.

The relevant efficiency is

\[
r(F):={\mathcal L(F)\over F(0)}
\tag{1.3}
\]

for positive-centre directions. If every direction in a cone satisfies `r(F)<=R`, then every repair in that cone must add centre more than `d_0/R`.

## 2. Exact three-ray safe cone and its optimal dual ratio

Define three source-valid safe directions.

### 2.1 Quadratic ray

Let

\[
F_2(m)={1-m^2\over4}.
\tag{2.1}
\]

This is the usual quadratic/Poincare safe currency. Its centre is `1/4`, and fleet02/B17 gives

\[
\mathcal L(F_2)=M_2={62098577\over239075328}.
\tag{2.2}
\]

Hence

\[
r_2={62098577\over59768832}
=1.038979262636419\ldots .
\tag{2.3}
\]

### 2.2 Quartic ray

Let

\[
F_4(m)={1-m^4\over8}.
\tag{2.4}
\]

Its centre is `1/8`, and fleet02/B17 gives

\[
\mathcal L(F_4)
={211575825297187673\over1628974855061766144}.
\tag{2.5}
\]

Thus

\[
r_4={211575825297187673\over203621856882720768}
=1.0390624490721942\ldots .
\tag{2.6}
\]

### 2.3 Proved shaped singleton-safe ray

For `F_*` from (0.1), fleet04/B13 gives

\[
F_*(0)=1-\varepsilon_*
={19546227\over20000000},
\tag{2.7}
\]

and

\[
\mathcal L(F_*)=
{14089027843865471581106016370764179
\over13874074233328574665473392640000000}.
\tag{2.8}
\]

Therefore

\[
\boxed{
r_*=
{14089027843865471581106016370764179
\over13559290218974564299889599750078464}
=1.0390682415034973\ldots .
}
\tag{2.9}
\]

Exact rational cross multiplication gives

\[
r_2<r_4<r_*.
\tag{2.10}
\]

Now define the explicit cone

\[
\mathcal C_3
=\{aF_2+bF_4+cF_*:a,b,c\ge0\}.
\tag{2.11}
\]

Every member is universally safe because each generator is safe and the gate-safety inequality is linear in the added direction.

### Theorem 2.1 — exact optimum on `C_3`

For every nonzero `F in C_3`,

\[
\boxed{r(F)\le r_*}.
\tag{2.12}
\]

Moreover equality is attained on the `F_*` ray.

#### Proof

Write `F=aF_2+bF_4+cF_*`. Then

\[
\mathcal L(F)=aF_2(0)r_2+bF_4(0)r_4+cF_*(0)r_*,
\]

while

\[
F(0)=aF_2(0)+bF_4(0)+cF_*(0).
\]

Thus `r(F)` is a convex combination of `r_2,r_4,r_*`, with weights equal to the nonnegative centre contributions. Equation (2.10) proves (2.12). QED.

### Corollary 2.2 — exact centre barrier for the richer proved cone

Any repair `Gamma^dagger+F` with `F in C_3` must have

\[
F(0)>{d_0\over r_*}
=
{1006982118193536300204879629420800770048
\over27517632507549749181847688224148787109375}.
\tag{2.13}
\]

Hence

\[
\boxed{
\Gamma(1/2)>
{46201059096054459434811835350317842456563941
\over7044513921932735790553008185382089500000000}
=6.558445282109503\ldots .
}
\tag{2.14}
\]

The current refined shaped known-witness candidate has centre `6.558445288811087`, only

\[
6.7015844741\times10^{-9}
\tag{2.15}
\]

above this rigorous necessary bound for `C_3`. Thus, within this concrete proved safe cone, scalar mixing of the quadratic, quartic and current shaped direction has essentially no room left on the strong source.

For comparison, the corresponding exact barriers using only the best available ray are

\[
C_{quad}>6.558448416049552\ldots,
\tag{2.16}
\]

\[
C_{quartic}>6.558445486109393\ldots,
\tag{2.17}
\]

and (2.14) for the richer three-ray cone. The shaped ray strictly improves the quartic cone, but only by about `2.04e-7` in this lower-bound comparison.

## 3. Exact near-optimality of the entire one-parameter shaped family

Consider

\[
F_\varepsilon(m)=1-m^4-\varepsilon(1-m^2)^3.
\tag{3.1}
\]

Write

\[
A:=\mathcal L(1-m^4)=r_4,
\tag{3.2}
\]

and determine the exact coefficient `B` from

\[
\mathcal L(F_\varepsilon)=A-B\varepsilon.
\tag{3.3}
\]

Using the exact source value (2.8) at `epsilon_*`,

\[
B={A-\mathcal L(F_*)\over\varepsilon_*}.
\tag{3.4}
\]

The centre-normalized efficiency is

\[
r(\varepsilon)={A-B\varepsilon\over1-\varepsilon}.
\tag{3.5}
\]

Exact arithmetic gives `A-B>0`, so

\[
r'(\varepsilon)={A-B\over(1-\varepsilon)^2}>0.
\tag{3.6}
\]

Fleet04/B13's actual two-input Boolean obstruction proves that universal safety within this family requires (0.2). Therefore every universally safe member of this family obeys

\[
\boxed{
r(\varepsilon)\le r(\varepsilon_{max})
={329886005658347604989102040382751
\over317482521792392773356227464790016}
=1.0390682416024957\ldots .
}
\tag{3.7}
\]

Consequently every repair of the fixed seed by this whole family must satisfy

\[
\boxed{
\Gamma(1/2)>
{1081769658721394171434893539602395784124729
\over164943002829173802494551020191375500000000}
=6.558445282106016\ldots .
}
\tag{3.8}
\]

This is a **necessary-family barrier**. It does not assert that the endpoint `epsilon_max` is universally safe. The proved `epsilon_*` lies only `3.7897362307e-7` below `epsilon_max`, and its exact cone barrier (2.14) differs from the family ceiling barrier (3.8) by only about `3.49e-12` in centre. Thus the present one-parameter shape is essentially exhausted as an efficiency optimization against the strong witness.

## 4. Repairing the broad safe-cone claim with the correct hypothesis

The current FEI correction state marks fleet02/B12's arbitrary globally gate-safe cone barrier as `NEEDS_REVALIDATION`: global gate safety alone does not justify deleting positive child slack and asserting a local selector inequality.

The numerical conclusion *can* be salvaged rigorously on a clearly defined stronger cone.

### Definition 4.1 — singleton-restriction-safe cone

Let `C_SR` be the set of even functions `F:[-1,1]->[0,infty)` with `F(+-1)=0` such that for every **realizable** physical singleton reveal of a finite product-biased Boolean function, with selector bias `t`, Boolean child means `a,b`, disagreement probability `delta`, and parent mean `c=(1-t)a+tb`,

\[
\boxed{
(1-t)F(a)+tF(b)+\delta F(1-2t)-F(c)\ge0.
}
\tag{4.1}
\]

This is a cone. By the literal-coordinate induction of fleet01/B14/fleet04/B13, every member of `C_SR` is globally gate-safe. The converse is **not** assumed.

### Lemma 4.2 — two exact selector consequences inside `C_SR`

For every `F in C_SR` and `0<x<1`,

\[
F(x)\le (1-x)F(0)+{1\over2}F(|1-2x|),
\tag{4.2}
\]

and

\[
F(x)\ge(1-x)F(0).
\tag{4.3}
\]

#### Proof

For (4.2), take the actual selector with `t=1-x`, `0`-child constant `-1`, `1`-child a balanced literal, so `a=-1,b=0,delta=1/2,c=-x`. Equation (4.1), endpoint zero and evenness give (4.2).

For (4.3), use the actual balanced selector between two Boolean children of means `-x,+x` and disagreement `x`, realized by the two biased-bit construction recorded in fleet02/B12. Then `t=1/2,c=0`, so (4.1) is `F(x)+xF(0)-F(0)>=0`. QED.

Crucially, these are now **direct instances of the assumed local inequality (4.1)**. No child defect has been dropped.

### Theorem 4.3 — infinite-dimensional exact barrier on `C_SR`

Let `F in C_SR` with `F(0)>0`. For the strong-witness tent orbit

\[
{5\over228}\to {109\over114}\to {52\over57}\to {47\over57}
\to {37\over57}\to {17\over57}\to {23\over57}\to {11\over57}
\to {35\over57}\to {13\over57}\to {31\over57}\to {5\over57}
\to {47\over57},
\tag{4.4}
\]

iterating (4.2) around the period-nine tail and then backward gives

\[
{F(5/228)\over F(0)}\le {129023\over116508}.
\tag{4.5}
\]

Applying (4.3) at the output mean gives

\[
{F(5/1024)\over F(0)}\ge {1019\over1024}.
\tag{4.6}
\]

Therefore

\[
\boxed{
{\mathcal L(F)\over F(0)}
\le {57\over256}{129023\over116508}
+{465\over256}-{1019\over1024}
={279387\over261632}
=1.06786249388454\ldots .
}
\tag{4.7}
\]

If `F(0)=0`, the same nonnegative tent recursion forces the strong-input orbit values to vanish, so the direction cannot provide positive strong-witness repair. Hence every fixed-seed repair with a direction in `C_SR` satisfies

\[
\boxed{
\Gamma(1/2)>
6.521851214+{38023734/10^9\over279387/261632}
={305344778449951\over46564500000000}
=6.557458545672153\ldots .
}
\tag{4.8}
\]

This is an **infinite-dimensional** exact barrier with a corrected, source-valid scope. It is not a lower bound on the true FEI constant and it is not presently proved for every globally gate-safe direction. Extending (4.8) from `C_SR` to the full global safe cone is exactly where a necessity theorem of the kind assigned to partner fleet04/B05 would enter.

## 5. Comparison with the degree-six necessary cone

Fleet03/B16 gives an exact two-selector dual ceiling for every universally gate-safe endpoint-zero even polynomial of degree at most six:

\[
R_6\le
{117399595402058107229743783687
\over112981776538836095856994516992}
=1.0391020481228088\ldots .
\tag{5.1}
\]

Using the stronger certified deficit lower endpoint `d_0` from (0.6) sharpens the corresponding fixed-seed centre barrier to

\[
\boxed{
\Gamma(1/2)>
{384979341406990814556655767050788317073
\over58699797701029053614871891843500000000}
=6.558444091541423\ldots .
}
\tag{5.2}
\]

Thus the exact hierarchy of currently available strong-source efficiency ceilings is

\[
r_2<r_4<r_*<R_6<{279387\over261632}.
\tag{5.3}
\]

Interpretation: the degree-six cone is already squeezed extremely close to the proved shaped direction; the arbitrary singleton-safe cone has much more formal room, but even there the strong witness imposes a nontrivial exact centre tax.

## 6. What changed and the next unpaid implication

**New proved result 1.** The explicit proved safe cone `C_3=cone{F_2,F_4,F_*}` has exact optimal strong-witness efficiency `r_*`, giving the rigorous fixed-seed centre barrier (2.14). The current refined shaped repair sits only `6.70e-9` above it.

**New proved result 2.** Across the entire one-parameter family `1-m^4-epsilon(1-m^2)^3`, the actual two-input obstruction and exact monotonicity of the strong-source ratio give the necessary efficiency ceiling (3.7) and centre barrier (3.8). Scalar retuning of this family is therefore mathematically exhausted at the `~1e-11` centre scale.

**New proved result 3 / correction repair.** The previously challenged infinite-dimensional barrier becomes valid when scoped to the explicit singleton-restriction-safe cone `C_SR`; the exact corrected centre barrier using the current strong-witness bracket is (4.8). The broader implication from global gate safety to local singleton safety remains open and is not used.

**First unpaid implication.** Either:

1. prove a necessity/approximation theorem showing that every globally gate-safe direction relevant to the repair can be represented or approximated by `C_SR`, which would broaden Theorem 4.3; or
2. construct a globally gate-safe direction outside `C_SR` with strong-source efficiency exceeding `279387/261632`, thereby showing the local cone is genuinely restrictive; or
3. abandon monotone-safe additive repair and trade existing gate slack in a final globally feasible potential.

The assigned partner fleet04/B05 is precisely tasked with item 1. Until such a theorem exists, this report keeps the singleton-safe and globally-safe cones separate.

Full uniform-cube FEI remains **OPEN / NOT PROVED**.

## 7. Verification boundary

All arithmetic in Sections 2, 3 and 5 was checked in this invocation with exact Python `fractions.Fraction` arithmetic. The finite tent-orbit fractions in Section 4 are inherited from the source-bound fleet02/B12 calculation but are used only after repairing its hypothesis: (4.2)-(4.3) are direct local singleton inequalities under Definition 4.1. The accompanying `CHECK.py` records the exact rational comparisons and centre barriers used here.

This report does not certify universality of the repaired base potential, does not claim an FEI lower bound, and does not claim the challenged broad safe-cone theorem. It contains only scoped FEI mathematics and source pins; no credentials, scheduler IDs, machine paths, private transcripts, email/Drive data, public release, workflow dispatch, paid remote compute, or cross-account native action were used.
