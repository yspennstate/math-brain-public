# From disjoint witnesses to a uniform long-path bound

The statements checked are `df:wi:continuous-bk` and `df:wi:long-paths` in OpenAI, *Strict convexity and differentiability of the planar exponential first-passage limit shape* (September 24, 2026), revision `4eaee87548250b2682affda7d05d947c05554bae`. The actual source is preserved in [source-witnesses.tex](source-witnesses.tex). This proves the stated probabilistic reduction using the earlier local-event and deterministic-extraction conclusions as hypotheses. It does not verify the whole differentiability manuscript or the universal continuous-law statement T095.

## 1. Finite Bernoulli input

For a finite set I of independent Bernoulli coordinates and increasing events C₁,…,C_q, let W(C₁,…,C_q) consist of configurations x for which there exist pairwise disjoint subsets S_j of the realized one-coordinates of x, with the configuration 1_{S_j} belonging to C_j. The two-event BK theorem gives

\[
 \mathbb P(W(C_1,C_2))\le\mathbb P(C_1)\mathbb P(C_2).
 \tag{1}
\]

The input is Theorem (3.3), equation (3.4), of J. van den Berg and H. Kesten, [*Inequalities with applications to percolation and reliability*](https://sites.math.northwestern.edu/~auffing/papers/vBK.pdf), Journal of Applied Probability 22 (1985), 556–569. Their Section 3 defines positive witnesses and iterates the theorem in Corollary (3.10). Only this finite monotone inequality is an external probabilistic input here.

Here is the required iteration without a general associativity assumption. W(C₁,…,C_{q−1}) is increasing. If S₁,…,S_q witness the q-fold event, the configuration with ones on S₁∪…∪S_{q−1} belongs to W(C₁,…,C_{q−1}), and its one-set is disjoint from S_q. Therefore

\[
 W(C_1,\ldots,C_q)
 \subset W\bigl(W(C_1,\ldots,C_{q-1}),C_q\bigr).
\]

Apply (1) and induction to obtain

\[
 \mathbb P(W(C_1,\ldots,C_q))
 \le\prod_{j=1}^q\mathbb P(C_j).                    \tag{2}
\]

The events need not be distinct. Empty positive witnesses are allowed only when the corresponding event contains the all-zero configuration, in which case that increasing event is certain. The convention also handles q=0, with product one.

## 2. Upper approximation of Gamma weights

Let E be the finite union of the deterministic edge sets for a finite list of path events A₁,…,A_q. An event A_j asks for a path P in a prescribed family with

\[
 \tau(P)<b_j(P),                                   \tag{3}
\]

where the bound and the family are deterministic. Bounds can be attached to labeled copies of the same path. The family is at most countable: finite paths are finite sequences from a countable vertex set. Repeated traversal of an edge is allowed, and its weight contributes its positive integer traversal multiplicity.

For κ,λ>0 the Gamma density is positive on (0,∞), has integral one, and has no atoms. Its distribution function F is continuous and strictly increasing there, with F(0)=0 and F(t)→1. Its inverse Φ is increasing and continuous on [0,1), with Φ(0)=0; set Φ(1)=∞. Continuity at zero follows because F(ε)>0 for every ε>0. No bounded-density condition is needed.

Take independent fair bits B_{e,h}, and put

\[
 U_e=\sum_{h\ge1}2^{-h}B_{e,h},\quad
 U_e^{(t)}=\sum_{h=1}^t2^{-h}B_{e,h}+2^{-t},\quad
 \tau_e=\Phi(U_e),\quad \tau_e^{(t)}=\Phi(U_e^{(t)}).
\]

The U_e are independent uniforms. Indeed the first t bits give each dyadic interval of length 2^{−t} probability 2^{−t}; the exceptional eventually constant binary expansions have probability zero. These dyadic interval probabilities determine the uniform law. Thus Φ(U_e) has distribution F, independently across edges.

Directly, for every bit sequence,

\[
 0\le U_e^{(t)}-U_e\le2^{-t},\qquad
 U_e^{(t)}-U_e^{(t+1)}=2^{-(t+1)}(1-B_{e,t+1})\ge0.
 \tag{4}
\]

Almost surely U_e<1 for every e∈E. On this probability-one event, continuity of Φ gives τ_e^{(t)}↓τ_e. Initial rounded values may equal ∞, but are eventually finite since U_e<1. Either binary representation of a dyadic value satisfies (4); no endpoint convention changes the almost-sure limit.

Let A_j^{(t)} be A_j with rounded weights. Let D^{(t)} ask for a rounded witness for each event, with pairwise disjoint unoriented edge supports. Costs are sums over traversed edges only. The rounded events depend on finitely many independent bits and are decreasing in each bit. They satisfy A_j^{(t)}⊆A_j, and both A_j^{(t)} and D^{(t)} increase with t.

## 3. Edge certificates become positive bit witnesses

Suppose a configuration is in D^{(t)}, with witnesses P₁,…,P_q. For each j, fix all t bits of every edge traversed by P_j. Any completion on the remaining bits leaves this path's cost unchanged, so its strict inequality (3) remains true. Thus the fixed bits are a certificate for A_j^{(t)}. Different certificates are disjoint because the path supports are disjoint, even if their spatial test boxes overlap or their event labels agree.

Complement every bit, writing X=1−B, so the events become increasing; call them C_j. In certificate j retain the realized one-bits of X and set every other X bit to zero. The resulting configuration still agrees with X on the whole certificate, including its zero-bits. Consequently it belongs to C_j. Its one-set is contained in certificate j. These configurations supply pairwise disjoint positive witnesses for C₁,…,C_q. By (2),

\[
 \mathbb P(D^{(t)})
 \le\prod_{j=1}^q\mathbb P(A_j^{(t)})
 \le\prod_{j=1}^q\mathbb P(A_j).                   \tag{5}
\]

This is a containment, not an assertion that arbitrary bit certificates must be whole-edge path witnesses. In particular there is no need for the boxes, or the events themselves, to be independent.

Let D be disjoint path occurrence for the original weights. Rounded witnesses remain valid original witnesses, so ∪_t D^{(t)}⊆D. Conversely fix a configuration with finite original weights and a finite disjoint witness list for D. Every path has finitely many traversals. Its rounded cost decreases to its original cost. Every inequality has a strictly positive margin, so for sufficiently large t all q inequalities hold at once. The same supports remain disjoint. Hence

\[
 D=\bigcup_{t\ge1}D^{(t)}\quad\hbox{almost surely}.
\]

These events are measurable: they are countable unions over finite path lists of finite-coordinate strict cost tests. No measurable selection of a witness and no uniform precision over all possible witnesses is required. Continuity of probability from below and (5) prove

\[
 \boxed{\mathbb P(D(A_1,\ldots,A_q))
               \le\prod_{j=1}^q\mathbb P(A_j).}     \tag{6}
\]

This establishes `df:wi:continuous-bk`, including κ<1, repeated paths within an event family, repeated event labels and overlapping regions. The strict inequality is what justifies this upper-approximation proof at equality thresholds.

## 4. Hypotheses at one fixed scale

Fix integers s≥2, L≥1, slope b∈[−1,1], and a number a=ηs>0. Put x(z)=z₁ and r(z)=z₂−bz₁. Use the source's chunk rule: stop the first time |Δx|≥2L or |Δr|≥s; include a possibly empty final remainder. For a simple path P starting at 0, let N be its number of full chunks. Assign each chunk starting at z the index (⌊x(z)/L⌋,⌊r(z)/s⌋).

Assume the following earlier conclusions, precisely as used by the source:

1. Each A_{i,h} is a strict path event on a deterministic finite edge set, and P(A_{i,h})≤p=2q₀ uniformly over all integer i,h.
2. The deterministic extraction supplies M_tot pairwise edge-disjoint witnesses assigned to their chunk positions, and

\[
 H(P)\ge(N-1)a-4aM_{\rm tot}.                     \tag{7}
\]

3. The single fixed scale satisfies

\[
 400p^{1/16}<1/2.                                 \tag{8}
\]

The previous round checked (7) under its explicit corner and scale hypotheses. This section uses those hypotheses; it does not derive the rare-event bound in item 1 anew. All randomness in a candidate path or its chunks is permitted.

## 5. How many witnesses a bad path forces

Let B_N mean that some such path has exactly N full chunks and H(P)<Na/2. From (7),

\[
 (N-1)a-4aM_{\rm tot}<Na/2,
 \qquad M_{\rm tot}>N/8-1/4.                      \tag{9}
\]

For N≥16 the right side is at least N/16, since N/16−1/4≥0. Thus at least t=⌊N/16⌋ witnesses may be retained from the extracted disjoint family. Discarding the others preserves disjointness. This conclusion depends on the integer multiplicity, not the number of distinct event labels.

## 6. Deterministic itinerary count

Nearest-neighbor steps satisfy |Δx|≤1 and |Δr|≤1. At the first chunk exit, |Δx|≤2L exactly, because x is integer, and |Δr|≤s+1. For real z,d and d≥0,

\[
 \lfloor z+d\rfloor-\lfloor z\rfloor\le\lceil d\rceil;
\]

the corresponding absolute bound follows by reversing the endpoints. Consecutive chunk starts therefore have longitudinal index difference at most 2 and transverse index difference at most ⌈(s+1)/s⌉≤2. In particular the source's looser bound 3 in each coordinate is valid. Starting at 0 fixes the first index to (0,0), including for negative later coordinates. There are N transitions to the start of the remainder, each with at most 7²=49 choices under that loose bound. Hence there are at most 49^N index lists of length N+1. Repeated indices and a last cut at the terminal vertex are included.

For a fixed itinerary, let m_j be the number of retained witnesses assigned to its j-th position, for j=0,…,N. The m_j are nonnegative integers with sum t. Their number is

\[
 \binom{N+t}{t}.                                  \tag{10}
\]

To verify (10), write a string of t stars and N separators; the numbers of stars between consecutive separators are the m_j, including zeros. This is a bijection, and choosing the star positions gives (10). Since these choices form a subset of all subsets of an (N+t)-element set,

\[
 \binom{N+t}{t}\le2^{N+t}\le4^N,                 \tag{11}
\]

where the last step uses t≤N. Allocations belong to positions in the itinerary. Collapsing equal coarse labels would lose this correspondence; retaining all positions gives a valid overcount.

## 7. Union bound, including adaptively selected paths

For every deterministic itinerary and every deterministic allocation, list the event A_{i,h} once for each assigned witness, in position order. This produces a deterministic list of exactly t events. Repeated events remain repeated entries. Its disjoint path-occurrence event has probability at most p^t by (6).

Whenever B_N occurs, choose any realizing path and any extracted subfamily of t witnesses. Its itinerary is among those counted above, its allocation is one of (10), and its witnesses certify the disjoint occurrence of that deterministic event list. Consequently B_N is contained in the union of the finitely many list-events. This containment holds for every configuration, without conditioning on a random itinerary. It requires no independence of path chunks and no count of microscopic paths. Union bounding (11) gives

\[
 \boxed{\mathbb P(B_N)\le196^N p^{\lfloor N/16\rfloor}
                  \quad(N\ge16).}                \tag{12}
\]

The factor 196 is 49 times 4, not a separate spatial-independence estimate. Directly retaining the exact number in (10) gives the independent, stronger intermediate bound 49^N binom(N+t,t)p^t, which also implies (12).

## 8. Summability and simultaneous eventual conclusion

Condition (8) gives 0<p<1 and p^{1/16}<1/800. Therefore

\[
 R=196p^{1/16}<196/800=49/200<1.                   \tag{13}
\]

Since ⌊N/16⌋≥N/16−1 and powers of p decrease with their exponent,

\[
 196^N p^{\lfloor N/16\rfloor}\le p^{-1}R^N.
\]

Thus ∑_{N≥16}P(B_N) is finite; more explicitly its tail from M≥16 is bounded by p^{−1}R^M/(1−R). The first Borel–Cantelli lemma, which does not require independence, implies that almost surely only finitely many B_N occur. On each configuration outside this null set, choose N₀ larger than every exceptional N and at least 16. For every simple path from 0 with N≥N₀ full chunks,

\[
 H(P)\ge\tfrac12N\eta s.
\]

This is exactly `df:wi:long-paths`. The assertion is simultaneous over the countable family of finite paths. The scale s,L remains fixed throughout this probability limit.

## 9. Independent checks and limits

The finite audit in [audit.py](audit.py) checks upper rounding with exact rational arithmetic and compares two different descriptions of disjoint occurrence: direct packing of successful path supports, and positive certificates extracted from the entire finite-bit truth table. It includes repeated events, overlapping edge regions, labeled copies with different bounds, repeated edge traversals, impossible events and certain events with empty witnesses. For the nontrivial quantile fixtures it uses exponential weights; a cost below log C is tested exactly by the rational inequality ∏_e(1−U_e)^{m_e}>1/C. No floating-point threshold decision is used.

Composition counts are also obtained by dynamic programming, independent of (10). Floor-index bounds are tested over negative positions and fractional phases. The all-case arguments above, rather than the finite fixtures, establish the reduction for every positive Gamma shape and rate.

No failure was found in this link under its explicit inputs. Establishing these two lemmas neither replaces the Gamma-specific change of measure for general continuous laws nor certifies every analytic input or the Lean dependency chain. A next check can address the final `df:wi:no-corner` argument and the conversion to global Fréchet differentiability and a C¹ boundary in the conclusion section, with an explicit dependency ledger for the earlier conditional reductions.
