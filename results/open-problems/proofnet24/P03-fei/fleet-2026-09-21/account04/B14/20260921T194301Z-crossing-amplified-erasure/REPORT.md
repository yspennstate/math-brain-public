# B14 — crossing-amplified corrected erasure and mass-weighted block selector

**Date:** 21 September 2026  
**Status:** **PARTIAL / PROVED new selector identities and critical-core consequences. Full uniform-cube Fourier entropy-influence remains OPEN / NOT PROVED.**  
**Execution:** `WITHOUT_VERIFIED_BRAIN`; no authenticated `math_brain` retrieval or receiver-context use occurred in this run.  
**Route:** realizable physical restriction / erasure selector, with folded-influence crossing accounting.  
**Publication priority:** **UNVERIFIED; no novelty claim.**

## 0. Fresh dependencies and the new join

This run consumed the current common FEI collaboration state and, substantively, two completed results from **account01** rather than restarting independently:

1. `account01/B14/20260921T191111Z-corrected-erasure-tube/REPORT.md` (blob `0767c0b57a9c6dab27ae2bc5f181a18a6149f70e`), which proves the corrected-entropy block rebate and the Bernoulli-erasure identity using the bounded influence potential;
2. `account01/B18/20260921T1856Z-curvature-refunded-crossing/REPORT.md` (blob `ef9f471c019a7d81e9864fd457a0e4bae9da890d`), which proves the exact **folded-influence drift**
   \[
   \mathcal J(f)-\mathbb E_z\mathcal J(f_{A=z})=I_A+C_A
   \]
   and identifies the posterior-majority crossing functional \(C_A\).

The new step is to put the *same* crossing term into the denominator of the corrected-erasure selector rather than continuing to compare corrected entropy only with ordinary influence. This produces an extra \(\rho C\) term in the all-scale critical tube, an exact mass-weighted ratio-loss identity, and a cardinality-by-cardinality deterministic block selector.

The inherited block-JS tensorization
\[
JS_A\le \sum_{i\in A}\mathfrak j(p_i)
\]
is also used at its proved scope. No every-prescribed-coordinate upper-payment statement is asserted; the known counterexamples remain untouched.

## 1. Normalization and exact block objects

Let
\[
f:\{-1,1\}^n\to\{-1,1\},\qquad
\mu(S)=\widehat f(S)^2,
\]
and let \(X\sim\mu\). Write
\[
H=H(X),\qquad p_i=\Pr(i\in X)=\operatorname{Inf}_i(f).
\]

Multiply by a character so that every current coordinate is median-centered:
\[
0\le p_i\le \frac12.
\]
This preserves spectral entropy. With
\[
\mathcal J(f)=\sum_i \min(p_i,1-p_i),
\]
the centered parent has
\[
\mathcal J(f)=I(f)=\sum_i p_i.
\]

Use
\[
\mathfrak j(p)
=
1-h_2\!\left(\frac12+\sqrt{p(1-p)}\right),
\qquad
\Phi(f)=\sum_i\mathfrak j(p_i),
\]
where \(\mathfrak j(p)=\mathfrak j(1-p)\), and define corrected entropy
\[
\mathcal F(f)=H(f)-\Phi(f).
\]
The inherited scalar cap is
\[
0\le \Phi(f)\le \frac{2}{\ln2}\,\mathcal J(f).
\tag{1.1}
\]

Fix a physical restriction block \(A\). For \(j\notin A\), let
\[
p_j(z)=\operatorname{Inf}_j(f_{A=z})
\]
for the raw restricted child. Influence is a martingale:
\[
\mathbb E_z p_j(z)=p_j.
\]

Define
\[
c_j(A)=\mathbb E_z(2p_j(z)-1)_+,
\qquad
C_A=\sum_{j\notin A}c_j(A),
\tag{1.2}
\]
and
\[
G_A
=
\sum_{j\notin A}
\left[
\mathfrak j(p_j)-\mathbb E_z\mathfrak j(p_j(z))
\right].
\tag{1.3}
\]
Because \(\mathfrak j\) is symmetric, this is exactly the potential Jensen gap after child recentering.

Let
\[
I_A=\sum_{i\in A}p_i,
\qquad
B_A=H(X_A\mid X_{A^c}).
\tag{1.4}
\]
The block restriction identity is
\[
\Delta_AH=B_A+JS_A.
\tag{1.5}
\]

Finally put
\[
R_A
=
\sum_{i\in A}\mathfrak j(p_i)-JS_A
\ge0,
\qquad
Q_A=G_A+R_A.
\tag{1.6}
\]
Thus \(R_A\) is unused recombination capacity and \(Q_A\) is the total corrected-entropy rebate.

## 2. Exact folded-influence and corrected-entropy drifts

For a surviving coordinate,
\[
\min(p_j(z),1-p_j(z))
=
p_j(z)-(2p_j(z)-1)_+.
\]
Averaging and using \(\mathbb E p_j(z)=p_j\) gives
\[
\mathbb E_z\min(p_j(z),1-p_j(z))
=p_j-c_j(A).
\]
Coordinates in \(A\) disappear. Therefore
\[
\boxed{
\Delta_A\mathcal J
:=
\mathcal J(f)-\mathbb E_z\mathcal J(f_{A=z})
=
I_A+C_A.
}
\tag{2.1}
\]

The potential drop is also exact:
\[
\Delta_A\Phi
=
\sum_{i\in A}\mathfrak j(p_i)+G_A.
\tag{2.2}
\]
Subtracting (2.2) from (1.5),
\[
\boxed{
\Delta_A\mathcal F
=
B_A-Q_A.
}
\tag{2.3}
\]

Equation (2.3) keeps *all* of the block rebate rather than replacing it only by a tangent lower bound.

The inherited reflected-tangent and strong-concavity inequalities remain available:
\[
G_A
\ge
\sum_{j\notin A}\mathfrak j'(p_j)c_j(A),
\tag{2.4}
\]
and
\[
G_A
\ge
\frac{2}{3\ln2}
\sum_{j\notin A}
\operatorname{Var}_z p_j(z).
\tag{2.5}
\]

## 3. Main theorem: exact crossing-amplified critical payment

Choose, among all nonconstant physical restriction descendants of the starting function and after character recentering, a descendant \(g\) maximizing
\[
\rho=\frac{\mathcal F(g)}{\mathcal J(g)}.
\tag{3.1}
\]
At its centered representative, \(\mathcal J=I\).

Every recentered child has corrected ratio at most \(\rho\). Hence for every block \(A\),
\[
\Delta_A\mathcal F
\ge
\rho\,\Delta_A\mathcal J
=
\rho(I_A+C_A).
\tag{3.2}
\]
Combining (3.2) with the exact identity (2.3) proves:

### Theorem 3.1 — exact block surplus payment

For every physical block \(A\) of an \(\mathcal F/\mathcal J\)-critical centered core,
\[
\boxed{
B_A
\ge
\rho I_A+\rho C_A+Q_A.
}
\tag{3.3}
\]

Equivalently,
\[
\boxed{
B_A-\rho I_A
\ge
\rho C_A
+
G_A
+
\left[
\sum_{i\in A}\mathfrak j(p_i)-JS_A
\right].
}
\tag{3.4}
\]

All three terms on the right are nonnegative. Thus the Shannon erasure surplus above slope \(\rho\) must pay, without reuse:

1. posterior-majority crossings of surviving pivotalities;
2. the full influence-potential Jensen gap;
3. any recombination capacity not actually spent by \(JS_A\).

This strictly refines the tangent-only crossing payment whenever either the Jensen gap is larger than its tangent lower bound or \(JS_A<\sum_{i\in A}\mathfrak j(p_i)\).

## 4. Fixed-cardinality balance and a deterministic physical block selector

Let \(1\le m\le n-1\), choose \(A\) uniformly among the \(m\)-subsets, and set \(q=n-m\). Define
\[
h_q=\mathbb E_{|B|=q}H(X_B),
\qquad
A_q=h_q-\frac qn H(X)\ge0.
\tag{4.1}
\]
The nonnegative \(A_q\) is the fixed-cardinality Han excess.

Write
\[
C_m=\mathbb E_{|A|=m}C_A,\quad
G_m=\mathbb E_{|A|=m}G_A,\quad
Q_m=\mathbb E_{|A|=m}Q_A,\quad
JS_m=\mathbb E_{|A|=m}JS_A.
\tag{4.2}
\]
Since
\[
\mathbb E B_A
=
\frac mn H-A_q,
\qquad
\mathbb E I_A=\frac mn I,
\tag{4.3}
\]
and on the critical core \(H=\rho I+\Phi\), averaging Theorem 3.1 gives
\[
\boxed{
\rho C_m+Q_m
\le
\frac mn\Phi-A_q.
}
\tag{4.4}
\]

Because
\[
Q_m
=
G_m+\frac mn\Phi-JS_m,
\]
(4.4) is equivalent to the exact sandwich
\[
\boxed{
A_q+G_m+\rho C_m
\le
JS_m
\le
\frac mn\Phi.
}
\tag{4.5}
\]

The right inequality is the block-JS tensorization. The left inequality is new here: actual block recombination information must simultaneously cover Han excess, full influence-instability, and folded-influence crossing cost.

### Corollary 4.2 — mass-weighted existential block selector

Assume \(I>0\). Since \(\mathbb E I_A=(m/n)I\), (4.4) implies that for **every prescribed cardinality** \(m=1,\dots,n-1\), there is an \(m\)-block \(A\) with \(I_A>0\) such that
\[
\boxed{
\frac{\rho C_A+Q_A}{I_A}
\le
\frac{\Phi}{I}
-
\frac{nA_q}{mI}
\le
\frac{\Phi}{I}
\le
\frac{2}{\ln2}.
}
\tag{4.6}
\]

In particular,
\[
\boxed{
\frac{C_A}{I_A}
\le
\frac{1}{\rho}
\left(
\frac{\Phi}{I}
-
\frac{nA_q}{mI}
\right)
\le
\frac{2}{\rho\ln2},
}
\tag{4.7}
\]
so the exact folded-influence drift of the selected physical block satisfies
\[
\boxed{
\Delta_A\mathcal J
=I_A+C_A
\le
\left(1+\frac{2}{\rho\ln2}\right)I_A.
}
\tag{4.8}
\]

This is an existential, mass-weighted physical block statement. It does **not** claim that every prescribed coordinate is cheap.

### Singleton form

For \(m=1\), \(A_{n-1}=\operatorname{DTC}(X)/n\). Thus
\[
\boxed{
\sum_i\left[\rho C_{\{i\}}+Q_{\{i\}}\right]
\le
\Phi-\operatorname{DTC}(X).
}
\tag{4.9}
\]
Consequently some relevant coordinate \(i\) satisfies
\[
\boxed{
\rho C_{\{i\}}+Q_{\{i\}}
\le
\frac{\Phi-\operatorname{DTC}(X)}{I}\,p_i.
}
\tag{4.10}
\]
This is the requested influence-mass-weighted coordinate selector: one coordinate has jointly small folded-influence crossing overhead and total corrected-entropy rebate relative to its own influence mass.

At the current inherited unrestricted lower-bound scale
\[
C_0=6.521845710923046575
\]
(calibration only; externally sourced in the repository), a counterexample above \(C_0\) would have
\[
\rho>C_0-\frac2{\ln2}
=
3.6364556291451198\ldots.
\]
The crude version of (4.7) then gives
\[
\frac{C_A}{I_A}<0.79346220,
\qquad
\frac{\Delta_A\mathcal J}{I_A}<1.79346220,
\tag{4.11}
\]
with the Han-excess term in (4.7) providing any additional improvement.

## 5. Bernoulli erasure: the missing crossing term enters exactly

Let \(A_t\) contain each physical coordinate independently with probability \(t\). Use the inherited notation
\[
D(t)=tH-\mathbb E B_{A_t}\ge0,
\quad
\mathcal J\!S(t)=\mathbb E JS_{A_t},
\quad
G(t)=\mathbb E G_{A_t},
\quad
C(t)=\mathbb E C_{A_t}.
\tag{5.1}
\]
Then
\[
\mathbb E I_{A_t}=tI
\]
and (2.1) gives
\[
\mathbb E\Delta_{A_t}\mathcal J=tI+C(t).
\tag{5.2}
\]

Using (2.3),
\[
\mathbb E\Delta_{A_t}\mathcal F
=
t\mathcal F-D(t)+\mathcal J\!S(t)-G(t).
\tag{5.3}
\]
Therefore, for any centered \(f\) with
\[
\rho=\frac{\mathcal F(f)}{\mathcal J(f)}
\]
and \(\mathcal J(f)=I(f)>0\),
\[
\boxed{
\mathbb E\left[
\Delta_{A_t}\mathcal F
-
\rho\,\Delta_{A_t}\mathcal J
\right]
=
-\left[
D(t)+G(t)+\rho C(t)-\mathcal J\!S(t)
\right].
}
\tag{5.4}
\]

### Theorem 5.1 — crossing-amplified erasure selector

If for some \(0<t<1\),
\[
\boxed{
D(t)+G(t)+\rho C(t)>\mathcal J\!S(t),
}
\tag{5.5}
\]
then some nonempty proper physical restriction has a nonconstant child whose corrected ratio \(\mathcal F/\mathcal J\) is **strictly larger** than \(\rho\).

The proof is immediate from (5.4): the empty block contributes zero to the bracketed payment defect, the full block has only constant children and zero surviving \(\mathcal J\), so a negative average must come from a proper nonconstant restriction.

This strictly strengthens the earlier corrected-erasure criterion
\[
D(t)+G(t)>\mathcal J\!S(t)
\]
whenever \(\rho>0\) and \(C(t)>0\).

Hence on an \(\mathcal F/\mathcal J\)-critical centered core,
\[
\boxed{
D(t)+G(t)+\rho C(t)
\le
\mathcal J\!S(t)
\le
t\Phi
\qquad(0<t<1).
}
\tag{5.6}
\]

Using strong concavity,
\[
\boxed{
D(t)
+\rho C(t)
+
\frac{2(1-t)}{3\ln2}
\sum_j
\operatorname{Var}(P_{j,t})
\le
\mathcal J\!S(t)
\le
t\Phi,
}
\tag{5.7}
\]
where \(P_{j,t}\) is the posterior pivotality probability of coordinate \(j\) after a Bernoulli-\(t\) restriction of the other physical variables.

Using the reflected tangent instead,
\[
\boxed{
D(t)
+
\mathbb E_{A_t}
\sum_{j\notin A_t}
\bigl(\rho+\mathfrak j'(p_j)\bigr)c_j(A_t)
\le
\mathcal J\!S(t).
}
\tag{5.8}
\]

## 6. Exact mass-weighted ratio-loss identity

The all-scale tube has a more informative interpretation.

For a restricted child \(g_{A=z}\), recenter by a character and write
\[
\rho_{A,z}
=
\frac{\mathcal F(g_{A=z})}{\mathcal J(g_{A=z})}
\]
when \(\mathcal J(g_{A=z})>0\). Constants and character states have zero \(\mathcal J\) and contribute zero below.

Because \(\mathcal F(g)=\rho\mathcal J(g)\),
\[
\Delta_A\mathcal F-\rho\Delta_A\mathcal J
=
\mathbb E_z
\left[
\mathcal J(g_{A=z})
\bigl(\rho-\rho_{A,z}\bigr)
\right].
\tag{6.1}
\]
Averaging over Bernoulli blocks and using (5.4) yields the exact identity
\[
\boxed{
\mathcal J\!S(t)
-
D(t)
-
G(t)
-
\rho C(t)
=
\mathbb E_{A_t,z}
\left[
\mathcal J(g_{A=z})
\bigl(\rho-\rho_{A,z}\bigr)
\right].
}
\tag{6.2}
\]

Thus the residual in the crossing-amplified tube is not an anonymous slack: it is precisely the **surviving-folded-influence-weighted loss of corrected ratio** under physical restriction.

There is an exact fixed-cardinality version. If \(|A|=m\),
\[
\boxed{
JS_m-A_q-G_m-\rho C_m
=
\mathbb E_{|A|=m,z}
\left[
\mathcal J(g_{A=z})
(\rho-\rho_{A,z})
\right].
}
\tag{6.3}
\]
Also
\[
\boxed{
\mathbb E_{|A|=m,z}\mathcal J(g_{A=z})
=
\left(1-\frac mn\right)I-C_m.
}
\tag{6.4}
\]

Therefore, whenever the denominator in (6.4) is positive, the \(\mathcal J\)-size-biased mean child ratio is exactly
\[
\boxed{
\rho
-
\frac{
JS_m-A_q-G_m-\rho C_m
}{
(1-m/n)I-C_m
}.
}
\tag{6.5}
\]
Consequently at least one proper nonconstant \(m\)-block child has corrected ratio at least the quantity in (6.5).

This gives a concrete stopping-policy criterion: find a cardinality \(m\) for which Han excess, influence-instability, and crossing cost consume most of \(JS_m\). Then a genuinely lower-dimensional physical descendant preserves almost all of the critical corrected ratio. No biased restriction value is assumed; (6.5) is an existence statement extracted from uniform physical restrictions.

## 7. Finite decisive check

`verify_crossing_amplified_tube.py` is a finite sanity check, not part of the proof. It exhausts Boolean functions modulo global output sign through \(n=3\), enumerates all physical descendants, selects an \(\mathcal F/\mathcal J\)-maximizing descendant, character-recenters it, and then checks every physical block and every nontrivial block cardinality.

Results:

- critical cores checked: `124`;
- fixed-cardinality cases checked: `212`;
- maximum absolute folded-\(\mathcal J\) drift identity error: `0.0`;
- maximum absolute corrected-entropy identity error: `1.1102230246251565e-16`;
- maximum criticality violation: `0.0`;
- maximum lower-sandwich violation in (4.5): `0.0`;
- maximum upper-sandwich violation in (4.5): `0.0`;
- maximum mass-weighted selector violation in (4.6): `0.0`;
- maximum absolute ratio-loss identity error in (6.3)/(6.5): `1.6653345369377348e-16`;
- maximum absolute surviving-\(\mathcal J\) identity error in (6.4): `1.1102230246251565e-16`.

The analytic proof above does not depend on the finite computation.

Verifier source SHA-256:
`b973e9c059344afa9c544081be16a644208050c7ae5258d5834d68826839bf54`.

Verification-output SHA-256:
`2e8a153db53fb61398e63085edef3971dd1eab203f09028cfb4657c9a73fed88`.

## 8. What changed and what remains

**What changed.** The previous corrected-erasure tube compared corrected entropy against ordinary removed influence and therefore had
\[
D+G\le \mathcal J\!S
\]
on a critical descendant. The folded-influence accounting shows that the true denominator loses
\[
I_A+C_A,
\]
not merely \(I_A\). The missing term is therefore not optional: on a corrected-ratio critical core the stronger necessary condition is
\[
\boxed{D+G+\rho C\le \mathcal J\!S.}
\]
At fixed cardinality, this becomes the exact mass-weighted balance (4.5), and the residual is the descendant ratio loss (6.3).

**What remains.** This does **not** prove FEI. A high-ratio critical core can survive only if, at every erasure scale, all three of the following simultaneously fit inside the same recombination bank:

1. spectral Han/dependence deficit;
2. full influence-posterior instability;
3. posterior-majority crossings, multiplied by the current corrected ratio \(\rho\).

The next universal implication should exploit that triple suppression together with the signed Boolean all-shift convolution identities. In particular, a useful target for the next A/B interface is:

> show that if a primitive centered Boolean core has small \(G(t)\) and small \(C(t)\) at every scale while the mass-weighted ratio-loss residual in (6.2) is small, then its pivotality rows are quantitatively close to a jointly integrable low-complexity family, forcing a dimension-independent bound on \(\mathcal F/\mathcal J\).

That is the remaining gap. Full uniform-cube FEI remains **OPEN / NOT PROVED**.
