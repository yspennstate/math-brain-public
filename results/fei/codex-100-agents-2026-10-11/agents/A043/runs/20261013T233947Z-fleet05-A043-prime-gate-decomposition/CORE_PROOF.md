# Ternary prime closure with a signed singleton reserve

Work with Boolean signs on independent interior Bernoulli bits Yi, pi=P(Yi=1), vi=4pi(1-pi). Let P(S) be the squared normalized Fourier coefficient, delta=sum_{|S|>=2}(|S|-1)P(S), and E=(ln2)Hplus=sum_{S nonempty}P(S)ln(v_S/P(S)). Define c_S=fhat(S)/sqrt(v_S), so E=sum v_S h(c_S), h(c)=c^2 ln(1/c^2). Zero terms are interpreted by continuity.

## A signed reserve valid for every Boolean gate

The half-difference Di=(f|Yi=1-f|Yi=0)/2 takes values in {-1,0,1}. Its mean is c_i. Since E Di^2>=|E Di|, Var(Di)>=|c_i|(1-|c_i|). For 0<|c|<=1, ln(1/|c|)<=1/|c|-1 gives h(c)<=2|c|(1-|c|). Thus

    E_single <= 2 sum_i vi Var(Di)
             = 2 sum_{|S|>=2}|S|P(S)
             = 4 delta - 2 sum_{|S|>=3}(|S|-2)P(S).           (R)

The equality is Parseval applied to Di: its nonempty coefficients are fhat(T union {i})/sqrt(vi). This proof uses no monotonicity. For three inputs, write B=sum_{|S|=2}P(S) and T=P(123), so delta=B+2T and (R) is E_single<=4delta-2T. The favorable -2T must not be discarded.

## Complete ternary prime catalogue

Input permutations, input reflections accompanied by reflected biases, and output negation preserve the prime criterion and the entropy ratio. The exact 256-table catalogue in out/catalogue.json partitions all 104 essential ternary primes into five orbits, represented by masks 22,23,24,25,27, of sizes 16,8,8,48,24. Bit x of a mask indicates a positive output at assignment x. Representative 23 is the majority orbit, and 27 the mux orbit. The following three representatives were not closed by the majority or mux work.

### Orbit 24: equality of three signs

Use the orbit-equivalent gate f=2*1[X1=X2=X3]-1, with mi=E Xi. Its sign polynomial is

    f=(X1X2+X1X3+X2X3-1)/2.

Hence c_i=(mj+mk)/2, c_ij=1/2 and c_123=0. Its pair entropy is exactly ln4*delta. For a,b in [-1,1], let c=|(a+b)/2|. Reflect both signs if needed to make a+b>=0. Then (1-a)(1-b)>=0 implies

    2c(1-c) <= [(1-a^2)+(1-b^2)]/2.

Together with h(c)<=2c(1-c), this gives E_single_i<=vi(vj+vk)/2. Summing yields E_single<=4delta. Therefore

    E <= (4+ln4)delta.                                       (E)

This is strictly below in the interior, since at c=0 the right scalar bound is positive and at 0<c<1 the logarithm inequality is strict. With all pi=q decreasing to zero, delta=12q^2+O(q^3), the singleton entropy is 48q^2+O(q^3), and the pair entropy is ln4*delta. The exact supremum for this orbit is consequently (4+ln4)/ln2=2+4/ln2.

### Orbit 22: exactly one positive bit

Use the representative gate f=2*1[Y1+Y2+Y3=1]-1, whose bit polynomial is

    f=-1+2(Y1+Y2+Y3)-4(Y1Y2+Y1Y3+Y2Y3)+6Y1Y2Y3.

Its normalized mixed differences are

    c_i=1-2pj-2pk+3pjpk,
    c_ij=-1+(3/2)pk=(3mk-1)/4,
    c_123=3/4.

Let u=2c_ij=(3mk-1)/2, so -2<u<1. The excess pair entropy over ln4*P(ij) is (vi vj/4)[-u^2 ln u^2], and T=(vi vj/4)(1-u)(u+2). If |u|>=1 the excess is nonpositive. If |u|<1, -u^2 ln u^2<=1-u^2 and

    (1-u^2)/[(1-u)(u+2)]=(1+u)/(u+2)<=2/3.

Every pair therefore satisfies E_ij<=ln4*P(ij)+(2/3)T. The triple entropy is ln(16/9)*T. Combining the three pair bounds with (R) gives

    E <= (4+ln4)delta - ln9*T.                               (O)

All algebra is on positive vi; zero pair amplitudes require no division. For probabilities (1-q^3,q,q), the dominant pair {2,3} has c_23=1/2+O(q^3), while c_2=c_3=-1+q+O(q^3). Its deficit is 4q^2+O(q^3), its singleton entropy is 16q^2+O(q^3), and its dominant pair entropy is 8(ln2)q^2+O(q^3). Every other term is O(q^4) or smaller apart from harmless logarithmic factors. Hence the ratio tends to 2+4/ln2. This establishes the sharp orbit supremum and strict interior inequality from T>0.

### Orbit 25: a signed quadratic gate with one exceptional corner

The canonical representative is positive at assignments 0,3,4. Its bit polynomial is

    f=1-2Y1-2Y2+4Y1Y2-2Y1Y2Y3.

Thus

    c_1=-1+2p2-p2p3, c_2=-1+2p1-p1p3, c_3=-p1p2,
    c_12=1-p3/2, c_13=-p2/2, c_23=-p1/2, c_123=-1/4.

For pair {1,2}, set u=2c_12=2-p3 in (1,2). Its excess over ln4*P(12) is -(v1v2/4)u^2 ln u^2, while T=(v1v2/4)(u-1)(2-u). The scalar bound ln u>=1-1/u gives

    u^2 ln u^2>=2u(u-1)>=2(u-1)(2-u),

so E_12<=ln4*P(12)-2T. For pair {1,3}, set u=p2 in (0,1). Its excess is (v1v3/4)u^2 ln(1/u^2), and T=(v1v3/4)u(1-u). Consequently

    E_13-ln4*P(13)=2T * [u ln(1/u)/(1-u)] <= 2T.

The last inequality is ln(1/u)<=1/u-1. Pair {2,3} has the same bound with u=p1. The triple entropy is ln16*T. Thus

    E_ge2<=ln4*B+(2+ln16)T=ln4*delta+2T.

Together with (R), this yields

    E <= (4+ln4)delta.                                       (Q)

The negative -2T in the distinguished pair is necessary: discarding it would produce an unpaid +2T in the final inequality. These are the actual same triple mass, not three independent budgets. The pair bounds are strict in the interior. With probabilities (q,q,1-q^3), c_1=c_2=-1+q+q^4, c_12=1/2+q^3/2, the deficit is 4q^2+O(q^3), and E=(16+8ln2)q^2+O(q^3). The remaining singleton has mass O(q^7) and logarithmic entropy; the other pairs and triple are higher order. This again proves the sharp supremum 2+4/ln2.

## Majority review and mux interface

A042-SHARP-MAJORITY3-BIASED-ENDPOINT@1 is independently reconstructed in REVIEW_MAJORITY.md using the sign polynomial rather than the author's bit polynomial. Its core bound is E<=(4+ln4)delta-(ln4-1)T. This review does not accept the author's explicit all-rate error constant or unreplayed validation counts.

For the mux orbit, A044's source-complete checkpoint gives a direct spectrum formula at address probability q and data means m0,m1. Its formula and proof are independently reconstructed in REVIEW_MUX.md; this stage's exact checker validates it as well. The resulting bound is E<=(4+ln4)delta, with the same sharp supremum. A044's broader two-mean profile transfer remains outside this review.

It follows that the sharp corrected product-biased constant over all essential ternary primes is 2+4/ln2. Along with the source-complete binary theorem and the exact disjoint composition identity reconstructed below, the same sharp constant holds for every Boolean gate on at most three essential inputs and every genuine read-once formula with fan-in at most three under arbitrary product biases. Uniform physical inputs give ordinary H<=[2+4/ln2]I. This is a finite gate-basis conclusion, not full FEI.

For completeness, in a disjoint composition F=G(f1,...,fk), let Vi=Var(fi)>0 and let eta be the induced product law of the child signs. Every nonempty child spectrum is normalized by Vi. For U in the outer spectrum and nonempty Ti in each selected child's spectrum, the unique block intersections give P_F(union Ti)=P_G(U) product_{i in U} P_i(Ti)/Vi. Splitting the logarithm log(v_union/P_F) into the outer corrected logarithm and child corrected logarithms yields Hplus(F)=Hplus_eta(G)+sum alpha_i Hplus(fi), where alpha_i=I_i^eta(G)/Vi. Summing degrees gives I(F)=sum alpha_i I(fi), while Var(F)=Var_eta(G). Since sum alpha_i Vi=I_eta(G), delta(F)=delta_eta(G)+sum alpha_i delta(fi). All alpha_i are nonnegative. Constant children are contracted before division. These identities prove the asserted read-once closure by induction. At uniform physical inputs H=Hplus-t log2 t, where t=(E f)^2; -t ln t<=1-t=Var gives H<=Cstar delta+Var/ln2<=Cstar I.

## Exact obstruction to extending the ternary reserve companion

Write R=sum_{|S|>=3}(|S|-2)P(S). All five ternary prime proofs above pay E_ge2<=ln4*delta+2R. The signed singleton reserve would then prove the sharp bound. However, this higher-degree companion is FALSE even on the prime class, not just unproved.

First, for uniform AND3, f=-1+2Y1Y2Y3, every nonempty mass is 1/16 and every c_S=1/4. Hence delta=5/16, R=1/16, E_ge2=(ln16)/4, and

    E_ge2-ln4*delta-2R=(3ln2-1)/8>0.

The strict sign follows from ln2>1/2. AND3 itself is decomposable, so it is not a prime witness. Instead take the four-input sign gate positive exactly at bit assignments 7,8,15 (mask 33152), with bit 0 representing Y1. At Y4=0 its slice is AND3. At Y4=1 it is the all-equal gate on the first three bits. Every essential coordinate is checked directly; the six size-two and four size-three blocks have more than two distinct cofactor rows, so it is a genuine prime. With p=(1/2,1/2,1/2,1/1024), exact centered moments and rigorous rational log intervals in out/prime_obstruction.json certify

    delta=5257209/16777216, R=262911/4194304,
    E_ge2-ln4*delta-2R > 13/100.

Thus this particular all-arity prime payment fails at an actual interior product law. It does not refute the sharp ternary theorem or FEI. Indeed, the same certificate gives (4+ln4)delta-E_total>9/20 at this point: the unused singleton slack is more than sufficient here. As p4 decreases to zero, the excess tends to (3ln2-1)/8 by continuity of the normalized mixed-difference polynomials and of x^2 ln(1/x^2); terms involving coordinate four vanish. This explains why irreducibility does not remove a degenerating composite slice.

The exact first unsupported replacement is a cofactor-sensitive higher-degree payment which can use the unused singleton slack, without reusing spectral mass already charged elsewhere. The affine missing-coordinate identities establish ternary closure but do not supply this replacement for quaternary primes or all arities. NEXT must retain that slack rather than invoke the now-refuted universal companion.
