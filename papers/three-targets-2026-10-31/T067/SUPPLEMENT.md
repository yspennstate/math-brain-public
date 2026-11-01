# Supplementary material

A three-state posterior cone and reconstruction on finite-mean Galton-Watson trees
Yitzchak Shmalo, 31 October 2026

This supplement contains the editable paper, the two original three-state exact verification programs and a dependency-free Python reconstruction, all 80,532 coefficients, the four-state verifier and its license, complete-run outputs, and reproduction instructions.

## Compile the paper

From this T067 directory:

    cd paper
    mkdir -p build
    pdflatex -interaction=nonstopmode -halt-on-error -output-directory=build T067_full_proof.tex
    pdflatex -interaction=nonstopmode -halt-on-error -output-directory=build T067_full_proof.tex
    pdflatex -interaction=nonstopmode -halt-on-error -output-directory=build T067_full_proof.tex

Use TeX Live with amsart, lmodern, microtype, mathtools, booktabs, enumitem, listings, xurl, and hyperref. The bibliography is contained in the source.

## Reproduce the certificates

Follow Appendix A.6 of the paper. The simplest independent three-state verification is:

    python3 computation/verify_q3_python.py

This needs only the Python standard library and rewrites its result JSON and full coefficient TSVs alongside the script. Keep Python assertions enabled.

For the original C++ checks, Requirements are Python 3, a C++17 compiler providing GCC-compatible headers, and Boost multiprecision headers. Keep assertions enabled. If Boost is outside the default compiler search path, set CPLUS_INCLUDE_PATH to its include directory.

The original three-state implementation is analytic/q3_exact_pair_simple.cpp. The independent integer implementation is computation/q3_independent_coefficients.cpp. The complete coefficient tables are computation/q3_independent_coefficients_A.tsv and computation/q3_independent_coefficients_B.tsv. The first rows describe their formats. Exact comparison uses the positive scalings derived in Appendix A.3. Run outputs accompany the source.

The four-state programs and detailed instructions are in computation/published_q4/verification/checks/. The lightweight Python check does not replace the two full C++ traversals. The full traversal terminal markers must be:

    done 4479 19 lp=2074 lt=166
    done 1935 20 lp=871 lt=97

The independent complete traversal output is in computation/published_q4/verification/artifacts/fresh/. All sign decisions use exact integer or rational arithmetic. SHA-256 checksums and byte lengths for every supplementary file are in ../MANIFEST.json.

