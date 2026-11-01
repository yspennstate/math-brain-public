# fleet04/B19 r4 — aggregate third-arm compiler and noncircular proof graph

Programme: \`QFORM-DENSITY-3EIG-20260922\`  
Run: \`20260924T071532Z-fleet04-B19-QFORM-r4\`  
Status: \`ESSENTIAL_STEP_APPLIED / NEW SUPPORTING COMPILER / FULL TARGET OPEN\`

The unrestricted universal theorem is not claimed. All matrices below are literal original-coordinate blocks. No rotated independence, moment assumption, support restriction, conditional-density supremum, arbitrary-joint coarea estimate, or deletion of a nonzero coefficient is used.

## 1. Source pins and terminal nodes

The Claude baseline is \`math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837\`, directory
\`proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/\`.
Its \(D'\), \(D_5\), mixed-hub/Fresnel, and ruled-side results are retained only in their stated hypotheses; the ruled estimate does not pay arbitrary translated access to the convex/two-sheet side.

The live two-column input is fleet04/B20 r13,
\`math-open-problems@d2560a041fd91c05d7fddf50f5b5414ecd2680a2\`.
After the child-window, scalar-pivot, strong-edge, and alignment splits, its transverse double-anchor branch supplies a literal physical block
\[
M=[u\ v],\qquad
s_2(M)>\sigma_0 L,\qquad
\sigma_0=4.6565947316667495\times10^{-10}.
\tag{1.1}
\]

The marginal-free terminal receiver is fleet01/B04's
\`QFORM-THIRDCOMPOUND-CROSS-PROMOTION-v1\`,
\`math-open-problems@c2ce876df8b5483a00802170001d4144bb4cdbfa\`:
for every literal physical cross block \(B\),
\[
\|p_Q\|_\infty\le 6^{4/3}E_3(B)^{-1/6},
\qquad E_3(B)=e_3(BB^\top),
\tag{1.2}
\]
with a continuous \(C_0\) density, while arbitrary same-bank quadratic blocks and outside affine couplings are retained.

The newest completed fleet01/B19 input is
\`QFORM-PHYSICAL-HUB-ONE-SQUARE-FRESNEL-LINFINITY-v1\`,
\`math-open-problems@c47451aed1eb3e9a621cb1f327bca666c7f760cf\`.
For a physical hub \(h\), receiver bank \(I\), self block
\[
A[I,I]=D+\lambda vv^\top,
\]
and hub coupling \(c=A[I,h]\), if the two-frame Gram
\[
G=\begin{pmatrix}\|v\|_2^2&\langle v,c\rangle\\
\langle v,c\rangle&\|c\|_2^2\end{pmatrix}
\]
is positive definite and every normalized physical row leverage is at most \(1/2\), then
\[
\boxed{\|p_Q\|_\infty
\le 12\,2^{-2/3}(|\lambda|\det G)^{-1/3}.}
\tag{1.3}
\]
This is an actual terminal node in the graph. For the principal-minimal maximal-coloop family in that source, \(\lambda=1\) and \(G=\operatorname{diag}(1,a^2)\); at the target endpoint \(|a|=1/2\), (1.3) gives
\[
\boxed{\|p_Q\|_\infty\le12.}
\tag{1.4}
\]
Thus the zero-pair-Schur maximal-coloop example is paid without scalarizing away its third source.

## 2. New deterministic compiler

### Theorem — \`QFORM-DOUBLEANCHOR-AGGREGATE-THIRDARM-v1\`

Let \(R\) and \(J=\{i,j\}\sqcup T\) be disjoint original-coordinate banks and write
\[
B=A[R,J]=[u\ v\ W],\qquad M=[u\ v].
\tag{2.1}
\]
Let \(P\) be the orthogonal projection in \(\mathbb R^R\) onto
\(\operatorname{span}\{u,v\}^\perp\). If
\[
s_2(M)\ge \sigma L,\qquad \|PW\|_F\ge\delta L,
\tag{2.2}
\]
then
\[
\boxed{E_3(B)\ge \sigma^4\delta^2L^6}
\tag{2.3}
\]
and hence, for every independent cap-one product input,
\[
\boxed{
\|p_{X^\top AX}\|_\infty
\le
\frac{6^{4/3}}{\sigma^{2/3}\delta^{1/3}}\frac1L.
}
\tag{2.4}
\]
The density has a continuous \(C_0\) representative.

If (2.2)'s second inequality fails, the entire remaining physical third bank satisfies the quantified aggregate alignment collar
\[
\boxed{\|P W\|_F<\delta L.}
\tag{2.5}
\]

### Proof

Write the columns of \(W\) as \(w_t\), \(t\in T\). The part of the full third-compound energy using the fixed columns \(u,v\) and one column \(w_t\) is
\[
\sum_{t\in T}\ \sum_{\substack{S\subset R\\|S|=3}}
\det [u\ v\ w_t][S,:]^2.
\tag{2.6}
\]
By Cauchy--Binet, the inner sum equals the Gram determinant
\[
\det\operatorname{Gram}(u,v,w_t)
=
\det\operatorname{Gram}(u,v)\,
\operatorname{dist}(w_t,\operatorname{span}\{u,v\})^2.
\tag{2.7}
\]
Summing over \(t\) gives
\[
E_3(B)
\ge
\det\operatorname{Gram}(u,v)\,\|PW\|_F^2.
\tag{2.8}
\]
The two eigenvalues of \(\operatorname{Gram}(u,v)=M^\top M\) are
\(s_1(M)^2,s_2(M)^2\). Therefore
\[
\det\operatorname{Gram}(u,v)
=s_1(M)^2s_2(M)^2
\ge s_2(M)^4
\ge \sigma^4L^4.
\tag{2.9}
\]
Equations (2.8)-(2.9) and (2.2) prove (2.3). Apply the marginal-free physical third-compound receiver (1.2) to the same cross block \(B\) to obtain (2.4) and \(C_0\) regularity. If the transverse gate fails, (2.5) is its exact negation. QED.

The use of the full Frobenius norm in (2.2) is essential: it aggregates many individually tiny physical arms without selecting a reciprocal small column and without introducing a dimension factor.

## 3. Live numerical consequence

Apply the theorem with the live value \(\sigma=\sigma_0\) from (1.1) and choose the fixed transverse gate
\[
\delta=\frac1{64}.
\tag{3.1}
\]
Then
\[
E_3(B)>
\sigma_0^4\,2^{-12}L^6
=
1.1479258132674004\times10^{-41}L^6,
\tag{3.2}
\]
and (2.4) gives
\[
\boxed{
\|p_Q\|_\infty
<
\frac{72{,}590{,}986.237}{L}.
}
\tag{3.3}
\]
Thus the live transverse double-anchor branch is terminal whenever a disjoint remaining physical bank has aggregate component at least \(L/64\) outside the anchor plane. The complementary survivor is now the explicit same-matrix collar
\[
\boxed{
\|P_{\operatorname{span}\{u,v\}^\perp}W\|_F<\frac{L}{64}.
}
\tag{3.4}
\]

## 4. Noncircular proof graph after this step

The source-valid graph is:

1. \(D'\), \(D_5\), physical \(E_3\), ridge/window, scalar-pivot, mixed-hub/Fresnel, pair-log, and ruled-side receivers are terminal only in their exact hypotheses.
2. The diffuse/deletion route pays the small-\(s_3\) child by volume and the diffuse large-\(s_3\) child by ridge; failure of child ridge produces a physical pivot or second star.
3. The pivot is paid. The two-star branch yields a strong edge, an aligned pair, or the live rank-two block (1.1).
4. The new theorem pays the live rank-two block whenever a disjoint third bank has aggregate transverse mass \(L/64\). Failure is exactly (3.4), not a return to an earlier node.
5. The fleet01/B19 one-square hub theorem pays the maximal-coloop branch whenever a retained third source has diffuse augmented hub-square Gram; its six-leaf failure remains a finite physical localization.
6. Claude's ruled theorem pays only the one-sheet class. The shared-bank convex/two-sheet collar remains separate.

The remaining leaves are therefore:

- the aggregate plane-alignment collar (3.4), including the strong-edge/aligned-star compiler;
- the finite at-most-six-leaf failure in the hub-plus-third-source manufacture;
- the global latent-eight endpoint with its nonzero tail retained;
- the robust light-light rank-two endpoint with retained third/high-spectrum source;
- the shared-bank indefinite convex/two-sheet collar.

None is declared solved. A full candidate would still require all leaves to terminate and two actual independent end-to-end reviews.

## 5. Scope

The theorem is deterministic plus the already completed marginal-free receiver. It preserves every sign, arbitrary same-bank terms, arbitrary outside couplings, all extra spectrum, and arbitrary independent cap-one input laws. It does not prove that a suitable disjoint third bank always exists; that manufacture is precisely the remaining separator/alignment obligation. Full QFORM and full-target continuity remain open.
