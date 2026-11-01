# Independent arbitrary-order marked-score transfer audit

Date: 2026-10-02. Audited assembly:
`ALL_GRAPH_HIGH_FUGACITY_INDUCTION_DRAFT.md`, together with
`RESPONSE_INDUCTION_INDEPENDENT_AUDIT.md`,
`RESPONSE_CLOSURE_INDEPENDENT_AUDIT.md`, and `GENERAL_H3_SOS_PROOF.md`.

**Internal verdict: PASS; no analytic gap or counterexample found.** The
marked-score transfer is valid at arbitrary delayed order under the assembly's
explicit invariants. It is not being inferred from geometric closure or from
H4/H5/H6 numerical agreement. With the previously audited initial score and
H0/H1 equality geometry, the assembled induction supplies the sign of the
first nonzero high-fugacity Rayleigh coefficient, or exact independence.
This is an internal mathematical audit, not a priority or external peer-review
certificate. It does not prove negative correlation at arbitrary fugacity.

I independently derived the transfer before reading the global assembly,
then read the complete assembly and checked its invariant-compatible
coefficient extraction. The substantive points are below.

## 1. The marked normalization remains fixed for the required reason

The invariant includes a physical original marked unit-current potential
\(v_e\) with \(Lv_e=b_e\) and zero values outside \(I\). For any
Dirichlet harmonic extension \(h\) into \(I\),
\[
b_e^Th=v_e^TLh=0.
\]
Thus the two marked-endpoint harmonic rows coincide. Varying the marked
conductance differentiates the Schur quadratic by the square of their
difference, so its derivative vanishes. The harmonic-row derivative also
vanishes: the rank-one Laplacian change acts on a vector whose marked
endpoint difference is zero. This argument remains valid for every larger
interior containing the original current support.

Consequently, in successive elimination, the outer Schur Gaussian kernel
does not acquire a marked derivative. The determinant quotient between the
new and old interior Gaussian normalizations has zero marked derivative.
Any determinant normalization left in a raw local integral contributes
only a boundary-field scalar. The enlarged score is therefore the tilted
conditional average of the original score, rather than an invented response
observable or an average with an omitted normalization derivative.

The two original marked edges belong to distinct disjoint regions, with no
joining graph edge. Each local partition depends on its own marked
conductance only. After conditioning on the common boundary, both marked
variations leave its Gaussian covariance fixed. This verifies the global
mixed logarithmic derivative identity as a covariance of the two original
local marked scores.

## 2. Exact Ward transfer does not depend on the delayed order

Use the intrinsic polynomial with every geometric local port free. The
raw integral includes the interior vertex product \(\prod(1+tq_i)\) and
all original edge terms incident to the interior. Each edge deformation is
annihilated by the sum of its two endpoint odd vector fields. Interior
integration by parts is legitimate in the finite exterior algebra, with
\((1+tq_i)(1-tq_i)=1\). This supplies the exact port Ward identities for
the complete marked score after the marked-fixed Schur normalization is
removed. No uniform translation is applied through a grounded zero field.

Suppose
\[
U_e(t)=C_e(t)+t^\ell Q_B+t^{\ell+1}P+O(t^{\ell+2}),
\quad Q_B=\bar\psi B\psi,
\]
where \(C_e\) is scalar and \(B\mathbf1=0\). At order
\(t^{\ell+1}\), the Ward equations are precisely
\[
Q_0P=\sum_iq_i\partial_{\psi_i}Q_B,
\qquad
\bar Q_0P=\sum_iq_i\partial_{\bar\psi_i}Q_B.
\]
There is no \(\ell\) factor. Direct left differentiation verifies the
particular solution \(\sum_{i<j}B_{ij}q_iq_j\). Therefore
\[
P=\sum_{i<j}B_{ij}q_iq_j+R,
\qquad Q_0R=\bar Q_0R=0.
\]
This statement includes all Grassmann degrees in \(R\), not merely
bilinears or quartics. Applying \(-\bar Q_0Q_0\) gives the same
constant-mode contraction used at H3, regardless of \(\ell\).

## 3. Why uncontrolled higher-degree terms do not survive absorption

The vanishing cross trace and shifted-wedge energy provide physical
response potentials \(a_\rho\) supported in the enlarged region
\(I'\), with \(La_\rho=\rho\) for full zero-sum old-port charges.
Their sources span the full old contrast space. For every harmonic
extension from the new ports,
\(\rho^Th_A=a_\rho^TLh=0\). Hence every old port has the same new
harmonic row \(\pi\), even if some zero-response old port remains on the
new boundary.

Write every old port field as \(\chi_i+h\), where
\(h=\pi\psi_{A'}\) is the same odd field for every old port. The
bilinear \(Q_B\) has no harmonic or cross term because both row and
column sums of \(B\) vanish. Its conditional expectation is scalar.
The exact equations \(Q_0R=\bar Q_0R=0\) imply invariance under
adding a common unbarred and barred odd field, so
\(R(\chi+h)=R(\chi)\). Thus its entire conditional expectation is
scalar, including arbitrary higher Grassmann-degree pieces.

The Ward quartic leaves the new-boundary bilinear
\[
\sum_{i<j}B_{ij}(C_{ii}+C_{jj}-2C_{ij})q(h)
=-\operatorname{tr}(C_{AA}B)q(h).
\]
The identity uses the zero row sums, including the diagonal entries.
Its uncontracted quartic is zero because \(q(h)^2=0\). These facts
show why no unspecified high-degree term is silently discarded.

## 4. Exact leading coefficient after the new conditional tilt

Since all earlier score coefficients are scalar, normalized tilted
averaging preserves them as scalars exactly. At order \(\ell\),
\(\mathbb E Q_B\) is scalar. At order \(\ell+1\), the only
possible terms are
\[
\mathbb E P+\operatorname{Cov}(Q_B,W_1^{\mathrm{local}}).
\]
No later tilt coefficient can appear at this order. The first local tilt
is still the conditional expectation of the original physical vertex and
edge interaction; it is not an effective interaction whose quartic
coefficients have been guessed. Its Grassmann degree is at most four.
Its bilinear and scalar parts give only scalar covariance with the
pure fluctuation bilinear \(Q_B\).

For a Gram channel \(\rho\), insertion of
\(\bar\chi\rho\rho^T\chi\) differentiates the Gaussian covariance
in the direction \(-a_\rho a_\rho^T\), where
\(a_\rho=C\rho\) in the remaining interior variables. The original
physical potential agrees with this conditional response: it has the same
Dirichlet equation and zero boundary values. If an old source port remains
on the new boundary, its potential and fluctuation field are zero; its
physical boundary charge is compatible with the same Dirichlet solution.
For original vertices previously eliminated inside \(I\), harmonic
composition extends this response to the physical \(a_\rho\).

Rank-one Wick differentiation of each physical quartic therefore gives
the raw bilinear Gram
\[
\sum_{\rho,xy}c_{xy}
 (a_\rho(x)p'_y-a_\rho(y)p'_x)^T
 (a_\rho(x)p'_y-a_\rho(y)p'_x).
\]
The sign is positive because the original edge quartic and the covariance
variation each have a minus sign. It has coefficient one. The Ward term
subtracts
\(\sum_\rho R_\rho\pi^T\pi\), with
\(R_\rho=\rho^TC\rho
=\sum_{xy}c_{xy}(a_\rho(x)-a_\rho(y))^2\).

To identify this difference without assuming that a response matrix is
an M-matrix, evaluate it on arbitrary new boundary data \(z\). Let
\(h\) be their harmonic extension. The flow
\(j_{xy}=c_{xy}(a_\rho(x)h_y-a_\rho(y)h_x)\) has divergence
\(h\rho-a_\rho Lh=(\pi z)\rho\). The electrical flow
\(i_{xy}=c_{xy}(a_\rho(x)-a_\rho(y))\) has divergence \(\rho\).
Consequently \(j-(\pi z)i\) is a circulation and is orthogonal in
the edge-energy inner product to \(i\). Its energy is exactly the
raw energy minus \(R_\rho(\pi z)^2\). This proves the displayed
new Gram formula (16), with its sign, coefficient, and ordinary order
\(t^{\ell+1}\).

All new boundary-dependent terms at that order are bilinear: the invariant
remainder has lost its boundary fields, the Ward quartic's fourth-degree
part is nilpotent, and the covariance derivative of a quartic can leave
at most a bilinear. Thus the analytic invariant is restored, not merely
the geometric one.

## 5. The general cross coefficient is also controlled

At the global boundary, constants in either local score vanish from
covariances and cumulants exactly. The first possible mixed coefficient
is at \(t^{2\ell}\), and Gaussian determinant differentiation gives
\(-\operatorname{tr}(TB_eTB_f)\).

When this trace vanishes, PSD implies every channel cross Green product
vanishes. Full contrast range allows a root in \(A\setminus C\)
unless a singleton stop has already occurred. The f-channel potential
then vanishes on \(A\), so the covariance of \(P_e\) with the
f-leading bilinear is zero even if \(P_e\) has high Grassmann degree.
The e-channel potential is constant on \(C\); its covariance variation
there is a uniform rank-one direction. Ward contracts \(P_f\) in this
direction exactly as at H3. The translation-invariant remainder is
annihilated by this contraction.

At \(t^{2\ell+1}\), the only remaining contributions are the two
next-score covariances and the first-tilt third cumulant. The first tilt
contains no degree beyond four. Its bilinear third cumulant vanishes
because the whitened PSD leading matrices have product zero.
The quartic third cumulant for orthogonal channels is the unshifted
wedge square, with coefficient one. Completing its electrical flow
removes exactly the uniform-mode second-score correction and produces
the shifted wedge in (13). This computation has no dependence on
\(\ell\) other than the external power of \(t\).

The assembly uses the same name \(a_\rho\) for a grounded potential
and its opposite-port-zero shift in Section 4. I recommended explicitly
writing the former as \(\widetilde a_\rho\), with
\(a_\rho=\widetilde a_\rho-k_\rho\), to make the covariance
correction's \(k_\rho\) unambiguous. The intended H3 calculation is
clear; this is a notation correction, not a missing algebraic term.

## 6. Invariant-compatible closure and the global conclusion

The previously audited geometry supplies disjoint enlarged interiors
with no joining edge and a nonempty remaining boundary. Union with the
old interior is essential; the global draft retains it. The full-range
argument also treats new ports adjacent only to the dormant old interior,
rather than falsely assuming every new port adjoins an actual response
support. The Gram's kernel is exactly boundary data constant on the full
new geometric port set. Hence it again spans the full contrast space.

Original marked current supports remain in their respective enlarged
regions, restoring fixed harmonic and Schur data. The intrinsic local
Ward identity remains exact. Scalar lower coefficients and the leading
bilinear coefficient were proved in Sections 3–4 above. Each continuing
step therefore genuinely restores every stated invariant with
\(\ell\) increased by one.

A singleton port set forces the entire original marked score to be
scalar by the exact one-port Ward identity, since \(1-tq\) is
invertible. It is an all-orders stop. It also gives ordinary graph
factorization at a one-vertex interface, hence exact marked independence.
Otherwise both nonzero response families add an old port to their
interiors. Finite strict growth while the interiors remain disjoint
and separated forces eventual termination at a positive trace, a
positive wedge, or exact independence.

The multiplier \(F(t)^2\) in the Rayleigh identity does not alter
the first nonzero mixed coefficient because every preceding mixed
coefficient has vanished. A negative first mixed logarithmic coefficient
therefore supplies a positive leading Rayleigh coefficient. This gives
eventual pairwise negative correlation. A singleton separating interface
cannot put two marked edges of the same cycle on opposite sides; such
a pair must reach a strict alternative. Distinct graphic-matroid
components already factor exactly.

No later Rayleigh coefficient is asserted positive, and the argument
does not supply a full-fugacity sum of squares. The finite numerical
response tests were not used to justify any of the analytic transitions
in this audit.
