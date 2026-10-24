# R08 E0011 — idea before checker code

Methods this run: **B3 PROVE SOMETHING STRONGER / B14 FIND THE GROUP ACTING / B19 MAKE IT AN ALGORITHM**.

Starting point is the newest complete R08 report, `runs/R08/20260919T1045Z_e0011_robust_bootstrap_b18_6a4c2e.md`. Its certified bootstrap event permits at most one use of the seven halo-dependent adsorption labels during the eight-arrival window and gives `B_cat >= b18_boot`, `log10 b18_boot ~= -49.89688548885152`, unchanged count 0.

The stronger object to compute is the **unrestricted adversarial-bootstrap Bellman value** on exactly the same protected Harris family and the same four halo coordinates. Let `R_0(s)=1_A(s)` and for `n>=1`

`R_n(s) = sum_{ell in L0} T_ell R_{n-1}(s) + min_{h in H(s)} sum_{ell in L1} T_{ell,h} R_{n-1}(s)`.

Here `L0` is the ten halo-independent support-closed labels, `L1` the seven already-owned halo-dependent labels, and before each accepted arrival the exterior chooses one stable halo assignment `h` before the random clock identity is revealed. Unlike the previous `F_1` recursion, the second term feeds back into `R_{n-1}`, so the successful history may use **arbitrarily many** halo-dependent labels within the eight-arrival window. This is a strictly stronger event than the `k<=1` subevent and costs no additional hazard or dependency family.

The exact algorithm should first compute the old-only polynomial `P_O` on all 48,027 projected entrance descriptors, then evaluate the unrestricted robust polynomial on the old minimizer to get a cutoff. Because `R_n >= O_n` pointwise, any state with `P_O` already at or above the cutoff can be discarded exactly. Evaluate `R` only on states below that cutoff and prove the global minimum by branch-and-bound. Compare its exact polynomial with the previous `F_1` minimum `7492177630527378997219688448`; any strict increase moves `B_cat` by the exact polynomial ratio because the Poisson/exponential prefactor and all other block factors are unchanged.

B14 symmetry check: enumerate square-lattice affine isometries preserving the full 18-cell patch, then require preservation of the 14-cell core, four-cell adversarial halo, the two fixed entrance vacancies, and six-site target. Only symmetries preserving **all** these structures may quotient the Bellman state space. If the full patch has symmetries that exchange core and halo, they are not valid reductions because the quantifiers on those coordinates differ.

No closure is assumed. If the unrestricted eight-arrival robust bootstrap still gives only a constant-factor gain, the architecture-cap result remains decisive: the next method must attack the rare multi-stage product rather than continue local bootstrap tuning.
