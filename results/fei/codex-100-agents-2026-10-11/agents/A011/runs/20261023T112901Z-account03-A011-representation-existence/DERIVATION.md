# Count-independent actual edit construction with one original reserve

Author proof, independent reconstruction pending. Bits and complete subprobability reference costs throughout. Full FEI remains OPEN.

## Exact family and references

Let g be ANY nonconstant Boolean function on a>=1 uniform bits. Supply a nonnegative reference R, mass s in(0,1], covering P_g, finite c=CE(P_g,R)<=C0 I_g, C0>=0. Fix b>=12 padding bits ONCE. For each finite M>=1 choose arbitrary widths r_j>=1 and arbitrary points z_j of the entire current cube of dimension D_(j-1), where D_0=a+b and D_j=D_0+sum_(i<=j)r_i. At operation j add r_j fresh controls and flip the current Boolean function at z_j when all fresh controls equal0. F_0=g with padding; F_j is this ACTUAL successive point edit, with the sign determined by F_(j-1)(z_j). Put rho_j=2^-D_j. Points may overlap, undo earlier flips, involve all old controls, or hit different stopped siblings. The initial rate K=4C0+15 is never renewed. There is no infinite-dimensional Boolean function claim: every finite M is covered with constants independent of M.

Keep the EXACT first and second references already prescribed by A011 v3: first data floor coefficient6rho_1, second coefficient8rho_2, each lifted by the true conditional fresh-control law. For j>=3 set

    eta_j=1/[8j(j+1)], alpha_j=1+eta_j,
    s_j=j(j+1), A_j=1+s_j, B_j=1+4s_j,
    beta_j=4 B_j rho_j.

Prescribe data reference (Q_current+beta_j U)/(1+beta_j), then its TRUE control-kernel lift. At a physical node at depth d, use rho_j,local=2^d rho_j and the local ambient data dimension. If the node does not contain z_j, its function and reference are simply embedded with zero fresh-control frequency. If it contains z_j, update the ACTUAL incoming model just described. No first/second model is reset, no descendant source certificate is assumed, and every mass normalizer remains in CE.

The physical tree is exactly the old A011 padding-then-source comb: expose padding along the first edited point, then source coordinates along that point in any adaptive order, stopping all nonmatching siblings. All controller bits remain unqueried. The theorem covers its root and EVERY old nonempty padding/source frontier, for EVERY operation prefix M. All source reference restrictions at the initial construction use original R and the physical mass-preserving inheritance already reconstructed by A086. Later updates at every node use its actually current model, even after previous edits hit that node.

## 1. Sharpen the price of the existing first floor without changing it

For a Boolean source h on n>=1 data bits, r>=1 controls, p=2^-r,t=2^-n,rho=pt, the actual data marginal is q_T=A_T^2-4rho b_T A_T+4pt^2. Young eta=1/4 gives

    q <=(5/4)P_h+12rho U_n.

The ACTUAL first floor remains (Q+6rho U)/(1+6rho). Its nonnegative losses allow the new analytical domination above without changing that model. Since 6rho<=3/2, log(1+6rho)<=12rho and <=3, while log(1/(6rho))<=n+r-2,

    CE_data <=(5/4)c_h+rho(24n+12r+27).

For any point edit, the total nonempty fresh-control frequency mass is e=4p(1-p)t. Jensen gives conditional-control entropy <=h2(e)+er<=4rho(n+2r+2), using e>=2rho, e<=4rho and log2(euler)<2. Consequently the EXISTING first model obeys

    CE_first <=(5/4)c_h+48rho(n+r).                 (1)

Indeed 48(n+r)-(28n+20r+35)=20n+28r-35>=13. At zero remaining source dimension the old scalar floor mass (s+6p)/(1+6p)>=s gives CE<=c_h+16pr, also <=(5/4)c_h+48pr. This boundary is handled directly, not by invoking n>=1 at n=0.

The ACTUAL second model, unchanged from v3, still obeys

    CE_second <=(3/2)CE_current+40rho_2,local D_2,local. (2)

Thus no conversion from the old8rho floor to a newly chosen second floor is hidden in this proof.

## 2. Average complete costs at the paid two-edit frontier

Source complete CE contracts under original mass-preserving physical inheritance: entropy and complete divergence each contract. All source terminal CE values are nonnegative, including constants with -log s. At a nonempty padding frontier let v=2^-ell<=1/2; at a source frontier after padding let v=2^-b. For its first-active source restriction h and physical reach lambda, lambda c_h<=v c. If h is fully exposed, this includes its scalar mass penalty.

Replacing just the first active source leaf by its prescribed first floor, (1) gives

    Cbar_1=E CE_first,leaf <=(1+v/4)c+48rho_1D_1.

If the second point hits that first active leaf, its old weighted CE is at most(5v/4)c+48rho_1D_1; (2) therefore gives Cbar_2<=(1+7v/8)c+72rho_1D_1+40rho_2D_2. If the second point instead hits a distinct source leaf, its weighted CE is at most c/2: an off-padding sibling reaches at most1/2 and retains g,R; an off-source sibling has weighted CE<=2^-b c. The resulting source coefficient is <=1+v/4+1/4. Uniformly, because v<=1/2,

    Cbar_2 <=(23/16)c+72rho_1D_1+40rho_2D_2.       (3)

At the ROOT, (1),(2) instead give

    CE_2,root <=(15/8)c+72rho_1D_1+40rho_2D_2.     (4)

Equations(3),(4) keep the existing first and second complete models. They are analytical improvements to their costs, not new source certificates.

## 3. Every later actual floor has a summable multiplicative price

At a reached edited node at stage j>=3 the unqueried previous controllers give n>=j-1; D_local=n+r_j>=j. Young eta_j gives

    q <=alpha_j P_current+4rho_local(1+p_j/eta_j)U
       <=alpha_j P_current+4B_j rho_local U.

The chosen beta=4B_jrho_local is <=25: B_j2^-j decreases for j>=2, since B_(j+1)<=2B_j, and the j=2 value is25/4. Hence log(1+beta)<5, alpha_j<2 and log(1/beta)<=D_local. The same direct entropy bound as in section1 gives

    CE_new <=alpha_j CE_current
                    +beta(3D_local+11)
           <=alpha_j CE_current+36B_jrho_local D_local. (5)

Here D_local>=2, so3D_local+11<=9D_local. All log losses are nonnegative since every actual model is a subprobability. Mass changes from m to(m+beta)/(1+beta) on a hit and is retained on a miss; no scalar penalty disappears.

At any fixed frontier, exactly one leaf contains the new point. Its physical reach lambda converts rho_local back to rho_j. Complete CE is nonnegative on every leaf. Thus

    Cbar_j <=alpha_j Cbar_(j-1)+36B_jrho_jD_j.

The identical recurrence holds for root CE. Since sum_(j=3)^M eta_j=1/24-1/[8(M+1)]<1/24,

    product_(j=3)^M alpha_j <=1/(1-sum eta_j)<=24/23. (6)

To justify (6), expand the product or use product(1-eta)>=1-sum eta and 1+eta<=1/(1-eta). No independence or multiplicative conditional-probability claim is involved. Iterating (5) from the ACTUAL models in(3) gives

    Cbar_M <=(3/2)c+(24/23)[72rho_1D_1+40rho_2D_2
                                  +36sum_(j=3)^M B_jrho_jD_j]. (7)

For M=2 this bound remains valid. At the root replace the source coefficient3/2 by45/23. Future products, each at most24/23, pay each additive term once; no source owner is renewed.

## 4. One scalar entropy bound for arbitrarily many overlapping edits

On the final cube F_M=g+sum_j delta_j, where delta_j is a signed point cylinder on its first D_j coordinates. Its squared Fourier amplitudes are4rho_j U_Dj. With weights w_j=1/[j(j+1)], sum_(j=1)^M w_j<1. Weighted Cauchy and Young eta=1/4 give

    P_FM <=(5/4)P_g,embedded +5sum_j s_j delta_jhat^2
          =(5/4)P_g,embedded +sum_j20s_jrho_j U_Dj.

The normalized mixture of the EXACT source spectrum and these floors is used ONLY as an auxiliary scalar entropy comparison. Its total floor B<=160*2^-(a+b)<1/2, because sum_j j(j+1)2^-j=8 and D_j>=a+b+j. At every D_j>=8 its CE yields

    H(F_M) <=(5/4)H(g)+50sum_j s_jrho_jD_j.         (8)

Indeed log(1+B)<=2B, log(1/(20s_jrho_j))<=D_j, and the total cost over floors is at most sum beta_j(2D_j+4)<=sum(5/2)beta_jD_j. The root source contribution(5/4)log(1+B)<= (5/2)B fits the looser4B overhead. No auxiliary exact-source model replaces an actual terminal.

## 5. Full history, all target prefixes, exact old booking

For the fixed F_M physical tree, define the signed complete reset at each internal node by avg D_child-D_parent using the actual prescribed stage-M models. Its root CE and all reset increments telescope EXACTLY to

    L_M=H(F_M)+E D_full_terminal
       =H(F_M)+Cbar_M-E H_true_terminal.           (9)

Using nonnegative last term, (7),(8) give at every old nonempty frontier, and also at the root,

    L_M <=(11/4)c+201 S_M,
    S_M=sum_(j=1)^M A_jrho_jD_j.                   (10)

For j>=3 the additive coefficient is(864/23)B_j+50s_j=(864+4606s_j)/23<=201A_j. At j1 it is1728/23+100<=201A_1; at j2 it is960/23+300<=201A_2. The root source coefficient45/23 is smaller than11/4. These deliberately loose inequalities unify all frontiers. For M=1 use(1) and the same entropy comparison; its source coefficient<=5/4+9/8<11/4 and its additive bound also fits(10).

All widths may vary. Since x2^-x decreases for integer x>=2, D_jrho_j<=(a+b+j)2^-(a+b+j). Exact geometric moments sum A_j2^-j=9 and sum jA_j2^-j=34 give

    S_M <=2^-(a+b)[9(a+b)+34].

This is a proved infinite majorant, not a finite extrapolation. An exact finite tail certificate, L=a+b, is

    sum_(j=1)^M A_j(L+j)2^-j
     =9L+34-2^-M[M^3+(L+7)M^2+(5L+23)M+9L+34]. (11)

It follows by subtracting consecutive partial sums; the positive polynomial tail tends to0. Minimum cube boundary I_g>=2a2^-a, b>=12 and monotonicity in b imply

    S_M/I_g <=(9b+43)/2^(b+1)<=151/8192.          (12)

Let d_(j-1) be the actual pivotal degree of F_(j-1) at z_j, E_j=2rho_j d_(j-1), G_j=2rho_j(D_j-d_(j-1)). Literal cube edges give

    I(F_M)=I_g+sum_j(G_j-E_j).

Since d_(j-1)<=D_(j-1)<=D_j,

    sum E_j/I_g <=(b+3)/2^b<=15/4096,
    I(F_M)>=(4081/4096)I_g+sum G_j.               (13)

The same sparse geometric sum proves(13) for EVERY operation prefix and arbitrary edited points, including cancellations. Combining(10)-(13) at K=4C0+15,

    K I(F_M)-L_M >=[(1265/1024)C0+92079/8192]I_g
                                     +K sum G_j. (14)

Retain the FULL nonvanishing old booking from A094's new first-edit allowance,

    0<=U<=(C0+37/8)I_g.

Then root and EVERY old padding/source frontier at EVERY M satisfy

    K I(F_M)-L_M-U >=[(241/1024)C0+54191/8192]I_g
                                     +K sum G_j>0. (15)

This includes the previous smaller U_star in full. A094's first-edit theorem guarantees the named larger booking was eligible before the later operations; (15) independently verifies it for every prefix in this narrower b>=12 regime. All dimensions/counts are universally quantified; finite tests validate definitions and signs only.

The original account is S=K I_g-c. For an already booked preceding construction bill L_(M-1), define the actual operation debit Delta_M=L_M-L_(M-1). Then B_M=B_(M-1)+K[I(F_M)-I(F_(M-1))]-Delta_M EXACTLY, and also B_M=S+K[I(F_M)-I_g]-(L_M-c)-U. The old bill remains charged; Delta changes the target as well as the model and is NOT a KL-only reset. Within each fixed target, (9) retains every old signed reference conversion and both complete terminal bills. Independent tensor references retain additive CE/KL and multiplied masses, without funding this account.

## 6. Precise limitation and a Boolean guard

The fixed-padding, fixed-rate edit-count inflation is removed for this FRESH-CONTROL family. It does not construct every Boolean function. All edit cylinders together have measure at most sum rho_j<=2^-(a+b). Thus F_M disagrees with g on at most2^-(a+b) of its cube. Parity of ALL D_M variables has disagreement EXACTLY1/2 with every function of the first a coordinates, so it cannot belong to this construction at any M>=1. This is an actual Boolean representation obstruction, not a counterexample to FEI (parity has zero entropy).

For fixed-ambient-dimension edits, rho_j need not decay: the polynomially weighted error S_M and erased-edge bill can accumulate. The first unsupported universal continuation is a source/policy-compatible supplier or selection rule ensuring those TWO aggregate costs are paid for an arbitrary target, without inserting a new source certificate or increasing padding. Arbitrary controller-query policies are also not certified by the old comb. The NEXT target is this aggregate admission line, not another fixed edit-count result. Full FEI remains OPEN.

There is an exact obstruction to merely asserting the same positive majorant is universally affordable. In a FIXED N-dimensional cube, take source g=x1 (I_g=1,c=0 under its exact source law), and target parity of ALL N coordinates. Any point-flip construction needs at least M=2^(N-1) distinct corrections, independent of ordering. With rho=2^-N the same proposed majorant is

    S=N2^-N sum_(j=1)^M[1+j(j+1)]
     =N2^-N[M+M(M+1)(M+2)/3]
     >=(N/3)2^(2N-3).

It diverges although target parity has H=0. Thus S<=constant*I_g is FALSE as a universal fixed-dimension continuation of this positive-sum method. A useful next mechanism must retain coherent signed Fourier cancellation or change the representation primitives; another positive-floor count estimate cannot close FEI.
