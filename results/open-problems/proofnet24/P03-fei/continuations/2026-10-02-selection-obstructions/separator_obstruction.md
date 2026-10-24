# Monotone zero-separator obstruction for FEI split induction

Status: proved obstruction to a proposed sufficient condition; **not a proof
or disproof of classical FEI, and not a resolution of deterministic LTF FEI**.

This is the separately archived continuation of the exact split and tribe
construction. The required prior facts are fully proved in
`split_identity_and_obstructions.md` §§2–4:

- For n=3k, ε=8^(−k), the monotone tribe function f_k is +1 iff one of k
  disjoint three-bit blocks is all +1. Choose the minimal positive point y
  with the first block +1 and all other blocks −1. The Boolean extension
  F_k(x,+1)=f_k(x), F_k(x,−1)=f_k(x)−2·1_{x=y} has I_z=ε.
- Its exact entropy increment obeys Δ_zH(F_k)/ε=c k+O(1), where
  c=log₂7/4, with lower bound c k−c and upper bound c k+8.65.
- Substituting independent balanced Boolean gates for its old coordinates
  preserves I_z and Δ_zH exactly. This follows from
  H(F∘g)=H(F)+Σ_j I_j(F)H(g_j) and
  I_j(F)=[I_j(F⁺)+I_j(F⁻)]/2 for j≠z.

All logarithms below are base 2.


This section gives another rigorous obstruction to a promising restricted
FEI proof route. For a monotone linear threshold function split on a largest
defining weight, write F=A+zB, where A takes values in {−1,0,+1} and
B=1_{A=0}. No hypercube edge of the remaining coordinates joins A=+1 to
A=−1: a single remaining coordinate changes the defining weighted sum by
at most twice the chosen largest weight, and cannot cross both parallel
thresholds defining the zero slab. The tempting general statement

"For every monotone ternary A with no +/− edge, Δ_zH(A+z1_{A=0})
 is at most a universal constant times Pr(A=0)"

is false. Its failure does not establish failure of the LTF case, which has
additional parallel-halfspace geometry.

### 6.1 Dimension-free continuity for a split increment

For any two Boolean functions F,G on the same cube with a distinguished
coordinate z, let p=Pr(F≠G). Their Fourier coefficient vectors have squared
L² distance 4p. For unit vectors c,d, the total variation distance between
their squared-coordinate distributions is at most ||c−d||₂, by Cauchy–Schwarz:

(1/2)Σ|c_s²−d_s²|
≤(1/2)||c−d||₂||c+d||₂≤||c−d||₂.

The full-function Fourier pairs form one probability law on (S,bit). The
restriction coefficient vectors (hat(F⁺),hat(F⁻))/√2 form another such law.
The latter is obtained from the full pairs by the orthogonal two-by-two
Hadamard matrix, so its squared vector distance between F and G is also 4p.
Both laws thus change in total variation by at most t=2√p.

For joint laws P,Q on (X,Y), with X binary and total variation t≤1/2,

|H_P(X|Y)−H_Q(X|Y)|≤t+h₂(t).           (6.1)

To prove (6.1), write their common part as weight 1−t times a probability
law R and their two residual parts as weight t times laws P′,Q′. Under a
mixture with label J, conditional entropy differs from its component average
by I(X;J|Y), which lies between zero and h₂(t). Each binary conditional
entropy lies in [0,1], proving the displayed bound. This proof is independent
of the size of Y.

The exact split identity can be written as

Δ_zH(F)=H_full(bit|S)+1−H_restriction(bit|S).

Applying (6.1) to the two laws gives

|Δ_zH(F)−Δ_zH(G)|≤2[t+h₂(t)]           (6.2)

whenever t=2√p≤1/2. In particular, a tiny physical modification can have
dimension-free control of this difference of spectral entropies, even
though continuity of the individual spectral entropies costs dimension.

### 6.2 Constructive majority substitution followed by erosion

Return to F_k from §3, with n=3k and ε=8^(−k). Its ternary part is

A_0=f_k−1_{x=y},    B_0=1_{x=y}.

A_0 is monotone: it changes the minimal positive point y from +1 to zero,
while points strictly below y are negative and points above y are positive.

Replace each of its n input coordinates by balanced odd majority on

r=(2n)²ε^(−12),    M=2r+1

fresh bits. These are explicit positive integers. Write A for the resulting
monotone ternary function and B=1_{A=0}; its distinguished-coordinate
extension F=A+zB has I_z(F)=ε and exactly the same Δ_zH as F_k, by §4.

Define two eroded regions on the enlarged cube:

P′={u:A(u)=+1 and A(v)=+1 for every neighbor v of u},
N′={u:A(u)=−1 and A(v)=−1 for every neighbor v of u}.

Let A′=1 on P′, −1 on N′, and zero elsewhere; put B′=1_{A′=0} and
G_k=A′+zB′.

P′ is an upset: when an input is increased, every downward neighbor of the
new input lies above either a downward neighbor of the old input or the old
input itself. All such points remain positive. The negative analogue shows
N′ is a downset. Thus A′ is monotone, and the two increasing maps

a↦a+1_{a=0},    a↦a−1_{a=0}

show that the two z-restrictions of G_k are monotone. The first is pointwise
at least the second, so G_k is a monotone Boolean function.

There is no +/− edge for A′. If u∈P′, every neighbor has original A-value +1,
so no neighbor can belong to N′, whose original A-value is −1.

Let δ=Pr(A′≠A). A change can occur only at an input where some single bit
can change the output of an inner majority. Such a majority block must have
sum equal to +1 or −1. For M=2r+1, the probability of those two margins is

Pr(|sum_M|=1)=((2r+1)/(r+1))α_M<2α_M<2/√(r+1).

A union bound over n blocks therefore gives

δ<2n/√(r+1)<ε⁶.                      (6.3)

The originally zero points remain zero, so I_z(G_k)=Pr(A′=0)=ε+δ. At a
newly zero point, G_k differs from F for exactly one of the two z values.
Consequently Pr(F≠G_k)=δ/2 and (6.2) applies with t=√(2δ)<√2ε³.

Using h₂(t)≤t[log₂(1/t)+log₂e], monotonicity for t≤1/2, and n=3k,

|Δ_zH(G_k)−Δ_zH(F_k)|/ε
≤2√2 ε²[9k+1/2+log₂e]<1/2.           (6.4)

For the last inequality, log₂e<3/2 and k64^(−k)≤1/64 give the upper bound
22√2/64<1/2. Combining (3.3), (6.3), and (6.4), for k≥2,

Δ_zH(G_k)/I_z(G_k)
≥[ck−c−1/2]/[1+ε⁵],

where c=log₂7/4. It diverges linearly in k; in fact the previous upper bound
and (6.4) also give ratio=ck+O(1).

The complete function has finite explicit dimension n(2(2n)²8^(12k)+1)+1.
Its ternary part is monotone and has no +/− edge. This proves that the
separator condition alone cannot furnish a dimension-free LTF induction
lemma. Any successful LTF argument must use more than monotonicity and the
absence of direct sign-crossing edges.
