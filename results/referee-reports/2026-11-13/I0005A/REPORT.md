PARTIAL

# I0005: critical parking in dimension four

This report does not decide the nearest-free-spot question for integer cars on
\(\mathbb Z^4\), for either the original Bernoulli parking law or the sparse
three-state law of the source's counterexample. A complete result below proves
the affirmative statement for the divisible-sandpile comparison when “active”
means any strictly positive residual mass. That convention is essential and
does not transfer to cars. The literature search found no printed resolution.

The status is PARTIAL solely because of this proved variant and the quantitative
consequences below. There is no proof or counterexample here for the requested
integer-car process in dimension four.

## Model and question

Write \(|x|_1=\sum_i|x_i|\). On the nearest-neighbor graph \(\mathbb Z^d\), the
original parking law assigns independently one car with probability \(p\), or
one parking spot with probability \(1-p\), at each site. Initially a car site
has no spot. In each **synchronous discrete round**, every car still driving
takes one independent simple-random-walk step, uniformly among the \(2d\)
neighbors. Arrivals fill free spots immediately; if several cars arrive at the
same free spot in the same round, one is chosen uniformly to park. Parked cars
never move again. Cars can drive through occupied spots and through sites that
were initially car sites. This is not a continuous-time model.

In the source's generalization, \(\eta(x)\) are iid integers. After cancelling
particles and holes initially at the same site, site \(x\) has \(\eta(x)^+\)
active particles or \(\eta(x)^-\) holes. A site with \(\eta=0\) has neither.
If \(j\) particles arrive at \(h\) holes in one round, uniformly choose
\(\min(j,h)\) to settle. Initial data and walks are independent. Criticality is
\(\mathbb E\eta=0\) with nonconstant law. Original critical parking is
\(\mathbb P(\eta=1)=\mathbb P(\eta=-1)=1/2\).

Let \(A_t(x)\) count active particles after \(t\) rounds and \(H_t(x)\) count
unfilled holes. Let \(U_t(x)\) count departures from \(x\) in the first \(t\)
rounds, so \(U_{t+1}-U_t=A_t\). Define

\[
D_A(t)=\inf\{|x|_1:A_t(x)>0\},\qquad
D_H(t)=\inf\{|x|_1:H_t(x)>0\}.
\]

The question is whether \(\mathbb P(D_H(t)<D_A(t))\to0\). The origin itself
is included in both infima; a tie does not count. Distances are graph distances,
namely \(\ell^1\), as specified in the parking paper §1.9, printed p. 10. They
are not distances along a car's trajectory, Euclidean distances, or hitting
times. These sets exist almost surely at every finite time for the laws at
issue. The convention \(\inf\varnothing=\infty\) handles variants or finite
checks.

Model references: parking paper pp. 1–3 and §2, pp. 10–12; DGJLS pp. 2089–2090.
The newer source's Theorem 1.5 is on p. 5, and its counterexample is the separate
Theorem 1.6 on p. 6. The latter uses \(\eta\in\{-1,0,1\}\) with probabilities
\((p_d,1-2p_d,p_d)\), for a small \(p_d\), not Bernoulli parking with
\(p=1/2\). Thus even the higher-dimensional counterexample does not settle
the original two-state parking question.

## Proved variant

Let \(d\ge1\). Take iid \(\eta(x)\in\{-1,0,1\}\), with
\(\mathbb P(\eta=1)=\mathbb P(\eta=-1)=p\in(0,1/2]\).
Let \(P\) average over the \(2d\) nearest neighbors and define the total-emission
divisible odometer by

\[
u_0=0,\qquad u_{t+1}=(\eta+Pu_t)^+.
\]

The signed mass after \(t\) rounds is
\(s_t=\eta+(P-I)u_t\). Define active mass \(a_t=s_t^+\), unfilled capacity
\(b_t=s_t^-\), and graph distances to their strictly positive supports,
with the distance to an empty set taken as infinity.

**Claim.** Almost surely, for every fixed site \(x\), there is a finite random
\(T_x\) such that \(a_t(x)>0\) and \(b_t(x)=0\) for every integer \(t\ge T_x\).
Consequently the probability that the origin is strictly closer to unfilled
capacity than to active mass tends to zero. In particular this holds for \(d=4\).

**Proof.** The recursion is monotone in time. Put
\(q_t=u_{t+1}-u_t\ge0\). If \(u_t(x)=0\), then
\(q_t(x)=(\eta(x)+Pu_t(x))^+=s_t(x)^+\). If \(u_t(x)>0\), monotonicity gives
\(\eta(x)+Pu_t(x)=u_{t+1}(x)\ge u_t(x)>0\), and again
\(q_t(x)=s_t(x)^+\), while \(b_t(x)=0\).
Once \(u_t(x)>0\), subtracting the two unreflected recursions gives

\[
q_t(x)=Pq_{t-1}(x).
\tag{V1}
\]

There is almost surely an edge \(\{y,z\}\) with \(\eta(y)=\eta(z)=1\):
choose infinitely many disjoint edges, whose two-positive events are independent
with probability \(p^2>0\). For this pair, \(u_1(y)=u_1(z)=1\) and
\(q_0(y)=q_0(z)=1\). Both sites have emitted by round one. Induction in (V1)
therefore gives
\(q_t(y)\ge q_{t-1}(z)/(2d)>0\) and
\(q_t(z)\ge q_{t-1}(y)/(2d)>0\) for every \(t\ge1\).

Critical explosion of the iid divisible sandpile implies
\(u_t(v)\uparrow\infty\) for every site \(v\), almost surely. This is the
critical explosion result of Levine–Murugan–Peres–Ugurcan (2016), recalled on
printed p. 2 of the companion; it also follows from that companion's critical
growth results. Its hypotheses hold for \(\sigma=1+\eta\), which is nonnegative,
has mean one and positive finite variance. The companion's odometer is
\(u/(2d)\), so explosion has the same meaning.

Fix a finite nearest-neighbor path \(y=v_0,v_1,\ldots,v_\ell=x\). There is a
finite random \(T\ge1\) by which all its sites have emitted. For \(t\ge T+\ell\),
iterate (V1) along this path to obtain

\[
q_t(x)\ge (2d)^{-\ell}q_{t-\ell}(y)>0.
\]

Also \(u_t(x)>0\), so \(b_t(x)=0\). Thus the distance to active mass at \(x\)
is zero eventually, whereas the distance to unfilled capacity is positive or
infinite. The strict nearer-capacity event is eventually false almost surely;
bounded convergence proves the probability assertion. A countable intersection
gives the stated property simultaneously for all sites. \(\square\)

This proof includes the bipartite-lattice issue: an adjacent positive pair feeds
both time parities. It does not assume that a positive increment stays positive
at the same site without this pair.

For dimension four, the explosion input can be obtained directly from Theorem
5.1 of the companion (p. 36): at every fixed site \(u_t/\mathbb Eu_t\to1\)
almost surely and \(\mathbb Eu_t\ge c\log t\). Countably many sites give the
simultaneous statement used along the path. The all-dimensional formulation
above uses the established critical explosion theorem recalled in its
introduction.

There is also a quantitative bound for the nearest unfilled capacity in this
variant. In the total-emission normalization, Theorem 5.1 implies, for constants
\(c_0,c_1,C>0\) depending on the fixed law,

\[
\mathbb Eu_t(0)\ge c_0\log t,\qquad
\mathbb P\bigl(|u_t(x)-\mathbb Eu_t(0)|>s\bigr)
 \le C\exp\{-c_1\min(s^2/\log t,s)\}.
\]

Put \(s=\mathbb Eu_t(0)/2\). For some \(\kappa>0\), uniformly in \(x\),
\(\mathbb P(u_t(x)=0)\le Ct^{-\kappa}\). A union bound over the graph ball
of radius \(t^\alpha\) gives

\[
\mathbb P\bigl(\exists |x|_1\le t^\alpha:u_t(x)=0\bigr)
 \le Ct^{4\alpha-\kappa}\longrightarrow0
 \quad(0<\alpha<\kappa/4).
\]

An unfilled capacity requires \(u_t(x)=0\). Hence its nearest distance exceeds
\(t^\alpha\) with probability tending to one, whereas the nearest strictly
positive active mass is at distance zero eventually almost surely. No explicit
value of \(\alpha\) follows from the unspecified concentration constants.

For integer cars an active particle leaves its current site in a single random
direction. It does not leave a positive fraction at every neighbor. The two-site
positivity induction therefore fails. Neither conditional Jensen comparison
\(u_t\le\mathbb E[U_t\mid\eta]\) nor a comparison of expected odometers transfers
strict positivity or distances between supports. No result for a fixed positive
activity threshold is claimed here.

The distinction can be quantified. Monotonicity of the expected increments
(companion Lemma 2.4, p. 16) and \(\mathbb Eu_t\le C\log t\) give
\(\mathbb Ea_t(0)\le C\log(t+2)/(t+1)\). For every fixed \(\varepsilon>0\),

\[
\mathbb P(a_t(0)\ge\varepsilon)
 \le C\log(t+2)/(\varepsilon(t+1))\to0.
\]

Thus eventual positive activity at the origin consists of vanishingly small
amounts. Treating this support theorem as a theorem for cars would be incorrect.

## What the dimension-four scales actually establish

Use \(u\) for the parking paper's **total** emitted mass. The companion instead
uses \(\widetilde u\), mass sent to **each** neighbor, and scenery
\(\zeta=(\sigma-1)/(2d)\). Its recursion is
\(\widetilde u_{t+1}=(\zeta+P\widetilde u_t)^+\) (p. 2, equation (1)).
For comparison with parking set \(\sigma=1+\eta\), so
\(\zeta=\eta/(2d)\) and \(u=2d\widetilde u\). In particular, in \(d=4\),

\[
\mathbb Eu_t(0)\asymp\log t,\qquad
\frac{u_t(0)-\mathbb Eu_t(0)}{\sqrt{\log t}}
 \Rightarrow N\left(0,\frac{4\operatorname{Var}\eta(0)}{\pi^2}\right),
\quad
\frac{\operatorname{Var}u_t(0)}{\log t}
 \to\frac{4\operatorname{Var}\eta(0)}{\pi^2}.
\tag{S1}
\]

These are Theorem 1.3(ii), pp. 5–6; Theorem 5.1, p. 36, proved on pp. 36–38;
and Proposition 5.5, p. 41. **There is no claimed limit for
\(\mathbb Eu_t/\log t\) or explicit leading coefficient for that mean.**
For Bernoulli parking the variance coefficient in (S1) is \(4/\pi^2\);
for the sparse law with each sign of probability \(p\), it is \(8p/\pi^2\).

Independently checking the coefficient: if
\(g_t(x)=\sum_{j<t}P_0(X_j=x)\), then
\(\sum_xg_t(x)^2=\sum_{a,b<t}P_0(X_{a+b}=0)\).
The period-two local central limit expansion gives
\(P_0(X_s=0)=8/(\pi^2s^2)+O(s^{-3})\) for even \(s\), and zero for odd \(s\).
For \(s<t\) there are \(s+1\) pairs, so summing even \(s\) gives
\((4/\pi^2)\log t+O(1)\). The pairs with \(t\le s<2t\) contribute \(O(1)\).
Multiplying by \(\operatorname{Var}\eta\) agrees with (S1).

For the integer-car process, Theorem 1.2 (p. 4) says

\[
c(\mathbb Eu_t+\log t)\le\mathbb EU_t\le
C(\mathbb Eu_t+\log t).
\]

The error and divisible mean have the same order in dimension four. Theorem
1.4(ii), p. 5, only bounds their expected ratio for each fixed law. Theorem 7.2,
pp. 21–22, proves that for the sparse law with total nonzero probability
\(\epsilon=2p\),
\(\liminf\mathbb EU_t/\mathbb Eu_t\ge c\log(e/\epsilon)\).
This rules out assuming equality of the leading odometers uniformly over laws.
It does not rule out a better comparison for the fixed Bernoulli law.

For both laws considered here, put \(h_t=\mathbb P(H_t(0)=1)\). Conservation
and mass transport (Lemmas 2.5–2.6, pp. 12–13) give

\[
\mathbb EA_t(0)=\mathbb EH_t(0)=h_t,
\qquad \mathbb EU_t(0)=\sum_{s<t}h_s.
\]

Corollary 1.3, p. 4, proves only
\(c/(t+1)\le h_t\le C\log(t+2)/(t+1)\) in dimension four. It does not
give a sharp one-time density. In particular, summing the density to obtain a
logarithmic odometer does not establish \(h_t\sim c/t\).

An independent-point approximation would predict both nearest distances of
order \(h_t^{-1/4}\), between the reference scales
\((t/\log t)^{1/4}\) and \(t^{1/4}\). This is a heuristic, not a theorem.
Active-site intensity can also be smaller than active-particle intensity because
several cars can share a site. The unconditional rigorous consequence is just

\[
\mathbb P(D_H(t)\le r),\ \mathbb P(D_A(t)\le r)
 \le |B_r|h_t\le C(r+1)^4\frac{\log(t+2)}{t+1}.
\tag{S2}
\]

For example both distances exceed
\(t^{1/4}/(\log t)^{1/4+\delta}\) with probability tending to one, for every
\(\delta>0\). This common lower bound compares neither distance with the
other. No matching upper bounds or ratio limit follow from these inputs.

The logarithmic correlation is the other obstruction. The infinite-volume
convolution \(G*G\) diverges in dimension four. With walks truncated at time
\(t\), its size for \(1\ll r\ll\sqrt t\) is of logarithmic order,
\(1+\log(t/r^2)\), up to the parity restriction and constants. Thus simply
substituting \(d=4\) into a bound proportional to \(r^{4-d}\) is invalid.
At the nominal spacing \(r\approx t^{1/4}\), this correlation is still
of order \(\log t\). The high-dimensional pair-hole estimate cannot be
transferred by adjusting a bounded constant.

There is indeed a \(\log\log t\) correction in the companion, but its meaning
is specific: Proposition 5.4 (pp. 39–41) bounds
\(u_t-\mathbb Eu_t-V_t\), where \(V_t=g_t*\eta\), with a tail
\(C\exp[-c\min(\lambda^2/(1+\log\log t),\lambda)]\), after adjusting
normalization constants. Its mean square is \(O(1+\log\log t)\).
This is an error estimate for the centered divisible odometer, not an estimate
of distances to extreme contact sites or of integer-car activity. A Gaussian
central limit theorem on the \(\sqrt{\log t}\) scale also cannot estimate the
event that an odometer with mean of order \(\log t\) is zero. That requires a
far-tail estimate and its spatial dependence.

Accordingly there is no justified calculation here of a power of \(\log\log t\)
that makes cars or holes win. The source's sparse-law simulations suggest a
counterexample (p. 6); that is a conjectural direction, rather than a derivation
of such a correction. The companion even leaves identification of its centered
diffusive spatial limit open (Problem 1.5, p. 11). Its identified membrane limit
is at superdiffusive times \(t=R^\alpha\), \(\alpha>2\), modulo constants and
in a negative Sobolev topology (Proposition 5.7, pp. 42–43). Such convergence
does not control zeros or nearest supports.

## Computation and verification

All downloaded paper PDFs were converted through memory-only byte streams;
only plain text and provenance are retained. `code/get_text.py` records URLs,
retrieval times, SHA256 hashes and page counts. The two arXiv papers were freshly
retrieved and have 43 and 82 pages; DGJLS has 25. Form feeds preserve page
boundaries. PDF font control characters were removed from the saved text.

Run `python3 code/checks.py` with `OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1
MKL_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1`. It checks:

- The divisible identities and persistent adjacent pair using exact rational
  arithmetic on a 9-cycle for 80 rounds. There were 158 identity checks at
  emitted sites; the final seed increment was exactly \(2^{-79}>0\).
- The \(4/\pi^2\) coefficient by a separate closed-walk enumeration, evaluated
  with logarithmic binomial coefficients. Dyadic slopes of \(\|g_t\|_2^2\)
  were 0.412399 at \(t=64\), 0.405714 at \(t=1024\), and 0.405392 at
  \(t=4096\), approaching \(4/\pi^2=0.405285\). See `data/green_d4.csv`.
- Synchronous parking on periodic tori, with original Bernoulli law and sparse
  law \(p=0.05\) for each sign, in dimension four at sides 24 and 32, and
  dimension two at side 128. Two seeds per configuration; observations at
  rounds 4, 16, 64 and 256. Each step checks conservation of cars minus holes.
  Nearest distances are exact periodic graph distances; their routine was
  independently checked against brute-force distances on a small torus.

For orientation only, these are averages of the two spatial fractions in
dimension four. All raw counts, ties, distances and odometers are in
`data/parking_tori.csv`.

| Law | Side | round 16 | round 64 | round 256 |
|---|---:|---:|---:|---:|
| Bernoulli, each sign 0.5 | 24 | 0.3187 | 0.3258 | 0.3317 |
| Bernoulli, each sign 0.5 | 32 | 0.3175 | 0.3196 | 0.3117 |
| Sparse, each sign 0.05 | 24 | 0.3386 | 0.3487 | 0.3600 |
| Sparse, each sign 0.05 | 32 | 0.3400 | 0.3523 | 0.3678 |

These are \(\{D_H<D_A\}\) fractions, not independent samples or estimates
with independent-site error bars. Periodicity, random global imbalance,
ties and finite time matter. Even the two-dimensional check has not reached
a visibly decaying regime. No exponent or limiting probability was fitted.
These computations neither resolve the four-dimensional question nor verify
an infinite-volume theorem.

Measured process priority was nice 10, numerical libraries were limited to one
thread, and peak RSS on macOS was 215,302,144 bytes (about 205 MiB), below 4 GB.
An initial `nice -n 10` invocation warned that changing priority was prohibited;
inspection showed the process already inherited nice 10. A platform matrix-dot
operation emitted floating-point flag warnings despite finite correct output;
it was replaced by elementwise summation and the Green check was rerun cleanly.
The independent asymptotic derivation above checks the magnitude and the
period-two constant. No simulation is used in either proof.
The source-hash, page-anchor and artifact checks are recorded in
`data/final_audit.json`.

## Literature and detailed proof audit

All page numbers below are the printed page numbers of the specified version.
The arXiv physical and printed page numbers coincide. For the published DGJLS
article, add 2088 to the physical page number. These references can be located
using the form-feed-separated pages of the saved source texts.

Verified records:

- Ahmed Bou-Rabee and Christoforos Panagiotis, [*Sharpness and critical scaling
  of parking*](https://arxiv.org/abs/2609.02820v1), arXiv:2609.02820v1,
  submitted Wednesday 2 September 2026 at 17:08:08 UTC; 43 pages, two figures.
  Local text: `sources/2609.02820v1.txt`.
- The same authors, [*Quantitative explosion and percolation of the divisible
  sandpile*](https://arxiv.org/abs/2609.02829v1), arXiv:2609.02829v1,
  submitted Wednesday 2 September 2026 at 17:14:34 UTC; 82 pages, three figures.
  Local text: `sources/2609.02829v1.txt`.
- Michael Damron, Janko Gravner, Matthew Junge, Hanbaek Lyu and David Sivakoff,
  [*Parking on transitive unimodular graphs*](https://doi.org/10.1214/18-AAP1443),
  *Annals of Applied Probability* **29** (2019), no. 4, pp. 2089–2113.
  [Published author-hosted article](https://www.math.ucdavis.edu/~gravner/hidden/clanki/AAP_2019.pdf);
  local text: `sources/DGJLS2019.txt`. Its arXiv identifier is 1710.10529;
  this audit uses the published article for page numbers.

The current, unversioned arXiv listings were also checked on 13 November 2026
and showed only v1. Search queries and results are recorded in
`sources/SEARCH_NOTES.txt`. The author's publication list and the September
2026 Bath lecture abstract provided no further resolution. No printed
dimension-four solution was found. This is the outcome of this search,
not an exhaustive nonexistence claim.

### DGJLS Open Question 3 and its context

Open Question 3 is on **p. 2100**, in §3, “Examples and further questions”
(the open questions begin on p. 2099).
It asks, at \(p=1/2\), whether
\(\lim_{t\to\infty}\mathbb P(0\text{ is closer to a spot than to a car})=0\),
and asks for the decay rate if it does. The spots and cars are the remaining
free spots and driving cars in the process, rather than all initial labels.

The question is motivated by Figure 2 on p. 2092: critical two-dimensional
unoriented parking on a periodic \(300\times300\) square, at times 10, 50 and
300. Empty sites are colored according to which remaining type is nearer;
ties are gray. The surrounding discussion on p. 2092 emphasizes dependence
between survival and the prior filling of spots along a trajectory, and the
resulting clusters. Theorem 2.1 on p. 2096 establishes infinite visits at
criticality; Theorem 2.2 on pp. 2096–2097 says that all cars eventually park
and all spots eventually fill. Thus eventual individual removal is compatible
with infinitely many visits. Neither theorem answers this spatial-distance
question. The preceding Open Questions 1–2, pp. 2099–2100, concern critical
visit growth and divergence of subcritical expected visits, respectively.

### Theorem 1.5, exactly: dimensions at most three

For \(d\in\{1,2,3\}\), iid nonconstant integer \(\eta(x)\) with
\(\mathbb E\eta(0)=0\) and \(\mathbb Ee^{\theta|\eta(0)|}<\infty\) for some
\(\theta>0\), Theorem 1.5 (p. 5) proves

\[
\mathbb P(D_H(t)<D_A(t))\longrightarrow0.
\]

Its stronger statement is that, for every fixed \(K\ge1\),
\(\mathbb P(D_H(t)\ge K D_A(t))\to1\). The proof actually constructs
strict separation by more than \(K\) on a high-probability event.
The proof occupies pp. 23–24 and relies on Proposition 8.1, pp. 22–23.
Here is each part of that argument, including where the dimension enters.

1. **Joint scaling, p. 22 and p. 23, Step 1.** For spatial scale \(R\), multiply
   odometers at time \(\lfloor sR^2\rfloor\) by \(R^{d/2-2}\) and sample at
   \(\lfloor Rx\rfloor\). The scenery tested against a smooth function is
   \(\langle\eta_R,\phi\rangle=R^{-d/2}\sum_y\eta(y)\phi(y/R)\).
   The companion's low-dimensional limit, transferred by Proposition 7.1,
   gives jointly
   \((\eta_R,u^R,U^R)\Rightarrow(W,\mathcal U,\mathcal U)\),
   with locally uniform convergence of both odometers on positive times.
   Here \(W\) is spatial white noise with variance \(\operatorname{Var}\eta\),
   and \(\mathcal U\) is the continuous Brownian optimal-stopping value.
   Positivity on a compact set removes the positive part in the divisible
   recursion. Passing to distributions gives
   \(\partial_s\mathcal U=L\mathcal U+W\) on
   \(\mathcal O=\{\mathcal U>0\}\), with \(L=\Delta/(2d)\).

2. **Particle-minus-hole field, p. 23, Step 2.** At \(t=\lfloor R^2\rfloor\),
   set \(\langle\nu_R,\phi\rangle=R^{-d/2}\sum_y(A_t-H_t)(y)\phi(y/R)\).
   Conservation, equation (45), writes this as scenery plus
   \(R^{-d/2}\sum_yU_t(y)(P-I)\phi(y/R)\), plus an instruction martingale.
   Each scaled instruction difference is bounded by \(C_\phi/R\), and
   \(\mathbb EM_R(\phi)^2\le CR^{-d-2}\sum_{y\text{ near }R\operatorname{supp}\phi}
   \mathbb EU_t(y)\le CR^{-d/2}\to0\). Taylor expansion then gives
   \(\nu_R\Rightarrow W+L\mathcal U(1,\cdot)\).

3. **Positive time derivative, p. 23, Steps 3–4.** Time monotonicity makes
   \(v=\partial_s\mathcal U\) nonnegative. Time differences cancel the static
   white noise in the PDE, so \((\partial_s-L)v=0\) inside \(\mathcal O\).
   Interior regularity makes \(v\) smooth. If \(v(s_0,x_0)=0\) while
   \(\mathcal U(s_0,x_0)>0\), let \(\tau\) be the first positive time at that
   spatial point. The strong minimum principle forces \(v=0\) on the vertical
   segment from just after \(\tau\) to \(s_0\). Integrating and using continuity
   at \(\tau\) contradicts \(\mathcal U(s_0,x_0)>0\). Thus \(v>0\) there.

4. **Nearest distances, pp. 23–24.** Put \(R=\sqrt t\), and fix \(K,\epsilon\).
   The critical lower-tail estimate gives \(\mathcal U(1,0)>0\) almost surely.
   Choose deterministic \(r,a>0\) and a nonzero nonnegative smooth bump \(\phi\)
   supported in \(B_r\), so that with probability at least \(1-\epsilon\),
   \(\inf_{B_{(K+2)r}}\mathcal U(1,\cdot)>2a\) and
   \(\int\phi v(1,\cdot)>2a\). Convergence implies \(U_t>0\) on the lattice
   ball \(B_{(K+1)rR}\) and \(\langle\nu_R,\phi\rangle>a\), with limiting
   probability at least \(1-\epsilon\). A departure from a site certifies
   that all its holes have filled. Hence that large ball has no remaining
   hole. On the bump's support, \(H_t=0\), so the positive test integral
   certifies an active particle within \(rR\). Consequently
   \(D_H>(K+1)rR>K D_A\). Let \(\epsilon\downarrow0\).

**The precise low-dimensional input** is Step 1 and the positive continuous
limit in Step 4. The divisible mean has scale \(n^{(4-d)/4}\). Proposition 7.1,
p. 21, bounds the \(L^{\lceil\log n\rceil}\) odometer discrepancy by, respectively,
\(Cn^{5/8}(\log n)^{3/4}\), \(Cn^{1/4}(\log n)^{5/4}\), and
\(Cn^{1/8}(\log n)^{3/4}\). Dividing by the respective means
\(n^{3/4},n^{1/2},n^{1/4}\) gives a negative power of \(n\) times a logarithm.
The resulting \(\exp[-c(\log n)^2]\) tail survives a union bound over
\(O(R^{d+2})\) space-time mesh points. At \(d=4\) there is no such
power gap, the mean has logarithmic growth, and the centered membrane field
does not have a continuous point-valued spatial limit in this topology.
Steps 2–4 alone do not fix that failure.

The proof controls distances by a hole-free ball on the **diffusive spatial
scale** \(\sqrt t\), not by comparing the numerical values of an odometer
and a distance. It also implies \(D_A/\sqrt t\to0\) in probability by taking
the test bump arbitrarily small, while \(D_H/\sqrt t\) is bounded away from
zero in probability. It does not assert a precise asymptotic scale for either
nearest distance.

### Theorem 1.6, exactly: dimensions at least five

For each \(d\ge5\), Theorem 1.6 (p. 6) constructs \(p_d\in(0,1/2)\) and
\(c>0\) such that iid
\(\mathbb P(\eta=1)=\mathbb P(\eta=-1)=p_d\),
\(\mathbb P(\eta=0)=1-2p_d\), satisfy

\[
\liminf_{t\to\infty}\mathbb P(D_H(t)<D_A(t))\ge c.
\]

The construction takes \(p_d\le1/4\). Here is the proof in §8.2, pp. 24–28,
including the auxiliary estimates it uses. All its constants are independent
of \(p\in(0,1/4]\) until the final choice of a sufficiently small \(p\).

1. **Potential kernel, p. 24, equation (46).** Set
   \(G(x)=\sum_{n\ge0}P_0(X_n=x)\), \(g=G(0)\) and
   \(q_x(y)=G(y-x)/g=P_y(T_x<\infty)\). Chapman–Kolmogorov and Gaussian
   bounds give
   \[
   \sum_yG(y-x)G(y-z)=\sum_{n\ge0}(n+1)P_0(X_n=z-x)
      \le C(1+|x-z|_1)^{4-d}.
   \tag{H1}
   \]
   In particular \(\sum_yG(y)^2<\infty\). Write
   \(m_t=\mathbb EU_t(0)\), \(h_t=\mathbb P(H_t(0)=1)\). Then
   \(\mathbb EA_t=\mathbb EH_t=h_t\) and \(m_t=\sum_{s<t}h_s\).

2. **Odometer and survival, Lemma 8.2, pp. 24–26.** For \(r\ge2\),
   \[
   \|U_t(x)\|_r\le C(m_t+r),\qquad
   m_t\le C\log(1/h_t),\qquad h_t\downarrow0.
   \tag{H2}
   \]
   Raising an initial coordinate from \(-1\) to \(1\) changes the expected
   odometer, conditional on the initial configuration, by at most
   \(2G(y-x)\), using the one-particle discrepancy walk. Square summability
   gives \(\|\mathbb E[U_t\mid\eta]-m_t\|_r\le C\sqrt r\).
   Revealing used instructions next gives bounded increments and quadratic
   variation with total weight \(\sum G^2\); the martingale inequality gives
   \(\|U_t\|_r\le m_t+C\sqrt r+C\sqrt{r\|U_t\|_r}+Cr\).
   Absorb the square root to obtain the first bound.

   Empty the origin and make it a permanent sink. If \(J\) is its arrival
   count by time \(t\), its compensator is
   \(\lambda=(2d)^{-1}\sum_{y\sim0}U_t^{\rm sink}(y)\).
   Independence of the initial origin gives \(h_t=pP(J=0)\), equation (50).
   Monotone comparison gives \(E\lambda\le m_t\); optional stopping of the
   expected sink odometer at the origin or the radius-\(t\) boundary gives
   \(E\lambda\ge m_t/g\), equation (51).
   For the conditional initial-data part, oscillations are at most
   \(2q_0(y)\); for instructions, the variance weights again sum to
   \(\sum q_0^2<\infty\). Bounded differences and the first moment bound
   with \(r\) a small multiple of \(m_t\) yield
   \(P(\lambda<E\lambda/2)\le Ce^{-cm_t}\), equation (52).
   Revealing chronological instructions produces the supermartingale
   \(1_{\{J=0\}}e^\lambda\), in the sense
   \(E[1_{\{J=0\}}e^\lambda]\le1\), since \((1-a)e^a\le1\).
   Splitting at \(\lambda=E\lambda/2\) gives
   \(P(J=0)\le Ce^{-cm_t}\), hence the second bound in (H2).
   If \(m_t\) is bounded, summability of \(h_t\) implies \(h_t\to0\);
   otherwise the exponential bound does. Holes never reappear, so the decrease
   is monotone.

3. **Two-hole probabilities, Proposition 8.3, pp. 26–28.** The conclusion is
   \[
   P(H_t(x)=H_t(z)=1)\le Ch_t^2
       \exp\{C\log(1/h_t)(1+|x-z|_1)^{4-d}\}\quad(x\ne z).
   \tag{H3}
   \]
   Reveal initial values in the finite influence region, followed by used
   instructions in chronological order. A discrepancy started at \(v\)
   reaches \(x\) with conditional probability at most \(q_x(v)\). If
   \(a_0,a_1\) are the conditional hole probabilities before and after adding
   one particle, this gives
   \((1-q_x(v))a_0\le a_1\le a_0\), equation (54).
   Divide the product of the two conditional hole probabilities by the
   accumulated upper factors for its conditional mean increase. Calling
   their product \(D\), the resulting supermartingale gives
   \(E[1_{\{H_t(x)=H_t(z)=1\}}/D]\le h_t^2\), equation (55).

   The initial-value factors are at most
   \(\exp[C\sum_vq_x(v)q_z(v)]\). For an instruction at \(y\), set
   \(k_y=(2d)^{-1}\sum_{v\sim y}q_x(v)q_z(v)\).
   Expanding the normalized conditional product gives a factor at most
   \(e^{Ck_y}\). Thus
   \(D\le\exp[C\sum_vq_x(v)q_z(v)+C\sum_yk_yU_t(y)]\), equation (57), and
   \(\sum_yk_y\le C(1+|x-z|_1)^{4-d}\), equation (56).
   Put \(\ell=\log(1/h_t)\), choose \(r=\lceil4\ell\rceil\), and use Hölder,
   Minkowski and (H2), conditional on the hole at \(z\), to get
   \(\|\sum_yk_yU_t(y)\|_{r\mid H_t(z)=1}\le C\ell\sum_yk_y\).
   Markov at a sufficiently large multiple of this threshold gives a
   conditional exceptional probability at most \(e^{-r}\le h_t^4\).
   Splitting the supermartingale bound at that threshold gives (H3).

4. **Close-hole bound, Lemma 8.4, p. 28.** For distinct \(x,z\),
   \(P(H_t(x)=H_t(z)=1)\le2p h_t\), equation (59).
   On a two-hole event change the initial \(-1\) at \(z\) to \(0\).
   No particle had reached \(z\), so the evolution elsewhere is unchanged.
   The injective change of initial configuration multiplies its probability
   weight by \((1-2p)/p\), proving the bound.

5. **Isolated holes, p. 28, final proof Step 1.** Write \(h=h_t\) and
   \(\ell=\log(1/h)\). Choose \(L\) with \(C(1+L)^{4-d}\le1/4\), and
   then small \(p,b>0\) with \(CL^dp+Cb^d\le1/8\).
   Let \(R=\lfloor bh^{-1/d}\rfloor\). Eventually \(R\ge2d\) and
   \(\ell^{1/(d-4)}<R\). A union bound for other holes within \(4R\)
   has three ranges. At distances below \(L\), Step 4 bounds the sum by
   \(CL^dph\). From \(L\) to \(\ell^{1/(d-4)}\), (H3) makes each term
   at most \(Ch^{7/4}\), and their total is
   \(C\ell^{d/(d-4)}h^{7/4}=o(h)\). Above that threshold the exponential
   in (H3) is bounded, giving total \(CR^dh^2\le Cb^dh\).
   Thus nonisolated holes have density at most \(h/4\), and isolated ones
   density at least \(3h/4\).

6. **Few active sites, p. 28, Step 2.** Balls of radius \(2R\) about isolated
   holes are disjoint. Let every active site in such a ball send unit mass
   to its center. Since \(P(A_t(0)>0)\le EA_t(0)=h\), mass transport bounds
   the density of isolated holes with at least two active sites in the ball
   by \(h/2\). At least \(h/4\) of hole centers consequently have at most
   one active site in their radius-\(2R\) ball.

7. **A positive volume is nearer a hole, p. 28, Step 3.** At a good center \(y\)
   choose the coordinate orthant opposite its one possible nearby active
   site \(a\), with a fixed choice for tied coordinates; if none exists,
   choose a fixed orthant. For \(w\) in this orthant and \(B_R(y)\),
   \(|w-a|_1=|w-y|_1+|a-y|_1>|w-y|_1\).
   Every other active site lies beyond \(2R\) and is also farther from
   \(w\) by the triangle inequality. The region has at least \(cR^d\)
   sites. The radius-\(R\) regions from distinct isolated holes are disjoint,
   so mass transport yields
   \(P(D_H<D_A)\ge cR^dh/4\ge c'>0\) for all sufficiently large \(t\).
   This proves the stated liminf.

**Every use of \(d\ge5\).** The decay and finiteness in (H1) require
\(d>4\). Its square summability controls both the initial-data and instruction
parts of Lemma 8.2, including its sink lower tail; the same kernel controls
Proposition 8.3. Finally Step 5 needs a finite \(L\) making
\(L^{4-d}\) small and the polylogarithmic radius \(\ell^{1/(d-4)}\), which
is negligible compared with the density spacing \(h^{-1/d}\). None of those
choices exists by this argument at \(d=4\). The last two geometric
mass-transport steps do not require \(d>4\); they would transfer if the
isolated-hole density estimate could be proved there.

The high-dimensional proof therefore compares **hole correlations with their
density spacing**, rather than relying just on the odometer's growth rate.
The dimension-four logarithmic divergence enters precisely before that
isolation step. Neither this audit nor the checks supply its replacement.

Task: “Open problem I0005 … decide d = 4.” Work began 13 November 2026,
15:17 +04 (Asia/Tbilisi); the prompt's receipt time was not separately supplied.
