# Independent review: normalized multiscale hybrid reference

**Verdict:** PASS for the stated fixed-gate recursive-composition theorems. A small scale-count notation refinement is recommended below. The result does not establish unrestricted FEI.

**Reviewed source:** `fei_proof_20260922/path_b/REPORT.md`, read in full. This review independently derives the normalization, source weighting, omitted-KL sums, and all-depth constants. Numerical checks are not used as substitutes for these arguments.

## 1. Source law and the I-projection normalization

For a fixed balanced gate with nonempty squared spectrum \(\pi\), composition on disjoint blocks has a unique active-child pattern at each active node. Every nonempty leaf set determines its active subtree. Fourier coefficients multiply along that tree, so squared coefficients give the claimed independent nonempty branching generator.

The expected number of active height-\(j\) nodes under the source is \(\mu^{m-j}\). The entropy is therefore
\[
H(P_m)=h\sum_{j=1}^m\mu^{m-j}
=\frac{h}{\mu-1}(\mu^m-1).
\]
Equal gate influences give equal leaf occurrences \(r=(\mu/b)^m\), and \(Nr=\mu^m>1\).

For \(0<r<1\), the function
\[
\phi(c)=1-(1-cr)^N-c
\]
has \(\phi(0)=0\), positive derivative \(Nr-1\) at zero, strictly negative value at one, and strict concavity. Thus there is exactly one positive root in \((0,1)\). Conditioning a Bernoulli-\(t\) product law on nonemptiness with \(t=cr\) has occurrence \(t/c=r\), as required.

With \(u_j=1-(1-t)^{b^j}\), one has \(u_m=c\), and the conditional child-pattern probabilities
\[
R_j(T)=u_{j-1}^{|T|}(1-u_{j-1})^{b-|T|}/u_j
\]
sum to one. All their entries are positive. Conditional on child activation, disjoint child blocks have the required independent product laws. The source/reference hierarchy and the displayed local KL formula are valid.

## 2. Hybrid normalization and correct active-node weights

Replacing \(R_j\) by \(\pi\) at a prescribed set of heights defines a normalized law: every local transition is a normalized distribution on nonempty child patterns. This remains true when \(\pi\) has zero entries.

A \(P_m\)-positive leaf set uses only \(\pi\)-positive patterns. Consequently it has positive hybrid probability. On that support, the hybrid/reference likelihood ratio is exactly the product of the selected local \(\pi/R_j\) factors.

The expectation in the certificate is under \(P_m\), so the active-node weights are \(\mu^{m-j}\), independently of how often those nodes would be active under the hybrid law. This is an important distinction, and the report uses the correct weights.

The identity
\[
D(P_m\Vert Q_m)-\mathbb E_{P_m}\log(\widetilde Q/Q_m)
=D(P_m\Vert\widetilde Q)
\]
proves both the variational lower bound and nonnegative omitted credit. Its exact value is the sum of the unselected local divergences with source weights. It is not a sum of unrelated event inequalities and does not reuse KL credit.

Outside the source support, zero hybrid atoms can give a minus-infinite test. The report's positive-\(\delta Q_m\) regularization is valid; at a fixed finite depth the source-support expectation converges without a support ambiguity.

## 3. Finite-depth omitted-scale bound

The three inequalities
\[
u_j\le bu_{j-1},\quad u_{j-1}\ge t,\quad
-\log_2(1-u_{j-1})=b^{j-1}\ell
\]
give
\[
d_j\le(\mu-1)\log_2(1/t)
 +(b-\mu)b^{j-1}\ell+A.
\]
The signs are correct because \(\mu>1\) and \(b-\mu>0\).

For \(L<j\le M\),
\[
\sum_j\mu^{m-j}
=\frac{I\mu^{-L}-\mu^{m-M}}{\mu-1}.
\]
Independently,
\[
\sum_j\mu^{m-j}(b-\mu)b^{j-1}\ell
=I\ell\bigl[(b/\mu)^M-(b/\mu)^L\bigr].
\]
These two exact geometric sums reproduce Theorem 5.1. No endpoint term or multiplicative factor is missing.

## 4. Two-sided truncation and the epsilon constants

Under \(I\ge2\),
\[
\phi(1/2)=1/2-(1-r/2)^N
\ge1/2-e^{-I/2}>0,
\]
so the positive root satisfies \(c>1/2\). Thus
\[
\log_2(1/t)\le m\log_2(1/\alpha)+1.
\]
With the prescribed ceiling for \(L\), the first discarded contribution is at most \(\varepsilon I/2\).

For the other term, using \(t\le\alpha^m\le1/2\),
\[
\ell\le \frac{t}{(1-t)\ln2}
\quad\Longrightarrow\quad
I\ell\alpha^{-(m-K)}
\le \frac{2I\alpha^K}{\ln2}.
\]
The stated ceiling for \(K\) makes this at most \(\varepsilon I/2\). Intersecting selected heights with \([1,m]\), retaining all heights when the cutoffs meet, and retaining all finitely many shallow exceptional depths correctly covers every \(m\ge1\).

The implication from error \(\varepsilon I\) to \(2\varepsilon(I-1)\) uses \(I\ge2\) exactly where needed. At shallow exceptional depths the loss is zero, so the displayed certificate remains valid.

Minor notation refinement: a bound intended uniformly over \(m\ge1\), \(0<\varepsilon\le1\) should be written
\[
O_g(1+\log m+\log(1/\varepsilon))
\]
or with \(\log(m+1)\). Without the constant term the formal expression is zero at \(m=1,\varepsilon=1\). The explicit cutoffs are already correct; this does not affect the substantive theorem.

## 5. Majority and the all-depth center-6 certificate

For ternary majority, the local spectrum has four equiprobable patterns, giving \(h=2,\mu=3/2,\alpha=1/2,A=0\).

The small-depth full-retention assertion is correct. If there is an omitted interval, using \(M=m\) in Theorem 5.1 yields the displayed bottom-only remainder. The choice of \(L_m\) makes its first term at most \(I/4\). For \(m\ge6\), its second term is at most \(64I/(63\ln2)\). Thus
\[
\text{loss}\le\left(\frac14+\frac{64}{63\ln2}\right)I
<\frac{149}{84}I.
\]
The last strict inequality follows from \(\ln2>2/3\).

The inequality \((149/84)I\le2(I-1)\) is equivalent to \(I\ge168/19\). At \(m\ge6\), \(I\ge729/64>168/19\), so the stated all-depth bound follows. At every other depth the loss is zero when all heights are retained.

Combining with the exact family identity \(H=4(I-1)\) gives the retained-certificate center 6. This is an information-extraction certificate for a family whose exact entropy ratio is already 4, not an improved universal FEI constant.

## 6. Limits that must remain explicit

The physical disjoint composition tree and equal leaf occurrences are essential hypotheses. For a general fixed regular gate, the constants depend on the actual gate, including \(h/(\mu-1)\); no gate-independent bound is proved.

The count concerns retained hierarchy heights. It does not bound the number of active nodes, coordinates, Fourier atoms, or computational operations. Even a few retained heights can involve exponentially many physical nodes.

Extending the normalized hybrid construction to arbitrary composition-prime sources, or proving a universally affordable adaptive hierarchy, remains open. The report states these limits correctly.

**Review conclusion:** normalization, weighting, omitted-scale bound, and constant choices pass independent analytic verification.

