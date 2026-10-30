# Preserving the actual booked source through post-reset data histories

Uniform independent Boolean inputs; entropy/KL in bits. This refines A038-BALANCED-CANONICAL-ADMISSION@2, not full FEI. Keep its actual root F_h: chi_a on x=0, h on x=b=1, and +1 otherwise, with h=h_m=chi_z d_m and d_m(y)=1-2*1[y=0], m>=3. M is the original completed canonical occupancy reference; A=D(P_F||M)=(15/16)K_occ. The nonempty source definition and forced-coordinate boundary are unchanged.

Reach any v2-eligible finite data/x frontier: b first, b0 untouched, a unqueried, x exposed on all b1 terminal paths. Preserve its actual booked full liability L0=A+[D0-4R0]_+, with D0=Hroot-Hfront and R0=Iroot-Ifront. Then perform the specified first canonical terminal reset at every b1 leaf. Its booked full terminal cost B0<=7/32 remains fixed. Preserve every earlier conservative extra booking in 0<=omega<=11/32. No earlier component of L0, B0 or omega may be retired.

Now allow ANY further finite adaptive fresh DATA-only stopping tree below those reset b1 terminals, with no second reset. Keep b0 untouched and a unqueried. Carry the CURRENT reset references by the actual coherent common kernels, fair on every source-zero row, retaining all reference-only mass and using reference-specific outcome normalizers. All physical branches and terminal laws remain.

Let S0=E(4I-H) at the reset frontier and S1 at the new frontier. Define the additional physical transaction debit U=[Dpost-4Rpost]_+=[S1-S0]_+, where Dpost=Hfront-Hnew and Rpost=Ifront-Inew are weighted over the whole physical frontier. THEOREM:

    L0<39/32,  S0>=2,  S1>=2,
    S1-(L0+B0+omega+U)>7/32.                    (T)

The complete transported reference bill after reset equals B0: all weighted post-reset erasure/outcome releases PLUS full inherited terminal KL sum to B0. Thus that bill is retained once; it is neither added a second time nor used as new spendable credit. The new U is additionally charged in (T). This proves the requested one-query continuation and, more strongly, every stated finite stopping continuation.

This is one post-reset stopping transaction. If a policy additionally books positive components at intermediate cuts, their excess over U is an additional explicit liability, not automatically included in (T). Old such excess is already in omega. No reset occurs INSIDE the post-data leg; section4 then pays one second canonical reset AFTER it. Queries of a or b0 and arbitrary-core supplier certificates remain excluded.

## 1. New lower entropy bound and a stopping potential

For k>=1 put epsilon=2^-k. The actual d_k spectrum has empty mass (1-2epsilon)^2 and all nonempty masses 4epsilon^2. Thus I(d_k)=2k epsilon and nonempty entropy is 8(k-1)epsilon(1-epsilon). We prove

    H(d_k)>=8(k-1)epsilon,
    4I(d_k)-H(d_k)<=8epsilon.                   (1)

k=1 and k=2 are exact: H=0 and H=2 respectively. For k>=3 set p=(1-2epsilon)^2. Since -ln p>=1-p, the empty entropy is at least p(1-p)/ln2. The positive atanh series gives ln2<=2/3+1/36=25/36<3/4, so this is strictly greater than (16/3)epsilon(1-epsilon)(1-2epsilon)^2. Meanwhile

    (2/3)(1-epsilon)(1-2epsilon)^2 >=21/64>1/4,
    (k-1)epsilon<=1/4                         (k>=3).

The first inequality uses epsilon<=1/8; the second decreases from k=3. Consequently the empty entropy exceeds 8(k-1)epsilon^2, exactly filling the deficit in the nonempty entropy. This proves (1), without assuming any unproved entropy-influence statement.

Give an active k-bit point-defect state potential V_k=8*2^-k for k>=1, and a constant state potential0. A query of an active point bit at k>=2 produces d_(k-1) and a constant, so the mean child potential is V_k. At k=1 both children are constants, so the mean drops to0. Dummy queries preserve the potential. By (1), each terminal actual surplus is at most its potential. Therefore every finite adaptive data stopping tree starting at d_k has mean terminal surplus <=V_k. This is a finite supermartingale induction, not a product of conditional bounds.

For a surviving independent character chi_z times a point-defect state use potential4+V_k; for chi_z times a constant use4. If z is queried, the character's4 disappears and the remaining state is a signed point defect. Point-bit queries have the preceding mean-potential behavior. Constants and signed characters have the obvious exact bounds; signs do not change spectrum. Thus EVERY adaptive restriction tree of h_m has

    E(4I(g)-H(g)) <=4+8*2^-m.                  (2)

Notice the k=1 active state: chi_z*d_1 is a TWO-coordinate character with surplus8, not a single-coordinate character with surplus4. The potential 4+V_1=8 includes this boundary explicitly.

## 2. The full old booking, not just A, is uniformly bounded

At any v2 frontier with all b1 paths exposing x, its exact surplus is

    S0=2+(1/4)E_core(4I(g)-H(g)).

The first2 comes from untouched b0 (weight1/2, surplus2) and b1x0 (weight1/4, character surplus4). Conditional on b1x1, simulate the actual policy with x fixed to1: its remaining data restrictions form an ordinary adaptive h_m tree on uniform data. Fairness of fresh x makes this conditional law uniform; no independence of the adaptive data decisions is assumed. By (2),

    S0<=3+2epsilon,  epsilon=2^-m.

Exact root sectors give Sroot=3+2m epsilon-H(h_m)/4. Since (1) implies H(h_m)>=8(m-1)epsilon, the upper bound on S0-Sroot is nonnegative. Hence

    L0=A+[S0-Sroot]_+
       <= A+H(h_m)/4-2(m-1)epsilon
       <= G_m-1-2(m-1)epsilon,                (3)

where v2 proves A<=G_m-1-H(h_m)/4 and G_m=2h2(1/4)+m h2(2^(-m-1)). Unlike v2's A<39/32, (3) bounds the ENTIRE already booked L0. The same constant has a stronger scope; it is not a changed numerical estimate of A.

For completeness, h2(1/4)<13/16 follows from3^12>2^19. Since ln2>2/3, binary entropy gives m h2(2^(-m-1))<e_m=m(m+5/2)/2^(m+1). Its successive comparison has positive difference m^2+m/2-7/2 for m>=3, so e_m decreases. At m=3, (3)<85/32-1-1/2=37/32. At m=4, (3)<39/16-1-3/8=17/16. At m>=5, (3)<283/128-1=155/128<39/32. Thus L0<39/32 for EVERY eligible prior frontier, with every actual previous positive whole liability retained unchanged.

The finer upper bound in (3) is attained as an upper-surplus envelope before the marginal-entropy estimate: keep z and query active point bits until k=2 (or k=1). Terminal point-defect surplus equals V_k there, so S0=3+2epsilon. This is why the new stopping potential addresses the actual booked-debt bottleneck rather than merely improving the source KL estimate.

## 3. Current reference transport and incremental physical debit

Every actual restricted core has H<=4I, by the explicit point-defect upper entropy bound and tensoring with a fresh character from v2. After the new data-only stopping tree, b0 and the b1x0 character have the same contributions as before. The b1x1 cores still have nonnegative surplus. Therefore S0,S1>=2, regardless of divergent choices among reset branches.

At a current reference node q and actual spectrum p, erasure followed by the common coherent outcome kernel gives

    KL(p||q)=erasure_KL+outcome_KL+mean child_KL.

This follows from two finite KL chain rules. The actual outcome law is fair; the reference outcome law need not be fair. Reference-only rows remain in the erasure marginals and normalization, with fair common fallback on zero-source rows. Iteration from ALL reset terminals weighted by their ORIGINAL physical probabilities proves that the full new reference bill equals the ORIGINAL B0. This is a decomposition of a kept bill, not an additional payment or refund.

For the newly queried physical leg, Dpost-4Rpost=S1-S0. Thus the exact separate-account identity is

    S1-[L0+B0+omega+[S1-S0]_+]
      =min(S0,S1)-L0-B0-omega.

Using S0,S1>=2, (3), B0<=7/32 and omega<=11/32 yields a strict lower bound 2-39/32-7/32-11/32=7/32. This proves (T), preserving old L0 even if a net re-evaluation at the new frontier would lower it. No shrinking-booking refund is used.

## 4. A second prescribed canonical reset is also paid

The three cases in (3) actually imply L0<155/128 uniformly: 37/32 and17/16 are both below155/128, and the m>=5 case is already strictly below it. After the post-data tree, prescribe a SECOND canonical reset on all b1 terminals. They remain the same restricted family, and their total b1x1 physical weight remains1/4. Thus its full new terminal bill B1<=7/32, and the positive actual second conversion is <=B1. Keep the ENTIRE first B0, L0, omega and U. The same identity gives

    S1-(L0+B0+omega+U+B1)
      >2-155/128-7/32-11/32-7/32=1/128.        (4)

This is a full additional conservative booking, not reuse of a first-reset refund. The reference from before the second reset retains every outcome/erasure/terminal bill in B0. The second reset separately adds its complete new terminal KL B1.

One explicit nonzero-new-bill witness uses m=4, first b then x with no core query, first canonical reset, one active point-bit query, then the second canonical reset. For s_k=4I(d_k)-H(d_k) and T_k=k h2(2^(1-k))-H(d_k), the actual values are S0=3+s_4/4, S1=3+s_3/8, L0=A (the initial b/x pair is rate4-neutral), B0=T_4/4 and B1=T_3/8. Both full new reference bills are strictly positive. These are actual Boolean spectra and actual completed canonical laws. This witness does not assert that the signed NEW-minus-inherited conversion itself is positive; the theorem pays its positive part via the larger full new bill.

## 5. First unsupported line

The stated post-reset data-only transaction and following second canonical reset are proved. The next unpaid transaction is an actual query AFTER that second reset with L0,B0,omega,U,B1 all retained, or an actual a exposure. Arbitrary Boolean cores lack the stopping potential and affordable original source admission; supplying those remains the universal gap. Repeated intermediate positive bookings cannot be collapsed to a net U without recording their excess. Full FEI remains OPEN, and all new proof claims await independent review.
