# QFORM Gaussian heat-height closure

**Run:** `20260922T211430Z-fleet04-B15-heat-regularity-r4`  
**Account/slot:** fleet04/B15  
**Outcome:** `ESSENTIAL_STEP_APPLIED / EXACT_POSITIVE_REGULARIZATION_NORMAL_FORM`  
**Full universal bound:** OPEN  
**Fixed-instance continuity:** PROVED by the completed B15 partner chain and used here  
**Brain status:** `WITHOUT_VERIFIED_BRAIN`

## 1. Target and separation of claims

Let \(X=(X_1,\ldots,X_n)\) have independent real coordinates with probability
densities \(0\le f_i\le1\), and let \(A=A^T\) have at least three eigenvalues
of absolute value at least one. Put
\[
Q=X^TAX,\qquad \mu_Q=\mathcal L(Q).
\]
The owner asks separately for:

1. absolute continuity of \(\mu_Q\);
2. a universal bound on its density;
3. a continuous representative.

The completed fleet02/B15 theorem, consumed through the completed
fleet01/B15 handoff below, proves for every fixed rank-\(\ge3\) instance that
\(\mu_Q\) has a matrix-dependent bounded density \(p_Q\in C_0(\mathbb R)\).
Thus (1) and (3), and fixed-instance boundedness, are closed. The only
remaining target is uniformity of the height over all admissible dimensions,
matrices and product laws.

This report proves an exact positive finite-scale formulation of that
remaining height problem.

## 2. Heat functional

For \(\varepsilon>0\), define
\[
\gamma_\varepsilon(u)
 =\frac1{\sqrt{2\pi}\varepsilon}
   \exp\!\left(-\frac{u^2}{2\varepsilon^2}\right),
\qquad
H_\varepsilon(\mu;y)
 =\int\gamma_\varepsilon(x-y)\,d\mu(x).
\]
For the quadratic output this is the positive expectation
\[
H_\varepsilon(Q;y)
 =\mathbb E\,\gamma_\varepsilon(X^TAX-y).
\]
Let
\[
M_\varepsilon(\mu)=\sup_{y\in\mathbb R}H_\varepsilon(\mu;y).
\]

## 3. Exact heat-height theorem

### Theorem 3.1

For every Borel probability measure \(\mu\) on \(\mathbb R\):

1. \(M_\varepsilon(\mu)\) is nonincreasing as \(\varepsilon\) increases.
2. For every \(C<\infty\),
   \[
   \sup_{\varepsilon>0}M_\varepsilon(\mu)\le C
   \quad\Longleftrightarrow\quad
   \mu=p\,dx\ \text{with}\ \|p\|_\infty\le C.
   \]
3. Consequently, with the convention \(+\infty\) when no bounded density
   exists,
   \[
   \boxed{\quad
   \sup_{\varepsilon>0,y\in\mathbb R}
   H_\varepsilon(\mu;y)=\|p\|_\infty .
   \quad}
   \]
4. If \(p\in C_0(\mathbb R)\), then
   \[
   \|p*\gamma_\varepsilon-p\|_\infty\longrightarrow0,
   \qquad
   M_\varepsilon(\mu)\uparrow\max_y p(y)
   \quad(\varepsilon\downarrow0).
   \]

### Proof

The Gaussian semigroup identity is
\[
\gamma_{\varepsilon_2}
 =\gamma_{\varepsilon_1}*
   \gamma_{\sqrt{\varepsilon_2^2-\varepsilon_1^2}}
 \qquad(0<\varepsilon_1<\varepsilon_2).
\]
Convolution by a probability density contracts \(L^\infty\). Hence
\[
M_{\varepsilon_2}(\mu)\le M_{\varepsilon_1}(\mu),
\]
proving (1).

If \(\mu=p\,dx\) and \(\|p\|_\infty\le C\), then
\[
H_\varepsilon(\mu;y)=(p*\gamma_\varepsilon)(y)\le C,
\]
so the forward bound is immediate.

Conversely, assume \(H_\varepsilon(\mu;y)\le C\) for all
\(\varepsilon,y\). For every nonnegative \(\varphi\in C_c(\mathbb R)\),
Tonelli and the assumed bound give
\[
\int \varphi(y)\,d(\mu*\gamma_\varepsilon)(y)
 =\int \varphi(y)H_\varepsilon(\mu;y)\,dy
 \le C\int\varphi(y)\,dy.
\]
The measures \(\mu*\gamma_\varepsilon\) converge weakly to \(\mu\) as
\(\varepsilon\downarrow0\). Therefore
\[
\int\varphi\,d\mu\le C\int\varphi\,dy
\quad\text{for every nonnegative }\varphi\in C_c.
\]
By regular approximation this says \(\mu(E)\le C|E|\) for every Borel set
\(E\), hence \(\mu=p\,dx\) with \(0\le p\le C\) almost everywhere.

Taking the least \(C\) proves (2) and (3). Alternatively, when
\(p\in L^\infty\), the lower equality follows by choosing a Lebesgue point
\(y\) with \(p(y)>\|p\|_\infty-\eta\) and using
\((p*\gamma_\varepsilon)(y)\to p(y)\).

Finally, every \(C_0\) function is uniformly continuous. Splitting the
Gaussian integral into \(|u|\le\delta\) and \(|u|>\delta\), uniform
continuity controls the first part and the Gaussian tail controls the
second, uniformly in \(y\). Thus
\(\|p*\gamma_\varepsilon-p\|_\infty\to0\). A nonnegative
\(p\in C_0\) with integral one attains its maximum, proving (4). \(\square\)

## 4. Fourier representation without an absolute-Wiener premise

For every probability law, Gaussian damping makes the inversion integral
absolutely convergent:
\[
\boxed{\quad
H_\varepsilon(\mu;y)
 =\frac1{2\pi}\int_{\mathbb R}
 e^{-ity}\widehat\mu(t)e^{-\varepsilon^2t^2/2}\,dt .
\quad}
\]
Indeed \(|\widehat\mu(t)|\le1\) and the Gaussian multiplier is integrable.
This identity does not assert that \(\widehat\mu\in L^1\), and it does not
use the false pointwise quadratic-phase decay claim. The real-space
functional remains manifestly nonnegative.

There is also a direct small-ball consequence. Since
\[
\gamma_r(u)\ge \frac{e^{-1/2}}{\sqrt{2\pi}\,r}
\quad\text{for }|u|\le r,
\]
one has
\[
\boxed{\quad
\Pr\{|Q-y|\le r\}
 \le \sqrt{2\pi e}\,r\,H_r(Q;y).
\quad}
\]
Thus any uniform bound on the positive heat functional gives linear
small-ball scaling immediately. The exact density constant is recovered
without the factor \(\sqrt{2\pi e}\) by Theorem 3.1.

## 5. Application of the completed fleet01/B15 result

The completed partner result is fleet01/B15 r13:

- canonical commit:
  `yspennstate/math-open-problems@1b7a876f7577cf99599322926154ce0032a034fd`;
- path:
  `proofnet24/QFORM-density/fleet-2026-09-22/fleet01/B15/20260922T210451Z-fleet01-B15-qform-r13/REPORT.md`.

It proves with zero loss that the sharp full target constant \(C_{\rm full}\)
equals the sharp constant \(C_{\rm AS}\) restricted to:

- \(s_3(A)=1\), where \(s_3\) is the third largest singular value;
- strictly positive real-analytic Schwartz marginal densities;
- marginal caps \(f_i\le1\).

Combining that theorem with Theorem 3.1 gives the actual target-level
identity
\[
\boxed{
C_{\rm full}
 =
\sup_{\substack{s_3(A)=1\\
 f_i>0\ {\rm analytic\ Schwartz}\\
 \|f_i\|_\infty\le1}}
\ \sup_{\varepsilon>0,\ y\in\mathbb R}
\mathbb E\,
\frac{\exp(-(X^TAX-y)^2/(2\varepsilon^2))}
     {\sqrt{2\pi}\varepsilon}.
}
\]

This is an end-to-end equivalence, not merely a necessary condition.

To see the forward implication, if the full density bound is \(C\), then
convolution contraction gives every heat functional at most \(C\).

For the reverse implication, assume the displayed heat functional is at
most \(C\) on the normalized analytic-Schwartz subclass. Theorem 3.1 gives
\(\|p_Q\|_\infty\le C\) for every member of that subclass. Hence
\(C_{\rm AS}\le C\), and the partner theorem yields
\(C_{\rm full}=C_{\rm AS}\le C\).

The normalization is exact: if \(s=s_3(A)\ge1\) and \(A_0=A/s\), then
\(s_3(A_0)=1\), \(Q=sQ_0\), and
\[
\|p_Q\|_\infty=s^{-1}\|p_{Q_0}\|_\infty.
\]

## 6. Regularity ledger

The completed fleet02/B15 theorem
(`yspennstate/math-open-problems@9b8bb7e84811978a2c46c7bb5ec50f2570dbc056`)
proves that every fixed rank-\(\ge3\) target instance has
\[
p_Q\in C_0(\mathbb R)\cap L^\infty(\mathbb R),
\]
with a matrix-dependent bound. Therefore:

- absolute continuity is proved for every target instance;
- continuity, uniform continuity, vanishing at infinity, and attainment of
  the maximum are proved for every target instance;
- the owner’s stronger continuity request is closed qualitatively;
- the universal height is still open.

For each fixed target instance the heat profiles satisfy
\[
M_\varepsilon(Q)\uparrow\max_y p_Q(y)
\quad(\varepsilon\downarrow0).
\]
No uniform rate in \(\varepsilon\) is claimed. Such a rate would require
uniform control not supplied by the density cap alone.

## 7. First unpaid implication

The remaining problem is exactly to prove a universal bound for the
positive normalized heat functional in Section 5, uniformly in dimension,
the normalized symmetric matrix, the analytic-Schwartz product law,
the center \(y\), and the heat scale \(\varepsilon\).

The formulation avoids three known invalid shortcuts:

1. it never rotates the product law into spectral coordinates;
2. it does not require pointwise decay of the undamped characteristic
   function;
3. it does not select and invert a single tiny coordinate minor.

A successful proof may retain cancellation through the Gaussian-damped
Fourier representation, or work directly with the positive real-space
kernel. Either way, it must aggregate original-coordinate product
structure before paying reciprocal local-minor costs.

## 8. Control and provenance

Freshly re-read before publication:

- `scheduled_tasks/README.md`, blob
  `fca13a89d221115332ce5e60d49554ee0e213efa`;
- live `CORRECTION_INBOX.json`, blob
  `c7000cf3822ae4935a2faf43b89ac92ea65ac0fe`;
- `assignments/fleet04/B15.json`, blob
  `ad3b34a7b78902175a8ef48cc496854a7b617cfd`.

scheduler, notification, email, permission, public-release, or task-setting
change was made. Repository use is not native brain ingestion; status
remains `WITHOUT_VERIFIED_BRAIN`.
