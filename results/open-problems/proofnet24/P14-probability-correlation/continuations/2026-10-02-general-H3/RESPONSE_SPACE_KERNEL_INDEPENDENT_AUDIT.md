# Exact kernel of the first marked-edge response space

Independent audit, 2 October 2026. This concerns a current support E in the
H0=H1=0 equality geometry, with boundary S, marked edge e=ab, special current
potential v zero on S, and harmonic exit rows p_a=p_b=pi. Let A be the set of
boundary vertices adjacent to E. This note uses all coordinates of S; deleting
a grounded boundary coordinate gives the equivalent grounded formulation.

## Kernel lemma

For positive conductances define

\[
 \eta_g=v_xp_y-v_yp_x-(v_x-v_y)\pi,\qquad
 B=\sum_gc_g\eta_g^{\mathsf T}\eta_g.
\]

Then

\[
 \ker B=\{z: z\text{ is constant on }A\},\qquad
 \operatorname{range}B=\operatorname{span}\{e_s-e_t:s,t\in A\},
 \qquad\operatorname{rank}B=|A|-1.
\]

Values at boundary vertices outside A are unrestricted in the kernel. The
claim is valid even when a marked endpoint is in S.

### Proof

Since c_g>0, Bz=0 is equivalent to eta_g z=0 for every edge. Let h be the
harmonic extension of the boundary values z, put k=h_a=h_b, and u=h-k.
The edge equations are v_x u_y=v_y u_x. On each component of the nonzero
support E, u_x/v_x is therefore constant.

Every component of E contains a nonzero marked endpoint. Otherwise v would
be harmonic there with zero values on all neighboring vertices outside E,
contradicting the maximum principle. At such an endpoint u=0 because both
marked endpoint values equal k. Consequently u=0 throughout E. An edge from
x in E to s in S then gives v_x u_s=0, hence z_s=k. This proves that z is
constant on A.

Conversely, if boundary values are constant k on A, their harmonic extension
is constant k on every component of E. A marked endpoint in S lies in A
because its marked neighbor has nonzero potential; otherwise the current
would vanish. Thus h_a=h_b=k, and every eta equation vanishes.

All p rows on E are supported on A and sum to one. Hence every eta row is
supported on A and sums to zero. The exact kernel characterization now gives
the asserted range and rank by finite-dimensional orthogonal complement.

## Important limit

This first-response kernel does not establish all-orders linear-mode
confinement. For two twins over two boundary hubs, the first response uses
only their contrast mode, but the marked score at the next order contains a
quartic q_s q_t. That term involves the common mode. It instead combines with
the contrast bilinear into the deformed edge invariant

\[
 f_{st}^{(t)}=q(\psi_s-\psi_t)-tq_sq_t.
\]

The independent exact two-twin calculation is being recorded separately.
The kernel lemma therefore controls leading response and boundary attachment
geometry; it does not by itself prove the proposed all-orders recursion.

## Off-diagonal question

The range/rank statement only says B is a positive semidefinite matrix with
zero row sums, supported on A. That does not in general imply its
off-diagonal entries are nonpositive. Whether this particular electrical B
is always a graph Laplacian needs an additional proof or counterexample.
`response_space_laplacian_search.py` constructs exact balanced-current
three- and four-vertex interiors to investigate that separate claim.
