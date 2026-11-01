# C0044 independent adversary derivation

2026-10-10. Phase I recorded before reading w576's proof. Exact primary-source assumptions and current openness still require verification. The full target is not claimed solved.

## I. An explicit obstruction to a stationarity argument

Let d >= 3, E = {+/-e_i: 1 <= i <= d}, and let (sigma_x) be independent uniform signs. Put a=1/(2d) and delta=1/(4d). Define

    omega(x,+e_1) = a + delta sigma_x,
    omega(x,-e_1) = a - delta sigma_x,
    omega(x,e) = a for all other e in E.

These probability vectors are iid, their entries sum to one, and every entry is at least 1/(4d). Set (theta_z omega)(x,e)=omega(x+z,e), and Kf(omega)=sum_e omega(0,e) f(theta_e omega).

For f(omega)=sigma_{-e_1}, E_P f=0. The +e_1 summand of Kf is (a+delta sigma_0)sigma_0, with mean delta. Each remaining summand has mean zero: its sign is at e-e_1 != 0, independent of sigma_0, and has mean zero. Thus E_P Kf=delta > 0. The iid spatial law P is not K-invariant. This is a proof-step counterexample, not a counterexample to directional zero-one.

## II. Exact energy defect for a quenched harmonic function

For any spatially stationary law P, define c(omega)=sum_e omega(-e,e). If a bounded real h satisfies Kh=h, then expansion of the square and a change of spatial variables give

    E_P sum_e omega(0,e)[h(theta_e omega)-h(omega)]^2
      = E_P[(c(omega)-1)h(omega)^2].

Indeed, the first square term transforms to E_P[c h^2]; the cross term is -2 E_P[h Kh]=-2 E_P[h^2]; the last term is E_P[h^2]. Spatial stationarity gives E_P c=1, but does not make the right side vanish. h can depend on the incoming probabilities in c. Independence of environment rows does not imply independence of c and the quenched tail probability.

## III. A sufficient input, still not established for the target

If there were a probability measure Q equivalent to P and invariant under K, then any bounded K-harmonic h would be spatially constant P-almost surely: integrate the square identity under Q to get zero; ellipticity makes every neighbour difference vanish; equivalence transfers this to P; countable translates and P's ergodicity make h deterministic. For h(omega)=P_0^omega(X_n.l -> +infinity), the quenched Markov property makes h(theta_{X_n} omega) a bounded conditional-probability martingale converging to the tail-event indicator. A deterministic h must therefore be 0 or 1.

This is a conditional reduction. Existence of such Q for arbitrary iid elliptic environments is not proved here. Treating P as Q would be false by section I. No multiplication of conditional estimates or claim of a new general zero-one theorem is used.

NEXT: Verify C0044's exact assumptions and primary references, then obtain w576's proof and audit the step that would eliminate the energy defect or rule out coexistence.
