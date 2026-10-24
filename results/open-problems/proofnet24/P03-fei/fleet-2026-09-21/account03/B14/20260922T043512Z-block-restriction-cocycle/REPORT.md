# B14 — exact physical-block restriction cocycle and a no-geometry-loss block for B0

**Classification:** `ESSENTIAL_STEP_APPLIED / EXACT_BLOCK_COCYCLE_AND_B0_NO_GEOMETRY_LOSS`.  
**Full uniform-cube FEI:** **OPEN / NOT PROVED.**  
**Execution:** `WITHOUT_VERIFIED_BRAIN`; authenticated repository sources were used directly, but no authenticated installed-brain retrieval/context entered the mathematics.

## 0. Candidate version, live target, and what changed

The live owner target is the all-gate defect

\[
D_\Gamma(G;p)=
\sum_i\frac{\operatorname{It}_i(G;p)}{V_{p_i}}
\bigl(\Gamma(p_i)+h_2(V_{p_i})\bigr)
-\Gamma(p_{\rm out})-\widetilde H_G(p),
\qquad V_u=4u(1-u),
\tag{0.1}
\]

and the associated quadratic-lift margin

\[
c_G(p)=-\frac{D_{\Gamma_0}(G;p)}{W_G(p)},
\qquad
W_G(p)=\frac{I(G;p)}4-p_{\rm out}(1-p_{\rm out})\ge0.
\tag{0.2}
\]

The operational extremality statement consistent with the owner's explicit falsification test is

\[
\sup_{G,p}c_G(p)
\stackrel{?}{=}
\sup_{a,b}c_{\rm AND}(a,b).
\tag{0.3}
\]

A proof of (0.3) for the read-once fixed-point potential would prove the intended gate-extremality route to FEI; a Boolean gate/bias with larger margin would refute that route. This remains open.

The exact candidate version attacked here is **`GATE-EXTREMALITY-BLOCK-v1`**:
replace a lossy one-coordinate split by a realizable *physical block* restriction, keeping every information credit and the exact quadratic currency, and apply it to the same four-bit prime hard case

\[
B_0^{-1}(1)=\{0,1,2,3,4,5,8,10\}\subset\{0,1\}^4.
\tag{0.4}
\]

**Prior missing implication.** The preceding B14 run proved that one of the two middle coordinates of `B0` captures at least half of the parent quadratic currency, but then still had to prove a selected one-coordinate gluing inequality while carrying nontrivial binary-child slack.

**New proved inference.** There is a two-coordinate *physical* block restriction of `B0` whose four children are constants or literals. Consequently it captures **100 percent** of the parent quadratic currency at every product bias, and the parent gate margin is exactly one block-local gluing margin. No affine coordinate change is used or charged.

This does **not** prove (0.3): the remaining block-local margin inequality is still universal in four product biases. It does remove the geometry-loss/child-slack issue for this source-exact prime gate.

## 1. Named compatible peer theorem consumed

This run consumes the completed other-account theorem

`account04/B17/20260922T031352Z-biased-restriction-margin-cocycle/REPORT.md`,
report blob `d32321447c5f30282f243d9a2907ec719d483c92`.

That report proves for a single physical pivot the exact biased restriction entropy/defect cocycle, retaining the branch/KL and vertical-overlap credits, and the exact quadratic currency

\[
\omega_j=t(1-t)\bigl(\delta_j-(r_1-r_0)^2\bigr)\ge0.
\tag{1.1}
\]

It also proves the one-coordinate weighted-average margin theorem. The block theorem below is a genuine extension of that exact identity, not a credit-free surrogate.

I also use the compatible completed formula from
`account01/B12/20260922T0342Z-b0-two-overlap-shannon/REPORT.md`,
report blob `077fb66fc99525d525139ab059409170a87a49b3`, which confirms that the same `B0` middle restrictions have read-once children and gives the exact four-scalar one-coordinate Shannon increment. The block calculation below replaces the residual child bookkeeping by an exact four-branch identity.

## 2. General exact physical-block entropy cocycle

Let `G:{0,1}^n->{0,1}` and let `f=(-1)^G`. Fix a nonempty physical coordinate block `T` and let

\[
Z=X_T,
\tag{2.1}
\]

with its original product bias. For each branch `z`, expand the restricted function `f_z` in the biased orthonormal Fourier basis on `T^c`:

\[
a_z(S)=\widehat{f_z}(S),
\qquad
P_z(S)=a_z(S)^2.
\tag{2.2}
\]

Thus every `P_z` is an actual spectral probability law. Put

\[
M(S)=\mathbb E_ZP_Z(S).
\tag{2.3}
\]

For each fixed outside support `S`, the vector `z\mapsto a_z(S)` is transformed by the tensor biased Walsh transform on `T`. Write the resulting parent coefficient as

\[
b_K(S)=\widehat f(S\cup K),\qquad K\subseteq T.
\tag{2.4}
\]

Orthogonality gives

\[
\sum_{K\subseteq T} b_K(S)^2=M(S).
\tag{2.5}
\]

Hence the parent spectral law can be viewed as a joint law `(S,K)` with

\[
\Pr(S=s,K=k)=b_k(s)^2.
\tag{2.6}
\]

The marginal of `S` is `M`. The marginal inclusion probability of a block coordinate is exactly its biased spectral influence:

\[
\Pr(i\in K)=\operatorname{It}_i(G;p),\qquad i\in T.
\tag{2.7}
\]

Now

\[
H(S)=\mathbb E_Z H(P_Z)+I(Z;S)
=\mathbb E_Z\widetilde H_{G_z}+H(Z)-H(Z\mid S),
\tag{2.8}
\]

while

\[
H(K\mid S)=H(K)-I(S;K).
\tag{2.9}
\]

Because the physical block bits are independent,

\[
H(Z)=\sum_{i\in T}h_2(p_i).
\tag{2.10}
\]

Define the total correlation of the block-spectrum subset `K` by

\[
\operatorname{TC}(K)
:=\sum_{i\in T}h_2(\operatorname{It}_i)-H(K)\ge0.
\tag{2.11}
\]

Combining (2.8)--(2.11) with `\widetilde H_G=H(S,K)` proves the exact identity

\[
\boxed{
\widetilde H_G
=
\mathbb E_Z\widetilde H_{G_z}
+\sum_{i\in T}\bigl[h_2(p_i)+h_2(\operatorname{It}_i)\bigr]
-\mathcal C_T,
}
\tag{2.12}
\]

where

\[
\boxed{
\mathcal C_T
=H(Z\mid S)+I(S;K)+\operatorname{TC}(K)\ge0.
}
\tag{2.13}
\]

For `|T|=1`, `TC(K)=0`, and (2.12)--(2.13) reduce exactly to the account04/B17 one-coordinate cocycle. The new term `TC(K)` is forced by simultaneous restriction: it measures dependence among the block Fourier-layer bits and must not be dropped.

## 3. Exact block defect cocycle

For every outside coordinate `i\notin T`, physical sensitivity averages over the block branches:

\[
\operatorname{It}_i(G;p)
=\mathbb E_Z\operatorname{It}_i(G_Z;p_{T^c}).
\tag{3.1}
\]

Substitute (2.12) and (3.1) into (0.1). This gives

\[
\boxed{
D_\Gamma(G;p)
=
\mathbb E_ZD_\Gamma(G_Z;p_{T^c})
+\mathcal R_{\Gamma,T}+\mathcal C_T,
}
\tag{3.2}
\]

with the source-exact block remainder

\[
\boxed{
\begin{aligned}
\mathcal R_{\Gamma,T}:={}&
\mathbb E_Z\Gamma(r_Z)-\Gamma(r)\\
&+\sum_{i\in T}
\left[
\frac{\operatorname{It}_i}{V_{p_i}}
\bigl(\Gamma(p_i)+h_2(V_{p_i})\bigr)
-h_2(p_i)-h_2(\operatorname{It}_i)
\right].
\end{aligned}}
\tag{3.3}
\]

Here `r_Z=Pr(G_Z=1)` and `r=E r_Z`. No probability-law relaxation or affine coordinate change is used.

## 4. Quadratic lift and the exact block currency

Let

\[
\Gamma_c(u)=\Gamma_0(u)+c\,u(1-u).
\tag{4.1}
\]

The local quadratic change in (3.3) is

\[
\boxed{
\Omega_T
:=\frac14\sum_{i\in T}\operatorname{It}_i
-\operatorname{Var}_Z(r_Z).
}
\tag{4.2}
\]

Indeed `p_i(1-p_i)/V_{p_i}=1/4`, and

\[
\mathbb E r_Z(1-r_Z)-r(1-r)=-\operatorname{Var}(r_Z).
\]

Moreover

\[
\boxed{
W_G=\mathbb E_ZW_{G_Z}+\Omega_T.
}
\tag{4.3}
\]

The currency is always nonnegative. To see this, put `m(Z)=E[f\mid Z]=1-2r_Z`. The Fourier expansion of `m` contains exactly the parent coefficients with support contained in `T`, so

\[
4\operatorname{Var}(r_Z)
=\operatorname{Var}(m(Z))
=\sum_{\emptyset\ne A\subseteq T}\widehat f(A)^2
\le\sum_{i\in T}\operatorname{It}_i.
\tag{4.4}
\]

Thus `Omega_T>=0` by a source-exact Fourier/Poincare calculation.

Equations (3.2) and (4.3) show that whenever `Omega_T>0`, the block-local required correction

\[
c_T^{\rm loc}
:=-\frac{\mathcal R_{\Gamma_0,T}+\mathcal C_T}{\Omega_T}
\tag{4.5}
\]

is the correct margin currency for this restriction. Iterating single-coordinate restrictions inside `T` shows that (4.5) is itself the `Omega`-weighted average of the account04/B17 one-coordinate local margins in any physical ordering of `T`; the block identity packages all intermediate child slack and all information credits without reuse.

## 5. Same hard case B0: a two-bit physical block captures 100 percent of W

Use the coordinate convention of the preceding B14 report. Directly from the truth table,

\[
G\vert_{x_2=0}=1-x_0x_3,
\qquad
G\vert_{x_2=1}=(1-x_1)(1-x_3).
\tag{5.1}
\]

Now restrict the *physical block*

\[
T=\{x_2,x_3\}.
\tag{5.2}
\]

The four branches are exactly

\[
\boxed{
G_{00}=1,
\quad G_{01}=1-x_0,
\quad G_{10}=1-x_1,
\quad G_{11}=0.
}
\tag{5.3}
\]

Thus every child is a constant or a literal. For every symmetric boundary-normalized potential,

\[
D_\Gamma(G_z)=0,
\qquad W_{G_z}=0
\tag{5.4}
\]

for all four branches and for every interior product bias on the two surviving leaf variables. Consequently (3.2) and (4.3) collapse to

\[
\boxed{
D_\Gamma(B_0;p)=\mathcal R_{\Gamma,T}(p)+\mathcal C_T(p),
}
\tag{5.5}
\]

and

\[
\boxed{
\Omega_T(p)=W_{B_0}(p).
}
\tag{5.6}
\]

This is the exact no-geometry-loss selector promised by the B14 assignment: the old single-coordinate policy guaranteed only `max omega_j >= W/2`; the two-bit block captures **all** of `W`, with zero affine-coordinate-change charge and no child reserve left unpaid.

Whenever `W_{B_0}>0`, its global gate margin is therefore exactly

\[
\boxed{
 c_{B_0}(p)
 =-\frac{\mathcal R_{\Gamma_0,T}(p)+\mathcal C_T(p)}{W_{B_0}(p)}.
}
\tag{5.7}
\]

So the source-exact four-bit prime is not merely bounded by a restriction-tree average: it is represented by one realizable two-bit block-local gluing margin.

## 6. Decisive uniform calculation and a dead stronger route

At uniform bias on all four inputs,

\[
W_{B_0}=\Omega_T=\frac18.
\tag{6.1}
\]

The joint source calculation gives

\[
H(Z\mid S)=\frac12.
\tag{6.2}
\]

For the parent block-spectrum variable `K`, the marginal law is

\[
\Pr(K=\emptyset,K=\{2\},K=\{3\},K=\{2,3\})
=\left(\frac18,\frac38,\frac38,\frac18\right),
\tag{6.3}
\]

while the exact conditional entropy is

\[
H(K\mid S)=\frac32.
\tag{6.4}
\]

Because each central spectral inclusion has probability `1/2`,

\[
I(S;K)+\operatorname{TC}(K)
=2-H(K\mid S)=\frac12.
\tag{6.5}
\]

Hence

\[
\boxed{\mathcal C_T=1.}
\tag{6.6}
\]

For the read-once base potential with `C_0=Gamma_RO(1/2)=6.4548`, the block remainder is

\[
\boxed{
\mathcal R_{\Gamma_{\rm RO},T}=\frac{C_0}{2}-4=-0.7726.
}
\tag{6.7}
\]

Therefore the base parent defect is `0.2274` and the corresponding margin is

\[
\boxed{c_{B_0}(1/2,1/2,1/2,1/2)=-1.8192.}
\tag{6.8}
\]

For the inherited full-FEI scalar lift

\[
a_*=0.2682048,
\tag{6.9}
\]

the quadratic payment is `a_* W=0.0335256`, so

\[
\boxed{
\mathcal R_{\Gamma_*,T}=-0.7390744,
\qquad
D_{\Gamma_*}(B_0)=0.2609256.
}
\tag{6.10}
\]

This gives a genuine Boolean refutation of a tempting stronger block rule:

> **REFUTED:** demand the credit-free local remainder `R_{Gamma_*,T}>=0`.

It already fails by `0.7390744` at the uniform `B0` gate. The exact information credit `C_T=1` is not optional; it reverses the sign and yields the positive parent defect `0.2609256`.

## 7. Verification

`CHECKER.py` independently reconstructs `B0` from its truth table, computes biased Walsh coefficients, and tests (2.12) and (4.3) on 5,000 deterministic random interior bias vectors. It also verifies that all four `T={2,3}` children have zero Poincare currency and reproduces the uniform arithmetic.

Observed regression output:

```
random_points=5000
max_entropy_identity_error=4.441e-16
max_currency_identity_error=1.943e-16
max_abs_child_W=2.220e-16
min_observed_Omega=0.00212533940831
uniform_W=1/8
uniform_C_block=1
uniform_R_base=-0.7726000
uniform_R_stable=-0.7390744
uniform_D_stable=0.2609256
PASS
```

Executed checker SHA-256:
`cd74d9ea96e8ac867ea19eccd459bbe7f61d056fc612c2112eb7d0cde58eaeda`.

Captured-output SHA-256:
`b9283abd04c6039953f074460f11fbed422500920983917c86ef3134a1490625`.

The numerical run is a regression check only; the universal block cocycle and nonnegativity of `Omega_T` are proved algebraically above.

## 8. Exact remaining implication and handoff

**New remaining implication for this hard prime.** With `T={x_2,x_3}`, prove

\[
\boxed{
 c_T^{\rm loc}(B_0;p)
 \le c_{\rm AND}^{\rm global}
 \quad\text{for every }p\in(0,1)^4,
}
\tag{8.1}
\]

where the left side is the exact source-realizable expression (4.5), or find a product-bias vector violating (8.1). This is now precisely the owner's gate-extremality/falsification target on `B0`; there is no residual geometry-loss factor and no hidden child deficit.

The next useful proof move is not another coordinate sweep. It is to exploit the special four-branch structure (5.3) in the exact credit

\[
\mathcal C_T=H(Z\mid S)+I(S;K)+TC(K)
\tag{8.2}
\]

to compare the block margin directly with the binary AND extremal margin. A violating bias would be a genuine Boolean counterexample to the proposed extremality statement for this prime class.

**next_recipient:** `account01/B18` (A lead / gate-extremality integrator).  
**consumed_peer_artifact:** `account04/B17/20260922T031352Z-biased-restriction-margin-cocycle/REPORT.md`, blob `d32321447c5f30282f243d9a2907ec719d483c92`.  
**applied_to_claim:** `GATE-EXTREMALITY-BLOCK-v1` on `B0`.  
**replacement_obligation:** prove or refute (8.1) with the exact block credit retained.  
**implication_to_full_FEI:** closing `B0` is only one source-exact prime case. Full FEI still requires the universal gate-extremality theorem (or another universal Gamma satisfying (G)) for every finite arity and every product bias.
