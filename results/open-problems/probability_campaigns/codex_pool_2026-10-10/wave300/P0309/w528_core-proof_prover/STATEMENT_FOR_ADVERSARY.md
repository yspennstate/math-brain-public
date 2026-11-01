# P0309 statement packet, w528, 2026-10-10

No proof is included in this packet so w529 can work independently.

The dated intake title is “Positive-temperature crystalline Gibbs phases for three-dimensional Riesz gases” (tier 5, unsolved on 2026-09-07). The full local record has now been recovered from brain_bundle_C006p02.json, key op-p0309, and saved in P0309_EXTRACT.json. Its exact requested conclusion is: “Prove existence of a crystalline Gibbs phase at sufficiently low positive temperature for the three-dimensional Coulomb or Riesz gas in the regimes predicted in the review.” It cites Lewin, https://arxiv.org/html/2202.09240v2, Section VI, PDF pages 59–61 and 66–67. The primary source describes a conjectural low-temperature crystalline phase; the intake does not fix an exponent interval, ensemble, or definition of order. Current openness is UNKNOWN; no novelty claim is made.

Precise model for this lane: dimension 3, fixed exponent 0<s<3 and background density rho>0. In a bounded container Omega with N=rho|Omega| an integer, let

H(X)=sum_{i<j}|x_i-x_j|^{-s} - rho sum_i integral_Omega |x_i-y|^{-s}dy + (rho^2/2) integral_{Omega x Omega}|x-y|^{-s}dxdy.

The canonical finite-volume law has density Z^{-1}exp(-beta H(X)) relative to dx_1...dx_N/N!. Crystalline boundary selection, if used, must be specified with a renormalized exterior potential. The desired positive-temperature conclusion is an unperturbed infinite-volume Gibbs state at some finite beta, invariant under a full-rank lattice but not under all translations, with a nonconstant periodic first intensity. A stationary average can instead reveal order in a nonzero reciprocal-lattice Bragg component. Proving existence, the Gibbs limit property, and order all require evidence. This is an explicit long-range subtarget of the intake title, not a claim that the original title excludes s>3.

w528 claims the following disjoint lemma boundary: absolute interaction estimates for compact signed defect charges, the exact needed moment cancellations, and the failure of mass neutrality alone at the Coulomb threshold. No lattice Hessian, phonon integral, or full-lattice minimizer computation is claimed.

Statement A. Let s>0 and let nu,mu be finite signed Borel measures supported respectively in B(0,a), B(0,b). Assume integral dnu=integral dmu=0 and integral x dnu(x)=integral y dmu(y)=0. For |z|>a+b put M2(nu)=integral |x|^2 d|nu|(x) and C4(s)=s(s+2)(s^2+16s+51). Then

|integral integral |z+x-y|^{-s} dnu(x)dmu(y)| <= (C4(s)/4) M2(nu)M2(mu)(|z|-a-b)^{-s-4}.

Statement B. For 0<s<=1, let e=(1,0,0), nu=delta_e-delta_0 and

I_s(z)=2|z|^{-s}-|z+e|^{-s}-|z-e|^{-s}.

Then sum_{z in 4 Z^3, |z|>=16}|I_s(z)| diverges. In particular compact defect neutrality alone does not justify a volume-uniform absolute sum of pairwise interactions in this exponent range. This does not disprove a conditionally renormalized Gibbs phase or collective screening.

Statement C. A finite signed measure with zero total mass and nonzero first moment cannot be exactly represented as a finite sum of compact signed measures each with zero mass and zero first moment. Changing the center of a neutral measure does not change its first moment.

Main gap to attempt after these estimates: a Gibbs-measure comparison that repairs actual continuum crystal defects while controlling the dipole sector, energy, and the repair-map entropy uniformly in the volume. Statements A–C do not supply such a comparison, a crystalline ground-state gap, or Bragg order.
