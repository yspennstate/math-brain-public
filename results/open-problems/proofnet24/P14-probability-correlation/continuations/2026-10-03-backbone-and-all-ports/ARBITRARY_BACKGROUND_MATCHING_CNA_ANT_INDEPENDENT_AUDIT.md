# Independent audit: arbitrary-background matching negative association

2 October 2026. Auditor: `/root/antivoter_audit`.

**PASS within the written restricted-family scope.** I read the full
`forest_matching_arbitrary_background_logconcavity_extension.md`, the
actual exact checker and saved results, and reread the complete forced-
subset/OR argument in
`forest_rank_one_core3_matching_negative_association_proof.md`.
I independently verified the primary log-concavity input and its exact
normalization, rederived the new closure identity, checked the complete
matching law and conditioning closure, and built a separate exact checker
without author imports. No mathematical gap was found.

This is negative association of the selected matching-indicator vector,
including the specified conditioning and fields. It is not negative
association of all graph edges or of the arbitrary background's edge
vector, and it does not solve the unrestricted forest conjecture.
Historical novelty and external acceptance remain unverified.

## 1. Actual primary theorem and normalization

I independently opened the full primary PDF
[Anari–Liu–Oveis Gharan–Vinzant, arXiv:1811.01600](https://arxiv.org/pdf/1811.01600).
Its first page identifies v1. Theorem 4.1, printed page 8, displays

\[
g_M(y,z)=\sum_{I\text{ independent}}y^{n-|I|}\prod_{i\in I}z_i
\]

and states complete log-concavity. The displayed coefficients are one;
there is no factorial normalization. The factorial seen later in Lemma
4.2 belongs to a differentiated/rescaled quadratic, not to (g_M\).
Lemma 2.2, printed pages 5–6, gives affine composition preserving complete
log-concavity for maps taking the nonnegative orthant into itself.
The HTML v1 rendering independently gives the same formulas.

Setting (y=1\), fixing background coordinates at their nonnegative edge
activities, and setting apex coordinates to (Ba_j\) is exactly such an
affine map. The graphic-matroid independent sets are ordinary forests.
Thus the actual ordinary apex partition (Z(B)>0\) satisfies
\((\log Z)''\le0\) for (B>0\). Only scalar log-concavity is used;
no conclusion about signs of individual mixed logarithmic derivatives is
silently inferred.

## 2. Apex partition is the right scalar normalizer

Fix an acyclic edge subset (F\) of the terminal background H. Each tree
component C may connect to the new apex by zero or one spoke. Two apex
spokes into the same component produce a cycle. Conversely, at most one
per component cannot produce a cycle, since there is no other connection
between distinct F-components. Summing over the possible original spoke
choices gives (1+B\sum_{j\in C}a_j\). Therefore

\[
Z(B)=\sum_{F\text{ forest in H}}w_F\prod_C(1+Bx_C)
\]

is literally the ordinary apex-graph forest sum, including coefficient
one for each original forest. It is not a rooted-forest determinant or a
size-normalized partition. The empty F term ensures positivity even at
zero activities. H may have cycles and need not belong to any special
graph class.

For the actual three-core transfer, contracting an acyclic F sums the
rank-one spoke rows within each component. Parallel spoke options
aggregate with their activities; selecting two of them is forbidden as a
cycle. Expanding the commuting nilpotent operators gives

\[
\sum_Fw_FD_F e^{U_FP+G_FQ}
=Z(B)e^{UP+\Gamma Q},\qquad
\Gamma=EG_F+B\operatorname{Var}(U_F).
\]

The variance coefficient B is required by (P^2/2=BQ\) and is correct.
This is a term-by-term equality of ordinary forest sums. It does not
replace a dependent H forest by independent component choices.

## 3. Closure identity rederived

Let (A=\sum_ja_j\), independent of F, and
\(W_F=\sum_Cx_C/(1+Bx_C)\). For (B>0\), direct arithmetic gives

\[
U_F=\frac{A-W_F}{B},\qquad
\frac{U_F}{B}-G_F=\frac1B\sum_C\frac{x_C^2}{(1+Bx_C)^2}.
\]

Differentiating the finite sum for Z gives

\[
(\log Z)'=EW_F,\quad
(\log Z)''=-E\sum_C\frac{x_C^2}{(1+Bx_C)^2}
+\operatorname{Var}(W_F).
\]

Since \(\operatorname{Var}(U_F)=\operatorname{Var}(W_F)/B^2\), substitution
into the exact variance-corrected transfer yields

\[
\boxed{\frac UB-\Gamma=-\frac{(\log Z)''}{B}\ge0.}
\]

All factors and signs check. (U,\Gamma\ge0\) separately follow from
their definitions. Thus arbitrary H produces precisely the scalar cone
needed by the previous matching argument. Isolated unmatched terminals
already belong to H; adding them a second time would be wrong, and the
new report explicitly avoids that error.

## 4. Entire matching law, not only pairwise correlation

Adding split matching endpoints preserves
\(0\le\Gamma_0\le U_0/B\), because every individual
\(\gamma(x)\le\alpha(x)/B\). The common normalizer is
\(D_0=Z(B)\prod_{\text{matched endpoints}}d(a_j)>0\).
The complete matching partition, after including every edge, is

\[
D_0\prod_i(1+c_iw_i)
\left[F_0+\sum_i h_i\delta_i\theta_i
+2BJ\sum_{i<j}\delta_i\delta_j\theta_i\theta_j\right].
\]

This follows by exact multiplication of the split/contracted normalized
transfers. I checked the cross-term coefficient (2BJ\) and the singleton
term (h_i=M+J\epsilon_i/\delta_i+BJ\delta_i\).

The law (X=Y\vee R\) is valid configuration by configuration. Given a
forced subset S, dividing the probability of an ordinary Bernoulli
configuration containing S by \(\prod_{i\in S}\theta_i\) cancels the
same product in the forced weight. Summing S recovers the coefficient of
that actual matching configuration, with the same global scalar
normalizer. Merely having the same partition function would not suffice;
the written proof supplies the stronger identity and it is correct.

For positive matched rows, strict superadditivity and the explicit d
identities give \(0<\delta_i<1/B^2\) and
\(0<\epsilon_i/\delta_i<2/B\). Consequently
\(M<h_i<M+3J/B\). The complete positive core polynomial for
\(L^2-2BJS\), and \(BL\ge9J\), remain unchanged by the background.
Direct expansion with the new closure cone gives

\[
M^2-2BJF_0
\ge L^2-2BJS+2J(BL-J)U_0+2B^2J^2U_0^2>0.
\]

Thus (h_{\min}^2>2BJF_0\), and
\(h_{\max}<M+3J/B\le4M/3<2h_{\min}\).
The assumptions of the size-at-most-two lemma hold uniformly in the
number of matching edges and in H.

I reread that lemma's full hit-covariance expansion. All its internal
pair terms are present and have nonnegative coefficients under these
two scalar assumptions. Its reduction from arbitrary increasing events
to singleton-triggered hit events is valid: pair-only triggers in one
block cannot co-occur with any nontrivial trigger in a disjoint block on
a support of total size at most two. Upper level sets extend the result
to increasing real functions. Averaging over independent Bernoullis on
disjoint blocks then preserves the desired inequality for X. No general
unproved closure theorem is used.

## 5. Conditioning and fields

Present conditioned matching edges contract disjoint endpoint pairs and
sum their rows; their merged vertices can be incorporated as isolated
background vertices. Absent conditioned matching edges are deleted. No
remaining matching endpoint acquires an H edge.

For conditioning H edges present, positive conditional probability forces
the required H subset to be acyclic. Contracting its components sums their
rows, and deleting conditioned-absent edges leaves an arbitrary graph on
the other terminals again. Nonrequired edges becoming loops are
unselectable and may be deleted; parallel nonrequired edges aggregate
exactly for the remaining matching marginal. The product of required
activities is constant and cancels. A required cycle would instead have
zero conditioning probability and is explicitly excluded.

These operations commute for combined H/matching conditioning because
their endpoint sets are disjoint. The resulting graph stays in the same
family, so reapplying the theorem proves the stated conditional property.
Positive fields on matching or background edge coordinates only change
their permitted activities. They do not change the rank-one spoke
requirement. Zero endpoint rows produce independent bridge indicators
and can be removed before divisions by \(\delta_i\). The positive
column assumption keeps B and J positive throughout.

## 6. Actual checkers and independent checks

I inspected the author's actual
`forest_matching_arbitrary_background_exact.py`, its imported previously
audited forced-law/conditional-event helpers, and the complete JSON. It
enumerates acyclic H subsets, literal eight-choice three-spoke stars,
and every indicated conditioning; its original apex enumeration is a
different check of the cluster formula. Its saved 676 valid H partial
conditionings, 19,656 matching conditional laws and 43,836 event checks
are consistent with its loops and reports. These examples are checks of
the algebra and scope, not a substitute for the log-concavity theorem.

My new `arbitrary_background_ant_independent_check.py` imports no author
code. It independently implements original forest union-find tests,
enumerates all eight original choices of each three-spoke star, and
propagates actual core connectivity partitions. A separate original
apex-graph enumeration checks Z, Z′ and Z″. It builds the OR law by
enumerating forced subsets and every Bernoulli configuration, then
enumerates every nonconstant increasing Boolean event on every disjoint
free matching block under all partial H and matching conditionings.
Exact rational arithmetic is used throughout.

| Independent test | Triangle H | Complete four-vertex H |
|---|---:|---:|
| Matching edges | 3 | 3 |
| H edges | 3 | 6 |
| Valid H partial conditionings | 26 | 624 |
| Matching conditional laws | 702 | 16,848 |
| Increasing-event inequalities | 546 | 13,104 |
| Apex derivatives and exact closure identity | PASS | PASS |
| Whole OR configuration law | PASS | PASS |

The triangle case uses new nonuniform rational rows, columns, core and
activities. The four-vertex case includes a zero core edge. My event
counts use unordered pairs of disjoint blocks, avoiding the two symmetric
copies used by the author's loops. Full results are saved in
`arbitrary_background_ant_independent_checks.json`.

## 7. Exact boundary of the result

The proof covers any finite arbitrary weighted graph among unmatched
terminals, with all selected matching endpoints excluded from that
background, over the weighted three-vertex core with rank-one spokes.
It covers the ENTIRE selected matching vector and the specified H and
matching conditioning. It does not cover arbitrary spoke/core
conditioning or arbitrary additional incidence at matching endpoints.
Neither the scalar log-concavity input nor this derived corollary proves
negative association of every forest indicator. The established
log-concavity theorem is credited prior work; novelty of the restricted
corollary remains an independent historical question.
