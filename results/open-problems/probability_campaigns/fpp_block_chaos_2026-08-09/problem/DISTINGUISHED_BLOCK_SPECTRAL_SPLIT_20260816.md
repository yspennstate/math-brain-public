# Isolating the compulsory target-block query

Date: 2026-08-16  
Status: exact finite-product spectral lemma proved; the target-main-effect and
conditional-revealment estimates needed for FPP remain open

Companion: `BLOCK_INCREMENT_NOISE_SPLIT_20260816.md`, SHA-256
`c106b719e76e584157c36a840a55fbb3c68571e0b4386ff509bec699366f0de0`.

The positive increment

`z_L=(X^L-X)^+`

has a distinguished product coordinate: the original--replacement pair in
block `L`.  An exact algorithm may have to inspect that coordinate, so applying
Schramm--Steif with the maximum revealment over all coordinates can charge one.
This note conditions on the distinguished coordinate first.  Only its pure
one-coordinate ANOVA mass remains unsmoothed; interactions with the rest of the
environment can still be controlled by conditional revealment.

## 1. A distinguished-coordinate lemma

Let `Omega=Omega_j x product_(i in J) Omega_i` be a finite product probability
space and let `f` be real and square integrable.  Write its Hoeffding--ANOVA
decomposition as

`f=sum_(S subseteq {j} union J) f_S.`                          (1)

Define the pure distinguished-coordinate mass and the remaining variance by

`P_j(f)=||f_{ {j} }||_2^2=Var(E[f|omega_j]),`                 (2)

`V_j(f)=E[Var(f|omega_j)]
      =sum_(S: S intersect J != empty)||f_S||_2^2.`            (3)

After observing `omega_j=u`, suppose a zero-error randomized adaptive algorithm
determines the slice `f_u` by querying coordinates in `J`.  Its private
randomness is independent of the product variables.  Put

`delta(u)=max_(i in J) P(i is queried | omega_j=u)`

and

`D_j(f)=E[delta(omega_j) Var(f|omega_j)].`                     (4)

Then, for every integer `k>=1`,

`sum_(S: |S intersect J|=k)||f_S||_2^2 <= k D_j(f).`           (5)

This is the Schramm--Steif level estimate with the compulsory query removed
from the revealment maximum.

### Proof

For `B subseteq J`, the `B`-component of the conditional slice `f_u` is

`(f_u)_B=f_B+f_(B union {j})(u,.)`.

The two terms are orthogonal after integration in `u`, because every ANOVA
component containing `j` has mean zero in that coordinate.  Hence

`E_u ||(f_u)_B||_(L2(Omega_J))^2
 =||f_B||_2^2+||f_(B union {j})||_2^2.`                        (6)

For fixed `u`, apply the usual product-space Schramm--Steif estimate to the
algorithm determining `f_u`:

`sum_(|B|=k)||(f_u)_B||_2^2
 <=k delta(u) Var_(Omega_J)(f_u).`

Integrating in `u` and using (4)--(6) proves (5).  No discretization of the
distinguished block law is used.

Let `Y^(t)` retain every product coordinate of `Y` independently with
probability `t` and otherwise resample it.  For any integer `r>=2`, put

`c_r=r(r-1)/2.`                                                (7)

The ANOVA noise identity, split according to the number of coordinates from
`J`, and (5) give

`E[f(Y)f(Y^(t))]
 <=(E f)^2+t P_j(f)+(t^r V_j(f)+c_r D_j(f)).`                  (8)

Indeed, the nonconstant term supported only on `j` has noise weight `t`.
Terms using between one and `r-1` coordinates from `J` cost at most the sum of
(5), while every term using at least `r` such coordinates has weight at most
`t^r`.  A term may also use `j`; that only gives it one additional factor of
`t` and cannot weaken the upper bound.

The same proof works for a fixed exceptional set `E` in place of `{j}`.
Condition on all coordinates in `E`, define
`P_E(f)=Var(E[f|omega_E])` and `V_E(f)=E[Var(f|omega_E)]`, and run the
algorithm only on the complementary coordinates.  For a complementary support
`B`, integrating the slice component sums the squared norms over every
`A subseteq E` by ANOVA orthogonality.  The pure exceptional terms have noise
weights at most `t`, so (8) holds with `P_E,V_E,D_E`.  This permits a bounded
set of compulsory endpoint queries to be pre-revealed, at the explicit price of
their larger pure-exceptional mass.

## 2. The positive block increments

Use the product coordinates `Y_i=(w_i,w_i')` from the companion note.  For each
label `L`, take `j=L` in the lemma and define

`P_L=Var(E[z_L|Y_L]),          V_L=E[Var(z_L|Y_L)].`           (9)

Let a conditional algorithm, after seeing `Y_L`, determine `z_L` from the
other pair coordinates, and define `D_L` by (4).  Sum the quantities as

`C_z=sum_L(E z_L)^2,   P_z=sum_L P_L,`

`V_z=sum_L V_L,        D_z=sum_L D_L.`                        (10)

There are two exact identities:

`A_2^+=sum_L E[z_L^2]=C_z+P_z+V_z,`                           (11)

and, for two conditionally independent copies of the coordinates outside `L`,

`(E z_L)^2+P_L
 =E[z_L(Y_L,Y_(-L)^1) z_L(Y_L,Y_(-L)^2)].`                   (12)

Thus `C_z+P_z` is a target-sharing weighted collision: the two increments share
only their own original--replacement pair and have independent environments
elsewhere.

Summing (8) over `L` gives the refined noise bound

`S_z(t)<=C_z+t P_z+t^r V_z+c_r D_z.`                          (13)

The engine inequality in the companion note is

`Var(X_(Mn))<=kappa A_2^+ + S_z(1-kappa).`

Using (11)--(13), with `t=1-kappa`, yields

`Var(X_(Mn))
 <=(1+kappa)C_z+P_z+(kappa+t^r)V_z+c_r D_z.`                  (14)

The coefficient of `P_z` is exactly one: the engine time split contributes
`kappa P_z`, while the shared-noise term contributes `t P_z`.  Querying the
target block first therefore removes a false revealment obstruction, but it
does not make the target main effect disappear.

For `D=Var(X_n)`, define

`iota=C_z/(M D),   pi=P_z/(M D),`

`upsilon=V_z/(M D),   Delta_out=D_z/(M D).`

A sufficient variance-halving criterion is

`(1+kappa)iota+pi+(kappa+(1-kappa)^r)upsilon
  +c_r Delta_out <=1/2.`                                     (15)

This retains the exact moment ledger
`iota+pi+upsilon=A_2^+/(M D)`.  Unlike a maximum-revealment statement, the
criterion does not automatically fail merely because the algorithm always
reads `Y_L`.

## 3. The target main effect is a one-block overlap

The target-sharing term has an exact local overlap bound.  Let `U_L` be the
event that the fixed canonical old geodesic uses block `L`.  The companion note
proves `z_L=1_(U_L)z_L`.  Set

`q_L(Y_L)=P(U_L|Y_L)=P(U_L|w_L),`                             (16)

`P_self=sum_L E[q_L(Y_L)^2],`

`A_4^+=sum_L E[z_L^4].`                                      (17)

The replacement reservoir in `Y_L` is independent and `U_L` only uses the old
environment, which gives the second equality in (16).  If

`m_L(Y_L)=E[z_L|Y_L],   e_L(Y_L)=E[z_L^2|Y_L],`

then conditional Cauchy--Schwarz gives

`m_L(Y_L)^2<=q_L(Y_L)e_L(Y_L).`                              (18)

Using (12), Cauchy--Schwarz first for each label and then over labels, followed
by conditional Jensen, yields

`C_z+P_z=sum_L E[m_L(Y_L)^2]
 <=sum_L sqrt(E[q_L^2] E[e_L^2])
 <=sqrt(P_self A_4^+).`                                      (19)

This overlap has a direct coupling interpretation.  In its `L`th summand, two
old environments share only `w_L` and are independent outside it; `E[q_L^2]`
is the probability that both canonical geodesics use `L`.  It also has the
exact ANOVA split

`E[q_L^2]=P(U_L)^2+Var(E[1_(U_L)|w_L]).`                     (20)

The first term is the independent-route collision floor.  The second measures
the route's self-attraction to its own block weights.  No other shared
environment appears, so `P_self` is a strictly more local obligation than the
full conditional block-overlap gate in the old fourth-moment factorization.
The sum `P_self` is a collision mass, not generally a single probability, and
it is not automatically small: in the straight-path control every `q_L=1`.

There is also an exact comparison with the old full block-use noise mass.  If

`Pbar_U(t)=sum_L E[f_L(Y)f_L(Y^(t))],   f_L=1_(U_L),`

then ANOVA positivity gives, for every `0<t<=1`,

`P_self<=t^(-1) Pbar_U(t).`                                  (21)

Indeed, the `L`th noise mass contains `p_L^2` and also the pure-coordinate
term `t Var(E[f_L|Y_L])`; together these dominate
`t(p_L^2+Var(E[f_L|Y_L]))=t E[q_L^2]`.  Thus the self-conditioned requirement
is genuinely weaker than full block chaos.  The converse need not hold because
`P_self` sees none of the ANOVA interactions involving other blocks.

For example, if the corrected moment route supplies

`A_4^+<=kappa_4 beta^2 C_occ M D^2`

and one proves

`P_self<=epsilon_self M,`                                    (22)

then (19) gives

`(C_z+P_z)/(M D)
 <=sqrt(kappa_4 beta^2 C_occ epsilon_self).`                  (23)

In particular, the first two terms in (14) obey

`(1+kappa)C_z+P_z
 <=(1+kappa)M D
    sqrt(kappa_4 beta^2 C_occ epsilon_self).`                 (24)

This is still conditional: it trades full shared-environment chaos for a
one-block self-selection estimate and leaves the outside-interaction
revealment term untouched.

## 4. Winner-take-all control: keep the increment weight

The quantity `P_self` need not itself become a chaos parameter even in the
simplest competitive model.  Let `W_1,...,W_K` be iid uniform on `[0,1]`, set
`X=min_j W_j`, and let block `j` replace `W_j` by an independent `W_j'`.
The selected route uses `j` exactly when `W_j` is the minimum.  Conditional on
`W_j=x`,

`q_j(x)=P(j is selected|W_j=x)=(1-x)^(K-1),`

so the summed self-overlap is

`P_self=K E[q_j(W_j)^2]=K/(2K-1) ->1/2.`                     (25)

It does not become small as the number of competing routes grows.

For the positive replacement increment `z_j=(X^j-X)^+`, however, conditioning
on `W_j=x,W_j'=x'` gives

`m_j(x,x')=E[z_j|x,x']
 =1_(x'>x) ((1-x)^K-(1-x')^K)/K.`                            (26)

Indeed, if `Y` is the minimum of the other `K-1` costs, the conditional
increment is `(min(x',Y)-x)^+`, whose tail integral from `x` to `x'` is (26).
A direct integration gives

`C_z+P_z=K E[m_j(W_j,W_j')^2]
 =K/((K+1)^2(2K+1))=Theta(K^(-2)).`                          (27)

For completeness, the integral is

`K^(-2) integral_(0<b<a<1) (a^K-b^K)^2 db da
 =1/((K+1)^2(2K+1))`

for each label.  The fourth moment retains the same gap information: the tail
identity

`P(z_j>u)=(1-u)^(K+1)/(K+1)`

gives

`A_4^+=K E[z_j^4]=24K K!/(K+5)!=Theta(K^(-4)).`               (28)

Consequently the sufficient bound `sqrt(P_self A_4^+)` in (19) also has the
correct `K^(-2)` order in this model, despite `P_self` staying bounded away
from zero.  The honest lesson is that a successful FPP argument must preserve
the small route-gap magnitude inside `z_L`, either directly in `C_z+P_z` or
through a sharp increment moment.  Proving unweighted self-chaos is not a
necessary intermediate goal; combining a constant-scale fourth-moment bound
with a demand that `P_self` itself be tiny may be unnecessarily strong.

## 5. What remains geometric

The reduction exposes two separate obligations.

1. Prove a strict bound on the target-sharing collision `C_z+P_z`, either
   directly or through (19) while retaining a sharp increment moment.  Making
   the self-conditioned overlap `P_self` itself tiny is only a sufficient route,
   not a necessary one.
2. Given the target pair, construct exact conditional algorithms with small
   variance-weighted outside revealment `D_z`, or develop the approximate
   transcript analogue of (5).

Neither follows from confinement alone.  A localization tube limits where a
geodesic can be, but an exact shortest-path certificate may still inspect most
of that tube.  The fixed-endpoint blocks near the endpoints can also have high
conditional revealment.  They may be placed in the exceptional set described
after (8), but the resulting pure-exceptional mass must then be bounded rather
than hidden inside a global maximum.

The straight-path model is the necessary negative control.  There each `z_L`
depends only on `Y_L`, so `V_L=D_L=0` and all of its nonconstant variance is
`P_L`.  Equation (14) gives that mass coefficient one, exactly matching the
absence of block chaos.

This note proves only the finite-product reduction.  It neither supplies the
two FPP estimates above nor establishes variance halving.  An independent proof
audit is required before it is used as a campaign dependency.
