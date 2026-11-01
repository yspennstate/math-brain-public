# Width-two Bellman reduction to universal GU

Let

\[
q(t)=t\log_2(1/t)+\frac{2t}{\ln2},\qquad
L_c=M+2U-cI,
\]

and let `Theta_Y` be the reviewed physical-orbit potential.  At a restriction
node with inherited block `Y`, query `x`, and branch-specific child blocks
`Z_+`, `Z_-`, the exact signed opening/reveal identity gives the node charge

\[
\mathcal C(f,Y;x,Z_+,Z_-)=
\Delta_xL_c(f)+2\Theta_Y(f)
-\Theta_{Z_+}(f_{x=+1})-\Theta_{Z_-}(f_{x=-1}). \tag{1}
\]

No terminal reserve or normalization is omitted.

Fix

\[
c=c_*:=\frac{29}{2}+\frac4{\ln2}. \tag{2}
\]

For `|Y|<=2`, define

\[
\mathcal E_2(f,Y)=
\min_x\min_{|Z_+|,|Z_-|\le2}
\mathcal C(f,Y;x,Z_+,Z_-). \tag{3}
\]

Because the two child terms enter with negative signs, (3) is equivalently

\[
\min_x\left\{\Delta_xL_c(f)+2\Theta_Y(f)
-\max_{|Z_+|\le2}\Theta_{Z_+}(f_{x=+1})
-\max_{|Z_-|\le2}\Theta_{Z_-}(f_{x=-1})\right\}. \tag{4}
\]

Assume the universal local statement

\[
\mathcal E_2(f,Y)\le0 \tag{W2B}
\]

for every nonconstant finite-cube Boolean `f` and every `|Y|<=2`.

Start at `(f,emptyset)`.  At every nonconstant node choose a query and the
two child blocks supplied by (W2B).  Each child has one fewer input, so the
construction terminates after finitely many levels.  Multiply (1) by the
path probability and sum over internal nodes.  The ordinary `L` restriction
telescope and the reviewed signed-orbit telescope cancel all intermediate
child terms.  Constant leaves have `L=Theta=0`.  Hence

\[
L_{c_*}(f)+2\Theta_\varnothing(f)le0. \tag{5}
\]

At empty history `Theta_empty=Phi>=0`, so (5) implies

\[
M(f)+2U(f)\le c_*I(f). \tag{6}
\]

The reviewed pair-entropy estimate `B(f)<=2I(f)` and `G=M+B` then give

\[
G(f)\le(c_*+2)I(f)
=\left(\frac{33}{2}+\frac4{\ln2}\right)I(f). \tag{7}
\]

Thus (W2B) is sufficient for GU with `b=0`; the recorded GU reduction yields

\[
H(f)\le(2+2(c_*+2))I(f)
=\left(35+\frac8{\ln2}\right)I(f). \tag{8}
\]

If `I(f)=0`, Booleanity makes `f` constant and every quantity above is zero.

The proof establishes only the implication `(W2B) => GU => FEI`.  The sign
in (W2B) remains unproved in arbitrary dimension.
