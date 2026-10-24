# A general electrical sum of squares for the third forest Rayleigh coefficient

Research continuation, 2 October 2026. The theorem below is a partial result on
the forest negative-correlation conjecture. Mathematical novelty has not been
certified. The original exploratory derivation is preserved separately in
`GENERAL_H2_SOS_DRAFT.md`.

## Theorem

Let G be a connected finite graph on n vertices with positive conductances c_g.
Let e=ab and f=cd be distinct non-bridge edges, oriented arbitrarily. Define the
multivariate forest polynomial

\[
 Z(\mathbf z)=\sum_{F\subseteq E(G)\,\mathrm{acyclic}}\prod_{g\in F}z_g,
 \qquad \mathcal R_{ef}=(\partial_eZ)(\partial_fZ)-Z\partial_{ef}Z.
\]

Derivatives are taken before specializing z_g=lambda*c_g. Write

\[
 \mathcal R_{ef}(\lambda\mathbf c)
 =H_0\lambda^{2n-4}+H_1\lambda^{2n-5}
       +H_2\lambda^{2n-6}+O(\lambda^{2n-7}).
\]

**If H_0=H_1=0, then H_2>=0.** More precisely, H_2 has the electrical
sum-of-squares representation defined below.

The hypotheses imply that, after choosing special additive constants, the unit
current potentials v for e and w for f have disjoint supports E and F, with no
edge from E to F. Put S={x:v(x)=w(x)=0}; it is nonempty. Their constants are
chosen so that v(c)=v(d)=0 and w(a)=w(b)=0. Choose any root r in S.

Let L be the full conductance Laplacian and K=L_r^{-1} its grounded inverse,
extended by a zero row and column at r. Thus v=K b_e and w=K b_f. Put
B=S\{r} and U=E union F. Define grounded harmonic boundary rows p_x by

\[
 P_U=-L_{UU}^{-1}L_{UB},\qquad
 p_s=\mathbf e_s^T\ (s\in B),\qquad p_r=0.
\]

The endpoint rows satisfy p_a=p_b=:pi_e and p_c=p_d=:pi_f. Let T=K_{B,B},
the inverse grounded Schur complement after eliminating U. For an oriented
edge g=xy define

\[
\begin{aligned}
 \eta_{e,g}&=v(x)p_y-v(y)p_x-(v(x)-v(y))\pi_e,\\
 \eta_{f,g}&=w(x)p_y-w(y)p_x-(w(x)-w(y))\pi_f.
\end{aligned}
\]

Let tau be the full graph's weighted spanning-tree sum. Then

\[
 \boxed{
 H_2=\tau^2\sum_{g,h\in E(G)}c_gc_h
        \bigl(\eta_{e,g}T\eta_{f,h}^T\bigr)^2.
 }
\]

The sums use all edges, including the marked edges; their own response rows
vanish. Orientation changes affect only signs inside squares. If B is empty,
the right-hand side is zero. No unlisted factor of c_e or c_f occurs.

Consequently, if this expression is strictly positive, the marked forest edge
indicators are strictly negatively correlated for all sufficiently large
lambda. Equality is characterized exactly by

\[
 \eta_{e,g}T\eta_{f,h}^T=0\quad\text{for all }g,h.
\]

This theorem gives no sign conclusion for the next coefficient when this
expression vanishes. It therefore does not solve the general forest conjecture
or even every high-fugacity case.

## 1. Previously known boundary and the equality geometry

The transfer-current theorem gives H_0=tau^2(b_e^T L^dagger b_f)^2.
Conditionally on H_0=0, the second coefficient has the electrical formula

\[
 H_1=\tau^2\sum_{xy\in E(G)}c_{xy}
            (v(x)w(y)-v(y)w(x))^2.
\]

For unit conductances this is the main forest result in Çiçeksiz–Ravichandran,
*Negative Correlation for Forests and the q<1 Random-Cluster Model*,
https://arxiv.org/html/2610.00549v1. Their Theorem 4.8 gives the equipotential
interface decomposition used here. Their discussion immediately preceding that
theorem explicitly leaves H_2 or the full Rayleigh difference for further
investigation. The support decomposition is thus prior art; the present
continuation is the displayed third-coefficient formula. The weighted identity
is verified directly in Section 7 below.

For clarity, the short equality argument is repeated. At every edge xy,
H_1=0 forces the vectors (v(x),w(x)), (v(y),w(y)) to be collinear. A component
outside S with both coordinates nonzero contains no marked endpoint; each
potential is harmonic there, with zero boundary values on S. The maximum
principle forces it to vanish, a contradiction. Thus each component outside S
lies on one coordinate axis. The supports E,F are disjoint; an E–F edge would
have a nonzero wedge and is forbidden. Connectivity forces S to be nonempty.

If H_0=0 for adjacent marked edges, their shared vertex separates the relevant
forest blocks and their indicators are independent. Alternatively the formula
below remains valid, with zero response on that side. Bridge edges are also
independent of all other edge indicators and can be treated separately.

## 2. Two elementary grounded forest identities

Write tau_k for the weighted unrooted k-component forest sum, Q_2=tau_2/tau,
and Q_3=tau_3/tau. With a root r grounded, put D_I=det(K_{I,I}). All indices
in the following sums exclude r:

\[
\begin{aligned}
 Q_2={}&\sum_iK_{ii}-\sum_{ij\in E(G-r)}c_{ij}D_{ij},\\
 Q_3={}&\sum_{i<j}D_{ij}
 -\sum_{ij\in E(G-r)}c_{ij}\sum_{k\notin\{i,j\}}D_{ijk}\\
 &+\sum_{\substack{ij,kl\in E(G-r)\\ij<kl,\{i,j\}\cap\{k,l\}=\varnothing}}
                         c_{ij}c_{kl}D_{ijkl}.
\end{aligned}
\]

These follow from the all-minors matrix-tree theorem. In the first formula the
positive term marks one vertex in the component not containing r. The negative
term removes and marks one edge in that component, creating two additional
rooted components. Each unrooted two-component forest has net multiplicity
|V(C)|-|E(C)|=1.

For the second formula, a three-component forest's two non-root components
have net feature multiplicity

\[
 |V(C_1)||V(C_2)|-|E(C_1)||V(C_2)|
 -|V(C_1)||E(C_2)|+|E(C_1)||E(C_2)|=1.
\]

Removing the selected edge or edges produces exactly the rooted forests counted
by the corresponding principal minors. The edge pair is unordered and must be
vertex-disjoint because all four endpoints are distinct marked roots. Every
resulting three-component forest has its selected edges in different non-root
components. These observations fix every multiplicity and sign in the formulas.

Introduce formal Grassmann pairs barpsi_i,psi_i with q_i=barpsi_i psi_i, and
q_r=0. Let <.> be the normalized Gaussian Wick functional with covariance K,
so <prod_{i in I}q_i>=D_I. Put

\[
 V=\sum_iq_i-\sum_{ij\in E(G-r)}c_{ij}q_iq_j.
\]

The two identities are precisely Q_2=<V> and Q_3=<V^2>/2. This functional is
an algebraic determinant device, not a probability measure. The forest
Grassmann representation is classical; see Caracciolo–Jacobsen–Saleur–Sokal–
Sportiello, https://arxiv.org/abs/cond-mat/0403271. Only the two explicitly
proved identities above are required here.

## 3. Harmonic data are fixed by either marked conductance variation

The block equation for v gives

\[
 L_{UU}v_U=(b_e)_U,\qquad L_{BU}v_U=(b_e)_B.
\]

Since P_U=-L_UU^{-1}L_UB and L is symmetric,
P_U^T(b_e)_U=-(b_e)_B, which says p_a=p_b. This includes an endpoint in S;
the boundary row is then its coordinate identity. The f argument is identical.

Any harmonic extension h_x=p_x z of boundary values satisfies h_a=h_b and
h_c=h_d. Changing the conductance of e or f therefore leaves this same h
harmonic: the added Laplacian term b_e b_e^T h or b_f b_f^T h is zero.
Uniqueness of the Dirichlet solution shows that every row p_x is unchanged.
The Dirichlet energy is unchanged as well, so the boundary Schur complement
and its inverse T are unchanged.

These statements hold in a whole neighborhood of the positive marked
conductances. Thus mixed derivatives below may legitimately treat P,T as
constant. The conditional interior inverse changes by the usual rank-one rule,
with derivative -v_Uv_U^T for e and -w_Uw_U^T for f.

## 4. Conditional Grassmann algebra gives a boundary covariance

Gaussian block elimination writes the fields as

\[
 \psi_x=p_x\psi_B+\chi_x,\qquad
 \bar\psi_x=\bar\psi_Bp_x^T+\bar\chi_x.
\]

The boundary covariance is T. The E interior covariance is L_EE^{-1}, the
F covariance is L_FF^{-1}, and these two interior families are independent
in the Wick sense, because L_EF=0. At boundary vertices chi=0.

Partition the local interaction as V=V_E+V_F+V_S: assign a vertex term to its
own part, an E–E or E–S edge term to V_E, an F–F or F–S edge term to V_F,
and an S–S edge term to V_S. There are no other edge types. Define boundary
polynomials

\[
 A_E(\psi_B)=\langle V_E\mid\psi_B\rangle_E,\qquad
 A_F(\psi_B)=\langle V_F\mid\psi_B\rangle_F.
\]

Only the e variation affects A_E and only the f variation affects A_F.
The boundary covariance and harmonic rows stay fixed. In <V^2>/2, all terms
other than V_EV_F involve at most one affected interior family. Conditional
independence gives

\[
 \partial_eQ_2=\langle A'_E\rangle_B,\quad
 \partial_fQ_2=\langle A'_F\rangle_B,\quad
 \partial_{ef}Q_2=0,\quad
 \partial_{ef}Q_3=\langle A'_EA'_F\rangle_B.
\]

Here primes mean differentiation in the corresponding marked conductance.
The coefficient of V_EV_F in V^2/2 is exactly one.

To identify A'_E, write h_x=p_x psi_B. For an edge xy assigned to V_E, its
conditional quartic expectation consists of a degree-four boundary term, a
bilinear term, and a constant. The bilinear term is

\[
 C_{yy}\bar h_x h_x+C_{xx}\bar h_y h_y
       -C_{xy}(\bar h_x h_y+\bar h_y h_x),
\]

where C=L_EE^{-1}, extended by zero outside E. Its e derivative, using
partial_e C=-v v^T, is

\[
 -\bigl(v_y\bar h_x-v_x\bar h_y\bigr)
        \bigl(v_yh_x-v_xh_y\bigr).
\]

The interaction contains minus c_xy times this quartic, so its covariance
variation contributes the boundary matrix

\[
 \sum_{g=xy}c_g(v_xp_y-v_yp_x)^T(v_xp_y-v_yp_x).
\]

The explicit derivative of the marked coefficient contributes minus its
conditional quartic expectation. Its degree-four boundary term vanishes:
p_a=p_b=pi_e implies q(pi_e psi_B)^2=0. Its bilinear part has coefficient
R_e pi_e^T pi_e, where R_e=C_aa+C_bb-2C_ab=K_aa+K_bb-2K_ab.
Vertex terms and remaining contractions contribute only a constant.
Therefore

\[
 A'_E=\text{constant}+\bar\psi_B\widehat B_e\psi_B,\qquad
 \widehat B_e=\sum_gc_g\delta_{e,g}^T\delta_{e,g}-R_e\pi_e^T\pi_e,
 \quad \delta_{e,g}=v_xp_y-v_yp_x.
\]

The F calculation gives A'_F=constant+barpsi_B widehat B_f psi_B.

The normalization from activity derivatives is important. Since
Z(lambda*c)=lambda^{n-1}(tau+tau_2/lambda+tau_3/lambda^2+...), each edge
activity derivative contributes a factor lambda^{-1}. Under H_0=H_1=0,

\[
\begin{aligned}
 H_2/\tau^2
 &=-\partial_{ef}(Q_3-Q_2^2/2)\\
 &=(\partial_eQ_2)(\partial_fQ_2)-\partial_{ef}Q_3\\
 &=-\operatorname{Cov}_{B}(A'_E,A'_F).
\end{aligned}
\]

The Gaussian Grassmann bilinear covariance is

\[
 \operatorname{Cov}_B(\bar\psi_B A\psi_B,
                      \bar\psi_B B\psi_B)=-\operatorname{tr}(TATB),
\]

which follows immediately from the two-pair determinant. Hence

\[
 H_2=\tau^2\operatorname{tr}(T\widehat B_eT\widehat B_f).
\]

## 5. Subtracting a unit current turns each response into squares

For arbitrary real grounded boundary values z, put h_x=p_x z. Define an
oriented flow j_g=c_g(v_xh_y-v_yh_x). Its divergence is

\[
 (\operatorname{div}j)_x=h_x(Lv)_x-v_x(Lh)_x
                       =(\pi_e z)(b_e)_x.
\]

Indeed h is harmonic on U, v=0 on S, and h_a=h_b=pi_e z. The electrical unit
flow i_g=c_g(v_x-v_y) has divergence b_e and energy R_e. Thus j-(pi_e z)i
is a circulation, and integration by parts makes it energy-orthogonal to i.
Consequently

\[
\begin{aligned}
 z^T\widehat B_e z
 &=\sum_gc_g(v_xh_y-v_yh_x)^2-R_e(\pi_e z)^2\\
 &=\sum_gc_g\bigl(v_xh_y-v_yh_x-(v_x-v_y)\pi_e z\bigr)^2\\
 &=z^T\left(\sum_gc_g\eta_{e,g}^T\eta_{e,g}\right)z.
\end{aligned}
\]

Since this holds for every z, widehat B_e=B_e. The same gives widehat B_f=B_f.
Both are positive semidefinite. Finally expanding their trace product gives
exactly the theorem's sum of squares.

## 6. Consistency checks and the unresolved next step

For two twin pairs over an arbitrary weighted core, the boundary responses
reduce to the covariance matrices of their spoke profiles, recovering the
independent two-profile calculation. For four identical twins the formula
reduces to the earlier adjugate sum of squares. For an interface consisting of
one vertex the response spaces are zero-dimensional and the relevant forest
blocks are independent.

The vanishing condition H_2=0 is precise but can occur nontrivially. The current
paper gives chains with arbitrarily many leading zero coefficients. The next
research step would require control of higher conditional boundary interactions,
not merely positivity of the two bilinear response matrices. No recursion or
sign theorem for those higher interactions is claimed here.

This result concerns pairwise edge negative correlation. It does not prove
negative association of arbitrary increasing functions, nor any q<1 random-
cluster assertion.

## 7. Direct weighted second-coefficient verification

To verify the weighted equality condition without importing an unstated
extension, ground r=a. When H_0=0, the f potential w is zero at both a,b;
the grounded e potential v has one common value k at c,d. Rank-one Green
updates in the explicit Q_2 identity give

\[
 -\partial_{ef}Q_2=
  \sum_gc_g(v_xw_y-v_yw_x)^2-k^2R_f.
\]

The flow c_g(v_xw_y-v_yw_x) has divergence -k b_f. Its energy inner product
with the f electrical unit flow is -kR_f. Replacing v by v-k adds k times
that unit flow, so its energy becomes exactly the displayed difference:

\[
 -\partial_{ef}Q_2=
  \sum_gc_g((v_x-k)w_y-(v_y-k)w_x)^2.
\]

Since H_1=-tau^2 partial_ef Q_2 when H_0=0, this is the weighted electrical
formula stated in Section 1. The v-k and w representatives have the required
special endpoint constants.

## Independent checks and novelty boundary

The original operator proof was read independently by the root analyst, which
found no gap in the principal-minor counting, derivative normalization, support
cancellations, Wick signs, harmonic projection, or flow energy identity. A
second analyst obtained the conditional proof above independently. Exact full-
graph coefficient checks include genuinely non-twin support regions with
nonconstant harmonic rows and varied marked conductances. The companion
independent audit files record the exact graphs and values.

Primary-source comparison shows that arXiv:2610.00549v1's stated H_0/H_1 results
and equality classification do not already give this H_2 formula. That limited
comparison does not certify historical novelty. A wider literature review or
specialist review remains necessary before describing the theorem as new.
