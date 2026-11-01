import math

eta = 1/512
tau = 1/64
delta = 7/32
sigma0 = delta - tau
gamma_q = sigma0 / math.sqrt(2)
lev_q = (1/math.sqrt(7) + tau/gamma_q)**2
theta_q = sigma0**2/(gamma_q**2 + sigma0**2)
beta_q = theta_q/2
c14 = math.gamma(3/4)*math.sin(math.pi/8)/math.pi
L1 = math.pi*math.e*math.sqrt(2)
C_diff_quarter = 32*c14*(L1/(2*gamma_q))**0.25

K11 = 3.663273516008612
C_diag = 2**(7/4)*eta**(-1/4)
C_cross = K11*eta**(-1/4)
cmin = eta/math.sqrt(2)
C_diag_partner = 2**(7/4)*(cmin/2)**(-1/4)
C_face = 4*(1-1/math.sqrt(2))**(-1/8)*cmin**(-1/4)

gamma2 = sigma0/2
lev2 = (1/math.sqrt(7) + tau/gamma2)**2
theta2 = 2*sigma0**2/(gamma2**2+sigma0**2)
C_sqdiff = (
    8*3**(-5/8)*math.e**0.25
    * math.sqrt(3*theta2/(3*theta2-4))
    / math.sqrt((1/312)*gamma2)
)

C_half_second = 4*math.sqrt(2)*eta**(-1/4)*25
C_full_second = math.sqrt(312)*C_half_second

Delta_min = (1-1/math.sqrt(2))*cmin**2
C_half_face = 8*Delta_min**(-1/4)
C_full_face = math.sqrt(312)*C_half_face

vals = {
    "quarter_diffuse_ridge_leverage": lev_q,
    "quarter_diffuse_theta_lower": theta_q,
    "quarter_diffuse_constant": C_diff_quarter,
    "quarter_heavy_diagonal_constant": C_diag,
    "quarter_diffuse_bank_constant": C_cross,
    "quarter_partner_diagonal_constant": C_diag_partner,
    "quarter_indefinite_face_constant": C_face,
    "two_direction_ridge_leverage": lev2,
    "two_direction_theta_lower": theta2,
    "square_residual_diffuse_density_constant": C_sqdiff,
    "second_scalar_full_density_constant": C_full_second,
    "localized_face_full_density_constant": C_full_face,
    "partner_null_heavy_constant": 6*math.e**(2/3),
}
for k,v in vals.items():
    print(f"{k}={v:.15f}")

assert lev_q < 0.5
assert theta_q >= 2/3 - 1e-15
assert C_diff_quarter < 12.164
assert max(C_diag, C_cross, C_diag_partner, C_face) < 25
assert lev2 < 0.5
assert theta2 >= 8/5 - 1e-15
assert C_sqdiff < 702
assert C_full_second < 11883
assert C_full_face < 5169
assert 6*math.e**(2/3) < 11.687
print("QFORM_ONE_EIGEN_QUARTER_RIESZ_CHECK_PASS")
