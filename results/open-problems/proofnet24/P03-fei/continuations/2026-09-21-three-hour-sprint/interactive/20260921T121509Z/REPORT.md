# FEI sprint result 1: balanced composition, cancellation entropy, and a false sharp target

Date: 21 September 2026. Author context: owner-directed interactive research, not a scheduled slot. Brain status: WITHOUT_VERIFIED_BRAIN. Full uniform-cube FEI: OPEN; no full proof or counterexample is claimed here. Model self-report: GPT-6 Astra Pro; configured effort and provider thinking counters are not exposed. Native work was first instrumented at 12:15:09 UTC. This report records completed work, not three hours of uninterrupted execution.

## What changes the research target

1. The full-FEI constant cannot equal 6.4547837. A public July 2026 construction already gives C > 6.521845710923046575. This report independently reconstructs its exact 18-variable truth table, matches the published SHA-256, checks balance and every monotonicity edge, and encloses its entropy using exact rational arithmetic. This is external prior work, not a newly discovered FEI lower bound.
2. The particular proposed auxiliary inequality B_can(f) <= 2.2273918583 I(f) is false. A finite balanced Boolean function obtained by five levels of disjoint composition of that seed has B_can/I > 2.25806507780602610165. A complete composition proof and a reproducible rational certificate are supplied below.
3. A weaker dimension-independent cancellation bound remains a legitimate route to full FEI, but its constant must be at least 2.32399499026264678602. Neither this lower bound nor a successful finite check proves the remaining universal upper bound.
4. The read-once AND/OR/NOT upper-bound calculation is a DIFFERENT scope. Its reported 6.4573 upper bound and attempted 6.45555 improvement are not refuted by a general Boolean construction. Do not transfer an alleged sharp read-once constant to unrestricted FEI.

No publication-priority or novelty claim is made for the identities assembled here. The new operational contribution is an explicit proved obstruction to a live fleet target and exact recurrences that avoid exponential truth-table expansion.

## 1. Definitions and inherited reduction

Use the uniform cube, Boolean values in {-1,+1}, normalized Walsh coefficients, and base-2 logarithms. Write

p_f(A) = fhat(A)^2,
u_f(A) = sum_{B superset A} p_f(B),
B_can(f) = sum_{A:p_f(A)>0} p_f(A) log2(u_f(A)/p_f(A)).

Thus u_f(empty)=1. In particular the empty-atom contribution to B_can is exactly its entropy contribution. Set H(f)=sum_A p_f(A) log2(1/p_f(A)) and I(f)=sum_A |A|p_f(A).

The prior fleet report at proofnet24/P03-fei/fleet-2026-09-21/fleet01/B12/20260921T111623Z-spectral-cancellation/REPORT.md (creation commit 1ec69f5e1e70004d119f7055a231ad536e4c67be) gives, with V=1-p_f(empty),

H(f) <= 2I(f)-2V-p_f(empty)log2(1/p_f(empty))+2B_can(f).

For completeness, its key step follows directly from Boolean granularity. For a nonempty A of size k, the top coefficient C_A(y) of each k-dimensional restriction is in 2^(1-k) Z. Hence C_A(y)^2 >= 2^(1-k)|C_A(y)|. Averaging yields u_f(A) >= 2^(1-k)|fhat(A)|. Take logarithms, multiply by p_f(A), sum, and use H=sum p log2(1/u)+B_can to obtain the displayed inequality. No FEI assumption is used. In particular H <= 2I+2B_can. Conversely B_can<=H because u_f(A)<=1, so finiteness of a universal B_can/I bound is equivalent to finiteness of the FEI constant, though the constants need not coincide.

## 2. Exact balanced-block composition theorem

Let F be any Boolean function on m inputs. For each i let g_i be a balanced Boolean function on a nonempty input block; the blocks are pairwise disjoint. Define f=F(g_1,...,g_m). Then

B_can(f) = B_can(F) + sum_i Inf_i(F) B_can(g_i).                 (2.1)

The corresponding entropy and influence identities are

H(f) = H(F) + sum_i Inf_i(F) H(g_i),                            (2.2)
I(f) = sum_i Inf_i(F) I(g_i).                                  (2.3)

### Proof

Decompose a spectral subset S of all input coordinates as S=(T_1,...,T_m), and let J={i:T_i is nonempty}. Balance means ghat_i(empty)=0. Expanding F in its Walsh basis therefore gives the unique factorization

p_f(S) = p_F(J) product_{i in J} p_{g_i}(T_i).

For the upper mass, an outer support K may be any superset of J. In each additional block i in K\J the total nonempty inner spectral mass is 1; in each active block i in J, summing over supersets of T_i gives u_{g_i}(T_i). Consequently

u_f(S) = u_F(J) product_{i in J} u_{g_i}(T_i).

For a positive atom, divide these two equalities and take the logarithm. Summing with its probability weight gives (2.1): each inner term is included with probability P(i in J)=Inf_i(F). The same factorization gives (2.2) by the entropy chain rule. Taking expected support sizes gives (2.3). This also covers J=empty, since both upper masses at the empty set are 1. Zero atoms contribute zero. The proof requires balanced inner functions and disjoint blocks; it does not assert the same formula for biased inner functions or shared variables.

## 3. Amplification and an exact reformulation of the cancellation constant

Let g be balanced with i=I(g)>1, h=H(g), and b=B_can(g). Put F_0=x and recursively F_{r+1}=g(F_r,...,F_r), with a fresh disjoint copy for every input. Induction from (2.1)-(2.3) gives

I(F_r)=i^r,
H(F_r)=h (i^r-1)/(i-1),
B_can(F_r)=b (i^r-1)/(i-1).

Every F_r is a finite balanced Boolean function. Thus

H(F_r)/I(F_r) -> h/(i-1),
B_can(F_r)/I(F_r) -> b/(i-1).

In fact

sup_{nonconstant Boolean f} B_can(f)/I(f)
 = sup_{balanced Boolean g, I(g)>1} B_can(g)/(I(g)-1).           (3.1)

One direction is the preceding amplification. For the other, given a nonconstant f, use the balanced lift g(x,z)=z f(x). Its spectrum is the spectrum of f with a new coordinate adjoined to every support. Therefore B_can(g)=B_can(f) and I(g)=I(f)+1, proving the reverse inequality. The analogous entropy identity gives the familiar FEI amplification. No numerical limiting argument is needed to infer a finite counterexample: the exact finite-r formulas suffice.

## 4. External seed, independently recovered

The seed is Numaro's July 22, 2026 balanced monotone 18-variable construction, developed from the earlier Mosaic Intelligence 17-variable example. Attribution and primary sources:

- https://teorth.github.io/optimizationproblems/constants/71a.html
- https://github.com/teorth/optimizationproblems/pull/130 (merged August 2, 2026)
- https://numaro.tech/research/fourier-entropy-influence-2026/
- https://numaro.tech/assets/research/fei/check_c71_n18.py
- O'Donnell-Tan composition/amplification: arXiv:1304.1347; Hod's earlier lower bound: arXiv:1711.00762.

The external verifier was read as source data, not executed. Ten 512-bit truth-table slices were extracted: the all-zero auxiliary slice and the nine one-hot auxiliary slices. They determine nine disjoint two-cell hosts over a nine-bit core. The independently written reconstruction regenerates all 262,144 values and accepts the host representation only after matching the published full-table SHA-256:

f8a7bb2c738d86368305111633376b1a3a83d8ee1f1abcc9a37d841b0f9c7839.

The digest is over the comma-joined decimal +/-1 values in increasing binary input order. See external_seed_recovery.json for the compact core mask and exact host coordinates.

Exact checks in this invocation:

- Sum of all Boolean values: 0 (balanced).
- Monotonicity violations: 0 over all 2,359,296 coordinate edges, with true represented by -1.
- Parseval identity checked with integer Walsh coefficients.
- Influence from edge-boundary counting and Fourier weights agrees exactly: I(g)=261/128.
- Nonzero Fourier coefficients: 2,770.

Independent rational enclosures, outward rounded here:

6.776605309005978082519790221891882314787235038
 <= H(g) <=
6.776605309005978082519790221891882314787235039;

2.414776044569781426105693601659421954528425002
 <= B_can(g) <=
2.414776044569781426105693601659421954528425003.

The resulting H/(I-1) enclosure reproduces the external lower bound:

6.521845710923046575658143972948578468366662292
 <= H(g)/(I(g)-1) <=
6.521845710923046575658143972948578468366662293.

The cancellation amplification yields

2.323994990262646786026532188063203084057431581
 <= B_can(g)/(I(g)-1) <=
2.323994990262646786026532188063203084057431582.

Therefore the full-FEI target 6.4547837 is already too small, and a universal cancellation bound must allow at least the latter constant. This correction does not claim that either lower bound is optimal.

## 5. A concrete finite counterexample to the proposed sharp auxiliary lemma

Take r=5 in the recursion of section 3. This gives an explicit recursive Boolean function on 18^5=1,889,568 independent input bits; its enormous truth table need not be expanded. Its exact influence is

I(F_5)=1211162837301/34359738368.

By (3.1)'s finite-r formulas and the rational entropy certificate,

2.258065077806026101650608838715068071504635245
 <= B_can(F_5)/I(F_5) <=
2.258065077806026101650608838715068071504635246.

This is strictly greater than 2.2273918583 by more than

0.030673219506026101650608838715068071504635245.

Hence B_can(f)<=2.2273918583 I(f) for every Boolean f is REFUTED. In particular it refutes the earlier smaller beta(1/2)/2-1 target. The witness remains Boolean and balanced at every level; it is not an abstract non-Boolean spectral law.

For clarity, its H(F_5)/I(F_5) lies between
6.336826070786839252084118443363073574539277042 and
6.336826070786839252084118443363073574539277043.
This particular finite witness is not even above the known amplified FEI lower bound. It refutes the auxiliary cancellation constant, NOT the existence of a finite full-FEI constant.

A method that uses only H<=2I+2B_can followed by B_can<=cI cannot produce an upper constant smaller than 2+2c, and our lower bound forces c>=2.32399499026264678602. Such a method cannot reach below approximately 6.64798998 without additional information or a sharper reduction. This is a limitation of that proof strategy, not an upper bound on FEI.

## 6. Constant-size disjoint AND/OR recurrences

These support further numerical exploration without materializing truth tables. Use true=-1. For disjoint Boolean a,b put p=P(a=-1), q=P(b=-1), V_a=4p(1-p), V_b=4q(1-q), and phi(t)=-t log2 t with phi(0)=0. Remove the empty atom:

E_a=H(a)-phi((1-2p)^2),
T_a=B_can(a)-phi((1-2p)^2),

and similarly for b. Let

R=q^2 V_a log2(1/q)+p^2 V_b log2(1/p),

with continuous endpoint conventions. For f=AND(a,b)=(1+a+b-ab)/2,

P(f=-1)=pq,
I(f)=qI(a)+pI(b),
E_f=qE_a+pE_b+2R+V_a V_b/2,
T_f=qT_a+pT_b+R.                                             (6.1)

Negating a Boolean function leaves H,I,B_can unchanged and replaces p by 1-p, so OR follows by De Morgan.

Proof: a nonempty spectral atom supported only in a's block has mass q^2 p_a(A), and upper mass q u_a(A); exchange a,b for the other single-block case. An atom meeting both blocks has mass p_a(A)p_b(B)/4 and upper mass u_a(A)u_b(B)/4. Sum the entropy and logarithmic upper-mass ratios over these three disjoint cases. Since q^2+V_b/4=q and p^2+V_a/4=p, the coefficients reduce exactly to (6.1). The mixed entropy contributes V_a V_b/2, while the scaling factors cancel from its cancellation ratio.

Finite regression evidence: 360 random disjoint formulas in dimensions 2 through 12 matched the recurrences with exact integer probabilities/influences and maximum float64 H/B errors below 2.7e-15/8.9e-16. A separate 100-test arbitrary-outer/balanced-inner composition check matched (2.1)-(2.3) on nine input bits, with maximum H/B errors below 8.9e-16/4.5e-16 and exactly matching influences. These are regression tests, not substitutes for the algebraic proofs above.

## 7. Rigorous numerical method and reproduction

Run, in this directory:

python reconstruct_external_seed.py
python test_balanced_composition.py
python rational_entropy_certificate.py
python explore_edge_grafts.py

Requirements: Python and NumPy; the rigorous logarithm routine uses only fractions.Fraction and integer arithmetic after the integer Walsh transform. No external network, model API, secret key or private corpus is required.

For a positive rational x, reduce x=2^e m with 1<=m<2 and put z=(m-1)/(m+1). Then 0<=z<1/3 and

ln m = 2 sum_{k=0}^{N-1} z^(2k+1)/(2k+1) + R_N,
0<=R_N<=2 z^(2N+1)/((2N+1)(1-z^2)).

Use the same rational enclosure for ln2, divide outward, and take N=80. Negative logarithms are handled by reciprocation and reversed endpoints. Entropy and cancellation sums group identical integer Walsh-square/upset-square pairs before evaluation. Every strict inequality above is a comparison of rational endpoints, not a decimal-string or floating-point comparison. Reported decimal endpoints are integer floor/ceiling conversions. The JSON width is an upward-rounded bound, not an assertion that the interval width equals that display value.

For this n=18 seed, Walsh squares, upper-zeta sums and Parseval fit safely in signed 64-bit integers. The implementation does not authorize arbitrarily large explicit int64 transforms without a new overflow check. Formula recurrences should use arbitrary precision when biases approach 0 or 1; float64 exploration can lose a tiny bias and must not be called an exact constant function.

## 8. Failed new search retained, and next constructive step

An exploratory new graft replaced one of the nine auxiliary dictators on a middle-layer core edge by majority-of-three of the edge coordinate and two fresh auxiliary bits. All nine single-edge trials gave the same lower amplified score, approximately 6.50929460118, rather than the seed's 6.52184571092. These are unsuccessful float64-ranked trials, not a theorem that every graft or every larger construction fails. The code and all nine trial records are retained in explore_edge_grafts.py and edge_graft_exploration.json.

Next useful work: exploit the balanced-block identity to test genuinely different seed families against B_can/(I-1), rather than repeatedly checking small dimensions; develop a weaker summable Boolean cancellation payment with c above the certified obstruction; and test biased or joint edge gadgets in the compressed core representation before certifying any improved witness. Separately, improve the unfinished read-once region-2 enclosure while retaining its restricted scope. The remaining universal mathematical gap is still a dimension-independent upper bound, not a missing numerical decimal.
