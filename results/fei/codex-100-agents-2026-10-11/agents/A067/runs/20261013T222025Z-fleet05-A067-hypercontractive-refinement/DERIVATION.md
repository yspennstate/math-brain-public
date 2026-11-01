# A single owned reserve for bounded-fiber edits

All cubes are finite and uniform, outputs are actual Boolean signs, and entropies are bits. Write x for m active core coordinates and z for r dummy controls of a seed g(x). Let E be an arbitrary physical edit set and

    F(x,z)=g(x)(-1)^{1_E(x,z)}.

This is the final edit mask: two sequential flips use E=D1 symmetric-difference D2; union-once editing uses E=D1 union D2. No sum of incoherent difference spectra is substituted for F.

## 1. Exact scope and theorem

Let A={x:E_x is nonempty}, epsilon=P_x(A), rho=P(E), and assume every fiber E_x has at most k control assignments, with

    1<=k<2^r,  k*2^{-r}<=1/4.

Put I_Z=sum of the control influences of F, I_X=sum of its core influences, and let Q=H(F)-E_z H(F_z). Then, with c=2/ln2,

    Q <= [4r/(r-log2 k)+c] I_Z + 2 I_X.                 (T)

The theorem includes empty E, where Q=I_Z=0 and no logarithm of rho/epsilon is used. For k=1,r>=2 the coefficient is 4+c. For k=2,r>=3 it is at most 6+c. All quantities on the right belong to the final edited Boolean F, not the seed or the sum of separate edit budgets.

Two graph-controlled events D_j={(x,z):x in A_j,z=a_j(x)} sharing the full core and control block satisfy the k=2 hypothesis after either sequential-XOR or union-once editing. Their domains and control maps may overlap arbitrarily; their projections need not be orthogonal. This does not cover arbitrary large subcube fibers for free.

## 2. Elementary entropy tensorization, with constants

For a nonnegative density w on a product space define Ent(w)=E[w log2(w/Ew)]. The log-sum inequality proves convexity of Ent. The exact two-block identity is

    Ent_{X,Y}(w)=E_X Ent_Y(w)+Ent_X(E_Y w).

Convexity bounds the last term by E_Y Ent_X(w). Induction gives Ent(w)<=sum_i E Ent_i(w), without assuming normalized w or nonzero means.

Apply it first to w=1_A on a uniform cube. On a crossing edge the two entries are 0,1 and Ent_i is 1/2; on a noncrossing edge it vanishes. Hence

    Inf(1-2*1_A)>=2 epsilon log2(1/epsilon).             (ISO)

This holds for every epsilon in [0,1], with endpoints interpreted continuously; it is not restricted to small sets.

Apply tensorization to w=a(z)^2 for a real control field. On one bit write a=a0+z_i a1 and q=a0^2+a1^2. Its entropy is q*g(2a0a1/q)/ln2, where

    g(u)=((1+u)ln(1+u)+(1-u)ln(1-u))/2
        <=1-sqrt(1-u^2).

For u>=0, atanh(u)<=u/sqrt(1-u^2) follows by comparing derivatives, then integration proves the displayed bound; evenness and continuity cover the whole domain. Therefore Ent_i(a^2)<=2 min(a0^2,a1^2)/ln2<=c a1^2. Tensorization gives Ent_z(a^2)<=c sum_i E(D_i a)^2.

For each core Fourier label T take a_T(z)=hat(F_z)(T). Its row mass is q_T=E_z a_T(z)^2. The actual physical restriction identity is

    Q=B_Z+J_Z,
    B_Z=H(S_Z|S_X),
    J_Z=sum_T Ent_z(a_T^2)>=0.

The row formula follows by grouping full Fourier coefficients by T and averaging actual signed child squares. Parseval in x and z yields sum_{T,i} E(D_i a_T)^2=I_Z(F), using Booleanity for the physical influence interpretation. Thus J_Z<=c I_Z. This channel bound is a general real-field algebraic fragment; the new Boolean payment is the reserve ownership below.

## 3. The padding entropy flag and its exact mass

For a fixed core x, let a_x=|E_x|/2^r. Then the conditional control mean is g(x)(1-2a_x). Partial Parseval gives the exact nonempty-control spectral mass

    alpha=P(S_Z nonempty)=E_x[4a_x(1-a_x)]<=4rho<=1.

Conditioning on the flag S_Z nonempty, whose nonempty alphabet has at most 2^r-1 labels, gives

    B_Z<=h2(alpha)+alpha*r.

The scalar bound h2(alpha)<=alpha log2(e/alpha), together with monotonicity of u log2(e/u) on [0,1] and alpha<=4rho<=1, implies

    B_Z<=4rho[r+log2(e/(4rho))].                       (1)

Every nonempty fiber has at least one assignment, so rho>=epsilon*2^{-r}. Therefore, when rho>0,

    B_Z<=4rho[2r+log2(1/epsilon)-2+log2 e]
        <=8r rho+4rho log2(1/epsilon).                (2)

The last discarded constant is negative: log2 e<2 follows, for example, from e<3<4. Empty fibers and epsilon=1 are allowed. No entropy of a restricted seed or of an arbitrary core is discarded here: Q is only the access drop and every actual core leaf remains on the left ledger.

## 4. A queried-control budget and one core ownership inequality

Apply (ISO) to each Boolean control fiber 1-2*1_{E_x}. Its influence is exactly the control influence of F at x (multiplication by g(x) does not change pivots). Since a_x<=k2^{-r},

    I_Z>=2 E_x[a_x log2(1/a_x)]
        >=2rho(r-log2 k).                             (3)

For a core edge (x,x'), put p=P_z(1_E(x,z)!=1_E(x',z)). The fiber cap gives p<=a_x+a_x'<=1/2. If the seed edge is nonpivotal, the corresponding F edge is pivotal with probability p. If it is pivotal, F is pivotal with probability 1-p, which is at least p. Thus the pointwise FINAL-edge comparison is

    Inf_X(F)>=Inf_X(1-2*1_E).                         (4)

This is the cancellation-aware ownership step. It is applied once to the combined mask E, never separately to D1 and D2.

For each control assignment z, the core slice E^z is a subset of A. Write epsilon_z=P_x(E^z)<=epsilon and E_z epsilon_z=rho. Applying (ISO) and then using epsilon_z<=epsilon yields

    I_X>=E_z Inf(1-2*1_{E^z})
        >=2 E_z[epsilon_z log2(1/epsilon_z)]
        >=2rho log2(1/epsilon).                       (5)

Consequently 4rho log2(1/epsilon)<=2I_X. Equations (2),(3),(5) give B_Z<=4r/(r-log2 k) I_Z+2I_X. Adding J_Z<=cI_Z proves (T).

The sparse-fiber cap is substantive. Without it the edge comparison (4) fails: on m=r=1 let g(x)=(-1)^x and E={(0,0),(1,1)}. Each fiber has probability 1/2 and F depends only on z; I_X(F)=0 while I_X(1-2*1_E)=1. This refutes only extending the ownership inequality beyond its hypothesis, not (T), FEI, or a different compensated ledger.

Booleanity is also substantive even with the cap. Take the normalized real psi=(1/4)sum_{i=1}^{16} x_i, whose core spectral Dirichlet energy is 1 and entropy is 4. Edit only at the zero middle Hamming layer (weight 8) and z=00 on r=2 controls. Each fiber has at most one assignment and density <=1/4, but the real function is unchanged because every edited value is zero. The mask's core influence is (1/4)*2*16*binom(16,8)/2^16=6435/4096>1. Thus (4) fails if physical Boolean influence is replaced by real Dirichlet energy. No real function is submitted as a FEI counterexample. This certifies that the new final-core reserve is not merely a restatement of the general real-field channel inequality.

## 5. Full and early U stopping, with all terminal entropy retained

Reveal all r controls in any adaptive fair order and stop before touching the core. The leaf partition is the actual family F_z. The exact influence telescope gives spent influence I_Z and E I(leaf)=I_X; the entropy telescope gives total drop Q. The reserve in (T) is 2I_X once over this entire tree; it is not renewed at the first separation of the two edits.

Use the reviewed A067 local-granularity certificate H(h)<=2I(h)+2U(h)-(2-log2 e)Var(h). If every F_z satisfies U(F_z)<=bI(F_z), b>=0, then

    H(F)<=K I_Z+(4+2b) I_X
         <=max(K,4+2b) I(F),
    K=4r/(r-log2 k)+2/ln2.                            (6)

For k=1,r>=2,b=1, this is K=4+2/ln2<7; for k=2,r>=3,b=1 it is K<=6+2/ln2<9. Core admission remains a real hypothesis.

For any earlier padding-only stopping tree, extend its leaves by revealing all remaining controls. Physical entropy decrements are nonnegative, so Q_partial<=Q_full. Meanwhile I_Z(root)=I_queried+E I_Z(early leaf) and I_X(root)=E I_X(early leaf). Hence

    Q_partial<=K I_queried+K E I_Z(leaf)+2 E I_X(leaf).

If the early leaves satisfy U<=bI, their complete entropy ledger is therefore

    H(F)<=K I_queried+(K+2+2b) E I(leaf)
         <=(K+2+2b) I(F).                            (7)

Do not substitute I_queried for root I_Z in (T) without this remaining-control term. Local descendants need not satisfy the original sparse-fiber cap; (7) follows from the full root ledger, not by applying (T) anew at every node.

## 6. Hypercontractive loss and the exact remaining bridge

The channel price cI_Z is already the tensorized two-point/log-Sobolev estimate. It incurs no logarithm in degree or ambient core dimension. The extra loss in this route is the conditional label bound H(S_Z|flag,S_X)<=r, compared with the physical control budget 2rho(r-log2 k). The resulting factor is precisely r/(r-log2 k), not a hidden log m. For one or two assignments per fiber it stays bounded; for large dense or poorly encoded fibers it can grow. The Boolean improvement is that the logarithmic active-core rarity 4rho log2(1/epsilon) is paid by a FINAL-core influence reserve using (4),(5), after combining signed edits and cancellations.

The alphabet loss is visible on an exact all-r control: m=0, g=1, E={z:first two bits are zero}, r>=2. Here H(F)=2 and I(F)=1; alpha=3/4. The crude flag bound is h2(3/4)+(3/4)r, growing solely because r-2 irrelevant labels were counted. The theorem's k=2^{r-2} coefficient is 2r+c. Removing irrelevant labels contracts this example to r=2, but does not solve unequal overlapping subcube fibers where the union block remains relevant. This is an explicit location of a dimension loss in the entropy-label step, not a failure or purported refinement of the already dimension-free real log-Sobolev channel bound.

This closes a measurable two-event access regime, not FEI for arbitrary Boolean cores. The first unsupported universal line is either admission/payment of the actual core leaves or replacing the r-bit conditional-control label price by a dimension-independent source-compatible code for large fibers, with its core reserve owned once. NEXT should test structured two-subcube fibers with growing cardinality and bounded overlap, retaining their actual terminal cores; another point-edit limit does not address this newly isolated loss.
