P0309, w528 core-proof packet, 2026-10-10. Full problem unresolved; auxiliary deterministic results below are author-proved and await independent review by w530. No formal proof receipt or novelty claim is made.

**Exact target and provenance.** The recovered intake row op-p0309 requests existence of a crystalline Gibbs phase at sufficiently low positive temperature for the three-dimensional Coulomb or Riesz gas in the regimes predicted by Lewin's review. The full row and the old attempt are saved in P0309_EXTRACT.json. The row is a concept, labels its current status unverified, and supplies no quantitative definition of crystalline order. The public primary source is [Lewin, 2202.09240v2](https://arxiv.org/html/2202.09240v2), Section VI (especially VI.2), with zero-temperature context in IV.2. Its predicted 3D phases depend on the exponent and temperature. Its dated discussion is not a certificate of present openness. Current openness: UNKNOWN.

For the present lane, the precisely specified long-range model is the neutral canonical jellium Hamiltonian in STATEMENT_FOR_ADVERSARY.md, with dimension 3, 0<s<3, density rho>0, integer N=rho|Omega|, and finite inverse temperature beta. A full solution requires an unperturbed infinite-volume Gibbs state and a stated order criterion, such as a nonconstant lattice-periodic first intensity in a phase-selected state. A uniformly translated mixture can have constant first intensity even when its phases have order. No exterior potential, DLR limit, or order criterion is being silently supplied by the following charge estimates. The auxiliary estimates apply to K_s(x)=|x|^{-s} for every s>0, including the Coulomb value s=1.

**Prior-attempt digest and boundaries.** The recovered at-p0309 attempt computed the radial infrared integral for harmonic displacements around an assumed lattice: integral_0^1 r^{d-3}dr is finite in d=3 and logarithmically divergent in d=2. That author explicitly left defect control, anharmonic fluctuations, competing configurations, an infinite-volume Gibbs measure, and nontrivial positional order open. It had no independent review. Scoped searches of the named H/I attempt folders returned no P0309-specific text; the Lean ranking repeats the dated unsolved label and supplies no formal theorem. Team O's board has no P0309 row. This lane does not redo the phonon integral or BCC/FCC optimization. The statement-only A–C packet was prepared before this proof and routed to adversary w529; delivery receipts are saved separately. Referee: w530; w533 is reserved for any new mathematical result of w530.

**L1: neutral charges gain two powers of distance.** Let nu and mu be finite signed Borel measures, supported in B(0,a) and B(0,b), with zero total mass. Put M1(nu)=integral |x| d|nu|(x). For |z|>a+b,

|I_s(z)| <= s(s+1) M1(nu)M1(mu)(|z|-a-b)^{-s-2},

where I_s(z)=integral integral K_s(z+x-y)dnu(x)dmu(y).

Proof. Mass cancellation replaces K_s(z+x-y) inside the integral by K_s(z+x-y)-K_s(z+x)-K_s(z-y)+K_s(z). By the fundamental theorem of calculus this is minus integral_0^1 integral_0^1 D^2K_s(z+tx-uy)[x,y]dtdu. The Hessian has radial eigenvalue s(s+1)|w|^{-s-2} and tangential eigenvalues -s|w|^{-s-2}; its operator norm is s(s+1)|w|^{-s-2}. All w=z+tx-uy satisfy |w|>=|z|-a-b. Taking absolute values and integrating the two finite total variations proves the bound. These are deterministic integrals, not multiplied conditional probabilities.

**L2: vanishing dipoles gain another two powers.** Assume in addition integral x dnu(x)=integral y dmu(y)=0. Define M2(nu)=integral |x|^2 d|nu|(x) and C4(s)=s(s+2)(s^2+16s+51). Then

|I_s(z)| <= C4(s) M2(nu)M2(mu)/(4(|z|-a-b)^{s+4}).

Proof. Apply Taylor's formula with integral second-order remainder first in x, then in y. The constant and linear terms vanish by the two moment assumptions in each variable, leaving the exact identity

I_s(z)=integral_0^1 integral_0^1 (1-t)(1-u) integral integral D^4K_s(z+tx-uy)[x,x,y,y] dnu(x)dmu(y)dtdu.

To bound D^4, its coordinate formula at w is

s(s+2)(s+4)(s+6) w_i w_j w_k w_l |w|^{-s-8}
- s(s+2)(s+4) (delta_ij w_k w_l + the five other pair placements) |w|^{-s-6}
+ s(s+2) (delta_ij delta_kl + delta_ik delta_jl + delta_il delta_jk) |w|^{-s-4}.

Contracting against any four vectors v1,...,v4 and applying Cauchy-Schwarz bounds its absolute value by

s(s+2)[(s+4)(s+6)+6(s+4)+3] |w|^{-s-4} product_j |vj|
= C4(s)|w|^{-s-4} product_j |vj|.

The path stays away from zero. The two remainder weights integrate to 1/4. Finite total variation, compact supports, and this uniform derivative bound justify Fubini and give the asserted inequality, including for atomic signed measures.

**L3: a uniform cross-interaction bound, with its full hypotheses.** Put block centers c_i=L i for i in Z^3, with L>=4a>0. Let every compact signed block nu_i be supported in B(c_i,a), have zero mass and first moment about c_i, and have M2(nu_i)<=M. For any finite set I of blocks, even if all other blocks are present,

sum_{i in I} sum_{j not in I} |interaction(nu_i,nu_j)| <= J_s |I|,

J_s=(C4(s)M^2/4)(2/L)^{s+4}[24 zeta(s+2)+2 zeta(s+4)]<infinity.

Proof. For i!=j, |c_i-c_j|-2a >= (L/2)|i-j|. Apply L2. The infinity-norm shell |k|_infinity=n has exactly (2n+1)^3-(2n-1)^3=24n^2+2 integer points, and |k|>=n. Hence sum_{k!=0}|k|^{-s-4} is at most 24 sum_n n^{-s-2}+2 sum_n n^{-s-4}, which is finite for s>0. Summing the resulting per-block bound over I proves the claim. This bounds only these signed-block cross terms: the interaction with the reference lattice, local energies, a positive defect gap, and a physical repair map are separate inputs. Block radii and M must be uniform; grouping increasingly distant charges invalidates the stated constant.

**L4: neutrality alone does not give the needed absolute sum at or below Coulomb.** Let e=(1,0,0), nu=delta_e-delta_0, and I_s(z)=2K_s(z)-K_s(z+e)-K_s(z-e). For 0<s<=1,

sum_{z in 4Z^3, |z|>=16} |I_s(z)|=infinity.

Proof. Consider z=4(n,m,l), n>=4, |m|,|l|<=floor(n/4), and f(t)=K_s(z+te) for -1<=t<=1. Throughout this interval the squared cosine with e is at least 9/11 and |z+te|<=6n. Thus

f''(t)=s |z+te|^{-s-2}[(s+2)(z_1+t)^2/|z+te|^2-1]
>= (7s/11)(6n)^{-s-2}.

The exact central-difference identity gives -I_s(z)=integral_{-1}^1 (1-|t|) f''(t)dt, so |I_s(z)|>=(7s/11)(6n)^{-s-2}. There are (2floor(n/4)+1)^2>=n^2/16 such centers for each n. Distinct n give distinct centers, and the total contribution at n is therefore at least 7s/(176*6^{s+2}) n^{-s}. The p-series diverges for 0<s<=1. This proves absolute divergence on an explicit separated set, not just an upper-bound failure or an angular heuristic. Conditional angular cancellation, renormalization, and collective screening remain possible; this is not a counterexample to crystallization.

Two exact Coulomb controls are I_1(R e)=-2/[R(R^2-1)] for R>1, and, for q=delta_e+delta_{-e}-2delta_0, interaction(q,q+R e)=24/[R(R^2-1)(R^2-4)] for R>2. The first decays as R^-3 and the second as R^-5. The axial R^-3 series by itself converges; the cone count above is essential to establish the 3D absolute divergence.

**L5: a physical dipole cannot be removed by recentering or finite regrouping.** For a neutral measure nu, integral(x-c)dnu(x)=integral x dnu(x), independent of c. First moments are additive. Consequently a neutral measure with nonzero first moment cannot be a finite sum of dipole-free neutral measures. In particular a single displaced particle relative to its reference position gives delta_{c+u}-delta_c, with mass zero and dipole u. It satisfies L2 only if u=0. Likewise a point against a symmetric unit-volume cell background has dipole u when displaced by u from the cell center. Thermal displacements therefore do not automatically satisfy L2.

**L6: the precise conditional repair estimate, without independence.** Let a finite-volume canonical reference measure be lambda, Z=integral exp(-beta H)dlambda, and P_beta=Z^{-1}exp(-beta H)lambda. Suppose a contour gamma of size m has event E_gamma and a measurable repair map T_gamma:E_gamma->configuration space such that (i) H(x)-H(T_gamma x)>=tau m for lambda-a.e. x in E_gamma, and (ii) (T_gamma)_#(lambda restricted to E_gamma)<=exp(kappa m)lambda as measures. Then

P_beta(E_gamma)<=exp[-(beta tau-kappa)m].

Proof. The energy inequality bounds integral_E exp(-beta H(x))dlambda(x) by exp(-beta tau m) integral_E exp(-beta H(Tx))dlambda(x). The pushforward inequality bounds the latter integral by exp(kappa m)Z. Divide by Z. This argument requires neither contour independence nor a product of per-row conditional estimates. If at most A^m contours of size m cover a given marked block, and its bad event is contained in their union, then its bad probability is at most q/(1-q) when q=A exp(kappa-beta tau)<1. The counting and event-cover assumptions must be proved for the chosen contours.

**Attempt at the hardest missing lemma G, and its failure point.** G is a volume-uniform crystalline reconstruction estimate for the actual jellium law: phase-selected boundary conditions, an explicit core-defect contour definition, admissible same-N repairs, a strictly positive tau, and a finite kappa satisfying L6, while the charge/dipole sector and all competing configurations are controlled. The estimate must be derived from the real Riesz Hamiltonian; a lattice assumed globally optimal does not establish it. The old attempt already identifies this as the unresolved bridge from a harmonic crystal to the full law.

The natural first route is to assign defects to small neutral blocks, apply L3 to bound the worst far-field loss by J_s m, and prove a local repair gain tau_0 m with tau_0>J_s. This would yield the energy part of L6. L4 and L5 show exactly why this route currently fails for actual Coulomb defects: the signed charges of ordinary displacements have nonzero dipoles; they cannot all be made dipole-free by changing block centers or finite regrouping. Pairing opposite dipoles works only when the actual total dipole cancels and pair distances stay bounded. A boundary dipole carrier, if introduced, needs its own quantitative energy and entropy bound. None has been proved here.

There is a second concrete obstruction to a naive repair. Sending an open positive-lambda-volume set of displaced particles to exactly fixed lattice sites maps it into a lambda-null set. Then its pushforward has positive mass on a null set, contradicting L6(ii) for every finite kappa. Thus an energy-lowering “put every particle back on its site” map cannot by itself bound a positive-temperature Gibbs probability. A nondegenerate, finite-multiplicity repair must retain and account for configuration volume. The collapse obstruction is proved by evaluating the supposed pushforward inequality on the null image.

Even a valid core-defect estimate would still need phonon/anharmonic phase coherence, an unperturbed Gibbs limit, and an order observable. They are not claimed as automatic consequences of L6. G is the hardest bridge isolated in this lane, not a claim that the rest of the full problem has been solved.

**Validation and handoff.** The proofs above are analytic and author-only. A bounded deterministic checker will verify exact rational controls, derivative identities, cone geometry, and bundle structure; these checks do not prove G. CLAIMS.jsonl keeps theorem scope, reviewer, status, and remaining gap separate. DRAFT brain entries must preserve these distinctions and use owner-own-work for this campaign's own derivations.

NEXT: Construct an admissible two-cell repair with an explicit dipole carrier, then bound its exact energy loss and pushforward density before asserting any volume-uniform crystalline reconstruction estimate.
