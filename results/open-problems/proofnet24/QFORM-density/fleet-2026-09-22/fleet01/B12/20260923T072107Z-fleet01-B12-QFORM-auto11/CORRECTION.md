# Correction / clarification for REPORT.md concrete examples

Status: constants and conclusions unchanged.

In Sections 4 and 5, the separately introduced arbitrary small symmetric matrix `L` need not commute with the large spectral modification `H`. Therefore it should not be described as the `L_h` *spectral-threshold component of the same matrix* unless that commutation/spectral decomposition is imposed.

The examples remain valid exactly as written after the following bookkeeping, which is what the proof actually needs:

* Section 4: use `S=H`, threshold `h=0`, and combine the arbitrary small matrices as `T'=L+T`. Then `||T'||op<=1/32`, `chi(H;I,J)<=1/64`, hence `epsilon_0<=1/32+1/64=3/64<2/16`. All displayed density and spectral bounds remain unchanged.
* Section 5: use `S=H`, threshold `h=0`, and `T'=L+T`. Then `||T'||op<=1/40`, `chi(H;I,J)<=1/40`, hence `epsilon_0<=1/20`. Equations (5.14)--(5.19), including the partner bound `5.602062744709504...`, remain unchanged.

Theorem 3.1 itself is unchanged: when one starts with a single symmetric spectral modification `S`, its canonical spectral split `S=H_h+L_h` satisfies `||L_h||op<=h`. More generally, any independently supplied operator-norm-small symmetric remainder can simply be merged into the `T` term before applying the theorem.

This clarification avoids attributing a common spectral decomposition to two arbitrary symmetric matrices. No probabilistic perturbation argument is introduced.
