# B17 FEI new proof mechanism: signed diagonal comparison for shared-variable composition

**Date:** 2026-09-21  
**Status of full FEI:** **OPEN / NOT PROVED**  
**Run status:** `WITHOUT_VERIFIED_BRAIN` — no genuine brain retrieval/context was available or used in this mathematical derivation.  
**Role:** fleet03 / B17, FEI new proof mechanisms.  
**Fresh mathematical source:** `master` at `e7217b10f3760736adfb1fa0542acbfb1f9c85ac`.

## What changed in this run

I did **not** audit the read-once certificate or continue the restriction-potential route. I used three different fleet moves:

1. **Move 1 — change the category:** replace a shared-variable composition by a disjoint Boolean function followed by a *diagonal identification* of two coordinates.
2. **Move 2 — attack the negation first:** search for exact Boolean functions where identifying two variables makes the FEI ratio worse, including when both possible relative signs are tried.
3. **Move 25 — count the same thing twice:** encode the original spectral sample and the randomly signed diagonal spectral sample by the same pair-cell variable. This gives an exact entropy bookkeeping identity rather than an inequality guessed from numerics.

The named universal obstruction is the failure of the disjoint-block composition theorem to survive **variable reuse**. The new calculation isolates this failure into (i) a two-coordinate spectral collision mass and (ii) a signed phase/interference term.

Tracked quantity for this route: the fixed-sign diagonal comparison had no exact decomposition before this run; after the run its FEI defect is an exact parent term plus a collision/payment term plus **one scalar sign-skew remainder**.

## 1. Setup

Let \(F:\{-1,1\}^n\to\{-1,1\}\), and fix distinct coordinates \(i,j\). For
\(\sigma\in\{-1,1\}\), define the signed diagonal restriction
\[
 g_\sigma(x_{\neq j})=F(x_1,\ldots,x_j=\sigma x_i,\ldots,x_n).
\]
For every \(T\subseteq[n]\setminus\{i,j\}\), write
\[
 a_T=\widehat F(T),\quad
 b_T=\widehat F(T\cup\{i\}),\quad
 c_T=\widehat F(T\cup\{j\}),\quad
 d_T=\widehat F(T\cup\{i,j\}).
\]
Direct substitution of \(x_j=\sigma x_i\) gives the exact pairwise Hadamard rule
\[
 \widehat g_\sigma(T)=a_T+\sigma d_T,\qquad
 \widehat g_\sigma(T\cup\{i\})=b_T+\sigma c_T. \tag{1}
\]
This is the basic comparison map.

Define
\[
 W_{ij}(F)=\sum_T d_T^2
 =\Pr_{S\sim\widehat F^2}[i,j\in S].
\]

## 2. PROVED: exact influence loss under random signed identification

Averaging (1) over \(\sigma=\pm1\),
\[
 \frac{(u+v)^2+(u-v)^2}{2}=u^2+v^2.
\]
Every residual-coordinate contribution is therefore preserved on average. The two old memberships \(i,j\) contribute
\(b_T^2+c_T^2+2d_T^2\) to \(I(F)\), whereas the collapsed coordinate contributes
\(b_T^2+c_T^2\) on average. Hence

\[
 \boxed{\frac{I(g_+)+I(g_-)}2=I(F)-2W_{ij}(F).} \tag{2}
\]

This is an identity for every Boolean \(F\), with no regularity or balance hypothesis.

## 3. PROVED: exact entropy bookkeeping and a sharp two-bit sandwich

Partition the Fourier coefficients into the two-member cells
\[
 (a_T,d_T)\quad\text{and}\quad(b_T,c_T).
\]
Let \(R\) denote the cell and let \(B\in\{0,1\}\) denote which member of the original pair was sampled. Then the original spectral sample has entropy
\[
 H(F)=H(R)+H(B\mid R). \tag{3}
\]

Now draw \(\Sigma\) uniformly from \(\{\pm1\}\) and, conditional on \(\Sigma=\sigma\), draw the spectral sample of \(g_\sigma\). By (1), within a cell with amplitudes \(u,v\), the joint masses are
\[
 \Pr[\Sigma=\sigma,R=r]=\frac{(u+\sigma v)^2}{2}.
\]
Summing over \(\sigma\) gives \(u^2+v^2\), so the marginal law of \(R\) is exactly the same as in (3). Parseval for each Boolean \(g_\sigma\) makes \(\Sigma\) uniform. Therefore
\[
 1+\frac{H(g_+)+H(g_-)}2
 =H(\Sigma,R)
 =H(R)+H(\Sigma\mid R). \tag{4}
\]
Combining (3) and (4), define the **diagonal entropy payment**
\[
 L_{ij}(F)
 :=H(F)-\frac{H(g_+)+H(g_-)}2
 =1+H(B\mid R)-H(\Sigma\mid R). \tag{5}
\]
Since both conditional entropies are in \([0,1]\),
\[
 \boxed{0\le L_{ij}(F)\le2},\qquad
 \boxed{H(F)-2\le\frac{H(g_+)+H(g_-)}2\le H(F).} \tag{6}
\]
Both endpoints are attained by explicit Boolean functions below, so the constant two cannot be improved in this unrestricted comparison.

This is not a proof of FEI; it is an exact local identity for the operation that turns a disjoint representation into a shared-variable one.

## 4. PROVED: exact FEI-defect transport identity

For a candidate constant \(C>0\), set
\[
 D_C(f)=H(f)-C I(f).
\]
Equations (2) and (5) give

\[
 \boxed{
 \frac{D_C(g_+)+D_C(g_-)}2
 =D_C(F)+2C\,W_{ij}(F)-L_{ij}(F).
 } \tag{7}
\]

Thus at least one sign obeys
\[
 \min_{\sigma=\pm1}D_C(g_\sigma)
 \le D_C(F)+2C W_{ij}(F)-L_{ij}(F). \tag{8}
\]

### Conditional transfer criterion

If \(D_C(F)\le0\) and
\[
 L_{ij}(F)\ge 2C W_{ij}(F)+D_C(F), \tag{9}
\]
then at least one signed diagonal \(g_\sigma\) satisfies FEI with constant \(C\).
A cleaner sufficient condition is \(L_{ij}\ge2CW_{ij}\) when the parent already satisfies \(D_C(F)\le0\).

For the *fixed* \(+\) diagonal, define the sign-skew
\[
 A_C(F;i,j)=\frac{D_C(g_+)-D_C(g_-)}2.
\]
Then there is the exact decomposition
\[
 \boxed{
 D_C(g_+)=D_C(F)+2CW_{ij}-L_{ij}+A_C.
 } \tag{10}
\]
The analogous formula for \(g_-\) has \(-A_C\).

Equation (10) is the proposed new mechanism: a shared-variable composition can be studied by disjointizing it and paying three explicit quantities. The collision term \(2CW\) is geometric, \(L\) is an entropy credit, and \(A_C\) is the only fixed-polarity remainder. A full FEI proof would still need a dimension-free way to pay the collision and sign-skew terms in the actual reuse pattern.

## 5. Exact Boolean boundary example: the entropy sandwich loses the full two bits even when \(W=0\)

Let \(F(x_1,x_2,x_3,x_4)\) ignore \(x_4\) and be the selector
\[
 F=
 \begin{cases}
 -x_1,&x_3=+1,\\
 -x_2,&x_3=-1.
 \end{cases}
\]
Its Fourier expansion is
\[
 F=-\frac12x_1-\frac12x_2-\frac12x_1x_3+\frac12x_2x_3.
\]
Hence its four nonzero spectral masses are all \(1/4\):
\[
 H(F)=2,\qquad I(F)=\frac32,\qquad W_{12}(F)=0.
\]
On \(x_2=x_1\), \(g_+=-x_1\), so \(H(g_+)=0, I(g_+)=1\).
On \(x_2=-x_1\), \(g_-=-x_1x_3\), so \(H(g_-)=0,I(g_-)=2\).
Thus
\[
 L_{12}(F)=2.
\]

**Consequence — REFUTED-LEMMA:** no inequality of the form
\(L_{ij}\le c\,W_{ij}\) with finite universal \(c\) is possible. The entropy-interference effect and the double-membership collision mass are genuinely different resources.

This example also proves the lower endpoint in (6) is sharp.

## 6. Exact Boolean counterexample: both signed identifications can make \(H/I\) three times larger

Define \(G:\{-1,1\}^3\to\{-1,1\}\) by
\[
 G(x_2,x_3,x_4)=-1
 \quad\text{if }x_2=+1\text{ or }(x_2,x_3,x_4)=(-1,+1,+1),
\]
and \(G=+1\) otherwise. Put \(F=x_1G(x_2,x_3,x_4)\).

The exact spectral mass multiset of \(F\) is
\[
 \left\{\frac9{16},
 \underbrace{\frac1{16},\ldots,\frac1{16}}_{7\text{ times}}\right\}.
\]
Therefore
\[
 H(F)=4-\frac9{16}\log_2 9
 =2.216917186688699\ldots,
 \qquad I(F)=\frac94,
 \qquad W_{12}(F)=\frac34.
\]
For **both** \(x_2=x_1\) and \(x_2=-x_1\), the diagonal function has the same spectral-mass multiset, but
\[
 I(g_+)=I(g_-)=\frac34.
\]
Consequently
\[
 \frac{H(g_+)}{I(g_+)}
 =\frac{H(g_-)}{I(g_-)}
 =3\frac{H(F)}{I(F)}
 =2.955889582251599\ldots.
\]

**REFUTED-LEMMA:** identifying a duplicate coordinate does not preserve or decrease the FEI ratio, even if one is allowed to choose the better of the two relative signs.

Here \(L_{12}=0\), so (7) says exactly what went wrong: all of the damage is the collision payment \(2CW_{12}\). This example attains the upper endpoint in (6).

## 7. Finite stress test

`verify_signed_diagonal.py` checks the two examples with exact rational Walsh coefficients. It additionally enumerates all \(65,536\) Boolean functions on four variables for the fixed pair \((x_1,x_2)\).

Results:

- exact identity (2): passed for all 65,536 functions;
- entropy sandwich (6): zero observed violation (float logs used only for this finite check);
- among functions with \(W_{12}=0\), the maximum observed entropy loss is exactly the selector's \(2\);
- mask 2040 is the largest fixed-pair example in this enumeration for the quantity
  \(\min\{H(g_+)/I(g_+),H(g_-)/I(g_-)\}-H(F)/I(F)\), with increase
  \(1.9705930548343993\ldots\).

The enumeration is a sanity/stress test, **not** evidence for a universal theorem. The universal statements above are proved algebraically.

## 8. Relation to known FEI composition work

A bounded literature search in this run recovered O'Donnell--Tan's 2013 disjoint-block composition theorem and the later Wan--Wright--Wu protocol/composition treatment. Those results explain why disjoint composition is powerful; this run specifically targets the missing operation of re-identifying duplicated variables. I did not find this exact signed-diagonal defect decomposition in the bounded search, but **I make no novelty or priority claim** without a deeper literature review.

Relevant established sources:

- R. O'Donnell and L.-Y. Tan, *A composition theorem for the Fourier Entropy-Influence conjecture*, ICALP 2013 / arXiv:1304.1347.
- A. Wan, J. Wright, C. Wu, *Decision Trees, Protocols, and the Fourier Entropy-Influence Conjecture*, arXiv:1312.3003.
- X. Han, *A New Bound for the Fourier-Entropy-Influence Conjecture*, Combinatorica 45 (2025), for a recent influence-profile-type upper bound.

## 9. Claim ledger

**PROVED (this report):**
1. Signed diagonal Fourier pair formula (1).
2. Exact averaged influence identity (2).
3. Exact entropy bookkeeping identity (5) and sharp sandwich (6).
4. Exact averaged FEI-defect transport (7), existential signed transfer criterion (8)-(9), and fixed-sign decomposition (10).
5. Exact Boolean examples attaining both entropy endpoints.

**REFUTED-LEMMA:**
1. “Variable identification cannot worsen \(H/I\)” — false.
2. “Choosing the better relative sign prevents worsening” — false.
3. “Diagonal entropy loss is controlled by the two-coordinate collision mass \(W_{ij}\)” — false.
4. “The averaged FEI defect never worsens under signed identification” — false unless the \(2CW-L\) payment is controlled.

**CONDITIONAL:**
A disjoint-to-shared composition induction works through this mechanism if its reuse pattern supplies enough parent slack/entropy payment to cover \(2CW\), and for a fixed polarity also controls the sign-skew \(A_C\).

**OPEN:**
Full FEI. In particular, no universal bound on the cumulative collision/sign-skew budget has been proved here.

## 10. Next attack

Do **not** repeat the four-variable enumeration. The next run should take an actual shared-variable composition
\[
F_{\rm disjoint}(u^{(1)},\ldots,u^{(m)})
\]
to which O'Donnell--Tan applies, then identify copies of each reused input one pair at a time. Compute the exact telescoping sum of the terms
\[
2C W_{ij}-L_{ij}+A_C.
\]
The decisive question is whether composition structure, as opposed to arbitrary Booleanity, forces cancellation or a summable bound for that telescoping budget. A particularly clean first target is a read-twice formula/circuit where every physical variable occurs exactly twice and the disjointized parent is balanced. If this fails, the failure should produce an explicit shared-variable family showing which of collision or sign skew is the true universal obstruction.
