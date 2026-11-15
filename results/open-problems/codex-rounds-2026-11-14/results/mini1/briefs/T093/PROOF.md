# The subcritical failure probability for three colours

Let G have distribution G(n,c/n), where 0 < c < 1 is fixed. Write B for the event that G is not 3-colourable and X for its number of copies of K4. Then

\[
\Pr(B,\ X=0)=\left(\frac{c^{10}}{10}+\frac{c^{11}}8\right)n^{-4}
                 +O_c(n^{-5}).                                      \tag{1}
\]

Moreover,

\[
\begin{split}
\Pr(B)={}&\frac{c^6}{24}n^{-2}-\frac{c^6}{4}n^{-3}\\
 &+\left(\frac{11c^6}{24}-\frac{c^9}{12}
          +\frac{c^{10}}{10}+\frac{c^{11}}8-\frac{c^{12}}{1152}\right)n^{-4}
   +O_c(n^{-5}).                                                     \tag{2}
\end{split}
\]

The proof uses a finite exhaustive classification, checked by two independent programs. All graphs are simple. A copy is a subgraph, not necessarily induced. The excess of a graph H is e(H)-v(H). Constants in O_c may depend on c; there is no uniformity as c tends to 1.

## 1. The finite classification

If a graph is not 3-colourable, choose a vertex-minimal induced subgraph H that is not 3-colourable. It is connected, since otherwise a non-3-colourable component would be smaller. Every vertex of H has degree at least 3: a 3-colouring of H-v extends to v whenever its degree is at most 2. Consequently

\[
e(H)\ge\lceil 3v(H)/2\rceil.
\]

If H has excess at most 4, this inequality gives v(H) <= 8. The following is the complete labelled census for 4 <= v <= 8, minimum degree at least 3, and e-v <= 4:

| v | e | All graphs | K4-free graphs | K4-free graphs not 3-colourable |
|---:|---:|---:|---:|---:|
| 4 | 6 | 1 | 0 | 0 |
| 5 | 8 | 15 | 15 | 0 |
| 5 | 9 | 10 | 0 | 0 |
| 6 | 9 | 70 | 70 | 0 |
| 6 | 10 | 537 | 537 | 72 |
| 7 | 11 | 5670 | 5670 | 630 |
| 8 | 12 | 19355 | 19320 | 0 |

These exhaust the possible edge counts because e >= ceil(3v/2), e <= v+4, and e <= binom(v,2). The 72 graphs in row (6,10) form one isomorphism class H6; the 630 in row (7,11) form one class H7.

Here are representatives, with vertices numbered from zero:

```
H6: 01 02 03 12 14 23 24 25 35 45
H7: 01 02 03 12 13 24 35 36 45 46 56
```

H6 is a wheel with a five-cycle as rim. Vertex 2 is the hub; its rim, in order, is 0,1,4,5,3. Its automorphisms are the ten symmetries of the rim. Its hub and odd rim cannot be coloured with three colours.

H7 consists of diamonds on {0,1,2,3} and {3,4,5,6}, together with edge 24. In a diamond K4 minus an edge, the two nonadjacent vertices must receive the same colour in every 3-colouring. The first diamond forces colours 2=3, the second forces 3=4, and edge 24 contradicts these equalities. Its degree-four vertex 3 is unique. Its neighbours induce the two edges 01 and 56. An automorphism can flip either edge and can exchange the two diamonds, giving exactly 2*2*2=8 automorphisms. Thus the orbit counts also follow independently as 6!/10=72 and 7!/8=630.

For completeness, the two exhaustive checks work as follows.

* `enumerate_obstructions.py` processes vertices in their fixed numerical order. At vertex i it chooses every possible set of neighbours with larger index, consistent with the remaining edge count and the degree lower bounds. Every labelled graph occurs once: each edge is chosen at its smaller endpoint. The pruning conditions only discard branches that cannot reach degree 3 or the prescribed edge count. A recursive proper-colouring test decides 3-colourability. All permutations of each non-colourable representative verify that the entire set in that row is one orbit.
* `independent_check.cpp` enumerates every edge subset of each prescribed cardinality, using increasing fixed-population bit masks. It filters minimum degree and K4 containment directly. For colouring, it generates all 3^v assignments and their allowed edge masks. A graph is 3-colourable exactly when its edge mask is contained in one of these masks. This uses neither the first graph generator nor its colouring backtracker.

Both checks produce the table above. The exact data are in `obstructions.json` and `independent_counts.csv`; `run_independent.py` compares every entry. This finite verification is the computational part of the proof.

## 2. The probability of any larger critical obstruction

We prove that the probability of a connected subgraph of minimum degree at least 3 and excess at least 5 is O_c(n^-5).

First control component sizes. Explore the component of a fixed vertex by a queue. Each processed vertex reveals at most n independent Bernoulli(c/n) edges to undiscovered vertices. Padding each step with additional independent trials couples the numbers of newly discovered vertices below independent random variables Y_i with distribution Bin(n,c/n). If the component has at least k vertices, then after k-1 processing steps at least k-1 new vertices have been discovered. Thus

\[
\Pr(|C(v)|\ge k)\le
\Pr\left(\sum_{i=1}^{k-1}Y_i\ge k-1\right).
\]

Take t=log(1/c)>0. Using 1+x <= exp(x),

\[
\mathbb E e^{t(Y_i-1)}
 =e^{-t}(1+(c/n)(e^t-1))^n
 \le\exp(c(e^t-1)-t)=c e^{1-c}=:\rho<1.
\]

The last strict inequality follows from log c < c-1 for c != 1. Markov's inequality gives Pr(|C(v)| >= k) <= rho^(k-1). A union bound over starting vertices, with

\[
L=\left\lceil\frac{7\log n}{-\log\rho}\right\rceil+1,
\]

shows that the probability of any component with more than L vertices is at most n rho^L <= n^-6.

It remains to consider subgraphs with s <= L vertices. For fixed s <= 10, a subgraph of excess at least 5 has at least s+5 edges. The union bound

\[
\binom ns\binom{\binom s2}{s+5}(c/n)^{s+5}=O_c(n^{-5})
\]

applies; an impossible binomial coefficient is interpreted as zero. There are only ten such sizes.

For 11 <= s <= L, minimum degree 3 requires at least r=ceil(3s/2) edges. The probability that any s-set spans at least r edges is at most

\[
\binom ns\binom{\binom s2}{r}(c/n)^r.
\]

For all sufficiently large n, ecL/(3n)<1. The preceding expression is bounded by

\[
\left(\frac{en}{s}\right)^s
\left(\frac{ecs}{3n}\right)^r
\le \left[B\sqrt{s/n}\right]^s=:a_s,
\qquad B=e^{5/2}(c/3)^{3/2}.                              \tag{3}
\]

To sum this bound without a logarithmic loss, extend a_s to real s and differentiate:

\[
\frac{d}{ds}\log a_s=\log B+\tfrac12\log(s/n)+\tfrac12.
\]

Uniformly for 11 <= s <= L=O_c(log n), this is at most -(log n)/3 for sufficiently large n. Therefore a_(s+1)/a_s <= n^-1/3, and

\[
\sum_{s=11}^L a_s\le \frac{a_{11}}{1-n^{-1/3}}=O_c(n^{-11/2}).
\]

Adding the fixed-size and large-component bounds proves the asserted O_c(n^-5) probability. In particular, if a K4-free non-3-colourable graph contains neither H6 nor H7, its vertex-minimal obstruction has excess at least 5 by the census, and this event has probability O_c(n^-5).

## 3. Converting small-copy counts into a probability

Let Z count all copies of H6 and H7. With (n)_s=n(n-1)...(n-s+1), their symmetry factors give

\[
\mathbb E Z=\frac{(n)_6}{10}(c/n)^{10}
             +\frac{(n)_7}{8}(c/n)^{11}
 =\left(\frac{c^{10}}{10}+\frac{c^{11}}8\right)n^{-4}
       +O_c(n^{-5}).                                             \tag{4}
\]

We need to check both multiple counting and coexistence with K4. If F has minimum degree at least 3 and excess 4, every proper subgraph J of F has excess at most 3. Indeed, deleting s>=1 vertices removes at least 3s/2 edges, and hence leaves excess at most 4-s/2, an integer at most 3. Deleting any additional edges only decreases excess. If no vertices are deleted but at least one edge is, the excess is at most 3 as well.

For two distinct copies counted by Z, their intersection is proper in at least one copy. Counting the shared vertices even if isolated in the intersection, inclusion-exclusion for vertices and edges gives

\[
e(F_1\cup F_2)-v(F_1\cup F_2)
 =4+4-(e(F_1\cap F_2)-v(F_1\cap F_2))\ge5.
\]

There are finitely many intersection types, each with bounded vertex count. A type with v vertices and e edges has expected count O_c(n^(v-e)), since it has O(n^v) embeddings and each embedding needs e independent edges. Thus E binom(Z,2)=O_c(n^-5), and the first two Bonferroni bounds yield

\[
\Pr(Z\ge1)=\mathbb E Z+O_c(n^{-5}).                     \tag{5}
\]

The intersection of K4 with H6 or H7 is a proper subgraph of K4, since both are K4-free. Every proper subgraph of K4 has excess at most 1. Therefore the union of a K4 and either obstruction has excess at least 2+4-1=5. The same finite-type counting gives E[XZ]=O_c(n^-5), so

\[
\Pr(Z\ge1,\ X=0)=\mathbb E Z+O_c(n^{-5}).              \tag{6}
\]

Every occurrence of H6 or H7 prevents 3-colouring. Conversely, Section 2 bounds the probability of K4-free failure without either occurrence by O_c(n^-5). Combining (4) and (6) proves (1).

## 4. The K4 contribution

Here

\[
\mathbb E X=\binom n4(c/n)^6
 =\frac{c^6}{24}n^{-2}-\frac{c^6}{4}n^{-3}
    +\frac{11c^6}{24}n^{-4}+O_c(n^{-5}).                \tag{7}
\]

Two distinct copies of K4 share r=0,1,2, or 3 vertices. Their union has 8-r vertices and 12-binom(r,2) edges. For r=1,2 the excess is 5, contributing O_c(n^-5) in total. For r=0 and r=3 the counts of unordered pairs are respectively

\[
\frac12\binom n4\binom{n-4}4,
\qquad \binom n3\binom{n-3}2.
\]

Consequently,

\[
\mathbb E\binom X2
 =\left(\frac{c^{12}}{1152}+\frac{c^9}{12}\right)n^{-4}
       +O_c(n^{-5}).                                      \tag{8}
\]

Every union of three distinct K4 copies has excess at least 5. To see this, the first two have excess at least 4. If the third shares t<=3 vertices with their union, it adds 4-t vertices and at least 6-binom(t,2) edges, increasing excess by at least 2+t-binom(t,2)>=2. If it shares all four vertices, it adds at least one edge. Indeed, the union of two K4 copies has no further K4: any vertex exclusive to one copy has no edge to a vertex exclusive to the other, so a clique lies entirely in one of the two copies. Thus the third again increases excess by at least 1. Finite-type counting now gives E binom(X,3)=O_c(n^-5).

Bonferroni, (7), and (8) give

\[
\Pr(X\ge1)=\frac{c^6}{24}n^{-2}-\frac{c^6}{4}n^{-3}
 +\left(\frac{11c^6}{24}-\frac{c^9}{12}-\frac{c^{12}}{1152}\right)n^{-4}
 +O_c(n^{-5}).
\]

Since the failure event is the disjoint union of {X>=1} and {B,X=0}, equation (1) proves (2).

The algebra and all overlap types used in Sections 3–4 are independently checked with integer arithmetic by `check_coefficients.py`; its output is in `coefficient_checks.json`. The proof does not determine the transition near c=4.69.
