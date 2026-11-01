# Fixed-depth payment survives rare padding

Entropy is in bits. All functions below are actual Boolean signs on independent uniform physical cubes. Put E=log2(e), L=log2(3), and

    a=6L-8/3-4E, A=4a,
    R=(128/3)(2-E), beta=256/3-48L,
    theta=4 beta/(3R)=(8/3-(3/2)L)/(2-E).

The rational logarithm certificates give A>0, R>0, beta>0 and

    1/2 < theta < 13/25,
    theta=0.5189670589801948... .

These strict signs, rather than the displayed decimals, are used below.

## Statement and quantifiers

Let g_n be -1 exactly on {0,1,2} in F2^n, n>=6, and +1 elsewhere. Let h on six bits be -1 exactly on {0,1,2,4,8,16,32,6,17,40}; set J(x)=-h(x xor 1). Form F_n=J(g_n,...,g_n) on six disjoint n-bit blocks. Set p=3*2^(-n) and S=4I-H. All queries below concern block 0, with original coordinates numbered from 0.

Query coordinate 2 and retain its zero branch. Query coordinate 0 next. Denote their signed full excesses by e1,e2, where e=average S(full children)-S(full parent). The constant-core first sibling remains a full function of the other five cores. At the two second-query children b=0,1 write U_b=q0 S(core_b), M_b=S(full child_b)-U_b and B2=(U_0+U_1)/2. Preserve exactly the original allocation

    T2=2e1+e2, D_b=T2 U_b/B2.

For every fixed nonnegative integer k, there exists N(k) such that, for all integers n>=N(k), the following extension is feasible at the SAME rate 4 and SAME original debit: on the second-query zero branch reveal original padding coordinates 3,...,k+2 in order, stop on a 1, and otherwise continue on 0. At each added query all old labels and the new signed query label can be paid solely from the corrected selected-core capacity. No positive other-core owner is spent. Retain the full root sibling, the other second-query sibling and all new constant-core siblings with their actual reach probabilities and debits.

At the j-th retained zero branch (j fixed), the booked-to-selected-capacity ratio tends to theta. Each queried-core-constant sibling has a positive complete full-function surplus and zero selected debit. This is an eventual fixed-depth statement. N(k) is not explicit and is not uniform in k. In particular it does NOT prove payment when k grows with n, payment of a complete reveal, arbitrary-core eligibility, or FEI.

## Exact coefficient and multiplicity formulas

For a core with s fixed coordinates, remaining dimension d=n-s, and sparse side B contained in {0,1,2}, let b=|B|, N=2^d, and

    L_z=sum_(x in B) (-1)^(z dot x), z in F2^2.

The empty Walsh coefficient is 1-2b/N. Every nonempty coefficient whose first two frequency bits are z is -2L_z/N. Its multiplicity is N/4 minus 1 when z=0, and N/4 otherwise. These are exact: sum the indicator of B in the defining Walsh average, and count all remaining d-2 free frequency bits. This formula is used only for d>=2. If E_B is the number of internal cube edges of B, direct boundary counting gives

    I(core)=(2bd-4E_B)/N.

The sets used are {0,1,2}, with E_B=2, {0,1}, with E_B=1, and {0}, with E_B=0. An empty sparse side is a constant core and contributes H=I=0. The exact formula also proves physical realizability for every admissible n; no interpolated probability law is substituted for a Boolean function.

For a core of mean mu, put v=1-mu^2. For an outer Walsh polynomial J, independent inputs of means mu_l give the occupied-block masses

    P_T=product_(l in T) v_l * [sum_(U containing T) Jhat(U) product_(l in U\T) mu_l]^2.

Let q_l be the corresponding biased pivotal probability. Parseval and the derivative identity give sum_(T containing l) P_T=q_l v_l. Conditional on T, nonempty core spectra factor independently. The Shannon chain rule therefore proves, INCLUDING every empty and terminal sector,

    H(F)=sum_l q_l H(core_l)+C,
    I(F)=sum_l q_l I(core_l),
    C=H(P_T)-sum_l q_l h2(v_l).

When v_l=0 its physical core is constant and the associated term is omitted. The formulas extend continuously to that endpoint; no division by v_l is made there.

## The outer correction is affine to second order

Allow block 0 to have minority probability t p, with each other block at p, for any FIXED t>=0. Let Q={1,2,3,5}. Direct expansion of the displayed occupied-block formula gives the following complete table through order p^2:

| occupied block T | multiplicity | mass through p^2 |
|---|---:|---|
| empty | 1 | 1-16p+(88+16t)p^2 |
| {j}, j in Q | 4 | 4p-(28+8t)p^2 |
| {0,j}, j in Q | 4 | 4t p^2 |
| {i,j}, distinct i,j in Q | 6 | 4p^2 |
| every other T | 49 | O_t(p^3) |

For t=0 the {0,j} masses are identically zero. Every mass polynomial is quadratic at most in t: if 0 is absent its amplitude is affine in mu0 and is squared; if 0 is present its amplitude is independent of mu0 and is multiplied by v0. Thus exact interpolation at t=0,1,2 certifies these coefficients for EVERY t, rather than sampling a continuum. code/packet_table.py reconstructs all 192 coefficients and checks them separately at t=3 and 7/3; out/PACKET_GROUPS.json lists every mask. The claimed degree bound follows from the displayed formula itself.

The table implies

    q0=4p+O_t(p^2),
    qj=1-(3+t)p+O_t(p^2), j in Q,
    q4=O_t(p^2).

For clarity the two complete entropy expansions are

    H(P) = [-16 log2(p)-32+16E]p
           +[64 log2(p)+176+32t-16t log2(t)+(-104+16t)E]p^2
           +O_t(p^3(1+|log2 p|)),

    sum q_l h2(v_l) = [-16 log2(p)-32+16E]p
           +[64 log2(p)+128-16t log2(t)-80E]p^2
           +O_t(p^3(1+|log2 p|)).

Use 0 log 0=0 at t=0. Subtraction yields the key identity

    C(t,p)=[48+32t+(16t-24)E]p^2
           +O_t(p^3(1+|log2 p|)).                         (1)

The coefficient is affine in t. The error is justified without exchanging an infinite sum and a limit: there are only 64 fixed mass polynomials. A polynomial of order r>=3 contributes O(p^3|log p|); at orders 0,1,2 the logarithm has a Taylor expansion about a strictly positive leading coefficient. The same finite-polynomial argument treats the six binary entropies. Constants may depend on t, which is essential.

## Inner asymptotics and the preserved debit

The exact core formulas give

    S(g_n)=a p+O(p^2(1+|log p|)).

For a pair sparse side {0,1} after s fixed coordinates, with s FIXED,

    S(pair_s)=(2^s/3)(16-8E)p+O_s(p^2(1+|log p|)).

For a point sparse side {0} the coefficient is half the pair coefficient at the same s. Multiplication by q0=4p+O(p^2) gives, on the two second-query children,

    U_b=R p^2+O(p^3(1+|log p|)),
    U_c=(R/2)p^2+O(p^3(1+|log p|)).

All retained zero-prefix states and all constant-core siblings have

    M=A p+O_s(p^2(1+|log p|)),                            (2)

because four untouched cores have limiting pivotal probability one, the selected q0 is O(p), and C has no linear term. In particular M>0 for sufficiently small p. This pays the actual signed outer correction before unused selected slack is named.

Under a physical split only one core changes, q0 stays fixed, and the mean other-core pivotal weights equal their parent values (condition on the queried physical bit). Hence

    e=q0 [average S(core children)-S(core parent)]
      +C(parent)-average C(children).                    (3)

The relative densities in (1) average correctly at every physical split, so the p^2 outer correction in (3) cancels. The first split doubles a three-point core with probability one half and otherwise makes it constant, so e1=o(p^2). The second split replaces the three-point core with the pair and point cores, yielding

    e2=beta p^2+O(p^3(1+|log p|)).

Thus

    T2/B2 -> beta/(3R/4)=theta,
    D_b/p^2 -> 4 beta/3.

No new core allowance has replaced the incoming labels. T2 and D_b are exactly the allocations in the statement, including e1.

## Any fixed number of padding queries

After j additional zero-valued padding queries, the pair shape has s=2+j fixed coordinates and

    U_j=2^j R p^2+O_j(p^3(1+|log p|)).

At the next padding query its zero core doubles its minority density and its other core becomes constant. Its leading inner S coefficient averages to the parent coefficient. Equation (1) is affine, so (3) gives e_j=o(p^2) for every fixed j. If D_j is the full incoming selected debit, book all outgoing debit D_j+e_j in the zero child, giving

    D_(j+1)=2(D_j+e_j).

The constant-core sibling receives zero selected debit; it retains its COMPLETE other-core law. Induction over a fixed j gives

    D_j=2^j(4 beta/3)p^2+o_j(p^2),
    (D_j+e_j)/(U_(j+1)/2) -> theta < 1.

By (2) both child M are positive eventually. Thus corrected selected capacity equals U in both children and total outgoing debit fits its true mean capacity. Split every old label a and new signed query label e_j between the children with the same proportional capacity rule; since the constant core has U=0, their zero-child amounts are 2a and 2e_j. Each conditional mean is preserved exactly. Signed excess may be a refund; no positivity of an individual excess is assumed. The combined debit is positive eventually because theta>0.

For any fixed k there are finitely many such strict inequalities. Their separate small-p neighborhoods have a common neighborhood, which defines N(k). This is a finite intersection, NOT an assertion uniform in k. The root constant-core sibling has reach 1/2; the untouched second sibling has reach 1/4 and its original D_c; the new siblings have reaches 2^(-j-3). None is discarded. Their M are positive eventually, and D_c/U_c->theta<1. Exact telescoping leaves the same root budget.

Every full constant-core sibling is nonconstant: J with its zeroth input fixed to +1 is nonconstant, and the other five g_n attain both signs with positive probability. Its entropy and influence therefore stay present even though its selected core is constant.

## What was tested, and what failed

out/FINITE.json covers ONLY n in {6,7,8,12,24,48} at the fixed third-query prefix. Exact outward intervals certify feasibility throughout that finite domain. At n=6 the required sibling fraction is 0.2559298287526758...; at the other five declared values the corrected selected capacity suffices, so the required fraction is exactly zero. No claim is made for all n>=7 from that finite list.

The first analytic attempt incorrectly expected every relevant capacity to start at p^2. Its assertion failed because M starts at positive A p. Its finite helper also temporarily used V=S in states where M>0; that special-case formula is inapplicable there. out/INITIAL_ATTEMPT.json preserves the failure and out/SERIES_DIAGNOSTIC.json the actual coefficients. The final helper uses V=U-max(0,-M), W=max(0,M) and reruns the full declared domain. Negative initial displayed 'fractions' were signed diagnostic gaps, never valid transfers.

out/ANALYTIC.json checks all low-order coefficients as exact rational linear forms in logarithms, and checks fixed-depth instances s=2,...,6. The proof above, with arbitrary fixed s and equation (1), supplies the all-fixed-depth extension; the five checked s values alone do not prove it. The strict logarithmic constants use 192-bit outward rational bounds from 80 atanh terms and an explicit geometric remainder. All canceled denominators are either certified positive (R,B2,eventual mean selected capacity) or explicitly excluded and handled as constants (v=0).

## Independent review and remaining unsupported line

A089-CORRECTED-CAPACITY-SIBLING-TRANSFER@1 is independently accepted at its unchanged generic allocation and seven-query finite scope. Direct A(other)+g0 B(other) packet expansion reconstructs the complete entropy and influence on seven source profiles without executing source code. Exact intervals reproduce every source incoming debit, new excess, required corrected capacity and transfer fraction. The scalar allocation proof is reconstructed including B=0, W=0, T=0, equality, and 1,792 rational boundary instances. out/REVIEW_A089.json records 7,439 predicates and the exact source statement hash. No arbitrary-core or hereditary extension is accepted by that review.

For completeness, the allocation proof is elementary. With child weights w summing to one, corrected selected capacities V and unused other capacities W, put B=sum wV and Z=sum wW. Any total debit T has other draw at least max(0,T-B), by summing selected capacity constraints. Conversely set s=min(T,B), tau=max(0,T-B). Book sV/B when B>0 (zero when B=0), and tau W/Z when Z>0 (zero when Z=0). These fit each child iff T<=B+Z, and their weighted sum is exactly T. Thus the stated minimum is both necessary and attained, including all zero/equality boundaries. Negative M is paid before these nonnegative capacities are defined.

The new theorem here is an analytic proof pending independent review, not a Lean certification of the Fourier argument. code/Ledger.lean formalizes only the integer-scaled no-renewal telescoping identity; its outcome is separately recorded. It does not certify the logarithmic asymptotics or their translation into the full statement.

The first unpaid universal line is a signed reserve inequality valid when the physical reveal depth grows with n, or for arbitrary retained non-flat cores, with the SAME already booked debit. Constants in (1)--(2) depend on the prefix density t. Taking k=n-O(1) is not licensed. A075's earlier negative complete endpoint and full-block rate-4 obstruction remain valid: they lie beyond every fixed-depth limit studied here. No FEI constant is improved.
