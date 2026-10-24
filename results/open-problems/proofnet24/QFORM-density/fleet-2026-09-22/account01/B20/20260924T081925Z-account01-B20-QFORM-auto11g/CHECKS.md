# Deterministic checks for account01/B20 auto11g

No simulation and no input-law approximation is used. These are arithmetic/source-scope checks for `REPORT.md`.

Constants:

- `tau=2^-16=0.0000152587890625`.
- `s0=1/64=0.015625`.
- `g=32/63=0.5079365079365079...`.
- `h=1/2-1/(4sqrt(2))=0.32322330470336311889978890947...`.
- `s_pre=h*g*s0=h/126=0.00256526432304256443571261039...`.
- `mu_1=1/(16h)=0.19336477008475339460006031158...<1/2`.
- `h_1=1/2-sqrt(mu_1/2)=0.18906208812308413313574889517...>0`.
- `c_1=sqrt(h_1)*s_pre-tau=0.00110015072937599525885835960...>0`.
- `c_1^4*tau^2=3.410742264602589e-22...`.
- With `C_E3=3*2^(4/3)*exp(1/3)=10.550168831164775...`,
  `C_E3*c_1^(-2/3)*tau^(-1/3)=39913.32659448459...<39914`.

Linear-algebra checks:

1. If `G_a>=hI` and an inherited row has squared norm at most `1/16`, then after normalizing by `G_a^(-1/2)` its leverage is at most `1/(16h)=mu_1`; this is the exact premise of the completed two-frame Bernoulli balance lemma.
2. If `K_r=U_a[R_a^r]^T U_a[R_a^r]>=h_1I` and `s_2(B_ab)>=s_pre`, then
   `s_2(U_a[R_a^r] B_ab V_b^T)>=sqrt(h_1)s_pre` because `V_b` has orthonormal columns.
3. Restricting the retained tail cannot increase Frobenius or operator norm, so Weyl loses at most `tau`, giving the actual child-cell lower bound `s_2>c_1`.
4. For the literal cut `K=[M,D]`, account02/B20 r49 Lemma 2.1 applies with no random-variable rotation: `e_3(KK^T)>=s_1(M)^2 s_2(M)^2||(I-P)D||_F^2`.
5. In the no-payment branch, `||(I-P_0)D||_F<tau` and `||D(I-P_1)||_F<tau`; therefore
   `||D-P_0DP_1||_F<=||(I-P_0)D||_F+||P_0D(I-P_1)||_F<2tau`, and `dist_F(D,rank<=2)<tau`.

Source-scope checks:

- account03/B20 r49 provides the original `1/16` normalized row-leverage gate, the physical four-bank partitions, the `h` restricted-Gram lower bound, `s_2(B)>=g s0`, and the genuine Frobenius tail `<tau`.
- account02/B20 r49 Lemma 2.1 is applied to the newly constructed **literal physical** child/self augmented cuts, not cited abstractly.
- The marginal-free physical `E_3` theorem pays the complete ambient law and permits arbitrary same-side curvature, outside couplings, affine terms, signs and extra spectrum.
- No conclusion treats the deterministic `tau` coefficient tail as a small random perturbation.

Terminal marker: `QFORM_B20_AUTO11G_SECONDGEN_SELFNODE_CHECK_PASS`.
