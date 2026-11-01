# Independent audit of the proposed general forest H2 sum of squares

2 October 2026. Auditor: heat_entropy. This is an audit of
`GENERAL_H2_SOS_DRAFT.md`, not a claim to have solved the complete forest
negative-correlation conjecture. The proposed theorem concerns the third
high-fugacity Rayleigh coefficient under simultaneous vanishing of the first
two coefficients. Its novelty has not been certified.

## Audit result

The coefficient normalization, weighted equality geometry, Gaussian lowering
product rule, normal-ordering reduction, and harmonic cycle-flow projection
all pass this independent analytic audit. Seven independent exact full-forest
tests pass, including cases with non-twin supports, nonconstant harmonic exit
rows inside those supports, omitted spokes, an endpoint in the common-zero
set, and adjacent marked endpoints. The exact test script is
`general_H2_mirror_stress_heat.py`; its output is the adjacent JSON file.

The resulting formula is, with the definitions in the draft,

\[
 H_2=\tau^2\operatorname{tr}(T B_e T B_f)
    =\tau^2\sum_{g,h}c_gc_h
       (\eta_{e,g}T\eta_{f,h}^T)^2\ge0.
\]

All conductances, including the two marked conductances, occur in the
Laplacian defining the Green matrix and spanning-tree weight. Marked activities
are differentiated before the common scaling is substituted. These choices
are essential to the normalization.

## 1. Independent coefficient normalization

Let the unrooted forest partition function be
\(Z(\lambda c)=\lambda^{n-1}\tau+lambda^{n-2}\tau_2+lambda^{n-3}\tau_3+\cdots\).
Derivatives with respect to activities evaluated at \(\lambda c\) equal
\(\lambda^{-1}\) times conductance derivatives of this expression. Thus

\[
 R_{ef}(\lambda c)
 =-\lambda^{-2}Z(\lambda c)^2\partial_{ef}\log Z(\lambda c).
\]

Put \(Q_2=\tau_2/\tau\), \(Q_3=\tau_3/\tau\). The coefficients of
\(\lambda^{-1}\) and \(\lambda^{-2}\) in \(\log Z\) are respectively
\(Q_2\) and \(Q_3-Q_2^2/2\). Consequently, if \(H_0=H_1=0\),

\[
 H_2/\tau^2
 =-\partial_{ef}(Q_3-Q_2^2/2).
\]

The forest-ratio formulas for \(Q_2,Q_3\) in draft section 2 have the correct
multiplicities: each non-root tree component contributes vertices minus edges,
namely one. For two non-root components, the product of these two differences
gives precisely the three displayed terms. No rooted-forest weighting remains
in the ratios.

## 2. Weighted H1 and equality geometry

Ground at \(a\). Under \(H_0=0\), the f-potential \(w\) vanishes at both
\(a,b\); the e-potential \(v\) has a common value \(k\) at \(c,d\).
The rank-one updates satisfy
\(\partial_e K=-vv^T\), \(\partial_f K=-ww^T\), and
\(\partial_{ef}K=0\) at this point. For every two-element principal minor,

\[
 \partial_{ef}\det K_{\{x,y\}}
 =(v_xw_y-v_yw_x)^2.
\]

The explicit f-edge derivative contributes
\(\partial_e\det K_{\{c,d\}}=-k^2R_f\).
The e-edge minor is zero because one endpoint is grounded. Differentiating the
displayed formula for \(Q_2\) therefore gives

\[
 -\partial_{ef}Q_2
 =\sum_g c_g(v_xw_y-v_yw_x)^2-k^2R_f.
\]

For \(j_{xy}=c_{xy}(v_xw_y-v_yw_x)\), divergence is \(-k b_f\).
Its electrical-energy inner product with the f-unit-current flow is
\(-kR_f\). Replacing \(v\) by \(v-k\) adds \(k\) times that electrical
flow, so the shifted flow energy is exactly the preceding difference. This
proves the weighted H1 formula, with the claimed positive sign.

When it vanishes, neighboring two-vectors \((v_x,w_x)\) are collinear.
Every connected component of the complement of the common-zero set has one
projective direction. If both coordinates of that direction were nonzero,
the component could contain no current source or sink: every endpoint of
either marked edge has the other potential zero. Both potentials would then
be harmonic with zero boundary values, contradicting the maximum principle.
Thus every such component has one axis direction. The two nonzero supports
are disjoint, no edge connects them, and connectivity forces a nonempty
common-zero set S. This argument does not require twin vertices.

If one marked endpoint itself belongs to S, the harmonic-row identity still
holds. In block form it is
\(P_U^T(b_e)_U=-(b_e)_S\), with identity rows for vertices in S. This is
equivalent to \(p_a=p_b\), including boundary endpoints. The script explicitly
tests this possibility.

## 3. Independent product-rule check

Use the formal Grassmann Gaussian Wick functional with covariance K; this is
determinant algebra, not a positive measure. The quadratic vertex terms and
quartic edge terms in
\(V=\sum_iq_i-\sum_{ij}c_{ij}q_iq_j\) yield
\(Q_2=\langle V\rangle\), \(Q_3=\langle V^2\rangle/2\).

For the even second-order contraction operator \(D_v\), define its cross
product term \(\Gamma_v\) by

\[
 D_v(V^2/2)=V D_vV+\Gamma_v(V,V).
\]

Every first Grassmann derivative of V contracted with v is supported on
E union S. This follows because each monomial is supported on one vertex or
one edge, and no E--F edge exists. Consequently:

* \(D_vV\) and \(\Gamma_v(V,V)\) involve only E union S variables;
* a w-contraction of either expression vanishes;
* the cross product term between V and \(D_vV\) under \(D_w\) vanishes;
* marked f explicit derivatives of these expressions vanish.

Therefore

\[
 D_wD_v(V^2/2)=(D_vV)(D_wV).
\]

The same support argument gives
\(D_v(C_fV)=C_fD_vV\), \(D_w(C_eV)=C_eD_wV\), where
\(C_e=q_aq_b\), \(C_f=q_cq_d\). The four mixed derivative terms consequently
sum to \(\langle J_eJ_f\rangle\), with
\(J_e=D_vV+C_e\), \(J_f=D_wV+C_f\).
There is no omitted cross-gradient term. Also
\(\partial_{ef}Q_2=0\). It follows that

\[
 H_2/\tau^2=-\operatorname{Cov}_{\rm Wick}(J_e,J_f).
\]

## 4. Independent normal-order and sign check

Contraction of the quartic edge term contributes the bilinear matrix
\(-c_{xy}(v_y e_x-v_x e_y)(v_y e_x-v_x e_y)^T\).
The bilinear part of the normal-ordered endpoint quartic has matrix

\[
 K_{bb}E_{aa}+K_{aa}E_{bb}-K_{ab}(E_{ab}+E_{ba}).
\]

Hence the centered bilinear matrix of \(J_e\) is \(-A_e\), with exactly the
draft's A_e. Its remaining normal-ordered quartic is supported only on a,b.
A normal-ordered degree-four term cannot pair with a normal-ordered degree-two
term: without internal contractions, one side has more barred and unbarred
fields than the other. The quartic--quartic pairing is a signed square of a
two-by-two cross-covariance determinant. Because
\(K_{a,x}=K_{b,x}\) outside E, that determinant is zero. The sign does not
matter for this vanishing.

For the surviving bilinears,
\(\operatorname{Cov}_{\rm Wick}(:\bar\psi A\psi:,:\bar\psi B\psi:)
=-\operatorname{tr}(KAKB)\).
The two minus signs in \(-A_e,-A_f\) cancel. Thus
\(H_2/\tau^2=\operatorname{tr}(KA_eKA_f)\), with the positive sign claimed.

## 5. Independent boundary projection and flow check

The cross Green block between E union S and F union S factors as
\(P_{E\cup S}T P_{F\cup S}^T\). Projection of the endpoint bilinear matrix
is \(R_e\pi_e^T\pi_e\), since \(p_a=p_b=\pi_e\). For any grounded boundary
value column z, put \(h_x=p_xz\). The flow

\[
 j_{xy}=c_{xy}(v_xh_y-v_yh_x)
\]

has divergence \(h_x(Lv)_x-v_x(Lh)_x=(\pi_ez)b_e\).
Here h is harmonic off S and v is zero on S. Subtracting
\((\pi_ez)\) times the electrical unit-current flow leaves a circulation.
Electrical current is energy-orthogonal to every circulation. Thus

\[
 z^TP^TA_ePz
 =\sum_g c_g[\eta_{e,g}z]^2=z^TB_ez.
\]

This proves \(P^TA_eP=B_e\) without a positivity assumption on A_e itself.
The same argument applies to f and yields the global formula.

## 6. Exact independent cases and limitations

The test enumerates forests of the graph with the two marked edges removed,
then tests insertion of each marked edge and their joint insertion to form
the four deletion-contraction coefficients. It computes the entire Rayleigh
polynomial from these coefficients. Separately, exact Fraction Gaussian
elimination constructs the full marked Laplacian, current potentials,
harmonic exit rows, B matrices, and trace formula. This independence is useful:
the coefficient side uses no Green function or Grassmann identity.

| Case | Vertices | Exact H2 |
|---|---:|---:|
| Mirrored path, two boundary vertices | 8 | 4608 |
| Mirrored path with internal rung | 8 | 4608 |
| One-point attachment | 8 | 0 |
| Two mirrored paths, three boundary vertices | 11 | 122683392 |
| Unequal mirrored branches with omitted spokes | 10 | 14938560000 |
| One marked endpoint in S | 6 | 0 |
| Adjacent marked endpoints | 5 | 0 |

Every case also agrees after changing the marked conductances to (2,3) and
(1/2,7/5), and after grounding at every vertex of S. The zero cases have an
identically zero full Rayleigh polynomial in these examples.

This result would establish only H2 nonnegativity on the simultaneous H0=H1=0
stratum. It does not control subsequent coefficients when H2 also vanishes.
The source paper's chain examples allow arbitrarily many leading coefficients
to vanish. No complete Kahn conjecture solution follows from this audit.
