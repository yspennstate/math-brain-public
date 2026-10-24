# Independent conditional-cumulant derivation of the fourth-coefficient SOS

Research audit, 2 October 2026. This derivation independently checks the
proposed H3 formula, using the already audited H2 equality geometry and the
one-sided local Ward identity. It does not imply a general all-orders
high-fugacity theorem.

## Statement and root choice

Assume H0=H1=H2=0. Let E,F be the two original current supports and S their
common zero boundary. Let A=N(E) intersect S, C=N(F) intersect S be their port
sets. If either response Gram is zero, its support attaches at a single
vertex and the marked edges are independent by forest factorization across
that articulation. Handle those cases directly.

Otherwise |A|,|C|>=2. The H2 SOS implies the two contrast response spaces are
orthogonal in the positive Green inner product, hence |A intersect C|<=1.
Choose the ground r in A minus C. The F-side Ward identity then has all ports
active; no E-side Ward identity is needed.

For each oriented edge pair g,h write alpha=eta_e,g, beta=eta_f,h, with full
boundary coordinates when discussing sources and grounded coordinates when
multiplying the Green matrix T. Define boundary response potentials

\[
 u=T\alpha^{\mathsf T},\qquad v=T\beta^{\mathsf T},
\]

and harmonically extend them through E and F to the full graph, with root
values zero. Every eta row is supported on its corresponding port set and
has zero sum in full coordinates. Thus

\[
 Lu=\alpha^{\mathsf T},\qquad Lv=\beta^{\mathsf T}.
\]

H2=0 gives alpha*T*beta^T=0 for every g,h. The response kernel lemma gives
v constant on A and u constant on C. Since r in A and v_r=0, v|A=0. Put
k_g=u|C. The claim is

\[
 \boxed{
 H_3=\tau^2\sum_{g,h}c_gc_h
     \sum_{xy\in E(G[S])}c_{xy}
       \bigl((u_x-k_g)v_y-(u_y-k_g)v_x\bigr)^2\ge0.
 }
\]

Edges of G[S] touching the grounded root ARE included in this final shifted
square. Omitting them would in general be incorrect.

## 1. Exact covariance of local scores

The normalized boundary integrand is

\[
 e^{tV_S}M_E(t)M_F(t),\qquad
 U_e=\partial_e\log M_E=tU_{e,1}+t^2U_{e,2}+\cdots,
\]

and similarly for f. The port harmonic maps and boundary Green covariance
are marked-independent at this equality geometry. The mixed derivative of
log(tau) is zero. Consequently the mixed logarithmic derivative of the full
forest polynomial is exactly the covariance of U_e,U_f under this formal
tilted boundary Wick functional.

Let A1=V_S+A_E1+A_F1 be the first-order boundary tilt, where A_E1 is the
conditional expectation of V_E and similarly for F. Since H2=0, the t^3
coefficient of that covariance is

\[
 C_3=\operatorname{Cov}_0(U_{e,2},U_{f,1})
    +\operatorname{Cov}_0(U_{e,1},U_{f,2})
    +\kappa_0(U_{e,1},U_{f,1},A1).
\]

The coefficient normalization is H3=-tau^2*C3. No lower coefficient or
normalizing-factor correction survives because H0,H1,H2 all vanish.

## 2. Gaussian contraction identities

Write the first scores as constants plus

\[
 U_{e,1}=\sum_gc_g q(\alpha_g\psi)+\text{constant},\qquad
 U_{f,1}=\sum_hc_h q(\beta_h\psi)+\text{constant}.
\]

For u=T alpha^T and any boundary polynomial P,

\[
 \operatorname{Cov}_0(q(\alpha\psi),P)=-\langle D_uP\rangle_0.
\]

If alpha*T*beta^T=0, the third cumulant obeys

\[
 \kappa_0(q(\alpha\psi),q(\beta\psi),P)
       =\langle D_uD_vP\rangle_0.
\]

These follow by differentiating the normalized Gaussian functional with
respect to rank-one precision changes. The covariance update is -u*u^T;
the mixed response update vanishes because alpha*T*beta^T=0. The signs agree
with Cov(bar(psi)A psi,bar(psi)B psi)=-tr(TATB).

## 3. The two second-score terms

U_e2 is supported on A, while v|A=0. Thus D_v U_e2=0 and the first covariance
term is zero. On C the vector u is the constant k_g. The valid F-side Ward
identity proved in `LOCAL_MARKED_SCORE_WARD_INDEPENDENT_AUDIT.md` gives

\[
 D_{\mathbf1_C}U_{f,2}=-\bar\psi B_f\psi.
\]

Therefore the second covariance, after summing response rows, contributes

\[
 \sum_{g,h}c_gc_h k_g^2\,\beta_hT\beta_h^{\mathsf T}
 =\sum_{g,h}c_gc_h k_g^2\,\mathcal E_G(v_h).
\]

Here E_G(v)=sum_edges c_xy(v_x-v_y)^2 is the full electrical energy. The
equality holds because Lv=beta on the full graph and beta has zero sum.

## 4. The boundary-tilt third cumulant

The two lowering operators annihilate all constants and bilinears in A1.
Only its quartic terms contribute. Conditional expectation of the original
quartic on an edge xy has boundary degree-four part
-c_xy*q(p_x psi)*q(p_y psi). Its double contraction is

\[
 -c_{xy}(u_xv_y-u_yv_x)^2.
\]

On edges incident to E both v endpoints vanish, since v|A=0 and its harmonic
extension into E is zero. Their contribution is zero. On edges incident to F,
both u endpoint values are k_g, since u|C=k_g and its harmonic extension into
F is constant. Their contribution is -k_g^2 times the F-region energy of v.
The remaining S-edge interactions contribute minus the unshifted wedge
energy. Thus

\[
 C_3=\sum_{g,h}c_gc_h\left[
   k_g^2\mathcal E_S(v_h)
  -\sum_{xy\in E(G[S])}c_{xy}(u_xv_y-u_yv_x)^2\right].
\]

This is an intermediate difference of energies, not yet a termwise square.
For grounded-root edges, u_r=v_r=0 so their unshifted wedge is zero; they
still occur in the electrical-energy term.

## 5. The global circulation square

For a fixed response pair define j_xy=c_xy(u_xv_y-u_yv_x), oriented x to y.
Its divergence is

\[
 \operatorname{div}j=v\,Lu-u\,Lv=-k_g\beta.
\]

The first term vanishes because alpha is supported on A and v|A=0; the
second uses beta supported on C and u|C=k_g. Let i_v=c_xy(v_x-v_y). It has
divergence beta, so j+k_g*i_v is a circulation. Its energy is

\[
 \mathcal E(j+k_gi_v)=\mathcal E(j)-k_g^2\mathcal E_G(v),
\]

because the cross inner product is
sum_x v_x div(j)_x=-k_g*E_G(v). This is exact summation by parts on the full
graph, including the root.

The unshifted j energy on F is k_g^2*E_F(v); on E it is zero. The remainder
is the S-edge wedge energy. Consequently this circulation energy is exactly
the bracket in -C3. Edgewise the circulation is

\[
 c_{xy}\bigl[(u_x-k_g)v_y-(u_y-k_g)v_x\bigr].
\]

It vanishes on every edge incident to E or F, leaving precisely the S-edge
sum in the statement. This proves its positivity, sign, and coefficient
normalization.

## Audit boundary

The derivation is contingent on the already proved H2 geometry/kernel lemma
and the explicitly root-restricted local Ward identity. It uses neither
all-orders linear response-space confinement nor a positive edge-weight
representation of B; both stronger assertions have exact counterexamples.
It gives H3>=0 under H0=H1=H2=0 and does not resolve a further vanishing H3.
