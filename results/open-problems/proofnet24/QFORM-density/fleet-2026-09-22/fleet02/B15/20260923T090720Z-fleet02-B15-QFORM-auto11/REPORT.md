SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet02, slot B15, 2026-09-23T09:07:20Z.
attacking: the first unpaid rough-law implication after the ruled one-sheet estimate: turn the completed one-sheet density bound and the newest partner heat-mode theorem into a quantitative ambient inequality with a random conditional critical value, while keeping essential boundedness separate from continuity.

# QFORM B15 — random-critical-value posterior bridge for rough product laws

**Status:** PROVED SUPPORTING INEQUALITY / FULL TARGET OPEN  
**Execution:** WITHOUT_VERIFIED_BRAIN

## 1. Exact obligation and source pins

The owner target remains: for arbitrary independent real coordinates with probability densities `0<=f_i<=1`, and arbitrary real symmetric `A` with at least three eigenvalues of modulus at least one, prove a universal essential density bound for `Q=X^TAX`, or give a valid counterexample. No moment, support, log-concavity, connected-support, Gaussianity, or independence after spectral rotation is assumed. Continuity is separate.

The first unpaid implication in this B15 branch is the minority/two-sheet or near-critical contribution after the majority/ruled one-sheet submeasure has been paid. The new issue is that in an ambient matrix, after conditioning outside a physical 3-block, the critical value depends on the outside variables; the deterministic-critical-value heat-mode estimate from the previous run cannot simply be averaged.

Required Claude source actually used:

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`

`proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/COUNTEREXAMPLE_SEARCH.md`.

Its completed ruled theorem states that for an exact rank-three signature `(2,1)` form with eigenvalues `lambda_1,lambda_2,-mu`, the majority-sign one-sheet submeasure has density at most

`C_B=(lambda_1 lambda_2 mu)^(-1/2) int_0^(2pi) [sin^2(theta)/lambda_1+cos^2(theta)/lambda_2+1/mu]^(-1/2) dtheta`.

Writing `kappa=min(lambda_1,lambda_2,mu)`, one has

`C_B <= pi sqrt(2)/kappa`.                                           (1.1)

The newest compatible designated-partner result actually used is fleet03/B15:

`yspennstate/math-open-problems@bf0267ac8f46c8e0d3ce773ed1401673bc0e3d02`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B15/20260923T082718Z-fleet03-B15-qform-auto16/REPORT.md`.

At every global Gaussian heat mode it proves the exact Gibbs posterior identity and the 1-subgaussian residual bound used below. I use those statements at equations (4.2), (5.1), and (6.1); this is not a copied citation.

## 2. Ambient physical 3-block and its random critical value

Let `S` be three ORIGINAL coordinates and write `X=(X_S,W)`, with `W=X_{S^c}`. Assume the fixed principal block

`B=A_SS`

is invertible of signature `(2,1)`, with eigenvalues `lambda_1,lambda_2,-mu` and `kappa>0` as above. Conditional on `W=w`, the form is

`Q_w(x)=x^T Bx+2d(w)^T x+c_0(w)`

for a deterministic vector `d(w)` and scalar `c_0(w)`. Completing the square INSIDE the original physical coordinates gives

`Q_w(x)=(x+B^{-1}d(w))^T B(x+B^{-1}d(w))+c(w)`,                    (2.1)

where

`c(w)=c_0(w)-d(w)^T B^{-1}d(w)`.                                  (2.2)

The translation `x -> x+B^{-1}d(w)` translates each of the three original one-dimensional laws. It therefore preserves their independence and their cap `<=1`. No independence after diagonalizing `B` is asserted or used.

Define the conditional-majority event

`G={Q>=c(W)}`                                                         (2.3)

and its output submeasure

`mu_+(E)=P(Q in E, G)`.                                               (2.4)

## 3. Independent rough-law check of the ruled bridge

The one-sheet formula is easiest for smooth positive source densities. To pass it to arbitrary rough cap-one marginals, mollify ONLY the three active original coordinates:

`f_i^(eta)=f_i*gamma_eta`, `i in S`.                                (3.1)

Then `0<=f_i^(eta)<=1`, each remains a probability density, independence is preserved, and

`delta_eta := || product_(i in S) f_i^(eta) - product_(i in S) f_i ||_1`
`          <= sum_(i in S) ||f_i^(eta)-f_i||_1 ->0`.               (3.2)

For every fixed outside value `w`, translation in (2.1) does not change this L1 distance. Therefore the corresponding conditional probability measures on the three active coordinates differ in total variation by at most `delta_eta/2` (or by at most `delta_eta` under the unhalved TV convention). Deterministic quadratic pushforward and restriction to the measurable majority set `Q_w>=c(w)` cannot increase total variation. Hence for every interval `I`, uniformly in `w`,

`|P_eta(Q_w in I, Q_w>=c(w)) - P(Q_w in I, Q_w>=c(w))| ->0`.       (3.3)

For every `eta`, the completed ruled theorem applies with the SAME matrix constant `C_B`, so

`P_eta(Q_w in I, Q_w>=c(w)) <= C_B |I|`.                            (3.4)

Passing `eta ->0` in (3.3) and averaging the untouched outside law gives

`boxed(mu_+(I) <= C_B |I| for every interval I.)`                   (3.5)

By open-set decomposition and outer regularity this extends to every Borel set, so

`boxed(mu_+ <= C_B dx,  C_B<=pi sqrt(2)/kappa.)`                    (3.6)

This is an ESSENTIAL-BOUNDEDNESS statement for a positive submeasure. No continuity of the rough output density is used or concluded by this limiting argument.

## 4. Gaussian heat mode and partner Gibbs posterior

Let `mu` be the full output law of `Q`. For `epsilon>0` define

`gamma_epsilon(u)=(sqrt(2pi) epsilon)^(-1) exp(-u^2/(2epsilon^2))`,

`H_epsilon(y)=(mu*gamma_epsilon)(y)`.                               (4.1)

For every probability law `mu`, `H_epsilon` is continuous and vanishes at infinity, hence has a global maximizer `y_*`. Put `M=H_epsilon(y_*)` and define the Gaussian Gibbs posterior `nu` on the ORIGINAL source space by

`dnu/dP = gamma_epsilon(Q-y_*)/M`.                                  (4.2)

Let

`U=(Q-y_*)/epsilon`.                                                 (4.3)

The completed fleet03/B15 theorem gives, exactly at a global heat mode,

`boxed(E_nu exp(vU) <= exp(v^2/2) for all v in R.)`                  (4.4)

Thus `E_nu U=0`, `E_nu U^2<=1`, and Chernoff gives

`nu(U<-d) <= exp(-d^2/2)` for every `d>0`.                           (4.5)

The same partner report gives the exact identity

`boxed(1 = sqrt(2pi) epsilon M E_nu exp(U^2/2))`,                    (4.6)

and consequently

`D(nu||P)+(1/2)E_nu U^2 = -log(sqrt(2pi) epsilon M)`.                (4.7)

Equation (4.7) is used only after the height estimate below; it is not used to infer boundedness from continuity.

## 5. Main theorem: random-critical-value posterior bridge

Define the normalized random critical gap

`D=(y_*-c(W))/epsilon`.                                              (5.1)

The key identity is

`(mu_+*gamma_epsilon)(y_*)`
` = E[gamma_epsilon(Q-y_*) 1_G]`
` = M nu(G)`.                                                        (5.2)

Since `mu_+<=C_B dx`, convolution with a probability density preserves the L-infinity cap:

`M nu(G) <= C_B`.                                                    (5.3)

Hence

`boxed(nu(G) <= C_B/M.)`                                             (5.4)

Now fix `d>0`. On the event `{D>=d}` and outside `{U<-d}`, one has

`U>=-d>=-D`,

which is exactly `Q>=c(W)`, i.e. `G`. Therefore

`{D>=d} subset G union {U<-d}`.                                     (5.5)

Combining (4.5) and (5.4) yields the new ambient inequality

`boxed(nu(D>=d) <= C_B/M + exp(-d^2/2),   d>0.)`                    (5.6)

Equivalently, whenever

`a_d:=nu(D>=d) > exp(-d^2/2)`,                                      (5.7)

one has

`boxed(M <= C_B/[a_d-exp(-d^2/2)]`
`          <= [pi sqrt(2)/kappa]/[a_d-exp(-d^2/2)].)`               (5.8)

This is a genuine global heat-height inequality with a RANDOM conditional critical value. The earlier deterministic-critical-value theorem is the special case in which `D` is constant.

### Self-consistent high-mode trapping

If `M>=C_B`, set

`d_M=sqrt(2 log(M/C_B))`.                                            (5.9)

Then `exp(-d_M^2/2)=C_B/M`, so (5.6) gives

`boxed(nu(D>=d_M) <= 2 C_B/M.)`                                     (5.10)

Thus a sequence of heat modes with `M/C_B -> infinity` can occur only if, under its own Gibbs posterior, the conditional critical value `c(W)` tracks the mode from below to within

`epsilon sqrt(2 log(M/C_B))`

except on posterior mass `O(C_B/M)`. This is a structural obstruction to a blow-up sequence, not yet a contradiction.

## 6. Information-theoretic corollary

Combining (5.8) with the exact partner identity (4.7) gives, whenever (5.7) holds,

`boxed(D(nu||P)+(1/2)E_nu U^2`
` >= log(a_d-exp(-d^2/2)) - log(sqrt(2pi) epsilon C_B).)`            (6.1)

Using `C_B<=pi sqrt(2)/kappa`,

`boxed(D(nu||P)+(1/2)E_nu U^2`
` >= log kappa + log(a_d-exp(-d^2/2))`
`    - log(2 pi sqrt(pi) epsilon).)`                                 (6.2)

At unit heat scale, any branch in which `kappa` carries the relevant spectral scale and the posterior puts a fixed positive excess mass above the Gaussian tail on fibers whose critical value lies below the mode therefore pays the desired logarithmic information growth directly.

The remaining obstruction is explicit: a putative large heat mode can avoid this payment only by forcing the Gibbs posterior critical gap distribution to satisfy

`nu(D>=d) <= exp(-d^2/2)+o(1)`                                      (6.3)

at every fixed `d` along a blow-up sequence. In words, the posterior must concentrate on minority/two-sheet fibers or on fibers whose cone vertex shadows the mode. This is now the first unpaid implication in this physical-3-block branch.

## 7. Logical regularity ledger

1. **Absolute continuity.** For any nonzero symmetric `A`, the full quadratic pushforward of an absolutely continuous joint law is absolutely continuous. If `N` is Lebesgue-null, local coarea gives `int_(q^{-1}(N)) F |grad q|=0`; `grad q=2Ax` vanishes only on the proper null subspace `ker A`, so the pushforward charges no null set.
2. **Essential boundedness.** The ruled theorem plus the rough bridge proves `mu_+<=C_B dx` in the exact stated branch. The full universal owner bound remains OPEN because the minority/two-sheet part and the global structural reduction remain unpaid.
3. **Continuity.** No continuity statement is needed for (3.6), (5.6), or (5.8). Gaussian heat convolution is continuous even when the original output law has no continuous density. Hence none of the height bounds in this report smuggles in continuity.
4. The general logical implications remain strict: absolute continuity alone does not imply an L-infinity density; an L-infinity density need not have a continuous representative; continuity alone does not imply boundedness.

## 8. What changed and next implication

Before this run, the ambient conditioning obstruction was: the ruled submeasure bound survives averaging, but the deterministic-critical-value heat-mode estimate does not because `c(W)` is random. Equation (5.6) replaces that obstruction by an exact posterior quantile criterion.

**First unpaid implication now:** in an unpaid N3/physical-3-block class, prove from original-coordinate product provenance that a global heat-mode Gibbs posterior cannot satisfy the critical-value shadowing condition (6.3) at all relevant scales, OR combine (5.10) with another completed structural branch that controls those shadowing fibers. The generic two-sheet X-ray bound remains unavailable by the live correction; no such premise is used here.

The full QFORM conjecture remains OPEN / NOT PROVED / NOT DISPROVED.