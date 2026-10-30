SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet03, slot B02, 2026-09-24T18:25:40Z.

# fleet03/B02 r54 — weighted scalar-square Fourier gain and the exact multiplicity-seven shared-anchor collar

Run: \`20260924T182540Z-fleet03-B02-fixedmult-r54\`  
Current owner objective actually followed: \`QFORM-FIXED-MULTIPLICITY-AUDIT-20260924\`.  
Execution context: \`WITHOUT_VERIFIED_BRAIN\`.

## 1. Fresh source state

The later fixed-multiplicity objective supersedes the older B02 unstructured-three-direction assignment for this invocation while preserving the QFORM programme and all exact input quantifiers.

The complete nine-direction source remains

- repository: \`yspennstate/math-open-problems\`;
- source commit: \`eeb752c8943536541b34b42b8bf48e924f4d3d2f\`;
- path: \`proofnet24/QFORM-density/fixed-multiplicity-2026-09-24/improvements/interactive/20260924T145418Z-nine-400/paper.tex\`;
- blob: \`19fb119877426b640b2c0dae19ec2f78a399fe11\`;
- SHA-256: \`bf1caf6ae4b4bc33992f501c169b5dc6c795db757b0f6089eff9991391effdf3\`.

My preceding B02 run independently audited that source and found it mathematically PASS after the local negative-hyperbolic-tail coordinate-label repair.

There is now a later complete multiplicity-eight candidate, \`QFORM-FIXED-MULTIPLICITY-8-v1\`, at fleet03/B07, and two genuinely separate complete PASS reconstructions are already present:

1. fleet03/B08, \`audits/fleet03/B08/20260924T151825Z-fleet03-B08-s8-full-review-r59/AUDIT.md\`;
2. fleet01/B03, \`audits/fleet01/B03/20260924T154801Z-fleet01-B03-fixedmult-audit-r15/AUDIT.md\`.

I reread the complete B07 theorem, both review files, the B04 terminal-collar proof, the B17 robust-anchor extraction, the B13 independent replacement proof, and the designated fleet04/B02 overlap audit. I found no contradiction with either PASS reconstruction. Thus the repository now contains the two independent complete reviews required by the owner before treating the multiplicity-eight candidate as having met the review-count gate. I do not edit any protected release/control file here.

The reviewed multiplicity-eight statement is

\[
 s_8(A)\ge s>0
 \quad\Longrightarrow\quad
 \|p_{X^TAX+b^TX+c}\|_{\infty,\mathrm{ess}}
 <2400\,{K^2\over s},
\]

for arbitrary independent real coordinate densities bounded by \(K\), arbitrary real symmetric \(A\), and arbitrary affine terms. Global continuity is not proved by the pivot branches; the no-pivot Fourier branches are \(C_0\).

The new mathematics below pushes the structural/analytic frontier to multiplicity seven.

---

## 2. New integrated-Fourier lemma for one rough scalar square

### Theorem \`QFORM-SCALAR-SQUARE-WEIGHTED-FOURIER-v1\`

Let \(Y\) have an arbitrary real probability density \(0\le f\le1\). Let
\[
 q(y)=ay^2+by+c,\qquad a\ne0,
\]
and
\[
 \Psi(t)=\mathbb E e^{itq(Y)}.
\]
Then
\[
 \boxed{
 \int_{|t|\ge |a|^{-1}} {|\Psi(t)|\over |t|}\,dt
 \le {4\over 1-2^{-1/4}}<26.
 }
 \tag{2.1}
\]

More quantitatively, after completing the square and writing
\(\Phi(s)=\mathbb E e^{isZ^2}\) for a translate \(Z\) of \(Y\),
\[
 \boxed{
 \int_0^U|\Phi(s)|^2\,ds\le4\sqrt2\,U^{1/2},
 \qquad U\ge1.
 }
 \tag{2.2}
\]

This is an integrated estimate, not a pointwise van-der-Corput estimate. It remains valid for fragmented, phase-aligned supports.

### Proof

Translation preserves the density cap, and constants and the sign of \(a\) do not affect absolute values, so it suffices to prove the assertion for \(q(y)=y^2\). Let \(Z'\) be an independent copy of \(Z\) and
\[
 \Delta=Z^2-(Z')^2.
\]

For every fixed \(z'\) and \(r>0\), the set
\[
 \{z:|z^2-(z')^2|\le r\}
\]
has Lebesgue length at most \(2\sqrt{2r}\). Indeed, if \((z')^2\le r\), it is contained in
\([-\sqrt{(z')^2+r},\sqrt{(z')^2+r}]\), whose length is at most \(2\sqrt{2r}\). If \((z')^2>r\), its two components have total length
\[
 2\left(\sqrt{(z')^2+r}-\sqrt{(z')^2-r}\right)
 ={4r\over \sqrt{(z')^2+r}+\sqrt{(z')^2-r}}
 \le2\sqrt{2r}.
\]
Since the conditional density of \(Z\) is bounded by one,
\[
 \mathbb P(|\Delta|\le r)\le \min\{1,2\sqrt{2r}\}.
 \tag{2.3}
\]

For \(U>0\), Fubini on the bounded interval gives
\[
 I(U):=\int_0^U|\Phi(s)|^2\,ds
 =\mathbb E\,{\sin(U\Delta)\over\Delta},
\]
with the continuous value \(U\) at \(\Delta=0\). Hence
\[
 I(U)\le
 \mathbb E\min\{U,|\Delta|^{-1}\}.
\]
For \(U\ge1\), layer cake and (2.3) give
\[
 I(U)
 \le1+\int_1^U2\sqrt2\,v^{-1/2}\,dv
 =1+4\sqrt2(\sqrt U-1)
 \le4\sqrt2\,\sqrt U,
\]
which proves (2.2).

On the dyadic interval \([2^k,2^{k+1}]\), Cauchy--Schwarz gives
\[
 \int_{2^k}^{2^{k+1}}{|\Phi(s)|\over s}\,ds
 \le I(2^{k+1})^{1/2}
 \left(\int_{2^k}^{2^{k+1}}s^{-2}\,ds\right)^{1/2}
 \le2\,2^{-k/4}.
\]
Summing \(k\ge0\), and then doubling for negative \(s\),
\[
 \int_{|s|\ge1}{|\Phi(s)|\over|s|}\,ds
 \le {4\over1-2^{-1/4}}.
\]
The change of variables \(s=|a|t\) proves (2.1). Finally,
\[
 {4\over1-2^{-1/4}}<26
\]
because \(2^{-1/4}<11/13\), equivalent after taking fourth powers to
\(13^4<2\cdot11^4\), i.e. \(28561<29282\). QED.

### Why this matters

The live source correction says cap-one densities do not give a uniform pointwise quadratic-phase decay because fragmented supports can phase-align. The theorem above shows that the exact weighted quantity needed to upgrade a critical \(1/|t|\) rank-two Fourier tail is nevertheless uniformly summable.

It also shows why an amplitude-free vector-valued extension is impossible: if one allowed an arbitrary measurable amplitude \(G_t(y)\) with \(|G_t(y)|\le1\), taking \(G_t(y)=e^{-itq(y)}\) cancels all scalar oscillation. Any shared-anchor extension must exploit the actual product/quadratic structure of the amplitude, not only its modulus.

---

## 3. A complete separated \(2+1\) Fourier-\(L^1\) receiver

### Theorem \`QFORM-SEPARATED-RANK2-PLUS-SQUARE-L1-v1\`

Let \(U=(U_1,U_2)\), \(V=(V_1,V_2)\), \(H\), and \(Z\) be disjoint blocks of original independent coordinates. Assume all one-dimensional densities are bounded by one. Conditional on \(Z=z\), suppose
\[
 Q=
 F_z(U)+G_z(V)+2U^TBV+aH^2+b_zH+c_z,
 \tag{3.1}
\]
where \(B\) is a fixed invertible \(2\times2\) real matrix, \(a\ne0\), and \(F_z,G_z\) are arbitrary measurable real phases. Then
\[
 \boxed{
 \int_{\mathbb R}|\phi_Q(t)|\,dt
 \le {2\over|a|}
 +{4\pi\over1-2^{-1/4}}\,|\det B|^{-1/2}
 <{2\over|a|}+26\pi|\det B|^{-1/2}.
 }
 \tag{3.2}
\]
Consequently \(Q\) has a continuous \(C_0\) density and
\[
 \boxed{
 \|p_Q\|_\infty
 \le {1\over\pi|a|}
 +{2\over1-2^{-1/4}}\,|\det B|^{-1/2}
 <{1\over\pi|a|}+13|\det B|^{-1/2}.
 }
 \tag{3.3}
\]

### Proof

For fixed \(z,t\), put
\[
 a_t(u)=f_U(u)e^{itF_z(u)},\qquad
 b_t(v)=f_V(v)e^{itG_z(v)}.
\]
Since the two-dimensional product densities are pointwise at most one and have mass one,
\[
 \|a_t\|_2,\|b_t\|_2\le1.
\]
With the convention \(\widehat a(\xi)=\int e^{i\xi\cdot u}a(u)\,du\),
Plancherel gives \(\|\widehat a_t\|_2\le2\pi\). Therefore
\[
 \begin{aligned}
 \left|\mathbb E_{U,V}e^{it(F_z(U)+G_z(V)+2U^TBV)}\right|
 &\le \|b_t\|_2
 \left(\int_{\mathbb R^2}|\widehat a_t(2tBv)|^2\,dv\right)^{1/2}\\
 &\le {\pi\over |t|\sqrt{|\det B|}}.
 \end{aligned}
 \tag{3.4}
\]
The \(H\)-factor is independent of \(U,V\) given \(Z=z\). Thus for \(|t|\ge|a|^{-1}\), multiply (3.4) by the scalar-square factor and apply (2.1). For \(|t|<|a|^{-1}\), use \(|\phi|\le1\). The resulting bound is uniform in \(z\), so Tonelli/conditioning gives (3.2). Fourier inversion gives the \(C_0\) density and (3.3). QED.

This receiver is deliberately stated only for genuine source separation. It does not silently convert a shared physical coordinate into an independent copy.

---

## 4. Designated fleet04/B02 result applied: exact multiplicity-seven same-seed collar

The designated current partner result is fleet04/B02's scoped overlap audit:

\`proofnet24/QFORM-density/fixed-multiplicity-2026-09-24/audits/fleet04/B02/20260924T161206Z-fleet04-B02-nine400-overlap-audit-r1/REPORT.md\`.

It proves, for an order-two volume-sampled physical seed \(B=A[S,T]\), with \(L=(S\cup T)^c\) and interpolation
\[
 P=A[:,T]B^{-1}A[S,:],
\]
a completion \(A=D+R+E\) in which \(D\) is diagonal on \(L\), \(E\) is zero-diagonal on \(L\), \(\operatorname{rank}R\le6\), \(\operatorname{rank}R[L,L]\le2\), and one may choose the same seed with
\[
 \|E\|_F^2\le9\,{V_3(A)\over V_2(A)}.
 \tag{4.1}
\]

The partner applied this at \(s_8\). Applying its completed same-seed estimate to the actual \(s_7\) inequality gives the following new structural theorem.

### Theorem \`QFORM-S7-SAMESEED-SHAREDANCHOR-COLLAR-v1\`

Use
\[
 \eta={1\over100},\qquad \kappa={1\over6400}.
\]
Let \(A=A^T\) satisfy \(s_7(A)\ge1\) and have no \(\eta\)-pivot (no physical scalar \(|A_{ii}|\ge\eta\) and no physical principal \(2\times2\) determinant of modulus at least \(\eta\)). Then either

1. \(V_3(A)\ge\kappa^3\), hence the completed order-three receiver gives
   \[
   \|p_Q\|_\infty<2400
   \]
   and a continuous \(C_0\) density; or

2. there are disjoint physical two-sets \(S,T\), an index \(h\notin S\cup T\), and the same interpolation seed \(B=A[S,T]\) such that, with \(\rho=V_3/V_2<\kappa\),
   \[
   \boxed{\|E\|_F\le3\sqrt\rho<{3\over80},}
   \tag{4.2}
   \]
   \[
   \boxed{|D_{hh}|\ge1-3\sqrt\rho>{77\over80},}
   \tag{4.3}
   \]
   \[
   \boxed{|P_{hh}|>{381\over400},}
   \tag{4.4}
   \]
   and the literal overlap-one bordered minor obeys
   \[
   \boxed{
   |\det A[S\cup\{h\},T\cup\{h\}]|
   >{77\over80}\,|\det A[S,T]|.
   }
   \tag{4.5}
   \]

### Proof

First \(V_1\ge\kappa\). Otherwise
\[
 \|A\|\le\|\operatorname{diag}A\|+\|\operatorname{off}A\|_F
 <{1\over100}+{1\over80}={9\over400}<1,
\]
contrary to \(s_7(A)\ge1\).

Next \(V_2\ge\kappa V_1\). If \(V_2<\kappa V_1\), the order-one sampled interpolation gives a completion with
\[
 \|E\|_F<{1\over40},\qquad \operatorname{rank}R\le3,\qquad
 \operatorname{rank}R[L,L]\le1.
\]
Then
\[
 s_7(D+R)\ge{39\over40},
\]
so rank perturbation forces \(s_4(D)\ge39/40\). Pick two of the resulting large diagonal entries. Since \(E\) is zero diagonal,
\[
 |R_{ii}|>{39\over40}-{1\over100}={193\over200},
\]
while, for \(i\ne j\),
\[
 |R_{ij}|<{\sqrt{101}\over100}+{1\over40}< {27\over200}.
\]
The corresponding \(2\times2\) restricted block is strictly row-diagonally dominant and hence invertible, contradicting restricted rank at most one. Therefore
\[
 V_2\ge\kappa V_1\ge\kappa^2.
 \tag{4.6}
\]

If \(V_3\ge\kappa V_2\), then \(V_3\ge\kappa^3\) and branch 1 follows exactly as in the multiplicity-eight proof. Otherwise put
\[
 \rho={V_3\over V_2}<\kappa.
\]

Now apply the completed fleet04/B02 same-seed estimate (4.1). For that seed,
\[
 \epsilon:=\|E\|\le\|E\|_F\le3\sqrt\rho<{3\over80}.
\]
Since \(A-E=D+R\),
\[
 s_7(D+R)\ge1-\epsilon.
\]
The global rank bound \(\operatorname{rank}R\le6\) yields
\[
 s_1(D)\ge s_7(D+R)\ge1-\epsilon.
\]
Thus some \(h\in L\) obeys (4.3). By construction
\[
 D_{hh}=A_{hh}-P_{hh}.
\]
The no-scalar-pivot condition gives \(|A_{hh}|<1/100\), so
\[
 |P_{hh}|
 \ge |D_{hh}|-|A_{hh}|
 >{77\over80}-{1\over100}
 ={381\over400},
\]
proving (4.4). Finally the exact bordered-determinant identity is
\[
 \det A[S\cup\{h\},T\cup\{h\}]
 =\det(B)\,(A_{hh}-P_{hh})
 =\det(B)D_{hh},
\]
which gives (4.5). QED.

This is an equation-level application of the designated fleet04/B02 result to a new threshold, not merely a citation.

---

## 5. Exact remaining analytic obstruction at multiplicity seven

All physical pivot branches already close under \(s_7(A)\ge1\): a scalar pivot loses at most one spectral direction and leaves at least six, more than the five-direction full-half-potential receiver needs; a two-coordinate pivot leaves at least five, while the definite branch is direct and the indefinite logarithmic branch needs only one surviving spectral direction.

Thus the only new no-pivot obstruction at seven is branch 2 of Theorem 4.

The new weighted-Fourier theorem explains exactly what would close it. If the large coefficient \(D_{hh}\) in (4.3) could be realized as a genuinely separated scalar square while the two-seed supplied the critical rank-two \(1/|t|\) Fourier factor, Theorem 3 would make the characteristic function integrable without any pointwise quadratic-phase estimate.

But the source coordinate \(h\) occurs on both the row and column sides of the bordered minor. The interpolation identity \(D_{hh}=A_{hh}-P_{hh}\) is coefficient algebra; it is not a product-preserving change of random variables. In the actual conditional Fourier integral, the amplitude seen by \(X_h\) depends on \(t\) and on \(X_h\) through its couplings to the seed banks. Replacing that amplitude by an arbitrary modulus-one function is invalid, and in fact no amplitude-agnostic extension of (2.1) can hold, since \(G_t(h)=e^{-itq(h)}\) cancels the scalar oscillation completely.

Therefore the next exact B02 obligation is:

> prove a structure-sensitive shared-anchor analogue of Theorem 3 for the same-seed collar (4.2)--(4.5), retaining the original-coordinate dependence created by \(P_{hh}=A[h,T]B^{-1}A[S,h]\); or produce a source-valid counterexample to that structured receiver and switch to direct small-ball/coarea on the same collar.

Small interpolation error alone may not be discarded: the rough input laws have unbounded support, so coefficient-small quadratic terms are not uniformly phase-small.

---

## 6. Status

- multiplicity 9: proved source and independently audited; B02 has a sharper candidate constant from the preceding run;
- multiplicity 8: complete candidate \(<2400K^2/s\), with two separate complete PASS reviews now present (B08 and B03); this run found no contradiction in the reviewed chain;
- multiplicity 7: **OPEN**, but reduced here to the explicit same-seed shared-anchor collar (4.2)--(4.5);
- unrestricted multiplicity 3: **OPEN / not proved / not disproved**;
- global continuity: **OPEN**; the Fourier \(V_3\) branches are \(C_0\), while full pivot assemblies are currently recorded only as essentially bounded.

No post-rotation independence, moment, bounded-support, Gaussian, log-concavity, connected-support, interval-extremality, arbitrary-joint coarea, or law-uniform pointwise quadratic-phase decay is used.
