# A058 handoff: affine-cylinder lifting

The affine positive class now includes internal physical directions.

For

`b(x,y)=1_A(y) g_y(x)`,

where `A` is affine and every `y` coordinate is transverse to it, if all
Boolean fibers satisfy `H(g_y)<=C I(g_y)`, then

`Eraw(b) <= C I_x(b)+4 I_y(b) <= max(C,4) I(b)`.

The proof retains the entire coherent affine-label spectrum.  With affine
dimension `d`, codimension `r`, and density `p`, it constructs a normalized
joint law `Q` and proves

`Eraw(b)=2rp+pH(Q)`,

`H(Q)<=2d+average_y H(g_y)`.

The internal and boundary influences are exact:

`I_x(b)=p average_y I(g_y)`,

`I_y(b)=(r+d)p/2`.

Thus both posterior label costs are paid once by the physical boundary.  The
constant 4 is sharp for point support.  When combined with the preceding
affine-collision theorem, this pays the coherent signed source term for the
corresponding Boolean overlap realization.

The class is restriction hereditary if the fiber class is.  X007 remains a
valid obstruction because its support is non-affine.

Next: derive or refute a two-piece affine-cylinder gluing lemma.  The extra
binary piece label must be charged to the physical edge boundary between the
pieces, not to the number of pieces or restriction depth.  Preserve X007 and
the signed-mask tensor family as controls.

Independent review is pending.  Full FEI is open.

