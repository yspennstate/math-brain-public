# B15 — exact packet/free-energy profile of the post-Hod record ladder

**Status: OPEN / PARTIAL. Full uniform-cube FEI is not proved here.**  
**Execution context: WITHOUT_VERIFIED_BRAIN.** The repository control plane and FEI files were read directly through authenticated GitHub access; no claimed cognitive-brain retrieval/context was used in the mathematics.

This run follows the spectral magnitude/arithmetic route after the earlier B15 handoff retired the conjecture that Hod's `beta(1/2)` is the universal sharp FEI constant. The current `teorth/optimizationproblems` `constants/71a.md` (blob `d5fcdad39105d4cb594176b128119ab6f7dda9e4`) records the n=18 balanced monotone lower bound

\[
C_{71}>6.521845710923046575,
\]

so the sharp-Hod target is genuinely false as a universal statement. Full FEI remains open.

The new work here is not another lower-bound audit. It computes the **arithmetic packet profile** of the explicit merged n=14 post-Hod seed and of the public discovery ladder `g10 -> g12 -> g12* -> g14`, then asks which part of the packet decomposition actually moves when the amplification score improves.

## 1. Inputs and exact checks

The four canonical truth tables are the ones embedded in merged PR #94 of `teorth/optimizationproblems`. The accompanying script `profile_record_ladder.py` reconstructs each truth table from the canonical TRUE-set hex mask, checks the published truth-table SHA-256, computes the integer Walsh transform, and verifies the exact published total influences:

| seed | nonzero coefficients | distinct magnitude packets | exact influence | amplification score `H/(I-1)` |
|---|---:|---:|---:|---:|
| `g10` | 738 | 18 | `257/128` | `6.459372281637855...` |
| `g12` | 2176 | 50 | `259/128` | `6.474205515063261...` |
| `g12*` | 1361 | 29 | `259/128` | `6.476066828368973...` |
| `g14` | 4542 | 67 | `521/256` | `6.490112843523394...` |

The exact integer/rational checks pass. Binary64 logarithms reproduce the published entropy values to the displayed precision; the public certificates, not this binary64 recomputation, are the source of the certified transcendental endpoints.

## 2. Packet decomposition used

For each distinct nonzero Fourier magnitude `a`, let

\[
A_a=\{S:|\widehat f(S)|=a\},\qquad
p_a=|A_a|a^2,
\]

let

\[
V_a(x)=\sum_{S\in A_a}\operatorname{sgn}(\widehat f(S))\chi_S(x),
\qquad
r_a=\min_{V_a(x)\ne0}\nu_2(V_a(x)),
\]

and put `b_a=a2^{r_a}`. Write

\[
R(f)=\sum_a p_a r_a,
\qquad
D(f)=\sum_a p_a\log_2\frac1{b_a}.
\]

Then the inherited exact identity is

\[
\boxed{H(f)=2R(f)+2D(f)}.
\tag{1}
\]

The packet free-energy normalizer and KL credit are

\[
N(f)=\sum_a\frac{p_a}{b_a^2},\qquad
K(f)=D_{\rm KL,2}(p\|q),
\]

so

\[
\boxed{2D(f)=\log_2N(f)-K(f)}.
\tag{2}
\]

All `p_a`, `r_a`, `b_a`, `R`, `N`, and influences below are computed exactly with integer Walsh transforms and `Fraction` arithmetic.

## 3. Exact record-seed profile

For the merged n=14 seed `g14`,

\[
I=\frac{521}{256},\qquad
R=\frac{189797}{262144}=0.724018096923828125,
\]

\[
D=2.635122339665429\ldots,\qquad
N=\frac{7869}{2}=3934.5,
\]

and therefore

\[
\log_2N=11.94196459298614\ldots,\qquad
K=6.671719913655283\ldots.
\]

Thus the raw normalizer is enormous compared with `2D`: the negative KL credit removes about `6.67172` bits from `log_2 N`. Any magnitude-count or raw-normalizer proof that discards this credit is badly misaligned even on the known record seed.

The valuation bands are especially simple:

| valuation `r` | exact spectral mass | `D` contribution | normalized-energy `N` contribution | coefficient count | packet count |
|---:|---:|---:|---:|---:|---:|
| 0 | `80457/262144` = 0.3069191 | 0.98923022 | 3750 | 3750 | 20 |
| 1 | `173577/262144` = 0.6621437 | 1.56265967 | 180 | 720 | 42 |
| 2 | `4055/131072` = 0.0309372 | 0.08323245 | `9/2` | 72 | 5 |

There are no packet valuations outside `{0,1,2}` for this seed. In particular, the post-Hod seed is **not** driven by a long 2-adic carry tower. Most spectral mass sits at valuation one.

## 4. The decisive comparison: `g12* -> g14`

The immediately preceding merged record `g12*` has

\[
R(g_{12}^*)=\frac{8389}{16384}=0.51202392578125,
\qquad
D(g_{12}^*)=2.801900896548185\ldots.
\]

Moving to `g14`, the amplification score improves by

\[
\Delta L
=6.490112843523394\ldots-6.476066828368973\ldots
=0.014046015154421\ldots.
\tag{3}
\]

But the arithmetic remainder itself moves in the **opposite** direction:

\[
\boxed{
D(g_{14})-D(g_{12}^*)=-0.166778556882757\ldots<0.
}
\tag{4}
\]

Meanwhile the valuation head rises exactly by

\[
\boxed{
R(g_{14})-R(g_{12}^*)=\frac{55573}{262144}
=0.211994171142578125.
}
\tag{5}
\]

Normalize (1) by the O'Donnell--Tan amplification denominator `I-1`. Define

\[
L_R(f)=\frac{2R(f)}{I(f)-1},
\qquad
L_D(f)=\frac{2D(f)}{I(f)-1},
\qquad
L=L_R+L_D.
\]

For `g12*`,

\[
L_R=\frac{8389}{8384}=1.000596374045802\ldots,
\qquad
L_D=5.475470454323172\ldots.
\]

For `g14`,

\[
L_R=\frac{189797}{135680}=1.398857606132075\ldots,
\qquad
L_D=5.091255237391319\ldots.
\]

Hence

\[
\boxed{\Delta L_R=\frac{7078727}{17774080}=+0.398261232086274\ldots}
\tag{6}
\]

while

\[
\boxed{\Delta L_D=-0.384215216931853\ldots.}
\tag{7}
\]

The positive record gain (3) is the small remainder after a **large transfer from the `D` side into the valuation `R` side**. This answers the immediate B15 question about the merged n=14 seed: there is no high-depth `D` band whose growth explains the post-Hod improvement. The `D` contribution to the amplified score actually falls substantially.

The band movement is explicit. From `g12*` to `g14`, valuation-one mass rises from

\[
\frac{8389}{16384}=0.5120239\ldots
\quad\text{to}\quad
\frac{173577}{262144}=0.6621437\ldots,
\]

and a new valuation-two mass `4055/131072 = 0.0309372...` appears. This raises `R`; at the same time the finer-mesh free-energy term `D` falls.

## 5. The whole public ladder shows neither half can be optimized alone

The exact/numerical packet summaries are:

| seed | `R` | `D` | `N` | packet KL `K` | `L_R` | `L_D` |
|---|---:|---:|---:|---:|---:|---:|
| `g10` | `43317/32768` | 1.93298813 | `1545/4` | 4.72741486 | 2.62336483 | 3.83600746 |
| `g12` | `27695/65536` | 2.89038019 | 1564 | 4.83026442 | 0.82582896 | 5.64837656 |
| `g12*` | `8389/16384` | 2.80190090 | `1147/2` | 3.55984788 | 1.00059637 | 5.47547045 |
| `g14` | `189797/262144` | 2.63512234 | `7869/2` | 6.67171991 | 1.39885761 | 5.09125524 |

Two opposite moves occur in successive record improvements:

- `g10 -> g12`: the record improves while the normalized valuation contribution collapses and the `D` contribution rises;
- `g12 -> g12* -> g14`: the record improves while the `D` contribution falls and the valuation contribution rises.

So neither `R` nor `D`, nor raw `log N`, is a monotone proxy for the amplification record. The only exact conserved sum here is

\[
R+D=H/2,
\]

and the known near-extremal seeds move substantial mass between the two arithmetic ledgers while improving `H/(I-1)` only slightly.

This is a concrete obstruction to a proof strategy that tries to optimize the arithmetic remainder `D` in isolation and then pays `R` by a coarse universal inequality. The coarse payment can erase exactly the transfer visible in (6)--(7).

## 6. Structural target that survives this computation

A more faithful spectral-arithmetic route should track the **joint valuation/free-energy budget** through restriction or composition rather than pay the two pieces independently. For balanced amplification seeds the relevant objective is

\[
\frac{2(R+D)}{I-1}=\frac{H}{I-1},
\tag{8}
\]

not `D/(I-1)` alone. Equation (8) is an identity, not a new upper bound; the unsolved task is to connect this joint packet geometry to influence without collapsing either the KL credit or the valuation-transfer information.

A useful next lemma would have to be stable under the already-proved collision identity: when equal magnitudes with unequal valuations merge, an increase in `D` is exactly accompanied by a corresponding decrease in the valuation side of (1), and vice versa. Any proposed local payment should therefore charge the **net change of `R+D`**, with packet KL retained inside magnitude/depth bands, rather than charge positive `D` infection alone.

The present record-ladder computation says where to look next: not deep carry depth, but the mechanism that moves order-one spectral mass between `r=0` and `r=1` while keeping entropy high at influence only slightly above two.

## 7. Reproducibility and limits

`profile_record_ladder.py` is a clean-room exact profiler for the four public PR #94 truth tables. It checks the published SHA-256 hashes, balance, nonzero-spectrum counts and exact influences, then computes all packet valuations and exact masses. Its native run ends `PASS`; output is saved in `profile_record_ladder.out`.

Script SHA-256 in the native run: `a6502fea3fc2c0abbf4bfa6c2ea1b082bc04dc80102ac33825817961ace65bd6`.

The current n=18 record was not reprofiled here; this run used the merged n=14 truth table because it is explicit in PR #94 and already decisively post-Hod. The natural next B15 step is to ingest the n=18 certificate from merged PR #130 and test whether its certified `1/133` amplification gain is again a valuation/free-energy transfer or a genuinely new mesh-depth phenomenon.

No publication-priority claim is made for this packet accounting. Full FEI remains **OPEN**.
