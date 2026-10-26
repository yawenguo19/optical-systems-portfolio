import pytest

from optical_systems.validation import LinkBudget

def test_basic_link_budget():
    link = LinkBudget(
        tx_power_dbm=3.0,
        fiber_length_km=40.0,
        fiber_attenuation_db_per_km=0.22,
        connector_loss_db=1.0,
        receiver_sensitivity_dbm=-16.0,
        required_margin_db=3.0,
    )
    result = link.evaluate()

    assert result.fiber_loss_db == pytest.approx(8.8)

def test_link_budget_fail():
    link = LinkBudget(
        tx_power_dbm= 0.0,
        fiber_length_km= 100.0,
        fiber_attenuation_db_per_km= 0.22,
        connector_loss_db= 2.0,
        receiver_sensitivity_dbm= -16.0,
        required_margin_db= 3.0,
    )
    result = link.evaluate()

    assert result.net_margin_db == pytest.approx(-11.0)
    assert result.status == "FAIL"

def test_negative_fiber_length():
    with pytest.raises(ValueError):
        LinkBudget(
            tx_power_dbm=3.0,
            fiber_length_km= -10.0,
            fiber_attenuation_db_per_km= 0.22,
        )
