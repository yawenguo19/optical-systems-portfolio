"""
Optical link-budget models.

This module provides a simple point-to-point optical link-budget model
for calculating fiber loss, total link loss, receiver power, available
margin, net margin, and pass/fail status.
"""

from dataclasses import dataclass
from typing import Literal

LinkStatus = Literal["PASS", "FAIL"]

@dataclass(frozen = True)
class LinkBudgetResult:
    """
    Calculated results for an optical link budget.
    """
    fiber_loss_db: float
    total_loss_db: float
    receiver_power_dbm: float
    available_margin_db: float
    net_margin_db: float
    status: str


@dataclass(frozen = True)
class LinkBudget:
    """
    Parameters and calculations for a point-to-point optical link.

    Parameters
    ----------
    tx_power_dbm:
        Optical transmitter output power in dBm.
    fiber_length_km:
        Fiber length in kilometers.
    fiber_attenuation_db_per_km:
        Fiber attenuation coefficient in dB/km.
    connector_loss_db:
        Total connector loss across the link in dB.
    additional_loss_db:
        Additional fixed insertion loss in dB.
    receiver_sensitivity_dbm:
        Minimum receiver input power required for operation, in dBm.
    required_margin_db:
        Additional engineering margin required for the link, in dB.
    """
    tx_power_dbm: float
    fiber_length_km: float
    fiber_attenuation_db_per_km: float
    connector_loss_db: float = 0.0
    additional_loss_db: float = 0.0
    receiver_sensitivity_dbm: float = -16.0
    required_margin_db: float = 0.0

    def __post_init__(self)->None:
        """
        Validate physical input parameter
        """
        non_negative_parameters = {
            "fiber_length_km": self.fiber_length_km,
            "fiber_attenuation_db_per_km": self.fiber_attenuation_db_per_km,
            "connector_loss_db": self.connector_loss_db,
            "additional_loss_db": self.additional_loss_db,
            "requied_margin_db": self.required_margin_db,

        }
        for name, value in non_negative_parameters.items():
            if value<0:
                raise ValueError(f"{name} must be non-negative")


    def fiber_loss_db(self)->float:
        """
        return accumulated fiber attenuation in db
        """
        return (self.fiber_length_km * self.fiber_attenuation_db_per_km)

    def total_loss_db(self)->float:
        """
        return total passive link loss in db
        """
        return (self.fiber_loss_db() + self.connector_loss_db + self.additional_loss_db)

    def received_power_dbm(self)->float:
        """
        return optical power delivered to the receiver in dbm
        """
        return (self.tx_power_dbm - self.total_loss_db())

    def available_margin_db(self)->float:
        """
        return received power margin before engineering margin
        """
        return (self.received_power_dbm() - self.receiver_sensitivity_dbm)

    def net_margin_db(self)->float:
        """
        return remianing margin after the required margin is applied
        """
        return (self.available_margin_db() - self.required_margin_db)

    def evaluate(self) ->LinkBudgetResult:
        """
        evaluate the optical link and return all calculated results.
        """
        fiber_loss = self.fiber_loss_db()
        total_loss = self.total_loss_db()
        received_power = self.received_power_dbm()
        available_margin = self.available_margin_db()
        net_margin = self.net_margin_db()

        status:LinkStatus = (
            "PASS" if net_margin>=0.0 else "FAIL"
        )

        return LinkBudgetResult(
            fiber_loss_db = fiber_loss,
            total_loss_db = total_loss,
            receiver_power_dbm = received_power,
            available_margin_db = available_margin,
            net_margin_db = net_margin,
            status = status,
        )


