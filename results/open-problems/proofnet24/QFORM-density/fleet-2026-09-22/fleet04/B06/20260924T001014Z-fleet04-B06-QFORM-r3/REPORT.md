SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet04, slot B06, 2026-09-24T00:10:14Z.
attacking: absorb tangential shared-bank leakage by an output shear and exact fold recentering before the curved Jacobian is paid.

# QFORM-TANGENTIAL-SHARED-LEAKAGE-ABSORPTION-v1

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `20260924T001014Z-fleet04-B06-QFORM-r3`  
Status: `ESSENTIAL_STEP_APPLIED / FULL_TARGET_OPEN`  
Execution: `WITHOUT_VERIFIED_BRAIN`.

The full conjecture is not proved here. This theorem extends the preceding fresh-transverse curved-section payment to a genuinely shared-source transverse statistic whenever its shared component is tangential to the curved two-frame. The shared term is removed exactly, not bounded as a random error.

## Theorem

Partition the independent original coordinates into disjoint banks (S) and (R). Let (w,vinmathbb R^S) be orthonormal and satisfy
[
 w_i^2+v_i^2lerac12qquad(iin S).
]
Set
[
 L=langle w,X_Sangle,qquad V=langle v,X_Sangle.
]
Let (B_R) be any random variable determined by (X_R), and define a transverse statistic sharing the curved bank by
[
 B=alpha L+gamma V+B_R
]
for arbitrary (alpha,gammainmathbb R). Thus (B) need not be independent of ((L,V)).

For (lambda
e0), (eta,c,v_0inmathbb R), put
[
 Y=lambda(V-v_0)^2+eta B+c
]
and define the actual shifted fold
[
 v_*:=v_0-rac{etagamma}{2lambda}.
]
For every (r>0), the subprobability pushforward of
[
 (L,Y)mathbf1_{{|V-v_*|>r}}
]
has a density (g_r) satisfying
[
 oxed{ |g_r|_inftylerac4{|lambda|r} }. 	ag{1}
]
The bound is uniform in (alpha,gamma,eta), including (eta=0), and in the law of (B_R). No support or moment assumption is used.

## Proof

Complete the square in the shared (V)-term:
[
 lambda(V-v_0)^2+etagamma V
 =lambda(V-v_*)^2+C_0,
]
where (C_0) is deterministic. Therefore
[
 Y=lambda(V-v_*)^2+etaalpha L+eta B_R+C_1. 	ag{2}
]
Apply the determinant-one output shear
[
 (l,y)mapsto(l,y-etaalpha l-C_1). 	ag{3}
]
It preserves two-dimensional Lebesgue measure and hence preserves the (L^infty) norm of the joint density. After (3), the pushforward is exactly that of
[
 (L,lambda(V-v_*)^2+eta B_R)
]
on (|V-v_*|>r).

Now use the completed fleet01/B06 product-Fourier calculation. For
[
 psi_i(t)=int e^{itx}f_i(x),dx,
]
the sharp Hausdorff--Young input and geometric Brascamp--Lieb on the two-frame ((w_i,v_i)) give the actual inequality
[
 int_{mathbb R^2}
 prod_{iin S}|psi_i(sw_i+tv_i)|,ds,dt
 le(4pi)^2. 	ag{4}
]
Fourier inversion yields
[
 |p_{L,V}|_inftyle
 rac{(4pi)^2}{(2pi)^2}=4. 	ag{5}
]

The map (vmapstolambda(v-v_*)^2), restricted to
(|v-v_*|>r), has at most two inverse branches, each with Jacobian greater than (2|lambda|r). Hence the off-fold joint density (h_r) of
((L,lambda(V-v_*)^2)) satisfies
[
 |h_r|_infty
 lerac{2cdot4}{2|lambda|r}
 =rac4{|lambda|r}. 	ag{6}
]
Finally (B_R) is independent of ((L,V)) by the original-coordinate bank split. Adding (eta B_R) convolves (6) by a probability measure in the second output coordinate and cannot increase its essential supremum. Undoing the shear (3) proves (1).

The proof uses independence only across (Ssqcup R). It does not assert independence after a spectral rotation.

## Exact shear-flat endpoint

Let (g_1,g_2,h) denote the two curved/shear directions and the transverse shared direction on one original-coordinate bank. If (g_1,g_2) are linearly independent and
[
 detoperatorname{Gram}(g_1,g_2,h)=0,
]
then (hinoperatorname{span}{g_1,g_2}). After orthonormalizing the same two-dimensional coefficient plane, the shared transverse statistic has exactly the form
[
 B_S=alpha L+gamma V.
]
Thus Theorem (1) closes the exact Gram-zero shear-flat endpoint without requiring a fresh transverse bank at all.

At the live scale
[
 |lambda|ge1,qquad r=rac1{64},
]
this gives
[
 oxed{ |g_{1/64}|_inftyle256 }. 	ag{7}
]

This is a concrete payment for the exact shear-flat face of the three-bank hybrid. It also covers a fresh remainder (B_R) of arbitrary size and law.

## Scope and first remaining implication

The theorem does not control a shared component orthogonal to the curved plane. Writing generally
[
 B_S=alpha L+gamma V+N,
]
the residual innovation (N) is the genuine shared-bank obstruction. Small coefficient norm is insufficient to discard (N) for arbitrary unbounded fragmented laws.

The remaining B06 implication is therefore sharpened from all shared-bank leakage to:

> prove a curvature-weighted product estimate for the nonzero normal innovation (N), or route a quantitatively nonzero normal Gram determinant to the existing bankwise triple-curvature/overlap receivers.

In particular, exact Gram zero is now paid; only positive but small Gram volume remains in the shear-flat collar.

## Sources and corrections

- Claude source: `math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`.
- fleet01/B06 curved-section Fourier/BL theorem: `math-open-problems@3ae4b0c272e0d3c60f956c9f039bea38fc0f9077`.
- preceding fresh-transverse theorem: `math-open-problems@769800c0ab0851828772adabfb6874aa813e423d`.
- Corrections retained: no arbitrary-joint coarea, no worst conditional-density cap, no small-random-perturbation deletion, and no post-rotation independence.
