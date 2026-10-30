# A042 bias endpoint certificates

## exact target, quantifiers, hypotheses and units

For every fixed finite Boolean sign table f on independent Bernoulli inputs, derive the boundary extension and symbolic expansions of corrected entropy Hplus and spectral deficit D=I-Var. No threshold hypothesis is needed for these identities. Contract coordinates with input probability zero or one before forming an orthonormal basis or dividing by D. Natural corrected entropy is E=(ln 2) Hplus. Influence here is spectral I=sum |S| P(S), not unweighted physical pivotal probability. The target G-BIASED-LTF / C025 remains open in arbitrary arity. This packet supplies a boundary interface, not that theorem.

## sources actually read, revisions and theorem locators

Read EXECUTION_PROTOCOL.json in full, revision 2026-10-11-execution-v2, and campaign README, CURRENT_STATUS, claim/obstruction registries, A042 packet status, STREAM_NEXT_ACTIONS and the A041/A042 and weighted-control portions of FEI_100_agent_research_plan.tex. Read BOARD.md at stage start (snapshot 2026-10-11 21:55 UTC). The requested claude/B09/STREAM_NOTES.md is absent; canonical B09 next actions govern. A046's board entry already covers the restriction-tax lower bound, so this packet does not duplicate it.

Read the supplement CAMPAIGN, CLAIMS, COUNTEREXAMPLES, NATIVE_MAPPING, and seed interfaces; relevant source notes include ROUTE_MAP_CURATED, with full-Booleanity and composition scope guards. The mathematical primary source used for the three threshold controls is reports/fei-2026-10-11/source_material/reductions/paper/biased.tex: labels biasfull:hplus, biasfull:composition, biasfull:mixture, biasfull:weightedcounter, biasfull:andmany and biasfull:localTC. These controls are recovered results, not new discoveries. Its complete text was read. Earlier B09 REPORT.md sections 0--3 were read for normalization and to avoid adopting its stronger tax-necessity claim; no uncertainty theorem from that report is used as a proof dependency.

The supplied threshold_paper_38pp.txt Section 6.1 defines corrected entropy and deficit; Section 7 gives disjoint composition. The earlier threshold version's introduction was compared for scope. The percolation papers' introductions/Section 1.1 were compared: their I is unweighted pivotal expectation and J is spectral influence under nonuniform bias. Neither paper's percolation theorem is invoked here. No new literature priority assertion is made. Source hashes and exact inspection scope are recorded in out/SOURCE_RECEIPTS.json; reading a file mechanically is not an audit of every theorem in it.

## complete derivation or exact first unsupported line

### 1. Polynomial coordinates remove all apparent boundary singularities

For S define w_S=prod_{i in S}4p_i(1-p_i) and

    c_S(p)=2^(-|S|) E_{p outside S}[ Delta_S f ],

where Delta_i f=f(x_i=1)-f(x_i=0), and c_empty=E f. Integration of each selected coordinate gives fhat_p(S)=sqrt(w_S)c_S(p). The polynomial c_S is independent of p_i for i in S; |c_S|<=1 because |Delta_S f|<=2^|S|. Thus

    P(S)=w_S c_S^2,
    E(f)=sum_{S nonempty} w_S c_S^2 ln(1/c_S^2),
    D(f)=sum_{|S|>=2} (|S|-1) w_S c_S^2.                 (1)

Use x ln(1/x)=0 at x=0. Formula (1) extends continuously to the closed bias cube. Any S intersecting a deterministic coordinate has w_S=0, while coefficients on the remaining coordinates are those of the actual restricted Boolean table. This proves path-independent contraction and transfers any fixed-arity inequality E<=C_nat D on the entire interior to its boundary. It does not bound the ratio at a boundary point with D=0 merely by continuity.

More precisely, along a fixed real-analytic one-parameter path into an endpoint, write a nonzero atom as w_S(t)=W_S t^r(1+O(t)), c_S(t)=b_S t^s(1+O(t)), W_S>0, b_S nonzero, r,s nonnegative integers. Then

    P(S)=W_S b_S^2 t^(r+2s)(1+O(t)),
    E_S=W_S b_S^2 t^(r+2s)[2s ln(1/t)-ln(b_S^2)]
         +O(t^(r+2s+1)(1+ln(1/t))).                    (2)

The same P(S) multiplied by |S|-1 supplies its deficit term. When r=0 the O(t) formulation still follows from analyticity. Identically zero atoms contribute zero. For c_S identically of magnitude one, E_S is identically zero. All logarithms in (2) arise from a vanishing normalized c_S, not from the boundary factor w_S. Summing this finite list gives an algorithm for symbolic leading orders along any such path. Formula (2) is fixed-table/path asymptotics, not an arity-uniform remainder or an assertion for nonanalytic paths. Arbitrary paths still have the continuity statement (1).

### 2. One rare coordinate: exact polynomial deficit and entropy expansion

Fix all remaining biases strictly inside (0,1). Let the rare coordinate X have P(X=1)=e, f(0,y)=g(y), f(1,y)=h(y). Use a_T=ghat(T), b_T=hhat(T)-ghat(T), and w_T for the remaining-coordinate normalization. Then exactly

    fhat(T)=a_T+e b_T,
    fhat(T union {X})=sqrt(e(1-e)) b_T.                (3)

Consequently, with D0=D(g),

    D(f)=D0+e L-e^2 Q,
    L=2 sum_{T nonempty} (|T|-1)a_T b_T
        +sum_T |T|b_T^2,
    Q=sum_{T nonempty} b_T^2.                        (4)

The reduction of the quadratic coefficient to -Q includes the empty packet correctly: its coefficient in both degree sums is zero. This identity holds for every e in [0,1]. It also follows without radicals by replacing a_T b_T with w_T c_g(T)(c_h(T)-c_g(T)).

The entropy identity is

    E(f)=sum_{T nonempty} (a_T+e b_T)^2
              ln[w_T/(a_T+e b_T)^2]
         +e(1-e) sum_T b_T^2 ln[4w_T/b_T^2].          (5)

Zero b terms are omitted. The bound |b_T|<=2sqrt(w_T) ensures every log in the second sum is nonnegative. The factor 4e(1-e) in w_{T union X} cancels exactly with the factor e(1-e) in P; the empty T in this second sum must not be discarded.

Define

    K=2 sum_{T nonempty,a_T!=0} a_T b_T
                      (ln[w_T/a_T^2]-1)
          +sum_T b_T^2 ln[4w_T/b_T^2],
    Z=sum_{T nonempty,a_T=0} b_T^2.

For each fixed table and remaining bias vector, Taylor expansion of u^2 ln(w/u^2) at u=a_T!=0, and exact evaluation at u=e b_T for a_T=0, give

    E(f)=E(g)+e K+2 e^2 Z ln(1/e)+O(e^2).            (6)

No first-order e ln(1/e) term occurs. Constants in O(e^2) depend on the fixed spectra and biases and are not uniform when a nonzero a_T approaches zero. For p_X tending to one, exchange g and h and set e=1-p_X. Equations (3)--(6) give the requested zero/one endpoint expansion.

### 3. Zero deficit and unit-atom endpoints

At an interior bias, D=0 means all degree>=2 Fourier coefficients vanish. Hence f is affine in the bits. In the unique multilinear expansion of f^2=1, the coefficient of x_i x_j is twice the product of the two affine slopes. At most one slope is nonzero. A nonconstant affine Boolean function on two values is a signed literal. Thus D=0 iff f is constant or a signed literal; both have E=0 by (1). This proof uses the full truth table, made available by interior probabilities.

If D0=0 and L=0 in (4), nonnegativity of D(f) for e>0 forces Q=0. It follows that D(f)=0 for all e and E(f)=0. There is no permissible division by that zero polynomial. If D0=0 and L>0, (6) gives the finite limit

    lim_{e->0} Hplus(f)/D(f)=K/[(ln 2)L].             (7)

K>=0 follows from E(g)=0, E(f)>=0 and (6). The limit is conditional on this particular fixed-table slice; (7) does not supply a uniform bound over growing arity or varying remaining biases. If D0>0 the ordinary continuous ratio tends to Hplus(g)/D(g). These exhaust the possibilities, since D0=0 and L<0 contradicts (4).

For a unit spectral atom P(U)=1 on the contracted interior cube, Parseval implies f=+/-phi_U pointwise. Since |f|=1 and the coordinates have full independent support, varying any one coordinate in U shows that its two phi_i magnitudes must agree; this forces p_i=1/2. Hence f is a signed parity on fair coordinates U (irrelevant coordinates may have any bias). E=0 and D=|U|-1 for U nonempty. U empty gives a constant and D=0. In particular a unit singleton atom is a fair dictator; a higher-degree unit atom is not a zero-deficit endpoint. Its neighboring slice obeys (4)--(6) with D0=|U|-1. At a deterministic endpoint the assertion is made only after contraction; the unreduced basis is undefined there.

### 4. All three weighted-threshold guards and their order of limits

Write r=q^m, a=q0, z=1-a, A={X0=1} union {X0=0, all light bits=1}, f=2 1_A-1, alpha=a+zr. The source's mixture parameter is eta=P(X0=0 | A), giving a=(1-eta)r/[eta+(1-eta)r]. The exact spectrum is

    P(empty)=(2alpha-1)^2,
    P({0})=4az(1-r)^2,
    P(T)=4z^2 r^2 [(1-q)/q]^k              (T light, k>=1),
    P({0} union T)=4az r^2 [(1-q)/q]^k     (T light, k>=1).

There are binom(m,k) light subsets of size k. This is an actual Boolean weighted threshold with weights m,1,...,1. Its influences are I0=4az(1-r), sum_light Ij=4mzr(1-q), and V=4alpha(1-alpha).

For the sign conjunction g of the light variables, binomial summation gives exactly

    Dg=4r[m(1-q)-1+r],
    Hplus(g)=2Dg+8mr(q-r) log2(1/q).                  (8)

The outer two-bit OR on probabilities a,r has

    Do=4ar z(1-r),
    Hplus_o=8az(1-r)^2 log2[1/(1-r)]
             +8r(1-r)z^2 log2(1/z)+8ar z(1-r).

Direct coefficient summation, or exact disjoint composition, gives

    D(f)=Do+z Dg,    Hplus(f)=Hplus_o+z Hplus(g).     (9)

Using -ln(1-u)<=u/(1-u) proves Hplus_o<=(2+4/ln2)Do. Thus (8)--(9) keep all charges without estimating raw entropy or dividing a deterministic child variance.

Growing arity regime: m>=2, q=m^(-2), eta=1/m, d=1+(m-1)r. Then a=(m-1)r/d, alpha=mr/d, and I/(4alpha)=2-1/m-q-a. The exact conditional law has

    TC(Q)=m h(1/m+(1-1/m)q)-(m-1)h(q)              (nats).

The estimate h(u)=u ln(1/u)+u+O(u^2), uniformly for 0<u<=1/2, gives TC(Q)=ln m+1+O((ln m)/m). Consequently

    alpha TC(Q)/I=(ln m+1)/8+O((ln m)/m).            (10)

For the coefficient-one pivotal credit, rho0=1-r, rho_light=z q^(m-1), and both logarithm arguments exceed one for m>=2. They are (1-r)/[alpha(1-alpha)] and m/(1-alpha). Set Lalpha=ln(1/alpha)=2m ln m-ln m+ln d. The residual R divided by 4alpha is exactly

    (1-alpha)[Lalpha-ln4-ln(1-alpha)]
       -(1-1/m-a)[Lalpha+ln(1-r)-ln(1-alpha)]
       -(1-q)[ln m-ln(1-alpha)].                    (11)

Since r=m^(-2m), all r Lalpha, a Lalpha and alpha Lalpha terms vanish faster than (ln m)/m. Equation (11) is ln m-ln4+O((ln m)/m). Dividing by I/(4alpha) yields

    R/I=(1/2)ln m-ln2+O((ln m)/m).                  (12)

This refutes the credit multiplier one, and changing the fixed factor inside the logarithm contributes only O(I). It makes no claim that all larger multipliers fail.

Meanwhile Do/Dg=O(r), and the extra term in (8), divided by Dg, is O((ln m)/m^2). Equations (8)--(9) give the explicit dimension-varying bound

    Hplus(f)/D(f)=2+O((ln m)/m^2)+O(r) ->2.          (13)

The constants here can be absolute for m>=2, since m(1-q)-1+r>=m/4 and a<=mr. This establishes the growing-arity limit separately rather than misusing the fixed-m series (6).

Third guard, a different limit: fix m>=1 and eta=1/2, then let q->0, with a=r/(1+r). Q tends to the equal mixture of the complementary deterministic vectors (1,0,...,0) and (0,1,...,1). For every distinct pair j,k, I_Q(Xj;Xk)->ln2 by finite-law entropy continuity. Also I0/alpha=2(1-r)/(1+r)->2, and each Ij/alpha=2(1-q)->2. Therefore for every coordinate

    alpha sum_{k!=j} I_Q(Xj;Xk)/Ij -> m ln2/2.      (14)

First take q->0 with fixed m; only then let m grow. No uniform-in-m small-q remainder is asserted. This concerns conditional physical input TC, not spectral erasure. For m>=2, (8)--(9) also give Hplus/D->2 in this fixed-m regime; m=1 is exceptional and has limit 2+4/ln2, as follows directly from the two-bit OR formula. Recording this exception prevents a spurious all-m assertion.

The first unsupported step toward the global target would be inferring an arity-uniform weighted-threshold FEI+ constant from the fixed-table slice coefficient K/L or from these particular guards. No such inference is made.

## executed validation with domain, arithmetic, commands and outputs

Frozen before computation: out/FROZEN_SPEC.json. Executed `python -X utf8 code/check_endpoints.py` from this run (or with its full relative path from the agent root). The standard-library Fraction checker exhausts every sign truth table on n=1,2,3, each distinguished coordinate, remaining rational biases alternating 1/3 and 2/5, and rare bias 1/7 or 6/7: 1,608 fixtures without symmetry reduction. It checks mixed-difference spectra, normalization, (3)--(4), coefficient bounds, zero-deficit classification, and all fair-input unit atoms. It separately compares direct Boolean spectra to the compressed weighted formula for m=1..5, and certifies six weighted finite ratios for m=2,3,4,8,16,32 using rational log enclosures. Result: 24,095 assertions passed, 80 zero-deficit slice fixtures and 28 fair-input unit atoms, measured computation 2.792 seconds. Estimated memory below 80 MB; no heavy search or memok threshold was approached.

For log x, range-reduce x=2^k u with 1<=u<2 and use z=(u-1)/(u+1). The first N=28 terms of 2 sum z^(2h+1)/(2h+1) are a lower bound; the omitted positive tail is at most 2z^(2N+1)/[(2N+1)(1-z^2)]. Negative k uses swapped ln2 endpoints. Signed scaling swaps endpoints, division considers all four rational corner quotients, and outputs are rounded outward to rational multiples of 10^(-10). These enclosures are finite certificates, while the proofs above establish all-parameter limits. CHECK_OUTPUT.json stores the exact outward rational bounds.

## proof dependencies and changed downstream conclusions

The new endpoint proof uses elementary mixed-difference integration, Parseval, Taylor expansion and Boolean f^2=1. The weighted controls reproduce the recovered biased.tex identities and their consequences; they do not adopt the B09 uncertainty claim or its disputed tax optimality. Exact disjoint composition can be replaced by the displayed direct spectra throughout (8)--(9). The symbolic interface lets A041/A044/A045/A084 contract deterministic inputs and certify removable first-order logarithms without invalid 0/0 division. It does not turn physical TC or coefficient-one pivotal credits into valid replacements. No campaign registry was modified and no full-FEI conclusion changed.

## one next mathematical action and independent reviewer

Ask A090 and A091 to reconstruct (5)--(7) and the simultaneous-endpoint mixed-difference formula, paying special attention to empty packets and the m=1 exception. The next mathematical action is to compare K/[(ln2)L] over zero-deficit slices of weighted thresholds while other biases also degenerate, using (1)--(2) to identify every competing leading monomial. A dimension-independent bound for that joint regime, rather than a fixed-bias limit, is the useful missing boundary lemma for A041.

## actual persistence receipts or precise save blocker

All artifacts are saved inside A042 only: REPORT.md, BIASED_ENDPOINT_SERIES.tex, WEIGHTED_CONTROL_LIMITS.json, CLAIMS.json, PROGRESS.json, PACKET_DELTA.json, code/check_endpoints.py, out/FROZEN_SPEC.json, out/CHECK_OUTPUT.json, and source/persistence receipts. STATUS.md, WORKLOG.md and LEARNED.md are maintained at the agent root. Independent review, supervisor copy, Brain ingestion, and mirror verification remain pending; no remote receipt is claimed. The only access issue is the absent lead-notes file; it did not block independent packet work.

**Universal bridge:** This stage moves C025 / G-BIASED-LTF, the canonical B09 replacement target, by supplying exact deterministic contraction, arbitrary analytic-path atom orders, and a finite zero-deficit slice ratio formula, while preserving all three normalization obstructions with correct units and order of limits. It leaves the dimension-independent bound for simultaneous degenerating biases and the weighted-threshold interior estimate unpaid. Comparing the joint leading monomials at a zero-deficit slice is the shortest next route because it tests the precise singular boundary that a composable all-arity gate inequality must survive; repeating another finite class or an already refuted physical-TC payment would not advance that interface.
