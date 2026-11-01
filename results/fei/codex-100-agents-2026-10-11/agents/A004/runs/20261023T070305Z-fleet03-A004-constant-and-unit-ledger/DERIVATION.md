# Occupancy and marginal discrepancy in the isospectral sector

Author proof; independent review pending. All logs, entropies, KL and CE
are in bits. All cubes are finite and uniform, all functions in the theorem
are Boolean signs, and influences, when mentioned, are physical flip
influences. Full FEI remains OPEN. This theorem consumes a SUPPLIED finite
source; it supplies no new initial influence price.

## 1. Independent reconstruction of A003's new refund

For G=a+sigma*b*h on disjoint controller and seed cubes, a in {-1,0,1},
b=1-a^2, put A=ahat, B=bhat, beta=sum B^2, m=Eh. Supply normalized R with
R(0)=m^2 and finite CE(hhat^2,R). The coherent reference is

    Q(U,0)=(A_U+sigma*m*B_U)^2,
    Q(U,T)=B_U^2 R(T), T!=0.

It normalizes because sum A^2=1-beta and sum AB=E(ab)=0. At a seed query j,
let d=hhat({j}), r=R({j}), delta=r-d^2. In the partition into individual
controller/vacuum atoms and one whole nonempty tail, the two true child
laws v_tau and COMMON inherited reference q obey

    mean(v_tau)(U)-q(U)=-delta B_U^2,
    mean(v_tau)(tail)-q(tail)=beta delta,
    (v_+-v_-)(U)/2=2d B_U(sigma A_U+m B_U),
    (v_+-v_-)(tail)/2=-2 beta m d.

Thus mean ||v_tau-q||_2^2 equals

    4d^2 [sum B_U^2(sigma A_U+m B_U)^2+beta^2 m^2]
      +delta^2 [sum B_U^4+beta^2].                         (1)

Set C=sum A^2 B^2, D=sum AB^3, E4=sum B^4 and
Gamma=C-D^2/E4 when E4>0, else 0. Completing the square gives
sum B^2(sigma A+mB)^2 >=Gamma. Pinsker in bits therefore gives mean coarse
KL >=2x/ln2, x=Gamma*d^2+(E4+beta^2)*delta^2/4. Restoring these coarse
blocks reduces CE by that KL exactly. Mixing the current conditional tail
with any prescribed target at epsilon=x/(t+x) costs at most
t log2(1+x/t)<=x/ln2. Together with the distinct conditional occupancy KL
this proves A003's stated transaction unchanged. No source repair is made.
For A079's controller E4=21/512, beta=3/8, Gamma=9/3584 and the discrepancy
coefficient is (E4+beta^2)/4=93/2048. These two coefficients multiply
different squared quantities. This is independent acceptance of the new
calculation, not acceptance of any unproved initial supplier.

Pinsker used throughout follows by grouping {p>q}, log-sum, and the binary
KL second derivative 1/[p(1-p)ln2]>=4/ln2; integrate from the equal-law
minimum. Thus D_2(p||q)>=||p-q||_1^2/(2ln2). The Euclidean version is weaker.
No numerical estimate of ln2 is needed in this proof.

## 2. New target: a fixed reset in the double-null, isospectral sector

Keep the setup above and assume beta>0, a0=1-m^2>0, and at ONE physical
seed query j assume

    d=0, R({j})=0, and hhat(T) hhat(T+j)=0 for every T not containing j.

The last condition is exactly equality of both restricted seed spectral
laws: P_+=P_-=pbar, where p=hhat^2 and pbar=M_j p. Write rbar=M_j R.
Both vacuum masses equal m^2. On remaining nonempty frequencies define

    pi(T)=pbar(T)/a0, M(T)=rbar(T)/a0,
    delta0=TV(pi,M)=(1/2)sum |pi-M|,
    W=sum_{T:pbar(T)>0} pbar(T)
          [p(T+j)/pbar(T)-R(T+j)/rbar(T)]^2,
    eta=delta0^2+W/a0.                                    (2)

All quantities are rational for rational R. Finiteness gives rbar(T)>0
whenever pbar(T)>0; omitted zero-actual fibers contribute zero. The empty
fiber contributes zero because both singleton masses are zero.
Isospectrality also forces deterministic actual occupancy in every fiber,
so B_j(h)=B_j(G)=0. This stage extracts already supplied reference mismatch;
it does not discover new entropy erasure or a fresh physical influence bank.

The query's actual conditional occupancy refund is EXACTLY

    rho=beta sum_T pbar(T)
           D_2(Ber(p(T+j)/pbar(T)) || Ber(R(T+j)/rbar(T)))
        >=2 beta W/ln2.                                  (3)

Indeed, on every nonempty seed fiber the full actual/reference laws have
the common controller factor B_U^2, and the empty fiber has deterministic
absent-j occupancy. Sum over U to get beta. Binary Pinsker proves the bound.
No child calibration refund or ancestor reserve is included in rho.

Choose the SAME two nonempty bins for both physical outcomes:

    Wplus={T!=0: pi(T)>M(T)}, Wminus=the complement.

Calibrate the inherited reference on each (U,Wplus), (U,Wminus), preserving
its conditional law inside each bin, and preserve the true individual
vacuum atoms. Explicitly the new normalized seed reference is

    Rcal(0)=m^2,
    Rcal(T)=a0*pi(Wbin)*M(T)/M(Wbin) for T in an occupied bin.

A zero-actual bin receives zero. A positive-actual bin has positive
reference mass, so no occupied denominator vanishes. This is a genuine
nonempty-profile calibration when delta0>0. Its CE refund on EACH child is

    k=beta*a0*D_2((pi(Wplus),pi(Wminus)) ||
                         (M(Wplus),M(Wminus)))
       >=2 beta*a0*delta0^2/ln2.                          (4)

The equality is the normalized block-calibration identity, including
removed reference-only mass. The difference of the plus-bin probabilities
is exactly delta0. An empty plus-bin when delta0=0 simply gives k=0.

Now on EACH child mix the CURRENT calibrated nonempty tail with ANY
prescribed normalized nonempty target S_tau. The true wrapper tail mass
is t=beta*a0 on BOTH children. At epsilon=eta/(1+eta) the signed CE cost z_tau
obeys z_tau<=t log2(1+eta)<=t eta/ln2. Thus the complete local transaction is

    B_j(G)+mean CE(P_child,Qnew_child)-CE(P_G,Q)
        =-rho-k+mean z_tau <=-t eta/ln2.                  (5)

More concretely, a prescribed FIXED strength epsilon=1/64 is paid with
the SAME retained bound -t eta/ln2 whenever eta>=1/63, because
log2(64/63)<=1/(63 ln2)<=eta/ln2. This is an explicit sufficient condition
for a fixed conversion, not just existence of an arbitrarily small refresh.
Targets may contain zeros or introduce reference-only labels; epsilon<1
keeps support on every actually occupied atom. If no nonempty label remains
the hypotheses a0>0 cannot hold. beta=0 and a0=0 use their explicit zero-tail
references and receive no strict positive authorization.

## 3. Exact nullspace and two orthogonal witnesses

Under this sector's hypotheses eta=0 if and only if R=p. In one direction
this is immediate. In the other, delta0=0 gives rbar=pbar including vacuum;
W=0 then gives equality of the two conditional occupancies in every
positive fiber, while equal zero marginals force no extra reference mass.
The full seed laws therefore agree atom by atom. This closes the
reference-mismatch part of the isospectral sector for supplied sources;
exact-source isospectral queries remain a real zero-refund boundary.

Take h=parity3, query physical seed bit0, and beta=3/8 from A079's controller.
All actual seed mass is at mask7; d=R({0})=m=0. With
R=(delta7+delta6)/2, inherited seed marginals are already exact, so delta0=0,
W=1/4, eta=1/4. Only occupancy pays: rho=3/8 and k=0.
With R=(delta7+delta3)/2, occupancy matches exactly, so W=0, delta0=1/2,
eta=1/4. Only two-bin calibration pays: rho=0 and k=3/8.
In both cases the calibrated child source is the true parity2 point law.
A fixed1/64 mixture toward a different nonempty point has positive cost
(3/8)log2(64/63). The complete increment is

    -(3/8)+(3/8)log2(64/63) < -93/256,

using 64^32<2*63^32. Both physical children, including opposite signs, have
been retained. With the exact seed reference R=delta7 instead, eta=rho=k=0
and the SAME target mixture costs +(3/8)log2(64/63)>0. The criterion must
refuse that transaction. This is a reference-payment obstruction, not FEI.

## 4. Same owner, iteration, units and the first unsupported line

For any normalized finite reference, the physical chain is
CE(P,Q)=B_j(P)+mean CE(P_child,M_j Q)+rho. A block calibration changes CE by
minus the KL of its block masses. These two identities prove (5) without
omitting empty atoms or adding a new H/I allowance. Multiplying by the
node's physical reach preserves every old query debit, old source charge
and complementary terminal. Any finite adaptive sequence of admissible
transactions telescopes in the ORIGINAL account, recomputing current R,
eta and controller factors at every node; it cannot reissue an old refund.
Mixed coherent controller steps may use the already paid A079 block
restoration, while ordinary steps keep complete reference marginals.

For sign f, p=hat f^2 has total mass1 and influence I_j=sum_{S:j in S}p(S).
Nonempty H_+=sum_{S!=0}p(S)log2(1/p(S)) is unnormalized; full H=H_++eta_ent(m^2).
Normalized nonempty conditional entropy is a different quantity. An
indicator (1+f)/2 has nonempty Fourier coefficients hat f/2 and energy
I_j/4; a flip-probability definition of influence for that indicator still
equals I_j. Natural-log versions multiply all information quantities by
ln2; the factors 1/ln2 above must then disappear. No directional influence
or normalized indicator entropy has been substituted for these units.
Constants, dictators, parity and nearly constant endpoints are tested in
the separate exact checker; beta=0/a0=0 supply zero strict slack.

First unsupported universal line: arbitrary Boolean roots still have no
influence-priced initial reference with enough admissible surplus; eta
can be arbitrarily small and is exactly zero at an exact-source isospectral
query. No uniform positive reset strength can be charged to every physical
influence by this argument. The next target is a NECESSARY prescribed
conversion after actual paid history in that matched nullspace, from its
actual unused original surplus, not another fixed-bank calibration cycle.
