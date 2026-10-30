# Dummy-data resets with both full terminals and the original bank

Units are bits. This extends A096's active-reset and A097's mixed active/control supplied-reference mechanism; it is not a universal source construction. The proof below closes their next dummy-data exposure at the same original rate. Imported floor/active envelopes are the exact versions recorded in CLAIMS.json; independent review of this new extension remains pending.

Let a>=1,b>=1,r>=1, n=a+b, s=2^-a,t=2^-n,e=2^(1-n-r),mu=1-2s. Set g=1-2A_a and F=g+2A_(n+r). Supply a normalized finite-source-cost R on the n data spectral bits, calibrated by R(0)=mu^2. Write c=CE(P_g,R), L=n+r. Its complete canonical floor is

    R_e(T)=(1-e/s)R(T)+(e/s)mu 1_(T=0)+2et,
    Q(T,U)=R_e(T) P_F(T,U)/M_e(T),
    M_e(T)=sum_U P_F(T,U).

The imported A097 floor inequality is CE(P_F,Q)<=W=c+10eL. All denominators M_e(T)>0, since each control-nonempty Fourier amplitude is e>0. R_e is normalized and positive. The source may have arbitrary reference-only mass, including on labels involving a dummy data bit.

## 1. Source marginalization and calibration

Query a dummy physical data bit j. The off-child is g; keep its FULL inherited reference Q_-j. The on-child is the same family with (a,b-1,r,e'=2e). Let V=R_-j and calibrate its empty atom to mu^2, obtaining Rbar. Since V(0)>=R(0)=mu^2, calibration increases every nonempty V atom: Rbar(T)=V(T)(1-mu^2)/(1-V(0))>=V(T). On the true source support, T is active-only, so V(T)>=R(T), while Rbar(0)=R(0). Hence cbar=CE(P_g,Rbar)<=c, POINTWISE on every occupied source atom. The zero-true-mass vacuum at a=1 contributes zero and is never logged. Finite source cost ensures V(0)<1 because the nonempty active singleton has positive true mass and positive reference mass. This proves finiteness and rules out the only potentially vanishing calibration denominator.

Reset ONLY the on-child to the specified canonical floor built from Rbar, with b replaced by b-1. Its complete envelope is W_on=cbar+20e(L-1). This reset retains the reference marginal of the already supplied source; it assumes no new influence-priced source certificate at the child.

## 2. Full complementary likelihood bill

For a nonempty true source label T, the inherited off-reference atom is Q(T,0)+Q(T+j,0). Its second term is nonnegative, and its first term equals R_e(T)kappa, where

    kappa=(2s-e)^2/(4s^2-4se+2te).

Here h=e/s<=1/2 and t<=s/2, since b,r>=1. All denominators are strictly positive. Indeed 2s-e>=3s/2 and

    kappa^-1-1=(2te-e^2)/(2s-e)^2 <= (se)/(2s^2)=h/2.

The numerator is nonnegative because e<=t. Therefore Q_-j(T,0)>=(1-h)R(T)/(1+h/2). At the vacuum, exact empty calibration gives Q(0,0)=(mu+e)^2>=mu^2=R(0); additional marginalized reference mass is retained. There is no total-variation substitution.

The total nonempty source probability is v=4s(1-s)<=4s. Using -log2(1-h)<=2h on [0,1/2] and log2(1+h/2)<=h/(2ln2) gives the SIGNED complete off-child bound

    c_off-c <=v[2h+h/(2ln2)] <= (8+2/ln2)e <11e,

where ln2>2/3. All reference-only atoms and all control normalizers remain in c_off.

## 3. Actual dummy erasure and the local substitution

Every non-active physical coordinate has the same Fourier-pair geometry in this Boolean F, even though its supplied reference is not symmetric. Direct coefficient summation gives

    sum_pairs |alpha beta|=e[4-4s+2e-2e/s]<=4e.

The scalar inequality phi(alpha^2,beta^2)<=2|alpha beta|/ln2 follows from ln(1+z^2)<=z (integrate 2z/(1+z^2)<=1); zero amplitudes follow by continuity. Hence the ACTUAL query debit B_j(F)<12e. Combining this, both full child bills, and cbar<=c proves

    B_j(F)+(c_off+W_on)/2
       <c+10eL+(12+11/2-10)e
       =W+(15/2)e < W+8e.

This is an envelope comparison, not a local influence inequality. In particular the old erasure debits and other already retained terminals have not been removed.

## 4. All eligible mixed histories at the SAME original rate

Start with a_root>=1,b_root>=0,r_root>=1 and d=b_root+r_root>=2. Supply an uncalibrated source reference of cost <=C0 I(g), C0>=0; calibration only decreases cost. Put K=2C0+10. Follow any adaptive sequence on the surviving edited branch of: (A) active queries with A096's reset and explicit a=1 point boundary; (D) the dummy-data reset above whenever b>=1; (C) A097's control reset whenever r>=2. Each complementary branch keeps its full inherited reference and either stops or continues with no resets. Every stopping cut retains all full terminal bills.

Each nonterminal on-step halves its physical reach rho and doubles e, so rho e_current=e_root. Active steps cost at most their previous W; the new D and prior C steps each cost less than W+8e_current. There are at most d-1 non-active steps before b=0,r=1. Consequently

    booked expected erasures + ALL full terminal CE
       <= W_root+8(d-1)e_root.

No matter how much of this has already been spent before a dummy query, it remains charged to the SAME original quota. Let Ig=2a_root*s_root,E=a_root*e_root,X=d*e_root. The exact influence is I(F)=Ig+X-E. Since E/Ig=2^-d<=1/4,

    K I(F)-W_root
       >=(C0+10)(Ig-2E)+2C0 X >=5Ig
       =5a_root*2^d*e_root.

For every integer d>=2, 5*2^d-8(d-1)>=12: equality at d=2, and the increment is 5*2^d-8>0. Thus the COMPLETE history ledger is <=K I(F_root)-12e_root. Structural R=P_g has C0=4 and unchanged K=18. Arbitrary independent untouched terminal references remain additive and fund nothing. Different labels and adaptive orders are covered by the local proof; finite validation uses only a fixed least remaining label per type and does not claim to exhaust asymmetric label permutations.

## 5. Checks, scope and first unsupported line

The checker independently reconstructs truth tables by direct integer character sums, verifies physical edge influence, normalizations, true child spectra, full inherited references and all mixed type histories in its frozen finite domain. Log enclosures use a fixed 12-term atanh expansion after exact reduction to [1,2), with positive tail 2z^25/[25(1-z^2)]. Signed linear combinations use outward interval arithmetic. There is no precision refinement. Boundary a=1 is checked through the explicit point-law rule, not the false active-erasure comparison. Finite cases verify the implementation; the analytic argument supplies the quantifiers.

Rung: analytic proof with exact finite validation if RESULT.json is PASS; new extension awaits independent reconstruction. Lean was NOT launched: memok refused admission (physical free 2.2 GB versus required 4.0 GB). The key rational inequality is saved separately; it is not a Lean certificate. Full FEI remains OPEN. The first unsupported universal line is construction/payment of a generic complete source reference or a prescribed fresh reset in a retained off-branch after the preceding debits, from the same remaining account. The point-source geometry and calibration above cannot be silently extended to a signed non-point source.
