# B14 — the repaired erasure selector holds for every disjoint tribes family

**Run:** 2026-09-21T12:14:40Z, fleet04/B14  
**Live role:** FEI erasure and selector proof  
**Execution context:** `WITHOUT_VERIFIED_BRAIN`  
**Directive:** `FEI-PROOF-NUMERICS-SPRINT-20260921T120803Z`, B14/fleet04: prove or refute a candidate existential selector on a growing family.  
**Fresh P03 source used before this derivation:** `master` observed through `95856e10bc5c6a547a219b1fa05d936a3164f483`.  
**Status:** PARTIAL / structured-family theorem. **Full uniform-cube FEI remains OPEN / NOT PROVED.**  
**Publication priority:** UNVERIFIED; no novelty claim is made.

## 1. Exact target

For the spectral sample `X`, fix a coordinate `i` and write

\[
p_i=\Pr[i\in X]=\operatorname{Inf}_i(f),\qquad
B_i=H(X_i\mid X_{-i}).
\]

The current exact restriction decomposition is

\[
\Delta_i H=B_i+JS_i.
\]

The preceding fleet04/B14 run proved the recombination bound

\[
JS_i\le j(p_i),\qquad
j(p):=1-h_2\!\left(\frac12+\sqrt{p(1-p)}\right)
\]

in the low-influence regime (indeed via the stronger fibre law
`JS_i <= j(M_i) - (2/(3 ln 2)) V_i`). Therefore the following is a
sufficient local payment at the Hod-scale calibration

\[
C_H=6.4547837:
\qquad
\boxed{B_i+j(p_i)\le C_H p_i.}
\tag{1}
\]

The old tangent-surcharge target `B_i + (2/ln 2)p_i <= C_H p_i` is false
already for width-two tribes with eight tribes. This run asks whether
the repaired target (1) survives not just that witness but the entire
disjoint-tribes family.

## 2. Family and exact Fourier fibres

Let `T_{w,s}` be disjoint tribes: `s` disjoint blocks of `w>=2` bits,
with `f=+1` iff no block is all `1`, and `f=-1` otherwise. Put

\[
a=2^w-1,\qquad b=a+1=2^w,\qquad q=\frac ab.
\]

Every coordinate is symmetric, with exact influence

\[
\boxed{
p=p_{w,s}=\frac{2}{b}q^{s-1}
=\frac{2a^{s-1}}{b^s}.
}
\tag{2}
\]

For completeness, the squared Fourier mass at the empty set is
`(2 q^s - 1)^2=(1-ap)^2`. A nonempty set meeting exactly `m` tribes
has common squared coefficient

\[
c_m=4q^{2(s-m)}b^{-2m}
=\frac{4a^{2(s-m)}}{b^{2s}}.
\tag{3}
\]

Fix a coordinate `i`. Pair the spectral masses `x_T=p_T` and
`y_T=p_{T union {i}}`. There are exactly three fibre classes.

1. **The focal tribe is already active.** If `T` contains another
   variable of the focal tribe, then `x_T=y_T`. The total pair mass is
   \[
   W_A=\frac{2p(a-1)}{b}.
   \tag{4}
   \]
   These fibres contribute `W_A` to `B_i`.

2. **The focal tribe is empty, but another tribe is active.** Here
   `x_T/y_T=a^2`, so the small conditional parameter is
   \[
   t=\frac1{a^2+1}.
   \]
   The total pair mass is
   \[
   W_B=(a^2+1)\left(\frac{2p}{b}-p^2\right).
   \tag{5}
   \]

3. **The residual label is empty.** The two masses are
   \[
   x_0=(1-ap)^2,\qquad y_0=p^2,
   \]
   with `W_C=x_0+p^2` and `t_0=p^2/W_C`.

Consequently

\[
\boxed{
B_i=
\frac{2p(a-1)}b+
(a^2+1)\left(\frac{2p}{b}-p^2\right)
h_2\!\left(\frac1{a^2+1}\right)
+
F((1-ap)^2,p^2),
}
\tag{6}
\]

where

\[
F(x,y)=(x+y)h_2\!\left(\frac{y}{x+y}\right).
\]

This is an exact formula; no truth-table expansion is needed.

## 3. A one-variable envelope

Define

\[
c_a=(a^2+1)h_2\!\left(\frac1{a^2+1}\right),
\qquad c_*=\frac2{\ln2}.
\]

Two elementary inequalities give a convenient upper envelope.

First,

\[
F(x,y)\le h_2(y)
\tag{7}
\]

whenever `x,y>=0`, `x+y<=1`. Probabilistically, `F(x,y)` is the
conditional entropy of the indicator of the `y`-atom after one is told
whether the outcome lies in the `x union y` part; conditioning cannot
increase the unconditional entropy `h_2(y)`.

Second, the inherited tangent bound gives `j(p)<=c_* p` for
`0<=p<=1/2`.

Dividing (6) by `p`, adding `j(p)/p`, and applying (7) yields

\[
\boxed{
R_{w,s}:=\frac{B_i+j(p)}p
\le
U_a(p):=
\frac{2(a-1)}{a+1}
+\frac{2c_a}{a+1}
-c_ap
+\frac{h_2(p^2)}p
+c_*.
}
\tag{8}
\]

Thus the whole infinite family reduces to bounding one explicit scalar
function.

## 4. Theorem: all disjoint tribes satisfy the repaired Hod selector

### Theorem 4.1

For every `w>=2` and every `s>=1`,

\[
\boxed{
B_i+j(p_i)<6.4547837\,p_i
}
\tag{9}
\]

for every coordinate `i` of `T_{w,s}`.

More quantitatively, the certificate below proves the uniform bound

\[
\boxed{
\frac{B_i+j(p_i)}{p_i}
\le 6.428955323826338
<6.4547837.
}
\tag{10}
\]

Hence this complete structured family cannot refute the repaired
existential erasure selector. Since all coordinates are symmetric,
(9) is stronger here than the existential statement needed by the
restriction induction.

### Proof

#### Width `w=2`

Here `a=3` and

\[
p_s=\frac{3^{s-1}}{2^{2s-1}}.
\]

For `s=1,...,10`, direct interval evaluation of the exact formula (6)
gives an upper bound below `C_H`. The tightest of those displayed
integer cases is `s=9`:

\[
p_9=\frac{6561}{131072},
\qquad
R_{2,9}\in
[6.426796285219886,\ 6.4267962852199165].
\tag{11}
\]

For the tail `s>=11`,

\[
p\le p_{11}=\frac{59049}{2097152}.
\]

The derivative of the nonconstant part of `U_3` obeys, with `z=p^2`,

\[
\frac{d}{dp}\frac{h_2(p^2)}p
=
-\log_2z+\frac{1+z}{z}\log_2(1-z)
\]

and `ln(1-z)>=-z/(1-z)`, hence

\[
U_3'(p)\ge
-\log_2 z
-\frac{1+z}{(1-z)\ln2}
-c_3.
\tag{12}
\]

The right side decreases with `z`. Directed interval evaluation at
`p_11` gives

\[
U_3'(p)\ge
[4.165809647913998,\ 4.165809647914014]>0
\]

throughout `0<p<=p_11`, so `U_3` is increasing there. At the endpoint,

\[
U_3(p_{11})\in
[6.428955323826333,\ 6.428955323826338]
<C_H.
\tag{13}
\]

This covers every `s>=11`.

#### Width `w=3`

Now `a=7` and `0<p<=1/4`. The same scalar envelope `U_7(p)` was
enclosed on the *whole continuous interval*, not merely the discrete
tribes values. On `10^-4<=p<=1/4`, 5000 rational cells with outward
interval evaluation give

\[
U_7(p)\le6.305163516071847.
\tag{14}
\]

For `0<p<=10^-4`, use `h_2(p^2)<=p^2 log_2(e/p^2)`; the resulting tail
upper bound is

\[
U_7(p)\le6.156198675530686.
\tag{15}
\]

Thus every width-three tribes function satisfies (9).

#### Width `w=4`

Here `a=15` and `0<p<=1/8`. The same continuous interval certificate
gives

\[
U_{15}(p)\le5.864133031732683
\qquad (0<p\le1/8),
\tag{16}
\]

with the `p<=10^-4` tail separately bounded by
`5.795651579007814`.

#### Width `w>=5`

Let `b=a+1=2^w>=32`. Since

\[
h_2(t)\le t\log_2(e/t),
\]

we have

\[
\frac{2c_a}{a+1}
\le
\frac2b\log_2(eb^2).
\]

The right side decreases for `b>=32`. Also `p<=2/b<=1/16`, and
`p log_2(e/p^2)` increases on this interval. Dropping the favorable
term `-c_a p` in (8) therefore gives the uniform bound

\[
R_{w,s}
<
2+\frac2{32}\log_2(e\,32^2)
+\frac1{16}\log_2(e\,16^2)
+\frac2{\ln2}.
\]

Directed interval evaluation gives

\[
R_{w,s}\le
6.190726961889049
<C_H.
\tag{17}
\]

Equations (11)--(17) prove (10), hence (9). QED.

## 5. Induction ratio and H/I were kept separate

The sprint explicitly requires that a local restriction ratio not be
confused with the global FEI ratio. For width-two tribes, the exact
formula and the closed-form Fourier spectrum give:

| `s` | `p` | `Delta_i H/p` | `H/I` | repaired `R=(B_i+j(p))/p` |
|---:|---:|---:|---:|---:|
| 5 | 0.158203125 | 5.782549183603 | 3.685517731653 | 6.099777784802 |
| 6 | 0.11865234375 | 5.940609096619 | 3.972285325434 | 6.300754969852 |
| 7 | 0.0889892578125 | 5.996806000052 | 4.179025877218 | 6.391542323130 |
| 8 | 0.066741943359375 | 6.003746056559 | 4.329597870801 | 6.424389329915 |
| 9 | 0.05005645751953125 | 5.987004834046 | 4.440414238063 | 6.426796285220 |
| 10 | 0.0375423431396484375 | 5.959948813006 | 4.522797166104 | 6.413882488352 |

The repaired selector charge is thus a distinct object from both
`Delta_i H/p_i` and `H/I`.

## 6. What this does and does not accomplish

This result is useful because width-two tribes with `s=8` was the
explicit obstruction to the older tangent-erasure target. The
obstruction disappears not only at `s=8`, but uniformly across every
disjoint tribes width and size after the exact recombination profile is
retained.

It is **not** a proof of full FEI. Disjoint tribes are a structured
read-once family. The known counterexamples to universal
every-prescribed-coordinate payment remain untouched. The remaining
universal obligation is still to show that an arbitrary low-influence
Boolean state has *some* coordinate with the repaired charge

\[
B_i+j(M_i)-\frac{2}{3\ln2}V_i\le Cp_i
\]

(or the weaker `B_i+j(p_i)<=C p_i`) for a universal `C`.

The next useful B14 move is therefore to attack a genuinely
non-read-once perturbation family—such as the current exact top-flip
tribes witnesses—or to exploit the all-shift Boolean convolution
identities to force a favorable fibre profile at one coordinate. The
present theorem rules out “ordinary disjoint tribes at another width
or scale” as a source of failure of the repaired selector.

## 7. Reproducibility

`tribes_selector_certificate.py` uses exact rational influences and
`mpmath.iv` outward interval arithmetic for every strict numerical
comparison in (11)--(17). Its output status is `PASS`.

- certificate SHA-256:
  `a2de491d1de786004d1e79a3a4a42febbe23035382bc203b2d5a13b876347cf0`
- output SHA-256:
  `2647e5fe48c28601361dd1bccbd312d6f3766edb832efe6409fc463fbfd97a26`

A separate direct Walsh-transform spot check on `(w,s)=(2,3),(3,2),
(3,3),(4,2)` agreed with the closed-form `H,I,B_i` formulas to at
worst `2.4e-14` in ordinary double arithmetic. This spot check is only
corroborative; the proof above uses the exact formulas and the directed
interval certificate.

No claim of literature novelty is made.
