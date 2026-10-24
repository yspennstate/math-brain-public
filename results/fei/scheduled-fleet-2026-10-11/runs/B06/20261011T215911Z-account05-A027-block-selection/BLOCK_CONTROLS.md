# Frozen data-first rule and controls

Input is an explicitly represented activation F=1+A_r(u-1) with r>=1 fresh physical controls. Query all core coordinates in one block, uniformly over their actual physical assignments; stop without further queries. This is a deterministic special case of a history-measurable proper-block rule. It is not an assertion of adaptive universality. Leaves are constant or D_r=1-2A_r and have their own proved entropy bound. The rule does not inspect a spectral sample to choose the block.

## Coded plateau

For even k>=2 let b be the k-bit quadratic bent function and let u(x,t)=b(x_1+t,...,x_k+t), with binary addition. Its spectrum is uniform on an even-parity code of size 2^k. Thus H(u)=k, every singleton erasure is zero, and I(u)=(k+1)/2. Zero erasure alone does not pay those k bits. Apply the data-first block to F=1+A_r(u-1): m=k+1, eta=1/2, B_W<=12 I_W, every leaf is a point defect, and the complete constant is 12+2/ln2, independently of k and r. In particular influence of F tends to zero with rarity. This is a quantified proper-block payment on a coded plateau, not a new claim that parity-coded spectra are universally easy. Exact fixtures k=2,4,6 verify parity support, entropy, influence and zero singleton erasure.

## Bent marker and sparse B05 obstruction

Take k even and b'=b-2*1_{x=0}. Let u(x,y) splice b and b'. Its core dimension is m=k+1, I(u)=k/2+(k+1)2^{-k} >= m/3 for k>=2. In fact the original k data coordinates contribute k/2+k2^{-k}, and the marker contributes 2^{-k}. Activating this core on r=2k controls is exactly the archived B05 obstruction. The data-first block includes x AND y and leaves only the controls. It yields B_W<=18 I_W and a complete constant 18+2/ln2. This pays the all-dimensional obstruction without a local marker bound, and without reusing control influence.

The bad singleton y still has B_y/Inf_y >= (1-2^{-k})(k-2) for k>=4. That archived theorem is retained. The proper block includes the dense core data coordinates; its budget is pI(u), much larger than the bad marker's p2^{-k}. Exact fixtures k=2,4,6 check the marker and core influence separately. No finite fixture replaces the source's all-k lower-bound proof.

## Scope and shortest next target

The core-density hypothesis m<=I(u)/eta is not hereditary. Arbitrary low-influence cores are excluded and are not assumed to be certified leaves. Formula (*) in ADAPTIVE_BLOCK_SELECTION.tex shows that universally paying this same full-core block is FEI-equivalent in finiteness, with explicit constants. Blindly removing the hypothesis is therefore not a new easier endpoint. The next rule should query a smaller physical core block when I(u)/m is small, keeping the actual restricted-core fiber entropy and all terminal costs. A point defect core is already a certified terminal; parity lifts of arbitrary seeds are not.

The exact scalar identity B_W/p in (*) is the reviewable interface to A028/A029/A065/A087/A097. It separates defect spectral entropy from the exceptional empty-control fiber and avoids paying an r-sized logarithm from a pI(u) budget. No independent review has yet occurred; no novelty clearance is claimed.
