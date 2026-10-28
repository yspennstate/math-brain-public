# Source-reference histories lift through an unqueried physical address

All entropies and reference costs are in bits. All physical inputs are
independent and uniform. For any Boolean seed h(x), keep A079's displayed
four-bit rows a(u), b(u)=1-a(u)^2 and F_h=a+zbh. Only the u-controller
coordinates and seed coordinates may be queried in this theorem. The
physical address z remains unqueried at every node. Seed biases are arbitrary.

## 1. Actual child normalizers and a complete inherited reference

After any physical controller restriction s, write a_s,b_s for the actual
restricted rows, and alpha_s=E a_s^2, beta_s=E b_s^2. They satisfy
alpha_s+beta_s=1, including zero endpoints. Define the normalized tagged
structural law

  P_s(0,U)=ahat_s(U)^2,   P_s(1,U)=bhat_s(U)^2.

Its Shannon entropy is k_s and its physical mean frequency degree, counting
z and the remaining u coordinates, is j_s. For a source reference R on the
CURRENT seed-frequency cube, assume R is a probability law positive wherever
ph= hhat^2 is positive. Define the complete wrapper reference by

  Q_(s,R)(0,U,T)=P_s(0,U) 1{T=empty},
  Q_(s,R)(1,U,T)=P_s(1,U) R(T).

This is normalized exactly, not up to a discarded factor. The corresponding
true law has ph in place of R. Distinct physical z-frequency labels separate
the two sectors even when h is biased, so their support is disjoint. Consequently

  CE(F_h|s,Q_(s,R))=k_s+beta_s CE(h,R),
  H(F_h|s)=k_s+beta_s H(h),
  I(F_h|s)=j_s+beta_s I(h).

Every source reference-only atom is retained. Terms with zero true mass
contribute zero; structural zeros remain reference zeros in that sector.
No division by alpha_s or beta_s is needed at a zero endpoint. If a normalized
row presentation is wanted, its normalizers are exactly alpha_s,beta_s.

## 2. One active seed query: exact debit, with both full terminals

Let i be a remaining physical seed coordinate, h_+,h_- its two actual Boolean
restrictions, and R_+,R_- any specified normalized child references of finite
cross entropy. Write B_i for spectral conditional erasure, not the full entropy
decrement. Conditioning on the other spectral coordinates, including z,
separates the a-sector (seed frequencies empty) and the b-sector. Therefore

  Inf_i(F_h|s)=beta_s Inf_i(h),
  B_i(F_h|s)=beta_s B_i(h).

The exact source reset increment

  d=B_i(h)+[CE(h_+,R_+)+CE(h_-,R_-)]/2-CE(h,R)

lifts without alteration except its actual probability:

  B_i(F_h|s)+[CE(F_(h_+)|s,Q_(s,R_+))
                +CE(F_(h_-)|s,Q_(s,R_-))]/2
       -CE(F_h|s,Q_(s,R)) = beta_s d.

The structural entropy k_s cancels exactly. The two source terminal costs
remain distinct; neither is replaced by its average before it enters the
equation. If a source account pays d, the wrapper spends beta_s times that
same source account. If d is unpaid, this identity does not pay it.

## 3. Controller query: seed reserve conserved, actual JS released

At a controller query u_i the two children have their actual restricted
rows and normalizers. Physical conditional expectation gives

  (beta_(s,+)+beta_(s,-))/2=beta_s.

Thus the seed reference and its unspent account are conserved in expectation.
The source reference R is unchanged by this controller query. The controller
erasure is exactly the erasure of P_s in the queried structural frequency.
Let J_(s,i) be the Jensen--Shannon divergence between the two ACTUAL structural
child laws, embedded in the common residual structural-frequency cube.
The physical restriction entropy identity gives

  k_s-[k_(s,+)+k_(s,-)]/2 = B_(s,i)+J_(s,i),  J_(s,i)>=0.

Hence the complete wrapper reference obeys

  B_(s,i)+[CE_(s,+)+CE_(s,-)]/2 = CE_s-J_(s,i).

This pays the structural reset to its actual normalized rows from the
structural reference already present, while keeping the seed reference and
bank unchanged. It does not assert a rate4 local influence payment: A032
correctly records failures of that DIFFERENT local inequality.

## 4. Mixed adaptive histories and the SAME original bank

Supply a source history interface W(v) on actual seed restrictions v, including
their prescribed incoming reference, past source debits and remaining account.
Require W(v)>=CE(h_v,R_v) at stopping, and for every admitted source transition

  B_i(h_v)+[W(v,+)+W(v,-)]/2 <= W(v).

No locally finite interface of this kind is assumed for arbitrary Boolean
seeds. An already proved source history theorem can supply one: remaining
worst-case continuation cost, with all earlier debits booked, is a valid W.
For a fixed finite admitted source tree the remaining subtree cost supplies
it exactly. Controller outcomes may choose different source continuations
only when the source interface certifies all the choices actually allowed.

At a joint controller/source state use potential

  V(s,v)=k_s+beta_s W(v).

Sections2--3 prove the local expected erasure-plus-child-potential inequality
for every controller or admitted source query. Induction proves it for EVERY
finite adaptive mixed stopping tree leaving z unqueried. At a controller
query the precise unused bank beta_s[W(v)-CE(h_v,R_v)] is split using the
two actual beta-child normalizers. At a source query it spends the exact
scaled source debit. It is never renewed. All stopped terminal references
are complete Q_(s,R_v), including both source and structural components.

At the original root, beta=3/8, k=5-(9/16)log2(3), j=17/8. If a source
certificate starts with W_root<=K I(h)-rho, rho>=0, then the entire lifted
ledger is at most

  k+(3/8)K I(h)-(3/8)rho.

Since k<2j=17/4 (equivalent to 3^3>2^4), for K>=2 this is at most

  K I(F_h) - [K(17/8)-k] - (3/8)rho.

For a source rate below2 replace K by max(K,2). At K=18, for example,
the ORIGINAL structural margin is 133/4+(9/16)log2(3), in addition to the
scaled unused source reserve. This is arithmetic substitution, not independent
acceptance of any source theorem's admission conditions. There is no new
initial influence-priced source reference for arbitrary h.

After a fixed earlier controller stopping cut T, let E_T be its actually
booked controller erasure. The exact identity is

  E_T+sum_s reach_s k_s = k_root - sum_(queried controller nodes) reach J.

Also sum_s reach_s beta_s=3/8. Thus the same remaining global potential
funds every subsequent eligible source continuation. Neither the root
structural margin nor a source reserve is allocated a second time after T.
This explicitly includes every prior controller spend.
If that history was recorded in A032's rate4 notation, its unchanged record
satisfies E_T=C4(T)+4 sum reach*Inf_u-J_T, with J_T the actually released
controller JS. This translates the existing record into the complete-reference
ledger; it does not spend A032's separate 1/8 reserve a second time.

## 5. The signed Renyi term and exact frontier

At any positive b-sector, R_(b_s tensor h)=R(b_s)+R(h). The signed
sector-normalization gap includes -beta_s R(h), which cancels that term
before the Shannon source reference is priced. This is the same cancellation
as A079 stage6, now with the ACTUAL child beta_s. A zero sector is omitted.
No universal Renyi/influence estimate is substituted. A source reference
reset must satisfy the supplied source interface; it is not free because
one sibling has product spectrum.

Querying z and retaining the FULL marginalized incoming reference is already
paid by the general no-reset reference chain rule, including arbitrary further
no-reset queries. No new reserve is needed for that allowed continuation.
For completeness, at any physical query let p be the parent squared law,
q its frequency marginal and Qbar the same marginal of the incoming Q.
The mean child law is q. Therefore mean child CE=CE(q,Qbar), and
CE(p,Q)-CE(q,Qbar)=B_i(p)+D_cond, where D_cond is the nonnegative expected
conditional occupancy KL. It follows that B_i+mean child CE<=CE(p,Q).
Support positivity follows from the finite parent CE, and all reference-only
atoms remain in Qbar. Repeating this calculation proves the asserted
no-reset continuation without an additional source-price assumption.
The first unsupported extension is querying the physical address z and then
RESETTING to a new descendant reference. Its children are a_s +/- b_s h. Their
Fourier amplitudes are ahat_s(U)1{T=empty} +/- bhat_s(U)hhat(T), so a
biased seed creates a coherent collision at T=empty. The disjoint tagged
reference formula then ceases to apply. A balanced source prevents the first
collision, but later physical restrictions may introduce a nonzero mean.
The source's own universal initial reference payment also remains unpaid.
