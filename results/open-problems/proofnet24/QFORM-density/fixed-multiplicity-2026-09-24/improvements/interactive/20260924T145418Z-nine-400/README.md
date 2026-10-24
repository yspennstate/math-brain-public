# Nine large eigenvalues: constant 400 and an overlap estimate

The complete, single-file, self-contained LaTeX manuscript is `paper.tex`. It proves the written candidate bound `||p_Q||_infinity <= 400 K^2/s` when `s_9(A)>=s`, for arbitrary real symmetric A, independent coordinate densities <=K, and all affine terms. It also proves the spectral-tail/overlap inequality below. The original seventeen-eigenvalue baseline is preserved unchanged in the parent project.

The threshold-nine mechanism was supplied by account03/B04 and is reconstructed fully here. This run improves the explicit constant and the overlap estimate, not the historical first occurrence of threshold nine. The new combination awaits independent review. Eight and three are not claimed solved.

## Source pin and files

- Complete paper source: commit `eeb752c8943536541b34b42b8bf48e924f4d3d2f`, `paper.tex`.
- Source git blob: `19fb119877426b640b2c0dae19ec2f78a399fe11`.
- Source SHA-256: `bf1caf6ae4b4bc33992f501c169b5dc6c795db757b0f6089eff9991391effdf3`.
- Source length: 955 lines, 60,749 bytes.
- `NINE_400_AND_OVERLAP.md`: all derivations, source credits, precise scope, and the unsuccessful maximum-determinant route.
- `AUDIT_NEW.md`: authoring-agent audit and limitations.
- `proof_map.csv`: statement/equation labels and source lines.
- `verify_new.py`, `checks_new.json`: executed finite exact checks and explicitly numerical diagnostics.
- `MANIFEST.json`: source/PDF hashes and reproducibility metadata.

The compiled 20-page PDF is delivered in the conversation. This GitHub directory stores the full reproducible source and all textual results; it does not contain a compiled PDF binary. Do not conflate those delivery forms.

## Build

Run three times:

```sh
pdflatex -interaction=nonstopmode -halt-on-error -no-shell-escape paper.tex
```

Run finite checks:

```sh
python verify_new.py --output checks_new.json
```

No other mathematical source, figure, or bibliography file is needed to compile the paper. The checker needs numpy and sympy. Finite checks do not replace the general proofs or independent review.

## New algebraic theorem

For arbitrary real square A and V_r(A)>0, let W^cross_(r,1) sum squared overlap-one bordered minors over invertible disjoint r-seeds only. Then

`W^cross_(r,1)+(r+1)^2 V_(r+1) >= V_r sum_(j>3r) s_j(A)^2`.

In particular, s_8(A)>=1 implies `W^cross_(2,1)>=2 V_2-9 V_3`. This strengthens the overlap mass bound but is NOT an eight-eigenvalue density theorem: a product-preserving analytic estimate handling the shared original coordinate is still required.

## Review priority

Independently audit the grouped mollified-L2 argument, all row-promotion cases, the separate pivot scales d=3/40 and p=1/400, the full pair half-potential, all constants, and the Frobenius-orthogonality overlap theorem. Preserve the baseline and this pinned revision; put corrections/reviews in immutable worker folders. Two genuinely separate end-to-end reviews are needed before treating the new synthesis as independently validated. Continue reducing the multiplicity without weakening any input, spectrum, sign, or affine-term hypothesis.
