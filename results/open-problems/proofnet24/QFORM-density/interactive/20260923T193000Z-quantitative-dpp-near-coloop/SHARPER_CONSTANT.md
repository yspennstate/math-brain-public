# Optional sharper DPP constant using intersecting basis pairs

This strengthens, without changing, the proof in REPORT.md. Under the same exact-rank-three and physical N3(1/64) assumptions, keep
\[
 p=V_3(A)/\det(\Lambda)^2,qquad
 m=\max_i\|u_i\|^2,qquad
 \delta_S=1-\lambda_1(U_S^{\mathsf T}U_S).
\]
Let \(c=1/64\), \(d=\sqrt{c+c^2}=\sqrt{65}/64\), \(\tau_3=c+2d\), and \(\tau_5=c+4d=0.5195161092\ldots<1\). The preceding two-frame-direction lemma implies \(\lambda_2(G_W)\leq\tau_5\) for every physical set \(|W|\leq5\). The DPP identity still gives
\[
 p\geq k\,\mathbb E\delta_S,qquad k=(1-\tau_3)^2=0.5364528924\ldots .
\tag{1}
\]
For two iid DPP bases \(S,T\), on the event \(S\cap T\ne\varnothing\) one has \(|S\cup T|\leq5\). The same projective-angle argument in REPORT.md yields
\[
 v_S^{\mathsf T}G_Tv_S
 \geq 1-\delta_T-
 \frac{2(\delta_S+\delta_T)}{1-\tau_5}.
\]
On the complementary event, the trivial bound \(v_S^{\mathsf T}G_Tv_S\geq0\) yields the common globally valid inequality
\[
 v_S^{\mathsf T}G_Tv_S
 \geq 1-\delta_T-
 \frac{2(\delta_S+\delta_T)}{1-\tau_5}
 -\boldsymbol1_{\{S\cap T=\varnothing\}} .
\tag{2}
\]
Average over independent \(S,T\). The DPP one-point marginals give \(\mathbb E_TG_T\preceq mI\), so
\[
 1-m\leq p+
 \left(1+\frac4{1-\tau_5}\right)\mathbb E\delta_S
 \leq
 \left[1+\frac{1+4/(1-\tau_5)}{k}\right]p .
\]
Consequently
\[
 p\geq
 \frac{k}{k+1+4/(1-\tau_5)}(1-m)
 =0.0543992972\ldots\,(1-m),
\tag{3}
\]
and \(1-m\leq18.38259043\ldots\,p\leq18.38259043\ldots\,V_3(A)\).

All statements in REPORT.md, EXACT_COLOOP_TRUNCATION.md and DIFFUSE_LEAKAGE_OBSTRUCTION.md remain valid with their conservative constants. If one substitutes the sharper (3) into the truncation proof, the rank-two leakage estimate improves to
\[
 \|A-A_0\|_F
 \leq3\sqrt{18.382591\,V_3(A)}
 <12.87\sqrt{V_3(A)} .
\]
The remaining need for a density receiver robust to this overlapping leakage is unchanged.
