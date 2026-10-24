# B07 / A034 — Boolean-granularity phase deficit with a fiber-sparse completion

**Run:** `20261011T213754Z-account01-B07-a034-fiber-phase`  
**Primary packet:** A034 (Phase-energy transfer)  
**Attempt:** `A034-BOOLEAN-GRANULARITY-FIBER-1`  
**Claim version:** `B07-A034-FIBER-PHASE-v1`  
**Gap:** `G-PHASE-COND`  
**Status:** theorem proved, exact checks passed, independent review pending. Full FEI remains OPEN.

## Mathematical movement

Let `f:{-1,1}^X x {-1,1}^Y -> {-1,1}` be genuine Boolean on disjoint
uniform physical cubes. Assume every nonzero full Fourier coefficient has
`X`-degree at most an integer `d>=1`. For a physical slice `f_y`, put

`c_R(y)=E_X f(X,y) chi_R(X)`.

Boolean degree granularity gives `c_R(y)=2^(1-d)m_R(y)` with integral
`m_R(y)`. Define

`Gamma_d(f_y)=4^(1-d) sum_R m_R(y)^2 log_2(m_R(y)^2)`.

The first result is the exact identity

`H(f_y)=2(d-1)-Gamma_d(f_y)`.

Thus the coarse slice cap `2(d-1)` has a nonnegative logarithmic deficit,
specific to actual Boolean signs. For the full `X`-spectral marginal
`p_X(R)=sum_T fhat(R,T)^2`, the existing phase-energy argument sharpens to

`H(p_X) <= (2/ln 2) I_Y(f)+2(d-1)-E_y Gamma_d(f_y)`.

This does not discard the remaining entropy. The exact full chain rule is

`H(f)=H(p_X)+H(S_Y|S_X)`.

The packet's new restricted completion assumes that every positive-mass
`X`-fiber contains at most `K` nonzero `Y` frequencies. Then
`H(S_Y|S_X)<=log_2 K`, hence

`H(f) <= (2/ln 2) I_Y(f)+2(d-1)+log_2 K-E_y Gamma_d(f_y)`.

If additionally `Var(f)>=nu>0`, Poincare gives the dimension-independent
restricted FEI estimate

`H(f) <= [2/ln 2+(2(d-1)+log_2 K)/nu] I(f)-E_y Gamma_d(f_y)`.

The proof, including endpoint conventions and the exact use of Boolean
granularity, is in `CONDITIONAL_PHASE_THEOREM.tex`.

## Tensor and counterexample controls

The fiber condition is not a disguised universal hypothesis. If
`F(x,y,z)=f(x,y)g(z)` on a fresh block, then exactly

`Fhat(R,T,U)=fhat(R,T) ghat(U)`.

Consequently the `X` marginal and degree bound are unchanged, while every
positive fiber support is multiplied by `|supp(ghat)|` and

`H_F(S_{Y union Z}|S_X)=H_f(S_Y|S_X)+H(g)`.

For `g^{tensor t}` with positive spectral entropy, the support multiplier
grows at least as `2^t`. Fixed `K` therefore excludes the arbitrary-core
tensor embedding that leaves a cyclic marginal unchanged. Characters are
the only support-one factors and carry zero spectral entropy. This is the
required noncircular boundary; no claim about arbitrary Boolean functions
is made.

Addressing, rare point defects, parity lifts, near tensors, a majority/parity
selector, activation equivalence, and the cyclic-marginal tensor test were
checked. Ordinary addressing has `d=1`, so the deficit may vanish without
creating a false payment. Near tensors preserve the conditional term rather
than hiding it. Prime Boolean gates retain exact signs and realizability.

## Verification

`verify_granularity_deficit.py` uses exact rational Walsh transforms and
rational outward logarithm intervals. It exhausts all 256 Boolean functions
on an `X^2 x Y^1` cube and checks five named controls, for 3975 exact/interval
assertions.

`verify_conditional_fiber.py` exhausts the same 256 functions for the exact
chain-rule/fiber bookkeeping and checks support multiplication through four
tensor powers, for 2168 assertions. Both checkers are deterministic and use
no random seed. The all-dimensional claims rest on the written proofs, not
finite extrapolation.

## Exact remaining obstacle

Without bounded fiber support or another independently paid conditional
mechanism, `H(S_Y|S_X)` can retain the full FEI difficulty under arbitrary
tensor embeddings. No universal bound on `d`, `K`, or `nu`, and no globally
paid decomposition into such pieces, is proved. The packet therefore remains
`ACTIVE / PROVED RESTRICTED THEOREM / PENDING INDEPENDENT REVIEW`, not solved.

The next mathematical question is whether a Boolean-stable soft substitute
for hard fiber support can pay the conditional entropy while still forcing
the exact tensor multiplier to appear. Any candidate must preserve the
logarithmic deficit and exclude the signed arbitrary-core embedding.

## Source pins and routing

- Inspected open-problems head: `21d81fc67d500fd7a0fd131d0694aeb055bf2036`.
- Campaign status blob: `b41d59bda7a8b8c67bb047894906b1cf3aa8a44e`.
- Supplement mapping/counterexample/claims/campaign blobs:
  `27ec2c0d811b9145acb413d518805ecc8c321fc7`,
  `4c393aa5507b67198127bae61f71f1a7fdb328ac`,
  `c1f4c6d9543d0474599d9eeb9f193e09aabcc999`, and
  `1eb09316c0b40da377bc19ff543649b6ea0474b1`.
- Reviewed phase-energy source blob:
  `4fa283ff7e3847d3b7b3c2ceead8274498de04c2`.
- Current threshold-paper mathematics SHA-256:
  `5cff9d1b91c92883a6d35ec7674ff5953365cadc85299747e4047d9deb150dac`.

The Boolean granularity input is known and is not claimed as new. Route the
package to A088 and A094 for independent review, with A003/A079/A096 as
consumers. No review acceptance or downstream ingestion is claimed.

