# Bounded actual-Boolean critical-core search and exact orbit certificates

30 September 2026. **Full FEI remains OPEN. No new record, unbounded Boolean family, or universal proof was found.**

This pass scored 9,350,000 states (including restarts and repeated proposals) in six transitive block-Hamming-profile families. It also enumerated 2,130,944 small orbit assignments, examining all 3,481 balanced representatives up to output negation, and evaluated their balanced self-composition recurrence. No result exceeded the pre-existing critical-core benchmarks.

The constructive computational deliverable is an exact orbit-compressed Walsh implementation: genuine 48-variable functions are evaluated using only325 or969 coefficient types, without enumerating2^48 inputs. Six selected candidates have independently reconstructed integer Walsh data and integer-only outward logarithm certificates. The corresponding analytic identities are standard character symmetry and the previously established composition law; no priority claim is made for them.

## 1. Scope and timing

The task was to seek actual Boolean critical families that might guide a dimension-free all-shift argument, not to treat finite search as a proof. Every scored function is explicitly +/-1 on its cube. Its histogram definition is invariant under within-block bit permutations and permutations of equal-size blocks, so the group is transitive on physical coordinates. Consequently the ratio at one coordinate is exactly the existential minimum over coordinates, apart from the numerical evaluation used during search.

All heavy runs were sequential, one CPU, with BLAS/OpenMP/MKL thread counts fixed to1. Actual search time was2198.6758 seconds (36.645minutes); the six rigorous candidate verifications totaled7.5549seconds. Initial regression probes added about13seconds. The bounded computational milestone finished within the authorized initial one-hour budget. No paid computation was used. RESULTS.json records actual counts, timings, software versions and seeds.

## 2. Completed searches

The fixed random seed was20260930. The full-table searches use annealing and seeded/random restarts; the orbit-compressed searches use the same family definition at larger dimensions. These are not exhaustive searches of the large families.

| Dimension | Block width | Blocks | Objective evaluations | Certified interval for selected best rho0 |
|---:|---:|---:|---:|---|
|16|2|8|500,000|[6.00374605655908825141422865358018755, 6.00374605655908825141422865358018756]|
|15|3|5|500,000|[5.21273052512200298922860865843442234, 5.21273052512200298922860865843442235]|
|16|4|4|350,000|[4.95493502231181107629098403830741646, 4.95493502231181107629098403830741647]|
|48|2|24|3,000,000|[5.74734028662185407919401997381006207, 5.74734028662185407919401997381006208]|
|30|3|10|3,000,000|[5.46167296746313965772094840394173645, 5.46167296746313965772094840394173646]|
|48|3|16|2,000,000|[5.59888684295527378372831819882839638, 5.59888684295527378372831819882839639]|

Here rho0=min_i Delta_i H/Inf_i. Each interval certifies the named candidate only; it does not certify global optimality of the search or even ordering against every unretained candidate.

The first result reproduces the known eight-pair width-two tribes value. The three larger compressed bests are ordinary disjoint-tribes seeds; no improvement over those seeds was found. The width-four/four-block best is retained as its explicit orbit assignment, without asserting that it is extremal or novel.

The stronger pre-existing F4 Numaro tower benchmark has rho0>7.0518 on104,976 variables, aggregate B/I>4.5388 and minimum local erasure ratio>4.5048, under the source certificate's stated8-ulp numpy-log assumption. Thus none of this search's candidates raises that obstruction. Those quantities concern a proof mechanism, not the best lower bound for the FEI constant.

## 3. Exact orbit-Walsh recurrence

Divide n=bk bits into k blocks of width b. A physical input has a histogram h=(h_0,...,h_b), where h_j counts blocks of Hamming weight j and sum h_j=k. The Boolean function is specified by one sign s_h per histogram. There are binom(k+b,b) histogram types.

For a Fourier set with block-weight histogram c, define the integer block character sum

    K_j(r)=sum_l (-1)^l binom(r,l) binom(b-r,j-l),
    P_r(t)=sum_(j=0)^b K_j(r)t_j.

Then its unnormalized Walsh coefficient is

    A_c=sum_h s_h [t^h] product_(r=0)^b P_r(t)^(c_r).            (1)

This follows by multiplying the exact character sum separately over physical blocks, then collecting equal physical histograms. The multiplicity of a Fourier histogram is

    w_c=k!/product_j c_j! * product_j binom(b,j)^(c_j).          (2)

Consequently Parseval and entropy are computed exactly/compressibly as

    sum_c w_c A_c^2=2^(2n),
    H=sum_c w_c (A_c/2^n)^2 log2(2^(2n)/A_c^2).

For a queried bit in one distinguished block, let r be the residual Fourier weight on the other b-1 bits of that block and let c describe the remaining k-1 blocks. The paired coefficients are A_(c+e_r), A_(c+e_(r+1)), with multiplicity

    binom(b-1,r) * (k-1)!/product_j c_j! * product_j binom(b,j)^(c_j). (3)

These pairs give exact influence, erasure and restriction entropy difference. The search computes the last two with homogeneous binary-entropy/JS formulas to avoid subtracting nearly equal global entropies.

The coefficient matrix was checked against complete physical Walsh transforms for the n15 and n16 regression families. The independent certificate reconstructs (1) again by dictionary polynomial multiplication, rather than trusting the saved coefficient vector or the search update code.

## 4. Balanced seed self-compositions

To avoid treating a weak small seed as evidence about its deep tower, the pass also enumerated every orbit assignment for pair-block seeds in dimensions6,8,10, retained balanced representatives, and evaluated the exact balanced composition law recovered from F4.

For a balanced transitive seed G, write d for each coordinate influence, a for its common singleton coefficient, and let K_G(mu) be the homogeneous entropy-decrement kernel of the root coefficient pairs with their queried member scaled by mu. Let E_G(mu) be the corresponding binary-erasure kernel. For depth-j balanced self-composition,

    d_j=d^j, singleton coefficient=a^j,
    rho_j=rho_(j-1)+K_G(a^(j-1))/d^j,
    beta_j=beta_(j-1)+E_G(a^(j-1))/d^j,                         (4)

where beta_j is the aggregate (equivalently local, by transitivity) erasure ratio. Equation (4) is the known composition identity, specialized to one coordinate orbit. No monotonicity of G is needed.

All increments are nonnegative. If a=0, all later increments vanish. Otherwise rho=a^2/d<1, and the remaining full-entropy tail after depthJ is bounded by

    rho^J [C_n/(1-rho)+2L(J/(1-rho)+rho/(1-rho)^2)],
    C_n=1+2n+3log2(e), L=log2(1/|a|).                          (5)

To see this, any nonzero normalized seed coefficient has magnitude at least2^-n. The logarithmic packet bound plus the JS payment bounds the j-th normalized increment by rho^(j-1)[C_n+2(j-1)L]. Sum the geometric series and its derivative. The same bound also bounds the erasure tail. The search evaluates (4)-(5) in floating arithmetic; this part is explicitly exploratory, not an outward-certified limit.

| Seed dimension | Orbit assignments exhaustively enumerated | Balanced representatives | Largest numerical tower rho limit |
|---:|---:|---:|---:|
|6|1,024|12|3.04657494043|
|8|32,768|143|3.71118514338|
|10|2,097,152|3,326|4.11588511092|

These computations do not beat the known Numaro tower. The finite enumeration is exhaustive only within each stated symmetry class. It does not characterize arbitrary balanced seeds or all transitive Boolean functions.

## 5. Integer-only entropy certification

For each selected root candidate, certify_compressed.py independently reconstructs every integer A_c, checks Parseval, checks both child normalizations, and computes the influence numerator exactly. Logarithms are enclosed without floating transcendental assumptions.

For integer x>0, write x=2^e y with1<=y<2, z=(y-1)/(y+1)<=1/3. Use

    ln y=2 sum_(j=0)^(L-1) z^(2j+1)/(2j+1)+R,
    0<=R<=2 z^(2L+1)/[(2L+1)(1-z^2)].

At L=90 and fixed denominator Q=2^256, each summand is rounded downward by integer division; the upper endpoint adds at most L units plus the explicit rational tail ceiling. The same procedure bounds ln2. Positive interval division supplies base-two logs. All probability weights are integer squares divided by2^(2n), so entropy sums and ratio endpoints can be accumulated using integer arithmetic with one common denominator. Certificate JSON files contain the exact numerator/denominator endpoints as well as decimal displays.

These are executable finite certificates, not formal proof-assistant verification. They certify actual specified Boolean functions. They do not infer a universal bound from tested cases.

## 6. Result for the full-scope programme

This is a completed negative search milestone. The stronger full-scope target remains the actual all-shift signed Boolean convolution problem, or a nonreusing physical entropy payment. The accompanying ATTEMPTS.md retains the tried global mechanisms and their exact stopping reasons, including the all-shift cubic entropy identity, without promoting an unpaid signed sum to a theorem.

The September30 local lemmas and their scoped constructive corollaries remain valid in the separate fei-log-allocation package. The present search does not replace them, weaken their quantifiers, or change the full-FEI status.

## 7. Prior work consumed

- The verified shared route map at brain commit0bdd6c7177d0b756b4b16be317caed29f0cf75e4, including its quantum/classical and overlapping-product guardrails
- Sept20 BOOLEANITY_ORDER and sharp-derivative reports: finite-order and unsigned-summation obstructions, not newly discovered here
- Sept21 top-flipped tribes report: prior searches of up to3 whole pair orbits, distinguished from the present arbitrary-orbit annealing
- Sept22-23 F4 report, exact composition laws and tower benchmark (blob b8ee8759677c6c115691918aada049d6dd5120e7)
- F2 new-gates report (blob3f87fba82faf4ce32402258278b42c7e13498724): prior extensive Numaro-core searches were not repeated

No controls, schedules, owner allocations, earlier proofs, or public repositories were modified. Publication priority is unverified.

## Executable source availability

The four executable scripts are proposed in draft PR [#13](https://github.com/yspennstate/math-open-problems/pull/13), pinned at commit 60d3a823b0f55ab46df5916d0cbed87208c187a6. They are not yet merged into master. For replay, obtain those four scripts from that commit and place the candidate JSON files alongside them. Research results and data are archived on master separately.
