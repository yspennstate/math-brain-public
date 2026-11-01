# Mixed-history odds conversion from the same original account

All costs are bits. Analytic author proof, external review pending. Full FEI OPEN.

## 1. Independently reconstructed supplied-reference mixed account

For arbitrary Boolean binary mux f=(1-c)G+cH, controller a=1-2c on
independent uniform controls, p=Ec,V=Var(a),gamma=Pr(G!=H), retain fixed
original source/controller references Rg,Rh,Ra, positive on true supports.
Each reference inherits by its OWN actual-phase pair kernel and OWN branch
normalizer; zero-true pairs use a fair kernel. Retain all off-support mass.
Let q=(1-p)Pg+pPh,r=(1-p)Rg+pRh, W=(1-p)D(Pg||Rg)+pD(Ph||Rh),
Z=W-D(q||r). For each data row put z=(1-p)ghat+p hhat,
w=V(ghat-hhat)^2/4; q=z^2+w. Define A=Pa/V on nonempty controller sets,
beta=1-Ra(empty),B=Ra/beta on nonempty sets. The canonical external-shape
output reference has row marginal r, actual nonempty odds k=w/q and shape B;
all q0 row mass is at the empty controller set.

Conditional-label KL gives Z>=0. The true output spectrum has masses z^2
and w A. Direct chain rules give

 Dstar=D(q||r)+gamma V D(A||B),
 Da=D(Pa||Ra)=Cvac+V D(A||B), Cvac=D(Bern(V)||Bern(beta)),
 T=W+gamma Da, S=Z+gamma Cvac>=0, Dstar=T-S.                 (1)

At DATA queries gamma is harmonic, Da is fixed, and W contracts by weighted
source erasure/outcome KL. At CONTROL queries W is affine in p and gamma
is fixed, while Da contracts by its own controller erasure/outcome KL. Thus
Atot=T-average Tchild>=0 for either query. Finite actual reaches telescope:

 sum w sigma+sum w Atot+E Sleaf=Sroot,
 sigma=average Dstar_child-Dstar_parent.                   (2)

Full true entropy path plus BOTH full terminal CE equals
Hroot+Troot-sum w Atot-E Sleaf. Raw output reconstruction charge equals
sigma plus actual output erasure/outcome KL refunds. They cannot be omitted
or charged twice. This proves A028@8 sections1-3 at supplied-reference scope,
without its optional v5 influence surcharge or universal suppliers.

## 2. The missing row-odds transaction

For this transaction require a nonempty controller index set and beta>0, so
the inherited normalized B exists. The concrete selected node has V=1.
At a selected canonical node replace ONLY k_t by

 ell_t=(1-epsilon) k_t+epsilon/2, 0<=epsilon<=1/16,          (3)

keeping SAME inherited row marginal r, external nonempty shape B, and every
zero-true-row atom. For q_t>0 put Qnew(empty,t)=r_t(1-ell_t),
Qnew(U,t)=r_t ell_t B(U). At q_t=0 retain old completion. Exact extra KL is

 Ceps=sum_t q_t D(Bern(k_t)||Bern(ell_t))>=0.               (4)

Thus S becomes S-Ceps, with T unchanged. Neither a new source reference nor
another controller allowance is issued. Thereafter every finite adaptive
physical continuation inherits the CURRENT changed full reference, with no
free canonical reconstruction. KL disintegration proves its full payment
can only decrease, retaining all query refunds and both physical terminals.

## 3. Actual mixed prefix, including the first paid transaction

Use EXACTLY A029@2's original family: controller a negative at points0,1,2
on3 bits, g negative only at000, h negative at Hamming weight>=2 on3 data
bits, both multiplied by a common character chi_m on m>=1 fresh bits.
Original Rg=Rh are uniform on all2^(m+3) data frequencies. First expose DATA
x0. Keep original child0 and its complete canonical reference. In child1
G=chi_m,H=chi_m times signed point2, gamma=3/4,V=15/16.
The TRUE nonempty controller shape A has one3/5 and six1/15 atoms.

Retain the SAME FIRST profile change B=(7/8)A+(1/8)Uniform_7. Its exact old
cost C1=(45/64)D(A||B)<1/128 is A029@2 equation(8), reconstructed by the
same rational curvature bound16768/17689. It was already paid from the
inherited source-label Z>45/2576. To represent this CURRENT shape through a
controller query, declare Ra=(Pa(empty),V B) before either query and carry
it unchanged across DATA x0. Use it only on selected child1; the root and
unselected output references remain their original canonical laws. Ra is a
fixed bookkeeping reference, not a fresh descendant supplier. At the selected
node Cvac=0 and gamma Da=C1, so Tparent=Wparent+C1 EXACTLY.

Now query physical controller y0. Carry the CURRENT changed output reference
through its actual output channel, and reconstruct each output child using
that child's inherited Ra/Rg/Rh. Keep the full raw charge and both refunds.
A028@8 equation(2) pays the NET reconstruction using the account just defined.
Both controller children, all source children and the original DATA sibling
remain in the tree. The controller child y0=0 has p=1/2,V=1 (a character),
G=chi_m,H=the same signed point2 times chi_m. Both data sources/output
children remain nonconstant because m>=1. Select only this child for(3).

## 4. Uniform inherited child slack and exact odds cost

Put M=2^(m+2). In the selected child, the common-character data atom has
q=5/8, true source-label posterior(4/5,1/5). The inherited source reference
masses at that atom remain8/(5M-12) and1/M from the first DATA query.
With equal source weights its reference posterior first-label probability is

 beta_M=8M/(13M-12),
 Zselected=(5/8)D(Bern(4/5)||Bern(beta_M)).                  (5)

Every other occupied row has matching deterministic label posterior. M>=8
implies8/13<beta_M<=16/23<4/5. beta decreases with M; binary KL decreases
in its reference argument below4/5. Taylor in the true parameter, with
p(1-p)<=b(1-b) on[b,p], and ln2<3/4, gives

 Zselected>= [ (5/8)(4/5-16/23)^2/(2(16/23)(7/23)) ]/ln2
           =9/(560 ln2)>3/140>1/48.                       (6)

In this selected child, true nonempty odds are9/10 at that data atom and
1/2 on every other occupied row. Thus the genuine new row-odds charge is

 Ceps=(5/8)D(Bern(9/10)||Bern(9/10-(2/5)epsilon)).           (7)

For positive epsilon it is STRICTLY positive. It changes conditional
empty/nonempty odds, whereas the old B transaction changed only shape.
Along epsilon0..1/16, the first denominator is>=7/8 and its complement>=1/10.
The second derivative of the unscaled binary KL is bounded by

 (1/ln2)[(9/10)(2/5)^2/(7/8)^2+(1/10)(2/5)^2/(1/10)^2]
   =(10952/6125)/ln2.

Value and first derivative vanish at0. Taylor and ln2>2/3 imply

 Ceps < (5/8)(1/16)^2(3/2)(10952/6125)/2
       =4107/1254400<1/256.                              (8)

Integral midpoint/trapezoid bounds for1/x on[1,2] prove the ln2 bounds.
These all-width/all-real proofs do not extrapolate finite tests.

## 5. Keep the first debit; do not count child slack twice

Let A0 be the first DATA source contraction. Let Acontrol be the controller
T contraction at the selected first child. Before final continuation, the
EXACT full entropy path plus the THREE full terminal CE bills is

 Hroot+Wroot-A0-(1/2)Z_DATA0+(1/2)C1-(1/2)Acontrol
              -(1/4)[S_control0-Ceps+S_control1].          (9)

This is an alternative expansion of actual terminal CE, NOT another debit
added on top of it. C1 occurs ONCE and is never dropped. The two S terms are
computed from CURRENT inherited references, with their controller vacuum KL.
Since S_control0>=Zselected, S_control1>=0, A0,Acontrol>=0, equations(6)-(8)
give

 (1/2)[S_control0-Ceps+S_control1]-C1
    > (1/2)(1/48-1/256)-1/128=1/1536.                    (10)

The selected first child's original reach is1/2. Equation(9) is therefore
strictly below Hroot+Wroot-1/3072, before any later physical query refunds.
This is the same original source account, including the FIRST profile debit.
The previous >1/128 selected remainder concerned one shape transaction;
the present >1/1536 accounting margin concerns a later controller query plus
new odds transaction and includes the earlier C1. They are different scopes.

For SAME U=4I(F_m), old debit b=1/8, I(F_m)=m+29/16,
Hroot<=6,Wroot<=m+3, the full payment after ANY finite adaptive continuation
of all three CURRENT references, with NO additional free reset, satisfies

 U-b-payment >3m-15/8+1/3072>=3457/3072.                   (11)

No descendant4I is granted, no initial Z is added to(9) again, and source or
output refunds are never spent a second time. The slightly smaller proved
whole-quota floor than stage7 reflects the extra mixed/odds transactions and
weaker lower bounds, not a changed influence rate or changed old debit.

## 6. Adversarial scope and unpaid universal line

m=0 gives M=4,beta=4/5, selected Z=0 exactly; any positive odds conversion
costs>0. Thus the local bound from Z alone fails without m>=1, while actual
S may still include positive controller vacuum credit. This is not a
counterexample to the full original quota or FEI. Epsilon beyond1/16 is not
admitted by this proof, even when individual finite cases happen to pass.

The universal first unsupported line remains an influence-priced ORIGINAL
source/controller/reference account guaranteeing required profile/odds
eligibility for arbitrary Boolean sources. After the new odds change the
reference is no longer in the actual-row-odds canonical family. Another
canonical reconstruction must retain and price its signed difference from
the CURRENT transported odds-changed reference. This stage does not license
arbitrary repeated odds reset, controller-source re-admission or full FEI.
