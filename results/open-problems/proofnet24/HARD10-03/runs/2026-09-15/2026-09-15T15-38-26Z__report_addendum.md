# HARD10-03 addendum — spatial exclusion for finite cycles

**SOLUTION STATUS: PARTIAL**

This append-only addendum records one further consequence obtained after the main report

`proofnet24/HARD10-03/runs/2026-09-15/2026-09-15T15-34-11Z__report.md`

was already durably committed. It does not replace that report.

## 1. Infinite-volume finite-support extension of the master determinant identity

Let \(P=\pi_\beta\) be the infinite-volume interchange permutation on \(\mathbb Z^3\), acting unitarily on \(\ell^2(\mathbb Z^3)\), and let \(p_\beta=e^{\beta L}\) be the one-particle continuous-time simple-random-walk semigroup.

For every finite set \(S\subset\mathbb Z^3\), let \(D_S\) be multiplication by \(\mathbf1_S\). Then \(D_SP\) and \(D_Sp_\beta\) are finite-rank, so their Fredholm determinants are ordinary finite determinants after restriction to the nonzero row space.

For a finite subset \(T\subset S\),
\[
\det P[T,T]
=
\langle e_T,(\bigwedge^{|T|}P)e_T\rangle,
\]
where \(e_T\) is the canonical wedge vector. The edge-by-edge exterior-generator identity from NEW-L4 in the main report extends directly to the bounded-degree infinite lattice on every fixed exterior degree:
\[
\mathbb E[\bigwedge^jP]
=
\bigwedge^j p_\beta.
\]
Therefore
\[
\mathbb E\det P[T,T]
=
\det p_\beta[T,T].
\]
Expanding the finite-rank Fredholm determinant in principal minors gives
\[
\boxed{
\mathbb E\det(I-D_SP)
=
\det(I-p_\beta[S,S]).
}
\tag{A.1}
\]

For a deterministic permutation of an infinite set, every orbit which only partially intersects \(S\) contributes a nilpotent broken path to \(D_SP\), hence determinant factor one; every permutation cycle wholly contained in \(S\) contributes factor zero at fugacity one. Consequently
\[
\det(I-D_SP)
=
\mathbf1_{\{\text{no permutation cycle is wholly contained in }S\}}.
\]
Thus the finite-graph NEW-L6 from the main report has the exact infinite-volume finite-support form
\[
\boxed{
\mathbb P\bigl(\exists\text{ a }\pi_\beta\text{-cycle wholly contained in }S\bigr)
=
1-\det(I-p_\beta[S,S]).
}
\tag{A.2}
\]

## 2. New spatial confinement bound for the root cycle

Because \(p_\beta\) is a positive self-adjoint contraction, every eigenvalue \(\theta_i\) of the finite principal matrix \(p_\beta[S,S]\) belongs to \([0,1]\). Hence
\[
1-\det(I-p_\beta[S,S])
=
1-\prod_i(1-\theta_i)
\le
\sum_i\theta_i
=
\operatorname{Tr}p_\beta[S,S].
\]
By translation invariance on \(\mathbb Z^3\),
\[
\operatorname{Tr}p_\beta[S,S]
=|S|p_\beta(0,0).
\]
If \(0\in S\), the event that the root cycle is finite and wholly contained in \(S\) is a subset of the event in (A.2). Therefore:

## NEW-L7 — PROVED

For every finite \(S\subset\mathbb Z^3\) containing the origin,
\[
\boxed{
\mathbb P\bigl(\operatorname{Cycle}_{\pi_\beta}(0)\subseteq S\bigr)
\le
1-\det(I-p_\beta[S,S])
\le
|S|p_\beta(0,0).
}
\tag{NEW-L7}
\]

The standard three-dimensional heat-kernel bound
\[
p_\beta(0,0)\le C\beta^{-3/2},\qquad \beta\ge1,
\]
gives
\[
\boxed{
\mathbb P\bigl(\operatorname{Cycle}_{\pi_\beta}(0)\subseteq S\bigr)
\le C|S|\beta^{-3/2}.
}
\tag{A.3}
\]

For the \(\ell^\infty\)-ball
\[
B_R=[-R,R]^3\cap\mathbb Z^3,
\]
\[
|B_R|=(2R+1)^3,
\]
so
\[
\boxed{
\mathbb P\bigl(\operatorname{Cycle}_{\pi_\beta}(0)\subseteq B_R\bigr)
\le C(2R+1)^3\beta^{-3/2}.
}
\tag{A.4}
\]
In particular, for every \(\varepsilon>0\), taking
\[
R_\beta=\lfloor\beta^{1/2-\varepsilon}\rfloor
\]
yields
\[
\boxed{
\mathbb P\bigl(\operatorname{Cycle}_{\pi_\beta}(0)\subseteq B_{R_\beta}\bigr)
=O(\beta^{-3\varepsilon})\to0.
}
\tag{A.5}
\]

Thus, in addition to the earlier result that a finite root cycle has more than \(\beta^{1/2-\varepsilon}\) permutation iterates with high probability, we now have a genuinely spatial statement: with high probability the root cycle, if finite, is not confined to any subdiffusive ball of radius \(\beta^{1/2-\varepsilon}\).

This conclusion is unconditional on previous cyclic entanglements and does not use chronological transience as a surrogate for cycle behavior.

## 3. Limitation

NEW-L7 does not solve the conjecture. For fixed \(\beta\), every finite cycle is contained in some sufficiently large finite ball, while the upper bound \(C|B_R|\beta^{-3/2}\) becomes useless once \(R\) reaches the diffusive scale and beyond. The theorem is therefore a quantitative large-\(\beta\) spatial-delocalization statement, not a fixed-\(\beta\) proof of infinite cycles.

Its likely use is in a multiscale argument: any hypothetical large-\(\beta\) finite cycle must simultaneously have many orbit iterates and diffuse over at least a nearly \(\sqrt\beta\) spatial scale before closing.

## 4. Reproducible certificate added after the main report

A finite-state checker for the master determinant identity and its spatial-avoidance corollary has been added at

`proofnet24/HARD10-03/artifacts/2026-09-15T15-34-11Z__master_determinant_check.py`.

It enumerates all \(4!\) interchange states on \(C_4\), evaluates the exact finite-state semigroup by matrix exponentiation, and checks five deterministic random matrices \(A\) in
\[
\mathbb E\det(I-A\Pi_t)=\det(I-Ap_t),
\]
as well as
\[
\mathbb P(\text{no cycle is wholly contained in }\{0,1\})
=
\det(I-p_t[\{0,1\},\{0,1\}]).
\]
The locally executed version gave maximum determinant discrepancy below \(9\times10^{-16}\) and spatial-avoidance discrepancy below \(6\times10^{-16}\). This is only a numerical sanity check; the proof is analytic.

Artifact commit receipt:

`5d976c65d53bf954b4de07baff7762987d377c9d`

Readback blob:

`bd288a8d52a50ca6b2d6f09164d7466516807ddc`.

The artifact was read back at that exact commit, so its **delivery status is VERIFIED**. Mathematical verification remains self-review.

## 5. Updated next attack

The determinant identity now gives exact spatial exclusion information, while the Alon–Kozma cutoff formula in the main report gives exact low-degree representation information for long cycles. A useful next synthesis is to test whether the low-degree non-fermionic terms in the torus long-cycle formula can be localized to boxes of radius comparable to \(\sqrt\beta\) and bounded by a defect expansion around the exact fermionic determinant. The target remains a sign-preserving estimate on the entire alternating block, not termwise absolute bounds.
