# Source-bound stopping review and sharp depth-law admission

Uniform finite Boolean signs; normalized Walsh coefficients; entropy bits.
A051-REFERENCE-ERROR-OCCUPATION-STOPPING-BOUND@1 has statement SHA256
250e8066d00318071c5094e9fd3924e48cc7799c41af4625ecada4cdeda78bbb.
Verdict: HOLDS without repair for STOPPING Sections1--4. This is an
independent reconstruction, not a universal critical-pair selection claim.

## 1. Reconstructing the fixed-event ledger

Fix a signed root character c and original event Z={f!=c}. An invertible
input affine map permutes inputs. Applying the same output character to
f and c preserves their comparison pointwise. Restricting either sign to
one current coordinate preserves the character form of c. Thus original
inputs can be carried as ancestry labels, with Z fixed once at the root.
The errors on two query daughters average to the parent's conditional q.
For a translated edge the reference character has constant disagreement
0 or1, and the f-edge can differ only at an erroneous endpoint. This gives
minority m<=2q, and trivially m<=1/2. No independence is asserted.

For clarity, the one-query entropy bound is a distributional decomposition:
B_i=H(S_i|S_-i)<=h2(Inf_i), and the established scalar Walsh-packet
JS bound gives L_i=B_i+JS_i<=h2(Inf_i)+2 Inf_i/ln2. Multiplication by
the queried character complements Inf_i, preserving root and both complete
child entropies. Thus L_i<=phi(m), phi(x)=h2(x)+2x/ln2. Phi is increasing
and concave on[0,1/2]. The function psi(q)=phi(min(2q,1/2)) is concave
on[0,1]: its derivative drops to0 at q1/4. These derivative properties
follow directly from h2''=-1/(ln2*x*(1-x)) and hold at endpoints by limits.

Every original input visits tau internal nodes. Counting visits gives
sum_v w_v=E tau=dbar and sum_v w_v q_v=E[1_Z tau]=a. Normalizing these
finite INTERNAL-node weights, rather than terminal weights, and applying
Jensen gives sum w_v L_v<=dbar psi(a/dbar). Entropy telescopes despite
arbitrary affine resets, since they preserve H. For dbar0 there are no
queries and both sides0. This proves the source occupation inequality.

For the influence ledger, query splits satisfy I_parent=Inf_query+E I_raw_child.
Define each actual reset release as I_raw_child-I_reset_child, signed if
necessary. Summing at original reaches gives Q+R=I_root-E I_leaf. With
D_K=H-KI and S=E[K I_leaf-H_leaf], exact subtraction yields
D_K(root)+S+K(Q+R)=H_root-E H_leaf. Nonincreasing-I resets ensure R>=0
and license the deficit lower bound. Every full terminal remains, including
constant or negative-reserve terminals. No preprocessing can renew a bank.

## 2. Independent reconstruction of the depth boundary

Take a canonical nonconstant d-bit seed g, t=2^k,p=2^-k,k>=2, and activate
g^tensor(t) on k zero controls. Query controls until first1, stopping then;
after all-zero controls, query all dt data bits even if the function becomes
constant earlier. All complete terminals are constants. Exact path counts:

E tau=2(1-p)+pdt=d+2(1-p),
e=P(F!=1)=p(1-mu^t)/2,
E[1_Z tau]=e(k+dt).

Every error input reaches the unique long data branch. Since |mu|<1,
a->d/2 while e->0 and E tau<=d+2. The constant character is optimal:
its Fourier coefficient >=1-2p, all others have magnitude<=2p.
The canonical full-span/minimum admission follows the already reconstructed
activation/basis ledger, not an arbitrary probability-law relaxation.

At bent2,k10,t1024: E tau=2047/512, H_root>=1933/1024,
D_1(root)>=889/1024. The false expected-depth substitution would charge
less than4*(29/1024)=116/1024. All comparisons are rational using
ln2>2/3 and the signed activation profile error p(10k+15).
This independently accepts the source finite negative arms without
constructing a2058-bit truth table. No full FEI disproof follows.

## 3. Sharp occupation envelope from a complete depth law

This narrow consequence is new author work, pending independent review.
For ANY actual finite tree let T=tau, e=P(Z), and let its finite complete
path-depth law be retained. Then

 a=E[1_Z T] <= A(e,T):=min_{L in {0,...,max T}}
                      [L e+E(T-L)_+].                    (4)

Proof: pointwise T*1_Z<=L*1_Z+(T-L)_+. For optimality, order the N
uniform original inputs by decreasing T and choose Z to be the first eN
inputs (eN is an integer for a Boolean root). Pick L at the boundary depth.
Then all selected inputs have T>=L and all omitted inputs have T<=L,
so equality holds in the pointwise inequality after averaging. This is
also an exact rational primal/dual certificate: select the upper e-tail
of the depth law; L is the dual threshold. Ties and e0/e1 cause no problem.
Sharpness is for the occupation bound, not for the entropy inequality.
For any fixed actual input-query tree, the selected event is itself an
actual Boolean error event of f=1-2*1_Z against constant1. No claim says
that this reference must be the best character in every sharpness fixture.

Consequently the source's entropy decrement is bounded by
 dbar phi(min(2A(e,T)/dbar,1/2)). This uses the complete terminal-depth
law and error mass, without assuming that stopping and error are independent.
An upper expected-depth bound alone cannot make A small. In the activated
source tree, every error occupies the maximum-depth stratum and its mass
is no more than p. Choosing L=max T gives A<=e max T=a; therefore (4)
is EXACT on the actual all-k counterguard, not just a loose obstruction.

For a sequence of finite trees with e->0 and uniformly integrable depth
laws, fix L, use a<=Le+E(T-L)_+, then take limits to obtain a->0.
If dbar<=D<infinity, entropy loss->0: for D>0, the perspective bound is
<=D phi(min(2a/D,1/2)); this follows from concavity and psi(0)=0.
If D=0 all trees have no queries. Under the same bounded-mean assumption,
a sufficient easily checked criterion is e E[T^2]->0, since Cauchy--Schwarz gives a<=sqrt(e E[T^2]). Neither
criterion is inferred from bounded E T. The rare-source tree has
E[T^2]>=p(k+dt)^2, so e E[T^2] has liminf>=d^2/2 and fails this
sufficient test, as it must. These are frontier-admission conditions,
not a theorem paying every query or providing an influence-priced source.

## 4. Exact unpaid universal line

C019 still requires one ORIGINAL proper pair of a genuine finite least-
dimensional high-K witness with adequate independent quotient-rank funding
from the SAME unused NONNEGATIVE smaller-affine-child reserves, mixed
interaction and all complete terminals. The reviewed stopping ledger and
sharp depth-law certificate constrain possible admission; they do not
force that pair or pay its bill. Universal constant gain0. Next use actual
critical eligibility rather than bounded expectation or a changed error event.
