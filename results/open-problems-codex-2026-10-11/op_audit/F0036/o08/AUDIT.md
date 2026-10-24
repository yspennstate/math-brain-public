VERDICT: PASS (correct and complete)

# Independent audit of F0036

Audit date: 2026-10-12. Claimant directory was accessed read-only. All downloads, independent calculations, and this report were written in the assigned o08 directory. No claimant scripts were executed and no repository was changed.

## Exact claim and scope

The current claim, in ATTEMPT.md, Exact target (line 4) and Section 12 (line 137), and CLAIMS.jsonl, is the following almost-sure assertion for the standard Brownian net N:

Let N_0 consist of all net paths started at time exactly zero. Define

    M = {(x,t): t>0, there exist pi,pi' in N_0,
         pi(u)<pi'(u) for every 0<u<t, and pi(t)=pi'(t)=x}.

Then M intersects every compact subset of R x (0,infinity) in finitely many points, on a single probability-one event.

This is exactly the requested Conjecture 8.3. I independently downloaded https://arxiv.org/pdf/1506.00724 and read equation (8.3) and Conjecture 8.3 on PDF page 72. The quantifiers include every net continuation, rather than just marginal-web paths or finite-hop paths. Equality of the two starting positions at zero is permitted. Strict ordering at all positive times before the meeting is retained. No conclusion at the time-zero boundary is required or claimed.

The accepted argument is ATTEMPT.md Sections 9-12, expanded in PROOF.md, Lemmas 1-6 and Conclusion. Sections 1-8 explicitly preserve a superseded partial attempt. I read STATUS.md, ATTEMPT.md, CLAIMS.jsonl, LITERATURE.md and the referenced PROOF.md. The verdict is SOLVED by deduction, not SOLVED_IN_LITERATURE. I therefore checked the deduction rather than treating a citation as an existing solution.

## Issues found

No mathematical defect requiring a correction was found in the completed proof. In particular, none of the following tempting objections survives examination:

- ATTEMPT.md Section 8 (line 103) really does describe a gap in the historical finite-site approach, but Section 12 uses a different argument that controls the entire contact observable at once. The old gap is not silently assumed away.
- ATTEMPT.md Section 11 (line 128) uses a time-reversed occupied image, rather than the dual Brownian net. PROOF.md makes the required distinction and performs the rotation in distribution.
- ATTEMPT.md Section 12, item 2, needs actual incoming web representatives, not merely two paths newly started at the fork. The published special-point structure supplies exactly those representatives; the proof uses them correctly.
- ATTEMPT.md Section 12, items 3 and 6, transfers a completed null event, not a first moment or an unsupported closedness assertion for strict order. The analytic-event argument is adequate.
- ATTEMPT.md Section 12, item 5, needs one common spatial radius for every witness in a target box. Lemma 6 establishes that common radius; a countable union of separately localized finite sets is not being used as a finiteness argument.

There are evidentiary limitations, already acknowledged by the claimant: the stochastic proof is not Lean-certified; the finite computations do not certify a continuum limit; and novelty is unestablished. None is a missing mathematical hypothesis or proof step. No repair is needed for the asserted local-finiteness theorem.

## Primary sources independently checked

Fresh successful HTTP downloads, with text extracted locally:

1. Schertzer, Sun, Swart, *The Brownian web, the Brownian net, and their universality*, arXiv:1506.00724, 80 PDF pages: exact target on page 72; containment Proposition 3.14; deterministic-time hopping Proposition 3.15; density Proposition 3.18; web outgoing equivalence and classification.
2. Schertzer, Sun, Swart, *Special points of the Brownian net*, arXiv:0806.2326, 55 PDF pages: outgoing equivalence Definition 1.5 and equation (1.9), page 7; subscript-s type definition, page 8; Theorems 1.11 and 1.12, pages 12-13; image identity (1.16), page 14; Definition 2.3 and Proposition 2.6, pages 22-23; Lemma 2.8 and Proposition 2.9, pages 24-25; local equivalence (3.3) and its proof, pages 31-32; Lemma 3.12, page 36.
3. Sun, Swart, *The Brownian net*, arXiv:math/0610625, 58 PDF pages: containment Proposition 1.8, page 10; image-set Proposition 1.13, page 14; backbone rotation Proposition 1.15(ii), page 16. I also read the image-set property's proof, which uses the mesh characterization.

The downloads are source.pdf, special_points.pdf, and brownian_net.pdf, with corresponding .txt files. These are independent fetches, not the claimant's saved copies.

## Step-by-step verification of the completed deduction

### 1. Reconstruction of finite backbone segments

Location: ATTEMPT.md Section 10 (line 121); PROOF.md Lemma 1 (line 30).

Proposition 1.13 explicitly includes starting time minus infinity, and states its image characterization simultaneously for all such paths. For a continuous segment f in the backbone image B, its two endpoint memberships provide a backbone past through the first endpoint and a backbone future through the second. Grafting them to f produces a continuous path in the compactified path space: the joins agree, and the two infinite-time tails are unchanged. Its graph stays in B. The image-set identity therefore puts the grafted path in the net. Restriction to a finite starting time cannot enter a previously forbidden dual wedge from outside, so is again a net path. This is a simultaneous pathwise assertion, valid for witnesses selected from the observed image.

No unjustified assertion about the reversal of an individual original-net path is required here.

### 2. Arbitrary surviving branches imply canonical relevance

Location: ATTEMPT.md Section 12, item 2; PROOF.md Lemma 2 (line 36).

I checked the source definitions rather than interpreting the word 'separation' informally. Definition 2.3 requires both paths to start strictly before the intersection and to be unequal on an immediately following open interval. The hypothesized common incoming segment from S<t and strict outgoing gap satisfy this. Lemma 3.12 consequently identifies the point as type (p,pp)_s.

The two witnesses cannot be equivalent as outgoing paths: Definition 1.5 would require equality along a sequence of times decreasing to the fork. There are exactly two outgoing classes at this type. The left witness and right witness occupy the corresponding ordered classes. Proposition 2.6 and the subscript-s definition identify an incoming left-web path l continuing in the left class and an incoming right-web path r continuing in the right class.

Theorem 1.12(b) gives local class bounds with extended representatives. Theorem 1.11(b), followed by strong uniqueness in 1.11(a), permits the appropriate outer bounds to be taken as these same incoming true web paths. Thus, on a sufficiently short interval after the fork,

    l <= eta_1 < eta_2 <= r.

For any later w before H, choose a comparison time v strictly between the fork and w in this short interval. Proposition 1.8 applies because v is strictly later than both relevant starting times. It propagates l(w)<=eta_1(w) and eta_2(w)<=r(w), giving l(w)<r(w). The incoming witness reaches the fork from S, so all clauses of Lemma 2.8(i) hold. This proves membership in R_{S,H}, not merely membership in the unrestricted countable set of separation points.

The containment directions are correct. This argument does not use the failed identification with earliest inward-extremal contacts.

### 3. Measurability of the compact-image observable

Location: ATTEMPT.md Section 12, item 3; PROOF.md Lemma 3 (line 50).

The hyperspace of compact subsets of D_m, with an isolated empty set adjoined, is Polish. The bounded continuous-function space is a closed subspace of a Polish function space. Graph containment is closed under simultaneous Hausdorff and uniform convergence. Equality on the moving compact interval [t,U] is closed, since the maximum discrepancy on that interval is continuous in the functions and t.

For t>s, the intervals

    [s, s+(1-1/k)(t-s)], k>=2,

exhaust [s,t). Positivity of the continuous gap on each such compact interval is equivalent to strict order at every point of [s,t). Their minimum-gap functions depend continuously on the functions and endpoint. Hence this requirement is Borel, despite strict order not being closed.

A sequence of witnessed contacts, with pairwise distinct contact points, is a Borel relation in a countable product of these Polish spaces. Its projection is exactly the infinite-count event. This makes that event analytic and universally measurable. If it is null under the backbone law, it has a Borel null envelope under that law; absolute continuity transfers the envelope and thus the analytic event. This is sufficient for completed probability laws. The argument never needs strict order to persist under a scaling limit.

### 4. Stationary finiteness by rotation

Location: ATTEMPT.md Section 11 and Section 12, item 4; PROOF.md Lemma 4 (line 77).

I re-derived the coordinate change. Under J(x,t)=(-x,-t), meeting time t becomes fork time -t, [s,U] becomes [-U,-s], and the common suffix becomes a common incoming segment of duration U-t>0. Swapping the two reflected curve labels preserves their left-right ordering. The strict gap lasts until -s. The target times [-b,-a] lie strictly inside (-U,-s).

In an ordinary backbone realization, Lemma 1 reconstructs the reflected continuous segments as actual net segments, and Lemma 2 injects their distinct fork locations into R_{-U,-s}. Proposition 2.9 gives a finite expected count in the reflected target box. Backbone rotation invariance then gives finiteness of the original observable. These are statements in distribution about images, not a purported pathwise reversal symmetry of the original forward net.

### 5. Local absolute-continuity transfer

Location: ATTEMPT.md Section 9, Approach A (line 111), and Section 12, item 6; PROOF.md Lemma 5 (line 89).

Equation (3.3) is actually proved in the proof of Proposition 3.6: it asserts equivalence of the laws of A_T intersected with K and B intersected with K for a deterministic compact K strictly above T. It is not just a heuristic consequence of the proposition's time-reversal formulation. The source reduces both laws to the same finite mixture of local image pieces, with positive weights for every occupancy subset.

Here T=0 and K=D_m has earliest time s>0, satisfying the restriction. The event from Step 3 depends solely on this compact image. Absolute continuity therefore transfers its null probability. Intersecting over integer m is legitimate and makes finiteness simultaneous for those windows. Nothing in this step transfers a density or an expectation bound to the time-zero image.

### 6. A common bound for every visiting witness

Location: ATTEMPT.md Section 12, item 5; PROOF.md Lemma 6 (line 97).

For h=b-s and d=n-R-h>0, a drift-minus-one left barrier reaching R from n requires a Brownian fluctuation of size at least d. The reflection principle and union bound give

    P(sup_{[0,h]} |B| >= d) <= 4(1-Phi(d/sqrt(h)))
                               <= 4 exp(-d^2/(2h)).

The displayed barrier estimates follow, and are summable over integer n. Borel-Cantelli needs no independence. A path above the successful high left barrier at time s cannot subsequently cross below it, so cannot visit the target box. The low right barrier gives the corresponding lower exclusion. Strict comparisons just after s justify containment despite the barrier's starting time being s.

Once all visiting paths have time-s positions in [-n,n], the left barrier from -(n+1) and right barrier from n+1 bound every one of them on the entire [s,U]. Their finite continuous ranges give a single random finite integer m. All integer-start barriers are available on a countable probability-one event. No exceptional random-time density assertion or independence at a random cut is used.

### 7. Inclusion and the final quantifiers

Location: ATTEMPT.md Section 12; PROOF.md Conclusion (line 116).

For each PMRCA in C, restrict its two witnesses to [s,t] and use one witness as their common suffix after t. The resulting continuous graphs remain in A_0, irrespective of whether a separate hopping theorem is invoked. They lie in the common D_m from Step 6 and satisfy the observable's strict-order and equality requirements. Thus all PMRCAs in C are contained in one finite observable, rather than a potentially infinite union of finite sets.

The countable boxes [-k,k] x [1/k,k] exhaust all compact subsets of R x (0,infinity). Intersecting their probability-one events proves the required simultaneous almost-sure local finiteness. This includes same-position starts at time zero, since the positive cut forces distinct witness positions at s.

## Additional claims and independent computations

The appended deterministic-cut corollary in PROOF.md (line 138), referred to in ATTEMPT.md Section 12, is also justified. Survey Proposition 3.15(ii) permits the required simultaneous concatenations at each fixed deterministic s, including a new tail whose starting time equals s. The resulting image observable ignores earlier ordering and controls all these contacts together. This establishes the stated corollary for each deterministic s; it makes no assertion at a net-dependent random cut.

For the stationary expectation claim, Proposition 2.9 yields exactly

    E|P(B intersect D_m)| <= 2 integral_C Psi(U-t)Psi(t-s) dx dt,
    Psi(v)=exp(-v)/sqrt(pi*v)+2 Phi(sqrt(2v)).

The rotation swaps the two time distances as stated. The inequality Psi(v)<=1/sqrt(pi*v)+2 gives the claimant's bound with coefficient 4R(b-a), since the spatial width of C is 2R. The positivity of a-s and U-b prevents endpoint singularities. Absolute continuity alone does not give this first moment for A_0; the claimant correctly refrains from asserting it.

Independent audit_checks.py, written and run in this directory, recorded:

- 330 exact integer instances of l<=f<g<=r imply l<r;
- exhaustive enumeration of all paths in each of 200 independently generated finite planar arrow systems, compared against greedy outward paths in the reversed occupied graph: 315 distinct contacts overall, zero mismatches;
- 35 numerical checks of the Gaussian reflection/union estimate and seven checks of the Psi bound;
- a 10,000-subinterval midpoint calculation with R=2, s=0.5, a=1, b=2, U=3: stationary integral approximately 33.3782559804, below the analytic upper bound 57.3944515742.

Results are in audit_checks.json. These computations test algebra and finite geometry only. They are not a proof of a stochastic scaling limit, a check of all continuum configurations, or independent verification of the claimant's reported 500-case run.

The historical fixed-pair uniqueness lemma follows immediately because an earlier equality contradicts the strict-order requirement for a later contact. The historical finite inward/outward counterexample's listed sequences have first contacts at times 2 and 4 respectively. Neither historical finite-site localization nor the nine small scaling samples is used as a proof of the full conjecture. The conditional three-connected-point reduction remains explicitly conditional on that other conjecture and is not an input to the accepted deduction.

No Lean job was run for this audit. The claimant explicitly records that the new SurvivingExtrema artifact was not successfully compiled. That artifact is unnecessary for the scalar implication above and does not certify the Brownian-net proof.

## Fresh bounded literature search and limits

The arXiv API query all:"Brownian net", requesting up to 40 records sorted by submission date, succeeded and returned 14 records. I screened all returned titles and abstracts. The source, original net paper, special-point paper, stochastic-flow paper, marking construction, net-with-killing papers, convergence/universality papers, and related particle-system work did not identify an abstract-level theorem settling this exact PMRCA question. Some records concern a different 'Brownian net' in random geometry and are irrelevant.

I also freshly fetched the abstracts of arXiv:2512.10761 and arXiv:2401.09370. Kou's paper studies exceptional time slices with cluster points and their Hausdorff dimension 1/2. The universality paper proves a scaling-limit result for branching-coalescing walks with crossing paths. Neither abstract settles the PMRCA set's local finiteness, and exceptional time-slice nonfiniteness is not a counterexample to that claim.

A Crossref title query returned the foundational papers and related work; no exact solving result was identified. Three fresh OpenAlex searches, including the exact ancestor phrase, all returned HTTP 429. Those failures are not negative search results. An additional broad arXiv HTML search was noisy and provides no useful exhaustive-search assurance. Raw responses and summaries are saved here by check_sources.py and search_more.py.

This bounded search does not certify novelty or the absence of an earlier solution. The mathematical PASS is based on the complete written deduction from the independently checked published results. What is proved is almost-sure local finiteness for the exact set M in the question, plus the stated fixed-deterministic-cut corollary and stationary-observable bound. Novelty, a time-zero PMRCA intensity bound, statements at arbitrary random cuts, and the separate bubble-complexity and three-connected-point conjectures are not proved by this audit.
