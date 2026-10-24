P0309 independent obstruction and conditional bridge (w538, 2026-10-10)

Independence: This checkpoint was saved before reading any w537 proof or ATTEMPT file. Sources inspected: dated P0309 ranking; Lewin arXiv:2202.09240v2, Definition 15, Section VI opening, and the distinction from Conjectures 35/38. Current openness: UNKNOWN. The ranking and 2022 survey establish only dated provenance. The survey describes a finite-temperature periodic Gibbs phase but does not attach a unique exponent range and full quantifier package to this intake title. Work below is on an explicitly bounded surrogate, not a proof of P0309.

Independent obstruction O1 (exact computation)
For s>0 and x!=0 in R^3, V_s(x)=|x|^{-s} has
D^2 V_s(x)=s|x|^{-s-2}[(s+2)ee^T-I], e=x/|x|.
Its radial eigenvalue is s(s+1)|x|^{-s-2}, but both transverse eigenvalues are -s|x|^{-s-2}. Thus convexity of r -> r^{-s} does not imply convexity in vector displacements. A concrete two-particle path x(t)=(1,t,0) has V_s(x(t))=(1+t^2)^{-s/2} and second derivative at t=0 equal to -s. Any attempt to apply a convex Gibbs variance inequality to the full Riesz energy requires a separately proved lower bound for the assembled Hessian; positivity cannot be obtained term by term. This counterexample does not show that a full lattice Hessian is unstable: other bonds and the background can compensate.

Candidate bridge B1 (conditional special case; pending w539)
Fix any finite nonempty D subset Z^3. On R^{3|D|}, let u=(u_x) and let L_D be the Dirichlet lattice Laplacian: diagonal 6, off-diagonal -1 for nearest neighbors in D, boundary coordinates fixed to zero. Suppose H_D is C^2 on all of R^{3|D|}, even (H_D(-u)=H_D(u)), and
D^2 H_D(u) >= kappa (L_D tensor I_3) for every u,
with the same kappa>0 for all D. Let beta>0 and dP_D=Z_D^{-1} exp(-beta H_D(u)) du. For every nonzero G in 2pi Z^3, set
B_{D,G}=|D|^{-1} sum_{x in D} exp(i G dot (x+u_x)).
Define
C_3=(2pi)^{-3} integral_{[-pi,pi]^3} [2 sum_j(1-cos q_j)]^{-1} dq.
Then C_3 is finite and
Re E B_{D,G} >= 1 - |G|^2 C_3/(2 beta kappa).
Consequently, if a=1-|G|^2 C_3/(2 beta kappa)>0, E|B_{D,G}|^2>=a^2 uniformly in D.

Proof: Strong convexity in each finite D gives integrability and all linear moments; evenness gives E u_x=0. The Brascamp-Lieb variance inequality for the potential beta H_D and f(u)=G dot u_x gives
Var(G dot u_x) <= |G|^2 (L_D^{-1})_{xx}/(beta kappa).
The inverse inequality follows from the assumed matrix lower bound and order reversal of positive definite matrices. The killed simple-random-walk expansion of L_D^{-1} is bounded by the unrestricted Green series; equivalently its diagonal is at most C_3. Finiteness follows from the integrable |q|^{-2} singularity in dimension three. Since cos t >= 1-t^2/2 and e^{iG dot x}=1, averaging over x proves the real-part bound. Jensen gives E|B|^2 >= |EB|^2 >= a^2. No independence among displacements is used. Using 1-cos t >= 2t^2/pi^2 for |t|<=pi and enclosing the Fourier cube in the radius sqrt(3)pi ball also gives the loose explicit bound C_3<=sqrt(3)pi/8.

Hardest missing piece
No argument here establishes the Hessian comparison, centered phase, lattice labeling, or control of vacancies/dislocations under an actual continuum Riesz Gibbs specification. The full interacting Riesz energy is not an even globally convex displacement potential. Conditioning on a defect-free neighborhood changes the measure and is not the unconditioned DLR specification. O1 refutes the automatic transfer of scalar convexity. Even a bound for these labeled finite-volume Fourier observables would still need a justified thermodynamic/DLR limit and an extremal periodic phase. Those are separate missing premises, not conclusions of B1.

Retrieval failure checkpoint
Command: python -X utf8 recall_probe.py. brain.py recall completed in 15.881437 seconds. Its first three hits are Bernoulli-convolution Riesz-product memories, not Riesz-gas theorems (0/3 directly relevant; see brain_recall_receipt.json). The response reports P0309 absent. Proposed bounded repair: recognize the query's explicit Riesz-gas/Gibbs scope, flag product-only matches as a homonym collision, and expose an unresolved target rather than supply these as proof support. Do not silently rerank all uses of the word Riesz. A local replay guard and controls will measure this proposal; no live recall change is authorized.

NEXT: Retrieve the complete Brascamp-Lieb card and compare its hypotheses to B1, then read w537's saved proof and audit its central bridge.


Additional independent counterexample O2: centering is essential (pending w539)
Let D consist of N nonadjacent sites of Z^3, N even, so L_D=6I. Fix G=2pi e_1. Take m_x=0 for half the sites and m_x=e_1/2 for the other half. Set H_D(u)=3 kappa sum_x |u_x-m_x|^2. Its Hessian is exactly kappa (L_D tensor I_3), uniformly in N. The density factorizes, hence the u_x are independent Gaussians with means m_x and covariance I_3/(6 beta kappa). Put a=exp(-|G|^2/(12 beta kappa)). The means of exp(iG dot u_x) are +a and -a, giving E B_{D,G}=0. Independence gives E|B_{D,G}|^2=(1-a^2)/N ->0. Thus a uniform covariance bound alone does not give the proposed positive lower bound for a specified reciprocal Fourier mode. A coherent mean phase is a separate premise; evenness in B1 is one sufficient way to ensure it. This example does not disprove any crystalline Gibbs phase or exclude every possible Bragg mode. It refutes only the centering-free transfer to this fixed G. The site set is explicitly nonadjacent; it is not being passed off as a connected-box Riesz system.

Source checkpoint update: Exact op-p0309 campaign entry was recovered from the cited bundle and is in p0309_exact_intake.json. Its phrase "in the regimes predicted in the review" leaves quantitative exponent and ensemble quantifiers unspecified; the source ambiguity belongs to the intake row, not to a proved theorem. Brascamp-Lieb card/source comparison is in HYPOTHESIS_AUDIT.md.


Independent strengthening O3: full finite-particle convexity fails near collision (pending w539)
For s>0, N>=2, consider E(x_1,...,x_N)=sum_{i<j}|x_i-x_j|^{-s}+sum_i U(x_i), with U C^2 near an interior point, and all other particles held at fixed positive distance from that point. Put x_1=0, x_2=(epsilon,0,0), and perturb only x_2(t)=(epsilon,t,0). The pair (1,2) contributes -s epsilon^{-s-2} to d^2E/dt^2 at zero. Every other interaction involving particle 2 and the smooth external/background term have a bounded second derivative as epsilon->0. Hence d^2E/dt^2=-s epsilon^{-s-2}+O(1)<0 for sufficiently small epsilon>0. The negative curvature holds on an open set of collision-free configurations. No positive-definite global lower bound for the full Hessian can hold on the whole finite-particle configuration space. Multiplying by beta>0 does not fix the sign. This applies to the direct short-range finite-volume energy and any smooth finite-volume background term; it does not analyze a renormalized infinite-volume Hessian or the Hessian restricted near a fixed crystal. A positive-temperature near-collision configuration is rare but has positive Gibbs density wherever the finite energy is defined. Thus a pointwise-global Brascamp-Lieb premise cannot be justified merely by low temperature. A repair must restrict/convexify a controlled region and separately control its complement, or use an inequality not requiring global convexity.


Paired-attempt audit and independent law-transfer obstruction O4 are in PAIRED_AUDIT.md. The most important C5 pressure implication checks under its stated full-law premise; B1 does not supply that premise. The global finite-volume convexity shortcut is refuted by O3.
