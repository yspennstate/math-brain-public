# Independent referee report

Overall verdict: **SOUND**.

I found no gap or counterexample in the filling criterion or the Brownian-prefix theorem. The proof uses the invariant sigma-field correctly, the random stopping rule has the claimed law, and the transfer step retains the given X on an extension. The numerical claims checked exactly. This verdict concerns mathematical validity. The exact source attributions and novelty are not fully verified under the required memory-only restriction; those limitations are recorded separately below.

Audited file: `PAPER.tex`, SHA-256 `a5702bc05e0c099aed322756d62626b37909b739c1bc9ca00a6ef15215b705a1`. Line numbers refer to this unchanged source. Audit date: 12 November 2026, Asia/Tbilisi. No browsing, other agents, author programs, pushes, or visible windows were used. All new artifacts are in this folder. Shared brain/mesh/checklist stores were left untouched because this run forbids outside writes.

## What the theorem establishes

Theorem [thm:main] answers the quoted question under the usual coupling interpretation, in which independent auxiliary randomness may be added to the given probability space. Put tau=N and take P to be the restriction of B to [0,N]. Then [eq:concat] is B itself. The piece is continuous, has a.s. finite length, and may depend on X and on the future of B. The theorem does not require an independent prefix, an original-space measurable prefix, or a stopping time. None of these extra requirements appears in the quotation supplied here. Whether the original authors imposed additional conventions elsewhere cannot be checked without their text.

The extension preserves X as a random element, not merely its distribution. Brownian motion here has its standard Wiener law and is Brownian relative to its own augmented natural filtration. It need not be Brownian in a filtration containing the whole original sigma-field at time zero. This is the ordinary meaning of the stated coupling conclusion and should be explicit to avoid a stronger reading.

Remark [rem:stopping] is correct: if the concatenation is Brownian relative to a filtration in which the finite length is a stopping time, strong Markov makes the post-length increments Wiener. An independent random seed can be adjoined initially without changing that argument. Thus a non-Wiener target needs an anticipative length.

## The load-bearing proof checks

For [thm:filling](ii), every strictly invariant set A has 1_A(theta^n z)=1_A(z) for all integers n and points z. Substitution of an arbitrarily dependent N proves Q(A)=P(A). The argument needs neither a stopping-time assumption nor a standard-Borel underlying space.

For (i), the density pushforward is Lh=h composed with theta inverse. Equal mass removal gives integral a_n=integral b_n=r_n and sum m_n=f-b_infinity. The crucial identity is

    (1/M) sum_(n<M) a_n -> h=E[b_infinity | I] in L1(P).

It follows from the mean ergodic theorem applied separately to each m_k, with tails bounded by 2 sum_(k>=K) integral m_k. The L1 theorem is valid for this probability-preserving map: apply the L2 mean ergodic theorem to bounded truncations, then use the L1 contraction bound. It is not an unjustified general assertion about arbitrary L1 operators.

If r>0, an invariant set H={h>=epsilon} has positive b_infinity integral. A positive-measure D inside H has b_infinity>=delta, where 0<delta<=1. Since a_n<=1, m_n>=delta a_n on D. The displayed L1 limit makes the Cesaro averages of integral_D m_n bounded below by delta epsilon P(D)>0, contrary to their summability. This proves r=0. No claim that residual demand is disjoint from all future supply images is needed or made.

Conversely, the recursion preserves integral_A(b_n-a_n)=integral_A(f-1) on every invariant A. If r_n tends to zero, both integrals vanish and invariant balance follows. Thus zero residual occurs exactly under the stated condition, not just in one direction.

The rule g_n=m_n/a_n, set to zero when a_n=0, is measurable. Independent uniforms yield survival density a_n and stopping density m_n by induction. Consequently P(N>=n)=r_n, N is finite a.s., and theta^N Z has law sum m_n P=fP. A null-set modification makes N literally finite-valued everywhere if required.

For the Brownian application in section [sec:proof], the two-sided path space is Polish, the unit increment shift is an invertible measure-preserving homeomorphism, and its unit-interval increment pieces form a two-sided iid sequence. The source proves ergodicity in compressed form. An independent check is to approximate an invariant event A by a finite-coordinate event C, shift C far enough to obtain independence, and deduce |P(A)-P(A)^2|<=4 P(A symmetric-difference C). Thus P(A) is zero or one.

The density f=(dQ/dWiener) composed with forward restriction has integral one and forward marginal Q. W remains two-sided Wiener under the construction. The paper defines B_t=W(t), not W(t-N)-W(-N). Therefore pi(theta^N W)_t=W(N+t)-W(N)=B_(N+t)-B_N, with the correct signs and law.

Finally, disintegrate law(Y,B,N) over its Polish path variable Y to obtain a kernel K(x,db,dn). On the original space form

    P_tilde(domega,db,dn)=P_original(domega) K(X(omega),db,dn).

This is an extension preserving X and giving the required joint law. The measurable graph x=Phi(b,n) carries probability one, which proves the simultaneous path identity. No regularity hypothesis on the original Omega is missing.

The filling proof is independent of Rost's embedding theorem once the standard mean ergodic theorem is granted. The optional forward-path/Rost discussion in [rem:rost] does not carry any part of the main proof.

## Verdict table: statements, displays and proof steps

The table includes every labeled theorem/remark/equation and every displayed or load-bearing proof step. CORRECT includes routine null-set or wording qualifications described in the reason column. Bibliographic gaps below are gaps in this restricted source verification, not in the mathematical derivation.

| Statement / step | Verdict | Reason |
|---|---|---|
| Lines 4246: quotation and attribution to Problem 7.5 | CORRECT (as the supplied quotation) | The mathematical question being audited is explicit. Exact wording, problem number and page in the external source cannot be independently verified without that source. |
| Lines 4851, [eq:concat] | CORRECT | X(0)=0 makes the two definitions agree at the join; continuity follows for a continuous finite prefix. |
| Lines 5460, [thm:main], as an answer to that quotation | CORRECT | Take tau=N and P=B restricted to [0,N]. The displayed identity gives Z=B simultaneously for all times. Absolute continuity includes equivalence. N is finite a.s., integer-valued and nonnegative. |
| on an extension of the probability space (line 55) | CORRECT | Standard meaning: preserve the given X by pullback to an enlarged space and add auxiliary randomness. The quoted question imposes neither original-space measurability nor independence of the piece. Either added requirement would be a different question. The theorem should say explicitly that this is the interpretation of the quote. |
| The time N looks into the future, and it has to (line 62) | CORRECT with qualification | The following remark proves the obstruction when Q differs from Wiener measure. For Q=Wiener measure, N=0 suffices, so the sentence is overbroad if read without that qualification. |
| [rem:stopping], line 65: strong Markov argument | CORRECT | Brownian motion relative to the stated filtration has Brownian post-tau increments at an a.s. finite stopping time. Thus Q must be Wiener measure. Usual augmentation can be used; independence of the post-tau process from the stopped sigma-field is more than needed. |
| Line 65: independent randomized stopping times | CORRECT | Enlarge the Brownian filtration at time zero by an independent random seed (or independent randomization process). Brownian increments remain independent of the past; strong Markov still applies. A seed dependent on the Brownian future would not satisfy this argument. |
| Line 74: strictly invariant sigma-field I | CORRECT | It is a sigma-field. Strict invariance makes membership constant along every two-sided orbit, without exceptional sets. |
| Line 84: arbitrary integer-valued N on any underlying space | CORRECT | N need only be jointly measurable with Z. Countability of the possible n makes theta^N Z measurable; no conditional distributions, independence, standard-Borel hypothesis, or stopping-time property is needed. |
| Line 91: 1_A(theta^n z)=1_A(z) for all z and n in Z | CORRECT | Uses strict invariance and invertibility, including for negative n. |
| Line 91: Q(A)=P(A) and conditional-expectation conclusion | CORRECT | Apply the orbit identity pointwise at n=N, then the defining characterization of E[f&#124;I]. |
| Lines 7478: Lh=h composed with theta inverse; [eq:push] | CORRECT | This is the density of the pushforward measure. The direction of the inverse is correct. Integrals and the constant 1 are preserved. Random element with subprobability law needs the usual restriction-to-an-event or cemetery-state convention, explained below. |
| Line 83: [thm:filling](i), including arbitrary measurable E | CORRECT | All functions and countable operations used are measurable on any such space. No disintegration is needed here. A product with the uniform sequence supplies the required probability space. |
| Line 88: ergodic specialization | CORRECT | Trivial means trivial modulo P-null sets, which suffices for conditional expectations. |
| Lines 9598, [eq:recursion] | CORRECT | Nonnegative measurable differences; min removes exactly the same density from supply and demand before advancing the remaining supply. |
| Line 99: 0<=m_n<=a_n<=1 and 0<=b_(n+1)<=b_n<=f | CORRECT | Induction uses L positivity and L1=1. Uniform boundedness of a_n is important later. |
| Line 99: equal masses r_n and decreasing limit r | CORRECT | Both integrals start at 1 and lose exactly integral m_n at step n. |
| Lines 100102, [eq:sum], all three identities | CORRECT | Pointwise telescoping and Tonelli give the sum; b_n is dominated by integrable f, so its decreasing limit has integral r. The text's monotone convergence is justified by applying it to f-b_n. |
| Lines 104107: a_n=1-sum_(k<n) L^(n-k)m_k | CORRECT | Direct induction; exponent n-k includes the shift after each removal. Empty sum gives a_0=1. |
| Lines 108111, [eq:cesaro] | CORRECT | For each k the relevant n range is k+1,...,M-1, giving j=1,...,M-1-k. Zero convention handles empty ranges. |
| Line 112: mean ergodic theorem in L1 | CORRECT | True for a measure-preserving map on a probability space, despite failure for some general L1 contractions. Truncate g to bounded functions, use the L2 mean ergodic theorem, then L1 contraction to pass to every integrable g. No ergodicity hypothesis is required. |
| Line 112: inverse has same invariant field and limit E[g&#124;I] | CORRECT | Invertibility identifies the two invariant fields. Almost invariant level sets have strict representatives, so the stated strict I gives the same conditional expectation modulo null sets. |
| Line 112: fixed-k convergence and norm bounds for c_(k,M) | CORRECT | The number of terms divided by M tends to 1. Positivity and integral preservation give the asserted bounds. |
| Lines 113116: infinite-sum L1 estimate and double limit | CORRECT | The tails are uniformly bounded by twice sum_(k>=K) integral m_k, which tends to zero. No unjustified exchange of limits. |
| Lines 117120, [eq:limit] | CORRECT | Conditional monotone convergence identifies the sum as E[f-b_infinity&#124;I]; the balance hypothesis is used precisely in replacing 1-E[f&#124;I] by 0. |
| Line 122: positive invariant H and positive-measure D | CORRECT | h is nonnegative, I-measurable, with integral r. On H, conditional expectation transfers the positive integral to b_infinity; some positive threshold delta<=1 gives a positive-measure D. |
| Lines 123125: m_n>=delta a_n on D | CORRECT | For 0<=a<=1 and 0<delta<=1, min(a,delta)>=delta a. |
| Lines 126129: positive lower bound on Cesaro averages over D | CORRECT | L1 convergence gives convergence of integrals over every measurable D; D does not have to be invariant. h>=epsilon on D. |
| Line 130: contradiction with summability | CORRECT | sum_n integral_D m_n<=1, hence its partial sums divided by M tend to 0. This contradicts the positive lower bound. |
| Line 130: r=0, b_infinity=0 and sum m_n=f | CORRECT | Nonnegative b_infinity has zero integral; then [eq:sum]. |
| Line 132: g_n, including a_n=0 | CORRECT | m_n=0 there. The piecewise definition is measurable, lies in [0,1], and satisfies a_n g_n=m_n. |
| Lines 133135: definition of N | CORRECT up to a routine null modification | Countable first success is measurable and initially takes values in N union {infinity}. Later finiteness a.s. allows setting N=0 on the null infinite-survival event to get literally N-valued N. Using <= rather than < changes nothing, even when g_n=0, since U_n has no atoms. |
| Line 136: base case and independence induction | CORRECT | Survival to n only depends on Z and earlier uniforms, and theta^n Z only on Z. U_n is independent of both jointly. |
| Lines 137139: stopping and surviving subprobability densities | CORRECT | Integrating the independent uniform gives g_n or 1-g_n; multiplication by survival density a_n gives m_n or a_n-m_n. |
| Line 140: push surviving density to a_(n+1) | CORRECT | Apply [eq:push] to the restricted law, not to an unconditional probability distribution. |
| Line 140: P(N>=n)=r_n, finiteness and output law | CORRECT | Integrate survival density; continuity from above makes P(N=infinity)=0. Sum the disjoint stopping events to obtain sum m_n P=fP. |
| Line 145: path space E is Polish | CORRECT | C(R) with uniform convergence on compacts is Polish and the condition w(0)=0 is closed. The forward and unit-piece spaces are Polish for the same reason. |
| Line 145: two-sided Wiener measure | CORRECT | Independent Brownian motions on the positive and negative half-lines, both anchored at zero, define the standard two-sided increment law. |
| Lines 146149: theta and its displayed inverse | CORRECT | Composing the formulas cancels the shifts and normalizations. Both maps are continuous in the compact-open topology. |
| Line 149: P-invariance | CORRECT | Recentered increments across any finite collection of ordered times have the same independent centered normal laws, including intervals crossing zero. |
| Line 149: bimeasurable bijection with unit pieces | CORRECT | The pieces xi_k start at zero. For k>0 sum preceding endpoints, and for k<0 subtract endpoints from k through -1 to recover w(k), then add xi_k(s). These formulas reconstruct one continuous anchored path and are measurable. |
| Line 149: independent Wiener pieces and conjugacy to the Bernoulli shift | CORRECT | Disjoint unit-interval increment paths are independent Brownian pieces. xi_k(theta w)=xi_(k+1)(w). |
| Line 149: ergodicity by finite-coordinate approximation and tail triviality | CORRECT | This is a compressed standard proof, not a mere unsupported assertion. Completed-tail measurability can be made explicit as below; alternatively cylinder mixing proves it directly. |
| Line 151: f=f_+ composed with restriction pi | CORRECT | Choose a Borel version of the RadonNikodym derivative. Integral equals 1 and the forward marginal of fP is exactly Q. Past and future were independent under P; no unexplained density normalization is needed. |
| Line 151: application of [thm:filling](i) | CORRECT | Invariance, invertibility and ergodicity have all been checked. Integrable nonnegative f satisfies the invariant balance condition. |
| Line 151: B_t=W(t) is Brownian | CORRECT | W itself still has law P. It is theta^N W, rather than W, whose law is changed to fP. N may depend on W and the uniforms. |
| Lines 152155: Y=pi(theta^N W), identity and output law | CORRECT | Iteration gives (theta^n w)(t)=w(n+t)-w(n). Thus Y_t=B_(N+t)-B_N and Y has law Q. No expression W(t-N)-W(-N) occurs in the paper. |
| Line 155: measurability of Phi | CORRECT | For each fixed integer n this is a continuous path map. A countable disjoint union over n is Borel measurable. |
| Line 157: transfer to an extension of the given space | CORRECT | Disintegrate law(Y,B,N) over Y in Polish spaces; a measurable probability kernel for (B,N) given Y can be evaluated at the original X on any probability space. No standard-Borel assumption on the original Omega is necessary. |
| Line 157: equality for all times, Brownian marginal and finite N | CORRECT | The graph x=Phi(b,n) is measurable (equality of continuous paths is a closed diagonal condition). The transferred joint law puts mass one there. B' retains its Wiener marginal and N' its finite integer law. |
| Lines 5559: [thm:main], final verdict after proof | CORRECT | The transfer retains the actual given X by pullback, not just a new copy with its law. Taking its finite prefix constructs the required concatenation. |
| [rem:rost], line 162: deterministic kernel interpretation | CORRECT | Removing m_n then applying the deterministic kernel gives exactly [eq:recursion] on densities. |
| Line 162: every nonnegative measurable N built from Z and independent uniforms is a randomized stopping time for this chain | CORRECT with a convention stated | Here N must be integer-valued, and all auxiliary randomization may be adjoined at time zero. The full initial state Z determines the entire chain, so {N<=n} is in sigma(Z,all uniforms). If only U_0,...,U_n are revealed at time n, this assertion is true for the paper's N but not for every arbitrary function of the whole uniform sequence. This is a filtration clarification. |
| Line 162: forward-path chain with stationary Wiener law | CORRECT | The one-sided increment shift is measurable and Wiener-preserving, although not invertible. Its chain state Y_0 is the entire Brownian future, so its stopping times are not Brownian stopping times. |
| Line 162: bounded excessive functions are constant a.s. | CORRECT | u(theta y)<=u(y) has zero integral difference by stationarity, so equality holds a.s. One-sided iid-piece shift ergodicity makes invariant measurable functions constant a.s. Absolute continuity of Q removes the exceptional sets for the target too. |
| Line 162: Rost embedding on forward paths | CORRECT in mathematical content | The stationary recurrent probability setting, excessive-function balance, and Q<<Wiener are the intended filling-theorem setting. Exact statements of the cited Rost/DM/PT results are unavailable here and their numbering/hypotheses cannot be source-checked. This optional alternative is not used in the proof of [thm:main]. |
| Line 162: self-contained proof | CORRECT with ordinary mathematical usage | The filling argument is proved rather than delegated to Rost; it still uses the standard mean ergodic theorem. |
| [rem:integer], lines 166170: integer-density calculation | CORRECT | Partition by k and change variables z=theta^(-k)y. Tonelli gives the sum of indicators as density. Its integral is 1, so it is finite and integer-valued a.s.; an infinite value on a null set can be replaced by zero. |
| Line 170: auxiliary randomness necessary for the general invertible criterion | CORRECT | Noninteger f cannot be the density of a deterministic orbit map. For example, swap two equally likely points and take f=(3/2,1/2); invariant balance holds but deterministic images have densities in {0,1,2}. |
| Line 170: Brownian B-only measurability is a separate question | CORRECT | Passing to the forward marginal discards the negative path, and the forward shift is noninvertible. The integer-density obstruction cannot simply be transferred to that different question. No resolution of it is claimed. |
| [rem:size], line 174: tail P(N>=n)=r_n and mean formula | CORRECT | Established by the survival induction; Tonelli gives E N=sum_(n>=1)P(N>=n), possibly infinite. |
| Line 174: two-sided law stronger than forward-law target | CORRECT | Conditioning x_0=1 fixes no negative coordinates under fP. First success at n>0 forces x_(n-1)=0 after shifting, so it does not in general give the two-sided target. |
| Line 174: Bernoulli formula for n=1,...,13 | CORRECT | Independently computed on the common window [-n,0], with exact integer densities and rational probabilities. Every displayed value agrees; see bernoulli_results.json. |
| Line 174: a sequence with infinite sum if the pattern continues | CORRECT | Central binomial coefficients give an n^(-1/2) tail. This wording is conditional, not a claimed inference about an infinite sum from thirteen terms. A ballot argument below actually extends the formula to all n. |
| Line 174: first n with x_n=1 has mean one and correct forward law | CORRECT | Here n starts at 0. P(T=k)=2^(-k-1), E T=1, and the bits after the first 1 are fresh iid fair bits. With a start at 1 the mean would instead be 2. |
| Line 177: finite orbit-balanced targets fill within &#124;E&#124; steps | CORRECT | All exact cases pass. There is also a direct proof of the bound below. Steps here mean removal rounds n=0,...,d-1, giving b_d=0 and N<=d-1. |
| Line 177: unbalanced targets leave positive residual | CORRECT | Every unbalanced case leaves the exactly predicted orbit-imbalance mass; no tolerance or floating-point decision was used. |
| [eq:recursion] on finite permutations | CORRECT in every tested case | 4,139 exhaustive half-integer cases on sets of size <=4, plus 640 seeded random rational cases on sizes <=16. Supply pushforward, common mass, bounds and cycle balance were checked exactly. |
| Construction of N on finite permutations | CORRECT in every tested case | An independent branch enumeration over each starting point reproduces the filled target density and survivor mass exactly. Three 50,000-sample simulations using independent exact rational coins give the expected endpoint laws. |

## Exact Bernoulli experiment

Commands that produced the saved results:

```sh
python3 bernoulli_exact.py > bernoulli_stdout.txt
```

This is my own finite-window program. At stage n it stores the common window [-n,0], with 2^(n+1) atoms. L shifts the old function to [-n-1,-1]; the residual demand keeps its unshifted coordinates. Densities are integer-valued in this example and all probabilities use fractions. The comparison formula is binom(2j,j)/2^(2j+1), j=floor(n/2).

| n | a_n window | b_n window | Common-window atoms | Exact r_n | Paper formula |
| --- | --- | --- | --- | --- | --- |
| 1 | [-1,-1] | [0,0] | 4 | 1/2 | 1/2 |
| 2 | [-2,-1] | [-1,0] | 8 | 1/4 | 1/4 |
| 3 | [-3,-1] | [-2,0] | 16 | 1/4 | 1/4 |
| 4 | [-4,-1] | [-3,0] | 32 | 3/16 | 3/16 |
| 5 | [-5,-1] | [-4,0] | 64 | 3/16 | 3/16 |
| 6 | [-6,-1] | [-5,0] | 128 | 5/32 | 5/32 |
| 7 | [-7,-1] | [-6,0] | 256 | 5/32 | 5/32 |
| 8 | [-8,-1] | [-7,0] | 512 | 35/256 | 35/256 |
| 9 | [-9,-1] | [-8,0] | 1024 | 35/256 | 35/256 |
| 10 | [-10,-1] | [-9,0] | 2048 | 63/512 | 63/512 |
| 11 | [-11,-1] | [-10,0] | 4096 | 63/512 | 63/512 |
| 12 | [-12,-1] | [-11,0] | 8192 | 231/2048 | 231/2048 |
| 13 | [-13,-1] | [-12,0] | 16384 | 231/2048 | 231/2048 |

All entries agree exactly. A separate dynamic program counts nonnegative simple walks, and the program also checks the following description of b_n pointwise on every cylinder: x_0=1 and the backward walk on x_-1,...,x_(-(n-1)), with +1 for a 1 and -1 for a 0, never becomes negative.

This description extends beyond the finite test. After initial removal, every 0 supplies one unit and every 1 demands one unit. Advancing supplies fills the first unfilled demand to their right. A surplus of 0s in a backward prefix sends a supply to 0; if every such prefix has at least as many 1s as 0s, intervening demands consume every supply. Hence parenthesis matching and the reflection principle give, for every n>=1,

    r_n = (1/2) P(S_1,...,S_(n-1)>=0)
        = binom(n-1,floor((n-1)/2))/2^n
        = binom(2j,j)/2^(2j+1).

Thus the filling scheme's mean time really is infinite: its tail is of order n^(-1/2). The paper's weaker conditional wording is valid. The first success T=inf{n>=0:x_n=1} instead has P(T=k)=2^(-k-1), E T=1 and the correct forward law. It fails for the two-sided target: after T>0 the bit immediately before the new origin is necessarily 0. In fact P(x_(T-1)=1)=1/4, whereas under fP the negative bit is still fair, giving probability 1/2.

## Exact finite-permutation experiments

```sh
python3 finite_exact.py > finite_stdout.txt
```

The recursion uses Fraction, an independently coded push along the permutation, and no author code. Exhaustive tests include every permutation and every nonnegative half-integer density summing to the set size, through size four. Random tests use seed 20261112 and 40 cases at each size. Half are normalized per cycle; half are normalized globally and then classified by their actual cycle balances. There are 4,139 exhaustive and 640 random cases. Every exact check passed.

Exhaustive cases:

| Size | Cases | Balanced | Unbalanced | Largest first n with b_n=0 |
| --- | --- | --- | --- | --- |
| 1 | 1 | 1 | 0 | 1 |
| 2 | 10 | 6 | 4 | 2 |
| 3 | 168 | 72 | 96 | 3 |
| 4 | 3960 | 1320 | 2640 | 4 |

Random rational cases:

| Size | Cases | Balanced | Unbalanced | Largest first n with b_n=0 |
| --- | --- | --- | --- | --- |
| 1 | 40 | 40 | 0 | 1 |
| 2 | 40 | 32 | 8 | 2 |
| 3 | 40 | 26 | 14 | 3 |
| 4 | 40 | 25 | 15 | 4 |
| 5 | 40 | 26 | 14 | 5 |
| 6 | 40 | 24 | 16 | 6 |
| 7 | 40 | 22 | 18 | 7 |
| 8 | 40 | 24 | 16 | 8 |
| 9 | 40 | 22 | 18 | 9 |
| 10 | 40 | 21 | 19 | 10 |
| 11 | 40 | 22 | 18 | 11 |
| 12 | 40 | 21 | 19 | 12 |
| 13 | 40 | 22 | 18 | 13 |
| 14 | 40 | 21 | 19 | 14 |
| 15 | 40 | 20 | 20 | 14 |
| 16 | 40 | 20 | 20 | 15 |

For d=cardinality(E), first n with b_n=0 counts completed removal rounds. Thus n=d means the last possible stopping time is d-1, not d. All cases also satisfy the sharper maximum-cycle-length bound.

The exact surviving demand is stable by d steps, and its mass is

    (1/d) sum_over_cycles C max(sum_(z in C) f(z)-cardinality(C), 0).

Here is an independent proof of the bound and formula. A positive supply surviving a full cycle has traversed every site. At every visit some supply was left after matching, so that site's remaining demand became zero. Demand never increases. Thus, after the cycle length, either supply is exhausted or demand is exhausted on that cycle. Their conserved difference is the initial demand sum minus the cycle length. This proves the formula, strict positivity for unbalanced targets, and filling for balanced targets within d rounds. Concentrating all d units of demand at one point of a d-cycle attains the bound.

Named exact cases, with states numbered from 0 and each listed cycle oriented by theta:

| Example | Cycles | Target density f | First b-zero index | Residual at n=size | Exact r_0,...,r_size |
| --- | --- | --- | --- | --- | --- |
| fractional_swap | (0, 1) | (3/2, 1/2) | 2 | 0 | (1, 1/4, 0) |
| mixed_cycles | (0, 1); (2, 3, 4) | (3/2, 1/2, 0, 1, 2) | 3 | 0 | (1, 3/10, 1/5, 0, 0, 0) |
| six_cycle_fractional | (0, 1, 2, 3, 4, 5) | (0, 3/2, 1/2, 2, 1, 1) | 4 | 0 | (1, 1/4, 1/12, 1/12, 0, 0, 0) |
| six_cycle_concentrated | (0, 1, 2, 3, 4, 5) | (0, 0, 0, 0, 0, 6) | 6 | 0 | (1, 5/6, 2/3, 1/2, 1/3, 1/6, 0) |
| unbalanced_two_cycles | (0, 1); (2, 3) | (3/2, 3/2, 1/2, 1/2) | never | 1/4 | (1, 1/4, 1/4, 1/4, 1/4) |
| unbalanced_identity | (0); (1) | (1/2, 3/2) | never | 1/4 | (1, 1/4, 1/4) |

The program independently enumerates every initial point and its survive/stop branches using g_n. This recovers endpoint probabilities (f-b_d)/d and survivor probability r_d identically, including the unbalanced cases. Thus it checks the construction of N, not just the density recursion.

Three examples were each sampled 50,000 times using independent exact rational Bernoulli coins: draw an integer uniformly from 0 through denominator(g_n)-1 and compare it to numerator(g_n). This has precisely the same stopping probability as an independent uniform U_n. Endpoint vectors list states in order 0,...,d-1.

| Example / seed | Endpoint counts (50,000) | Exact endpoint probabilities | Empirical probabilities | Largest absolute error |
| --- | --- | --- | --- | --- |
| fractional_swap / 7100 | (37565, 12435) | (3/4, 1/4) | (0.7513, 0.2487) | 0.00130 |
| mixed_cycles / 7101 | (15030, 5119, 0, 10039, 19812) | (3/10, 1/10, 0, 1/5, 2/5) | (0.3006, 0.10238, 0.0, 0.20078, 0.39624) | 0.00376 |
| six_cycle_fractional / 7102 | (0, 12332, 4198, 16765, 8299, 8406) | (0, 1/4, 1/12, 1/3, 1/6, 1/6) | (0.0, 0.24664, 0.08396, 0.3353, 0.16598, 0.16812) | 0.00336 |

The stopping-time distributions were also recorded:

| Example | Exact probabilities P(N=0),P(N=1),... | Sample time counts |
| --- | --- | --- |
| fractional_swap | (3/4, 1/4) | (37451, 12549) |
| mixed_cycles | (7/10, 1/10, 1/5, 0, 0) | (35029, 5011, 9960, 0, 0) |
| six_cycle_fractional | (3/4, 1/6, 0, 1/12, 0, 0) | (37543, 8232, 0, 4225, 0, 0) |

The empirical differences are consistent with sampling noise. Exact branch enumeration, rather than simulation, establishes equality in these finite examples.

## Attributions and novelty: memory only

I did not consult external sources. GAP in this table means a specific source or priority claim remains unverified, not that the proved existence result is false.

| Attribution / statement | Verdict | Memory and confidence |
|---|---|---|
| Lines 36,68,162: ChaconOrnstein/Rost filling-scheme lineage | CORRECT in broad attribution | High confidence that this is classical filling-scheme mathematics and that Rost's stopping-distribution work is the relevant embedding lineage. ChaconOrnstein's 1960 paper is an ergodic-theorem source; I cannot certify from memory how much of the explicit stopping construction should be credited to that paper rather than Rost's later work. |
| Lines 70,162: DellacherieMeyer Chapter IX, nos. 6374 and no. 69 | GAP in source verification only | I remember this as a standard source for filling/embedding theory, but not these exact numbered statements or all their hypotheses. The paper supplies no excerpt to verify. This is not a gap in the main proof, which never invokes them. |
| Line 70: AldousThorisson and Thorisson invariant-field criterion | CORRECT as classical antecedent; discussion understates it | High confidence: agreement on the invariant sigma-field iff shift-coupling exists is an established theorem, not just a related question. For an invertible integer action, a coupling with two shifts can be rewritten as one signed shift. The invariant-field characterization in the paper must not be presented as new without a precise comparison. |
| Implicit novelty of [thm:filling] | GAP in novelty substantiation | The supplied discussion does not distinguish its exact formulation from classical shift-coupling and Rost embedding results. Arbitrary measurable E, a one-direction nonnegative shift, and this explicit proof should be compared separately with prior hypotheses and conclusions. No new criterion is established as new merely by the supplied references. |
| Does standard shift-coupling immediately prove the stated nonnegative-N theorem? | CORRECT to distinguish the formulations | A generic two-sided shift-coupling gives a signed shift after subtraction, which alone does not justify replacing the shift by a nonnegative one. I do not remember the exact forward-shift formulation in the cited Thorisson sources sufficiently to say it directly includes (i). The stationary-law Rost embedding formulation does yield this existence result and hence the Brownian application; the paper already attributes its construction to Rost. |
| Line 70: Liggett and HolroydPeres extra-head schemes | CORRECT in broad attribution | High confidence: choosing a random origin so the origin is a head/Palm point is the appropriate analogy, and f=2*1{x_0=1} is exactly the fair-bit extra-head target on two-sided configurations. I am not verifying exact historical priority or every bibliography field. |
| Lines 70,162: PitmanTang path-pattern and embedding connection | CORRECT in broad topic | Moderate confidence: these works concern finding path laws, including conditioned Brownian pieces, by time/space shifts and use filling ideas. I cannot verify Section 3.5, its precise meander domination hypothesis or the page data from memory. These exact claims need a source check. |
| Line 70: LastMortersThorisson unbiased shifts and nonnegative embeddings | CORRECT to the best of memory | Moderate-to-high confidence that they characterize unbiased two-sided Brownian shifts using local-time transport and construct nonnegative stopping embeddings of arbitrary probability distributions. I cannot certify the exact filtration convention or theorem formulation from memory; this result is separate from changing the full forward path law here. |
| Is Problem 7.5 already answered by another paper? | GAP in priority verification | I do not remember a specific published paper answering that numbered problem. This is not evidence of absence, and I will not invent a reference or certify a priority claim without a literature check. |

The introduction should say more than close to shift-coupling: the invariant-field equivalence is already classical. In an invertible action a two-shift coupling reduces to a signed shift, but this formal subtraction alone does not ensure a nonnegative shift. I do not remember enough of the exact Thorisson forward formulation to determine whether it directly states (i). Rost's stationary embedding theorem is the other classical route to this forward existence statement; the paper already credits it. The defensible contribution here is the Brownian-prefix application and its explicit proof, unless a precise source comparison establishes more. I cannot certify first resolution of Problem 7.5 and do not remember a specific contrary paper.

## Typos and unclear sentences

I found no consequential algebraic typo, wrong sign or missing index. These are the wording/version points noticed during the audit; many are optional clarifications of valid mathematics.

| PAPER.tex lines | Wording / location | Suggested clarification |
| --- | --- | --- |
| 55,157 | on an extension of the probability space | State explicitly that X is preserved by pullback and that Brownian means the Wiener path law, or Brownian relative to its own filtration. No claim is made about a filtration containing the entire original sigma-field at time zero. |
| 62 | The time N looks into the future, and it has to. | Qualify by Q different from Wiener measure; N=0 works for the Wiener target. |
| 70 | is close to the questions on shift-coupling | Explain the existing invariant-sigma-field equivalence theorem explicitly and distinguish signed from forward shifts. This is a novelty clarification. |
| 74 | a random element Y ... has the subprobability law hP | An unconditional law of an everywhere-defined random element has total mass one. Say restricted law on an event, a subprobability measure, or add a cemetery state. Actual uses are restricted laws and are valid. |
| 99 | by monotone convergence | b_n decreases. Cite dominated convergence, or apply monotone convergence to f-b_n; the stated conclusion is correct. |
| 112 | the mean ergodic theorem in L1 | Correct here. A brief bounded-truncation/L2 argument would avoid confusion with false statements about arbitrary L1 contractions. |
| 134,140 | N=inf{...} | Use inf(empty set)=infinity until finiteness is proved, then set N=0 on the null infinite-survival event if literally N-valued N is desired. |
| 149 | lies, up to a null set, in the tail sigma-field | The approximation argument is compressed; clarify completed tail fields or use the finite-cylinder mixing proof supplied here. |
| 157 | transfer theorem ... Theorem 6.10 | Mathematically valid. Add the disintegration kernel formulation if desired; the printed theorem number has not been checked. |
| 162 | every nonnegative measurable N ... is a randomized stopping time | Say nonnegative integer-valued N and specify that the whole independent random seed is available initially. With sequentially revealed U_n, not every arbitrary function of future uniforms is a stopping time. |
| 162 | self-contained proof | Accurate for the filling argument relative to standard ergodic theory; it still cites the mean ergodic theorem. |
| 170 | a density with values in {0,1,2,...} | Say integer-valued almost surely, or choose a finite version. The indicator sum can be infinite on a null set. |
| 174 | the first n with x_n=1, which has mean one | Specify n>=0. With n>=1, the mean would be two. |
| 174 | infinite sum if the pattern continues | This conditional wording is correct. It can be strengthened to the all-n ballot formula proved here. |
| 177 | within cardinality(E) steps | Specify cardinality(E) removal rounds, numbered 0 through cardinality(E)-1. Equivalently b_d=0 and the stopping time is at most d-1. |
| 30,235 | 16 October 2026 date; October 24 Math Brain paper identifier | Possible version-date inconsistency: a reference identifier postdates the displayed manuscript date. This may reflect a later bibliography update; check it. |
| 201 | No data were used. | For clarity, distinguish no external datasets from the generated exact-computation outputs. This has no effect on the mathematics. |

## Limits of this audit and reproducibility

The original BurdzyScheutzow paper was not supplied, so I checked the question as quoted here, not its verbatim transcription, original page number or any conventions elsewhere in that paper. I could not source-check Kallenberg's theorem number, DellacherieMeyer's numbered statements, PitmanTang's section number and exact hypotheses, bibliographic metadata, funding/history declarations, or the latest priority status. No author repository was opened. I did not compile the LaTeX, audit the author's unseen programs, or settle deterministic B-only measurability in the Brownian theorem. The general invariant-field criterion and Brownian theorem were checked by proof; finite tests are supporting checks and not substitutes for that proof.

Files: `LOG.md`, `bernoulli_exact.py`, `finite_exact.py`, `make_report.py`, `bernoulli_results.json`, `finite_results.json`, `bernoulli_stdout.txt`, `finite_stdout.txt`, and this report. Rebuild with:

```sh
python3 bernoulli_exact.py > bernoulli_stdout.txt
python3 finite_exact.py > finite_stdout.txt
python3 make_report.py
```

Measured final numerical runs:

| Program | Elapsed seconds | Peak resident memory (MiB) |
| --- | --- | --- |
| bernoulli_exact.py | 0.018763 | 19.42 |
| finite_exact.py | 1.803248 | 18.25 |

Each numerical program has a 240-second internal guard, uses one process and no numerical worker libraries. Runs were sequential. An initial attempt to lower priority with nice was refused by the sandbox; that first tiny Bernoulli run still completed in approximately 0.017 seconds. No heavy computation was started. Source hashes match both result files.

Task: You are refereeing a mathematical paper that is already public but has had no outside audit. Received in this run at approximately 2026-11-12 05:05 +04; the exact message timestamp is unavailable, so this is the first observed local clock time.

Overall verdict: **SOUND**.
