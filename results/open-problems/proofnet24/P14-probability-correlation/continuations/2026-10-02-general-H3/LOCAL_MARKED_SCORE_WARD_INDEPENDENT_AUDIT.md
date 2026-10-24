# Independent audit of the local marked-score Ward identity

Research audit, 2 October 2026. The Ward route is valid with the root placement
specified below. The identity is false if a fixed zero root is simply omitted
from a support's active port set. This note audits local score invariance and
the order-two contraction; it does not itself prove the proposed H3 theorem.

## 1. Algebra and invariant local integral

Use left Grassmann derivatives and q_i=bar(psi_i)*psi_i. Thus
partial_{psi_i}q_i=-bar(psi_i) and partial_{bar(psi_i)}q_i=psi_i.
For each active vertex define

\[
 Q_t=\sum_i(1-tq_i)\partial_{\psi_i},\qquad
 \bar Q_t=\sum_i(1-tq_i)\partial_{\bar\psi_i}.
\]

The edge invariant is

\[
 f_{ij}^{(t)}=q(\psi_i-\psi_j)-tq_iq_j.
\]

Direct differentiation gives Q_t f_ij=bar(Q_t) f_ij=0 when BOTH endpoint
variables are active. In the bilinear part the ordinary simultaneous shift
derivatives cancel. Its nonlinear derivative cancels the derivative of the
quartic part; all further terms contain a repeated Grassmann variable and
vanish.

Let E be an interior current support and A its boundary port set. Suppose
there is no edge from E to the fixed grounded root. Integrate the interior
variables in

\[
 I_E(t;\psi_A)=\int_E\prod_{i\in E}(1+tq_i)
       \exp\left(\sum_{g\text{ incident to }E}c_g f_g^{(t)}\right).
\]

Every incident edge has both endpoints in the active set E union A. Its
exponential is invariant under Q_E+Q_A. The interior measure is invariant
under Grassmann integration by parts, since

\[
 (1-tq_i)\prod_{j\in E}(1+tq_j)
      =\prod_{j\in E\setminus\{i\}}(1+tq_j)
\]

has zero psi_i and bar(psi_i) derivative. Hence integration of Q_E against
this measure gives zero, and Q_A I_E=bar(Q_A) I_E=0. This is an exact formal
polynomial identity, rather than a statement about an ordinary probability
measure.

## 2. Gaussian normalization is marked-independent at the boundary

Let A_E=L_EE, let P be the harmonic exit map, and let N_E be the boundary
Schur complement contributed by this region. The conditional Gaussian
forest factor used in the H2 proof is

\[
 M_E(t;\psi_A)=\frac{I_E(t;\psi_A)}{\det A_E}
                     \exp(-\bar\psi_A N_E\psi_A).
\]

For the marked edge e=ab, the equality p_a=p_b implies

\[
 \partial_e N_E=(p_a-p_b)^{\mathsf T}(p_a-p_b)=0.
\]

This is exact electrical Dirichlet-energy differentiation. The derivative
of log(det A_E) is a boundary-independent scalar. Therefore the marked score

\[
 U_e=\partial_e\log M_E
     =\partial_e\log I_E-\partial_e\log\det A_E
\]

is annihilated by Q_A and bar(Q_A). The Gaussian reference need not itself
be invariant: only its marked derivative needs to be boundary-independent.
This is precisely why the reference normalization causes no extra term.

## 3. The grounded-root obstruction is real

If r in A is fixed to psi_r=bar(psi_r)=0, then an incident edge becomes
f_ir=q_i. The generator on the remaining active vertices gives
Q_t q_i=-bar(psi_i), which is nonzero. The missing root derivative had
provided the cancellation before fixing the root.

The two-twin/two-port exact score gives a marked counterexample: before
grounding its nonconstant part is C(t)[q(psi_s-psi_r)-tq_sq_r]. After grounding
r this becomes C(t)q_s and Q_s U_e=-C(t)bar(psi_s), not zero. Equality of
endpoint harmonic rows does not remove this obstruction.

Thus the above Ward proof requires the grounded root to lie OUTSIDE the
port set of the region whose Ward identity is used. One may also work with
all port variables active and introduce grounding only after applying a
correctly transformed identity, but simply omitting the root is invalid.

In the nontrivial H2=0 setting, the kernel/range lemma implies port sets A,C
have at most one common vertex: two shared vertices would give a nonzero
contrast lying in both response spaces, contradicting their orthogonality
in the positive definite Green inner product. If both B_e,B_f are nonzero,
then |A|,|C|>=2, and one may choose r in A minus C and apply the Ward identity
to the F region safely. Only one region's Ward identity is available with
that choice in general.

If a response Gram is zero, its port set has size one. The corresponding
support is attached to the rest of the graph at a single vertex, and the
forest polynomial factors across that articulation. Its marked edge is
independent of marked edges in the rest of the graph. Such cases can be
handled directly, rather than forcing a root choice.

## 4. Exact order-two constant-mode contraction

Expand the local marked score as U_e=tU_{e,1}+t^2U_{e,2}+..., with

\[
 U_{e,1}=\kappa_e+\bar\psi B_e\psi,
 \qquad B_e\mathbf1=0.
\]

Write Q_t=Q_0-tQ_1, Q_1=sum_s q_s partial_{psi_s}. Ward invariance gives
Q_0 U_e1=0 and Q_0 U_e2=Q_1 U_e1. Explicitly,

\[
 Q_1U_{e,1}=-\sum_{s\ne r}(B_e)_{sr}q_s\bar\psi_r.
\]

Consequently

\[
 P_2=\sum_{s<r}(B_e)_{sr}q_sq_r
\]

satisfies Q_0P_2=Q_1U_e1, and R_2=U_e2-P_2 is annihilated by Q_0.

Let D_1 be the Gaussian lowering operator for the constant boundary vector.
With these left-derivative conventions,

\[
 D_1=-\bar Q_0Q_0,
 \qquad D_1(q_sq_r)=q(\psi_s-\psi_r).
\]

Hence D_1R_2=0 and

\[
 D_1U_{e,2}=\sum_{s<r}(B_e)_{sr}q(\psi_s-\psi_r)
            =-\bar\psi B_e\psi.
\]

The last equality uses zero row sums: the diagonal coefficient is
sum_{r!=s}(B_e)_{sr}=-(B_e)_{ss}, and the off-diagonal coefficient is
-(B_e)_{sr}. There is no factor two, and the minus sign agrees with the exact
two-twin quartic coefficient. Nonpositive offdiagonal entries are NOT needed;
indeed the separate exact counterexample shows B_e need not have them.

This proves the requested contraction identity when the applicable Ward
generator has all its port variables active. It does not justify applying
the same formula to a region with a grounded port.
