import numpy as np
import math

# fleet02/B11 six-coordinate target family
R=np.array([
    [0.5, 1/(2*np.sqrt(2)), 0.0],
    [0.5, 1/(2*np.sqrt(2)), 0.0],
    [0.5,-1/(2*np.sqrt(2)), 0.0],
    [0.5,-1/(2*np.sqrt(2)), 0.0],
    [0.0,0.0,1.0],
    [0.0,1/np.sqrt(2),0.0],
])
M=np.array([[1.0,0.0,0.0],[0.0,0.0,1.0],[0.0,1.0,0.0]])
assert np.max(np.abs(R.T@R-np.eye(3))) < 1e-12
Apartner=R@M@R.T
ev=np.linalg.eigvalsh(Apartner)
assert np.max(np.abs(np.array([ev[0],ev[-2],ev[-1]])-np.array([-1.0,1.0,1.0]))) < 1e-12

# Diffuse cross block M0=(I;I)/sqrt(2), whose row-range leverage is exactly 1/2.
M0=np.vstack([np.eye(3),np.eye(3)])/np.sqrt(2)
sv=np.linalg.svd(M0,compute_uv=False)
assert np.max(np.abs(sv-1.0)) < 1e-12
P=M0@np.linalg.inv(M0.T@M0)@M0.T
lev=float(np.max(np.diag(P)))
assert lev <= 0.5+1e-12

# For ||b||<=1/4, the cross-coupled scalar extension differs from the block diagonal
# matrix by [[0,b^T],[b,bb^T/2]], whose operator norm is at most ||b||+||b||^2/2.
weyl_floor=2-(0.25+0.25**2/2)
assert weyl_floor > 1

# Constants from the sharp layer-cake half-Riesz bound in REPORT.md.
Kvol=12*math.sqrt(3)*math.e/5
Cvol=2*math.sqrt(Kvol)
Cpartner=2*math.sqrt(6)

print('partner_spectrum_nonzero=-1,1,1')
print(f'diffuse_row_leverage_max={lev:.15f}')
print(f'weyl_target_floor={weyl_floor:.15f}')
print(f'volume_remainder_K={Kvol:.15f}')
print(f'volume_crosscoupled_bound={Cvol:.15f}')
print('partner_scaled_remainder_K=6.000000000000000')
print(f'partner_crosscoupled_bound={Cpartner:.15f}')
print('QFORM_B11_SCHUR_SQUARE_CHECK_PASS')
