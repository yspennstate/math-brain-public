# The distinguished-block mass is bounded by a gap-weighted target collision

Date: 2026-08-16  
Status: exact finite-product reduction proved; no FPP estimate for the new
collision functional is claimed

Companions:

* `DISTINGUISHED_BLOCK_SPECTRAL_SPLIT_20260816.md`, SHA-256
  `f18916f69b7fbd24c96325ae3da9c046ba31152a893ca736fb11de737e083f0f`;
* `POSITIVE_PART_IS_GAP_CAPPED_20260815.md`, SHA-256
  `62dbe428dc02a4d4e1c38e0d546155a4e604c670c1fc6cd005b5d23f9471bafb`.

The first companion isolates the target-block spectral mass
`C_z+P_z`; the second proves that the positive replacement increment is
capped by the gap from the selected through-block route to the best route
avoiding the block.  Combining the two identities gives a more faithful
geometric target than unweighted route self-overlap: two paths share only the
target block, but their contribution is weighted by both avoidance gaps.

## 1. Exact gap-weighted collision

Fix a finite product of block-pair coordinates

`Y_i=(w_i,w_i')`.

For a label `L`, let `X` be the old passage time and `X^L` the passage time
after replacing the weights in `L` by `w_L'`.  Put

`z_L=(X^L-X)^+.`                                             (1)

For a fixed canonical old geodesic, let `U_L` be the event that it uses an
edge of `L`.  Split all routes according to whether they use `L` and write

`A_L=min passage time through L,`

`C_L=min passage time avoiding L.`

The avoiding cost is unchanged by replacement inside `L`.  On `U_L`,
`X=A_L<=C_L`; off `U_L`, the unchanged avoiding route shows `X^L<=X`.
Consequently, define `g_L=C_L-A_L` on `U_L` and `g_L=0` off `U_L`.  Then

one has the pointwise cap

`0<=z_L<=g_L.`                                               (2)

This remains valid with ties under a deterministic canonical selector.  If
the selector uses `L` in a tie, then `C_L-A_L=0`; if it avoids `L`, the
positive increment is zero.  If deleting `L` disconnects the endpoints, take
`C_L=+infinity`; the inequality remains an extended-value statement but gives
no finite certificate.  Such compulsory endpoint blocks must instead be put
in the exceptional set of the spectral companion.

Write `R_L=Y_(-L)` for all coordinates outside the target pair and define

`m_L(Y_L)=E[z_L|Y_L],      h_L(Y_L)=E[g_L|Y_L].`              (3)

The distinguished-block decomposition uses

`C_z=sum_L(E z_L)^2,`

`P_z=sum_L Var(E[z_L|Y_L]).`

Thus

`C_z+P_z=sum_L E[m_L(Y_L)^2].`                               (4)

Define the gap-weighted target collision

`Gamma_gap=sum_L E[h_L(Y_L)^2].`                             (5)

Then (2) gives the exact upper bound

`C_z+P_z<=Gamma_gap.`                                        (6)

Equivalently, conditionally on `Y_L`, take two independent outside
completions `R_L^1,R_L^2`.  If `g_L^i=g_L(Y_L,R_L^i)`, then

`Gamma_gap=sum_L E[g_L^1 g_L^2].`                            (7)

The two geodesics in (7) share only the original target-block weights.  The
replacement weights are also shared as part of `Y_L`, but `g_L` does not use
them.  Formula (7) is a collision mass, not generally a probability.

## 2. Relation to the raw self-overlap and moments

Let

`q_L(Y_L)=P(U_L|Y_L)=P(U_L|w_L),`

`P_self=sum_L E[q_L(Y_L)^2],`

`A_(4,gap)=sum_L E[g_L^4].`                                  (8)

Conditional Cauchy--Schwarz gives

`h_L(Y_L)^2
 <=q_L(Y_L) E[g_L^2|Y_L].`                                  (9)

Applying Cauchy--Schwarz over probability and labels, then conditional
Jensen, yields

`Gamma_gap<=sqrt(P_self A_(4,gap)).`                         (10)

Also, conditional Jensen alone gives

`Gamma_gap<=sum_L E[g_L^2].`                                 (11)

The direct quantity in (5) can be materially sharper than either bound.  More
importantly, it can decay even when `P_self` does not: the avoidance gap keeps
the magnitude discarded by an event-only overlap.

There is a separate exact influence comparison for the raw event.  Let
`I_L` be the probability that resampling only `w_L`, while keeping the outside
environment fixed, toggles `U_L`.  If `p_L=P(U_L)`, then

`E[q_L^2]<=p_L^2+(1/2)I_L.`                                  (12)

Indeed, for `f_L=1_(U_L)` and independent target values `w_L,w_L'`, Jensen
against the common outside environment gives

`Var(E[f_L|w_L])
 <=(1/2)E[(f_L(w_L,R_L)-f_L(w_L',R_L))^2]=(1/2)I_L,`

and `E[q_L^2]=p_L^2+Var(E[f_L|w_L])`.  In ANOVA language, the gap in (12) is
exactly the interaction mass involving both the target block and the outside
coordinates.  This comparison is useful diagnostically, but it drops the gap
weight and therefore need not be sharp enough for the variance engine.

## 3. Direct insertion into the spectral ledger

The distinguished-block companion proves, with `t=1-kappa`,

`Var(X_(Mn))
 <=(1+kappa)C_z+P_z+(kappa+t^r)V_z+c_r D_z.`                 (13)

Since

`(1+kappa)C_z+P_z<=(1+kappa)(C_z+P_z),`

equation (6) gives

`Var(X_(Mn))
 <=(1+kappa)Gamma_gap+(kappa+t^r)V_z+c_r D_z.`               (14)

For `D=Var(X_n)`, put

`gamma_gap=Gamma_gap/(M D),`

`upsilon=V_z/(M D),       Delta_out=D_z/(M D).`

A sufficient halving condition is therefore

`(1+kappa)gamma_gap
 +(kappa+(1-kappa)^r)upsilon+c_r Delta_out<=1/2.`             (15)

This does not prove any term in (15) is small.  It only identifies an exact
geometric replacement for the target main-effect obligation.  In particular,
small raw self-overlap is sufficient through (10), but it is not necessary.

## 4. Winner-take-all control

For `K>=2`, let `W_1,...,W_K` be iid uniform on `[0,1]`, let
`X=min_j W_j`, and replace
`W_j` by an independent `W_j'`.  For route `j`, set

`U_j={W_j=min_i W_i}`

and let `G_j` be the gap from `W_j` to the minimum of the other `K-1` costs on
`U_j`; set `g_j=1_(U_j)G_j`.

Conditional on `W_j=x`,

`h_j(x)=E[g_j|W_j=x]
 =integral_x^1 (1-u)^(K-1) du=(1-x)^K/K.`                   (16)

The replacement value `W_j'` does not enter `g_j`, so conditioning on the
full target pair gives the same function.  Hence

`Gamma_gap
 =K integral_0^1 ((1-x)^K/K)^2 dx
 =1/(K(2K+1))=Theta(K^(-2)).`                               (17)

The companion computes exactly

`C_z+P_z=K/((K+1)^2(2K+1)).`                                (18)

Therefore

`(C_z+P_z)/Gamma_gap=K^2/(K+1)^2 ->1.`                      (19)

The gap-weighted collision has not merely the correct order here; its relative
loss vanishes.  By contrast, the unweighted route self-overlap is

`P_self=K/(2K-1)->1/2.`                                     (20)

This control separates the intended mechanism cleanly.  More competing routes
do not make a selected route forget its own winning cost, but they shrink the
winning margin.  Equation (5) retains that shrinkage.

## 5. Scope and next obligation

The new target is to prove a strict estimate for `Gamma_gap` in lattice FPP,
at the actual tall-block geometry and scale used by the multiscale engine.
Confinement alone does not do this: it bounds where the path can travel but
does not bound the gap to the best block-avoiding competitor.  Nor does (12)
close the argument by itself; winner-take-all already shows that an
unweighted toggle estimate can lose the decisive gap scale.

The finite-window straight-path family remains the negative control.  Its
block use is deterministic, the avoiding gap is stable rather than small, and
neither raw nor gap-weighted collision supplies chaos.  A successful estimate
must therefore use genuine route competition, not only variance magnitude or
localization.

No estimate for lattice FPP, no variance-halving theorem, and no progress on
the exponent `chi=1/3` is claimed here.  An independent proof audit is required
before this note is used as a campaign dependency.
