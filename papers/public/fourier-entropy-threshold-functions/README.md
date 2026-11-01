# Fourier entropy of threshold functions and their compositions

Yitzchak Shmalo

[Paper (PDF)](paper/main.pdf) · [LaTeX source](paper/main.tex) · [Declarations](DECLARATIONS.md)

The paper proves the Fourier entropy–influence inequality for every linear threshold function, with arbitrary real weights and arbitrary threshold. It also treats regular Boolean functions, Boolean combinations of halfspaces, unions with bounded variable overlap, symmetric threshold formulas under product measures, selectors with separated leaf Fourier supports, and orthogonal multiplexers whose branches share data variables.

All logarithms below are to base 2. Write $H(f)$ for Fourier entropy, $I(f)$ for total influence, and

$$D(f)=\sum_i\min\{I_i(f),1-I_i(f)\}=\min_U I(\chi_U f).$$

## Main results

- **Theorem A.** Every regular Boolean function, including every linear threshold function, satisfies $H(f)\le C_{\rm reg}D(f)$, where

  $$C_{\rm reg}=\log_2(4+e)+2\log_2(e\pi)=8.9364746578\ldots<8.937.$$

  Every character multiple $g$ therefore satisfies $H(g)\le C_{\rm reg}I(g)$ and $H(g)\le4C_{\rm reg}[I(g)-\operatorname{Var}(g)]$, with $4C_{\rm reg}<35.746$. Here *regular* means that the coordinates admit a desirability order after a monotone orientation; it is not a small-weight assumption.

- **Theorem B.** An arbitrary Boolean combination of $m$ regular functions satisfies

  $$H(f)\le(11.238+3.4\log_2m)I(f),\qquad H(f)\le(11.460+4.4\log_2m)D(f).$$

  The component functions may share variables and have different orders and orientations. A partition into $w$ desirability chains adds $\log_2w$ to the corresponding coefficient.

- **Theorem C.** A union or intersection of any number of gates, each a Boolean combination of at most $M$ regular functions, satisfies

  $$H(f)\le(41+7\log_2k+5.8\log_2M)I(f)$$

  when each input variable belongs to at most $k$ gates. A strengthened bound by influence minus variance is also proved. A refinement keeps the cost of the gates used by each whole Fourier set, its overlap congestion, and its root probabilities instead of replacing them by the worst-case read number.

- **Theorem D.** Symmetric thresholds under arbitrary product measures satisfy corrected FEI+ with constant $80+460/\ln2<744$. This constant is preserved under read-once composition with symmetric threshold and parity gates, independently of depth and fan-in. Uniform original inputs give $H(f)\le744I(f)$ and $H(f)\le747[I(f)-\operatorname{Var}(f)]$.

- **Selector identities and closure.** For a partition of the control cube and balanced leaves with pairwise disjoint Fourier supports, the Fourier entropy and influence admit exact conditional decompositions. Affine-subspace selectors feeding distinct nonconstant characters satisfy the sharp bound $H(F)\le4[I(F)-1]$. Strong entropy bounds for general selector cells and leaves compose with the maximum of their constants and $4$. The leaf input variables themselves may overlap.

- **Multiplexers with shared data.** An exact entropy identity accounts for collisions between branch Fourier coefficients, without a balance or Fourier-support-separation assumption. If neighboring branches are orthogonal and each has FEI constant $C$, their multiplexer has constant $\max\{4,C\}$. Recursive constructions with regular leaves and fresh independent selectors therefore satisfy $H(F)\le C_{\rm reg}I(F)<8.937I(F)$, independently of depth, fan-in and data reuse, provided the orthogonality condition holds at each node.

The unrestricted FEI conjecture and product-biased FEI+ for arbitrary weighted thresholds remain open in this paper. The two-cell selector and rare-activation reductions preserve the optimal universal FEI constant; they identify the remaining difficulty and are not a proof of its finiteness.

## Contents and reproduction

The source includes the references, acknowledgements and funding, competing interests, AI declaration, and data availability statement. The same declarations are provided separately in [DECLARATIONS.md](DECLARATIONS.md).

The computations use Python 3.10 or later and only its standard library:

```sh
python3 computations/check_signed_derivatives.py
python3 computations/check_biased_composition.py
python3 computations/verify_rank_improvement.py
python3 computations/verify_selectors.py
python3 computations/verify_sparse_activation.py
python3 computations/verify_witness_forests.py
python3 computations/verify_shared_data_multiplexers.py
```

Saved JSON outputs accompany the scripts. The shared-data multiplexer checker covers all 256 ordered pairs of Boolean branches on two shared data variables, including all 96 orthogonal pairs, using exact rational spectra and prime-log entropy signatures. These are finite checks of identities, coefficient calculations, and inequalities; they are not formal verification. The proofs are analytical and do not depend on the enumerations.

Build the paper with a standard TeX Live installation:

```sh
cd paper
pdflatex main.tex
pdflatex main.tex
pdflatex main.tex
```

## Related paper

[Entropy and singularity of spectral and pivotal sets in planar percolation](https://github.com/yspennstate/percolation-crossing-entropy) treats percolation crossings by spatial refinement and arm estimates. It is cited as a complementary geometric case of FEI.

## Citation

Yitzchak Shmalo. *Fourier entropy of threshold functions and their compositions*. Preprint, October 2026.
