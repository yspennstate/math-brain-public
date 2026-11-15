# Exact first moment with all one-edge shortcuts across three or five path edges

w685, T170 target 2(ii), C003-v2. Status: proof (unaudited). Novelty has not been established. This supersedes the sixteen-state numerical bounds of C003-v1; both proofs and certificates are retained.

## Certified statement

For independent Exp(1) weights on unoriented nearest-neighbour edges of Z^d, the following Euclidean-normalised diagonal lower bounds hold, subject to independent audit of this proof:

    d=5  .163583594538    d=6  .146617260797    d=7  .134037012407
    d=8  .124229229166    d=9  .116304794409    d=10 .109728570946
    d=11 .104156715917    d=12 .099356876711    d=13 .095165638290
    d=14 .091464273436    d=15 .088164156999    d=16 .085197611304
    d=17 .082511941816    d=18 .080065422991    d=19 .077824524846
    d=20 .075761952989    d=21 .073855233803

These are decimal floors of exactly certified rational lower bounds. Every bound exceeds the exact Couronne-Enriquez-Gerin Theorem 2 lower bound c/sqrt(d), c=sqrt(alpha^2-1)/2, coth(alpha)=alpha. The certified relative improvement is at least 10.384811% in d=5 and 2.135212% in d=21. No axis bound or new non-ball dimension is asserted here.

For H_N={x in Z^d:sum_i x_i=N}, its Euclidean distance is N/sqrt(d). The diagonal time constant is mu_diag=sqrt(d) lim_N T(H_N)/N, matching CEG's Euclidean units; integer level N avoids any issue with irrational n sqrt(d). First hitting the closed halfspace sum_i x_i>=N is equivalent to first hitting H_N, because every nearest-neighbour step changes the height by one.

## General chord integration identity

Let P=(x_0,...,x_k) be a fixed vertex-simple path. Select every pair (i,j) with j-i in {3,5} and x_i,x_j nearest neighbours. The corresponding shortcut edge f_{i,j} is not a path edge, since its endpoints occur at nonconsecutive positions. Distinct pairs give distinct shortcut edges: equality of unordered vertex pairs, together with injectivity of the path's vertex indices, forces equality of the unordered index pairs and then of their increasing orders. Thus all shortcut weights are independent Exp(1), independently of the path's edge weights.

For edge index e, let c_e count selected shortcut intervals containing that path edge. Conditional on the path weights t_e, the probability that every subpath costs at most its direct shortcut is exp(-sum_e c_e t_e). Therefore for s>=0,

E[exp(-s tau(P)) 1_{all selected competitions}]=product_e (s+1+c_e)^(-1).       (1)

This argument also works for any fixed finite set of odd shortcut interval lengths >=3. It accounts exactly for all overlapping subpath costs; independence is used only for the distinct off-path edges.

If an arbitrary path to H_N has time at most t, loop erasure first gives a simple path no slower. Replace any failing three- or five-edge competition by its cheaper direct edge. Each replacement preserves the endpoints and vertex simplicity, removes at least two edges, and decreases the time. The shortening procedure terminates at a simple path obeying all selected competitions. Approximate the passage-time infimum by t+epsilon if it is not attained. Thus bounding locally competitive simple paths bounds the unrestricted passage event.

## The exact finite transfer

All simple paths have no immediate reverse and no four-edge return. We count the larger set of direction words satisfying just these two local prohibitions. The words can have longer loops; they are assigned positive formal weights and only enlarge the count of genuinely simple paths for which (1) is valid.

After at least four steps, a state contains (i) the last four signed coordinate directions, with their axes canonically renamed in order of first appearance, and (ii) the four coverage counts C_0,...,C_3 from all already detected three- and five-edge shortcut intervals that cover these edges. Once a new direction is appended, detect a new interval of length l in {3,5} precisely when the last l directions have l1 displacement one. Each detected interval increments the coverage of its l edges by one.

Let h3 and h5 be those two indicators. The final coverage of the oldest remembered edge is C_0+h5. The next remembered four coverage counts are

(C_1+h5, C_2+h5+h3, C_3+h5+h3, h3+h5).

The oldest edge has now seen all possible future selected intervals covering it, and contributes factor 1/(s+1+C_0+h5). The appended direction contributes height tilt z^(its sign). If r distinct axes occur in the remembered history, a step along a represented axis has multiplicity 1, while an unrepresented axis has multiplicity d-r. An unrepresented axis may have appeared earlier in the full path; this is deliberately allowed in the larger locally constrained word count.

There are 138 canonical initial four-step states. Their initial coverage counts are obtained from the two possible three-step windows. For an initial word using r axes and having total height h, its initial tilted multiplicity is the falling factorial (d)_r times z^h. The first four edge factors are delayed. After k-4 transfers for a word of length k, the first k-4 edge factors have been finalised; dropping the last four factors, each at most one, is an upper bound on (1).

Closure under the stated transition rule has 1,778 states and 11,770 transitions for every d>=5. The graph is stored as integer combinatorial data in scripts/chord5_graph.json. Its state set and every transition are independently checked in scripts/certify_chord5.py from the incidence-vector description above, including all initial states. Each row of M_d(s,z) is the sum of transition weights

(axis multiplicity) z^(new sign)/(s+1+final coverage).

For a strictly positive vector v with Mv<v, rho=max_i(Mv)_i/v_i<1. With A the initial tilted row vector, nonnegativity gives

sum_{k>=4} A M^(k-4) 1 <= (A v)/(min(v)(1-rho)) < infinity.

Lengths below four add a finite constant. Markov inequality applied to (1), the height tilt z^(sum_i x_i), and the sum over all qualifying simple paths consequently yield

P(T(H_N)<=t) <= C exp(s t) z^(-N),

where C is finite and depends only on d,s,z,v. Borel-Cantelli at t=bN, b<log(z)/s, proves

mu_diag >= sqrt(d) log(z)/s.                                          (2)

## Exact certificates, not floating-point bounds

scripts/chord5_certificate_parameters.json contains fixed integer numerators and denominators for s,z and each strictly positive 1,778-entry vector. scripts/certify_chord5.py rebuilds all rational transition weights and checks all 30,226 componentwise inequalities for d=5,...,21. It also verifies graph closure and each initial state, and re-encloses the primary CEG constant with exact sinh/cosh Taylor tails. logs/chord5_exact_certificates.json records the exact lower rationals, strict rho upper rationals, and source-data hashes.

The log lower bound uses the positive rational series log(z)=2 sum_{j>=0} u^(2j+1)/(2j+1), u=(z-1)/(z+1). Terms through j=80 give a lower bound; the remainder is bounded above by a geometric tail and also recorded when needed. Integer square roots give outward rational bounds on sqrt(d). No floating arithmetic enters these proofs or comparisons. Exploratory sparse floating-point optimisation selects the certificate data only.

scripts/validate_chord5.py separately enumerates actual direction words in d=3 through length seven, checks their incidence counts and exact tilted sum against the compressed transfer, and checks all three/five shortcut-edge witnesses in its simple-path sample. This finite check verifies the implementation; the general proof above supplies the inclusion and independence arguments.

Reproduce with:

    python -I -X utf8 scripts/certify_chord5.py
    python -I -X utf8 scripts/validate_chord5.py

The original sixteen-state proof and weaker block proof are in proofs/hairpin_lower_bound.md and proofs/block2_lower_bound.md. The primary normalisation and comparator source is CEG arXiv:1008.5069v2, Section 3, Theorem 2, pp. 5-6. Alm-Parviainen (2002) already used transition-matrix lower bounds on the square lattice; its abstract was read, but a bounded search did not obtain its full theorem. Thus neither novelty nor an absence of prior art is claimed. Only the independent reviewer can upgrade C003-v2 to independently checked proof.
