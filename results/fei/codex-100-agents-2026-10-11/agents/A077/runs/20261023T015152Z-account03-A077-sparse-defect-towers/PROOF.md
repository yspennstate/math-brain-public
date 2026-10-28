# The masked carrier is the extra shared bill

All entropies are in bits; all inputs are physical independent uniform bits. This is a supplied-source continuation theorem, not a universal FEI certificate.

## 1. Exact shared-sector decomposition, arbitrary carrier

Let h be a Boolean carrier on r shared bits. At m=0,1,2 distinguished vertices replace its value by actual Boolean private profiles, independent of the shared cube and possibly fully correlated with each other. In the two-vertex phase the vertices are adjacent and their original carrier values are +1. Every live profile has mean zero. Put p=2^-r and let M(s)=0 at edited vertices, M(s)=h(s) elsewhere. M is a real function with values in {0,+1,-1}, not an invented Boolean source. Write

    T=p sum_live H(profile), R=r p m.

For two adjacent live profiles V,W set Xi=p sum_(A nonempty) k(Vhat(A),What(A)), with k as in A077 stage6 and A078's account. In the one-vertex and zero-vertex phases set Xi=0. The complete empty-private spectrum of F is exactly Mhat. Expansion of the other rows gives

    H(F)=T+Xi+2R+Hhat(M),                              (1)

where Hhat(M)=sum_S -Mhat(S)^2 log2 Mhat(S)^2 is unnormalized spectral entropy. It is not the entropy of a probability law unless M has norm one. Every zero row contributes zero. Formula (1) follows from Walsh scaling: a single event contributes pH(profile)+2rp; two adjacent events contribute the sum of those terms plus Xi. No empty private Fourier label is included in Xi.

For a shared query j define B_j(G)=sum_(S not containing j) Phi(Ghat(S)^2,Ghat(S+j)^2), Phi(a,b)=(a+b)h2(b/(a+b)), including zero by continuity. Partition the actual erasure fibers by the private Fourier label. Then exactly

    B_j(F)=B_j(M)+B_j(nonempty-private sector).        (2)

Because Phi(a,b)<=a+b, the second term is at most the total squared mass in that sector, namely mp. The ACTUAL inherited reserve release at this query is precisely

    R-parent minus average R-child = mp.              (3)

Indeed the average number of live vertices times the new p is mp, while the remaining shared dimension decreases from r to r-1. Formula (3) also covers a separating query, one-point states, killed-event siblings, and r=1. The inherited entropy allocation T is harmonic at shared queries. Thus the full physical channel bound Delta_j H(F)<=B_j(F)+(2/ln2)Inf_j(F) gives

    Delta_j H(F)<=release_R+B_j(M)+(2/ln2)Inf_j(F).    (4)

This is an all-dimensional identity/bound for arbitrary h and balanced profiles. It identifies the new bill exactly; it does not universally bound B_j(M) or remove its payment obligation.

For direct physical accounting define J_j(M) as the edge average with cost 1 for disagreeing unedited endpoints, 1/2 for one edited and one unedited endpoint, and 0 for two edited endpoints. Then

    Inf_j(F)=J_j(M)+p*2*Pr(V!=W)                      (5)

if j separates two adjacent live vertices; otherwise Inf_j(F)=J_j(M). The extra term is nonnegative. Balancedness supplies the exact 1/2 in the one-edited-edge case. Genuine carrier edges, private controller edges, guard edges and padding edges are never discarded.

## 2. Every restricted majority-three carrier pays B_j(M)<=2 J_j(M)

Take h(s)=+1 when at most one of its three bit coordinates is 1, and -1 otherwise. Initially edit vertices 000 and 100 (integer labels0 and1). Consider EVERY partial shared assignment, not just a chosen path. There are 27 states and 27 remaining-coordinate queries altogether. Direct Fourier calculation reduces them to the following cases; sign changes and coordinate permutations preserve B and J, and are used only in this proof, not to omit finite certificate cases.

* Three shared bits remain. The masked spectrum, in binary-index order, is (-1/4,1/2,1/4,0,1/4,0,-1/4,-1/2). For the separator, B=(5log2(5)-8)/8<=7/8 and J=1/2. For either other coordinate B=1/4 and J=1/2. Thus B<=2J, using log2(5)<3.
* Two bits remain after the separator is fixed. There is one edited vertex; all four Fourier magnitudes are (3/4,1/4,1/4,1/4). At either query B=1/8+Phi(9/16,1/16). The smaller possible J is1/4 (the other is3/4). The elementary bound Phi(a,b)<=b log2((a+b)/b)+b/ln2 gives B<=1/8+(4+3/2)/16=15/32<1/2, using log2(10)<4 and ln2>=2/3. Hence B<=2J on BOTH separator answers.
* Two bits remain after a nonseparator answer0. There are two adjacent edited vertices, and M is zero on their edge and a signed literal on the opposite edge. The two query erasures are 0 and1/2, and both J are1/2. After answer1 there are no edited vertices and the carrier is a two-bit AND sign: B=1 and J=1/2 at each query. This equality makes the coefficient2 sharp for this restricted carrier state space.
* One bit remains. The mask is constant, a signed literal, identically zero, or (0,+/-1) up to reversing endpoints. The first three give B=0. The last gives B=1/2 and J=1/2. No query remains when all three bits are assigned.

The elementary ln2>=2/3 follows from the first positive term in 2atanh(1/3). All 27 cases also have separately saved exact prime-log expressions and rational enclosures in CARRIER_CERTIFICATE.json. This finite classification is the entire carrier argument, so no finite-to-infinite extrapolation of h is made. The private dimension and profile spectra are unrestricted. Combining this proof with (4)-(5),

    Delta_shared H(F)<=release_R+5 Inf_shared(F).     (6)

The strict channel coefficient is 2+2/ln2<5; the convenient price5 is used in the ledger.

## 3. Carry the SAME original collision account

Require all still-live private profiles to have a common untouched private sign y: V=yU and W=yP on any other private inputs. Query arbitrary other private coordinates adaptively, and arbitrary shared coordinates in arbitrary order. The guard y may be queried only after ALL shared bits have been exposed on that path. This restriction is substantive: it keeps all live means zero while the new shared theorem is used. All actual stopping siblings and complete terminal spectra are retained.

At every private query before y, M,R and p stay fixed and both child profiles remain balanced. Consequently (1) gives the EXACT equality

    Delta_private H(F)=Delta_private T+Delta_private Xi. (7)

There is no new private transaction price in (7). Once no shared bit remains, F is a true core (or the carrier constant), H(F)=T, and a final guard query also retains its complete core entropy decrement exactly. No universal child FEI certificate is introduced.

At one original continuation state o, e_o=1/8, supply an unused ancestor earmark B after ALL old debits. Write chi_o=Xi_o/e_o and beta=B/e_o. In a still-live two-point state v set

    K_v=p_v(beta-chi_o)+Xi_v.                         (8)

If both events are killed before separation, K=0 on that carrier branch, whose true generally nonconstant h terminal is retained. On a shared nonseparator, the surviving p and Xi double, so K is harmonic. At a shared separator freeze K_parent in BOTH children and all their descendants, even after the last event is killed. It is an inherited earmark, not a new claim of local source surplus. On a private query in the two-point phase,

    Delta Xi+average K_child=K_parent.                (9)

In the one-point phase Xi=0 and K is frozen. The binary-entropy identity for k gives -4p<=Xi<=0. Therefore B>=4e_o ensures K>=0 throughout; freezing preserves this. The source event mass p, doubled on a surviving gate and zero on a killed gate, is a martingale up to separation. Freeze that bookkeeping mass at separation. For every finite adaptive stopping frontier,

    E K_leaf >= B-4e_o.                              (10)

These are A078's signed-account mechanism and A076's shared/freezing transport, now applied to the true nonconstant carrier. Neither the account nor its old debit is reset.

Summing (6)-(9) with the original physical reach probabilities yields, for EVERY finite adaptive permitted stopping tree,

 H(F_o)-E H(F_leaf)+E[R_leaf+K_leaf]
   <=T_o-E T_leaf+R_o+B+5 P_shared,                  (11)

where P_shared=sum_shared_nodes reach(v) Inf_query(F_v). All inherited input entropy decrements and all actual terminal entropies remain in (11). Private influence is present in the actual F spectra/influence ledger but is not needed as an extra local transaction allowance in this balanced-preserving scope.

## 4. Original bent donor, first debit and another old debit retained

At the ORIGINAL source take even k>=4, any m>=2, quadratic bent b_k on k data bits, V=y b_k, and W=y[1-2*1{z=0,x1=...=xm=0}]. H(V)=k and I(V)=k/2+1, including guard y; all padding influences of V are zero. Its actual original C5 allocation splits ONCE into

    5 e_o I(V) = e_o H(V)+S,
    S=e_o(3k/2+5)>=11e_o.                            (12)

Retain the already booked FIRST4e_o collision debit and any old D0>=0. After exposing x1, retain BOTH actual controller answers and both conditional full core bills; do not recertify either bent child. In each conditional continuation assign the same inherited B=S-D0-4e_o. Their physical conditional average is the same B, not twice B. If D0<=S-8e_o, (8)-(11) give

    E K_leaf>=S-D0-8e_o>=3e_o-D0.                   (13)

The stronger final inequality is just a uniform lower bound; the exact admissibility is D0<=S-8e_o. For k>4 the bound3e_o-D0 may be negative while the exact remainder is still nonnegative; only the exact remainder is used for admission.

The executed k4,m2 fixture has e_o=1/8,S=11/8, the old first debit4/8, ANOTHER old debit D0=1/8, B=6/8, and guaranteed remainder2/8. Three distinct mixed policies, each on BOTH initial x1 children and with every subsequent sibling retained, include bent-data queries, the remaining padding coordinate, both kinds of shared query, killed-event nonconstant carrier branches and a final guard query after all shared bits. Every core terminal spectrum is saved. Neither the original entropy allocation nor the same surplus is counted twice.

## 5. First unsupported universal line

For arbitrary h, equation(4) is valid but B_j(M)<=2J_j(M) is not supplied. It has only been proved for the complete restricted Maj3 carrier state space. Arbitrary carrier shared erasure, a guard query before shared geometry is finished, arbitrary-root eligibility for the original unused donor, and full inherited input/terminal FEI certification remain open. The concrete original donor does not prove a universal source exists. Full FEI remains OPEN; (11) is a restricted same-source continuation theorem. The shortest further test is an EARLY guard query followed by one actual shared query on the SAME nonconstant carrier and remaining original account: the empty-private row now contains nonzero inherited means, so the present masked-carrier certificate cannot simply be reused. Retain both mean profiles, old bookings and every terminal rather than renewing a child source.
