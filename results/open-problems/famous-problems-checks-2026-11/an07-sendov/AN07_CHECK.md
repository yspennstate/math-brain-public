# AN07 Sendov's conjecture: the 2026 proof, read and tested

Checked 12 Nov 2026 by an agent.

## Verdict

Sendov's conjecture is proved for every degree, and with it the Phelps–Rodriguez strengthening. The row should
leave the open list.

Sources:

- L. Mazur, "A Computer-Assisted Proof of Sendov's Conjecture", public version of 5 August 2026 (ProofAtlas),
  AI-generated, verified in Lean (about 90,000 lines). Not read here.
- T. Tao, "A digestion of the proof of Sendov's conjecture", What's New, 12 August 2026. A streamlined
  human-readable version of the argument, with its own Lean formalization (about 15,000 lines,
  github.com/teorth/sendov). Read here: introduction, Section 1 and Section 2 in full. Not read: Section 3
  (a new proof of Rubinstein's theorem, the case a = 1, known since 1968), the n <= 4 section (classical,
  Meir–Sharma), the Lean code.
- S. An, arXiv 2609.04246 (22 Aug 2026): the last scalar inequality with an exact rational certificate on 34
  slabs in alpha. Read here: Sections 1–3 and the start of Section 4; the certificate was not run.
- Earlier: n <= 8 Brown–Xiang; large n Tao (Acta Math. 229, 2022), made effective by Zhang (arXiv 2609.20256).

## The argument

A counterexample of degree n >= 5 has zeros a, z_1, ..., z_{n-1} with 0 <= a < 1 and critical points
a - 1/q_j with all z_j, q_j in the closed unit disk. Four identities link the two point sets (Lemma 6:
centroid, polar, first and second origin identity; they come from p'(z) at infinity, p(1/a)/p'(a), p(0),
p'(0)). The case a = 0 is immediate. With alpha = (n-1)(1-a^2)/2, x = Re mean(q_j) and
beta(t) = 1 - 2atx + a^2 t^2:

- Polar inequality (Prop. 10): the Möbius map gives |(1-a z_j)/(a-z_j)| >= 1, then AM–GM on
  prod |t(1-a^2)q_j + a|, then 1 + y <= e^y, give 1 < int_0^1 exp(alpha(-1 + (2 - beta(1))t)) dt, and from it
  0 < beta(1) < min(alpha/(3+alpha), 1 - log(alpha)/alpha).
- Origin inequality (Prop. 11): F(t) = prod(1 - a t q_j) satisfies F' = -(n-1)a(x+iy)F + error, the error
  bounded by Maclaurin's inequality and Cauchy–Schwarz; the two origin identities turn F(1) and int F into
  expressions in J = prod z_j q_j and sum 1/z_j; the defect lemma (Lemma 13) and the centroid identity
  replace sum 1/z_j by the mean of the q_j at a cost 1 - |J|^2; monotonicity in |J| reduces to |J| = 1. The
  result is (19), then alpha <= 17 (20), then the form (21) in alpha, beta(1), n.
- The right side of (21) increases with beta(1), so beta(1) is replaced by its polar bound, leaving a
  function of (alpha, n) that must be >= 1. It is below 0.399 for n > 200 by a direct estimate and below 1
  for 5 <= n <= 200 by computation (Lean in Tao's version; a rational certificate in An's).

## What was checked

By hand: the passage from the differential identity to (32); (33) from (9) and (10); the substitution of the
defect estimate; the monotonicity in |J| that gives (36) from (34) and (35); the rearrangement giving (19);
formulas (10)–(13) of An from his (6).

By computer (an07_check2.py, floating point, random and grid tests, output an07_check2.out):

| step | test | result |
|---|---|---|
| Lemma 6 (7)–(10) | 1926 random polynomials, degree 3–10 | largest relative error 7e-12 |
| (24)–(25) and the exponential bound | 4000 point sets, 8 values of t | no violation |
| derivative bound (Maclaurin step) | same sets | largest ratio 0.98 |
| Lemma 13 (defect lemma) | 20000 point sets | largest ratio 1.0000, no violation |
| step after the defect lemma | 3000 configurations satisfying the centroid identity | largest ratio 0.79 |
| (27) log(sinh h/h) <= sqrt(h^2+9) - 3 | 40000 values of h up to 400 | no violation |
| (17) implies (18) | 4,000,000 grid points, 3,113,093 satisfying (17) | no violation |
| (35) | 5 <= n < 400 | holds; discriminant changes sign between n = 4 and 5 |
| constants in alpha <= 17 | direct | 0.18244 (text 0.1825), 1.9476 (text 1.948) |
| (19) implies (21) | 40000 random (a, x, n), n up to 250 | no violation |
| (22), 5 <= n <= 200 | alpha step 0.005 | largest value 0.8528 at n = 53, alpha = 17 (text: 0.853 at n = 53) |
| n > 200 | direct | 0.3990 (text 0.399); (3+17)c(17)^4 = 1.1530 (text 1.1529) |

The last scalar inequality in An's form, with both polar bounds (an07_check.py, output an07_check.out):
23,986,000 grid points over n = 6..300, alpha in (0, 17] with step 0.01, 50 values of eta per alpha. The
supremum of F is 0.704023 at n = 35, alpha = 10.11, eta at the polar bound; F never decreases in eta on the
grid; on a finer grid 0.7040302 at alpha = 10.1095. For n from 500 to 10^6 the maximum falls from 0.252 to
0.2497 (limit 1/4). An's proved bound is 0.966537. The two suprema differ (0.853 against 0.704) because (22)
uses only alpha/(3+alpha) while An also uses 1 - log(alpha)/alpha.

## Limits of this check

The computer tests are floating-point evaluations on random samples and grids; they would catch a wrong
statement or a wrong constant, they do not prove the inequalities. The rigorous closing of the finite range
is the Lean verification and An's certificate, neither run here. Mazur's original text, the Lean code,
Section 3 and the n <= 4 section of the exposition were not read.

## Literature

arXiv search all:Sendov AND all:conjecture, by date, 30 entries (lit/search/s1.xml): papers after August 2026
build on the result (An 2609.04246; Zhang 2609.19126 on the quadratic Tang–Zhang inequality; Bouthat–Fallat
2610.12499 on Borcea's quadratic variance conjecture); none disputes it. A second search, abs:Sendov by date, 25
entries (lit/search/s2.xml), shows the same papers and nothing that disputes the proof; the older claimed proofs
it lists (Petrov 2104.00348, Drury–Lin 2210.08720) predate it.

## For the list

Remove AN07. Open neighbours stated in the exposition: Borcea's conjecture for general q, Schmeisser's
conjecture, Smale's mean value problem.
