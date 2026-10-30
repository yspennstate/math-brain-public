SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet03, slot B05, 2026-09-24T14:38:26Z.

# fleet03/B05 r13 — the one-sided grouped coarea currency is exactly disjoint E3; robust two-anchor data alone cannot remove the s8 logarithm

Objective: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`.
Run: `20260924T143826Z-fleet03-B05-fixedmult-r13`.
Baseline manuscript: `yspennstate/math-open-problems@7c0d6e60946b19423e6400a12d34b473cf0591e2`, blob `183ccd294763214e6a707e8d4749ff9a8cf7006d`, SHA-256 `9f3bdec0b88debe9a66076c7b4a5cc894fb14e69b89591a4107e785340f65e69`.
Fresh nine-eigenvalue input: `yspennstate/math-open-problems@de66db60d643a9d2366ba542afb8ea295957438a`.
Fresh robust-pair input: `yspennstate/math-open-problems@0408c579bcda638e72c010ff99892a22b9049796`.
Fresh critical-endpoint input: `yspennstate/math-open-problems@72bc34125d82485d473030d663ce0dedd2de3eb3`.
Designated partner input: `fleet04/B05`, `yspennstate/math-open-problems@84b63093480022df1a463895b8b77eb2a2ea19db`.

Status: **proved exact structural identities + a sharp product-law counterexample to the determinant-free L-infinity extension; multiplicity eight remains open.** The lowest complete bounded-density threshold presently used here is nine. The unrestricted three-eigenvalue conjecture remains open.

## 1. B05 audit of the new grouped receiver

The grouped product-Fourier compiler in `de66db...` is source-valid in the product-projection / exceptional-slice interfaces checked here. It conditions only on literal original-coordinate banks; after squaring, the difference coordinates remain independent and have density caps at most one. The product-projection input is used only for a genuine linear image of those product coordinates. The entropy step uses the canonical subset marginals and never conditions on a rotated projection. The scale `2t`, Plancherel power, and determinant exponents are consistent.

The designated `fleet04/B05` reconstruction supplies the needed rough-law projection detail: after zero Brascamp--Lieb weights are omitted, the final entropy line is an inequality, not a restricted-index equality,

\[
 \log p(y)
 \le \frac12\sum_{b_i>0}(-b_i\log b_i)
 \le \frac12\sum_{b_i>0}(1-b_i)
 \le \frac d2.
\]

This leaves the product-projection cap `e^{d/2}` unchanged. Its definite/hyperbolic coarea reconstruction also verifies that critical fibers are treated by measure domination/Tonelli; no pointwise density trace on a condition-dependent hyperbola is required.

For the particular grouped parameters used below, the compiler says:

* `(k,ell)=(2,1)`, `d=3`:
\[
 \|p_Q\|_\infty
 \le C_{21} S^{-1/3}Z_1^{-1/6},
 \qquad C_{21}=3\,2^{1/6}e^{2/3}=6.55877262385\ldots .
\tag{1.1}
\]
* `(k,ell)=(1,2)`, `d=3`:
\[
 \|p_Q\|_\infty
 \le C_{12} S^{-1/3}Z_2^{-1/6},
 \qquad C_{12}=3\,2^{1/3}e^{5/6}2^{1/6}=9.76221393478\ldots .
\tag{1.2}
\]

These are continuous-`C_0` branches because their characteristic-function majorants are integrable.

## 2. Exact identity: a two-anchor one-sided promotion spends only disjoint order-three volume

Fix two literal original-coordinate anchors `H={h_1,h_2}` and partition the remaining coordinates as `I disjoint_union J`. Put

\[
 C_J=A[H,J]\in\mathbb R^{2\times |J|}.
\]

Let `P_J` be the orthogonal projection in `R^J` onto the row space of `C_J`. For every `i in I`, write

\[
 a_i=A[i,J],\qquad r_i=a_i(I-P_J),
\]

and set

\[
 S^2:=\det(C_JC_J^T),\qquad Z_1:=\sum_{i\in I}\|r_i\|^2.
\]

If `rank C_J<2`, both sides of the identity below vanish. If `rank C_J=2`, the Gram Schur complement gives, for every `i`,

\[
 \det\!\begin{pmatrix}C_J\\ a_i\end{pmatrix}
       \begin{pmatrix}C_J\\ a_i\end{pmatrix}^{\!T}
 =\det(C_JC_J^T)\,\|r_i\|^2.
\]

Cauchy--Binet therefore yields the exact formula

\[
\boxed{
 S^2Z_1
 =\sum_{i\in I}\ \sum_{\substack{T\subset J\\|T|=3}}
   \det A[H\cup\{i\},T]^2 .
}
\tag{2.1}
\]

Every determinant on the right is a **disjoint** `3 x 3` minor: `H union {i}` is disjoint from `T` because `i in I` and `T subset J`. Consequently

\[
\boxed{S^2Z_1\le V_3(A).}
\tag{2.2}
\]

Substituting into (1.1), the entire `(k,ell)=(2,1)` one-sided grouped receiver depends on

\[
 S^{-1/3}Z_1^{-1/6}=(S^2Z_1)^{-1/6},
\]

so its geometric currency is exactly an anchored piece of disjoint `V_3`, not the overlap-one currency surviving at multiplicity eight.

There is also an exact random-cut interpretation. If each coordinate of `H^c` is independently sent to `I` or `J` with probability `1/2`, then a fixed disjoint term with row set `H union {i}` and column triple `T` is selected with probability

\[
 (1/2)(1/2)^3=1/16.
\]

Hence

\[
 \mathbb E_{I,J}[S^2Z_1]
 ={1\over16}
 \sum_{i\notin H}\sum_{\substack{|T|=3\\T\cap(H\cup\{i\})=\varnothing}}
 \det A[H\cup\{i\},T]^2
 \le {V_3(A)\over16}.
\tag{2.3}
\]

This is not merely an averaging loss: (2.2) holds for every partition.

## 3. The analogous one-anchor `(1,2)` receiver also sees only disjoint V3

Fix one literal anchor `h` and a partition of its complement as `I disjoint_union J`. Put

\[
 m=A[h,J],\qquad S^2=\|m\|^2.
\]

For `i in I`, project `a_i=A[i,J]` orthogonally off `m`, obtaining residual rows `r_i`. Let

\[
 Z_2=e_2(RR^T)
 =\sum_{i<j}\det\operatorname{Gram}(r_i,r_j).
\]

Gram--Schmidt followed by Cauchy--Binet gives

\[
\boxed{
 S^2Z_2
 =\sum_{\substack{i<j\in I}}
   \sum_{\substack{T\subset J\\|T|=3}}
   \det A[\{h,i,j\},T]^2
 \le V_3(A).
}
\tag{3.1}
\]

Thus (1.2) also pays exactly

\[
 S^{-1/3}Z_2^{-1/6}=(S^2Z_2)^{-1/6},
\]

again a disjoint order-three currency. Under a fair random cut, a fixed term is selected with probability `(1/2)^2(1/2)^3=1/32`.

### Consequence for the multiplicity-eight terminal collar

The current `s_8` terminal branch is precisely the chamber in which the already-completed `E_3` receiver did **not** fire; one works with `V_3(A)<kappa^3` and a positive overlap-one/two-sided currency instead. Equations (2.1) and (3.1) prove that simply feeding the new robust two-anchor pair into the existing one-sided grouped compiler cannot spend that surviving overlap currency. Any total-degree-three one-sided promotion of the forms `(2,1)` or `(1,2)` collapses back to the disjoint `V_3` branch already separated off.

This is the precise missing factor:

> the new analytic receiver must keep a physical anchor **shared on both sides** of the quadratic interaction before Cauchy--Schwarz/Plancherel removes it. A one-sided promoted anchor only sees disjoint third exterior volume.

This explains algebraically why the five-role overlap determinant

\[
 \det A[S\cup\{h\},T\cup\{h\}]
\]

cannot be replaced by an ordinary one-sided cross determinant without losing the very curvature that survives when `V_3` is small.

## 4. Sharp counterexample: robust two-anchor cross density alone cannot imply L-infinity

The fresh determinant-free two-anchor theorem at `72bc3412...` proves finite `L^r`, `r<infinity`, uniformly in the anchor self-block `K`, assuming only that the random slope `L` has a bounded two-dimensional density. That endpoint cannot be upgraded to `L^infinity` under those hypotheses alone.

Fix `0<epsilon<1`. Let

\[
 U_1,U_2,V_1,V_2\stackrel{ind}{\sim}\operatorname{Unif}[-1/2,1/2].
\]

Set

\[
 K=\epsilon\begin{pmatrix}0&1\\1&0\end{pmatrix},
 \qquad C=I_2,
 \qquad R=K^{-1}={1\over\epsilon}
      \begin{pmatrix}0&1\\1&0\end{pmatrix}.
\]

For `U=(U_1,U_2)` and `V=(V_1,V_2)`, consider

\[
 Q=U^TKU+2U\cdot V+V^TRV.
\tag{4.1}
\]

The original four coordinates are independent and have density cap one. The anchor-to-complement cross block is exactly `C=I_2`, hence

\[
\boxed{\det(CC^T)=1.}
\tag{4.2}
\]

The anchor principal block has zero diagonals and

\[
 \det K=-\epsilon^2,
\]

which may be arbitrarily close to zero. Completing the square is exact:

\[
 Q=(U+K^{-1}V)^TK(U+K^{-1}V).
\]

Writing

\[
 Z_1=U_1+V_2/\epsilon,\qquad
 Z_2=U_2+V_1/\epsilon,
\]

we have

\[
\boxed{Q=2\epsilon Z_1Z_2.}
\tag{4.3}
\]

The variables `Z_1,Z_2` are independent because they depend on disjoint pairs of the original independent coordinates. Their common density `g_epsilon` is the convolution of `Unif[-1/2,1/2]` with the density `epsilon 1_{[-1/(2epsilon),1/(2epsilon)]}`. Therefore

\[
 g_\epsilon(z)=\epsilon
 \qquad\text{for } |z|\le a_\epsilon:={1-\epsilon\over2\epsilon}>0.
\tag{4.4}
\]

For `0<|t|<2\epsilon a_\epsilon^2`, the product change of variables gives

\[
 p_Q(t)
 ={1\over2\epsilon}
 \int_\mathbb R g_\epsilon(z)
 g_\epsilon\!\left({t\over2\epsilon z}\right){dz\over|z|}.
\]

Restricting to

\[
 { |t|\over2\epsilon a_\epsilon}\le z\le a_\epsilon
\]

and using (4.4),

\[
\boxed{
 p_Q(t)
 \ge {\epsilon\over2}
 \log {2\epsilon a_\epsilon^2\over |t|}
 \longrightarrow\infty
 \quad(t\to0).
}
\tag{4.5}
\]

Thus the output density is essentially unbounded despite the strongest possible robust-cross determinant `det(CC^T)=1` and despite every source coordinate having density cap one.

The exact missing structural quantity is visible from the Schur complement:

\[
 R-C^TK^{-1}C=0.
\tag{4.6}
\]

The full `4 x 4` quadratic matrix has rank two, so this is **not** a counterexample to the fixed-multiplicity theorem or the unrestricted QFORM conjecture. It is a counterexample to any attempted theorem saying that a dimension-free two-anchor cross determinant plus a small/near-singular self-block is by itself enough for a bounded output density.

It also shows that the finite-`L^r` result of `72bc3412...` is qualitatively sharp under its stated hypotheses: the logarithmic endpoint can genuinely occur. To prove `s_8`, one must use the extra Schur/overlap-one curvature forced by the eight-large-eigenvalue hypothesis, not only the random-slope density.

## 5. Designated fleet04/B05 result applied to an actual inequality

The robust-pair theorem `0408c579...` gives in the unpaid `s_8` collar a literal pair `H` with

\[
 D_H=\det(CC^T)\ge D_0=0.3649442658827020\ldots .
\]

Let `G=CC^T` and `U=G^{-1/2}C`. Then `UU^T=I_2`. Applying the completed `fleet04/B05` product-projection reconstruction to the actual complement product law gives

\[
 \|p_{U X_{H^c}}\|_\infty\le e.
\]

Hence the physical slope

\[
 L=CX_{H^c}+b_H/2
\]

has density cap

\[
\boxed{
 M\le {e\over\sqrt{D_H}}
 \le {e\over\sqrt{D_0}}
 =4.499675651055483\ldots .
}
\tag{5.1}
\]

At the exact-zero anchor endpoint `A[H,H]=0`, conditioning on the complement gives the literal-anchor density bound

\[
 {1\over2\max(|L_1|,|L_2|)}
 \le {1\over\sqrt2|L|}.
\]

The two-dimensional bathtub integral with (5.1) gives

\[
 \mathbb E|L|^{-1}\le2\sqrt{\pi M},
\]

so

\[
\boxed{
 \|p_Q\|_\infty
 \le \sqrt{2\pi e}\,D_H^{-1/4}
 \le 5.31716991809.
}
\tag{5.2}
\]

This is an actual target-branch inequality using the designated partner result. The same integrable majorant yields continuity at this exact-zero endpoint. No rotated variables are declared independent.

## 6. Status ledger and next obligation

**PASS:** the B05 product-projection and exceptional-slice interfaces of the fresh grouped compiler are consistent with the independent `fleet04/B05` reconstruction.

**PROVED:** identities (2.1) and (3.1). They show that the standard one-sided grouped `(2,1)` and `(1,2)` receivers spend disjoint `V_3` and therefore cannot by themselves consume the multiplicity-eight overlap-one currency.

**PROVED / counterexample to an extension:** (4.1)--(4.6) give a cap-one product source with `det(CC^T)=1` but logarithmically unbounded quadratic density. Robust two-anchor cross control alone is insufficient; a quantitative transverse Schur/shared-anchor factor is logically necessary.

**OPEN:** multiplicity eight. The exact remaining analytic theorem should be a **shared-anchor overlap receiver** that consumes determinants of the form `det A[S+h,T+h]` before the common physical coordinate `h` is lost. The existing one-sided grouped compiler, the determinant-free random-slope finite-`L^r` theorem, and the critical split-row `1/|t|` estimate are each sharp at their stated interfaces and do not supply this endpoint.

**OPEN:** unrestricted three-eigenvalue conjecture and its global continuity conclusion.

No Gaussianity, moments, compact support beyond the explicit stress-test uniforms, log-concavity, diagonal-basis independence, or pointwise quadratic van der Corput decay is used in any positive target implication. The stress test is explicitly a mechanism counterexample, not a target counterexample.
