# [a mining calculations module (mining_calcs.py) with functions for tonnage (volume × density),
# contained metal (tonnage × grade), stripping ratio (waste ÷ ore),
# and head grade after dilution. Import it into a second script and 
# handle bad inputs like negative volumes.]
 

from mining_calcs import (
    contained_metal,
    calculate_tonnage,
    stripping_ratio,
    head_grade_after_dilution
)

volume_m3 = 10,000
density_tonnes_per_m3 = 2.7
ore_tonnes = calculate_tonnage(10000,2.7)
grade_pct = 0.6


print(f' ore tonness is {ore_tonnes:,.0f} tonnes')
print(f'contained metal is {contained_metal(ore_tonnes, grade_pct):.2f} tonnes')
print(f'stripping ratio = {stripping_ratio(1500000, ore_tonnes):.2f}:1')
print(
    "head grade after dilution = "
    f'{head_grade_after_dilution(ore_tonnes,grade_pct, 250000, 0.45):.3f}'
)

try:
    ore_tonnes
except ValueError as error:
    print(f'invalid input {error}')
    

































