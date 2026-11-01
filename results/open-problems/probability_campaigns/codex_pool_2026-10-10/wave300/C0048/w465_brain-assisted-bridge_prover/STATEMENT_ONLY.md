# C0048: statement for an independent adversarial attempt

Primary source: Hugo Duminil-Copin, Lectures on the Ising and Potts models on the hypercubic lattice, Conjecture 2, printed p.93 (zero-based PDF page 92): https://www.ihes.fr/~duminil/publi/2017PIMS.pdf . Intake record: probability_1000_intake_claude_20260907/problems.jsonl, C0048, line 48.

Exact target in explicit conventions: for every integer q>=3 and integer d>=3, consider the zero-field ferromagnetic nearest-neighbor q-state Potts model on Z^d with Gibbs weights exp(beta sum_{<x,y>} 1{sigma_x=sigma_y}), beta>0. Put p=1-exp(-beta). Let phi^w_{p,q} be the infinite-volume wired random-cluster measure and p_c=inf{p: phi^w_{p,q}(0 connected to infinity)>0}. Prove phi^w_{p_c,q}(0 connected to infinity)>0. Equivalently, the monochromatic-boundary spontaneous magnetization mu^1_beta(sigma_0=1)-1/q has a positive value at beta_c=-log(1-p_c), since it equals (q-1)/q times wired infinite-cluster probability.

Scope: all fixed q,d above, including q=d=3; no spread-out interactions, external field, large-q assumption or unspecified large-d cutoff. The unverified intake's q_c(d)=2 shorthand is historical context, not an extra proof obligation for noninteger q in this Potts formulation. The 2017 source lists large-q, large-d and spread-out special cases.

Current openness as of this session: UNKNOWN. Primary historical conjecture verified; bounded recent-source and owner's prior-work checks do not certify the absence of a later solution. No novelty or solved claim is made.

This file contains no new proof or proposed bridge. The adversary's first attempt should be independent.
