account03/B08 r11 audit report

Source pin: math-open-problems ec211ba2d77a4a9850168c6af1574ea651feaa7c; short.tex blob c4f2a997cf336ee974e15409b5bccdd8cca039d8.
PDF SHA-256: 4c1a8eb808b32739625aa475c1aad24dc857a3f35fc960504b371487f2850423. Audited lines 271-335, Lemma 4.3 setup and Steps 1-2, PDF pages 6-7. Forward cursor: 336.
Finding: no FALSE clause found in this range. Literal line 319 omits the explicit Jensen step from the conditional bound to equation (4.5). CORRECTIONS C02 supplies the needed inequality and is a correct minimal repair; no constant changes.
Complex measure check: the setwise bound on nu_x implies total-variation domination by taking the supremum over finite partitions; Radon-Nikodym then gives the claimed L2 bound. PASS.
Scaled Plancherel check: the change of variables contributes (2|t|)^(-k) and Plancherel contributes (2pi)^k, so the coefficient is exactly (pi/|t|)^k. PASS.
Mollifier check: the autocorrelation kernel is a probability density, the convolution L2 identity is correct, and approximate-identity convergence plus Young supplies the stated dominated-convergence bound. PASS.
