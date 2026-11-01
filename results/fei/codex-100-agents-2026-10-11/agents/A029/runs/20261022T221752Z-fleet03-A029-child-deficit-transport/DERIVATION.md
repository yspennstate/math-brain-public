# A finite-label signed source account

All entropy is in bits. This is a residual-payment theorem, not a proof of FEI.
The structural term and every source terminal cost remain in the formula.

## 1. Exact object and sector identity

Let Y and X be disjoint independent uniform finite Boolean cubes. Let
L:Y->{0,...,r-1} be any label map and let g_0,...,g_(r-1) be arbitrary Boolean
functions on the SAME data cube X. Set F(y,x)=g_L(y)(x) and pi_j=Pr(L=j).
Every physical restriction retains this representation, including zero-weight
labels and constant sources. No source is silently removed.

For a data Fourier set t define a_t(y)=ghat_L(y)(t),
P_j(t)=ghat_j(t)^2 and q(t)=E_y a_t(y)^2=sum_j pi_j P_j(t).
Parseval over Y gives q(t)=sum_s Fhat(s,t)^2, the actual data-set marginal.
Thus q is normalized, even when some rows vanish. Put

    T=sum_j pi_j H(g_j),
    J=H(q)-T=JS_pi(P_0,...,P_(r-1)),
    Lstr=sum_(t:q(t)>0) q(t) H((Fhat(s,t)^2/q(t))_s).

The exact entropy chain rule is

    H(F)=T+J+Lstr.                                      (1)

J and Lstr are nonnegative and J<=H(pi). All sums are finite. A zero row is
omitted, not divided by zero. No assumption on overlap, source balance,
orthogonality, controller shape, or number of labels is imposed.

## 2. Quantitative root price from the actual physical control influence

For a nonnegative function v on a uniform finite cube, write
Ent(v)=E[v log2 v]-(Ev)log2(Ev), with 0 log 0=0.
For arbitrary reals a,b the two-point inequality is

    Ent_(uniform pair)(a^2,b^2) <= (a-b)^2/(2 ln 2).    (2)

Here is a scalar proof, including the sign issue. If a=b=0, both sides vanish.
Otherwise put p=a^2/(a^2+b^2), z=|2p-1|. In natural logarithms the entropy
defect is

    A(z)=((1+z)ln(1+z)+(1-z)ln(1-z))/2.

For 0<=z<1,
z/sqrt(1-z^2)-atanh(z)>=0: its derivative is
(1-z^2)^(-3/2)-(1-z^2)^(-1)>=0 and its value at zero is zero.
Integrating once gives A(z)<=1-sqrt(1-z^2). Continuity gives both endpoints.
Multiplication by (a^2+b^2)/(2 ln 2) gives the stronger RHS
(|a|-|b|)^2/(2 ln 2), which is <= the RHS of (2). This proves (2) without
cancelling a possibly zero amplitude or requiring equal signs.

Entropy tensorizes:

    Ent_Y(v) <= sum_i E_(Y without i) Ent_(Y_i)(v).     (3)

One finite-dimensional proof uses induction and the exact decomposition of
Ent over a coordinate. Convexity of Ent on nonnegative vectors gives
Ent(E_i v)<=E_i Ent(v). On positive vectors that convexity follows from
sum h_x^2/v_x >= (sum h_x)^2/sum v_x (weighted Cauchy--Schwarz);
continuous extension includes zero entries. This supplies the induction step.

Apply (2)--(3) to each a_t^2 and sum over t. Exactly

    J=sum_t Ent_Y(a_t^2)
     <= (1/(2 ln 2)) sum_i E_y sum_t(a_t(y)-a_t(y^i))^2
      = (1/(2 ln 2)) sum_i E_(y,x)(F(y,x)-F(y^i,x))^2
      = (2/ln 2) I_controls(F).                        (4)

The middle equality is Parseval on the shared data cube. The last equality
uses Boolean outputs: the squared difference is four times a flip indicator.
Independence of X,Y is essential here. Equation (4) is an explicitly
reconstructed tensorized JS estimate, not a new general FEI theorem.

For two sources selected by c=(1-a)/2, I_controls(F)=Pr(G!=H)I(a).
Consequently (4) independently supplies A028@6's optional quantitative
premise J<=2log2(e) gamma I(a), at the same constant, without assuming
the rest of A028@5's structural/reference payment. In particular no claimed
constant changes: this is the finite-label form of that bound.

## 3. One signed account through every mixed physical tree

At a DATA query, pi is unchanged and source j has its two actual children.
Writing Delta Z=Z-parent-average(Z-children), define the ACTUAL booked bill

    d_v=Delta H(F)-sum_j pi_j Delta H(g_j)-Delta Lstr
       =J_v-(J_v0+J_v1)/2.                            (5)

Both child source entropies and the signed structural difference are present.
At a CONTROL query, sources do not change and pi=(pi^0+pi^1)/2.
J(pi)=H(sum pi_j P_j)-sum pi_j H(P_j) is concave on the entire simplex,
since entropy is concave and the second summand is linear. Therefore

    c_v=J_v-(J_v0+J_v1)/2>=0.                        (6)

No differentiation at a vanished row is needed. For EVERY finite adaptive
mixed physical stopping tree, with physical reach w_v, telescoping gives

    sum_DATA w_v d_v + sum_CONTROL w_v c_v
         + sum_leaf w_l J_l = J_root.                 (7)

In particular the signed DATA bill is at most
min(H(pi_root),(2/ln 2)I_controls(F_root)). Every partial frontier obeys (7).
The remaining account after BOTH kinds of booked transactions is exactly
sum_frontier w_v J_v. Negative data bills are refunds. No child receives a
fresh root allowance. All terminal H(F_l)=T_l+J_l+Lstr_l remain.

For comparison with A029@5's AND2 guard: the old unbooked entropy decrement
is 2, while (5) subtracts the structural decrement 1 and leaves J debit 1.
Thus the old extra-price floor 3 and this new residual bound concern
different bills. The structural bit is still owed; there is no contradiction
and no new full entropy price.

## 4. The supplied-slack condition, without counting it twice

If one ORIGINAL earmark U is supplied for this JS component, with U>=J_root,
and b is a pre-existing debit from that SAME earmark, then b+J_root<=U is
the sufficient admission condition. After a partial history the exact unused
amount is

    U-b-sum_DATA w d-sum_CONTROL w c
       = U-b-J_root+sum_frontier w J.                 (8)

If full frontier JS remains promised, the amount available for an additional
reference conversion is ONLY U-b-J_root, not the frontier JS a second time.
This is the condition under which a difficult signed split is compensated by
supplied unused child slack. It does not assert that an arbitrary function
supplies such an earmark. In particular adding (4)'s allowance again after
each restriction spends the original control influence repeatedly.

For an FEI deficit, the exact root relation is

    K I(F)-H(F)=sum_j pi_j[K I(g_j)-H(g_j)]
                    +K I_controls(F)-J-Lstr.          (9)

The source deficits in (9) stay signed. A proposed payment must supply the
JS earmark AND pay Lstr and every source deficit from disjoint unspent parts
of the SAME original budget. Equations (7)--(8) do not discharge those bills.

For the packet's actual PHYSICAL children, use the already established B06-R2
identity, without adding any new reserve:

    D_K(F_v)= [D_K(F_v0)+D_K(F_v1)]/2 + K Inf_i(F_v)
                      -Delta T-Delta Lstr-Delta J.    (10)

Equation (5) identifies only the last term's DATA account. Both physical
child deficits in (10) remain signed. The source terms in (9) are an
ALTERNATIVE expansion of those same costs, not additional child slack.
In particular neither T nor frontier J is an independent donor merely
because it also appears in the sector representation. The exact local
condition is that the actual signed averaged child deficit plus K Inf_i
covers the full three-term decrement. Any JS earmark used here must be a
declared part of that SAME budget, disjoint from source/structural payments;
it cannot be added again to the physical child deficits. The theorem prices
only its specified signed JS component. Terminal physical deficits may be
expanded or retained, never added to their own expansion.

## 5. Two actual Boolean controls against invalid accounting

First, take a fair one-bit controller choosing between the two two-bit point
defects negative at 00 and 01, and multiply both by a common fresh character z.
Both root spectra are flat on the same four sets, so J_root=0. Reveal the data
bit that distinguishes 00 from 01: each physical child has one source a
character times z and the other constant times z, so J_child=1. The first data
debit is -1. Reveal the other original data bit: terminal source spectra are
all the common character, so J_terminal=0 and each next debit is +1.
The signed total is 0; the positive-part total is 1>J_root. All four sources
at the first exposure are nonconstant because of z. This is an actual Boolean
counterexample to clipping refunds, not a counterexample to (7) or to FEI.

Second, fix the declared non-flat three-label seven-bit fixture with positive
J_root and adjoin d unused physical controller coordinates. Query them and
stop. Every frontier node has the SAME J_root, every release is zero, and the
true remaining account is J_root. Summing newly issued accounts over the d+1
levels gives (d+1)J_root. The discrepancy is unbounded with d, while the
Boolean function and its H/I are unchanged by dummy extension. This directly
tests that transported child slack is not being counted repeatedly.

If controls and data are not fresh, even the sector premise fails: on one
sign variable x let L=0 at x=+1 and L=1 at x=-1, with g0=x and g1=-x.
The represented output is constant, but the proposed mixture of source
spectra is the nonempty character. It is not the actual marginal spectrum.

## 6. Exact remaining line

The author proof establishes (1)--(9) for the stated finite-label scope.
Independent review is requested from A028/A087/A094. The exact unpaid
universal step is to pay Lstr, all signed source deficits and one prescribed
inherited terminal-reference conversion from a SINGLE genuinely unused
original account, with (8)'s prior debits and both physical terminals retained.
No result here bounds that combined cost for arbitrary Boolean functions.
Full FEI remains OPEN.
