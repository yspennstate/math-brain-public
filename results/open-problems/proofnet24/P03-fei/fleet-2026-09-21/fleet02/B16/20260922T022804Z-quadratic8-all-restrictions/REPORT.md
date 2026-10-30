# B16 — all-restriction GS8 survival on the source-bound ten-input prime gate

**Run:** `20260922T022804Z-b16-fei-r11`  
**Outcome:** `ESSENTIAL_STEP_APPLIED / FULL_FEI_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`  
**Full uniform-cube FEI:** **OPEN / NOT PROVED.**

## 0. Control correction and exact live target

The fresh owner control is revision `2026-09-22.2`. It supersedes the stale Campaign-C half-band assignment in the native B16 prompt and directs all FEI workers to the all-gate reformulation. In particular, the owner asks either for decomposable/AND extremality of the gate margin or for a source-valid falsifying gate/bias.

The newer source state already contains such a falsifier to the historical read-once extremality claim: the source-bound balanced monotone ten-input gate `G_*` from fleet03/B12 satisfies

\[
I(G_*)=\frac{257}{128},\qquad
\frac{H(G_*)}{I(G_*)-1}>6.459372281637855731.
\]

Relative to the historical read-once center \(C_0=6.4548\), its balanced quadratic-lift margin is therefore

\[
c_{G_*}>4(6.459372281637855731-6.4548)
       =0.018289126551422924.
\]

Relative to the owner's quoted sharp read-once number \(\beta(1/2)=6.4547837\), the same source certificate gives

\[
c_{G_*}>0.018354326551422924.
\]

Thus the owner's decomposable/AND-extremality branch is already falsified by newer source-valid work; I do not rerun that old finite sweep.

This run instead consumes the newest compatible replacement from fleet01/B18,
`proofnet24/P03-fei/fleet-2026-09-21/fleet01/B18/20260922T0156Z-quadratic-eight-good-split/REPORT.md`,
which gives an explicit universal candidate at constant 8 and a precise first missing implication.

## 1. Consumed peer theorem and candidate

fleet01/B18 defines

\[
\Gamma_8(p)=32p(1-p)=8V_p
\]

and, for a uniform-cube Boolean function \(F\),

\[
D_8(F):=8I(F)-H(F)-32q_F(1-q_F)
       =8\bigl(I(F)-\operatorname{Var}(F)\bigr)-H(F).
\tag{1.1}
\]

For a physical coordinate \(i\), with restrictions \(F_0,F_1\), write

\[
L_i(F):=H(F)-\frac{H(F_0)+H(F_1)}2
\]

and

\[
C_i(F):=
\bigl(I-\operatorname{Var}\bigr)(F)
-\frac{\bigl(I-\operatorname{Var}\bigr)(F_0)+
       \bigl(I-\operatorname{Var}\bigr)(F_1)}2.
\]

The exact restriction recursion is

\[
\boxed{
D_8(F)=\frac{D_8(F_0)+D_8(F_1)}2+8C_i(F)-L_i(F).
}
\tag{1.2}
\]

In fleet01/B18's notation \(C_i=4Q_i\). Hence the sufficient universal statement is

\[
\boxed{\text{GS8: every nonaffine Boolean }F
\text{ has an essential }i\text{ with }L_i(F)\le 8C_i(F).}
\tag{1.3}
\]

If GS8 holds, induction on essential arity in (1.2) gives
\(D_8(F)\ge0\), and therefore

\[
H(F)\le 8I(F)-32q_F(1-q_F)\le 8I(F)
\]

for every Boolean \(F\). Thus GS8 is a noncircular finite-constant compiler to full FEI. The two-input AND/OR class is equality for this local mechanism.

fleet01/B18 had already checked one fixed physical reveal corridor through `G_*`, using fleet04/B12's exact unbalanced-corridor theorem. The question left open for this explicit hard prime gate was whether an arbitrary restriction can enter a state with **no** GS8-good continuation.

## 2. New theorem: the complete coordinate-restriction closure of `G_*` is GS8-safe

Let a restriction state be encoded by
\(\sigma\in\{0,1,*\}^{10}\), where `*` denotes a free coordinate, and let \(G_\sigma\) be the corresponding restriction of `G_*`.

The source truth table is reconstructed from fleet03/B12's immutable generator and checked against SHA-256

`3168d8fb8ac9f5d6d7dca1d79146392aecb5eb55cc76ccb028395a9e6a62bfb4`.

### Theorem 2.1 — complete finite closure

For every one of the \(3^{10}=59{,}049\) physical coordinate restrictions \(G_\sigma\),

\[
\boxed{D_8(G_\sigma)\ge0.}
\tag{2.1}
\]

Moreover:

1. equality occurs exactly on essential arity \(0,1,2\);
2. every restriction of essential arity at least three has
   \[
   \boxed{D_8(G_\sigma)>0.261289833275743;}
   \tag{2.2}
   \]
3. every nonaffine restriction has at least one free coordinate \(i\) with
   \[
   \boxed{8C_i(G_\sigma)-L_i(G_\sigma)\ge0;}
   \tag{2.3}
   \]
4. for essential arity at least three, there is always a coordinate with the strict certified margin
   \[
   \boxed{8C_i-L_i>0.123130616218629.}
   \tag{2.4}
   \]

Thus **no coordinate restriction of the first source-bound ten-input prime obstruction is an all-bad GS8 state**.

### Equality structure

The exact state counts by essential arity are:

| essential arity | states | exact equality states |
|---:|---:|---:|
| 0 | 22,962 | 22,962 |
| 1 | 9,054 | 9,054 |
| 2 | 9,888 | 9,888 |
| 3 | 7,848 | 0 |
| 4 | 4,924 | 0 |
| 5 | 2,708 | 0 |
| 6 | 1,180 | 0 |
| 7 | 392 | 0 |
| 8 | 80 | 0 |
| 9 | 12 | 0 |
| 10 | 1 | 0 |

Every essential-arity-two state is a monotone two-input AND/OR type (up to literal/output conventions), with four equal Fourier-square masses and exact \(D_8=0\).

At the root,

\[
I(G_*)-\operatorname{Var}(G_*)=\frac{129}{128},
\]

and the rigorous entropy enclosure gives

\[
D_8(G_*)>1.552663872411848.
\]

## 3. The important obstruction: arbitrary-coordinate induction is false

The complete closure is not pointwise safe in every coordinate.

Across all

\[
10\cdot 3^9=196{,}830
\]

physical one-coordinate restriction edges, exactly **31** have rigorously negative residual

\[
8C_i-L_i<0.
\tag{3.1}
\]

The most negative edge has

\[
8C_i-L_i<-0.004950465885095.
\tag{3.2}
\]

The worst certified local ratio satisfies

\[
\boxed{\frac{L_i}{C_i}>9.214217019614940>8}
\tag{3.3}
\]

at restriction code `2222220222`, split coordinate 9 (using `2=*`).

Therefore the stronger statement “every essential coordinate is GS8-good” is false even in the restriction closure of `G_*`. A proof of GS8 must genuinely **select** a good physical coordinate or use an equivalent compensated argument. This is consistent with the current all-block/minimal-obstruction warnings and prevents a blind coordinate induction from being misread as a proof.

The first state attaining the minimum certified best-coordinate margin in essential arity at least three is `1002020222`; one certified good continuation is coordinate 3 and has

\[
8C_3-L_3>0.123130616218629.
\]

## 4. Proof/certificate method

For every restriction state, the checker:

1. reconstructs the restricted Boolean truth table exactly;
2. computes the integer Walsh transform exactly;
3. computes \(I\), variance and \(I-\operatorname{Var}\) as exact rational numbers;
4. encloses spectral entropy by rigorous rational logarithm intervals using an atanh series, treating powers of two exactly;
5. certifies (2.1) and the strict margins in (2.2);
6. checks every physical split edge, with outward-rounded rational interval bounds for \(L_i\);
7. proves there are exactly 31 negative residual edges;
8. proves that every nonaffine state has at least one residual lower bound \(\ge0\), and every state of essential arity at least three has a best residual lower bound \(>0.12\).

No floating-point value is used to decide pass/fail. This is a finite exact/interval certificate for this one source-bound gate family only.

Checker SHA-256:
`97e9173199d88f0b9dc173ea1b9e9eec4d7cdfab9b3c7ac7ddade738e5d6ca7d`

Verification-output SHA-256:
`647eba4b90ce75568cad5772149a119fb8c8827b59c45aa1a18805b643eb0b36`

## 5. Before / after / exact universal gap

**FULL-PROBLEM CHANGE: NONE.**  
Unrestricted uniform-cube FEI remains **OPEN / NOT PROVED**. No universal \(C=8\) theorem is claimed.

**MECHANISM CHANGE: YES.**

Before this run:
- the latest owner-aligned source already falsified the historical decomposable/AND extremality through the source-valid `G_*`;
- fleet01/B18 supplied the explicit \(\Gamma_8\) / GS8 compiler;
- only one fixed source-valid reveal corridor through `G_*` had been proved locally paid.

After this run:
- the **entire 59,049-state coordinate-restriction closure** of `G_*` is proved \(D_8\)-nonnegative;
- every nonaffine state in that closure has a GS8-good physical continuation;
- the stronger arbitrary-coordinate variant is decisively false by 31 exact bad edges.

The exact universal gap is therefore now clean:

\[
\boxed{
\forall\text{ Boolean }F\text{ nonaffine},\quad
\exists i\text{ essential}:\ L_i(F)\le8C_i(F).
}
\tag{5.1}
\]

Proving (5.1) universally would settle FEI with \(C=8\). A genuine Boolean function for which every essential coordinate has \(L_i>8C_i\) would refute this candidate and force a deeper adaptive/block potential. The current finite theorem does neither universally.

The stronger aggregate spectral-edge inequality `E8` proposed by fleet01/B18 remains unproved; this run does not silently substitute the finite `G_*` closure for it.

## 6. Relation to current literature

A current primary-source check still finds unrestricted FEI open. Potapov (18 September 2026) proves FEI for plateaued functions, with sharp class constant 4, and for partially bent functions, with sharp class constant 2. González–MacManus–Pereyra (29 May 2026) prove further structured/stopping-tree cases and explicitly retain a missing universal restriction inequality. Neither result supplies GS8 or a universal all-gate potential.

No novelty or publication-priority claim is made for the finite theorem or the quadratic-eight formulation.

## 7. Sources actually consumed

- fleet01/B18, `20260922T0156Z-quadratic-eight-good-split/REPORT.md`, report blob `d4c76a91adca43e82b88ab50b16136426b60f4bb`;
- fleet04/B12, `20260922T014248Z-unbalanced-corridor-game/REPORT.md`;
- fleet03/B12, `20260922T004418Z-arity10-gate-refutation/` source/checker for the exact ten-input truth table;
- fleet02/B18, `20260922T0117Z-balanced-restriction-minimal-gate/REPORT.md`;
- fleet04/B18, `20260922T021124Z-all-block-safe-split-barrier/REPORT.md`;
- fleet02/B17, `20260921T124438Z-support-deficit-balanced-equivalence/REPORT.md`.

These sources are used at their stated scopes; no finite/subclass result is promoted to full FEI.
