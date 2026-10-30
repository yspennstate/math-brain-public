TASK: B17 ACCOUNT: fleet02 RUN: 2026-09-21T15:48:09.324537Z — buried-atom derivative lattice, unbounded receiver congestion, and signed cancellation replacement

MODEL: GPT-5.6 Sol (runtime self-report). Requested effort: maximum actually exposed. Configured reasoning selector: UNKNOWN / NOT_EXPOSED by the scheduler interface. Provider reasoning tokens/time: NOT_EXPOSED. Execution: WITHOUT_VERIFIED_BRAIN. Observed elapsed work through the scientific snapshot: 1070.158 s, explicitly not pure thinking.

STATUS: PARTIAL. The full Friedgut–Kalai Fourier entropy-influence conjecture remains OPEN / NOT PROVED.

Normalization: f:{0,1}^n->{-1,+1}, normalized Walsh coefficients a_S=\hat f(S), p_S=a_S^2, spectral entropy H(f)=sum_S p_S log_2(1/p_S), total influence I(f)=sum_S |S|p_S.

Fresh scientific source at entry: yspennstate/math-open-problems master c687362ab487b56d0b9aa2c7c5c3dcf017ec3156. The newest own B17 report at entry was the central-cone normal form. Relevant newer neighboring work included fleet01/B17's exact signed-autocorrelation characterization and maximal-support granularity lemma, and fleet04/B17's exact no-amplification theorem for affine tensor products. This run does not duplicate those results: it starts from the “buried coefficient” obstruction and tries to build the missing bounded-congestion charging mechanism.

FLEET_RULES moves, deliberately different from the immediately preceding own route (#3/#6/#23):
- #11 DUALIZE: turn buried-atom entropy debt into a finite max-flow/min-cut problem on strict support inclusions.
- #20 FIND WHY THE ALGORITHM FAILS: construct an exact all-dimensional Boolean family with unbounded receiver-only congestion.
- #25 COUNT THE SAME THING TWICE: identify strict-superset mass simultaneously as a derivative variance and as Fourier cone mass, then use signed xor autocorrelation to expose the missing lateral resource.

No publication-priority or novelty claim is made. Current primary literature checked this run includes O'Donnell–Tan's composition theorem, Hod's recursive lower-bound construction, Xiao Han's coordinate-influence entropy bound, and Potapov's 18 Sep 2026 plateaued/partially-bent class theorem. None of those sources was used as authority for the new lemma below.

## 1. Before / after

Before this run, the strongest compatible route statement was:

- every inclusion-maximal Fourier atom has |a_S| >= 2^{1-|S|}, hence maximal atoms pay entropy with FEI constant 2;
- therefore any genuinely hard entropy must lie in nonmaximal “buried” coefficients;
- the missing theorem was a bounded-congestion charge from a buried coefficient to strict spectral supersets.

After this run:

1. I prove a universal **local derivative-lattice debt inequality** quantifying exactly how much a buried coefficient can fall below its maximal-support dyadic scale.
2. I formulate the resulting strict-superset transport as an exact max-flow/min-cut invariant kappa(f), and prove the sufficient implication
       H(f) <= (2+kappa(f)) I(f).
3. I then disprove the hoped-for universal bound kappa(f)=O(1) by an exact source-admissible Boolean family: two antipodal defects in every even dimension n have kappa(f) >= n-1, while the same family satisfies H(f)<4 I(f). Thus receiver-only support-poset transport is decisively the wrong universal mechanism.
4. The obstruction identifies the missing resource: **signed xor-cancellation partners**. For every nonzero shift U, Booleanity makes the U-orbit products sum to zero. I record the exact orbit-balance lemma and a replacement two-channel route that must use those lateral partners rather than charge only strict supersets.

The measurable mechanism gain is therefore not a better FEI constant. It is a reduction-and-refutation:
- local debt constant: exact analytic 2/ln 2 = 2.8853900817779268...;
- proposed universal receiver-only congestion: REFUTED, with lower bound n-1 on an explicit even-n Boolean family;
- remaining universal gap: bounded signed-cancellation-partner transport.

## 2. PROVED: derivative-lattice debt inequality

Fix a nonempty S subseteq [n], m=|S|, and put

    q_S := sum_{T superset S} p_T,
    delta_S := 2^{1-m}.

Define the normalized additive derivative on the complementary cube

    D_S f(x_{S^c})
      = 2^{-m} sum_{z in {0,1}^S} (-1)^{|z|} f(z,x_{S^c}).

Its Fourier expansion is

    D_S f = sum_{R subseteq S^c} a_{S union R} chi_R.

Consequently

    E D_S f = a_S,
    E (D_S f)^2 = q_S.                                      (2.1)

Because D_S f is an alternating average of 2^m values in {-1,+1}, the unnormalized alternating sum is an even integer. Hence pointwise

    D_S f in delta_S Z.                                      (2.2)

Set Y=D_S f/delta_S and mu=E Y=a_S/delta_S. Then Y is integer-valued and

    Var(Y) = (q_S-p_S)/delta_S^2.                            (2.3)

### Integer-mean lemma

For any integer-valued Y with |E Y|<=1,

    Var(Y) >= |mu|(1-|mu|).                                 (2.4)

Proof. By replacing Y by -Y assume 0<=mu<=1. Pointwise Y(Y-1)>=0 for every integer Y, so E Y^2>=E Y=mu. Therefore
Var(Y)=E Y^2-mu^2 >= mu-mu^2. QED.

Now define the positive dyadic entropy deficit

    d_S := [ p_S log_2(delta_S^2/p_S) ]_+,                  (2.5)

with d_S=0 when p_S=0. If |mu|>1 then p_S>delta_S^2 and d_S=0. If 0<=|mu|<=1, then p_S=delta_S^2 mu^2 and

    d_S
      = delta_S^2 mu^2 log_2(1/mu^2)
      = (2 delta_S^2/ln 2) mu^2 ln(1/mu).

Using mu ln(1/mu)<=1-mu,

    d_S <= (2/ln 2) delta_S^2 mu(1-mu)
          <= (2/ln 2)(q_S-p_S).

Thus for every nonempty Fourier atom,

    boxed:
    d_S <= (2/ln 2) sum_{T strictly superset S} p_T.         (2.6)

The scalar constant 2/ln 2 is sharp for this one-variable integer-variance argument as |mu|->1.

If S is inclusion-maximal in the Fourier support then q_S=p_S, so (2.6) forces d_S=0, equivalently
p_S>=delta_S^2 or |a_S|>=2^{1-|S|}. Thus the preceding maximal-support granularity lemma is exactly the zero-variance endpoint of (2.6).

## 3. Strict-superset flow reduction

Let D be the set of nonempty support atoms with d_S>0. Build a finite bipartite transport network:

- each source S in D has demand d_S;
- each nonempty supported receiver T has capacity lambda |T|p_T;
- S may send only to strict supported supersets T supersetneq S.

Define kappa(f) as the least lambda for which all demands can be routed.

Equation (2.6) implies every positive-demand S has at least one strict supported receiver, so kappa(f)<infinity for every finite Boolean f.

By max-flow/min-cut,

    kappa(f)
      = max_{A subseteq D}
          [ sum_{S in A} d_S ]
          /
          [ sum_{T in N(A)} |T|p_T ],                       (3.1)

where N(A) is the union of strict supported supersets of members of A. This is an exact Hall-type obstruction.

### Theorem 3.1 — bounded kappa would imply FEI

For every Boolean f,

    boxed: H(f) <= (2+kappa(f)) I(f).                       (3.2)

Proof. Let r=sum_{S nonempty}p_S=1-p_empty. For nonempty S of size m,

    p_S log_2(1/p_S)
      = 2(m-1)p_S + p_S log_2(delta_S^2/p_S)
      <= 2(m-1)p_S + d_S.

Summing,

    H_nonempty <= 2(I-r) + sum_S d_S
               <= 2(I-r) + kappa(f) I.

For the empty coefficient, using -ln x <= x^{-1}-1,

    -p_empty log_2 p_empty
      <= (1-p_empty)/ln 2
      < 2r.

Adding gives H(f)<=(2+kappa(f))I(f). QED.

This is only a sufficient reduction. The next section shows that its hoped-for dimension-independent premise is false.

## 4. DISPROVED stronger lemma: receiver-only congestion is not bounded

A tempting strengthening of (2.6) is:

> False receiver-packing lemma. There is an absolute K such that kappa(f)<=K for every Boolean f.

This is false, even for a two-defect family with an elementary exact spectrum.

For every even n>=4, let f_n be +1 everywhere except at the two antipodal points 0^n and 1^n, where it is -1. Write N=2^n and epsilon=4/N=2^{2-n}.

Its exact Walsh spectrum is

    a_empty = 1-epsilon,
    a_S     = -epsilon   for every nonempty even |S|,
    a_S     = 0          for odd |S|.                       (4.1)

Hence every nonempty supported atom has the same mass

    p := epsilon^2 = 2^{4-2n}.                              (4.2)

Consider all S of size n-2. There are binom(n,2) of them. Since n is even, each is supported. For such S,

    delta_S^2 / p
      = 2^{2-2(n-2)} / 2^{4-2n}
      = 4,

so

    d_S = 2p.                                               (4.3)

What strict supported supersets can S have? Size n-1 is odd and therefore absent. The only one is T=[n]. Its entire receiver capacity at lambda=1 is

    |T|p_T = n p.                                          (4.4)

Therefore the Hall cut consisting of all binom(n,2) near-top atoms gives

    kappa(f_n)
      >= [2p binom(n,2)]/[np]
      = n-1.                                                (4.5)

Thus

    boxed: sup_f kappa(f)=infinity.                         (4.6)

So no receiver-only strict-superset charging theorem can prove universal FEI through (3.2), no matter how the local scalar constant is optimized.

### This family is not an FEI counterexample

Its influence is

    I(f_n)= n epsilon = n 2^{2-n}.                          (4.7)

Its entropy can be written exactly as

    H(f_n)
      = - (1-epsilon)^2 log_2((1-epsilon)^2)
        + (2^{n-1}-1) epsilon^2 log_2(1/epsilon^2).         (4.8)

Since the nonempty spectral mass is r=2epsilon-epsilon^2<=2epsilon and
-log(1-epsilon)<=epsilon/(1-epsilon),

    H(f_n)
      <= (2/ln 2) epsilon + 4(n-2)epsilon
      < 4n epsilon
      = 4 I(f_n).                                           (4.9)

Hence this exact Boolean family has **unbounded receiver congestion while remaining FEI-easy with constant 4**. It refutes only the stronger receiver-only transport lemma, not FEI.

At n=4 the spectrum is especially transparent:
p_empty=9/16, and p_S=1/16 on all six 2-sets and on [4]. Each 2-set has exact debt 1/8, all six share the single top receiver of capacity 1/4, and therefore kappa=3 exactly. There are no supported size-3 intermediates, so one-step Hasse-edge transport fails as well.

## 5. What the obstruction reveals: signed xor-cancellation is the missing resource

The two-antipodal family explains why the poset flow overcharges. A near-top atom S=[n]\U, with |U|=2, collides with all other near-top atoms at the same top receiver. But every such S has a distinct complementary pair U. Those low-level atoms are real spectral mass and are invisible to a receiver-only upward flow.

Booleanity supplies exactly the lateral relation that sees them. Let a_A=\hat f(A). Since f^2=1,

    sum_A a_A a_{A xor U} = 0                              (5.1)

for every nonzero U.

Partition the cube of Fourier indices into unordered xor-U orbits {A,A xor U}. Then

    sum_orbits a_A a_{A xor U}=0.                           (5.2)

Therefore for any chosen orbit {S,T=S xor U},

    boxed:
    |a_S a_T|
      <= sum_{other xor-U orbits}
            |a_A a_{A xor U}|.                              (5.3)

This is a genuine cancellation certificate, not an absolute-value replacement of the Boolean equations: it follows by isolating one signed orbit in the exact zero sum and applying triangle inequality only after the cancellation identity is written.

In the two-antipodal family, taking T=[n] and U=[n]\S pairs every bad near-top S with a distinct 2-coordinate shift U. The low-level complementary atoms and the other even-even xor-U orbits supply the cancellation balance that the top receiver alone cannot pay. The n-1 divergence of kappa is therefore a **false bottleneck created by throwing away signed lateral structure**.

## 6. Replacement proof route

The next universal target should not be another bound on kappa(f). It should be a two-channel signed transport indexed by xor shifts U.

A workable formulation must combine:

1. **vertical derivative debt** — (2.6) says every entropy deficit d_S is generated by strict-superset variance;
2. **signed lateral cancellation** — for each selected inclusion S subsetneq T with U=T\S, equation (5.2) supplies opposite-sign xor-U partner orbits;
3. **influence-weighted congestion** — partner endpoints must be charged with a bounded total coefficient over all U, without assuming a prescribed single partner such as a_empty a_U pays every edge.

The last clause is essential. A “prescribed complement pays” lemma would repeat a known killed shortcut: (5.2) only guarantees aggregate cancellation across the entire U-orbit partition, not that one named partner has sufficient size.

A precise next lemma is therefore:

> Signed partner-packing target. Decompose each d_S among strict supersets T and then, for U=T\S, among opposite-sign xor-U partner orbits, so that the total charge incident to a Fourier atom A is O(|A|p_A), after allowing a bounded scalar reserve for the empty atom.

The two-antipodal family passes this architecture for the reason the receiver-only flow fails: its near-top demands have distinct shifts U and can access distinct low-level cancellation structure. Proving such a packing with a dimension-independent constant would feed directly into the entropy decomposition in Section 3.

I have not proved this packing theorem. That is the current universal gap.

## 7. Exact finite sanity checks

The accompanying standard-library checker uses integer Walsh transforms and exact Fraction arithmetic. It executed successfully and checked:

- all 65,812 Boolean functions in dimensions 1 through 4;
- 791,324 nonzero nonempty Fourier coefficients;
- 697,964 exact integer-variance inequalities in the |mu|<=1 regime;
- 87,948 maximal-support granularity endpoints;
- the n=4 antipodal witness with exact kappa=3;
- an n=3 Hasse-skip witness whose buried singleton has a strict size-3 receiver but no supported immediate size-2 receiver;
- the two-antipodal spectral/congestion formulas at n=4,6,8,10, obtaining receiver lower bounds 3,5,7,9.

Finite checks establish only this tested implementation scope. The derivative-lattice theorem and the all-even-n congestion counterexample are analytic.

Checker SHA-256:
01f6ef551fffe3e12675c75cd6de6f77f9c5c304e70ddd0596f84059aeed5566

Recorded stdout SHA-256:
4ed09def5a3303d0599272bcb179b02a356b07863d15450a5c76f52661b0dbf4

## 8. Literature applicability

Primary literature checked on 21 Sep 2026:

- O'Donnell–Tan (2013, arXiv:1304.1347): composition theorem for FEI; relevant background for recursive/tensor mechanisms, not this strict-superset flow.
- Hod (2017, arXiv:1711.00762): recursive lexicographic lower bounds, including >6.454784; confirms high ratios are compatible with recursive Boolean constructions.
- Xiao Han, Combinatorica 45 (2025), arXiv:2312.08271: H(f)=O(I(f)+sum_i I_i log(1/I_i)) using iterative Fourier moment bounds. It does not provide the signed subset-lattice packing derived here.
- Potapov (arXiv:2609.21563, 18 Sep 2026): FEI with sharp constant 4 for plateaued functions and 2 for partially bent functions; it does not imply the universal signed partner-packing target.

A bounded search did not locate a published statement of the exact derivative-lattice debt inequality (2.6) or the kappa flow formulation. That search miss is not a novelty proof, and no priority claim is made.

## 9. Scientific ledger

PROVED:
- derivative identities (2.1), dyadic lattice (2.2), integer variance (2.4);
- local entropy debt inequality (2.6);
- exact Hall/max-flow formulation (3.1);
- sufficient FEI reduction H<=(2+kappa)I;
- all-dimensional exact Boolean family with kappa(f_n)>=n-1;
- same family satisfies H(f_n)<4I(f_n);
- xor-orbit cancellation certificate (5.3).

DISPROVED:
- universal bounded receiver-only strict-superset congestion;
- same-local-constant packing kappa<=2/ln2 (already n=4 has kappa=3);
- one-step Hasse-only support transport.

OPEN:
- signed xor-partner packing with influence-weighted bounded congestion;
- full FEI.

This run therefore changes the universal route rather than adding another lemma to an unchanged receiver-only scheme: the poset-only algorithm is dead, and any surviving buried-atom proof must spend the signed cancellation structure that fleet01's perfect-autocorrelation characterization preserved.
