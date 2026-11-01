# fleet04/B18 — dimension-uniform rare-corner closure for the antipodal EQ family

**Run:** `20260922T041349Z-b18-fei-r20`  
**Classification:** `ESSENTIAL_STEP_APPLIED / DIMENSION_UNIFORM_BOUNDARY_CLOSED`.  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.  
**Full unrestricted uniform-cube FEI:** **OPEN / NOT PROVED**.

## 0. Exact live target and why this is not a duplicate

The current owner control converges FEI on the all-gate inequality
\[
D_\Gamma(G;p):=
\sum_i {\operatorname{It}_i(G;p)\over V_{p_i}}
\bigl(\Gamma(p_i)+h_2(V_{p_i})\bigr)
-\Gamma(p_{\rm out})-\widetilde H_G(p)\ge0,
\qquad V_u=4u(1-u).
\tag{0.1}
\]
A finite symmetric nonnegative potential satisfying (0.1) for every Boolean gate/product bias would imply full FEI.

I use the newest source-defined stable candidate from fleet01/B18,
`fleet01/B18/20260922T0325Z-addressing-star-cdagger/REPORT.md`:
\[
C^\dagger=6.521851214,
\qquad
\Gamma^\dagger(z)=\Gamma_0(z)+a^\dagger z(1-z),
\qquad
a^\dagger=0.268204856,
\tag{0.2}
\]
where `Gamma_0` is the committed h96 read-once candidate with
`Gamma_0(1/2)=C_0=6.4548`.

The fresh fleet04/B13 theorem proved the arbitrary-bias formulas for the antipodal two-corner gate `EQ_d` and excluded every fixed-ratio rare-corner ray. During this run I found and read the newer fleet01/B16 theorem `20260922T0350Z-eq-hierarchical-rare-corner`, which already closes hierarchical rare-corner escape **for each fixed arity**. I therefore do not repeat that result. The new statement below is arity-uniform: one explicit neighborhood works simultaneously for every finite `d>=3`, including sequences in which `d` itself tends to infinity.

This run also preserves, without spending them again, fleet01/B18's earlier curvature-refunded physical-restriction identity, fleet04/B18's mixed-curvature law and exact zero-depth one-point classification, fleet04/B12's child-slack conservation, and fleet04/B14's two-face reserve. None is promoted into an unconditional FEI closure here.

## 1. The theorem

Let `EQ_d` be the sign function that is `-1` on `0^d` and `1^d` and `+1` elsewhere. Put
\[
\varepsilon:=2^{-13}={1\over8192}.
\tag{1.1}
\]

### Theorem 1.1 — one boundary box for all arities

For every integer `d>=3` and every interior product-bias vector
\[
p=(p_1,\ldots,p_d)\in(0,1)^d
\]
with
\[
\boxed{\sum_{i=1}^d p_i\le2^{-13},}
\tag{1.2}
\]
the stable candidate obeys
\[
\boxed{D_{\Gamma^\dagger}(\operatorname{EQ}_d;p)>0.}
\tag{1.3}
\]
The same holds, by input-complement symmetry, whenever
\[
\boxed{\sum_i(1-p_i)\le2^{-13}.}
\tag{1.4}
\]
More quantitatively, if `p_1>=p_2>=...>=p_d`, then
\[
\boxed{
D_{\Gamma^\dagger}(\operatorname{EQ}_d;p)
\ge {69369496937\over1024000000000}\,p_1p_2
>0.06774364935\,p_1p_2.
}
\tag{1.5}
\]
Thus no arity-growing sequence of antipodal gates can escape through either rare corner while the **total** rare-side mass tends below this fixed threshold.

## 2. Read-once one-corner reserve

Let `N_d` be the one-corner NOR sign gate, `-1` only at `0^d`. Write
\[
Q=\prod_i(1-p_i),
\qquad s=\sum_i p_i.
\]
Its biased influences satisfy
\[
{\operatorname{It}_i(N_d;p)\over V_{p_i}}=Q_{-i},
\]
so its Poincare-defect currency is exactly
\[
W_N={I(N_d;p)\over4}-Q(1-Q)
=Q\,[s-(1-Q)].
\tag{2.1}
\]
If `X_i` are independent Bernoulli variables of means `p_i` and `K=sum_i X_i`, then
\[
s-(1-Q)=E[K]-Pr(K\ge1)=E[(K-1)_+].
\tag{2.2}
\]
On the event `X_1=X_2=1`, `(K-1)_+>=1`; hence
\[
\boxed{s-(1-Q)\ge p_1p_2.}
\tag{2.3}
\]
Under (1.2), `Q>=1-s>=1-epsilon`.

The certified read-once theorem is valid for
\[
\Gamma_{\rm cert}(z)=\Gamma_0(z)+0.01z(1-z).
\]
The exact quadratic-lift identity says that replacing `Gamma` by
`Gamma+bz(1-z)` adds `b[I/4-p_out(1-p_out)]` to every gate defect. Therefore, with
\[
b:=a^\dagger-0.01=0.258204856,
\tag{2.4}
\]
we have
\[
D_{\Gamma^\dagger}(N_d;p)
\ge bW_N
\ge b(1-\varepsilon)p_1p_2.
\tag{2.5}
\]
Numerically and exactly in the decimal normalization used here,
\[
b(1-\varepsilon)=0.2581733368525390625\ldots .
\tag{2.6}
\]

## 3. Adding the antipodal corner: an arity-uniform entropy cost

Put
\[
P=\prod_i p_i.
\]
The fleet01/B16 fixed-arity theorem proves the exact spectral perturbation estimate
\[
\boxed{
\|\mu_{\rm EQ}-\mu_N\|_1\le(8\,2^d+4)P.
}
\tag{3.1}
\]
For completeness, its mechanism is elementary: for every nonempty spectral set the cross product between the NOR coefficient and the all-ones point perturbation has magnitude `4PQ`, the perturbation has total squared mass `4P`, and the empty coefficient contributes at most `8P`.

Let `delta` be total variation of the two squared-Fourier laws. Since
\[
\delta\le(4\,2^d+2)P\le5\,2^dP=:\zeta,
\tag{3.2}
\]
and (1.2) implies `P<=epsilon^d`, we have `zeta<1/2` for every `d>=3`.
Fannes--Audenaert on an alphabet of size `2^d`, followed by
`h_2(x)<=x log_2(1/x)+x/ln2`, gives
\[
\begin{aligned}
|\widetilde H_{\rm EQ}-\widetilde H_N|
&\le h_2(\zeta)+\zeta\log_2(2^d-1)\\
&\le\zeta\left[\log_2{1\over P}-\log_2 5+{1\over\ln2}\right]\\
&\le\boxed{5\,2^dP\log_2{1\over P}},
\end{aligned}
\tag{3.3}
\]
because `log_2 5>1/ln2`.

Set
\[
R={P\over p_1p_2}=\prod_{i=3}^d p_i,
\qquad L=\log_2(1/\varepsilon)=13.
\]
For every `i`,
\[
R\log_2{1\over p_i}\le\varepsilon^{d-2}L.
\tag{3.4}
\]
Indeed, for `i>=3` factor out `p_i` and bound every other factor of `R` by `epsilon`; for `i=1,2`, use `p_3<=p_i` and the monotonicity of `x log(1/x)` on `(0,epsilon]`. Summing (3.4),
\[
R\log_2{1\over P}\le d\varepsilon^{d-2}L.
\tag{3.5}
\]
Substitution into (3.3) yields the dimension-explicit but uniformly summable bound
\[
\boxed{
|\widetilde H_{\rm EQ}-\widetilde H_N|
\le20d(2\varepsilon)^{d-2}L\,p_1p_2.
}
\tag{3.6}
\]
The coefficient decreases with `d>=3`, since the ratio of consecutive terms is
\[
{d+1\over d}(2\varepsilon)<1.
\]
Its maximum is therefore at `d=3`:
\[
20\cdot3\cdot(2\varepsilon)\cdot13
=120\varepsilon L
={1560\over8192}
=0.1904296875.
\tag{3.7}
\]

## 4. The output-potential term is favorable throughout this box

There is no hidden output-potential loss in (3.6). On the small side write
\[
z=2^{-x},\qquad \Gamma_0(z)=zG(x).
\]
The committed h96 source diagnostics, already consumed in fleet01/B18's star theorem and the read-once analytic tail work, give the conservative source inequalities
\[
G(x)>4.9096x+2.22,
\qquad |G'(x)|<31.
\tag{4.1}
\]
(The stored transformed derivative bound is `|Ghat'|<=30.080`; `Ghat=G+0.003(1-2^{-x})`, so the weakened `31` bound follows.) Since `1/ln2<3/2`, for `x>=13`
\[
\Gamma_0'(z)
=G(x)-{G'(x)\over\ln2}
>4.9096\cdot13+2.22-{93\over2}
=19.5448>0.
\tag{4.2}
\]
The added quadratic has positive derivative on this interval, so
\[
\boxed{(\Gamma^\dagger)'(z)>0\quad(0<z\le2^{-13}).}
\tag{4.3}
\]

For NOR the negative output mass is `Q`; for EQ it is `Q+P`. Put `u=1-Q`. Then `u<=s<=epsilon`, and by symmetry of the potential
\[
\Gamma^\dagger(Q+P)-\Gamma^\dagger(Q)
=\Gamma^\dagger(u-P)-\Gamma^\dagger(u)\le0.
\tag{4.4}
\]
Thus the output-potential change helps rather than hurts when the second corner is added.

The remaining new input terms are
\[
\sum_iP_{-i}\bigl(\Gamma^\dagger(p_i)+h_2(V_{p_i})\bigr)\ge0.
\tag{4.5}
\]
Consequently
\[
\boxed{
D_{\Gamma^\dagger}(EQ_d;p)
\ge D_{\Gamma^\dagger}(N_d;p)
-|\widetilde H_{EQ}-\widetilde H_N|.
}
\tag{4.6}
\]

## 5. Finish the estimate

Combine (2.5), (3.7), and (4.6):
\[
D_{\Gamma^\dagger}(EQ_d;p)
\ge
\left[b(1-\varepsilon)-{1560\over8192}\right]p_1p_2.
\tag{5.1}
\]
With `b=0.258204856` and `epsilon=1/8192`, the bracket is exactly
\[
\boxed{
{69369496937\over1024000000000}
=0.0677436493525390625\ldots>0,
}
\tag{5.2}
\]
which proves (1.3)--(1.5). Replacing every input by its complement exchanges the two rare corners and preserves the symmetric candidate, proving (1.4).

## 6. What changed and what remains unpaid

**PROVED for the fixed source candidate:** the antipodal `EQ_d` family is safe in one explicit rare-corner neighborhood that is independent of arity. This strengthens the fresh fleet01/B16 fixed-arity hierarchical theorem by ruling out an adversarial sequence in which arity grows while the rare-side total mass tends to zero. The proof retains a quantitative margin rather than an `o(1)` statement.

**PRESERVED:** the exact mixed-curvature identity, the all-zero-depth one-point classification with `H<4J`, the child-slack conservation law, the two-face orientation/checkerboard surcharge, and all previously refuted bridges. None is used as an unsupported shortcut.

**OPEN / unpaid:** this does not prove `D_{Gamma^dagger}(EQ_d;p)>=0` throughout the compact/mixed-bias region, does not treat arbitrary composition-prime gates, and does not prove full FEI. The smallest honest all-gate target remains a source-valid proof or counterexample for arbitrary prime gates/product biases. For this particular antipodal family, the remaining search is now away from both arity-uniform rare-corner boxes.

## 7. Independent checker

`CHECKER.py` directly reconstructs biased Fourier laws for NOR/EQ on 480 deterministic unequal-bias cases in dimensions 3--6, tests (3.1), tests the exact NOR Poincare-currency identity, and checks the all-d rational constants. It returned `PASS` with

- maximum Parseval error `1.110e-15`;
- maximum observed L1/bound ratio `0.914561692786`;
- exact analytic final gap coefficient `0.06774364935253906...`.

Checker SHA-256: `8f8b4585907e854893158bd56d9a53e9c8045b543ac014a7dbbb084934a94efc`.  
Captured-output SHA-256: `a1f3df8376a108e94cdf24888f7edb41d18c73068a726e63f4b61e4d0740b5e2`.

The finite calculations are regression/falsification checks only; the theorem is Sections 2--5.

No novelty or publication-priority claim is made. No email/Drive action, paid or remote compute, workflow dispatch, permission change, notification change, benchmark gold, or unrelated private data entered this run.
