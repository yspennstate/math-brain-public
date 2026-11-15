# Referee log

Task: “You are refereeing a short mathematical note.” Started 2026-11-11, 22:04 +04 (Asia/Tbilisi).

## Setup

Read T104_NOTE.md. All new files and outputs will remain here. No agents, network, pushes, visible windows, or shared-state writes. In particular I am not running the global mesh/checklist/recall commands, which can write outside this folder; the run-specific restriction takes precedence. Computations run serially under `nice -n 15`, with numerical libraries limited to one thread and a 270-second alarm. Matrices will be small; no computation approaches 1 GB. The compute governor reports status ok. The note itself is the source under review, not evidence of correctness.

## 1. Matrix model — proof before numerical check

The symmetric zero-diagonal matrices are the permutation module on unordered pairs. The row-sum map has matrix B with B B^t = (n-2)I + J, hence rank n for n >= 3. Its kernel has dimension binom(n,2)-n = n(n-3)/2 and is invariant. The pair permutation module has commutant dimension three (ordered pairs of edges intersect in 0, 1, or 2 vertices). It contains the trivial and standard modules, each once, via B^t. Complete reducibility and the commutant dimension force the remaining summand to be irreducible. It is [n-2,2]: the polytabloid (12)-(14)-(23)+(34), obtained from a tableau with first two columns (1,3),(2,4), is a nonzero vector in the kernel. This also identifies the module without relying on its dimension alone.

For trace-zero row-sum-zero T, put d=diag T as a vector and H=Pi diag(d) Pi. Then diag H=(n-2)d/n, H has zero row sums and trace zero, and <T,H>=|d|^2. Also |H|^2=(n-2)|d|^2/n. Therefore T-nH/(n-2) has zero diagonal and is orthogonal to every such H, proving (5.2) and its norm identity. The same construction proves surjectivity of diag:S_0 -> V.

For an off-diagonal entry T_ab in the kernel, summing conjugation by transpositions gives (binom(n-2,2)+1)T_ab plus sum_{k != a,b}(T_kb+T_ak) = (binom(n-2,2)-1)T_ab. This is (n-1)(n-4)T_ab/2. The diagonal remains zero. Numerical verification follows.

### Step 1: CORRECT

Command: `nice -n 15 /Library/Frameworks/Python.framework/Versions/3.13/bin/python3 referee.py 1`. Numerical/exact output: `step1.json`.

```json
[
  {
    "n": 4,
    "dimension": 2,
    "projection_max_error": 1.7763568394002505e-15,
    "class_sum_scalar": 0.0,
    "class_sum_error": 2.7755575615628914e-16
  },
  {
    "n": 5,
    "dimension": 5,
    "projection_max_error": 2.220446049250313e-15,
    "class_sum_scalar": 2.0,
    "class_sum_error": 4.440892098500626e-16
  },
  {
    "n": 6,
    "dimension": 9,
    "projection_max_error": 4.440892098500626e-15,
    "class_sum_scalar": 5.0,
    "class_sum_error": 1.7763568394002505e-15
  },
  {
    "n": 7,
    "dimension": 14,
    "projection_max_error": 5.329070518200751e-15,
    "class_sum_scalar": 9.0,
    "class_sum_error": 3.552713678800501e-15
  },
  {
    "n": 8,
    "dimension": 20,
    "projection_max_error": 5.329070518200751e-15,
    "class_sum_scalar": 14.0,
    "class_sum_error": 7.105427357601002e-15
  }
]
```

### Step 2: CORRECT

Command: `nice -n 15 /Library/Frameworks/Python.framework/Versions/3.13/bin/python3 referee.py 2`. Numerical/exact output: `step2.json`.

```json
[
  {
    "n": 5,
    "graph": "star",
    "checks": {
      "tau": {
        "dim": 4,
        "coxeter_error": 1.1102230246251565e-16,
        "JM_error": 1.1102230246251565e-16
      },
      "sigma": {
        "dim": 5,
        "coxeter_error": 1.1102230246251565e-16,
        "JM_error": 4.440892098500626e-16
      },
      "dual_sigma": {
        "dim": 5,
        "coxeter_error": 1.1102230246251565e-16,
        "JM_error": 4.440892098500626e-16
      }
    },
    "lambda_min_tau": 3.0,
    "lambda_min_sigma": 3.9999999999999996,
    "F_rhs": 2.9999999999999996,
    "eq51_lhs": 5.0,
    "eq51_rhs": 5.0
  },
  {
    "n": 5,
    "graph": "edge",
    "checks": {
      "tau": {
        "dim": 4,
        "coxeter_error": 1.1102230246251565e-16,
        "JM_error": 1.1102230246251565e-16
      },
      "sigma": {
        "dim": 5,
        "coxeter_error": 1.1102230246251565e-16,
        "JM_error": 4.440892098500626e-16
      },
      "dual_sigma": {
        "dim": 5,
        "coxeter_error": 1.1102230246251565e-16,
        "JM_error": 4.440892098500626e-16
      }
    },
    "lambda_min_tau": 0.0,
    "lambda_min_sigma": 0.0,
    "F_rhs": 0.0,
    "eq51_lhs": 2.0,
    "eq51_rhs": 2.0
  },
  {
    "n": 6,
    "graph": "star",
    "checks": {
      "tau": {
        "dim": 5,
        "coxeter_error": 1.1102230246251565e-16,
        "JM_error": 2.220446049250313e-16
      },
      "sigma": {
        "dim": 9,
        "coxeter_error": 1.1102230246251565e-16,
        "JM_error": 4.440892098500626e-16
      },
      "dual_sigma": {
        "dim": 9,
        "coxeter_error": 1.1102230246251565e-16,
        "JM_error": 4.440892098500626e-16
      }
    },
    "lambda_min_tau": 3.9999999999999996,
    "lambda_min_sigma": 4.9999999999999964,
    "F_rhs": 3.9999999999999973,
    "eq51_lhs": 6.0,
    "eq51_rhs": 6.000000000000001
  },
  {
    "n": 6,
    "graph": "edge",
    "checks": {
      "tau": {
        "dim": 5,
        "coxeter_error": 1.1102230246251565e-16,
        "JM_error": 2.220446049250313e-16
      },
      "sigma": {
        "dim": 9,
        "coxeter_error": 1.1102230246251565e-16,
        "JM_error": 4.440892098500626e-16
      },
      "dual_sigma": {
        "dim": 9,
        "coxeter_error": 1.1102230246251565e-16,
        "JM_error": 4.440892098500626e-16
      }
    },
    "lambda_min_tau": 0.0,
    "lambda_min_sigma": 0.0,
    "F_rhs": 0.0,
    "eq51_lhs": 2.0,
    "eq51_rhs": 2.0
  }
]
```

## 2. Star, edge, and conjugation — CORRECT

Relabel the centre as n. The star operator is (n-1)I-J_n. In Young's orthogonal form J_n is diagonal with entry equal to the content of the box holding n; these are precisely the removable boxes. The largest content is 1 for [2,1^(n-2)], and 0 for [2,2,1^(n-4)], including n=4. The least star eigenvalues are therefore n-2 and n-1. On [n-2,2] the least removable-box content is 0, so its largest star Laplacian eigenvalue is n-1. This makes (5.1) n <= n. On one edge that largest eigenvalue is twice the weight, as is lambda_max(L_G); (5.1) is equality. Conjecture F on one edge is 0 >= 0, so this equality does not define a nonzero ratio. Substitution of (3.1) into F and rearrangement, multiplying only by n-1>0, gives precisely (5.1), in both directions.

Execution limitation: every computation is launched with the requested `nice -n 15`, but this sandbox prints `setpriority: Operation not permitted`. Actual scheduling priority cannot be guaranteed. All runs remain serial, one numerical thread, and use small matrices. Step 1 also produced floating-point flag warnings from the BLAS-backed matrix multiplication despite finite results and residuals below 8e-15; exact model checks in step 4 will provide a separate check.

## 3. Graph parametrisation and equivalence — CORRECT

For g=lam-mu>0, a top unit eigenvector is orthogonal to 1, even if mu=0. The spectral decomposition gives L=mu Pi+g xx^t, so w_ij=mu/n-g x_i x_j. Conversely the row sums give L=cn Pi+g xx^t. Nonnegative off-diagonal weights are equivalent to c>=g m(x). For a sum-zero vector in dimension >=3, m>=0: either two nonzero coordinates have the same sign, or there are at most two nonzero coordinates and some pair has product zero. Thus c>=0 follows too. The eigenvalues are cn and cn+g, and trace L=cn(n-1)+g=2W.

Using the class sum from step 1, sum (c-g x_i x_j)(I-rho_ij) equals [2c(n-1)+g/2]I+g X(x). Subtracting the two sides of (5.1) gives the equivalent scalar bound lambda_max(X)>=1/2-2(n-1)c/g.

Theorem 5.3 implies every c>=g m, because this right-hand side decreases with c. Conversely apply Theorem 5.2 at c=g m, with any g>0, to obtain Theorem 5.3. This includes mu=0: for n>=5 m=0 forces an edge vector (two nonzero coordinates of opposite signs); the least-admissible graph is one edge. If mu=lam>0 then L=mu Pi is a uniform complete graph, and (5.1) has RHS 3mu(n-2)/(n-1)>=mu for n>=4. If mu=lam=0 it is the zero graph and equality holds. Repeated top eigenvalues when g=0 do not obstruct parametrisation: set g=0 and choose any unit x in V. Thus every graph in the theorem is covered. The parametrisation itself works already for n>=3 (the representation formula for n>=4); n>=5 is needed for positivity in Lemma 5.4 and Theorem 6.1. The phrase “two nonzero eigenvalues, the larger one simple” in the abstract describes only the nondegenerate part of the theorem's family, whose statement explicitly also permits mu=0 and mu=lam.

### Step 4: CORRECT for n>=5; n=4 has a zero denominator at balanced vectors

Command: `nice -n 15 /Library/Frameworks/Python.framework/Versions/3.13/bin/python3 referee.py 4`. Numerical/exact output: `step4.json`.

```json
{
  "exact": [
    {
      "n": 4,
      "x": [
        "229/566",
        "175/566",
        "-481/566",
        "77/566"
      ],
      "pair_sum_residuals": [
        "0",
        "0",
        "0",
        "0",
        "0",
        "0",
        "0"
      ],
      "replacement_residuals_all_zero": true,
      "trace_A": "7898505696/6414247921",
      "trace_XA": "43331594201424/513710701744969",
      "trace_residuals": [
        "0",
        "0"
      ],
      "final_identity_residual": "0"
    },
    {
      "n": 5,
      "x": [
        "1027/1934",
        "1087/1934",
        "-747/1934",
        "-607/1934",
        "-380/967"
      ],
      "pair_sum_residuals": [
        "0",
        "0",
        "0",
        "0",
        "0",
        "0",
        "0"
      ],
      "replacement_residuals_all_zero": true,
      "trace_A": "5860419169447/5246348627526",
      "trace_XA": "395039883647829169/3270535261176439876",
      "trace_residuals": [
        "0",
        "0"
      ],
      "final_identity_residual": "0"
    },
    {
      "n": 6,
      "x": [
        "1391/2722",
        "1421/2722",
        "-1251/2722",
        "-1181/2722",
        "135/1361",
        "-325/1361"
      ],
      "pair_sum_residuals": [
        "0",
        "0",
        "0",
        "0",
        "0",
        "0",
        "0"
      ],
      "replacement_residuals_all_zero": true,
      "trace_A": "29886187825269/13724372348164",
      "trace_XA": "26398034553480992555/50843886224646977288",
      "trace_residuals": [
        "0",
        "0"
      ],
      "final_identity_residual": "0"
    },
    {
      "n": 7,
      "x": [
        "279/553",
        "563/1106",
        "-802/1659",
        "-523/1106",
        "45/1106",
        "95/1659",
        "-515/3318"
      ],
      "pair_sum_residuals": [
        "0",
        "0",
        "0",
        "0",
        "0",
        "0",
        "0"
      ],
      "replacement_residuals_all_zero": true,
      "trace_A": "11773833948353/3607167001410",
      "trace_XA": "46168527002085987929/46330373608436008980",
      "trace_residuals": [
        "0",
        "0"
      ],
      "final_identity_residual": "0"
    }
  ],
  "numerical_max_error": 1.1657341758564144e-15,
  "Z_n4": "2q-1/2; zero exactly at permutations of (1,1,-1,-1)/2"
}
```

## 4. Lemma 5.4 — CORRECT for n>=5

The tensor identity <a b^t,c d^t>=(a.c)(b.d) gives |S|^2=|x|^2|y|^2+(x.y)^2=1 and diag S=sqrt(2)(x_k y_k). A transposition has sigma x=x-d(e_i-e_j), sigma y=y-e(e_i-e_j). The four scalar products in the note follow. Expanding the two symmetric tensors yields (1-d^2)(1-e^2)+d^2 e^2. Since sigma S sigma has zero row sums, Pi drops out of its inner product with Pi diag(S) Pi; its diagonal is sqrt(2)(x_sigma(k)y_sigma(k)). Only i,j change, and swapping two entries in a dot product subtracts their squared difference. This proves the second inner product.

Every permutation conjugation preserves S_0 and M_n and is orthogonal, hence preserves their orthogonal complement. It therefore commutes with P, as does their weighted sum (no centrality of X is needed). Applying P to both sides of the inner product gives <PS,O PS>=<S,O S>-n/(n-2)<Pi diag(S) Pi,O S>. Together with (5.2) this proves both formulas for A y.

For the three replacements, Q_ij=delta_ij-1/n-x_i x_j. Thus (e_i-e_j)^t Q(e_i-e_j)=2-d^2; sum x_k^2 Q_kk=1-1/n-q; and (x_i e_i-x_j e_j)^t Q(x_i e_i-x_j e_j) is exactly the displayed quartic expression. Constants sum to rank Q=n-2. This distinction matters: the replacement for e^2 alone has no factor n-2.

Here are independent derivations of all seven pair sums. Write p_r=sum x_i^r, with p_1=0,p_2=1. (1) p_1^2=p_2+2 sum x_i x_j gives -1/2. (2) Expanding d^2 gives sum_i x_i^3 sum_{j!=i}x_j - 2 sum_{i<j}x_i^2 x_j^2 = -q-(1-q)=-1. (3) Expanding d^4 gives -p_6 -4(p_4 p_2-p_6)+6(p_3^2-p_6)/2=3p_3^2-4q. (4) sum_i x_i^3 sum_{j!=i}x_j=-q. (5) Expand p_2^2 to obtain (1-q)/2. (6) sum_i x_i^5 sum_{j!=i}x_j=-p_6. (7) Expand p_3^2 to obtain (p_3^2-p_6)/2. These prove the claims without numerics.

For clarity the trace calculation can be reduced to two short expressions. Put K_0=1-1/n-q. The summed nonprojection bracket is (n-4)+(7-n)d^2-2d^4, giving (n-2)/2-4+8q-6p_3^2 after summation with x_i x_j. The summed last squared-diagonal replacement has pair sum -q+1/n+p_3^2. Consequently the pair sum of K_0 minus that replacement is (3q-2p_3^2-1-1/n)/2. Multiplication by -2n/(n-2) gives the last term of the claimed trace. The other trace is n-2-2n K_0/(n-2)=(n-2)Z. Subtracting half of this trace and dividing by n-2 yields exactly the final identity. The exact program builds each A column as P(x(Qe_k)^t+(Qe_k)x^t) and X by actual permutation conjugations; it does not feed the trace formulas into the construction. The omitted sqrt(2) is accounted for by dividing traces by 2.

For n>=5, n^2-6n+6>=1 and q>=1/n, so Z>0. At n=4, Z=2q-1/2>=0. It vanishes exactly at permutations of (1,1,-1,-1)/2; there A=0 and R is undefined. At all other n=4 vectors the algebraic identity holds, but positivity cannot be asserted uniformly. Lemma 5.4 should explicitly retain the ambient hypothesis n>=5 if it is to define R for every x. Exact tests at n=4,5,6,7 have all residuals zero; the numerical tests of all seven sums and the preliminary inner products have maximum error 1.17e-15.

Step 5 checkpoint n=5: minimum residual 2.7755575615628914e-17, 4473 evaluations, no value below -1e-9.

Step 5 checkpoint n=6: minimum residual 5.5511151231257827e-17, 5822 evaluations, no value below -1e-9.

Step 5 checkpoint n=7: minimum residual -5.5511151231257827e-17, 6246 evaluations, no value below -1e-9.

Step 5 checkpoint n=8: minimum residual 2.2204460492503131e-16, 8426 evaluations, no value below -1e-9.

Step 5 checkpoint n=9: minimum residual 3.3306690738754696e-16, 7510 evaluations, no value below -1e-9.

### Step 5: CORRECT conditional on Theorem 6.1; no numerical counterexample

Command: `nice -n 15 /Library/Frameworks/Python.framework/Versions/3.13/bin/python3 referee.py 5`. Numerical/exact output: `step5.json`.

```json
[
  {
    "n": 5,
    "equalities": {
      "edge": {
        "lambda_max": 0.49999999999999994,
        "bound": 0.5,
        "residual": -5.551115123125783e-17,
        "Z": 0.6666666666666665,
        "Psi": -3.3306690738754696e-16
      },
      "star": {
        "lambda_max": 0.10000000000000006,
        "bound": 0.10000000000000003,
        "residual": 2.7755575615628914e-17,
        "Z": 0.8333333333333329,
        "Psi": 2.220446049250313e-16
      }
    },
    "counts": {
      "equality": 2,
      "random": 1500,
      "two_values": 4,
      "three_values": 72,
      "neighbourhood": 280,
      "Powell": 2615
    },
    "minima": {
      "equality": 2.7755575615628914e-17,
      "random": 0.17051649994864612,
      "two_values": 2.7755575615628914e-17,
      "three_values": 0.004410554106745734,
      "neighbourhood": 9.892087149410145e-11,
      "Powell": 6.8368644079441765e-12
    },
    "minimising_vectors": {
      "equality": [
        0.8944271909999159,
        -0.22360679774997896,
        -0.22360679774997896,
        -0.22360679774997896,
        -0.22360679774997896
      ],
      "random": [
        -0.217896398857229,
        -0.24154684362880388,
        0.8930337781033775,
        -0.18028104745582085,
        -0.253309488161524
      ],
      "two_values": [
        0.8944271909999159,
        -0.22360679774997896,
        -0.22360679774997896,
        -0.22360679774997896,
        -0.22360679774997896
      ],
      "three_values": [
        -0.8944245176648201,
        0.2257235128370254,
        0.222900334942598,
        0.222900334942598,
        0.222900334942598
      ],
      "neighbourhood": [
        0.894427190999916,
        -0.2236067977238664,
        -0.22360679774942507,
        -0.22360679777785145,
        -0.2236067977487731
      ],
      "Powell": [
        0.8944271909999157,
        -0.22360679774875195,
        -0.22360679774906872,
        -0.2236067977490687,
        -0.2236067977530264
      ]
    },
    "optimiser": [
      {
        "residual": 0.32677792620415336,
        "evaluations": 400,
        "success": true
      },
      {
        "residual": 0.3267779292203346,
        "evaluations": 396,
        "success": true
      },
      {
        "residual": 0.32677793014760675,
        "evaluations": 567,
        "success": true
      },
      {
        "residual": 1.9053036925953393e-11,
        "evaluations": 763,
        "success": true
      },
      {
        "residual": 6.8368644079441765e-12,
        "evaluations": 489,
        "success": true
      }
    ]
  },
  {
    "n": 6,
    "equalities": {
      "edge": {
        "lambda_max": 0.5000000000000001,
        "bound": 0.5,
        "residual": 1.1102230246251565e-16,
        "Z": 0.7499999999999999,
        "Psi": -6.661338147750939e-16
      },
      "star": {
        "lambda_max": 0.16666666666666685,
        "bound": 0.16666666666666674,
        "residual": 1.1102230246251565e-16,
        "Z": 0.8999999999999999,
        "Psi": -2.220446049250313e-15
      }
    },
    "counts": {
      "equality": 2,
      "random": 1500,
      "two_values": 5,
      "three_values": 120,
      "neighbourhood": 280,
      "Powell": 3915
    },
    "minima": {
      "equality": 1.6653345369377348e-16,
      "random": 0.20313040200962285,
      "two_values": 5.551115123125783e-17,
      "three_values": 0.0028010206379196767,
      "neighbourhood": 1.391173287679237e-10,
      "Powell": 1.9583695776148602e-11
    },
    "minimising_vectors": {
      "equality": [
        0.9128709291752769,
        -0.18257418583505539,
        -0.18257418583505539,
        -0.18257418583505539,
        -0.18257418583505539,
        -0.18257418583505539
      ],
      "random": [
        0.13101893528395367,
        -0.910904061392515,
        0.18919596629113447,
        0.20929062053764122,
        0.2101637134726425,
        0.17123482580714294
      ],
      "two_values": [
        0.18257418583505536,
        0.18257418583505536,
        0.18257418583505536,
        0.18257418583505536,
        0.18257418583505536,
        -0.9128709291752769
      ],
      "three_values": [
        0.18399197988377106,
        -0.9128697819293559,
        0.182219450511396,
        0.182219450511396,
        0.182219450511396,
        0.182219450511396
      ],
      "neighbourhood": [
        0.9128709291752769,
        -0.18257418581592985,
        -0.18257418581955784,
        -0.18257418584325852,
        -0.18257418581791515,
        -0.18257418587861537
      ],
      "Powell": [
        0.9128709291752769,
        -0.18257418583345955,
        -0.18257418583790852,
        -0.18257418583921373,
        -0.182574185831972,
        -0.1825741858327231
      ]
    },
    "optimiser": [
      {
        "residual": 0.32309040577487796,
        "evaluations": 626,
        "success": true
      },
      {
        "residual": 0.32309040372289005,
        "evaluations": 468,
        "success": true
      },
      {
        "residual": 0.3230904027015881,
        "evaluations": 466,
        "success": true
      },
      {
        "residual": 3.122502684194117e-08,
        "evaluations": 1800,
        "success": false
      },
      {
        "residual": 1.9583695776148602e-11,
        "evaluations": 555,
        "success": true
      }
    ]
  },
  {
    "n": 7,
    "equalities": {
      "edge": {
        "lambda_max": 0.5,
        "bound": 0.5,
        "residual": 0.0,
        "Z": 0.7999999999999998,
        "Psi": -9.992007221626409e-16
      },
      "star": {
        "lambda_max": 0.21428571428571438,
        "bound": 0.21428571428571425,
        "residual": 1.3877787807814457e-16,
        "Z": 0.9333333333333331,
        "Psi": 8.881784197001252e-16
      }
    },
    "counts": {
      "equality": 2,
      "random": 1500,
      "two_values": 6,
      "three_values": 180,
      "neighbourhood": 280,
      "Powell": 4278
    },
    "minima": {
      "equality": -5.551115123125783e-17,
      "random": 0.48061629804953443,
      "two_values": 1.3877787807814457e-16,
      "three_values": 0.02602760072954735,
      "neighbourhood": 2.3697049877924314e-10,
      "Powell": 1.5867723801576972e-11
    },
    "minimising_vectors": {
      "equality": [
        0.9258200997725514,
        -0.15430334996209188,
        -0.15430334996209188,
        -0.15430334996209188,
        -0.15430334996209188,
        -0.15430334996209188,
        -0.15430334996209188
      ],
      "random": [
        -0.20103548704337346,
        0.9153271336514007,
        -0.2493122183072406,
        -0.1719082903304972,
        -0.06961354548127976,
        -0.10079181004751606,
        -0.1226657824414937
      ],
      "two_values": [
        0.9258200997725514,
        -0.1543033499620919,
        -0.1543033499620919,
        -0.1543033499620919,
        -0.1543033499620919,
        -0.1543033499620919,
        -0.1543033499620919
      ],
      "three_values": [
        0.0031192464099528043,
        0.0031192464099528043,
        0.0031192464099528043,
        0.0031192464099528043,
        0.0031192464099528043,
        0.6992484631628314,
        -0.7148446952125954
      ],
      "neighbourhood": [
        0.9258200997725516,
        -0.15430334997499046,
        -0.15430334996265244,
        -0.1543033499994312,
        -0.15430334989381175,
        -0.15430334998380352,
        -0.1543033499578622
      ],
      "Powell": [
        0.9258200997725514,
        -0.15430334996010509,
        -0.15430334995959905,
        -0.1543033499632603,
        -0.1543033499636735,
        -0.15430334995983025,
        -0.15430334996608316
      ]
    },
    "optimiser": [
      {
        "residual": 0.3198799862903047,
        "evaluations": 663,
        "success": true
      },
      {
        "residual": 0.31987998444921056,
        "evaluations": 561,
        "success": true
      },
      {
        "residual": 0.31987998503513904,
        "evaluations": 578,
        "success": true
      },
      {
        "residual": 0.00038281816913576794,
        "evaluations": 1800,
        "success": false
      },
      {
        "residual": 1.5867723801576972e-11,
        "evaluations": 676,
        "success": true
      }
    ]
  },
  {
    "n": 8,
    "equalities": {
      "edge": {
        "lambda_max": 0.49999999999999994,
        "bound": 0.5,
        "residual": -5.551115123125783e-17,
        "Z": 0.8333333333333333,
        "Psi": -1.3322676295501878e-15
      },
      "star": {
        "lambda_max": 0.2500000000000002,
        "bound": 0.24999999999999994,
        "residual": 2.7755575615628914e-16,
        "Z": 0.9523809523809526,
        "Psi": 7.105427357601002e-15
      }
    },
    "counts": {
      "equality": 2,
      "random": 1500,
      "two_values": 7,
      "three_values": 252,
      "neighbourhood": 280,
      "Powell": 6385
    },
    "minima": {
      "equality": 2.220446049250313e-16,
      "random": 0.8384960680909217,
      "two_values": 2.7755575615628914e-16,
      "three_values": 0.0022481143591192576,
      "neighbourhood": 2.2325341575424318e-10,
      "Powell": 9.648226662051229e-12
    },
    "minimising_vectors": {
      "equality": [
        0.7071067811865476,
        -0.7071067811865476,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0
      ],
      "random": [
        0.4011406765940367,
        0.09191843556018396,
        0.15449290427935283,
        -0.8851430844210201,
        0.02107450911470662,
        0.028440884444962324,
        0.04739251099222269,
        0.1406831634355545
      ],
      "two_values": [
        0.9354143466934853,
        -0.1336306209562122,
        -0.1336306209562122,
        -0.1336306209562122,
        -0.1336306209562122,
        -0.1336306209562122,
        -0.1336306209562122,
        -0.1336306209562122
      ],
      "three_values": [
        0.13378074508842014,
        0.13378074508842014,
        0.13378074508842014,
        0.13378074508842014,
        0.13378074508842014,
        0.13378074508842014,
        0.13272943307434185,
        -0.9354139036048624
      ],
      "neighbourhood": [
        0.9354143466934853,
        -0.13363062094201777,
        -0.13363062093885292,
        -0.13363062102453355,
        -0.13363062095976408,
        -0.13363062092440475,
        -0.1336306209719892,
        -0.1336306209319233
      ],
      "Powell": [
        0.9354143466934853,
        -0.13363062095634978,
        -0.13363062095722134,
        -0.13363062095834605,
        -0.13363062095427936,
        -0.13363062095616196,
        -0.13363062095525538,
        -0.13363062095587153
      ]
    },
    "optimiser": [
      {
        "residual": 0.3165530902334376,
        "evaluations": 874,
        "success": true
      },
      {
        "residual": 0.31655309023343553,
        "evaluations": 825,
        "success": true
      },
      {
        "residual": 0.0200753566602484,
        "evaluations": 1800,
        "success": false
      },
      {
        "residual": 5.5143889454711825e-11,
        "evaluations": 1629,
        "success": true
      },
      {
        "residual": 9.648226662051229e-12,
        "evaluations": 1257,
        "success": true
      }
    ]
  },
  {
    "n": 9,
    "equalities": {
      "edge": {
        "lambda_max": 0.5,
        "bound": 0.5,
        "residual": 0.0,
        "Z": 0.8571428571428571,
        "Psi": -1.6653345369377348e-15
      },
      "star": {
        "lambda_max": 0.27777777777777807,
        "bound": 0.27777777777777773,
        "residual": 3.3306690738754696e-16,
        "Z": 0.9642857142857145,
        "Psi": 7.993605777301127e-15
      }
    },
    "counts": {
      "equality": 2,
      "random": 1500,
      "two_values": 8,
      "three_values": 336,
      "neighbourhood": 280,
      "Powell": 5384
    },
    "minima": {
      "equality": 3.3306690738754696e-16,
      "random": 1.326545044349569,
      "two_values": 3.3306690738754696e-16,
      "three_values": 0.010029966583202432,
      "neighbourhood": 2.860937597937152e-10,
      "Powell": 1.5150158905186117e-11
    },
    "minimising_vectors": {
      "equality": [
        0.9428090415820635,
        -0.11785113019775793,
        -0.11785113019775793,
        -0.11785113019775793,
        -0.11785113019775793,
        -0.11785113019775793,
        -0.11785113019775793,
        -0.11785113019775793,
        -0.11785113019775793
      ],
      "random": [
        0.39296806591912087,
        -0.029763734486308653,
        0.03794545671732349,
        0.1814072070285401,
        -0.03447085649184882,
        -0.8659674162462324,
        0.13749986743867296,
        -0.019534043237705502,
        0.19991545335843802
      ],
      "two_values": [
        0.9428090415820635,
        -0.11785113019775793,
        -0.11785113019775793,
        -0.11785113019775793,
        -0.11785113019775793,
        -0.11785113019775793,
        -0.11785113019775793,
        -0.11785113019775793,
        -0.11785113019775793
      ],
      "three_values": [
        -0.11919562133083736,
        -0.11919562133083736,
        -0.11919562133083736,
        -0.11919562133083736,
        -0.11919562133083736,
        -0.11560651631987906,
        -0.11560651631987906,
        -0.11560651631987906,
        0.942797655613824
      ],
      "neighbourhood": [
        0.9428090415820634,
        -0.1178511302069216,
        -0.1178511301387038,
        -0.117851130241681,
        -0.11785113019299141,
        -0.11785113023911266,
        -0.11785113023200319,
        -0.11785113018727737,
        -0.11785113014337235
      ],
      "Powell": [
        0.9428090415820632,
        -0.11785113019949152,
        -0.11785113019718335,
        -0.11785113019973663,
        -0.11785113019471552,
        -0.11785113019605965,
        -0.11785113020037088,
        -0.11785113019491905,
        -0.11785113019958678
      ]
    },
    "optimiser": [
      {
        "residual": 0.31302050483434873,
        "evaluations": 760,
        "success": true
      },
      {
        "residual": 0.3130205082187655,
        "evaluations": 904,
        "success": true
      },
      {
        "residual": 0.31302050692662725,
        "evaluations": 747,
        "success": true
      },
      {
        "residual": 0.005961558732939076,
        "evaluations": 1800,
        "success": false
      },
      {
        "residual": 1.5150158905186117e-11,
        "evaluations": 1173,
        "success": true
      }
    ]
  }
]
```

## 5. Theorem 5.3 — CORRECT, conditional on Theorem 6.1

A A^* is positive semidefinite and has strictly positive trace for n>=5. Therefore tr(X A A^*)/tr(A A^*) is a convex combination of Rayleigh quotients and is at most lambda_max(X). The lemma and Psi>=0 then give the theorem with exactly the stated constants.

The equality argument in the note is complete once its earlier star and edge calculations and the equivalence at c=g m are used: at the edge vector m=0 the graph has just one edge of weight g/2; at the star vector m=1/(n(n-1)) its centre-to-leaf weights are g/(n-1), and all leaf-to-leaf weights vanish. These graphs saturate (5.1), and the reduction to Theorem 5.3 is an equivalence, so equality follows. Equality does not require proving that the trial state is supported on the top eigenspace, although that would give another proof. The theorem claims equality at these vectors, not an exhaustive list of equality cases.

The independent search tested random vectors, all multiplicity splits into two values, random three-value vectors for every positive multiplicity split, seven scales of neighbourhoods of both equality vectors, and five Powell runs per n. It found no residual below -1e-9. Some Powell runs hit their evaluation cap; this is evidence, not a proof of a global minimum. Exact equality-vector predictions are lambda_max=1/2 at the edge and 1/2-2/n at the star. All agree numerically through n=9. Full counts, minima, and vectors are in step5.json.

### Step 6: CORRECT; direct independent Specht-module check

Command: `nice -n 15 /Library/Frameworks/Python.framework/Versions/3.13/bin/python3 referee.py 6`. Numerical/exact output: `step6.json`.

```json
[
  {
    "n": 5,
    "graphs": 2264,
    "undefined_zero_denominator": 1,
    "smallest": {
      "ratio": 0.7499999999999998,
      "x": [
        0.8944271909999159,
        -0.22360679774997896,
        -0.22360679774997896,
        -0.22360679774997896,
        -0.22360679774997896
      ],
      "c": 0.049999999999999996,
      "g": 1,
      "source": "star",
      "increment": 0.0,
      "lambda_min_tau": 0.7499999999999997,
      "lambda_min_sigma": 0.9999999999999998
    },
    "target": 0.75,
    "ratio_divided_by_target": 0.9999999999999997,
    "smallest_by_increment": {
      "0.01": 0.8035714285714292,
      "0.2": 1.102941176470588,
      "1.0": 1.2115384615384617,
      "0.0": 0.7499999999999998
    },
    "minimum_signed_gap": -1.1102230246251565e-16,
    "coxeter_error": 1.1102230246251565e-16
  },
  {
    "n": 6,
    "graphs": 2268,
    "undefined_zero_denominator": 1,
    "smallest": {
      "ratio": 0.8000000000000006,
      "x": [
        0.18257418583505536,
        0.18257418583505536,
        0.18257418583505536,
        0.18257418583505536,
        0.18257418583505536,
        -0.9128709291752769
      ],
      "c": 0.033333333333333326,
      "g": 1,
      "source": "two_values",
      "increment": 0.0,
      "lambda_min_tau": 0.7999999999999999,
      "lambda_min_sigma": 0.9999999999999991
    },
    "target": 0.8,
    "ratio_divided_by_target": 1.0000000000000007,
    "smallest_by_increment": {
      "0.01": 0.8666666666666667,
      "0.2": 1.1199999999999999,
      "1.0": 1.1809523809523812,
      "0.0": 0.8000000000000006
    },
    "minimum_signed_gap": 0.0,
    "coxeter_error": 1.1102230246251565e-16
  }
]
```

## 6. Direct graph comparison — CORRECT

The direct Young-form computation used the two conjugate shapes themselves, not X(x), not the symmetric-matrix model, and not formula (3.1). It checked 2264 graphs at n=5 and 2268 at n=6, at c=m and at c=m+0.01, m+0.2, m+1 (g=1). The least defined ratios were 0.7499999999999998 and 0.8000000000000006, respectively, attained at star vectors. These equal the targets 3/4 and 4/5 to rounding. The single-edge denominators were zero and were excluded from ratios, while their signed comparison gaps were checked. No negative gap beyond roundoff occurred.

Step 7 checkpoint n=5, R1: 5 rays, 209 nonzero coefficients, 0 negative.

Step 7 checkpoint n=5, R2: 5 rays, 208 nonzero coefficients, 0 negative.

Step 7 checkpoint n=6, R1: 6 rays, 461 nonzero coefficients, 0 negative.

Step 7 checkpoint n=6, R2: 6 rays, 460 nonzero coefficients, 0 negative.

Step 7 checkpoint n=7, R1: 11 rays, 8007 nonzero coefficients, 0 negative.

Step 7 checkpoint n=7, R2: 10 rays, 5003 nonzero coefficients, 0 negative.

### Step 7: CORRECT for reproduced n=5,6,7; larger certificates not yet checked

Command: `nice -n 15 /Library/Frameworks/Python.framework/Versions/3.13/bin/python3 referee.py 7`. Numerical/exact output: `step7.json`.

```json
{
  "certificates": [
    {
      "n": 5,
      "cone": 1,
      "ray_count": 5,
      "rays": [
        [
          1,
          0,
          0,
          0,
          -1
        ],
        [
          1,
          1,
          0,
          -1,
          -1
        ],
        [
          2,
          1,
          -1,
          -1,
          -1
        ],
        [
          2,
          2,
          -1,
          -1,
          -2
        ],
        [
          3,
          3,
          -2,
          -2,
          -2
        ]
      ],
      "total_degree6_monomials": 210,
      "nonzero_coefficients": 209,
      "zero_coefficients": 1,
      "negative_coefficients": 0,
      "smallest_nonzero_coefficient": 96,
      "largest_coefficient": 1247400,
      "scalar_crosscheck": true,
      "certificate": "certificate_n5_R1.txt"
    },
    {
      "n": 5,
      "cone": 2,
      "ray_count": 5,
      "rays": [
        [
          1,
          0,
          0,
          0,
          -1
        ],
        [
          1,
          1,
          0,
          -1,
          -1
        ],
        [
          2,
          1,
          -1,
          -1,
          -1
        ],
        [
          2,
          1,
          1,
          -2,
          -2
        ],
        [
          4,
          -1,
          -1,
          -1,
          -1
        ]
      ],
      "total_degree6_monomials": 210,
      "nonzero_coefficients": 208,
      "zero_coefficients": 2,
      "negative_coefficients": 0,
      "smallest_nonzero_coefficient": 96,
      "largest_coefficient": 511440,
      "scalar_crosscheck": true,
      "certificate": "certificate_n5_R2.txt"
    },
    {
      "n": 6,
      "cone": 1,
      "ray_count": 6,
      "rays": [
        [
          1,
          0,
          0,
          0,
          0,
          -1
        ],
        [
          1,
          1,
          0,
          0,
          -1,
          -1
        ],
        [
          1,
          1,
          1,
          -1,
          -1,
          -1
        ],
        [
          2,
          2,
          -1,
          -1,
          -1,
          -1
        ],
        [
          3,
          1,
          -1,
          -1,
          -1,
          -1
        ],
        [
          3,
          3,
          -1,
          -1,
          -1,
          -3
        ]
      ],
      "total_degree6_monomials": 462,
      "nonzero_coefficients": 461,
      "zero_coefficients": 1,
      "negative_coefficients": 0,
      "smallest_nonzero_coefficient": 240,
      "largest_coefficient": 5375232,
      "scalar_crosscheck": true,
      "certificate": "certificate_n6_R1.txt"
    },
    {
      "n": 6,
      "cone": 2,
      "ray_count": 6,
      "rays": [
        [
          1,
          0,
          0,
          0,
          0,
          -1
        ],
        [
          1,
          1,
          0,
          0,
          -1,
          -1
        ],
        [
          1,
          1,
          1,
          -1,
          -1,
          -1
        ],
        [
          3,
          1,
          -1,
          -1,
          -1,
          -1
        ],
        [
          3,
          1,
          1,
          1,
          -3,
          -3
        ],
        [
          5,
          -1,
          -1,
          -1,
          -1,
          -1
        ]
      ],
      "total_degree6_monomials": 462,
      "nonzero_coefficients": 460,
      "zero_coefficients": 2,
      "negative_coefficients": 0,
      "smallest_nonzero_coefficient": 240,
      "largest_coefficient": 5223168,
      "scalar_crosscheck": true,
      "certificate": "certificate_n6_R2.txt"
    },
    {
      "n": 7,
      "cone": 1,
      "ray_count": 11,
      "rays": [
        [
          1,
          0,
          0,
          0,
          0,
          0,
          -1
        ],
        [
          1,
          1,
          0,
          0,
          0,
          -1,
          -1
        ],
        [
          1,
          1,
          1,
          0,
          -1,
          -1,
          -1
        ],
        [
          2,
          1,
          1,
          -1,
          -1,
          -1,
          -1
        ],
        [
          2,
          2,
          1,
          1,
          -2,
          -2,
          -2
        ],
        [
          2,
          2,
          2,
          -1,
          -1,
          -2,
          -2
        ],
        [
          3,
          3,
          3,
          -2,
          -2,
          -2,
          -3
        ],
        [
          4,
          1,
          -1,
          -1,
          -1,
          -1,
          -1
        ],
        [
          4,
          4,
          -1,
          -1,
          -1,
          -1,
          -4
        ],
        [
          4,
          4,
          4,
          -3,
          -3,
          -3,
          -3
        ],
        [
          5,
          5,
          -2,
          -2,
          -2,
          -2,
          -2
        ]
      ],
      "total_degree6_monomials": 8008,
      "nonzero_coefficients": 8007,
      "zero_coefficients": 1,
      "negative_coefficients": 0,
      "smallest_nonzero_coefficient": 480,
      "largest_coefficient": 910139328,
      "scalar_crosscheck": true,
      "certificate": "certificate_n7_R1.txt"
    },
    {
      "n": 7,
      "cone": 2,
      "ray_count": 10,
      "rays": [
        [
          1,
          0,
          0,
          0,
          0,
          0,
          -1
        ],
        [
          1,
          1,
          0,
          0,
          0,
          -1,
          -1
        ],
        [
          1,
          1,
          1,
          0,
          -1,
          -1,
          -1
        ],
        [
          2,
          1,
          1,
          -1,
          -1,
          -1,
          -1
        ],
        [
          2,
          2,
          1,
          1,
          -2,
          -2,
          -2
        ],
        [
          2,
          2,
          2,
          -1,
          -1,
          -2,
          -2
        ],
        [
          3,
          2,
          2,
          2,
          -3,
          -3,
          -3
        ],
        [
          4,
          1,
          -1,
          -1,
          -1,
          -1,
          -1
        ],
        [
          4,
          1,
          1,
          1,
          1,
          -4,
          -4
        ],
        [
          6,
          -1,
          -1,
          -1,
          -1,
          -1,
          -1
        ]
      ],
      "total_degree6_monomials": 5005,
      "nonzero_coefficients": 5003,
      "zero_coefficients": 2,
      "negative_coefficients": 0,
      "smallest_nonzero_coefficient": 480,
      "largest_coefficient": 147957120,
      "scalar_crosscheck": true,
      "certificate": "certificate_n7_R2.txt"
    }
  ],
  "R1_ray_counts": [
    {
      "n": 4,
      "count": 2,
      "claimed": 2
    },
    {
      "n": 5,
      "count": 5,
      "claimed": 5
    },
    {
      "n": 6,
      "count": 6,
      "claimed": 6
    },
    {
      "n": 7,
      "count": 11,
      "claimed": 11
    },
    {
      "n": 8,
      "count": 12,
      "claimed": 12
    },
    {
      "n": 9,
      "count": 19,
      "claimed": 19
    },
    {
      "n": 10,
      "count": 20,
      "claimed": 20
    },
    {
      "n": 11,
      "count": 29,
      "claimed": 29
    },
    {
      "n": 12,
      "count": 30,
      "claimed": 30
    },
    {
      "n": 13,
      "count": 41,
      "claimed": 41
    },
    {
      "n": 14,
      "count": 42,
      "claimed": 42
    },
    {
      "n": 15,
      "count": 55,
      "claimed": 55
    },
    {
      "n": 16,
      "count": 56,
      "claimed": 56
    },
    {
      "n": 17,
      "count": 71,
      "claimed": 71
    },
    {
      "n": 18,
      "count": 72,
      "claimed": 72
    },
    {
      "n": 19,
      "count": 89,
      "claimed": 89
    },
    {
      "n": 20,
      "count": 90,
      "claimed": 90
    }
  ]
}
```

## 7. Cone proof and exact certificates — CORRECT for n=5,6,7; GAP in the submitted certificate for n=8,...,13

The reduction is valid. A nonzero sum-zero vector has positive and negative coordinates. After sorting, replace x by -x and reverse the order if x_1+x_n<0; this preserves Psi, T, and M. The normalised vector then lies in exactly one cone or their common boundary. Both M_1 and M_2 are products of an actual pair, so M>=M_i regardless of how many coordinates have either sign. The coefficient (n-1)((n^2-6n+6)T^2+2nQ) is strictly positive for n>=5, hence T^3 Psi>=G_{M_i}. No assumption about two negative coordinates is needed. If there is exactly one negative coordinate and at least two positive ones, x_1+x_n<0, so the sign change puts it in the single-positive regime in R_2. The edge case with zeros lies on the boundary.

Exact extreme-ray enumeration: in gap coordinates the order cone is the nonnegative orthant on n-1 generators v_i=((n-i)^i,(-i)^(n-i)). Intersect with the two extra homogeneous halfspaces. An extreme ray has support of size at most three: on a support of size k, at least k-1 independent extra constraints must be active. Enumerate all size-one supports, size-two supports with either constraint active, and size-three supports with both active. Solve by integer 2D perpendiculars and 3D cross products, retaining only positive supports satisfying both inequalities and removing duplicates after gcd scaling. This is exhaustive, including degenerate active constraints; zero coordinates are handled at smaller support sizes.

For R_1 one can prove the ray-count formula directly. Let p=s-1 for n=2s+1 or n=2s+2. On the gap generators, the first extra form has coefficients a_i=n-2i; the second has the same coefficients except b_1=-2 and b_(n-1)=2. There are p inner positive and p inner negative coefficients. Inner positive singletons contribute p rays (plus the middle zero singleton in the even case). Opposite inner signs contribute p^2 rays; first endpoint with an inner positive contributes p, inner positive with the last endpoint contributes p, and the two endpoints together contribute one. There are no support-three rays: a=b=0 forces equal endpoint coefficients, and no single remaining nonzero inner coefficient can cancel them; with no endpoints the two constraints coincide. Thus odd counts are p+p^2+2p+1=s^2+s-1; even counts add one, giving s^2+s. Exact enumeration agrees for n=4,...,20.

All six reproduced expansions have zero negative coefficients. Nonzero/zero counts are R1: 209/1, 461/1, 8007/1, and R2: 208/2, 460/2, 5003/2 for n=5,6,7. The full ray lists and all coefficients have been saved in certificate_n*_R*.txt. Each expansion was also evaluated at a positive integer coefficient vector and compared exactly with direct G evaluation.

The submitted line “For n = 5, ..., 13 none of these polynomials has a negative coefficient” is not accompanied by the program, ray lists, or certificates. Our independent n=5,6,7 checks support it, but do not verify n=8,...,13. This is a reproducibility gap in the finite part of the proof, fillable by supplying the exact checker and its outputs (including overflow checks for the claimed 128-bit route). It is not a counterexample to Psi>=0. No missing finite cases can be supplied by Theorem 6.1's n>=14 argument.

### Step 8: WRONG: final Section 5 state-matching claim; other cross-checks correct

Command: `nice -n 15 /Library/Frameworks/Python.framework/Versions/3.13/bin/python3 referee.py 8`. Numerical/exact output: `step8.json`.

```json
{
  "horizontal_strips": [
    {
      "n": 6,
      "tau": [
        2,
        2,
        1,
        1
      ],
      "sigma": [
        2,
        2,
        2
      ],
      "alphas": {
        "tau": [
          [
            2,
            1,
            1
          ]
        ],
        "sigma": [
          [
            2,
            2
          ]
        ]
      },
      "star_gaps": [
        5,
        6
      ],
      "star_ratio": 0.8333333333333334
    },
    {
      "n": 7,
      "tau": [
        3,
        2,
        1,
        1
      ],
      "sigma": [
        3,
        2,
        2
      ],
      "alphas": {
        "tau": [
          [
            2,
            1,
            1
          ]
        ],
        "sigma": [
          [
            2,
            2
          ]
        ]
      },
      "star_gaps": [
        4,
        4
      ],
      "star_ratio": 1.0
    },
    {
      "n": 8,
      "tau": [
        4,
        2,
        1,
        1
      ],
      "sigma": [
        4,
        2,
        2
      ],
      "alphas": {
        "tau": [
          [
            2,
            1,
            1
          ]
        ],
        "sigma": [
          [
            2,
            2
          ]
        ]
      },
      "star_gaps": [
        4,
        4
      ],
      "star_ratio": 1.0
    }
  ],
  "claimed_matching_state_counterexample": {
    "n": 5,
    "integer_vector": [
      1,
      1,
      0,
      0,
      -2
    ],
    "squared_norm": 6,
    "edge": [
      1,
      5
    ],
    "state_transposition_expectation": "-5/18",
    "prop21_lhs": "1/2",
    "prop21_rhs": "13/24",
    "violation": "1/24",
    "direct_matrix_expectation": -0.2777777777777779,
    "direct_lhs": 0.4999999999999998,
    "direct_rhs": 0.5416666666666665,
    "least_admissible_c": 0.1666666666666667,
    "graph_weights": [
      0.0,
      0.1666666666666667,
      0.1666666666666667,
      0.5000000000000001,
      0.1666666666666667,
      0.1666666666666667,
      0.5000000000000001,
      0.1666666666666667,
      0.1666666666666667,
      0.1666666666666667
    ]
  }
}
```

### Step 8: WRONG: final Section 5 state-matching claim; other cross-checks correct

Command: `nice -n 15 /Library/Frameworks/Python.framework/Versions/3.13/bin/python3 referee.py 8`. Numerical/exact output: `step8.json`.

```json
{
  "horizontal_strips": [
    {
      "n": 6,
      "tau": [
        2,
        2,
        1,
        1
      ],
      "sigma": [
        2,
        2,
        2
      ],
      "alphas": {
        "tau": [
          [
            2,
            1,
            1
          ]
        ],
        "sigma": [
          [
            2,
            2
          ]
        ]
      },
      "star_gaps": [
        5,
        6
      ],
      "star_ratio": 0.8333333333333334
    },
    {
      "n": 7,
      "tau": [
        3,
        2,
        1,
        1
      ],
      "sigma": [
        3,
        2,
        2
      ],
      "alphas": {
        "tau": [
          [
            2,
            1,
            1
          ]
        ],
        "sigma": [
          [
            2,
            2
          ]
        ]
      },
      "star_gaps": [
        4,
        4
      ],
      "star_ratio": 1.0
    },
    {
      "n": 8,
      "tau": [
        4,
        2,
        1,
        1
      ],
      "sigma": [
        4,
        2,
        2
      ],
      "alphas": {
        "tau": [
          [
            2,
            1,
            1
          ]
        ],
        "sigma": [
          [
            2,
            2
          ]
        ]
      },
      "star_gaps": [
        4,
        4
      ],
      "star_ratio": 1.0
    }
  ],
  "claimed_matching_state_counterexample": {
    "n": 5,
    "integer_vector": [
      1,
      1,
      0,
      0,
      -2
    ],
    "squared_norm": 6,
    "edge": [
      1,
      5
    ],
    "state_transposition_expectation": "-5/18",
    "prop21_lhs": "1/2",
    "prop21_rhs": "13/24",
    "violation": "1/24",
    "direct_matrix_expectation": -0.2777777777777779,
    "direct_lhs": 0.4999999999999998,
    "direct_rhs": 0.5416666666666665,
    "least_admissible_c": 0.1666666666666667,
    "graph_weights": [
      0.0,
      0.1666666666666667,
      0.1666666666666667,
      0.5000000000000001,
      0.1666666666666667,
      0.1666666666666667,
      0.5000000000000001,
      0.1666666666666667,
      0.1666666666666667,
      0.1666666666666667
    ],
    "exact_direct_matrix_expectation": "-5/18",
    "exact_trace_AAstar": "2"
  }
}
```

## 8. Whole-note consistency — WRONG in one additional claim; principal proof chain otherwise consistent subject to the finite certificate gap

The sentence “In the terms of Proposition 2.1, the state matched to the top eigenvector x of L_G is A A^*/tr(A A^*), the image of the uniform state on {1, x}^perp” claims more than was proved, and is false if “matched” has its stated transposition-by-transposition meaning.

Counterexample: n=5, x=(1,1,0,0,-2)/sqrt(6), and the pair (1,5). For D=A A^*/tr(A A^*), an exact rational matrix construction gives tr(A A^*)=2 and tr(D rho_[3,2]((1 5)))=-5/18. In the sign-twisted modules of Conjecture F, Proposition 2.1 requires

    2-(x_1-x_5)^2 >= (3/4)(1+tr(D rho_[3,2]((1 5)))),

which is 1/2 >= 13/24, false by 1/24. The direct matrix calculation was performed independently of the scalar trace formula, both numerically and with rational Sympy matrices. This x is the actual top eigenvector of the admissible graph c=1/6,g=1, so restricting the sentence to the graph family does not rescue it. Lemma 5.4 proves a weighted average inequality for that family, which is sufficient for Theorem 5.3; it does not prove the individual inequalities of Proposition 2.1. Delete or weaken the sentence. This is not a counterexample to Theorems 5.2 or 5.3.

Section 1's numbering, constants, partitions and stated equality cases agree with the later theorems. The star's nonzero ratio proves sharpness; the single edge gives degenerate equality 0=0. The family has generic dimension (n-2)+2=n. The abstract omits the degenerate boundary cases that Theorem 5.2 includes, which is harmless if read as a narrower description. A standalone Lemma 5.4 should explicitly say n>=5. Its literal all-n reading fails to define R at the balanced n=4 vector.

Proposition 3.1 follows from Lemma 3.2 even when eigenvalues vanish: for ordered eigenvalues, sum_{i=1}^j lambda_i/j <= lambda_j <= lambda_(j+1) <= ... <= lambda_k. Averaging the last k-j entries with the first j cannot decrease the mean. There is no division by an eigenvalue and no positivity assumption beyond the setting.

The Littlewood-Richardson restriction formula in Section 7 is right. For connected G_2 every nontrivial irreducible has a strictly positive interchange Laplacian: zero energy would give a vector fixed by all edge transpositions, which generate the symmetric group. Scaling G_2 therefore leaves only beta=[n-k]. Pieri's rule gives c^nu_{alpha,[n-k]}=1 exactly for horizontal strips, equivalently nu_i>=alpha_i>=nu_(i+1). This proves the displayed limit inequality when the indexing sets are nonempty; otherwise one needs the usual min(empty)=+infinity convention.

For the named pairs, k=4 and n=6,7,8. In tau=(n-4,2,1,1), interlacing forces alpha_1>=2, alpha_2>=1, alpha_3>=1, and sum alpha=4, hence alpha=211 only. In sigma=(n-4,2,2), it forces alpha_1>=2 and alpha_2>=2, hence alpha=22 only. Thus the fast-component limit is the 4-vertex ratio 2/3 in all three cases. On the full n-vertex star the gaps are (5,6), (4,4), (4,4), so the ratios are 5/6,1,1, each larger than 2/3. The listed n=5 open pairs are also the remaining dominance pairs after the hook, standard and sign cases are removed.

The numerical-evidence sentence should say “smallest ratios found,” rather than suggest that local search establishes global least ratios. The unsupplied exact finite certificates remain the only outstanding dependency for the main theorem chain, apart from external cited results not being re-refereed here.

Audit correction to step 3: a second derivation of the complete-graph case gives RHS of (5.1) equal to mu(3n-4)/n, not 3mu(n-2)/(n-1) as written in the earlier log entry. Indeed c=mu/n, 2W=mu(n-1), and lambda_max(G,[n-2,2])=2mu(n-1)/n. The corrected value is >=mu for n>=2, so the conclusion and the equivalence proof are unchanged.

Step 7 extension: attempting to fill the remaining finite gap with a streaming polarization checker. Prepared exact rays for n=5,...,13 and proved integer-overflow bounds in certificate_bounds.json. The checker stores only degree-2/3/4 moment lookups and streams the degree-six coefficients; maximum lookup memory is 23184352 bytes. Every run has a 270-second alarm.

Step 7 exact extension: {"n":5,"cone":1,"rays":5,"monomials":210,"negative":0,"zero":1,"min_nonzero":"96","max":"1247400","sum_coefficients":"36624640","sum_check":true,"seconds":0.000334959}

Step 7 exact extension: {"n":5,"cone":2,"rays":5,"monomials":210,"negative":0,"zero":2,"min_nonzero":"96","max":"511440","sum_coefficients":"15247216","sum_check":true,"seconds":0.000322}

Step 7 exact extension: {"n":6,"cone":1,"rays":6,"monomials":462,"negative":0,"zero":1,"min_nonzero":"240","max":"5375232","sum_coefficients":"322851816","sum_check":true,"seconds":0.000438}

Step 7 exact extension: {"n":6,"cone":2,"rays":6,"monomials":462,"negative":0,"zero":2,"min_nonzero":"240","max":"5223168","sum_coefficients":"294780320","sum_check":true,"seconds":0.00042}

Step 7 exact extension: {"n":7,"cone":1,"rays":11,"monomials":8008,"negative":0,"zero":1,"min_nonzero":"480","max":"910139328","sum_coefficients":"382192888896","sum_check":true,"seconds":0.00651425}

Step 7 exact extension: {"n":7,"cone":2,"rays":10,"monomials":5005,"negative":0,"zero":2,"min_nonzero":"480","max":"147957120","sum_coefficients":"53932461600","sum_check":true,"seconds":0.00751667}

Step 7 exact extension: {"n":8,"cone":1,"rays":12,"monomials":12376,"negative":0,"zero":1,"min_nonzero":"840","max":"2380627968","sum_coefficients":"1339181805168","sum_check":true,"seconds":0.000924417}

Step 7 exact extension: {"n":8,"cone":2,"rays":11,"monomials":8008,"negative":0,"zero":2,"min_nonzero":"840","max":"753235968","sum_coefficients":"295216411968","sum_check":true,"seconds":0.000622917}

Step 7 exact extension: {"n":9,"cone":1,"rays":19,"monomials":134596,"negative":0,"zero":1,"min_nonzero":"1344","max":"46443510432","sum_coefficients":"163290489204896","sum_check":true,"seconds":0.0220656}

Step 7 exact extension: {"n":9,"cone":2,"rays":17,"monomials":74613,"negative":0,"zero":2,"min_nonzero":"1344","max":"21213125184","sum_coefficients":"37157377464912","sum_check":true,"seconds":0.00516104}

Step 7 exact extension: {"n":10,"cone":1,"rays":20,"monomials":177100,"negative":0,"zero":1,"min_nonzero":"2016","max":"93944475648","sum_coefficients":"376709366572992","sum_check":true,"seconds":0.017493}

Step 7 exact extension: {"n":10,"cone":2,"rays":18,"monomials":100947,"negative":0,"zero":2,"min_nonzero":"2016","max":"49551224832","sum_coefficients":"93059092196424","sum_check":true,"seconds":0.0124938}

Step 7 exact extension: {"n":11,"cone":1,"rays":29,"monomials":1344904,"negative":0,"zero":1,"min_nonzero":"2880","max":"867947775552","sum_coefficients":"30137895270029184","sum_check":true,"seconds":0.0952}

Step 7 exact extension: {"n":11,"cone":2,"rays":26,"monomials":736281,"negative":0,"zero":2,"min_nonzero":"2880","max":"397162734672","sum_coefficients":"5555536113759296","sum_check":true,"seconds":0.0503417}

Step 7 exact extension: {"n":12,"cone":1,"rays":30,"monomials":1623160,"negative":0,"zero":1,"min_nonzero":"3960","max":"1331192045568","sum_coefficients":"29781633228573240","sum_check":true,"seconds":0.111265}

Step 7 exact extension: {"n":12,"cone":2,"rays":27,"monomials":906192,"negative":0,"zero":2,"min_nonzero":"3960","max":"966116849664","sum_coefficients":"10603942964221952","sum_check":true,"seconds":0.0672342}

Step 7 exact extension: {"n":13,"cone":1,"rays":41,"monomials":9366819,"negative":0,"zero":1,"min_nonzero":"5280","max":"7377981510432","sum_coefficients":"1835427550035745152","sum_check":true,"seconds":0.645169}

Step 7 exact extension: {"n":13,"cone":2,"rays":37,"monomials":5245786,"negative":0,"zero":2,"min_nonzero":"5280","max":"4601973292704","sum_coefficients":"420738494349887280","sum_check":true,"seconds":0.432864}

### Step 7audit: CORRECT for the full n=5,...,13 range; earlier certificate GAP filled independently

Command: `nice -n 15 /Library/Frameworks/Python.framework/Versions/3.13/bin/python3 referee.py 7audit`. Numerical/exact output: `step7audit.json`.

```json
{
  "all_coefficient_comparisons": [
    {
      "n": 5,
      "cone": 1,
      "all_coefficients_agree": true,
      "nonzero_coefficients": 209
    },
    {
      "n": 5,
      "cone": 2,
      "all_coefficients_agree": true,
      "nonzero_coefficients": 208
    },
    {
      "n": 6,
      "cone": 1,
      "all_coefficients_agree": true,
      "nonzero_coefficients": 461
    },
    {
      "n": 6,
      "cone": 2,
      "all_coefficients_agree": true,
      "nonzero_coefficients": 460
    },
    {
      "n": 7,
      "cone": 1,
      "all_coefficients_agree": true,
      "nonzero_coefficients": 8007
    },
    {
      "n": 7,
      "cone": 2,
      "all_coefficients_agree": true,
      "nonzero_coefficients": 5003
    }
  ],
  "full_finite_range": [
    {
      "n": 5,
      "cone": 1,
      "rays": 5,
      "monomials": 210,
      "negative": 0,
      "zero": 1,
      "min_nonzero": "96",
      "max": "1247400",
      "sum_coefficients": "36624640",
      "sum_check": true,
      "seconds": 0.000334959
    },
    {
      "n": 5,
      "cone": 2,
      "rays": 5,
      "monomials": 210,
      "negative": 0,
      "zero": 2,
      "min_nonzero": "96",
      "max": "511440",
      "sum_coefficients": "15247216",
      "sum_check": true,
      "seconds": 0.000322
    },
    {
      "n": 6,
      "cone": 1,
      "rays": 6,
      "monomials": 462,
      "negative": 0,
      "zero": 1,
      "min_nonzero": "240",
      "max": "5375232",
      "sum_coefficients": "322851816",
      "sum_check": true,
      "seconds": 0.000438
    },
    {
      "n": 6,
      "cone": 2,
      "rays": 6,
      "monomials": 462,
      "negative": 0,
      "zero": 2,
      "min_nonzero": "240",
      "max": "5223168",
      "sum_coefficients": "294780320",
      "sum_check": true,
      "seconds": 0.00042
    },
    {
      "n": 7,
      "cone": 1,
      "rays": 11,
      "monomials": 8008,
      "negative": 0,
      "zero": 1,
      "min_nonzero": "480",
      "max": "910139328",
      "sum_coefficients": "382192888896",
      "sum_check": true,
      "seconds": 0.00651425
    },
    {
      "n": 7,
      "cone": 2,
      "rays": 10,
      "monomials": 5005,
      "negative": 0,
      "zero": 2,
      "min_nonzero": "480",
      "max": "147957120",
      "sum_coefficients": "53932461600",
      "sum_check": true,
      "seconds": 0.00751667
    },
    {
      "n": 8,
      "cone": 1,
      "rays": 12,
      "monomials": 12376,
      "negative": 0,
      "zero": 1,
      "min_nonzero": "840",
      "max": "2380627968",
      "sum_coefficients": "1339181805168",
      "sum_check": true,
      "seconds": 0.000924417
    },
    {
      "n": 8,
      "cone": 2,
      "rays": 11,
      "monomials": 8008,
      "negative": 0,
      "zero": 2,
      "min_nonzero": "840",
      "max": "753235968",
      "sum_coefficients": "295216411968",
      "sum_check": true,
      "seconds": 0.000622917
    },
    {
      "n": 9,
      "cone": 1,
      "rays": 19,
      "monomials": 134596,
      "negative": 0,
      "zero": 1,
      "min_nonzero": "1344",
      "max": "46443510432",
      "sum_coefficients": "163290489204896",
      "sum_check": true,
      "seconds": 0.0220656
    },
    {
      "n": 9,
      "cone": 2,
      "rays": 17,
      "monomials": 74613,
      "negative": 0,
      "zero": 2,
      "min_nonzero": "1344",
      "max": "21213125184",
      "sum_coefficients": "37157377464912",
      "sum_check": true,
      "seconds": 0.00516104
    },
    {
      "n": 10,
      "cone": 1,
      "rays": 20,
      "monomials": 177100,
      "negative": 0,
      "zero": 1,
      "min_nonzero": "2016",
      "max": "93944475648",
      "sum_coefficients": "376709366572992",
      "sum_check": true,
      "seconds": 0.017493
    },
    {
      "n": 10,
      "cone": 2,
      "rays": 18,
      "monomials": 100947,
      "negative": 0,
      "zero": 2,
      "min_nonzero": "2016",
      "max": "49551224832",
      "sum_coefficients": "93059092196424",
      "sum_check": true,
      "seconds": 0.0124938
    },
    {
      "n": 11,
      "cone": 1,
      "rays": 29,
      "monomials": 1344904,
      "negative": 0,
      "zero": 1,
      "min_nonzero": "2880",
      "max": "867947775552",
      "sum_coefficients": "30137895270029184",
      "sum_check": true,
      "seconds": 0.0952
    },
    {
      "n": 11,
      "cone": 2,
      "rays": 26,
      "monomials": 736281,
      "negative": 0,
      "zero": 2,
      "min_nonzero": "2880",
      "max": "397162734672",
      "sum_coefficients": "5555536113759296",
      "sum_check": true,
      "seconds": 0.0503417
    },
    {
      "n": 12,
      "cone": 1,
      "rays": 30,
      "monomials": 1623160,
      "negative": 0,
      "zero": 1,
      "min_nonzero": "3960",
      "max": "1331192045568",
      "sum_coefficients": "29781633228573240",
      "sum_check": true,
      "seconds": 0.111265
    },
    {
      "n": 12,
      "cone": 2,
      "rays": 27,
      "monomials": 906192,
      "negative": 0,
      "zero": 2,
      "min_nonzero": "3960",
      "max": "966116849664",
      "sum_coefficients": "10603942964221952",
      "sum_check": true,
      "seconds": 0.0672342
    },
    {
      "n": 13,
      "cone": 1,
      "rays": 41,
      "monomials": 9366819,
      "negative": 0,
      "zero": 1,
      "min_nonzero": "5280",
      "max": "7377981510432",
      "sum_coefficients": "1835427550035745152",
      "sum_check": true,
      "seconds": 0.645169
    },
    {
      "n": 13,
      "cone": 2,
      "rays": 37,
      "monomials": 5245786,
      "negative": 0,
      "zero": 2,
      "min_nonzero": "5280",
      "max": "4601973292704",
      "sum_coefficients": "420738494349887280",
      "sum_check": true,
      "seconds": 0.432864
    }
  ],
  "max_lookup_bytes": 23184352,
  "maximum_integer_bound": 2711711312504248214160,
  "signed128_limit": 170141183460469231731687303715884105727
}
```

## 7. Final verdict after extending the certificate: CORRECT

The earlier finite-case GAP has now been filled, including every n=8,...,13 case. This supersedes the earlier provisional verdict; it does not change the false state-matching claim in step 8. Every coefficient is nonnegative for both cones throughout n=5,...,13.

The extension avoids storing degree-six polynomials. For six labelled ray vectors r_a,...,r_f, the coefficient of the product of six distinct scalar variables in G is its sixth directional derivative. Divide by the product of factorials of repeated ray multiplicities to obtain the ordinary monomial coefficient. Put D2(a,b)=sum_i r_ai r_bi, D3(a,b,c)=sum_i r_ai r_bi r_ci, D4(a,b,c,d)=sum_i r_ai r_bi r_ci r_di, and H(a,b)=r_au r_bv+r_bu r_av, where (u,v)=(1,2) or (n,n-1).

Sum over the 15 choices of a pair among six positions, with the four complementary positions in increasing order. For the complement write J=D2(c,d)D2(e,f)+D2(c,e)D2(d,f)+D2(c,f)D2(d,e). Define B_QT=sum D2(a,b)D4(c,d,e,f), B_TTT=sum D2(a,b)J, B_TTM=sum H(a,b)J, B_QM=sum H(a,b)D4(c,d,e,f). Also B_PP is the sum over the ten unordered partitions into two triples of D3(a,b,c)D3(d,e,f). Then the numerator of each coefficient is

    (n-4)(96 B_QT - 16 B_TTT) - 144(n-3) B_PP
      + 8(n-1)(n^2-6n+6) B_TTM + 48n(n-1) B_QM.

The factors follow from differentiating Q (4!), P (3!), T (2!), and the two labelled factors in each product. In B_TTT each perfect matching is counted three times, producing the factor 16 instead of 48. This is an exact coefficient formula, not sampling. The checker enumerates all binom(r+5,6) multisets of six rays, checks divisibility by the repetition factorial, and counts every sign. For n=5,6,7 its entire coefficient dictionaries agree with the independent Python polynomial multiplication, coefficient by coefficient (not just in totals). For every n it also checks the sum of coefficients against G evaluated directly at all ray coefficients equal to one.

Commands for the extension:

    nice -n 15 /Library/Frameworks/Python.framework/Versions/3.13/bin/python3 referee.py 7prep
    nice -n 15 /usr/bin/clang++ -O2 -std=c++17 certificate_stream.cpp -o certificate_stream
    nice -n 15 ./certificate_stream rays_nN_RC.input
    nice -n 15 /Library/Frameworks/Python.framework/Versions/3.13/bin/python3 referee.py 7audit

The third command was run separately and serially for each N=5,...,13 and C=1,2. Each completed command appended its exact summary to this log and saved rays_nN_RC.input.json. The largest coefficient pass took 0.646 seconds of its own wall clock. The largest lookup allocation is 23,184,352 bytes. Explicit unbounded-integer bounds, saved before execution, put even the sum of absolute coefficient numerators below 2.712e21, whereas signed 128-bit capacity is approximately 1.701e38. Lookup moments fit signed 64-bit integers. Thus neither memory nor fixed-width overflow is an unresolved issue in this independent certificate.

The main mathematical arguments for Theorems 5.2 and 5.3 are SOUND, using the independently supplied finite certificate and the previously refereed n>=14 argument. As submitted, the author should attach a reproducible certificate/checker and delete or correct the false state-matching sentence. No counterexample to either theorem was found.

## Report written

REPORT.md now contains all eight final verdicts, the exact counterexample to the auxiliary matching claim, reproducible commands and numerical tables, the completed finite certificate counts, limitations, and SOUND verdicts for Theorems 5.2 and 5.3. The original note was left unchanged. All files produced remain inside this folder.

Final artifact audit: all REPORT.md links resolve; all 18 finite certificates report zero negatives; all six independent coefficient dictionaries agree. No remaining requested computation is running.
