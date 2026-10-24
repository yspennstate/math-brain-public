# Exact split identity and monotone obstructions

## 1. Definitions

For a Boolean function f:{−1,+1}^n→{−1,+1}, write

f=Σ_S a_S χ_S,   H(f)=Σ_S a_S² log₂(1/a_S²),
I(f)=Σ_S |S|a_S²,   I_i(f)=Σ_{S∋i}a_S².

Zero summands are interpreted by continuity. For a split on coordinate i,
let f⁺ and f⁻ denote the two restrictions and set

Δ_iH(f)=H(f)−[H(f⁺)+H(f⁻)]/2.

The influence identity is

I(f)=[I(f⁺)+I(f⁻)]/2+I_i(f).

Consequently, a constant C such that every nonconstant Boolean function has
some coordinate i with Δ_iH(f)≤C I_i(f) would prove FEI by dimension induction.
This remains an unproved sufficient condition.

## 2. Correct exact entropy-increment identity

For S⊆[n]∖{i}, put a=hat(f⁺)(S), b=hat(f⁻)(S),

w=(a²+b²)/2,  q=(a−b)²/[2(a²+b²)],  r=a²/(a²+b²).

Pairs with w=0 contribute zero and q,r may be assigned any values there.
The full-function Fourier pair is ((a+b)/2,(a−b)/2). Its squared masses are
w(1−q) and wq. Using φ(u)=u log₂(1/u), its entropy is

φ(w)+w h₂(q).

The average entropy of the two restriction coefficients is

[φ(a²)+φ(b²)]/2
=φ(w)−w+w h₂(r),

because a²=2wr, b²=2w(1−r), and φ(2u)=2φ(u)−2u.
Subtracting proves

Δ_iH(f)=Σ_S w_S[1+h₂(q_S)−h₂(r_S)],
I_i(f)=Σ_S w_S q_S.

In particular Δ_iH≥Σ_S w_Sh₂(q_S)≥0. The discarded term
Σ_S w_S[1−h₂(r_S)] is nonnegative and is in general not zero.
For OR on two bits, Δ_iH=2 while Σ_S w_Sh₂(q_S)=1.

The binary entropy bound h₂(u)≥4u(1−u) yields

1−h₂(r)≤4q(1−q),

since r(1−r)=(1−2q)²/4. Hence

h₂(q) ≤ 1+h₂(q)−h₂(r) ≤ h₂(q)+4q(1−q) ≤ 2h₂(q).

Thus omission of the extra term changes constants by at most a factor two,
but a same-constant equivalence is false. The elementary lower entropy bound
can be checked by applying derivatives to h₂(u)−4u(1−u) on [0,1/2], then
using symmetry. The second derivative changes sign once there; the first
derivative starts at +∞, becomes negative, and returns to zero at 1/2, so
the function rises from zero and then returns to zero without going below it.

Also, h₂(q)≤q log₂(1/q)+q log₂e, giving

w[1+h₂(q)−h₂(r)]
≤wq[log₂(1/q)+log₂e+4].                 (2.1)

## 3. A monotone prescribed-coordinate obstruction

Partition n=3k coordinates into k blocks of size three. Let f_k output +1
iff some block is entirely +1. Choose y with the first block +1 and all
other coordinates −1. The point y is a minimal positive input. Define

F_k(x,+1)=f_k(x),
F_k(x,−1)=f_k(x)−2·1_{x=y}.

Removing a minimal positive input preserves monotonicity, the second
restriction is pointwise no larger than the first, and therefore F_k is
monotone. Write z for its extra coordinate and ε=2^(−n)=8^(−k).
The two restrictions differ at exactly one input, so I_z(F_k)=ε.

Let A_j indicate that block j is all positive. Then

f_k=1−2∏_j(1−A_j).

For each block, hat(1−A_j)(empty)=7/8 and every nonempty block Fourier
coefficient is −1/8. For a nonempty global Fourier index S, let t(S) be
the number of blocks S misses. The coefficient of f_k therefore satisfies

|hat(f_k)(S)|=2ε·7^{t(S)}.              (3.1)

Since hat(1_{x=y})(S)=εχ_S(y), the Fourier pair of F_k is

(hat(f_k)(S)−εχ_S(y), εχ_S(y)).

Set w_S=(hat(f_k)(S)−εχ_S(y))²+ε² and q_S=ε²/w_S.
For S≠empty, the triangle inequality and (3.1) give

ε²7^{2t(S)}≤w_S≤10ε²7^{2t(S)}.        (3.2)

For the lower bound, put x=7^{t(S)}≥1 and observe
(2x−1)²+1≥x². The upper bound uses (2x+1)²+1≤10x².

Applying the exact identity, nonnegativity, and h₂(q)≥q log₂(1/q),

Δ_zH(F_k)≥ε²Σ_{S≠empty}log₂(w_S/ε²)
≥2ε²log₂7·Σ_{S≠empty}t(S).

Each particular block is missed by exactly 2^(n−3) indices; excluding the
empty index subtracts k. Hence

Σ_{S≠empty}t(S)=k(2^(n−3)−1).

Dividing by I_z(F_k)=ε proves

Δ_zH(F_k)/I_z(F_k)
≥(k/4)log₂7−2kεlog₂7.                (3.3)

For the upper bound, (2.1) contributes at most

ε²[log₂(w_S/ε²)+log₂e+4]

for each index. For the empty index, |hat(f_k)(empty)|≤1 and ε≤1/8,
so w_empty≤(1+ε)²+ε²<2 and
log₂(w_empty/ε²)≤6k+1. Sum (3.2) over all nonempty indices to get

Δ_zH(F_k)/I_z(F_k)
≤(k/4)log₂7−2kεlog₂7+(1−ε)log₂10
  +ε(6k+1)+log₂e+4.

Since k8^(−k)≤1/8 and ε(6k+1)≤7/8 for k≥1, putting c=log₂7/4 gives

ck−c ≤ Δ_zH(F_k)/I_z(F_k) ≤ ck+8.65.

Thus the exact asymptotic statement is

Δ_zH(F_k)/I_z(F_k)=(log₂7/4)k+O(1),

with an absolute error bounded uniformly in k. This rules out an arbitrary
prescribed-coordinate increment inequality, even for monotone functions.
It does not rule out an adaptive choice of a different coordinate.

## 4. Maximum influence is also an invalid selection rule

Let G be any outer Boolean function of m coordinates and let g_j be
balanced Boolean functions on mutually disjoint variable blocks. Define
G∘g=G(g_1,...,g_m). Distinct outer Fourier indices have disjoint inner
Fourier supports because each g_j has zero constant Fourier coefficient.
Taking squared coefficients and expanding Shannon entropy proves exactly

H(G∘g)=H(G)+Σ_j I_j(G)H(g_j),
I_leaf(G∘g)=I_j(G)I_leaf(g_j)          (4.1)

for a leaf of block j. This is a direct coefficient computation, independent
of the conjecture.

Apply it to F_k, replacing each old x-coordinate by odd majority on M fresh
bits and leaving z as a single dictator bit. For each old coordinate j,

I_j(F_k)=[I_j(F_k⁺)+I_j(F_k⁻)]/2.

Subtracting the entropy composition formulas for F_k and its z-restrictions
therefore shows

Δ_zH(F_k∘g)=Δ_zH(F_k),
I_z(F_k∘g)=I_z(F_k)=ε.               (4.2)

For M=2r+1, every majority leaf has influence

α_M=binom(2r,r)/2^(2r),

which tends to zero as M tends to infinity. An explicit choice is

r=64^k,    M=2·64^k+1.

Indeed, α_M=∏_{j=1}^r(1−1/(2j)) and

(1−1/(2j))²<j/(j+1)

for every positive integer j (after multiplication, this is 1<3j).
Taking products gives α_M²<1/(r+1), and therefore

α_M<1/√(64^k+1)<8^(−k)=ε.

The resulting function has the explicit finite dimension

N_k=3k(2·64^k+1)+1.

Since every
outer influence is at most one, all new leaf influences are below ε, while
z has influence ε. Thus z is the unique maximum-influence coordinate, but
its entropy-increment/influence ratio still grows linearly in k by (3.3).
All gates and the resulting function are monotone.

**Conclusion:** no universal constant can make the exact split inequality
hold whenever one chooses a coordinate of maximum influence. This refutes
a natural strengthening of the adaptive induction route; it does not solve
or refute FEI itself.

### Quantified approximate-maximum corollary

For every η∈(0,1] and every C>0 there is a monotone Boolean function G such
that every coordinate i satisfying

I_i(G)≥η·max_j I_j(G)

also satisfies Δ_iH(G)>C I_i(G). In particular, a universally good adaptive
split cannot be required to lie within any fixed factor of maximum influence.

Choose an integer k≥2 with ck−c>C, where c=log₂7/4, and set

r=ceil(η^(−2)64^k),  M=2r+1.

Replace the 3k old coordinates of F_k by majority_M, leaving z unchanged.
The product estimate gives

α_M<1/√(r+1)<η·8^(−k)=ηε.

All replacement leaf influences are at most α_M; only z qualifies for
I_i≥η max_jI_j. Its ratio exceeds C by (3.3), which survives exactly by
(4.2). Strict inequalities eliminate ties. This establishes the corollary
with the explicit finite dimension 3k(2ceil(η^(−2)64^k)+1)+1.

At the opposite extreme, choosing a minimum positive influence also fails.
In the original F_k, write a=(1/4)(7/8)^(k−1). Removing y removes one boundary
edge in each of the three positive-block directions and adds one in every
other direction. Since an edge contributes 2ε to influence, the old
coordinate influences of F_k are a−ε in the positive block and a+ε elsewhere.
For k≥2, a/ε=2·7^(k−1)>2, so every old coordinate has influence above ε,
and z is the unique minimum positive-influence coordinate. Its bad ratio
still diverges. These two results do not refute the unrestricted adaptive
existence statement.

## 5. A finite constant obstruction

For AND_3, the constant coefficient has magnitude 3/4 and the seven other
coefficients have magnitude 1/4. Therefore

H(AND_3)=4−(9/8)log₂3,
I_i(AND_3)=1/4.

Each split gives a constant function and AND_2, whose entropy is 2. Thus

Δ_iH(AND_3)/I_i(AND_3)=12−(9/2)log₂3≈4.867668746754797

for every relevant coordinate. Any uniform adaptive split constant must
therefore exceed this value. This is not the best known lower bound on the
constant in the full FEI conjecture, which is a different quantity.

## 6. Even a monotone zero-separator condition is insufficient

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
