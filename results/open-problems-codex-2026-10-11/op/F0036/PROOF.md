# F0036: local finiteness by local equivalence with the reversible backbone

2026-10-12. This is a proof deduced from published Brownian-net theorems. It is not a claim that an inspected paper already states Conjecture 8.3 as a theorem. Novelty has not been established.

## Statement

Let N be the standard Brownian net and let N_0 be its paths started at time exactly zero. Set

M = {(x,t): t>0, there are pi,pi' in N_0 with pi(u)<pi'(u) for every 0<u<t, and pi(t)=pi'(t)=x}.

Then, almost surely, M is locally finite in R x (0,infinity).

Throughout, an image set is a subset of space-time; it is distinct from a collection of paths. Write A_T for the image of all net paths with starting time T, and B=A_{-infinity} for the stationary backbone image. The order of spatial and temporal coordinates is (x,t).

## Published inputs and their precise uses

1. **Image-set property.** Schertzer–Sun–Swart (2009), equation (1.16), PDF p.14, quoting Sun–Swart (2008), Proposition 1.13: almost surely, for each T in [-infinity,infinity), the paths in N started at T are exactly the continuous paths in the path space with starting time T whose entire graphs lie in A_T. We use T=-infinity, to reconstruct finite graph segments in B by attaching an existing past and future. No image reconstruction for an arbitrary closed set is assumed.
2. **Backbone reversal.** Schertzer–Sun–Swart (2009), Section 3.2, PDF p.31, cites Sun–Swart (2008), Proposition 1.15: the law of B is symmetric under time reversal. In its original precise formulation, the space-time rotation J(x,t)=(-x,-t) sends B to a set with the same law as B. We use this rotation and exchange the labels of the two curves to preserve their spatial ordering. This is reversal of the occupied forward image, not the dual net.
3. **Local equivalence with the backbone.** In the proof of Proposition 3.6 (Local reversibility), SSS09, PDF pp.31–32, equation (3.3) is proved:

   Law(A_T cap D) is equivalent to Law(B cap D)

   for every deterministic compact D contained in R x (T,infinity). Equivalence means mutual absolute continuity. Only Law(A_0 cap D) << Law(B cap D) is needed. The source's proof proves (3.3) itself, not merely a consequence asserted here.
4. **Recognition and structure of separation points.** SSS09, Lemma 3.12, PDF p.36: a separation point of two net paths, both started strictly before the point, has type (p,pp)_s. Theorems 1.11(b) and 1.12(b), PDF pp.12–13, with the outgoing configuration of type (p,pp)_s, bounds each outgoing net class locally between its left/right web representatives. At this type the representatives used below are true marginal-web paths, and the left-most and right-most outgoing representatives are continuations of incoming web paths. See Proposition 2.6 and the type definition in Section 1.3. We use these facts to identify arbitrary surviving branches with a relevant separation point at the same location.
5. **One-sided containment.** Survey Proposition 3.14, PDF p.22, citing Sun–Swart (2008), Proposition 1.8: after an ordering comparison at a time strictly later than both start times, a net path cannot cross a left-web path from right to left, or a right-web path from left to right. It propagates the local bounds in input 4 for the entire desired interval. It also supplies spatial localization.
6. **Relevant-separation finiteness.** SSS09, Proposition 2.9, or survey Proposition 4.7, PDF pp.30–31: for deterministic S<H, the set R_{S,H} of points reached from time S with outgoing canonical left/right paths strictly separated on (t,H) is almost surely locally finite inside R x (S,H). Our target box lies strictly inside this strip. The finite expected density 2 Psi(t-S) Psi(H-t) suffices. Incoming canonical representatives at a separation point give the same definition as their outgoing restrictions.

All these inputs are assertions for almost every realization simultaneously over the paths or points they discuss; we do not replace a fixed deterministic-point assertion by an uncountable intersection.

## Lemma 1: finite segments in B are net segments

On the probability-one event of the image-set property, let u<v and let f:[u,v]->R be continuous with graph contained in B. Choose backbone paths alpha and beta through (f(u),u) and (f(v),v), respectively; they exist by the definition of B. Concatenate alpha before u, f on [u,v], and beta after v. This defines a path gamma started at minus infinity. It is continuous at u,v by the endpoint identities and at the compactified endpoints because its tails are unchanged. Its entire graph is contained in B. The image-set property therefore makes gamma a backbone path in N. Thus f is a segment of a genuine net path. Restrictions to a finite starting time are net paths: the restriction preserves the property of not entering any dual wedge from outside, so the wedge characterization applies. QED.

This lemma holds for every continuous finite segment contained in B, not just for ones selected before seeing B.

## Lemma 2: a common incoming segment and two surviving branches imply relevance

Fix deterministic S<H. Suppose two net paths eta_1,eta_2 have starting time S, coincide on [S,t], and satisfy eta_1(v)<eta_2(v) for every t<v<=H, with S<t<H. Put z=(eta_1(t),t).

Both paths started strictly before t. They separate at z in the sense of SSS09 Definition 2.3, so Lemma 3.12 makes z a true separation point of type (p,pp)_s. There are two outgoing equivalence classes. The two paths cannot belong to the same class: such equivalence would give a sequence of equality times decreasing to t, contradicting their strict separation on (t,H]. The left path belongs to the left class and the right path to the right class.

By Proposition 2.6(iii), choose incoming l in W^l and r in W^r which separate at z. Their ordering just after the meeting is l<r, by the left/right ordering constraint, so l belongs to the left outgoing class and r to the right outgoing class. By Theorem 1.11(a),(b), their extended representatives in these classes agree strongly with these true web paths near z. Theorem 1.12(b) therefore supplies the local outer bounds for eta_1 and eta_2 using these same incoming l,r. For some epsilon>0,

l(v) <= eta_1(v) < eta_2(v) <= r(v)    for t<v<t+epsilon.

Fix any w in (t,H). Choose v with t<v<min(w,t+epsilon). This comparison occurs strictly after the start times of l,r and eta_i (without any assumption about a deterministic starting point at z). Containment propagates l(w)<=eta_1(w) and eta_2(w)<=r(w). Hence l(w)<r(w). Since w was arbitrary, l<r on (t,H). The common incoming path eta_1 reaches z from S. Therefore z belongs to R_{S,H}. QED.

Notice the distinction from the rejected earliest-meeting shortcut: this lemma concerns an actual fork and separated outgoing paths, and uses outward extremals to bound them. It does not identify first contacts between different source continuations with an inward-extremal contact.

## Lemma 3: an image observable for finite-horizon meetings is measurable

Fix numbers 0<s<a<=b<U, R>0, and an integer m>=R. Let

C=[-R,R] x [a,b],     D_m=[-m,m] x [s,U].

For a closed F subset of D_m, let P(F) be the set of points (x,t) in C for which there are continuous functions f,g:[s,U]->[-m,m] with both graphs contained in F and

f(v)<g(v) for all s<=v<t;     f(v)=g(v) for all t<=v<=U;     f(t)=x.

We claim that E_m={F: P(F) is infinite} is analytic, and therefore universally measurable, in the hyperspace of compact subsets of D_m, allowing the empty set.

Proof. The continuous-function space with the uniform metric is Polish. The tuple conditions on (F,f,g,t) are Borel:

- graph containment is closed, expressible as maximum distance of the graph to F equal to zero (treat the empty set separately);
- equality on [t,U] is closed, since max_{v in [t,U]} |f(v)-g(v)| depends continuously on (f,g,t);
- strict order on [s,t) is equivalent to the countably many positive minima

  min_{v in [s, s+(1-1/k)(t-s)]} (g(v)-f(v)) > 0,     k=2,3,...;

  each minimum depends continuously on (f,g,t). Indeed uniform perturbation changes a minimum by at most the uniform error; moving interval endpoints changes it by a quantity tending to zero by uniform continuity of the limiting function;
- t in [a,b] and f(t) in [-R,R] are closed conditions.

Now take a sequence (f_j,g_j,t_j) of such witnesses and require all their points (f_j(t_j),t_j) to be distinct. This is a Borel relation, since pairwise distinctness is a countable conjunction of open conditions. A set has infinitely many points exactly when it has such a countably infinite sequence of distinct points with witnesses. Hence E_m is the projection of this Borel relation from a product of Polish spaces, so is analytic. Analytic sets are measurable in the completion of every Borel probability measure on a Polish space. In particular, if one Borel law gives E_m probability zero and another law is absolutely continuous with respect to it, the latter also gives E_m probability zero: cover the completed-null event by a Borel null set. QED.

No assertion that strict order is closed is made. Its countable positive-minimum formulation above is the necessary Borel formulation.

## Lemma 4: the observable is finite for the stationary backbone

For each deterministic choice of s,a,b,U,R,m above, P(B cap D_m) is almost surely finite.

Proof. Apply J(x,t)=(-x,-t). The configurations defining P become configurations in J(B) over the compact time interval [-U,-s]: the two curves have a common incoming portion on [-U,-t] and strictly separated outgoing portions on (-t,-s]. Exchanging the two curve labels restores their left/right spatial order after the spatial reflection. The contact point becomes (-x,-t), in J(C)=[-R,R] x [-b,-a].

Consider this reflected configuration observable first in an ordinary backbone image B. Lemma 1 extends each of its two curves to an actual net path and then restricts it at S=-U. The paths coincide through the fork at -t and remain strictly separated until H=-s. Lemma 2 therefore places that fork in R_{-U,-s}. Different points of the observable produce different relevant separation points. Since [-b,-a] is strictly inside (-U,-s), relevant-separation local finiteness gives only finitely many such points in J(C).

This is a probability-one assertion for the observable evaluated at B. Reversal invariance of the law of B makes it also a probability-one assertion for the observable evaluated at J(B). Space-time rotation, with this exchange of curve labels, is a bijection between that latter observable and P(B cap D_m), proving the lemma.

We use reversal in distribution, not the false assertion that the time reversal of a path in the original net belongs to the same original net. Lemma 1 is applied only in a realization with the ordinary backbone law. All configurations are confined to the deterministic compact window used by the observable. QED.

## Lemma 5: the observable is finite for the time-zero image

For every fixed m, P(A_0 cap D_m) is almost surely finite.

Proof. D_m is a deterministic compact set whose earliest time s is strictly positive. Equation (3.3), the local-equivalence result, applies with T=0. Lemma 4 makes E_m a null event under the backbone-image law on D_m. Lemma 3 allows this analytic null event to transfer under absolute continuity. It is therefore null under the A_0-image law on D_m. Intersecting the probability-one events over the positive integers m makes this statement simultaneous in m. QED.

The transfer asserts only almost-sure finiteness; no integrability or numerical intensity bound for P(A_0 cap D_m) follows from absolute continuity alone.

## Lemma 6: one spatial window suffices for all witnesses visiting C

Almost surely there is a finite random integer m>=R such that every time-zero net path visiting C stays in [-m,m] throughout [s,U].

Proof. For each positive integer n, choose the left-web path L_n started at (n,s) and the right-web path R_{-n} started at (-n,s). These deterministic starting points have unique marginal-web paths almost surely, simultaneously in n. Marginally they are Brownian motions with drifts -1 and +1. With h=b-s, for n>R+h,

P(inf_{[s,b]} L_n <= R) <= 4 exp(-(n-R-h)^2/(2h)),
P(sup_{[s,b]} R_{-n} >= -R) <= 4 exp(-(n-R-h)^2/(2h)).

The estimates follow from the reflection principle and a Gaussian tail bound; their sums in n are finite. Borel-Cantelli gives a finite n for which both barriers stay strictly outside the target spatial interval on [s,b]. If pi(s)>n, continuity gives a strict ordering pi(v)>L_n(v) just after s, and one-sided containment then forces pi(w)>=L_n(w)>R for all s<w<=b. Thus pi cannot visit C. Similarly pi(s)<-n prevents a visit. Every visiting path therefore has pi(s) in [-n,n]. This argument does not require finite point-set density.

Next use the left-web path L_{-(n+1)} and the right-web path R_{n+1} started at the indicated positions at time s. They are available on the same probability-one event for all integer starting positions. Because every visiting path starts strictly between these barriers at s, continuity and containment give

L_{-(n+1)}(w) <= pi(w) <= R_{n+1}(w)    for every w in [s,U].

Both barrier paths are continuous real-valued functions on the compact interval [s,U]. Their ranges are bounded. Choose an integer m>=R exceeding the absolute values of both ranges and n. This same m bounds every visiting path for the whole interval. QED.

A separate radius for each witness would not suffice; the common bound is essential.

## Conclusion

Fix C=[-R,R] x [a,b] with a>0 and choose deterministic s=a/2 and U=b+1. Work on the probability-one events of Lemmas 5 and 6, including all integers m. Let m be the common spatial bound from Lemma 6.

For any z=(x,t) in M cap C, take its two defining time-zero paths pi,pi'. On [s,t), they are strictly ordered, including at s, since s lies in (0,t). They are equal at t. Define f=pi on [s,U], and define g=pi' on [s,t] and g=pi on [t,U]. These are continuous graph segments in A_0 cap D_m. Both original paths visit C and are bounded by the common m; the modified common suffix is also bounded. No path reconstruction for A_0 is needed: only their graph containment is used. The functions witness z in P(A_0 cap D_m).

Thus M cap C is a subset of P(A_0 cap D_m), which is finite by Lemma 5. Finally intersect these probability-one assertions for the countable exhaustion C_k=[-k,k] x [1/k,k], k=1,2,... (degenerate initial boxes can be omitted). Every compact subset of R x (0,infinity) lies in some C_k. This proves almost-sure local finiteness of M with precisely the quantifiers in Conjecture 8.3. QED.

## Referee checks and scope

- The proof uses a published local-equivalence result, not an unproved bubble or three-connected-point conjecture.
- Both reversed paths have a common incoming interval of positive duration, so Lemma 3.12 applies to a genuine separation point; a fresh two-path start with no incoming history would not suffice.
- Local canonical bounds are propagated by the correct one-sided containment inequalities. Outward extremals are used; the rejected inward first-contact identification is never used.
- The same net realization need not contain time-reversed paths. Reversibility is used only at the level of an image observable's law.
- All information transferred under absolute continuity is contained in a fixed compact window strictly above zero; there is no transfer of time-zero boundary data or infinite past information.
- The infinite-count event is analytic. Its completed null status, not an unsupported Borel assertion, is what is transferred.
- The common random spatial bound is supplied independently of the count. Countably many fixed-window statements alone would not imply finiteness of their union.
- The argument allows identical time-zero starting positions if strict order holds thereafter. At the positive cut s the witnesses necessarily have distinct positions.
- No first-moment formula for the time-zero PMRCA count is claimed. Equivalent laws can have very different expectations.
- The proof uses the standard nondegenerate Brownian net of the source. The zero-branching Brownian web already has the stated local finiteness and does not have the stationary backbone used here.
- This is a complete deduction conditional only on the published inputs listed above. Independent external review and novelty assessment have not been performed.

## Corollary: the first attempt's sufficient gap is also closed

Fix deterministic s>0 and let Xi_s be the locations at s of time-zero net paths. For p<q in Xi_s, let E_s(p,q) be as in ATTEMPT.md Section 8. Then, almost surely, the union over all such p<q of E_s(p,q) is locally finite in R x (s,infinity).

Proof. At deterministic s, the simultaneous hopping statement, survey Proposition 3.15(ii), permits concatenation of any time-zero path reaching p at s with any net path started at (p,s), and similarly at q. Thus any witness defining E_s(p,q) extends to two time-zero net paths; their earlier histories may meet, but their portions from s to the contact are strictly ordered. For any compact target C strictly above s, apply Lemmas 5 and 6 with precisely this cut s and a future boundary U above C. The image observable P ignores the histories before s and therefore contains all these contacts at once. The common spatial bound still applies to every extended time-zero path visiting C. Its count is finite as proved above. A countable exhaustion proves the corollary. QED.

The required hopping theorem is simultaneous over all witnesses at each deterministic s; it is not a union over random-time hopping assertions. No conclusion is claimed for a random cut s selected from the net.

## Quantitative check on the stationary observable

The same argument gives a finite first-moment bound in the backbone, independently of the spatial witness radius m:

E[|P(B cap D_m)|] <= 2 integral_C Psi(U-t) Psi(t-s) dx dt.

Indeed, the rotated fork observable is pointwise contained in R_{-U,-s}, its cardinality has the same distribution as |P(B cap D_m)|, and Proposition 2.9 supplies the displayed expected count. Counts are measurable in completed laws by the same finite-witness projection argument as Lemma 3 (for the event count>=n). Since Psi(v)<=1/sqrt(pi v)+2, the right-hand side is at most

4R(b-a) [1/sqrt(pi(U-b))+2] [1/sqrt(pi(a-s))+2],

which is finite because U>b and a>s. This checks quantitatively that the stationary null event used in Lemma 5 is supplied by a genuine finite expected count. This estimate is only for the backbone law; absolute continuity alone does not give the same expectation estimate for A_0.

## Verification record and final assessment

The full handwritten proof above has survived the documented source and hostile-referee checks. The original Sun-Swart image-set, backbone rotation, and containment assertions were fetched and checked directly; the 2009 local-equivalence proof and special-point structure were re-read. No unproved bubble or three-connected-point conjecture is an input.

reversal_experiment.py checked the finite contact/fork correspondence in 500 occupied arrow images with 1,562 contact sites and zero mismatches. Raw data are in reversal_checks.json. This verifies finite geometry only; it does not replace the published stochastic inputs.

SurvivingExtrema.lean records the scalar order implication preserving the strict gap. Its `lake env lean` invocation waited for the automatic shared slot for over half an hour and remained queued when this attempt was closed. It is therefore NOT called kernel-checked. The inequality is proved directly in Lemma 2. The older OrderedContact.lean compiled successfully during the first attempt, but it does not formalize this stochastic proof.

Final verdict: SOLVED by the full written deduction from the checked published results. No mathematical gap remains identified in the self-audit. This is not SOLVED_IN_LITERATURE: no inspected paper states and proves the exact question as a theorem. Independent external review and novelty assessment are not claimed.
