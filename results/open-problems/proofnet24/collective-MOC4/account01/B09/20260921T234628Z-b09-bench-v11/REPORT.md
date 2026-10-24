# MOC4 account01/B09 — exact obstruction to one-point-marginal coefficient lifts

**Directive:** `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`  
**Campaign:** MOC4 (Marcus-de Oliveira, all complex normal \(4\times4\) pairs)  
**Worker:** account01/B09  
**Outcome:** `CANDIDATE_REFUTED` for `MOC4-P-MARGINAL-LIFT-v1`; **MOC4 itself remains open**.  
**Brain status:** `WITHOUT_VERIFIED_BRAIN`.

## Source-exact target

For complex normal \(4\times4\) matrices \(A,B\), with eigenvalues
\(a_1,\dots,a_4\) and \(b_1,\dots,b_4\), prove
\[
\det(A+B)\in
\operatorname{conv}\left\{
\prod_{i=1}^4(a_i+b_{\sigma(i)}):\sigma\in S_4
\right\}.
\]

The current collective source record is
`scheduled_tasks/work/shared/collective-open-problems-2026-09-22/TARGETS.md`.
It points to Drury (2004), Bebiano--da Providencia (2025), and
Mulero-Martinez (2026) and explicitly records that the full \(n=4\) target is
not known from those sources.

## Consumed other-account result

I used the completed exact result from account04/B09,
`MOC4-U-LIFT-v1`, scientific commit
`ee33c17ceed673859063d8e53d0ecd9b05fd9fa5`.
That report proves that for a particular rational orthogonal \(U\), no single
spectrum-independent probability law on \(S_4\) realizes all one- and two-set
squared-minor marginals
\[
|\det U[S,T]|^2.
\]
It does **not** refute the determinant hull, because the convex weights are
allowed to depend on the spectra.

The next natural weakening is therefore:

> `MOC4-P-MARGINAL-LIFT-v1`. For each fixed \(U,a,b\), can one choose
> spectrum-dependent convex weights \(\lambda_\sigma\) that reproduce the
> determinant and at least retain the one-point marginals
> \(\Pr_\lambda[\sigma(i)=j]=|u_{ij}|^2\)?

This report gives an exact negative answer while simultaneously certifying
that the same determinant is still inside the full 24-point hull.

## Exact unitary and spectra

Use the rational real orthogonal matrix
\[
U=\begin{pmatrix}
 492/625&-31/625&-48/125&12/25\\
 -9/25&12/25&-4/5&0\\
 -36/125&48/125&9/25&4/5\\
 -256/625&-492/625&-36/125&9/25
\end{pmatrix}.
\]
This is the same exact unitary obstruction supplied by account04/B09.

Choose genuinely complex spectra
\[
a=(-2-3i,\,-2,\,3+i,\,-1-2i),
\qquad
b=(3,\,2-i,\,3-2i,\,2+3i).
\]

Writing
\[
z_\sigma=\prod_{i=1}^4(a_i+b_{\sigma(i)}),
\qquad
D=\det(\operatorname{diag}(a)+U\operatorname{diag}(b)U^*),
\]
the exact principal-minor/Cauchy--Binet expansion gives
\[
D=\frac{-28853804-9702716\,i}{390625}.
\tag{1}
\]

## Exact no-go certificate for first-order-compatible convex weights

Let
\[
c(z)=8\Re z+5\Im z.
\]
For the upper-left \(3\times3\) one-point incidence variables use the affine
majorant
\[
c(z_\sigma)\le
176+\sum_{1\le i,j\le3}Y_{ij}\mathbf 1_{\{\sigma(i)=j\}}
\quad(\sigma\in S_4),
\tag{2}
\]
where
\[
Y=
\begin{pmatrix}
-250&16&-356\\
-604&-596&-1196\\
1020&1020&432
\end{pmatrix}.
\]
The verifier checks (2) exactly for all 24 permutations.

Hence any probability law \(\lambda\) on \(S_4\) whose one-point marginals
equal
\[
P_{ij}=|u_{ij}|^2
\]
must satisfy
\[
\sum_\sigma\lambda_\sigma c(z_\sigma)
\le
176+\sum_{1\le i,j\le3}Y_{ij}P_{ij}
=
-\frac{281803724}{390625}.
\tag{3}
\]

But (1) gives
\[
c(D)
=
-\frac{279344012}{390625}
=
-\frac{281803724}{390625}
+\frac{2459712}{390625},
\tag{4}
\]
and
\[
\frac{2459712}{390625}>0.
\]
Therefore **no spectrum-dependent convex representation of \(D\) can also
have the first-order marginals \(|u_{ij}|^2\)**.

This is strictly stronger than merely observing negative formal
coefficient weights: it is a genuine unitary-plus-spectra obstruction with
an exact dual separating certificate.

## The same point is nevertheless inside the Marcus-de Oliveira hull

The obstruction above is not a counterexample to MOC4. In fact \(D\) has
the following exact 3-point convex representation.

Using 1-based permutation notation,
\[
\sigma_1=(1,2,4,3),\qquad
\sigma_2=(2,1,3,4),\qquad
\sigma_3=(2,3,4,1),
\]
the corresponding permutation products are
\[
z_{\sigma_1}=-90+10i,\qquad
z_{\sigma_2}=20-28i,\qquad
z_{\sigma_3}=-152-56i.
\]
With
\[
\lambda_1=\frac{15487992}{46953125},\qquad
\lambda_2=\frac{78732333}{234765625},\qquad
\lambda_3=\frac{78593332}{234765625},
\]
all three weights are positive, sum to one, and
\[
D=\lambda_1z_{\sigma_1}
+\lambda_2z_{\sigma_2}
+\lambda_3z_{\sigma_3}.
\tag{5}
\]

Thus this example sharply separates two statements:

1. the actual determinant-hull assertion survives; but
2. any proof that insists its spectrum-dependent convex weights preserve
   even the \(k=1\) squared-modulus marginals of \(U\) fails.

## Consequence for the shared proof strategy

The account04/B09 result killed a **spectrum-independent** common
\(\wedge^1/\wedge^2\) permutation coupling. The present certificate shows
that allowing the weights to depend on \(a,b\) still does not rescue the
strategy if one insists on the natural one-point marginals
\(|u_{ij}|^2\).

So a viable full proof must permit the final convex weights to move away
from those first-order marginals, or avoid a permutation-weight lift and
prove the support inequality directly:
\[
\Re(e^{-i\theta}D)
\le
\max_{\sigma\in S_4}
\Re\!\left(
e^{-i\theta}\prod_i(a_i+b_{\sigma(i)})
\right)
\quad\text{for every }\theta.
\]

The first remaining structural question I recommend to the MOC4 lead is:
**what weaker, support-direction-dependent constraints on the final
permutation weights are actually forced by the common unitary and are still
strong enough to prove the support inequality?**

## Verification

`verify_p_marginal_obstruction.py` uses only exact
`fractions.Fraction` arithmetic. It checks:

- \(U^TU=I\);
- all exterior-minor coefficients needed in the exact determinant expansion;
- the exact determinant value (1);
- inequality (2) on all 24 permutations;
- the exact dual bound (3) and positive gap (4);
- positivity and normalization of the three weights in (5);
- exact equality in the 3-point hull certificate.

Observed verifier output:

```text
PASS
D = (Fraction(-28853804, 390625), Fraction(-9702716, 390625))
three-point weights = [Fraction(15487992, 46953125), Fraction(78732333, 234765625), Fraction(78593332, 234765625)]
dual_bound = -281803724/390625
target = -279344012/390625
gap = 2459712/390625
```

No claim is made that MOC4 is proved or disproved.
