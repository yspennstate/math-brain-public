# A094 stage 5

Target: full A086-UNEQUAL-AMPLITUDE-NEUTRAL-POINT-FLOOR@1 and A097-NEGATIVE-CELL-FLOOR-SOURCE-BANK@1. Verdict HOLDS at the entire stated scopes, without source repairs. Additional challenge: expose an active data coordinate while retaining the incoming complete reference. Full FEI OPEN. All information quantities below are in bits, with ordinary physical influence and separate single-word rounding.

## 1. Signed law, physical surgery and complete mixture debt

For any Boolean source g, edit (x*,y*) under r fresh point controls, p=2^-r,t=2^-n: F=g-2g(y*)1_x*1_y*. Write a_T=g_hat(T), b_T=g(y*)chi_T(y*), rho=4pt. Direct Fourier expansion gives F_hat(empty,T)=a_T-2pt b_T and all nonempty control coefficients -2pt b_T chi_U(x*). Summing the 2^r control choices yields the actual data marginal q_T=a_T^2-rho b_T a_T+rho t. This expression is signed, not an automatic positive mixture. If j old data edges at y* were pivotal, C=2pt(n-j), E=2ptj, J=2rpt; I(F)=I(g)+C-E+J. Every erased edge is subtracted. The total nonempty control spectral mass is V=(1-p)rho and is uniform on 2^r-1 sets. Hence the actual conditional control entropy B<=H(S_control)<=rho(n+2r), by h2(V)<=Vlog2(e/V) and exact cancellation of log2(1-p).

Given a proved positive mixture q=sum_l w_l P_l and reference mixture Rprime=sum_l w_l R_l, use the actual control kernel K(U|T)=P_F(U,T)/q_T, normalized on every fiber. Q=Rprime K retains the full reference mass and all true support. Analytical mixture labels are not transmitted physical children. True/reference joint likelihood factorization proves

    D(P_F||Q)=sum_l w_l D(P_l||R_l)-kappa,
    CE_F=sum_l w_l CE(P_l,R_l)+H(w)-H(label|T)-kappa+B,

with kappa the measured conditional posterior KL for those SAME references. For subprobability R_l their missing mass is retained in the generalized divergence; adding a failure atom proves nonnegativity. Zero-weight labels are omitted, so endpoint mixtures cause no division by zero. These identities are independently reconstructed and every actual output atom and component likelihood is checked exactly.

## 2. Full A086 neutral unequal-amplitude proof

Let g=1-2AND_3 with three dummy data bits. Its mean is 3/4, its seven nonempty active-only coefficients are -1/4, and its others vanish. At any negative point its active phases are fixed and dummy phases affect only zero source coefficients. The source identity a_T=-4P_g(T)+3*1_empty(T) thus gives

    q=(1-4rho)P_g+3rho delta_empty+rho U_6.

The prior is positive and sums to one for every r>=1. For ANY fixed subprobability R positive on P_g support, Rprime replaces only the P_g component. Its mass is (1-4rho)||R||+4rho; uniform mass covers off-source zeros. The exact identities in section 1 give precisely the source CE and debt clauses, including the entire conditional source divergence.

I(g)=3/4 and the edited point has three erased and three created data edges, C=E=6pt; I(F)=3/4+J. The coarse label entropy is H(w)=h2(4rho)+4rho h2(1/4), with log2(1/(4rho))=r+2. Dropping only nonnegative posterior terms gives CE_F<=c+rho[6r+20+4/ln2+4h2(1/4)]<=c+rho(6r+30)<=c+72J. The proof uses ln2>2/3 and h2(1/4)<1, not floating optimization. For every rate K the inherited source slack is S_K=3K/4-c and KI(F)-CE_F>=S_K+(K-72)J. An independent arbitrary terminal retains its full additive CE and KL through the fixed product reference. Every clause of the exact source claim holds; no active-reference hereditary claim is imported.

## 3. Full A097 all-width negative-cell source-bank proof

Set g=1-2AND_a with b dummies, n=a+b, s=2^-a, t=2^-n, mu=1-2s, lambda=2p2^-b, rho=4pt=2s lambda. The old coefficients are mu at empty, -2s on nonempty active subsets, zero otherwise. For a negative edited point the signed law in section 1 becomes

    q=(1-lambda)P_g+lambda mu delta_empty+rho U_n.

Weights are nonnegative and sum to one, including lambda=1 and mu=0 endpoints. Empty-calibrate a normalized prescribed R to mu^2: exact CE saving is D_Ber(mu^2||R(empty)), and its conditional nonempty law stays intact. The same mixture for R0 gives a normalized complete floor and exact debt (1-lambda)D(P_g||R0)-kappa. The a=b=3 substitution is exactly section 2; a=1 reduces to the parity floor, rederived here rather than assuming a generic signed profile.

For a>=2 the calibrated vacuum agrees with q0=mu^2+rho(mu+t). Let v=1-mu^2, M=1-q0, A=(1-lambda)v and B0=rho(1-t), so M=A+B0<=v. The full nonempty sector is the retained source conditional law mixed with uniform nonempty sets. The log-sum bound gives

    CE(q,Rprime)-c0 <= L(q0)-L(mu^2)+L(M)-L(v)
                      +B0 log2(2^n-1)+phi(A,B0).

Since the original conditional reference CE is nonnegative and its weight shrinks from v to A, no positive source bill was dropped. Here L=-xlog2x, q0>=mu^2>=1/4 gives vacuum change <=rho, and the nonempty normalization change is <3rho/2. Bound their sum conservatively by 4rho. With t<=1/4, v<=4s, B0>=3rho/4 and M/B0<=(4/3)2^(b+r), phi<=rho(b+r+2). Thus CE(q,Rprime)<=c+rho(n+b+r+6). Adding the actual control bill proves CE_F<=c+rho(2n+b+3r+6)<=c+5rho(n+r)=c+10(C+E+J); n+r>=3 supplies the last step. For a=1 the parity mixture directly bounds CE_F<=c+3rho(n+r), which is stronger. These arguments allow zeros off source support because the uniform floor is positive.

Physical charges are I_g=2as,C=2ptb,E=2pta,J=2rpt. At K>=10,

    KI_F-CE_F>=S_K+(K-10)C-(K+10)E+(K-10)J,
    S_K=KI_g-c.

Since E/I_g=p2^-b<=1/2, supplied c<=C0 I_g pays at K=2C0+10: the actual unused source bank minus the erased-edge debit is >=[K-C0-(K+10)/2]I_g=0, and created/control terms are nonnegative. The point-defect structural reference has H_g<4I_g by its explicit vacuum and equal nonempty masses, yielding the source's 18I_F consequence. The arbitrary-terminal tensor retains c_h, D_h and physical influence additively; no terminal influence funds the edit. All clauses of A097's source statement hold. This independent review supplies no substantive repair.

## 4. Exact one-query transport of the incoming reference

Fix ANY actual parent P and normalized complete Q, and expose a fair physical coordinate j. Let child laws P_0,P_1 have marginal m_T=(P_0(T)+P_1(T))/2, and let r_T=sum_{u=0,1}Q(u,T). Use the actual physical-child posterior pi_b(T)=P_b(T)/(2m_T). On zero true fibers choose an explicit normalized posterior; never delete positive r mass there. Define unnormalized inherited child references Rtilde_b(T)=2r_T*pi_b(T), Z_b=sum_T Rtilde_b(T), and normalized R_b=Rtilde_b/Z_b. Support positivity gives Z_b>0, and Z_0+Z_1=2. The exact true/reference child likelihood factors are

    P_b(T)/R_b(T) = [m_T/r_T]*Z_b.

Writing L_j=sum_T m_T D(P(u|T)||Q(u|T)) for the incoming parent conditional divergence, direct disintegration gives

    D_parent - [D(P_0||R_0)+D(P_1||R_1)]/2
       = L_j - [log2 Z_0+log2 Z_1]/2 >=0.

The normalizer sign follows from Z_0+Z_1=2 and concavity of log. Let Delta_j=H(parent)-avg H(child). The complete cost ledger is

    CE_parent = avg CE_child + Delta_j
                + L_j - [log2 Z_0+log2 Z_1]/2.

This reconstructs a one-query reference-change accounting identity, not a new universal payment theorem. Both the incoming conditional likelihood and actual child normalizers matter. It does not replace child reference costs by fresh descendant floors. For a normalized independent terminal reference R_h tensor Q, choose product-compatible zero-fiber posteriors; every child reference is exactly R_h tensor R_b. Its whole c_h and D_h remain additive. The implementation checks the exact atom likelihoods and all zero-fiber reference mass, including terminal models with off-true-support mass.

## 5. Incoming paid-floor descendant obstruction, all dimensions

For every n>=2 take a=1,b=n-1,r=1, negative/control point zero. The source is a nonempty one-bit character padded with n-1 dummies, I_g=1 and source spectrum delta_A, A={active bit}. Supply the normalized reference R(A)=1/2,R(empty)=0, and R(T)=1/[2(2^n-2)] on every other subset. It is positive on the actual source support and has EXACT source cost c=1. Empty calibration leaves it unchanged. A097's proved floor has root CE<=12I_root; it does not start with a bad unbounded-cost source.

Put t=2^-n. Exposing the active physical bit gives a constant +1 child and a negative child h=-1+2*1_zero on n remaining bits. Their actual influences are 0 and 2nt. The root influence is 1+(n-1)t, and the queried coordinate has influence 1-t. The negative child's actual vacuum is mminus=(1-2t)^2.

The root source-frequency marginal and reference mass at A are q_A=1-2t+2t^2 and Rprime_A=(1-2t)/2+2t^2. Its reference marginal after deleting the queried membership bit at the remaining empty frequency is

    rv=t^2+Rprime_A*(1-t)^2/q_A.

Consequently Z_positive=rv/q_A, Z_negative=2-Z_positive, and the inherited normalized negative reference vacuum is

    Rnegative(empty)=(1-2t)^2*rv/(2q_A-rv).

As n grows these tend to Z_positive=1/2,Z_negative=3/2 and Rnegative(empty)=1/3, while true negative vacuum tends to one. The child is an ordinary signed point-defect function with H(h)<4I(h); the inherited MODEL does not track that law at low cost.

For an exact all-n certificate, write N=t^2 q_A+Rprime_A(1-t)^2. The inequality Rnegative(empty)<1/3 is equivalent to

    2q_A^2-[1+3(1-2t)^2]N
    =2t[3-18t+51t^2-79t^3+66t^4-24t^5]>0.

With u=4t in [0,1], the degree-five Bernstein coefficients of the bracket are exactly 3,21/10,243/160,145/128,557/640,11/16, all positive. This proves the sign for every n>=2, not only the compressed checks. For n>=3, true negative vacuum >=9/16 and log2(3)>1, so

    CE(P_negative,R_negative) >9/16,
    CE_negative/I_negative >9*2^n/(32n) -> infinity.

Thus the prospective uniformly influence-paid inheritance of the normalized incoming child references is false, even though source c=1, the root floor is paid at rate 12, and the actual child has H/I<4. This refutes only that hereditary reference-price extension, not A097 or FEI. No accepted source claims that extension.

## 6. One-use repair of this exposed fixture, with complete terminals

The ledger in section 4 says the fair average incoming descendant divergence never exceeds the original parent divergence. A constant leaf ratio problem therefore does not require a fresh unbounded source bank. Here the root cost bound is sharper than its 12I consequence:

    CE_root <=1+10(n+1)t <=(34/3)(1-t).

Indeed (n+1)2^-n decreases from 3/4 at n=2 and 1-t>=3/4. The right side prices the entire retained-core query ledger, not only one favorable remainder: avg incoming child CE+Delta_j+L_j-avg log2 Z equals CE_root. Assign this whole amount ONCE to the exposed active coordinate's actual influence. Any independent arbitrary terminal keeps its full c_h outside that account. There is no same-C child-reference claim and no new floor/reset.

This closes the single active exposure on the declared shock family with the SAME incoming model and source ownership. It uses a uniformly influential pivot. Further descendants cannot renew this booked budget; their inherited reference costs and later changes must be disintegrated from the already-carried bill. The universal unpaid line is such one-use payment when the selected non-flat coordinate is weak and both child cores remain nonconstant, with prescribed terminal CE retained. The all-n inherited-child obstruction rules out replacing that ledger by fresh influence-paid child models without an explicit reset cost. The next useful source is exactly that weak-pivot two-nonconstant-child collision, rather than another larger negative-cell root census.
