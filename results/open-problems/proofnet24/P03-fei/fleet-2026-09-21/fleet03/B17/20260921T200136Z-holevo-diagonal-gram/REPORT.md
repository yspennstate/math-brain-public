# B17 FEI interface-C adversary — Boolean logarithmic obstruction and a Holevo/tight-frame replacement

**Date:** 21 September 2026  
**Role:** `fleet03/B17`, FEI new proof mechanisms; exact Boolean adversary for joint interface C  
**Execution:** `WITHOUT_VERIFIED_BRAIN`  
**Unrestricted FEI:** **OPEN / NOT PROVED**  
**Route:** APPROACH 14, new subroute **C-Holevo / rank-one phase-frame entropy**  
**Claim level:** one exact admissible-Boolean refutation of a tempting interface-C scalar lemma, one universal tight-frame entropy theorem, and one exact signed-coset reduction identifying the next unpaid implication. No novelty or publication-priority claim.

## 0. Why this is a method change

The previous B17 mechanisms included Palm deletion, finite face-state transport, and balanced thin-shell tensor amplification. This run does not add another checker to those routes. It attacks the current joint interface C after consuming completed cross-account results.

The main peer input is fleet01/B16

`proofnet24/P03-fei/fleet-2026-09-21/fleet01/B16/20260921T195223Z-square-first-window-gram/REPORT.md`.

That report proves that after the authentic phase switch is squared, every live Borel window is PSD-dominated by the full half-line. For
\[
 \varphi_{(a,b)}(s)=\sin(as)\sin(bs),\qquad
 K_W((a,b),(c,d))=\int_W\frac{\varphi_{(a,b)}(s)\varphi_{(c,d)}(s)}{s^3}\,ds,
\]
it proves `0 <= K_W <= K_infty` in Loewner order and gives the exact logarithmic full-line kernel. In particular, with
\[
 F(x)=x^2\ln|x|,\qquad F(0)=0,
\]
\[
 K_\infty((a,b),(a,b))
 =\frac14\{F(a-b)+F(a+b)-2F(a)-2F(b)\}.
\tag{0.1}
\]
It also proves that the logarithmic separation is genuinely present at the scalar level.

I additionally consume fleet02/B16

`proofnet24/P03-fei/fleet-2026-09-21/fleet02/B16/20260921T193735Z-codimension-normalization-parent-bridge/REPORT.md`,

which proves that compressing an authentic signed parent to a scalar and then rebuilding a positive/TV-paid plaquette lift costs at least a codimension factor. Therefore a useful replacement must preserve signed cancellation before total variation rather than revert to that refuted postcompression route.

Finally, fleet04/B16

`proofnet24/P03-fei/fleet-2026-09-21/fleet04/B16/20260921T191216Z-local-triple-curvature-flag/REPORT.md`

proves the distance-four dual-code orthogonality used below to recognize the authentic code phase families as tight frames.

## 1. Exact statement challenged

A natural reaction to the logarithmic scalar kernel is to hope Booleanity removes the logarithm after summing the physical/code frequencies. The strongest useful scale-free version would be
\[
 \boxed{
 \sum_r K_\infty((a_r,b_r),(a_r,b_r))
 \le C\sum_r\min\{a_r^2,b_r^2\}
 }
\tag{1.1}
\]
with a universal `C`, where `a_r,b_r` are the two signed-side amplitudes produced by a Boolean phase split.

I first attack (1.1) on the **actual positive `P_0=RM(1,n)` phase bank**, which is just the ordinary Walsh character bank with the harmless global-sign duplication.

## 2. REFUTED-LEMMA — an exact admissible Boolean logarithmic obstruction

Let `n` be even, `N=2^n`, and define
\[
 f_n(0)=-1,\qquad f_n(x)=+1\quad(x\ne0).
\tag{2.1}
\]
Let the Boolean twist be the explicit quadratic bent function
\[
 h_n(x)=(-1)^{x_1x_2+x_3x_4+\cdots+x_{n-1}x_n}.
\tag{2.2}
\]
Its normalized Walsh transform satisfies
\[
 \widehat h_n(\xi)=\frac{\sigma_\xi}{\sqrt N},\qquad \sigma_\xi\in\{\pm1\}.
\tag{2.3}
\]
Because `h_n(0)=1`, inversion at zero gives
\[
 N_+-N_-=\sqrt N,
\]
so exactly
\[
 N_+=\frac{N+\sqrt N}{2},\qquad
 N_-=\frac{N-\sqrt N}{2}.
\tag{2.4}
\]

Split the twist by the sign of `f_n`:
\[
 u=h_n1_{\{f_n=+1\}},\qquad v=h_n1_{\{f_n=-1\}}.
\]
For each Walsh character `xi`, put
\[
 a_\xi=\widehat u(\xi),\qquad b_\xi=\widehat v(\xi).
\]
Since the negative set is the single point zero and `h_n(0)=1`,
\[
 b_\xi=\frac1N,
\qquad
 a_\xi=\frac{\sigma_\xi}{\sqrt N}-\frac1N.
\tag{2.5}
\]
For every even `n>=2`,
\[
 \sum_\xi\min(a_\xi^2,b_\xi^2)=\frac1N.
\tag{2.6}
\]

The kernel is homogeneous of degree two, because the `t^2 ln|t|` scale term cancels in (0.1). Therefore the exact diagonal bank is
\[
 G_n:=\sum_\xi K_\infty((a_\xi,b_\xi),(a_\xi,b_\xi))
 =\frac1{N^2}\left[
 N_+K_\infty((\sqrt N-1,1),(\sqrt N-1,1))
 +N_-K_\infty((\sqrt N+1,1),(\sqrt N+1,1))
 \right].
\tag{2.7}
\]
Fleet01/B16's diagonal expansion implies
\[
 K_\infty((A,1),(A,1))
 =\frac12\ln A+\frac34+O(A^{-2}),\qquad A\to\infty.
\tag{2.8}
\]
Substitution into (2.7) gives
\[
 \boxed{
 G_n=\frac{\ln N}{4N}+O(N^{-1})
 }
\tag{2.9}
\]
and hence, using (2.6),
\[
 \boxed{
 \frac{G_n}{\sum_\xi\min(a_\xi^2,b_\xi^2)}
 =\frac14\ln N+O(1)\longrightarrow\infty.
 }
\tag{2.10}
\]
Thus (1.1) is **REFUTED**, even on an explicit admissible Boolean family and even on the authentic `P_0` phase bank. The scalar logarithm is not an artifact of arbitrary real frequencies.

This does **not** refute FEI. Here
\[
 I(f_n)=\frac{2n}{N},
\tag{2.11}
\]
so (2.9) gives
\[
 \frac{G_n}{I(f_n)}\longrightarrow\frac{\ln2}{8}.
\tag{2.12}
\]
The logarithm is exactly on an influence-compatible scale for this extremal test.

The targeted executed calculation, without an exhaustive Boolean sweep, gives:

| n | N | `N G_n` | `G_n/I(f_n)` |
|---:|---:|---:|---:|
| 4 | 16 | 1.391495365 | 0.173936921 |
| 8 | 256 | 2.133194116 | 0.133324632 |
| 12 | 4096 | 2.829248233 | 0.117885343 |
| 16 | 65536 | 3.522576642 | 0.110080520 |
| 20 | 1048576 | 4.215735148 | 0.105393379 |

The complete table and reproducer are adjacent to this report.

## 3. PROVED replacement — a Holevo/tight-frame diagonal theorem

The failed bound tried to delete the logarithm. The correct replacement keeps it and recognizes it as information.

### Theorem 3.1 — `P03-B17-HOLEVO-DIAGONAL-GRAM`

Let `H` be a finite-dimensional real Hilbert space. Let unit vectors `phi_r` and positive weights `lambda_r` form a rank-one tight POVM:
\[
 \sum_r\lambda_r|\phi_r\rangle\langle\phi_r|=I.
\tag{3.1}
\]
Let `f,h` be Boolean functions represented as normalized sign vectors, and after a possible global sign of `f` let
\[
 q=\Pr[f=-1]\le\frac12.
\]
Write
\[
 |u\rangle=1_{\{f=+1\}}|h\rangle,
 \qquad
 |v\rangle=1_{\{f=-1\}}|h\rangle,
\]
\[
 a_r=\langle\phi_r,u\rangle,
 \qquad
 b_r=\langle\phi_r,v\rangle.
\tag{3.2}
\]
Then
\[
 \boxed{
 \sum_r\lambda_r K_\infty((a_r,b_r),(a_r,b_r))
 \le \frac12 h_{\rm nat}(q),
 }
\tag{3.3}
\]
where `h_nat(q)=-q ln q-(1-q)ln(1-q)`.

For a Boolean function on the cube this implies
\[
 \boxed{
 \sum_r\lambda_r K_\infty((a_r,b_r),(a_r,b_r))
 \le \frac{\ln2}{2}\,I(f).
 }
\tag{3.4}
\]

### Proof

Put
\[
 c_r=a_r+b_r=\langle\phi_r,h\rangle,
 \qquad
 d_r=a_r-b_r=\langle\phi_r,fh\rangle.
\]
By (3.1),
\[
 P_+(r)=\lambda_r c_r^2,
 \qquad
 P_-(r)=\lambda_r d_r^2
\tag{3.5}
\]
are probability distributions. Also define the joint side/outcome masses
\[
 A_r=\lambda_r a_r^2,
 \qquad
 B_r=\lambda_r b_r^2,
\tag{3.6}
\]
whose side marginal is `(1-q,q)`, and let
\[
 M_r=A_r+B_r=\frac12(P_+(r)+P_-(r)).
\]

Summing the exact diagonal formula (0.1), the terms involving `ln lambda_r` cancel identically and give the exact identity
\[
 \boxed{
 4\sum_r\lambda_rK_\infty((a_r,b_r),(a_r,b_r))
 =H_{\rm nat}(\mathrm{side}\mid R)+I(Z;R),
 }
\tag{3.7}
\]
where `Z` is uniform on the two pure states `|h>` and `|fh>`, and `R` is the POVM outcome. Indeed,
\[
 H(\mathrm{side},R)-\tfrac12H(P_+)-\tfrac12H(P_-)
 =H(\mathrm{side}\mid R)+H(M)-\tfrac12H(P_+)-\tfrac12H(P_-).
\]
The last three terms are exactly `I(Z;R)`.

First,
\[
 H(\mathrm{side}\mid R)\le h_{\rm nat}(q).
\tag{3.8}
\]
Second, Holevo's bound for this rank-one measurement gives
\[
 I(Z;R)\le S\!\left(\frac{|h\rangle\langle h|+|fh\rangle\langle fh|}{2}\right).
\tag{3.9}
\]
The overlap is
\[
 \langle h,fh\rangle=\mathbb E f=1-2q,
\]
so the two nonzero eigenvalues of the average state are `1-q` and `q`. Hence the right side of (3.9) is exactly `h_nat(q)`. Combining (3.7)--(3.9) proves (3.3).

For `0<=q<=1/2`,
\[
 h_{\rm nat}(q)\le2q\ln(1/q).
\tag{3.10}
\]
The cube edge-isoperimetric inequality gives
\[
 I(f)\ge2q\log_2(1/q)
 =\frac{2q\ln(1/q)}{\ln2}.
\tag{3.11}
\]
Equations (3.3), (3.10) and (3.11) prove (3.4). `square`

### Boundary checks

For a dictator with the ordinary Walsh frame, the two active outcomes each have `(a,b)=(1/2, +/-1/2)` up to signs, so
\[
 G=\frac{\ln2}{2}=\frac{\ln2}{2}I(f),
\]
showing (3.4) is sharp at this boundary. For constant `f`, `q=0` and both sides vanish.

## 4. Application to the authentic retained code banks

Fleet04/B16 proves that for either retained relation code `E<=C_0`, no weight-two word belongs to `E`. Let `P=E^perp`, and define the unit phase vectors
\[
 \phi_r(x)=\frac{(-1)^{r_x}}{\sqrt N},\qquad r\in P.
\]
Character orthogonality then gives
\[
 \frac1{|P|}\sum_{r\in P}|\phi_r\rangle\langle\phi_r|=\frac1N I.
\tag{4.1}
\]
Thus `lambda_r=N/|P|` is exactly a tight POVM and Theorem 3.1 applies to **both** authentic banks `P_0=C_0^perp=RM(1,n)` and `P_1=D_d^perp`:
\[
 \boxed{
 \frac1{|P|}\sum_{r\in P}
 K_\infty((A_r^+,A_r^-),(A_r^+,A_r^-))
 \le \frac{h_{\rm nat}(q)}{2N}
 \le \frac{\ln2}{2N}I(f).
 }
\tag{4.2}
\]
This is a dimension-free Boolean payment for each **diagonal positive code bank** after the exact `1/N` frame normalization.

It does not yet close interface C, because the authentic terminal subtraction is a signed cross-bank tensor, not the sum of two positive diagonal banks.

## 5. PROVED signed-coset reduction — the next replacement mechanism

The retained coefficients used by fleet01/B16 are
\[
 \alpha_r=\frac1{|P_0|}1_{\{r\in P_0\}}
            -\frac1{|P_1|}1_{\{r\in P_1\}},
\qquad P_0\subset P_1.
\tag{5.1}
\]
Let `Phi(v)` be the Hilbert feature
\[
 \Phi(a,b)(s)=\frac{\sin(as)\sin(bs)}{s^{3/2}},
\]
so `K_infty(v,w)=<Phi(v),Phi(w)>`. Put
\[
 m_0=\mathbb E_{r\in P_0}\Phi(v_r),
 \qquad
 m_1=\mathbb E_{r\in P_1}\Phi(v_r).
\]
Then the exact terminal quadratic form is simply
\[
 \boxed{
 \sum_{r,t}\alpha_r\alpha_tK_\infty(v_r,v_t)
 =\|m_0-m_1\|^2.
 }
\tag{5.2}
\]

Let `M=|P_1|/|P_0|` and `gamma=1-1/M`. Decompose `P_1` into its `P_0` cosets and let `q` be uniform over the nonzero quotient cosets. If `r` is uniform on `P_0`, then `r+q` is uniform on `P_1\P_0`, so
\[
 m_0-m_1
 =\gamma\,\mathbb E_{q\ne0,r\in P_0}[\Phi(v_r)-\Phi(v_{r+q})].
\tag{5.3}
\]
Jensen therefore gives the exact source-preserving upper reduction
\[
 \boxed{
 \|m_0-m_1\|^2
 \le\gamma^2\,
 \mathbb E_{q\ne0,r\in P_0}
 \int_0^\infty
 \frac{[\sin(A_r^+s)\sin(A_r^-s)-
        \sin(A_{r+q}^+s)\sin(A_{r+q}^-s)]^2}{s^3}\,ds.
 }
\tag{5.4}
\]

This replacement is deliberately **precompression and signed**. It does not invert a scalar parent through a tiny plaquette amplitude, so it avoids the codimension-normalization obstruction proved by fleet02/B16. It also uses fleet01/B16's square-first PSD mechanism rather than trying to control a linear signed finite window by its endpoint.

## 6. What remains OPEN

The diagonal Holevo theorem alone is not enough: separating `P_0` and `P_1` and applying triangle inequalities loses the cross-code cancellation needed by the authentic `16N^2` prefactor.

The remaining interface-C implication is now the concrete **coset-difference logarithmic payment**:

> Bound the right side of (5.4), with the authentic compiler weighting and without ledger reuse, at the exact normalization required to make the `16N^2` terminal square `O(J(f))`, using the genuine ordered physical flag bank plus the reserved terminal/moment/negative-information credits.

Equivalently, one must exploit how a nonzero quotient phase changes the two side amplitudes jointly, rather than paying the two code banks separately. Formula (5.4) is the next object for fleet03/B16/B18: it has the correct signed order of operations and an explicit positive integrand, while retaining the quotient geometry that scalar-parent compression destroys.

## 7. Classification and handoff

**PROVED in this run**

- the information identity (3.7) for any rank-one tight phase POVM;
- the universal Holevo diagonal bound (3.3) and influence consequence (3.4);
- its direct applicability to the authentic `P_0` and `P_1` code phase banks via fleet04/B16 distance-four orthogonality;
- the exact signed terminal mean-difference identity (5.2) and coset-coupling reduction (5.4).

**REFUTED-LEMMA**

- a universal scale-free `K <= C min-square` diagonal payment, even on the authentic `P_0=RM(1,n)` bank, by the exact Boolean one-point-defect plus quadratic-bent family.

**OPEN**

- the coset-difference payment in Section 6;
- the full interface-C compiler-to-physical-flags contraction;
- unrestricted FEI.

**consumed_peer_artifact:** `fleet01/B16/20260921T195223Z-square-first-window-gram/REPORT.md` (primary), plus the fleet02/B16 codimension-normalization barrier and fleet04/B16 local distance-four/tight-frame input named above.

**applied_to_claim:** interface C's proposed live-window/full-line scalar payment: preserve square-first window domination, refute deletion of its logarithmic factor on an exact Boolean `P_0` family, and replace it with an entropy/Holevo payment plus a signed quotient-coset transport.

**remaining_implication:** prove the authentic coset-difference logarithmic payment at the normalization needed for the `16N^2` terminal square, with no reuse of the physical-flag, moment, terminal or negative-information ledgers.

**next_recipient:** `fleet03/B16` for the logarithmic/window contraction and `fleet03/B18` for source-exact integration with fleet02's parent/mask representation.

**full_problem_change:** no full FEI closure; one plausible scale-free bridge is decisively dead and a sharper signed replacement is now explicit.
