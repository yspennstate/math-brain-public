# The exact response space in the H2 equality problem

Continuation of `GENERAL_H2_SOS_PROOF.md`, 2 October 2026. This lemma has an
independent analytic check. It does not prove a higher-coefficient sign.

Use the theorem's E,F,S decomposition, harmonic boundary rows p_x, potentials
v,w, and response matrix B_e=sum_g c_g eta_e,g^T eta_e,g. Put
A=N(E) intersect S, the common interface vertices adjacent to the nonzero
support of the e current. Root r is fixed in S as before.

**Lemma.** The kernel of B_e consists exactly of the grounded boundary values
that are constant on A. Thus its range is the full contrast space

\[
 \operatorname{range}B_e
 =\operatorname{span}\{\mathbf e_s-\mathbf e_t:s,t\in A\},
 \qquad \operatorname{rank}B_e=|A|-1.
\]

Coordinates at the grounded root are omitted; if r belongs to A, the difference
with e_r means the remaining coordinate identity. Boundary coordinates outside
A are unconstrained in the kernel. The analogous statement holds for f with
C=N(F) intersect S.

**Proof.** For boundary values z let h_x=p_x z. A vector lies in ker B_e exactly
when every eta_e,g z vanishes, since all c_g are positive. Writing k_x=h_x-h_a,
this says

\[
 v_xk_y-v_yk_x=0\quad\text{at every edge }xy.
\]

On a connected component of E, the nonzero v values imply that k/v is constant.
Every such component contains a marked endpoint: otherwise v would be harmonic
there with zero boundary on S and vanish by the maximum principle. At that
endpoint k is zero, since h_a=h_b. Its v value is nonzero by membership in E.
The constant ratio is therefore zero, and h=h_a throughout E. On an edge from
E to S, the displayed relation then forces k=0 at its boundary endpoint.
Consequently h is constant on all of A.

Conversely, if boundary h has one common value kappa on A, its harmonic
extension on each E component is the constant kappa. At least one marked
endpoint is in E, and any marked endpoint in S belongs to A, so h_a=h_b=kappa.
Every response edge then vanishes; edges outside E have v_x=v_y=0. This proves
the kernel assertion. The range is its orthogonal complement, giving the
contrast-space and rank assertions.

## Consequence for H2=0

Since the global H2 formula is a sum of squares,

\[
 H_2=0\quad\Longleftrightarrow\quad
 \eta_{e,g}T\eta_{f,h}^T=0\quad\text{for every }g,h.
\]

The rows eta_e span the contrast space on A and the rows eta_f span that on C.
Therefore

\[
 H_2=0\quad\Longleftrightarrow\quad
 (\mathbf e_s-\mathbf e_t)^T T(\mathbf e_u-\mathbf e_v)=0
 \quad\text{for all }s,t\in A,\ u,v\in C.
\]

This means that every current between two e-interface ports produces zero
voltage difference between every pair of f-interface ports in the effective
boundary electrical network. It is a structural statement about all port
currents, rather than an accidental cancellation of response coefficients.

If A and C share two distinct vertices, strict H2 positivity follows immediately:
choose their shared pair, whose effective resistance is positive. Thus H2=0
requires at most one shared interface vertex. Disjoint port sets may still have
zero cross current by symmetry or by a further equipotential decomposition.
The already known chains with many leading zero coefficients show that this
condition does not imply independence of the original marked forest edges.

The response matrix is positive semidefinite and has the stated range. This
lemma does not show that it has nonpositive off-diagonal entries, nor that it
can be decomposed into nonnegative conductances of individual port-pair edges.
That stronger property is under investigation.

## A failed stronger inference

The leading marked boundary score is a constant plus a bilinear on this
contrast space. It is tempting to assume that every higher score uses only
those linear Grassmann modes. That literal assertion is false. For the minimal
twin-pair/two-port example, the second score contains a quartic proportional to
q_s q_t, which also uses the common boundary mode. However its combination
with the first bilinear is the deformed forest-edge invariant

\[
 f_{st}^{(t)}=(\bar\psi_s-\bar\psi_t)(\psi_s-\psi_t)-t q_s q_t.
\]

The independent exact local-score calculation is checkpointed separately by
the heat analyst and the conditional audit branch. Whether an appropriate
invariant-edge or invariant-hyperedge expansion gives a positive propagation
rule for the first nonzero higher coefficient remains unproved.
