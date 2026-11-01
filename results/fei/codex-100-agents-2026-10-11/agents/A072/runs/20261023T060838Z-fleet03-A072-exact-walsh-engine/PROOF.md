# Exact admission damage and an actual Boolean family

All entropies use base two. Full FEI remains OPEN. The obstruction below is at accounting rate K=1; it is not an obstruction to an influence-paid universal bank, nor a rate4 counterexample.

## 1. Exact robust capital for a prescribed local-hull allocator

Consider any finite physical-restriction DAG, with admitted coordinate/core set M, full-function slack S=KI-H, and b(v)=max(0,-S(v)). Let rho_M(v) be its exact stopping hull when only admitted coordinates may be queried. A physical query v->(v0,v1) under mask M allocates inherited credit by

    a_b = a + delta_b,   delta_b=rho_M(v_b)-(rho_M(v0)+rho_M(v1))/2.

Admissions change M and leave the actual credit unchanged. Every subsequent query uses the newly current local hull. Define on the augmented acyclic DAG

    T(v,M) = max{ b(v),
                  T(v,M+j) for allowed admissions j,
                  T(v_b,M)-delta_b for every allowed query and b=0,1 }.

This is the EXACT least initial credit which supports every future admission/query/stopping choice under this prescribed allocator. The max over query children is unweighted, unlike the stopping hull: each child must be solvent at its actual arrival. Induction proves necessity by choosing any violating child/admission, and sufficiency by checking every outgoing arrival. In particular T>=rho_M: average the two query constraints and use E delta=0, then apply the least-superharmonic characterization of rho_M. With all coordinates admitted initially, T=rho_all by induction.

An equivalent closed form is

    T(v,M)=max_path [ b(terminal)-sum_query_edges delta ].

The path can stop anywhere. This is a maximum over actual arrivals, not an expectation over terminal deficits. This identity supplies a forward path audit independent of the backward capital recurrence.

Every credit-owner label uses kernel a_b/a (zero-credit case gives zero nonnegative labels). Full debit d_b=S(v_b)+a_b is nonnegative when a_b>=T(v_b,M). If D=S(v)+a and e=E S(v_b)-S(v), then E d_b=D+e. Old signed debit labels and the new signed label e use common kernel d_b/(D+e) when this total is positive. When it is zero, both child debits vanish and kernel1 preserves the signed labels whose total is0. Thus the criterion preserves the individual old owners, all actual reaches and any already spent external donor. It does not create a donor or erase history.

## 2. No admission damage through three physical bits, every K>=0

For a function on at most two free bits, each nonconstant proper restriction has at most one bit, Fourier entropy0 and nonnegative slack K I. Consequently rho_M(v)=b(v) for EVERY admitted mask M. For three free bits the children of the first physical query therefore have rho_all=b. Its full stopping hull covers the average of these two deficits. A local-hull query sends a_b=b(v_b)+a-E b(v_b), so starting a>=rho_all covers each child's full hull. At all smaller states this remains true. Admissions alone change no account. Hence T(v,empty)=rho_all(v) for every Boolean function on at most three bits and every K>=0. The all256 three-bit rate1 census is a check of this theorem, not its proof for a continuum of rates.

## 3. Boolean family, exact Walsh and independent edges

For d>=0 let n=d+3. On d selector bits s and three parity bits x, define

    F_d(s,x)=chi_{123}(x) * (-1 if (s,x)=0^n else +1).

Bits0,1 are the uniform signs encoded by +1,-1 respectively. Thus F_d is explicitly sign valued on every vertex. More generally write F_{r,t} for parity on r coordinates, t selector coordinates, and the same single-vertex sign flip; m=r+t. A restriction which has observed a1 is a pure parity function, with entropy0 and nonnegative rate1 slack. A restriction observing only0 is another F_{r',t'}.

For m>=1, N=2^m, the integer Walsh spectrum is

    W(A)=N*1_{A=P}-2,

where P is the subset of the r parity coordinates. Its squares sum to (N-2)^2+4(N-1)=N^2. Its inverse character sum divided by N is chi_P(z)-2*1_{z=0}, exactly the prescribed Boolean truth table. This also handles r=0 and m=1; m=0 is a constant. Count edges independently: pure parity has r*N/2 crossing edges; flipping vertex0 removes r such edges and adds m-r previously noncrossing edges. Thus

    I_{r,t}=r+2(m-2r)/N.

Only after these integer checks do we compute entropy. Put u=2/N. The squared main coefficient is (1-u)^2 and each other squared coefficient is u^2, so

    H_m= -2(1-u)^2 log2(1-u) -2u(2-u) log2 u.

Use 0 log0=0 and H_0=0. Every negative-deficit stopping leaf must lie on the unique all-zero query path; all side leaves are pure parity and need0. Therefore the full hull has the EXACT finite formula

    R_d = max_{0<=r<=3, 0<=t<=d}
              2^{-(d+3-r-t)} * (H_{r+t}-I_{r,t})_+.

Any pair r,t can be reached on that unique path, establishing attainment as well as the upper bound. This is an all-d statement obtained from the Boolean family, not from numerical extrapolation.

## 4. Global reserve tends to zero, while local-admission capital stays positive

First H_m is decreasing for m>=3. In natural units its derivative with respect to u is

    4(1-u) ln((1-u)/u)-2 >0,  0<u<=1/4,

because ln3>1 (the positive atanh series proves this directly). As m increases, u decreases. Also I_{3,t}>=9/4 for all t>=0, checking m=3,4,5 directly and using m>=6 thereafter. At m=3,

    H_3=4-(9/8)log2 3 <9/4,

since 3^9=19683>16384=2^14. Hence EVERY F_{3,t} has strictly positive rate1 slack. Querying only selector bits can consequently never encounter a deficit. Its local stopping hull is identically0, even if all selector bits are admitted together. Such queries have delta=0: credit is unchanged along the all-zero selector path.

At its end stands F_{3,0}. Each parity query has one two-bit point-defect child, H=2,I=1, need1, and one pure-parity child, need0. Root need0, so rho_all(F_{3,0})=1/2. Any robust sequential-admission scheme which permits first admitting and revealing all selectors must therefore start with T_d>=1/2: it cannot pay this subsequent admission from smaller unchanged actual credit.

In contrast R_d tends to0. For m>=2 put v=1-(1-2/N)^2, so 1/N<=v<=4/N. Shannon's formula gives H_m=h2(v)+v log2(N-1). The elementary bound -(1-v)ln(1-v)<=v yields

    H_m <= v[log2(1/v)+1/ln2+m] <= 8(m+1)/2^m.

Here ln2>1/2, also immediate from its positive atanh series. The m=0,1 entropies vanish. Multiplying by the true reach 2^{-(n-m)} in the exact hull formula proves

    0<R_d<=8(d+4)/2^{d+3} ->0,    T_d>=1/2.

Positivity follows by retaining two parity bits and no selectors: need1 at reach2^{-(d+1)}. Consequently there is NO absolute L with T_d<=L R_d for this actual Boolean family at K=1. In fact T_d/R_d>=2^{d-1}/(d+4). This refutes the proposed generic implication that a full stopping-hull bank, even enlarged by a constant factor, automatically pays arbitrary sequential local-hull admissions.

## 5. Smallest dimension witness and scope

For d=1 (four physical bits) direct integer reconstruction and all path auditing give exactly R_1=1/4 and T_1=1/2. The bad path first admits selector0, queries it with answer0, then admits the parity bits. The local selector hull0 leaves credit1/4 at the three-bit branch whose full hull is1/2. Its current slack is still positive. This is a deficiency in the available future reserve, not a claim that its current debit is negative. Continuing to the attaining two-bit deficit makes the solvency failure explicit.

For an analytic upper bound T_1<=1/2, any first query has full-child hulls1/2 and0. Under any admitted mask, the bad child's local hull is between0 and1/2 and the other child's is0. Starting with1/2 leaves the bad child at least1/2 and the good child nonnegative. The three-bit theorem pays all later admissions. Hence equality is proved without relying on a floating calculation or a path sample.

This result does NOT refute A071's exact rate4 four-core certificate, which separately checks every actual admission. It does NOT refute an influence-paid envelope: I(F_d)=3+2(d-3)/2^{d+3}->3, so a fixed positive capital need is compatible with a constant multiple of influence. The obstruction distinguishes financing an initial global hull from preserving that financing under a prescribed sequence of changing local hulls. A coherent full-universe envelope avoids this particular switch, at the cost of constructing and initially paying that envelope.

The first unsupported universal line remains: at a suitable absolute rate, construct a dimension-independent influence-paid superharmonic envelope on arbitrary Boolean restriction DAGs, with owner-preserving allocations coherent under every allowed admission. Neither the bounded source certificate nor this obstruction supplies it.
