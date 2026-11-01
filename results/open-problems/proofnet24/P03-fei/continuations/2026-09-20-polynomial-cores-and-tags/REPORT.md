# Polynomially coupled symmetric cores and a joint entropy deletion bound

20 September 2026. Research continuation for Yitzchak Shmalo.

**Status.** The results below are all-dimensional restricted theorems with written proofs and executed exact finite checks. They do not prove unrestricted Friedgut–Kalai FEI. Independent expert review, formal verification, and publication-priority clearance have not been completed.

## 1. What is added to the existing work

The scheduled report `scheduled-continuation/runs/2026-09-20/2026-09-20T03-23-21Z__report.md` already proves the single-core theorem

\[
H((-1)^P h)\le \max\{12.04+\log_2 d,\;2^r h_2(2^{-r})+2/\ln2\}\,J((-1)^P h)
\]

for a degree-at-most-\(r\) polynomial \(P\) over \(\mathbb F_2\) and a \(d\)-part-symmetric core \(h\). Its unchanged constant through degree seven and its linear degree dependence are **prior repository results**, not discoveries claimed by this continuation. That report explicitly leaves a factor-count-free theorem for higher-degree cross-core coupling unproved. The preceding quadratic-symmetry report proves that product extension only for degree two.

The additional result here is the product extension for every degree: arbitrarily many independently supported, arbitrarily high-degree symmetric or part-symmetric cores may be coupled by an arbitrary degree-\(r\) polynomial, with dependence on \(\max_t d_t\), not on the number of cores or the total number of parts. The proof supplies a cross-core derivative payment, an exact joint entropy identity for a fixed physical deletion, and a weighted version using local symmetry-defect degrees. It also extends the hereditary allocation certificate to this product class.

No product spectral law is imposed on the coupled parent. Factorization is used only after actual physical restrictions have removed all cross-core interactions.

The companion [polynomial tag extension](TAG_PHASE_EXTENSION.md) combines this result with the concurrent affine-fibre gluing theorem. It permits arbitrary cubic tag phases at the sharp class constant four, and arbitrary degree-at-most-eleven tag phases at constant 12.04 when the physical sections use the polynomially coupled symmetric cores certified here. These are restricted closure theorems, not an unrestricted representation theorem.

## 2. Definitions and main theorem

All logarithms in entropies are base two. For Boolean \(f:\mathbb F_2^n\to\{-1,1\}\), write

\[
a_S=\widehat f(S),\quad p_S=a_S^2,\quad
H(f)=\sum_Sp_S\log_2(1/p_S),
\]
\[
\alpha_i(f)=\Pr[f(x)\ne f(x+e_i)],\quad
j_i(f)=\min\{\alpha_i(f),1-\alpha_i(f)\},\quad
J(f)=\sum_i j_i(f),\quad I(f)=\sum_i\alpha_i(f).
\]

The empty Fourier atom is included. Terms of the form \(0\log 0\) are zero. Multiplication by a character translates the squared spectrum, preserves \(H\) and \(J\), and can change \(I\) to exactly \(J\).

Partition the physical coordinates into nonempty, pairwise disjoint groups \(U_1,\ldots,U_m\). Within \(U_t\), fix a partition into \(d_t\ge1\) nonempty parts. A function \(h_t\) is part-symmetric if it depends only on the Hamming weights of these parts. No bound is imposed on its algebraic degree or on its table of weight-dependent values.

Set

\[
F(x)=(-1)^{P(x)}\prod_{t=1}^m h_t(x_{U_t}),\qquad
C_t=12.04+\log_2d_t,\quad C_*=\max_t C_t,
\]
\[
h_2(q)=-q\log_2q-(1-q)\log_2(1-q),\quad
\phi(s)=2^s h_2(2^{-s}),\quad
\kappa_s=\phi(s)+\frac2{\ln2}\quad(s\ge1).
\]

**Theorem 2.1.** If \(\deg_{\mathbb F_2}P\le r\), where \(r\ge2\), then

\[
\boxed{
H(F)\le \max\{C_*,\kappa_r\}\,J(F)
\le \max\{12.04+\log_2(\max_t d_t),\;r+3/\ln2\}\,I(F).
}
\tag{2.1}
\]

For an affine \(P\), the coefficient is simply \(C_*\). In particular, for every \(r\le7\),

\[
\boxed{
H\!\left((-1)^P\prod_t h_t\right)
\le \bigl(12.04+\log_2\max_t d_t\bigr)J(F).
}
\tag{2.2}
\]

When each core is fully symmetric, the constant is **12.04**, independently of the number and sizes of the cores, the number of polynomial terms, and their overlapping within-core and cross-core supports. For example, the cores can be majority functions on arbitrarily large disjoint groups, while \(P\) contains arbitrarily many interacting monomials of degrees at most seven.

This is not merely a bounded-degree theorem for \(F\): the cores, and hence \(F\), can have unbounded algebraic degree.

## 3. Published leaf input and its exact scope

O'Donnell–Wright–Zhou [OWZ11, Theorems 1–2] prove

\[
H(u)\le (12.04+\log_2d)I(u)
\tag{3.1}
\]

for a \(d\)-part-symmetric Boolean function. Influences agree inside a symmetry part. Multiplying by the character of the union of all parts whose influence exceeds one half preserves part symmetry and changes total influence to \(J\). Consequently (3.1) also holds with \(J\).

Physical restrictions preserve part symmetry, with no increase in the number of parts. Character multiplication preserves entropy and folded influence. For products on disjoint physical groups, both spectral entropy and folded influence add. Therefore every character times a product of part-symmetric factors on those groups has the leaf certificate

\[
H(u)\le\sum_t C_tJ(u_t)\le C_*J(u).
\tag{3.2}
\]

The published symmetry bound and ordinary tensorization are reused inputs. They are not new claims.

## 4. A fixed-block deletion identity with paid recombination

This section applies to **every** Boolean function, without symmetry or degree assumptions.

Fix a set of coordinates \(E\), write \(R=[n]\setminus E\), and let \(f_z\) be the physical restriction fixing \(x_E=z\). Let \(S\) have squared Fourier law \(p\). Construct another joint law by taking \(Z\) uniform on \(\mathbb F_2^E\), then sampling \(Y\), conditionally on \(Z=z\), from the squared Fourier law of \(f_z\) on \(R\).

Partial Parseval gives

\[
\Pr(Y=T)=2^{-|E|}\sum_z\widehat {f_z}(T)^2
=\sum_{A\subseteq E}\widehat f(T\cup A)^2
=\Pr(S_R=T).
\tag{4.1}
\]

The entropy chain rule therefore gives the exact identity

\[
\boxed{
H(f)-\mathbb E_zH(f_z)
=H(S_E\mid S_R)+I(Z;Y).
}
\tag{4.2}
\]

The first term retains joint dependence among all deleted spectral bits. The second is a mutual information under the explicitly constructed physical-restriction law; the two terms must not be conflated.

**Lemma 4.1.** With \(c=2/\ln2\),

\[
0\le I(Z;Y)\le c\sum_{i\in E}j_i(f).
\tag{4.3}
\]

**Proof.** Order \(E\) and expose its physical bits in that order. Condition on a previously exposed prefix, obtaining a Boolean restriction \(g\). The two conditional laws of \(Y\) at the next bit \(i\) are marginals of the squared Fourier laws of \(g_{i=0}\) and \(g_{i=1}\). Data processing bounds their equal-weight Jensen–Shannon divergence by that of the full two child spectra. The repository's exact one-coordinate estimate is

\[
\operatorname{JS}(\widehat{g_0}^{\,2},\widehat{g_1}^{\,2})\le c j_i(g).
\tag{4.4}
\]

For completeness, write the paired parent Fourier amplitudes as \(u,v\). The child amplitudes are \(u+v,u-v\). Their contribution to JS is at most \(c\min(u^2,v^2)\), by

\[
\frac{(1+z)\ln(1+z)+(1-z)\ln(1-z)}2
\le1-\sqrt{1-z^2},\quad 0\le z\le1.
\]

Both sides vanish at zero; the derivative comparison is \(\operatorname{atanh}z\le z/\sqrt{1-z^2}\). Summation proves (4.4). The sharpness of its universal coefficient is already established in the scheduled sharp-recombination report [R3].

Averaging over the previously fixed coordinates preserves the ordinary (unfolded) influence of an unqueried coordinate. Concavity of \(q\mapsto\min(q,1-q)\) gives \(\mathbb E j_i(g)\le j_i(f)\). Sum the conditional mutual informations along the exposure chain to obtain (4.3). QED.

By conditional subadditivity,

\[
H(S_E\mid S_R)\le\sum_{i\in E}h_2(j_i(f)).
\]

Thus

\[
\boxed{
H(f)\le\mathbb E_zH(f_z)+
\sum_{i\in E}\bigl[h_2(j_i(f))+c j_i(f)\bigr].
}
\tag{4.5}
\]

Also, for each retained coordinate,

\[
\mathbb E_z j_i(f_z)\le j_i(f),\qquad i\in R.
\tag{4.6}
\]

These inequalities refine the earlier two-bits-per-deleted-coordinate bound. They can also be obtained by telescoping the one-coordinate entropy decomposition and applying concavity. The exact joint identity (4.2) specifies what the marginal relaxation in (4.5) discards.

For \(0<\eta\le q\le1/2\),

\[
\frac{h_2(q)}q\le\frac{h_2(\eta)}\eta,
\qquad
\frac{d}{dq}\frac{h_2(q)}q=\frac{\log_2(1-q)}{q^2}<0.
\tag{4.7}
\]

A deleted coordinate with \(j_i\ge2^{-s}\) therefore costs at most \(\kappa_s j_i\), not a fixed two bits.

## 5. Cross-core and internal symmetry-defect payments

Use the unique multilinear algebraic normal form of \(P\). Write

\[
\partial_iP=P|_{x_i=0}+P|_{x_i=1},
\]

with addition in \(\mathbb F_2\). Define two disjoint sets of coordinates.

* \(E_{\rm cross}\) contains \(i\in U_t\) when \(\partial_iP\) depends on at least one variable outside \(U_t\). Equivalently, some monomial of \(P\) contains \(i\) and a variable in another core group.
* \(E_{\rm mix}\) contains the remaining \(i\in U_t\) for which \(\partial_iP\) is changed by a transposition of two coordinates in one of the parts of \(U_t\), with \(i\) excluded.

Let \(E=E_{\rm cross}\cup E_{\rm mix}\).

We use the elementary minimum-weight fact: a nonzero Boolean polynomial of degree at most \(s\) is one on at least a \(2^{-s}\) fraction of its cube. One proof is induction on degree: choose a relevant variable; on every point where its nonzero derivative is one, exactly one of the two extensions makes the polynomial one. The nonzero constant case starts the induction.

For \(i\in U_t\), put

\[
g_i=h_t|_{x_i=0}\,h_t|_{x_i=1}.
\]

It is Boolean, depends only on \(U_t\setminus\{i\}\), and is invariant under the allowed within-part transpositions. The other core factors cancel in the multiplicative derivative, so

\[
1-2\alpha_i(F)=\mathbb E[g_i(-1)^{\partial_iP}],
\qquad
j_i(F)=\frac{1-|\mathbb E[g_i(-1)^{\partial_iP}]|}{2}.
\tag{5.1}
\]

**Lemma 5.1 (cross-core payment).** If \(i\in E_{\rm cross}\) and \(\deg P\le r\), then

\[
\boxed{j_i(F)\ge2^{1-r}.}
\tag{5.2}
\]

**Proof.** Choose \(j\notin U_t\) with \(A=\partial_j\partial_iP\ne0\). Its degree is at most \(r-2\), so \(\Pr(A=1)\ge2^{2-r}\). The core derivative \(g_i\) is independent of \(x_j\). On any remaining assignment with \(A=1\), the average over \(x_j\) of \((-1)^{\partial_iP}\) is zero. Everywhere else its magnitude is one. Consequently

\[
|\mathbb E[g_i(-1)^{\partial_iP}]|\le1-\Pr(A=1),
\]

which yields (5.2). QED.

This is the extra payment needed to pass from the prior single-core theorem to arbitrarily many coupled cores. It does not assert that a higher-degree derivative is a character or has zero mean.

**Lemma 5.2 (internal payment, reused mechanism).** If \(i\in E_{\rm mix}\), then

\[
\boxed{j_i(F)\ge2^{-r}.}
\tag{5.3}
\]

**Proof.** Choose an allowed transposition \(\tau\) for which

\[
D=\partial_iP+\partial_iP\circ\tau\ne0.
\]

Its degree is at most \(r-1\), so \(\Pr(D=1)\ge2^{1-r}\). Write \(\psi=(-1)^{\partial_iP}\). Invariance of \(g_i\) and of uniform measure gives

\[
|\mathbb E g_i\psi|
=\left|\mathbb E g_i\frac{\psi+\psi\circ\tau}{2}\right|
\le1-\Pr(D=1).
\]

Equation (5.1) proves (5.3). This is the scheduled single-core transposition/minimum-weight argument, now applied inside each independently supported core. QED.

Both scales are attained. For the cross-core scale, take constant cores on two nonempty groups and \(P=x_1\cdots x_r\), involving both groups; all its relevant coordinates have \(j_i=2^{1-r}\). For the internal scale on \(r+1\) variables, take the fully symmetric core \(h=(-1)^{x_1\cdots x_{r+1}}\) and \(P=x_1\cdots x_r\). Then \(F\) differs from one at precisely \((1,\ldots,1,0)\), all its influences equal \(2^{-r}\), and its first \(r\) coordinates are internally mixed.

## 6. The actual restricted leaves factor

Fix every coordinate in \(E\), and let \(R\) be the retained set.

First, no nonlinear monomial of a restricted polynomial \(P_z\) can meet two residual core groups. Any original monomial that could produce it contains retained variables \(i,j\) from different groups; then \(i\in E_{\rm cross}\), contradicting retention. Cancellations under restriction can remove monomials, but cannot create one without an original monomial containing its support.

Second, for each retained \(i\), \(\partial_iP_z\) is invariant under every within-part transposition of retained coordinates other than \(i\). This follows from its original invariance and the fact that these transpositions fix all deleted coordinates.

To conclude symmetry of the nonlinear part, take a monomial \(A\) of size at least two and replace \(j\in A\) by \(k\notin A\) in the same residual part. The old and new supports share an \(i\ne j,k\). Invariance of \(\partial_iP_z\) under \((jk)\) forces equality of their coefficients. These replacements connect all monomials with the same part-count vector. Therefore the nonlinear coefficients within each residual group depend only on that vector.

It follows that

\[
P_z=L_z+\sum_t Q_{t,z},
\tag{6.1}
\]

where \(L_z\) is affine and each \(Q_{t,z}\) is part-symmetric on the retained coordinates of \(U_t\). Consequently

\[
F_z=\text{a character and global sign}\;\times
\prod_t\left[(-1)^{Q_{t,z}}(h_t)_z\right].
\tag{6.2}
\]

Every bracket is part-symmetric and the brackets have disjoint physical supports. Equation (3.2), followed by (4.6), gives

\[
\mathbb E_z H(F_z)\le
\sum_t C_t\sum_{i\in U_t\setminus E}j_i(F).
\tag{6.3}
\]

Empty residual groups contribute zero entropy and zero influence.

## 7. Proof of the theorem and a stronger weighted statement

Combine (4.5), (5.2), (5.3), (6.3), and (4.7):

\[
\boxed{
H(F)\le
\sum_t C_t\sum_{i\in U_t\setminus E}j_i(F)
+\kappa_{r-1}\sum_{i\in E_{\rm cross}}j_i(F)
+\kappa_r\sum_{i\in E_{\rm mix}}j_i(F).
}
\tag{7.1}
\]

Since \(\kappa_{r-1}\le\kappa_r\), (2.1) follows. Also

\[
\phi(r)=r-\frac{1-2^{-r}}{2^{-r}}\log_2(1-2^{-r})
\le r+\frac1{\ln2}.
\tag{7.2}
\]

Thus \(\kappa_r\le r+3/\ln2\). For \(r\le7\), this is less than \(12.04\), proving (2.2). The exact values at the transition are

\[
\kappa_7=11.3224348617\ldots,\qquad
\kappa_8=12.3252636827\ldots.
\]

The checker encloses these numbers by rational intervals rather than using the displayed decimals as proofs.

### Local defect-degree version

There is no need to use the largest degree of \(P\) for every deleted coordinate. Define

\[
\rho_i=1+\min_{j\notin U_t:\,\partial_j\partial_iP\ne0}
\deg(\partial_j\partial_iP),\quad i\in E_{\rm cross}\cap U_t,
\]

and, for \(i\in E_{\rm mix}\), define

\[
\rho_i=1+\min_{\tau:\,D_{i,\tau}\ne0}\deg(D_{i,\tau}),
\qquad D_{i,\tau}=\partial_iP+\partial_iP\circ\tau,
\]

where \(\tau\) ranges over the allowed within-part transpositions. The same proof gives \(j_i(F)\ge2^{-\rho_i}\), and hence

\[
\boxed{
H(F)\le\sum_t C_t\sum_{i\in U_t\setminus E}j_i(F)
+\sum_{i\in E}\kappa_{\rho_i}j_i(F).
}
\tag{7.3}
\]

This version applies even when \(P\) has high degree but each deleted coordinate has a low-degree incompatibility witness. It does not assert that those witnesses always exist with uniformly bounded degree.

## 8. Hereditary allocation extension

For a complete physical restriction tree \(T\), put

\[
R_T(f)=\sum_{v\text{ internal}}2^{-\mathrm{depth}(v)}B_{i(v)}(f_v),
\quad B_i(g)=H(S_i\mid S_{-i}),
\quad R_*(f)=\min_T R_T(f).
\]

Then the product class in Theorem 2.1 satisfies

\[
\boxed{
R_*(F)\le \max\{C_*,\phi(r)\}\,J(F).
}
\tag{8.1}
\]

To prove this, repeatedly query any cross-core or internally mixed coordinate of the current restricted phase. The groups remain disjoint and the degree never increases. Equations (5.2)–(5.3) imply \(B_i\le h_2(j_i)\le\phi(r)j_i\) at every queried node. Stop when no bad coordinate remains; Section 6 supplies a product part-symmetric leaf.

The leaf class is restriction-stable and satisfies \(H\le C_*I\). Since \(\sum_iB_i\le H\), some relevant coordinate at each nonconstant leaf has \(B_i\le C_*\alpha_i\). Induction supplies a complete continuation tree whose allocation cost is at most \(C_*I\) of that leaf. Graft these trees onto the stopped tree and use the exact physical influence telescope

\[
I(F)=\sum_{v\text{ queried}}2^{-\mathrm{depth}(v)}\alpha_{i(v)}(F_v)
+\mathbb E I(F_{\rm leaf}).
\]

This proves the bound with \(I\). Character multiplication preserves every \(B_i\) along a given physical tree and stays within the stated class, so normalizing the root influence proves (8.1) with \(J\).

This extends the preexisting single-core hereditary certificate. No claim about an optimal tree for an unrestricted function follows.

## 9. Attempted passage to unrestricted FEI: what remains unpaid

The new theorem removes the **number-of-cores penalty**, not the unbounded-degree penalty. Every Boolean function can be written as \((-1)^P\) with a constant core, but \(\deg P\) can grow with dimension. That substitution yields a coefficient growing with degree, not a universal constant. Treating an arbitrary core as part-symmetric by using singleton parts likewise leaves a growing \(\log d\) term. Arbitrary input-affine changes are not permitted to preserve the physical core partition without a separate argument.

The exact fixed-block allocation in (4.2) can be substantially smaller than its marginal upper bound in (4.5). This is not a removable constant-factor issue. In the sharp internal-gap family of Section 5, let \(q=2^{-r}\) and delete its first \(r\) coordinates. Then

\[
I(F)=(r+1)q,\qquad
\sum_{i\in E}h_2(j_i)=r h_2(q),
\]

so

\[
\frac{\sum_{i\in E}h_2(j_i)}{I(F)}
=\frac{r}{r+1}\frac{h_2(q)}q\sim r.
\tag{9.1}
\]

Each physical leaf is constant or a character. The squared spectrum has mass \((1-q)^2\) at the empty set and mass \(q^2\) at each of its \(2^{r+1}-1\) nonempty labels. Therefore

\[
H(F)=2(1-q)^2\log_2\frac1{1-q}+2r(2q-q^2),
\qquad \frac{H(F)}{I(F)}\longrightarrow4.
\]

The one retained spectral bit has Bernoulli parameter \(q\), and every leaf has zero entropy, so the two exact terms in (4.2) are

\[
I(Z;Y)=h_2(q),\qquad H(S_E\mid S_R)=H(F)-h_2(q).
\]

Relative to \(rq\), these two terms tend to one and three respectively. Their sum is bounded by a constant times influence, although replacing the second term by the sum of marginal entropies produces (9.1). Therefore uniformly bounding the marginal charges used in (4.5) cannot finish the proof. The dependence inside the joint conditional entropy must be retained, or a better stopping representation must be used. One-point/rare-monomial obstructions to other marginal and two-bit deletion schemes are already recorded in the repository; this calculation identifies the same issue in the precise new bound.

The directly equivalent universal target from the existing erasure reduction is still

\[
\boxed{
\sum_i H(S_i\mid S_{-i})\le K I(f)
\quad\text{for every Boolean }f,
}
\tag{9.2}
\]

with one finite \(K\) independent of dimension. It would imply full FEI with constant \(K+2/\ln2\). Equation (9.2) is **not proved here**. The Boolean signed-convolution constraints

\[
\sum_S\widehat f(S)\widehat f(S\triangle U)=0\quad(U\ne\varnothing)
\]

cannot be replaced by arbitrary nonnegative spectral probabilities. No coordinatewise bound for every individual erasure term, no false pointwise converse \(H\le\sum_iB_i+(2/\ln2)I\), and no already-refuted fixed-exponent or affine-drift estimate is being assumed.

The advancement toward that target is a larger rigorously certified stopping class and a joint, influence-paid block decomposition. It is not a claimed solution of the remaining universal allocation inequality.

### A further universal route tested and refuted

The companion [operator obstruction](UNITARY_ERASURE_OBSTRUCTION.md) tests whether one can prove (9.2) by replacing Boolean convolution matrices by general real orthogonal involutions. Its proposed averaged-column erasure / trace-norm commutator inequality would indeed imply full FEI. An explicit family instead has an unbounded ratio, greater than \((\log_2 M)/10\). The companion supplies the full analytical construction and an exact \(64\times64\) verification. Those matrices are not Boolean convolution matrices, so the result refutes the relaxation, not FEI. It pinpoints additional structure that any successful operator argument must preserve.


## 10. Reproduction and actual check coverage

Run

```sh
python3 verify_polynomial_symmetry.py --output verification.json
```

The supplied `verification.json` is actual output of this command. It reports `PASS` and records the checker SHA256. Its verification families are:

| Family | Actual coverage |
|---|---:|
| All symmetric core tables and all nonlinear phases of degree at most three, through dimension four | 33,044 parameter cases |
| All nested physical core/part partitions, all core weight tables, and all nonlinear phases, through dimension three | 13,140 parameter cases |
| Sampled products of part-symmetric cores with polynomial couplings and arbitrary linear/constant terms, dimensions 4–12 | 432 parameter cases |
| Sharp internal and cross-core influence-gap families, degrees 2–10 | 18 parameter cases |
| Total twist parameter cases, with overlap between families allowed | 46,634 |
| Cross-core coordinate lower-bound checks | 14,753 |
| Internally mixed coordinate lower-bound checks | 126,240 |
| Polynomial/partition structure instances | 31,244 |
| Physical assignments checked for residual polynomial structure | 365,403 |
| Universal block-deletion checks, including every Boolean function and every deleted subset through dimension three | 2,308 |

The sampled seed is `202609200741`. Parameter families overlap and must not be described as that many distinct Boolean functions. The structure checks verify that actual restricted ANFs have no nonlinear cross-core monomials and that their residual nonlinear parts are invariant under the required transpositions. The deletion checks verify the partial Fourier mixture identity, joint entropy identity, mutual-information payment, marginal relaxation, and folded-influence concavity.

Walsh amplitudes, physical and spectral influences, and ANF restrictions are exact integers/rationals. Entropies are exact rational linear forms in logarithms of primes. Inequalities use outward rational enclosures with 48 terms of

\[
\ln x=2\sum_{k=0}^{M-1}\frac{z^{2k+1}}{2k+1}+R_M,
\quad z=\frac{x-1}{x+1},\quad
0\le R_M\le\frac{2z^{2M+1}}{(2M+1)(1-z^2)},\quad1\le x\le2,
\]

followed by outward rounding at 90 binary digits. Exact prime-log cancellation handles entropy equalities. Floating-point tolerances are not used to certify inequalities. The checker uses only Python's standard library.

Finite checks do not prove the all-dimensional theorem. Sections 3–8 supply the analytical argument, using [OWZ11] for the leaf class. The local defect-degree variant and the hereditary allocation conclusion are proved analytically; the finite coverage above should not be relabeled as exhaustive verification of every possible adaptive tree or every local witness choice.

## 11. Sources, provenance, and continuation safeguards

### Public mathematical sources

[OWZ11] Ryan O'Donnell, John Wright, Yuan Zhou. *The Fourier Entropy–Influence Conjecture for certain classes of Boolean functions*. ICALP 2011, LNCS 6755, 330–341. DOI: `10.1007/978-3-642-22006-7_28`. The author manuscript was read, including page images of Theorems 1–2. Its constants and exact symmetry hypotheses are used in Section 3.

[GMP26] María José González, Paul MacManus, María Cristina Pereyra. *Further evidence towards the Fourier Entropy-Influence conjecture*. arXiv:2606.00246v2, 2026. Its physical restriction and stopping-tree approach was consulted for current context. It is not treated as a proof of the missing universal branching estimate.

A bounded current search did not clear the publication priority of the product extension or the block formulation. Lack of a search hit is not evidence of novelty. Minimum weight of low-degree Boolean polynomials, entropy chain rules, data processing, and tensorization are standard ingredients.

### Repository dependencies actually consumed

[R1] `proofnet24/P03-fei/continuations/2026-09-20-quadratic-symmetry/REPORT.md`, blob `11605492453c978a7cb45261eb563d006fee2db0`: theorem/proof chain, scope, and quadratic product extension. Read in contiguous ranges covering the report.

[R2] `proofnet24/P03-fei/scheduled-continuation/runs/2026-09-20/2026-09-20T03-23-21Z__report.md`, blob `a2ba1c534818eba94035e8a68d884630c6d5e547`: complete single-core bounded-degree theorem, its unchanged constant through degree seven, hereditary allocation proof, direct-deletion and minor-child obstructions, and explicit lack of a higher-degree `max d_t` product theorem. This was found during continuation after an overlapping single-core derivation; its priority inside the repository is retained.

[R3] `proofnet24/P03-fei/runs/2026-09-20/2026-09-20T08-15-00Z__fei-sharp-recombination-clarkson-endpoint.md`, blob `37d0738076bd5f686a874e150f23d7ed54e7636d`: opening status and complete sharp-recombination proof, read through line 260. Its later Clarkson proof is not used as a premise here.

[R4] `proofnet24/P03-fei/solo-2026-09-17/ERASURE_REDUCTION.md`, blob `770f1fc8438b360549ed89480cb260768d839923`: complete one-coordinate identity, sharp scalar bound, and correctly quantified universal implication.

[R5] `proofnet24/P03-fei/README.md`, observed blob `9201da45afcf21156ae078cc505d37b57a1ae4b7`: current entry-point status and retired routes. The historical index and Library searches of the September 13 handoff and September 19 stability patch were used for navigation and scope; the entirety of those archives was not reread or certified.

**Superseded targets checked.** No use of the refuted absolute-overlap selector, either all-constant pointwise resolvent bound, a fixed-coefficient affine-drift payment, zero-debt boundary decomposition, the false pointwise erasure converse, or a fixed-Rényi-exponent influence payment. No contraction of an unknown seed's positive entropy excess is presented as a proof that the seed excess is nonpositive.

**New mathematical delta.** Higher-degree cross-core payment; factor-count-free product extension with the maximum per-core part count; weighted local-defect and hereditary versions; and the fixed-block joint-information formulation used in its proof. The single-core bounded-degree theorem is explicitly credited to [R2].

**Actual checks.** Exactly Section 10 and the supplied output; no independent agent or formal proof checker was used.

**Remaining full-scope gap.** No dimension-independent allocation payment for unrestricted dependent high-degree Boolean functions has been obtained. Schedules, ownership, visibility, and native finite-dimensional metrics are not changed by this report. Repository delivery does not establish that a later worker has read it.
