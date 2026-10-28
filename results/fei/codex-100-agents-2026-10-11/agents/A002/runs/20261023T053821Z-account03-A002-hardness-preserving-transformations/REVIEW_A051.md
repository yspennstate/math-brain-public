# Independent reconstruction of A051's tail/escape admission

Scope: A051-TAIL-CERTIFIED-FINITE-APPROXIMATION-AND-ESCAPE@1,
COMPACTNESS Sections 1--3, statement hash
aaf4e19351e6507e14c5a12878753d34c8ffaa0354f775c8a9f9d82a9e089d20.
Verdict: HOLDS without repair. This is a scoped independent-agent
reconstruction, not approval of a universal critical-pair selector.

## 1. Approximation, reconstructed from errors and coupling

Let z=E[f|first m bits] and g=sign(z), with sign(0)=+1.
Conditionally the disagreement probability is (1-|z|)/2. Since
|z|>=z^2, its expectation e is at most delta/2. Flipping coordinate j
can change the comparison of the f and g edge indicators only when
an endpoint lies in their disagreement set. Invariance of the uniform
measure bounds the influence difference by 2e. The sum of omitted
coordinate influences is <=T_I, so the stated m delta+T_I bound holds.

Writing Fourier vectors a,b, Parseval gives ||a-b||_2=2sqrt(e).
Half the l1 distance of their squares is at most
||a-b||_2 ||a+b||_2/2 <=2sqrt(e). Collapsing the escaping labels cannot
increase variation. The collapsed entropy loses precisely
T_H+delta log2(delta), between zero and T_H. For two laws on M atoms,
a maximal coupling disagrees with probability v, and conditioning on
its mismatch flag bounds either conditional entropy by
h2(v)+v log2(M-1). Here M=2^m+1. At delta<=1/8 the replacement
v<=eta=sqrt(2delta)<=1/2 is legitimate by monotonicity. This proves
the entropy estimate and hence the fixed-K deficit estimate, including
delta=0, missing labels and sign ties. The same steps on the countable
cube use the given finite H,I and convergent Parseval expansions.
Finite affine minimization preserves H and decreases I; it needs no
infinite optimizer. The sufficient rate m sqrt(delta)->0 is explicitly
additional, not deduced from finite H or I.

## 2. Escape, reconstructed by signed coefficient multiplicities

For h=g^tensor(t), t=2^k, p=2^-k, nu=mu^t, activation has coefficients
1-p(1-nu) at the empty label, -p(1-nu) at each of 2^k-1 nonempty
control-only labels, and p hhat(s) at every control label for each
nonzero data s. With q(x)=-x^2 log2(x^2), summing these three disjoint
parts gives

H(F)=pt H(g)+q(1-p(1-nu))-p q(nu)+p(1-p)q(1-nu)
     +2kp[(1-nu^2)+(1-p)(1-nu)^2].

Physical data edges give p t I(g), and each control contributes
p(1-nu); this independently gives I(F)=I(g)+kp(1-nu).
The same negative-event probability gives ||F-1||_2^2=2p(1-nu).
On the indicated ranges the four remaining entropy terms have absolute
bounds 6p, p, 8p, 10kp. For the first bound use
q(1-pb)<=2pb/ln2, b<=2 and ln2>2/3. Thus
|H(F)-H(g)|<=p(10k+15) and the stated fixed-K error follows.
These estimates are valid also for negative means and vanishing terms.

## 3. Canonical admission and tail escape

For any data direction u, the Boolean negative-event union bound gives
w_h(u)<=1-|nu|<=1-nu. Tensor parity biases multiply, so the centered
cost of a tensor parity dominates each participating seed cost.
Consequently tensors of affine-minimal seeds remain affine-minimal.
All activated direction costs are <=2p<=1/2. Data-only directions have
cost p w_h(u); directions involving any controls have cost p(1-nu).
The basis criterion therefore proves full affine minimality of F.

The nonzero root coefficient supplies the origin in the support.
Replicas of one nonzero data coefficient generate every control
direction. Projecting support to data contains the tensor support,
whose affine span is full. The support span is thus the entire data
plus control space, including the zero-mean boundary.

Use one countable coordinate system with the first k bits as controls
and the subsequent dt as data. No independence between different k
is required: a sample whose first 1 occurs at coordinate j has F_k=1
for every k>=j. The exceptional all-zero sample has probability zero.
Every fixed nonempty spectral label is eventually control-only and
has mass <=4p^2. The empty mass tends 1. Their finite-window entropy
and influence vanish although the total limits are H(g),I(g)>0.
Also kp(1-nu)<=1 for k>=2, proving the asserted uniform I bound.
This validates the exact scope: no continuity or optimizer admission
from bounded I and L2 convergence alone; no assertion of optimizer
nonexistence or an unknown-K violating seed.

## 4. Bounded original-data-query corollary (narrow new consequence)

Fix r and any adaptive tree making at most r ORIGINAL DATA-coordinate
queries on F_k; controls stay unresolved, and there are no intervening
input resets before the queries. At each physical leaf at
most r seed copies have been touched. Its unactivated data function h_b
is a product of t-s untouched g copies and s restricted copies, s<=r.
Entropy additivity and 0<=H(restricted g)<=d imply
|H(h_b)-tH(g)|<=r(d+H(g)). Affine spectral minimum is additive over
disjoint products: minimize factors individually, then the tensor
bias/basis criterion above gives global minimality. Thus
a(h_b)>=(t-s)I(g), while I(h_b)<=(t-s)I(g)+sd.

The activated linear and full-affine minima both equal
p[ell(h_b)+k(1-E h_b)], with a(h_b)<=ell(h_b)<=I(h_b).
One can also reconstruct this without a transported child refund:
all data costs are <=p(1-E h_b), all control-involving costs equal that
threshold; minimum-basis rank integration first selects the cheapest
independent data directions, then k control directions. Every centered
activated cost equals its uncentered cost since k>=2.
Therefore uniformly in every leaf and every such bounded tree,

|H(F_b)-H(g)| <=p[r(d+H(g))+10k+15],
|a(F_b)-I(g)| <=p[r(d+I(g))+2k].

For K>=0 put E=p[r(d+H(g))+10k+15+K(r(d+I(g))+2k)].
Every complete optimized leaf obeys |D_K(F_b)-D_K(g)|<=E. Hence if a
specified seed has deficit Delta>0 and E<Delta, ALL complete leaves
still violate K. In particular the signed terminal bank
E_leaf[K a(F_b)-H(F_b)] is at most -Delta+E<0, regardless of adaptive
reach probabilities. Expected queried influence is <=rp (each
queried data influence <=p), and expected terminal-reset release is <=prd:
the untouched copies cancel between I(h_b) and a(h_b). Both vanish.
This restriction on bounded ORIGINAL-data queries is essential; no
claim covers querying controls or adaptive basis-changing policies.

## Universal gap

These are admission obstructions, not genuine critical witnesses.
The first unsupported line remains: select and fund an original proper
pair of a finite least-dimensional positive high-K witness from SAME
unused NONNEGATIVE smaller-affine-child reserves, independent quotient
rank, mixed interaction and all full terminals. Universal constant gain
is zero. Compactness or bounded data-query depth cannot replace that
eligibility hypothesis.
