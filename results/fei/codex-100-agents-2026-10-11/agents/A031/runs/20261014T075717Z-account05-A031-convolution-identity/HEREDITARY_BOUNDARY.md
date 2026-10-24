# A fixed root private budget cannot be replaced by a fresh child private budget

This is an actual all-width Boolean family, not a numerical extrapolation.
Start with the triangle widths(1,L,L), L>=1. Query the sole X1 bit and
take the outcome0, of physical reach1/2. The inherited clauses are
E1={a,c}, E2=X2 union{a,b}, E3=X3 union{b,c}. Write q=2^-L.
The signed inclusion-exclusion expansion(1) of DERIVATION.md gives exactly

    a_c=a_a=-1/2, a_ac=-(1-q)/2.

Pair23 and triple terms CANCEL before squaring. The remaining private
coordinates each have influence q/4 (gamma=1/8 since q1=1), hence

    I_private(child)=Lq/2.

At the shared a edge with lower residual label c, the oriented cost is
p_ac log2(1+p_c/p_ac). Since p_c=1/4 and p_ac=(1-q)^2/4,
the logarithm is at least1. The symmetric shared c edge gives another
copy. Therefore

    M_shared(child)>= (1-q)^2/2,
    M(child)/I_private(child)>= (1-q)^2/(Lq) ->infinity.     (1)

This refutes every fixed coefficient on a newly computed child PRIVATE
influence budget after width exhaustion, even though the parent has
M(parent)<17 I_private(parent) and a lossless width-independent trace.
It does NOT refute a budget carried from the parent, nor an I_TOTAL bill:
the child shared influences remain order one. In fact querying all three
shared coordinates first gives one of only eight disjoint-product/private
terminal forms; nothing here is an FEI counterexample or an all-policy
obstruction. The exact source owner and its already used fraction must
remain separate from new child influence.

The lossless local child trace thus survives, but the private-owner
admission needed for the root payment does not. NEXT must price the
actual incoming-reference change and surviving terminal rows from the
original unused bank, or choose an exposure policy before exhausting
that owner's private width. A fresh sufficient child reference is not a
new reserve. This is the same hereditary issue exposed independently by
A035's incoming delta-minus-K identity; it is a distinct triangle witness.
