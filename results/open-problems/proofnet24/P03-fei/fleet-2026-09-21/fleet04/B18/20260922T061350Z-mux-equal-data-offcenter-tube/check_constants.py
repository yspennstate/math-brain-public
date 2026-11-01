from decimal import Decimal, getcontext

getcontext().prec = 80
C = Decimal('6.521851214')
a = Decimal('0.268204856')

same_bracket = C - Decimal(6) - Decimal(45)/Decimal(224) - Decimal('0.135')/(Decimal(224)**2)
same_reserve_per_m = same_bracket / 2
center_R = (C-Decimal(6))/2 * (Decimal(1)-Decimal(1)/(Decimal(224)**2))
center_J = Decimal('58.440217') / Decimal(448)
center_reserve = center_R - center_J

K = Decimal(8192)
entropy_loss_per_m = (Decimal('2.5')/K) * Decimal('17.5')
address_loss_per_m = Decimal(67)/K
data_output_loss_per_m = Decimal(164)/(K*Decimal(224))
total_loss_per_m = entropy_loss_per_m + address_loss_per_m + data_output_loss_per_m
remaining_per_m = Decimal('0.13') - total_loss_per_m

print('same_bracket =', same_bracket)
print('same_reserve_per_m =', same_reserve_per_m)
print('center_R =', center_R)
print('center_J =', center_J)
print('center_reserve =', center_reserve)
print('entropy_loss_per_m =', entropy_loss_per_m)
print('address_loss_per_m =', address_loss_per_m)
print('data_output_loss_per_m =', data_output_loss_per_m)
print('total_loss_per_m =', total_loss_per_m)
print('remaining_per_m =', remaining_per_m)

assert same_reserve_per_m > Decimal('0.16')
assert center_reserve > Decimal('0.13')
assert total_loss_per_m < Decimal(1)/Decimal(64)
assert remaining_per_m > Decimal('0.1')
print('PASS')
