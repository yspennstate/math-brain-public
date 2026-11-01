# A single prepaid controller owner through unequal-depth surgery histories

Author proof; external review pending. Bits throughout. Full FEI remains OPEN.

## 1. Interface and one ORIGINAL payment

Consume A021-NONFLAT-INHERITED-REFERENCE-DATA-QUERY@3 at its stated scope:
g=-1 only at000, b=g tensor t, t>=2, delta=8^-t, F(v,z)=b(v)a(z),
and F=b elsewhere. DATA follows a fixed block-first order, pathwise depth
at most3floor(t/2)+2. Arbitrary CONTROL queries occur only on active DATA
cylinders. DATA depths and stopping can depend on control outcomes. Keep
its prescribed q_h, old0<=U<=t/64, original R_delta,a on active leaves,
frozen original-delta R on inactive leaves and ALL complete terminal costs.
The actual entropy-liability bank is

 B_H=4I_DATA,remaining+L_H-C_old-U,
 L_H=delta sum_active p_e H(a_e).

A021@3 proves B_H>=t/32 when t=2 and B_H>=t/16 when t>=3.
These are stronger estimates of the SAME account used in A022@8, not new
credits. Its proof and exact finite certificate retain their review status.

At the ORIGINAL controller root choose ANY normalized external law q0
and0<=sigma<=1/2. Set r0=(1-sigma)P_a+sigma q0. Thus r0>=P_a/2 and
D0=D(P_a||r0)<=log2(1/(1-sigma))<=1. Prepay epsilon=delta D0 ONCE
from the old unused bank. This is the entire additional original controller
CE liability; it is not supplied again at descendants. Uniform q0 is an
example, not a restriction of the theorem. No influence-priced controller
certificate is assumed or manufactured by smoothing.

Inherit r0 through actual CONTROL queries by the physical phase channel.
For each pair of parent Fourier amplitudes u,v, erase the queried frequency
bit and output physical bit b with probability (u+(-1)^b v)^2/[2(u^2+v^2)].
Use any normalized extension on zero-actual-mass pairs, e.g. fair b. Apply
this channel to BOTH actual spectrum and reference, retaining the reference
outcome normalizers. It pushes actual mass to half each actual child law.
The source KL chain rule gives A_node=D_parent-average D_child>=0,
including BOTH erasure and outcome KL. Inherit only; no new r0 is chosen.

For active e, write w_e=2^-d_e, eta_e=delta/w_e, and CONTROL reach p_e.
The active control cylinders partition the original controller cube even
at unequal DATA depths. Inactive branches do not query control coordinates.
The single original source owner obeys EXACTLY

 delta CE(P_a,r0)=K_H+delta sum_control p A_node+L_r,         (1)
 L_r=delta sum_active p_e CE(P_(a_e),r_e),
 K_H=delta sum_control p[H(a_parent)-average H(a_child)].

Equivalently L_r-L_H=delta sum_active p_e D_e and
D0=sum_control p A_node+sum_active p_e D_e. DATA queries leave(1)
unchanged. Every original entropy spend remains explicitly in K_H.

## 2. Actual terminal odds and the exact logarithmic refund

For any law P define M_eta(P)=(1-eta)point_empty+eta P.
At an active terminal the ACTUAL controller marginal is M_eta(P_e).
Use the NEW complete reference q_h tensor M_eta(r_e), with ACTUAL eta;
at inactive terminals use q_h tensor point_empty. DATA references stay as
prescribed. This is a genuine change of controller vacuum odds AND inherited
nonempty profile; it is not identified with free physical inheritance.

For finite D(P||r), data processing for the mixture channel has the exact
slack

 V_eta(P,r)=eta D(P||r)-D(M_eta(P)||M_eta(r))>=0.            (2)

Only the empty observed row erases the mixture selector. Writing p=P(0),
q=r(0), x=1-eta+eta p and y=1-eta+eta q, the logarithmic term is EXACTLY

 V_eta=eta p log2(p/q)-x log2(x/y)
      =x D(Bern(eta p/x)||Bern(eta q/y)).                  (3)

Use continuous zero conventions. Actual densities here are below1; the
formula also extends to eta=1 with zero slack. Nonempty-profile mismatch
itself has NO extra erasure refund. In particular p=q implies V_eta=0;
positive vacuum refund cannot be invented for an isovacuum shape change.

## 3. Same-bank comparison, every inactive cost retained

Let A_cal be the full, nonnegative calibration credit

 sum_active w_e p_e D(M_eta(P_e)||M_delta(P_e))
 +sum_inactive reach_h[-log2 R_frozen,h(empty)].

This second sum is generally strictly positive and is NOT dropped. It is
the exact complete controller CE released when the inactive reference
becomes point_empty. Define C_new as ALL terminal CE against the new
references. Since product-reference CE splits into DATA and CONTROL
marginals, direct subtraction gives

 B_r=4I_DATA,remaining+L_r-C_new-U,
 B_r-B_H=A_cal+sum_active w_e p_e V_eta(P_e,r_e).            (4)

The extra source liability is prepaid at the original root, so the genuine
remaining original account is Bstar=B_r-epsilon, NOT B_r with a fresh
supplier. Its EXACT identity is

 Bstar-B_H=A_cal+sum_active w_e p_e V_eta-epsilon.           (5)

Thus Bstar>=B_H-delta D0>=B_H-delta for EVERY allowed mixed cut,
using one original r0 inherited along the whole history. In particular

 t=2: Bstar>=1/16-1/64=3/64>26/576=13t/576;
 t>=3: Bstar>=t/16-8^-t>=13t/576.                         (6)

For the second inequality use8^-t<=1/512 and
(1/16-13/576)t=23t/576>=69/576>1/512. This covers all t analytically.
The old numerical reserve is unchanged; the smallest displayed surplus
above it is1/576 at t=2. Old U, frozen costs, all earlier signed spend and
both target/inherited terminal KLs remain. No root Jensen gain is added
again to A021's actual B_H.

For a strict actual vacuum-refund witness, take a two-bit literal, eta=1/64
and r=(P+uniform4)/2. Then P(empty)=0,r(empty)=1/8, and
V_eta=(63/64)log2(505/504)>0. For a bent two-bit controller, P is uniform;
choose an external q with empty atom1/4 while
changing only the nonempty profile. Then V_eta=0 although source and output
profile KL are strictly positive. Section5 supplies an explicit rational q.

## 4. Full signed history and owner eligibility

Let D_new=C_new-H_frontier. Keep DATA history increments
reach*(4Inf_i-DeltaH_F) and CONTROL history increments
delta p[CE_source,parent-average CE_source,child]-reach*DeltaH_F.
Call their accumulated sum E_r. Then, at EVERY physical frontier,

 Bstar+D_new+E_r=4I_DATA,root+delta H(a_root)-H(F_root)-U.   (7)

This follows directly from(1), influence partition and entropy telescoping.
The left keeps K_H and the extra source contraction delta sum p A_node
separately; its initial mismatch epsilon was paid once, not renewed.
Physical target-minus-inherited KL conversion is retained with actual
erasure/outcome refunds; (4) does not pay clipped positive raw reset costs.

If claiming the original controller owner has rate C, its necessary original
eligibility is CE(P_a,r0)+old_controller_booking<=C I(a), with no overlap
of already spent controller influence. This is NOT a consequence of(1)--(7).
The uniform external law actually obstructs this source-only certificate,
as Section5 proves. A fixed additive1 cannot be absorbed using a false
I(a)>=1 assertion; nonconstant point defects have influence tending to0.

There is a precise repair: preserve the ORIGINAL vacuum atom p=P_a(empty)
and smooth only the nonempty law, q0=(p,(1-p)nu), with ANY normalized nu.
At p=1 set q0=P_a. Then

 D0=(1-p)D(P_a(.|nonempty)||[(1-sigma)P_a(.|nonempty)+sigma nu])
    <=1-p=Var(a)<=I(a).                                   (8)

This charges at most ORIGINAL controller influence delta I(a), if that
influence is eligible and unspent; the proved same-bank handoff above
already pays it from DATA slack and does not spend it a second time.
Moreover an all-Boolean source certificate CE(P_a,r0)<=K I(a) for these
vacuum-calibrated references IMPLIES FEI with K; conversely FEI with C
implies this CE certificate with C+1, including constants. This equivalence
is just H<=CE=H+D0<=H+I using(8), not a proof of the missing supplier.

## 5. First unsupported line and a guard against circular supplier claims

An actual controller obstruction to UNIFORM full-spectrum smoothing is
a_m=-1 only at0 on m bits, m>=3. Put N=2^m. Then p0=(1-2/N)^2,
p_nonempty=4/N^2 and I(a_m)=2m/N. For r0=(P+uniform_N)/2,
r0(empty)<=(1+1/8)/2=9/16, p0>=9/16 and log2(16/9)>1/2.
Consequently CE(P,r0)>=9/32 for every m>=3, so CE/I diverges at
least as9*2^(m-6)/m. Meanwhile, with c=log2 e<3/2,

 H(a_m)<=[8m-8+4c]/N<8m/N=4I(a_m).

This uses phi(p0)<=c(1-p0)<=4c/N and the exact nonempty entropy
(N-1)(4/N^2)(2m-2). It refutes influence-priced UNIFORM-smoothed CE
suppliers even on an FEI-paid Boolean family, not FEI or the handoff.
Vacuum-calibrated nonempty-uniform smoothing equals P on this family,
so the artificial constant bill disappears exactly.

The explicit isovacuum guard uses bent a=(-1,1,1,1), P=uniform4,
q0=(1/4,1/8,1/4,3/8) and sigma=1/2, giving
r0=(1/4,3/16,1/4,5/16). Thus p=q=1/4, V_eta=0, while
D(P||r0)=(1/4)log2(16/15)>0. It rules out a claimed positive selector
refund for every nonempty profile mismatch, not the paid handoff.

First unsupported universal line: influence-price the ONE original
vacuum-calibrated controller CE owner without assuming FEI or allocating
its entropy again; by(8) this source-only route is FEI-equivalent.
Removing the DATA cap also remains open; unchanged-reference CE collapse
cannot be used to bypass all full terminal KLs. This stage pays the actual
compatible odds/profile handoff through arbitrary already admitted mixed
histories, not the universal supplier itself.
