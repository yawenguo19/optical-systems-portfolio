# ============================================================
# Example: point-to-point optical link budget
# ============================================================
from optical_systems.validation import LinkBudget

def print_report(result)->None:
    """
    Print a formatted engineering report
    """
    print("="*50)
    print("Print Link Budget Report")
    print("="*50)

    print(f"Fiber loss          : {result.fiber_loss_db:.2f} dB")
    print(f"Total loss          : {result.total_loss_db:.2f} dB")
    print(f"Receiver power      : {result.receiver_power_dbm:.2f} dBm")
    print(f"Available margin    : {result.available_margin_db:.2f} dB")
    print(f"Net margin          : {result.net_margin_db:.2f} dB")
    print(f"Status              : {result.status}")

    print("="*50)

def main()->None:
    link = LinkBudget(
        tx_power_dbm = 3.0,
        fiber_length_km = 40.0,
        fiber_attenuation_db_per_km = 0.22,
        connector_loss_db = 1.0,
        receiver_sensitivity_dbm = -16.0,
        required_margin_db = 3.0,
    )

    result = link.evaluate()
    print_report(result)

if __name__ == "__main__":
    main()
