# B17 — gate extremality: exact addressing collapse and sparse-defect reduction

**Date:** 2026-09-22  
**Classification:** `ESSENTIAL_STEP_APPLIED`  
**Full Friedgut–Kalai FEI:** **OPEN / NOT PROVED**.

## 1. Exact target and source binding

This run uses the current gate reformulation in
`proofnet24/P03-fei/continuations/2026-09-22-gate-reformulation/REPORT.md`
(current Git blob observed at entry: `1c0596f786fccf542f1f9ea65cc728b2c21ddef5`).
For a symmetric potential `Gamma`, put

\[
V_p=4p(1-p),\qquad
L(p)=\frac{\Gamma(p)+h(V_p)}{V_p},
\]

and for a Boolean gate `G` at product input biases `p=(p_i)` define

\[
D_G(p)=\sum_i \operatorname{It}_i(G;p)L(p_i)
       -\widetilde H_G(p)-\Gamma(p_{\rm out}),
\]
\[
W_G(p)=\frac{I(G;p)}4-p_{\rm out}(1-p_{\rm out})\ge0.
\]

Adding `c z(1-z)` to `Gamma` changes the gate slack by exactly `c W_G`, so
for `W_G>0`

\[
c_G(p)=-\frac{D_G(p)}{W_G(p)}.
\]

The full target is still to prove that all gates/all arities have margin no
larger than the binding AND margin (or to find a counterexample).

### Named other-account result consumed

I used account04/B18's fresh **decomposable-margin telescope**, immutable checker
blob `8d56291e28c6c4f29ebaa58af2e78845b1e96f97` and PASS output blob
`d3aa5e7ff4b38d290b55b51006903be5d8cdb448`, recorded at commit
`747270cb4562dadf27889ea4484cee8b9b86dd84`.
For a disjoint composition

\[
G=H(G_1,\ldots,G_m),\qquad q_j=\Pr[G_j=1],\qquad
\alpha_j=\frac{\operatorname{It}_j(H;q)}{V_{q_j}},
\]

that result gives the exact algebraic identities

\[
D_G=D_H+\sum_j\alpha_jD_{G_j},\qquad
W_G=W_H+\sum_j\alpha_jW_{G_j}.
\tag{1}
\]

Consequently, away from zero-denominator trivial components,

\[
c_G=
\frac{W_Hc_H+\sum_j\alpha_jW_{G_j}c_{G_j}}
     {W_H+\sum_j\alpha_jW_{G_j}}.
\tag{2}
\]

Thus a decomposable gate cannot have margin larger than its worst component.
This is applied below rather than merely cited.

## 2. Immediate application: tribes is not a high-arity obstruction

Every tribes gate (arbitrary block widths, arbitrary product input biases) is
a disjoint read-once composition of AND/OR gates. By (2), its gate margin is a
nonnegative weighted average of the margins of its binary AND/OR nodes.
Input/output complementation preserves `c_G` because `Gamma`, `h(V_p)` and
`V_p` are symmetric. Hence

\[
\boxed{\sup c_{\rm TRIBES}\le \sup c_{\rm AND_2}.}
\tag{3}
\]

The same statement holds for every disjoint AND/OR read-once gate, including
all one-point-defect gates. Therefore tribes cannot furnish the requested
counterexample to AND extremality.

## 3. New theorem: arbitrary-size addressing collapses exactly to one MUX

Let `Addr_k` have address bits `A_1,...,A_k`, with
`Pr[A_i=1]=p_i`, and data bits `Y_j`, `j in {0,1}^k`. Assume all data bits
have the same bias `Pr[Y_j=1]=q`, with no assumption that `q=1/2`. The gate
outputs the addressed data bit:

\[
\operatorname{Addr}_k(A,Y)=Y_A.
\]

Let `V_i=V_{p_i}` and `V_q=4q(1-q)`.

### The spectral law

Write `J` for the data-coordinate label appearing in a nonconstant spectral
atom. Directly from the biased Fourier basis,

\[
\widehat{\operatorname{Addr}_k}(S\cup\{Y_j\})
 =\sqrt{V_q}\,\Pr[A=j]\,\phi_S(j).
\tag{4}
\]

Hence the nonconstant spectral mass is `V_q`. Conditional on being in that
part, `J` has exactly the product law of `A`. Conditional on `J=j`, each
address coordinate belongs to the spectral set independently, with

\[
\Pr[i\in S\mid J_i=0]=p_i,\qquad
\Pr[i\in S\mid J_i=1]=1-p_i.
\]

Equivalently, if `J'` is an independent copy of `J`, then

\[
\mathbf 1_{\{i\in S\}}=J_i\oplus J_i'.
\tag{5}
\]

It follows exactly that

\[
\boxed{
\widetilde H_{\rm Addr_k}
 =h(V_q)+2V_q\sum_{i=1}^k h(p_i),
}
\tag{6}
\]

\[
\boxed{
\sum_{j}\operatorname{It}_{Y_j}=V_q,
\qquad
\operatorname{It}_{A_i}=\frac{V_qV_i}{2},
\qquad
p_{\rm out}=q.
}
\tag{7}
\]

Substitution in the exact gate functional gives complete cancellation of the
common data-bit terms:

\[
\boxed{
D_{\rm Addr_k}
 =\frac{V_q}{2}\sum_{i=1}^k
   \bigl(\Gamma(p_i)+h(V_i)-4h(p_i)\bigr),
}
\tag{8}
\]

\[
\boxed{
W_{\rm Addr_k}=\frac{V_q}{8}\sum_{i=1}^k V_i.
}
\tag{9}
\]

Define the one-address-bit MUX margin

\[
c_{\rm MUX}(p)
 =\frac{4\,[4h(p)-\Gamma(p)-h(V_p)]}{V_p}.
\tag{10}
\]

Then (8)–(9) yield

\[
\boxed{
 c_{\rm Addr_k}(p_1,\ldots,p_k;q)
 =\frac{\sum_i V_i c_{\rm MUX}(p_i)}{\sum_i V_i}.
}
\tag{11}
\]

This identity is independent of the common data bias `q` (for `0<q<1`; the
boundary follows by continuity). Therefore

\[
\boxed{
\sup_{k\ge1,\,p_i,\,q}
 c_{\rm Addr_k}
 =\sup_{0<p<1}c_{\rm MUX}(p).
}
\tag{12}
\]

So high-dimensional addressing **cannot amplify the gate margin at all**.
The entire common-data-bias addressing family, including arbitrary biased
address bits and biased limits, reduces to one genuine three-input MUX gate.
Thus the planned arity-3 interval check, once it certifies that MUX is below
AND for the immutable candidate potential, automatically certifies every
such addressing gate in every dimension.

This is not a read-once consequence: address bits are reused across all data
leaves. Equation (11) is a separate exact spectral identity.

## 4. Sparse defects: exact reduction of all one- and two-point gates

Use NPN symmetry and let the minority/defect set of a gate have size at most
two.

* One defect point is NPN-equivalent to an `AND_n` one-point defect and is
  already decomposable.
* For two defect points, input negations send one point to `0^n`, and a
  permutation sends the other to
  `(1^d,0^{n-d})`, where `d` is their Hamming distance.
  If `d<n`, the defect event factors on disjoint coordinates as

\[
\{\text{last }n-d\text{ bits are }0\}
\quad\wedge\quad
\{\text{first }d\text{ bits are all equal}\}.
\tag{13}
\]

Thus by the B18 telescope every two-defect gate with `d<n` has margin bounded
by the maximum of an AND component and the **antipodal equality gate**

\[
\operatorname{EQ}_d=1_{\{0^d,1^d\}}
\]

(up to output convention/NPN symmetry). For `d=1` the equality condition is
trivial, and for `d=2` it is the binary XNOR gate. Hence the first genuinely
new sparse core is `EQ_3`.

Therefore

\[
\boxed{
\text{all one/two-defect counterexample searches reduce to the biased }
\operatorname{EQ}_d\text{ family.}
}
\tag{14}
\]

### Uniform biases: even the antipodal core is strictly safer than AND

At uniform input bias, use the invertible linear change of variables

\[
y_j=x_1\oplus x_{j+1},\qquad j=1,\ldots,d-1.
\]

Then `EQ_d` is exactly a one-point-defect `AND_{d-1}` in the `y` variables,
with one irrelevant linear coordinate. Thus it has the same output measure
and exactly the same spectral entropy as `AND_{d-1}`. A Fourier atom of
`y`-degree `r` maps to `x`-degree `r` when `r` is even and `r+1` when `r` is
odd. For a one-point defect all nonempty Fourier masses are equal, so

\[
I(\operatorname{EQ}_d)-I(\operatorname{AND}_{d-1})=2^{2-d}>0.
\tag{15}
\]

For the adjusted potential `Gamma_c(z)=Gamma(z)+c z(1-z)`, the uniform gate
slack difference is therefore

\[
[D+cW]_{\operatorname{EQ}_d}-[D+cW]_{\operatorname{AND}_{d-1}}
 =\bigl(\Gamma(1/2)+c/4\bigr)2^{2-d}>0.
\tag{16}
\]

So any margin that certifies the uniform AND gate automatically certifies the
uniform antipodal two-defect gate with strict extra slack. A sparse two-point
counterexample, if it exists, must be genuinely biased.

## 5. Direct verification

`check_gate_addressing_collapse.py` independently constructs biased Fourier
coefficients from the truth table. With a synthetic symmetric potential
(the identities are potential-independent), it checks 25 direct addressing
instances through `k=3` against (6), (8), (9), and checks the uniform
`EQ_d`/`AND_{d-1}` entropy/output identities for `d=3,...,8`.

Observed output:

```text
PASS
addressing_direct_cases=25
max_abs_addressing_H_error=1.776e-15
max_abs_addressing_D_error=1.332e-15
max_abs_addressing_W_error=3.331e-16
uniform_EQ_cases=6
max_abs_EQ_AND_H_error=0.000e+00
max_abs_EQ_AND_pout_error=0.000e+00
min_EQ_minus_AND_influence=0.015625
```

Checker SHA-256:
`3cdbd8cc0139d8955dddbf233eb68ef3f4c448710d2c3087a1daca0d732c34f8`.
Output SHA-256:
`39a860ed1dedaad33b7c8caf283bf8ac11ce6ece00a643918aa1fcd68f169d2f`.

## 6. Exact movement of the FEI proof gap

**Old missing implication:** prove `c_G <= c_AND` for every Boolean gate and
every product bias, or produce a gate/bias violating it.

**Applied essential step:** the other-account composition telescope plus the
new identities above remove three large adversarial classes without any
finite-arity extrapolation:

1. all tribes / disjoint AND-OR read-once gates reduce exactly to AND;
2. all common-data-bias addressing gates in arbitrary dimension reduce
   exactly to a single 3-input MUX scalar margin;
3. every one/two-point sparse defect reduces to AND plus the antipodal
   `EQ_d` family, and uniform `EQ_d` is strictly safer than AND.

**New first missing implication:** establish the immutable-candidate bound on
the one-bit MUX (an arity-3 interval problem), and then attack genuinely
biased `EQ_d` and other composition-prime gates. The current rough
`cert_vi_h96k40_f4` potential is named by the canonical gate report, but its
NPZ was not present at the canonical repository path during this run, so no
new numerical margin for that exact candidate is asserted here.

This report is **not** a full FEI proof and does not claim that finite tests or
these family reductions settle the all-gate inequality.
