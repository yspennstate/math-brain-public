# Majority-of-tribes: exact transport and a logarithmic stopping-tree obstruction

Uniform independent physical signs; entropy and logarithms are in bits. Let
`B_i(f)=H(S_i|S_-i)`, `j_i=min(Inf_i,1-Inf_i)`, and
`kappa(h)=1-max_S hhat(S)^2`. The source charge is exactly

`Lambda_v=j_v log2(1+kappa_min,v/(2j_v))`,

with zero-j terms zero. This is LOG_ALLOCATION_CURATED §5, not the
blind Hellinger charge `M log(1/M)`. Node and leaf weights are their actual
uniform physical probabilities. Every queried and retained input counts in I.

## 1. Exact arbitrary-core transport

Let m>=2 be even, alpha=binom(m,m/2)/2^m, and

`F(x,y)=Maj_(m+1)(x_1,...,x_m,G(y))`,

where G is any Boolean sign on a disjoint uniform cube, with no balance
assumption. Set `g(x)=sign(sum x)` with sign(0)=0, and
`c(x)=1_{sum x=0}`. Then **F=g+cG**. The Fourier support of g has odd
x-cardinality, whereas that of c has even x-cardinality. Also
`sum ghat^2=1-alpha` and `sum chat^2=alpha`.

For any x-index X and y-index Y,

`Fhat(X,Y)=ghat(X)*1_{Y=empty}+chat(X)*Ghat(Y)`. (1)

The parity supports are disjoint even in the empty Y sector. The spectrum
is consequently the disjoint union of the g-square sector and the tensor
of the c-square sector with the full G spectrum, **including its empty
coefficient**. Splitting the logarithm of each tensor mass proves

`H(F)=H(Maj_(m+1))+alpha H(G)`,
`I_Y(F)=alpha I(G)`, `Inf_(x_i)(F)=alpha`,
`I(F)=alpha[m+I(G)]`. (2)

For the x influence, the sum of the other m-1 x signs must be +1 or -1;
these two events have equal probability alpha. Whether each is pivotal
depends on G, and their complementary G probabilities sum to one.

Fix a data coordinate i. At every residual x-index with a g coefficient,
the queried y coefficient is zero, so the erasure is zero. At every
residual x-index with a c coefficient, both entries of each G fiber are
multiplied by the same chat(X), which multiplies the fiber mass and its
minority mass by chat(X)^2 without changing the conditional ratio.
Thus, exactly,

`B_i(F)=alpha B_i(G)`, `M_i(F)=alpha M_i(G)`,
`Q_i(F)=alpha Q_i(G)`, `JS_i(F)=alpha JS_i(G)`. (3)

Here M_i and Q_i are the ISOSPECTRAL §2-3 minority mass and retained
packet logarithm. The JS identity also follows from (2) for G and both
physical children and the exact decrement identity. No pending sandwich
claim is assumed in (1)-(3).

For x erasures, nonempty Y sectors have only even x support and contribute
zero. The empty Y sector has fibers containing one g square and one
`mu^2 c square`, where mu=E G. This is an exact finite Krawtchouk expression
depending on mu alone. In particular, if G is balanced then

`B_(x_i)(F)=0` for all x_i, and `B(F)=alpha B(G)`. (4)

For m=2, the entire spectrum is especially simple: two g coefficients
1/2 and two c coefficients of magnitude 1/2. Therefore

`H(F)=2+H(G)/2`, `I(F)=1+I(G)/2`,
`B_(x_i)(F)=(1+mu^2)/2 * h2(mu^2/(1+mu^2))`,
`B(F)=B(G)/2+(1+mu^2)h2(mu^2/(1+mu^2))`. (5)

At every data split, **both children F have kappa exactly 3/4**, even
when the core child is constant: the two unchanged g coefficients have
square 1/4 and all cG coefficients have square at most 1/4. Thus

`Lambda_y(F)=(Inf_y(G)/2) log2(1+3/(4 Inf_y(G)))`. (6)

These identities preserve arbitrary core entropy. In particular they do
not supply a universal payment of B(G): an attempted payment which omits
that conditional entropy fails the arbitrary-core admission test.

## 2. Exact tree ledger for a finite physical order

At a node, let u_T and v_T be the parent coefficients without/with the
next physical coordinate. Set `p_T=u_T^2`, `r_T=v_T^2`, `q_T=p_T+r_T`,
and `m_T=min(p_T,r_T)`. Then the exact quantities are

`B_v=sum_T[p_T log2(q_T/p_T)+r_T log2(q_T/r_T)]`,
`Q_v=sum_{T:m_T>0}m_T log2(q_T/m_T)`,
`kappa_min=min(1-max child0hat^2,1-max child1hat^2)`. (7)

Each child coefficient is `u_T+v_T` or `u_T-v_T`, so all masses, j and
kappa are rational. The code stores complete rational-coefficient
logarithmic expressions for Lambda_T, B_T and exact H(leaf). It checks
the independent physical-edge influence and the identity

`I(root)=sum_v weight_v Inf_v + E I(leaf)`. (8)

At every leaf certified as a symmetric threshold, the supplied threshold
paper gives `H(leaf)<=C_reg I(leaf)<9 I(leaf)`. This run uses **9**,
not a read-once formula theorem or an arbitrary-core leaf certificate.
Zero-influence residual coordinates can be discarded without changing
either H or I. The three tested schedules are x-first, y-first, and
alternating x,y (then all remaining coordinates of the nonempty list).
Both constant-only and symmetric-threshold stopping are evaluated.

For m=2 there is also a closed **exact** expression for the entire
y-first tree, for every w,t>=1. Put q=2^-w, b=1-q,
beta=2q b^(t-1). The unchanged two x coefficients force kappa_min=3/4
throughout every y query. The weighted queried influence at each
position (j,u), j=0,...,t-1, u=1,...,w, is beta/2. Consequently

`Lambda_yfirst=(beta/2) sum_(j=0..t-1,u=1..w)
log2(1+(3/4) 2^(u-1) b^-(t-j-1))`. (8a)

After G is decided, the remaining OR/AND of two x signs contributes
zero Lambda (one child is constant at its first split). In the
symmetric-stopped version, the last position j=t-1,u=1 is skipped:
the remaining function is majority3 of three literals. These are the
only nonconstant symmetric stopping states prior to deciding G,
since a core with multiple tribes is nonsymmetric, and with one
tribe of width u>1 the y influence differs from the x influence.
Thus

`Lambda_yfirst,stop=Lambda_yfirst-(beta/2)log2(7/4)`,
`E I(leaf)=1+beta/2`, `E H(leaf)=2`. (8b)

The expressions in (8a)-(8b) are independently matched against all
small m=2 y-first tree log ledgers in the checker, including zero
coefficients and irrelevant residual coordinates.

## 3. All-width divergence for the actual Lambda on these schedules

Let w>=16 be an even integer, t=2^w, q=2^-w, b=1-q, and
G=Tribes_(w,t), positive when any all-positive tribe occurs. Use m=2
in (5). All `2+tw` inputs are uniform physical inputs. The tribes
influence is

`I(G)=tw beta`, `beta=2q b^(t-1)`,
`I(F)=(2+I(G))/2`. (9)

The following lower bound holds for **every fixed shuffle of the two x
queries with the contiguous, block-by-block y order**, hence for all
three specified schedules:

`Lambda_T/I(F) >= w/64`. (10)

It remains true when nodes with exact B_v=0 are assigned zero charge,
and when the tree stops whenever the remaining function is a symmetric
threshold. It is not a claim about every adaptive y order or every
possible stopping class.

### Good physical queries

Consider the first t/4 tribes, indexed j=0,...,t/4-1, and the first w/2
positions in each such tribe. Require earlier j tribes to have failed,
and the queried tribe's previous positions to have been all positive.
If u bits of that tribe remain before this query, then u ranges from
w down to w/2+1; there are exactly w/2 such positions. The other
`r=t-j-1>=3t/4` untouched tribes retain width w.

The probability of the stipulated y prefix is `b^j 2^-(w-u)`.
The influence of the queried core bit in this state is
`d=2^-(u-1) b^r`. Consequently the weighted pivotal mass is exactly

`b^j 2^-(w-u) d = beta`, (11)

independent of j and u. Summing over any already revealed x bits and
any nonconstant gate branches multiplies this by exactly alpha=1/2:
the bit is pivotal in F iff it is pivotal in G and x_1+x_2=0. All x
assignments are independent of the y prefix. Decisive x branches have
zero pivotal mass, so dropping their constant leaves changes nothing.

### Uniform child-defect bound

The elementary function `(1-1/N)^N` increases with N>=2: its derivative
in real N has sign `ln(1-1/N)+1/(N-1)>=0`, since
`-ln(1-z)<=z/(1-z)`. Exact integer arithmetic gives
`3*15^16>16^16`. Thus for w>=4, `b^t>1/3`.

At a good query, the child which kills the current tribe has no-active
probability `a_1=b^r`; the child which extends the positive prefix has
`a_0=(1-2^-(u-1))b^r`. The elementary bounds

`b^r<=exp(-rq)<=exp(-3/4)<1/2`,
`a_1>=b^t>1/3`, `a_0>=(7/8)b^t>7/24` (12)

hold because u-1>=7. The strict exponential upper bound uses only
`ln2<3/4`, which follows, for example, from the atanh series for ln2.
Both core children therefore have means in [0,5/12], in particular
absolute mean at most 1/2.

For a tribes sign with nonempty remaining widths, a nonconstant
coefficient has magnitude `2 product_(active blocks) p_h
product_(inactive blocks)(1-p_h)`, hence at most `2 max p_h`.
At these child states max p_h<=1/8, so all nonconstant squares are
at most 1/16. With the mean square <=1/4, both core children have
kappa>=3/4.

If neither x bit has been queried, the majority3 child has kappa=3/4
by (6). If both are queried and the x assignment is nonconstant,
the remaining function is G or a sign equivalent, so kappa>=3/4.
If one x bit has been queried, the remaining function is an OR/AND
gate of the other fair x sign and G. Its largest coefficient has
magnitude `(1+|mu_child|)/2`: the constant or remaining-x coefficient
has this magnitude, and every coefficient involving y has magnitude
at most 1/2. Thus its kappa is at least

`1-(3/4)^2=7/16`. (13)

This proves `kappa_min>=7/16` at every nonconstant good query in
every allowed shuffle. The queried influence j is unfolded here,
and is at most d<=2^-(u-1)<=1/8. Therefore

`log2(1+kappa_min/(2j)) >= u-1+log2(7/32) >= u-4 >= w/4`. (14)

The middle inequality uses `7/32>=1/8`, so is purely rational.
This is the **actual kappa** lower bound of LOG_ALLOCATION's charge,
not a replacement by a blind constant without justification.

### Stopping and exact-isospectral guards

At each good state the core has at least two surviving tribes, every
width at least two, and is not symmetric: compare an input with the
u positive signs concentrated in the smallest block to an input
with the same u positives split between two blocks without completing
either block. All other signs can be negative. The two inputs have
the same Hamming weight and different outputs. Every mixed nonconstant
gate branch restricts to this core on a suitable assignment of its
remaining x signs. A restriction of a symmetric function remains
symmetric on its remaining variables, so no such good node can be a
symmetric-threshold leaf.

Nor is a good query isospectral. Select a nonempty residual subset of
the queried tribe's unqueried bits. The two parent core coefficients
without/with the queried bit are equal and nonzero. Under a remaining
x gate, multiply them by any nonzero Fourier coefficient of its tie
indicator c; no g term can interfere because the residual y index is
nonempty. The corresponding erasure packet is strictly positive.
Thus zero-erasure skipping cannot erase the lower-bound queries.

The entire family is monotone in each physical sign. A nonconstant
monotone Boolean sign cannot be a product of two nonconstant signs on
disjoint physical blocks: a pivotal edge of one factor would reverse
its orientation when the other factor changes sign. Hence there is
no nonconstant physical spectator tensor factor to remove here.

### Sum and normalization

There are `(t/4)(w/2)` good positions. By (11)-(14), each contributes
at least `(beta/2)(w/4)` after averaging the independent x assignments.
Therefore

`Lambda_T >= (I(G)/2)(w/32)`.

Also `I(G)=2w b^(t-1)>=2w/3>2`. Dividing by (9) gives

`Lambda_T/I(F) >= [I(G)/(I(G)+2)] w/32 >= w/64`,

proving (10), with all influence included and no limiting numerical
sign assertion. Adding the nonnegative symmetric leaf certificates
cannot repair this lower bound.

For the y-first schedule the asymptotic is sharper. Expanding (8a)
using `log2(1+z)=log2 z+log2(1+1/z)` gives

`Lambda_yfirst/(I(G)/2)
=(w-1)/2+log2(3/4)-(t-1)log2(b)/2+R_w`,
`0<=R_w<=8/(3w ln2)`. (14a)

Indeed z>=(3/4)2^(u-1), so the remaining summand is at most
`(4/3)2^-(u-1)/ln2`; its u sum is at most 8/(3 ln2).
For t=2^w, `(t-1)(-ln b)=1+O(q)`, I(G)=2w/e+O(wq), and
I(F)=(2+I(G))/2. Therefore

`Lambda_yfirst/I(F)=w/2+O(1)`. (14b)

Stopping at the symmetric leaves changes Lambda by only beta times
a fixed constant, and adding 9 E I(leaf) changes this ratio by O(1/w).
Thus the same leading divergence holds for the certificate actually
using those leaves, not just the fully expanded tree.

## 4. True erasure plus the same leaves stays paid

Let a=b^t. The exact tribes formula from stage 1 is

`H(G)=phi((1-2a)^2)+8w a-8t(ba-a^2)log2 b-8(a-a^2)`.

Using `phi<=1`, `a>=1/3`, `-log2 b<=q/(b ln2)`, t q=1,
and `ln2>1/2`, discard only the negative final term and obtain

`H(G)/I(G) <= 4 + [3/2+4/ln2]/w < 4+10/w <=5` (w>=16). (15)

Here the leading ratio is 4b<=4. Equations (5) and (15) give
`H(F)<=5 I(F)` without using any formula-closure theorem.

At a genuine restriction tree, the exact decrement is B_v+JS_v
with JS_v>=0. Telescoping thus gives

`B_T+E H(leaf)<=H(F)<=5 I(F)`.

If the leaves are symmetric thresholds, replace their entropy by the
same certified bound `9 I(leaf)` used in the Lambda tree. Since
`E I(leaf)<=I(F)`, the true-erasure certificate satisfies

`B_T+9 E I(leaf) <=14 I(F)`. (16)

The standard paid JS contribution adds at most `(2/ln2) I(F)` if
one reconstructs an entropy bound from this stopping certificate.
Thus **the identical leaves and schedules have a bounded true bill
and an unbounded scalar Lambda bill**. The gap is at least linear
in width w, and survives isospectral skipping and spectator removal.

## 5. What remains universal

This disproves the claimed sufficiency of these schedules with only
the scalar logarithmic child-defect surrogate. It does not disprove
LOG_ALLOCATION's valid one-node upper bound, every adaptive choice of
y order, a richer certified leaf class, C019, or FEI. It provides an
exact arbitrary-core transport interface (1)-(4), plus a family on
which a proposed nonreusing charge must use the retained packet
profile rather than treating child defect alone as the unpaid bill.
The first unsupported universal line remains a hereditary coordinate
or stopping rule with a dimension-free payment of actual erasure
and terminal entropy. All bounded H/I facts above are used only to
identify overcharge, not to test Q/I as a proposed FEI disproof.

The arbitrary-core transport also gives a precise C018 admission
guard. For any Boolean seed h, tensor k independent copies, multiply
by one fresh literal z to balance, and call the resulting core G.
Then `H(G)=k H(h)`, `I(G)=k I(h)+1`, and `B(G)=k B(h)`:
tensor independence makes erasures add, and the literal spectral bit
is deterministic. For fixed even m, (2)-(4) imply

`B(F)/I(F)=k B(h)/(m+1+k I(h)) -> B(h)/I(h)`,
`H(F)/I(F)=[H(Maj_(m+1))/alpha+k H(h)]/(m+1+k I(h))
 -> H(h)/I(h)`. (17)

Constants h with I(h)=0 have B(h)=H(h)=0 and need no limiting ratio.
Hence the optimal universal erasure ratio is unchanged if one
restricts to these central-majority compositions with arbitrary
balanced cores. This is an equivalence/obstruction, not a solution:
retaining the core conditional erasure is essential in any proposed
hereditary transport through the first noncentral x-child.
