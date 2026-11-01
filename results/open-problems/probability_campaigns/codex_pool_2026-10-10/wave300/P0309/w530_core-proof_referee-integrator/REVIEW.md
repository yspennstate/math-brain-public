# P0309 referee packet (working)

## w529 C1 — KEEP as a counterexample to fixed-reference coercivity

Reproduction: for integer L>=2 on T_L=(R/LZ)^3, let X={0,...,L-1}^3 and t=(1/2,0,0). The translated configuration Y=X+t has E(Y)=E(X) for every jointly translation-invariant energy E. Each y has torus distance exactly 1/2 from the nearest point of X. For any 0<delta<1/2, all L^3 points are counted as defects against the *fixed* X, while the energy excess is zero. Thus E(Y)-E(X)>=c N_bad fails for every c>0. This is an algebraic symmetry argument, independent of numerical evidence or Riesz exponent.

Scope: it does not refute an estimate minimized over common translations/rotations, or an estimate with phase-pinning boundary conditions. It does not solve P0309. Status: independently checked proof of this counterexample only. Source: w529/CLAIMS.jsonl C1 and independent rederivation here.

NEXT: recover the exact P0309 source and check whether w528 or w529 has any phase-fitted argument to audit.

## Source correction and w528 source row — KEEP, with file correction

I independently located the campaign key `op-p0309` in the named intake's `brain_bundle_C006p02.json` (w528's P0309_EXTRACT.json gives its fields). The campaign wording is: "Prove existence of a crystalline Gibbs phase at sufficiently low positive temperature for the three-dimensional Coulomb or Riesz gas in the regimes predicted in the review." This is the exact recovered *campaign wording*, not a fully quantified theorem: the exponent, ensemble, long-range neutralization and observable remain open to specification. The cited primary survey is Lewin, arXiv:2202.09240, Section VI; that survey's Conjectures 35 and 38 concern zero temperature. Thus w528-S1.0 is correct as a warning about the *ranking and title*. w528's SOURCE_STATUS.json was later updated with the recovered row. Current 2026 openness remains UNKNOWN.

## w528 L1–L6 — referee verdicts

| Claim | Verdict | Independent check and scope |
|---|---|---|
| L1 neutral-pair decay | KEEP | Subtract constants in both integration variables. The mixed finite difference is a double integral of the Hessian; radial eigenvalue is s(s+1)r^(-s-2), tangential eigenvalues -s r^(-s-2). The displayed M1 bound follows. |
| L2 dipole-free pair decay | KEEP | I independently differentiated r^(-s) four times. The three absolute tensor contributions are s(s+2)(s+4)(s+6), 6s(s+2)(s+4), and 3s(s+2), totaling s(s+2)(s^2+16s+51). Two second-order Taylor remainders each integrate to 1/2, giving the claimed factor 1/4. Both mass and first moment must vanish for *each* signed measure. |
| L3 lattice cross sum | KEEP bundle; FIX ATTEMPT notation | The shell count is exactly 24n^2+2, so the zeta bound converges for s>0. The useful hypothesis is a uniform *centered* moment integral |x-c_i|^2 d|nu_i|(x)<=M. ATTEMPT.md writes `M2(nu_i)` after L2 defined M2 about the global origin; the literal stronger global bound still implies the centered bound here. The brain bundle's L3 statement explicitly says the moment is measured about each block's center, so its mathematical statement is correctly scoped. Neither version supplies a bound on crystal-reference interactions. |
| L4 neutrality-only absolute divergence | KEEP | On z=4(n,j,k), n>=4, |j|,|k|<=floor(n/4), the axial squared cosine is at least 9/11: (4n-1)^2>=9n^2 while the transverse squared radius is <=2n^2. The second directional derivative is therefore at least (7s/11)(6n)^(-s-2). There are at least n^2/16 such sites per n, so the lower series is a positive constant times sum n^(-s), divergent for 0<s<=1. This is *absolute* divergence, not failure of a renormalized or angularly canceled interaction. |
| L5 dipole conservation | KEEP | For neutral nu, integral (x-c)dnu = integral x dnu. Finite additivity makes a nonzero total dipole incompatible with every summand having zero dipole. This directly blocks applying L2 to ordinary single-particle displacements. |
| L6 pushforward repair implication | KEEP as conditional lemma | The energy gain contributes exp(-beta tau m), and the pushforward domination contributes exp(kappa m) after integrating exp(-beta H) against its image. No independence is used. The physical repair map and positive tau are absent; the lemma does not prove crystallization. |
| L7 null-image repair obstruction | KEEP | If lambda(E)>0 and T(E) lies in a measurable lambda-null B, the pushforward mass of B is at least lambda(E)>0 but C lambda(B)=0 for every finite C. This rules out exact site-collapse as a repair satisfying L6(ii); it does not rule out full-dimensional repairs. |

The hardest unchecked claim is w528's proposed lemma G: a full Gibbs-law contour repair with phase fitting, dipole/exterior-energy control, positive energy gain and finite entropy cost. L1-L6 do not establish any of these physical premises. An exact rigid-site map collapses positive configuration volume and cannot meet L6's pushforward domination.

## w529 C2–C8 — referee verdicts

| Claim | Verdict | Independent check and scope |
|---|---|---|
| C2 acoustic mode | KEEP | The first Fourier cosine has eigenvalue 4 sin^2(pi/L); H/||u||_2^2=(kappa/2) times that eigenvalue. It tends to zero as L grows, so no uniform coercivity against absolute displacement in this model. |
| C3 matching-to-Fourier lower bound | KEEP | Each matched site contributes cos(G.u_j)>=1-(G.u_j)^2/2 after removing the common phase; an unmatched particle contributes at least -1. Hence Re(e^(-iG.a)A)>=1-2m/N-(2N)^(-1)sum_matched(G.u_j)^2. If the expectation lower bound b is nonnegative, Jensen gives E|A|^2>=b^2. It supplies no Gibbs-law mismatch estimate. |
| C4 DLR vacancy | KEEP in its s>3 grand-canonical scope | The empty interior term equals 1 and every other Boltzmann weight is at most 1, so 1<=Z_C(eta)<=exp(z|C|) and conditional vacancy probability is at least exp(-z|C|). It does not apply unchanged to neutralized long-range canonical jellium. |
| C5 harmonic inverse trace | KEEP | Representative Fourier modes with max-coordinate m have at most 26m^2 members; sin(pi m/L)>=2m/L makes each inverse eigenvalue at most L^2/(16m^2). Dividing by L^3 and summing at most floor(L/2) shells gives T_L<=13/16. The Gaussian characteristic function then gives the stated positive bound. This is an exactly quadratic toy model only. |
| C6 entropy counterexample | KEEP | The good sector has length exp(-n^2); multiplying its weight by exp(beta tau n) still tends to zero compared with the bad sector's length. Thus P_bad tends to 1 despite an energy gap tau n. It is not a Riesz example. |
| C7 area-formula repair implication | KEEP as conditional lemma | Energy gain, lower Jacobian and multiplicity bound give P(B)<=M exp(-beta Delta)/J by the area formula. The actual full-dimensional Riesz repair map is unconstructed. |
| C8 rigid-repair obstruction | KEEP | Outputs of a translated fixed k-point template lie in a 3-dimensional affine subspace of R^(3k), so for k>=2 the derivative rank is at most 3 and the image is Lebesgue null. This refutes only exact rigid-template repairs. |

The apparent tension between C2 and C5 is resolved: the smallest nonzero elastic eigenvalue vanishes like L^-2 while the *normalized sum* of inverse eigenvalues stays bounded in dimension three. C3 needs a bound under the unrestricted Riesz Gibbs measure before it can imply order. KEEP on these auxiliary claims is not a KEEP on P0309.

NEXT: construct a two-cell dipole-carrier repair and bound its actual energy change and pushforward density uniformly in carrier distance.

Final packet check: w528's updated SOURCE_STATUS.json has the recovered source row, and its bundle_001.json L3 statement already makes the centered-moment convention explicit. G stays a conjectural input. The peer review status does not certify account-distinctness or the served model of this referee thread; those gates remain for the coordinator.

## Final target verdict

**NOT PROVED:** P0309 positive-temperature crystalline Gibbs phases. The KEEP verdicts cover only w528 L1-L7 and w529 C1-C8 under their exact assumptions. No full-dimensional repair satisfying both an actual Riesz energy gain and a uniform entropy/pushforward bound was supplied. Neither a harmonic calculation nor a neutral-block far-field bound closes this gap. The subsequent phase-coherence, genuine DLR/Gibbs-limit, and nontrivial order-observable steps remain open as well. Current 2026 openness is UNKNOWN rather than certified.

The final w528 REVIEW_PACKET.md adds no new mathematical claim beyond L7; it requests these per-claim verdicts and the full-target NOT PROVED verdict. w528's submitted nine-entry draft and this review are separate artifacts. Its bundle relations and coordinator integration status are not certified by this referee's mathematical verdict.
