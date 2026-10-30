# B16 FEI signed transport — square-first Borel window Gram and logarithmic polarization

**Date:** 21 September 2026  
**Scope:** `fleet01 / B16`, signed transport / noise interpolation, APPROACH 10/13  
**Execution:** `WITHOUT_VERIFIED_BRAIN`  
**Status of unrestricted FEI:** **OPEN / NOT PROVED**  
**Claim level:** a new exact PSD polarization of the retained phase-switch square, a finite-window-to-full-line domination, an explicit logarithmic four-sine kernel, and a rigorous scale-separation obstruction. No novelty or publication-priority claim.

## 0. Fresh state and the precise route change

This run uses the live four-account FEI coordination order and does not revisit the settled read-once certificate.

The newest cross-account result consumed substantively is fleet04/B16
`20260921T191216Z-local-triple-curvature-flag/REPORT.md`. It proves that each authentic doubled-parent odd current is exactly
\[
  D_jF_s^{\rm odd}
  =\frac12\Delta_{g_{j,0}}\Delta_{g_{j,1}}\Delta_f\Psi_s,
\]
that the apparent local quadratic term cancels codewise by the distance-four relation-code constraint, and that the complete ordered-parent local square bank has a dimension-free small-\(s\) payment by \(J(f)\). Its remaining gap is the large Borel corridor.

I also use fleet03/B16
`20260921T185632Z-integrated-phase-switch-logarithmic-bridge/REPORT.md`, which gives the exact signed full-line *linear* phase-switch/entropy identity and correctly warns that a signed full-line endpoint does not control an arbitrary finite subwindow.

The move here is different: **polarize the authentic phase-switch square before doing any Borel-time estimate**. Once the square is expanded, the Borel kernel is a genuine Gram kernel. Therefore every finite live window is automatically dominated, in PSD order, by the full half-line. The linear synthetic-window obstruction does not survive this square-first reformulation.

This does not prove the remaining full-line Gram form is \(O(J)\). In fact a new diagonal calculation below shows a logarithmic scale-separation term is unavoidable, so a pure quartic-moment payment cannot finish the argument. That logarithm is exactly the structure that the terminal-aware entropy and moment-credit ledgers are designed to retain.

No R32 relation coefficient is positive-parted. The signed terminal weights stay inside the quadratic form. R16/moment credits, negative entropy credits, dual-code multiplicity and the terminal-band ledger are not spent below.

---

## 1. Retained phase switch and the two-copy kernel

Keep the notation of the current retained dual-code compiler:
\[
  P_0=RM(1,n),\qquad P_1=D_d^\perp,\qquad N=2^n,\qquad L=|P_1|.
\]
Put
\[
  \alpha_r=\frac1{2N}\mathbf 1_{\{r\in P_0\}}
            -\frac1L\mathbf 1_{\{r\in P_1\}}.
\tag{1.1}
\]
For a Boolean twist \(h\), split the normalized dual correlation by the sign of the actual Boolean phase \(f\):
\[
  A_r^\pm
  =\frac1N\sum_{x:f(x)=\pm1}h(x)(-1)^{r_x}.
\tag{1.2}
\]
The exact retained phase-switch factorization from the current compiler is
\[
  R_h(s):=\Psi_s(h)-\Psi_s(fh)
  =-4N\sum_r\alpha_r
       \sin(sA_r^+)\sin(sA_r^-).
\tag{1.3}
\]

For a pair \(v=(a,b)\), define
\[
  \varphi_v(s)=\sin(as)\sin(bs),
\]
and for a Borel set \(W\subset(0,\infty)\),
\[
  K_W(v,w)
  :=\int_W\frac{\varphi_v(s)\varphi_w(s)}{s^3}\,ds.
\tag{1.4}
\]
The full-line kernel is \(K_\infty:=K_{(0,\infty)}\).

Each integral in (1.4) is absolutely convergent on the full half-line: near zero the numerator is \(O(s^4)\), and at infinity it is bounded.

---

## 2. `P03-B16-SQUARE-FIRST-WINDOW-GRAM` — PROVED

### Theorem 2.1 — PSD window domination

For every Borel \(W\subset(0,\infty)\), the kernel \(K_W\) is positive semidefinite. Moreover
\[
  0\preceq K_W\preceq K_\infty.
\tag{2.1}
\]
Equivalently, for every finite set of real coefficients \(z_j\) and frequency pairs \(v_j\),
\[
  0\le
  \sum_{j,k}z_jz_kK_W(v_j,v_k)
  \le
  \sum_{j,k}z_jz_kK_\infty(v_j,v_k).
\tag{2.2}
\]

### Proof

By definition,
\[
\sum_{j,k}z_jz_kK_W(v_j,v_k)
=
\int_W
 \frac{\left(\sum_jz_j\varphi_{v_j}(s)\right)^2}{s^3}\,ds
\ge0.
\]
Replacing \(W\) by its complement in \((0,\infty)\) gives
\(K_\infty-K_W\succeq0\), proving (2.1). \(\square\)

### Corollary 2.2 — exact retained terminal square

For every Boolean twist \(h\),
\[
\boxed{
 \int_W\frac{R_h(s)^2}{s^3}\,ds
 =
 16N^2
 \sum_{r,t}\alpha_r\alpha_t\,
 K_W\!\left((A_r^+,A_r^-),(A_t^+,A_t^-)\right)
}
\tag{2.3}
\]
and therefore
\[
\boxed{
 \int_W\frac{R_h(s)^2}{s^3}\,ds
 \le
 \int_0^\infty\frac{R_h(s)^2}{s^3}\,ds.
}
\tag{2.4}
\]

The signs in the terminal subtraction are the actual \(\alpha_r\alpha_t\) signs. No termwise absolute value has been inserted.

The same inequality survives averaging over the genuine syndrome twists \(h=g_S\).

### Compiler consequence

The fresh phase-switch Dirichlet theorem gives pointwise
\[
  \mathcal E_{\rm cur}(s)
  \le\frac19\,\mathbb E_S R_{g_S}(s)^2,
\qquad
  \mathcal E_{\rm cen}(s)
  \le\frac{11}{1152}\,\mathbb E_S R_{g_S}(s)^2.
\tag{2.5}
\]
Hence for **any** live Borel window \(W\),
\[
\boxed{
  \int_W\frac{\mathcal E_{\rm cur}(s)}{s^3}\,ds
  \le
  \frac19\,
  \mathbb E_S\int_0^\infty\frac{R_{g_S}(s)^2}{s^3}\,ds
}
\tag{2.6}
\]
and similarly
\[
\boxed{
  \int_W\frac{\mathcal E_{\rm cen}(s)}{s^3}\,ds
  \le
  \frac{11}{1152}\,
  \mathbb E_S\int_0^\infty\frac{R_{g_S}(s)^2}{s^3}\,ds.
}
\tag{2.7}
\]

Thus the *window-specific sign problem* identified for the linear phase-switch integral is absent at the authentic square stage. The remaining task is a full-line quadratic-form payment, not a finite-window monotonicity theorem.

---

## 3. `P03-B16-FOUR-SINE-LOG-KERNEL` — PROVED

Put
\[
  F(x)=
  \begin{cases}
    x^2\log|x|,&x\ne0,\\
    0,&x=0.
  \end{cases}
\tag{3.1}
\]
For \(v=(a,b)\), \(w=(c,d)\), write
\[
  x=a-b,\quad u=a+b,\quad y=c-d,\quad z=c+d.
\]

### Theorem 3.1 — exact full-line kernel

\[
\boxed{
\begin{aligned}
K_\infty((a,b),(c,d))
=\frac1{16}\big[&
 F(x-y)+F(x+y)-F(x-z)-F(x+z)\\
 &-F(u-y)-F(u+y)+F(u-z)+F(u+z)
 \big].
\end{aligned}}
\tag{3.2}
\]

### Proof

Use
\[
  \sin(as)\sin(bs)
  =\frac12\{\cos(xs)-\cos(us)\}
\]
and the analogous identity for \(c,d\). After multiplying, use
\[
  \cos(ps)\cos(qs)
  =\frac12\{\cos((p-q)s)+\cos((p+q)s)\}.
\]
This gives eight cosine terms with signs
\[
(+,+,-,-,-,-,+,+).
\]
Their constant coefficients sum to zero. Their quadratic coefficients also cancel:
\[
\sum_\ell \sigma_\ell\lambda_\ell^2=0.
\tag{3.3}
\]
Therefore we may insert the regularized primitive
\[
  \mathcal C(\lambda)
  =
  \int_0^\infty
  \frac{\cos(\lambda s)-1+\frac12\lambda^2s^2\mathbf1_{\{s<1\}}}{s^3}\,ds
  =
  \frac{\lambda^2}{2}
  \left(\log|\lambda|+\gamma-\frac32\right),
\tag{3.4}
\]
with \(\mathcal C(0)=0\). The common quadratic constant in (3.4) cancels again by (3.3), leaving exactly (3.2). \(\square\)

This is an eight-term logarithmic polarization of \(x^2\log|x|\). In particular, the full-line two-copy square is already written in the same logarithmic language as the entropy-side retained bridge.

---

## 4. A dimension-free absolute envelope

Let
\[
  0<q_1\le q_2\le q_3\le q_4
\]
be the four numbers \(|a|,|b|,|c|,|d|\) in increasing order. If one is zero then \(K_\infty=0\).

Using \(|\sin(qs)|\le\min\{1,qs\}\) and splitting at
\(q_4^{-1},q_3^{-1},q_2^{-1},q_1^{-1}\) gives

### Theorem 4.1 — two-smallest logarithmic envelope

\[
\boxed{
\begin{aligned}
|K_\infty((a,b),(c,d))|
&\le
q_1q_2
\left(
2-\frac{q_3}{2q_4}
+\log\frac{q_3}{q_2}
\right)
-\frac{q_1^2}{2}\\
&\le
q_1q_2\left(2+\log\frac{q_3}{q_2}\right).
\end{aligned}}
\tag{4.1}
\]

### Proof

The five threshold ranges contribute respectively
\[
\frac{q_1q_2q_3}{2q_4},
\qquad
q_1q_2\left(1-\frac{q_3}{q_4}\right),
\qquad
q_1q_2\log\frac{q_3}{q_2},
\]
\[
q_1(q_2-q_1),
\qquad
\frac{q_1^2}{2}.
\]
Their sum is the first right side of (4.1). \(\square\)

The important point is that the full-line kernel is dimension-free at the scalar level. The only scale loss is logarithmic.

---

## 5. `P03-B16-LOG-SCALE-BARRIER` — PROVED

The logarithm in (4.1) cannot be removed.

For the diagonal kernel with \(0<b\le a\),
\[
\boxed{
K_\infty((a,b),(a,b))
=
\frac14\left[
(a-b)^2\log(a-b)
+(a+b)^2\log(a+b)
-2a^2\log a
-2b^2\log b
\right],
}
\tag{5.1}
\]
with \(0^2\log0=0\). Also
\[
\boxed{
K_\infty((a,b),(a,b))
\le
b^2\left(1+\log\frac ab\right).
}
\tag{5.2}
\]

Taking \(a=1\), \(b=\varepsilon\downarrow0\), Taylor expansion of
\(x^2\log x\) at \(x=1\) gives
\[
\boxed{
K_\infty((1,\varepsilon),(1,\varepsilon))
=
\frac{\varepsilon^2}{2}\log\frac1\varepsilon
+\frac34\varepsilon^2
-\frac1{24}\varepsilon^4
+O(\varepsilon^6).
}
\tag{5.3}
\]

Therefore
\[
\frac{K_\infty((1,\varepsilon),(1,\varepsilon))}
{\varepsilon^2}
\longrightarrow\infty.
\tag{5.4}
\]

### Consequence

There is **no** universal constant \(C\) such that
\[
K_\infty((a,b),(a,b))
\le C\min\{a^2,b^2\}
\tag{5.5}
\]
for all \(a,b\), and in particular no universal
\[
K_\infty((a,b),(a,b))\le C a^2b^2
\]
after normalizing \(\max\{|a|,|b|\}=1\).

This is a rigorous obstruction to finishing the large-Borel corridor by extending the fresh small-\(s\) quartic estimate with a scale-free quartic-moment bound. The full-line payment necessarily sees an entropy-like logarithm of amplitude separation.

It does **not** obstruct the signed compiler itself: (3.2) retains cross terms, terminal signs and the exact \(x^2\log|x|\) structure. It says only that the logarithmic/entropy or moment-credit structure cannot be discarded.

---

## 6. How this changes the remaining FEI interface

The fresh fleet04/B16 theorem already handles the authentic local clone-pair/terminal geometry at small Borel time and gives a dimension-free ordered-parent square bank. The fresh fleet03/B16 theorem already identifies the full-line *linear* signed phase switch with a terminal-aware entropy increment, but its synthetic packet shows that linear endpoint control alone does not dominate a finite live subwindow.

The square-first theorem above removes that particular finite-window obstruction:

1. keep the exact signed terminal coefficients;
2. form the authentic phase-switch square;
3. integrate the square on the live window;
4. enlarge the window to \((0,\infty)\) by PSD order;
5. use the exact logarithmic polarization (3.2).

The remaining universal inequality is now the explicit full-line two-copy problem
\[
\boxed{
16N^2\,
\mathbb E_S
\sum_{r,t}\alpha_r\alpha_t
K_\infty\!\left(
(A_{r,S}^+,A_{r,S}^-),
(A_{t,S}^+,A_{t,S}^-)
\right)
\le C\,J(f),
}
\tag{6.1}
\]
or a compatible bound by the already-reserved R16/moment/terminal/negative-credit banks.

The diagonal asymptotic (5.3) says the next proof should **not** try to dominate (6.1) by a scale-free second or fourth moment. The natural next attack is to sum the eight \(F(x)=x^2\log|x|\) terms in (3.2) against the signed terminal tensor \(\alpha_r\alpha_t\) and identify which pieces are exactly terminal-aware entropy differences and which pieces are the retained moment/R16 credits.

That is a much narrower algebraic target than the previous “control an arbitrary finite Borel window” formulation.

---

## 7. Falsification checks

The companion script `check_b16_four_sine_gram.py` is a new checker for this run; it does not touch the settled read-once certificate.

It verifies:

- 3,969 exact integer instances of both regularizer cancellations in (3.3);
- nine independent numerical comparisons between (3.2) and direct oscillatory quadrature, with maximum observed discrepancy \(5.23\times10^{-8}\) at cutoff 1200, below the crude absolute tail bound \(3.48\times10^{-7}\);
- the absolute envelope (4.1) on those tests;
- positivity of one deterministic five-by-five closed-kernel Gram matrix;
- the diagonal expansion (5.3) numerically down to \(\varepsilon=10^{-4}\), with the normalized fourth-order remainder tending to \(-1/24\).

Executed checker SHA-256:
`383b8c2e8d0334040d405dbbae4a9be574933ac008082e9b4bbfbfabffa056a8`.

Archived output SHA-256:
`ce10b7ca116a0b183eb0b83adf154876b66a8c47d5f9d5502846a5cc0a9ca2c4`.

These checks are falsification evidence only; the all-dimensional statements above are proved analytically.

---

## 8. Classification and handoff

### PROVED here

- finite-window four-sine kernels are PSD and are dominated by the full half-line in Loewner order;
- the authentic retained phase-switch square has the exact two-copy representation (2.3), with terminal signs preserved;
- every current-side live window can therefore be enlarged to the full half-line **after squaring**;
- the full-line kernel is the exact eight-term logarithmic polarization (3.2);
- the dimension-free two-smallest envelope (4.1);
- the unavoidable logarithmic scale-separation barrier (5.3)--(5.5).

### NOT proved

- the full-line quadratic form (6.1) is not yet bounded by \(CJ(f)\);
- no terminal/R16/moment or negative-credit ledger is spent here;
- unrestricted FEI remains OPEN / NOT PROVED.

### Next recipient / next exact calculation

The most direct continuation for the signed-window interface is fleet03/B16 together with fleet03/B18:

> Expand the signed \(\alpha\otimes\alpha\) sum of the eight \(x^2\log|x|\) polarizations in (3.2), keeping the same terminal code and syndrome twist. Try to rewrite its diagonal/logarithmic component as a terminal-aware entropy or Hardy collision term, and send the remaining off-diagonal part to the signed derivative flag bank. A scale-free quartic bound is now rigorously ruled out; the logarithmic credit must remain visible.

**Full unrestricted FEI remains OPEN / NOT PROVED.**
