# Conserved selected-block accounts: independent reconstruction and exhaustive restriction boundary

All entropies are in bits. Binary one denotes a negative input. Let h be negative on {0,1,2,4,8,16,32,6,17,40}, J(x)=-h(x xor1), and g_n negative on {0,1,2}. Blocks are physically disjoint. Only block0 is queried; the other five complete cores remain present.

## 1. Actual Boolean realization and complete-domain claim

For n=6 the search family consists of all partial assignments t in {0,1,*}^6 to block0 of the actual function J(g_6^6). There are exactly729 tags. Summing the number of free bits gives6*3^5=1458 query tags. Each query has two genuine uniform children, of conditional reach1/2. This covers every node and edge of every adaptive tree that queries this block without repeating a bit, including constant-core nodes and dummy queries. It does not enumerate allocation policies, other queried blocks, or arbitrary Boolean functions. No symmetry quotient is used. Coordinate symmetries and constant/dummy duplicates remain in the census.

For arbitrary independent cores let p_l=P(g_l=-1), v_l=4p_l(1-p_l), and q_l be the actual outer pivotal probability. Expand J in the orthogonal centered-bit basis product(x_l-p_l). Orthogonality gives squared masses c_T^2 product_{l in T}p_l(1-p_l). In an occupied block, substitute the actual nonempty Fourier spectrum of g_l, normalized by its variance. Its total entropy contribution is q_l[H(g_l)-h2(v_l)]. Therefore, including constant cores by polynomial continuity,

H(F)=sum_l q_l H(g_l)+C(p), I(F)=sum_l q_l I(g_l),

C=H_p(J)-sum_l q_l h2(v_l).

The implementation obtains all centered coefficients by six two-point interpolation steps, and obtains each q_l independently by weighted edge enumeration. It checks Parseval and every actual inner influence by integer Walsh coefficients and physical edges. These identities concern the full composed function, not just the outer law.

Under a physical query in block0, q0 is unchanged and each other q_l averages affinely over the two child biases. Thus

DeltaH(F)=q0 DeltaH(core)+DeltaC, Inf_query(F)=q0 Inf_query(core).

The census checks the influence equality exactly on every edge; entropy interval residuals are diagnostics for this algebraic proof, not proofs of equality.

## 2. Independent review of A075's parameterized obstruction

Source: A075-COMPLETE-BLOCK-RATE4-OWNER-OBSTRUCTION@1, statement SHA256 4afac355602af67ca82513596cbeb08bde4c32580d92ffcbc4a72e891a592238. The source statement, hypotheses, version, hash, and contributors are preserved in the reviewed claim copy. No source executable code is imported or run.

Write p=3/2^n, C_p=C(p,...,p), C_+=C(0,p,...,p), C_-=C(1,p,...,p), and D=C_p-(1-p)C_+-p C_-. Every determining tree of the selected block has final core entropy and influence zero. Weighted physical influence telescoping gives q0 I(g_n), independently of query order; full entropy telescoping gives q0 H(g_n)+D. Hence the full signed cumulative rate-K excess is

e_K=D-q0[K I(g_n)-H(g_n)].

A selected-only account with no other-owner transfers must finish with nonnegative mean remaining balance. It cannot do so when e_K>0, even if negative query excesses refund the same account. A positive-excess-only convention cannot improve this necessary condition. This is a constraint on that account, not on every possible proof of FEI.

We independently build the192 exact squared-mass polynomials using centered-bit interpolation rather than the source uniform-Walsh reexpansion. Each q polynomial comes from direct outer edge enumeration. Formal logarithm coefficients are dictionaries of rational coefficients of log2(prime), log2(e), and log2(p). Polynomial identities and cancellation of log2(p) are checked exactly, rather than numerically fitted. The checked expansions are

D=(32+16log2(e))p^2+O(p^3(1+|log p|)),

C_-=(64-32log2(e))p^2+O(p^3(1+|log p|)),

q0=4p-14p^2+18p^3-10p^4+2p^5,

sum_{l>0}q_l(1,p,...,p)=16p-42p^2+36p^3-10p^4.

For completeness the parent correction has expansion C_p=(80-8log2(e))p^2+O(p^3(1+|log p|)), and sum_l q_l(p,...,p)=4-12p+26p^2-40p^3+30p^4-8p^5.

For any nonzero polynomial w=p^r(a+bp+cp^2+...), a>0, expand -w log2(w). Through degree2 its terms are obtained by the Taylor expansion of log(a+bp+...). For r=0 the quadratic coefficient includes -b^2 log2(e)/(2a); for r=1 the next coefficient is -b[log2(a)+log2(p)+log2(e)]; for r=2 only -a[log2(a)+2log2(p)] remains. Terms r>=3 are O(p^3(1+|log p|)). There are finitely many fixed polynomials and each leading coefficient is positive, so a common sufficiently small positive neighborhood and a finite remainder constant exist. This proves the stated asymptotic remainders without a numerical tail cutoff.

The actual core spectrum is (1-6/N)^2 once, 36/N^2 with multiplicity N/4-1, and4/N^2 with multiplicity3N/4. Its two special physical coordinates have influence2/N and the other n-2 have6/N. Hence I=(6n-8)/N. Independent expansion of that exact entropy formula gives

S4(g_n)=[6log2(3)-8/3-4log2(e)]p+O(n p^2).

Substitution proves exactly

e_4/p^2 -> 128/3-24log2(3)+32log2(e)>50.79,

S4(J(-1,g_n^5))/p^2 ->96log2(3)-320/3-32log2(e)<-0.6765.

Signs are certified by outward intervals. Thus both source eventual assertions hold with their unchanged quantifiers, without an explicit cutoff. The parent total influence is asymptotic to8np and its correction is O(p^2(1+|log p|)); the negative endpoint influence is asymptotic to32np^2. Since H(g_n)/I(g_n)->4, both complete H/I ratios tend to4. There is no FEI disproof.

All twelve source finite parameter values n=6..12,16,24,32,48,64 independently have positive parent S4, positive e4, and negative negative-endpoint S4. The specified order[2,0,1,3,4,5] has27 stopping-tree nodes and first negative full S4 at depth6. Its first two queries are in the exhaustive census. For any incoming debit d, B'-d-e2=(U_parent-d)-DeltaC2 follows directly by substituting e2=q0 DeltaH(core)-4q0 Inf+DeltaC2 and B'-U_parent=q0 DeltaH(core)-4q0 Inf. This retains the source debit once and verifies its no-renewal interpretation. Verdict: HOLDS at unchanged stated scope, without substantive repair.

## 3. Exhaustive finite boundary and exact counterexamples to proposed repairs

The729-state and1458-edge census gives the following rigorous enclosures; decimals here only label exact outward rational intervals saved in RESULTS.json:

* Max full-terminal H/I lies in(4.198,4.2), approximately4.198915754294231, attained at the selected negative constant (tag000000). In particular every complete restricted function satisfies H<(21/5)I.
* Max complete-selected-reveal required rate [q0 H(core)+D]/[q0 I(core)] over nonconstant selected cores lies in(5.47,5.48), approximately5.471866515118908, with witness tag**00**. All tags are stored; stars denote free physical bits. The bracket is for the exact finite maximum, not a universal constant.
* Max individual full physical query DeltaH/Inf lies in(6.29,6.3), approximately6.292913225302942, at tag**00**, querying physical coordinate0. Dummy queries have exact zero influence and entropy decrement and are excluded from this ratio.

The exact full selected reveal at the original root has e_(9/2)>0.0553. Therefore raising the selected-only rate from4 to9/2 does not repair this complete reveal. This does not rule out all larger rates, and was not asserted by A089 or A075.

At a node define M_K=sum_{l>0}q_l S_K(g_6)-C, the margin of the five OTHER complete core owners after paying the complete outer correction. There are76 negative M4 tags and23 negative M_(9/2) tags. The explicit tag00000* leaves a balanced one-bit selected core; its complete function has H<(9/2)I, but M_(9/2)<-1/10. Thus even a rate exceeding every complete terminal ratio in this family does not make the other owners alone sufficient to pay C, leaving the selected owner wholly unused. This refutes that proposed availability inference. It does not refute A089's conditional rule U=A-max(0,-M): that rule explicitly allows deduction from the selected owner and requires U>=0 to be checked. Nor does it establish failure of every signed transfer or allocation policy.

The frozen family directly targets hereditary unused-surplus eligibility through a real physical history. It retains positive and negative endpoints, duplicate tags, full core bills, and dummies. The finite maxima do not prove a uniform bound for arbitrary cores.

## 4. Honest remaining line

No universal FEI bound, C018 erasure bound, or complete C019 payment theorem is proved. What remains is a conserved allocation rule across block owners that pays positive inherited debit and DeltaC, covers the negative M nodes, and remains valid for arbitrary rare cores with the original entropy retained. The source obstruction is independently accepted; the new finite census/counterexample statement awaits independent review. The shortest next calculation is an explicit source-and-destination transfer at tag00000* and its incoming path, with both full terminal balances and old debits displayed, rather than another untracked rate increase or sign-depth search.
