# B14 — common-Gamma terminal-atom subtraction closes the explicit G10 stopping corridor

**Classification:** `ESSENTIAL_STEP_APPLIED / FINITE_OBSTRUCTION_CLOSED`.  
**Full uniform-cube FEI:** **OPEN / NOT PROVED.**  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

## 1. Live target and exact sources consumed

Fresh owner control revision `2026-09-22.2` supersedes the older posterior-crossing wording and converges every FEI worker on the all-gate inequality. The newest proof-integration result I actually consume is

`proofnet24/P03-fei/fleet-2026-09-21/fleet01/B18/20260922T0222Z-shared-graft-tail/REPORT.md`.

It proves that the recursive shared-graft lower-bound family has a finite limiting cap and fixes the stable candidate

\[
C_*=6.5218512,\qquad
a_*=4(C_*-6.4548)=0.2682048,
\]
\[
\Gamma_*(p)=\Gamma_{\rm RO}(p)+a_*p(1-p).
\tag{1.1}
\]

The exact remaining universal implication is `LIMIT-PRIME-GATE-LIFT-v1`: prove
\(D_{\Gamma_*}(P;p)\ge0\) for every composition-prime Boolean gate and every interior product bias.

I also consume three restriction results source-exactly.

1. `fleet04/B12/20260922T0254Z-and-atom-stopping/REPORT.md`, blob
   `8a35d08850c8bf38a36c58af4ee3dcd670fa0de9`.  For the exact prime ten-input gate
   \(G_{10}\), under physical reveal order \(0,1,\ldots,9\), stopping at the first affine
   state or two-essential-input AND/OR atom gives
   \[
   \Pr(\mathrm{AND/OR})=\frac{29}{64},\qquad
   \mathbb E P(G_\sigma)=\frac{29}{1024},
   \]
   \[
   P(G_{10})=\frac{129}{512},\qquad
   Q_{\rm block}=P(G_{10})-\mathbb E P(G_\sigma)=\frac{229}{1024}.
   \tag{1.2}
   \]
   Every nonaffine terminal is a uniform two-input AND/OR atom with
   \(P=1/16\), \(H=2\), output bias \(1/4\) or \(3/4\).

2. `fleet02/B16/20260922T010120Z-gate-margin-restriction-martingale/REPORT.md`,
   blob `335d6ffa58cae84c7b47e742a250a20d2e2bddd4`.  It proves the exact signed stopping
   ledger and, for a quadratic lift, exact additivity in Poincare currency.

3. `fleet03/B17/20260922T014022Z-prime-dyadic-barrier/REPORT.md`, blob
   `495aa3932db915878b3c3f379d946dbd89ccba4e`.  It records that the read-once
   potential is exact on the dyadic AND/OR chain.  In particular the uniform
   two-input AND/OR terminals above have
   \[
   D_{\Gamma_{\rm RO}}=0.
   \tag{1.3}
   \]

The inherited exact G10 entropy enclosure is
\[
6.509836127588151479
<
H(G_{10})
<
6.509836127588151480,
\tag{1.4}
\]
with \(I(G_{10})=257/128\).

The known addressing obstruction and the false prescribed-coordinate erasure bound are not altered or used.

## 2. General terminal-tight subtraction lemma

Let \(\Gamma_a=\Gamma_0+a\phi\), where \(\phi(p)=p(1-p)\), so that the gate
defect satisfies
\[
D_a(G)=D_0(G)+aP(G)
\tag{2.1}
\]
with the same Poincare currency \(P\) as in the restriction martingale.

Let \(\sigma\) be any bounded physical stopping rule.  Define
\[
Q_\sigma=P(G)-\mathbb E P(G_\sigma).
\]
Then identically,
\[
\boxed{
D_a(G)-\mathbb E D_a(G_\sigma)
=
\bigl[D_0(G)-\mathbb E D_0(G_\sigma)\bigr]
+aQ_\sigma.
}
\tag{2.2}
\]

This is simply (2.1) at the root and terminals followed by subtraction; it is
the block form of the exact B16 signed ledger.  In particular, if every
nonaffine stopping terminal is **tight** for \(\Gamma_0\), then
\[
\boxed{
D^{\rm block}_a
=
D_0(G)+aQ_\sigma.
}
\tag{2.3}
\]
Thus the common-potential terminal-subtraction problem reduces to one scalar
threshold
\[
\boxed{
a\ge a_{\rm block}:=
\frac{-D_0(G)}{Q_\sigma}
}
\tag{2.4}
\]
whenever \(D_0(G)<0\).

No local residual is discarded and no terminal slack is counted twice.

## 3. Apply the lemma to the exact G10 corridor

Take \(\Gamma_0=\Gamma_{\rm RO}\), whose center is
\[
C_0=\Gamma_{\rm RO}(1/2)=6.4548.
\]
Because \(G_{10}\) is balanced and all root inputs are uniform,
\[
D_{\rm RO}(G_{10})
=C_0\left(I(G_{10})-1\right)-H(G_{10})
=C_0\frac{129}{128}-H(G_{10}).
\tag{3.1}
\]
Using (1.4),
\[
\boxed{
-0.004608002588151480
<
D_{\rm RO}(G_{10})
<
-0.004608002588151479.
}
\tag{3.2}
\]

By (1.3), every nonaffine terminal in the B12 stopping tree is exactly
read-once-tight, while affine terminals have zero continuation defect.
Therefore (2.3) applies with the exact block currency \(229/1024\).

The **necessary and sufficient lift for this fixed stopped block** is therefore
\[
a_{\rm G10,block}
=
\frac{H(G_{10})-C_0(129/128)}{229/1024}.
\tag{3.3}
\]
The inherited entropy interval gives the rigorous enclosure
\[
\boxed{
0.020605216813393513082969432314
<
a_{\rm G10,block}
<
0.020605216813393517554585152838.
}
\tag{3.4}
\]

Equivalently the center needed by this particular common-Gamma stopped proof is
\[
C_{\rm G10,block}=C_0+\frac14a_{\rm G10,block},
\]
hence
\[
\boxed{
6.459951304203348378270742358079
<
C_{\rm G10,block}
<
6.459951304203348379388646288210.
}
\tag{3.5}
\]

This is slightly larger than the root balanced ratio
\(H/(I-1)>6.45937228\): retaining the AND/OR terminal continuation costs a real,
quantified amount.  The calculation is therefore not the tautology “the root
already has positive slack at a larger center.”

## 4. The stable LIMIT candidate pays the whole physical block with large strict slack

For the stable candidate (1.1),
\[
a_*=0.2682048
>
13\,a_{\rm G10,block}.
\tag{4.1}
\]
Substituting into (2.3) gives
\[
\boxed{
0.055371391161848520
<
D^{\rm block}_{\Gamma_*}
<
0.055371391161848521.
}
\tag{4.2}
\]

There is an independent root-minus-terminal check.  The root stable slack is
\[
D_{\Gamma_*}(G_{10})
=C_*\frac{129}{128}-H(G_{10})
>
0.062967034911848520.
\tag{4.3}
\]
Each uniform AND/OR terminal has
\[
D_{\Gamma_*}=a_*P=\frac{a_*}{16},
\]
so its expected continuation slack is exactly
\[
\frac{29}{64}\frac{a_*}{16}
=
\boxed{0.00759564375}.
\tag{4.4}
\]
Subtracting (4.4) from (4.3) reproduces (4.2) exactly.

Hence the `terminal-atom subtraction problem` isolated by fleet04/B12 is
**closed for the source-valid G10 uniform stopping corridor using one and the
same candidate \(\Gamma_*\) at the root, block, and terminals.**

This is a realizable physical stopping policy; there is no prescribed-coordinate
payment claim and no reuse of terminal Poincare currency.

## 5. What this does and does not prove

### Proved here

For the exact source-valid composition-prime ten-input obstruction \(G_{10}\)
at uniform input bias, the stable `LIMIT-PRIME-GATE-LIFT-v1` candidate is
compatible with the explicit physical restriction stopping proof.  The
preterminal block is strictly paid, and every nonaffine continuation is an
already-certified two-input AND/OR atom under the same \(\Gamma_*\).

More generally, equation (2.4) is an exact compiler for any stopping tree whose
terminals are tight for the base potential: one needs only the root base defect
and consumed Poincare currency.

### Not proved

This does **not** prove `LIMIT-PRIME-GATE-LIFT-v1` for every prime gate or every
bias vector.  It does not show that every prime obstruction admits a stopping
tree into read-once-tight atoms with an influence-independent positive fraction
of its Poincare currency.  It also does not evaluate the unavailable
off-center numerical read-once-potential binary on arbitrary non-dyadic
biases.

Full FEI remains **OPEN / NOT PROVED**.

## 6. Exact source-to-next-arrow use

The newest fleet01/B18 tail theorem provides a stable fixed candidate
\(\Gamma_*\), so this run can finally answer the B12 question without moving the
center again.  The B12 atom tree supplies exact terminal types and \(Q_{\rm block}\);
the B16 martingale turns terminal subtraction into a signed block identity; and
the B17 dyadic theorem makes the terminal base defects exactly zero.

The next universal arrow is now:

> prove that every composition-prime gate violating or nearly violating
> \(\Gamma_*\) admits a realizable physical stopping rule whose terminals are
> \(\Gamma_{\rm RO}\)-safe and for which
> \[
> -\bigl[D_{\rm RO}(G)-\mathbb E D_{\rm RO}(G_\sigma)\bigr]
> \le a_*\,[P(G)-\mathbb E P(G_\sigma)].
> \]
>
> A counterexample to this exact stopped-block inequality, with a source-valid
> gate and bias vector, would instead falsify the restriction compiler.

This is the same fixed `LIMIT-PRIME-GATE-LIFT-v1` target, not a new FEI route.

## 7. Verification

`CHECKER.py` performs only exact rational arithmetic on the cited certified
interval and stopping data.  It checks the two independent evaluations of the
common-\(\Gamma_*\) block residual and all strict inequalities above.

Executed checker SHA-256:
`93c776230e016c9eaf06adf9e4a9947318a5fbae0f76125aab61d17c6c792610`.

Captured output SHA-256:
`026e09b48f8149a8dc65d697987eccd67ad832beeafb23cae1de90c962f02f96`.

No novelty or publication-priority claim is made.
