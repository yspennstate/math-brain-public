# Audit of the reduction

## Independent derivations

**Translation sign.** Take a divergence-free Fourier mode with frequency \(k\ne0\) and amplitude \(a\perp k\). The deterministic Stokes mode is \(a e^{-\nu|k|^2t}e^{ik\cdot x}\). The proposed lifted centered field is

\[
 y(t,x)=a e^{-\nu|k|^2t}e^{ik\cdot(x-X(t))}.
\]

Its time derivative contributes \(-i(k\cdot m)y\), and the mean advection contributes \(+i(k\cdot m)y\). These cancel. Using \(x+X\) in the lift would double rather than cancel that term. This direct mode calculation is independent of the weak spatial-mollification proof. The finite Fourier audit also checks the full projected quadratic convolution for interacting modes, so the verification does not rely only on a single mode whose self-interaction vanishes.

**Itô coefficient.** For \(E(m)=|m|^2/2\), the gradient is \(m\) and the Hessian is the identity. The generator of \(dm=\Sigma\,d\beta\) is \(\tfrac12 K:D^2\), so its action on \(E\) is \(\tfrac12\operatorname{tr}K\). Independently, for a centered increment \(\delta m\) of covariance \(hK\),

\[
 \mathbb E[E(m+\delta m)-E(m)]
 =\mathbb E[m\cdot\delta m+|\delta m|^2/2]
 =h\operatorname{tr}K/2.
\]

The script obtains the latter identity by exact enumeration of independent symmetric increments, not by using an Itô formula implementation. With \(h=1/100\), its covariance traces and mean increments check by hand as follows:

| Columns of \(\Sigma\) | \(\operatorname{tr}K\), from squared column lengths | Mean increment |
|---|---:|---:|
| \((0,0,0)\) | 0 | 0 |
| \((2,-1,3)\) | \(4+1+9=14\) | \(14/200=7/100\) |
| \((1,0,0),(0,2,0)\) | \(1+4=5\) | \(5/200=1/40\) |
| \((1,0,0),(0,2,0),(0,0,3)\) | \(1+4+9=14\) | \(7/100\) |
| \((1,2,0),(0,1,1),(1,0,2),(2,-1,1)\) | \(5+2+5+6=18\) | \(18/200=9/100\) |

The last case really has rank three: the determinant formed by its first three columns is 4. Thus covariance rank and number of Brownian coordinates are not being conflated.

**Energy splitting.** In physical space, \(\int y\,dx=0\) makes the cross term in \(\|y+m\|_2^2\) vanish. Independently, the Fourier audit adds the constant coefficient at frequency zero, disjoint from the nonzero Fourier support, and checks Parseval's identity by exact sums. Normalized torus measure is essential to the displayed coefficient \(|m|^2\). With unnormalized volume \(V\), every mean-energy and trace term acquires the same factor \(V\), which cancels as well.

**Output-mode count.** The four positive base frequencies in the script are \((1,0,0),(0,1,1),(1,1,0),(1,-1,2)\). Their only primitive integer relation, up to sign, is

\[
 4k_1+2k_2-3k_3-k_4=0.
\]

Its coefficient absolute sum is 10. Hence two signed sums with at most two summands each cannot coincide unless they agree formally (a nontrivial relation from their difference would have coefficient absolute sum at most 4). Adding the zero frequency gives exactly one zero mode, eight original modes, eight doubles, and \(4\binom42=24\) cross-sum modes: 41 outputs. The script reports 41 in each trial. For a solenoidal field without a constant mode, self-pairs and opposite pairs contribute zero, leaving at most 24 nonzero nonlinear output modes; the generic finite examples have all 24.

## Attempts to break the argument

- **Only a weak solution, no pointwise chain rule.** The proof first subtracts the mean, obtains an absolutely continuous path in a negative Sobolev space, then smooths only in space. The chain rule is applied after this smoothing. The nonlinear term is the mollification of \(y\otimes y\); it is never replaced by \(y_\epsilon\otimes y_\epsilon\).
- **A Brownian translation might add viscosity.** The spatial shift is \(\int_0^t m(a)\,da\), a finite-variation path. Translation by \(m(t)\) itself would be a different transformation with an Itô correction and does not prove the result.
- **A random solution of a deterministic equation might be called deterministic.** The proof asserts membership in the deterministic solution set sample by sample. It becomes a fixed trajectory only after deterministic uniqueness is assumed.
- **Joint-law nonuniqueness might not imply velocity-law nonuniqueness.** The recovery map uses the mean of the velocity path itself. Distinct deterministic trajectories give distinct pushforwards of the velocity laws. No Brownian-coordinate recovery is assumed.
- **Initial data might have nonzero mean.** The shift includes \(t\bar u_0\), and the centered datum is \(u_0-\bar u_0\). Omitting that term would leave a deterministic mean-advection term.
- **Covariance might be degenerate or have redundant columns.** The proof uses only \(m\) and \(K\); it never inverts \(\Sigma\). Exact checks cover ranks zero through three and a representation with four Brownian coordinates.
- **Good energy starting times might be lost.** The equality of energy defects is interval by interval. It preserves the original full-measure set of good starting times, including zero; no assertion that every starting time is good is needed.
- **A zero-probability noise path might be used to infer deterministic regularity.** Instead, any sample in the positive-probability global-regularity event yields a deterministic strong solution. The proof never conditions on the event that Brownian motion vanishes identically.
- **Finite checks might be mistaken for PDE evidence.** The script checks finite algebra only. Compactness, the weak equation, energy transfer, measurability, and lifetime equivalence are proved analytically in PROOF.md.
- **The usual phase space might exclude constants.** It often does. This result then has no nonzero-noise application in that phase space. It does not prove anything about regularization by nonconstant mean-zero additive noise.
- **“Leray–Hopf” might refer to a weaker energy-supermartingale definition.** The exact defect identity still holds whenever the expressions make sense, but the theorem as written uses the pathwise energy inequality. A statement about only expected inequalities requires its own formulation and is not claimed.

No counterexample to the stated reduction was found. The result is an elementary exact reduction, not a resolution of T091 and not a claim of a new theorem in the literature.

## Reproduction

Run from this folder:

```sh
env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 nice -n 15 python3 audit_reduction.py
```

All exact checks passed; the actual inherited nice was 20, and measured peak RSS was 16,154,624 bytes. The managed sandbox rejected the requested priority adjustment and Darwin memory caps, but the inherited priority satisfied the limit and actual memory remained small. Two earlier invocations stopped at resource setup before running the algebra. LOG.md records all three invocations and their outputs. Data: audit_results.json.
