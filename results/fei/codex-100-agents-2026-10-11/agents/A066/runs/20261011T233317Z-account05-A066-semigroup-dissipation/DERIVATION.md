# Restriction-compatible heat entropy: a positive row ledger

Natural logarithms throughout. Zero mass contributes zero. Let f be a Boolean sign on a finite uniform cube, p_S=hat(f)(S)^2, H_nat(f)=sum p_S ln(1/p_S), I=sum |S|p_S. Retain the previous stage's heat functional

K(f)=integral_0^infinity J_f(t)dt=(H_nat(f)-b(f))/2,
b(f)=p_empty ln(1/p_empty), J_f(t)=sum |S|p_S exp(-2t|S|)ln(1/p_S).

This integral is finite at both endpoints for each f, as proved in the first stage. It is not assumed bounded universally by influence.

## 1. Exact physical-block identity, including the level term

Partition coordinates into a physical block B and its complement V. Write Fourier indices as U union T, U subset B, T subset V. For uniformly sampled y on B the child coefficient is

c_y(T)=sum_{U subset B} hat(f)(U union T) chi_U(y), p_y(T)=c_y(T)^2.

Orthogonality gives q_T=E_y p_y(T)=sum_U p_{U union T}. Define row charges

M_T=sum_U p_{U union T} ln(q_T/p_{U union T}),
C_T=E_y p_y(T) ln(p_y(T)/q_T).

For q_T=0 both charges vanish. M_T>=0 is q_T times conditional entropy. C_T>=0 follows from convexity of x ln x and E p_y=q_T. Summing gives C006 in natural units:

H_nat(f)-E_y H_nat(f_y)=M_B+C_B,
M_B=sum_T M_T=H_nat(S_B|S_V), C_B=sum_T C_T=I_nat(Y;T).

The heat drop is therefore exactly

2[K(f)-E_y K(f_y)]=M_B+C_B-b(f)+E_y b(f_y).                       (1)

The empty T row can be canceled explicitly. Set

M_B^+=sum_{T nonempty} M_T, C_B^+=sum_{T nonempty} C_T,
ell_B(f)=sum_{empty != U subset B} p_U ln(1/p_U).

Then

2[K(f)-E_y K(f_y)]=M_B^+ + C_B^+ + ell_B(f).                     (2)

Indeed M_empty+C_empty equals sum_{U subset B} p_U ln(1/p_U)-E_y b(f_y); subtract b(f) to obtain ell_B. This identifies precisely which level mass leaves the heat integral: coefficients wholly contained in B become constant coefficients in the children. In particular K(f)>=E_y K(f_y) for every physical block. This positivity is not obtained merely by dropping the boundary term in (1).

## 2. Singleton costs which are paid uniformly

Take B={i}. Let d_i=Inf_i(f), a=hat(f)(T), c=hat(f)(T+i), q=a^2+c^2. The two child masses are (a+c)^2 and (a-c)^2. The row channel is

C_T=q g(2ac/q), g(r)=((1+r)ln(1+r)+(1-r)ln(1-r))/2.

For |r|<=1, g(r)<=1-sqrt(1-r^2). For r>=0 the derivatives satisfy g'(r)=atanh(r)<=r/sqrt(1-r^2): the derivatives of the latter two functions are 1/(1-r^2) and 1/(1-r^2)^(3/2), respectively, and both functions start at zero. Integrating proves the bound; continuity covers r=1 and evenness covers negative r. Hence

C_T<=2 min(a^2,c^2), C_{ {i} }^+<=C_{ {i} }<=2d_i.               (3)

For a Boolean sign, |hat(f)({i})|<=d_i, since its coefficient is the mean of the discrete derivative, which takes values in {0,+1,-1}. Put x=|hat(f)({i})|. Since x ln(1/x)<=1/e,

ell_{ {i} }=x^2 ln(1/x^2)<= (2/e)x <=(2/e)d_i.                  (4)

Thus the level charge is paid by the physical coordinate being erased, including on majority. No all-block version of (4) is asserted. For a block containing all relevant coordinates, ell_B can be the entire nonempty Fourier entropy; bounding it universally by I_B is already FEI strength.

## 3. Explicit C018/C019 residual, without hiding a level charge

Let M_i^+(f) be the conditional erasure row sum omitting T=empty, and define R_nat(f)=sum_i M_i^+(f). If B_nat(f)=sum_i H_nat(S_i|S_without_i), then

0<=B_nat(f)-R_nat(f)<= (1+2/e)I(f).                              (5)

To prove this, the omitted row has masses u=p_empty, v=p_{ {i} }, q=u+v<=1. Its entropy is v ln(q/v)+u ln(q/u)<=v ln(1/v)+v, using ln(1+v/u)<=v/u. With x=sqrt(v), v ln(1/v)<=2x/e and v<=x<=d_i, giving (5). The zero-u or zero-v cases follow by continuity.

Consequently a finite dimension-independent R_nat(f)<=A I(f) is equivalent to C018 up to this paid additive constant, and remains OPEN. A direct physical-singleton heat proof gives an explicit FEI implication: choose i with M_i^+<=A d_i at every node (by weighted averaging). Telescope (2), (3), (4) down a complete tree and the ordinary influence identity. Then

H_nat(f)<= (A+3+2/e) I(f),
H_bits(f)<= [(A+3+2/e)/ln 2] I(f).                              (6)

Conversely R_nat<=B_nat<=H_nat, so FEI with bit constant C gives R_nat<=C ln(2)I. The inequality B_nat<=H_nat follows by comparing each fully conditional bit entropy with the entropy conditioned only on preceding bits and summing the chain rule.

There is a sharper universal scope guard: deleting the empty context does not lower the optimal all-Boolean erasure constant at all. For any Boolean g and any m>=1 let F_m=y product_{j=1}^m g(x^(j)), with disjoint copies and one fresh character coordinate y. Every occupied Fourier set contains y. Thus for every core coordinate its remaining context is nonempty, M_i^+(F_m)=B_i(F_m); the y-coordinate has both quantities zero. Independence of the copy spectra gives

R_nat(F_m)=m B_nat(g), I(F_m)=m I(g)+1.                          (6a)

If R_nat<=A I universally, (6a) gives B_nat(g)<=A[I(g)+1/m]; letting m grow proves B_nat<=A I with the SAME constant. Since R_nat<=B_nat, the optimal universal constants for R_nat/I and B_nat/I are equal. The original C018 implication consequently yields the stronger global FEI constant (A+2)/ln2; (6) is the direct heat-ledger implication with its separately paid level and boundary terms. This arbitrary-core admission is why zero-context removal is a bookkeeping reduction rather than an easier structural class.

Booleanity is indispensable in the paid level step. The normalized non-Boolean singleton spectrum p_{ {i} }=1/n has R_nat=0, but ell_{ {i} }=(ln n)/n and d_i=1/n, so (4) fails for large n. Neither (6) nor the equal-constant conclusion is asserted for arbitrary real normalized wavefunctions.

For an arbitrary finite stopping tree, weighted (2) gives the exact C019 ledger

2[K(f)-E_leaf K(leaf)] = sum_nodes w_v M_i^+(f_v)
                       + sum_nodes w_v C_i^+(f_v)
                       + sum_nodes w_v ell_{ {i} }(f_v),         (7)

where the last two sums together are at most (2+2/e)[I(f)-E_leaf I(leaf)]. Every query spends the same physical influence once. Terminal K is retained. In terms of full entropy, (7) also retains b(f)-E_leaf b(leaf). No terminal arbitrary core is declared free.

The FIRST UNSUPPORTED LINE is a universal bound on the remaining M_i^+ charge: either R_nat<=A I at every Boolean restriction, or sum_nodes w_v M_i^+<=A[I(f)-E_leaf I(leaf)] with separately paid terminal entropy for a specified tree. Removing the empty context is a rigorous paid simplification, not a proof of this inequality.

## 4. Odd majority: a closed all-n singleton calculation

Let n=2m+1 and f=Maj_n, m>=0. Complement symmetry f(-x)=-f(x) forces only odd Fourier levels. In each singleton row T,T+i at most one coefficient is nonzero. Thus M_i^+=M_i=C_i^+=C_i=0, and both children preserve the parent's Fourier entropy exactly. The singleton coefficient and influence are

hat(f)({i})=d_i=alpha_m=binom(2m,m)/2^(2m).

The child mean is +/-alpha_m, so (1) and (2) agree and give

K(Maj_n)-E K(child)=(alpha_m^2/2)ln(1/alpha_m^2),
[K(Maj_n)-E K(child)]/d_i=alpha_m ln(1/alpha_m)<=1/e.              (8)

For m>=1 this heat drop is positive despite a zero C006 channel term and zero erasure. The whole drop is the paid singleton level charge. For m=0 it is zero. Therefore a channel-only bound K(f)-E K(child)<=A C_{ {i} } is false for every finite A, already on Maj_3. Formula (8) does not pay the majority entropy left in the children. Higher-block costs are given exactly by (2), and are checked on Maj_n for odd n<=9 and every block size.

## 5. Point-defected addressing: exact block histograms

Let Addr_a have a address bits and 2^a distinct data bits, a>=1. Its base dimension is k=a+2^a. Put A=2^(-a), M=4^a, m_+=(M+2^a)/2, m_-=(M-2^a)/2. At the all-plus vertex Addr_a=+1; its Fourier coefficients are +A at m_+ indices, -A at m_- indices, and zero elsewhere. Pad by r>=1 coordinates, D=k+r, delta=2^(-D), and flip that vertex:

F_{a,r}=Addr_a-2 indicator_{all D inputs are +1}.

This is a genuine Boolean sign. Its coefficients are b_S-2delta, where b_S is an original addressing coefficient or zero. With eta(z)=z ln(1/z),

H_nat(F)=m_+ eta((A-2delta)^2)+m_- eta((A+2delta)^2)
          +(2^D-M)eta(4delta^2),
I(F)=1+a/2+2delta(D-2), b(F)=eta(4delta^2).                     (9)

The influence formula also follows physically: only the selected data coordinate loses a pivotal edge; the other D-1 coordinates gain one, each changing influence by 2delta.

Erase b of the r padding coordinates, 1<=b<=r, and write w=2^b. Each erased coordinate has influence 2delta, hence I_B=2b delta. For each residual index T, its original coefficient z belongs to {+A,-A,0}. There are m_+,m_-,2^(D-b)-M such rows, respectively. Define

x_z=(z-2delta)^2, s=4delta^2, q_z=x_z+(w-1)s,
c_z=(z-2w delta)^2,
M(z)=x_z ln(q_z/x_z)+(w-1)s ln(q_z/s),
C(z)=(c_z/w)ln(c_z/q_z)+(1-1/w)z^2 ln(z^2/q_z).                (10)

Then M_B and C_B are the corresponding three weighted row sums. These formulas follow directly from the exceptional physical block assignment, of probability 1/w; all other children are the clean address function. For zero rows, M(0)=C(0)=w s ln w exactly. To obtain M_B^+,C_B^+ remove the one empty residual zero row. The entire lost level charge is

ell_B=(w-1)eta(4delta^2),
b(F)-E b(child)=eta(4delta^2)-(1/w)eta(4w^2delta^2).             (11)

The heat drop is the nonnegative expression (2), or one half of M_B+C_B minus the boundary difference in (11). Equations (9)–(11) are exact for every a,r,b, including blocks of all padding coordinates. No child histogram is treated as an incoherent substitute for the actual signed coefficients.

For fixed a and fixed b, as r tends to infinity, the zero rows dominate at order delta and the original-support row erasure/channel contributions are O_a,b(delta^2 ln(1/delta)) and O_a,b(delta^2), respectively. Thus

M_B/I_B -> 2ln 2, C_B/I_B -> 2ln 2,
[K(F)-E K(child)]/I_B -> 2ln 2.                                (12)

For the full padding block b=r, put rho=M/2^k and sigma=2^(-k). An expansion of (10) instead gives

M_B/I_B -> 2(1+rho)ln 2, C_B/I_B -> 2(1-rho)ln 2,
ell_B/I_B -> 4sigma ln 2,
[K(F)-E K(child)]/I_B -> 2ln 2.                                (13)

Proof of the changed proportions: the zero-row count is now fixed, 2^k-M; their common row charge w s ln w divided by 2r delta tends to 2sigma ln2, hence total 2(1-rho)ln2. For a nonzero row, x_z tends to z^2, q_z-x_z=(w-1)s=4sigma delta+o(delta); its M charge has leading term (w-1)s ln(1/s)=8sigma delta r ln2+O_a(delta), giving 4sigma ln2 per row after normalization. Its C charge is O_a(delta), since the exceptional child coefficient z-2w delta=z-2sigma is fixed, so its normalized channel tends to zero. Adding gives (13). The normalized boundary difference tends to zero. These are analytic limits, not grid extrapolations.

For the full padding block the level mass has a nonzero limiting share, 4sigma ln2. It is not supplied by C_B. Refining the block into singletons pays each resulting level charge using (4), but leaves the M_i^+ tree debt in (7). The point-defected address family is a stress test of the bridge, not an arbitrary-core terminal admission.
