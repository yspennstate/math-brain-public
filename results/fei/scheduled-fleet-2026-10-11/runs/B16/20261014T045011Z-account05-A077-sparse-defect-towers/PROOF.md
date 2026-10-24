# A geometric source mark pays repeated sparse collisions

All variables are independent uniform bits; entropy is in bits. Let k>=2 be even, r>=1, and let

    G(s,x)=1-2*1{s=0,x=0},
    H(s)=(-1)^(s1*s2+...+s(k-1)*sk),
    A(t)=1{t=0}, G'=1+A(G-1), H'=1+A(H-1),
    W=G' if z=0, H' if z=1.

This is the previous stage's actual rare/rare family. The result below allows any adaptive fresh-coordinate tree, arbitrary stopping, and selector revelation at any time.

## 1. Source-bound private admission and its independent reconstruction

For any two Boolean branches U,V with V independent of queried bit i, write d=Inf_i(U), delta=Pr[U!=V], and

    A_i=B_i(select(U,V))-B_i(U)/4.

Then

    0<=A_i<=d+Phi(4delta-d,d)/2<=4delta.             (1)

This is A076 PRIVATE_ADMISSION_PROOF sections1-3, equations (1)-(5), independently reconstructed here. With u=Uhat(T), a=Uhat(T+i), v=Vhat(T), the actual erasure has two pairs (u+v,a)/2 and (u-v,a)/2. Put e=u-v. For fixed q=a^2, f(p)=Phi(p,q) is increasing, concave, subadditive and satisfies f(cp)<=f(p)+q log2(c), c>=1. The estimate (2u-e)^2<=8u^2+2e^2 gives

    0<=f((u+v)^2)+f((u-v)^2)-f(u^2)
                       <=4q+2f(e^2).

The lower half follows because one of |u+v|,|u-v| is at least |u|. Sum, divide by four and use homogeneous concavity to obtain A_i<=d+Phi(E,d)/2, E=sum(u-v)^2=4delta-d. On a pivotal i-edge, exactly one endpoint disagrees with i-independent V, so d<=2delta. Finally Phi(E,d)<=E+d=4delta proves (1). Zero boundaries are continuous and admitted.

The source's antichain theorem pays one exposure by the martingale delta. Repeated private layers require a genuine release of that account; repeatedly assigning 4delta is not allowed.

## 2. Residual physical states and the eligible mark

Before z is queried, every nonconstant residual W is again a common point activation of two residual base branches. A gate answer 1 makes W constant. On other histories the base G is either a point defect at the remaining zero vertex, or constant. If G survives, every queried base coordinate was zero; H is then a product of remaining intact quadratic pairs. Fixing zero at one endpoint of a pair removes that pair. If G has died, H may also contain linear factors, but still has quadratic degree at most two.

Call a node eligible if z is unqueried, no gate has failed, the residual base G is a nonconstant surviving point defect, and the residual base H is nonconstant. Write delta_v=Inf_z(W_v). Put

    M_v=12 delta_v *1{eligible},
    S_v=10 delta_v *1{z unqueried},
    K_v=M_v+S_v.                                    (2)

After z is queried both marks are zero. Eligibility is absorbing: data restrictions cannot turn an ineligible node into an eligible one. Delta is the conditional expectation of the fixed physical disagreement event as long as z remains unqueried. Consequently S is a martingale under data queries, and M is a nonnegative supermartingale.

## 3. Private point-defect exposure releases at least one third

At an eligible node suppose the queried data bit i affects G but not H. This can be x, or a quadratic partner made irrelevant in H by an earlier zero answer. Let l be remaining activation controls, p=2^-l, and h=E H_base. H contains j>=1 intact pairs, so h=2^-j<=1/2. If m is the number of remaining point-defect base coordinates, put a=2^(1-m). The private i is outside the 2j H-relevant coordinates, hence m>=2j+1 and

    a<=h^2<=(1-h)/2.

The true mismatch masses before and after the i query are

    delta=p(1-h+a)/2,
    delta_0=p(1-h+2a)/2,
    delta_1=p(1-h)/2.

The answer 1 kills G and exits eligibility. The surviving zero child remains eligible, since it retains all H-relevant coordinates. Therefore

    E[M_child]=12 delta_0/2 <=(2/3) M_parent,
    M_parent-E[M_child]>=4 delta.                   (3)

Indeed delta_0/(2delta)<=2/3 is equivalent to 2a<=1-h. Apply (1) to the actual activated branches, with all gate Fourier rows present, to conclude

    A_i<=4delta<=M_parent-E[M_child].                (4)

Thus each repeated private exposure consumes released mass of the same original mark. Intervening shared-data and control queries cannot increase its expected mass. At k=2, queried x, the ratio E[M_child]/M_parent is exactly 2/3 for every activation depth; the contraction used in this mark is sharp. This is not a sharpness claim for the final erasure constant.

For the antichain union of all marked private queries, repeated over time, (3) also yields

    sum_marked w_v delta_v <=3 delta_root.

The proof is a stopped supermartingale telescope, not a reset of the root reserve at each layer.

More generally, for any Boolean pair let an eligibility flag be absorbing under data restrictions. At marked private-query nodes suppose the expected eligible-child mismatch mass is at most (1-gamma) times the parent mismatch, for some fixed 0<gamma<=1. The single mark M=(4/gamma)delta*1{eligible} then pays

    sum_marked w A_i + E M_leaf <= M_root.

At marked queries its released mass is at least 4delta, while at other data queries its expected release is nonnegative by absorption and the mismatch martingale. This conditional ownership lemma is reusable without point-defect or quadratic assumptions; proving its release hypothesis for arbitrary certified children is still open. The actual family above verifies gamma=1/3.

## 4. Every other local query is paid by physical influence

For an arbitrary core f with mean mu and singleton coefficient nu at data bit i, activation V=1+A_l(f-1), p=2^-l, has exact data-erasure correction

    B_i(V)=p B_i(f)+E,
    E=Phi((1-p+p mu)^2,p^2 nu^2)
       +p(1-p)Phi((mu-1)^2,nu^2)-p Phi(mu^2,nu^2).

The envelope Phi(u^2,v^2)<=2|uv| and |nu|<=Inf_i(f) give

    B_i(V)<=p B_i(f)+6 Inf_i(V).                    (5)

The envelope follows by differentiating Phi_nat(1,t^2)/(2t) on 0<t<=1: its derivative numerator (t^2-1)ln(1+t^2)-t^2 ln(t^2) is nonnegative by ln(1+x)<=x and -ln x>=1-x. Its maximum at t=1 is ln2. Homogeneity and symmetry complete the proof. Formula (5) is exact at l=0 with E=0.

At a remaining gate query, with j=Inf_t(V),

    B_t(V)=Phi((1-j)^2,j^2)+2j(1-j)<=4j.            (6)

These are direct paired-coefficient counts; derivative squared mass is j, its empty coefficient is -j, and every nonempty pair has equal magnitudes.

If a base data query affects the quadratic H, its relevant influence is at least 1/2. Thus the base mux influence is at least 1/4, and B_i(base mux)<=1<=4Inf_i(base mux). Applying (5) costs at most 10Inf_i(W). This includes histories on which G has died. If H is constant and G survives, that H constant is +1; W itself is a point defect, including gates and selector where present. Both-constant unequal branches similarly give a point defect on gates and z; equal branches give a constant.

A point defect has B_i<=3Inf_i at any relevant coordinate: for at least two relevant bits, delta=2^(1-m) and

    B_i=Phi((1-delta)^2,delta^2)+2delta(1-delta)
       <=delta[2(1-delta)+delta(2(m-1)+log2(e))]<=3delta.

For m=2,3 use log2(e)<2; for m>=4 use 2(m-1)/2^(m-1)<=3/4. A one-bit point defect has B=0. At an eligible private query, its inherited quarter bill is <=3Inf_i(G')/4=3Inf_i(W)/2. Combining with (4), all pre-selector data queries obey

    B_i(W)<=10Inf_i(W)+K_v-E[K_child].              (7)

After selector revelation, the actual branch is a point activation of either a point defect or a restricted quadratic. The point branch has local rate <=3, and the quadratic branch has base B_i<=2Inf_i and, by (5), activated rate <=8. Its gate rate is <=4. Thus (7) still holds with zero bank. Arbitrary irrelevant physical queries have zero B and influence.

## 5. Selector revelation uses the separately retained component

Before z is queried, if G and H are both nonconstant with G surviving, the base mismatch is (1-h+a)/2>=1/4. If G=+1 and H is a nonconstant restricted product of quadratic/linear factors, |E H|<=1/2, so the base mismatch is again >=1/4. This mean bound follows directly from intact pairs (mean magnitude 1/2 each) and linear factors (mean zero). Thus base B_z<=1<=4Inf_z, and (5) gives B_z(W)<=10delta. All remaining constant/point cases have rate <=3 or zero. Therefore

    B_z(W)<=S_v<=K_v,                               (8)

and K is zero on both actual post-selector branches. M has not been assigned again to the selector bill. S is the portion held back throughout the data prefix.

## 6. Any adaptive stopping tree, exact terminals and one budget

For ANY finite adaptive fresh-coordinate tree T on W, let P_D be its actual consumed data influence (s,x,t queries), and P_z the consumed selector influence. Let w_v be actual reach probabilities, with unused dummy queries contracted if desired. Sum (7)-(8):

    B_T(W)+E_T K_leaf <=10 P_D+K_root
                           =10P_D+22delta_root.      (9)

Both summands in K_root belong to the single initial selector-influence account. Twelve units release through the geometric point-defect exits; ten units remain reserved for actual selector revelation. Neither is reset, and unspent K_leaf remains explicit.

Coordinate-wise physical influence conservation gives

    P_D=I_data(W)-E I_data(W_leaf),
    P_z=Inf_z(W)-E Inf_z(W_leaf),
    P_D+P_z=I(W)-E I(W_leaf).                       (10)

Unqueried-coordinate influences are preserved in conditional average by any other coordinate query. Thus early selector revelation does not invent a data reserve, and arbitrary data exposure does not consume the actual selector influence before it is revealed.

The entropy identity is exact:

    H(W)=B_T+JS_T+E H(W_leaf),
    JS_T<=(2/ln2)(P_D+P_z).                        (11)

At a leaf with z unqueried,

    H(W_leaf)=[H(G'_leaf)+H(H'_leaf)]/2+R_leaf,
    R_leaf=sum_C[phi((g_C+h_C)^2/4)+phi((g_C-h_C)^2/4)
                           -phi(g_C^2)/2-phi(h_C^2)/2].

When z is revealed the exact selected branch entropy is retained instead. K_leaf is an influence-owned allowance, not a replacement for these terminal spectra. The JS bound follows by differentiating
[(1+t)ln(1+t)+(1-t)ln(1-t)]/2<=1-sqrt(1-t^2).

For complete constant-leaf trees, (9)-(11) imply

    B_T,Q_T<=10I_data(W)+22Inf_z(W)<=22I(W),
    H(W)<25I(W).

Here Q at a node is sum min(u_T^2,v_T^2)log2((u_T^2+v_T^2)/min), with zero boundaries. Each summand is one of the two nonnegative summands of Phi, so Q_T<=B_T without an additional hypothesis.

The existing H(W)<8I(W) paid-order result is stronger as a class entropy bound. The new result is arbitrary interleaving with repeated private exposures, actual selector timing, and exact stopping terminals; no class-constant improvement is claimed.

## 7. Exact universal gap

The release (3) depends on a private answer killing the unique point defect and on a<=(1-h)/2. For arbitrary Boolean cores both answer branches can remain eligible, so delta's conditional average is unchanged and no analogous released mark is available. A076's repeated quadratic/literal example already refutes a selector-only reset without core payment. NEXT must replace the exiting point-defect mass by genuinely unused, certified signed child surplus at a second private collision with two nonconstant children. The inherited quarter core bill and both full terminal laws must remain. This is the first unsupported line toward universal C019, not a claimed universal theorem.
