# B17 — a second certified shared-core iterate raises the balanced FEI lower bound

**Outcome:** `CANDIDATE_REFUTED` for every all-gate potential whose center cap is at most the previously certified fleet02/B15 `G2` upper endpoint. Full uniform-cube Friedgut–Kalai Fourier entropy–influence remains **OPEN / NOT PROVED**.

**Execution:** `WITHOUT_VERIFIED_BRAIN`. Authenticated repository controls and source artifacts were read directly; no native brain retrieval/runtime was used in the mathematics.

## 1. Exact candidate state consumed

The current owner all-gate formulation asks for one symmetric nonnegative finite-cap potential `Gamma` satisfying, for every Boolean gate and every product bias vector,

\[
\Gamma(p_{\rm out})+\widetilde H_G(p)
\le
\sum_i \operatorname{It}_i(G;p)
\frac{\Gamma(p_i)+h(V_{p_i})}{V_{p_i}},
\qquad V_p=4p(1-p).
\tag{1.1}
\]

The old read-once-`Gamma` / AND-extremality candidate is already source-validly refuted by fleet01/B14, `20260922T0044Z-balanced-gate-margin-refutation`: for every balanced gate at uniform input bias,

\[
c_G(1/2,\ldots,1/2)
=4\left(\frac{H(G)}{I(G)-1}-C_0\right),
\tag{1.2}
\]

and the certified 18-input balanced Numaro gate has `H/(I-1)>6.5218457`, far above the read-once cap. I therefore do not rerun the killed AND-extremality search.

I substantively consume the exact other-account theorem

`fleet02/B17/20260921T124438Z-support-deficit-balanced-equivalence/REPORT.md`, blob `040ed0078f4905b9b4a11e963f27a1e6dcc3ee8d`,

which proves constant-for-constant

\[
\boxed{
C_{\rm FEI}
=
\sup_{g\ \mathrm{balanced},\ I(g)>1}
\frac{H(g)}{I(g)-1}.}
\tag{1.3}
\]

Thus every finite balanced Boolean gate gives a necessary lower bound on the center cap `Gamma(1/2)` of any universal all-gate potential.

The newest compatible construction consumed is fleet02/B15,

`20260922T011717Z-iterated-shared-graft/REPORT.md` and `verification_output.json`.

It proves a general shared-core operator `T(h)` on any balanced monotone gadget `h` with distinguished singleton coefficient `b`:

\[
H(T(h))=H_0+\frac9{256}H(h)+K(b),
\tag{1.4}
\]
\[
I(T(h))-1=(I_0-1)+\frac9{256}(I(h)-1),
\tag{1.5}
\]

where

\[
I_0=\frac{261}{128},
\qquad
H_0\in
[6.776605309005978082519790221891882314787235038,
 6.776605309005978082519790221891882314787235039].
\tag{1.6}
\]

Its first iterated witness

\[
G_2=T(F^{\circ4})
\]

is a finite balanced monotone Boolean function on `6,198,727,824` variables, with exact influence

\[
I_2=
\frac{784028312243315011737}{295147905179352825856}
\tag{1.7}
\]

and certified ratio

\[
\rho_2:=\frac{H(G_2)}{I(G_2)-1}
\le
6.521850763518463531668608228451477683404661344818698905249910.
\tag{1.8}
\]

The same source certifies the shared-core correction at

\[
\ell=\frac{14593}{65536},\qquad
b_1=\ell^4,
\]

as

\[
K(b_1)\ge
0.000005669659456255203780880696514165710505627614411852309871367271610481643.
\tag{1.9}
\]

## 2. New reusable-coordinate identity

Reconstructing the exact 9-bit host core from the source truth table gives, for each of its nine reusable pivot coordinates,

\[
A_{\{j\}}=114,
\qquad
Q_{\{j\}}=2,
\]

in the denominator-512 Walsh normalization used in the B15 proof. Therefore, if `T(h)` is formed from a gadget whose distinguished singleton coefficient is `b`, the corresponding output-core singleton coefficient is exactly

\[
\boxed{c(T(h))=\frac{57+b}{256}.}
\tag{2.1}
\]

This is the missing closure needed to iterate the shared-core construction itself, rather than merely iterate the inner gadget by disjoint composition.

For `G_2=T(F^{\circ4})`, set

\[
c_2=\frac{57+b_1}{256},
\qquad
b_2=c_2^4.
\tag{2.2}
\]

Exactly,

\[
c_2=
\frac{1051509762309885453313}{4722366482869645213696},
\]

and

\[
b_1-b_2
=2.4975300149436774350857419738504760475244999554\ldots\times10^{-7}.
\tag{2.3}
\]

Now define the second shared-core iterate

\[
\boxed{G_3:=T(G_2^{\circ4}).}
\tag{2.4}
\]

Because balancedness and monotonicity are preserved by disjoint self-composition and by `T`, `G_3` is again a genuine finite balanced monotone Boolean function.

## 3. Rigorous transport of the core correction

The exact host reconstruction has only 19 distinct pairs `(A_s,Q_s)` among the 512 core frequencies. For

\[
x_s(b)=\frac{A_s+bQ_s}{512},
\qquad
\phi(u)=-u\log_2 u,
\]

the derivative of the core entropy term is

\[
\left|\frac{d}{db}\phi(x_s(b)^2)\right|
=
\frac{2|Q_s|}{512}|x_s(b)|
\left(-\log_2 x_s(b)^2-\log_2 e\right).
\tag{3.1}
\]

On the rational interval

\[
J=[0.00245,0.00247]
\tag{3.2}
\]

both `b_1` and `b_2` lie in `J`, and no nonzero affine core amplitude crosses zero. Grouping the 512 terms by the 19 exact `(A,Q)` types, and bounding every logarithm by the same rational atanh series used in the inherited B15 certificate, gives

\[
\sup_{b\in J}|K'(b)|
<1.1797175971431805681
<\frac{59}{50}.
\tag{3.3}
\]

The checker proves (3.3) by exact rational comparisons; floating point is used only to print decimals.

Hence, from (1.9),

\[
\boxed{
K(b_2)
\ge
K(b_1)-\frac{59}{50}(b_1-b_2)
>
0.000005374950914491849843540578961251354332019723417113253228359314046056825.
}
\tag{3.4}
\]

## 4. Certified second-iterate improvement

Balanced disjoint self-composition gives

\[
I(G_2^{\circ4})=I_2^4,
\qquad
H(G_2^{\circ4})=(1+I_2+I_2^2+I_2^3)H(G_2).
\tag{4.1}
\]

Applying the exact `T` ledger (1.4)–(1.5) with (3.4) yields

\[
I(G_3)-1
=(I_0-1)+\frac9{256}(I_2^4-1),
\tag{4.2}
\]

and, using the inherited lower entropy endpoint for `G_2`,

\[
H(G_3)
>
17.9640524927134739964287878585621663333825656497175617713277075076948196.
\tag{4.3}
\]

The resulting rigorous balanced-excess lower bound is

\[
\boxed{
\frac{H(G_3)}{I(G_3)-1}
>
6.5218508088955452795495486657190660299841879159297347703759704933813175.
}
\tag{4.4}
\]

Comparing (4.4) with the *upper* endpoint (1.8) gives the strict certified gain

\[
\boxed{
\rho_3^{\rm lower}-\rho_2^{\rm upper}
>
4.5377081747880940437267588346579526571111035865\times10^{-8}.}
\tag{4.5}
\]

The finite dimension is

\[
\boxed{
9\,(6{,}198{,}727{,}824)^4
=13{,}287{,}790{,}733{,}194{,}203{,}608{,}289{,}203{,}380{,}089{,}898{,}205{,}184.}
\tag{4.6}
\]

No truth-table enumeration at that dimension is claimed; the function is specified recursively by finite Boolean composition and the exact shared-core operator.

By the consumed balanced equivalence (1.3), this gives the source-bound necessary lower bound

\[
\boxed{
C_{\rm FEI}
>
6.5218508088955452795495486657190660299841879159297347703759704.}
\tag{4.7}
\]

This is a lower-bound advance only; it supplies no dimension-independent upper bound and does not prove FEI.

## 5. Recursive mechanism and the remaining implication

The new identity (2.1) closes the construction under further iteration. If

\[
G_{m+1}=T(G_m^{\circ4}),
\]

and `c_m` is the reusable outer-core singleton, then exactly

\[
c_{m+1}=\frac{57+c_m^4}{256},
\tag{5.1}
\]
\[
I_{m+1}-1=(I_0-1)+\frac9{256}(I_m^4-1),
\tag{5.2}
\]
\[
H_{m+1}=H_0+\frac9{256}(1+I_m+I_m^2+I_m^3)H_m+K(c_m^4).
\tag{5.3}
\]

Equivalently, for `rho_m=H_m/(I_m-1)`,

\[
\rho_{m+1}
=
\frac{H_0+K(c_m^4)+\frac9{256}(I_m^4-1)\rho_m}
{(I_0-1)+\frac9{256}(I_m^4-1)}.
\tag{5.4}
\]

Numerical exploration suggests further small increases, but **only the `G_3` improvement (4.4)–(4.7) is claimed rigorously here**.

### Exact old/new implication

- **Old live implication:** the read-once potential is universally controlled by decomposable/AND gates. This is already `CANDIDATE_REFUTED` by the consumed balanced gate identity and the 18-input witness.
- **Successor necessary cap:** any universal all-gate potential must have `Gamma(1/2)` at least the best certified balanced-excess value. Fleet02/B15 raised this to the `G_2` interval.
- **New result:** the same source-valid shared-core mechanism is recursively iterable, and `G_3` strictly exceeds the entire `G_2` interval. Thus every candidate with center cap at most the `G_2` upper endpoint is `CANDIDATE_REFUTED`.
- **Remaining universal implication:** prove a finite upper envelope for the balanced excess / all-gate center cap, or construct an unbounded sequence. The recurrence (5.1)–(5.4) gives one exact family on which any proposed cap must be tested.

Checker SHA-256: `8ac41bb5132d07f7c6125f9a57f0f11b26e2551009437ef2799572b8621c23ea`.

Captured output SHA-256: `3500fb2b68c75306a17af8935ffadf7da3793ed4cf2c1b911a8d8b9188c94a94`.

No novelty or publication-priority claim is made. The inherited balanced equivalence, source skeleton, `T`-ledger and first `G_2` certificate are credited to their exact source artifacts above; the new applied contribution is the reusable-coordinate identity, derivative transport certificate, and strict second recursive iterate.