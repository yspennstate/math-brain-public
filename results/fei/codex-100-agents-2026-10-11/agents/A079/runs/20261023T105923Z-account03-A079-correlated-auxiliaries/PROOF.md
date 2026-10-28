# Exact singleton-ghost payment in the zero-phase sector

Bits throughout. Let a take values in {-1,0,1} on physical controller bits,
b=1-a^2, and h be Boolean on independent seed bits. Use actual signed
G=a+sigma*b*h, sigma=+/-1. Put A=ahat,B=bhat,beta=E b^2,m=E h,r=m^2,
t=1-r,p=hhat^2. Supply a complete normalized source reference R with
R(empty)=r and finite CE(p,R). The coherent complete wrapper reference is

 Q(U,empty)=(A_U+sigma*m*B_U)^2;
 Q(U,T)=B_U^2 R(T), T nonempty.

It normalizes because sum AB=E(ab)=0. The source price and all earlier
history debits, if an influence-rate conclusion is wanted, are SUPPLIED.
No universal initial price is proved.

## 1. A different currency from A097's phase energy

Query actual seed coordinate i with hhat({i})=0. BOTH child means equal m.
Let rho=R({i}); this is reference-only singleton mass because p({i})=0.
If t>0, finite CE forces rho<t: otherwise R would put no mass on any
occupied nonempty coefficient other than the actually zero singleton.
Set theta=rho/t in [0,1). Define Rbar=M_i R and

 R0_child(empty)=r;
 R0_child(T)=t*Rbar(T)/(t-rho), T nonempty.                 (1)

This is the CURRENT inherited source marginal, then calibrated. Both
references are complete normalized laws. For t=0 the seed is constant,
R is the vacuum point law, rho=0, and no nonempty law or division is formed.
For beta=0 every source-tail charge below is zero.

Index each remaining frequency T by parent pair (T,T+i), with T!=empty.
Write p_b=p(T+b*i), q_b=R(T+b*i), w=p_0+p_1, and define

 D_* = sum_(T nonempty,w>0) w D((p_0,p_1)/w || (q_0,q_1)/(q_0+q_1)). (2)

Every occupied pair has positive reference mass by finite CE. Empty
unoccupied pairs contribute zero. All reference-only atoms inside q remain.
Then the EXACT physical erasure-plus-mean-terminal increment is

 B_i(G)+mean_tau CE(P_Gtau,C(a,b,h_tau,R0_child))-CE(P_G,Q)
      =-beta*D_*-beta*t*log2(1/(1-theta)).                 (3)

This stronger credit includes the full conditional occupancy KL of the
physical query, not merely a Pinsker estimate for a subsequent coarse reset.

## 2. Direct proof of the full identity

For fixed mean m, the signed-vacuum entropy terms in coherent CE are
identical before and after i. Expanding the nonempty terms therefore gives
CE_wrapper=c(a,b,sigma,m)+beta*CE_seed. The constant c need not be positive;
it is the same at both physical children. At the vacuum frequency fiber,
the true queried-singleton coefficient is zero. At every nonempty fiber,
both true masses carry the factor B_U^2, so conditional erasure is exactly
B_i(G)=beta*B_i(h). This derivation uses actual phases and d=0; it does not
extend that erasure scaling to an arbitrary biased tag collision.

The average of the actual child squared spectra is M_i p. Source vacuum
CE is unchanged, since (1) restores r and both true child vacua equal r.
For each nonempty pair the decrease in source CE is

 sum_b p_b log2((q_0+q_1)/q_b) + w log2(t/(t-rho)).

The first term is that pair's conditional entropy plus its weighted
conditional KL. Summing nonempty pairs yields B_i(h)+D_*; the empty pair
has true masses (r,0) and contributes no erasure. Nonempty true mass sums
to t. Multiplying by beta and subtracting the physical erasure proves (3).
Every terminal normalizer and the prior incoming CE appear in this equality.

## 3. Fund an actual new conditional-nonempty profile

Choose any normalized nonempty target S_tau separately at BOTH physical
children. Starting with the tail L of (1), prescribe

 M_tau=(1-lambda_tau)L+lambda_tau*S_tau,
 Rnew_tau=r*delta_empty+t*M_tau, 0<=lambda_tau<1.           (4)

Keep every actual signed controller-vacuum atom and use B_U^2 Rnew_tau(T)
for the complete nonempty reference. The exact extra terminal cost is
beta*t[D(p_tail_tau||M_tau)-D(p_tail_tau||L)]. Its likelihood-floor bound
is beta*t*log2(1/(1-lambda_tau)). Thus (3) and BOTH full terminal costs give

 increment <= -beta*D_*
   -beta*t[log2(1/(1-theta))-mean_tau log2(1/(1-lambda_tau))]. (5)

In particular ANY lambda_tau<=theta is paid without increasing the incoming
account. Lambda=theta/2 retains at least
beta*D_*+beta*t*log2((1-theta/2)/(1-theta)). This is strictly positive when
beta>0 and rho>0. This is a genuine conditional-nonempty profile change,
not merely vacuum calibration. Targets can have zeros or new ghost labels;
the positive old component guarantees support on actual occupied atoms.

The statement holds for EVERY zero-singleton query, including nonisospectral
ones. At an isospectral query, p_0*p_1=0 on every frequency pair, but D_*
need not vanish if the supplied reference has both occupancies. The ghost
credit in (3) still works when A097's entire nonempty-bin phase energy is0.
No amount is reissued: rho is read from the CURRENT reference and is
removed by its actual marginalization/calibration. Descendants must read
their changed references again. Finite-tree induction telescopes (3)--(5)
with physical reaches and both complete child CEs. Paid coherent controller
calibrations and ordinary no-reset continuations can be interleaved at their
existing admission. Previously executed source/tag/reset debits and old
nonconstant siblings remain. Any supplied original rate K is unchanged.

## 4. Actual Boolean sharpness, including the remaining zero-ghost boundary

Use original A079 mask beta=3/8 and h=x1*x2*x3. Query x1. Both actual
children are +/-x2*x3, hence nonconstant and isospectral. All singleton
coefficients and every u_T*v_T are zero: A097 phase energy x=0 EXACTLY.
Supply R=(1-rho)delta_{123}+rho*delta_{1}, 0<=rho<1. It is finite on
the actual spectrum and already calibrated at empty mass0. Its singleton
ghost is exactly rho. Here D_*=0. After the query (1) is delta_{23}.
Choose (4) with target delta_{2}. Both complete signed child references
have tail (1-lambda)delta_{23}+lambda*delta_{2}. The physical erasure is0,
and the EXACT full increment at EACH signed parent is

    (3/8)log2((1-rho)/(1-lambda)).                         (6)

Thus lambda=rho is paid with exact equality; lambda>rho has strictly
positive charge. This proves the worst-case ghost credit is sharp.
For rho=1/32, a genuine lambda=1/64 change is funded with retained release
(3/8)log2(63/62)>0. For rho=1/128 that SAME target incurs a positive cost;
at rho=0 it costs (3/8)log2(64/63)>0. Both full terminals and their actual
truth spectra/references are saved; no normalized non-Boolean surrogate
or FEI counterfamily is asserted.

## 5. Exact prepayment guard: creating the ghost is not free

Let Rbase be any calibrated finite-CE source with Rbase({i})=0, and let
the true singleton also be zero. Inject a new singleton ghost by

 Rtheta(empty)=r;
 Rtheta(T)=(1-theta)Rbase(T)+theta*t*1[T={i}], T nonempty.

Every occupied nonempty source atom is multiplied by1-theta. Consequently

 CE(p,Rtheta)-CE(p,Rbase)=t*log2(1/(1-theta)),

and coherent wrapper injection costs beta times this amount, EXACTLY the
ghost term in (3). Manufacturing reference-only mass to pay the next reset
is therefore advance payment, not a new Boolean phase-energy supplier.
Old profile debt cannot be hidden behind a reference-only label.

## First unsupported universal line

The supplied initial source CE remains influence-unpriced for an arbitrary
Boolean seed. In the residual local nullspace d=0, all bin phase energy0,
rho=0 and D_*=0, no refund exists; (6) gives an actual Boolean positive
conversion charge. The missing universal step is paying a NECESSARY
conversion there from an actual unused original source/influence surplus,
or proving the conversion can be avoided by an admissible construction.
There is no free singleton-ghost injection, arbitrary source optimization,
or renewed finite controller bank. The present probability identity is not
a new Booleanity admission inequality. Full FEI and universal C018/C019/
C020/C024 remain OPEN. New independent review and formal verification are
separate from the author's proof and exact finite certificates.
