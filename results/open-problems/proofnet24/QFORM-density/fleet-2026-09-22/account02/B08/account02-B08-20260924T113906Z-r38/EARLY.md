# account02/B08 r38 early calculation — balanced-bank spectral shadow

Programme: QFORM-DENSITY-3EIG-20260922. Full target remains open.

Consider the exact-rank-two deletion-child state
\[
A=\begin{pmatrix}a&b^T\\ b&V\Lambda V^T\end{pmatrix},\qquad V^TV=I_2,
\]
with `s_3(A)>=L`. Let `J union K` be the inherited original-coordinate balanced cut, put
`G=V_J^T V_J`, `H=V_K^T V_K`, and assume `G,H>=g I_2`, where
`g=1/2-1/(4 sqrt(2))` in the live account03/B08 collar. Let `c_J,c_K` be the bankwise least-squares coefficients,
`r_J=b_J-V_Jc_J`, `r_K=b_K-V_Kc_K`, and
`c_*=Gc_J+Hc_K`. Set
`u=b-Vc_*`, `beta=||u||`, `e_B=||r_B||`.

Define the aligned shadow
\[
A_0=\begin{pmatrix}a&(Vc_*)^T\\Vc_*&V\Lambda V^T\end{pmatrix}.
\]
Then
\[
\|A-A_0\|_{op}=\beta,
\qquad s_3(A_0)\ge L-\beta.
\]
Indeed `A-A_0=[[0,u^T],[u,0]]`, whose nonzero eigenvalues are exactly `+-beta`, and Weyl gives the singular-value claim. Since `rank(A_0)<=3`, whenever `beta<L` the shadow is an exact rank-three matrix whose three nonzero eigenvalues all have modulus at least `L-beta`.

For either bank `B in {J,K}`, let `G_B=V_B^T V_B` and normalize `W_B=V_B G_B^{-1/2}`, so `W_B^T W_B=I_2`. The aligned bank core with slope `c_*` is the congruence
\[
K_{B,*}=S_B K_* S_B,
\quad S_B=\operatorname{diag}(1,G_B^{1/2}),
\quad K_*=\begin{pmatrix}a&c_*^T\\c_*&\Lambda\end{pmatrix}.
\]
Hence
\[
s_3(K_{B,*})\ge g\,s_3(K_*)\ge g(L-\beta).
\]
Replacing `c_*` by the actual bank coefficient `c_B` changes this symmetric core by an off-diagonal rank-two matrix of operator norm
\[
\|G_B^{1/2}(c_B-c_*)\|=\|V_B(c_B-c_*)\|\le\beta,
\]
because `u_B=r_B+V_B(c_B-c_*)` is an orthogonal decomposition. Therefore the exact-aligned bank shadow has
\[
 s_3\ge g(L-\beta)-\beta.
\]
Finally the actual principal bank matrix differs from this aligned bank shadow by
`[[0,r_B^T],[r_B,0]]`, of operator norm exactly `e_B`; consequently
\[
\boxed{s_3(A_{\{0\}\cup B})\ge g(L-\beta)-\beta-e_B.}
\]
This is an actual spectral gate on a literal original-coordinate principal matrix; no random-variable perturbation has been discarded.

If `r_B=0`, that bank principal matrix is itself exact aligned rank three. Conditioning on the opposite bank only creates deterministic affine terms, and the completed account03/B08 exact-aligned endpoint theorem therefore yields
\[
\boxed{\|p_Q\|_\infty\le {128\,64^{1/4}\over g(L-\beta)-\beta}.}
\]
Thus one vanishing bank residual closes the punctured split-mismatch endpoint uniformly, without any negative power of `beta`.

At the current ultra-puncture gate
`beta<=beta_0 L`, `beta_0=4 sqrt(2) 2^-20=5.394796609394436e-6`, and on the unpaid old-residual branch `e_B<eta L`, `eta=2^-20`, the literal bank spectral gate is
\[
s_3(A_{\{0\}\cup B})>
[g(1-\beta_0)-\beta_0-\eta]L
=0.323215212508449\,L.
\]
If one residual vanishes, the density constant is at most
`1120.114/L` (rounded upward).

This leaves a genuinely two-sided residual collar rather than a pure split-mismatch collar. The next calculation will construct a target-valid Walsh family with `e_J,e_K>0`, zero bankwise mismatch, arbitrarily small `beta`, and all physical 2x2 pairs below `L/64`.
