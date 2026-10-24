# Independent analytic audit of the all-graph high-fugacity forest proof

2 October 2026. Auditor: the independent queueing-research agent, reassigned
to the forest argument. This record concerns the mathematics, not historical
novelty. No numerical example or finite enumeration is used as a substitute
for an argument below.

## Verdict and reviewed scope

**PASS.** I read `ALL_GRAPH_HIGH_FUGACITY_PROOF.md` completely, as well as the
earlier assembly, the complete general H2 and H3 proofs, and the independent
local-transfer and range-closure audit notes. I found no analytic gap in the
assembled theorem: for each fixed finite graph and fixed positive conductance
vector, every marked forest-edge pair has nonpositive covariance at all
sufficiently large common fugacities. The proof gives eventual strictness for
edges on a common cycle, and exact independence for different graphic-matroid
components.

The main new claims I checked independently are the delayed-order cross
coefficients, the normalized transfer of the **original marked score**, and
the preservation of its full port contrast range. Their combination really
does give a finite induction. The conclusion is about sufficiently large
fugacity; it does not settle the all-fugacity forest conjecture, negative
association, or the positive-q random-cluster conjecture.

## 1. Activity conversion and the exact covariance identity

The relation

\[
 R_{ef}(\lambda c)=-\lambda^{2n-4}\tau^2F(t)^2
 \partial_{ef}(\log\tau+\log F(t)),\qquad t=\lambda^{-1},
\]

has the correct two conductance-to-activity factors. In particular the
factor `F(t)^2` can be ignored when finding the first nonzero mixed logarithmic
coefficient, but only because all its earlier mixed coefficients have already
vanished. The final proof applies this condition at every stopping stage.

The Gaussian covariance and harmonic rows in the separator reduction are
fixed under each marked variation. Compact support of the original electrical
current implies equality of the marked endpoint harmonic rows, so both the
Schur-complement derivative and the harmonic-extension derivative vanish.
Consequently the exact mixed derivative is the normalized formal covariance
of the two local marked scores. This remains true after enlarging the
interiors: the original current is still compactly supported there.

All these expectations are finite Grassmann Wick functionals or formal
series. Neither the covariance calculation nor its subsequent use requires a
positive measure on Grassmann variables.

## 2. Independent delayed-order cross calculation

Suppose the exact local scores have first boundary-dependent terms

\[
 U_e=C_e(t)+t^\ell Q_{B_e}+t^{\ell+1}P_e+O(t^{\ell+2}),
 \qquad
 U_f=C_f(t)+t^\ell Q_{B_f}+t^{\ell+1}P_f+O(t^{\ell+2}).
\]

The scalar series disappear from every connected covariance, including
under the normalized tilt. Thus there are no cross coefficients before
`2 ell`. Wick's bilinear covariance gives

\[
 [t^{2\ell}]\partial_{ef}\log F
 =-\operatorname{tr}(TB_eTB_f).
\]

For Gram charges `rho` and `sigma`, this is minus the sum of
`(rho^T T sigma)^2`. The full-range assumption is essential here: zero trace
then means that *every* contrast on the old e ports is Green-orthogonal to
*every* contrast on the old f ports, rather than just orthogonality of a
possibly deficient response family. It implies that the two port sets share
at most one vertex. Choosing the root in the e ports outside the f ports is
therefore legitimate unless a one-port stop has already occurred.

At that root, the grounded f response is zero on the e ports and e interior,
while the grounded e response is a constant `k_rho` on the f ports and f
interior. At order `2 ell+1` the normalized covariance has exactly

\[
 \operatorname{Cov}(P_e,Q_{B_f})+
 \operatorname{Cov}(Q_{B_e},P_f)+
 \operatorname{Cum}(Q_{B_e},Q_{B_f},W_1).
\]

There is no `ell` multiplier and no contribution of any later tilt
coefficient. I checked the three terms without assuming that `P_e` or `P_f`
has only quartic degree:

* The first covariance is zero. Rank-one precision differentiation by an
  f charge changes the covariance restricted to the e ports by minus its
  response potential outer product, which is zero there. This kills the
  covariance of **any** polynomial on those ports.
* The second covariance is the constant-mode correction
  `sum_rho k_rho^2 tr(T B_f)`. The exact Ward identity gives
  `D_1 P_f=-Q_(B_f)`, and covariance differentiation in direction
  `-k_rho^2 11^T` produces this positive sign.
* The bilinear part of `W_1` has zero third cumulant. With the positive
  covariance whitening, trace zero for the two PSD response matrices forces
  their product to be zero, annihilating the cyclic third-cumulant traces.
  The quartic part of `W_1` is minus the uncontracted original edge quartics;
  its Wick cumulant is the square of the unshifted electrical wedge, with
  no extra factor of two.

For completeness, write the unshifted wedge flow of a charge pair as
`j_xy=c_xy(a_x b_y-a_y b_x)`, where `a=k_rho` on the opposite ports and
`b=0` on the first ports. Its divergence is `-k_rho sigma`. The electrical
flow `i_xy=c_xy(b_x-b_y)` has divergence `sigma`, and therefore

\[
 \langle j,i\rangle_{c^{-1}}=-k_\rho\mathcal E(b),
 \qquad
 \|j+k_\rho i\|_{c^{-1}}^2
 =\|j\|_{c^{-1}}^2-k_\rho^2\mathcal E(b).
\]

This completes exactly the constant-mode correction above. The resulting
flow is the wedge formed with `alpha=a-k_rho` and `beta=b`, so the negative
odd mixed coefficient is precisely the sum of shifted wedge energies in
the final proof. The calculation uses only the displayed two score orders
and the first tilt coefficient; it is valid for every delayed order `ell`.

## 3. Exact normalization in the absorption step

This is the point at which an approximate response recursion would be
insufficient. Eliminating the old interior first gives a fixed outer Gaussian
law on the added vertices, conditional on the new free ports. The local
partition obeys an exact identity of the form

\[
 M_{I'}=\mathbb E_{\rm outer}
       [e^{tV_{\rm added}}M_I].
\]

The covariance and conditional mean of the outer law have zero marked
derivative because the old Schur data have zero marked derivative. The
determinant identity has the old determinant times the outer Schur
determinant; only the former has a marked derivative, already included in
the definition of the old normalized score. Differentiating the displayed
identity consequently gives

\[
 U'_e=
 \frac{\mathbb E_{\rm outer}
 [e^{tV_{\rm added}}M_I U_e]}
 {\mathbb E_{\rm outer}[e^{tV_{\rm added}}M_I]}.
\]

Thus the transferred object is exactly the original marked derivative of
the enlarged intrinsic partition. There is no omitted derivative of a
boundary-dependent normalizer and no replacement of the original mark by a
new auxiliary observable.

The use of all free ports is necessary. The convenient ground used for
the odd cross calculation may be absorbed into the next interior. The
intrinsic identities above are formed before grounding, so one may choose a
new global ground afterwards. A uniform translation through a previously
fixed zero root field would not justify this step; the final proof does not
make that substitution.

## 4. The transferred leading coefficient and its degree

All old port harmonic rows become a common row `pi_e`. This follows from
`rho^T h=alpha^T Lh=0` for every new harmonic extension and every old contrast
charge. Write each old port field as its fluctuation plus the same harmonic
field `h`. Since `B_e 1=0`, the old leading bilinear is then a polynomial of
the fluctuations alone. Its conditional mean at order `ell` is scalar.

At order `ell+1`, normalized averaging gives only the expectation of `P_e`
and the connected covariance of `Q_(B_e)` with the first local tilt. The
Ward decomposition is

\[
 P_e=\sum_{a<b}(B_e)_{ab}q_aq_b+R_e,
 \qquad Q_0R_e=\bar Q_0R_e=0.
\]

Ordinary translation invariance makes `R_e` unchanged by the common
harmonic field, even if `R_e` has degree higher than four. It therefore
contributes only a scalar. The Ward quartic contributes the boundary
bilinear

\[
 -\operatorname{tr}(C_{AA}B_e)q(h),
\]

using zero row sums to combine
`sum_(a<b) B_ab(C_aa+C_bb-2C_ab)`. Its degree-four boundary part vanishes
because `q(h)^2=0`. A bilinear first tilt contributes only a scalar connected
covariance; all its harmonic parts factor or have odd fluctuation degree.

The uncontracted quartic tilt contributes the raw positive Gram of
`alpha_x p'_y-alpha_y p'_x`. All previously contracted old-interior terms
are of bilinear or scalar degree, so they supply no missing boundary Gram.
The uncontracted old terms together with the added terms exhaust the
original edges incident to the new interior. The fluctuation response is
the physical `alpha`, by uniqueness of the Dirichlet equation with zero
values outside that interior.

For a new boundary value vector `z`, its harmonic extension `h` gives a
raw flow with divergence `(pi_e z) rho`. Its energy projection onto the
electrical rho flow is exactly `(pi_e z)` times that flow. Subtracting it
removes the Ward energy term. The surviving coefficient is therefore the
Gram of

\[
 \alpha_xp'_y-\alpha_yp'_x
       -(\alpha_x-\alpha_y)\pi_e.
\]

This proves its PSD sign, its exact order `ell+1`, and its purely bilinear
boundary degree. It establishes the coefficient map required by the
induction, rather than just a plausible electrical analogue.

## 5. Support, range, base exceptions, and termination

When both cross expressions vanish, every charge-pair wedge vanishes on
every original edge. A connected nonaxis projective support component could
meet neither set of source ports, because the opposite response is zero
there. Both responses would then be harmonic with zero exterior values,
contradicting the maximum principle. Thus their nonzero supports are
disjoint and have no joining edge. Each support component meets an old
source port and attaches to its connected old interior. Each nonzero charge
family also absorbs at least one old port. This gives connected, disjoint
enlarged interiors and a nonempty remaining separator.

I checked the range conclusion also for old dormant interior vertices and
old zero-response ports. If the transferred Gram vanishes on a boundary
vector, its harmonic extension minus the common old-port value has zero
wedge with every absorbed response. It is zero at an old source port in
each nonzero support component, so it is zero on that whole component.
Every new port adjacent to such a component is forced to have the same
value. A new port adjacent only to the dormant old interior was already an
old port and hence has that value as well. Conversely a constant on the
new geometric ports annihilates every Gram row. This proves exactly the
full contrast range, with no assumption about off-diagonal signs of the
response matrix.

The final base case also treats a zero-potential marked endpoint. Its
block current equation makes the other endpoint's harmonic exit row the
coordinate row of that one port. Every geometric port has strictly positive
exit probability from that endpoint in a connected positive-conductance
interior. Hence this case has only one port and exact forest factorization;
it cannot be silently admitted as a two-endpoint interior. With both
endpoints nonzero, their marked edge connects the original support, and
the audited H2 local calculation supplies the initial full-range invariant.

One-port Ward invariance makes the entire marked score scalar, since
`1-tq` is invertible in the exterior algebra. Otherwise every continuing
zero-zero step enlarges both disjoint interiors. Finiteness therefore
forces a positive cross coefficient or an exact one-port factorization.
A common simple cycle cannot traverse a one-port cut to reach both marked
interiors. These observations establish the eventual strictness assertion
and the exact stopping alternatives.

## 6. What would be needed beyond high fugacity

The proof does not control the sign of all later coefficients after its
first positive Rayleigh coefficient. A finite polynomial with a positive
leading coefficient can change sign at smaller positive arguments. The
normalized Grassmann tilt is not a positive measure that would turn the
leading Gram into an inequality at arbitrary `t`. The absorption recursion
is triggered by exact zero leading responses; it is not a finite-t
monotonicity argument.

One possible focused next question is the exact two-port marked score.
With two free ports, an even, charge-balanced Ward-invariant raw local
polynomial has the form `A(t)+B(t) F_ab(t)`, with
`F_ab=q(psi_a-psi_b)-t q_a q_b` and `F_ab^2=0`. Thus its marked score is a
scalar plus `partial_e(B/A) F_ab`. Establishing a nonperturbative sign
inequality for that scalar response ratio could address restricted
separator or series-parallel settings. I have not established that
inequality, and arbitrary multiport interiors admit further invariant
Grassmann terms, so this observation is not an all-graph extension.

For a fixed pair the current theorem can give an explicit, usually crude
threshold once its polynomial coefficients are known. If
`R(lambda c)=H_d lambda^m+sum_(j>=1) H_(d+j) lambda^(m-j)` with `H_d>0`,
then

\[
 \lambda\ge\max\left\{1,
   2\sum_{j\ge1}|H_{d+j}|/H_d\right\}
\]

ensures that the later terms have absolute sum at most half the leading
term. This is only a pair-specific domination bound; it does not remove
the high-fugacity qualification. I found no justified route from the
present induction alone to a proof at all fugacities.
