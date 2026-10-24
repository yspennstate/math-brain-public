# Separated-conjunction prime payment

All logarithms in the proof are natural. Physical inputs are independent Bernoulli bits with interior probabilities. Write vi=4pi(1-pi), vS=product vi, cS=fhat(S)/sqrt(vS), P(S)=vS cS^2, delta=I-Var, E=sum_{S nonempty}P(S)ln(vS/P(S)). Thus E=(ln2)Hplus. Let C0=4+ln4 and K0=4+2C0=12+4ln2.

## 1. Independent scoped review of A042 stage 4

Source A042-RETAINED-SINGLETON-RESERVE-SELECTOR-ENDPOINT@1, statement hash 34db76116f2e3e71acdafec19f3dfa7494ce740480dca6a32187eced16171fbd. Its original REPORT, CLAIMS and PROOF were read. The following is independently reconstructed; no source repair is supplied.

If Di=(f|Yi=1-f|Yi=0)/2, ti=|E Di| and di=E Di^2, Parseval says sum vi(di-ti^2)=2delta-R, with R=sum_{|S|>=3}(|S|-2)P(S). Subtracting the singleton entropy gives exactly

    4delta-2R-E_single
      =sum_i vi[2(di-ti)+2ti(1-ti)-ti^2 ln(1/ti^2)].

Since Di takes values -1,0,1, di-ti=2min(P(Di=1),P(Di=-1))>=0. Also ti^2 ln(1/ti^2)<=2ti(1-ti). The identity is nonnegative local slack, not a new independently spendable budget.

For mask33152 with fair data and selector probability z, direct expansion around the fair sign characters gives ci=(1-z)/4 for the three singleton data sets and the triple, cij=(1+z)/4 for the three pairs, and |c_{T union selector}|=1/8 for all eight selector sets. Put h(t)=t^2 ln(1/t^2). Counting degrees gives delta=(5+14z-7z^2)/16, E=4h((1-z)/4)+3h((1+z)/4)+z(1-z)ln64/2.

Split the log16 term from the first seven contributions. The positive remaining term is (1-z)^2 ln(1/(1-z))/2<=z(1-z)/2. The three (1+z) terms have negative remaining entropy and can be discarded. Subtracting this upper bound from C0 delta gives

    [20-18ln2 +(48-12ln2)z+(-20+6ln2)z^2]/16.

Its z-dependent part is nonnegative: z[(48-12ln2)+(-20+6ln2)z]>=z(28-6ln2)>=0, using ln2<1. Equality at z=0 gives the sharp absolute margin (10-9ln2)/8. The rational upper bound ln2<52/75 gives margin>47/100. Direct differentiation of h at1/4 yields the first endpoint expansion E=(7/4)ln2+[(5/2)ln2+1/8]z+O(z^2); at s=1-z the four small coefficients contribute h(s/4)*4=(s^2/4)ln16+(s^2/2)ln(1/s), and the remaining terms give E=(3/2)ln2+[3/4+(3/2)ln2]s+(s^2/2)ln(1/s)+O(s^2). Ratios tend to28/5 and2, respectively. Both endpoint deficits are positive. Verdict HOLDS for the source's exact identity, selector-line theorem and fixed-line endpoint expansions. Its arbitrary-bias and universal payment gaps are not asserted closed by this review.

## 2. Scalar entropy collision bound with bounded amplitudes

Set h(a)=a^2 ln(1/a^2), h(0)=0. For |a|,|b|<=1/2 and |a+b|<=1,

    h(a+b) <= 2h(a)+2h(b).                            (L)

If a,b have opposite signs, |a+b|<=max(|a|,|b|)<=1/2. Since h'(t)=2t[ln(1/t^2)-1]>=0 on [0,1/2] (ln4>1), h(a+b)<=h(max(|a|,|b|))<=h(a)+h(b). If they have the same sign, write w=a^2+b^2 and r=(a+b)^2. Then w<=r<=2w<=1 and

    -r ln r <= -r ln w <= -2w ln w
               <= 2[-a^2 ln(a^2)-b^2 ln(b^2)].

The last line uses a^2,b^2<=w. Zeros follow continuously. This argument does not apply to arbitrary singleton amplitudes near1: the unit-amplitude collision is an actual obstruction to that extension. We pay all singletons by the signed reserve instead.

## 3. Two conjunction events with separated derivative supports

Let A,B be conjunction events, each fixing a nonempty set of physical coordinates to specified bit values. Suppose at least two shared coordinates are fixed to opposite values. Then A and B are disjoint, and their half-difference derivatives have disjoint supports for every coordinate. Indeed, after deleting any one coordinate, at least one of the two contradictory fixed literals remains. Hence their derivative product is identically zero. Define fA=2*1_A-1, fB=2*1_B-1 and F=2*1_{A union B}-1=fA+fB+1.

By independence, the normalized coefficient of a conjunction on a nonempty subset S of its support is a signed

    cA(S)=2^(1-|S|) product_{j in supp(A)\S} P(Yj=specified value),

and it is zero if S is not contained in that support. In particular |cA(S)|,|cB(S)|<=1/2 for |S|>=2. The nonempty coefficient of F is cA+cB. Lemma (L), term by term with common physical normalization vS, proves

    E_ge2(F)<=2E_ge2(fA)+2E_ge2(fB)
              <=2E(fA)+2E(fB).                         (H)

The individual conjunctions are genuine read-once compositions of the already proved binary corner gate, so E(fA)<=C0 delta(fA) and E(fB)<=C0 delta(fB). This consumes the known binary formula and exact disjoint entropy/deficit identity; no new AND coefficient calculation or sharp-tax theorem is needed.

Disjoint derivative supports give I(F)=I(fA)+I(fB). Let a=P(A), b=P(B). Disjointness gives Cov(fA,fB)=-4ab and thus

    Var(F)=Var(fA)+Var(fB)-8ab,
    delta(F)=delta(fA)+delta(fB)+8ab
                >=delta(fA)+delta(fB).                 (D)

The existing universal signed singleton reserve gives E_single(F)<=4delta(F); the negative higher-degree reserve can safely be discarded here. Combining (H),(D) pays both entire constituent higher-degree ledgers and the output singletons by

    E(F)<=4delta(F)+2C0[delta(fA)+delta(fB)]
          <=K0 delta(F), K0=12+4ln2.

In bit units this is Hplus(F)<=[4+12/ln2]delta(F), independent of the number of physical coordinates or of all interior product biases. Costs are additive with the displayed constants against the same output deficit; no coefficient-one reuse of a singleton slack or triple mass is claimed. This is a proved overlap interface, not an application of disjoint composition to the overlapping physical supports.

If ordinary inputs are uniform, H=Hplus-t log2 t with t=(E F)^2. Since -t ln t<=1-t=Var(F), and K=4+12/ln2>1/ln2, the same constant gives H(F)<=K I(F). Deterministic inputs can be handled by contracting the resulting gate: continuity of vi cS^2 ln(1/cS^2) supplies the limiting inequality without dividing zero variances.

## 4. An unbounded-arity genuine prime family

For every k>=2, set A={Y1=...=Yk=1} and B={Y1=...=Yk=0,Z=1}. These events disagree on all k data literals. Let Fk be positive exactly on A union B. Every data coordinate is essential, by taking the other data bits1 and Z=0; Z is essential at all-zero data.

For any proper block B0 with 2<=|B0|<=k, the cofactor rows have exactly three distinct values:

- If B0 consists only of data coordinates, the all-one block row selects the all-one complementary data, independently of Z; the all-zero block row selects Z=1 and all-zero complementary data; a mixed block row is constant negative. If no complementary data remain, these become constant positive, the Z literal and constant negative. They are distinct.
- If B0 contains Z and at least one data coordinate, properness leaves at least one data coordinate outside. The all-one block data give the all-one complementary indicator. The all-zero block data with Z=1 give the all-zero complementary indicator, and with Z=0 give constant negative. Any mixed block gives that same negative row. The two indicators and negative row are distinct.

Thus no proper block has two cofactor rows, and Fk is a genuine essential prime for every k>=2. The theorem above supplies a single all-bias constant K to this entire unbounded-arity prime family. F3 is the prior obstruction mask33152, so its arbitrary four-bias corrected inequality is now proved, though its sharp supremum remains unresolved. This family tends to a composite ANDk slice when Z becomes deterministic; the payment remains stable under that degeneration.

## 5. Exact remaining universal gap

The proof uses both the conjunction mixed-difference amplitude cap and at least two conflicting literals. For arbitrary prime cofactor pieces, higher-degree normalized amplitudes need not be <=1/2, derivative products need not vanish, and delta(F)>=delta(fA)+delta(fB) is not available. The first unsupported replacement would pay those coherent derivative intersections and the actual component entropy with one exclusive output deficit. The source A042 slack identity alone only rewrites that target. No all-arity prime estimate or full FEI proof follows from this family.
