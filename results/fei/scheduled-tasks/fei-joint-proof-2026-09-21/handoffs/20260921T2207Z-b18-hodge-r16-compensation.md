# Joint FEI handoff — B18 q=1/q=3 Hodge companion and R16 localization

Source scientific report: `yspennstate/math-open-problems`, `proofnet24/P03-fei/fleet-2026-09-21/account02/B18/20260921T214713Z-hodge-r16-compensation/REPORT.md`, creation/readback commit `12b8647e3fcf2a79f933156ac8221e831d6289c7`.

Status: **FULL FEI OPEN / NOT PROVED**. Execution: `WITHOUT_VERIFIED_BRAIN`.

## New proved source identity

For any affine truth-table two-plane `Q`, arbitrary base phase `h`, affine-code component `P0=RM(1,D)`, terminal component `P1=RM(d,D)`, retained active coefficients `b_R=b_R^P0-b_R^P1`, and `i in Q`, put `T_i=Q\{i}` and `sigma_Q=prod_{x in Q}h(x)`. Then

`b_{T_i} + sigma_Q tan^2(t) b_{i} = H_i`,

where the complete error is the source-exact terminal character defect

`H_i(Nt) = -2N sigma_Q sin^3(t) cos(t) E_{r in P1}[(chi_Q(r)-1)y_i sin(t W_r)]`.

For the affine component alone `chi_Q=1`, so the `q=3` mode is exactly the oppositely phased Hodge complement of the current-killed `q=1` mode. The sign `sigma_Q` is the actual physical plaquette product; orientations are not merged.

## Why this matters for interface C

The account03/B18 genuine half-band positive-current no-go has only charged `(q,k)=(3,1)` modes and

`P_cen ~ 11/(864 n^3)`, while `J=8n/2^D`.

On that same family, B18 now proves the authentic R16 half-band bank is only `O(n/2^D)` by the exact closed form

`Delta_inf = log(3/2) - p0 log(1+p0/2) - m p1 log(1+p1/2)`,

with terminal-saturation error at most `2^(3-2^d) J`. Thus R16, the net terminal endpoint, and any fixed `O(J)` sink cannot furnish the required polynomial-scale compensation.

The Hodge cross term does. Using the existing bounded-independence collision lemma, the terminal Hodge defect satisfies

`int_0^Sf |H_i(s)|^2 ds/s^3 <= 16 pi T^3/sqrt(2^(d-1)-1) = o(T^6)`

at the half-band, whereas each charged triple has energy `~(2/3)T^6`. Hence with `u_i=sigma_Q tan^2(s/N)b_i` and central multiplier `eps=11/288`, the source-level companion

`C_H = -eps sum_i <b_{T_i},u_i>`

obeys the exact remainder identity

`P_cen - C_H = eps sum_i <b_{T_i},H_i> = o(n^-3)`,

so `C_H ~ 11/(864 n^3)` on the obstruction family.

This is **not yet an authorized ledger credit**. It identifies the only currently verified compensation at the correct scale as a pre-square cross-degree source term. Syndrome-translation diagonalisation kills exactly this cross term, so it is too early on the saturating packet.

## Nonoverlapping next target

B16 / interface-C work should try to extract the global sum of these `q=1/q=3` Hodge cross terms directly from the authentic signed R32/Aumann--Shapley current before Walsh-frame squaring, with actual multiplicity and terminal boundary retained. Then pay the explicit `chi_Q-1` terminal defects and the non-saturating `q>=5` sector without reusing R16 or the terminal endpoint.

B17's new low-plaquette factorization theorem is compatible but does not replace this source identity; its adaptive `n sqrt(Q)` amortization is still open. Do not revive universal positive-current `<= C J` or R16/terminal-only compensation.
