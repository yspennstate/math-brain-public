# R19 / I0120 — gcd-boundary strata and an exact obstruction to the first factor-aligned level-15 route

Date: 2026-09-17 UTC.  
Status: **PARTIAL / source OPEN / no `N_LR` movement**.  
Scope: this note proves a structural lemma about the Sungkawichai--Trakulthongchai finite-checking properness condition and gives one exact relation-compatible improper branch through levels `1,3,5,15`. It does **not** refute `LRC(14)`, does **not** prove a prime gate nonempty in the eventual sense, and does **not** claim that the exhibited residue remains improper at every later level.

## 1. Framework and the question tested

For the active R19 claim `I0120`, `k=14`, so the lonely-runner threshold is `1/(k+1)=1/15`. For a prime `p` and a positive integer `l`, Sungkawichai--Trakulthongchai call a tuple `v in Z_{p,l}^k` `(k,p,l)`-proper when either

1. for some coordinate `i`,

   `gcd(l,v_1,...,omit v_i,...,v_k)>1`,

or

2. there is `t in (lp)^(-1) Z` with `||t v_j|| >= 1/(k+1)` for every `j`.

Otherwise the tuple is improper. Their lifting sieve retains exactly the improper lifts.

The preceding mandatory stuck report selected one recovery experiment: imitate the successful fourteen-total-runner proof at the composite target scale `15=3*5`, beginning with the simplest short relation

`v_2 = 2 v_1`

and the prime `p=37`. The first question was deliberately modest: can a factor-aligned path

`1 -> 3 -> 15`

or

`1 -> 5 -> 15`

force every surviving relation-compatible branch into the gcd-proper clause at level `15`?

The answer is **no**. The obstruction is not accidental: the gcd clause has a sharp minimal boundary stratum with exactly two coordinates escaping a prime divisor, and no-witness cores can be inflated directly onto that boundary.

## 2. Exact gcd-boundary criterion

For a prime `q | l`, define

`e_q(v) = #{j : q does not divide v_j}`.

### Lemma R19-LR6 — gcd properness is exactly the `e_q <= 1` boundary

For any integer tuple `v=(v_1,...,v_k)` and positive integer `l`, the gcd clause

`there exists i with gcd(l,v_1,...,omit v_i,...,v_k)>1`

holds if and only if

`there exists a prime q | l with e_q(v) <= 1`.

Consequently, a tuple that fails the gcd clause satisfies

`e_q(v) >= 2` for every prime `q | l`.

#### Proof

Suppose the gcd clause holds for an index `i`. Choose any prime `q` dividing the displayed gcd. Then `q|l` and `q|v_j` for every `j != i`. Thus at most the omitted coordinate is nondivisible by `q`, so `e_q(v)<=1`.

Conversely, if `q|l` and `e_q(v)<=1`, omit the unique `q`-nondivisible coordinate if one exists, and omit any coordinate if `e_q(v)=0`. Then `q` divides `l` and every retained coordinate, so the corresponding gcd is at least `q>1`. QED.

This exposes the relevant boundary. The gcd clause kills the strata `e_q=0` and `e_q=1`; the **minimal gcd-improper stratum is `e_q=2`**.

## 3. Two-unit inflation of a no-witness core

The next lemma explains why a composite terminal factor need not kill the last branches.

Fix integers `k>=4`, a prime `p`, a positive integer `l`, and a prime `q != p`. Call a tuple

`y=(y_1,...,y_{k-2}) in Z_{p,l}^{k-2}`

a **blocking core at threshold `1/(k+1)`** if for every integer `a` there is some `j` such that

`||(a/(lp)) y_j|| < 1/(k+1)`.

Notice that the threshold here is the `k`-coordinate threshold, not the natural threshold for a `(k-2)`-runner problem.

### Lemma R19-LR7 — two-unit inflation

Assume `y` is such a blocking core. Choose integers `z_1,z_2` with

`gcd(z_1,pql)=gcd(z_2,pql)=1`.

Then

`v=(q y_1,...,q y_{k-2},z_1,z_2)`

is `(k,p,ql)`-improper.

If, in addition, an integer relation is supported entirely on the core coordinates and holds for `y` modulo `lp`, then the corresponding scaled relation holds for `v` modulo `qlp`.

#### Proof: witness clause

Take any candidate grid time

`t=a/(qlp)`.

For a core coordinate,

`||t(q y_j)|| = ||a y_j/(lp)||`.

By the blocking-core hypothesis, at least one of these `k-2` quantities is strictly below `1/(k+1)`. Therefore **no** time in `(qlp)^(-1) Z` is a witness for all `k` coordinates of `v`.

#### Proof: gcd clause

Let `r` be any prime divisor of `ql`. Both `z_1` and `z_2` are nondivisible by `r`. After omitting any one coordinate of `v`, at least one of `z_1,z_2` remains. Hence not all retained coordinates can be divisible by `r`. This is true for every prime divisor `r` of `ql`, so

`gcd(ql,v_1,...,omit v_i,...,v_k)=1`

for every `i`. Thus the gcd clause also fails.

The tuple is therefore improper.

For the relation statement, if `sum_j m_j y_j = 0 mod lp`, then

`sum_j m_j(qy_j) = q sum_j m_j y_j = 0 mod qlp`.

QED.

### Interpretation

The lemma embeds any lower-level no-witness core into the minimal gcd-improper boundary by appending two unit coordinates. If `q` is the new terminal factor, the scaled core may be completely `q`-divisible while the two units force

`e_q(v)=2`,

which is exactly one step beyond the gcd clause's killing range.

This is the mechanism the first factor-aligned recovery idea was missing.

## 4. Exact `p=37`, relation `(2,1)` survivor

Set

`p=37`, `k=14`, and

`Y = (3,6,11,5,7,46,1,8,13,2,9,10)`.

This twelve-coordinate core lives at level `l=3`, modulus `lp=111`. The executed exact checker verifies:

1. every coordinate is nonzero modulo `37`;
2. `Y_2 = 2 Y_1` modulo `111` (indeed as an integer equality, `6=2*3`);
3. for every numerator `a mod 111`, at least one coordinate has

   `15 * min(aY_j mod 111, -aY_j mod 111) < 111`.

Thus `Y` is a blocking core at the fifteen-runner threshold `1/15`.

Now take `q=5`, append the two units `1,2`, and set

`T=(5Y,1,2)`,

that is

`T=(15,30,55,25,35,230,5,40,65,10,45,50,1,2)`.

Since `1` and `2` are units modulo `37*3*5=555`, Lemma R19-LR7 proves immediately that `T` is `(14,37,15)`-improper. It also retains the exact relation

`T_2=2T_1`.

Moreover,

`e_5(T)=2`,

so this is **exactly** a minimal gcd-improper boundary survivor for the terminal factor `5`.

## 5. The same branch survives both factor orders through level 15

The checker does more than certify the endpoint. For each

`l in {1,3,5,15}`

it projects `T` modulo `37l` and verifies all of the following exactly:

- every coordinate remains nonzero modulo `37`;
- the relation `v_2=2v_1 mod 37l` holds;
- there is no grid witness in `(37l)^(-1) Z` at threshold `1/15`;
- the gcd-proper clause has no valid omitted coordinate.

The exact summaries are:

| level `l` | modulus `37l` | witness count | gcd-proper omissions | `e_3` | `e_5` |
|---:|---:|---:|---|---:|---:|
| 1 | 37  | 0 | none | 10 | 8 |
| 3 | 111 | 0 | none | 11 | 3 |
| 5 | 185 | 0 | none | 10 | 2 |
| 15| 555 | 0 | none | 11 | 2 |

Therefore the same relation-compatible residue branch survives

`1 -> 3 -> 15`

and also

`1 -> 5 -> 15`.

Any exact lift sieve that starts with this level-one class, retains every improper relation-compatible lift, and hopes that merely reaching the factor-aligned terminal level `15` forces the gcd clause cannot close on this branch.

This is a **finite-route obstruction only**. It does not show that the level-one class is non-eventually-proper: a later level not tested here may still kill every lift. It therefore does not prove `J_{(2,1)}^rel(14,37)` nonempty, and it is not a counterexample to the Lonely Runner Conjecture.

## 6. Section-B moves used

### #6 DEFORM TO A POINT YOU CAN SOLVE

Instead of attacking the whole level-15 survivor space, deform to the divisibility boundary `e_5=2`. On this boundary the endpoint splits into a twelve-coordinate level-3 blocking core plus two unit padding coordinates. This is not merely an analogy: Lemma R19-LR7 gives an exact construction, and `T=(5Y,1,2)` is its smallest concrete pilot found in this run.

**Outcome:** successful as a structural diagnosis. It gives a complete explanation of one survivor and refutes the hope that the first factor-aligned terminal level automatically forces gcd properness.

### #21 ASK WHO ELSE HAS THIS SHAPE

The relevant shape already sits inside the published finite-checking framework: Definition 2.1's gcd clause is a divisibility-boundary test, and Allikvere's fourteen-runner terminal computation succeeds because its no-witness completions fall *inside* that killing boundary (all coordinates divisible by `7`). The recent restricted fifteen-runner congruence-family paper also has to split the common-divisor branches for the composite count `15`; it explicitly does not settle general fifteen runners.

**Outcome:** the useful portable object is not “composite terminal level” by itself but the defect count `e_q`. The fourteen-runner success has `e_7=0`; the present fifteen-runner branch has the minimal surviving value `e_5=2`.

### #29 ADD THE POINTS AT INFINITY

Treat the divisibility patterns `e_q=0,1,2,...` as boundary strata of the lift state space. The gcd clause compactifies away the first two strata (`0` and `1`). The first new boundary face is `e_q=2`, and Lemma R19-LR7 shows that lower-level blocking cores can land on it systematically.

**Outcome:** the terminal problem is sharpened. Future work must classify or eliminate the `e_q=2` boundary strata; simply choosing a level divisible by `15` is not a termination mechanism.

## 7. Consequence for the active route

The selected STUCK-RECOVERY-1 experiment has produced a decisive negative result about its first implementation:

> **Factor alignment alone is insufficient.** At `p=37` and the easiest support-two relation `v_2=2v_1`, both natural paths to level `15` retain an exact improper branch, and the branch lies on the minimal gcd-improper boundary `e_5=2`.

This is useful progress because it prevents the next run from spending its budget on a larger version of the same terminal-level enumeration.

The active source theorem remains open and the fixed metric remains `N_LR=14`. The next run should attack the boundary mechanism itself, not add another state-space compression. Suggested unused Section-B moves for I0120 are **#12 FIND WHAT IS CONSERVED, #13 FIND WHAT ONLY INCREASES, #25 COUNT THE SAME THING TWICE**. One concrete question is whether a relation-compatible lift admits an invariant or monovariant controlling the pair of exceptional unit coordinates on every `e_q=2` boundary face; a positive answer could supply the missing termination mechanism, while a negative answer should yield a durable survivor classification for handoff.

## 8. Exact finite evidence

Checker:

`artifacts/R19/2026-09-17_14-36-19_UTC__i0120_boundary_check.py`

Archived execution:

`artifacts/R19/2026-09-17_14-36-19_UTC__i0120_boundary_check_output.txt`

The output ends

`ALL_EXACT_CHECKS_PASS`.

The finite checker is a self-check of the displayed residue claims. The general Lemmas R19-LR6 and R19-LR7 are proved on the page above and do not depend on the computation.

## 9. Literature boundary

Primary line checked 2026-09-17:

- Touch Sungkawichai and Tanupat Trakulthongchai, arXiv:2604.23906v2, *Eleven, twelve, and thirteen lonely runners*: Definition 2.1 gives exactly the witness/gcd properness used above and Proposition 3.1 gives the lift sieve.
- Jaan Allikvere, arXiv:2609.02604v1, *Fourteen lonely runners*: full current record, with a `7^13` mixed-level terminal calculation; every no-witness completion in the certified gates is gcd-proper because all coordinates are divisible by `7`; the recurring two-orbit pattern is explicitly empirical.
- Matthias Beck and Samuel Everett, arXiv:2609.06259v1, *Lonely Runner Relations*: supplies the short-relation localization used by the broader R19 route.
- *A certified congruence family for fifteen lonely runners* (2026-09-05) is a restricted congruence-family theorem and explicitly does not resolve the general fifteen-runner case.

A bounded current search found no unrestricted proof or refutation of `LRC(14)`. This negative search is not a novelty certificate.
