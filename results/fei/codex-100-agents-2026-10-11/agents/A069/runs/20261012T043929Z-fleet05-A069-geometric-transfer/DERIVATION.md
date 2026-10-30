# Stage 2 mathematical result (bits, uniform actual Boolean signs)

Let L_T(S)=1+sum_v b_v 1{S intersects C_v}; Gamma_T(g)=sum ghat(S)^2 L_T(S). The all-set prefix decoder and weighted Parseval transfer from A069 v1 were independently accepted by A070 without repair. All trees below are fixed before sampling S.

## Exact lead-directed recursive-majority certificates

For depth-2 complete ternary recursive majority, I=9/4. The main tree has one root and three internal depth-1 vertices, so its expected internal occupancy is 1+3/2=5/2. Thus Gamma=1+3*(5/2)=17/2 at N=9. Attaching padding by a binary join adds exactly 2 and no occupied padding internal vertices. Hence Gamma=21/2 at every N>9, in particular N=10,11,12. The earlier exact run covered every one of the 512 one-point edits at N=9 and certified Gamma(edited)<=25I(edited); this stage reuses that result and its A070 review rather than rerunning it. New direct integer transforms check the base at N=11,12.

## Addressing: complete hierarchy versus influence code

Let A_a(z,y)=y_z, a>=1, m=2^a data bits, n=a+m, and pad to N>=n. Every Fourier set has one data bit j and an arbitrary subset of the a selectors. The pair (j,selector subset) is uniform on m*2^a possibilities: each coefficient is 2^{-a} times the selector character at j. Thus I=1+a/2, selector influences=1/2, data influences=2^{-a}, and H=2a. These are existing addressing identities, not new FEI claims.

Use a balanced binary tree on selector coordinates and a complete binary tree on data coordinates; join them under a binary root. When present, attach the binary padding tree under one additional binary join. Put R(1)=0 and, for k>=2,

    R(k)=1-2^{-k}+R(floor(k/2))+R(ceil(k/2)).

Every selector-tree cell of size k is occupied with probability 1-2^{-k}. The lone chosen data leaf occupies exactly one internal cell per data depth, giving a occupied internal data vertices. Root occupancy is certain. Therefore

    Gamma_T(A_a)=3+2a+2R(a)+2*1{N>n}
               <=4a+3=8I(A_a)-5,                         (A1)

since R(a)<=a-1. A binary tree has N-1 internal vertices, so max L_T=2N-1. For any edit set of fraction rho,

    Gamma_T(f)<=2Gamma_T(A_a)+8rho(2N-1)
              <=16I(f)-10+48N*rho-8rho.                  (A2)

Here |I(f)-I(A_a)|<=2N*rho retains the same physical edit budget. Thus N*rho<=1/8 gives Gamma_T(f)<=16I(f). For one point, N>=3, N*2^{-N}<=3/8 and I(f)>=Var(f)>=15/16. Consequently

    Gamma_T(f)<=16I(f)+8 <=(368/15)I(f)<25I(f).           (A3)

For N>=6 a one-point edit satisfies the stronger 16I bound. Since the code contains all subsets, new tail atoms are covered. Weighted L2 stability gives vanishing excess for fixed a under padding and one-point editing. This is a distinct complete reference from A070's proposed queue reference; no queue computation is duplicated.

For comparison, the influence reference length l_inf(S)=log2(e)+sum_{i in S}log2(I/Inf_i) has exact expected cost on unedited addressing

    log2(e)+a+(a/2)*log2(a+2)+log2((a+2)/2).              (A4)

Dividing by I=1+a/2 gives log2(a)+2+o(1), whereas (A1)/I<=8. Padding leaves (A4) unchanged on the original support. A070 separately proves divergence of the granularity/level/influence hybrid on point-edited addressing; that existing no-go is source-bound context, not a new claim here. The hierarchy code pays the selector choices and the one data label once for the whole set. The original addressing family is already a solved baseline; the delta is all-set coding after edits.

## Exact subcube edit energy with the terminal core retained

Split N coordinates into a nonempty control block Z of size r and a nonempty free block Y. Join fixed binary singleton-leaf trees T_Z,T_Y under a binary root. Let W_Z(U)=sum_{v internal in T_Z}2*1{U meets C_v}, similarly W_Y(V). Then

    L_T(U union V)=1+2*1{U union V nonempty}+W_Z(U)+W_Y(V).

For any Boolean g, choose z*, let D={z=z*}, rho=2^{-r}, h(y)=g(z*,y), and flip g on D to obtain f. Then delta=f-g=-2*1_D*h and, at every pair U,V,

    deltahat(U,V)=-2*rho*chi_U(z*)*hhat(V).

Thus delta's norm is 4rho and its normalized squared spectrum is the product of the uniform subset law on Z and the full squared spectrum of h, including its empty coefficient. Write m_h=hhat(empty),

    U_Z=sum_{v internal in T_Z}2*(1-2^{-|C_v|}),
    E_delta=sum_{U,V} deltahat(U,V)^2 L_T(U union V).

The exact complete energy identity is

    E_delta=4rho*[1+2*(1-rho*m_h^2)+U_Z+E_{S_h}W_Y(S_h)]. (S1)

This replaces the blind 4rho*max L_T bound, which scales with N, by an explicit r-scale charge PLUS the restricted core's full expected code cost. Dropping the final term is invalid for arbitrary cores. It is neither raw label entropy nor an assumed incoherent mixture for f: this product identity concerns the actual difference delta, whose coherent cross term with g is still retained by the weighted triangle.

Physical restriction Parseval gives the marginal identity

    E_{S_g}W_Y(S_g cap Y)=2^{-r} sum_z E_{S_{g_z}}W_Y(S_{g_z}). (S2)

Every term is nonnegative, so rho*E_{S_h}W_Y<=E_{S_g}W_Y. Also U_Z<=2(r-1). Therefore

    E_delta<=4E_{S_g}W_Y+4rho*(2r+1),                    (S3)
    Gamma_T(f)<=2Gamma_T(g)+2E_delta
              <=2Gamma_T(g)+8E_{S_g}W_Y+8rho*(2r+1).     (S4)

On every Y-edge, both endpoints are edited together or neither is, hence Inf_i(f)=Inf_i(g) for i in Y. On Z-coordinate i the crossing-D edges have total directed probability 2rho; one of f,g is pivotal on each such edge, while all other edge contributions are nonnegative. Hence

    Inf_i(f)+Inf_i(g)>=2rho (i in Z),
    I_Z(f)+I_Z(g)>=2r*rho.                              (S5)

The control-scale edit charge has a physical boundary budget, but (S4) is not a universal FEI theorem: a paid separating reference for arbitrary g and an influence budget that transfers to f without cancellation remain unproved. In particular f may be constant after cancellation; a root-bit code has positive cost even then. No conclusion Gamma_T(f)<=C I(f) is asserted for all subcube edits.

## Honest universal line and next mechanism

First unsupported line: select a normalized all-set source reference that separates a useful edit block, with Gamma_T(g) and the averaged restricted-core cost paid by a single conserved influence budget for an arbitrary Boolean source. Equations (S1)-(S5) expose rather than solve that obligation. Next: two subcube edits with overlapping controls, compute the exact signed cross-energy and determine whether first exposure can own it once while retaining both terminal cores. This advances the generic transfer interface rather than another unedited addressing/read-once FEI baseline.
