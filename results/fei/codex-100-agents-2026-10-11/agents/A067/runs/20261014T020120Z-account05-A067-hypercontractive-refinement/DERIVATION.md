# Two fixed subcube controllers: one complete output reference

All entropy is in bits, Fourier coefficients use the uniform cube, and I is physical total influence. X and Z are disjoint blocks. Let g(X) be a Boolean sign, A(X),B(X) indicators, and p(Z),q(Z) indicators of two fixed subcubes. Their fixed coordinate sets P,Q and assignments may be unequal, nested, disjoint, compatible or incompatible. Contract coordinates outside P union Q. Let E be either (Ap) XOR (Bq), or (Ap) OR (Bq), and F=g(-1)^E. Assume for every x that a_x=P_Z(E(x,Z))<=1/4. This is a final-mask condition; no cardinality bound or separate payment of the two events is used.

Write I_X,I_Z for FINAL F, rho=P(E), alpha=P_spectral(S_Z nonempty), and Q_access=H(F)-E_Z H(F_Z). Then

    Q_access <= K I_Z + 2 I_X,
    K=4+log2(5)+2/ln(2)<19/2.

For compatible assignments K can be replaced by 6+2/ln(2)<9. The theorem holds in every finite dimension. The same reference below is used for every core Fourier row. The actual conditional core entropy is retained. If all actual cores F_z satisfy U(F_z)<=b I(F_z), where U is the accepted A067 local Boolean granularity defect, then

    H(F)<=K I_Z+(4+2b)I_X<=max(K,4+2b)I(F).

In particular, if all actual cores have Fourier degree at most two, then U<=I and H(F)<=K I(F); this includes every choice of g,A,B on at most two core coordinates. The control widths remain arbitrary. This is a conditional leaf certificate and an unconditional access theorem, not universal FEI.

## 1. Frequency cells and their complete reference

If the contracted control block is empty, then Q_access=I_Z=0 and the theorem is immediate; the reference below is needed only for a nonempty contracted block.

Split Z into R=P intersect Q, U=P minus Q, V=Q minus P. Reflect coordinates so the first assignment is zero. In the compatible case the second assignment is zero as well. Partition all nonempty control Fourier subsets S by whether S_U and S_V are empty: 00,10,01,11, removing empty cells and excluding S=empty from 00. There are M<=4 cells.

In the incompatible case let D subset R be the nonempty set of conflicting assignments. Split 00 further according to parity of |S intersect D|. Keep 10,01,11 as before. There are M<=5 cells. The 11 cell is included even though it has zero Fourier mass for this family. Thus the reference covers EVERY nonempty subset of the contracted control block, not just a selected support.

For each cell C put R_tail(S)=1/(M |C|). This is a normalized probability on every nonempty control subset, independent of x, the core Fourier row, g, A,B, and all row coefficients. Include the empty atom using the single complete reference R_full(empty)=1-alpha and R_full(S)=alpha R_tail(S). Endpoint alpha=0 is interpreted by continuity. This reference is output-specific only through alpha; the same reference is used for all core rows.

Every occupied cell has constant squared Fourier coefficient in each fixed core Fourier row. Indeed for XOR,

    F=g(1-2Ap-2Bq+4ABpq),

and for OR the last coefficient is 2 instead of 4. Each row is c0+c1p+c2q+c12pq, with real coefficients. A subcube indicator has coefficient density times the common assignment character on every subset of its fixed set, and zero elsewhere. For compatible assignments all phases agree. In 00 each of p,q,pq is present; in 10 only p,pq; in 01 only q,pq; in 11 only pq. In the incompatible case pq=0; in 00 the relative phase of p and q is precisely the parity on D; in 10/01 only one term remains; 11 vanishes. Therefore conditional on a cell of positive row mass, S is exactly uniform on that cell. The empty atom, which may include c0, is kept separate.

For every cell C,

    log2 |C| <= 2 E_{S uniform C}|S|.                 (1)

For the compatible product cells, an unrestricted coordinate block has mean degree half its size and entropy equal to its size. Conditioning a nonempty private block increases its mean degree and decreases entropy. In 00, removal of the empty subset has the same effect. For an incompatible 00 parity class before empty removal, the uniform affine parity subspace has all free coordinate marginals 1/2. If |D|=1 one coordinate is fixed to zero or one; its dimension contributes zero entropy, while a fixed one contributes positive degree. Consequently twice the mean degree is at least its dimension, which equals log-cardinality. Removing empty from the even class raises the mean and lowers log-cardinality. This proves (1), including zero-dimensional and singleton cells.

Gibbs' inequality with the SAME R_full gives

    B_Z:=H(S_Z | S_X) <= h2(alpha)+alpha log2 M+2 I_Z. (2)

To see the binary term correctly, let alpha_T be the row tail probability. Cross entropy for R_full averages to h2(alpha), since E alpha_T=alpha. On each occupied cell the log-cardinality cost is bounded by twice its conditional mean degree by (1). Sum all row weights once. No row-specific renormalization or choice of reference occurs.

## 2. Boolean final-core reserve

Alpha=E_x 4a_x(1-a_x)<=4rho. For a core edge (x,x'), the probability p_edge that E differs is at most a_x+a_x'<=1/2. If g differs, F differs with probability 1-p_edge; otherwise it differs with probability p_edge. Hence I_X(F)>=I_X((-1)^E), while I_Z(F)=I_Z((-1)^E) exactly. This comparison is Boolean-specific and fails for normalized real seeds. It prices the COMBINED FINAL mask, so overlaps and cancellations are owned once.

Cube edge isoperimetry gives for a set of density a:

    I((-1)^set)>=2a log2(1/a).

A self-contained induction: split on one coordinate, with child densities a0,a1. Child influences average; the split coordinate contributes at least |a0-a1|. For a=(a0+a1)/2, t=a0/(a0+a1), the deficit between 2a log2(1/a) and average child lower bounds is 2a[1-h2(t)]. This is at most 2a|2t-1|=|a0-a1| because h2(t)>=2 min(t,1-t), by concavity between 0,1/2,1. This proves the induction, including empty sets.

Applied to each control fiber, the cap a_x<=1/4 yields I_Z>=4rho>=alpha. Applied to the whole final mask and the ownership comparison it yields

    I_X+I_Z>=2rho log2(1/rho).

For alpha<=4rho<=1, h2(alpha)<=alpha log2(e/alpha)<=4rho log2(e/(4rho))<=4rho log2(1/rho)<=2(I_X+I_Z). The middle comparison uses monotonicity of t log2(e/t) on [0,1], and log2(e)<2. All terms vanish when rho=0.

Insert these estimates into (2):

    B_Z <= (4+log2 M)I_Z+2I_X.                    (3)

## 3. The channel and the retained terminals

The exact physical restriction identity, used in accepted A067 bounded-fiber theorem v1, is Q_access=B_Z+J_Z. Tensorizing the two-point logarithmic Sobolev inequality rowwise gives J_Z<=2 I_Z/ln(2), valid even for real row amplitudes. This is the standard real-valued channel fragment, not the new Boolean improvement. The new contribution is (3), its complete flat-cell reference, and its Boolean ownership reserve. Standard ambient-label coding instead charges alpha |Z|, yielding a dimension factor for large subcube fibers; that precise loss is removed here.

Adding (3) and the channel price proves the theorem. ln(2)>2/3 and log2(5)<5/2 prove K<19/2; for compatible assignments K<9. All actual terminal cores remain in E_Z H(F_Z). The accepted local Boolean coefficient granularity theorem gives H(F_Z)<=2I(F_Z)+2U(F_Z). Under U<=bI on EVERY actual core, E_Z H(F_Z)<=(2+2b)I_X, proving the stated corollary. No hypothesis is placed solely on the original seed. There are at most four distinct core functions, selected by (p(z),q(z)); some may be absent.

## 4. Review and universal limitation

A088 independently accepted A067 bounded-fiber v1; its ownership/channel and the earlier granularity theorem are the exact dependencies. A069's simultaneous-mask refund and A070's signed physical-conversion audit are useful comparisons, not proof dependencies. In particular, this theorem requires g independent of Z. The cancellation witness g=q*y from A070 is outside that hypothesis and its negative signed conversion is not repaired by this result.

First unsupported universal line: admitting arbitrary actual core terminals with U<=bI for a universal b, or replacing this leaf certificate by another complete paid reference, remains unproved. The two-controller access bound itself has no unsupported line. Extension to an arbitrary number of controllers needs an explicit complete cell partition whose label and cardinality costs are paid by FINAL physical influence; a growing cell count cannot simply be renamed a constant.
