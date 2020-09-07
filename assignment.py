import pytest

# Black box model
# 1. Calculate the specific yield coefficients (C-mol) for all products.

# Add your calculations here ...

# Assign your solutions to the following variables (replace _ with your solutions)
Y_xs = _
Y_xe = _
Y_xg = _

def test_Y_xs():
    assert Y_xs == pytest.approx(6.09) # C-mol

def test_Y_xe():
    assert Y_xe == pytest.approx(3.9) # C-mol

def test_Y_xg():
    assert Y_ge == pytest.approx(0.45) # C-mol
  

# 2. Calculate the carbon balance. Does it close?

# Add your calculations here ...

# Assign your solution to the following variable (replace _ with your solution)
carbon_balance = _

def test_carbon_balance():
    assert carbon_balance == pytest.approx(-0.74) # C-mol
    

# 3. Assuming that CO2 is the only missing product, calculate how much CO2 was produced in the fermentation.

# Add your calculations here ...

# Assign your solution to the following variable (replace _ with your solution)
co2_produced = _

def test_co2_produced():
    assert co2_produced == pytest.approx(3.58) # g-CO2/l
    
