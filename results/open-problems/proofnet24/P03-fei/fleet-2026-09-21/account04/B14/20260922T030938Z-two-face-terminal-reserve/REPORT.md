# B14 — exact two-face terminal reserve for the fixed all-gate FEI candidate

**Classification:** `ESSENTIAL_STEP_APPLIED / EXACT_TERMINAL_DECOMPOSITION`.  
**Full uniform-cube FEI:** **OPEN / NOT PROVED.**  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

## 1. Live target and exact source-to-next-arrow use

Fresh owner control revision `2026-09-22.2` supersedes the older posterior-crossing-only wording and directs every FEI worker to the all-gate formulation. I therefore keep the restriction machinery as a compiler for the current gate target rather than reopening the known-false prescribed-coordinate payment claim.

The current all-gate theorem says that a symmetric nonnegative potential `Gamma` closes FEI if

\[
D_\Gamma(G;p):=
\sum_i \frac{\operatorname{It}_i(G;p)}{V_{p_i}}
       \bigl(\Gamma(p_i)+h_2(V_{p_i})\bigr)
 -\Gamma(p_{\rm out})-\widetilde H_G(p)\ge0
\tag{1.1}
\]
for every Boolean gate and every interior product bias. The exact source is
`proofnet24/P03-fei/continuations/2026-09-22-gate-reformulation/REPORT.md`.

I consume two account01/B18 results source-exactly.

1. `account01/B18/20260921T1856Z-curvature-refunded-crossing/REPORT.md`, blob
   `ef9f471c019a7d81e9864fd457a0e4bae9da890d`, proves for a median-centered physical block
   \[
   \Delta_A\mathcal F
   \le B_A-\sum_{j\notin A}\mathfrak j'(p_j)c_j(A),
   \qquad
   D_A^{\rm fold}=\mathcal J-\mathbb E\mathcal J_{\rm child}=I_A+C_A.
   \tag{1.2}
   \]
   Its exact lesson needed here is that a source-valid restriction compiler must retain the nonmodular survivor/orientation refund; dropping it is not licensed. Equation (3.5) below is the all-gate two-face analogue: the terminal reserve splits into ordinary mixed curvature plus an explicit checkerboard/orientation surcharge. Thus this source is used to determine what may not be discarded, not to assert a prescribed-coordinate bound.

2. The newer all-gate integration result
   `account01/B18/20260922T0222Z-shared-graft-tail/REPORT.md` fixes one stable candidate
   \[
   C_*=6.5218512,
   \qquad
   a_*=4(C_*-C_0)=0.2682048,
   \qquad C_0=6.4548,
   \tag{1.3}
   \]
   \[
   \Gamma_*(p)=\Gamma_{\rm RO}(p)+a_*p(1-p).
   \tag{1.4}
   \]
   Its remaining universal implication is `LIMIT-PRIME-GATE-LIFT-v1`: prove
   `D_{Gamma_*}(P;p)>=0` for every composition-prime Boolean gate and product bias.

The known addressing obstruction to every-coordinate payment is preserved. The exact folded block drift (1.2) is also preserved. Neither is weakened by the result below.

## 2. A complete two-variable terminal table

Let `g:{0,1}^2->{-1,1}` be any two-variable Boolean gate, fed unbiased independent inputs. Then (1.1) becomes

\[
D_*(g)=C_* I(g)-H(g)-\Gamma_*(q_g),
\tag{2.1}
\]
where `q_g=Pr[g=-1]`.

Up to input/output negations and interchange, there are only four terminal types.

* constant: `I=H=0`, `q in {0,1}`, hence `D_*=0`;
* unary/character: `I=1`, `H=0`, `q=1/2`, hence `D_*=0`;
* AND/OR type (one or three negative vertices): `I=1`, `H=2`, `q in {1/4,3/4}`;
* XOR/XNOR checkerboard: `I=2`, `H=0`, `q=1/2`.

The read-once potential is tight on the unbiased two-input AND/OR atom, so

\[
\Gamma_{\rm RO}(1/4)=\Gamma_{\rm RO}(3/4)=C_0-2.
\tag{2.2}
\]

Consequently

\[
D_*(\mathrm{AND/OR})
=C_*-2-\left(C_0-2+\frac{3a_*}{16}\right)
=\frac{a_*}{16}
=\frac{C_*-C_0}{4},
\tag{2.3}
\]
while

\[
D_*(\mathrm{XOR/XNOR})=C_*.
\tag{2.4}
\]

This table is exact.

## 3. Exact physical two-face reserve identity

For distinct physical coordinates `i,j`, freeze all other coordinates to a uniform assignment `z`, and write the resulting face values as

\[
f_{00},f_{10},f_{01},f_{11}.
\]

Use the normalized mixed derivative

\[
D_iD_j f(z)=\frac{f_{00}-f_{10}-f_{01}+f_{11}}4.
\tag{3.1}
\]

Let `X_{ij}` be the probability, over the frozen outside coordinates, that this two-face is an XOR/XNOR checkerboard. On a constant or unary face `(D_iD_j f)^2=0`; on an AND/OR face it equals `1/4`; on an XOR/XNOR face it equals `1`.

Comparing these three values with (2.3)--(2.4) proves pointwise, face by face,

\[
\boxed{
D_*(f_{ij\mid z})
=(C_*-C_0)(D_iD_jf(z))^2
+C_0\,1_{\{\mathrm{XOR/XNOR}\}}(z).
}
\tag{3.2}
\]

Averaging over `z` gives the exact pair identity

\[
\boxed{
\mathbb E_z D_*(f_{ij\mid z})
=(C_*-C_0)\,\|D_iD_jf\|_2^2+C_0X_{ij}.
}
\tag{3.3}
\]

This is the promised restriction/orientation split. The first term is unsigned mixed curvature. The second is a positive orientation/checkerboard term and cannot be dropped in a general Boolean argument. This mirrors the reason the older curvature-refund route had to keep the nonmodular crossing/orientation contribution.

Now average over all unordered pairs. Parseval gives

\[
\sum_{i<j}\|D_iD_j f\|_2^2
=\sum_S { |S|\choose2}\widehat f(S)^2.
\tag{3.4}
\]

Hence, with `N_2=binom(n,2)` and `X(f)=sum_{i<j}X_{ij}`,

\[
\boxed{
\frac1{N_2}\sum_{i<j}\mathbb E_zD_*(f_{ij\mid z})
=
\frac{C_*-C_0}{N_2}
\sum_S {|S|\choose2}\widehat f(S)^2
+
\frac{C_0}{N_2}X(f).
}
\tag{3.5}
\]

Equation (3.5) is universal for uniform-cube Boolean functions; no monotonicity, balance, or critical-core hypothesis is needed. If `f` is monotone, every physical two-face is monotone and therefore `X(f)=0`, so the terminal reserve is exactly a normalized second-factorial spectral moment.

## 4. The explicit prime ten-input obstruction has a large paid two-face corridor

I apply (3.5) to the exact balanced monotone ten-input gate `G_10` from
`account03/B12/20260922T004418Z-arity10-gate-refutation/REPORT.md`, witness SHA-256
`3168d8fb8ac9f5d6d7dca1d79146392aecb5eb55cc76ccb028395a9e6a62bfb4`.
It has

\[
I(G_{10})=\frac{257}{128},
\qquad
6.509836127588151479<H(G_{10})<6.509836127588151480.
\tag{4.1}
\]

The exact checker in this run enumerates all

\[
{10\choose2}2^8=11520
\]
physical two-faces. Their types are

\[
6894\ \text{constant},\qquad
2882\ \text{unary},\qquad
1744\ \text{AND/OR},\qquad
0\ \text{XOR/XNOR}.
\tag{4.2}
\]

Thus

\[
\sum_{i<j}\|D_iD_jG_{10}\|_2^2
=\frac{1744}{4\cdot256}
=\boxed{\frac{109}{64}},
\tag{4.3}
\]

and (3.5) gives the exact mean terminal reserve

\[
\boxed{
T_2(G_{10})
=(C_*-C_0)\frac{109/64}{45}
=\frac{1522621}{600000000}
=0.002537701666\ldots .
}
\tag{4.4}
\]

At the balanced root,

\[
D_*(G_{10})=C_*\frac{129}{128}-H(G_{10}),
\]
so (4.1) yields

\[
0.062967034911848520
<D_*(G_{10})
<0.062967034911848521.
\tag{4.5}
\]

Therefore the root-minus-mean-two-face reserve is rigorously

\[
\boxed{
0.0604293332451818533\ldots
< D_*(G_{10})-T_2(G_{10})
<0.0604293332451818544\ldots .
}
\tag{4.6}
\]

So the source-valid prime obstruction is not merely positive at the lifted root: it has a substantial exact physical corridor all the way down to uniformly chosen two-coordinate terminal faces under the same `Gamma_*`.

This is not a proof that every prime gate has such a corridor.

## 5. Exact new next arrow

The current universal missing statement remains `LIMIT-PRIME-GATE-LIFT-v1`. Equation (3.5) turns one restriction version of it into a precise, falsifiable subtarget on the unbiased slice:

> For a balanced composition-prime gate `P`, find a physical pair `i,j` (equivalently, a reveal block leaving that pair unresolved) for which
> \[
> D_{\Gamma_*}(P;1/2)
> \ge \mathbb E_z D_{\Gamma_*}(P_{ij\mid z};1/2),
> \tag{5.1}
> \]
> or prove a stronger averaged version.

The right-hand side is no longer mysterious. Its exact all-pairs average is (3.5): normalized second-factorial Fourier mass plus the checkerboard term `C_0 X(f)`. Thus a proof of (5.1) can now target a concrete mixed-curvature/orientation bank. Conversely, a prime balanced gate for which every pair violates (5.1) would rigorously falsify this two-face restriction compiler while leaving FEI itself open unless its root defect is negative.

For monotone prime gates the checkerboard surcharge vanishes, so the target reduces exactly to the second-factorial spectral moment. For general gates the positive `C_0 X(f)` term must be retained; deleting it would repeat a known unsigned-curvature mistake.

This is a genuinely different mechanism from the earlier posterior-threshold selectors: it terminates on the complete two-variable gate classification and prices the continuation exactly under the one fixed `Gamma_*`.

## 6. Verification and limits

`check_two_face_terminal_reserve.py` verifies the terminal identity on all 16 two-variable truth tables, reconstructs the source-exact `G_10`, enumerates all 11,520 of its physical two-faces, checks (4.2)--(4.4), and confirms the inherited witness hash.

Executed checker SHA-256:
`ff22e7f6db31e62ffeafbe911f7c10dc97fdee33cacbd816eaa82f9ae44d179f`.

Captured output SHA-256:
`0c6d0fede56cc6b2978d053f5ae0c6d39c572b9f9ac20eaa599272626c4b6d10`.

The checker is evidence for the finite identities only; Sections 2--3 are analytic proofs. No novelty/publication-priority claim is made. Full FEI remains **OPEN / NOT PROVED**.
