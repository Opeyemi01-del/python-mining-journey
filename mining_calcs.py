# [a mining calculations module (mining_calcs.py) with functions for tonnage (volume × density),
# contained metal (tonnage × grade), stripping ratio (waste ÷ ore),
# and head grade after dilution. Import it into a second script and 
# handle bad inputs like negative volumes.]

import math

def _validate_nonnegative(value: float, name: str) -> None:
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise TypeError(f'{name} must be a number')
    if not math.isfinite(value):
        raise ValueError(f'{name} must be finite')
    if value < 0:
        raise ValueError(f'{name} must be a positive value')


def _validate_grade(grade_pct: float, name: str) -> None:
    _validate_nonnegative(grade_pct, name)
    if grade_pct > 100:
        raise ValueError(f'{name} must be between 0 and 100')

def calculate_tonnage(volume_m3: float, density_tonnes_per_m3: float) -> float:
  """ return tonnage from volume in m3 and density in tonnes/m3"""
  _validate_nonnegative(volume_m3, "volume_m3")
  _validate_nonnegative(density_tonnes_per_m3, "density_tonnes_per_m3")
  if density_tonnes_per_m3 == 0:
      raise ValueError(f'density_tonnes_per_m3 must be greater than zero')
  return volume_m3 * density_tonnes_per_m3

def contained_metal(tonnage: float, grade_pct: float) -> float:
 """return contained metal tonnes; grade_pct is percentage points(e.g. 0.5 for 0.5%)"""
 _validate_nonnegative(tonnage, "tonnage" )
 _validate_nonnegative(grade_pct, "grade_pct")
 return tonnage * grade_pct / 100

def stripping_ratio(waste_tonnes: float, ore_tonnes: float) -> float:
    """return stripping ratio (waste ÷ ore)"""
    _validate_nonnegative(waste_tonnes, "waste_tonnes")
    _validate_nonnegative(ore_tonnes, "ore_tonnes")
    if ore_tonnes == 0:
        raise ValueError("ore_tonnes must be greater than zero")
    return waste_tonnes / ore_tonnes

def head_grade_after_dilution(
      ore_tonnes: float,
      ore_grades_pct: float,
      dilution_tonnes: float,
      dilution_grade_pct: float
)-> float:
   _validate_nonnegative(ore_tonnes, "ore_tonnes")
   _validate_grade(ore_grades_pct, "ore_grade_pct")
   _validate_nonnegative(dilution_tonnes, "dilution_tonnes")
   _validate_grade(dilution_grade_pct,"dilution_grade_pct")
   total_tonnes = dilution_tonnes + ore_tonnes
   if total_tonnes == 0:
      raise ValueError(f'{total_tonnes} is invalid')
   return(
      ore_tonnes * ore_grades_pct + dilution_tonnes *dilution_grade_pct
   ) / total_tonnes

