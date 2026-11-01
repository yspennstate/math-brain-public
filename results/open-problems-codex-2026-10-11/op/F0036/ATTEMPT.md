# F0036 research attempt — 2026-10-12

Latest assessment: SOLVED after the reopened attempt in Sections 9-12; full proof in PROOF.md. Sections 1-8 preserve the historical PARTIAL stopping point, now superseded.
## Exact target
For the standard Brownian net N, let N_0 be all paths with starting time exactly zero. Define M as the points (x,t), t>0, for which there are pi,pi' in N_0 with pi(u)<pi'(u) for every 0<u<t and pi(t)=pi'(t)=x. Prove that almost surely M intersects every compact subset of R x (0,infinity) in a finite set. The source uses W({0} x R) and N({0} x R) for paths started at time zero (despite coordinate-order inconsistencies elsewhere).

Verified source: Schertzer, Sun, Swart, arXiv:1506.00724, downloaded current version dated January 9, 2017; equation (8.3), Conjecture 8.3, printed page 72 / PDF page 72.

## Audit of earlier attempt
Read the F0036-A001 record in probability_1000_intake_F_20260908/attempts.jsonl. Its proposed extremal identification is not established. For starting sites y<y', containment gives pi <= r_y and l_y' <= pi'. If pi and pi' meet at t, then r_y(t)>=l_y'(t), so the first contact of the inward extremals is no later than t. This implication does not say t is that first contact. The later first contacts of alternative path pairs remain uncontrolled. No conclusion of the earlier sketch is accepted as a proof.

## Leads under investigation
1. Prove local finiteness when both witnesses are canonical paths in W^l union W^r, without hopping.
2. Localize all full-net witnesses using outward extremal barriers and take a deterministic positive-time slice. Finitely many positions at that slice do not imply finitely many path continuations.
3. Refute the unjustified extremal identification by an exact finite branching/coalescing directed graph.

The full conjecture is unproved at this stage.

## 1. Proved deterministic lemma: finite tails give finite contacts
Let s<a<=T. Suppose the restrictions to [s,T] of all admissible witness paths that can meet a box K=[-R,R] x [a,T] belong to a finite set F of functions. Suppose a meeting is witnessed by pi<pi' throughout (s,t), with equality at t. Then K contains at most |F|(|F|-1) such meeting points.

Proof. For each ordered pair (f,g) of distinct elements of F there is at most one t in [a,T] with f(t)=g(t) and f(u)<g(u) for all s<u<t. If there were t1<t2, the equality at t1 would contradict the strict inequality required by the event at t2. Equality of times forces equality of positions as well. Each meeting has one such ordered pair of tails. A finite union of sets of size at most one has size at most |F|(|F|-1). This argument needs neither continuity nor any probabilistic independence. QED.

The uniqueness step is formalized in OrderedContact.lean; compilation outcome will be recorded separately. This formalization does not certify the stochastic inputs below.

## 2. Proved localization for the full net
Fix deterministic 0<s<a<=T and R>0. Almost surely there is a finite integer n such that every N_0 path visiting K=[-R,R] x [a,T] has pi(s) in [-n,n].

Proof. Let l_n be the unique left-web path from (n,s), and r_-n the unique right-web path from (-n,s), for each positive integer n. Each has the marginal law of Brownian motion with drift -1 and +1 respectively (survey Theorem 3.2). Put H=T-s>0. For n>R+H,

 P(inf_[s,T] l_n <= R) <= P(sup_[0,H] |B| >= n-R-H)
                            <= 4 exp(-(n-R-H)^2/(2H)),

and the same bound applies to P(sup_[s,T] r_-n >= -R). The reflection principle and the Gaussian tail bound give the last inequality. These probabilities are summable in n. Borel-Cantelli (no independence needed) implies that for all sufficiently large n both barriers stay strictly outside [-R,R] on [s,T].

If pi(s)>n, continuity gives pi(u)>l_n(u) for some u>s arbitrarily close to s. Proposition 3.14 forbids crossing l_n from right to left after u, so pi(t)>=l_n(t)>R for every s<t<=T. For any fixed t>s choose u<t; hence pi cannot visit K. If pi(s)<-n, the analogous right barrier forbids crossing from left to right, yielding pi(t)<=r_-n(t)<-R. Endpoints pi(s)=+-n are included in [-n,n]. Thus every witness visiting K has its time-s location in that interval. QED.

By Proposition 3.18, Xi_s={pi(s): pi in N_0} is almost surely locally finite for each deterministic s>0. Indeed the displayed finite expectation for each deterministic bounded interval implies a finite count a.s.; intersecting the events for integer intervals permits use of the random n above. Consequently all meetings in K are witnessed from one of finitely many distinct ordered site pairs p<q in Xi_s cap [-n,n]. Strictness on (0,t) implies p<q because s is inside (0,t). The number of positions is finite; the number of continuations from each position is not known to be finite.

## 3. Proved special case: canonical continuations after a deterministic cut
Fix deterministic s>0. Define M_can(s) to consist of those points of M with t>s for which both witnessing paths, after time s, have a tail equal to a single path of W^l or W^r whose starting time is at most s, with no switch between the two webs. Then almost surely M_can(s) is locally finite in R x (s,infinity). In particular M restricted to witnesses entirely in W^l union W^r started at zero is locally finite in R x (0,infinity).

Proof. Fix K=[-R,R] x [a,T], s<a<=T. Apply Section 2 to localize both witnesses to the finite set A=Xi_s cap [-n,n]. For each p in A, survey Theorem 2.11 bounds the number of outgoing paths of an individual Brownian web at (p,s) by three. In the web definition, outgoing equivalence means equality on the entire future interval, not only equality arbitrarily close to s. The bound therefore counts distinct full tails. It applies simultaneously to every point, including random p, and also to drifted webs after shearing. Combining W^l and W^r gives a set F of at most 6|A| distinct tails on [s,T]. Every canonical-tail witness in K has its tail in F. Section 1 proves the finite bound |F|(|F|-1). Taking countably many boxes with rational parameters proves local finiteness throughout R x (s,infinity) on one probability-one event for fixed s. For entirely canonical time-zero witnesses, take s=1/j over positive integers; these events cover every compact box bounded away from zero. QED.

This is a special case, not the conjecture: full-net witnesses can switch infinitely many times, and the finite-tail argument no longer applies.

## 4. Exact finite counterexample to the earlier combinatorial identification
In the planar nearest-neighbour arrow system in finite_counterexample.json, start at -2 and 2 at time zero. The inward extremal paths have positions

 r_-2 = (-2,-1,0,1,0),   l_2 = (2,1,0,-1,0),

and first meet at (0,2). The outward extremal paths have positions

 l_-2 = (-2,-3,-2,-1,0), r_2 = (2,3,2,1,0),

and first meet at (0,4). Connect successive vertices by straight lines. Both witness pairs are strictly ordered on the whole open interval before their respective first contacts. All listed paths follow the same arrow configuration; choosing the minimum/maximum outgoing arrow verifies the extremal labels. The script checks the first contacts exactly. Thus containment and planarity alone cannot identify every pair's first meeting with the inward extremals' earliest meeting. This is not a counterexample to Brownian-net local finiteness, and no claim is made that a lattice diagram alone proves a positive-probability Brownian-net event.

## 5. Proved reduction to the older three-connected-point conjecture
The local-finiteness part of Conjecture 1.13 of Schertzer–Sun–Swart, Special points of the Brownian net (2009), implies Conjecture 8.3. This is a conditional reduction to another conjecture, not a theorem settling F0036.

Proof. Fix deterministic 0<s<a<=T<U. Consider z=(x,t) in M with a<=t<=T, witnessed by pi<pi' on (0,t). Restrict both paths at time s; such restrictions are net paths, since a restriction cannot enter any dual wedge from outside (survey Theorem 3.9). Their graphs from s to t lie in the image set N_s of paths started at s. The two graphs meet only at z, because their positions are strictly ordered throughout [s,t). Their boundary endpoints at time s are distinct. Continue pi from t to U. This third graph is in N_s, intersects each of the two earlier graphs only at z, and ends on the time-U boundary.

There are therefore three arcs from z to the boundary times s or U, pairwise disjoint apart from z. Removing at most two points other than z cannot hit all three arcs: each removed point lies on at most one arc. At least one intact arc still connects z to a boundary. Thus z is at least 3-connected in the graph-theoretic, time-unoriented sense used in the 2009 paper. As usual in this definition, removing z itself is excluded; otherwise every point would have connectivity one and the source's assertion that all image points are 2-connected would be impossible. The source additionally states that meeting/separation points are not 4-connected, but this upper bound is not needed: any claimed local finiteness of all points with this three-arm property would suffice.

Consequently M cap (R x [a,T]) is contained in the set of three-connected points to s,U. The local-finiteness clause of Conjecture 1.13 would make its intersection with every compact spatial interval finite. Use s=a/2 and U=T+1 for countably many boxes to obtain the desired almost-sure assertion. QED.

The reverse implication is not proved. Three-connected points need not have two forward histories separated since zero; they may have their three arms distributed differently between the past and future.

## 6. Finite computation and scaling diagnostic
pair_experiment.py implements the exact ordered-pair reachability recursion in a finite planar nearest-neighbour arrow graph. An entry A_t(i,j), i<j, means there exist two paths from time zero strictly ordered at every integer time 1,...,t and located at i,j at t. Initially use all source pairs i<=j; diagonal pairs at time zero permit distinct children immediately after zero, which the continuum definition allows. Propagate each pair through all four allowed choices of arrows, retain only ordered distinct endpoints, and record equality endpoints as first meetings. Only a strictly ordered previous pair can contribute a meeting. A diagonal initial pair sending both paths to the same child is excluded from the meeting count.

Proof of recursion. An ordered pair of paths at time t+1 has ordered parents at t (except for the permitted common start at zero). Deleting the last edges gives a state counted by A_t, and its last arrows appear in one of the four updates. Conversely each updated state extends witnesses of its parent state, and retaining strict order prevents all earlier meetings. Same-parity nearest-neighbour edges cannot cross without equality at a lattice time; linear interpolation therefore has exactly the same strict-order test throughout each open step. Equality of endpoints from a strict parent pair is a genuine first contact. Induction proves correctness.

Independent exhaustive path enumeration agreed with this recursion on 200 random finite systems, covering 685 distinct meeting sites, with zero mismatches. Includes branching probabilities 0, .1, .3, .7, 1; width 5--9 sites; time horizon 2--5 steps; seed 36012. Raw check summary: dp_checks.json. This finite-model test does not certify convergence of continuum meeting-point counts.

Fresh deliberately small scaling diagnostic: branching probability h; spatial scale h; time scale h^2; paths killed at +/-3; count window [-1,1] x [0.1,0.5]. Three samples per scale, with raw data in scaling_samples.jsonl:

- h=.1: counts 5,3,7; mean 5.
- h=.05: counts 16,14,8; mean 12.6667.
- h=.025: counts 11,6,25; mean 14.

The sample variability is large. These observations do not distinguish a finite limit from slow divergence. The boundary truncation excludes potential witnesses starting outside the strip; its error was not bounded for these samples. Maximum matrix size 241 x 241 Boolean entries, well below 1 GB; the longest individual sample took about 2.3 seconds. Prior September simulations in the read-only repository were read as hints and not incorporated as newly verified evidence.

## 7. Hostile-referee audit

- **Random sites versus deterministic sites.** Section 3 uses the simultaneous all-points outgoing-tail bound of Theorem 2.11, not the statement that a deterministic point has a unique path. An initial draft incorrectly attributed deterministic-slice uniqueness to that theorem; it was replaced before accepting the proof. Up to three outgoing tails per marginal web is sufficient. In the survey, outgoing web equivalence is explicitly equality for the entire future, so it genuinely gives a finite set of tails.
- **Barrier direction.** The high barrier is left-most, blocking a net path above it from crossing downward; the low barrier is right-most, blocking a path below it from crossing upward. Reversing these choices would fail. Their Gaussian bounds use only their marginal laws and Borel-Cantelli, so dependence of the two webs causes no problem.
- **Barrier start time.** Proposition 3.14 requires comparison at a time strictly after the paths' starts. The localization proof obtains a strict comparison just after s by continuity, using pi(s)>n or pi(s)<-n. It never applies the proposition directly at the starting time.
- **Random localization radius.** Finiteness is proved simultaneously on all deterministic integer intervals before choosing random n. No expectation estimate with a random interval is assumed.
- **Strict order.** A fixed pair of tails has at most one admissible contact even if it meets and separates infinitely often later. For any second proposed contact the first equality lies in the prohibited strict-order interval. Lean checks this exact implication.
- **Exceptional time slices.** Deterministic s is essential. Proposition 3.18 does not imply local finiteness at a random first-contact time. Kou's theorem quantifies a genuine exceptional-time set and supplies no avoidance statement for the proposed recursion.
- **Time-zero source equality.** The definition allows equal starting positions if the paths separate immediately after zero. The localization uses s>0, where strict order forces distinct slice positions. The finite algorithm permits initial diagonal pairs only when they produce distinct children.
- **Short bubbles.** Two paths that coincide up to a positive separation time do not satisfy strict order on (0,t); their bubble top alone is not a PMRCA witnessed by that pair.
- **Approximation.** Strict order is not closed under uniform convergence. For example f_n(u)=-(1-u)/n and g_n(u)=(1-u)/n meet first at 1 and are strict on (0,1), but both limit functions are identically zero. Thus a scaling-limit theorem for path collections does not alone transfer counts or certify local finiteness.
- **Countable unions.** For each fixed s the canonical-tail set is locally finite. Allowing s to vary over rational times is a countable union, which need not be locally finite. This proof therefore does not cover arbitrary finite-hop witnesses, let alone all net paths.
- **Finite graph lead.** Proposition 4.9 represents endpoint routes using edges that stand for families of net paths. Finite vertex count does not imply finite path-tail count or finite internal first contacts. No claim that all PMRCAs are graph vertices is established.
- **Three-arm reduction.** The arcs need not be forward-oriented from z to the past boundary; graph-theoretic connectivity in Conjecture 1.13 deliberately ignores direction. Their time-coordinate ranges make the forward arm disjoint from the two backward arms except at z. The definition must exclude deleting z itself, as is implicit in the source.
- **Finite counterexample scope.** The arrow diagram refutes the inference from containment/planarity alone. It is not claimed to disprove a Brownian-net theorem or the local-finiteness conjecture.
- **Numerical scope.** The exact finite recursion was checked against exhaustive enumeration, including zero branching and full branching. The nine scaling samples are too few, and their boundary error is uncontrolled. They provide no proof and no persuasive evidence against slow divergence.

Lean verification: `lake env lean ~/brain_workers/TRIO_1011/op/F0036/OrderedContact.lean` run from ~/lean_verify exited 0 with no output. It imports only Mathlib.Data.Real.Basic, has no sorry or native_decide, and uses an ordinary kernel-checked order proof. The first attempt failed because PowerShell wrote a UTF-8 BOM before import; removing the BOM fixed that parse error. No failed compilation is being reported as checked.

## 8. Precise remaining gap and final assessment

Fix deterministic s>0 and p<q in Xi_s. Let E_s(p,q) consist of all (x,t), t>s, admitting net paths started at (p,s),(q,s) which are strictly ordered throughout (s,t) and equal at (x,t). A sufficient missing theorem is: almost surely, simultaneously for every pair p<q in the countable Xi_s, E_s(p,q) intersects every compact box in R x (s,infinity) finitely. Section 2 and a finite union would then prove F0036. This condition is stronger than necessary, since the witnesses need not extend to histories strictly ordered since zero; no equivalence is asserted.

What is missing is control of later first contacts between different choices of continuations after the inward extremals have already met. Finite slice positions, local finiteness of relevant separation points, and the canonical-tail special case do not supply that control. Alternatively, proving the local-finiteness part of the older three-connected-point conjecture would suffice by Section 5, but that conjecture has not been proved here either.

Verdict: PARTIAL. A localization reduction, a canonical-tail special case, a conditional reduction to an older conjecture, and an exact finite obstruction to a prior shortcut are proved. No proof or counterexample to the full Brownian-net conjecture has survived the audit, and no exact printed solution was identified in the bounded searches. Novelty of the partial statements is not claimed.

## 9. Reopened attempt: two new approaches (2026-10-12)

**Approach A: transfer an image-set event through local reversibility.** The previous attempt used a conditional three-connected-point reduction, but did not use Proposition 3.6 of Special points of the Brownian net. That proposition's proof states equivalence of the local laws of N_0 and the stationary backbone image on compact sets strictly above zero. Reverse a finite-horizon PMRCA witness configuration in the backbone image and try to identify the reversed point with a relevant separation point. Unlike duality, this is time reversal of forward trajectories. The decisive checks are whether image-set membership suffices to reconstruct every finite path segment, whether arbitrary separated branches force canonical extremals to survive, and whether the finite-horizon bad event is measurable.

**Approach B: a two-arm Palm bound from the discrete arrow model.** A PMRCA corresponds to two ordered incoming arms from time zero. Apply planar vertex-Menger duality to characterize failure of such arms by a one-vertex bottleneck; seek a bound P(an adjacent pair has two surviving historical arms) <= C h at diffusive lattice scale h. Since ordinary merging sites have order 1/h intensity, this would give a uniform PMRCA intensity bound. The separate remaining requirement would be approximation of continuum strict first contacts by discrete two-arm witnesses; it cannot be inferred from path-set convergence alone. This approach has not been pursued previously here.

Approach A is selected because the local absolute-continuity theorem and image-set reconstruction theorem are already available in the checked 2009 source. No claim of a complete proof is made until the three checks above are resolved.

Research-brain query about the gap: math_recall.py "Brownian net first meeting arbitrary hopping Schertzer Sun Swart local reversibility maximal meshes". Returned cards were unrelated (including generic topology and spectral averaging), providing no theorem on the gap.

## 10. New checked lemma: finite segments in the backbone image
Write B=N_{-infinity} for the image of all net paths started at minus infinity. Assume the source's image-set identity (1.16), including T=-infinity. Every continuous real-valued forward path segment f:[u,v]->R whose graph is contained in B is a segment of a backbone net path.

Proof. Because (f(u),u) and (f(v),v) belong to B, choose backbone paths alpha and beta through these endpoints. Define gamma to be alpha up to u, f on [u,v], and beta from v onwards. The endpoint equalities make gamma continuous, including the compactified endpoints inherited from alpha and beta. Its starting time is minus infinity, and its entire graph is contained in B. Equation (1.16) therefore places gamma in N_{-infinity}. Its restriction at any finite time is a net path, either by the wedge characterization or by the same image identity after attaching the existing past. QED.

This lemma is about the stationary backbone image, not an arbitrary closed set. It avoids identifying reversal of a forward path with a dual path.

## 11. Candidate full argument being audited
For deterministic 0<s<a<=T<U and spatial bound R, define a closed-image observable: count points (x,t) in [-R,R] x [a,T] admitting two continuous graph segments in the image over [s,U], strictly ordered on [s,t), equal at t, and equal on [t,U]. If their entire graphs lie in a fixed compact D=[-m,m] x [s,U], this is an observable of the image restricted to D alone.

In the stationary backbone, reverse the two segments. Their common forward continuation becomes a common incoming reversed segment from -U to -t. Their strictly ordered historical segments become two outgoing paths separated throughout (-t,-s]. Backbone reversibility and Section 10 make the reversed segments actual net paths. If every such pair gives a (-U,-s)-relevant separation point, Proposition 4.7 bounds the count by a locally finite relevant-separation set in the reflected target box.

The local-law equivalence in equation (3.3) of the proof of Proposition 3.6 (SSS09) would then transfer finiteness of this observable from the backbone to N_0 on each fixed D. To cover all original witnesses simultaneously, one must prove a single random finite spatial bound for every witness visiting the target box; merely assigning a different D to each witness would not suffice.

Remaining checks before accepting a full proof: (i) arbitrary separated outgoing paths imply canonical relevant separation at the same point; (ii) the infinite-count image event is universally measurable; (iii) all witnesses have a common finite spatial bound on [s,U].

## 12. Outcome of the reopened approach and hostile audit

A full proof has now been written in PROOF.md. It closes the general-switching gap through a different reduction: form an observable of a compact occupied image window, transfer its null event from the stationary backbone using local absolute continuity, and identify its reversed configurations as surviving relevant forks. The old two-site recursion is no longer needed.

The nontrivial steps have complete proofs there:

1. A finite continuous segment in the backbone image can be grafted to existing backbone past/future paths; the published image-set identity then places it in the net.
2. Two genuinely incoming net paths with separated future branches give a true separation point (Lemma 3.12). Theorem 1.11(a),(b), Theorem 1.12(b), and the subscript-s type definition identify true incoming l,r bounding the two branches near the fork. One-sided containment propagates the bounds, proving relevance for the whole fixed horizon.
3. The infinite-count image event is analytic: strict order is encoded by countably many positive minima on compact subintervals; a sequence of distinct contacts with continuous witnesses is a Borel relation. Completed null events transfer under absolute continuity.
4. The primary source's exact reversal is space-time rotation (-x,-t), so one must exchange the two curve labels. An early draft used only temporal reflection; the accepted proof uses the original theorem's rotation and requires no extra symmetry assertion.
5. A common random spatial bound is proved for every time-zero path hitting the target box, using countably many deterministic-start extremal barriers. Assigning a different bound to each witness would not justify the conclusion, and is explicitly avoided.
6. The proof transfers only local-image events on deterministic compacts strictly above time zero. It does not transfer the whole time-zero ancestry or assume a density bound survives absolute continuity.

The original Sun–Swart paper was fetched and its image-set property (including T=-infinity), containment, and backbone rotation statements checked directly. The 2009 equation (3.3) and separation-point structure were re-read. All needed statements are published theorems or intermediate assertions proved in a published theorem's proof. None is an unproved conjecture.

An independent finite-graph test checked the geometric contact/fork correspondence on 500 fresh random occupied arrow images, seed 3612: 1,562 contact sites, zero mismatches. It computes forward first contacts by ordered-pair reachability and reversed surviving forks by greedy outer reverse paths. The raw per-case data are in reversal_checks.json and the script in reversal_experiment.py. This test checks the finite geometric step only; Brownian reversibility and local equivalence remain the published inputs.

SurvivingExtrema.lean formalizes the order implication l<=f<g<=r => l<r over a fixed interval. It uses an ordinary kernel proof, imports only Mathlib.Data.Real.Basic, and has no sorry/native_decide. Its check is queued through the machine's shared Lean-slot mechanism; it will be recorded as checked only after a successful exit.

The appended corollary in PROOF.md also establishes the sufficient missing assertion from Section 8: for every fixed deterministic s>0, the union of E_s(p,q) over p<q in Xi_s is locally finite above s. Deterministic-time hopping extends its witnesses back to time zero; no claim is made for a random cut.

Mathematical assessment: SOLVED by deduction from the checked published results. The full handwritten argument has survived the documented self-audit; its validity does not depend on the auxiliary finite-order Lean check, which remained queued at closure and is not certified as checked. This is not SOLVED_IN_LITERATURE: none of the inspected papers states and proves the exact conjecture as posed. Independent external refereeing and novelty assessment are not claimed. The first attempt's PARTIAL verdict and Sections 1–8 record the historical stopping point and are superseded by this reopened proof.

Additional quantitative audit: the stationary image-observable count is bounded in expectation by 2 integral_C Psi(U-t)Psi(t-s) dxdt, uniformly in the spatial witness radius. The bound follows from the pointwise relevant-fork injection and the original density formula, not from numerical extrapolation. It provides the stationary null event used for local-law transfer; it is explicitly not transferred as a first-moment estimate to the time-zero image.
2026-10-12 final verification note: the new SurvivingExtrema Lean job remained waiting for the shared slot for over half an hour. No successful compilation result was received, so this auxiliary file is not called kernel-checked. The old OrderedContact result from the first attempt remains checked. The full stochastic proof is verified on paper against the listed published inputs. No mathematical gap was identified.
