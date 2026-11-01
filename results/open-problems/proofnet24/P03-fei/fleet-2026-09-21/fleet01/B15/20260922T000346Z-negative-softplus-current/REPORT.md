# B15 — exact negative-softplus correction in the live Shannon residual

**Run:** `20260922T000346Z-b15-fei-negentropy-v11`  
**Directive:** `FEI-PROOF-EXECUTION-20260921T230620Z`, Campaign B  
**Assignment:** identify and quantitatively use the negative entropy term that offsets the candidate's largest loss.  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.  
**Outcome classification:** **AUXILIARY_ONLY**.  
**Full unrestricted FEI:** **OPEN / NOT PROVED**.

## 0. Exact candidate version and end-to-end target

No post-reset Campaign-B lead report from `fleet03/B18` was available in the completed builder snapshots read for this run. Per the execution-reset fallback rule, I bind to the smallest explicit common Shannon candidate already completed after the reset:

`fleet03/B15/20260921T232637Z-erasure-packet-kl-lattice/REPORT.md`

as read from scientific commit

`a91fd4e1f325982284c92769c8ca5db94ce041fc`.

That report proves, for each physical coordinate `i`, with

\[
x_T=p_T,\qquad y_T=p_{T+i},\qquad m_T=x_T+y_T,
\qquad \alpha_i=\sum_Ty_T=\operatorname{Inf}_i(f),
\]

and probability laws

\[
P_i(T)=y_T/\alpha_i,\qquad M_i(T)=m_T,
\]

the exact identity

\[
E_i:=\sum_Ty_T\log_2\frac{m_T}{y_T}
=\alpha_i\left[\log_2\frac1{\alpha_i}-D_2(P_i\Vert M_i)\right]. \tag{0.1}
\]

Writing `E=\sum_iE_i`, the inherited erasure reduction proves

\[
E\le B\le E+\frac1{\ln2}I, \tag{0.2}
\]

and a dimension-free bound `E<=C_0 I` yields

\[
H(f)\le\left(C_0+\frac3{\ln2}\right)I(f). \tag{0.3}
\]

Thus the old first missing universal implication is equivalently

\[
\sum_i\alpha_iD_2(P_i\Vert M_i)
\ge
\sum_i\alpha_i\log_2\frac1{\alpha_i}-C_0I(f). \tag{0.4}
\]

The purpose of this run is to use the negative KL term in (0.1), not drop it.

A second named completed dependency actually consumed is

`fleet01/B12/20260921T231256Z-conditional-count-code/REPORT.md`,

which independently shows that the live Shannon code has a literal negative mutual-information/KL rebate rather than a separate positive label cost. The calculation below is the exact edgewise form of that same principle for (0.1).

## 1. Exact negative-softplus identity

Let

\[
u_T=\widehat f(T),\qquad v_T=\widehat f(T+i),
\qquad x_T=u_T^2,\quad y_T=v_T^2.
\]

For `y_T>0` put

\[
z_T:=\frac{x_T}{y_T}.
\]

Retain the already-defined one-sided magnitude-gradient cost

\[
G_i:=\sum_{T:y_T>0}y_T\log_2^+\frac{|u_T|}{|v_T|}
=\frac12\sum_{T:y_T>0}y_T[\log_2z_T]_+. \tag{1.1}
\]

Define the **softplus correction**

\[
c(z):=1+[\log_2z]_+-\log_2(1+z). \tag{1.2}
\]

A useful symmetric form is

\[
\boxed{c(z)=1-\log_2\!\left(1+\min\{z,z^{-1}\}\right)} \tag{1.3}
\]

for `z>0`, with the continuous conventions `c(0)=c(+\infty)=1`. Hence

\[
0\le c(z)\le1,
\]

with equality `c(z)=0` exactly at `z=1`.

Set

\[
\Phi_i:=\sum_{T:y_T>0}y_Tc(z_T),\qquad \Phi:=\sum_i\Phi_i. \tag{1.4}
\]

Then the scalar identity

\[
\log_2(1+z)=1+[\log_2z]_+-c(z)
\]

gives, without an inequality,

\[
\boxed{E_i=\alpha_i+2G_i-\Phi_i}. \tag{1.5}
\]

Summing,

\[
\boxed{E=I+2G-\Phi},\qquad G:=\sum_iG_i. \tag{1.6}
\]

This is exactly where the earlier positive magnitude-flow bound loses information: replacing `log(1+z)` by `1+[log z]_+` discards the entire nonnegative `Phi` bank.

## 2. The KL credit and the softplus correction are the same ledger

Combining (0.1) and (1.5) yields, coordinate by coordinate,

\[
\boxed{
\alpha_iD_2(P_i\Vert M_i)
=
\alpha_i\log_2\frac1{\alpha_i}
-\alpha_i-2G_i+\Phi_i.
} \tag{2.1}
\]

Thus the negative KL term is not an abstract extra rebate. It is the exact amount that converts raw address entropy into the signed edge current below.

Define

\[
N_i:=G_i-\frac12\Phi_i,
\qquad N:=\sum_iN_i. \tag{2.2}
\]

Then

\[
\boxed{N=\frac{E-I}{2}}. \tag{2.3}
\]

More explicitly, each physical Fourier edge contributes

\[
\boxed{
n(z_T)y_T
:=\frac{y_T}{2}\log_2\frac{1+z_T}{2}.
} \tag{2.4}
\]

This is a **signed** current. Edges with `x_T<y_T` contribute negatively, equal-magnitude edges contribute zero, and only `x_T>y_T` contribute positively. No absolute value or positive-parting of the negative entropy credit occurs.

The previous open magnitude-flow target

\[
G\le\frac32I \tag{2.5}
\]

would imply `N<=3I/2` because `Phi>=0`. The new candidate is therefore strictly weaker:

\[
\boxed{N\le\frac32I}. \tag{2.6}
\]

Importantly, (2.6) is not introduced as a second unrelated residual. By (2.3) it is **exactly** the inherited common Shannon implication (0.4) with `C_0=4`.

If (2.6) holds universally, then

\[
E=I+2N\le4I,
\]
so (0.2) gives

\[
B\le\left(4+\frac1{\ln2}\right)I,
\]

and the already-proved erasure restriction induction gives

\[
\boxed{
H(f)\le\left(4+\frac3{\ln2}\right)I(f)
=8.32808512266689\ldots\,I(f).
} \tag{2.7}
\]

Constants and characters are covered by the inherited erasure proof; for `I=0`, `f` is constant and `H=0`.

Equation (2.6) remains **OPEN**. No full FEI proof is claimed.

## 3. Direct attempt on the new first missing inference: reduce it to a true large-ratio tail

The signed kernel (2.4) lets us remove the entire moderate-ratio sector at a fixed influence price.

If `z<=3`, then

\[
\frac12\log_2\frac{1+z}{2}\le\frac12.
\]

If `z>3`, then exactly

\[
\frac12\log_2\frac{1+z}{2}
=
\frac12+\frac12\log_2\frac{1+z}{4}.
\]

Therefore

\[
\boxed{
N
\le
\frac12 I
+
\frac12 T_3,
} \tag{3.1}
\]

where the only unpaid tail is

\[
\boxed{
T_3:=
\sum_{i,T:\,x_T>3y_T}
 y_T\log_2\frac{x_T+y_T}{4y_T}.
} \tag{3.2}
\]

Consequently the single concrete implication

\[
\boxed{T_3\le2I} \tag{3.3}
\]

would prove (2.6), hence the full FEI bound (2.7).

This is a genuine narrowing relative to (2.5):

* all edges with squared-magnitude ratio at most `3` are already paid;
* all reverse edges `x<y` retain their negative contribution rather than being discarded;
* the only remaining positive debt is on edges where the lower-level coefficient is more than `sqrt(3)` times the upper-level coefficient.

I do **not** prove (3.3) here. It is the new first essential missing inference after applying the negative entropy term.

## 4. Quantitative meaning of the correction

For any `R>=1`, if

\[
\max\{|u_T|/|v_T|,|v_T|/|u_T|\}\ge R,
\]
then `min(z,z^{-1})<=R^{-2}` and (1.3) gives

\[
\boxed{
c(z_T)\ge1-\log_2(1+R^{-2}).} \tag{4.1}
\]

Thus on very unequal-magnitude edges the negative correction refunds asymptotically one full `y_T` bit of the `+I` softplus loss. In particular, the correction is strongest exactly where the old positive-current approximation is most asymmetric.

The refund cannot by itself pay an arbitrarily large logarithmic ratio: `c<=1`. This explains why the surviving task is the logarithmic tail (3.2), not another attempt to bound `Phi` alone.

## 5. Required obstruction tests

### 5.1 Tensor products — PASSES the necessary scale test

The inherited erasure report proves that `E` is additive under disjoint Boolean products; `I` is additive as well. Hence by (2.3)

\[
N(f\otimes g)=N(f)+N(g). \tag{5.1}
\]

So the negative credit does not disappear under tensor powers. This directly addresses the earlier tensor-saturation obstruction to sublinear or one-shot refunds.

### 5.2 Recursive majority — the global one-level code obstruction does not kill this current

The completed `fleet02/B17/20260921T231240Z-recursive-majority-hierarchical-code/REPORT.md` proves that recursive ternary majority destroys every finite **one-level global coordinate-code** constant while its true `H/I` remains below `4`; it therefore forces scale-local cancellation. The signed current here is not that one-level envelope. Moreover `N<=G`, and the previously proved balanced self-composition formula for `G/I` has a convergent correction tail for every fixed balanced non-dictator seed. Thus recursive majority does not create the same divergence in this net current. This is not a proof of (2.6).

### 5.3 Rare tribes — PASSES strongly

The earlier exact rare-tribes calculation gives `G/I -> 0` in the hard rare-width limit. Since `Phi>=0`,

\[
\frac NI\le\frac GI\to0. \tag{5.2}
\]

So the family that makes the coarse depth/isoperimetric surrogates diverge does not threaten (2.6).

### 5.4 Sparse defect / bent-one-flip — fixed-coordinate payment still FAILS

The established bent-one-flip selector family has a physical coordinate with

\[
G_i/\alpha_i\to\infty.
\]

Because `0<=Phi_i<=alpha_i`,

\[
\frac{N_i}{\alpha_i}
\ge
\frac{G_i}{\alpha_i}-\frac12\to\infty. \tag{5.3}
\]

Hence the negative correction does **not** resurrect a fixed-coordinate inequality. Any proof of (2.6) must be genuinely cross-coordinate/global.

### 5.5 Addressing obstruction — not bypassed by a scalar relaxation

The existing addressing counterfamily rules out broad fixed-coordinate positive-power/superlinear-log edge majorants. The present target does not assume one: it keeps the exact signed logarithmic current (2.4). Therefore the next proof cannot replace `T_3` by one of those already-refuted coordinatewise envelopes.

### 5.6 Biased product-law limit — Booleanity is still essential

For an arbitrary independent Bernoulli spectral law with inclusion probability `theta`,

\[
E_i=\theta\log_2(1/\theta),\qquad I_i=\theta,
\]
so

\[
\frac NI
=
\frac12\left(\log_2\frac1\theta-1\right)\to\infty
\quad(\theta\downarrow0). \tag{5.4}
\]

Thus (2.6) is false for arbitrary nonnegative spectral distributions. A proof must use the signed Boolean convolution constraints; relaxing to an arbitrary probability law cannot work.

### 5.7 Current strongest recursive Numaro stress family — no refutation

The prior exact/certified B15 work bounds the corresponding positive aggregate flow `G/I` below `1.5` on the recursive Numaro closure (with the certified upper frontier below `1.499392`). Since `N<=G`, that family cannot refute (2.6). The negative correction only increases the margin.

## 6. Old implication, new inference, and remaining obligation

**Old missing implication:** prove the aggregate KL lower bound (0.4), equivalently `E<=C_0 I`, with one finite dimension-independent constant.

**New proved inference:** the exact negative KL rebate converts the live erasure residual into

\[
E=I+2G-\Phi=I+2N,
\]
where `Phi` is the explicit nonnegative softplus correction (1.4), and the `C_0=4` case reduces further to the genuine large-ratio tail inequality `T_3<=2I`.

**What this eliminates:** any proof that pays `G` while discarding `Phi` is unnecessarily stronger; any fixed-coordinate proof is still impossible; any arbitrary-probability relaxation is false.

**First remaining essential implication:** prove (3.3) for genuine Boolean spectra using the signed convolution constraints, or construct a genuine Boolean counterexample with `T_3>2I` (equivalently `N>3I/2`).

**Replacement obligations if (3.3) fails:** preserve the exact signed current and identify the smallest Boolean family causing the tail excess; do not return to the already-refuted positive-only magnitude flow or one-level global code.

**Classification:** `AUXILIARY_ONLY`. This run applies the requested negative entropy term exactly and strictly weakens/localizes the live candidate, but it does not prove the universal tail bound and therefore does not qualify as `ESSENTIAL_STEP_APPLIED` under the execution-reset admission rule.
