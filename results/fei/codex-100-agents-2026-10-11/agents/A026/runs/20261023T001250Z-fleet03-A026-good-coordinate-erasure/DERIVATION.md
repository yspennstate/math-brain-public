# Dummy-data reset from the same source account

Full FEI remains open. All costs are in bits; influences are uniform physical flip probabilities. This extends A097's source-reference theorem, not its already known read-once entropy class.

## 0. Exact decrement and complete-reference identity

For a Boolean f write P_f(S)=fhat(S)^2, M_i=marginal_i P_f, and B_i(f)=H(P_f)-H(M_i)=H(S_i|S_without_i). The exact restriction identity in bits is

    H(f)-[H(f_i+)+H(f_i-)]/2
       =B_i(f)+JS(P_f_i+,P_f_i-).

Indeed M_i=(P_f_i++P_f_i-)/2, and the Jensen-Shannon term is H(M_i)-[H(P_f_i+)+H(P_f_i-)]/2. Thus B is not the entire entropy decrement. If Q is a complete normalized reference and q=marginal_i Q, the exact no-reset identity is

    B_i(f)+[CE(P_f_i+,q)+CE(P_f_i-,q)]/2
      =CE(P_f,Q)-[KL(P_f||Q)-KL(M_i||q)].

The bracket is nonnegative by the conditional KL chain rule. This proves that arbitrary no-reset off-branch continuations cannot increase the complete-reference ledger. It does not remove the JS term from the true entropy decrement or supply a universal small reference. Coordinate selection must still exhibit some actual relevant coordinate for arbitrary Boolean f; no all-coordinate assertion follows from the present point-source history theorem.

## 1. Original source and complete floor

Let a>=1,b>=1,r>=1, n=a+b, s=2^-a, t=2^-n, e=2^(1-n-r), mu=1-2s. Write g=1-2A_a and F=g+2A_(n+r), where A is the zero-point indicator. The b data coordinates absent from g are the dummy data. Let R be a normalized source reference positive on P_g, with R(empty)=mu^2 and finite c=CE(P_g,R). Off-source reference mass is retained. Define h=e/s<=1/2 and

    R_e(T)=(1-h)R(T)+h mu 1_{T=empty}+2et.
    M_e(T)=ghat(T)^2+2e ghat(T)+2et.
    Q(T,U)=R_e(T) P_F(T,U)/M_e(T).

M_e(T)>0. This is the SAME complete canonical floor used by A097; no reference is chosen after the spectral draw. Its known envelope is W=c+10e(n+r). The original source admission c_raw<=C0 I(g) gives quota K I(F), K=2C0+10, with

    K I(F)-W >=5 I(g)=5a 2^(b+r)e,               (1)

for an original root with r>=2. Local dummy substitution below holds already for r>=1, since b>=1 implies h=2^(1-b-r)<=1/2. Empty calibration only reduces c_raw. A097's active/control theorem already keeps all old erasures and full complementary references: each active step with a>=2 releases at least e from W; each eligible control step costs at most8e beyond W; the a=1 final active boundary uses its explicit point rule. Those clauses are imported at their exact scopes, not widened by assumption.

## 2. Query one dummy DATA coordinate

The on child is F_on=1-2A_a+2A_(n+r-1), with b->b-1, t->2t, e->2e; r and a stay fixed. The off child is g with r dummy controls. Both functions are nonconstant. For a residual data set S let R_0=R(S) and R_1=R(S+j). Since g does not use j, its two parent coefficients are (ghat(S)+e,e) when U is empty, and (e,e) otherwise. These are EXACTLY the control-query coefficient pairs as a Boolean function. Therefore A097's erasure calculation applies unchanged:

    B_j(F) <12e.                                (2)

References do distinguish dummy data from a control, so the off-cost proof must change. Keep the complete OLD reference marginalized over j in the off child. For a nonempty occupied source frequency S, ghat(S)=-2s. Its actual off-reference atom is

    Q_off(S,empty)
      =R_e(S) (2s-e)^2/[4s^2-4se+2et]
         +R_e(S+j) e^2/(2et).                  (3)

Both summands are retained; the second is nonnegative reference-only capacity. Set k=(2s-e)^2/[4s^2-4se+2et]. Since R_e(S)>=(1-h)R(S), equation (3) implies Q_off(S,empty)>=(1-h)k R(S). Also

    k^-1=1+e(2t-e)/(2s-e)^2 <=1+h,              (4)

because e<=s/2, t<=s, and (2s-e)^2>=9s^2/4. In fact the increment is at most8h/9. All denominators are strictly positive. At the source vacuum, R_e(empty)=M_e(empty), so Q_off(empty,empty)>=(mu+e)^2>=mu^2=R(empty). If mu=0 this zero-probability atom contributes no logarithm.

Let beta=1/ln2<3/2. On 0<=h<=1/2, -log2(1-h)<=2h by the convex chord, while log2(1+h)<=beta h. The total occupied nonempty source mass is v=4s(1-s)<=4s. Thus the SIGNED full off-reference cost satisfies

    c_off-c <=v[-log2(1-h)+log2(k^-1)]
               <=(8+4 beta)e <14e.             (5)

No absolute-TV surrogate, reference deletion, or new off-reference is used.

## 3. Prescribed on-floor uses the ACTUAL source marginal

Marginalize the SAME current source law: R_m(S)=R(S)+R(S+j). It is normalized and has positive mass on every occupied source atom. Since R_m(S)>=R(S), CE(P_g,R_m)<=c. Empty-calibrate R_m to mu^2, retaining and rescaling its complete conditional nonempty law; this decreases CE by the corresponding Bernoulli KL. Call the resulting law R_new and its cost c_new<=c. This is a fixed prescription, not an unspecified favorable reference.

Reset the on child to the canonical floor Q_on(a,b-1,r,R_new). Its complete envelope is

    W_on=c_new+20e(n+r-1)<=c+20e(n+r-1).

Combining (2),(5) gives the local full-reference substitution

    B_j(F)+(c_off+W_on)/2
       <c+10e(n+r)+(12+7-10)e = W+9e.          (6)

All source entropy, structural sector entropy, JS, normalizers and reference-only atoms are inside these complete cross-entropies. None may also be claimed as an additional free bank. The unchanged opposite terminal cost remains whole.

## 4. Every eligible mixed history, one original quota

Allow arbitrary adaptive choices of active, control and dummy-data coordinates on the still-edited branch. On each on step, reach halves and e doubles, so reach*e=e_root. Off branches retain their whole incoming marginalized references and may undergo any no-reset continuation. Apply the imported active rule while a>=2, the control rule while r>=2, and (6) at dummy steps while b>=1,r>=1. At the final active a=1 query the imported explicit point-spectrum rule ends the edited branch; its whole local closure costs at most the current W, and is checked separately at every eligible prefix. Arbitrary earlier stopping cuts retain the current full canonical floor. A control step may reach r=1, after which active steps, dummy steps and stopping remain admitted. The last control query from r=1 to r=0 is excluded.

There are at most r_root-1 control steps and b_root dummy steps. Therefore the COMPLETE erasure-plus-terminal-reference ledger is at most

    W_root+[8(r_root-1)+9b_root]e_root.          (7)

For every a>=1,b>=0,r>=2,

    5a 2^(b+r)-8(r-1)-9b >=12.                 (8)

At a=1,b=0,r=2 equality holds. Increasing b increases the left side by5a2^(b+r)-9>=11, increasing r increases it by5a2^(b+r)-8>=12, and increasing a increases it. Finite induction proves (8). Equations (1),(7),(8) yield

    complete ledger <=K I(F_root)-12e_root,     (9)

at the SAME original rate K=2C0+10 (18 for the structural source R=P_g). All previous mixed-history debits, both full terminals and the current source reference remain present. No child receives a fresh source quota. Any independent untouched Boolean terminal with a supplied finite reference adds its full cross-entropy to both sides and contributes none of the edit reserve.

## 5. Scope and first unpaid line

The new mechanism prices the precise previously unpaid DUMMY-DATA source-marginal change. Arbitrary source references on this point-sign source are admitted, including nonflat laws with off-source mass. This does not create an O(I) reference for arbitrary Boolean functions, replace a non-point signed source by a point source, pay a further reset inside a retained off branch, or justify the last control query from r=1 to r=0. These are separate unpaid hypotheses. In particular this is not an all-coordinate B_i<=K I_i theorem, nor a universal good-coordinate theorem. It advances C019/C024 at a supplied-reference boundary, with zero improvement to a universal FEI constant.

## 6. Boundary and review audit

The r=1,a=1,b=1 dummy-on child has truth table (1,1,-1,1) and squared Fourier spectrum (1/4,1/4,1/4,1/4). Its prescribed complete floor is flat for every supplied calibrated source law. Nonflatness was an extraneous checker assertion, not a hypothesis of (3)-(9); the boundary is retained. Both Boolean children remain nonconstant. The original r>=2 on-floors remain checked as nonflat. This stage provides an author derivation and two finite computational representations, not a second human analytic review. A097's active/control source theorems are imported at their exact versions; their universal promotion is not assumed.
