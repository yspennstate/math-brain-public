# C0049: exact working target and scope

Author: w588. Date: 2026-10-10. Independent adversary: w589. Referee: w590.

Fix q in (0,4] excluding 2. Let D be a bounded simply connected Jordan domain with distinct boundary prime ends a,b. Take admissible simply connected square-lattice Dobrushin domains (D_delta,a_delta,b_delta) converging to (D,a,b), with boundary arcs also converging (for the working target, use Jordan boundary approximations converging uniformly). Sample the FK random-cluster measure with weight proportional to p^o(1-p)^(|E|-o) q^k, with the boundary vertices on arc ab identified and the complementary arc free. Let gamma_delta be the medial exploration separating the wired primal cluster and the free-side dual cluster, from a_delta to b_delta. The target is convergence in distribution of gamma_delta, in the uniform curve metric modulo increasing reparametrization, to chordal SLE_kappa in (D,a,b), where

    kappa(q) = 4*pi/arccos(-sqrt(q)/2).

This is the square-lattice bond model. Triangular site percolation does not prove its q=1 instance.

For q >= 1, set p=p_c(q)=sqrt(q)/(1+sqrt(q)). For 0<q<1, the finite measure still exists; equating p_c with that self-dual value requires a separate verified theorem. In the q<1 subproblem, p=self-dual is an explicitly conjectural critical tuning, rather than an imported theorem.

Primary statement: Hugo Duminil-Copin, *Lectures on the random-cluster model*, section 5.3.2, Conjecture 1; https://www.unige.ch/~duminil/publi/lectures%20on%20random%20cluster%20model.pdf . The lecture statement is less explicit about domain approximation topology; the Jordan specialization above fixes a reviewable instance, not a claim that all approximation variants are equivalent.

Endpoint update: Averous--Duminil-Copin--He--Lammers--Manolescu, arXiv:2610.08507v1 (6 October 2026), Theorem 1.2, claims convergence of q=4, p=2/3 **free-boundary loop ensembles** to nested CLE(4) under Caratheodory domain convergence. That statement does not directly assert Dobrushin chordal-interface convergence. It is a fresh primary-source claim, not an independently audited proof here. Source: https://arxiv.org/html/2610.08507v1#S1.SS3 . Do not keep the old blanket open-status statement unchanged; do not infer Dobrushin SLE(4) without the missing boundary-change argument.

Current openness: UNKNOWN for the exact full target as of 2026-10-10; literature checked only as documented in SOURCE_STATUS.json. No owner-solved/retired conclusion has yet been certified.

Proposed disjoint lemma boundary: identify a continuous Loewner driver from the first two Laurent coefficients of localized parafermionic-limit martingales, without assuming in advance that the driver is a semimartingale. Work with sigma=(2/pi)arcsin(sqrt(q)/2), so kappa=8/(1+sigma). This does **not** prove convergence of the discrete observable in random slit domains. That convergence, with martingale transfer and curve compactness, remains input.

Adversary request: independently test the target assumptions and the proposed coefficient-identification lemma. In particular test stopping/localization, complex branches, filtration, the 4*sigma*t coefficient, and whether any semimartingale assumption is smuggled in.
