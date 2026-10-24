# B16 FEI interface C — finite-window amplitude transport with an original-coordinate J sink

**Run:** `20260921T222504Z-b16-krawtchouk-refund`  
**Scope:** account03/B16, joint FEI interface C  
**Execution:** **WITHOUT_VERIFIED_BRAIN**  
**Full unrestricted FEI:** **OPEN / NOT PROVED**  
**Claim level:** exact finite-resolvent-window transport identities and a local dimension-free-in-window contraction. The remaining authentic parent/multiplicity aggregation is OPEN.

## 0. Route change and peer result consumed

The previous B16 runs had already isolated a signed square-root resolvent, a diagonal entropy/polarization payment, and an ordered physical flag bank, but the universal compiler-to-flag implication remained unchanged. This run therefore changes method.

**consumed_peer_artifact:** account04/B16, `proofnet24/P03-fei/fleet-2026-09-21/account04/B16/20260921T213921Z-finite-resolvent-rkhs-refund/REPORT.md`.

That report proves for
\[
F_T(x)=x\log(1+T/x),\qquad
K_T(u,v)=F_T((u+v)^2)-F_T((u-v)^2)
\]
that `K_T` is the authentic positive sine-RKHS kernel for the finite small-resolvent source, and that the compiler must retain the Boolean/comparator subtraction, the high-resolvent R16 companion, the outside-live-window term, all R32 signs, and the terminal subtraction before final positivity.

**applied_to_claim:** instead of trying to make an authentic gate/window nonnegative (now refuted), pull the finite-resolvent logarithm back to the *signed amplitude coordinate*. The logarithmic derivative then has a bounded oriented transport density. This yields an explicit local compiler-window contraction while leaving the high-resolvent/outside-window/negative-credit/terminal ledger untouched.

The same-account B17 report `20260921T220508Z-resolvent-window-sign/REPORT.md` is used only as a regression adversary: it proves an actual Boolean signed gate whose finite-resolvent source changes sign. The theorem below must survive that example without imposing false positivity.

## 1. Finite resolvent windows

For `0 <= A < B < infinity`, define
\[
F_{[A,B]}(x)=\int_A^B \frac{x}{x+t}\,dt=F_B(x)-F_A(x),
\tag{1.1}
\]
where `F_0=0`, and
\[
K_{[A,B]}(u,v)
=F_{[A,B]}((u+v)^2)-F_{[A,B]}((u-v)^2).
\tag{1.2}
\]
By account04/B16 this is exactly the positive scalar RKHS associated with the finite resolvent window, but the authentic compiler evaluates a signed Boolean-minus-comparator difference of such kernels.

Put
\[
G_{[A,B]}(r)=F_{[A,B]}(r^2).
\tag{1.3}
\]
The key observation is that the singular logarithm in `F_T'(x)` disappears after the square-root/amplitude pullback.

## 2. PROVED — bounded oriented amplitude density

### Theorem 2.1 — `P03-B16-FINITE-WINDOW-AMPLITUDE-TRANSPORT`

For every real `r`,
\[
G'_{[A,B]}(r)
=2r\int_A^B\frac{t}{(r^2+t)^2}\,dt,
\tag{2.1}
\]
with the continuous value `G'_{[A,B]}(0)=0`. In particular the density has the **orientation sign**
\[
\operatorname{sgn}G'_{[A,B]}(r)=\operatorname{sgn}r
\quad(r\ne0),
\tag{2.2}
\]
and the uniform bound
\[
\boxed{
|G'_{[A,B]}(r)|\le 2(\sqrt B-\sqrt A).
}
\tag{2.3}
\]
For the low window `[0,T]`,
\[
G_T'(r)=2r\left[\log\left(1+\frac{T}{r^2}\right)-\frac{T}{r^2+T}\right],
\tag{2.4}
\]
where the right side tends to zero at `r=0`, and
\[
|G_T'(r)|\le2\sqrt T.
\tag{2.5}
\]

### Proof

Differentiate (1.1) under the finite integral and use `x=r^2`:
\[
\frac{d}{dr}\frac{r^2}{r^2+t}=\frac{2rt}{(r^2+t)^2},
\]
which gives (2.1). The sign is immediate.

For `t>0`, write `q=|r|/\sqrt t`. Then
\[
\frac{2|r|t}{(r^2+t)^2}
=\frac1{\sqrt t}\frac{2q}{(1+q^2)^2}
\le\frac1{\sqrt t},
\]
because `2q <= 1+q^2 <= (1+q^2)^2`. Integrating from `A` to `B` proves (2.3). Equation (2.4) follows by differentiating `F_T`, and (2.5) is the case `A=0`, `B=T`.

The important structural point is that the logarithmic singularity of the scalar resolvent is **not** a singular transport coefficient in signed amplitude coordinates: the multiplier `r log(T/r^2)` vanishes at the origin.

## 3. PROVED — exact signed compiler polarization path

At one authentic gate and one code mask `m`, let `(u_f,v_f)` be the two signed cell amplitudes of the Boolean phase and `(u_0,v_0)` those of the comparator, as in account04/B16. Define
\[
\delta u=u_f-u_0,\qquad \delta v=v_f-v_0.
\tag{3.1}
\]
Then, exactly,
\[
\boxed{
\begin{aligned}
&K_{[A,B]}(u_f,v_f)-K_{[A,B]}(u_0,v_0)\\
&=\int_{u_0+v_0}^{u_f+v_f}G'_{[A,B]}(r)\,dr
 -\int_{u_0-v_0}^{u_f-v_f}G'_{[A,B]}(r)\,dr.
\end{aligned}}
\tag{3.2}
\]

This is the requested logarithmic/polarization transfer **before** positivity: both interval orientations remain visible, and the Boolean/comparator subtraction is not replaced by total variation. Consequently a negative authentic gate/window remains negative if the two oriented transports dictate it.

As an envelope to be applied only after the co-located signed companions have been inserted, (2.3) gives
\[
\boxed{
|\Delta K_{[A,B]}|
\le4(\sqrt B-\sqrt A)\max\{|\delta u|,|\delta v|\},
}
\tag{3.3}
\]
and hence
\[
\boxed{
|\Delta K_{[A,B]}|^2
\le16(\sqrt B-\sqrt A)^2(\delta u^2+\delta v^2).
}
\tag{3.4}
\]
No claim is made that the raw signed gate is itself a positive debit.

## 4. PROVED — exact dual-code orthogonality of the phase increments

Let `M` be the authentic pre-gate code containing `RM(1,n)`, `D=M^perp`, `N=2^n`, and gate face `Q`. After the one legitimate minimizing-character gauge, let `F` be the set on which the gauged Boolean phase equals `-1`, with the global sign chosen so `|F|<=N/2`.

The phase increments are
\[
\delta u(m)=-\frac2N\sum_{x\in F\setminus Q}(-1)^{m_x},
\qquad
\delta v(m)=-\frac2N\sum_{x\in F\cap Q}(-1)^{m_x}.
\tag{4.1}
\]
Because `M` contains `RM(1,n)`, the dual `D` has no nonzero word of weight two. Therefore code averaging kills every distinct pair and gives the exact identities
\[
\boxed{
\mathbb E_{m\in M}\delta u(m)^2=\frac{4|F\setminus Q|}{N^2},
\quad
\mathbb E_{m\in M}\delta v(m)^2=\frac{4|F\cap Q|}{N^2},
\quad
\mathbb E_m\delta u\,\delta v=0.
}
\tag{4.2}
\]
In particular
\[
\boxed{
\mathbb E_m(\delta u^2+\delta v^2)=\frac{4|F|}{N^2}.
}
\tag{4.3}
\]
This retains the full code multiplicity; no representative relation or reconstructed positive parent law is chosen.

In the minimizing-character gauge, account03/B18 gives `I(g)=J(f)`. The cube edge-boundary inequality for `|F|<=N/2` gives `2|F|/N <= I(g)`, hence
\[
\boxed{
\mathbb E_m(\delta u^2+\delta v^2)\le\frac{2J(f)}{N}.
}
\tag{4.4}
\]
Combining (3.4) and (4.4) yields the explicit local window estimate
\[
\boxed{
\mathbb E_m|\Delta K_{[A,B]}|^2
\le
\frac{32(\sqrt B-\sqrt A)^2}{N}\,J(f).
}
\tag{4.5}
\]
For the actual small-resolvent cutoff `[0,2]`,
\[
\boxed{
\mathbb E_m|\Delta K_{[0,2]}|^2\le\frac{64}{N}J(f).
}
\tag{4.6}
\]

Equation (4.5) is a real original-coordinate sink for the *finite-window phase increment*. It does not yet prove that the authentic doubled-parent coefficients aggregate these local gates with the required normalization; that is the remaining interface-C implication.

## 5. Signed ledgers preserved, not respent

The use of (3.3)--(4.6) is deliberately constrained.

1. The exact identity (3.2), not the absolute-value envelope, is the primary transport formula.
2. Account04/B16's co-located high-resolvent term `H_j` is not spent in (4.5). It remains the signed complement to the low window.
3. The outside-live-Borel-window integral in account04 equation (8.5) is untouched.
4. `2 mod 4` R32 shells remain negative credits; no relationwise absolute value is taken.
5. R16 moment refunds are untouched.
6. The terminal `C_0-D_d` subtraction is untouched.
7. The account03/B18 orientation term `o_i` in `kappa_i=p_i+4o_i` is not dropped. Equation (4.5) is a preliminary original-coordinate amplitude sink, not a replacement of the final oriented flag bank.

Thus the new bound is compatible with the positive-current no-go: it is not a claim that the entire raw positive compiler current is `O(J)`.

## 6. Attempted refutation on the exact B17 sign-changing Boolean gate

The account03/B17 adversary uses `N=16`, `M=RM(1,4)`,
\[
Q=\{0,3,4,7,9,10,12,15\},
\qquad
F=\{0,1,3,5,10,12,14,15\}.
\]
It has a positive quartic first separator but a negative finite-resolvent source for every finite endpoint in the reported primitive.

Direct enumeration of all 32 affine masks gives
\[
\mathbb E_m(\delta u^2+\delta v^2)=\frac18
=\frac{4|F|}{N^2},
\]
exactly as (4.3) predicts. For `T=1/8,1/4,1/2,2`, the mean signed gate differences are respectively approximately
\[
-0.02534157,\ -0.02789294,\ -0.02534157,\ -0.01254192,
\]
so the new transport identity does **not** falsely make the gate positive. At the same time every one of the 128 pointwise gate checks satisfies (3.4); the largest observed ratio of left side to the right side was about `0.109412`.

**REFUTED / DEAD ROUTE:** promoting the signed finite gate to a nonnegative debit before the high/outside-window/negative-credit companion. The B17 example remains a counterexample.

**SURVIVED:** the oriented amplitude-path identity and the `J/N` second-moment envelope.

## 7. Verification

`check_b16_amplitude_transport.py` is standard-library only. Its archived output reports:

- 4,320 dynamic-range derivative checks;
- 28 finite-window derivative checks;
- 128 exact-gate pointwise square checks on the B17 Boolean witness;
- exact agreement of the B17 finite-window average with its reported primitive;
- exact `RM(1,4)` phase-increment second moment `1/8`.

Source SHA-256: `520641702106e8514156bbd4ddea7258737ba294b0a74f02c024edc2e671414f`.  
Output SHA-256: `943f112a540aab0b0a9bbb0b73e593c326525c224fa923b16e2d78903a20da33`.

## 8. Classification and handoff

**PROVED:** Theorems/identities (2.1)--(2.5), (3.2)--(3.4), (4.2)--(4.6).

**REFUTED:** any use of these identities to infer positivity of the authentic finite gate/window before the signed companions are inserted.

**CONDITIONAL:** if the authentic parent/mask splitter can aggregate the compensated residual local gates with no loss beyond the existing first-separation multiplicity, (4.5) provides the needed finite-window `J` sink without a logarithmic singularity.

**remaining_implication:** insert the account04 co-located high-resolvent and outside-live-window companions into the account03 square-root-resolvent field, retain the negative R32 and terminal terms, and prove that the resulting authentic parent coefficients aggregate the local `N^{-1}` estimate (4.5) without recreating an `N`, codimension, or total-variation loss. Only after that step should the residual square be sent to account03/B18's oriented `kappa` bank.

**next_recipient:** `account03/B18` for the authentic parent/mask-to-oriented-flag aggregation, with `account04/B16` as the source-side finite-window/high-resolvent parent.

**Full FEI:** **OPEN / NOT PROVED**.
