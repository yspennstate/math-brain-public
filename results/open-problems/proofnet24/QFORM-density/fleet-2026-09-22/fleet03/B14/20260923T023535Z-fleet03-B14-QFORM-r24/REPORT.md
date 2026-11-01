# fleet03 / B14 / QFORM r24

## Status

**Run id:** `20260923T023535Z-fleet03-B14-QFORM-r24`

**Target:** the universal bounded-density conjecture for quadratic forms under independent one-dimensional density caps.

**Scope of this report:** translations/localization only, with one concrete application of the completed fleet04/B14 kernel-leakage-core estimate.

**Full QFORM status:** OPEN / NOT PROVED.

**Continuity:** not proved for the full target here.

**Brain transport status:** `WITHOUT_VERIFIED_BRAIN`. Repository controls were read and used, but no authenticated native receiver-memory ingestion was observed.

---

## 1. Compact conditional end-to-end plan attempted first

The current difficult routes repeatedly condition after a sum/difference or bank transform. The conditional one-dimensional laws need no longer have cap one; their caps can depend on the conditioning value and can become arbitrarily large on small fibers. A natural hope is:

1. localize each conditional law at its actual cap;
2. rescale the completed fleet04/B14 kernel-leakage theorem to that cap;
3. average the resulting fiberwise estimate.

This report proves the exact variable-cap localization step in (1), computes the precise cap exponent in (2), and then proves that (3) can fail arbitrarily badly on compact finite-fragment cap-one inputs. Thus the result both supplies a reusable localization theorem and rules out a tempting but invalid way of inserting it into conjugate-variable conditioning.

---

## 2. Variable-cap extreme localization with zero loss

For a cap vector \(M=(M_1,\dots,M_n)\), \(M_i>0\), let
\[
\mathcal D(M)=\left\{\bigotimes_{i=1}^n f_i(x_i)\,dx_i:\ 0\le f_i\le M_i,\ \int f_i=1\right\}.
\]
Let \(\mathcal F(M)\) consist of product laws whose marginals are
\[
M_i\mathbf 1_{E_i}(x_i)\,dx_i,
\]
where each \(E_i\) is a compact finite union of intervals of total length \(|E_i|=M_i^{-1}\).

### Theorem 2.1 — QFORM-VARIABLE-CAP-CONVEX-LOCALIZATION-v1

Let \(P:\mathbb R^n\to\mathbb R\) be measurable and let \(\Phi\) be any convex, total-variation-lower-semicontinuous extended functional of the output probability law. Then
\[
\boxed{
\sup_{\mu\in\mathcal D(M)}\Phi(P_\#\mu)
=
\sup_{\nu\in\mathcal F(M)}\Phi(P_\#\nu).
}
\]
No support-radius, translation, moment, fragment-count, or fragment-separation term appears.

#### Proof

Put \(D=\operatorname{diag}(M_1,\dots,M_n)\) and set \(Y=DX\). If \(X_i\) has density \(f_i\le M_i\), then \(Y_i\) has density
\[
g_i(y)=M_i^{-1}f_i(y/M_i)\le1.
\]
Hence the map \(X\mapsto Y=DX\) is a bijection between \(\mathcal D(M)\) and the cap-one product class \(\mathcal D(\mathbf 1)\). Define
\[
\widetilde P(y)=P(D^{-1}y).
\]
The completed fleet04/B14 law-level finite-mixture localization theorem, together with convexity and TV lower semicontinuity, gives
\[
\sup_{\rho\in\mathcal D(\mathbf 1)}\Phi(\widetilde P_\#\rho)
=
\sup_{\eta\in\mathcal F(\mathbf 1)}\Phi(\widetilde P_\#\eta).
\]
If \(\eta_i=\mathbf1_{F_i}\,dy\) with \(|F_i|=1\), pulling back under \(D\) gives density \(M_i\mathbf1_{E_i}\) with \(E_i=M_i^{-1}F_i\) and \(|E_i|=1/M_i\). Conversely every such extreme law pushes forward to a cap-one extreme law. This proves the equality. ∎

### Quadratic specialization

For
\[
P_{A,d,c}(x)=x^TAx+d^Tx+c,
\]
the same dilation gives
\[
P_{A,d,c}(D^{-1}y)
=
y^T(D^{-1}AD^{-1})y+(D^{-1}d)^Ty+c.
\]
Therefore every optimal output-law constant for the cap vector \(M\) at \((A,d,c)\) is exactly the corresponding cap-one constant for
\[
\boxed{A_M=D^{-1}AD^{-1},\qquad d_M=D^{-1}d.}
\]
This includes interval-concentration constants and all extended \(L^p\) output-density norms, \(1<p\le\infty\).

Range-compatible translations are preserved by the normalization. Indeed, if \(d=2As\), then
\[
D^{-1}d=2D^{-1}As=2(D^{-1}AD^{-1})(Ds),
\]
so an affine term removable before scaling is removable after scaling with exactly zero cost.

---

## 3. Exact cap-moment formula after a sum/difference transform

The variable-cap theorem is useful only if the random cap created by conditioning can itself be averaged without loss. The next result shows this fails in the strongest possible way on the allowed finite-fragment extreme class.

Let \(X,X'\) be iid with density \(\mathbf1_E\), where \(E\subset\mathbb R\) has Lebesgue measure one. Put
\[
U=X-X',\qquad V=X+X'.
\]
The inverse map is \(X=(V+U)/2\), \(X'=(V-U)/2\), with Jacobian \(1/2\). Hence the joint density is
\[
J(u,v)=\frac12\mathbf1_E\!\left(\frac{v+u}{2}\right)
\mathbf1_E\!\left(\frac{v-u}{2}\right).
\]
Define the overlap function
\[
m(u)=|E\cap(E-u)|.
\]
Then \(m\) is the density of \(U\), and for every \(u\) with \(m(u)>0\),
\[
V\mid U=u
\]
has a density equal to \(1/(2m(u))\) on a set of \(v\)-measure \(2m(u)\). Thus its exact essential-supremum cap is
\[
\boxed{M(u)=\frac1{2m(u)}.}
\]
Consequently, for every \(\alpha>0\),
\[
\mathbb E[M(U)^\alpha]
=2^{-\alpha}\int_{m(u)>0}m(u)^{1-\alpha}\,du,
\]
with the usual value \(+\infty\) if the integral diverges.

### Theorem 3.1 — QFORM-CONDITIONAL-CAP-RENYI-OBSTRUCTION-v1

For every \(\alpha>0\),
\[
\boxed{
\sup_{E\text{ compact finite union},\ |E|=1}
\mathbb E\|f_{V\mid U}\|_\infty^\alpha
=\infty.
}
\]
This remains true when \(f_X=f_{X'}=\mathbf1_E\) are themselves cap-one extreme densities.

#### Explicit finite-fragment witness and exact computation

Fix \(N\ge2\), let \(\ell=1/N\), and set
\[
E_N=\bigcup_{k=1}^N[4^k,4^k+\ell].
\]
Then \(|E_N|=1\). Distinct positive differences \(4^j-4^k\), \(j>k\), are distinct: if
\[
4^j-4^k=4^{j'}-4^{k'},
\]
then comparing the exact powers of \(4\) dividing the two sides first gives \(k=k'\), and then \(j=j'\). Hence all nonzero ordered-difference centers are distinct integers. Since \(\ell\le1/2\), their support intervals of radius \(\ell\) are disjoint up to null endpoints.

For an off-diagonal ordered pair \(j\ne k\), writing
\[
u=(4^j-4^k)+w,\qquad |w|<\ell,
\]
one has exactly
\[
m_N(u)=\ell-|w|.
\]
Near zero, all \(N\) diagonal pairs contribute and
\[
m_N(u)=N(\ell-|u|)=1-N|u|,\qquad |u|<\ell.
\]
Therefore for \(0<\alpha<2\), the off-diagonal contribution is
\[
\begin{aligned}
2^{-\alpha}N(N-1)
\int_{-\ell}^{\ell}(\ell-|w|)^{1-\alpha}\,dw
&=
2^{-\alpha}N(N-1)\frac{2\ell^{2-\alpha}}{2-\alpha}\\
&=
\frac{2^{1-\alpha}}{2-\alpha}
\left(1-\frac1N\right)N^\alpha.
\end{aligned}
\]
The diagonal cluster contributes
\[
\frac{2^{1-\alpha}}{N(2-\alpha)}.
\]
Thus the exact moment is
\[
\boxed{
\mathbb E[M_N(U)^\alpha]
=
\frac{2^{1-\alpha}}{2-\alpha}
\left[
\left(1-\frac1N\right)N^\alpha+\frac1N
\right],
\qquad 0<\alpha<2.
}
\]
In particular,
\[
\boxed{\mathbb E M_N(U)=N-1+\frac1N.}
\]
For \(\alpha\ge2\), every off-diagonal triangular overlap contributes
\[
\int_0^\ell r^{1-\alpha}\,dr=\infty,
\]
so
\[
\boxed{\mathbb E[M_N(U)^\alpha]=\infty,\qquad \alpha\ge2.}
\]
This proves the theorem for every positive \(\alpha\). ∎

### Interpretation

The failure is caused by distant fragments, but not by any pathology excluded by the owner hypotheses: each \(E_N\) is a compact finite union of intervals, the input density is exactly one on a set of total measure one, and no moment or diameter restriction is allowed in the target.

The theorem does **not** say that the quadratic-form output density becomes unbounded. It says that a proof architecture which normalizes conjugate-variable fibers and then pays any positive power of their conditional \(L^\infty\) cap cannot have a universal constant under the stated hypotheses.

---

## 4. Actual application of fleet04/B14 r6 to the obstruction

The completed fleet04/B14 theorem `QFORM-KERNEL-LEAKAGE-CORE-v1` states, in its four-coordinate scope, that a kernel-leakage core \(H\) has residual output density cap
\[
K_H(1)
=
1000(8+\log4)
\frac{\sqrt{s_1(H)s_2(H)}}{\kappa\sqrt{\nu_1\nu_2}},
\]
where \(\nu_1\ge\nu_2>0\) are the two nonzero singular values of the embedded rank-two triple, \(\kappa=|k^Tc|>0\) is the kernel-leakage coupling, and \(s_1(H),s_2(H)\) are the leading singular values of the four-coordinate core.

Suppose now that all four active coordinate densities have a common cap at most \(M\). Set \(Y_i=MX_i\). The transformed variables have cap one and the quadratic matrix becomes \(H/M^2\). Under this common scalar dilation,
\[
s_j(H/M^2)=M^{-2}s_j(H),\qquad
\nu_j(M^{-2}B)=M^{-2}\nu_j(B),\qquad
\kappa(M^{-2}H)=M^{-2}\kappa(H).
\]
Therefore the fleet04/B14 formula scales **exactly quadratically** in the cap:
\[
\boxed{K_H(M)=M^2K_H(1).}
\]
This is an actual inequality, not merely a dimensional heuristic.

Now splice this residual estimate into a physical completed square
\[
Q=a[Z+m(Y)]^2+R(Y),\qquad a\ne0.
\]
If the scalar pivot density has cap \(M_0\), conditioning on \(Y\) gives
\[
p_{a(Z+m)^2}(u)\le M_0|a|^{-1/2}|u|^{-1/2}.
\]
If \(R\) has density cap \(K\), the exact rearrangement estimate
\[
\sup_t\mathbb E|R-t|^{-1/2}\le2\sqrt{2K}
\]
yields
\[
\boxed{
\|p_Q\|_\infty
\le
2\sqrt2\,M_0|a|^{-1/2}\sqrt K.
}
\]
Using \(K=K_H(M)=M^2K_H(1)\),
\[
\boxed{
\|p_Q\|_\infty
\le
274.0261938008101\,
M_0M|a|^{-1/2}
\frac{[s_1(H)s_2(H)]^{1/4}}
{\kappa^{1/2}(\nu_1\nu_2)^{1/4}}.
}
\]
The numerical coefficient is
\[
2\sqrt2\sqrt{1000(8+\log4)}
=274.0261938008101\ldots.
\]

### What happens after conjugate-variable conditioning

For four independent coordinate pairs, condition on the difference vector \(U=(U_1,\dots,U_4)\). The sum coordinates remain conditionally independent, but their caps are random:
\[
M_i(U_i)=\frac1{2m(U_i)}.
\]
A common admissible cap is
\[
M_*(U)=\max_i M_i(U_i).
\]
If the physical pivot is left outside this transformed family so \(M_0=1\), the displayed partner splice pays a factor \(M_*(U)\). Hence its averaged proof constant is at least proportional to
\[
\mathbb E M_*(U)\ge\mathbb E M_1(U_1)=N-1+\frac1N
\]
on the explicit \(E_N\) witness.

If the pivot is also one of the conditioned sum coordinates, then \(M_0\le M_*\) and the same route pays \(M_*^2\). But
\[
\mathbb E M_*^2\ge\mathbb E M_1(U_1)^2=\infty
\]
for every \(N\ge2\).

Thus the variable-cap localization theorem is exact, and the fleet04/B14 kernel-leakage theorem rescales exactly, but **their naive fiberwise composition after conjugate conditioning is not uniform under the owner hypotheses**. The loss is not a defect of localization; it is the positive cap exponent created by normalizing thin overlap fibers.

This quantitatively strengthens the existing correction that conjugate-variable conditional density caps can blow up. It identifies the precise Renyi-type quantity which the naive proof would need to control and shows that quantity diverges or grows polynomially already on legal finite-fragment extremes.

---

## 5. Consequence for the full QFORM strategy

The safe localization order is now sharper:

1. Keep each cap-one extreme set intact.
2. If using independent copies, keep the unnormalized positive-copy / collision expression intact as long as possible.
3. Aggregate over overlap mass **before** converting a fiber to a normalized conditional density and before invoking a theorem with positive cap homogeneity.
4. Physical-coordinate translations and the variable-cap scaling theorem can be applied after an aggregate estimate has been obtained; they cost nothing beyond the explicit homogeneous cap factor already present in that estimate.

In particular, the present result supports the current owner directive to pursue aggregate-before-inversion / ridge-bank mechanisms. It rules out the shortcut “condition on differences, renormalize every thin fiber, apply the four-coordinate leakage theorem fiberwise, then average the resulting caps.”

A useful next target is an **unnormalized overlap-weighted kernel-leakage inequality** in which the factor \(m(u)\) from the conditioning law remains inside the estimate and cancels the inverse overlap produced by the conditional cap. That would be compatible with the exact finite-fragment localization theorem and would avoid the Renyi-spread obstruction proved here.

---

## 6. Quantifier audit

- Inputs remain independent before any optional copy transform.
- Original marginal density cap is exactly the owner cap \(\le1\).
- No Gaussian, log-concave, moment, connected-support, compact-support, or diagonal-basis assumption is introduced in the localization theorem.
- Compact finite fragments appear only as an **exact worst-case reduction**, not as an added assumption.
- The obstruction itself uses legal compact finite-fragment extreme inputs, so allowing unbounded/distant support cannot repair the failed proof route.
- The sum/difference calculation is explicitly not used to claim preservation of cap one; instead it computes the exact random conditional cap and exhibits its blow-up.
- Full bounded density under only \(s_3(A)\ge1\) is **not** claimed.
- Full-target continuity is **not** claimed.
