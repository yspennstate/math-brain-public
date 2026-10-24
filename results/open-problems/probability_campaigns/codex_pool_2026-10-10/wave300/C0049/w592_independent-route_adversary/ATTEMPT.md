# C0049: independent boundary-wiring route (saved before paired proof)

2026-10-10. Author w592. This derivation was written without reading w591's proposed proof or the core-proof lane. It is a finite-graph calculation and a candidate obstruction, not a proof of the scaling-limit conjecture.

Smirnov, ICM 2006, Conjecture 4 (printed p.1429, PDF p.9), concerns the square-lattice FK Dobrushin interface at the self-dual parameter. The proposed limit is chordal SLE with kappa(q)=4*pi/arccos(-sqrt(q)/2). For this task restrict to 0<q<=4, q!=2. Fix a simply connected Jordan domain with distinct boundary points a,b, lattice approximations retaining these boundary points, and wired/free complementary boundary arcs. The intended modern formulation asks convergence in law as unparametrized curves, with the topology and boundary-approximation convention explicitly supplied. The original conjecture alone does not specify all of that topology. For q<1, call p_sd=sqrt(q)/(1+sqrt(q)) self-dual; do not import a q>=1 critical-point theorem.

Primary source: https://www.unige.ch/~smirnov/papers/icm-publ.pdf . Current q=4 source lead: https://unige.ch/~duminil/publi/2026%20conformal%20invariance%20FK%20q=4.pdf . Its exact scope is still being checked.

Independent method: compare FK measures under merging two boundary classes. Use positive, bounded Radon-Nikodym martingales rather than assuming convergence of a parafermionic field. A nontrivial continuum limit would require proving conformal covariance of boundary connectivity probabilities, and stability in random slit domains. Those are the hard premises; the finite identity does not prove them.

Let G be a finite graph, 0<p_e<1 for all edges, q>0, and xi a boundary partition. Let mu=phi_G^xi, with weight product_e p_e^omega_e(1-p_e)^(1-omega_e) times q^k_xi(omega). Pick vertices u,v. Let eta merge their xi boundary classes and let A={u connected to v after the xi identifications}. Let Z_xi,Z_eta use the same edge factors and count all components, including wired components, consistently.

For every configuration, k_eta=k_xi-1+1_A. Therefore

R=Z_eta/Z_xi=q^(-1)+(1-q^(-1))*mu(A),

d phi_G^eta / d mu = [q^(-1)+(1-q^(-1))*1_A]/R.

If F_n reveals edges using the same predictable decision rule under both measures, the density on F_n is

D_n=[q^(-1)+(1-q^(-1))*M_n]/R,  M_n=mu(A|F_n).

Proof: the pointwise component-count identity gives the density. Conditional expectation gives its restriction to F_n; the tower property gives E[D_(n+1)|F_n]=D_n. No product of conditionally bounded events and no independence assumption is used. For q>=1, R lies in [1/q,1] and D_n in [1/(qR),1/R]; for 0<q<1 the two endpoints reverse. All are finite at each fixed q>0.

Concrete degeneracy: at q=1, R=1 and D_n=1 for every graph, boundary partition and exploration history. Thus martingales obtained solely by changing FK boundary wiring cannot distinguish any driving variance at q=1. A proposal using these martingales alone to identify SLE(6) lacks a nontrivial geometric observable. This is an obstruction to that method, not a counterexample to C0049.

A second exact diagnostic: for e=uv, H=G minus e, c=phi_H^xi(A),

phi_G^xi(e open)=p_e*R/((1-p_e)+p_e*R), R=c+(1-c)/q.

At p_e=p_sd this becomes (1+(q-1)c)/(sqrt(q)+1+(q-1)c). The endpoint values are 1/(1+sqrt(q)) and sqrt(q)/(1+sqrt(q)). At q=4 they are 1/3 and 2/3. Domain Markov gives the correct residual FK measure with induced wiring; it does not erase the domain-dependent c. A constant tip transition or q-only drift cannot be inferred from this identity. A continuum argument must derive, rather than assume, how c behaves in the explored conformal domain.

Exact target record recovered: intake problems.jsonl line 49 points to Duminil-Copin's 2017 lectures, Conjecture 3, printed p.93. https://www.ihes.fr/~/duminil/publi/2017PIMS.pdf gives the Dobrushin-domain statement at p=p_c and the same kappa formula. The prior C0049-A001 uses the parafermionic route. Its claim of an exact reduction to finding an additional discrete relation is stronger than the primary source's sufficient implication from observable convergence; no necessity has been proved.

Exact enumeration now completed: 1,792 finite graph/parameter/boundary cases, 20,412 pointwise checks, 39,032 adaptive histories, 18,620 tower identities, and 5,576 q=1 constant-density histories; zero failures. See MEASUREMENTS.json and check_fk_wiring.py. The q-only edge-predictor negative control has absolute error 1/3, corrected to zero by retaining wiring. These are finite diagnostics, not an FK scaling-limit proof.

After this independent file was saved, w591's statement was read. His chosen route also uses boundary profiles; I stopped further duplicate finite work and independently proved his precise localized two-observable driver lemma. The sharp one-observable counterexample and missing continuum premises are saved in ADVERSARIAL_AUDIT.md.

NEXT: Obtain w593's narrow mathematical review, and package the finite obstruction, driver proof and source-scope correction as concept/draft brain material.
