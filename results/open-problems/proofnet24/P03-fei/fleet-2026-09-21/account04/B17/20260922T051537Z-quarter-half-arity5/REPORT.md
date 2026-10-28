# B17 — exact arity-5 quarter/half gate slice is nonbinding once the quarter AND constraint is retained

**Run:** `20260922T051537Z-b17-fei-r17`  
**Role:** account04/B17, FEI adversarial constructions under the current all-gate `Gamma` convergence target.  
**Outcome:** `ESSENTIAL_STEP_APPLIED / FINITE SLICE EXCLUDED`; unrestricted FEI remains **OPEN / NOT PROVED**.  
**Execution:** `WITHOUT_VERIFIED_BRAIN`. Authenticated repository control and mathematical sources were read directly; no authenticated native/cognitive-brain retrieval was consumed.

## 0. Change summary


I nevertheless consume the newest compatible other-account B15 source exactly where it matters. Account02/B15,

`proofnet24/P03-fei/fleet-2026-09-21/account02/B15/20260922T040227Z-balanced-stop-kl-fusion/REPORT.md`,

proves the exact balanced Shannon identity

\[
H(f)=I H_2(q)+T_{\rm stop}-\mathbb E\log_2(K!)-\mathcal K_\rho-\mathcal J_{\rm mix},
\]

with both genuine KL credits retained. The newer same-account B15 continuation proves that the remaining scalar occurrence functional still has sharp constant exactly `C_FEI`, so a scalar credit-preserving remainder bound is FEI-complete rather than an easier replacement. I therefore do not repeat that witness.

The other-account B15 result used directly below is account01/B15,

`proofnet24/P03-fei/fleet-2026-09-21/account01/B15/20260922T0405Z-g10-terminal-atom-feasibility/REPORT.md`,

which keeps the exact negative terminal entropy continuation for the source-valid `G10` stopping corridor and proves that, writing

\[
C=\Gamma(1/2),\qquad g=\Gamma(1/4),
\]

the terminal AND/OR atoms impose

\[
\boxed{g\le C-2},
\]

while the stopped `G10` block imposes `g>=T(C)`, with the two constraints compatible iff `C>=R(G10)`. No terminal entropy, KL credit, or branch continuation is dropped here.

The new result is an exhaustive exact Boolean computation on a genuinely five-input product-bias slice that had not been covered by the arity-2--4 sweeps. It proves that **every** balanced five-input Boolean gate at biases

\[
(1/4,1/2,1/2,1/2,1/2)
\]

is compatible with the quarter-AND upper face as soon as

\[
C\ge C_5^{\rm qh}
:=\frac{52}{5}-\frac{27}{10}\log_2 3
=6.120601248052878310\ldots .
\]

Since `R(G10)>6.45937`, this entire arity-5 slice adds **no additional center obstruction** to the exact B15 `G10` corridor. The maximizer asks for a strongly negative quadratic margin relative to the old read-once center, not a new positive margin.

## 1. Exact slice reduction

Use the owner-standard all-gate inequality

\[
\Gamma(p_{\rm out})+\widetilde H_G(p)
\le
\sum_i \operatorname{It}_i(G;p)
\frac{\Gamma(p_i)+h_2(V_{p_i})}{V_{p_i}},
\qquad V_p=4p(1-p).
\tag{1.1}
\]

Let the first input be `y` with bias `t=1/4`; let the remaining four inputs be unbiased. Restrict to gates with balanced output. Put

\[
C=\Gamma(1/2),\quad g=\Gamma(1/4),\quad
A=\frac{\operatorname{It}_y}{V_{1/4}}=\frac43\operatorname{It}_y,
\]

and let

\[
B=\sum_{i=1}^4\operatorname{It}_{x_i}.
\]

Because `V_{1/2}=1` and `h_2(1)=0`, (1.1) is exactly

\[
C+\widetilde H_G
\le BC+A\bigl(g+h_2(3/4)\bigr).
\tag{1.2}
\]

The exact terminal-AND constraint from the B15 corridor is `g<=C-2`. Hence a **necessary condition for compatibility with that upper face** is

\[
\widetilde H_G+A\bigl(2-h_2(3/4)\bigr)
\le C(A+B-1).
\tag{1.3}
\]

For `A+B>1`, define the exact center demand

\[
\boxed{
C_{\rm req}(G)
=
\frac{\widetilde H_G+A(2-h_2(3/4))}{A+B-1}.
}
\tag{1.4}
\]

If `C>=C_req(G)`, the gate lower bound on `g` does not exceed the terminal-AND upper bound `C-2`. The only zero-currency case in the complete slice is a character independent of `y`, for which `H=0`, `A=0`, `B=1` and (1.2) is equality automatically.

Thus the exact adversarial question on this whole slice is to maximize (1.4) over actual Boolean gates.

## 2. Exact Boolean parameterization and normalization

Write the two four-bit restrictions as truth tables `G_0,G_1` on `Q_4`, and let `k_0,k_1` be their numbers of positive/output-one rows. Since `Pr(y=1)=1/4`, output balance is equivalent to

\[
\frac34\frac{k_0}{16}+\frac14\frac{k_1}{16}=\frac12,
\qquad\text{i.e.}\qquad
3k_0+k_1=32.
\tag{2.1}
\]

The only possibilities are

\[
(k_0,k_1)\in\{(6,14),(7,11),(8,8),(9,5),(10,2)\}.
\tag{2.2}
\]

Let `a_T,b_T` be the **integer unnormalised Walsh sums** of the two `Q_4` branches. For every `T subseteq [4]`, the full five-input biased squared Fourier masses are exactly

\[
\boxed{
P(T)=\frac{(3a_T+b_T)^2}{4096},
\qquad
P(T\cup\{y\})=\frac{3(b_T-a_T)^2}{4096}.
}
\tag{2.3}
\]

So all Fourier masses, all influences and every normalization identity are exact rationals before the final logarithms are evaluated. In particular,

\[
\operatorname{It}_y
=\sum_TP(T\cup\{y\}),
\qquad
B=\sum_T |T|\,[P(T)+P(T\cup\{y\})].
\tag{2.4}
\]

No arbitrary spectral probability law is introduced: every row of the search is an actual Boolean truth table.

## 3. Complete arity-5 slice enumeration

The four unbiased coordinates admit the full cube automorphism group of size

\[
4!\,2^4=384.
\]

I canonicalize `G_0` under this simultaneous action and enumerate **every** `G_1` of the required weight. This is complete because applying one cube automorphism to both branches preserves the product-bias slice and sends `G_1` to another table in the enumerated same-weight family.

The canonical branch counts and exact pair counts are:

| `(k0,k1)` | canonical `G0` orbits | all `G1` | evaluated pairs | maximum `C_req` |
|---|---:|---:|---:|---:|
| `(6,14)` | 50 | 120 | 6,000 | `6.120601248052878...` |
| `(7,11)` | 56 | 4,368 | 244,608 | `6.011041922388331...` |
| `(8,8)` | 74 | 12,870 | 952,380 | `6` |
| `(9,5)` | 56 | 4,368 | 244,608 | `6.011041922388331...` |
| `(10,2)` | 50 | 120 | 6,000 | `6.120601248052878...` |

Total exact Boolean gate pairs evaluated:

\[
\boxed{1,453,596}.
\]

They collapse to 12,138 exact spectral/influence signatures. The checker first computes all Walsh data as integers, then independently re-evaluates every distinct signature at 100 decimal digits. The next distinct signature lies at

\[
6.01104192238833175545\ldots,
\]

leaving a gap greater than `0.1095` below the maximum.

## 4. Exact maximizer

One maximizing representative has branch-positive sets

\[
G_0^+=\{0,1,2,3,4,5\},
\]

and

\[
G_1^+=\{0,1,2,3,4,5,6,8,9,10,11,12,13,14\}.
\]

Equivalently the 16-bit branch masks are `63` and `32639`. Its exact integer Walsh vectors are

\[
a=(-4,0,4,0,4,0,-4,0,12,0,4,0,4,0,-4,0),
\]

\[
b=(12,4,4,-4,4,-4,-4,4,0,0,0,0,0,0,0,0).
\]

The no-`y` mass numerators over `4096` occur with multiplicities

\[
1296^1,\;256^3,\;144^3,\;16^4,\;0^5,
\]

and the `y`-layer numerators with multiplicities

\[
768^1,\;432^1,\;48^7,\;0^7.
\]

Therefore, by direct simplification,

\[
\boxed{
\widetilde H_G
=\frac{13}{2}-\frac{33}{16}\log_2 3
=3.23101484226261537575\ldots
}
\tag{4.1}
\]

and

\[
\operatorname{It}_y=\frac38,
\qquad A=\frac12,
\qquad B=\frac98,
\qquad A+B-1=\frac58.
\tag{4.2}
\]

Since

\[
2-h_2(3/4)=\frac34\log_2 3,
\]

substitution into (1.4) gives

\[
\boxed{
C_{\rm req}^{\max}
=\frac{52}{5}-\frac{27}{10}\log_2 3
=6.12060124805287831007\ldots .
}
\tag{4.3}
\]

The complement-symmetric `(10,2)` case attains the same value.

## 5. Consequence for the live all-gate problem

Account01/B15 proves that the exact `G10` stopped corridor and its terminal AND/OR atoms are compatible iff

\[
C\ge R(G10)>6.4593722816378557311\ldots,
\]

with one common quarter value satisfying

\[
T(C)\le g\le C-2.
\tag{5.1}
\]

Because

\[
R(G10)>6.45937>6.120601248052878\ldots,
\]

every one of the 1,453,596 arity-5 gates in the present slice has its own lower bound on `g` at or below `C-2` whenever the B15 corridor is feasible. Hence the finite collection consisting of

1. the full B15 `G10` stopping corridor, including its exact negative terminal continuation, and
2. **every** balanced five-input Boolean gate at biases `(1/4,1/2,1/2,1/2,1/2)`

has a nonempty common interval for `Gamma(1/4)` for every `C>=R(G10)`.

This is a genuine exclusion of a complete untouched arity-5 slice. It is not a universal arity-5 theorem and not a proof of FEI. A counterexample to the current extremality picture must leave this slice, for example by using multiple non-half biases, an output bias different from `1/2`, or another product-bias geometry.

### Owner-requested margin units

At the old read-once center `C0=6.4548`, the symmetric quarter AND line is tight at `g=C0-2`. For the maximizer above,

\[
D_G=\frac58(C_0-C_{\rm req}),
\]

while the Poincare currency in the owner's margin definition is

\[
W=\frac{I(G;p)}4-\frac14
=\frac{3/2}{4}-\frac14
=\frac18.
\]

Thus its actual quadratic margin is

\[
\boxed{
c_G=-D_G/W
=5(C_{\rm req}-C_0)
=-1.670993759735608\ldots<0.
}
\tag{5.2}
\]

So even the worst gate on this slice has substantial slack in the comparable `c_G` units; it does not threaten the positive AND margin.

## 6. Verification and limitations

`CHECK.py` is standard-library only. It:

- constructs all exact `Q_4` Walsh sums;
- constructs the full 384-element cube automorphism group;
- verifies the canonical orbit counts `50,56,74,56,50`;
- evaluates all `1,453,596` covered Boolean branch pairs with exact integer spectral numerators;
- verifies that the only zero Poincare-currency signature is a character (`H=0,A=0,B=1`);
- collapses the enumeration to 12,138 exact signatures;
- independently replays all transcendental comparisons at 100-decimal-digit precision;
- verifies the exact maximizing histogram, influences, entropy formula and center-demand formula.

Executed checker SHA-256:

`d1af3e0df39a2f034dfad6eab4c6513884bcef77f63e4f5533bfc38b453dc7cb`

Captured output SHA-256:

`98f543dd54f79bb853a2c80a4c55d691f2955fedfb245bd70db15fe9b2c31a13`

The finite certificate is self-checked here and is not represented as an independently reviewed theorem. It certifies exactly this product-bias/output-balance slice; it does not certify all 616,126 five-input NPN classes over all bias vectors.

## 7. Next exact adversarial target

The result narrows the owner's arity-5 falsification job rather than opening another proof route. The next B17 attack should keep the same all-gate target and move to the closest genuinely new bias geometry: either

- two quarter-biased coordinates and three unbiased coordinates with the exact feasible output-bias classes, or
- one quarter-biased coordinate with an unbalanced output, retaining every exact `Gamma` value constraint inherited from the current B15 corridor.

The objective is unchanged: produce an actual Boolean gate whose comparable `c_G` exceeds the AND constraint, or rigorously exclude another complete slice without discarding child slack, terminal continuation, or information credits.
