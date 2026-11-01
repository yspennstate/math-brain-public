# The next genuine seed query: an exact inherited-bank obstruction

Bits for H, CE, KL, JS; natural logs for b and the heat area K. This continues A066-NONFLAT-DATA-RELEASE-AND-SOURCE-PAYMENT v2. It refutes a proposed literal-reference continuation of that admission, not v2 itself, FEI, or existence of a different paid query/calibration policy.

## 1. The correct signed payment identity

For ANY Boolean sign g and a physical singleton i, write a_T=ghat(T), c_T=ghat(T+i). Let p be the full Fourier probability and p_+,p_- the actual full child probabilities. Fix a complete normalized reference Q of finite CE. KEEP both physical children, including dummies. Set

    pbar(T)=a_T^2+c_T^2=(p_+(T)+p_-(T))/2,
    Qbar(T)=Q(T)+Q(T+i).                                      (1)

Both children inherit the SAME literal full Qbar. Positive child mass implies positive Qbar, so CE stays finite even if Q has zeros off actual support. Define

    B=H(p)-H(pbar) >=0,
    J=H(pbar)-E_s H(p_s) >=0,
    D=sum_T pbar(T) KL(p(v|T)||Q(v|T)) >=0,
    C=CE(p,Q)-E_s CE(p_s,Qbar).

The entropy and CE chain rules give EXACTLY

    DeltaH=B+J,  C=B+D,  DeltaH-C=J-D.                       (2)

Indeed C=sum_(T,v) p(T,v)log2[Qbar(T)/Q(T,v)], with zero actual terms omitted. It is nonnegative. But CE decreasing does NOT imply it pays the true entropy decrement: J, not -J, is added to erasure. The failed draft used B-J; its first pilot rejected that identity on the genuine two-bit negative AND. Rejected draft and helper are preserved in out/DRAFT_v1_REJECTED.md, code/check_v1_failed.py and out/PILOT_v1_FAILURE.json. They are not proof dependencies. Formula(2) is reconstructed here independently of A014's CE-only monotonicity. No novelty is claimed for erasure/JS chain rules or for reference projection.

For a finite adaptive forest, with ORIGINAL reaches w_h, (2) telescopes to

    sum_h w_h Delta_h H + E_leaf CE - CE_root
       =E_leaf KL - KL_root =sum_h w_h(J_h-D_h).              (3)

Every entropy decrement is nonnegative since B,J>=0. Both full terminal CE/KL bills remain. Old debits cannot be undone. No negative later entropy bill is used to refund a previous spend. Nonnegative conditional KL D is an actual reference-code refund and cannot also be spent a second time elsewhere.

## 2. Exact v2-admitted source with no initial off-support mass

Take d=1, b(x)=(-1)^x, delta=1/2. Use precisely the v2 attachment, ordered as (j,z,x):

    F=(1,-1,-1,-1,-1,-1,-1,-1),
    F_0=(1,-1,-1,-1) on (z,x), F_1=(-1,-1,-1,-1).

Its spectra are

    p_F=(9/16,1/16,1/16,1/16,1/16,1/16,1/16,1/16),
    p_0=(1/4,1/4,1/4,1/4), p_1=(1,0,0,0).

Choose the ORIGINAL finite-cost complete references, before the first debit,

    Q_0=(1/10,2/5,1/10,2/5), Q_1=(1,0,0,0).                 (4)

These references have EXACTLY the actual spectral supports. In particular Q_1 does not carry unused mass on its physical dummy z or x. A cleanup of initial occupied ghosts cannot supply the missing margin in this example. Complete means a normalized law on the complete physical spectrum, positive wherever actual p is positive; strict positivity on zero-actual atoms is unnecessary and was not a v2 hypothesis.

Physical edge counts give Ibar=1/2, e=Inf_j(F)=1/4, I(F)=3/4, R=(d+1)e=1/2. Fix ORIGINAL quota A=4 Ibar=2 and old debit tau=Ibar/4=1/8. Do not renew them after j. The opening complete terminal cost is

    E CE(F_s,Q_s)=(1/2)log2 5.

The root entropy is H(F)=4-(9/8)log2 3, so Delta_j H=3-(9/8)log2 3 <=5/4=5e. Thus the ACTUAL v2 extra spend L=max(Delta_j H-5e,0) is zero. The same original source and residual are

    U=15/8-(1/2)log2 5 =7/8-(1/2)log2(5/4),
    S=U-R-L=3/8-(1/2)log2(5/4).                             (5)

The v2 admission is satisfied:

    U>=3R/2-e/4=11/16,

equivalent to log2(5/4)<=3/8, certified by 5^8<2^19 (390625<524288). L=0 is certified by 3^9>2^14. Also S>=0 follows from admission. Therefore this is an actually admitted physical state with both full references and an old prior debit, not a freely rescaled local capacity.

## 3. Query the actual seed x next, on BOTH physical j branches

The F_0 children are the z literal and the constant -1. Their full spectra are (0,1) and (1,0). The F_1 children remain constants. Literal projection of (4) gives

    Qbar_0=(1/5,4/5), Qbar_1=(1,0).

For F_0, B=1,J=1,D=0,C=1,DeltaH=2. Conditional D=0 because both Q_0 and p_0 have uniform conditional x occupancy at each residual z atom. For F_1 every one of these costs is zero. At ORIGINAL reach1/2 for each j child,

    E Delta_x H=1, E C=1/2, E(J-D)=1/2.

The inherited old reserve has r_0=d delta=1/2 and r_1=0; the seed query removes it, releasing E r=1/4=R-e. The query therefore needs an additional1/4 from the SAME already-reduced S. But

    S<1/4 <=> log2(5/4)>1/4 <=>5^4>2^9 (625>512).           (6)

Thus the exact v2 admission alone does NOT guarantee this next prescribed data payment under unchanged FULL-reference projection. This is not merely failure of a conservative booking. Even if ALL unused slack of the first j charge is recovered and S is spent down to zero, the mandatory whole ledger has

    Delta_j H+E Delta_x H+E terminal CE+tau -(A+4e)
      =[5+4log2 5-9log2 3]/8
      =(1/8)log2(20000/19683)>0.                             (7)

Here E terminal CE=(1/2)log2(5/2), and the final old reserve is zero. Formula(7) has the exact rational sign20000>19683. No decimal sign or interval precision is needed. It retains both old terminal bills, the ORIGINAL quota, the old debit, actual L and the dummy z. It is a counterexample to the stated CONTINUATION rule, not to Boolean FEI: H(F)<4I(F), and no claim about every possible next query is made.

## 4. Paid empty calibration repairs this particular witness

Let u_s=p_s(empty), q=Qbar(empty). Preserve the old conditional nonempty profile but set

    Qcal_s(empty)=u_s,
    Qcal_s(T nonempty)=(1-u_s)Qbar(T)/(1-q).

Zero-sector endpoints use the corresponding point mass. Finite CE ensures occupied sectors have positive reference mass. The EXACT release from calibration is

    V=E_s KL(Ber(u_s)||Ber(q)) >=0,
    Ccal=C+V,  DeltaH-Ccal=J-D-V.                            (8)

This is a supplied-reference categorical identity, not a free replacement of the conditional nonempty profile. It agrees with the distinction in A014 v6: its calibration transports FULL CE, while a true entropy bill still needs its signed JS comparison. The two principles must not be conflated.

In the witness each remaining physical cube has one bit z. Its nonempty sector has just one atom. Calibration therefore makes every terminal reference its actual point-mass spectrum, without changing any conditional nonempty profile. Terminal CE becomes zero, and the original rate-four ledger, including old tau, is paid. It releases E terminal CE=(1/2)log2(5/2)>0. The witness does NOT refute A014, actual-occupancy calibration, a carefully selected continuation, or arbitrary-source FEI. Its role is to prohibit claiming that literal CE monotonicity alone closes the true A066 debit.

## 5. Semigroup endpoints, boundary, and the residual charge

For every finite Boolean g, write p=ghat^2, q_t(S)=p(S)exp(-2t|S|),

    J_g(t)=sum_nonempty |S|q_t(S)ln(1/p(S)),
    K(g)=integral_0^infinity J_g(t)dt,
    b(g)=p(empty)ln(1/p(empty)).

The corrected heat identity is2K=ln2 H-b. The raw entropy derivative requires subtraction of2t sum|S|q_t. At small times J_g(t)<=J_g(0); at large times J_g(t)<=exp(-2t)J_g(0). Both endpoints are integrable for each finite g. A universal2K<=C I would imply FEI since b<=Var<=I. The pointwise no-integrable-envelope obstruction from earlier stages is unchanged; no function supremum is interchanged with time integration.

There is also a uniform absolute SINGLETON boundary payment, not inferred in v2. Let m=E g and phi(m)=-m^2 ln(m^2), phi(0)=0. Its continuously extended derivative is -2m(ln(m^2)+1). For |m|=exp(-r), r>=0, exp(-r)|2r-1|<=1: on r<=1/2 it is at most1, and on r>=1/2 its maximum is2exp(-3/2)<1. Hence |phi'|<=2. Writing child means m+a,m-a, Booleanity gives |a|=|E(g_+-g_-)|/2<=e_i=Pr(g_+!=g_-). Therefore

    |Delta_i b|<=2|a|<=2e_i (natural-log units).              (9)

Its sign may be either. Over any finite adaptive tree, sum reach*|Delta b|<=2 sum reach*e_i<=2I(g). This uses the physical Boolean mismatch bound, stronger than only a^2<=e_i. It pays the boundary, not the nonempty spectral information debt.

For the COMPLETE heat reference Psi(g,Q)=ln2 CE(g,Q)-b(g)=2K+ln2 KL(p||Q), (2) and (8) give

    2Delta K+E_s Psi(g_s,Qbar)-Psi(g,Q)=ln2*(J-D),
    2Delta K+E_s Psi(g_s,Qcal_s)-Psi(g,Q)=ln2*(J-D-V).         (10)

The signed boundary cancels EXACTLY when retained in the terminals. These expressions are not asserted nonpositive. The earlier false draft had the wrong sign on J in precisely this identity. A querywise physical bound on the remaining JS exists, but using it on top of an already assigned A would require a legitimate UNUSED influence/source owner, not a second use of the same quota.

## 6. Correct bank test and first unsupported line

At an actual next frontier, denote its expected old-reserve release by dr>=0. The signed net demand on the same remaining source is E(J-D-V)-dr after paid categorical calibration (set V=0 for literal references). Its positive part must be covered by the actual remaining S, with earlier tau/L permanently booked. This is an exact eligibility test, not a proof that S supplies it. If it passes, the source, full references, old bills and same remaining reserve telescope correctly. The three-bit witness proves that the previous admission is insufficient if V is left unpriced/omitted.

FIRST UNSUPPORTED UNIVERSAL LINE: choose and pay a genuine post-calibration conditional-NONEMPTY profile/data continuation so that the positive signed residual E(J-D-V)-dr fits in the SAME diminished original source after all old debits and both terminal CE/KL bills. Alternatively supply a universally cheap opening reference and stronger valid source invariant. Neither a new reference nor a fresh local K I is a permitted substitute. Conditional nonempty profile replacement adds its actual CE conversion separately; the simple categorical repair above does not pay arbitrary changes of that profile.

Rung: complete analytic author derivation and exact rational certificates; independent A070/A088/A094 review pending. No full Lean certificate, universal source payment or full FEI proof is claimed.
