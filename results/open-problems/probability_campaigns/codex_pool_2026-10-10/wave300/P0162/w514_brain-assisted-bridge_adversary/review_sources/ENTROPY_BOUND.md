# Universal entropy-increment bound and exact remaining budget

Uniform Boolean assumptions and notation are as in BRIDGE_CHECKPOINT.md. Everything here is an independent elementary derivation of known bounds; no novelty claim.

For two nonnegative numbers x,y, put r=x+y. Their one-index Jensen-Shannon contribution in nats is j(x,y)=(x ln(2x/r)+y ln(2y/r))/2, with continuous zero conventions. Then

j(x,y) <= (sqrt(x)-sqrt(y))^2/2.

Proof: when r>0 write u=(x-y)/r and use symmetry to assume u in [0,1]. The inequality is equivalent to (1+u)ln(1+u)+(1-u)ln(1-u) <=2(1-sqrt(1-u^2)). Both sides vanish at zero. The derivatives are 2atanh(u) and 2u/sqrt(1-u^2). The latter is larger because atanh(u)=integral_0^u (1-v^2)^-1 dv <=integral_0^u (1-v^2)^-3/2 dv=u/sqrt(1-u^2). Extend to u=1 by continuity. The case r=0 is immediate.

Apply this with x=a_S^2 and y=b_S^2. Since (|a|-|b|)^2 <=(a-b)^2, summing and converting nats to bits gives

0 <=JS(P,Q) <=(1/(2ln2)) sum_S(a_S-b_S)^2=(2/ln2) I_i(f).

Binary entropy is concave and R is a probability distribution, so B_i=sum R h(q)<=h(sum Rq)=h(I_i). Consequently,

B_i <=Delta_i=B_i+JS <=B_i+(2/ln2)I_i <=h(I_i)+(2/ln2)I_i.

For t>0, h(t)<=t log2(1/t)+t/ln2, since -(1-t)ln(1-t)<=t. Thus Delta_i <=t[log2(1/t)+3/ln2]. This loses log(1/t); it is not a full FEI proof. For a chosen coordinate with t>=tau>0, it gives Delta_i <=[log2(1/tau)+3/ln2]t. This matches the small-influence reduction card retrieved from the brain (its printed constant is 2/ln2+log2(e/tau)).

If B_i<=K I_i at the selected split, then Delta_i <=(K+2/ln2)I_i. Conversely Delta_i<=K I_i implies B_i<=K I_i. Constant changes must be retained; Delta_i is not B_i.

An exact full-tree form identifies the single remaining mathematical budget. Let T be any finite adaptive restriction tree ending in constant functions, with each internal node v at depth d(v) splitting an unfixed coordinate i(v), and let w_v=2^-d(v). Telescoping the identities H(f_v)=average_child H+Delta_v and I(f_v)=average_child I+I_i(f_v) gives

H(f)=sum_{v internal} w_v Delta_v,
I(f)=sum_{v internal} w_v I_i(f_v),
sum_v w_v B_v <=H(f)<=sum_v w_v B_v+(2/ln2)I(f).

Thus a dimension-free bound sum_v w_v B_v <=K I(f) would prove FEI with constant K+2/ln2. FEI with constant C would imply this budget for every complete tree with constant C. Unlike a per-node good-coordinate assertion, this aggregate condition is equivalent to FEI up to an additive change in constant. Uniform product measure gives the weights; there is no multiplication of conditional probability bounds.

The hardest gap is this dimension-free aggregate conditional-entropy estimate for Boolean spectra. No such estimate is supplied. The rare-switch lemmas explain why replacing it by a bound at an arbitrary coordinate fails, even after reducing to small influences.
