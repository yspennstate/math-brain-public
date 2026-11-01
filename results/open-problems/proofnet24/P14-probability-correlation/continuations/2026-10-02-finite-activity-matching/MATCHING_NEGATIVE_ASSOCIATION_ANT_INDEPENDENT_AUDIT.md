# Independent audit: negative association of the matching-indicator vector

Date: 2026-10-02. Auditor: independent `antivoter_audit` agent.

**Verdict: PASS for the entire matching-indicator vector in the stated
rank-one, three-core family, including conditioning matching bits and
positive matching external fields.** I read the full
`forest_rank_one_core3_matching_negative_association_candidate.md`, the
separately preserved final
`forest_rank_one_core3_matching_negative_association_proof.md`, the
entire `forest_matching_negative_association_exact.py`, and its completed
results. I independently rederived the forced-subset lemma, matching
configuration law, numerical parameter bounds, Bernoulli-OR argument,
and conditioning closure. No mathematical gap was found. No author file
or Git state was modified. This audit does not certify novelty or
external peer review.

## 1. The support-at-most-two lemma

Let \(Y\) have raw masses \(A>0\), \(h_it_i\), and
\(Kt_it_j\) on the empty set, singletons, and pairs respectively.
Assume \(K>0\), \(t_i\ge0\), \(h_i>0\),
\(h_{\min}^2\ge KA\), and \(2h_{\min}\ge h_{\max}\).

For disjoint hit sets \(E,F\), let their complement be \(C\).
Writing \(s_H=\sum_{i\in H}t_i\),
\(q_H=\sum_{i<j\in H}t_it_j\), and
\(\beta_Hs_H=\sum_{i\in H}h_it_i\), direct enumeration gives
\[
 W_E=s_E\beta_E+Kq_E+Ks_E(s_F+s_C),\quad
 W_F=s_F\beta_F+Kq_F+Ks_F(s_E+s_C),\quad
 W_{EF}=Ks_Es_F.
\]
Independently expanding their covariance numerator yields exactly
\[
\begin{aligned}
 W_EW_F-W_{EF}Z={}&s_Es_F[
 \beta_E\beta_F-KA
 +Ks_C(\beta_E+\beta_F-\beta_C)
 +K^2(s_C^2-q_C)]\\
 &+Kq_Es_F(\beta_F+Ks_C)
  +Kq_Fs_E(\beta_E+Ks_C)+K^2q_Eq_F.
\end{aligned}
\]
In particular the internal-pair terms are retained. The terms
\(-K^2s_Es_Fq_E\) and \(-K^2s_Es_Fq_F\) from the base bracket
cancel their corresponding cross terms; they do not need to be ignored.
Every remaining term is nonnegative under the hypotheses, since
\(s_C^2-q_C=\sum_{i\in C}t_i^2+q_C\ge0\).
If a hit set has zero \(t\)-mass, its joint probability is zero;
if \(s_C=0\), its \(\beta_C\) value has no effect. These cases are
correctly handled in the candidate.

The reduction to all increasing events is also valid. Consider two
nontrivial increasing events on disjoint coordinate blocks, neither
containing that block's empty configuration. Each simultaneous
occurrence needs at least one \(Y\)-point in each block. Since
\(|Y|\le2\), it must use exactly one in each block; each singleton
must itself trigger the corresponding event. Consequently the joint
event is exactly the joint hit event for their singleton-trigger sets.
Each marginal event contains its hit event, and may additionally be
triggered by a pair wholly inside its own block. Such a pair cannot
co-occur with the other nontrivial event. This establishes the claimed
inequality, including events that have only pair triggers or no
singleton triggers. An increasing event containing the empty
configuration is identically true and has covariance zero.

Finally, on a finite cube every increasing real function is a constant
plus a finite nonnegative linear combination of increasing upper-level
event indicators. Bilinearity of covariance therefore extends the event
inequality to arbitrary increasing real functions, even when their
values can be negative. This proves negative association of \(Y\).
Empty index sets are trivially negatively associated.

## 2. Exact matching configuration law and normalization

Use \(B,J,S,L,d,\alpha,\gamma\) from the already audited weighted
transfer. With every matching edge absent put
\[
 D_0=\prod_jd(a_j),\quad U_0=\sum_j\alpha(a_j),\quad
 \Gamma_0=\sum_j\gamma(a_j),\quad
 F_0=S+LU_0+J\Gamma_0+BJ U_0^2.
\]
All these parameters are finite, and \(F_0\ge S\ge1\).
For matching edge \(i\), define its contraction increments
\(\delta_i,\epsilon_i\) and scalar factor \(c_i\).
Let \(M=L+2BJ U_0\), \(K=2BJ\), and
\[
 h_i=M+J\epsilon_i/\delta_i+BJ\delta_i.
\]
For a matching presence set \(x\), disjoint contraction gives the
forest coefficient
\[
 D_0\prod_{i\in x}c_i\left[
 F_0+\sum_{i\in x}h_i\delta_i
                  +K\sum_{i<j\in x}\delta_i\delta_j\right].
\]
Multiplying by \(\prod_{i\in x}w_i\) gives the exact raw matching
configuration mass. This independently verifies the quadratic expansion,
including its second-order coefficient \(2BJ\), for every matching
presence configuration.

Put \(\rho_i=c_iw_i\), \(\theta_i=\rho_i/(1+\rho_i)\), and
\(t_i=\delta_i\theta_i\). Summing those configuration masses gives
\[
 Z=D_0\prod_i(1+\rho_i)
   [F_0+\sum_ih_it_i+K\sum_{i<j}t_it_j].
\]
The bracket is exactly the normalization of the forced-subset law;
the product outside it is exactly the normalization of independent
Bernoullis with success probabilities \(\theta_i\). No scalar is
missing.

## 3. The forced-subset/Bernoulli OR identity

Independently sample \(Y\) with raw masses
\(F_0,h_it_i,Kt_it_j\), and independent Bernoulli coordinates \(R_i\)
with means \(\theta_i\). Let \(X_i=1_{i\in Y}\vee R_i\).
For a forced set \(s\subseteq x\),
\[
 \Pr(X=x\mid Y=s)
 =\frac{\Pr(R=x)}{\prod_{i\in s}\theta_i}.
\]
The summands involving an inadmissible \(s\) vanish. Multiplying by
the forced-set mass cancels the corresponding \(\theta_i\) factors.
Thus
\[
 \Pr(X=x)=\frac{\Pr(R=x)}{Z_Y}
 [F_0+\sum_{i\in x}h_i\delta_i
               +K\sum_{i<j\in x}\delta_i\delta_j],
\]
which agrees with the normalized forest matching mass above. The
representation is an exact finite-measure identity, rather than merely
agreement of partition functions or pair moments.

The candidate initially assumes positive matching endpoint rows and
positive matching activities, so both \(\delta_i\) and \(\theta_i\)
are positive in this calculation. Zero endpoint rows are factored out
separately, rather than divided by zero.

## 4. Uniform bounds required by the lemma

For positive endpoint rows \(a,b\), strict increase of
\(\alpha(x)/x\) and \(\gamma(x)/x\) proves
\(\delta_i,\epsilon_i>0\). The merge identity
\[
 \delta_i=B^{-2}[1+d(a+b)^{-1}-d(a)^{-1}-d(b)^{-1}]
\]
is correct and gives \(\delta_i<1/B^2\).
For \(H(x)=(2/B)\alpha(x)-\gamma(x)\),
\[
 H(x)/x=B^{-2}[1-d(x)^{-2}]
\]
is strictly increasing. Its strict superadditivity yields
\(\epsilon_i<(2/B)\delta_i\). Hence
\[
 M<h_i<M+3J/B.
\]
The positive column weights give \(BL\ge Be_2(b)\ge9J\), so
\(3J/B\le L/3\le M/3\). In particular
\(h_{\max}<4M/3<2M<2h_{\min}\). This bound is uniform over all
matching activities and external fields, which only change the
\(\theta_i\)'s.

Also \(\Gamma_0\le U_0/B\), and exact expansion gives
\[
 M^2-KF_0
 =L^2-2BJ S+2BJ LU_0+2B^2J^2U_0^2-2BJ^2\Gamma_0
 >0.
\]
The strict inequality follows from the independently audited primitive
positive core polynomial and \(BL>J\). Thus
\(h_{\min}^2>M^2>KF_0\), establishing the other lemma hypothesis.
The support-at-most-two forced law is negatively associated.

## 5. Passing from the forced law to all matching indicators

For increasing \(f,g\) on disjoint matching-coordinate blocks,
conditioning on \(Y\) leaves independent Bernoulli coordinates in
those two blocks. Their conditional product expectation factors as
\(F(Y_E)G(Y_F)\). Coupling the same Bernoulli variables before and
after adding forced coordinates shows both averaged functions are
increasing. Negative association of \(Y\) therefore yields
\(\mathbb E[fg]\le\mathbb E[f]\mathbb E[g]\) for \(X\).
This is a complete closure proof; it does not rely on an assumed
general closure theorem or an unproved real-stability claim.

If a matched endpoint has row zero, that endpoint has no usable spoke
and no other matching edge. The edge is a bridge, or an isolated
two-vertex component if both rows vanish. Forest weights factor as
\((1+w_i)\) times the rest, so this indicator is an independent
Bernoulli of mean \(w_i/(1+w_i)\). Such indicators can be appended
independently to the remaining negatively associated vector by the
same conditional-expectation argument. If there are no remaining
nonbridge matches, the vector is simply independent Bernoullis.

## 6. Conditioning and external fields

Conditioning selected matching edges present contracts their disjoint
terminal pairs and aggregates their row activities. A contracted pair
becomes an unmatched terminal of row weight \(a+b\); no remaining
matching edge was incident to either endpoint. Conditioning matching
edges absent deletes them. Parallel spokes aggregate exactly, retaining
the same three positive column factors. The residual graph therefore
lies in the same rank-one three-core family. The conditional forest
law is the forest law of that deletion/contraction graph, after a
configuration-independent factor cancels. All specified matching
conditioning events have positive probability under positive matching
activities, since the matching alone is acyclic.

Applying the already established theorem to the remaining indicator
vector proves negative association after every such partial
conditioning. Positive external fields simply multiply the matching
activities, so the same result holds with arbitrary positive fields,
before or after conditioning. No conditioning on spoke/core edges is
asserted.

## 7. Verifier audit and independent exact computation

The author verifier constructs every matching configuration mass by
explicit three-spoke subset transitions, compares the entire law with
the forced-OR representation, and checks increasing events and all
partial matching-bit conditionings using denominator-cleared integers.
Its recursive upper-set enumeration is complete, and its event lifting
and covariance normalization are correct. The completed report contains
four graph cases, 432 partial conditionings, and 10,714 exact disjoint
increasing-event comparisons, plus abstract forced-subset cases. I read
both the verifier and its reported values.

New independent files are `matching_na_ant_independent_check.py` and
`matching_na_ant_independent_checks.json`. They have no author imports.
They compute matching masses using raw \((I,P,Q)\)-basis products,
without the forced representation. The OR distribution is then computed
literally by summing independent \(Y,R\) outcomes and compared with
every normalized matching configuration mass.

For one six-matching-edge graph with unequal positive row/column weights,
an unmatched zero row, and activities ranging from \(1/100\) to 100,
the entire 64-state law agrees exactly. All 729 partial conditionings
pass 86,634 exact monotone-event comparisons. The independent checker
uses covering bipartitions and exact integer contingency matrices;
these suffice for arbitrary disjoint blocks because ignored coordinates
can be added to one side without altering either event. The upper-set
counts through dimension five are \(2,3,6,20,168,7581\), and all
nonconstant events are checked, including AND/pair-only triggers.

The forced law passes a further 58,674 comparisons. Two six-coordinate
abstract forced-law cases each pass 58,674 comparisons with both lemma
hypotheses at equality; one case also has zero \(t_i\)'s. This directly
checks the nonstrict lemma boundary, separately from the strict graph
parameters. All arithmetic in these law and event comparisons is exact.

These finite computations support the complete analytic proof. They do
not establish arbitrary dimension or all external fields by numerical
extrapolation; those follow from the support lemma, uniform parameter
bounds, OR identity, and deletion/contraction closure.

## 8. Exact scope and status

The negative-association conclusion concerns the entire terminal
matching-indicator vector in the specified rank-one spoke family, with
three positive column factors and nonnegative core/row activities. It
holds under positive matching fields and matching-bit conditioning.
It is stronger than pairwise matching-edge correlation, but it does not
assert negative association of all forest edges, arbitrary spoke
weights, overlapping terminal edges, arbitrary cores, or the full forest
negative-association conjecture. It does not require or assert a
real-stable matching polynomial or the strong Rayleigh property.

This internal audit finds the stated candidate mathematically complete;
historical priority and external peer review remain separate questions.

## 9. Final-proof continuity and non-real-stability witness

I read the entire final proof after its separate creation. Its explicit
primitive core coefficients agree with the earlier independent weighted
audit; its main NA argument is unchanged. The added scope witness is
also valid.

For the empty core, unit column weights, ten rows of activity \(1/100\),
and five matching edges, let all matching activity variables equal \(w\).
The exact matching generating polynomial has the factorization
\[
 Z(w,\ldots,w)=D_0(1+cw)^3
 \{F_0(1+cw)^2+5h\delta cw(1+cw)+10K\delta^2c^2w^2\}.
\]
The quadratic in braces has discriminant
\[
 c^2\delta^2[25h^2-40KF_0]<0.
\]
The corresponding \(\theta\)-quadratic discriminant without the
positive \(c^2\) factor is exactly
\(-553191/1580777123645\), as the author reports.

My independent checker obtains the actual diagonal degree-five
coefficients directly from the raw forest law, divides them exactly by
\((1+cw)^3\), and checks the resulting quadratic by convolution. Its
actual discriminant, including the positive \(D_0^2c^2\) factors, is
\[
 -788718090755324577011236610631/
 1250000000000000000000000000000000000<0.
\]
After dividing those positive factors, it reproduces the reported
\(\theta\)-discriminant exactly. Thus this scope witness is independently
verified from the original diagonal forest coefficients, rather than
only from the proposed representation.

Either the negative diagonal discriminant directly gives a zero with
all five matching variables equal in the upper half-plane, or one may
use the final proof's inverse map
\(w=z/[c(1-z)]\). Its imaginary part is
\(\operatorname{Im}z/(c|1-z|^2)>0\); its denominator cannot vanish at
the nonreal root. The product factor in the generating polynomial is
nonzero there. Hence the matching polynomial is not real stable, so the
NA theorem must not be restated as a strong-Rayleigh result. The final
proof states this distinction correctly.
