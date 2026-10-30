# B18 FEI integration — a scalar depth-defect threshold that forces an adaptive certificate

**Run:** `20260921T223832Z-b18-fei-r16`  
**Execution:** **WITHOUT_VERIFIED_BRAIN**  
**Status:** **PARTIAL. Full uniform-cube Fourier entropy--influence remains OPEN / NOT PROVED.**  
**Claim level:** universal source-exact implication obtained by composing completed interface-B stability with the interface-A physical peeling theorem and the newest fleet01/B18 folded-cooling compiler. No novelty or publication-priority claim.

## 0. What changed

The preceding B18 run localized the hard branch to a physical restriction core with no currently certified near-subcube trigger, but its stopping condition was geometric: for a maximum-influence pivot `x`, every codimension-`r` coordinate-subcube proxy had support error larger than `2^-r/(16r)`.

This run converts that geometric stopping condition into a **pure scalar condition on the pivot's folded influence and normalized depth defect**. The conversion is exact enough to feed the newest fleet01/B18 adaptive compiler:

> if a maximum-influence row has sufficiently small positive depth defect relative to `log2(1/j_x)`, then the fleet04/B13 stability proxy automatically satisfies the fleet04/B14 `q/(16r)` accuracy threshold, so a genuine physical block certificate exists and is paid by the existing adaptive telescope.

The threshold has a closed Lambert-W form. Consequently every terminal leaf of the recursive fleet04/B14 peeling policy has a quantitative positive-defect floor at its maximum-influence coordinate. At the same time, the newest fleet04/B12 theorem already pays that row's **codimension address** by its nonreused factorial share, so the surviving obstruction is not raw trigger-address length.

A new fleet01/B13 result landed during this invocation and is also integrated below: it converts the fleet04/B13 branch-character label entropy to a selected external mixed-boundary bank. I retain that bank explicitly; I do **not** replace it by the uncontrolled full second-factorial depth moment.

## 1. Exact completed inputs

All paths are under `proofnet24/P03-fei/fleet-2026-09-21/`.

1. **fleet01/B18 newest compatible adaptive synthesis**  
   `fleet01/B18/20260921T2205Z-folded-cooling-compiler/REPORT.md`, blob `9f2bb40584be20e5e440e7f3913873c34858bc91`.  
   It defines the character-invariant folded activation potential `A_z`, proves the nonreusing descendant-recentered telescope, and gives the conditional `(gamma,K,lambda)` compiler. Its curvature-refunded predecessor is `fleet01/B18/20260921T1856Z-curvature-refunded-crossing/REPORT.md`, blob `ef9f471c019a7d81e9864fd457a0e4bae9da890d`.

2. **fleet04/B12 newest harmonic companion code**  
   `fleet04/B12/20260921T220950Z-harmonic-companion-row-code/REPORT.md`, blob `c69ea11272bcfe9590a8d05dc662f336e313af05`.  
   For a physical near-subcube row with `|2^-r-j|<=j/16`, it proves the coefficient-one factorial address payment
   \[
   j\log_2(r+1)\le Q_x+\frac{19}{4}j,
   \tag{1.1}
   \]
   where `Q_x` is the row's exact nonoverlapping share of `E log2(K!)`.

3. **fleet04/B13 newest all-row stability / proxy-gauge closure**  
   `fleet04/B13/20260921T2225Z-proxy-gauge-closure/REPORT.md`, blob `1ec1555932e690e403f7d4320640040628697b96`.  
   For a low positive depth-defect row it supplies a coordinate-subcube support proxy with a quantitative error bound; after one source-frontier reveal it also proves an exact branchwise character gauge whose expected residual influence is paid by the defect bank.

4. **fleet04/B14 newest recursive certified peeling**  
   `fleet04/B14/20260921T221102Z-recursive-certified-peeling/REPORT.md`, blob `253268f70202891aa12c36d2ff4cf76519fa8241`.  
   If a maximum-influence pivot has a codimension-`r` support proxy of density `q=2^-r` with error `e<=q/(16r)`, then its physical control block is a genuine fleet01/B18 certificate with
   \[
   \gamma\ge\frac{14}{15},\qquad K=12,
   \tag{1.2}
   \]
   and recursively peeling all such blocks spends at most `12J(root)` total Shannon decrement. Every terminal leaf satisfies the negation of this geometric condition.

5. **fleet04/B18 mixed-curvature rigidity**  
   `fleet04/B18/20260921T191147Z-mixed-curvature-global-rigidity/REPORT.md`, blob `0e8c2cc28da81af8843b565cb47285684b164480`.  
   It proves
   \[
   \kappa_{ik}=p_{ik}+4o_{ik}=\kappa_{ki},
   \qquad
   \sum_{i\ne k}(p_{ik}+4o_{ik})=4d_k,
   \tag{1.3}
   \]
   and classifies the exact all-row zero-defect endpoint as a character-twisted one-point defect, hence `H<4J` there.

6. **new other-account result consumed during this invocation**  
   `fleet01/B13/20260921T223500Z-label-boundary-curvature/REPORT.md`, blob `7ef3c7b171d03943818ba28cc96f71442b9d30fa`, scientific commit `7a15319c636278e13c33389291572cb5c3adef43`.  
   It proves for the fleet04/B13 source-frontier character label `T`
   \[
   H(T)\le \frac{17}{8}J+\frac{15}{14}\mathcal P_{\rm ext},
   \tag{1.4}
   \]
   where `P_ext` is the selected external source-to-control support-boundary bank. It explicitly does **not** prove `P_ext=O(J)`.

Known false bridges remain excluded: `sum d_i=O(J)`, prescribed-coordinate payment, fixed-relative `q/16` in place of `q/(16r)`, ambient-alphabet Fannes continuity, unconditional `R_pref=O(I)`, and dropping the total-correlation or negative-credit terms.

## 2. Setup and the stability function

Median-character center the current nonconstant Boolean state. For a maximum-influence coordinate `x`, write

\[
 j:=\operatorname{Inf}_x(f)\le\frac12,
 \qquad
 L:=\log_2\frac1j\ge1,
\]

and define its normalized depth defect

\[
 \delta:=\frac{d_x}{j}-\frac12L\ge0.
 \tag{2.1}
\]

Let `eta_0<=1/32` be the low-defect threshold inherited by the newest fleet04/B13 theorem. In the range `0<delta<=eta_0`, that theorem supplies a coordinate subcube

\[
 Q=\{z_F=a\},
 \qquad r:=|F|,
 \qquad q:=2^{-r},
\]

with support error

\[
 e:=\mu(E_x\triangle Q),
 \qquad
 \alpha:=\frac ej,
\]

satisfying

\[
 \boxed{
 \alpha\le
 \phi(\delta):=
 \frac{4\delta}{\log_2(1/(2\delta))}
 \le\delta\le\frac1{32}.
 }
 \tag{2.2}
\]

Because symmetric-difference error controls density error,

\[
 |q-j|\le e=\alpha j.
 \tag{2.3}
\]

Set

\[
 c_0:=\log_2\frac{32}{31}=0.0458036896131247\ldots .
 \tag{2.4}
\]

Equation (2.2)--(2.3) gives

\[
 q\ge(1-\alpha)j\ge\frac{31}{32}j,
\]
so

\[
 \boxed{r\le L+c_0.}
 \tag{2.5}
\]

This elementary conversion is what lets the physical `q/(16r)` threshold be expressed in terms of the scalar pair `(j,delta)`.

## 3. New proved theorem: scalar defect-to-adaptive-certificate compiler

For real `s>=1`, define

\[
 A(s):=4\ln2\,(16s+1)
\]

and

\[
 \boxed{
 \delta_*(s):=
 \frac{W\!\left(2\ln2\,(16s+1)\right)}
 {4\ln2\,(16s+1)},
 }
 \tag{3.1}
\]

where `W` is the principal Lambert-W function. Equivalently, `delta_*(s)` is the unique positive solution of

\[
 \boxed{
 \phi(\delta_*(s))=\frac1{16s+1}.
 }
 \tag{3.2}
\]

The equivalence is immediate: if `A=A(s)`, then the equality in (3.2) is

\[
 A\delta=\ln\frac1{2\delta},
\]
which rearranges to `(A delta)e^(A delta)=A/2`.

The function `phi` is strictly increasing on `(0,1/2)` because, in natural logs,

\[
 \phi(\delta)=\frac{4\ln2\,\delta}{\ln(1/(2\delta))}
\]

has derivative proportional to `ln(1/(2delta))+1>0` in the present range. Therefore `delta_*(s)` is strictly decreasing in `s`.

### Theorem 3.1 — scalar sufficient condition for a genuine physical certificate

Assume `0<delta<=eta_0`. If

\[
 \boxed{
 \delta\le\delta_*(L+c_0),
 \qquad L=\log_2(1/j),
 }
 \tag{3.3}
\]

then the physical proxy `Q` supplied by fleet04/B13 automatically obeys

\[
 \boxed{e\le\frac{q}{16r}.}
 \tag{3.4}
\]

Since `x` is maximum influence, its defining block `F` also obeys

\[
 I_F\le rj.
 \tag{3.5}
\]

Consequently fleet02's near-support block theorem and the newest fleet04/B14 theorem apply. The block `F` satisfies

\[
 \boxed{
 \Delta_F H\le12I_F,
 \qquad
 c_x(F)\ge\frac{14}{15}j,
 \qquad
 I_F\le h_2(j).
 }
 \tag{3.6}
\]

In particular it is a valid fleet01/B18 folded-cooling certificate

\[
 \boxed{(\gamma,K,\lambda)=(14/15,12,\lambda)}
 \tag{3.7}
\]

for every fixed `lambda>=0`.

#### Proof

By (3.3), monotonicity of `phi`, and the definition of `delta_*`,

\[
 \alpha\le\phi(\delta)
 \le\frac1{16(L+c_0)+1}.
 \tag{3.8}
\]

By (2.5), `r<=L+c_0`, so

\[
 \alpha\le\frac1{16r+1}.
 \tag{3.9}
\]

Now (2.3) gives `q>=j-e=(1-alpha)j`. Hence

\[
 16r e=16r\alpha j
 \le(1-\alpha)j
 \le q,
\]
which is (3.4). Maximum influence gives (3.5). The already proved fleet02/fleet04 block and crossing theorems then give (3.6), and fleet01/B18's newest compiler definition gives (3.7). QED.

### Interpretation

This is a direct source-to-next-arrow integration of interfaces B and A. It replaces the statement

> "perhaps the stability proxy is accurate enough to use the physical block theorem"

by a checkable scalar criterion on the actual row invariants `j` and `delta`. No coordinate is prescribed in advance; the subcube comes from the completed Boolean stability theorem, and the physical restriction is the already verified B14 adaptive block.

## 4. New terminal-core corollary: every surviving maximum row has positive defect at the correct rarity scale

Apply the newest fleet04/B14 recursive policy until it stops. At any nonconstant terminal leaf, let `x` be a maximum-influence coordinate, with `j,L,delta` as above.

### Corollary 4.1 — terminal defect floor

Every such pivot satisfies

\[
 \boxed{
 \delta>
 \min\left\{\eta_0,\,\delta_*(L+c_0)\right\}.
 }
 \tag{4.1}
\]

Indeed, if `delta>eta_0` there is nothing to prove. If `delta<=eta_0`, Theorem 3.1 shows that `delta<=delta_*(L+c_0)` would produce another certifiable B14 block, contradicting terminality.

Equivalently, if one keeps the actual stability-proxy codimension `r`, every low-defect terminal pivot satisfies the slightly sharper

\[
 \boxed{
 \delta>\delta_*(r)
 =\frac{W(2\ln2(16r+1))}{4\ln2(16r+1)}.
 }
 \tag{4.2}
\]

The calculation delivered with this report gives

| `r` | `delta_*(r)` |
|---:|---:|
| 1 | 0.049195868187241 |
| 2 | 0.030550467626387 |
| 3 | 0.022746105337993 |
| 4 | 0.018341365822895 |
| 8 | 0.010738496469958 |
| 16 | 0.006168219922602 |
| 32 | 0.003490436954822 |
| 64 | 0.001951510501967 |

Because `eta_0<=1/32`, a codimension-one stability proxy can **never** be a low-defect terminal maximum row: `delta_*(1)>1/32`.

This is not a uniform positive constant as `j->0`; asymptotically the floor decays on the order of `log L/L`. It therefore does not by itself close FEI. Its value is structural: after the already-paid adaptive phase, arbitrarily tiny positive depth defect cannot survive unless the row is correspondingly rare/high-codimension.

## 5. New integration with B12: the surviving low-defect row's codimension address is already paid

For every low-defect row in the range of Section 2, (2.2) gives `alpha<=1/32`. Therefore

\[
 |q-j|\le e\le\frac1{32}j<\frac1{16}j.
 \tag{5.1}
\]

The newest fleet04/B12 harmonic-companion theorem applies immediately, without any extra Palm-TV hypothesis, and yields

\[
 \boxed{
 j\log_2(r+1)
 \le Q_x+\frac{19}{4}j.
 }
 \tag{5.2}
\]

Thus when a low-defect maximum row survives because its defect lies above the threshold (4.2), the remaining difficulty is **not** the raw codimension-address logarithm `j log(r+1)`: that term is already charged to the row's exact nonoverlapping factorial share plus a linear influence term.

This is important for nonreuse. The proof does not charge `rj` to the raw second derivative depth, and it does not spend the global factorial rebate twice.

## 6. Integrating the late fleet01/B13 label theorem

The newest fleet04/B13 one-shot proxy construction leaves a branch-dependent character label `T(z)`. The fleet01/B13 result that landed during this invocation proves

\[
 H(T)\le\frac{17}{8}J+\frac{15}{14}\mathcal P_{\rm ext}.
 \tag{6.1}
\]

Therefore the old phrase "pay the character-label entropy" is superseded. Its internal reciprocal-component part is already `O(J)`; the sole label-side positive term is the selected external mixed-boundary bank `P_ext`.

The present scalar compiler and terminal theorem do **not** prove

\[
 \mathcal P_{\rm ext}=O(J).
\]

Nor do they replace it by

\[
 \sum_k d_k,
\]

because the latter is the uncontrolled second-factorial bank already known not to be universally linear in `J`.

What the present theorem contributes is a clean routing rule for the external-target side: whenever the relevant maximum row lies below the scalar defect threshold, interface A removes it with a fully paid physical block. A genuinely terminal core must instead carry the positive-defect floor (4.1), while B12 has already removed its trigger-address logarithm from the unpaid ledger.

## 7. Smallest honest universal chain after this run

The current source-exact chain is now:

1. **PROVED — adaptive paid phase.** Every state with a maximum pivot satisfying the scalar criterion (3.3) admits a genuine `(14/15,12,lambda)` physical certificate. Recursively applying the B14 policy spends at most `12J(root)` total Shannon decrement.

2. **PROVED — terminal positive-defect localization.** Every nonconstant terminal leaf has a maximum pivot satisfying the rarity-dependent positive-defect floor (4.1). The exact zero-defect all-row phase remains separately classified by B18 as a character-twisted one-point defect with `H<4J`.

3. **PROVED — codimension address nonreuse.** In the low-defect stability sector, the maximum row's `j log(r+1)` address is paid by its own factorial share as in (5.2).

4. **PROVED — branch-label localization.** The fleet01/B13 theorem reduces the source-frontier branch-label Shannon term to `17J/8+(15/14)P_ext`.

5. **OPEN — external/exceptional contraction.** A universal nonreusing payment is still missing for the selected external mixed-boundary bank `P_ext` together with the high-defect / above-threshold terminal sector and the explicit B12 off-trigger/nonrobust companion channels. The fleet04/B13 proxy-gauged residual influence itself is defect-paid, but its parent-to-child physical Shannon recursion is not automatically free.

Nothing in items 1--4 implies item 5. In particular no conditional input is promoted to unconditional FEI closure.

## 8. Decisive calculation

`check_terminal_defect_certificate.py` was executed with the standard Python math library. It computes the unique roots of (3.2) by monotone bisection and checks the algebraic implication

\[
 \alpha\le\frac1{16r+1}
 \Longrightarrow
 16r\alpha\le1-\alpha
\]

for `1<=r<=4096`.

The maximum root-equation residual was `6.939e-18`; the maximum numerical violation of the final algebraic implication was `1.110e-16` (floating roundoff). The theorem itself is analytic; this calculation only calibrates the threshold and guards arithmetic/transcription mistakes.

Delivered checker commit: `88a71a095475addfc3e185de3b459d04221fd0dd`.  
Delivered output commit: `7689bb03f262bd959b59afa95968f243bbc5be09`.

## 9. Next implication

The next B18 target is now narrower than in the preceding run:

> On a terminal physical core satisfying (4.1), prove that the **selected** external source-to-control bank `P_ext` plus the B12 explicit off-trigger/nonrobust companion channels is absorbed by the positive depth-defect / folded-activation / curvature-refund resources with no reuse.

The scalar low-defect branch below `delta_*(L+c0)` no longer belongs to that target: it is already compiled into a paid physical certificate. The exact zero-defect branch is already classified. The codimension address is already factorial-paid. What remains is the genuinely positive-defect external/exceptional interaction.

**Full FEI remains OPEN / NOT PROVED.**
