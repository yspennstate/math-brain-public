# P0309 core audit: what the compact-defect estimates do not prove

Independent checkpoints C1-C3 were saved before the paired mathematical statement was read. On 2026-10-10 I read w528/STATEMENT_FOR_ADVERSARY.md. It specifies an explicitly narrowed 0<s<3 neutral canonical jellium target and isolates compact mass/dipole cancellation estimates. It expressly leaves the Gibbs comparison, ground-state gap and Bragg order open. No completed proof of the full target was supplied at that point.

The important missing lemma is an unrestricted, volume-uniform free-energy comparison for real continuum defects, compatible with the moment conditions required by the far-field estimate. It must provide an entropy-controlled repair, not merely decaying interactions between hypothetical dipole-free signed measures. A valid comparison also needs the exterior term, particle count, phase/phonon degrees of freedom and eventual Gibbs limit. C4 concerns s>3 ordinary grand-canonical DLR and is not a counterexample to w528's long-range canonical model.

## Concrete counterexample to the energy-to-probability shortcut (C6)

Fix beta,tau>0. For each integer n>=1 use Lebesgue measure on [0,1]. Set ell_n=exp(-n^2), H_n(x)=0 on [0,ell_n], and H_n(x)=tau n elsewhere. Every bad point has an extensive energy gap tau n over every good point. Nevertheless the Gibbs probability of the bad set is

P_n(bad)=(1-ell_n) exp(-beta tau n) / [ell_n+(1-ell_n) exp(-beta tau n)]
         =(1-ell_n)/[exp(-n^2+beta tau n)+1-ell_n] -> 1.

This is a counterexample to inferring an exponentially small defect probability from an extensive pointwise energy gap alone. It is not a Riesz counterexample. The missing premise is a suitable control of the ratio of phase-space volumes (or of a repair map's multiplicity and Jacobian). In this example the good sector's entropy loss n^2 defeats the energy gain beta tau n at every fixed beta.

## A sufficient comparison premise, stated exactly

Let a finite-volume Gibbs law have Lebesgue density Z^{-1}exp(-beta H) on Omega subset R^D. For a bad contour event B_Gamma suppose a piecewise C^1 map T_Gamma:B_Gamma->Omega obeys the area formula, has multiplicity at most M_Gamma almost everywhere, |det DT_Gamma|>=J_Gamma>0 almost everywhere, and H(x)-H(T_Gamma x)>=Delta_Gamma for almost every x in B_Gamma. Then

P(B_Gamma)<= (M_Gamma/J_Gamma) exp(-beta Delta_Gamma).

Proof: multiply the bad density by exp(-beta Delta_Gamma), replace H(x) by H(Tx), use dx<=|det DT| dx/J_Gamma, and apply the area formula with the multiplicity bound. The resulting image integral is at most M_Gamma Z. The required area-formula hypotheses, nonzero Jacobian, and energy inequality are real proof obligations. No independence between contours is invoked.

If Delta_Gamma>=tau |Gamma|, M_Gamma/J_Gamma<=exp(h |Gamma|), and the number of size-n contours at the observed site is at most A^n, then the union bound is at most q/(1-q) for q=A exp(h-beta tau)<1. This conditional implication is not a construction of T_Gamma for Riesz gas. It gives the exact form of the hardest open input.

## Why an exact rigid repair cannot justify that premise

For k>=2 labeled particles, a map whose output is only a rigid translation of a fixed k-point template has image contained in a three-dimensional affine subspace of R^{3k}. It has zero 3k-dimensional Lebesgue measure. For a differentiable such map on an open domain, rank(DT)<=3 and det(DT)=0. A finite union over label permutations is still null. On a positive-volume domain such a repair cannot obey both the area formula and J_Gamma>0. A valid continuum comparison must retain a full-dimensional family of phonon/defect configurations and control its entropy. This is an obstruction to that proposed repair class, not to every possible repair map or to crystallisation.

Verdict on the supplied statement packet: no overclaim to reject; it correctly records the Gibbs-comparison gap. Retain the auxiliary estimates only in their stated scope. Request the repair map with its energy and entropy bounds before labeling the full target proved.

## Subsequent audit of the actual paired proof

I subsequently read w528/ATTEMPT.md, containing L1-L6 and its failed attempt at reconstruction input G. The mass/dipole Taylor arguments keep the interpolation paths outside the singularity; the double second-order remainder has weight 1/4; the Coulomb cone count supplies the three-dimensional divergence rather than relying on a convergent axial series. The shell estimate in L3 is conditional on uniformly bounded compact dipole-free blocks and does not include their interaction with the reference lattice. Those scopes are explicitly acknowledged in the proof.

L6 is mathematically sound under its stated pushforward domination premise. It uses the full joint Gibbs integral, not a product of single-block probabilities. My C7 is a smooth finite-multiplicity sufficient case of its premise. My C6 refutes omitting the entropy condition; it does not refute L6, which explicitly includes that condition. Likewise the actual proof already acknowledges the null-image obstruction to exact lattice repair. The most important unresolved step is G: deriving both of L6's hypotheses for real configurations, including the dipole carrier, full exterior energy, and all competing states. Neither the fourth-derivative bound nor numerical controls prove G.

No counterexample to L1-L6 was found in this audit. The minimal missing premise for the proposed full-target route is a volume-uniform same-particle-count reconstruction with positive energy gain and finite exponential pushforward-density bound under the real Hamiltonian, together with the separate phase-coherence and Gibbs-limit inputs. Current openness of the full title remains UNKNOWN.

NEXT: Construct or refute a full-dimensional dipole-controlled repair with the comparison bound above; a replacement may instead use a derived collective-screening argument.
