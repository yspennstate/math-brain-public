# B16 — balanced composition-prime gates are FEI-complete

**Outcome:** `ESSENTIAL_STEP_APPLIED` to the live gate programme, with one natural replacement shortcut **REFUTED**. Full uniform-cube Fourier entropy-influence (FEI) remains **OPEN / NOT PROVED**.

**Execution context:** `WITHOUT_VERIFIED_BRAIN`. Fresh authenticated repository control and mathematical sources were consumed, but no genuine native brain retrieval/context was available in this invocation.

## 1. Live target, supersession, and peer results actually consumed


\[
\Gamma(p_{\rm out})+H_t(G;p)
\le \sum_i {\rm It}_i(G;p)
       {\Gamma(p_i)+h(V_{p_i})\over V_{p_i}},
\qquad V_u=4u(1-u),
\tag{G}
\]

with one finite-cap symmetric nonnegative potential \(\Gamma\). The source-exact equivalence between existence of such a potential and full FEI is in

`proofnet24/P03-fei/continuations/2026-09-22-gate-reformulation/REPORT.md`, blob `1c0596f786fccf542f1f9ea65cc728b2c21ddef5`.

Two newer peer results change the correct adversarial target.

1. I consumed **fleet01/B14**,
   `20260922T0044Z-balanced-gate-margin-refutation/REPORT.md`, blob
   `776ade5c2e2017844785b09ab7af50c7eaf54c03`.
   It applies the balanced-uniform identity to the source-valid 18-input Numaro seed and proves, for the current read-once candidate \(C_0=\Gamma(1/2)=6.4548\),
   \[
   c_G(1/2,\ldots,1/2)
   \ge 0.2681828436921863\ldots,
   \]
   more than sixty times the currently quoted two-input AND margin floor \(0.0043974201\). Thus universal AND/decomposable extremality for that candidate is already **REFUTED**.

2. I consumed **fleet01/B13**,
   `20260922T002604Z-gate-composition-prime/REPORT.md`.
   Its exact gate-slack composition law proves that a decomposable gate has margin equal to a nonnegative weighted average of its components, and it gives an exact cofactor criterion for functional decomposition. After deleting dummies, call a gate **composition-prime** when every proper block \(A\) with \(2\le |A|\le k-1\) has at least three distinct cofactors. That peer proves that, for any fixed candidate \(\Gamma\), it suffices to test (G) on composition-prime gates plus the unary base.

I also consume **fleet02/B17**,
`20260921T124438Z-support-deficit-balanced-equivalence/REPORT.md`, blob
`040ed0078f4905b9b4a11e963f27a1e6dcc3ee8d`, which proves constant-for-constant
\[
C_{\rm FEI}
=
\sup_{f\ {m balanced},\ I(f)>1}
{H(f)\over I(f)-1}.
\tag{1.1}
\]

The natural replacement hope after the B13 prime reduction is that composition-prime gates might be a genuinely simpler extremal class. The theorem below refutes that hope at the level that matters for full FEI.

## 2. New theorem: balanced composition-prime gates already carry the full FEI supremum

### Theorem

For every nonconstant Boolean function \(h:\{\pm1\}^n\to\{\pm1\}\), there is a sequence of **balanced composition-prime** Boolean functions \(F_N:\{\pm1\}^N\to\{\pm1\}\), with \(N\to\infty\), such that

\[
H(F_N)\longrightarrow H(h),
\qquad
I(F_N)-1\longrightarrow I(h).
\tag{2.1}
\]

Consequently, in the extended-real sense,

\[
\boxed{
\sup_{F\ {m balanced,\ composition\mbox{-}prime},\ I(F)>1}
{H(F)\over I(F)-1}
=
\sup_{h\ {m Boolean}}{H(h)\over I(h)}
=C_{\rm FEI}.
}
\tag{2.2}
\]

Thus restricting the all-gate problem to composition-prime balanced gates is an exact structural reduction but **does not lower the extremal constant at all**.

### Step 1: balanced suspension with exactly the target entropy and influence

Add one fresh sign \(y\) and enough dummy coordinates \(z\) to reach dimension \(N\). Put

\[
F_N^{(0)}(y,x,z)=y\,h(x).
\tag{2.3}
\]

Then \(F_N^{(0)}\) is balanced. Multiplication by the fresh character \(y\) just translates the Fourier support, so

\[
H(F_N^{(0)})=H(h),
\qquad
I(F_N^{(0)})=I(h)+1.
\tag{2.4}
\]

The dummies are intentional only at this intermediate stage; the perturbation below removes every nontrivial functional decomposition.

### Step 2: a sparse random perturbation destroys every decomposition simultaneously

Independently flip the value of \(F_N^{(0)}\) at every cube point with probability

\[
\delta=N^{-4}.
\tag{2.5}
\]

Call the perturbed truth table \(F\). Fix a proper block \(A\subset[N]\), \(2\le |A|=k\le N-1\). Let

\[
K=2^k,
\qquad
L=2^{N-k},
\qquad
M=2^N=KL.
\]

View the truth table as \(K\) independent noisy cofactor rows, each of length \(L\). By the exact criterion consumed from fleet01/B13, the block \(A\) gives a functional decomposition exactly when these \(K\) rows take at most two distinct values. Denote that event by \(E_A\).

The estimates below do not use any special property of the base rows; they therefore apply to the suspended truth table (2.3) despite its many initial dummies.

#### Case 1: \(L\ge 2N^4\)

If at most two distinct rows occur, some pair of row positions supplies the two possible values. Union over the fewer than \(K^2\) choices of anchors. After conditioning on those two noisy rows, any other row hits one of the two prescribed patterns with probability at most

\[
2(1-\delta)^L
\le 2e^{-\delta L}
\le e^{-\delta L/2},
\tag{2.6}
\]

because \(\delta L\ge2>2\log 2\). Since \(K\ge4\), \(K-2\ge K/2\). Hence

\[
\Pr(E_A)
\le K^2e^{-\delta L(K-2)/2}
\le 2^{2N}\exp\!\left(-{\delta M\over4}\right).
\tag{2.7}
\]

#### Case 2: \(L<2N^4\)

There are at most \(2^{2L}\) unordered candidate sets of at most two row patterns. For a fixed noisy row, the sum of the probabilities of its two most likely patterns is exactly at most

\[
(1-\delta)^L+\delta(1-\delta)^{L-1}
=(1-\delta)^{L-1}.
\tag{2.8}
\]

Rows are independent, and \(L\ge2\), so

\[
\Pr(E_A)
\le
2^{2L}(1-\delta)^{(L-1)K}
\le
\exp\!\left(2L\log2-{\delta M\over2}\right).
\tag{2.9}
\]

For \(N\ge64\),

\[
16(\log2)N^8<2^N.
\tag{2.10}
\]

Indeed \(\log2<7/10\), the exact integer check
\(5\,2^{64}>56\,64^8\) holds, and \(2^N/N^8\) is increasing from \(N=64\) onward because \(2N^8>(N+1)^8\) there and the ratio only improves. Since \(L<2N^4\), (2.10) turns (2.9) into

\[
\Pr(E_A)
\le
\exp\!\left(-{\delta M\over4}\right).
\tag{2.11}
\]

Combining the two cases and union-bounding over fewer than \(2^N\) proper blocks gives

\[
\boxed{
\Pr(F\text{ has any nontrivial functional decomposition})
<
2^{3N}\exp\!\left(-{2^N\over4N^4}\right).
}
\tag{2.12}
\]

Absence of every such block also excludes dummy coordinates: if coordinate \(i\) were dummy, then \(A=\{i,j\}\) with any other coordinate \(j\) would have at most two cofactors. Thus a table outside the event in (2.12) is composition-prime in the B13 sense without any deletion step.

### Step 3: exact balance is compatible with primeness

The independent perturbation is not automatically balanced, so this is the point at which a naive density argument could fail.

The base table has \(m=M/2\) positive points and \(m\) negative points. Let

\[
X=\#\{+\to-\},\qquad Y=\#\{-\to+\}.
\]

Then \(X,Y\) are independent \({\rm Bin}(m,\delta)\). Let \(r\) be a mode of that binomial law. A probability distribution on \(m+1\) values has maximal atom at least \(1/(m+1)\), so

\[
\Pr(X=Y=r)
\ge{1\over(m+1)^2}
>2^{-2N}.
\tag{2.13}
\]

On the event \(X=Y\), the perturbed function is exactly balanced.

For \(N\ge64\), the exact inequality \(2^N>20N^5\) holds and remains true thereafter. Since \(e^{-x}<2^{-x}\), (2.12) gives

\[
\Pr(F\text{ non-prime})
<
2^{3N-2^N/(4N^4)}
<2^{-2N}
<\Pr(X=Y=r).
\tag{2.14}
\]

Therefore the exact-balance event cannot be contained in the non-prime event. There exists a perturbation \(F_N\) that is simultaneously **balanced and composition-prime**.

A binomial mode can be chosen with

\[
r\le (m+1)\delta.
\]

Hence the fraction \(\eta_N\) of truth-table points changed in this balanced prime perturbation satisfies

\[
\boxed{
\eta_N={r\over m}
\le N^{-4}(1+2^{1-N}).
}
\tag{2.15}
\]

### Step 4: the FEI data survive the perturbation

Let \(a,b\) be the Fourier coefficient vectors of \(F_N\) and \(F_N^{(0)}\). Parseval gives

\[
\|a-b\|_2^2
=\mathbb E(F_N-F_N^{(0)})^2
=4\eta_N.
\tag{2.16}
\]

For the squared spectral laws \(P_S=a_S^2\), \(Q_S=b_S^2\),

\[
\|P-Q\|_1
\le \|a-b\|_2\|a+b\|_2
\le4\sqrt{\eta_N}.
\tag{2.17}
\]

Thus their total-variation distance is

\[
\tau_N\le2\sqrt{\eta_N}=O(N^{-2}).
\tag{2.18}
\]

For probability laws on \(2^N\) atoms, maximal coupling gives the elementary entropy-continuity estimate

\[
|H(P)-H(Q)|
\le h_2(\tau_N)+\tau_N\log_2(2^N-1)
\le h_2(\tau_N)+N\tau_N
=o(1).
\tag{2.19}
\]

Indeed, under a maximal coupling the mismatch indicator costs \(h_2(\tau_N)\), and conditioned on a mismatch at most \(2^N-1\) alternatives remain.

For influence, changing one truth-table value affects at most \(N\) undirected cube edges. Since total influence equals the number of bichromatic undirected edges divided by \(2^{N-1}\),

\[
|I(F_N)-I(F_N^{(0)})|
\le2N\eta_N
=O(N^{-3}).
\tag{2.20}
\]

Combining (2.4), (2.19), and (2.20) proves (2.1).

### Step 5: take the supremum

Because balanced composition-prime functions are a subclass of balanced functions, (1.1) gives

\[
\sup_{F\ {m balanced,prime}}{H(F)\over I(F)-1}\le C_{\rm FEI}.
\]

Conversely, for every nonconstant \(h\), (2.1) gives

\[
{H(F_N)\over I(F_N)-1}
\longrightarrow
{H(h)\over I(h)}.
\]

Taking the supremum over \(h\) proves (2.2). \(\square\)

## 3. Direct gate-margin consequence

At uniform input bias, any balanced gate \(F\) sees only the cap \(C=\Gamma(1/2)\); the shape of \(\Gamma\) away from \(1/2\) disappears. Exactly,

\[
D_\Gamma(F)=C(I(F)-1)-H(F),
\qquad
K(F)={I(F)-1\over4},
\]

so whenever \(I(F)>1\),

\[
\boxed{
c_F(1/2,\ldots,1/2)
=4\left({H(F)\over I(F)-1}-C\right).}
\tag{3.1}
\]

The theorem therefore yields, for every arbitrary Boolean \(h\), balanced composition-prime gates \(F_N\) with

\[
c_{F_N}(1/2,\ldots,1/2)
\longrightarrow
4\left({H(h)\over I(h)}-C\right).
\tag{3.2}
\]

So for every cap \(C<C_{\rm FEI}\), a violating gate can be chosen **balanced, composition-prime, and at uniform bias**. This is stronger than saying the current read-once potential happens to have a prime counterexample: primeness itself cannot lower the universal gate-margin obstruction for any future cap.

For the current read-once candidate \(C_0=6.4548\), the already source-valid 18-input peer witness gives the concrete margin

\[
c_G\ge0.2681828436921863\ldots,
\]

while fleet01/B13's exact slack-descent theorem separately guarantees a composition-prime violating descendant of arity at most 18. The present theorem explains the all-dimensional reason this is not accidental.

## 4. Attempted refutations and dead shortcuts

### Balance could have destroyed the random-prime argument — it does not

The first version of the perturbation argument only showed that a random sparse perturbation is prime with overwhelming probability. That is insufficient because the live uniform-bias reduction needs an **exactly balanced** gate. The comparison (2.13)-(2.14) fixes this: a particular exact-balance event has probability above \(2^{-2N}\), while non-primality is already below that quantity for \(N\ge64\). No conditioning-independence assumption is used.

### Tiny truth-table distance need not by itself preserve spectral entropy — the dimension factor is paid

Entropy lives on \(2^N\) Fourier atoms, so an \(o(1)\) total-variation perturbation alone would not suffice. Choosing \(\delta=N^{-4}\) yields \(\tau_N=O(N^{-2})\), and the full continuity loss \(N\tau_N\) is therefore \(O(N^{-1})\). The growing alphabet is explicitly paid in (2.19).

### `composition-prime` is not a useful replacement extremal hypothesis by itself — REFUTED

The peer B13 reduction remains exactly correct and useful algebraically: decomposable slack telescopes into component slacks. What is refuted is the stronger strategic hope that the prime subclass has a smaller or easier FEI supremum. Equation (2.2) shows that it is already FEI-complete.

This is not a counterexample to FEI and not a disproof of the all-gate equivalence. It removes one proposed simplification after the current read-once potential's AND-extremality claim failed.

## 5. Exact checker and numbers

`check_prime_balanced_density.py` verifies with exact integer arithmetic the two threshold inequalities used above and the monotonicity starts at \(N=64\):

- `5*2^64 - 56*64^8 = 92217957769851961344 > 0`;
- `2^64 - 20*64^5 = 18446744052234715136 > 0`;
- `2*64^8-(65)^8 = 244305140530687 > 0`;
- `2*64^5-(65)^5 = 987193023 > 0`.

The remaining printed rows are illustrative evaluations of the proved bounds, not finite certificates for FEI. At \(N=64\), for example,

\[
\eta\le5.9604644775\times10^{-8},
\quad
\tau\le4.8828125\times10^{-4},
\]

\[
|\Delta H|\le0.03732537\ {m bits},
\qquad
|\Delta I|\le7.6294\times10^{-6},
\]

while the logarithm base two of the non-prime probability upper bound is below approximately
\(-3.96565\times10^{11}\), compared with the exact-balance lower bound exponent \(-128\). The gap only increases rapidly with \(N\).

## 6. Old implication, new result, replacement obligation

**Version:** live all-gate formulation at source blob `1c0596f786fccf542f1f9ea65cc728b2c21ddef5`, after the fleet01/B14 refutation of the read-once-\(\Gamma\) AND-extremality candidate.

**Old missing implication:** after decomposable gates telescope to components, hope that proving the gate inequality on composition-prime gates is a structurally smaller extremal problem that can admit a better universal bound.

**New proved inference:** balanced composition-prime gates are dense enough, in a quantitatively controlled truth-table sense, to reproduce every FEI ratio after balanced suspension. Their support-deficit/gate-margin supremum is exactly \(C_{\rm FEI}\). Therefore primeness alone supplies no smaller extremal constant and no quantitative FEI shortcut.

**Replacement obligation:** a successful successor potential/proof must exploit additional quantitative structure that is *not* erased by an \(N^{-4}\)-density truth-table perturbation, or directly prove a finite upper bound for
\[
\sup_{F\ {m balanced,prime}}{H(F)\over I(F)-1},
\]
which by (2.2) is exactly full FEI. In particular, changing \(\Gamma\) only away from \(1/2\) cannot address the balanced-uniform obstruction.

**Consumed peer artifact:** fleet01/B13 `20260922T002604Z-gate-composition-prime/REPORT.md`, applied to the exact replacement claim that composition-prime reduction might simplify the universal extremum. The balanced equivalence from fleet02/B17 is used to identify the resulting supremum with full FEI.

**Next recipient:** fleet03/B18 (gate/shannon integration) and fleet02/B17 (balanced-support-deficit/Bellman line). The useful handoff is equation (2.2): any next universal gate candidate must be tested against balanced composition-prime gates, not merely decomposable families or low arity.

**Full-FEI implication:** none beyond the structural equivalence above. Full FEI remains **OPEN / NOT PROVED**; no finite universal upper constant is established here.

No novelty or publication-priority claim is made.
