# fleet04/B14 — Schur-convex amplification of the terminal MUX data-block credit

**Classification:** `ESSENTIAL_STEP_APPLIED / STRICT_POINTWISE_MARGIN_FILTER / FULL_FEI_OPEN`.  
**Execution:** `WITHOUT_VERIFIED_BRAIN`. Authenticated repository mathematics was read directly; no authenticated native mathematical-brain retrieval/receiver context or formal-kernel runtime entered this derivation.  
**Full uniform-cube FEI:** **OPEN / NOT PROVED.**

## 0. Live scope and exact target

The current owner control converges FEI work on the all-gate margin formulation. The live source-defined candidate used by the current MUX branch is

\[
C^\dagger=6.521851214,\qquad C_0=6.4548,
\qquad a^\dagger=4(C^\dagger-C_0)=0.268204856,
\]
\[
\Gamma^\dagger(z)=\Gamma_0(z)+a^\dagger z(1-z).
\]

For the one-bit MUX
\[
M(A;D_0,D_1)=D_A,
\qquad \Pr(A=1)=t,
\qquad \Pr(D_j=1)=q_j,
\]
write
\[
V_j=4q_j(1-q_j),
\qquad
W_M=t(1-t){V_0+V_1\over4}.
\]
The preceding terminal physical data-block theorem (fleet03/B14, `20260922T073515Z-mux-data-block-selector`) reveals the original coordinates `T={D0,D1}`. Every child is a constant or literal, and it proves
\[
D_\Gamma(M)=\mathcal R_{\Gamma,D}+\mathcal C_D,
\]
\[
\mathcal C_D=H(Z\mid S)+I(S;K)+\operatorname{TC}(K)\ge0.
\]
For the block-spectrum subset `K`,
\[
\Pr(K=\{D_0\})=a:=V_0(1-t),
\qquad
\Pr(K=\{D_1\})=b:=V_1t,
\]
\[
\Pr(K=\varnothing)=1-a-b.
\]
It used only the coarse estimate
\[
\operatorname{TC}(K)\ge {ab\over\ln2},
\]
which led to
\[
{\mathcal C_D\over W_M}
\ge {4V_0V_1\over\ln2\,(V_0+V_1)}.
\tag{0.1}
\]
The newest fleet01/B18 MUX residual (`20260922T080302Z-mux-newborn-cancellation-121`) retains this exact data-block filter while sharpening a deterministic-data boundary layer. The present run attacks the information-credit term itself by a different method.

## 1. Sharp fixed-sum theorem for the mutual-exclusion credit

For `a,b>=0`, `a+b<=1`, define the mutual-exclusion total correlation in **nats**
\[
F(a,b):=(1-a-b)\ln(1-a-b)
-(1-a)\ln(1-a)-(1-b)\ln(1-b),
\tag{1.1}
\]
with `0 ln 0=0`. Thus `TC(K)=F(a,b)/ln 2`.

Put `r=a+b`. For `0<r<=1`, define
\[
\boxed{
\phi(r):={4\over r^2}
\left[(1-r)\ln(1-r)
-2\left(1-{r\over2}\right)\ln\left(1-{r\over2}\right)
\right],
}
\tag{1.2}
\]
and set `phi(0)=1` by continuity.

### Theorem 1.1 — Schur-convex mutual-exclusion amplification

For every `a,b>=0`, `a+b<=1`,
\[
\boxed{F(a,b)\ge ab\,\phi(a+b).}
\tag{1.3}
\]
For fixed `r=a+b` in `(0,1]`, equality is attained at `a=b=r/2`; away from degenerate boundary limits this is the unique minimizer of `F(a,b)/(ab)`. Moreover `phi(r)` is increasing and
\[
\phi(r)>1\qquad(r>0).
\tag{1.4}
\]

### Proof

The mixed derivative and boundary values are
\[
{\partial^2F\over\partial a\partial b}={1\over1-a-b},
\qquad F(a,0)=F(0,b)=0.
\]
Hence
\[
F(a,b)=\int_0^a\int_0^b{dt\,ds\over1-s-t}.
\tag{1.5}
\]
For `a+b<1`, if `U,V` are independent uniform random variables on `[0,1]`, then
\[
{F(a,b)\over ab}
=\mathbb E{1\over1-aU-bV}.
\tag{1.6}
\]
Fix `r<1` and write
\[
G_r(a):=
\mathbb E{1\over1-aU-(r-a)V},
\qquad 0\le a\le r.
\]
It is symmetric under `a -> r-a`. Differentiating under the integral gives
\[
G_r''(a)
=\mathbb E\left[
{2(U-V)^2\over(1-aU-(r-a)V)^3}
\right]\ge0.
\tag{1.7}
\]
Thus the symmetric convex function `G_r` is minimized at `a=r/2`. Substituting `a=b=r/2` into (1.1) gives exactly (1.2)--(1.3). The endpoint `r=1` follows by continuity.

At the minimizer, (1.6) gives
\[
\phi(r)=
\mathbb E{1\over1-(r/2)(U+V)}.
\tag{1.8}
\]
The integrand is pointwise increasing in `r` and is strictly larger than `1` on a set of positive measure whenever `r>0`. This proves (1.4). QED.

The key point is that the old estimate (0.1) discarded the *fixed-sum geometry* of the mutually exclusive block-spectrum events. The new factor `phi(a+b)` is universal and strictly improves it at every interior MUX bias.

## 2. Apply the theorem to the terminal physical MUX data block

For the MUX data block,
\[
a=V_0(1-t),\qquad b=V_1t,\qquad
r=V_0(1-t)+V_1t.
\]
Since the exact block credit contains `TC(K)` plus two additional nonnegative terms,
\[
\mathcal C_D\ge{F(a,b)\over\ln2}.
\]
Combining this with Theorem 1.1 and
\[
W_M=t(1-t){V_0+V_1\over4}
\]
gives
\[
\boxed{
{\mathcal C_D\over W_M}
\ge
{4V_0V_1\over\ln2\,(V_0+V_1)}
\,\phi\!\left(V_0(1-t)+V_1t\right).
}
\tag{2.1}
\]
Because `phi(r)>1` for every interior MUX bias, (2.1) is a strict pointwise strengthening of the previous terminal-block estimate.

Let
\[
\bar c_D(t,q_0,q_1)
:=-{\mathcal R_{\Gamma_0,D}\over W_M}
\]
be the existing credit-free data-block margin request. The actual owner-requested gate margin is
\[
c_M
=-{D_{\Gamma_0}(M)\over W_M}
=\bar c_D-{\mathcal C_D\over W_M}.
\]
Therefore
\[
\boxed{
 c_M(t,q_0,q_1)
\le
\bar c_D(t,q_0,q_1)
-
{4V_0V_1\over\ln2\,(V_0+V_1)}
\phi\!\left(V_0(1-t)+V_1t\right).
}
\tag{2.2}
\]
For the live lift `a^dagger=0.268204856`, every genuine MUX counterexample must consequently satisfy the strictly stronger necessary condition
\[
\boxed{
\bar c_D(t,q_0,q_1)>
0.268204856+
{4V_0V_1\over\ln2\,(V_0+V_1)}
\phi\!\left(V_0(1-t)+V_1t\right).
}
\tag{2.3}
\]

Since `r` is a convex combination of `V0,V1` and `phi` is increasing, a `t`-free corollary is
\[
{\mathcal C_D\over W_M}
\ge
{4V_0V_1\over\ln2\,(V_0+V_1)}
\phi(\min\{V_0,V_1\}).
\tag{2.4}
\]

## 3. Central data square: the old threshold jumps from 2.4322 to 3.9758

Assume
\[
q_0,q_1\in[1/4,3/4].
\]
Then `V0,V1>=3/4`, hence
\[
{V_0V_1\over V_0+V_1}\ge{3\over8},
\qquad
r\ge{3\over4}.
\]
By monotonicity of `phi`,
\[
{\mathcal C_D\over W_M}
\ge {3/2\over\ln2}\phi(3/4).
\]
A direct evaluation gives
\[
\phi(3/4)={16\over9}\ln{8192\over3125},
\]
so
\[
\boxed{
{\mathcal C_D\over W_M}
\ge
{8\over3}\log_2{8192\over3125}
=3.7076254015018353617\ldots .
}
\tag{3.1}
\]
This TC-only central-square bound is sharp at `V0=V1=3/4` and `t=1/2`.

Thus every live-candidate MUX counterexample in the central data square must satisfy
\[
\boxed{
\bar c_D>
0.268204856+{8\over3}\log_2{8192\over3125}
=3.9758302575018353617\ldots .
}
\tag{3.2}
\]
The preceding data-block theorem only forced
\[
\bar c_D>2.432247417333445\ldots .
\]
So the realizable terminal selector now removes a substantially larger portion of the residual without touching the source potential.

For a compact integer sign check, the weaker statement `(8/3)log2(8192/3125)>3.7` is equivalent to
\[
2^{929}>5^{400},
\]
which holds exactly.

## 4. Exact source-to-next-arrow use of fleet01/B18 curvature refund

The source-exact fleet01/B18 physical-restriction inequality is
\[
\Delta_A\mathcal F
\le
B_A-
\sum_{j\notin A}\mathfrak j'(p_j)c_j(A),
\tag{4.1}
\]
and the folded influence currency has the exact physical block drift
\[
\boxed{
D_A=\mathcal J(f)-\mathbb E\mathcal J(f_{A=z})=I_A+C_A.
}
\tag{4.2}
\]
Its essential source-to-next-arrow lesson is that the nonmodular information/crossing refund generated by an actual restriction must be retained rather than erased in a blind induction.

The all-gate terminal data-block cocycle is the same structural mechanism in the current MUX coordinates: `C_D=H(Z|S)+I(S;K)+TC(K)` is an exact nonmodular refund created by revealing the original physical block `{D0,D1}`. The old estimate retained only `TC(K)>=ab/ln2`; Theorem 1.1 spends more of that already-generated credit without reusing it. The next arrow is therefore source-specific but narrow: bound the actual h96 remainder `bar c_D` against (2.3), intersecting it with the existing address-selector and deterministic-boundary certificates. On the central square the target is now the explicit scalar barrier (3.2).

No prescribed coordinate is asserted to pay for its own Shannon erasure. The known addressing obstruction is untouched. The selector is an actual original-coordinate block and terminates in constants/literals, so there is no hidden recoding or child deficit. Equation (4.2) remains the only folded-drift identity used.

## 5. Fresh peer state and remaining obligation

The fresh fleet03/B14 knot-jump theorem (`20260922T084937Z-mux-knot-jump-selector`) gives the complementary physical **address-bit** route: it resolves arbitrary h96 source-knot crossings into a signed downward-jump budget and shows upward slope jumps are favorable. The present theorem is deliberately different: it sharpens the terminal **data-block** information bank and does not depend on any source-cell geometry.

The two routes now leave a precise finite/source-defined residual: a negative MUX point must survive the boundary collars, the address-selector/knot budget, and the strengthened pointwise data-block inequality (2.3). A direct h96 segment scan against this combined residual is the next decisive calculation. Even complete MUX closure would still leave arbitrary composition-prime gates, so full FEI remains open.

## 6. Verification and provenance

`CHECK_TC_SCHUR.py` independently regression-tested 20,000 deterministic fixed-sum `(a,b)` cases and 20,000 deterministic MUX `(V0,V1,t)` cases with high-precision Decimal arithmetic. It also checks the exact integer certificate `2^929>5^400`. The minimum sampled gaps were positive. These tests are diagnostic only; Theorem 1.1 and its MUX corollaries are analytic.

- checker SHA-256: `26eab3040edcc59023198a36ea9cb4616b9213da63c9b26b94f3515fdc5ff562`
- captured output SHA-256: `d7dbf56b4dc9661e10eff376d573fda67843bdd42a6ad36b7586ba6faef8a8c4`
- source h96 candidate remains the committed `cert_vi_h96k40` object used by the inherited MUX branch; this theorem does not regenerate or alter it.

No scheduler mutation, email/Drive action, workflow dispatch, paid/remote compute, benchmark-gold access, permission change, or unrelated private-data access was used.
