# Latest-partner refresh addendum

This immutable addendum records a source refresh that appeared after the run's initial partner read. The mathematical report `REPORT.md` remains immutable.

Newest completed designated partner now read:

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B01/account03-B01-20260923T170256Z-auto11-crosscompiler/REPORT.md`

(blob `8fdd457349419e52da5fed98ab618d63f5d61246` on the current master when read).

## 1. What the newest partner proves

The partner combines the same current projected-crossing source with a correlated outer-square lemma, but at projected volume **two**. In scalar-completed notation

`R=F(Y)+2Y(ell dot Z+beta)+Z^T M Z+...`,

for a split `Z=I union J` it puts

`C=M[I,J](I-Pi_row(ell_J))`,
`Z2=e_2(CC^T)`.

If `Z2>0` and every two-volume row marginal is at most `1/2`, it proves a bounded density for the residual and then

`||p_Q||_infinity <= 8.67139291595 |a|^(-1/2) (||ell_J||_2^2 Z2)^(-1/12)`.

It also corrects a source extraction point: the random two-coloring argument gives a product lower bound on two slope-bank norms, not the same lower bound on each bank separately. The source-valid consequence after orienting the larger bank is

`||ell_J||_2 >= W2^(1/4)/(2 |a|^(1/2))`

for the selected coloring, not the stronger individually-symmetric claim.

## 2. Concrete obstruction showing the new account02 theorem is complementary, not duplicate

The strict-N3 target family in this run's `REPORT.md` has, after scalar completion of `x`,

`ell_J=eps^(-1)e`,
`C=eps^(-1)w q^T`,

with `e perp q` and `w,q` unit vectors. Thus `C` has **rank one**. Therefore

`Z2=e_2(CC^T)=0`.

So the newest account03/B01 projected-volume-two compiler is genuinely unavailable on this family: its main gate fails exactly, not merely quantitatively.

By contrast the account02 theorem spends projected volume one:

`Z1=e_1(CC^T)=||C||_F^2=eps^(-2)`,

and its one-volume row marginals are `1/m<=1/2`. Hence the residual gets the borderline joint estimate

`|phi_R(t)| <= min(1,2 pi eps |t|^(-1))`,

which is not directly `L1_t` but is sufficient after the required half-Riesz weight. The resulting full-form estimate remains

`boxed: ||p_Q||_infinity <= 8`.

This is an actual obstruction/application of the newest designated-partner theorem: it isolates a rank-one projected-crossing state lying outside the partner's `Z2>0` branch and paid by the new `Z1` half-Riesz compiler.

## 3. Source-valid W2-fed version using the newest partner correction

Suppose the newest partner's random-coloring extraction selects an orientation with

`||ell_J||_2 >= W2^(1/4)/(2|a|^(1/2))`

and, on that **same orientation**, the account02 projected-one-crossing gate holds with `C!=0` and row weights at most `1/2`. Then Theorem 2.1 of `REPORT.md` gives

`||p_Q||_infinity`
` <= 8*2^(1/4) |a|^(-3/8) W2^(-1/16) ||C||_F^(-1/4)`.

No assertion is made that the random-coloring orientation automatically has the projected-crossing gate; that structural compatibility remains unpaid.

## 4. Updated exact remaining implication

The combined account02/account03 endpoint is now sharper:

- rank-two-or-higher spread projected crossing can be paid directly by newest account03/B01 via `Z2`;
- rank-one spread projected crossing can be paid by account02/B01 via `Z1`, half-Riesz, and the outer square peel;
- the unresolved near-null leakage endpoint is therefore the state in which every substantial-slope orientation has **zero/tiny projected crossing** or a **heavy one-volume row** (and hence a fortiori blocks the spread `Z2` route).

This is the structural debt `QFORM-NEARNULL-ZERO-OR-HEAVY-PROJECTED-CROSSING-ROUTING-v1`. Full QFORM remains open.
