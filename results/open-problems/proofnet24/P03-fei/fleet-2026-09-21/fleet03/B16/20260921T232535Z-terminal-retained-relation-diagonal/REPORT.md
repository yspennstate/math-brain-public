# B16 FEI campaign C — terminal-retained codimension-two relation-diagonal no-go

**Run:** `20260921T232535Z-fleet03-B16-r11`  
**Scope:** `fleet03 / B16`, latest owner execution order `FEI-PROOF-EXECUTION-20260921T230620Z`  
**Execution:** **WITHOUT_VERIFIED_BRAIN**  
**Full unrestricted FEI:** **OPEN / NOT PROVED**  
**Outcome classification:** **CANDIDATE_REFUTED** — the positive relation-diagonal version of the degree-conversion step is false. The complete signed NET expression is not refuted.

## 0. Exact assignment and change from the entering gap

The latest common execution reset supersedes the older interface-C subassignment for this invocation. Its B16/fleet03 instruction is:

> attack the SAME net bound with exact sparse-defect and tensor/asymptotic Boolean constructions.

The current C lead result consumed here is

`proofnet24/P03-fei/fleet-2026-09-21/fleet02/B18/20260921T230348Z-oriented-relation-square-root/REPORT.md`

at scientific master `c307230eb8feea5358179fcefa2cd714c602cded`, blob
`74a8144e588366e95d5c8b5ca8f0e384d8f1d6fd`.

That report proves the all-order oriented root
\[
\zeta_A(y)=\frac{h_{A_V}(y)-h_{A_U}(y)}2,\qquad \zeta_A^2=\nu_A,
\]
and a dimension-free physical Dirichlet estimate after inverse **relation cardinality** `1/|A|`. It also records the exact unresolved alternative:

1. compare the authentic active-syndrome inverse degree `1/|R|` to `1/|A|` without losing signed cancellation; or
2. keep the off-diagonal even-correlation cross ledger and pay it once from the signed R16/high/terminal/entropy ledger.

This run attacks alternative 1 on an exact Boolean family and proves that the natural positive diagonal comparison is impossible even after the half-band terminal subtraction is kept exactly. The calculation simultaneously shows why alternative 2 is not optional.

The preceding B16 positive-current and finite-window routes are not retried.

## 1. The exact Boolean construction

Let the physical cube have dimension `n>=4`, and put `N=2^n`. Write
\[
x=(x_1,x_2,z)\in\mathbb F_2^2\times\mathbb F_2^{n-2}.
\]

Let
\[
Q=\{x:x_1=x_2=0\},
\qquad
g=1_Q=(1+x_1)(1+x_2)\in RM(2,n),
\]
and take the Boolean phase
\[
f(x)=(-1)^{g(x)}=
\begin{cases}
-1,&x\in Q,\\
+1,&x\notin Q.
\end{cases}
\tag{1.1}
\]

The function ignores all `n-2` dummy coordinates. Its Fourier law has four atoms of mass `1/4`, hence
\[
H_2(f)=2,\qquad I(f)=J(f)=1.
\tag{1.2}
\]
So this family is emphatically **not** an FEI counterexample.

Take the authentic one-step q-flip gate
\[
M_0=RM(1,n)\longrightarrow M_0+\langle g\rangle .
\tag{1.3}
\]
Its dual relation code is
\[
C_0=M_0^\perp=RM(1,n)^\perp.
\]
A relation `A` contributes to the gate exactly when
\[
A\in C_0,\qquad g(A):=\sum_{x\in A}g(x)=1\pmod2.
\tag{1.4}
\]
Because `f=(-1)^g`, every such relation is frustrated:
\[
f_A=\prod_{x\in A}f(x)=(-1)^{g(A)}=-1.
\tag{1.5}
\]

The active-syndrome cube for this one transition has one coordinate. Therefore every relation in (1.4) contributes to the same odd active syndrome
\[
R=\{j\},\qquad |R|=1,
\tag{1.6}
\]
and the active `L^{-1/2}` multiplier is exactly one. There is no hidden active-degree gain available in this example.

## 2. PROVED — terminal subtraction preserves the whole gate-separated relation ensemble

Use the current half-band terminal mask code
\[
M_d=RM(d,n),\qquad d=\lceil n/2\rceil,
\qquad D_d=M_d^\perp.
\]

Since `d>=2` and `g in RM(2,n) subseteq M_d`, every `A in D_d` obeys
\[
g(A)=0.
\tag{2.1}
\]
Hence
\[
\boxed{
\{A\in C_0:g(A)=1\}\cap D_d=\varnothing.
}
\tag{2.2}
\]

Equivalently, the terminal gate packet itself is pointwise zero: translation `m -> m+g` permutes `M_d`, so the two sides of the signed gate difference cancel before any square. Thus the retained projector `C_0-D_d` keeps **every** relation in (1.4), with the full dual-code multiplicity.

This removes a possible escape route: the terminal code does not delete the relation ensemble used below.

## 3. PROVED — none of these relations is physically frustration-null

For `b in F_2^2`, let
\[
c_b(A)=|A\cap\{(x_1,x_2)=b\}|\pmod2.
\]
If `A in C_0`, orthogonality to `1,x_1,x_2` says that the four-bit vector `(c_b)` is orthogonal to `RM(1,2)`. Since
\[
RM(1,2)^\perp=\operatorname{span}\{(1,1,1,1)\},
\]
and `g(A)=c_00(A)=1`, necessarily
\[
\boxed{c_b(A)=1\quad\text{for every }b\in\mathbb F_2^2.}
\tag{3.1}
\]

Translate the Boolean phase by an arbitrary physical `y`. Its negative set is the corresponding translated base fibre. Equation (3.1) therefore gives
\[
h_A(y)=\prod_{x\in A}f(x+y)=-1
\qquad\text{for every physical translation }y.
\tag{3.2}
\]
Consequently the peer oriented root satisfies
\[
\boxed{\zeta_A(y)^2=1\quad\text{for every }A\text{ in (1.4) and every }y.}
\tag{3.3}
\]

Thus the positive relation diagonal below is not inflated by relations whose physical root vanishes.

## 4. Exact coherent signed packet

Write
\[
\theta=\frac{s}{N}.
\]
The source-exact all-order relation formula from the finite-resolvent gate expansion specializes to
\[
G_n(s)
=
2\sum_{\substack{A\in C_0\\g(A)=1}}
(-1)^{|A|/2}
\sin^{|A|}\theta\,
\cos^{N-|A|}\theta .
\tag{4.1}
\]

The same quantity can be evaluated directly over the affine mask code. For the comparator `z=0`, the correlation with an affine character is nonzero only for the constant character, so
\[
\mathbb E_{m\in RM(1,n)}\cos(s\beta_0(m))
=
\left(1-\frac1N\right)+\frac1N\cos s.
\]
For `z=g`, the Walsh support of `(-1)^g` consists of the four characters on the first two variables, each with absolute coefficient `1/2`. Hence
\[
\mathbb E_{m\in RM(1,n)}\cos(s\beta_g(m))
=
\left(1-\frac4N\right)+\frac4N\cos(s/2).
\]
Using the exact product-to-sum gate identity gives
\[
\boxed{
G_n(s)=\frac{\cos s-4\cos(s/2)+3}{N}.
}
\tag{4.2}
\]

This is the **entire** retained one-gate packet, not a selected subfamily.

## 5. PROVED — exact dual-code multiplicity formula

Set
\[
p=\sin^2\theta,\qquad \rho=1-2p=\cos(2\theta),
\qquad a=\rho^{N/4}.
\]
Let `A_p` be an independent Bernoulli-`p` random subset of the `N` truth-table points and define the gate-separated relation event
\[
E=\{A_p\in C_0,\ g(A_p)=1\}.
\]

Fourier inversion over the `n+2` linear constraints gives an exact closed form. The affine code `RM(1,n)` has weights
\[
0\ (1),\qquad N\ (1),\qquad N/2\ (2N-2).
\]
The coset `g+RM(1,n)` has weights
\[
N/4\ (4),\qquad 3N/4\ (4),\qquad N/2\ (2N-8).
\]
Therefore
\[
\begin{aligned}
P_n(p):=\Pr(E)
&=\frac{1}{4N}
\left[
1+\rho^N+6\rho^{N/2}
-4\rho^{N/4}-4\rho^{3N/4}
\right]\\
&=\boxed{\frac{(1-a)^4}{4N}}.
\end{aligned}
\tag{5.1}
\]

This is an exact multiplicity calculation for the authentic retained relation ensemble.

Let
\[
Q_n(p)=
\mathbb E\bigl[|A_p|\,1_E\bigr].
\]
Differentiating (5.1) and using the Bernoulli derivative identity,
\[
P_n'(p)=
\frac{Q_n(p)-NpP_n(p)}{p(1-p)},
\]
gives
\[
P_n'(p)=\frac{a(1-a)^3}{2\rho},
\]
and therefore
\[
\boxed{
Q_n(p)=NpP_n(p)
+
p(1-p)\frac{a(1-a)^3}{2\rho}.
}
\tag{5.2}
\]

## 6. PROVED — the positive inverse-relation-degree bridge is unbounded

The most favorable positive relation-root diagonal compatible with the peer `1/|A|` physical allocation contains
\[
\mathcal D_n(s)
:=
4\sum_{\substack{A\in C_0\\g(A)=1}}
\frac{
\sin^{2|A|}\theta\,
\cos^{2(N-|A|)}\theta
}{|A|}.
\tag{6.1}
\]
By (2.2) this is already terminal-retained, and by (3.3) no additional `zeta_A^2` factor reduces it.

Cauchy-Schwarz gives
\[
\left(\sum_{A\in E}w_A\right)^2
\le
\left(\sum_{A\in E}\frac{w_A}{|A|}\right)
\left(\sum_{A\in E}|A|w_A\right),
\]
where
\[
w_A=p^{|A|}(1-p)^{N-|A|}.
\]
Hence
\[
\boxed{
\mathcal D_n(s)
\ge
4\frac{P_n(p)^2}{Q_n(p)}.
}
\tag{6.2}
\]

Now choose a live time
\[
s_n=\pi+4\pi k_n
\]
with `k_n` the nearest integer to
\[
\frac{N/\sqrt{2n}-\pi}{4\pi}.
\]
Then
\[
s_n=\frac{N}{\sqrt{2n}}+O(1),
\tag{6.3}
\]
and for all sufficiently large `n`,
\[
40<s_n<\frac{N}{\sqrt{2(n-1)}},
\]
so this is inside the current half-band live corridor.

Because `s_n=pi mod 4pi`, equation (4.2) gives exactly
\[
\boxed{G_n(s_n)=\frac2N,\qquad G_n(s_n)^2=\frac4{N^2}.}
\tag{6.4}
\]

Furthermore
\[
p_n=\sin^2(s_n/N)
=\frac1{2n}+O(n^{-2}),
\tag{6.5}
\]
while
\[
a_n=(1-2p_n)^{N/4}\to0
\]
super-exponentially in the physical dimension. Equations (5.1)-(5.2) yield
\[
P_n(p_n)=\frac{1+o(1)}{4N},
\qquad
Q_n(p_n)=\frac{p_n}{4}(1+o(1)).
\]
Substituting into (6.2),
\[
\mathcal D_n(s_n)
\ge
\frac{1+o(1)}{p_nN^2}
=
\frac{(2+o(1))n}{N^2}.
\tag{6.6}
\]
Comparing with (6.4),
\[
\boxed{
\frac{\mathcal D_n(s_n)}{G_n(s_n)^2}
\ge
\left(\frac12+o(1)\right)n
\longrightarrow\infty.
}
\tag{6.7}
\]

### Theorem `P03-B16-TERMINAL-RETAINED-RELATION-DIAGONAL-NOGO`

There is no finite universal constant `C` for which the authentic terminal-retained inverse-relation-degree positive diagonal of the one-step codimension-two gate always obeys
\[
\mathcal D_n(s)\le C\,|G_n(s)|^2
\tag{6.8}
\]
throughout the live corridor.

Since this example has only one active syndrome coordinate, `|R|=1`, the failure cannot be repaired by the active-syndrome `1/|R|` square-root allocation. A universal conversion from that coherent active square to a **positive relation-resolved** `1/|A|` bank is false.

This refutes precisely the positive-diagonal form of option (a) in the consumed fleet02/B18 handoff. It does **not** refute a signed degree conversion in which the off-diagonal cross ledger stays present.

## 7. PROVED — the missing mass is an enormous negative cross ledger

Before the `1/|A|` weight, the relation-resolved diagonal is
\[
\mathcal D_n^{(0)}(s)
=
4\sum_{\substack{A\in C_0\\g(A)=1}}
p^{|A|}(1-p)^{N-|A|}
=
4P_n(p).
\tag{7.1}
\]
At the live times `s_n`,
\[
\mathcal D_n^{(0)}(s_n)
=
\frac{1+o(1)}{N},
\qquad
G_n(s_n)^2=\frac4{N^2}.
\tag{7.2}
\]
Thus
\[
\boxed{
\frac{G_n(s_n)^2}{\mathcal D_n^{(0)}(s_n)}
=
\frac{4+o(1)}{N}\to0.
}
\tag{7.3}
\]

When the coherent signed relation sum is squared, the total off-diagonal cross ledger is therefore
\[
\boxed{
\mathcal X_n(s_n)
=
G_n(s_n)^2-\mathcal D_n^{(0)}(s_n)
=
-\frac{1+o(1)}{N}.
}
\tag{7.4}
\]
It cancels a `1-o(1)` fraction of the positive relation diagonal.

The consumed fleet02/B18 theorem identifies every product of two oriented roots exactly with a four-term **even-relation correlation** expression. Equation (7.4) therefore shows that the even-correlation cross bank is not a small technical remainder on this legitimate Boolean family. It is the leading cancellation mechanism.

This is the substantive application of the peer result: its alternative (b) must remain co-located with the signed source. Relationwise positivity, even with the correct `1/|A|` factor, destroys the cancellation by an unbounded factor.

## 8. Attempted refutation and dead route

The first construction tried in this run padded one frustrated weight-four relation by disjoint six-point `f`-null dual relations. It gives an exact binomial cancellation
\[
(1-\tan^6\theta)^p
\]
while every padded relation has the same oriented root and alternating R32 sign. That algebra is correct, but **by itself it is not enough** to refute a bound on the full compiler packet, because unselected relations may contribute to the same coherent syndrome.

That shortcut was therefore not promoted.

The replacement calculation in Sections 4–7 evaluates the **entire** gate-separated dual ensemble exactly via the affine-code/coset weight enumerator. It eliminates that objection.

Further attempted escapes were also checked:

- **Terminal subtraction:** fails as an escape because `g in RM(d,n)`, so `D_d` contains no gate-separated relation at all.
- **Physical-null roots:** fails because every retained relation is frustrated under every physical translation, equation (3.3).
- **Active-degree rescue:** fails because the authentic active cube has one coordinate, so `1/|R|=1`.
- **FEI counterexample interpretation:** false. The Boolean family has `H_2/I=2`.

What remains possible, and is not refuted, is exactly the signed cross-ledger mechanism.

## 9. Executable checks

`check_codim2_terminal_relation_diagonal.py` uses only the Python standard library.

It enumerates the complete event relation set through `n=4`, checking:

- the exact event-coset cardinality;
- all translated-frustration parities;
- the full signed relation packet (4.1) against the closed form (4.2);
- the exact probability formula (5.1);
- the exact first-moment formula (5.2);
- the Cauchy inverse-degree lower bound.

It checked 1,033 event relations, 4,132 translated-frustration instances, 9 full-packet identities, 18 probability/moment identities, and 9 inverse-degree Cauchy inequalities.

The asymptotic table uses the exact live phase choice above. The lower bound `D_n/G_n^2` was approximately
\[
3.846,\ 6.136,\ 8.078,\ 12.084,\ 16.084,\ 24.084,\ 32.083,\ 48.083,\ 64.083
\]
for
\[
n=8,12,16,24,32,48,64,96,128,
\]
consistent with `n/2+O(1)`.

These finite calculations are self-check/falsification evidence. The all-dimensional statements are the symbolic derivations above.

## 10. Honest proof chain after this run

**PROVED**

1. The codimension-two Boolean gate family (1.1) has `H_2=2`, `I=J=1`.
2. Its entire gate-separated `C_0` relation ensemble survives the half-band terminal projector exactly.
3. Every such relation has `zeta_A^2=1` under every physical translation.
4. The full coherent retained packet is exactly (4.2).
5. Its full dual-code multiplicity and first relation-size moment are exactly (5.1)-(5.2).
6. The positive inverse-relation-degree diagonal exceeds the coherent active-syndrome square by `(1/2+o(1))n` along authentic live times.
7. The unweighted off-diagonal signed cross bank cancels `1-o(1)` of the relation diagonal.

**REFUTED**

A universal **positive relation-diagonal** comparison converting the authentic active-syndrome `1/|R|` local square into the oriented-root `1/|A|` bank, even with terminal retention and at the correct live window.

**OPEN / CONDITIONAL**

- Identification of the exact even-correlation cross ledger with the already-reserved R16/high-resolvent/negative-entropy/terminal credits, without reuse.
- A complete source-exact NET signed candidate satisfying the execution-reset admission gate.
- Full unrestricted FEI.

The theorem does not permit dropping the negative R32 shell signs, cross terms, R16 refund, entropy credits, outside-window remainder, or terminal endpoint.

## 11. Joint handoff

- `consumed_peer_artifact`: `fleet02/B18/20260921T230348Z-oriented-relation-square-root/REPORT.md`, blob `74a8144e588366e95d5c8b5ca8f0e384d8f1d6fd`.
- `applied_to_claim`: its exact remaining option (a), converting active-syndrome inverse degree to a positive relation-root inverse-degree physical bank.
- `new_result`: `P03-B16-TERMINAL-RETAINED-RELATION-DIAGONAL-NOGO`, equations (6.7)-(6.8), plus the exact leading negative cross ledger (7.4).
- `remaining_implication`: keep and identify the off-diagonal even-correlation cross terms inside the one-use R16/high/terminal/negative-entropy ledger, and prove the resulting complete signed NET bound; do not attempt another positive relationwise contraction.
- `next_recipient`: `fleet02/B18` as campaign-C lead, with `fleet04/B16` as the exact all-order signed relation-ledger partner.
- `full_problem_change`: no FEI closure; one natural universal subbridge is now rigorously refuted.
- `mechanism_change`: yes — from positive degree conversion to an exact whole-ensemble MacWilliams/coset calculation that forces off-diagonal signed cancellation.
