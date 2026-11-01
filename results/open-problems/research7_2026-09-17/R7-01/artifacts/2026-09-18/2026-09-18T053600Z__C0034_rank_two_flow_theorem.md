Model actually running: GPT-5.6 Sol. Reasoning level: UNVERIFIED — this is not GPT-6 at maximum; no authenticated runtime model/effort telemetry or binding selector is exposed.

# C0034 — an exact rank-two union-coupling theorem via capacitated fractional orientation

Target: Russell Lyons, *Determinantal Probability: Basic Properties and Conjectures* (ICM 2014), Question 2.8.

Status of this artifact: **restricted theorem, not full source closure**. It proves Question 2.8 whenever the total projection rank is at most two, on finite ground sets and, by compactness, on countable ground sets. It does not settle decompositions of total rank at least three or arbitrary infinite rank.

Frozen R7-01 metric before this run: `R_univ >= 1`, where `R_univ` is the largest total finite rank for which every finite-ground-set orthogonal decomposition has a union-marginal coupling.

Result below: `R_univ >= 2`.

## 1. Idea before code

When `dim H1=dim H2=1`, write `H1=span(u)`, `H2=span(v)` with `u,v` orthonormal. Then `P^{H1}` and `P^{H2}` each choose one coordinate, while `P^{H1⊕H2}` chooses an unordered pair. The coupling problem is therefore exactly a **fractional orientation** problem: split the mass of every unordered pair `{i,j}` between the two possible labelings `(i,j)` and `(j,i)` so that the outgoing mass at vertex `i` is `|u_i|^2` and the incoming mass is `|v_i|^2`.

The obstruction to a fractional orientation is a cut-capacity inequality. For the determinantal pair weights, that cut inequality has an exact closed form and is automatically satisfied by orthogonality. This eliminates every possible rank-two counterexample.

## 2. Determinantal weights in rank two

Let `E` first be finite. Let `u,v in l^2(E)` be orthonormal and put

`a_i = |u_i|^2`,  `b_i = |v_i|^2`.

For distinct `i,j`, put

`w_ij = |u_i v_j - u_j v_i|^2 = w_ji`.

The projection DPP laws are

`P^{span(u)}({i}) = a_i`,

`P^{span(v)}({i}) = b_i`,

and, for `H=span(u,v)`,

`P^H({i,j}) = w_ij`.

The last identity is the two-by-two Gram determinant / Cauchy–Binet formula.

Orthogonality gives the exact weighted-degree identity

`sum_{j != i} w_ij = a_i + b_i`.                         (2.1)

Indeed,

`sum_j |u_i v_j-u_j v_i|^2`
`= |u_i|^2 ||v||^2 + |v_i|^2 ||u||^2`
`  - 2 Re( u_i conjugate(v_i) sum_j v_j conjugate(u_j) )`
`= a_i+b_i`,

because `||u||=||v||=1` and `<u,v>=0`.

Also `sum_{i<j}w_ij=1`, as expected for the rank-two projection DPP.

## 3. Fractional-orientation lemma

**Lemma 3.1.** Let a finite undirected graph have nonnegative edge weights `w_ij`. Let `a_i>=0` satisfy

`sum_i a_i = sum_{i<j} w_ij`.

There exist nonnegative directed masses `x_ij` (`i!=j`) such that

`x_ij+x_ji=w_ij`,                                         (3.1)

`sum_{j!=i} x_ij=a_i`                                    (3.2)

for every `i` if and only if, for every vertex set `S`,

`W(S) <= a(S) <= W(S)+C(S)`,                             (3.3)

where `W(S)` is the total weight of edges internal to `S` and `C(S)` is the total weight of the cut from `S` to `S^c`.

**Proof.** Necessity is immediate: every internal edge contributes exactly its full weight once to the sum of outgoing masses over vertices in `S`, while each crossing edge contributes between zero and its full weight.

For sufficiency, let

`m_i=sum_j w_ij`, `d_i=2a_i-m_i`.

Writing

`x_ij=(w_ij+y_ij)/2`,

conditions (3.1)–(3.2) become

`y_ji=-y_ij`, `|y_ij|<=w_ij`, and `sum_j y_ij=d_i`.       (3.4)

Thus we need a capacitated antisymmetric flow with prescribed divergence `d`. Since `sum_i d_i=0`, the standard finite max-flow/min-cut criterion says such a flow exists exactly when

`|d(S)| <= C(S)`                                           (3.5)

for every `S`. But

`d(S)=2a(S)-2W(S)-C(S)`,

so (3.5) is precisely the pair of inequalities (3.3). This proves the lemma. QED.

This proof is constructive: any max-flow algorithm on the cut-capacitated graph produces the required coupling.

## 4. The determinantal cut identity

Fix `S subset E`, and abbreviate

`A = sum_{i in S} a_i`,

`B = sum_{i in S} b_i`,

`c = sum_{i in S} conjugate(u_i) v_i`.

Because `<u,v>=0`, the corresponding sum over `S^c` equals `-c`.

The determinantal cut weight is

`C(S)=sum_{i in S, j notin S}|u_i v_j-u_j v_i|^2`

and direct expansion gives

`C(S)=A(1-B)+B(1-A)+2|c|^2`.                              (4.1)

In particular,

`C(S) >= |A-B|`.                                           (4.2)

To see this without any hidden case, if `A>=B` then

`C(S)-(A-B)=2B(1-A)+2|c|^2 >=0`;                          (4.3)

if `B>=A`, the symmetric formula is

`C(S)-(B-A)=2A(1-B)+2|c|^2 >=0`.                          (4.4)

Equation (4.2) is exactly the max-flow cut condition for the divergence

`d_i=a_i-b_i`,

because (2.1) gives `2a_i-m_i=a_i-b_i`.

Therefore the fractional orientation exists for every orthonormal pair `u,v`.

## 5. Universal total-rank-two coupling theorem

**Theorem 5.1 (finite ground set).** Let `E` be finite and let

`H=H1⊕H2 <= l^2(E)`

be an orthogonal decomposition with `dim H <=2`. Then there exists a coupling `(X1,X2)` with marginals `P^{H1}`, `P^{H2}` such that

`X1 union X2 ~ P^H`.

If both summands have rank one, the coupling is automatically disjoint.

**Proof.** If one summand is zero, couple it with the empty set and use the other DPP, so only the `1+1` split needs proof. Choose orthonormal `u,v` spanning the two lines. By Sections 3–4 there are nonnegative numbers `x_ij` satisfying

`x_ij+x_ji=w_ij`,

`sum_j x_ij=a_i`.

Define

`P(X1={i}, X2={j})=x_ij` for `i!=j`.

The first marginal is `a_i=P^{H1}({i})`. By (2.1), the incoming mass at `j` is

`sum_i x_ij = sum_i w_ij - sum_i x_ji = (a_j+b_j)-a_j=b_j`,

so the second marginal is `P^{H2}`. Finally, for every unordered pair `{i,j}`,

`P(X1 union X2={i,j})=x_ij+x_ji=w_ij=P^H({i,j})`.

This is the required coupling. QED.

### Countable extension

The same theorem holds for countable `E` when the total rank is two. The edge weights have total mass one and each weighted degree is finite. For an increasing finite exhaustion `F_n`, compress all vertices outside `F_n` to a reservoir vertex and apply Lemma 3.1; the cut inequalities needed for subsets of `F_n` are inherited from (4.2). Expand the reservoir-edge mass arbitrarily across the actual outside edges in proportion to their capacities. This gives orientations satisfying the exact degree constraints on `F_n` and all pair-splitting constraints.

The product `prod_{i<j}[0,w_ij]` is compact. Take a convergent subnet (a diagonal subsequence suffices because the edge set is countable). For each fixed vertex `i`, `sum_j x_ij` is a uniform limit of its finite partial sums because `0<=x_ij<=w_ij` and `sum_jw_ij=a_i+b_i<infinity`; hence the degree equality is closed under the limit. The limit orientation therefore gives the same coupling on countable `E`.

## 6. B2 — attack the negation

A rank-two counterexample would require some set `S` whose required divergence exceeds the total pair mass crossing the cut:

`|a(S)-b(S)| > C(S)`.

But (4.1) makes the deficit exact:

if `A>=B`,

`C(S)-(A-B)=2B(1-A)+2|c|^2`;

if `B>=A`,

`C(S)-(B-A)=2A(1-B)+2|c|^2`.

Both are nonnegative. Thus the complete negation route is impossible in total rank two.

## 7. B24 — extremal/tight cuts

The same formula identifies every possible tight cut. If `A>=B`, equality in the cut condition occurs exactly when

`B(1-A)=0` and `c=0`.

Thus either the `v`-mass inside `S` is zero, or all `u`-mass lies inside `S`, and in either case the restricted inner product vanishes. The symmetric statement holds when `B>=A`.

So the extremal rank-two transport obstructions are not mysterious LP vertices: they occur only at support-separation boundaries. In the genuine interior (`0<A,B<1`) every nontrivial cut has strict slack unless the smaller mass vanishes. This suggests that any first counterexample in higher rank must use a genuinely higher-order family constraint, not the one-cut obstruction visible in rank two.

## 8. B11 — dualization

The coupling LP in rank two has primal variables `x_ij`. Passing to the skew variables `y_ij` dualizes the feasibility question to a capacitated transshipment problem. Max-flow/min-cut collapses the entire Farkas dual to the scalar family

`|a(S)-b(S)| <= C(S)` for all `S`.

The determinantal identity (4.1) proves every dual inequality with an explicit nonnegative slack. Thus there is no hidden finite LP obstruction in rank two. This is stronger than the previous floating-point feasibility evidence: it is a universal exact proof.

## 9. Exact rational check (not part of the proof)

For

`u=(1,2,2)/3`, `v=(2,-2,1)/3`,

we have

`a=(1,4,4)/9`, `b=(4,4,1)/9`,

`w_01=4/9`, `w_02=1/9`, `w_12=4/9`.

An exact directed split is

`x_01=1/9`, `x_10=1/3`,

`x_02=0`,   `x_20=1/9`,

`x_12=1/9`, `x_21=1/3`.

Every row sum is `a_i`, every column sum is `b_i`, and each opposite pair sums to `w_ij`. An exact `Fraction` check of this witness and all six proper nonempty cuts was executed; archived output ends `ALL_EXACT_CHECKS_PASS`.

## 10. Metric movement and remaining gap

Frozen metric:

`R_univ >= 1  -->  R_univ >= 2`.

This is genuine movement.

The full source remains OPEN/PARTIAL. The first unresolved total rank is three (`1+2` split). Rank two works because pair masses form an ordinary weighted graph and the LP dual reduces to graph cuts. At rank three, a union is a 3-set and choosing which part belongs to which summand creates a higher-order transportation problem; the graph-cut reduction no longer directly applies.

The next attack should therefore target the minimal `1+2` case and ask whether its Farkas dual admits an analogous determinantal inequality or whether a finite rational counterexample exists.
