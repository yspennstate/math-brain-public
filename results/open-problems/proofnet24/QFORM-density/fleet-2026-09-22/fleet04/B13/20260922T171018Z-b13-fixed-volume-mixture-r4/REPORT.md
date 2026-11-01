# QFORM B13 — fixed-volume random-set representation and continuity transfer

**Run:** `20260922T171018Z-b13-fixed-volume-mixture-r4`  
**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Owner control:** revision `2026-09-22.8`  
**Status:** `ESSENTIAL_STEP_APPLIED / TARGET_LEVEL_REDUCTION / FULL_TARGET_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`

## 1. Fixed-volume random-set lemma

Let (f:mathbb R	o[0,1]) be measurable with (int f=1). There is a probability space ((Omega,
u)) and a jointly measurable random set (E_omegasubsetmathbb R) such that
[
|E_omega|=1quad	ext{for }
u	ext{-a.e. }omega,
qquad

u{omega:xin E_omega}=f(x)quad	ext{for a.e. }x.
]
Equivalently,
[
oxed{f(x)=int_Omega mathbf 1_{E_omega}(x),d
u(omega)}
]
almost everywhere, with every extreme component having exactly unit volume.

A standard constructive proof is the atomless fixed-sum dependent-rounding argument. On a refining sequence of finite equal-measure partitions of bounded windows, regard the cell averages as a vector in the hypersimplex
[
{pin[0,1]^N:sum p_j=m}.
]
Split any nonvertex vector along (e_i-e_j), with probabilities chosen to preserve its conditional mean, until a vertex with exactly (m) selected cells is reached. Couple successive refinements conditionally, and treat the two tails by increasing windows. The resulting bounded function-valued martingale (H_k) satisfies
[
0le H_kle1,qquad int H_k=1,qquad mathbb E H_k=mathbb E(fmidmathcal P_k),
]
and the dependent rounding makes the conditional quadratic variation exhaust
(int H_k(1-H_k)). Hence (H_k	o H) almost everywhere and in local (L^1), with
[
Hin{0,1} 	ext{a.e.},qquad int H=1 	ext{a.s.},qquad mathbb EH=f.
]
Writing (H=mathbf1_E) proves the assertion. Tightness follows from
[
mathbb E|Ecap{|x|>R}|=int_{|x|>R}f(x),dx	o0,
]
so no mass is lost at infinity. This proof does not impose bounded support, a moment, a connected support, or a finite number of components.

## 2. Exact product mixture

Apply the lemma separately to each admissible input density (f_i), and choose the random sets independently across coordinates. If
[
F(x)=prod_{i=1}^n f_i(x_i),
]
then Tonelli gives the exact identity
[
oxed{
F(x)=int prod_{i=1}^nmathbf1_{E_i}(x_i),
d(
u_1otimescdotsotimes
u_n)(E_1,ldots,E_n).
}
]
Consequently, for every Borel set (Bsubsetmathbb R) and every measurable map (T:mathbb R^n	omathbb R),
[
oxed{
Pr_f{T(X)in B}
=
int Pr_E{T(X)in B},d
u(E).
}
]
Here (Pr_E) is the product of the uniform laws on the arbitrary unit-measure sets (E_i). The sets may be unbounded and infinitely fragmented.

For (T(x)=x^TAx), this proves directly that the optimal interval-small-ball constant over all cap-one product densities equals the optimal constant over products of unit-measure indicators. It recovers the earlier coordinatewise bathtub reduction, but now as a simultaneous barycentric identity rather than a sequence of objective-dependent replacements.

## 3. New continuity-transfer consequence

Assume a constant (C) has the following property for every product of unit-measure indicators in the full target matrix class:

1. the quadratic output has a continuous density (p_E);
2. (0le p_E(t)le C) for all (t).

Then every admissible cap-one product law has a continuous density bounded by the same (C).

Indeed, choose the canonical continuous version
[
p_E(t)=lim_{m	oinfty}2^{m-1}
Pr_E{|Q-t|<2^{-m}},
]
which is jointly measurable as a pointwise limit. Define
[
p(t)=int p_E(t),d
u(E).
]
The Borel-set mixture identity and Tonelli show that (p) is a density of the original output. Also (ple C). If (t_k	o t), then (p_E(t_k)	o p_E(t)) for every (E), while (|p_E(t_k)|le C); dominated convergence gives (p(t_k)	o p(t)).

Thus
[
oxed{
	ext{uniform bounded continuous density for all extreme product laws}
Longrightarrow
	ext{the same for all admissible product laws,}
}
]
with no constant loss. Unlike total-variation approximation by smooth or finite-fragment inputs, this exact mixture transfers continuity itself.

The converse is immediate because indicator densities are admissible. Therefore the full bounded-continuous target is exactly equivalent to its restriction to arbitrary products (prod_imathbf1_{E_i}), (|E_i|=1). No single-interval or bounded-fragment extremality is asserted.

## 4. Application of fleet01/B13 to an actual inequality

The newest assigned-partner theorem is fleet01/B13,
`QFORM-2VAR-AFFINE-UNIFORM-HALF-RIESZ-v1`, canonical commit
`5dd9b87ba63ecc74fb887a38dc8a5d96e5beab23`.
Its three-coordinate corollary says that if an original-coordinate principal triple (T) is invertible and has a nonzero diagonal pivot (d), then after conditioning every outside coordinate,
[
|p_Q|_infty
le 8sqrt2,|ddet T|^{-1/4},
]
uniformly over all affine leakage from the conditioned coordinates.

Applied first to every indicator component in the exact mixture, for every interval (I),
[
Pr_E{Qin I}
le 8sqrt2,|ddet T|^{-1/4}|I|.
]
Averaging the actual inequality over (E) gives
[
oxed{
Pr_f{Qin I}
le 8sqrt2,|ddet T|^{-1/4}|I|
}
]
for the original rough cap-one inputs. In the partner's tetrahedral remote-support collar this yields the already certified numerical bound (<51.46), now explicitly viewed as an extreme-product geometric inequality averaged without any support-location or fragment-count loss.

The partner theorem already proves the arbitrary-density inequality directly; the point of this application is that its complete affine-fiber bound is compatible with the exact extreme-product representation and therefore can be used componentwise in any future geometric proof.

## 5. Remaining geometric target

The reduction eliminates fractional input densities as a separate issue, but it does not simplify the geometry of the sets. The live correction
`QFORM-NO-UNIFORM-FRAGMENT-COUNT-BATHTUB-v1` shows that even a one-coordinate optimizer can require arbitrarily many separated components.

The first remaining implication for this route is therefore:

[
oxed{
	ext{`QFORM-EXTREME-PRODUCT-SUBLEVEL-v1': }
|{xin E_1	imescdots	imes E_n:x^TAxin I}|
le C|I|
}
]
uniformly over arbitrary measurable (|E_i|=1), with product provenance and curvature used jointly. Proving the continuous-density version for those extreme laws automatically solves the rough-input continuity statement by Section 3.

## 6. Scope and corrections

The full conjecture is not proved. The argument makes no Gaussian, moment, log-concavity, compact-support, connected-support, centered-interval, or finite-fragment assumption. It does not use pointwise law-uniform Fresnel decay, post-rotation independence, or a fiberwise supremum. Continuity is transferred only under the stated uniform continuous-density hypothesis for every extreme component.
