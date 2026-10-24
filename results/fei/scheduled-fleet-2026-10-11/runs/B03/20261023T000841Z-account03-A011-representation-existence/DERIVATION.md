# One original bank pays all subsequent source-prefix floor resets

All costs are ideal base-2 complete-reference costs. Subprobability divergence means D(P||Q)=CE(P,Q)-H(P), including -log(sum Q). This refines the existing arbitrary-core point-edit envelope. Full FEI remains open.

Let g be any nonconstant Boolean function on a>=1 bits. Let b>=1 independent padded data bits and r>=1 fresh point controls. Put n=a+b,p=2^-r,t=2^-n,w=2^-b. Translate every edited coordinate value to0 and write

    F=g-2g(0)1_(controls=0)1_(source=0,padding=0).

Supply an arbitrary source subprobability R with mass s in(0,1], positive on P_g support, finite c=CE(P_g,R)<=C0 I_g, C0>=0. Its source entropy and divergence are H=H(g),D=c-H>=0. The root reference is the original general envelope (Rpad+6pt U_n)/(1+6pt), lifted through the true conditional control kernel. Set K=4C0+15. The prior envelope gives CE_root<=2c+15B_root, B_root=2pt(n+r). The same argument with the auxiliary exact source law P_g gives the SCALAR entropy bound

    H(F)<=2H+15B_root.                                    (1)

This auxiliary inequality does not replace the prescribed root reference or assign a free source code to an actual terminal.

First query all b padding bits on the unique branch matching the edit. All off-path branches stop at the original g and source reference R (zero unused-coordinate frequencies). Then query k=1..a SOURCE coordinates on that same surviving branch, stopping each nonmatching branch at its actual unedited source restriction. The source coordinates can be queried in any adaptive order. The only active branch values are fixed by the edited point, so a variable order need not be fixed in advance. Source-only references for all these restrictions are generated from the ORIGINAL R by actual physical mass-preserving inheritance, defined next. At every active residual prescribe the same general envelope based on its inherited SOURCE reference; no descendant influence certificate is assumed. Intermediate floors and all signed reset charges are retained.

## Source-reference inheritance contracts complete divergence

For any source node with true spectral law P and source model Q of mass s, query a fair physical source bit. Let P0,P1 be actual child laws on remaining frequencies, m=(P0+P1)/2, and r_marg the corresponding marginal of Q (sum over queried Fourier membership). Pairwise Parseval gives m=P_parent(queried membership0)+P_parent(queried membership1). Set pi_j=Pj/(2m) on positive m fibers and choose any normalized posterior on zero m fibers, here the fair posterior. Set

    raw_j=2 r_marg pi_j, Z_j=sum raw_j, Qj=s raw_j/Z_j.

Then Z0+Z1=2s and each Qj has mass s, including its off-true-support mass. On true atoms Pj/Qj=(m/r_marg)(Z_j/s). Write L_cond for the parent's nonnegative conditional KL on queried Fourier membership. Direct likelihood disintegration yields

    D(P||Q)-[D(P0||Q0)+D(P1||Q1)]/2
       =L_cond-[log2(Z0/s)+log2(Z1/s)]/2 >=0.             (2)

The last inequality uses Z0+Z1=2s and log concavity; the denominator is s, not1. Zero true fibers retain reference mass. Both child laws are normalized, so both Z_j are positive. Original finite CE and positivity on actual support make every subsequent source child cost finite.

For the source stopping tree that queries only along the edited source path for k coordinates, let its leaf reaches be alpha_v. If its active source restriction is h and its inherited model is R_h, write H_h,D_h,c_h for its entropy, complete divergence and cost. Its reach is2^-k. Telescoping (2), and the one-bit nonnegative entropy decrement H(parent)-avg H(children)>=0, give

    sum_v alpha_v D_v <=D,
    2^-k D_h<=D,             2^-k H_h<=H.                (3)

Every off-path source terminal is included in the first inequality. The entropy decrement is membership conditional entropy plus JS of the child squared spectra, so its sign requires no FEI or independence of child supports.

## Price the full final ledger, not the next query in isolation

For k<a, the active source restriction has m=a-k>=1 ambient source bits, possibly with a constant Boolean value. The general envelope still applies, because its source-reference hypothesis is only finite cost, not nonconstancy or a new influence-paid certificate. Its complete divergence obeys

    D_edit <=2c_h+15B_h-H(F_h)
           <=2D_h+2H_h+15B_h,
    B_h=2p 2^(-m)(m+r).                                 (4)

Compared with the unedited source leaf h, the replacement adds at most D_h+2H_h+15B_h to terminal divergence. The entire physical tree has off-padding terminals of total reach1-w and the source tree with total reach w. Therefore its prescribed final model divergence bill is bounded by

    avg D_final <= (1-w)D + w sum_v alpha_v D_v
                     +w2^-k(D_h+2H_h+15B_h)
                 <= (1+w)D+2wH+15w2^-k B_h.             (5)

Let Q_v denote the ACTUAL prescribed reference at every physical node, and lambda_v=avg_j D(P_vj||Q_vj)-D(P_v||Q_v). This signed reset is the net of actual physical-reference release and prescribed conversion; its mass normalizers remain in D. The complete history ledger is exactly

    L_k=CE_root+sum_internal reach(v) lambda_v
       =sum_internal reach(v) DeltaH_v+sum_leaves reach(v) CE_v
       =H(F)+avg D_final.                               (6)

Equations(1),(5) give the quantitative price

    L_k <=2(1+w)c+15[B_root+w2^-k B_h]
        =2(1+w)c+30pt(2a+b+2r-k),       1<=k<a.         (7)

The inequality uses D>=0: (1+w)D+(2+2w)H<=2(1+w)(D+H). It never resets a source model for free or asks c_h<=C0 I(h). In particular any constant off-path terminal keeps its entire -log(model mass).

## The original rate and an explicit old-debit allowance

For nonconstant g, the a-cube minimum edge boundary gives I_g>=2a2^-a. Put q=b+r>=2,e=2^-q. When a>=2 and k>=1,

    [B_root+w2^-k B_h]/I_g
       <=e[2+(b+2r-k)/a]
       <=(q+1)/2^q <=3/4.                              (8)

Indeed b+2r-k<=2q-2, a>=2, and (q+1)/2^q decreases for integers q>=2. Also 2(1+w)<=3. Thus L_k<=3c+(45/4)I_g.

Keep the physical edge accounts: d is g's original pivotal degree at the edited source point, C=2pt(n-d), E=2ptd and J=2rpt. Since I_g>=2*2^-a*d, E<=e I_g<=I_g/4, while

    I(F)=I_g+C-E+J >=(3/4)I_g+C+J.

Consequently, at the SAME original K=4C0+15,

    K I(F)-L_k >= K(C+J)>0,             1<=k<a.          (9)

The source coefficient cancels: (3/4)(4C0+15)=3C0+45/4. Thus the same original remainder B_original=K I(F)-CE_root pays ALL signed padding/source resets in(6), retaining at least K(C+J) at each new source frontier. Every previously executed padding reset is already in that sum. An additional external old booking U is permitted at the source frontiers whenever0<=U<=K(C+J), and leaves at least K(C+J)-U. Larger bookings are not silently refunded. This is a conservative lower bound, not a claim that the actual remaining bank equals K(C+J).

If the EXTRA booking must be eligible at EVERY preceding frontier as well, use

    U_star=min{(C0+1)I_g, K(C+J)}.

The root envelope gives initial remainder at least(C0+15/2)I_g+4C0(C+J), by E<=I_g/4 and B_root=C+E+J. Every padding-prefix remainder is at least(3C0/2+1)I_g by the preceding A011 padding theorem. Both exceed(C0+1)I_g. Thus any0<=U<=U_star is eligible at the root, every padding prefix, and every source prefix, using ONE original account. This restriction prevents a late earned credit from being treated as an earlier free booking.

## Final source bit, including a=1

For k=a, every unedited source leaf is constant. The inherited source model on its zero-dimensional frequency cube is the single atom of mass s, so each such source divergence is exactly -log2 s. On the active edited leaf there are only r control bits. Its data cube is zero-dimensional, true data atom1, and the prescribed floor is the scalar

    M_final=(s+6p)/(1+6p)>=s.

Lift this scalar through the EXACT true control law of the constant point-edited source. The complete edited-leaf divergence is -log2 M_final<=-log2 s. No n>=1 envelope is invoked on a zero-dimensional source. Since D(P_g||R)>=-log2 s, equations(1),(6) give

    L_a<=H(F)+D <=2c+15B_root.                          (10)

This is at most the original envelope bound, not a free normalization. The source bank calculation directly gives, for ALL a>=1,

    K I(F)-L_a >= C0 I_g+K(C+J)>0.                      (11)

Indeed K(3/4)-2C0=C0+45/4 and15B_root<=45I_g/4 for a>=1, because B_root/I_g<=2^-q[1+q/a]<=(q+1)/2^q<=3/4. Thus the source entropy and complete source divergence are both retained, with the conservative final margin

    K I(F)-L_a >= C0 I_g+K(C+J).                         (12)

Thus a=1 is covered by(10),(12); it needs no intermediate-prefix argument.

## Side conditions and remaining universal line

Source g must be nonconstant only for the minimum-boundary conversion and original source bank. The residual h in(4) may be constant, and all source supports may be unequal. Finite c and positive source support imply s>0. All source inheritance denominators and final scalar masses are positive. At every nonzero-dimensional floor p in(0,1/2],t_h>0 make its true data marginal positive by completing the square; all log divisions are on positive true fibers. Zero amplitudes use zero contribution. Independent arbitrary terminal tensors keep their original full CE and KL additively and multiply every reference mass; none funds this bank.

The theorem permits all active source prefixes AFTER the original padding has been exposed. It does not certify a fresh descendant source bound at rate C0, create a new point edit, or pay arbitrary unrelated prescribed off-path references. Repeating the original representation construction on a NEW core still replaces C0 by4C0+15. That per-edit rate inflation, or a genuinely off-path canonical conversion under an additional already booked debit, remains the first unsupported universal continuation. Full FEI stays OPEN.
