# FEI for monotone Boolean functions: status, three failed routes, exact data

24 September 2026. The Fourier entropy-influence conjecture for monotone functions is not proved here. This note
records where the monotone case stands, three natural routes that fail (each with an explicit example), and exact
computations over every monotone function of at most six variables and over monotone graph properties on at most
seven vertices.

Notation as in continuation 2026-09-23-readk-dnf: P(S) is the squared Walsh coefficient of the ±1 version of f,
H = sum P log2(1/P), I = sum |S| P(S), Inf_i = sum over S containing i of P(S). For a coordinate i,
Delta_i = H(f) - (H(f|x_i=0) + H(f|x_i=1))/2, and rho_0(f) = min over relevant i of Delta_i/Inf_i. Since
I(f) = Inf_i + (I(f|x_i=0) + I(f|x_i=1))/2 and restrictions of monotone functions are monotone, a bound
rho_0 <= K for all monotone f would give H <= K I for all monotone f.

## 1. Where the monotone case stands

- FEI for monotone functions would give total influence Omega(log^2 n) for every monotone graph property on n
  vertices with constant variance (Friedgut and Kalai, 1996). The best bound known is
  Omega(log^2 n / (log log n)^2) (Kelman, Kindler, Lifshitz, Minzer and Safra, GAFA 2020), which improved
  Bourgain and Kalai's (log n)^(2 - eps). So the monotone case contains a question that is itself open.
- Monotone classes with FEI proved: symmetric functions (O'Donnell, Wright and Zhou 2011); read-once formulas over
  AND and OR (O'Donnell and Tan 2013) and over symmetric threshold gates of any fan-in (2026-09-23-readk-dnf, 760
  bits); delta-tribes and monotone functions with the tribe separation property (Gonzalez, MacManus and Pereyra,
  arXiv:2606.00246); read-k monotone DNF (O(log k)); regular functions, including every linear threshold function
  (15.1, or 14.22 with the level-entropy bound of OWZ); monotone functions whose desirability preorder has width w
  ((15.1 + log2 w) I, Remark rem:width of the 09-23 paper); Boolean functions of m regular functions
  ((16.5 + 8.4 ln m) I).
- What these leave out is the transitive case: functions with almost no desirability relations and no read-once
  structure, such as graph properties.

## 2. Exact data

### 2.1 Every monotone function on at most six variables

`code/mono_enum.py` enumerates the monotone functions (Dedekind numbers; each count is checked) and computes H, I and
rho_0 exactly by the Walsh-Hadamard transform (Parseval and sum_i Inf_i = I hold to 0 in every case).

| n | monotone functions | max H/I | attained by | max rho_0 |
|---|---|---|---|---|
| 2 | 6 | 2.000000 | AND_2 | 4.000000 |
| 3 | 20 | 2.955890 | AND_3 | 4.867669 |
| 4 | 168 | 3.402476 | AND_4 | 4.867669 |
| 5 | 7,581 | 3.623740 | AND_5 | 4.867669 |
| 6 | 7,828,354 | 3.739764 | AND_6 | 5.194872 |

For n <= 5 the step constant is maximised by AND_3 (with dummy variables). At n = 6 it is maximised by the function
that equals 1 on the seven points of weight at least 5 and on the three points of weight 4 whose zeros form the
perfect matching {1,6}, {2,5}, {3,4}. All six coordinates have influence 3/16 and ratio Delta_i/Inf_i = 5.194872,
and H/I = 3.3127. The same value 5.1949 was found at n = 6 by hill climbing over all Boolean functions on
20 September, so at six variables the extremal function for the restriction step is monotone.

### 2.2 Monotone graph properties on five to seven vertices

`code/graph_props.py` evaluates each property on all 2^N graphs (N = 10, 15, 21 edge variables, uniform measure).
All edges are equivalent, so rho_0 = Delta_e/Inf_e for any edge e. The connected fractions 728/1024,
26704/32768 and 1866256/2097152 match the known counts of connected labelled graphs.

| property | H/I, n = 5, 6, 7 | rho_0, n = 5, 6, 7 |
|---|---|---|
| connected | 3.2768, 3.7455, 3.9288 | 4.6688, 5.1082, 4.9327 |
| contains a triangle | 3.2862, 3.9937, 4.3532 | 3.8531, 4.8268, 4.8325 |
| contains a cycle | 2.9868, 3.5813, 3.7309 | 3.5204, 4.2436, 3.7955 |
| contains an odd cycle | 3.2590, 3.9919, 4.3075 | 3.5306, 4.9620, 4.8230 |
| Hamiltonian | 3.4409, 3.5505, 3.6752 | 4.2926, 4.3320, 4.3615 |
| matching of size floor(n/2) | 3.9397, 4.0452, 4.3007 | 4.9974, 5.6393, 4.6717 |
| contains K4 | 3.9363, 3.9546, 3.9560 | 5.1370, 4.9104, 4.8779 |
| no isolated vertex | 3.5959, 3.8758, 3.9416 | 5.4390, 5.3423, 4.9123 |
| maximum degree at least 3 | 3.2381, 3.8305, 3.9456 | 3.9786, 4.2823, 3.9002 |
| minimum degree at least 2 | 3.2381, 3.2750, 3.4063 | 3.9786, 3.6287, 3.5912 |
| at least N/2 edges (symmetric) | 2.4559, 2.3560, 2.4628 | 3.0557, 0.0000, 0.0000 |

At these sizes nothing approaches the known extremes, both reached along the self-compositions of Numaro's balanced
monotone 18-variable function (H/I tends to 6.5218 there and rho_0 is certified at 7.05 on 104,976 variables).
Sizes this small say little about the asymptotic question in Section 1.

## 3. Three routes that fail

### 3.1 Shifting to a regular function

The shift S_ij replaces f(x_i=1, x_j=0, y) and f(x_i=0, x_j=1, y) by their maximum and minimum. For monotone f it never
increases total influence, and repeated shifts end at a regular function, for which FEI holds with 15.1. If each shift
satisfied H(f) - H(S_ij f) <= C (I(f) - I(S_ij f)), FEI for regular functions would give FEI for all monotone
functions. It does not. Take f with values ±1 (1 for true) and x in {-1,1}^n, and write
f = a + x_i b_i + x_j b_j + x_i x_j c in the pair (x_i, x_j), with a, b_i, b_j, c functions of the other coordinates.
The shift leaves a, c and b_i + b_j unchanged and replaces the pair (b_i, b_j) by (max(b_i, b_j), min(b_i, b_j))
pointwise. The influence it
removes is (I(w) - I(|w|))/2 with w = b_i - b_j, which vanishes when no edge joins a point with w = 1 to a point with
w = -1, while the spectral entropy can still move. For f = x_i x_j OR x_i y_1 OR x_j y_2
(`code/shift_counterexample.py`), S_ij f = x_i x_j OR x_i (y_1 OR y_2) OR x_j y_1 y_2 and

    H(f) = 3.000000,  I(f) = 1.5,   H(S_ij f) = 2.216917,  I(S_ij f) = 1.5.

One shift lowers the entropy by 0.783083 bits and leaves the total influence unchanged. An argument through shifting
would have to control a whole chain of shifts at once.

### 3.2 Restricting on the coordinate of maximal influence

F4's Proposition 6.1 (continuation 2026-09-22-opus-team) gives the monotone function
F_n(y, z) = Maj_n(y) OR (z AND [y = y*]), with y* of weight (n-1)/2, whose coordinate z has Inf_z = 2^-n and
B_z/Inf_z >= (n - 3 log2 n)/2 for odd n >= 11, where B_z = H(1[z in S] | S minus z) <= Delta_z. Exactly
(`code/maxinf_selector.py`):

| n | 3 | 5 | 7 | 9 | 11 | 13 | 15 |
|---|---|---|---|---|---|---|---|
| Delta_z/Inf_z | 5.9218 | 6.6596 | 7.4244 | 8.2239 | 9.0605 | 9.9254 | 10.8112 |
| B_z/Inf_z | 3.5231 | 4.2427 | 4.9888 | 5.7834 | 6.6185 | 7.4829 | 8.3685 |

Replace each y_j by Maj_k of fresh variables and call the result G. It is monotone, and Delta_z and Inf_z do not
change. Indeed Maj_k is balanced, so the spectral sample of G is that of F_n with every index j it contains replaced by
an independent sample of Maj_k, which gives H(G) = H(F_n) + sum_j Inf_{y_j}(F_n) H(Maj_k); the same identity holds for
the two restrictions in z, and Inf_{y_j}(F_n) is the average of the influences of y_j in those restrictions, so
Delta_z(G) = Delta_z(F_n); and z is pivotal for G exactly when it is pivotal for F_n at the induced (uniform) y.
By brute force for n = k = 3: Inf_z = 0.125, B_z = 0.440389 and Delta_z = 0.740223 before and after. Each leaf of the
j-th block has influence
Inf_{y_j}(F_n) iota_k with iota_k = C(k-1, (k-1)/2) 2^(1-k) <= (2/(pi k))^(1/2). Once iota_k < 2^-n, z is the unique
coordinate of maximal influence, and there Delta_z/Inf_z >= (n - 3 log2 n)/2 is unbounded. So even for monotone
functions the restriction step cannot be taken at the coordinate of maximal influence.

In G the coordinate z is also maximal for the desirability preorder. Given a leaf w of block j, fix the other
variables of block j so that its majority equals y*_j whatever w is, and the other blocks so that their outputs agree
with y*. Then G(w=0, z=1) = 1 because y = y*, while G(w=1, z=0) = Maj_n(y*) = 0; so no leaf is at least as desirable
as z. In F_n itself every y_j is at least as desirable as z, and z is minimal; the composition makes it maximal. The
rule "restrict on a most desirable coordinate", which is what the proof for regular functions suggests, fails as well. For general functions this is
F4's Proposition 6.2, whose base function is bent; the base function here is monotone. Together with F4's
Proposition 6.1 (no per-coordinate bound) and Remark 6.3 (no rule depending only on Inf_i and eta_i), any selection
rule for monotone functions has to look at more of the function than its influences.

### 3.3 Biased FEI+ for regular gates

Read-once formulas whose gates are regular functions, and more generally monotone functions whose modular
decomposition has regular prime components, would follow from the biased form of FEI+ for regular functions by the
composition theorem of O'Donnell and Tan. The regular functions include the weighted threshold functions, and for
those the biased form is open: the unequal-bias proof for symmetric threshold gates (2026-09-23-readk-dnf, report
section 27) uses an exponential tilt that works through the lattice of counts, and for weighted thresholds the tilt
does not control the total correlation (report section 28). This route therefore contains the open weighted-threshold
case.

## 4. What would finish the monotone case

The restriction lemma: there is K such that every nonconstant monotone f has a coordinate i with
Delta_i(f) <= K Inf_i(f). It gives H <= K I for all monotone functions. What is known about K and about the choice
of i:

- K >= 7.05, certified on the self-compositions of Numaro's monotone function (F4), and K >= 5.1949 at six variables
  (Section 2.1).
- The coordinate cannot be taken arbitrarily (F4, Proposition 6.1), at maximal influence (Section 3.2), or by a rule
  that sees only Inf_i and eta_i (F4, Remark 6.3).

A reduction in the other direction: every monotone function is a read-once composition, along its modular
decomposition, of AND, OR and prime monotone functions. By the composition theorem of O'Donnell and Tan, the biased
form of FEI+ for the prime components, with one constant under all product measures, implies FEI. The functions that
matter most here, graph properties among them, are prime, so this relocates the difficulty rather than reducing it;
it does show that nothing is lost at the AND and OR nodes.

## Files

- `code/mono_enum.py`, `logs/mono_enum_n1_5.log`, `logs/mono_enum_n6.log`: every monotone function on n <= 6 variables.
- `code/graph_props.py`, `logs/graph_props.log`: graph properties on 5-7 vertices.
- `code/shift_counterexample.py`, `logs/shift_counterexample.log`: Section 3.1.
- `code/maxinf_selector.py`, `logs/maxinf_selector.log`: Section 3.2.
- `code/desirability_check.py`, `logs/desirability_check.log`: the desirability remark of Section 3.2 (n = k = 3).
