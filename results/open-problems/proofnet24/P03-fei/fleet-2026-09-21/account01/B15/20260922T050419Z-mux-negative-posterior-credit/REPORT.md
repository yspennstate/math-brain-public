# B15 — exact negative posterior-entropy credit for unequal-data MUX

**Classification:** `ESSENTIAL_STEP_APPLIED / CREDIT_FREE_ROUTE_REFUTED / FULL_FEI_OPEN`.

**Full unrestricted uniform-cube Fourier entropy-influence:** **OPEN / NOT PROVED**.

**Execution:** `WITHOUT_VERIFIED_BRAIN`. Repository controls and mathematical artifacts were read directly. No authenticated cognitive-brain receiver/context entered the derivation.

## 0. Live candidate and exact peer theorem consumed

The active FEI target is the all-gate inequality
\[
D_\Gamma(G;p)=
\sum_i \frac{\operatorname{It}_i(G;p)}{V_{p_i}}
  \bigl(\Gamma(p_i)+h_2(V_{p_i})\bigr)
-\Gamma(p_{\rm out})-\widetilde H_G(p)\ge0,
\qquad V_x=4x(1-x).
\tag{0.1}
\]

The fixed candidate used here is the current `LIMIT-PRIME-GATE-LIFT-v1` / `Gamma^dagger` candidate
\[
C^\dagger=\Gamma^\dagger(1/2)=6.521851214,\qquad
\Gamma^\dagger=\Gamma_0+0.268204856\,p(1-p).
\tag{0.2}
\]
A proof of (0.1) for every composition-prime gate/product bias would, by the exact gate-composition cocycle and gate reformulation, prove full FEI with constant `C^dagger`.

The exact completed other-account theorem consumed and applied is account02/B12

`proofnet24/P03-fei/fleet-2026-09-21/account02/B12/20260922T045519Z-complementary-mux-fourstep/REPORT.md`

report blob `5246a98a875da29c7e902237e269a0f7acd899e9`.

It proves, for the same fixed candidate, the entire complementary-data balanced-address MUX line
\[
D_{\Gamma^\dagger}\!\left(M;\frac12,q,1-q\right)\ge0
\quad(0<q<1),
\tag{0.3}
\]
by an exact four-generation AND bootstrap plus a rational interval certificate. Its stated remaining MUX problem is to release the restrictions `t=1/2` and `q_1=1-q_0`.

The contemporaneous account03/B12 arithmetic diagnostic
`20260922T041041Z-unequal-mux-nonreuse`
is also used only for source-exact six-mass conventions and for the warning that naively reusing the equal-data reserve produces a negative residual. Its checker blob is `06b6cbc59f40ba570f3a3d321f26e4fee8ac9c86`.

This run does not reopen the already-refuted global AND-extremality claim. It attacks the fixed lifted candidate and, specifically, the negative Shannon term lost by the naive unequal-MUX estimate.

## 1. Exact six-mass MUX spectrum

Let
\[
M(a,x_0,x_1)=(1-a)x_0+a x_1,
\]
with independent input biases
\[
\Pr(a=1)=t,\qquad \Pr(x_0=1)=q_0,\qquad \Pr(x_1=1)=q_1.
\]
Put
\[
r=(1-t)q_0+tq_1,\qquad
m_j=1-2q_j.
\]
The squared biased Fourier masses are
\[
\begin{aligned}
w_\varnothing&=(1-2r)^2,\\
w_a&=V_t(q_1-q_0)^2,\\
w_0&=(1-t)^2V_{q_0},\\
w_1&=t^2V_{q_1},\\
w_{a0}&=t(1-t)V_{q_0},\\
w_{a1}&=t(1-t)V_{q_1}.
\end{aligned}
\tag{1.1}
\]
Consequently
\[
\frac{\operatorname{It}_a}{V_t}
=\delta:=q_0+q_1-2q_0q_1,\qquad
\frac{\operatorname{It}_0}{V_{q_0}}=1-t,\qquad
\frac{\operatorname{It}_1}{V_{q_1}}=t.
\tag{1.2}
\]

The all-gate slack is therefore
\[
D_\Gamma
=
\delta\bigl(\Gamma(t)+h_2(V_t)\bigr)
+(1-t)\Gamma(q_0)+t\Gamma(q_1)-\Gamma(r)-L,
\tag{1.3}
\]
where
\[
L:=\widetilde H_M-(1-t)h_2(V_{q_0})-t h_2(V_{q_1})
\tag{1.4}
\]
is the spectral-entropy increment created by the selector.

## 2. The exact negative entropy term

Define
\[
s:=(1-t)m_0^2+t m_1^2
=(1-2r)^2+t(1-t)(m_0-m_1)^2.
\tag{2.1}
\]
Think of the branch bit as a latent label. The two restricted child spectra have symbols
\[
\{\varnothing,d_0\},\qquad \{\varnothing,d_1\}.
\]
The nonempty symbols `d_0,d_1` identify the branch exactly. Only the empty symbol leaves branch uncertainty. Conditional on that empty symbol, the posterior probability of branch one is
\[
\theta=\frac{t m_1^2}{s}.
\tag{2.2}
\]
Hence the Jensen-Shannon term is exactly
\[
\boxed{
JS_t(\mu_0,\mu_1)
=
h_2(t)-s\,h_2(\theta).
}
\tag{2.3}
\]

This is the requested negative entropy credit. It is not an error term and it has the **negative** sign:
\[
\boxed{-\,s\,h_2\!\left(\frac{t m_1^2}{s}\right).}
\tag{2.4}
\]

The conditional entropy of the selector Fourier bit given the two data Fourier bits is also exact. On the empty/data-free group the selector-present probability is
\[
A=\frac{t(1-t)(m_0-m_1)^2}{s},
\tag{2.5}
\]
while on the `d_0` and `d_1` groups the selector-present probabilities are respectively `t` and `1-t`. Since
\[
(1-t)V_{q_0}+tV_{q_1}=1-s,
\]
we obtain
\[
\boxed{
H(S_a\mid S_{-a})
=
s\,h_2(A)+(1-s)h_2(t).
}
\tag{2.6}
\]

Adding (2.3) and (2.6) gives the exact selector entropy increment
\[
\boxed{
L
=
(2-s)h_2(t)
+s\left[
h_2\!\left(\frac{t(1-t)(m_0-m_1)^2}{s}\right)
-
h_2\!\left(\frac{t m_1^2}{s}\right)
\right].
}
\tag{2.7}
\]

No sign-free relaxation, uncharged branch label, or coverage assumption appears in (2.7).

## 3. Why dropping the negative term is genuinely wrong

Take complementary data
\[
q_1=1-q_0=1-q,\qquad m_1=-m_0.
\]
Then `s=(1-2q)^2=1-V_q`, `theta=t`, and (2.3) becomes
\[
\boxed{
JS_t=V_q\,h_2(t).
}
\tag{3.1}
\]
If one uses only the generic bound `JS_t<=h_2(t)`, the exact amount discarded is
\[
\boxed{
(1-V_q)h_2(t).
}
\tag{3.2}
\]
For every fixed interior `t`,
\[
(1-V_q)h_2(t)\longrightarrow h_2(t)
\qquad(q\downarrow0).
\tag{3.3}
\]

But at `q=0` the MUX is just the signed selector literal, whose exact gate slack is zero; by continuity the true MUX slack tends to zero as `q\downarrow0`. Therefore the **credit-free** local estimate has asymptotic slack
\[
\boxed{
D_{\rm no\ credit}(t,q,1-q)\longrightarrow -h_2(t)<0.
}
\tag{3.4}
\]
This is a genuine Boolean counterexample family to the stronger statement obtained by deleting the negative posterior-entropy term. It is not evidence against FEI or against `Gamma^dagger`; it proves that the negative term is structurally indispensable.

At the balanced address `t=1/2`, (3.2) is simply
\[
1-V_q=(1-2q)^2.
\]
Thus the discarded credit tends to a full **one bit**. This is exactly the scale on which a blind arity step loses the MUX boundary.

## 4. Complementary data: arbitrary address bias

Still take `q_1=1-q`. From (2.7),
\[
L
=
2V_q h_2(t)+(1-V_q)h_2(V_t).
\tag{4.1}
\]
Since
\[
r=q+t(1-2q),\qquad
\delta=1-\frac{V_q}{2},
\]
the exact gate slack for every symmetric potential is
\[
\boxed{
\begin{aligned}
D_\Gamma(t,q,1-q)
={}&
\left(1-\frac{V_q}{2}\right)\Gamma(t)
+\Gamma(q)-\Gamma(r)\\
&+\frac{V_q}{2}h_2(V_t)-2V_q h_2(t).
\end{aligned}
}
\tag{4.2}
\]

At `t=1/2`, `r=1/2` and (4.2) collapses to
\[
\boxed{
D_\Gamma\!\left(\frac12,q,1-q\right)
=
\Gamma(q)-V_q\left(\frac{\Gamma(1/2)}2+2\right),
}
\tag{4.3}
\]
exactly the scalar quantity proved nonnegative by account02/B12. Thus the completed peer theorem is recovered as the balanced-address section of the new signed formula, while (4.2) releases the address bias algebraically.

Equation (4.2) is not yet a proof for all `t`: the remaining term `Gamma(r)` must still be controlled. It does show that no extra Shannon loss is hidden in the complementary-data extension.

## 5. Balanced address, arbitrary unequal data: exact two-dimensional residual

Now set `t=1/2` but leave `q_0,q_1` arbitrary. Put
\[
u=\frac{m_0+m_1}{2},\qquad
v=\frac{m_0-m_1}{2}.
\tag{5.1}
\]
Then
\[
|u|+|v|\le1,\qquad
q_0=\frac{1-u-v}{2},\quad
q_1=\frac{1-u+v}{2},\quad
r=\frac{1-u}{2},
\tag{5.2}
\]
and
\[
s=u^2+v^2,\qquad
\delta=\frac{1-u^2+v^2}{2}.
\tag{5.3}
\]

Define
\[
\phi(x)=x\log_2(1/x),\qquad \phi(0)=0,
\]
and
\[
\boxed{
E(u,v)
=
\phi(u^2)+\phi(v^2)
-\frac12\phi((u+v)^2)
-\frac12\phi((u-v)^2).
}
\tag{5.4}
\]
Equation (2.7) gives
\[
\boxed{
L=2(1-u^2-v^2)+E(u,v).
}
\tag{5.5}
\]

For `s>0`,
\[
E
=
s\left[
1+h_2\!\left(\frac{v^2}{s}\right)
-h_2\!\left(\frac{(u-v)^2}{2s}\right)
\right]\ge0,
\tag{5.6}
\]
because the last binary entropy is at most one. The formula extends continuously at `s=0`.

Write
\[
C=\Gamma(1/2),\qquad
S=\frac C2-2,\qquad
B=\frac C2+2.
\tag{5.7}
\]
The balanced-address MUX slack is exactly
\[
\boxed{
D_\Gamma
=
R_C(u,v)-J_\Gamma(u,v),
}
\tag{5.8}
\]
where
\[
R_C(u,v):=S(1-u^2)+Bv^2-E(u,v)
\tag{5.9}
\]
and
\[
\boxed{
J_\Gamma(u,v)
:=
\Gamma\!\left(\frac{1-u}{2}\right)
-\frac12\Gamma\!\left(\frac{1-u-v}{2}\right)
-\frac12\Gamma\!\left(\frac{1-u+v}{2}\right).
}
\tag{5.10}
\]
Thus the only potential-dependent obstruction on the whole balanced-address MUX plane is an explicit midpoint-concavity gap of `Gamma`.

## 6. The entropy side is always paid when C>6

The negative credit in Section 2 permits a quantitative bound that fails if that credit is discarded.

Let
\[
z=\frac{v^2}{u^2+v^2},\qquad
x=\frac{2|uv|}{u^2+v^2}.
\]
Then
\[
h_2(z)\le2\sqrt{z(1-z)}=x
\tag{6.1}
\]
and the elementary lower bound `h_2(p)>=4p(1-p)` gives
\[
1-h_2\!\left(\frac{1-x}{2}\right)\le x^2.
\tag{6.2}
\]
Using (5.6) and symmetry of binary entropy,
\[
\boxed{
E(u,v)
\le
2|uv|+\frac{4u^2v^2}{u^2+v^2}
\le
2|uv|+4v^2.
}
\tag{6.3}
\]

Since `B=S+4`,
\[
R_C(u,v)
\ge S(1-u^2+v^2)-2|uv|.
\tag{6.4}
\]
For `|u|+|v|<=1`,
\[
1-u^2+v^2\ge2|uv|,
\tag{6.5}
\]
because
\[
1-u^2+v^2-2|uv|
=
1-(|u|+|v|)^2+2v^2\ge0.
\]
Hence, whenever `C>=6`,
\[
\boxed{
R_C(u,v)
\ge
(C-6)\,\delta
\ge0.
}
\tag{6.6}
\]
For the live center,
\[
C^\dagger-6=0.521851214.
\tag{6.7}
\]

Therefore **there is no unpaid Shannon/selector deficit anywhere on the balanced-address MUX plane once the negative posterior entropy is retained**. Any actual counterexample to the fixed candidate on this plane must satisfy
\[
\boxed{
J_{\Gamma^\dagger}(u,v)>R_{C^\dagger}(u,v)\ge0.
}
\tag{6.8}
\]
In particular it must come from the midpoint concavity of the potential, not from the selector entropy.

This is the quantitative use of the requested negative entropy term.

## 7. Closed faces and the new exact missing implication

The residual (5.8) is already closed on the main degeneracies:

* `v=0` (equal data): `J=E=0`, and the common-data MUX/addressing theorem applies.
* `u=0` (complementary data): `E=0`; (5.8) is exactly the scalar line closed by account02/B12.
* `|u|+|v|=1`: one data input is constant, so the Boolean gate reduces to an AND/OR/NPN-equivalent two-input gate, already certified for the candidate.
* literal endpoints are zero-slack base cases.

Thus a balanced-address MUX counterexample, if one exists, must be genuinely interior:
\[
uv\ne0,\qquad |u|+|v|<1,
\tag{7.1}
\]
and must violate exactly
\[
\boxed{
J_{\Gamma^\dagger}(u,v)
\le
R_{C^\dagger}(u,v).
}
\tag{7.2}
\]

This is not presented as an equivalence for full FEI. It is the exact remaining two-variable statement for the balanced-address unequal-data MUX slice. Releasing the address bias then uses (1.3)/(2.7), or the complementary special reduction (4.2).

## 8. Old/new missing implications and classification

**Old first MUX implication:** after the common-data/addressing family, control unequal-data MUX for the fixed `Gamma^dagger`; account02/B12 closed only `t=1/2, q_1=1-q_0`.

**New proved inference:** the selector entropy increment has the exact signed decomposition (2.7). The negative term `-s h_2(theta)` is order one on the complementary rare-data boundary and is indispensable: deleting it creates a genuine Boolean family with artificial slack tending `-h_2(t)`. With the term retained, every balanced-address MUX reduces exactly to the potential midpoint gap (5.8), and the entire nonpotential budget is nonnegative for `C>=6` by (6.6).

**New first missing implication on this slice:** prove (7.2) for the actual source-defined `Gamma^dagger`, or produce a genuine interior `(u,v)` violating it. No finite sampling or auxiliary theorem is claimed to settle that statement.

**Classification:** `ESSENTIAL_STEP_APPLIED` for the requested negative-entropy accounting and its quantitative application; `CREDIT_FREE_ROUTE_REFUTED` for any proof step replacing (2.3) by `JS_t<=h_2(t)` without carrying the posterior credit. This is **not** `FULL_PROOF_CANDIDATE`.

## 9. Checker and scope

The adjacent standard-library checker reconstructs the six masses, tests Parseval, compares the direct spectral entropy with (2.7), compares the balanced-address formula with (5.4)-(5.5), and stress-tests the analytic inequality (6.3). It is a falsification checker for the algebra, not the proof of the elementary entropy bounds.

Checker SHA-256:
`fd24d3fcf2e8a659e585c033ef1f83fdc3509dcb010bfd4c77a5d92ac0312a6a`.

Output SHA-256:
`467439a4aaddfb8ffb99d6e68b9255104bf512430fc83ee853851586de892f05`.

Only FEI mathematics, source-bound repository identifiers, and sanitized provenance are stored. No credentials, scheduler identifiers, machine paths, email/Drive data, unrelated private information, paid/remote compute, public posting, permission changes, or notification changes are included.
