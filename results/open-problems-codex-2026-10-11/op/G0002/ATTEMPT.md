# G0002: finite refutation of Conjecture 53.1

Date: 2026-10-11. Verdict: proof below refutes the conjecture for BOTH functionals. This is an independent proof motivated by the source's Section 62, not SOLVED_IN_LITERATURE.

## 1. Exact objects and statement

Identify a configuration with its support w subset [n]. Write w-i = w minus {i}. For an increasing A, first positive pivotality at an arbitrary configuration x means x-i not in A and x union {i} in A. The source's (49.1) allows deleting at most k-1 initially occupied coordinates before testing first pivotality. At w IN A, first pivots are {i in w: w-i not in A}. Formula (49.1), read literally with P^+ from (39.2), says

P_2^+(A,w) = P_1^+(A,w) union
 {i in [n]: there exists j in w,
    (w-j)-i not in A and (w-j) union {i} in A}.

An initially ZERO i may occur under this literal definition. The source's small-case tables instead match the restriction to initially occupied i. For instance for A={10,01,11} at n=2 the literal formula gives phi_2=6, while the table gives 4. This discrepancy is explicitly retained in verification.json. The proof below refutes the conjecture BOTH under the literal formula and under the occupied-coordinate restriction matching the tables. It does not require resolving the editorial discrepancy: its lower bound counts only occupied second pivots whose partner deletion stays in A, and its upper bound uses |P_2^+|<=n.

For an occupied coordinate i that is not first-order, the witness condition simplifies to: there exists j in w minus {i} such that w-j in A and w-{i,j} not in A. This sufficient condition is all that the lower-bound argument needs.

The exact objectives are phi_2(A)=sum_{w in A}|P_2^+(A,w)| and phi_{2\\1}(A)=sum_{w in A}|P_2^+(A,w) minus P_1^+(A,w)|. The intake's sum over all configurations is corrected here to the source's sum over A. The conjecture asserts that EVERY maximizer of either objective contains all supports of size at least n/2+1 and contains no support of size less than n/2-2.

We prove that at the concrete dimension n=100000000000000, EVERY maximizer of EITHER exact objective violates that band. Existence of a maximizer is automatic because the collection of increasing subsets is finite.

## 2. Uniform upper bound inside the conjectured band

Let n=2d be even, n>=20, and suppose {w:|w|>=d+1} subset A subset {w:|w|>=d-2}. If |w|>=d+3, any configuration obtained by deleting at most two occupied coordinates has size >=d+1 and belongs to A. Thus w has no positive pivots of order at most two. For w in A with a pivot, d-2 <= |w| <= d+2. There are FIVE possibly contributing levels. We deliberately do not use the source's displayed four-level estimate.

At a contributing configuration |P_2^+| <= n, under either reading of the definition. Each level has at most binom(2d,d) configurations. Consequently both normalized objectives are at most

  2^(-n) phi_2(A) <= 5n binom(2d,d)/4^d.                 (B1)

Here is an elementary bound sufficient for our purpose:

  binom(2d,d)/4^d <= 1/sqrt(d+1) <= 2/sqrt(n).              (B2)

For the first inequality, set b_d=binom(2d,d)/4^d. We have b_0=1 and b_{d+1}/b_d=(2d+1)/(2d+2). The induction step follows by squaring from

  (2d+1)^2(d+2) <= 4(d+1)^3,

whose right minus left is 3d+2>=0. The second inequality follows by squaring from n=2d<=4(d+1). Combining (B1)-(B2), gives

  2^(-n) phi_{2\\1}(A) <= 2^(-n) phi_2(A)
  <= 10 sqrt(n).                          (B3)

## 3. Random increasing CNF construction

Fix integers

  n=10^14, h=10^7, r=10^6, M=2^r.

Thus n=h^2=100 r^2 and r=h/10. Independently for each clause b in [M], draw r coordinates Y_{1,b},...,Y_{r,b} uniformly from [n], WITH replacement. Put

  A_Y = {w subset [n]: every clause b has at least one sampled coordinate in w}.

This is increasing for every fixed array Y. No array is actually generated; the argument uses a finite probability space to prove existence. All assertions below allow repeated coordinates.

Fix a support w of size s with |s-n/2|<=h. Write z=1-s/n. In particular n/3<=s<=2n/3 and (s-1)/n>=1/3. A clause fails with probability q_0=z^r. Its success probability is 1-q_0. Conditional on w in A_Y, the clauses remain independent, each with its original law conditioned on success: this follows directly by factoring the product probability of clause events.

We will use these elementary estimates. For 0<=u<1 and k u<1,

  (1+u)^k <= 1/(1-ku),                                   (E1)

since binom(k,j)<=k^j and the binomial expansion is bounded by the infinite geometric series. Also (1-u)^k>=1-ku (induction/Bernoulli). Because |2z-1|<=2/h and r(2/h)=1/5, these imply

  (2z)^a <= 2 for 0<=a<=r,
  (2z)^(r-2) >= 4/5.                                    (E2)

For the lower bound, if 2z>=1 it is immediate; otherwise use Bernoulli. Further,

  (2z+2/n)^(r-1) <= 2,                                  (E3)

because r(2/h+2/n)=1/5+1/(5h)<1/4 and (E1) bounds it by 4/3 when the base exceeds 1; otherwise it is <=1.

It follows that M q_0=(2z)^r<=2. Also q_0<=2/M<=1/2. Since log(1-u)>=-2u for 0<=u<=1/2 (integrate 1/(1-u)<=2),

  P_Y(w in A_Y)=(1-q_0)^M >= exp(-2 M q_0)
  >= exp(-4) > 1/81.                                    (E4)

For completeness e<3 follows from its series: for k>=2, k!>=2^(k-1), with a strict inequality for k>=3, hence e=2+sum_{k>=2}1/k!<3. Therefore e^4<81.

## 4. Deterministic graph lemma, with duplicate-safe singleton definition

For this fixed w and a successful array, let S be the set of first pivots. Equivalently, i belongs to S exactly when some clause's set of distinct positive sampled coordinates is {i}. This includes clauses that repeat i several times.

Build a multigraph G on w: each clause with exactly TWO positive sample POSITIONS, whose actual coordinate values are DISTINCT, supplies an edge joining those values. Let C be the set of vertices covered by these edges. Call an edge bad if either endpoint is in S; let B be the NUMBER of bad edge instances, counted with multiplicity. Let V_bad be the union of their endpoints.

Every vertex i in C minus V_bad is a second pivot that is not a first pivot. Indeed choose an incident edge {i,j}. Neither endpoint is in S. Deleting j alone preserves success of every clause, so w-j belongs to A_Y. Deleting i and j empties the positive part of the selected clause, so w-{i,j} does not belong to A_Y. Hence i is a first pivot at w-j, and is a second positive pivot at w. Since i is not in S it is not first-order at w. An endpoint of a covered edge lying in S would necessarily belong to V_bad, so there is no omitted case.

Since |V_bad|<=2B, pointwise on successful arrays,

  |P_2^+(A_Y,w) minus P_1^+(A_Y,w)| >= |C|-2B.             (G1)

A negative right side causes no problem. This is the key combinatorial certificate; Certificate.lean formalizes the pair-witness implication for arbitrary clause and coordinate types.

## 5. Coverage lower bound

For a fixed i in w, the unconditional probability a single clause supplies a graph edge incident to i is

  a_i = r(r-1)(s-1)/n^2 * z^(r-2).                        (C1)

To count it, choose the two positive positions in binom(r,2) ways, choose which position is i in two ways, choose the other value from s-1 options, and require the remaining positions to be outside w. No positive duplicates are counted as edges.

Conditional on success of a clause, t_i=a_i/(1-q_0). Using (E2), r(r-1)>=r^2/2, (s-1)/n>=1/3, and 1/(1-q_0)<=2, we obtain

  M t_i >= M a_i
  = 4 r(r-1)(s-1)/n^2 * (2z)^(r-2)
  >= (8/15) r^2/n >= r^2/(2n),

  M t_i <= (32/3) r^2/n < 1.                             (C2)

The upper bound used r(r-1)<=r^2, (s-1)/n<=2/3 and (2z)^(r-2)<=2. Under conditional clause independence, the first two terms of inclusion-exclusion give

  P(i in C | w in A_Y) >= M t_i - binom(M,2)t_i^2
  >= M t_i - (M t_i)^2/2 >= M t_i/2 >= r^2/(4n).

Summing over the s>=n/3 vertices yields

  E(|C| | w in A_Y) >= r^2/12.                            (C3)

## 6. Bound bad edges, including positive repetitions

Let q_S be the unconditional probability a clause has exactly ONE distinct positive coordinate (possibly repeated), and q_E the probability it supplies a graph edge. For any fixed i in w, the singleton-at-i probability is

  (z+1/n)^r-z^r <= (r/n)(z+1/n)^(r-1),

by the identity a^r-b^r=(a-b)sum_{k=0}^{r-1}a^(r-1-k)b^k. These events are disjoint across the s possible coordinates. Thus

  q_S <= (sr/n)(z+1/n)^(r-1),
  q_E = binom(r,2)(s/n)^2 z^(r-2)(1-1/s).

Let Q_S=q_S/(1-q_0) and Q_E=q_E/(1-q_0) be the conditional single-clause probabilities. By (E2)-(E3),

  M Q_S <= (16/3) r < 6r,
  M Q_E <= (32/9) r^2 < 4r^2.                             (D1)

For example, M q_S <= 2(sr/n)(2z+2/n)^(r-1) <= (8/3)r, and conditioning costs at most a factor two. Likewise M q_E <= 2 r(r-1)(s/n)^2(2z)^(r-2) <= (16/9)r^2, before conditioning.

An edge clause cannot itself be a singleton clause. Given an edge clause and its endpoints, every OTHER clause is independent under conditioning on w in A_Y. By symmetry its singleton-at-a-specified-endpoint probability is Q_S/s. A union bound over the two endpoints and the other M-1 clauses therefore gives

  E(B | w in A_Y) <= M Q_E * 2(M-1)Q_S/s
  <= (4r^2)(6r) * 2/(n/3) = 144 r^3/n.                  (D2)

This argument does not assume independence between different pivotal indicators. Multiple clauses with the same edge cause no problem because B counts edge instances.

By (G1),(C3),(D2),

  E(|P_2^+ minus P_1^+| | w in A_Y)
  >= r^2/12 - 288 r^3/n >= r^2/24.                       (D3)

The last inequality follows from n>=6912r, true for the fixed integers; its exact rational margin is checked in Lean.

## 7. Averaging and refutation of both extremal assertions

Now let w itself be uniform on the cube, independently of the array. Its size has mean n/2 and variance n/4. Chebyshev yields

  P(| |w|-n/2 |<=h) >= 3/4,

since h^2=n. For each fixed central w, (E4) and (D3) apply uniformly. Outside the central range the objective is nonnegative. Taking expectations in this order therefore gives

  E_Y[2^(-n) phi_{2\\1}(A_Y)]
  = E_w E_Y[1_{w in A_Y}|P_2^+ minus P_1^+|]
  >= (3/4)(1/81)(r^2/24) = r^2/2592
  = n/259200 > 10h = 10 sqrt(n).                           (R1)

Everything is a finite sum, so interchanging the expectations needs no limiting argument. By averaging there exists a FIXED array Y_0 with normalized phi_{2\\1}(A_{Y_0}) at least r^2/2592. Since phi_2>=phi_{2\\1}, that same increasing set exceeds the bound (B3) for both objectives.

Let F be either objective and A* any global maximizer of F among increasing subsets at this fixed n. Then

  2^(-n) F(A*) >= 2^(-n) F(A_{Y_0}) > 10 sqrt(n),

whereas every band-contained A has normalized F(A)<=10 sqrt(n) by (B3). Thus A* cannot satisfy the claimed pair of inclusions. This refutes Conjecture 53.1, for BOTH alternatives, at n=10^14. It is unnecessary to know the exact maximizer or to enumerate it. If a canonical witness is desired, order all finite arrays lexicographically, take the first whose objective is at least r^2/2592 times 2^n, and then take the first increasing global maximizer. The finite averaging argument proves these sets exist; this is an existential counterexample, not an explicitly stored truth table.

## 8. Hostile-referee checklist and practical limits

- Exact source functional: uses only w in A and counts coordinates, not pairs. The literal formula and the occupied-coordinate variant matching the tables are both treated. Source locators and raw PDF saved.
- Repeated sampled coordinates: singleton S uses DISTINCT positive coordinates. The singleton bound includes all repetitions. Pair edges require distinct values. This repairs a delicate point in the source's argument.
- Deletion of a partner: verified using partner not in S; merely having a two-positive clause would not suffice.
- Conditioning: only on the intersection of independent single-clause success events for a fixed w, so conditional clause independence is valid. No global pivotal independence is asserted.
- Bad-edge loss: at most two endpoints per bad edge instance, even for multigraphs.
- Band support: five levels, not four; independent upper bound proved.
- Finite quantifiers: concrete n, integer r,M, a finite averaging argument, and actual global maximizers by finiteness. No asymptotic o(1) or central limit theorem is used.
- Computation: exact rational checks and separate small-cube checks are logged separately. No gigantic array or cube is instantiated.
- Lean checks only the deterministic pair-witness step and explicit rational inequalities. The probabilistic and binomial arguments are mathematical proofs above, not claimed fully formalized.

Remaining mathematical gap: NONE in the refutation above, with the final checks below completed. The literal-formula versus table discrepancy is documented, and BOTH readings are refuted by the same proof. Literature coverage remains bounded because OpenAlex and Semantic Scholar returned HTTP 429; that does not affect the independent counterexample.

## 9. Completed checks

- `python -X utf8 verify.py` passed. Exhaustive monotone families in dimensions 1 through 5 had counts 3,6,20,168,7581. The literal formula produced maxima phi_2=1,6,15,36,100 and phi_{2\1}=0,4,12,24,76; all their maximizers satisfied the band in these dimensions. The direct formula and occupied-coordinate pair-witness characterization agree AFTER restricting the direct formula to occupied coordinates.
- `python -X utf8 verify_open.py` passed. The occupied-coordinate variant produced maxima phi_2=1,4,9,24,62 and phi_{2\1}=0,2,6,12,38, reproducing the source tables.
- All 729 arrays with n=3,r=2,M=3 were enumerated; all 2640 successful array/support pairs satisfied the duplicate-safe graph lemma.
- `lake env lean ~/brain_workers/TRIO_1011/op/G0002/Certificate.lean`, from ~/lean_verify, completed with exit code 0. Only Mathlib.Tactic.NormNum is imported. No sorry, no native_decide, and no unverified axioms are used. The Lean file checks the generic clause-witness implication and five explicit rational margins, including r^2/2592>10 sqrt(n) at the chosen square dimension. It does not formalize the full probability proof.
- The first Lean invocation failed because PowerShell wrote a UTF-8 BOM before the import. Rewriting the file as UTF-8 without BOM resolved that parser error. A small-case assertion also exposed the literal-versus-occupied discrepancy; the proof was corrected to cover both and the test now records each separately.

The final lower-bound certificate is r^2/2592=31250000000/81. The conservative common band bound is 100000000. Their exact positive difference is 23150000000/81. The more precise computed graph lower bound before weakening to r^2/24 is 249991360000/3. See verification.json and lean_check.txt.
