# Joint stopping credit after a paid negative terminal

All entropy is in bits. h is negative on{0,1,2,4,8,16,32,6,17,40}, and J(x)=-h(x xor1). Let g on six physical bits be negative on{0,1,2}. Retain the entire actual Boolean F_plus=J(-1,+1,g,g,g,g) with rate K=4 and S=4I-H. Its supplied original credit is A0=-S(F_plus)>0. The original outside donor expenditure, booked donor balance, other stopped full terminals and parked2tau account are fixed.

## Exact joint result already checked

Fix ANY pair of the four remaining physical cores. For all adaptive physical-coordinate reveal orders and all stopping decisions restricted to those two cores, the sharp minimum conserved incoming credit is EXACTLY A0. This is equality of canonical prime-log profiles, not overlapping intervals. The supplied credit can fund all such histories with ZERO new outside transfer. All real initial old net debits D>=0 are covered by incoming credit A0+D. Signed individual old debit labels remain present; total net debit remains nonnegative. This is a statement about the specified finite Boolean family, not arbitrary cores or full FEI.

The three pair-orbit representatives are{2,4},{3,5},{2,3}. Literal outer swaps2<->4 and3<->5 are checked on all16 supported outer assignments. Each single core has twelve canonical restriction profiles, obtained by deleting only pointwise irrelevant physical inputs. All729 labelled restrictions and1458 available labelled query rows are checked against that DAG. Their Cartesian product therefore covers all3^12 labelled two-core restrictions and EVERY allowed physical query, including arbitrary interleavings. No affine variable mixing or unproved symmetry quotient occurs. Every physical non-dummy outcome keeps its true weight1/2; dummy deletion introduces no conditioning or reach charge.

For each pair the certificate has144 states and840 query rows. The three joint roots have R=A0 exactly. The implementation directly checks all Bellman upper bounds and a maximizing stopping-policy lower bound. Its408 distinct full profiles are retained, including full constant boundaries if they occur. The untouched two complete cores are never dropped. Source-inherited-prefix compatibility is checked separately in PREFIX_VALIDATION.json; this root result by itself would not license retroactive reallocation of already assigned credit.

## Continuum account theorem and sharpness

For any finite physical restriction DAG, define

    R(v)=max(0,-S(v),max_allowed_query mean R(child)).

Credit a is nonnegative, old total net debit is D=S+a>=0, and a zero-new-flow continuation preserves the conditional mean of supplied credit. The exact necessary and sufficient condition for ALL allowed adaptive query/stop policies is a>=R(v).

Necessity follows by finite induction. Stopping requires a>=max(0,-S). Each possible next query must allocate child credit at least their R values, so a>=mean R(child). For sufficiency, choose any allowed query, put r=mean R(child), and set

    a_child=R(child)+(a-r), d_child=S(child)+a_child.

Since a>=R(v)>=r, these are nonnegative. The child credits average to a. Exact physical influence telescoping yields mean S_child=S+e, e=Delta H-4Inf_query, so mean d_child=D+e. No donor is renewed. Recurse finitely; each child credit is at least its own requirement.

Each nonnegative original credit-owner label is transported with kernel a_child/a when a>0; if a=0 all credits vanish. All signed old debit labels and the new signed query label e are transported with kernel d_child/T for T=D+e>0. Their means remain their old values and sums are the actual d_child. If T=0, both nonnegative child debits vanish; kernel1 preserves each signed label, whose total then equals0 pointwise. No zero denominator is canceled. Negative e is allowed; assuming it positive would discard actual refunds. Every outside donor's outgoing flow and booked balance remain unchanged.

All-real coverage follows algebraically: raising initial credit by any real b>=0 raises every child credit under this rule by exactly b, through every descendant; full debit rises by the same b. Thus the EXACT computed lower threshold covers the entire half-line, in particular every compact interval above it, without a credit grid. The attainable zero extra-funding threshold includes its boundary.

Sharpness is also finite induction: R equals the maximum expected terminal payoff max(0,-S_terminal). A maximizing query and the independently maximizing policies on its two children attain its mean. Stopping is an allowed action and cannot be omitted. The certificate's selected-policy DAG retains true reach weights and verifies their terminal sum1 and expected payoffR exactly.

## Arbitrary real weights and their boundary faces

The continuum account theorem holds unchanged for ANY finite conditional weights w_b>=0 summing1: replace every mean by sum_b w_b times its argument, and use only the positive-weight support. Necessity, sufficiency, sharpness, and the affine initial-credit shift use finite linear identities only. At a zero-weight face, remove unreachable outcomes before checking pointwise accounts; no expression divides by w_b. All physical applications in this run use weights1/2, so this algebraic generalization is not a claim about biased-cube physical influences.

In particular, for two supplied child requirements R0,R1, the whole real region0<=w<=1,a>=max(0,-S_parent,wR0+(1-w)R1) is certified, including the two boundary faces w=0,1 and the threshold equality. Any compact subset of that epigraph is covered. This is an analytic continuum reduction, not a sampling of weights or credits. If a=0, all positive-weight child credits vanish. If T=0, all positive-weight child net debits vanish and the kernel1 convention preserves even nonzero canceling signed labels. Scalar guards explicitly exercise these cases and show why nonnegative/normalized weights and the stop option are needed; the scalar data are accounting controls, not Boolean witnesses.

## Exact spectra and arithmetic

The reduced actual four-input gate is k(z)=-h(0,0,z2,z3,z4,z5). Each core's integer FWHT is checked against direct character sums, integer inversion, Parseval and physical edge counts. For core means mu_j, a tensor Taylor transform gives coefficients c_T in the centered basis product(y_j-mu_j). Occupied-sector masses are c_T^2 product_(j in T)(1-mu_j^2). A separate direct weighted centered-moment calculation reproduces EVERY mass, with positive-variance denominators only. Pivotal probabilities are independently counted under the exact product law, and the outer inverse is checked at all16 sign assignments, even outside deterministic support.

Given complete core entropies, the exact chain rule is

    H(F)=H(P_occupied)+sum_j q_j[H(g_j)-h2(Var(g_j))],
    I(F)=sum_j q_j I(g_j).

It follows by conditioning each occupied block on its nonempty spectrum, whose entropy is[H(g_j)-h2(Var(g_j))]/Var(g_j), with occupancy q_j Var(g_j). At zero variance that occupied sector has mass0 and contributes0; no zero division occurs. This retains all untouched core terminal entropies, rather than treating them as new available reserve.

All entropy expressions are represented as exact rational linear forms in log2(prime), with log2(2)=1. Packet log factors are expanded from their exact Taylor amplitude and variance factors before factoring; no giant full spectrum is enumerated. Symbolic equalities are exact coefficient equality in this representation. Unequal Bellman candidates are separated using outward192-bit80-term atanh logarithm bounds with a proved geometric tail. No floating comparison chooses a maximizing action. Every comparison must either have a strict certified sign or exact profile equality; an unresolved comparison aborts.

## Actual inherited prefixes: no retroactive reassignment

Let R1(t) be the original one-core hull and R2(t,u) the new two-core hull. A072's original allocation at a one-core query t->t_b is

    a_b=R1(t_b)+a-mean R1(t_b).                       (5)

Our independent one-core recursion exactly matches all24 source prime-log S/R profiles, covering both source orbits. Thus(5) is the actual previously authorized source rule, rather than a new preallocation chosen to fit the joint result.

For each ordered pair define m(t) as the minimum actual incoming credit over all one-core physical histories reaching canonical t under(5), starting at a=A0. The root value is m(g)=A0. Process the finite DAG in decreasing dimension. For every action t->c_b update

    m(c_b) = min over incoming edges of
             [R1(c_b)+m(t)-mean R1(c)].              (6)

Each edge formula has coefficient+1 in its incoming credit. Therefore the minimum at a parent supplies the minimum on that edge. Taking the finite minimum over all predecessors proves(6) by induction, with an actual attaining original-coordinate history retained. Dummy queries preserve both full function and credit and are removable. No assumption of independence of previously selected actions is used: the recursion covers every positive-reach history, including choices based on earlier answers.

The exact required extra initial old-debit threshold for retaining(5) through ANY source prefix and then enabling the joint policy is

    B=max_t [R2(t,g)-m(t)]_+ .                       (7)

The code computes all12 cuts for both choices of the first core in each of the three pair types,72 cuts total. Every B is EXACTLY0 in canonical prime-log arithmetic. Hence EVERY credit actually allocated by the original source rule is already at least the new joint requirement. There is no retrospective reallocation, external draw, or reuse of the already spent donor. The second core may be chosen based on the prefix answers, since all possible choices satisfy the inequality simultaneously. After enabling it, use the joint rule from the continuum theorem; any later adaptive interleaving/stopping within those two cores is covered.

For any supplied real initial old debit D>=0, incoming credit is A0+D. Formula(5) shifts every actual descendant credit by EXACTLY D; its minimum becomes m(t)+D. Thus(7) proves the entire real parameter region D in[0,infinity), including D=0, not just finitely many numerical allocations. Source leaves with positive old debit retain all their signed old labels via the debit kernel, and each existing credit-owner label via its own mean-one credit kernel. These additional credits are assumed ALREADY supplied with that source leaf; the theorem does not create them.

As falsification controls: omitting the stop option underprices a state with S=-1 and a sole next query to positive-capacity children; dropping conservation permits free credit creation; dropping nonnegativity permits credits(-1,1) to average0 without funding a negative child. If no extra credit is available, the sharpness argument forbids replacing R2 by only the current deficit. The full threshold test, not the number of sampled orders, certifies all-policy coverage.

## Hardest check and remaining gap

The nontrivial finite upper bound is R(F_plus)=A0 simultaneously for all three pair types and every state/query row, not simply a first-query test. The certificate checks those rows independently of the original A072 single-core implementation. Compatibility with credit already allocated after arbitrary source one-core histories also PASSES at every one of the72 cuts with exact extra threshold0. Unrestricted third/fourth-core histories and arbitrary Boolean core admission remain unproved. A dimension-independent bound on the FULL physical hull would be equivalent to FEI; no such bound is asserted here.
