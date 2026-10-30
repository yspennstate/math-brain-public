# Unequal-depth stopping cuts with the original controller liability

Author derivation with the exact finite certificate of Section5 checked by two
implementations; external review pending. Entropies are bits. FEI remains OPEN.

## 1. Scope and actual account

Let g on three uniform bits be -1 at000 and +1 elsewhere, b=g tensor t,
t>=2, delta=8^-t, and F=b(x) except F(v,z)=b(v)a(z), with arbitrary
independent Boolean controller a. Fix a block-first DATA order. On every
physical path DATA queries follow that order, but can stop at ANY depth
at most D=3floor(t/2)+2. CONTROL queries can be arbitrary and adaptive,
but occur only while the current DATA cylinder contains v. No coordinate
is queried twice along a path. Any finite mixed tree satisfying these rules
is allowed; DATA depth may depend on controller outcomes, and DATA queries
may occur on one leaf alone. This extends A022@8's synchronized interface.

Use the SAME prescribed DATA references q_h: untouched blocks have
(9,1,...,1)/16; after one local bit use uniform4 when its value is0,
otherwise (13,1,1,1)/16; after two bits put15/16 at the restricted seed's
character/constant frequency and1/16 at its other frequency. Completed
blocks contribute1. Always use ORIGINAL controller density delta. At an
active leaf use R_delta,a_e=(1-delta)point_empty+delta P_(a_e). Freeze
that controller reference when a DATA outcome leaves the active cylinder;
later inactive DATA queries modify only q. Keep EVERY terminal reference
q_h tensor R, including inactive costs and both child KLs.

For active leaf e let p_e be its CONTROL cube reach and w_e=2^-d_e its
DATA reach, so eta_e=delta/w_e. The active control cylinders partition
the original controller cube: sum_e p_e=1, even at unequal data depths.
There is a unique DATA path containing v for each fixed controller input.
Use only the ORIGINAL supplied entropy earmark
L=delta sum_active p_e H(a_e). Its signed spend K satisfies
K+L=delta H(a_root) exactly. No new controller supplier is admitted.

The actual global account is B=4I_DATA,remaining+L-C-U, with complete
frontier CE C and the SAME old0<=U<=t/64. We prove B>=t/32 for t=2,
and B>=t/16 for t>=3. In particular B>=13t/576 throughout the enlarged
history class. Larger lower bounds below use the same original account,
not a fresh descendant reserve or the old Gamma added twice.

## 2. Uniform complete controller bill

For s=Ea, r_delta=1-delta+delta s^2 and
G_delta(s)=H(R_delta,a)-delta H(a), A021@2's exact reconstruction gives

 w[CE(R_eta,a,R_delta,a)-eta H(a)]
      =J_delta,w(s)=G_delta(s)+(1-w)log2 r_delta(s).

Here the actual density is eta=delta/w and the reference keeps delta.
The elementary mixture entropy bound gives G<=h2(delta): introduce the
Bernoulli selector for the two reference components and use
H(Y)<=H(selector,Y)=h2(delta)+delta H(a). No concavity assumption or
earlier numerical admission is needed. Since log r<=0, J<=h2(delta).
Thus all ACTIVE terminal cross overheads sum to at most
h2(delta) sum p_e=h2(delta). Each inactive terminal has actual controller
spectrum point_empty, so its COMPLETE controller cost is -log2 r_delta
at its frozen mean, at most -log2(1-delta). Their physical reaches sum
to at most1. Therefore, without dropping inactive costs,

           C_CONTROL-L <= h2(delta)-log2(1-delta)
                        < delta(3t+4).                     (1)

For the last bound use log2(1/delta)=3t and c=log2 e<3/2:
h2(delta)<=delta(3t+c), and -log2(1-delta)<=c delta/(1-delta).
Since delta<=1/64, c+c/(1-delta)<3/2+32/21<4.
The estimate charges this complete ORIGINAL bill once, not at every node.

## 3. DATA account for t>=3

At a DATA terminal h let K_h=4I(b_h)-CE(P_(b_h),q_h), where b_h is
the UNEDITED restricted seed. Put beta=4I(g)-H(g)=-1+(9/8)log2 3>3/4.
If n untouched whole blocks remain, the one possible partial block has
seed bank bounded below by -1/3: its four possible types have values
2, log2(13)-4, log2(15), or log2(15)-4. This uses13^3>2^11 and
15^3>2^11. Completed blocks contribute0. Therefore

                   K_h >= (3/4)n-1/3.                     (2)

The depth cap implies n>=ceil(t/2)-1 at every terminal, regardless of
its controller reach or data outcomes.

For a currently active terminal, its DATA spectral marginal is the
mixture of the unedited and point-edited seed spectra with bias alpha_e.
An exact local computation gives

 4I_DATA(F_h)-CE_DATA(F_h,q_h)=K_h-eta_e alpha_e X_h.         (3)

For a product seed/reference, X is additive over remaining local blocks.
To verify this, write the Fourier change under a point flip as
P_edit(S)-P_seed(S)=4 eta[eta-b_h(v)bhat_h(S)chi_S(v)].
The DATA CE change is4 eta alpha J_q, where
J_q=sum_S[eta-b_h(v)bhat_h(S)chi_S(v)] log2(1/q(S));
the DATA influence change is2 eta alpha s_b, where
s_b=sum_remaining_i b_h(v)b_h(v^i). Thus X=4J_q-8s_b.
Expanding log of the product q and summing the other Fourier labels
establishes block additivity directly; no independence of spectral
corrections is assumed.

For an untouched g block the four vertex types give X=24-7log2 3,
5log2 3-8, or5log2 3-24; hence X<=118/9 from3^9>2^14.
For the partial-block types, respectively, X<=16,
3log2 13-16<0, 2log2 15+8<16, or2log2 15-8<0.
Consequently X_h<=(118/9)t+16. Multiplication by physical reach
w_e p_e uses w_e eta_e=delta, so all edit charges together are at
most delta[(118/9)t+16] sum p_e alpha_e<=delta[(118/9)t+16].

Combining(1)--(3) and old U gives the ACTUAL bank bound

 B >= (3/4)(ceil(t/2)-1)-1/3
                  -delta[(145/9)t+20]-t/64.               (4)

For t=3, (4) is121/512>3/16. For t>=4, delta[(145/9)t+20]
<=190t/(9*4096)<t/128 (24320<36864). Thus

 B >=45t/128-13/12 >=t/16,

because37t/128>=37/32>13/12. This proves the unbounded-parameter passage;
testing finitely many t is neither needed nor used.

## 4. Conditioning lemma for ALL controller dimensions

For t=2 improve the DATA bound instead of the controller bill. Fix the
ENTIRE original controller assignment z. Its responses make the physical
mixed tree a deterministic DATA stopping tree through depth5, after
contracting deterministic control nodes. Its DATA function is exactly
b if a(z)=+1 or the actual one-point edited b if a(z)=-1. Its reference
q_h is a function only of its DATA prefix. For each terminal the DATA
spectral marginal equals the average over remaining z of the conditional
DATA spectra, by Parseval. Physical DATA influences have the same
conditional averaging identity. Therefore the actual global DATA bank
is the average over z of these deterministic DATA stopping-tree banks.
This remains true when the stopping rule depends on the controller's
values or previously observed data. Hence a certificate for EVERY such
DATA cut of b and its64 actual single-vertex edits covers controllers
of EVERY finite dimension, without enumerating or bounding H(a).

## 5. Exact finite certificate, not extrapolation

For each of the65 actual six-bit functions, at each prefix(d,h),d<=5,
let k(d,h)=4I(f restricted h)-CE(P_(f restricted h),q_h). The minimum
over all allowed DATA stopping cuts has the exact finite Bellman rule

 V(5,h)=k(5,h),
 V(d,h)=min(k(d,h),[V(d+1,h)+V(d+1,h+2^d)]/2).

This recurrence exhausts the two possibilities at each node: stop or
query the next fixed coordinate. out/BELLMAN.json establishes
V(0,0)>=1/4 for ALL65 functions (4095 nodes), using exact Fourier
spectra, physical edges and rigorously decided rational-log comparisons.
out/INDEPENDENT.json replays EVERY node with direct character sums and
separate48-term outward rational log intervals, importing no production
helper. Both executions PASS. These finite instances exhaust the stated
t=2 exceptions; Section3 separately proves the all-t passage.
Together with(1), this certificate gives
B>=1/4-10/64-2/64=1/16=t/32>13t/576.
Relabelling symmetric blocks and their bits covers any fixed block-first
order; all vertices remain included, with no omitted orbit hypothesis.

## 6. Full KL and signed history; what remains

Every terminal D=C-H is retained, and the old cumulative signed account
E uses DATA increment reach*(4Inf_i-DeltaH_F) and CONTROL increment
delta p_e DeltaH_a-reach*DeltaH_F. Directly from C=H+D and the ORIGINAL
source-entropy spend, B+D+E=B_initial+D_initial at every frontier. This
identity is unaffected by unequal data depth. If tracking an actual
phase-inherited reference, the net target conversion remains average
D_target-D_parent after erasure and outcome refunds; no raw clipped
positive reset charge is assumed paid separately. Existing Jensen gains
remain in this actual account; none is renewed or added a second time.

The remaining universal line is removal of the source/depth restrictions:
the arbitrary controller's ORIGINAL entropy delta H(a) is supplied,
not influence-priced, and the DATA depth cap is essential to this bank
bound. The known final unchanged-R CE-only collapse obstruction prevents
asserting a nonnegative CE bank through all data queries without terminal
KL refunds. A universal extension must transport the original controller
liability and BOTH terminal debts to a compatible descendant owner; simply
charging another fresh entropy supplier would be circular. No FEI constant
or counterfamily is claimed here.
