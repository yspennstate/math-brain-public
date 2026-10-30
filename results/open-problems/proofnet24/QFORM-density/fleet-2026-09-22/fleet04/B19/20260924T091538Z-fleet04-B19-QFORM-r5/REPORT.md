# fleet04/B19 — finite-carrier curved rank-two terminal and noncircular proof graph

**Run:** `20260924T091538Z-fleet04-B19-QFORM-r5`  
**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Status:** `ESSENTIAL_STEP_APPLIED / NEW_TERMINAL_NODE / FULL_QFORM_OPEN`  
**Continuity:** separate; only essential boundedness is asserted below.

## 1. Exact target and source boundary

The target remains the unrestricted statement for independent real original coordinates with probability densities at most one and arbitrary real symmetric (A) satisfying (s_3(A)ge1). No moment, support, iid, smoothness, log-concavity, post-rotation independence, or small-remainder deletion is used.

The newest Claude directory was checked through scientific commit
`b0cbc2233369b6a3f366cf569d425f485f123e1c`, retaining the live corrections against arbitrary-joint coarea, conditional projection caps, pointwise quadratic van der Corput, and two-sheet X-ray closure.

The completed fleet01/B19 theorem actually consumed is scientific commit
`879ad8a0be00493b8a826558a993a45a6070f162`.
For a nonzero literal scalar pivot (a=A_{ii}), its exact Schur complement (S) satisfies
[
s_2(S)ge s_3(A)ge1,
]
and if
[
W_2(S)=sum_{substack{|I|=|J|=2\Icap J=arnothing}}det S[I,J]^2,
]
then
[
|p_Q|_infty
le 8sqrt2,e^{1/4}|a|^{-1/2}W_2(S)^{-1/8}.
	ag{1.1}
]
At (W_2(S)=0), (S=Delta+R) with (Delta) physical diagonal and (operatorname{rank}Rle2). When (|Delta|_{m op}<1/2), the target forces (R) to have rank two with both nonzero singular values (>1/2); fleet01/B19 either pays the diffuse carrier or localizes the obstruction to at most six literal coordinates.

The corrected fleet01/B18 input is scientific commit
`43beacb57eba0134d9b4b4cf8b7843a4f119049c`, built from the exact primary-source scopes of Banks--Garza Vargas--Kulkarni--Srivastava (arXiv:2005.08930), Rudelson--Vershynin (arXiv:1402.4492), and Livshyts--Paouris--Pivovarov (arXiv:1507.07949). It permits arbitrary curvature on one original-coordinate bank; it does not permit silently adding curvature on the zero-self side.

## 2. Finite-carrier curved rank-two terminal

Let (I,J,{w}) be disjoint sets of literal original coordinates. Suppose the retained coefficient packet is
[
A_R=
egin{pmatrix}
0&B&0\
B^	op&C&h\
0&h^	op&a
end{pmatrix},
qquad R=Isqcup Jsqcup{w},
	ag{2.1}
]
where (C=C^	op) and (h) are arbitrary, (a
e0), and (B) has singular values
(sigma_1gesigma_2>0). All coefficients involving outside coordinates are arbitrary.

### Theorem 2.1 — `QFORM-FINITECARRIER-CURVED-R2-TERMINAL-v1`

The full ambient quadratic form has a density and
[
oxed{
|p_{X^	op AX}|_infty
le
minleft{
rac{2sqrtpi}{sqrt{sigma_1sigma_2}},
rac{4sqrt2}{sqrt{|a|sigma_1}}
ight}.}
	ag{2.2}
]

#### Proof

Condition only on the outside original coordinates. The retained polynomial has the form
[
2X_I^	op B X_J+alpha^	op X_I+G(X_J)
+aX_w^2+ho(X_J)X_w+c,
	ag{2.3}
]
where (G) contains the entire (J)-bank curvature (X_J^	op C X_J), while (ho) contains the genuine (J-w) coupling and the conditioned outside-(w) couplings. Thus every conditioning weight is retained.

Apply the corrected fleet01/B18 one-sided-curvature theorem with (j=2). Since the two-dimensional unit-ball volume is (v_2=pi),
[
C_2(B)
=rac{2}{1}v_2^{1/2}(sigma_1sigma_2)^{-1/2}
=rac{2sqrtpi}{sqrt{sigma_1sigma_2}}.
	ag{2.4}
]
Its private-square branch gives the second term in (2.2). Both bounds are uniform in the conditioned outside values, so averaging proves (2.2). No rotated independence is used. QED.

At the live cross-volume gate
[
sigma_1sigma_2ge2^{-12},
]
Theorem 2.1 gives the actual terminal inequality
[
oxed{|p_Q|_inftyle128sqrtpi
=226.874ldots .}
	ag{2.5}
]
This improves the earlier fleet04/B18 (2sqrt{2pi})-constant packet, which gave (<320.849), and it retains arbitrary (C) and (h).

At the alternative private-square gate
[
|a|sigma_1ge2^{-12},
]
it gives
[
oxed{|p_Q|_inftyle256sqrt2<362.039.}
	ag{2.6}
]

The exact zeros in the (I-I) and (I-w) blocks are hypotheses, not perturbative conveniences. Small nonzero replacements are not discarded.

## 3. Actual fleet01/B19 threshold application

Choose
[
a_0=2^{-12},qquad w_0=2^{-32}.
]
Whenever a literal scalar pivot obeys (|a|ge a_0) and its Schur tetrad energy obeys (W_2(S)ge w_0), equation (1.1) gives
[
oxed{
|p_Q|_infty
le8sqrt2,e^{1/4}(2^{-12})^{-1/2}(2^{-32})^{-1/8}
<14{,}876.}
	ag{3.1}
]
This is a genuine full-law inequality: all same-bank curvature, affine terms, signs, and extra spectrum remain.

At the exact endpoint (W_2=0), (|Delta|_{m op}<1/2), fleet01/B19 either pays the diffuse rank-two carrier by
[
|p_Q|_infty<17.449,|a|^{-1/2},
	ag{3.2}
]
or produces a finite carrier set (H) of at most six literal coordinates. Theorem 2.1 now terminates every such finite-carrier child that exposes an exact packet (2.1) satisfying either gate (2.5) or (2.6).

Thus the finite-carrier output is no longer merely a localization statement: it has an explicit curved rank-two terminal whenever the localized coefficient geometry has one genuine zero-self side and a payable cross-volume or private-square product.

## 4. Compact noncircular proof graph

1. Start with the full target (s_3(A)ge1) in original coordinates.
2. Apply the existing (D'), (D_5), ridge/window, physical-pair, grouped-square, mixed-hub, and finite-core branches only at their stated gates.
3. If a literal scalar pivot (a
e0) is selected, use fleet01/B19 singular inheritance (s_2(S)ge1).
4. If (|a|ge2^{-12}) and (W_2(S)ge2^{-32}), terminate by (3.1).
5. If (W_2(S)=0) and (|Delta|_{m op}<1/2), use the exact diagonal-plus-rank-two rigidity theorem. The diffuse branch terminates by (3.2); the nondiffuse branch reduces to at most six literal carrier coordinates.
6. On a finite carrier, if an exact packet (2.1) has (sigma_1sigma_2ge2^{-12}), terminate by (2.5); if (|a|sigma_1ge2^{-12}), terminate by (2.6).
7. Separately, the ruled estimate pays only its one-sheet side. The shared-bank convex/two-sheet side is not imported into any node above.
8. The remaining leaves are:
   - quantitative (0<W_2(S)<2^{-32}) stability without a strong-triangle witness;
   - genuinely tiny or zero scalar pivots requiring a hub-star/third-resource compiler;
   - finite carriers lacking the exact zero-self-side geometry (2.1);
   - the shared-bank convex/two-sheet collar.

No node depends on a conclusion downstream from itself.

## 5. Status

The full QFORM conjecture remains **OPEN / NOT PROVED / NOT DISPROVED**. No full-candidate review is requested because the graph still has explicit leaves. The new contribution is the terminal node (2.2), its live constants (2.5)--(2.6), and its insertion into the finite-carrier output of fleet01/B19 without strengthening any source theorem beyond its hypotheses.
