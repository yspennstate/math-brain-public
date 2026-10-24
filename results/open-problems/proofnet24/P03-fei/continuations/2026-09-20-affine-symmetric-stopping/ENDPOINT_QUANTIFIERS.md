# The dimension-adaptive endpoint cannot pay every prescribed coordinate

20 September 2026. Companion to `REPORT.md`.

**Conclusion.** The proposed endpoint payment cannot hold uniformly for every relevant coordinate, even if every variable of the function is relevant. This does **not** refute a universal *existential* coordinate selector, the current character-child theorem, or FEI. The purpose is to keep the remaining quantifiers precise.

## 1. Exact target and scope

For an integer dimension parameter \(d\ge1\), define

\[
p_d=2-1/d,\qquad
\Phi_d(f)=d\left(\sum_S|\widehat f(S)|^{p_d}-1\right).
\]

Here a function on fewer than \(d\) variables may be viewed as independent of the remaining variables. At a physical coordinate of an \(n\)-variable function, put

\[
A_i^{(n)}(f)=\Phi_n(f)-\tfrac12[\Phi_{n-1}(f_0)+\Phi_{n-1}(f_1)].
\tag{1.1}
\]

The companion worker's live full-scope route asks for some suitable paid coordinate. We tested the stronger statement

\[
A_i^{(n)}(f)\le Cj_i(f)\quad\text{for every relevant coordinate }i.
\tag{1.2}
\]

**Theorem 1.** No finite universal \(C\) makes (1.2) true. This remains false on functions in which every input variable is relevant.

The following proof is all-dimensional. It does not depend on assuming that the endpoint method itself is equivalent to FEI, nor on the correctness of any uninspected worker estimate.

## 2. A previously known bent-background bad split

Let \(m\ge4\) be even, \(N=2^m\), \(\delta=N^{-1}\), and \(\rho=N^{-1/2}\). Set

\[
b_m(x)=(-1)^{x_1x_2+\cdots+x_{m-1}x_m},\qquad
c_m(x)=b_m(x)-2\mathbf1_{\{x=0\}}.
\]

Since \(b_m(0)=1\), \(c_m\) is the Boolean function obtained by flipping just that value. Let \(F_m(t,x)\) have children \(b_m,c_m\) at \(t=0,1\). Their disagreement probability is exactly

\[
j_t(F_m)=\operatorname{Inf}_t(F_m)=\delta.
\tag{2.1}
\]

The bent Fourier coefficients are \(\widehat b_m(S)=\epsilon_S\rho\), with \(\epsilon_S\in\{-1,1\}\). Consequently every parent Fourier pair has

\[
u_S=\epsilon_S\rho-\delta,\qquad v_S=\delta.
\tag{2.2}
\]

For \(m\ge2\), \(|u_S|\ge\rho-\delta\ge\rho/2\), and hence

\[
\frac{u_S^2}{v_S^2}\ge\frac1{4\delta}=2^{m-2}.
\]

Its erasure-entropy contribution is

\[
u_S^2\log_2(1+v_S^2/u_S^2)
+v_S^2\log_2(1+u_S^2/v_S^2)
\ge\delta^2(m-2).
\]

Summing all \(N\) fibres, and retaining the nonnegative Jensen–Shannon remainder, gives

\[
\boxed{\Delta_tH(F_m)\ge B_t(F_m)\ge\delta(m-2).}
\tag{2.3}
\]

This bent-background family already appears in the project's erasure-rigidity and sharp-recombination reports. The local bad-split mechanism is reused, not relabeled as a new construction. The new point below is what dimension padding does to the endpoint potential, including padding by genuinely relevant variables.

## 3. Endpoint convergence with a quantitative remainder

For a fixed finite Boolean function \(u\), write its nonzero squared Fourier masses as \(q_S\), and \(\lambda_S=\ln(1/q_S)\). Parseval gives

\[
\Phi_d(u)=\sum_Sq_S\,d(e^{\lambda_S/(2d)}-1).
\]

The elementary Taylor bound \(0\le e^z-1-z\le z^2e^z/2\), \(z\ge0\), proves

\[
0\le\Phi_d(u)-\frac{\ln2}{2}H(u)
\le\frac{L^2e^{L/(2d)}}{8d}
\quad\text{if all }\lambda_S\le L.
\tag{3.1}
\]

In particular,

\[
\Phi_d(u)\longrightarrow\frac{\ln2}{2}H(u)
\quad(d\to\infty).
\tag{3.2}
\]

The nonzero coefficients of \(F_m,b_m,c_m\) have magnitude at least \(2^{-m}\) for even \(m\ge4\); this follows immediately from (2.2) and \(\widehat c_m=\epsilon_S\rho-2\delta\). Thus \(L=2m\ln2\) is valid for all three functions. If \(d\ge m\), then \(e^{L/(2d)}\le2\), so their individual error bounds simplify to

\[
0\le\Phi_d(u)-\frac{\ln2}{2}H(u)
\le\frac{m^2(\ln2)^2}{d}.
\tag{3.3}
\]

First append dummy variables so that the total dimension is \(n\). In (1.1), the positive parent remainder may be discarded for a lower bound. The two child remainders are each bounded by (3.3). Therefore

\[
\boxed{
\frac{A_t^{(n)}(F_m)}{\delta}
\ge\frac{\ln2}{2}(m-2)
-\frac{m^2(\ln2)^2\,2^m}{n-1}.
}
\tag{3.4}
\]

The coordinate \(t\) remains relevant. Letting \(n\to\infty\) and then even \(m\to\infty\) already refutes (1.2) as stated. Dummy padding alone would not refute a rule that first deletes irrelevant coordinates, so the next section removes that limitation.

## 4. All variables can be made relevant

Let

\[
w_k(z)=1-2\mathbf1_{\{z=0\}},\qquad
G_{m,k}(t,x,z)=F_m(t,x)w_k(z),
\quad n=m+k+1.
\tag{4.1}
\]

All variables are relevant. Every \(x\)-coordinate is relevant already on the \(t=0\) bent slice, \(t\) changes the origin value, and every \(z\)-coordinate is relevant to \(w_k\). Multiplication by a disjoint sign factor preserves each original physical influence, so

\[
j_t(G_{m,k})=\delta.
\tag{4.2}
\]

For a common exponent \(p\), Fourier moments tensorize. At \(p=p_d\), with \(d\ge k\), the explicit one-point spectrum gives

\[
0\le M_{p_d}(w_k)-1
\le(2^k-1)(2^{1-k})^{2-1/d}
\le8\,2^{-k}.
\tag{4.3}
\]

The lower bound follows because \(p_d\le2\) and every normalized coefficient magnitude is at most one. For the upper bound, the main coefficient contributes at most one, and \((k-1)/d\le1\) bounds the displayed tail. This estimate is deliberately non-sharp.

If \(u\) depends on at most \(r\le d\) variables, Holder's inequality and Parseval give

\[
M_{p_d}(u)\le2^{r/(2d)}\le\sqrt2<2.
\]

Consequently,

\[
0\le\Phi_d(uw_k)-\Phi_d(u)
=d M_{p_d}(u)[M_{p_d}(w_k)-1]
\le16d\,2^{-k}.
\tag{4.4}
\]

Apply this at the parent and its two children. The positive parent correction can again be omitted for a lower bound. Combining (3.4) and (4.4) yields, for even \(m\ge4\) and \(k\ge2\),

\[
\boxed{
\frac{A_t^{(n)}(G_{m,k})}{j_t(G_{m,k})}
\ge\frac{\ln2}{2}(m-2)
-\frac{m^2(\ln2)^2\,2^m}{n-1}
-16(n-1)2^{m-k}.
}
\tag{4.5}
\]

For fixed \(m\), the two error terms vanish as \(k\to\infty\). Letting \(m\) increase proves Theorem 1 even with all variables relevant. These padding functions do not supply an existential-selector counterexample: other coordinates can still be useful.

## 5. A finite analytic certificate against coefficient four

Take

\[
m=16,\qquad k=2^{24}=16,777,216,\qquad n=16,777,233.
\]

Then

\[
\frac{m^2 2^m}{n-1}\le1,
\qquad
16(n-1)2^{m-k}<2^{-100}.
\]

The second inequality follows by comparing binary exponents; no enormous integer or truth table is needed. Thus (4.5) gives

\[
\frac{A_t^{(n)}(G_{16,2^{24}})}{j_t(G_{16,2^{24}})}
\ge7\ln2-(\ln2)^2-2^{-100}>4.37>4.
\tag{5.1}
\]

The exact rational atanh-series enclosure in `verify_endpoint_quantifiers.py` certifies the final strict inequality. This is a finite, explicitly described Boolean function with every coordinate relevant, not an extrapolation from numerical experiments. Its huge truth table was **not** enumerated or materialized. Formula (4.5), not a numerical simulation of that cube, is the certificate.

The report does not claim that four was the only plausible universal coefficient: Theorem 1 rules out every fixed coefficient for the every-coordinate statement. The finite example is included to make the quantifier distinction concrete.

## 6. What remains alive

The following are different statements:

1. Every relevant coordinate satisfies a fixed endpoint payment. **Refuted here.**
2. Every Boolean function has at least one suitable relevant coordinate with a fixed endpoint payment. **Not proved or refuted here.**
3. A specified physical tree reaches certified leaves and its actual accumulated endpoint charges are bounded by influence. **Must be checked for that tree.**
4. Full FEI. **Not proved or refuted here.**

The current character-child theorem is unaffected: the bad split here has two bent-background children, not one affine-character child. The previously certified symmetric, affine-fibre, polynomial-core and directional-compression classes are unaffected. The all-relevant tensor padding also does not make every coordinate bad, and must never be presented as doing so.

## 7. Executed checks and provenance

`verify_endpoint_quantifiers.py` depends only on the accompanying `verify_affine_symmetry.py` for exact Walsh and prime-log arithmetic. Its output `endpoint_verification.json` records the exact checker and dependency hashes.

Executed checks include six bent-background parents in dimensions 3,5,7,9,11,13, with **5,460** Fourier fibres, the exact queried influences, the fibre coefficient formulas, and rational entropy lower bounds. It also constructs **21** all-relevant products through dimension **17**, checks **252** positive physical influences and the exact Fourier tensor identities, and certifies the finite bound (5.1) analytically.

The \(m=2\) base is included as an exact boundary-case check of (2.3); the quantitative tail proof uses \(m\ge4\). No noninteger power at an astronomically large exponent is approximated by floating point. The huge-dimensional certificate uses only the proved Taylor bound and a rational enclosure of \(\ln2\).

Source scopes: the endpoint definition and current character-child/existential distinction were read in `proofnet24/NM13-02/progress-entropy/runs/2026-09-20/2026-09-20__endpoint-character-child-cross-fibre.md`, blob `6786f1a9417f4e6e80a4e6a45cb2cbce728a4237`, opening 250 lines. The bent-background construction is retained from the earlier project, including `proofnet24/P03-fei/runs/2026-09-20/2026-09-20T08-15-00Z__fei-sharp-recombination-clarkson-endpoint.md`, whose relevant proof appears in the conversation's retrieved record. The present proof reconstructs its coefficient formulas directly rather than assuming an unverified asymptotic.

No claim is made that a worker had previously asserted the false every-coordinate version. It is a strengthening tested in this continuation. Publication priority and independent review are unverified.
