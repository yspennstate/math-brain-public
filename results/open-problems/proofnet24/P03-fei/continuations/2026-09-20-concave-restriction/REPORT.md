# FEI: a concave restriction cap, dyadic rigidity, and shared-control envelopes

20 September 2026. Continuation of the directional-compression package for Yitzchak Shmalo.

**Full FEI remains unproved.** The results below improve an actual local payment coefficient, characterize equality in a sharper universal restriction bound, and give a valid replacement envelope for a shared-control inequality that the preceding report disproved. The proofs are complete within this note, but independent review and publication-priority clearance have not been obtained. The finite checker is not a formal proof assistant.

## 1. Definitions and exact fibre identity

For Boolean f on the uniform binary cube, use normalized Walsh coefficients and Fourier entropy in bits. Write alpha_i=Inf_i(f), j_i=min(alpha_i,1-alpha_i), and J=sum_i j_i. Let

    Delta_i H = H(f) - [H(f^{i=0}) + H(f^{i=1})]/2.

At a Fourier fibre T not containing i put u=fhat(T), v=fhat(T+i), w=u^2+v^2. For w>0 define

    t_T = min(u^2,v^2)/w,        M_i = sum_T w t_T,
    V_i = sum_T w (t_T-M_i)^2.

Parseval gives sum_T w=1, and 0<=M_i<=j_i<=1/2. Zero fibres are omitted. Define

\[
\Psi(t)=h_2(t)+1-h_2\!\left(\frac12+\sqrt{t(1-t)}\right),
\qquad 0\le t\le\frac12.
\tag{1}
\]

The endpoints are Psi(0)=0 and Psi(1/2)=2. Directly from the child coefficients u+v and u-v,

\[
\boxed{\Delta_iH(f)=\sum_T w_T\Psi(t_T).}
\tag{2}
\]

Indeed the contribution of u,v to the parent entropy is w[h_2(t)-log_2 w]. The corresponding half-sum of child contributions is w[h_2(1/2+sqrt(t(1-t)))-1-log_2 w]. Their difference is w Psi(t). Signs only swap the two child masses, so folding t loses no information.

This is a repackaging of the existing erasure/JS fibre identity, not a claim that the underlying restriction formula is new.

## 2. A complete concavity calculation

Put x=1-2t, r=sqrt(1-x^2), and E(x)=h_2((1-x)/2). Then Psi(t)=1+E(x)-E(r). On the open interval, E'(x)=-atanh(x)/ln 2 and E''(x)=-1/[(1-x^2)ln 2]. Differentiating twice, the terms 1/(r^2 ln 2) cancel and give

\[
\frac{d^2}{dx^2}[1+E(x)-E(r)]
=-\frac{\operatorname{atanh}r}{r^3\ln2}.
\]

Consequently

\[
\boxed{\Psi''(t)=
-\frac{4\operatorname{atanh}(2\sqrt{t(1-t)})}
{[2\sqrt{t(1-t)}]^3\ln2}<0.}
\tag{3}
\]

Continuity supplies the endpoints. Psi is strictly concave and increasing on [0,1/2]; for example the first derivative in x is

    -[atanh(x) + x atanh(r)/r]/ln 2 < 0.

Since atanh(r)>=r and 0<r<=1, (3) also gives Psi''<=-4/ln 2. Thus t -> Psi(t)+(2/ln 2)t^2 is concave. Jensen's inequality in (2) proves

\[
\boxed{
\Delta_iH(f)\le\Psi(M_i)-\frac{2}{\ln2}V_i
\le\Psi(M_i)\le\Psi(j_i).
}
\tag{4}
\]

The explicit variance term is a valid credit, not a proposed unproved cancellation. The constant 2/ln 2 in this credit is convenient, and is not asserted optimal.

For comparison, the preceding package used

    Delta_i H <= min(2, h_2(j_i)+2j_i/ln 2).

The sharper bound retains the dependence between the two parts of the fibre entropy rather than bounding them separately. No improvement to the previously sharp coefficient 2/ln 2 in the isolated JS bound is asserted.

## 3. Equality is rigid for dyadic Boolean spectra

Strict concavity says Delta_i H=Psi(M_i) exactly when all nonzero fibres have the same t_T. For Boolean Walsh coefficients this can happen only at the endpoints:

\[
\boxed{
\Delta_iH=\Psi(M_i)
\quad\Longleftrightarrow\quad
M_i=0\ \text{or}\ M_i=\frac12.
}
\tag{5}
\]

**Proof of the nontrivial direction.** Write U_T=2^n u_T, W_T=2^n v_T, which are integers. If all t_T agree, choose coprime nonnegative integers a,b representing the common unordered ratio |U_T|:|W_T|. Each nonzero pair is, up to signs and order, k_T(a,b), with k_T a nonnegative integer. Parseval gives

\[
2^{2n}=(a^2+b^2)\sum_T k_T^2.
\]

Therefore a^2+b^2 is a power of two. Coprimality rules out both being even. If both are odd, their square sum is 2 modulo 4, hence equals 2 and a=b=1. If exactly one is odd, the sum is odd, hence equals 1 and {a,b}={0,1}. These are t=1/2 and t=0. The converse follows from (2), since a mean of bounded t-values at an endpoint forces all values to be at that endpoint. QED.

This argument uses dyadic integrality and Parseval; it is not claimed to exhaust all consequences of f^2=1. It proves strictness in (4) for 0<M_i<1/2, not a dimension-independent lower bound on the strictness gap.

At M_i=0, each parent fibre has at most one nonzero coefficient, so the two children have identical squared Fourier spectra and Delta_i H=0. This recovers the prior isospectral case. At M_i=1/2, every fibre has |u|=|v|, the two children have disjoint Fourier supports, and Delta_i H=2. These characterize the endpoints.

For unrestricted real normalized amplitudes the scalar cap is optimal: take two fibres with u=(sqrt(1-t)/sqrt(2),sqrt(1-t)/sqrt(2)) and v=(sqrt(t)/sqrt(2),-sqrt(t)/sqrt(2)). Both child vectors u+v and u-v have norm one and equality holds. These vectors are not asserted to be Boolean Walsh spectra. Accordingly, no sharpness of the numerical coefficient below among Boolean functions is claimed.

## 4. Improved directional-compression constants

Concavity and Psi(0)=0 imply that Psi(t)/t decreases on (0,1/2]. Define

\[
\widetilde\kappa_d=2^d\Psi(2^{-d}),\qquad d\ge1.
\tag{6}
\]

Whenever j_i>=2^{-d}, (4) gives Delta_i H<=tilde_kappa_d j_i. The directional-compression theorem in the recovered report can therefore use tilde_kappa_d in place of its older kappa_d, with no change to the proof of the directional certificate or the physical restriction tree. In particular,

\[
\boxed{
\widetilde\kappa_2
=4\left[h_2(1/4)+1-h_2((2+\sqrt3)/4)\right]
=5.826796887175\ldots .
}
\tag{7}
\]

The checker rigorously encloses (7) between 5.8267968871754 and 5.8267968871756. The preceding coefficient was 6.130502579614458..., so this is a smaller sufficient payment, not merely a relabeling.

Precisely: let V_d(P)={v:deg(D_vP)<=d} for f=(-1)^P and algebraic degree over F_2. If r=dim V_d(P), there is an r-step physical restriction tree whose leaves have n-r variables. If those leaves satisfy H<=C_0 J, then

\[
\boxed{H(f)\le\max\{C_0,\widetilde\kappa_d\}J(f).}
\tag{8}
\]

The same holds for I with the corresponding leaf certificates. To reconstruct the argument: a nonconstant degree-at-most-d directional derivative forces some physical j_i>=2^{-d}; a constant directional derivative gives a zero-cost pivot. Query that coordinate. Intersect the inherited direction space with the coordinate hyperplane, losing at most one dimension, and continue. The inequality E J(child)<=J(parent)-j_i pays the tree upward at the maximum coefficient, not a sum of coefficients.

Thus a minimal-dimensional counterexample to any candidate constant C>=tilde_kappa_2 must still have V_2(P)={0}, now at this smaller threshold. The robust certificate with error epsilon<2^{-d} similarly improves to the payment

    Psi(2^{-d}-epsilon)/(2^{-d}-epsilon).

For an approximately constant signed derivative, the previous affinity estimate M_i<=epsilon improves its absolute entropy charge to Psi(epsilon), for epsilon<=1/2. The logarithmic small-error behavior survives; Section 6 states the resulting limitation explicitly.

The constant in (7) is a restriction-payment coefficient and a compression transfer floor. It is NOT a proved universal FEI constant.

## 5. A valid tensorizing envelope for shared controls

Let a_l(t,x_l) be Boolean functions with mutually disjoint residual physical blocks x_l and one shared physical coordinate t. Set F(t,x)=prod_l a_l(t,x_l). For each factor, let A_l and B_l be the Fourier amplitude vectors of its two t-children, and put

\[
\mathfrak a_l=\sum_S|A_l(S)B_l(S)|,
\qquad M_l=(1-\mathfrak a_l)/2.
\]

For the product, the child amplitude vectors are tensor products. Their affinity is therefore exactly multiplicative:

\[
\mathfrak a(F)=\prod_l\mathfrak a_l,
\qquad
M(F)=\frac{1-\prod_l(1-2M_l)}2.
\tag{9}
\]

Combining with (4) gives the uniform replacement

\[
\boxed{
\Delta_tH(F)\le
\Psi\!\left(\frac{1-\prod_l(1-2M_l)}2\right)
\le\sum_l\Psi(M_l).
}
\tag{10}
\]

Here is a direct proof of the final inequality. For s,t in [0,1/2], define s star t=s+t-2st. If s+t<=1/2, concavity and Psi(0)=0 imply Psi(s)+Psi(t)>=Psi(s+t)>=Psi(s star t). If s+t>=1/2, the chord inequality Psi(u)>=4u gives Psi(s)+Psi(t)>=2>=Psi(s star t). Induct over the factors.

Equation (10) is an upper bound that tensorizes. It does NOT reinstate the false inequality Delta_tH(F)<=sum_l Delta_tH(a_l). The actual decrements can lie strictly below their individual caps, and those gaps cannot be discarded. The six-variable/eleven-variable counterexample in the recovered package remains valid and unchanged.

No independence of the two children of a factor is assumed. The residual blocks of different factors must be disjoint. Arbitrary overlapping residual cores do not have the tensor amplitude identity (9).

## 6. Attempt at universal closure and the precise failure

A natural next move is to try using Psi(M_i) as a universally payable coordinate selector. This does NOT work alone: even all-coordinate selection fails for this envelope.

Take the one-point defect f_n=1-2*1_{x=0} with n>=3. Its Fourier coefficients are 1-2^(1-n) at the empty set and -2^(1-n) elsewhere. Every coordinate has

    j_i=M_i=2^(1-n).

The identity M_i=j_i follows by summing the minimum squared coefficient over the 2^(n-1) fibres; in the empty-set fibre the smaller coefficient has the same magnitude as all nonempty coefficients. A direct Taylor expansion of (1) gives

\[
\Psi(t)=t\log_2(1/t)+\frac{3}{\ln2}t+O(t^2),
\qquad t\downarrow0.
\]

Consequently, for every coordinate,

\[
\frac{\Psi(M_i)}{j_i}
=n-1+\frac{3}{\ln2}+o(1)\longrightarrow\infty.
\tag{11}
\]

This function itself satisfies FEI by existing symmetric-function results. Equation (11) refutes only the stronger proposal that the affinity cap always supplies a constant-paid coordinate. The older project already identified the one-point marginal-entropy obstruction; its appearance here is an explicit scope test, not relabeled as a newly discovered family.

The exact profile identity (2), unlike its Jensen envelope, retains the location-dependent distribution of t_T. The variance credit in (4) is valid but is not shown to compensate the entire logarithmic loss universally. Nor does replacing kappa_2 by tilde_kappa_2 guarantee a nonzero space V_2. Full FEI still needs a universal payment for the surviving core, an appropriate certified stopping class, or a genuinely influence-summable error ledger.

## 7. Actual verification

Run `python verify_concave_cap.py` with Python >=3.10 and NumPy. The assertions use integer Walsh transforms, exact rational arithmetic, and outward rational enclosures for logarithms and square roots. The logarithm enclosure is the 48-term atanh series after range reduction. Square roots use integer square roots on a denominator 2^180 grid. Endpoint/equality cases use exact algebraic certificates rather than tolerances.

The actual output records:

- All 65,812 Boolean functions in dimensions 1--4 and all 262,948 coordinate splits. There are 23,972 equality splits; all have M=0 or M=1/2. The 20 distinct fibre profiles are checked with exact rational certificates, including the variance credit in (4).
- Every pair of three-variable Boolean parents sharing one coordinate: 65,536 pairs, all exact product-affinity identities and cap checks. These induce nine distinct affinity pairs.
- 80 reproducibly sampled products of three to five such parents, with up to eleven physical variables.
- 1,089 rational-grid affinity-envelope comparisons and the rigorous interval for (7).
- Across all families, 71 distinct fibre profiles were checked. Cached profiles are not described as independently checked distinct Boolean functions beyond the stated enumerations.

Finite checks supplement the proofs in Sections 1--6. They neither prove unrestricted FEI nor constitute independent mathematical review or Lean formalization.

## 8. Sources, provenance, and scope control

The original directional-compression package was recovered from the actual conversation files and uploaded without changing its report, checker, output or handoff bytes. The report blob is `011865c0e85cc90c8af59bd9033173603ee5ebe0`; checker blob `e0d518097b8cb0d2c644bcdbcd02fd9d9e1467cc`; output blob `992fb6a9f592a25f477c5dc98420a03a19a40fe1`; handoff blob `0d31367092d80d826a5cb8dc087d9dfad563b34e`. All were read back and matched the local Git blob hashes. The exact original checker was replayed and produced byte-identical output. The original pending-delivery wording is historical and is superseded only as to delivery by the separate DELIVERY.md.

Consumed mathematical source: `proofnet24/P03-fei/continuations/2026-09-20-directional-compression/REPORT.md`, read in full. Reused with unchanged hypotheses: its directional certificate, inherited-subspace physical compression, signed-symmetry affinity estimate, and the disproof of raw shared-control subadditivity.

Current FEI entrypoint read: `proofnet24/P03-fei/README.md`, blob `be66b9115a00b721b72b262dd595fbebd49f5ff3`. Its newer affine-fibre gluing statement was consulted for scope; this report does not use any uninspected affine-fibre proof as a premise.

External primary source consulted on 20 September 2026: Maria Jose Gonzalez, Paul MacManus and Maria Cristina Pereyra, *Further evidence towards the Fourier Entropy-Influence conjecture*, arXiv:2606.00246v2, revised 9 June 2026, https://arxiv.org/abs/2606.00246 . It supplies context for existing restriction/stopping-tree methods; those methods are not claimed new here. The published symmetric-function input is O'Donnell--Wright--Zhou, ICALP 2011, DOI 10.1007/978-3-642-22006-7_28, consulted through the publisher record and credited by the recovered report.

Bounded searches did not establish publication priority for the exact cap/rigidity/compression improvement. No assertion of first discovery is made. The scalar fibre identity is explicitly inherited; the all-dimensional concavity proof, variance credit, dyadic equality proof, smaller payment and corrected product envelope are the mathematical additions of this continuation.

Superseded targets checked: no use of the false raw shared-control subadditivity, pointwise H<=B+(2/ln2)I, absolute-overlap selector, full-resolvent inequalities, fixed-coefficient affine drift, or unproved universal affinity-cap selector. Full FEI remains open in this work. No schedules, permissions, ownership, or unrelated files are altered by these proofs.
