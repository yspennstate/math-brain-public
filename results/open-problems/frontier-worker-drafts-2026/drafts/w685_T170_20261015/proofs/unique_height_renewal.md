# Unique-height renewal first moment for Exp(1) FPP (C013-v4)

Status: proof (unaudited). The scalar, finite matrix, and interval checks have separate scopes, C014-v2, C015-v1, and C016-v1. No independent proof review or novelty finding is claimed. The load-bearing step is the all-length decomposition below; finite-word Monte Carlo is not used in the proof.

Let h(x)=sum x_i. On Z^21, edges have independent Exp(1) times. At the exact positive rational s,z in logs/height_bridge_tail_certificate.json, put a=s+1. This manuscript proves that the tilted sum of locally competitive simple-path Laplace weights is finite. Therefore the Euclidean diagonal time constant satisfies mu_diag >= sqrt(21) log(z)/s. The downward decimal floor is computed in logs/height_renewal_mu_floor.json with exact rational logarithm and square-root lower bounds. The parameter point was selected from an older, now superseded axis comparison; this is a lower-bound result, not a new dimension claim.

## 1. A disjoint set of competing shortcuts

Fix a vertex-simple lattice path x_0,...,x_n. Include every one-edge chord x_i~x_(i+3). These are distinct edges off the path. Let c_j count those chords covering step j. For each even-start two-edge block b,b+1, keep its other square path only if its axes differ, neither even endpoint touches a three-step chord, and neither adjacent four-step pair involving the block has endpoint displacement of l1 norm at most two. Call this the even rule.

These even alternatives are disjoint from all actual and three-step-chord edges. If one of their edges were an actual edge, the other edge would be a three-step chord touching the opposite endpoint. Any alternative edge that is itself a three-step chord touches an even block endpoint. Both cases violate the rule. Two even alternatives sharing an edge must share its even actual endpoint. Simplicity then makes the blocks adjacent. Their equal alternative midpoints imply that the outer endpoints of the four-step pair are at distance at most two, again excluded.

Also keep an odd-start square when its actual middle vertex is at a height visited exactly once by the entire path, its two signs are positive, and its axes differ. We will use only heights strictly above four and strictly below the final height. Its alternative middle vertex has the same height as the actual middle vertex and differs from it. Hence it is not on the path. Both alternative edges have an endpoint outside the path, so are off every actual or three-step-chord edge. Two such alternatives cannot share an edge: each edge joins a path endpoint to an alternative midpoint, so sharing would require equal alternative midpoints, hence equal uniquely visited heights and the same original middle vertex. An odd-start alternative cannot overlap an even alternative because its even midpoint is outside the path, whereas every even alternative edge has an even endpoint on the path.

Thus all selected off-path edge sets are mutually disjoint. Conditional on the actual step times t_j, chord competitions contribute exp(-sum c_j t_j). Each square contributes the Gamma(2,1) survival exp(-(t_i+t_(i+1)))(1+t_i+t_(i+1)). Actual times remain coupled through overlapping squares; we integrate their joint polynomial, never multiply their marginal probabilities. A geodesic satisfies every competition, even when a replacement walk would meet an earlier vertex.

## 2. The finite operator preserves the couplings

The graph scripts/height_renewal_graph.json stores the last three directions up to axis relabeling, the three/four unfinished chord incidences, the one/two pending even flags, the next even-block dirty flag, the pending odd-square flags, and an incoming odd-square flag I and moment p. Here p=0,1, and p=0 if I=0. Seed states come from four-step words without two/four-step returns, with the initial odd-square flag false. Ignoring heights at most four guarantees this seed choice for the paths being counted.

When step 2k+5 is appended, all three-step chords touching either even endpoint of block 2k,2k+1 have been seen. Both neighboring four-step tests have also been seen. Its eligibility is therefore final. The pair can be integrated then. The unfinished counts are incremented precisely on the last three edges when the new three-step displacement has norm one. A chord dirties the even blocks incident to its even endpoint; a near four-step pair dirties its two blocks. These rules give the queue updates in the graph builder by induction. There are 641 states; rows have separate marked and unmarked inputs. A mark at a cut vertex activates an odd square across that cut only when its index is even and the two positive directions have different axes.

For a finalised pair, let E be its even-square flag and O its outgoing odd-square flag. With x=a+c0+I+E and y=a+c1+E+O, expand t0^p(1+t0+t1)^E(1+t1+t2)^O and integrate t0,t1 by factorial moments. Denote the coefficient of t2^q by B_pq. This is an exact positive two-by-two transfer. Similarity by D_even,p=a^(-1-p), D_odd,p=a^(-p) gives the balanced entry a^(1+p-q) B_pq. Nonfinalising entries are 1/a. A direction absent from the last-three history has multiplicity d-r; each old direction has multiplicity one. Multiplying by z^sign yields M_(mark,sign).

No actual time is reset at a height cut. The pending counts and moments pass through the boundary state. This permits matrix composition across cuts even when a square uses one step on each side.

At termination, drop all unfinalised chord contributions and squares except the incoming odd square already expanded into moment p. All dropped factors are at most one. With m=4 unfinished edges at even parity, or m=3 at odd parity, the raw terminal integral is (a+I)^(-p-1) a^(-m+1). After the similarity it is a^(-3) w, where w(I,p)=(a/(a+I))^(p+1). The initial seed similarity contributes another 1/a. Hence a fixed four-step seed contributes its finite direction/tilt multiplicity times a^(-4), followed by the balanced matrix product and terminal w. Words shorter than four contribute a finite separate sum. Allowing nonsimple words with these formal positive weights only enlarges the sum over actual simple paths.

Full-coordinate validation independently reconstructs all flags, incidences, moment branches and transitions from each entire coordinate prefix. It also checks disjoint alternative edge sets on simple words and compares the truncated block integral with a separate per-edge integration. The saved run checks 11,053 words, 87,234 transition branches, 10,525 simple-path geometries and 80 exact word integrals. These finite checks support, but do not replace, the induction above.

## 3. A common norm and an exactly bounded bridge tail

C015-v1 verifies, in exact rational arithmetic for every state, sign and mark,

M_(mark,sign) w <= (d z^sign/a) w.

There are 2,564 inequalities. Consequently any family of encoded sign profiles of length n, displacement ell, has common-norm bound (d/a)^n z^ell per profile. This statement includes arbitrary pending moments.

A strict positive height bridge starts at zero, ends at ell>=1, and has 0<h<ell at intermediate times. It is irreducible if every interior height is visited at least twice. For length n, the number of negative steps m satisfies 4m>=n-1. With t=7/5,

r=d(z+t^4/z)/(a t)<9/10,

so its total scalar length-n weight is at most t r^n. C014-v2 computes the total irreducible scalar mass through length 400 with integer reflection counts and the formal renewal identity, then bounds the entire omitted tail. See proofs/scalar_bridge_mass.md; no analytic continuation is used.

Let B be the height-bridge operator on boundary states whose last direction has positive sign. Its profile entry is M_(1,+) followed by unmarked matrices for the rest of the strict irreducible bridge, with the destination restricted to boundary states. The nonnegative series converges by the scalar bound. Let B_21 contain profiles through length 21; their count is 8,912. The exact length/height polynomial of this enumeration is independently checked against the formal scalar renewal recurrence.

For any positive boundary vector v, extend it by zero outside the boundary and put C=max(v_i/w_i). The omitted profiles satisfy

(B-B_21)v <= R C w,

where R is the total scalar mass above length 21. The exact upper endpoint from C014-v2 minus the exact enumerated short mass bounds R. The certificate computes an upper enclosure of B_21 v with every binary64 coefficient rounded upward by an exact rational comparison, and every vector multiplication and addition rounded upward using nextafter. Zero stays zero; nonzero operands and products are checked to stay in the normal finite range. No opaque sparse dot product or floating error estimate is used. Final comparisons and the scalar remainder are exact rational arithmetic.

All 330 boundary rows satisfy Bv <= kappa v with the recorded rational kappa<1 in logs/height_renewal_interval_certificate.json. Therefore sum_{j>=0} B^j converges on every positive boundary vector. C016-v1 records precisely this encoded-operator statement.

## 4. Initial and terminal pieces are summable

For any full word ending at height H, cut at the heights k with 4<k<H that are visited exactly once. These cuts occur in increasing order; before such a cut the word is below its height and afterwards above it. Thus between consecutive cuts the sign profile is a strict irreducible bridge. The incoming direction at a cut is positive, as required by the boundary space. The first step after each cut carries the mark, including the first step of the final suffix.

Fix the first four directions and their height h0, with -4<=h0<=4. A remaining prefix of n steps ending at the first cut k>4 has at least two visits to every height 5,...,k-1. Consequently n-1>=2(k-5). If m is its negative-step count relative to h0, this gives 4m>=n-17. The same inequality applies to a full remaining word with no cuts when H>4. When H<=4, its displacement from h0 is at most eight, giving 4m>=2n-16>=n-17 directly.

For any word satisfying 4m>=n-C, multiplying its scalar weight by t^(4m-n+C)>=1 and summing all sign choices bounds its length-n mass by t^C r^n. The no-cut words and initial prefixes are therefore summable with C=17. A suffix after the last cut has at least two visits to each height strictly between that cut and H, so 4m>=n-1 and C=1 suffices. The common norm holds for both marks, so these same bounds apply to the corresponding matrix products, including the suffix's marked first step.

The total tilted word sum is consequently a finite no-cut term plus a sum of prefix, B^j, suffix products. Prefixes have finite common-norm sum. Suffixes map terminal w to a finite multiple of w. On the finite boundary space w and the strictly positive v bound one another by finite constants. Finally B^j v<=kappa^j v with kappa<1. Summing the geometric series proves finiteness of the complete tilted Laplace sum. This accounts for every prefix, suffix, length and truncation.

## 5. From the word sum to the diagonal bound

Let H_N={x:h(x)=N}. A fastest path to H_N is simple and obeys all the chosen comparisons. Existence follows, for example, from the usual finite first-moment count of simple paths with passage time below any fixed time; choose a Laplace parameter above 2d-1 to make that count summable. For c<log(z)/s, Markov's inequality and the finite tilted sum K give

P(T(0,H_N)<=cN) <= K exp((sc-log(z))N).

The right side is summable in N. Borel-Cantelli yields liminf T(0,H_N)/N >= log(z)/s. The diagonal point k(1,...,1) lies on H_(dk) and has Euclidean norm k sqrt(d), so mu_diag>=sqrt(d) log(z)/s. This matches CEG's Euclidean diagonal normalisation.

Run python -X utf8 scripts/run_height_renewal_certificate.py to rebuild the graph, scalar mass, norm, coordinate checks and outward operator certificate from scratch. The saved positive vector is an arbitrary witness; its numerical derivation is not assumed. The exact rational point and its historical reference are pinned by hashes. Independent review is still required for this entire argument, its implementation, and any claim of novelty.
