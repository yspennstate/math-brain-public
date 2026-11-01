# Independent conditional-Gaussian proof of the proposed third-coefficient SOS

Independent audit, 2 October 2026. This note proves the proposed coefficient
formula by a route that does not use the mixed Grassmann lowering-operator
product rule or normal ordering. It does not prove full forest negative
correlation, does not certify novelty, and makes no claim that H2 is positive
in every non-independent case.

## Verdict

The formula in `GENERAL_H2_SOS_DRAFT.md` is mathematically consistent and has an
independent proof below. Its normalization has also passed six independent
exact subset enumerations, including non-twin current supports and a boundary
of dimension two. The weighted H1 identity and its equality classification
have been checked separately in Section 6.

The theorem proved is precisely: if the two highest Rayleigh coefficients
H0,H1 vanish, then

\[
 H_2=\tau^2\operatorname{tr}(TB_eTB_f)
     =\tau^2\sum_{g,h}c_gc_h
          (\eta_{e,g}T\eta_{f,h}^{\mathsf T})^2\ge0,
\]

with the exact definitions in the draft. Vanishing of this new expression
remains a real gap to any general high-fugacity or all-fugacity result.

## 1. Forest coefficient normalization

Let tau_k be the weighted sum of unrooted spanning forests with k components,
and let tau=tau_1. At activities lambda*c,

\[
 Z=\lambda^{n-1}\tau
    (1+\lambda^{-1}Q_2+\lambda^{-2}Q_3+\cdots),
 \qquad Q_2=\tau_2/\tau,\quad Q_3=\tau_3/\tau.
\]

An activity derivative is lambda^{-1} times a conductance derivative. Since
the Rayleigh difference is minus Z squared times the mixed second derivative
of log Z, if H0=H1=0 its third coefficient is

\[
 H_2/\tau^2=Q_{2,e}Q_{2,f}-Q_{3,ef}.
\]

There are no factors c_e or c_f in this identity. Such factors belong to the
covariance of edge indicators, not to the polynomial Rayleigh difference.

Ground r and put K=L_r^{-1}. The all-minors matrix-tree theorem gives

\[
 Q_2=\sum_iK_{ii}-\sum_{ij}c_{ij}\det K_{\{i,j\}},
\]

and

\[
 Q_3=\sum_{i<j}\det K_{\{i,j\}}
 -\sum_{ij}c_{ij}\sum_{k\ne i,j}\det K_{\{i,j,k\}}
 +\sum_{\substack{ij<kl\\\{i,j\}\cap\{k,l\}=\varnothing}}
       c_{ij}c_{kl}\det K_{\{i,j,k,l\}}.
\]

All vertices and edges here exclude the ground. The vertex-minus-edge counts
in each non-root tree component are one, which proves these identities.
For Grassmann variables q_i=bar(psi_i)*psi_i and normalized Wick covariance K,
define V=sum_i q_i-sum_{ij}c_ij q_iq_j. These two explicit determinant identities
are equivalently Q2=<V>, Q3=<V^2>/2. No all-orders Grassmann forest theorem is
needed for this proof.

## 2. Conditional Gaussian factorization and invariance

Use the equality geometry from Section 6. Let E and F be the respective
nonzero supports of the special unit-current potentials v and w, and let S
be their common zero set. There are no E-F edges. Remove the grounded root r
from S and write S0=S minus {r}.

In the grounded Laplacian, the E,F interior blocks are separate. Eliminating
them gives the boundary Schur complement J and covariance T=J^{-1}. Write
p_x for the harmonic extension row from S0 to x, with p_s the corresponding
identity row and p_r=0. Conditional Gaussian substitution is

\[
 \psi_x=p_x\psi_{S0}+\xi_x,\qquad
 \bar\psi_x=\bar\psi_{S0}p_x^{\mathsf T}+\bar\xi_x.
\]

The E and F residual Grassmann families are independent, independent of the
boundary family, with covariances L_EE^{-1},L_FF^{-1}. This is ordinary block
Gaussian elimination as a determinant/Wick identity.

The equation Lv=b_e with v=0 on S and F implies p_a=p_b=:pi_e. The analogous
identity is p_c=p_d=:pi_f. Therefore every harmonic extension has zero voltage
across the two marked edges.

Varying c_e or c_f leaves all p rows and J unchanged. Indeed, an added edge
conductance changes the harmonic equation by its conductance times the voltage
across that edge, which is zero. Its Dirichlet energy change is also zero, so
the Schur complement does not change. Equivalently,

\[
 \partial_e p_x=0,\quad\partial_f p_x=0,\quad
 \partial_e T=\partial_fT=0.
\]

Only the corresponding interior residual covariance changes:

\[
 \partial_e D_E=-vv^{\mathsf T},\qquad
 \partial_f D_F=-ww^{\mathsf T}.
\]

Here D_E,D_F are extended by zeros outside their respective interiors. These
statements also hold if a marked endpoint lies in S: its residual field is
zero and its boundary field is included in the relevant edge interaction.

## 3. The mixed coefficient becomes a boundary covariance

Split V as V_E+V_F+V_S. Assign vertex terms by their set, assign an edge with
an E endpoint to V_E, one with an F endpoint to V_F, and remaining edges to
V_S. No edge has both an E and an F endpoint, so this assignment is exhaustive.
Let

\[
 A_E(\psi_{S0})=\langle V_E\mid\psi_{S0}\rangle_E,\qquad
 A_F(\psi_{S0})=\langle V_F\mid\psi_{S0}\rangle_F.
\]

Since the p rows and boundary covariance are invariant and the two residual
families are independent, differentiating Q2 gives

\[
 Q_{2,e}=\langle A_{E,e}\rangle_{S0},\qquad
 Q_{2,f}=\langle A_{F,f}\rangle_{S0}.
\]

In Q3=<V^2>/2, the only term with a mixed e,f derivative is V_EV_F. Conditional
independence and the same invariance therefore give

\[
 Q_{3,ef}=\langle A_{E,e}A_{F,f}\rangle_{S0}.
\]

Thus H2/tau^2 is minus the Wick covariance of the two boundary polynomials.
This argument includes every term in V^2, rather than discarding gradient
terms by an informal locality assertion.

## 4. Each derivative is constant plus a boundary bilinear

For m_x=p_x psi_S and the corresponding barred field, conditional Wick
expansion of q_xq_y is

\[
 \det D_{\{x,y\}}+D_{xx}\bar m_y m_y+D_{yy}\bar m_xm_x
 -D_{xy}(\bar m_xm_y+\bar m_ym_x)
 +(\bar m_xm_x)(\bar m_ym_y).
\]

Under D'=-vv^T and p'=0, its derivative is a constant minus
the boundary bilinear with row v_x p_y-v_y p_x. Since V contains minus c_g
times this quartic, these terms contribute a positive bilinear matrix

\[
 \sum_g c_g\delta_{e,g}^{\mathsf T}\delta_{e,g},
 \qquad \delta_{e,g}=v_xp_y-v_yp_x.
\]

There is one explicit marked-conductance derivative, namely minus q_aq_b.
Because p_a=p_b=pi_e, its boundary quartic vanishes: it is the square of the
same Grassmann bilinear. Its bilinear matrix is

\[
 -R_e\pi_e^{\mathsf T}\pi_e,\qquad
 R_e=D_{aa}+D_{bb}-2D_{ab}=v_a-v_b.
\]

All derivatives of vertex terms are constants. Consequently

\[
 A_{E,e}=\kappa_e+\bar\psi_{S0}\widehat B_e\psi_{S0},\qquad
 \widehat B_e=\sum_gc_g\delta_{e,g}^{\mathsf T}\delta_{e,g}
              -R_e\pi_e^{\mathsf T}\pi_e.
\]

The analogous formula holds for f. Constants do not affect covariance.

## 5. Completion of the electrical square

Let d_g=v_x-v_y. Current energy gives sum_g c_g d_g^2=R_e. Harmonicity of p on
E union F, together with v=0 on S, gives the row identity

\[
 \sum_g c_gd_g\delta_{e,g}=R_e\pi_e.
\]

For example, its left side equals sum_x p_x v_x(Lv)_x by summation by parts;
the latter is v_a p_a-v_b p_b=R_e*pi_e. Completing the square therefore yields

\[
 \widehat B_e=\sum_gc_g
   (\delta_{e,g}-d_g\pi_e)^{\mathsf T}
   (\delta_{e,g}-d_g\pi_e)=B_e.
\]

Both B_e and B_f are positive semidefinite. The Grassmann bilinear covariance
identity is

\[
 \operatorname{Cov}(\bar\psi A\psi,\bar\psi B\psi)
 =-\operatorname{tr}(TATB).
\]

This follows from the two-by-two Wick determinant; its minus sign is
essential. Substituting into Section 3 proves exactly the stated SOS, with
no factor two. Expanding B_e,B_f proves its edge-pair sum-of-squares form.

## 6. Independent check of weighted H1 and equality geometry

Ground at a. H0=0 gives w_a=w_b=0 and v_c=v_d=k. The exact rank-one Green
derivative of the explicit Q2 determinant formula gives

\[
 -Q_{2,ef}=\sum_gc_g(v_xw_y-v_yw_x)^2-k^2R_f.
\]

Indeed, the Green derivative of the e quartic produces the negative square
sum; differentiating its coefficient at f contributes k^2 R_f. The explicit
e determinant has zero f derivative because w_a=w_b=0. These are all terms.

Put j_g=c_g(v_xw_y-v_yw_x). Its divergence is -k b_f and its energy inner
product with the f unit electrical flow i_f is -k R_f. Replacing v by v-k
replaces j by j+k i_f, whose squared energy is energy(j)-k^2 R_f. Hence

\[
 H_1=\tau^2\sum_gc_g(v_xw_y-v_yw_x)^2
\]

for the special potentials with v_c=v_d=0 and w_a=w_b=0.

If H1=0, nonzero potential pairs (v_x,w_x) have a fixed projective direction
on each component of G-S. A direction with both coordinates nonzero contains
no marked endpoint. Both potentials are harmonic there with zero boundary,
so the maximum principle rules it out. Thus every vertex has v_x*w_x=0.
An E-F edge would have a nonzero wedge, so there is no such edge. Connectivity
and the nonzero two currents imply S is nonempty. These facts prove the
geometry used above without assuming twins or a prescribed graph family.

## 7. Exact computational audit

`general_h2_sos_independent_audit.py` computes the SOS with exact Fraction
matrix inversion and independently obtains the full Rayleigh polynomial by
enumerating all subsets of the unmarked graph, rejecting cycles, and testing
the forced inclusion of each marked edge. It contains no Grassmann formulas
or coefficient recurrences.

Six cases passed: four twins over two hubs; two non-twin three-vertex current
supports; the same with a removed core edge; changed marked conductances;
three common boundary vertices; and that last graph with a different root.
The three-vertex supports have currents proportional to (2,-2,1), and their
interior harmonic exit rows differ from the marked endpoint rows. Thus these
are not merely instances of the earlier four-twin theorem. Exact coefficients
and graph data are in `general_h2_sos_independent_audit_results.json`.

The finite tests check implementation and normalization. The conditional Wick
derivation and electrical completion above provide the general proof.
