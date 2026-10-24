# One data exposure after the complete paid unequal-mean query

All CE, KL and entropy use bits. Let e=2^-k, k>=2, h0=u and hk=(1-Ek)u+Ek,
where Ek=1[v=0] on k private bits. Supply Q0=(P0+delta_empty)/2 and
Qk=(Pk+delta_empty)/2, exact two-bit nonlinear mask reference Qs=Ps,
and the original q-frequency conditional lift Qh of average(Q0,Qk).
The actual activation is F(x,z,w)=1 when the binary physical gate x=0,
and F(x,z,w)=h(z)s(w) when x=1; all physical bits are uniform. The parent
core selects h0 or hk by q. The mask is -1 at one of four input points and
+1 at the other three, so its mean is 1/2 and its squared spectrum is flat.
The activation reference has data marginal (Qcore tensor Ps+delta_empty)/2,
lifted by its actual x-frequency conditional law. This is fixed before queries.

Consume A018 stage18's FULL first query: B=average_b(4I(hb)-cb)/2>1,
Tq=CE(F)-average CE(Fb)-4Inf_q(F)<1/4. For any old booking 0<=U<=1/8,
B-U-(Tq)_+>5/8. Both complete original Fb terminals remain. This differs from
A019 stage17's >3/4, which paid ONLY Lambda, not the full entropy/profile bill.

Now query one actual v bit in the q1 terminal. Keep q0 unchanged. Let Rcore
be the frequency marginal of the ORIGINAL Qk over this v bit. Both core
children receive this SAME Rcore, not fresh contaminated spectra. Their
functions are u and h_(k-1). Keep the same mask reference. Construct their
prescribed complete activation references by the original data-mixture rule
using Rcore and each child's actual x-frequency conditional.

These supplied references are finite: each child squared spectrum is at most
twice the folded parent spectrum pointwise (by (a+b)^2<=2(a^2+b^2)), whereas
Rcore is at least half that folded spectrum. Thus Rcore>=Pchild/4.
No positive child atom loses support, including k2's nonconstant h1 terminal.

For clarity retain also the literally inherited activation reference Ract,
obtained by marginalizing the original Q(F1) over v. It and each prescribed
child reference have the SAME data marginal (Rcore tensor Ps+delta_empty)/2.
The inherited-to-prescribed conversion gain is exactly
K_b=CE(P_Fchild,Ract)-CE(P_Fchild,Q_Fchild)
   =sum_data P_Fchild(data) KL(P_Fchild(x|data)||Ract(x|data))>=0.
Hence the FULL new query decrement is
Tv=CE(F1)-average CE(F1|v)
  =[CE(F1)-average CE(P_Fchild,Ract)]+average K_b.
The positive K_b terms MUST be included; calling the cheaper child code a
free refund and deleting them from this decrement would change the ledger.

The full decrement satisfies Tv=DeltaH_F1+KL_parent-average KL_child
<=DeltaH_F1+KL_parent. The original Qk>=Pk/2 gives core KL<=1.
The original activation mixture has KL_parent<=core KL/2<=1/2 by
the physical-label log-sum identity. This bound concerns the actual incoming
reference before the v query, not a newly supplied exact-spectrum reference.

It remains to bound the actual entropy decrement uniformly. Put
f(e)=eta((1-e)^2), eta(z)=-z log2(z), eta(0)=0, and
Hk=f(e)+4k e-2k e^2. Indeed the u singleton coefficient is 1-e;
the other 2^(k+1)-1 nonzero coefficients have absolute value e, by
expanding (1-Ek)u+Ek in characters. Thus this is the full actual entropy.
Then exactly
DeltaH_core/2=2e+[f(e)-f(2e)/2]/2+(k-2)e^2.
On [0,1/2], f''(z)=-2[3+2ln(1-z)]/ln2 is negative and |f''|<9:
ln2>2/3 follows from the first positive term of the atanh series, and ln2<1.
The midpoint Jensen gap therefore gives f(e)-f(2e)/2<(9/2)e^2,
so DeltaH_core/2<2e+(k+1/4)e^2<=41/64 for every k>=2.
The last expression decreases with integer k: both 2^-k and (k+1/4)4^-k do.

Define phi(b)=Psi(b/2), using the earlier exact activation profile. The new
curvature is C(e)=phi(e)-[phi(0)+phi(2e)]/2. Since phi is concave,
C'(e)=phi'(e)-phi'(2e)>=0 for e>0. Continuity handles e=0.
Consequently C(e)<=C(1/4)<1/16. The final strict sign is a single exact
rational-prime-log comparison, certified in out/CERTIFICATE.json. This is
a continuum argument followed by one exact sign, not an extrapolated sweep.
Therefore DeltaH_F1=DeltaH_core/2+C(e)<45/64 and Tv<77/64.

The q1 terminal has original physical reach1/2. Book the COMPLETE positive
new decrement, including inherited conversion and BOTH new child costs,
as (Tv)_+/2<77/128. This deliberately leaves the new physical v influence
unspent; there is no second claim against it. The SAME original bank obeys

 B-U-(Tq)_+-(Tv)_+/2 > 5/8-77/128 = 3/128.

The q0 sibling and its complete reference are retained throughout. The
original old debit U and first FULL query debit remain booked. The statement
is uniform in k>=2 and in the chosen v coordinate. If v is also queried on
q0, it is a true/reference dummy and its decrement is exactly0.

The first unsupported universal line is another interacting exposure from
the already diminished account. The surviving child references are inherited
marginals of Qk, not (Pchild+delta_empty)/2; their next KL price cannot be
declared <=1/2 by renewing the previous incoming-reference assumption.
Full FEI remains OPEN. Independent review of this continuation is pending.
