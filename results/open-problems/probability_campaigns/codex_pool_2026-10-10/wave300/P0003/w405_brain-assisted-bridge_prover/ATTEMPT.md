# P0003: buffered restriction bridge (w405)

The target and scope are in STATEMENT.md. Current openness: UNKNOWN. P0003's primary source is Grimmett Question 2.2: fixed length, origin rooted, free endpoint. The chordal critical-fugacity model considered in C1 is a distinct ensemble. This packet proves finite counting and buffer lemmas and refutes two shortcuts; it does not solve P0003. Independent adversary: w406; referee: w407; all independent verdicts are pending.

## Prior attempt digest

The 2026-09-07 ranking and the Lean campaign's annotated list label P0003 attempted_un but contain no proof. The initial intake's C0096-A001 attempt explicitly lists both crossing/tightness and limit identification as missing for critical n=0. Its informal claims about other n are not used as theorems. Targeted P0003 searches of H_20260912 and I_20260914 found no exact-ID text record in the inspected text formats; this is a bounded negative search, not proof that no record exists elsewhere. The inspected Team O board has no exact P0003 row; it assigns the related C0095 observable-convergence task to w334. No shared artifact has been changed. This lane takes only buffered obstacle-transfer and ensemble bookkeeping, disjoint from proving parafermionic scaling limits.

P0003's primary source is Grimmett, arXiv:2205.07318v1, Question 2.2 (PDF p. 3). The related chordal conjecture is Duminil-Copin--Smirnov Section 4, Conjecture 1. Their Theorem 1 supplies the critical fugacity, not a scaling limit. Lawler--Schramm--Werner (LSW), arXiv:math/0209343v2, Definition 3.1, Lemma 3.2, Proposition 3.3 and Theorem 6.1 identify a continuum chordal law after its avoidance probabilities and sample-space conditions are obtained. The required scar is perceptron_proof_open_gaps_fleet_2026_07_12: a checked local fix cannot establish the whole proof.

## L1. Exact finite-graph restriction identity

Let G be a finite embedded graph with distinct marked vertices a,b. Let Gamma_G be its vertex-simple a-to-b paths, with polygonal traces. Give gamma weight w(gamma)>0; use w(gamma)=x^length(gamma) for critical SAW. Suppose Z_G=sum over Gamma_G of w(gamma)>0. For a closed obstacle A not containing a,b, form G^A by deleting every vertex in A and every edge whose embedded trace meets A. Retain the same marks, weights and path conventions. Then

P_G[trace(gamma) intersects A is empty] = Z_(G^A)/Z_G.

If Z_(G^A)>0, the conditional law given avoidance is exactly the weighted SAW law on G^A.

Proof. The surviving paths of G^A are exactly the paths of G avoiding A. This is a weight-preserving bijection; sum the weights and divide by Z_G. Dividing the surviving weights by Z_(G^A) gives the conditional law. Edge deletion is necessary: testing only vertices would miss crossings between lattice vertices. No independence is asserted or used.

For the actual fixed-n target, let c_n(G;0) count every n-step SAW from 0, summed over all endpoints. The identical bijection gives P_n[avoid A]=c_n(G^A;0)/c_n(G;0) whenever the denominator is positive. This remains true on a locally finite infinite graph: the fixed-n rooted path collection is finite. Multiplying all these fixed-n path weights by x_c^n leaves the uniform law unchanged.

These identities are exact. They supply neither counting asymptotics nor conformal invariance.

## L2. Outer buffers transfer avoidance without a boundary-atom hypothesis

Let S be a compact metric space, and K_n,K random nonempty compact subsets with K_n converging in distribution to K in Hausdorff metric. Let A be a fixed nonempty closed subset of S. For each positive integer m suppose A_m is closed and

N_(r_m)(A) subset A_m subset N_(R_m)(A),

where N_t is the closed t-neighborhood, 0<r_m<=R_m, and both radii tend to zero. Suppose, for each fixed m,

lim as n tends to infinity P[K_n intersects A_m is empty] = q_m,

and lim as m tends to infinity q_m=q. Then P[K intersects A is empty]=q.

Proof. Set d_n=dist(K_n,A), d=dist(K,A). The distance map is 1-Lipschitz for Hausdorff metric, so d_n converges in distribution to d. Compactness makes avoidance equivalent to strictly positive distance. For each m,

P[d_n>R_m] <= P[K_n avoids A_m] <= P[d_n>r_m].

Portmanteau applied to the open interval (R_m,infinity) and the closed interval [r_m,infinity) gives

P[d>R_m] <= q_m <= P[d>=r_m].

As positive radii tend to zero, both outer terms tend to P[d>0], including when d has an atom at zero. Squeezing gives q=P[d>0]. This is a full elementary proof. It takes the n limit for each fixed m first. It requires no rate, uniformity over m, diagonal interchange, independence, coupling, or assertion that boundary contacts have probability zero.

The lemma is for compact traces. It does not provide tightness in a curve metric. Its new contribution to this packet is explicit bookkeeping of the buffer inputs and limit order; no novelty claim is made.

## R1. Raw avoidance probabilities need not pass to a weak curve limit

Take D=(-1,1)^2, a=(-1,0), b=(1,0), and the closed boundary-attached obstacle A=[-1/4,1/4] times [-1,0]. Let gamma_n be the polygonal simple curve a -> (0,1/n) -> b. Each trace avoids A; its deterministic avoidance probability is 1. The uniform curve limit gamma is the horizontal segment a -> b, which meets A; its avoidance probability is 0. The curves converge uniformly under the same piecewise linear parameterization, with error at most 1/n.

Thus even simple limiting curves and fixed distinct boundary endpoints do not justify replacing a discrete avoidance event by the corresponding limiting event. This refutes that general inference, not the SAW conjecture. Positive outer buffers detect the contact: for every fixed positive buffer radius the curves eventually hit the buffer. L2 repairs exactly this discontinuity once buffered ratios are supplied.

## L3/R2. Length mixing does not identify a fixed-length ensemble

For any finite path ensemble on G, write c_k for the number of k-edge paths (with the chosen endpoint convention), and p_k=c_k(G^A)/c_k(G) when c_k>0. The fugacity-weighted avoidance probability is

q_x(A) = sum_k pi_x(k) p_k(A), where pi_x(k)=x^k c_k / sum_j x^j c_j.

Proof. Group the weight sum in L1 by length. This is an exact finite identity and also holds for an absolutely convergent infinite sum. It is an average over lengths, not an equality with any particular p_n. At fixed length, fugacity cancels completely.

Explicit family: for each N>=2 let G_N be a cycle with marked a,b splitting it into arcs of lengths N and N+2. There are exactly two simple marked paths. Put an obstacle on an internal vertex of the longer arc. Then p_N=1 and p_(N+2)=0, while q_x=1/(1+x^2) for every N and every x>0. Thus the weighted ratio converges as N grows while the shorter fixed-length avoidance probability differs by x^2/(1+x^2). This finite graph family refutes a general ensemble-substitution inference, not a honeycomb scaling-limit theorem. It also shows the gap persists with fixed endpoints before the further free-endpoint distinction in P0003.

## C1. Conditional chordal SAW-to-SLE identification (distinct from P0003)

Fix the bounded Jordan-domain lane in STATEMENT.md. Assume these unproved inputs:

T. The critical SAW laws are tight in the uniform curve metric modulo increasing reparametrization, and every subsequential limit is a simple curve from a to b otherwise in D.

B. For every smooth admissible boundary hull A away from a,b, choose closed outer buffers A_m satisfying L2, still away from the marks, with D minus A_m simply connected. Let F:D -> H map a to 0 and b to infinity. For each fixed m, the exact edge-deleted partition ratio tends, as delta tends to zero, to Phi_(F(A_m))'(0)^(5/8). Here Phi_B:H minus B -> H fixes 0,infinity and has derivative 1 at infinity.

C. The chosen hull buffers have Phi_(F(A_m))'(0) -> Phi_(F(A))'(0). This is a boundary conformal-map convergence input; it must be verified for the chosen buffers, not inferred just from Hausdorff convergence. LSW Lemma 2.1 proves a relevant smooth-hull approximation on one side. It does not, by itself, certify all metric-buffer geometry demanded here.

For any curve subsequence, the trace-image map is continuous into compact sets. L1 and B provide the fixed-m probabilities. L2 and C give the avoidance formula for every smooth admissible A. Map the simple trace by F, including infinity in the compactification. It belongs to LSW's sample space: it is connected, unbounded, meets the real line only at 0, and its complement in C is connected. Proposition 3.3 identifies its law from the smooth-hull formula with exponent 5/8; Theorem 6.1 identifies that law as the SLE(8/3) trace law. An oriented simple trace with fixed endpoints determines its unparametrized curve; the standard measurable identification then yields the same curve law. Tightness and uniqueness give convergence.

Status: conditional proof sketch, using the cited LSW theorems. Neither T nor B is proved here. The measurable identification of simple images with oriented curve classes should be checked by the referee if this conditional sketch is promoted. Arbitrary Hausdorff compact-set convergence alone cannot replace T.

## Hardest remaining gap for P0003 and unsuccessful closing attempt

For the exact P0003 ensemble, the single hardest bridge sought here is a fixed-length macroscopic counting estimate: under a stated rescaling and proposed limiting geometry, identify c_n(G_n^A;0)/c_n(G_n;0) on buffered obstacles. Neither the critical connective constant nor the length-averaged ratios determine these numbers. L3 makes that obstruction exact. Curve tightness and the precise scaling/target geometry remain separately necessary. No conversion from C1 to the free-endpoint fixed-n claim has been proved.

Within the related chordal model, the hardest missing estimate is B: at x_c, prove for each fixed buffered hull the ratio Z_(G_delta^A_m)/Z_(G_delta) tends to the boundary conformal derivative to the power 5/8. Pointwise convergence for each buffer is sufficient; uniformity in m is not required by L2.

Attempt: combine the exact finite restriction law with the known critical fugacity and the parafermionic contour relation to infer B. The first two only fix a normalization and the finite conditional law. The contour relation constrains signed winding-weighted sums, whereas B compares positive two-endpoint partition functions in two domains. No compactness bound or estimate removes winding cancellation, and no theorem checked here controls the ratio. The primary source explicitly keeps normalized observable convergence conjectural. Thus this attempted closure fails at B, before LSW may be invoked. T remains a separate essential gap. No per-row estimates are multiplied.

NEXT: Referee checks L2, R1 and L3/R2; the next proof step is a fixed-length buffered counting-ratio estimate, with scaling geometry and curve tightness kept explicit.
