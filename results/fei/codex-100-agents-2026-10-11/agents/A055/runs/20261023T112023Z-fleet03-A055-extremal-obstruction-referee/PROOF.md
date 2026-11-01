# Simultaneous approximate child eligibility still admits arbitrary cores

Uniform finite Boolean signs on F2^n; entropy H is in bits. Fix K>=0.
For an original physical block A, retain EVERY assignment u at reach
2^(-|A|), write g_u=f|X_A=u, and let a(g_u) be its full finite affine/
output-character minimum influence. Define

S_A*=E_u[K a(g_u)-H(g_u)],
N_A*=E_u[(H(g_u)-K a(g_u))_+].

N_A* measures expected positive terminal debt before any cancellation.
It vanishes precisely when every complete optimized terminal is a
K-nonviolator; for K>=0 this also licenses every child affine image.
This is a necessary condition for a least-dimensional positive witness,
not by itself a complete definition of genuine criticality.

## 1. A bound uniform over ALL original partitions

Suppose P(f=-1)=delta<=p=2^-k with integer k>=3. For any block A and
child g_u on d=n-|A| remaining coordinates let delta_u=P(g_u=-1) and
q_u=1-(E g_u)^2=4delta_u(1-delta_u). Parseval identifies q_u with the
TOTAL nonempty Fourier mass. Separate the empty atom from the other
at most2^d-1 atoms. Maximum entropy on that finite alphabet gives

H(g_u)<=h2(q_u)+d q_u.                                      (1)

This is valid also at q_u=0 or1 and for constant children; if d=0 its
nonempty mass is0. No FEI inequality is used. Averaging original reaches,
E delta_u=delta, hence E q_u<=4delta<=4p<=1/2. Concavity of binary entropy
and its monotonicity on[0,1/2] imply

E H(g_u)<=h2(4p)+4p d.                                     (2)

For0<=x<=1, -(1-x)ln(1-x)<=x. Since ln2>1/2,
h2(4p)<=4p log2(1/(4p))+8p=4kp. Therefore

E H(g_u)<=4p(d+k)<=B:=4p(n+k).                             (3)

The same B works SIMULTANEOUSLY for every block, regardless of the number
of blocks; there is no union-bound factor. All complete original reaches
are retained, including rare assignments where the arbitrary core is
exposed with large conditional debt. Output-character or affine child
optimization changes H by zero, so it does not evade this entropy bound.

Since K>=0 and a>=0, positive-part debt is pointwise at most entropy:

0<=N_A*<=E H(g_u)<=B.                                      (4)

Also a(g_u)<=I(g_u) and physical restriction accounting gives
E I(g_u)=I(f)-sum_(i in A)Inf_i(f)<=I(f). Consequently

-B<=S_A*<=K I(f),  |S_A*|<=max(B,K I(f)).                   (5)

Equations(1)--(5) hold for ANY such rare-negative-support Boolean root,
every physical partition, and all full affine minima, without criticality,
full span, or independent quotient-rank assumptions. They also hold for
an actually chosen entropy-preserving child reset whose influence is no
larger than the physical child; N only needs nonnegative reset influence.

## 2. Apply the bound to the independently reviewed paid-pair embedding

Consume A005-PAID-PAIR-WEAK-AFFINE-CORE-HARDNESS@1, DERIVATION Sections2--6,
independently reconstructed without repair in A055 stage8 REVIEW_A005.
For any seed f with positive entropy choose a full-span affine-minimal
compressed g with H0=H(g)=H(f), q=I(g)<=I(f), mu=Eg and |mu|<1. Put

Q=(-1)^(ab+ac+bc+za), G_t=Q times t disjoint copies of g,
k=max(3,ceil(sqrt(t))), p=2^-k, F_t=1+A_k(G_t-1).

Its dimension is n_t=d*t+4+k, where d is the fixed seed dimension.
Root negative support is contained in A_k, so delta<=p. The source proves
full affine span/minimality, I(F_t)=p[tq+2+k(1-mu^t/4)]->0 and
H(F_t)/I(F_t)->H0/q. At the original proper pair(a,b), an executable
non-character physical shear in one branch gives release p/4 at original
reach1/4 and queried influence p. With all four terminals retained,

L=4p+R_k(mu^t/4)-R_k(mu^t)/4-3R_k(0)/4,
|L/p-4|<=(13+6k)|mu|^t,
D_K(F_t)+S_pair^reset=L-5Kp/4.                             (6)

The complete nonlinear mean profile R_k is retained in (6); it is not
replaced by its leading term in the bank identity. All four actual
terminals retain all t copies of g. The pair is strictly paid eventually
for each FIXED K>16/5. We book only that one explicit reset; no repeated
dependent parity release, root preprocessing, or new reserve is added.

Here B_t=4p(n_t+k)->0 because p decays exponentially in sqrt(t) while
n_t+k grows linearly in t. Equations(4),(5) prove

max_proper_A N_A*(F_t)->0,
max_proper_A |S_A*(F_t)|->0.                               (7)

These maxima range over ALL nonempty proper ORIGINAL blocks, not just
the displayed pair or a chosen tree. They do not bound the unweighted
maximum individual terminal deficit; querying the controls can expose
the complete hard core at a very small reach.

Thus for every fixed K>16/5 and every epsilon>0, FEI(K) on the subclass
of full-span affine minima with I<epsilon, an original proper pair paid
by an executable non-character reset, and BOTH

N_A*<epsilon and |S_A*|<epsilon for every proper original A

implies full FEI(K) at the SAME K. The reverse implication is immediate.
Take t sufficiently large for all simultaneous bounds and payment, then
pass the ratio limit for each seed. No optimizer in unbounded dimension
or spectral-tail continuity is assumed. Zero-entropy seeds are trivial.
This is a narrow strengthening/application of the reviewed embedding,
not another broad candidate proof of universal FEI.

## 3. The exact failed condition survives every absolute tolerance

If the canonical seed has d_K=H0-Kq>0, (6) and paid-pair negativity give

S_pair*<=S_pair^reset<-D_K(F_t)<0,
N_pair*>=-S_pair* >D_K(F_t)>0                              (8)

eventually. Full optimization decreases terminal influence, so it can
only decrease S and increase positive terminal debt when K>=0.
The exact critical condition N_pair*=0 FAILS, even though every N_A*
and every absolute bank tends to zero simultaneously. Moreover

liminf N_pair*/I(F_t)>=H0/q-K>0,
limsup S_pair*/I(F_t)<=-(H0/q-K)<0.                         (9)

This is a quantitative relative-scale obstruction. An absolute epsilon
budget without accounting for I(F_t) cannot license nonnegative smaller
children. No conclusion about a fixed positive relative tolerance for
all unknown seeds is claimed; (9) is stated for a fixed violating seed.

## 4. An actual finite certificate at K=15/4

Use the eight-bit point defect g, negative only at zero. Its mean is
127/128, q=1/16, H=h(127/128)+255h(1/128). Exact rational logarithm
enclosures give H-(15/4)q>1/256. All nonzero directions have disagreement
1/128, so the seed is affine-influence-minimal and its spectrum has full
support. Choose t=100000000,k=10000, K=15/4. Then

n=800010004, B/p=4(n+k)=3200080016<2^32.

Also K*I(F_t)/p<=K*(tq+2+2k)<2^32. Therefore for EVERY original proper
block, simultaneously,

N_A*<2^-9968 and |S_A*|<2^-9968.                            (10)

The source paid-pair scalar argument is rechecked in this run: Bernoulli
bounds |mu|^t<=128/(128+t), paid margin/p>7633553/12500016, root deficit/p
>862406/4, and ALL FOUR explicit reset terminal deficits/p>862405/4.
Thus (10) coexists with an actual positive root deficit, strict local
payment and negative full optimized child reserve. The huge Boolean
function is defined by its formula, not enumerated. No enormous mean
power is evaluated. It is a fixed-K obstruction, not an unbounded-ratio
Boolean family or a disproof of full FEI.

## 5. Validation scope and exact remaining universal line

code/all_blocks.py separately evaluates the physical activated gadget
with three frozen seeds, all original partitions and every full terminal.
It computes integer Walsh spectra, physical edge influences, complete
finite affine influence minima via greedy independent parity bases, and
exact prime-log entropies. Identical truth-table caching does not merge
original reach weights or remove a terminal. It checks (1)--(5), positive-
part debt without cancellation and bank identities at K=0,15/4,8. Scalar
validation checks the finite point8 gap and all quantities in Section4.
The analytic all-t statement is established above, not by finite cases.

FIRST UNSUPPORTED UNIVERSAL LINE: on a genuine least-dimensional positive
high-K witness, use EXACT nonnegative complete child reserves to force
adequate independent cheap-parity rank after one ORIGINAL proper-pair
restriction, paying its signed bill from the SAME unused bank and keeping
every mixed row and complete terminal. Approximate absolute eligibility
of all blocks, or chart changes preserving their partitions, supplies no
such selection. Relative payment and exact eligibility remain essential.
No universal constant improves; full FEI remains OPEN.
