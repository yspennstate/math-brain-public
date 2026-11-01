# Draft: a general sum of squares for the third forest Rayleigh coefficient

Research continuation, 2 October 2026. The derivation below is under independent
analytic and exact computational audit. No claim of a complete solution of the
forest negative-correlation conjecture or of certified novelty is made.

## Proposed theorem and its exact data

Let G be a connected finite weighted graph. Every edge g=xy has positive
conductance c_g. Mark distinct non-bridge edges e=ab and f=cd, and scale all
activities by lambda. Form edge derivatives before specializing activities.
Write tau for the weighted spanning-tree sum and

\[
 \mathcal R_{ef}(\lambda\mathbf c)
 =H_0\lambda^{2n-4}+H_1\lambda^{2n-5}
     +H_2\lambda^{2n-6}+O(\lambda^{2n-7}).
\]

Assume H_0=H_1=0. For adjacent marked edges this is an independence case, so
focus on disjoint endpoints. Let v,w be their unit-current potentials with the
special constants

\[
 v(c)=v(d)=0,\qquad w(a)=w(b)=0.
\]

Put E={x:v(x)!=0}, F={x:w(x)!=0}, and S={x:v(x)=w(x)=0}. The electrical
classification proved below shows that E,F are disjoint, have no edge between
them, and S is nonempty. Choose any grounded vertex r in S. Extend the grounded
Green matrix K=L_r^{-1} by a zero row and column at r, so v=K b_e and w=K b_f.

For x outside S, let p_x be the harmonic exit-distribution row on S, with the
coordinate of r removed. Explicitly, in grounded coordinates, with U=E union F,

\[
 P_U=-L_{UU}^{-1}L_{U,S\setminus\{r\}},\quad
 p_s=\mathbf e_s^T\ (s\in S\setminus\{r\}),\quad p_r=0.
\]

The endpoint rows satisfy p_a=p_b=:pi_e and p_c=p_d=:pi_f.
Let T=K_{S\setminus\{r\},S\setminus\{r\}}, equivalently the inverse grounded
Schur complement of L after eliminating U. If S={r}, all these matrices have
size zero, and the formulas below are interpreted as zero.

For each oriented edge g=xy define row vectors

\[
\begin{aligned}
 \eta_{e,g}&=v(x)p_y-v(y)p_x-(v(x)-v(y))\pi_e,\\
 \eta_{f,g}&=w(x)p_y-w(y)p_x-(w(x)-w(y))\pi_f.
\end{aligned}
\]

Orientation changes only the sign. Define positive semidefinite matrices

\[
 B_e=\sum_g c_g\eta_{e,g}^T\eta_{e,g},\qquad
 B_f=\sum_g c_g\eta_{f,g}^T\eta_{f,g}.
\]

**Proposed formula.**

\[
 \boxed{\quad H_2=\tau^2\operatorname{tr}(TB_eTB_f)
       =\tau^2\sum_{g,h}c_gc_h
          (\eta_{e,g}T\eta_{f,h}^T)^2\ge0.\quad}
\]

No extra factors of marked-edge conductances occur, since these are derivatives
with respect to the edge activities. The formula uses the full conductance
Laplacian, including e and f. Their own eta vectors vanish.

If H_2>0 this proves strict marked-edge negative correlation at sufficiently
large lambda. It does **not** resolve graphs with H_0=H_1=H_2=0. The current
primary paper exhibits arbitrarily long strings of vanishing leading
coefficients, so the third-coefficient theorem alone cannot settle the general
high-fugacity conjecture.

## 1. The exact equality geometry

The transfer-current theorem gives H_0=tau^2(b_e^T L^dagger b_f)^2.
When this vanishes the special constants above are consistent. The weighted
version of the second-coefficient electrical identity is

\[
 H_1=\tau^2\sum_{xy\in E(G)}c_{xy}
        (v(x)w(y)-v(y)w(x))^2.
\]

For unit conductances this is Theorem 1.5 of
https://arxiv.org/html/2610.00549v1. Its equality geometry is explicitly left
for higher-coefficient analysis in that paper. The weighted identity also
follows from the grounded-minor calculation in Section 2: differentiate Q_2,
use the rank-one Green updates, and shift the nonzero common endpoint constant;
the shift subtracts the relevant current energy. A separate explicit calculation
is recorded at the end of these notes.

If H_1=0, the two-vectors (v(x),w(x)) and (v(y),w(y)) are collinear at every
edge. On each component of G-S they therefore have a fixed projective direction.
A component whose direction has both coordinates nonzero contains no endpoint
of e or f: at those endpoints one of the special potentials is zero. Each
potential is harmonic on that component and has zero boundary values on S.
The maximum principle forces both to vanish, a contradiction. Every component
thus has an axis direction. Hence v(x)w(x)=0 at every vertex, so E,F are disjoint.
An E–F edge would have nonzero wedge and is forbidden. Connectivity ensures
S is nonempty.

The harmonic row identity follows from v=K b_e and v=0 on S and F. In block
form, L_UU v_U=(b_e)_U and L_SU v_U=(b_e)_S. Since
P_U=-L_UU^{-1}L_US, symmetry gives P_U^T(b_e)_U=-(b_e)_S. In other words,
p_a-p_b=0, including the possibility that an endpoint itself lies on S.
The same argument gives p_c=p_d.

## 2. Two grounded forest-ratio identities

Let Q_2=tau_2/tau and Q_3=tau_3/tau, where tau_k is the weighted unrooted
k-component forest sum. Ground any root r, let K=L_r^{-1}, and write
D_I=det(K_{I,I}). All vertices and edges in the following sums exclude r:

\[
\begin{aligned}
 Q_2={}&\sum_i K_{ii}-\sum_{ij\in E}c_{ij}D_{ij},\\
 Q_3={}&\sum_{i<j}D_{ij}
       -\sum_{ij\in E}c_{ij}\sum_{k\notin\{i,j\}}D_{ijk}
       +\sum_{\substack{ij,kl\in E\\ij<kl,\{i,j\}\cap\{k,l\}=\varnothing}}
                  c_{ij}c_{kl}D_{ijkl}.
\end{aligned}
\]

These are exact elementary consequences of the all-minors matrix-tree theorem.
For Q_2, the first sum counts a two-component forest with a chosen vertex in
the component not containing r; the second counts a chosen edge there, by
removing it and marking its endpoints as roots. The net multiplicity is
|V(C)|-|E(C)|=1. For Q_3 the three terms choose respectively vertices in the
two non-root components, an edge and a vertex, or an edge in each. Their net
multiplicity is (|V(C_1)|-|E(C_1)|)(|V(C_2)|-|E(C_2)|)=1.
Edges touching r contribute zero because that component is already rooted.

For concise algebra introduce Grassmann pairs barpsi_i,psi_i, q_i=barpsi_i psi_i,
and the normalized Gaussian Wick functional with covariance K, characterized
by <prod_{i in I}q_i>=D_I. Define

\[
 V=\sum_iq_i-\sum_{ij\in E}c_{ij}q_iq_j.
\]

The two identities say Q_2=<V>, Q_3=1/2<V^2>. This formal functional is not an
ordinary probability measure. Only determinant/Wick algebra is used below.
The all-orders forest Grassmann representation is classical (Caracciolo,
Jacobsen, Saleur, Sokal, Sportiello 2004,
https://arxiv.org/abs/cond-mat/0403271), but is not needed here beyond these two
explicitly proved coefficient identities.

## 3. The mixed derivative collapses to one Gaussian covariance

The rank-one Green identities at the equality point are

\[
 \partial_e K=-vv^T,\quad \partial_f K=-ww^T,\quad
 \partial_f v=\partial_e w=0,
\]

because b_e^T K b_f=0. Let D_v be the Gaussian lowering operator defined by

\[
 D_vq_i=v_i^2,\qquad
 D_v(q_iq_j)=v_i^2q_j+v_j^2q_i
        -v_iv_j(\bar\psi_i\psi_j+\bar\psi_j\psi_i).
\]

Equivalently it contracts one bar and one unbarred Grassmann variable against
vv^T. For every polynomial U,

\[
 \partial_e\langle U\rangle=-\langle D_v U\rangle
                              +\langle\partial_eU\rangle.
\]

This is the determinant rank-one update, extended linearly. Put C_e=q_aq_b,
C_f=q_cq_d, with q_r=0 if an endpoint is grounded, and define

\[
 J_e=D_v V+C_e,\qquad J_f=D_w V+C_f.
\]

Since partial_e V=-C_e and partial_f V=-C_f,
partial_e Q_2=-<J_e>, partial_f Q_2=-<J_f>.

Every monomial obtained by a v contraction or a first v derivative of V is
supported on E union S: V is local to a vertex or an edge, and no edge joins E
to F. Thus any w contraction or first w derivative of these expressions
vanishes. The same holds with e,f reversed. In particular partial_ef Q_2=0.
Applying the product rule twice to Q_3=1/2<V^2>, the possible cross-gradient
terms vanish for exactly this support reason, leaving

\[
 \partial_{ef}Q_3=\langle J_eJ_f\rangle.
\]

One can check this without notation for cross-gradients by expanding:
D_wD_v(V^2/2)=(D_vV)(D_wV),
D_v(C_fV)=C_fD_vV, D_w(C_eV)=C_eD_wV;
the remaining explicit mixed term is C_eC_f.

The expansion of log(tau+t tau_2+t^2 tau_3+...) is
log tau+t Q_2+t^2(Q_3-Q_2^2/2)+.... Because H_0=H_1=0,

\[
 H_2/\tau^2=(\partial_eQ_2)(\partial_fQ_2)-\partial_{ef}Q_3
           =-\operatorname{Cov}_{\mathrm{Wick}}(J_e,J_f).
\]

## 4. Normal ordering removes the endpoint quartics

Normal ordering C_e separates a constant, a bilinear part, and a degree-four
part with no internal Wick contractions. Its bilinear matrix is

\[
 C_e^{(2)}=K_{bb}E_{aa}+K_{aa}E_{bb}
                 -K_{ab}(E_{ab}+E_{ba}),
\]

where E_ij is a matrix unit; grounded rows and columns are zero. The centered
bilinear part of J_e therefore has matrix -A_e, where

\[
 A_e=\sum_{g=xy}c_g(v_y\mathbf e_x-v_x\mathbf e_y)
                         (v_y\mathbf e_x-v_x\mathbf e_y)^T-C_e^{(2)}.
\]

The remaining degree-four normal-ordered part is supported only at a,b.
The f formulas are analogous. A_e is supported on E union S and A_f on F
union S.

From v=K b_e and v=0 outside E,
K_{a,x}=K_{b,x} for every x outside E. Hence the cross covariance between the
e-endpoint pair and anything supported on F union S has rank at most one.
A degree-four normal-ordered term has zero Wick pairing with a normal-ordered
bilinear term (there are too few fields on the other side), and its pairing
with the f degree-four term is a squared determinant of the two-by-two cross
matrix, which is zero. Thus only the bilinear covariance survives. The standard
Wick bilinear identity is

\[
 \operatorname{Cov}_{\mathrm{Wick}}
  (: \bar\psi A\psi :,: \bar\psi B\psi :)=-\operatorname{tr}(KAKB).
\]

Consequently

\[
 H_2/\tau^2=\operatorname{tr}(K A_e K A_f).
\]

## 5. Harmonic projection and the electrical cycle-flow square

Between E union S and F union S, the Green kernel factors through the common
boundary:

\[
 K_{E\cup S,F\cup S}=P_{E\cup S}\,T\,P_{F\cup S}^T.
\]

This follows either from block Gaussian elimination or harmonicity on the
eliminated components. Therefore

\[
 \operatorname{tr}(K A_e K A_f)
 =\operatorname{tr}(T\widehat B_e T\widehat B_f),\qquad
 \widehat B_e=P^T A_eP.
\]

Because p_a=p_b=pi_e, projection of C_e^(2) is R_e pi_e^T pi_e, where
R_e=K_aa+K_bb-2K_ab is the effective resistance. Thus

\[
 \widehat B_e=\sum_{g=xy}c_g(v_xp_y-v_yp_x)^T(v_xp_y-v_yp_x)
                       -R_e\pi_e^T\pi_e.
\]

To see its positivity exactly, prescribe arbitrary grounded boundary values z
and put h_x=p_x z. Define an oriented flow
j_g=c_g(v_xh_y-v_yh_x). Its divergence at x is
h_x(Lv)_x-v_x(Lh)_x. The second term is zero: h is harmonic on E union F,
and v=0 on S. Since h_a=h_b=pi_e z, this divergence is (pi_e z)b_e.
The unit electrical flow i_g=c_g(v_x-v_y) has divergence b_e and energy R_e.
The difference j-(pi_e z)i is a circulation, orthogonal in electrical energy
to i. Its edgewise energy is

\[
 \sum_gc_g
 [v_xh_y-v_yh_x-(v_x-v_y)\pi_e z]^2.
\]

Hence energy(j)-R_e(pi_e z)^2 is exactly z^T B_e z with B_e defined in the
statement. Since this holds for every z, widehat B_e=B_e. The same gives
widehat B_f=B_f. Substitution proves the proposed global formula.

## 6. The weighted H1 calculation used in the classification

For completeness, ground r=a. If H_0=0, then the grounded f potential w is
zero at both a,b, while the grounded e potential v takes a common value k at
c,d. The direct rank-one derivative of Q_2 gives

\[
 -\partial_{ef}Q_2=\sum_gc_g(v_xw_y-v_yw_x)^2-k^2R_f.
\]

The flow c_g(v_xw_y-v_yw_x) has divergence -k b_f. Its energy inner product
with the f unit electrical flow is -kR_f. Replacing v by v-k therefore turns
the preceding difference into

\[
 \sum_gc_g((v_x-k)w_y-(v_y-k)w_x)^2.
\]

Together with H_1=-tau^2 partial_ef Q_2 this proves the weighted second-
coefficient identity and validates its equality classification. The signs
can also be checked directly by reversing both edge orientations.

## Audit status and remaining boundary

Independent derivation and full-graph tests are being run in parallel. Before
using this as a proved result, the operator product-rule cancellation, Wick
normal-order sign, equality classification, and coefficient normalization all
need explicit audit. No assertion that H_2 is always strictly positive is made:
its vanishing condition is the exact orthogonality
eta_e,g T eta_f,h^T=0 for every edge pair g,h. Whether that condition supports
a recursive proof for higher coefficients is a separate open step.
