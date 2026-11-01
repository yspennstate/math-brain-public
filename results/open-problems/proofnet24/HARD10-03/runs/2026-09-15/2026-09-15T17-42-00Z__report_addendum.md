# HARD10-03 addendum — tilted long-cycle theorem from the rooted resolvent

**STATUS: PROVED UNDER AN EXPLICIT CYCLE-HITTING TILT; DOES NOT YET SOLVE THE ORIGINAL MEASURE.**

This addendum extends

`proofnet24/HARD10-03/runs/2026-09-15/2026-09-15T17-19-30Z__report.md`

commit `3f7d6ee8d3f11d246d5ae04d74964ecf77721664`.

The main report proves the exact rooted identity

\[
\mathbb E[z^{L-1}W_z]
=D(z)R(z),
\]

where \(L\) is the root cycle length,

\[
W_z=\prod_{C\ne C_o}(1-z^{|C|}),
\qquad
D(z)=\det(I-zK_\beta),
\]

and on a transitive graph

\[
R(z)
=
\sum_{m\ge1}z^{m-1}p_{m\beta}(o,o).
\]

The following consequence was derived after the main checkpoint was already durably written.

---

## A1. Other-cycles-hitting tilted permutation law

For a finite transitive graph define a probability law \(\mathbb Q_z^{o}\) on interchange permutations by

\[
\frac{d\mathbb Q_z^{o}}{d\mathbb P}(\pi)
=
\frac{W_z(\pi)}{\mathbb E W_z}.
\tag{A1.1}
\]

Probabilistically, this is the permutation law tilted by the probability that Bernoulli marks of density \(1-z\) hit **every cycle other than the root cycle**; equivalently the root is forced marked and the remaining marks must hit every other cycle.

The main report proves

\[
\mathbb EW_z
=D(z)(1+zR(z)).
\]

Therefore:

### Theorem A1 — PROVED

\[
\boxed{
\mathbb E_{\mathbb Q_z^{o}}[z^{L-1}]
=
\frac{R(z)}{1+zR(z)}.
}
\tag{A1.2}
\]

For every integer \(M\ge1\),

\[
\boxed{
\mathbb Q_z^{o}(L\le M)
\le
z^{1-M}\frac{R(z)}{1+zR(z)}.
}
\tag{A1.3}
\]

Indeed, on \(L\le M\), because \(0<z<1\),

\[
z^{L-1}\ge z^{M-1}.
\]

---

## A2. All-cycles-hitting tilted law

Define instead

\[
\frac{d\mathbb Q_z}{d\mathbb P}(\pi)
=
\frac{\prod_C(1-z^{|C|})}{D(z)}.
\tag{A2.1}
\]

This is exactly the interchange permutation conditioned by the likelihood that Bernoulli marks of density \(1-z\) hit every cycle.

Since

\[
\prod_C(1-z^{|C|})
=(1-z^L)W_z,
\]

the rooted identity gives

\[
\boxed{
\mathbb E_{\mathbb Q_z}
\left[
\frac{z^{L-1}}{1-z^L}
\right]
=R(z).
}
\tag{A2.2}
\]

This is an exact `Bose-factor` transform of the root cycle under the all-cycle-hitting tilt.

If \(z=e^{-1/M}\), then on \(L\le M\),

\[
\frac{z^{L-1}}{1-z^L}
\ge z^{M-1}>e^{-1}.
\]

Hence:

### Theorem A2 — PROVED

For \(z_M=e^{-1/M}\),

\[
\boxed{
\mathbb Q_{z_M}(L\le M)
\le e R(z_M).
}
\tag{A2.3}
\]

The same bound, up to the harmless denominator \(1+zR\), follows from A1 for \(\mathbb Q_{z_M}^{o}\).

---

## A3. Quantitative torus consequence in dimension three

Let

\[
T_n^3=(\mathbb Z/n\mathbb Z)^3,
\qquad V=n^3.
\]

For continuous-time rate-one-per-neighbor simple random walk there is a universal constant \(C\) such that for \(t\ge1\), uniformly in \(n\),

\[
p_{t,n}(0,0)
\le
C\left(t^{-3/2}+V^{-1}\right).
\tag{A3.1}
\]

This follows from the standard Gaussian heat-kernel estimate up to the mixing scale and the equilibrium bound afterward.

Therefore, for \(\beta\ge1\),

\[
\begin{aligned}
R_{n,\beta}(z)
&=
\sum_{m\ge1}z^{m-1}p_{m\beta,n}(0,0)\\
&\le
C\beta^{-3/2}\sum_{m\ge1}m^{-3/2}
+
\frac{C}{V}\sum_{m\ge1}z^{m-1}\\
&\le
C\beta^{-3/2}
+
\frac{C}{V(1-z)}.
\end{aligned}
\tag{A3.2}
\]

Choose \(z=z_M=e^{-1/M}\). Since

\[
1-e^{-1/M}\ge c/M
\]

for \(M\ge1\),

\[
R_{n,\beta}(z_M)
\le
C\beta^{-3/2}+C\frac{M}{V}.
\tag{A3.3}
\]

Combining with A2 gives:

### Theorem A3 — PROVED

For every \(\beta\ge1\), every three-dimensional torus with volume \(V\), and every \(1\le M\le V\), under the all-cycle-hitting tilt with Bernoulli mark density

\[
1-e^{-1/M}\asymp M^{-1},
\]

we have

\[
\boxed{
\mathbb Q_{e^{-1/M}}(L\le M)
\le
C\beta^{-3/2}
+C\frac{M}{V}.
}
\tag{A3.4}
\]

The same conclusion holds under the forced-root/other-cycles-hitting tilt \(\mathbb Q^o\).

Consequently, if \(\beta\) is large and \(M=o(V)\), then in either tilted ensemble the root lies in a cycle longer than \(M\) with probability

\[
1-O(\beta^{-3/2})-o(1).
\]

This is a rigorous long-cycle theorem for an explicit determinant-defined tilt.

---

## A4. Why this still does not prove Tóth's conjecture

For an event \(A\),

\[
\mathbb P(A)
\ge
\mathbb EW_z\,\mathbb Q_z^o(A),
\]

because \(0\le W_z\le1\). But

\[
\mathbb EW_z
=D(z)(1+zR(z)),
\]

and at fixed \(\beta\), with \(z=e^{-1/M}\to1\) on a growing torus, \(D(z)\) is exponentially small in the volume at the positive cycle-pressure rate established in earlier checkpoints. Thus A3 does not yield a nonvanishing lower bound under the original permutation law.

The theorem nevertheless clarifies the exact missing comparison:

> determinant tilting forces the root into a diverging cycle with overwhelming probability, but the Radon–Nikodym cost of that tilt is exponentially small. A proof of the original conjecture needs a way to recover long-root-cycle information without paying that global cycle-hitting cost.

This is consistent with the pressure no-go theorem in the main report.

---

## A5. Next attack sharpened

The natural next calculation is a **two-root Palm identity**. Give two roots \(o,x\) distinct diagonal variables in the master determinant and derive exact formulas for joint root marking under the cycle-hitting tilt. Summing the same-cycle part over \(x\) could expose the first moment of the tilted root-cycle size.

If that moment can be expressed by a one-particle Green/resolvent quantity, one can ask whether a switching/correlation inequality compares the tilted root cycle to the unweighted root cycle at only subexponential cost. That is the most direct determinant-side path remaining.

**Verification:** the addendum is a direct algebraic consequence of the already archived rooted identity plus the standard torus heat-kernel estimate. It is self-reviewed only; no independent/formal verification is claimed.
