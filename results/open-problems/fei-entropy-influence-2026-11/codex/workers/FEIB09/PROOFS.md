# Containment proofs and referee notes

All logarithms are base 2 unless `ln` is written. A_r denotes the brief's truncated L2 cost. A_L1 denotes FLOW.md's differently named A1. Statements below marked PROVED have full arguments here; numerical checks are recorded separately.

## 1. Referee of FLOW.md section 2

PROVED: the flow and telescoping identities are correct, with these conventions. Set m(empty)=1 and alpha(empty)=1. Then

    sum_R m(R) = E(|S|+1) = I+1,
    sum_{R nonempty} m(R) = I.

For fixed S and a uniform ordering of its elements, the probability of visiting R subset S, |R|=j, is 1/binom(|S|,j). Conditional on visiting R, the last element into R is uniform in R. Summing the telescoping increments log(alpha(R-s)/alpha(R)) therefore gives exactly E log(1/alpha(S)). Derivatives contract L1, so the increments are nonnegative. A zero alpha(R) implies no positive spectral mass on any superset; omit such zero-flow terms. The phrase “m-average” uses the nonempty flow, of total I, rather than the full flow of total I+1.

PROVED: generalized Talagrand has the stated constant 1 for r=|R|>=1. Write q=up(R), a=alpha(R), L=ln(sqrt(q)/a)>=0. Expanding the noise operator and using the beta integral gives

    m(R)=r integral_0^1 ||T_sqrt(t) g_R||_2^2 (1-t)^(r-1) dt.

Bonami hypercontractivity gives ||T_sqrt(t)g||_2<=||g||_(1+t). Interpolation between L1 and L2, with theta=(1-t)/(1+t), gives

    ||g||_(1+t)^2 <= ||g||_2^2 exp(-2 theta L)
                     <= q exp(-(1-t)L).

Thus m(R)<=q, and extending the last nonnegative integral from [0,1] to [0,infinity) gives m(R)<=q r!/L^r. At L=0 retain just m<=q. For r=1, g_i is {0,+1,-1}-valued, so a=q and L=(1/2)ln(1/q), giving m(i)<=2q/ln(1/q). These are upper bounds, not an assertion that the constant in the underlying sharp integral is attained for every L.

PROVED: the size statement is correct for real g_R, 0<rho<=1, integer k>=0. In its Fourier expansion the terms of degree at most k have rho^(2 degree)>=rho^(2k). Consequently

    sum_{S superset R, |S-R|<=k} mu(S)
      <=rho^(-2k)||T_rho g_R||_2^2
      <=rho^(-2k)||g_R||_(1+rho^2)^2.

“Almost all supersets” must refer to spectral mass normalized by up(R), not to the number of supersets. The quantitative conclusion needs L large and k a sufficiently small multiple of L. It does not assert anything when L is small.

PROVED: the printed level-1 argument works. For singleton i, ||g_i||_(4/3)^2=q_i^(3/2). With k measuring |S|-1 the direct bound is 3^k q_i^(3/2); FLOW.md's use of 3^k when k bounds |S| is weaker and valid. Charge each S to a coordinate of minimum q_i, resolving ties deterministically. Large |S| pay 4 log2(3)|S|; the small cases are bounded by sum_i q_i^(5/4) log2(1/q_i), which is at most 4I/(e ln2). Thus its displayed split yields an explicit valid constant 4 log2(3)+4/(e ln2). It does not establish the sharp constant.

## 2. A better explicit level-1 constant

PROVED: for every 0<t<1,

    A_1 <= C_1(t) I,
    C_1(t) = (1+t)/(1-t) * [ln(1/t)+t/e]/ln 2.

Proof. For each nonempty spectral set S choose i(S) in S minimizing q_i=up(i). Let nu_i be the mass assigned to i, v=Var(f), T=(ln2)A_1, and b=(1-t)/(1+t). Hypercontractivity for the singleton derivative gives

    sum_{S contains i} t^(|S|-1) mu(S) <= q_i^(1+b).

Jensen on the assigned submeasure, of mass nu_i, gives

    (1+b) nu_i ln(1/q_i)
      <=nu_i ln(1/nu_i)+ln(1/t) sum_{i(S)=i} (|S|-1) mu(S).

Sum over i. The log-sum inequality, sum q_i=I, and sum nu_i=v imply

    b T <= v ln(I/v)+ln(1/t)(I-v).

When v=0 the assertion is trivial. Otherwise set x=I/v>=1. The coefficient of I on the right, divided by b, is

    [ln(1/t)+(ln x-ln(1/t))/x]/b.

Its maximum over x>=1 is at x=e/t, and equals [ln(1/t)+t/e]/b. Divide by ln2.

Within this one-parameter argument the optimal t is unique. The derivative of C_1(t), after multiplying by the positive factor (1-t)^2 ln2, is

    N(t)=2 ln(1/t)-1/t+t+(1+2t-t^2)/e.

Its derivative is (1-t)^2/t^2+2(1-t)/e>0. It changes sign once, so the unique root minimizes the constant. A numerical minimizer is about 0.31237287; this is an optimization of the proof bound, not a sharpness assertion about Boolean functions.

Use the explicit rational t=312373/1000000. Its exact expression C_1(t) is the proved constant; constants.json evaluates it at high precision. In particular A_1<=3.520226 I.

PROVED: any universal constant for A_1/I is at least 2. For AND_n, q_i=2^(1-n), every nonempty spectral coefficient has square 2^(2-2n), and

    A_1/I = 2(n-1)(1-2^(-n))/n -> 2.

OPEN: the optimal universal constant. The phrase “best constant” here means the best explicit upper bound proved in this report; neither the scalar optimization nor the census proves that it is sharp over Boolean functions. No function is claimed to need 3.520226. AND_n needs the limiting lower bound 2.

## 3. A dimension-free bound at every fixed level

PROVED: if A_1<=c I, then, for every integer r>=1,

    A_r <= (r c + 1/ln2) I.

This already answers the fixed-r existence question, including r=2 and r=3. It does not give a constant independent of r.

Proof. For each S choose R(S) subset S, |R(S)|<=r, minimizing up(R). Resolve ties deterministically, set R(empty)=empty, and let nu be the distribution of R(S). Then nu(R)<=up(R) for nonempty R, so A_r<=H(nu). Put q_i=up(i), and disregard coordinates with q_i=0 (they never occur). Use the probability measure

    pi(R) = product_{i in R} q_i / product_i(1+q_i)

on all subsets. Gibbs' inequality and ln(1+q_i)<=q_i give

    (ln2)A_r <= (ln2)H(nu)
      <= E sum_{i in R(S)} ln(1/q_i) + sum_i ln(1+q_i)
      <= r (ln2) A_1 + I.

The middle entropy is in bits; multiplying it by ln2 converts it to natural units. This proof uses no higher-order influence budget, no granularity, and no LP fit.

## 4. Better pair bound: A_2 <= 6.1033 I

PROVED: let c be the exact constant from section 2, take any 0<t<1, b=(1-t)/(1+t), a=1+b=2/(1+t). Then

    A_2/I <= [2c + {ln(1/t)+sqrt(2)t/e}/ln2 + b]/a.

Taking t=9/50 yields A_2<=6.1033 I (exact evaluation in constants.json).

Proof. For |S|>=2 choose its minimizing pair R(S); monotonicity permits a pair rather than a singleton. For singleton S choose R=S. Write T_0 for the natural-log singleton contribution, T_1 for E[1_{|S|>=2} max_{i in S} ln(1/q_i)], T_2 for the pair contribution, and v=Pr[|S|>=2]. Thus (ln2)A_2=T_0+T_2 and (ln2)A_1=T_0+T_1.

For a pair R put q_R=up(R) and let nu_R be its assigned mass. A second derivative takes values in (1/2)Z intersect [-1,1], so alpha(R)<=2q_R. Interpolation and hypercontractivity give

    sum_{S contains R} t^(|S|-2) mu(S)
      <=||g_R||_(1+t)^2 <= 2^(2b) q_R^a.

Jensen on the assigned submeasure therefore gives, after summing pairs,

    a T_2 <= sum_R nu_R ln(1/nu_R)
              +ln(1/t)(E[|S|;|S|>=2]-2v)+2b ln2 v.

Let Z=sum_{i<j} q_i q_j<=I^2/2. Gibbs on pair weights q_i q_j/Z shows

    sum_R nu_R ln(1/nu_R) <=2T_1+v ln(Z/v).

The formula is vacuous when v=0. Otherwise z=I/v>=2 and v<=1. With h=ln(1/t),

    v ln(Z/v)+h(I-2v)
      <= I [h + (2ln z-ln2-2h)/z]
      <= I [h+sqrt(2)t/e].

The last one-variable maximum is attained at z=e sqrt(2)/t. Also 2b ln2 v<=b ln2 I. Finally a<=2 implies

    a(T_0+T_2)<=2(T_0+T_1)+I[h+sqrt(2)t/e+b ln2].

Divide by a ln2 and apply the level-1 theorem. The bound is in terms of I(f), never E binom(|S|,2).

## 5. A_3 and the induction obstruction

PROVED: a more uniform refinement, for any r>=1 and 0<t<1, is

    A_r/I <= C_r(t)
      = [r c + {ln(1/t)+t 2^(2b)}/ln2]/a,
    a=2/(1+t), b=(1-t)/(1+t).

For r=3, t=1/12 gives A_3<=7.872677 I. The exact expression, rather than a rounded decimal, defines the proved constant; see constants.json for the evaluation.

Proof. Choose minimizing R(S) of cardinality j=min(r,|S|), possible by monotonicity. Let nu_R be its mass. For j>=1, granularity gives alpha(R)<=2^(j-1)up(R). Hypercontractivity, interpolation, and Jensen, as above, imply

    a (ln2) A_r <= H_nat(nu_nonempty)
       +ln(1/t)(I-Ej)+2b ln2(Ej-Var).

Here H_nat(nu_nonempty)=sum_{R nonempty} nu_R ln(1/nu_R), not a conditional entropy. It is at most H_nat(nu), including the empty atom. For every real lambda use the probability measure proportional to product_{i in R}(q_i exp(-lambda)) on all subsets. Gibbs gives

    H_nat(nu) <= r (ln2) A_1+lambda Ej+exp(-lambda)I.

Choose lambda=ln(1/t)-2b ln2. The Ej terms cancel, leaving

    a (ln2) A_r <= r (ln2)A_1+[ln(1/t)+t2^(2b)]I-2b ln2 Var.

Discard the last nonpositive term and apply section 2.

OPEN: a constant independent of r, and therefore the full containment conjecture. The factor r enters through sum_{i in R}ln(1/q_i)<=r max_{i in S}ln(1/q_i). For AND_n, all singleton influences coincide and the endpoint sum is exactly r times the maximum whenever |S|>=r, so that pointwise step itself cannot be replaced by a constant independent of r. This is a proved source of loss in this argument, not a counterexample to containment. Keeping a fixed p or choosing cheaper chains does not remove that entropy cost by itself. The pair proof succeeds, so there is no obstruction family disproving A_2. Candidate (a)'s inequalities are valid, but its summed budget is 2 E binom(|U|,2), which is not O(I); majority demonstrates that. Candidate (b) is realized by the selector nu; its entropy, rather than a raw count of pairs, is what pays the cost. Candidate (c) avoids an exponential constant in the norm estimate: granularity contributes linearly after taking logarithms, but the remaining estimate above still grows with r.

## 6. What a finite universal-rule LP does and does not prove

CHECKED: lp_rules.py fits one nonnegative rule simultaneously to all functions through four variables and the declared samples at five and six variables. A finite optimum is not a universal-in-dimension theorem.

The rules are zero unless S is nonempty, S subset U, mu(U)>0 and mu(S)>0. The families are

    size:    w(U,S)=theta[|U|,|S|],
    local:   w(U,S)=theta[|U|,|S|,b(S)],
    demand:  w(U,S)=(mu(S)/up(S))theta[|U|,|S|,b(S)],
    b(S)=floor(4 log2(sqrt(up(S))/alpha(S))).

The spectral-support gate is part of every family. A receiver with mu(S)=0 needs no transfer. The LP includes self transfers S=U, as does the subset convention in the brief, and uses the same C for the direct allowance and the donor budget. Output JSON files contain every nonzero theta, so they describe executable rules, not just optimal values.

PROVED: every family has simultaneous LP optimum at least 45/64 on the all-through-four-variable corpus. Summing all receiver inequalities and donor budgets gives A_L1<=2CI. For AND_4, alpha(S)=1/8 for every nonempty S, Var=15/64 and I=1/2, hence A_L1=45/64 and C>=45/64. CHECKED (exact integer arithmetic): the size-family rule at C=45/64 satisfies every constraint on every four-variable NPN class. It also belongs to the local family, by ignoring the bin. The demand family's matching optimum is checked in floating point. audit_lp.py / lp_exact_certificate.json contains the rational size rule and checks receiver logarithms by integer exponentiation, not floating-point tolerances. This does not infer an infinite-dimensional bound from the census.

## 7. An obstruction to a summable per-level induction

PROVED: there is no summable sequence d_r>=0 such that A_r(f)-A_(r-1)(f)<=d_r I(f) for every Boolean f and every r>=2. This rules out one natural form of induction with a fixed final constant, while leaving the containment conjecture open.

For AND_n and r>=2, the only change in the cost is the extra unit charged to each spectral S of size at least r. Therefore

    (A_r-A_(r-1))/I = (2/n) Pr[Bin(n,1/2)>=r].

Put n=2r. Symmetry gives the probability at least 1/2, so d_r>=1/(2r). The harmonic series diverges. The function changes with r in this argument; it is not a function whose total containment cost diverges relative to influence. Indeed

    A(AND_n)/I = 3-4/n-(n-2)2^(1-n)/n ->3.

PROVED: the raw pair and conditional-chain budgets fail dimension-free accounting on odd majority. The singleton derivative is the indicator of the middle layer of the other n-1 coordinates. Every neighbor leaves that layer, so ||D_j g_i||_2^2=up(i)/2 for every j!=i. Hence

    sum_{|R|=2}up(R)/I=(n-1)/4,
    sum_i sum_{j!=i}||D_j g_i||_2^2/I=(n-1)/2.

These unbounded ratios refute a budget shortcut, not A_2<=CI, which section 4 proves by a different accounting.

PROVED: the level-1/fixed-r bounds do not require an L1 chain. For |g|<=1 and p>=1, alpha<=||g||_p<=alpha^(1/p); consequently the spectral log-average cost using ||g_R||_p lies between A_L1/p and A_L1. A fixed p controls that norm comparison, but alone does not supply a bound uniform in r.

PROVED: the same summed-budget lower bound applied to AND_n forces C>=(n-1)(1-2^(-n))/n in any family of transfer rules valid in every dimension, hence C>=1 in the limit. This is a necessary constant, not a construction of a rule at C=1.
