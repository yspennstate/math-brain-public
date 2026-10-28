# Both arbitrary connector blocks paid jointly

For every integer m>=2 take all edges of the two diagonal K_(m,m) blocks
L1--R1 and L2--R2. Insert ANY two labelled connector graphs H12 subset
L1 cross R2 and H21 subset L2 cross R1. At every original edge of the
resulting graph use lambda=1/(2m), rarity1/4 and both endpoint orders. Every
coordinate incidence row has sum at most1, because degree<=2m. The COMPLETE
nonempty cost against the FULL original queue output law Q1 satisfies

    C_F(Q1) < (147/2) I(F) <74 I(F).                 (T)

This is stronger in SCOPE than the preceding one-direction <49I result;
the constants concern different families. Both insertions may have arbitrarily
many edges, degree and interactions. The reference stays fixed before sampling.
It is not the SCC-restricted partition-forest residual: the all-root run
subfamily used below need not obey canonical source-SCC root minimality.

## One old output law, not a sequence of insertions

Let f0 be the OR of the two diagonal blocks and put t=2^-m. The previous
run JOINT_CONNECTORS.md section1 proves by third-order Bonferroni that
collision-free singleton-root assignments have probability at least1/8
inside each K_mm. It sums distinct actual run histories, with original
singleton-root numerator lambda/32. The unique global FIFO merge gives

    Q0(A)>=64^-|A|/(64D0),
    D0=(1+1/(8m))^(2m^2)-1,

for EVERY nonempty selected set. Thus log(1/Q0(A))<=log D0+6|A|+6.
No arbitrary shuffle, canonical root-disjointness lemma, or selected-cost
lower bound is used. This is a full original output-law upper certificate.

## Joint perturbation identities

Let h12,h21 be the actual zero-one edge-OR indicators of the two connector
graphs, on their disjoint2m-bit free blocks. Set p_ij=E h_ij, I_ij their
physical total influences, P=p12+p21 and J=I12+I21. Empty graphs have both
values zero. Let Z12 require R1=L2=0 and Z21 require R2=L1=0. Then

    delta=F-f0=2*1_Z12*h12+2*1_Z21*h21.

The two positive supports have Hamming distance at least4: a true edge-OR
requires at least one active vertex on each of its two sides, whereas all
those vertices are forced zero in the other support. Hence their physical
boundaries are disjoint and their Dirichlet inner product is zero. Their
Fourier coefficients need NOT have disjoint support and must not be bounded
by squaring a coefficientwise sum. Physical counting proves EXACTLY

    sum_A deltahat(A)^2=4t^2 P,
    sum_A |A|deltahat(A)^2=t^2(4mP+J),
    I1=I0+t^2(J-4mP),
    I0=8mt^2(1-t)(2-t),
    q1=(2t-t^2)^2-t^2 P.                            (1)

Each p_ij<=(1-t)^2, since h_ij true requires both free sides nonempty.
Consequently P<=2(1-t)^2, J>=0, and

    I1>=8mt^2(1-t)>=6mt^2,
    I0/I1<=2-t<2,
    v1=4q1(1-q1)<=16t^2.                            (2)

This physical lower bound improves the crude independent P<=2 estimate.
It does not assume total influence increases when edges are inserted.

## Complete occupation and exactly one root increment

Since log D0<3m/8 and log D0+6>0, the lower mass above and(1) give

    E_delta(Q0)
      <=4t^2 P(3m/8+6)+6t^2(4mP+J)
      <=99mt^2.                                    (3)

For the last line use P<=2, J<=4m and m>=2. Let k=|H12|+|H21|<=2m^2,
B=1+1/(8m) and D1=B^(2m^2+k)-1. Every old actual run embeds without using
an inserted gate. Its numerator is unchanged and its denominator becomes D1.
This pays all inserted-root exclusions, giving Q1>=D0 Q0/D1. Bernoulli
gives D0>=m/4, so

    log(D1/D0)<=k log B+log(1+4/m)<=3m/8+6/m,
    v1 log(D1/D0)/I1 <=(8/(3m))(3m/8+6/m)
                         =1+16/m^2<=5.              (4)

All logarithmic estimates use ln2>2/3 and ln(1+x)<=x, proved elementary
inequalities; no numerical logarithm approximation is part of the proof.

The SAME old reference has C_f0(Q0)<71I0/8 by the independently reviewed
A010 crossed-component theorem. One use of A006's full-output insertion
inequality at theta=1, with(2)--(4), gives

    C_F(Q1)/I1
      < 2*(71/8)*2 + 2*99/6 +5
       =147/2 <74.

This includes the actual posterior over all full queue runs. It is a feasible
fixed-reference upper bound, not a variational lower bound or a proof of
optimal weights. No source is reinitialized after a connector is added.

## Exact boundary of this result

The theorem covers every graph containing the two specified diagonal K_mm
blocks, with arbitrary remaining bipartite edges. It does not cover all
graphs, all Boolean functions, or the paper's narrower canonical source-SCC
partition-forest residual. The first unsupported universal step is paying
whole-set group/subdictionary compatibility when no supplied dense-block
root-assignment certificate exists. A008 reports a full-output obstruction
even to a fixed two-polarity prime-queue mixture, so unrestricted original
PI-J must not be claimed as a surviving universal route on this evidence.
The next mechanism must encode a shared group tag once, with a new normalized
global law and an influence-paid tag cost. This run supplies a verified
whole-set compatible-assignment building block, rather than another claim
that repeated labels or canonical root constraints are free. Full FEI OPEN.
