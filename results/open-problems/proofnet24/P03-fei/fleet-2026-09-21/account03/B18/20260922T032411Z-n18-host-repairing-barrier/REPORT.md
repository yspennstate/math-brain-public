# account03/B18 — the n=18 source gate is the unique best two-cell host pairing

**Run:** `20260922T032411Z-B18-a11`  
**Common candidate:** `LIMIT-PRIME-GATE-LIFT-v1`  
**Sub-attack:** `N18-HOST-REPAIR-v1`  
**Outcome:** `ESSENTIAL_STEP_APPLIED / EXACT_ADVERSARY_FAMILY_REFUTED`  
**Full uniform-cube FEI:** **OPEN / NOT PROVED**.  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

## 1. Fixed universal target and peer artifacts actually consumed

The fixed common target is the account01/B18 candidate

\[
C_*=6.5218512,
\qquad
\Gamma_*(p)=\Gamma_{RO}(p)+0.2682048\,p(1-p),
\]

with the still-unpaid universal implication

\[
D_{\Gamma_*}(P;p)\ge0
\tag{1.1}
\]

for every finite composition-prime Boolean gate `P` and every interior product-bias vector `p`.  By the exact gate-composition cocycle, (1.1) would imply the all-gate inequality and hence full FEI with constant `C_*`.  This report does **not** prove (1.1).

The named completed other-account artifact consumed substantively is

`account01/B12/20260922T011847Z-prime-n18-gate/REPORT.md`, blob
`9ab98c0e82f7cf0f34eac98923df23b7b160670b`.

It gives the exact source-valid balanced monotone 18-variable gate with

\[
I_0=\frac{261}{128}
\]

and certified entropy interval

\[
6.776605309005978082519790221891882314787235038
\le H_0\le
6.776605309005978082519790221891882314787235039.
\tag{1.2}
\]

It also reconstructs the gate as a nine-bit core plus nine host bits.  The 18 distinct core cells switched by the hosts are

\[
T=\{78,79,113,121,228,484,170,186,149,151,338,466,284,316,291,295,393,457\},
\]

with source pairing

\[
P_0=\{(78,79),(113,121),(228,484),(170,186),(149,151),
(338,466),(284,316),(291,295),(393,457)\}.
\tag{1.3}
\]

The previous source report proves this particular gate is composition-prime.  Here I use its exact source reconstruction to test a materially different adversarial mechanism: **keep the same 18 exceptional core cells, but re-pair them among the nine host bits in every possible way.**

## 2. The complete re-pairing family

Let `f_core:{0,1}^9->{-1,1}` be the source core, with the convention that each cell of `T` is a false core cell and hence has value `+1`.  For any perfect matching

\[
P=\{\{x_j,x'_j\}:1\le j\le9\}
\]

of the 18 points in `T`, introduce nine host bits `y_j` and define the Boolean gate `F_P` by

\[
F_P(x,y)=
\begin{cases}
(-1)^{y_j},&x\in\{x_j,x'_j\},\\
f_{core}(x),&x\notin T.
\end{cases}
\tag{2.1}
\]

This includes the published source gate at `P=P_0`.  Every `F_P` is a genuine finite Boolean gate.  It is also balanced: the core contains 247 true cells and 265 false cells, so deleting the 18 exceptional `+1` rows leaves zero signed mean; every exceptional row has zero host-average.  Monotonicity is not required for FEI, so arbitrary re-pairings remain admissible Boolean adversaries even when they destroy monotonicity.

There are exactly

\[
\frac{18!}{2^9 9!}=34,459,425
\tag{2.2}
\]

such perfect matchings.

## 3. Exact Fourier decomposition

Put `a(x)=f_core(x)` for `x notin T` and `a(x)=0` on `T`.  For a core character `chi_S` and a host character indexed by `U`, direct averaging over the host cube gives

\[
\widehat F_P(S,U)=
\begin{cases}
\widehat a(S),&U=\varnothing,\\
2^{-9}[\chi_S(x_j)+\chi_S(x'_j)],&U=\{j\},\\
0,&|U|\ge2.
\end{cases}
\tag{3.1}
\]

Thus the empty-host Fourier block depends only on the fixed set `T`, not on its pairing.

Fix one pair `{x,x'}` and let `d=x\oplus x'`.  Since `x!=x'`, exactly half of all 512 core characters obey `S dot d=0`.  On those 256 characters the squared coefficient is exactly

\[
\left(\frac2{512}\right)^2=2^{-16},
\]

and it vanishes on the other 256.  Consequently every pair contributes exactly

\[
256\,2^{-16}\cdot16=\boxed{\frac1{16}}
\tag{3.2}
\]

to spectral entropy, independently of the pair geometry.

### Theorem 3.1 — entropy is invariant under all 34,459,425 re-pairings

For every perfect matching `P` of the fixed source set `T`,

\[
\boxed{H(F_P)=H_0.}
\tag{3.3}
\]

This is an exact all-dimensional-within-family identity, not an exhaustive numerical comparison.

## 4. Exact influence penalty for breaking a source pair

The same one-pair block contributes

\[
2^{-16}\sum_{S:S\cdot d=0}(|S|+1)
\tag{4.1}
\]

to total influence, where the `+1` is the active host coordinate.

If `|d|=1`, the unique coordinate in the support of `d` is forced absent and the other eight coordinates are unbiased, so `E|S|=4`.  Hence the pair contribution is

\[
\boxed{\frac5{256}}.
\tag{4.2}
\]

If `|d|>=2`, every one of the nine core coordinates is unbiased under the single even-parity constraint, so `E|S|=9/2`.  Hence the contribution is

\[
\boxed{\frac{11}{512}}
=\frac5{256}+\boxed{\frac1{512}}.
\tag{4.3}
\]

The source reconstruction has a further rigid feature verified directly from the 18 cell labels:

> the **only** Hamming-distance-one edges inside `T` are the nine source pairs in (1.3).

Therefore `P_0` is the unique perfect matching using only adjacent pairs.  If `k(P)` denotes the number of nonadjacent pairs in a matching, then

\[
\boxed{I(F_P)=\frac{261}{128}+\frac{k(P)}{512}.}
\tag{4.4}
\]

Moreover `k(P)=0` only for `P=P_0`.  For every other perfect matching, `k(P)>=2`: the symmetric difference of two perfect matchings is a union of alternating even cycles, so a changed matching cannot differ in exactly one edge.

### Theorem 4.1 — the published pairing uniquely maximizes the balanced FEI obstruction

Combining (3.3) and (4.4),

\[
\boxed{
R(P):=\frac{H(F_P)}{I(F_P)-1}
=\frac{512H_0}{532+k(P)}.
}
\tag{4.5}
\]

Hence `P_0` is the unique maximizer among all 34,459,425 pairings.  Every non-source pairing satisfies

\[
R(P)\le \frac{512H_0}{534}.
\tag{4.6}
\]

Using only the certified entropy interval (1.2),

\[
R(P_0)
<6.521845710923046575658143972948578468366662293173
<6.5218512=C_* ,
\tag{4.7}
\]

with stable-center gap at least

\[
\boxed{5.4890769534243418560270514215\times10^{-6}.}
\tag{4.8}
\]

Every non-source re-pairing is much farther below:

\[
\boxed{
R(P)<6.497419322492623180243693995522.
}
\tag{4.9}
\]

Thus the exact adversarial claim

> some re-pairing of the published n=18 gate's same 18 exceptional cells among its nine two-cell host channels violates the balanced center `C_*`

is **REFUTED** for the entire family.

## 5. What changed and what remains unpaid

This result rules out 34,459,425 actual Boolean variants analytically, including nonmonotone variants; it is stronger than a local swap search.  It also identifies the mechanism: with the exceptional support fixed, pair geometry cannot buy entropy at all, while every broken source edge pays a quantized `1/512` influence penalty.

It does **not** prove `LIMIT-PRIME-GATE-LIFT-v1`.  The unpaid universal arrow remains

\[
D_{\Gamma_*}(P;p)\ge0
\quad\text{for every composition-prime }P\text{ and every product bias }p.
\tag{5.1}
\]

The theorem covers only the uniform balanced slice of the fixed-support two-cell-host family.  It does not cover biased input vectors, replacing the 18 exceptional cells, changing host group sizes, or changing the shared core.  Those are the legitimate next adversarial degrees of freedom.

The most useful next attack is therefore **not another re-pairing**.  In the source-valid shared-core construction, account02/B16 has already localized a stable-candidate threat to an extremely narrow singleton/defect corridor.  The next recipients should test a changed exceptional support or genuinely heterogeneous host grouping against that same `C_*`, or prove a joint realizability obstruction for the corridor.  On the builder side, the quantized pairing penalty may be used as a rigidity lemma when classifying near-saturating fixed-core gates.

**Final status:** exact failed adversarial mechanism / useful rigidity theorem; **full FEI remains OPEN / NOT PROVED**.
