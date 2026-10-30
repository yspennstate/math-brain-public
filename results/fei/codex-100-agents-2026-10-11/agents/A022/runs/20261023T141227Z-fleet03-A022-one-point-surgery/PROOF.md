# A022 stage11: adjacent selector drift, with the original owner retained

All logarithms are base2. V(f)=U(f)-phi(E[f]^2) is the NONEMPTY upper-set potential, not variance. Delta_j is the actual signed average over BOTH physical restrictions. Let G_z sum these differences only over the original shared controller coordinates. No sign is discarded.

## 1. Exact interface inherited from ledger v9

Let b be any Boolean seed on k DATA bits, v,w adjacent in coordinate i, delta=2^-k, epsilon=b(v)b(w). Replace b(v) by b(v)a(z) and b(w) by b(w)c_raw(z), where both genuine Boolean controllers use the SAME independent z cube. Set c=epsilon*c_raw; influence, V and GV are unchanged by this output sign. Let h(y,z)=a(z) for y=0 and c(z) for y=1. Write p_h=hat h squared, pi_h its complete upward tails, and

J_y(h)=p_h({y}) log2(pi_h({y})/p_h({y})),
R(a,c)=Delta_y V(h)-J_y(h).

Zero masses have zero contribution. In particular neither R nor its drift is itself a new original source allowance.

For T nonempty in z,

hat F(S,T)=delta b(v)chi_S(v)[hat a(T)+(-1)^(1_{i in S})hat c(T)],
pi_F(S,T)=delta^2 2^(k-|S|)[pi_a(T)+pi_c(T)-2*1_{i in S} sum_{L containing T}hat a(L)hat c(L)].

The cross term cancels only for i not in S. These identities hold for every seed, controller dimension, bias and adjacent vertex. Summing the nonempty-z rows yields exactly

Q_z(F)=delta[V(a)+V(c)]+2delta R(a,c)+delta(k-1)/2[Var(a)+Var(c)]. (1)

This is ledger v9's actual shared-mux identity, not an independent-controller approximation. Define E(F) to be the sum p_F(S,empty)log2(pi_F(S,empty)/p_F(S,empty)) over NONEMPTY DATA S. The global empty atom is already removed, so

V(F)=E(F)+Q_z(F). (2)

## 2. New exact all-coordinate CONTROL drift

Apply each physical z_j restriction to (1). DATA size, delta and epsilon stay fixed. The variance difference is Delta_j Var(a)=hat a({j})^2, by Parseval and the two conditional means. Therefore with W1(a)=sum_j hat a({j})^2,

G_z V(F)=delta[GV(a)+GV(c)]+2delta G_z R(a,c)
             +delta(k-1)/2[W1(a)+W1(c)]+G_z E(F). (3)

Every child uses the same actual restricted pair, including constant children. Equivalently, physical restrictions commute, and

G_z V(h)=1/2[GV(a)+GV(c)]+G_z R(a,c)+G_z J_y(h). (4)

Equations(3)--(4) are valid in ALL dimensions with no FEI premise. They retain the complete singleton term and the complete DATA/nonempty-z split. For m=0 all sums vanish. Formula(3) identifies the first unpaid quantity rather than declaring it nonpositive.

## 3. All-dimensional actual Boolean guard against dropping the drift

Take m>=1, r=2^-m, a_m=-1 only at 0^m and c=1. Then h is the one-point function on m+1 bits. Its Fourier probabilities are p_empty=(1-2r')^2 and p_nonempty=4r'^2 with r'=2^-d on d bits. For every nonempty S, pi(S)/p(S)=2^(d-|S|). Summing exactly gives

V(a_d)=2d*2^-d-4d*4^-d.

For h=a_(m+1), J_y=m r^2. Hence

R(a_m,1)=r-r^2. (5)

For z_j=0, the pair is(a_(m-1),1), with remainder 2r-4r^2 (also for m=1, where a_0=-1 and this equals0). For z_j=1 both controllers equal1 and R=0. Thus

Delta_j R=r^2,  G_z R=m r^2>0. (6)

This refutes the universal helper G_z R<=0 for genuine Boolean controllers, without changing a proposed constant or claiming an FEI disproof. It also shows the singleton term cannot be omitted: for this family J_y=m r^2 is exactly the positive aggregate drift. These are different operations/locations in the ledger, so their numerical equality does not authorize cancelling arbitrary histories. In contrast, the pair with two-bit truth masks a=7,c=1 has R=0 and G_z R=-1/2, giving the opposite sign exactly. Mask bit z means output+1, otherwise-1. Both signs are therefore unavoidable.

## 4. Antipodal family: negative logarithmic drift is not an absolute cost

For m>=1 let a=+1 only at0^m and c=+1 only at1^m. Both source means are2r-1, r=2^-m. The mux spectrum has one nonempty row for each nonempty T: y-frequency is |T| mod2 and its mass is4r^2. J_y=0. For even T, the upper-tail ratio is2^(m-|T|). For odd T of size less than m the y-frequency constraint halves this ratio; the full T has ratio1. There are2^(m-1)-1_{m odd} proper odd T. Therefore

R=-2r+4r^2*1_{m odd}. (8)

After either physical z_j restriction, one controller is the (m-1)-bit point function and the other is constant. Its remainder is2r-4r^2. Consequently

G_z R=m[-4r+4r^2(1+1_{m odd})]. (9)

For m>=2 this is strictly negative. The selector's ACTUAL influence d=Pr[a!=c]=2r, so

|G_z R|/d=2m-2mr(1+1_{m odd}) -> infinity. (10)

Thus no absolute bound |G_z R|<=K Inf_y(h) is possible for all Boolean pairs with a fixed K. Here m=log2(2/d), displaying the exact logarithmic term. This does not refute a signed upper bound or FEI: the negative sign helps the target inequality. Source influences are I(a)=I(c)=2mr, so the example does not exclude payment from their actual original influences. It excludes charging the absolute interference solely to selector disagreement. Masks1,8 at m2 give R=-1/2, G_z R=-3/2, d=1/2. In contrast the positive-drift point/constant family of Section3 has d=r and G_z R/d=mr.

All m+1 physical children of this antipodal mux are a point function on m bits, possibly translated or complemented. Both operations preserve V. Thus EVERY coordinate has Delta_i V(h)=R and GV(h)=(m+1)R<0 for m>=2. This confirms directly that these are not positive GU obstructions. At m2, V(h)=0 but [V(a)+V(c)]/2=1/2: naive source-potential domination also fails for an arbitrary mux. The proposed g tensor t endpoint in Section6 is narrower and is not refuted by this arbitrary-mux observation.

## 5. A concrete near-tensor zero corner

Let b=g tensor2 on six bits, g negative only at000, v=0,w=1, and flip BOTH values. Here b(v)=1,b(w)=-1 and

hat f(S)=hat b(S)-(1/16)*1_{1 in S}.

Indeed a flip subtracts2/64 times b(vertex)chi_S(vertex), and the two signs differ in coordinate1. The tensor coefficient equals1/16 whenever both three-bit blocks of S are nonempty. Consequently EXACTLY28 rows vanish: S containing coordinate1 and containing any coordinate in the second block (4 choices in the first block times7 in the second). All seed coefficients were nonzero. This refutes transplanting v9's uniform relative-perturbation<=1/2 proof to the t2 adjacent corner: its ratio reaches1 and p=0, so derivatives containing p'/sqrt(p) require separate limiting treatment. For t>=3 the crude two-point relative amplitude bound is4*2^-t<=1/2, so this particular root zero problem disappears. That observation alone pays neither the shared-selector remainder nor first DATA children. It is not a GU counterexample.

## 6. Exact sufficient implication and first unsupported line

For the adjacent g tensor t construction, t>=2, a stable extension of v9 would require a SINGLE dimension-independent K such that

G_DATA V(F)+G_z E(F)+2delta G_z R(a,c)
       +delta(k-1)/2[W1(a)+W1(c)] <= K I_DATA(F), (7)

and the endpoint V(F)>=delta[V(a)+V(c)]. If every source has GV<=A I+B V with0<=B<1, (3),(7) and the exact disjoint-input influence identity I(F)=I_DATA(F)+delta[I(a)+I(c)] then give

GV(F)<=max(A,K) I(F)+B V(F).

The v9 signed induction proves that a universal such pair yields V<=A I/(1-B), then H<=2I+2V and FEI. This is the complete relevance bridge, NOT a proof that adjacent activation is universal. Formula(7), with the SAME existing DATA margin and both endpoints, is the first unpaid line. Positive drift(6) refutes only the sign shortcut, not (7). The main finite enumeration classifies R as well, but finite signs do not prove a universal sign or estimate.

## 7. Verification boundary

Frozen SEARCH_SPEC gives all ordered two-bit controller pairs and eight actual adjacent-seed fixtures. Standalone direct-character replay independently reconstructs all finite sign counts and the explicit point family at m=1..6. It shares no production Fourier, upper-tail or logarithm implementation. Exact identities use rational prime-log coefficients; strict signs use outward rational atanh tails. This is author reproduction in a different representation, not independent-person review. The analytic identities(1)--(6) supply the all-dimensional argument; no finite search is promoted to it.
