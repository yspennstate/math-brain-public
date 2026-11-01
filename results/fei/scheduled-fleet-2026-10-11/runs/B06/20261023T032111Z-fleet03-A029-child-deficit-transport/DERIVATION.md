# A changed nonempty profile paid from the inherited child slack

All costs are bits. The new result pays a genuine profile change after a
physical DATA query. It does not provide universal FEI source suppliers.

## 1. Original supplied-source account and finite-label extension

For fresh uniform controls Y, shared uniform data X, a finite label map L,
and Boolean sources g_j, supply normalized source references R_j positive on
their true supports. At every physical history transport each source reference
by its own actual-phase pair channel and normalize by its own reference branch
mass. Zero true rows retain their reference mass; choose a fixed fair kernel
there. Set pi_j=Pr(L=j), P_j=ghat_j^2,

    q=sum_j pi_j P_j,  r=sum_j pi_j R_j,
    W=sum_j pi_j D(P_j||R_j), Df=D(q||r), Z=W-Df.

The prescribed joint reference is Rf(U,t)=r(t)k(U|t), where
k(U|t)=P_f(U,t)/q(t) for q(t)>0 and k(empty|t)=1 otherwise.
Parseval identifies q as the true data-set marginal. The log-sum/conditional
source-label chain rule proves Z>=0 and D(P_f||Rf)=Df. This reconstructs
A028@7's binary theorem and extends that interface to any finite label list.

At a physical query put A_v=W_v-average(W_children). For DATA queries it is
the weighted sum of source erasure KL and fair-versus-reference-branch KL;
for CONTROL queries it is zero by affinity in pi. Thus A_v>=0. With
sigma_v=average(Df_children)-Df_v,

    sum_old w_v sigma_v + sum_old w_v A_v + E_frontier Z = Z_root. (1)

All signs, physical reaches, child normalizers and BOTH full physical terminal
costs are retained. For common root source references, Z_root=J_root exactly.
After DATA restriction the source references generally differ: Z is inherited
conditional-label KL, not a renewed descendant Jensen--Shannon allowance.

## 2. Genuine conditional-profile conversion

At a selected frontier node prescribe another normalized conditional profile
ell(U|t), positive wherever the true conditional k has mass. Keep the SAME
inherited r and all off-target row mass, and set Rnew(U,t)=r(t)ell(U|t).
The EXACT additional cost is

    C_v=D(P_f||Rnew)-Df_v=sum_t q(t)D(k(.|t)||ell(.|t))>=0.       (2)

Consequently the complete old entropy path plus BOTH full changed/unchanged
terminal CE costs is exactly

    H_root+W_root-sum_old w A-E_frontier Z+E_frontier C.          (3)

In particular E C<=E Z is sufficient, without spending the already booked
source contraction or original admission reserve. Old unrelated debit b is
retained by requiring U-b>=H_root+W_root for ONE original earmark U. Neither
Z nor the source expansion is added again to actual physical child deficits.
Equation(3) is their alternative complete cost expansion.

After this ONE change, every arbitrary finite adaptive no-reset physical
continuation inherits the CURRENT changed reference. KL disintegration gives
CE_parent=DeltaH+average(CE_children)+erasureKL+outcomeKL. Thus it only
decreases (3)'s payment. This is not permission to reconstruct the old profile
again without paying its signed difference. Raw reconstruction charges before
the profile change still include the actual output erasure/outcome refunds;
only the net sigma in(1) belongs to Z.

For a binary mux, let a=1-2c, p=Ec, V=4p(1-p), gamma=Pr(G!=H).
Its true nonempty controller profile A(U)=ahat(U)^2/V is independent of the
data row. Change ONLY that nonempty profile to B, retaining each row's actual
empty/nonempty split and the inherited r. Then(2) is explicitly

    C=V gamma D(A||B).                                          (4)

## 3. Actual all-width family and paid physical prefix

Let a(y)=-1 precisely at binary controller points0,1,2 of the three-bit cube.
On three shared data bits put g=-1 precisely at000, and h=-1 precisely when
at least two data bits are1. For m>=1 multiply BOTH by the same character
chi_m on m fresh data bits. Let F_m be their mux. Supply the SAME complete
uniform reference on all2^(m+3) source Fourier indices. Keep the character
coordinates unqueried until the profile change. All four source children and
both physical output children at the following DATA exposure are nonconstant.

Query the first shared data bit x0. Retain child0 on its full inherited
prescribed reference. In child1, g becomes chi_m and h becomes a signed
two-bit point defect times chi_m. Here p=3/8, V=15/16, gamma_child1=3/4.
The controller nonempty profile has one atom3/5 and six atoms1/15.

For EVERY REAL theta in[0,1/8], prescribe

    B_theta=(1-theta)A+theta Uniform(seven nonempty controller sets). (5)

For theta>0 this changes the actual profile. At theta1/8 its large atom
changes from3/5 to19/35 and its six others from1/15 to8/105. This is a
controlled mixture toward an external uniform profile, not an arbitrary
fresh target and not a free return to an original-source marginal.

## 4. A genuinely unspent inherited Z, uniformly in m

Put M=2^(m+2). In selected child1 the true data spectral atom at the common
character has mass23/32. Its true posterior source label is(20/23,3/23).
The inherited source branch masses are

    rho_g1=(5M-12)/(10M), rho_h1=1/2.

The corresponding reference masses at that character are8/(5M-12) and1/M.
Thus the reference posterior first-label probability is

    beta_M=40M/(55M-36),
    Z_m=(23/32)D(Bernoulli(20/23)||Bernoulli(beta_M)).             (6)

All other occupied rows have matching deterministic source posterior and
contribute zero. For M>=8, every denominator is positive and
8/11<beta_M<=80/101<20/23; beta_M decreases with M. The derivative of binary
KL with respect to its reference parameter is(beta-p)/(beta(1-beta)ln2)<0.
Therefore Z_m>=Z_1.

For p0=20/23, b0=80/101, binary KL as a function of its true parameter has
second derivative1/[p(1-p)ln2]. On[b0,p0], p(1-p)<=b0(1-b0), so Taylor's
integral formula gives

    Z_1 >= (23/32)(p0-b0)^2/[2 b0(1-b0)ln2]
         =135/(10304 ln2)>45/2576>1/64.                          (7)

The bound ln2<3/4 follows from the strict trapezoidal bound for integral_1^2
1/x dx. No finite parameter extrapolation enters(6)--(7).

## 5. One actual profile change costs less than1/128

Let d=Uniform_7-A. The function D(A||A+theta d) has value and first derivative
zero at theta0, and second derivative

    (1/ln2) sum_U A(U)d(U)^2/(A(U)+theta d(U))^2.

All denominators are positive on[0,1/8]. The large atom decreases to19/35;
the others increase from1/15. Hence the sum is at most

    (3/5)(16/35)^2/(19/35)^2 + 6(8/105)^2/(1/15)
      =768/1805+128/245=16768/17689.

Since V gamma=45/64, Taylor's integral formula and ln2>2/3 give, uniformly
for every theta in[0,1/8],

    C_theta <= (45/64)(1/8)^2(16768/17689)/(2 ln2)
              <17685/(128*17689)<1/128.                          (8)

The strict midpoint bound for integral_1^2 1/x dx proves ln2>2/3. The final
comparison is EXACTLY17685<17689. Fractions in the checker independently
verify every rational reduction. The exact endpoint cost is

    C_(1/8)=(45/64)[(3/5)log2(21/19)+(2/5)log2(7/8)].           (9)

Equations(7)--(8) leave MORE than1/128 of the selected child's SAME Z.
Its original physical reach is1/2, so more than1/256 remains in full root
units. The unselected child retains its complete original H+KL bill.

## 6. Same original influence quota, old debit and all later physical trees

Direct edge counts give I(F_m)=m+29/16: source data influence33/32,
controller influence25/32, and m character influences. Use the SAME original
U=4I(F_m), old debit b=1/8. Tensoring the character shifts Fourier sets,
so H(F_m)<=6. Uniform source references give W_root<=m+3. Consequently

    U-b-[H_root+W_root]>=3m-15/8>=9/8.                          (10)

Combining(3),(7),(8),(10), every finite adaptive physical no-reset continuation
AFTER the prescribed changed profile has full payment

    old entropy path + complete terminal CE < U-b-(3m-15/8+1/256).

Thus more than289/256 of the original quota remains for every m>=1. This
whole-quota reserve and the selected child's Z remainder>1/128 are DIFFERENT
accounts, not two estimates for the same quantity. The profile change is paid
entirely from inherited Z; admission slack is not used to establish eligibility.
No child receives a fresh4I allowance, and both actual terminal references,
old source contraction and output refunds stay in the exact formula.

## 7. Required failure control and unpaid universal line

For m=0, M=4 and beta_M=20/23, so selected-child Z=0 EXACTLY. The same
theta1/8 profile change costs the positive value(9). Thus deleting the
remaining-character condition invalidates payment from this specific child Z.
It does not refute FEI, the root quota4I, other available original admission
slack, or a transfer from the unselected sibling. Querying away every common
character before this step can likewise remove the proved eligibility.

The new result is an analytic author proof with exact finite checks, pending
independent review. The generic finite-label condition(2)--(3) is available
without a class assumption, while the verified source of eligibility is the
family above. Full FEI remains OPEN. The first unsupported universal line is
an influence-priced source/structural/reference account guaranteeing useful
profile eligibility for arbitrary Boolean sources, or a second changed-profile
transaction after retaining this one's true debit and all old terminals.
