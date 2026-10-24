from pathlib import Path
p=Path('ATTEMPT.md')
with p.open('a',encoding='utf8') as f:f.write('''
## 15. Proved local branch uniqueness, conditional on sigma-PV

This section gives a precise local selection consequence of the new generator-side datum. It does not derive sigma-PV for the physical gap.

Fix a nonzero real a. For a formal power series Sigma(r)=-ar+b r^2+O(r^3), the coefficient of r^2 in the sigma-PV residual is

    4b(b+a^2).                                                     (17)

Proof: rSigma''=2br+O(r^2), so its square contributes 4b^2 r^2; rSigma'-Sigma=br^2+O(r^3), and (Sigma')^2=a^2+O(r), so the other term contributes 4ba^2 r^2. Thus b=0 or b=-a^2 for every formal solution. QED.

There is at most one formal solution in each of these two sectors. In the b=0 sector the solution is exactly -ar. To see this, if a solution differed from -ar first at order n>=3, write its difference as d r^n+O(r^(n+1)), d nonzero. The square term of the PV residual starts at order 2n-2>n, while the product term at order n is 4a^2(n-1)d r^n, which is nonzero. This contradicts PV. Thus all higher coefficients vanish.

In the b=-a^2 sector suppose two solutions differed first at order n>=3, with difference d r^n. For either base solution,

    rSigma''=-2a^2 r+O(r^2),
    A=rSigma'-Sigma=-a^2 r^2+O(r^3),
    B=A+(Sigma')^2=a^2+O(r).

The changes are delta(rSigma'')=n(n-1)d r^(n-1)+O(r^n), delta A=(n-1)d r^n+O(r^(n+1)), and delta B=O(r^(n-1)). Therefore the first term in the residual changes at order n by -4a^2 n(n-1)d r^n. The second term changes there by 4a^2(n-1)d r^n; the contribution A delta B is only order n+1. Quadratic changes have order at least n+1 because n>=3. Thus the residual difference has coefficient

    -4a^2(n-1)^2 d                                                (18)

at r^n. This is nonzero, a contradiction. QED.

The same coefficient proves existence of a unique FORMAL series in the nonlinear sector: after the first two coefficients, at every order n>=3 the new coefficient appears linearly with the nonzero multiplier (18); choose it to cancel the residual at that order. Adding a term at order n does not alter previously canceled residual coefficients, by the same order calculation. This recursively constructs the unique formal solution. Convergence is not proved here.

Now let F(r) be an analytic candidate for G_2(2r), with F(0)=1, slope F'(0)=-a where a=1/pi, and satisfying the physical Peano quadratic datum F(r)=1-ar+o(r^2). Analyticity forces its quadratic coefficient to be zero. Since F is nonzero near zero, Sigma=rF'/F is analytic and has

    Sigma=-ar-a^2 r^2+O(r^3).

If this Sigma satisfies PV, it must lie in the unique nonlinear formal sector just proved. Thus there is AT MOST ONE analytic PV gap germ satisfying the generator-side first- and second-order data. Equality of all Taylor coefficients identifies analytic germs. No existence or analyticity of the physical gap has been inferred from the moment bound; this conclusion is explicitly conditional on an analytic PV candidate.

The first coefficients of the formal nonlinear sector are

    Sigma=-ar-a^2r^2-a^3r^3+(a^2/9-a^4)r^4
                  +(5a^3/36-a^5)r^5+O(r^6).

Integrating the formal relation F'/F=Sigma/r, with F(0)=1, gives

    F(r)=1-ar+(a^2/36)r^4+O(r^6).

The coefficient a^2/36 agrees with the independently known beta=2 quartic coefficient after s=2r, but the agreement is a consistency check rather than a derivation for G_2. Higher formal coefficients are saved in new_symbolic_checks.txt.

## 16. Limits of the new route and refined remaining gap

The power-moment method has a transparent ceiling. Its nonpositive discounted generator term requires p(p-1)/2<=c; concavity in (14) requires p<=2. Hence within this particular direct estimate p cannot exceed the value used in (12). At beta=2 it yields exponent (3+sqrt(5))/2, not the sharp exponent 4 or its coefficient. This limitation is a limitation of the chosen bound, not evidence that sharper generator-side estimates are impossible.

The new result closes the specific gap "exclude the exponential sigma-PV branch using source-side information." Together with the formal uniqueness argument it also supplies conditional uniqueness of the analytic nonlinear PV germ. What remains is the principal global selection/closure problem: prove that the physical probabilistically selected carousel H has the extra integrable constraint and yields sigma-PV, or derive equivalent closed identities for its discounted hitting transform. The new moment bound supplies no such constraint. Neither convergence of the formal nonlinear PV series nor global continuation of a compatible Lax solution is proved here. D0047 therefore remains PARTIAL.
''')
with Path('LITERATURE.md').open('a',encoding='utf8') as f:f.write('''

## Additional-attempt brain queries, 2026-10-12

- math_recall.py "Painleve V isomonodromy connection Fokker Planck Rumanov boundary selection": returned unrelated general cards; no carousel selection theorem.
- math_recall.py "Brownian carousel discounted hitting time Girsanov small gap level repulsion": returned generic Girsanov/generator cards and unrelated hitting-time material.
- math_recall.py "Geometric Brownian Motion Characteristic Roots Generator ODE hitting discount": retrieved the Cauchy-Euler characteristic-root card.
- math_recall.py --id claim_51bd0f2420fc622328de59f07adda2e1aead98aac1ef31a4ca8bbdbad130f247: read full card and typed links. It cites arXiv:2505.18394, Optimal stopping involving a diffusion and its running maximum: a generalisation of the maximality principle.

The characteristic polynomial is a useful hint, but the card's unrestricted assertion that the positive root exceeds 1 is false without an extra drift restriction: with sigma=1, mu=2 and discount r=1, its positive root is (-3+sqrt(17))/2<1. No such card assertion was used. Our zero-drift power calculation p(p-1)/2=c is independently verified.

No additional online literature resolution is claimed in this continuation. The added work is a direct stochastic bound and a formal PV uniqueness calculation, not a new SOLVED_IN_LITERATURE verdict.
''')
print('Formal uniqueness proof and refined remaining gap saved.')
