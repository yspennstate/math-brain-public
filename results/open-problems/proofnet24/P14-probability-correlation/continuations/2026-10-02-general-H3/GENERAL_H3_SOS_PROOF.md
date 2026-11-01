# A general electrical sum of squares for the fourth forest Rayleigh coefficient

Research continuation, 2 October 2026. This note proves a partial result on the forest negative-correlation conjecture. The proof has undergone three independent internal analytic audits and exact checks on nine graph families. Historical novelty and external peer review are not certified. The exploratory derivation is preserved in [H3_CONDITIONAL_WARD_DRAFT.md](H3_CONDITIONAL_WARD_DRAFT.md).

## Theorem and complete notation

Let G be a connected finite loopless graph on n vertices with positive edge conductances c_g. Let e=ab and f=cd be distinct non-bridge edges, oriented arbitrarily. Define

\[
 Z(\mathbf z)=\sum_{F\subseteq E(G)\,\mathrm{acyclic}}\prod_{g\in F}z_g,
 \qquad \mathcal R_{ef}=(\partial_eZ)(\partial_fZ)-Z\partial_{ef}Z.
\]

Take the marked derivatives before specializing z_g=\lambda c_g. In the proof, \partial_e and \partial_f applied to harmonic or conditional data denote derivatives with respect to c_e and c_f; the activity conversion is explicit in Section 5. Write

\[
 \mathcal R_{ef}(\lambda\mathbf c)
 =H_0\lambda^{2n-4}+H_1\lambda^{2n-5}
      +H_2\lambda^{2n-6}+H_3\lambda^{2n-7}
      +O(\lambda^{2n-8}).
\]

**If H_0=H_1=H_2=0, then H_3\geq0.** Its precise sum of squares is given below.

Let L be the conductance Laplacian and \tau the weighted spanning-tree sum. Under H_0=H_1=0, the electrical equality geometry gives special unit-current potentials v,w with

\[
 Lv=b_e,\quad Lw=b_f,\qquad
 v(c)=v(d)=0,\quad w(a)=w(b)=0.
\]

Their nonzero supports E and F are disjoint and no graph edge joins them. Put S={x:v(x)=w(x)=0}; it is nonempty. These facts and the first conditional-score identity used below are proved in the companion [GENERAL_H2_SOS_PROOF.md](../2026-10-02-general-H2/GENERAL_H2_SOS_PROOF.md), which also includes the weighted extension of the previously known equality geometry.

Choose a root r\in S. Write B=S\setminus\{r\}, U=E\cup F, and K=L_r^{-1}, extended by a zero row and column at r. Define harmonic boundary rows p_x and the boundary Green matrix T by

\[
 P_U=-L_{UU}^{-1}L_{UB},\qquad
 p_s=\mathbf e_s^T\ (s\in B),\qquad p_r=0,
 \qquad T=K_{B,B}.
\]

The endpoint rows obey p_a=p_b=: \pi_e and p_c=p_d=: \pi_f. For each oriented original edge g=xy, let

\[
\begin{aligned}
 \eta_{e,g}&=v(x)p_y-v(y)p_x-(v(x)-v(y))\pi_e,\\
 \eta_{f,g}&=w(x)p_y-w(y)p_x-(w(x)-w(y))\pi_f.
\end{aligned}
\]

The response matrices and previous coefficient are

\[
 B_e=\sum_g c_g\eta_{e,g}^{T}\eta_{e,g},\qquad
 B_f=\sum_h c_h\eta_{f,h}^{T}\eta_{f,h},\qquad
 H_2=\tau^2\sum_{g,h}c_gc_h
          (\eta_{e,g}T\eta_{f,h}^{T})^2.
\]

Let A=N(E)\cap S and D=N(F)\cap S be the two port sets. Define auxiliary potentials

\[
 a_g(x)=p_xT\eta_{e,g}^{T},\qquad
 b_h(x)=p_xT\eta_{f,h}^{T}.
\]

The vanishing H_2 condition implies that a_g is constant on D\cup F, while b_h is constant on A\cup E. Subtract these respective constants to form \alpha_g,\beta_h, so

\[
 \alpha_g|_{D\cup F}=0,\qquad \beta_h|_{A\cup E}=0.
\]

Then

\[
 \boxed{
 H_3=\tau^2\sum_{g,h,k\in E(G)}c_gc_hc_k
  \bigl[\alpha_g(x_k)\beta_h(y_k)
        -\alpha_g(y_k)\beta_h(x_k)\bigr]^2.
 }\tag{T}
\]

All three sums use the original graph edges. The response rows use unit currents, so the displayed factors c_g,c_h,c_k are complete: no c_e or c_f factors occur. Orientations change only signs inside squares. The shifted auxiliary potentials are independent of the root chosen in S.

If the displayed expression is positive, e and f are strictly negatively correlated under the weighted forest measure for all sufficiently large \lambda. If it vanishes, this theorem gives no sign for any later coefficient. It therefore does not resolve the general forest conjecture or every high-fugacity case.

The proof below evaluates (T) at a convenient root. The ungrounded response charges are zero-sum and root-independent; shifting their potentials to vanish at the opposite ports makes (T) invariant under every allowed root choice.

## 1. Port support and the response kernel

To make grounding transparent, first use full harmonic rows p*_x on all of S, including the identity row at every s in S. For x in E or F, these are the Dirichlet harmonic-extension rows. Their entries sum to one. The grounded rows are obtained by deleting the root coordinate and setting its field to zero. Define full response rows by the same eta formula with p* in place of p. Their coordinates sum to zero. Their only possible support is A for the e response, and D for the f response. Indeed every nonzero term involving v belongs to an E–E or E–S edge, and all harmonic rows there are supported on A; similarly for F.

Let B_e*=sum_g c_g eta*_(e,g)^T eta*_(e,g) be the full response matrix on S. For arbitrary real boundary values z, let h be their harmonic extension and let pi_e z be the common marked-endpoint value. Then z^T B_e* z vanishes exactly when z is constant on A.

The forward direction follows from every E–S edge xs: its eta evaluation is v(x)(h(s)-pi_e z). Since v(x) is nonzero, vanishing of every response forces h(s)=pi_e z for every port s in A. Conversely, if z is constant on A, the maximum principle makes its harmonic extension constant throughout E, with that same endpoint value; every eta evaluation vanishes. Values outside A are immaterial. Thus

    range(B_e*)=the full zero-sum contrast space on A,
    range(B_f*)=the full zero-sum contrast space on D.       (1)

This is a kernel statement, not an assertion that either matrix has nonpositive off-diagonal entries. The proof does not require an auxiliary positive-weight graph representation of B_e or B_f.

The H2 sum of squares implies every e response and f response is orthogonal in the boundary Green inner product. By (1), every A contrast is orthogonal to every D contrast. Hence A and D cannot have two distinct vertices in common: their shared difference vector would have strictly positive Green norm but would be orthogonal to itself.

If either port set is a singleton, ground at that port. The corresponding entire conditional marked score is constant in the remaining boundary fields, so all mixed coefficients vanish; its response rows and formula (T) are zero. Equivalently this is the familiar forest-block factorization at a one-vertex interface. It therefore suffices to consider |A|,|D|>=2. In that case choose

    r in A minus D.                                       (2)

For this root the grounded e response matrix is positive definite on A minus {r}. H2=0 forces every f auxiliary potential b_h to vanish on A, and harmonicity forces it to vanish on E. The f kernel similarly forces each e auxiliary potential a_g to be constant on D and F. Write its constant as k_g. Thus for this calculation

    beta_h=b_h, alpha_g=a_g-k_g.                          (3)

The full physical source of a_g is the lifted zero-sum row eta*_(e,g), supported on A; that of b_h is eta*_(f,h), supported on D. Lifting restores the root coordinate as minus the sum of the remaining coordinates. Because r is not in D, each f charge already has total sum zero in its ungrounded coordinates.

## 2. Forest generating function and Berezin convention

Use left Grassmann derivatives throughout. Write q_i=barpsi_i*psi_i, with the root field fixed to zero. Normalize Berezin integration so that

    integral exp(+barpsi L_r psi)=det(L_r),
    <product_(i in I) q_i>=det(K_(I,I)).

The positive Gaussian exponent is essential for the covariance signs below. Define

    V=sum_(i!=r) q_i-sum_(xy in edges) c_xy*q_x*q_y.

Then the exact normalized forest expansion is

    F(t):=sum_(j>=0) (tau_(j+1)/tau)*t^j=<exp(tV)>,
    t=1/lambda.                                          (4)

One can verify (4) by the same Euler-feature argument used for Q2,Q3 in the H2 note. In a (j+1)-component forest, each non-root component chooses either a vertex, with sign +, or an edge, with sign −. Removing the chosen edges creates the rooted forests counted by principal Green minors. Each non-root component has net multiplicity |vertices|-|edges|=1. Distinct selected roots force chosen edge endpoints and chosen vertices to be disjoint, exactly as Grassmann nilpotence does. Thus every forest has net multiplicity one. In particular Q4=<V³>/6; this is not a new unproved identification of a fourth coefficient.

Partition V into V_E+V_F+V_S exactly as in the H2 note. Conditional Gaussian elimination gives

    M_E(t)=<exp(tV_E)|boundary>_E,
    M_F(t)=<exp(tV_F)|boundary>_F,
    F(t)=<exp(tV_S)*M_E(t)*M_F(t)>_B.                     (5)

The harmonic rows and boundary covariance remain fixed under either marked conductance variation. Only M_E depends on c_e and only M_F on c_f. Put

    U_e(t)=partial_e log M_E(t)=t*u_e1+t²*u_e2+O(t³),
    U_f(t)=partial_f log M_F(t)=t*u_f1+t²*u_f2+O(t³).

The already proved H2 calculation gives

    u_e1=constant+barpsi B_e psi,
    u_f1=constant+barpsi B_f psi,
    B_e=sum_g c_g eta_(e,g)^T eta_(e,g),
    B_f=sum_h c_h eta_(f,h)^T eta_(f,h).                  (6)

Also u_e2=partial_e[<V_E²>_E-<V_E>_E²]/2, and similarly for f. No claim that this second score is supported only on the contrast response space is made. It can contain quartics, and their contribution is indispensable.

## 3. Exact marked-score Ward identity

For a pair of vertices define the deformed edge polynomial

    F_xy(t)=(barpsi_x-barpsi_y)(psi_x-psi_y)-t*q_x*q_y.

The odd vector fields

    Qpsi_t=sum_i (1-t*q_i)*partial_(psi_i),
    Qbar_t=sum_i (1-t*q_i)*partial_(barpsi_i)

annihilate every F_xy(t) when their sum includes both endpoints. This follows by a direct left-derivative calculation. For example partial_(psi_i)q_i=-barpsi_i; the t correction from the quadratic difference cancels the derivative of -t*q_x*q_y.

Consider the raw local F integral before conditioning:

    I_F(t;psi_D)=integral_(interior F)
          product_(i in F)(1+t*q_i)
          exp(sum_(edges incident F) c_xy*F_xy(t)).       (7)

Every port in D is a genuine variable here; by (2), the grounded root is not in D. The edge sum is annihilated by Qpsi_(F union D), so applying Qpsi_D to the integrand is the negative of applying Qpsi_F to its edge exponential. Interior integration by parts gives zero:

    product_(i in F)(1+t*q_i)*(1-t*q_j)
       =product_(i in F minus {j})(1+t*q_i),

which is independent of psi_j. The integral of its product with partial_(psi_j) of the edge exponential is zero. Hence Qpsi_D I_F=0. The bar identity is identical. The weighted vertex measure is precisely what makes the interior divergence vanish.

At t=0, Gaussian elimination gives

    I_F(0;psi_D)=det(L_FF)*exp(barpsi_D N_F psi_D),

where N_F is the contribution of this local subgraph to the boundary Schur complement. The conditional Gaussian normalization yields exactly

    M_F(t)=I_F(t)/I_F(0).

Varying c_f leaves N_F fixed: every harmonic extension has equal values at the marked endpoints, so its Dirichlet energy and Schur complement are unchanged. Therefore

    U_f(t)=partial_f log I_F(t)-partial_f log det(L_FF).

The subtracted term is a boundary-field constant. Since the Ward operators do not depend on c_f, the complete marked score U_f satisfies the exact identities

    Qpsi_D U_f(t)=Qbar_D U_f(t)=0.                    (8)

This argument does not falsely claim that the entire normalized local partition M_F is invariant: its Gaussian boundary normalizer may not be. The marked derivative of that normalizer is constant, and this is the needed cancellation.

## 4. Ward identity for the second-score constant-mode contraction

Write Dpsi=sum_(i in D) partial_(psi_i) and Dbar=sum_(i in D) partial_(barpsi_i). At orders t and t², (8) gives

    Dpsi u_f1=0,
    Dpsi u_f2=sum_(i in D) q_i*partial_(psi_i)u_f1.

Since B_f has zero row and column sums on D, applying Dbar to the second identity gives

    Dbar Dpsi u_f2=barpsi B_f psi.                     (9)

To fix its sign explicitly, partial_(psi_i)(barpsi B_f psi)=-sum_j barpsi_j(B_f)_(ji). Differentiating q_i contributes -psi_i*sum_j barpsi_j(B_f)_(ji), which after reordering equals the bilinear. The other term vanishes by the zero column sums. Constants in u_f1 contribute nothing.

Define the constant-covariance contraction operator

    D1=-Dbar Dpsi.

For every boundary polynomial P, Gaussian Wick differentiation in the rank-one covariance direction J=1*1^T is

    d/ds <P>_(T+sJ)|_(s=0)=<D1 P>_T.                 (10)

It follows by introducing one auxiliary Grassmann pair with covariance s and adding it identically to every port field, or directly by differentiating the Wick minors. For example D1*q_i=1 and D1*(q_i*q_j)=q_i+q_j-barpsi_i psi_j-barpsi_j psi_i; these reproduce the derivatives of the one- and two-pair determinants. Equations(9),(10) give

    <D1 u_f2>=-tr(T B_f).                             (11)

The root restriction in this step is genuine: applying a uniform Ward operator through a fixed zero root field would be invalid. Choice(2) eliminates that issue.

## 5. Cumulant expansion and activity normalization

The logarithmic marked cross derivative of (5) is the covariance of U_e,U_f in the tilted boundary Wick functional. Its first tilted density coefficient is

    W1=V_S+<V_E|boundary>_E+<V_F|boundary>_F.

Thus the coefficient of t³ in partial_ef log F is

    Cov(u_e2,u_f1)+Cov(u_e1,u_f2)
         +Cum(u_e1,u_f1,W1).                          (12)

The conductance-to-activity factors are

    R_ef(lambda*c)
      =-lambda^(2n-4)*tau²*F(t)²
            *partial_ef[log tau+log F(t)].

H0=0 removes partial_ef log tau. Under the equality geometry, the t coefficient is zero. H2=0 removes the t² coefficient. Therefore the multiplier F(t)² makes no additional contribution at t³ and

    H3/tau²=minus the expression in(12).              (13)

No factorial is missing: u_e2,u_f2 are coefficients of t² in the logarithmic scores, and the first tilt contributes its ordinary third joint cumulant. Equivalently this is -partial_ef(Q4-Q2*Q3+Q2³/3) after the lower coefficients vanish.

## 6. Evaluate the two second-score covariance terms

For a bilinear q(a)=barpsi a^T a psi, Wick differentiation gives

    Cov(q(a),P)=d/ds <P>_((T^-1+s*a^T*a)^-1)|_0.

Its covariance variation is -T*a^T*a*T. The polynomial u_e2 is supported only on A (with the root field omitted), because every harmonic row in E and every E edge uses only those ports. Every f response potential vanishes on A. Hence its induced covariance variation restricted to A is zero, and

    Cov(u_e2,u_f1)=0.                                 (14)

Each e response potential a_g is constant k_g on D. Its induced covariance change on D is therefore -k_g²*J. Applying(10),(11), and decomposing B_e as in(6), gives

    Cov(u_e1,u_f2)
       =sum_g c_g*k_g²*tr(T B_f)
       =sum_(g,h) c_g*c_h*k_g²*R_h,                  (15)

where R_h=eta_(f,h)*T*eta_(f,h)^T is the energy of b_h. This is the nonzero second-score correction that a false literal contrast-span argument would miss.

## 7. Evaluate the tilted triple cumulant

Constants drop from third cumulants. The bilinear part of W1 also contributes zero. Indeed the Gaussian third cumulant of bilinears B_e,B_f,C is the sum of the two cyclic traces; after whitening by T, H2=0 means the positive-semidefinite matrices T^(1/2)B_eT^(1/2) and T^(1/2)B_fT^(1/2) have product zero, so both traces vanish.

The quartic part of W1 is exactly

    -sum_(xy in original edges) c_xy*q(p_x)*q(p_y),

because conditional contraction of the original quartic has this uncontracted degree-four boundary term. For two response rows a,b with a*T*b^T=0, the determinant Wick rule gives

    Cum(q(a),q(b),q(x)*q(y))
       =[(x*T*a^T)(y*T*b^T)
            -(y*T*a^T)(x*T*b^T)]².                  (16)

For verification, write the four-vector Gram determinant in a block with upper diagonal entries aTa,bTb and cross inner product zero. In the third-cumulant combination, its constant terms and the terms involving only one response cancel; the remaining determinant correction is precisely the displayed wedge square. This also fixes its positive sign.

Using(16) and the conductance decompositions of B_e,B_f gives

    Cum(u_e1,u_f1,W1)
      =-sum_(g,h,k) c_g*c_h*c_k
          [a_g(x_k)*b_h(y_k)-a_g(y_k)*b_h(x_k)]².     (17)

## 8. Electrical completion for arbitrary multiport source charges

Fix g,h. Write a=a_g, b=b_h, k=k_g. Their physical Laplacian charges are supported on A and D, respectively; b vanishes on A, and a equals k on D. Put

    j_xy=c_xy*(a_x*b_y-a_y*b_x),
    i_xy=c_xy*(b_x-b_y).

Their divergences are

    div j=b*(La)-a*(Lb)=-k*(Lb),
    div i=Lb.

The electrical flow i has energy R_h. Discrete integration by parts gives its energy inner product with j as

    <j,i>_energy=sum_x b_x*(div j)_x=-k*R_h.

Consequently j+k*i is a circulation and

    sum_edges c_xy*[a_x*b_y-a_y*b_x]²-k²*R_h
       =sum_edges c_xy*[(a_x-k)*b_y-(a_y-k)*b_x]².    (18)

This calculation uses general zero-sum multiport charges, not a unit dipole assumption. Equivalently it follows directly by expanding the shifted wedge and applying the same Laplacian integration by parts.

Combining(13)--(18) proves exactly (T), with alpha=a-k and beta=b under the convenient root. The full lifted response charges are independent of grounding and determine potentials up to additive constants. Their opposite-port shifts remove those constants; thus(T) is root-independent.

## 9. Prior art, verification, and the remaining boundary

The transfer-current formula for H_0 is classical. R. Altar Çiçeksiz and Mohan Ravichandran, *Negative Correlation for Forests and the q<1 Random-Cluster Model*, arXiv:2610.00549v1, 30 September 2026, [primary preprint](https://arxiv.org/html/2610.00549v1), establish the H_1 electrical sum of squares and its equipotential equality decomposition (Theorem 1.5 and Theorem 4.8). This note starts after those two coefficients and the companion H_2 coefficient vanish. It does not assert priority over unreviewed or subsequently published work.

The forest Grassmann representation is classical: Sergio Caracciolo, Jesper Lykke Jacobsen, Hubert Saleur, Alan D. Sokal, and Andrea Sportiello, *Fermionic field theory for trees and forests*, Physical Review Letters 93 (2004), 080601, [doi:10.1103/PhysRevLett.93.080601](https://doi.org/10.1103/PhysRevLett.93.080601), [arXiv:cond-mat/0403271v2](https://arxiv.org/abs/cond-mat/0403271v2). Section 2 gives the feature-counting justification needed here, so the fourth-coefficient identification is independently explicit.

Three separate derivations have checked the conditional normalization, grounding, Berezin signs, second-score contraction, fourth-order forest identity, activity powers, and the arbitrary-multiport electrical completion:

- [H3_ROOT_INDEPENDENT_DERIVATION.md](H3_ROOT_INDEPENDENT_DERIVATION.md).
- [H3_INDEPENDENT_AUDIT.md](H3_INDEPENDENT_AUDIT.md).
- [GENERAL_H3_AUDIT_HEAT.md](GENERAL_H3_AUDIT_HEAT.md), together with [H3_WARD_IDENTITY_HEAT.md](H3_WARD_IDENTITY_HEAT.md).

The independent exact forest enumeration or connectivity-DP checks are:

| Check | Algebraic feature | Exact output |
|---|---|---|
| [H3_response_wedge_heat.py](H3_response_wedge_heat.py) | Seven cases, including positive H_3 and H_3=0, varied ports, non-twin supports, and root/marked-weight variants | [H3_response_wedge_heat.json](H3_response_wedge_heat.json) |
| [H3_non_M_matrix_audit.py](H3_non_M_matrix_audit.py) | 11 vertices, 24 unmarked edges, positive off-diagonal response entry; H_3=83106928972800000 | [H3_non_M_matrix_audit.json](H3_non_M_matrix_audit.json) |
| [H3_positive_offdiag_audit_heat.py](H3_positive_offdiag_audit_heat.py) | Independent 11-vertex, 29-unmarked-edge example and frontier-DP route; H_3=42689908537165440000 | [H3_positive_offdiag_audit_heat.json](H3_positive_offdiag_audit_heat.json) |

These checks validate finite examples and normalization; they do not replace the general proof. In particular, neither response matrix needs to be an M-matrix. The second score can contain indispensable quartic terms, and H_2=0 does not imply independence.

The companion [GENERAL_H3_ZERO_GEOMETRY_LEMMA.md](GENERAL_H3_ZERO_GEOMETRY_LEMMA.md) derives an additional separation of aggregate shifted-response supports when H_3=0. That lemma does not provide a recursion for H_4. Chains of K_4 blocks in the primary preprint have arbitrarily long strings of leading zero coefficients, so the present finite extension cannot by itself establish an all-orders result.

No conclusion here proves the forest negative-correlation conjecture at arbitrary fugacity, negative association, or the q<1 random-cluster conjecture. The all-orders generating identity (4) is a combinatorial representation, not an all-orders positivity theorem.
