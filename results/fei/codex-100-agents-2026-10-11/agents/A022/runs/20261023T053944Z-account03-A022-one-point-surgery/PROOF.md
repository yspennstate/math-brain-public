# Synchronized DATA rounds interleaved with active-only CONTROL

Author derivation; independent-person review pending. Entropies are bits. FEI remains OPEN.

## 1. Exact statement and ownership

Use A022 ledger@7: b=g tensor t, g=-1 only at000, t>=2,
F(x,z)=b(x) times a(z) at x=v and b(x) elsewhere; delta=8^-t.
Fix a block-first data order, the positive partial-block references q_h of
that version, original controller density delta, and old 0<=U<=t/64.
Write Bpure_d for its original no-controller-query bank at depth d.
It is at least13t/576 for d<=3floor(t/2)+2.

Maintain a physical frontier in synchronized DATA rounds: every leaf has
exactly the same data prefix depth d. Between rounds execute any finite
adaptive controller tree ONLY on leaves whose data cylinder contains v.
Stopping and next controller coordinate may depend on previous outcomes;
no coordinate is queried twice along a path. Then query the next fixed
DATA coordinate on EVERY frontier leaf, including every inactive sibling.
Only data depth d within the paid range is claimed. Arbitrary unequal
data-depth stopping cuts are not included.

An active leaf e has controller cube reach p_e, current restricted a_e,
data reach w=2^-d, and full physical reach w p_e. Its complete reference
is q_h tensor R_delta,a_e, R_delta,a=(1-delta)point_empty+delta P_a.
On leaving the active cylinder at a DATA split, freeze its current
controller reference; never replace it with the later active reference.
Every later DATA conversion changes only q_h. Inactive leaves and their
complete CE/KL are retained, even when their actual controller is unused.
Controller rows with zero reference have zero actual mass.

The SAME original source entropy earmark has remaining value
L_d=delta sum_active p_e H(a_e). Its exact signed spend K obeys
K+L_d=delta H(a_root). Define C as complete frontier CE, D=C-H,
I as average remaining DATA influence, and B=4I+L_d-C-U.

## 2. Controller step, reconstructed from A021@2

Put phi(u)=-u log2(u), r(s)=1-delta+delta s^2,
G(s)=phi(r(s))-delta phi(s^2)+delta(1-s^2)log2(1/delta),
J_w(s)=G(s)+(1-w)log2 r(s), continuously at zero.
The actual active-leaf controller marginal uses eta=delta/w, whereas
the prescribed reference uses ORIGINAL delta. Direct cross-entropy gives

 w[CE(R_eta,a,R_delta,a)-eta H(a)]=J_w(Ea).

Remaining DATA influence and DATA CE against fixed q_h are affine in
alpha=(1-Ea)/2. For a physical controller split s=(s0+s1)/2,
the GLOBAL bank gain is exactly p_e gamma_w, where

 gamma_w=J_w(s)-[J_w(s0)+J_w(s1)]/2.                         (1)

This is not multiplied by w a second time. Inactive costs cancel because
they are unchanged, not because they vanish. For delta<=1/64, J_w is
concave uniformly over0<w<=1: writing c=1/ln2 and
u=(1-delta)/(delta s^2)>=63 gives
G''=-2delta c[ln(1+u)-2u/(1+u)]<-4delta c,
(log2 r)''<=2delta c/(1-delta)<=2delta c*64/63.
Since ln64>4 (ln2>2/3 by its positive atanh series), J_w''<0
off zero. J_w' extends continuously at zero, so concavity holds throughout.
Thus gamma_w>=0. This independently reconstructs the relevant scalar
and controller transaction, not the entire A021 review chain.

## 3. The next DATA transaction, including frozen inactive references

At a DATA split, the same controller reference is passed to BOTH physical
outcomes. Parseval says the average child controller spectral marginal is
the parent marginal: deleting one data Fourier bit merges its two squared
coefficient rows. Consequently complete controller CE is unchanged IN
EXPECTATION, even when its reference differs between frontier leaves.
The remaining source earmark L_d also stays unchanged: the unique active
child has half the data reach and twice the conditional point density.
The ORIGINAL multiplier remains delta p_e, not a new conditional density.

Let ell_d(s) denote the no-controller baseline bank loss at this DATA
round if the root controller has mean s. DATA CE and remaining influence
are affine in alpha: the physical data spectrum is the mixture of the
unedited and edited data spectra, obtained by averaging actual z values.
The DATA cost is independent of the shape or entropy of the controller.
The active controller leaves partition the ORIGINAL controller cube,
so sum_active p_e=1 and sum_active p_e s_e=s_root. Inactive DATA
branches have exactly the unedited function and prescribed q_h; their
controller partition changes neither DATA CE nor DATA influence. Hence

 B_after-B_before = -ell_d(s_root)
                  = Bpure_(d+1)-Bpure_d.                  (2)

One can verify (2) directly by writing DATA CE and influence as their
unedited values plus the signed local edit correction, whose coefficient
is delta sum_active p_e alpha_e=delta alpha_root. All inactive DATA
queries are necessary for this synchronized statement. Controller CE
does not enter ell_d; it has just been proved conserved, not reset.

## 4. Exact mixed-history invariant and the numerical corollary

Start at any admitted pure DATA frontier d0, then interleave the two
transactions above. If Gamma is the sum of p_e gamma_w over every
controller node actually executed, induction on the physical operations
using(1),(2) yields the EXACT identity

             B_frontier = Bpure_d + Gamma.                (3)

Every original controller query contributes once, and its contribution
remains in Gamma after later DATA queries. There is no fresh source
admission, restoration of U, or replacement of the original mean.
Thus B>=13t/576 after every synchronized round and after every intervening
active-only controller query in the admitted DATA range, for arbitrary
controller dimension and all finite allowed schedules. This closes the
next DATA query requested by A021@2 and permits repeating this interleaving.

For local entropy decrement DeltaH_F and local controller decrement
DeltaH_a, retain signed history increments
 DATA: physical_reach*(4 Inf_data-DeltaH_F),
 CONTROL: delta p_e DeltaH_a - physical_reach*DeltaH_F.
Let E be their cumulative sum. In both operations,

                    B+D+E = B_initial+D_initial.         (4)

Here D is the average of EVERY complete terminal KL, including BOTH
outcomes and inactive siblings. Equation(4) follows from D=C-H and
the source-spend identity; it does not claim local DeltaH_F<=4Inf.
If comparing a prescribed reference with a phase-inherited one, its net
signed conversion is average D_target-D_parent, after the actual erasure
and outcome refunds. Raw clipped positive reset costs are not paid by(3).

## First unsupported universal line

An outcome-dependent DATA stopping depth breaks the synchronized affine
comparison in(2); no same-reserve bound is proved here for that change.
Likewise the original controller entropy delta H(a_root) is supplied, not
bounded by controller influence. Full all-dimensional FEI still needs that
source admission and a general terminal/history account; the already
known all-DATA CE-only collapse obstruction retains its scope.
