# The smallest eigenvalue of the NTK of a deep tanh network in the ordered phase

Yitzchak Shmalo

This repository contains the paper (`paper/t249.tex`, `paper/t249.pdf`) and the scripts behind its numerical section
(`code/`).

Consider a fully connected tanh network of depth L in the infinite-width limit, with bias variance σ_b² > 0, in the
ordered phase χ₁ < 1. Take n distinct inputs on the fixed-point sphere. The smallest eigenvalue of the neural tangent
kernel Gram matrix is

    λ_min(Θ_L) = (q* + B T*/χ₁) · λ⊥_min(−A) · L χ₁^L · (1 + O(1/L)),

where q* is the fixed-point variance, T* = q*/(1 − χ₁), B = χ'(1), and A is the matrix of limiting rescaled correlation
gaps. The order L χ₁^L of the non-constant eigenvalues is due to Xiao, Pennington and Schoenholz (ICML 2020). The paper
adds three results:

- the constant;
- a proof that λ⊥_min(−A) > 0 for any distinct inputs, so the order is attained by the smallest eigenvalue; every
  Taylor coefficient of the limiting gap profile is strictly positive, and the Schoenberg and Chen–Menegatto–Sun
  criterion then applies;
- the same asymptotic form for inputs of unequal norm, whenever λ⊥_min(−A) > 0.

## Code

Each script needs Python 3 with numpy and prints its own table.

- `code/t249_kappa_check.py`: the two-input gap against κA, for the settings in Table 1.
- `code/t249_ninput.py`: eight random inputs, with the ratio λ_min(Θ_L)/(L χ₁^L) against κ λ⊥_min(−A).
- `code/t249_series.py`: the Taylor coefficients p_k of the limiting gap profile.

## License

Text CC BY 4.0, code MIT.
