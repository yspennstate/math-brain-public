# A rare coherent block funded by its original larger owner

Entropy is in bits on finite uniform cubes. Full FEI is OPEN. This stage consumes A059/A060 stage19: their reviews accept the earlier exterior pair module only, and their obstructions exclude universal length-priced and designated-pair-only admission. The result below uses neither of those failed admissions.

## 1. Exact character interface, including the old debit

Let Z be an exterior cube, C(Z) an indicator of density0<c<=1, and K(Z) zero on C and a sign off C. Let G(Y) be ANY independent Boolean sign. Let chi_J on a fresh nonempty physical block J be its full parity character. Set

    F=K+C G chi_J.

At every proper restriction of J, its remaining character is still nonempty. Its Fourier support is disjoint from the empty J-sector carrying K. The exact entropy is therefore

    H(F)=H_sub(Khat^2)+phi(c)+c H(Chat^2/c)+c H(G),       (1)

where H_sub(p)=sum p log2(1/p), without normalizing K's mass1-c, and phi(t)=t log2(1/t). This follows directly from the squared spectrum: empty-character sector Khat(s)^2, tagged sector Chat(s)^2 Ghat(T)^2. No independent copies or incoherent replacement are introduced.

Consequently any physical core Y-query while J remains nonempty has EXACT full decrement c D_iH(G), and querying a character bit while at least two remain has EXACT decrement0. These statements hold even for biased/nonflat G and both actual outcomes. They preserve all full exterior/core terminal functions. An actual old core query can have positive cost; its cost is at most2c, since every Boolean entropy split is at most2 bits.

## 2. The last character query is the coherent remainder

At a reached last-character state write alpha=E G, q=alpha^2. Pair the physical Fourier amplitudes by that bit. For a nonempty remaining core frequency T the pair is (0,Chat(s)Ghat(T)); it contributes zero erasure and zero JS. At T empty the pair is (Khat(s),alpha Chat(s)). Hence the ENTIRE full decrement is

    D_last=L(q)+J(alpha),
    L(q)=sum_s Phi(Khat(s)^2,q Chat(s)^2),                (2)

with Phi(a,b)=(a+b)log2(a+b)-a log2(a)-b log2(b), and J the actual coherent Jensen-Shannon packet of these same empty-core pairs. In particular D_last=0 when q=0, even if G is highly nonconstant. At q=1 it is the ordinary literal-splice decrement. Both child functions K+C G and K-C G are retained; their entropies are NOT dropped.

This is also the Brain/lead's original retained-log interface: L is nondecreasing, and L(q)<=min{L(1),q L(1)+c phi(q)}. To see the second bound directly, write Phi(a,qb)=phi(a)+phi(qb)-phi(a+qb), use phi(qb)=q phi(b)+b phi(q), and concavity phi((1-q)a+q(a+b))>=(1-q)phi(a)+q phi(a+b). Sum over s, where sum Chat(s)^2=c. Monotonicity follows from derivative b log2(1+a/(qb))>=0 for positive entries and continuity at zeros. Thus the retained q log(1/q) is the same exact coherent-composition term, not an unrelated rarity surrogate.

For q>0, Phi(a,b)<=b[1+ln(1+a/b)]/ln2. Use weights Chat(s)^2/c on nonzero rows, Jensen, and sum Khat^2=1-c to obtain

    L(q)<=cq[1+ln(1+(1-c)/(cq))]/ln2
         <=cq[log2(1/c)+log2(1/q)+1/ln2].             (3)

For the second inequality, 1-c+cq<=1. Omitted zero-Chat rows only decrease the numerator norm. For completeness the physical JS inequality follows by setting v=a^2+b^2 and r=2ab/v for a real amplitude pair: its natural-unit contribution is v[(1+r)ln(1+r)+(1-r)ln(1-r)]/2. The even bracket is at most1-sqrt(1-r^2): on r>=0 compare derivatives atanh(r)<=r/sqrt(1-r^2), whose difference has nonnegative derivative and is0 at0. Thus the packet is at most2 min(a^2,b^2)/ln2. Summing ONLY the empty-core pairs gives0<=J(alpha)<=2cq/ln2. Thus

    0<=D_last<=cq log2(1/c)+c phi(q)+(3/ln2)cq
              <=T(c,q):=c[q log2(1/c)+phi(q)+(9/2)q].  (4)

The last inequality uses ln2>2/3, proved by the first two positive atanh terms. The q log2(1/q) term is RETAINED, not replaced by O(q). This is the exact coherent remainder of(2), now with an explicit once-only payment. Endpoint q=0 uses literal zero packets, without logarithms at0.

When c=2^-m, m>=4, -q ln q<=1-q gives phi(q)<=(1-q)/ln2<=(3/2)(1-q). Therefore

    T(c,q)<=c[mq+(3/2)(1-q)+(9/2)q]<=c(m+9/2).       (5)

This bound is independent of the number of character coordinates, the dimension of G, and its Fourier entropy. Any adaptive character-query order or stopping frontier has at most one final query on each path, and all preceding character queries cost0. Ticket T(c,q) is constant during such proper character restrictions because alpha only changes by a sign. It pays the whole character block, with its actual terminal residual. No two-bits-per-coordinate allocation is needed.

## 3. Transfer from an ORIGINAL larger physical owner

Use A060's normalized non-hereditary family: m>=4 divisible by4, b(x)=(-1)^(sum x_(2j)x_(2j+1)), C=1_(x=1^m), c=2^-m, K=b-C. Then b(1^m)=1, so K is zero on C and a sign off C. Let F=K+C G chi_J, J ANY nonempty character block. At the original root the tag is balanced, so the actual X-block influence is

    I_X(F)=m/2-mc,
    B0=4 I_X(F)=2m-4mc.                                (6)

To check(6), each bent coordinate has influence1/2. At the exceptional all-one edge its old endpoint signs are opposite. Replacing b=+1 at the point by the balanced sign G chi_J removes c disagreements per coordinate. This is actual influence of F, not that of b or a phase surrogate.

Freeze B0 ONCE. Permit ONE specified actual core query i before any tag query, book its ACTUAL cost d_old=c D_iH(G)<=2c, and retain both full children. Each child has its actual restricted G_a and q_a=(E G_a)^2. Allocate T(c,q_a) from the SAME remaining B0-d_old, leaving the unused ORIGINAL cash B0-d_old-T(c,q_a) in that child. This allocation is funded because(5) gives

    d_old+T(c,q_a)<=c(m+13/2)<= (3/32)B0,
    B0-d_old-T(c,q_a)>=(29/32)B0.                       (7)

For the last inequality multiply by32: c(44m+208)<=6m. Equivalently2^-m(22+104/m)<=3, equality at m=4 and decreasing for integers m>=4. No floating-point sign or asymptotic extrapolation is used. In particular the new bill is not charged to the tiny designated tag influence |J|c, and not funded by a new source6 account.

On each actual old-query child allow ANY adaptive policy querying only J, with arbitrary stopping. Before the last remaining tag query retain the same T; at the last spend its ACTUAL D_last<=T and return unused T-D_last. All other inherited cash, full terminal exterior/core functions, and the complementary old-query child remain. Let B_v be the actual remaining sum of allocated tag ticket plus unused original cash after booked costs. The local-edge telescope is

    H(F_root)<=B0+E_leaf[H(F_leaf)-B_leaf],
    B_leaf>=(29/32)B0.                                 (8)

Book d_old at its actual node once (equally inherited cash B0-d_old in both children); all proper tag queries have zero debit; book the last actual decrement once and carry its unused ticket to BOTH full terminal children. This construction verifies(8) without assuming the terminal entropy is0 or discarding a favorable child. It also allows stopping on the old child without querying tags; that child simply returns its unspent allocation. The single old query is optional, but is executed with strictly positive cost in the certificates below.

The formula uses a separate original-owner cash allocation instead of replacing B_v by4 times the descendants' current X-influence. That replacement would lose the previously allocated tag payment and is not asserted. No X-coordinate is queried in this stage's NEW continuation. Arbitrary interleaved X queries after this transfer remain unpaid; the substantial remaining X/core entropy appears literally in(8). Thus this is a non-hereditary transfer after an old debit, not a proof of FEI.

## 4. Relation to the known obstructions and next unpaid line

For |J|=2,G=+1 this is exactly A060's relevant non-hereditary pair, whose pair-only price grows at least(m-1)/2. For general G and an actual positive core debit the same original larger owner still funds the current coherent bill, with uniform leftover29/32. Growing |J| creates no growing length price: all proper character queries are entropy isometries, and only the last query consumes the retained q-log ticket. The new proof is a physical coherent calculation and does not import the old private-controller or signed-DATA estimates.

This does not contradict sharp pair4/open2 for hereditary owners, source6-only exterior failure, or A059's length-admission obstruction. The interfaces and owners differ explicitly. It also does not price arbitrary core entropy: G can have arbitrarily large H(G), which remains in the complete terminal functions. The original X owner is genuinely present and large in this construction; an arbitrary Boolean gate need not supply such an owner.

Universal bridge: This stage advances C019 by funding an actual non-hereditary coherent character block after a positive internal debit from the SAME ORIGINAL larger physical owner4I_X, with at least29/32 left and BOTH full terminal profiles. The full q log(1/q) term is retained and paid once, independently of tag width. The first unpaid continuation is one X-query after this allocation, carrying CURRENT q, old core/tag bookings and this same remaining cash; a universal supplier for arbitrary exterior/core gates is also open. That X-query is the shortest next step toward a joint payment invariant: more rare-character examples alone would not connect the successful non-hereditary transfer to a complete physical restriction tree.
