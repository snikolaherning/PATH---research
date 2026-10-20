"""Five-year DCF, sensitivity grid, and reverse DCF for UiPath (PATH).

Uses only Python's standard library. Monetary amounts are USD millions except
per-share values. Edit the input block to test another set of assumptions.
"""

# ============================== EDITABLE INPUTS ==============================

STARTING_FCFF = 352.160
GROWTH_RATES = [0.12, 0.11, 0.10, 0.09, 0.08]
WACC = 0.11
TERMINAL_GROWTH = 0.03
NON_OPERATING_CASH = 1_405.0
DEBT = 0.0
DILUTED_SHARES = 523.013

WACC_SENSITIVITY = [0.09, 0.10, 0.11]
TERMINAL_GROWTH_SENSITIVITY = [0.02, 0.03, 0.04]

TARGET_SHARE_PRICE = 13.57
SHIFT_LOWER_BOUND = -0.05
SHIFT_UPPER_BOUND = 0.10
BISECTION_TOLERANCE = 0.0000001
BISECTION_MAX_ITERATIONS = 200

# ============================================================================


def calculate_dcf(growth_rates, wacc, terminal_growth):
    """Return the DCF outputs for one set of assumptions."""
    if terminal_growth >= wacc:
        raise ValueError("terminal growth must be less than WACC")
    if wacc <= -1.0:
        raise ValueError("WACC must be greater than -100%")
    if any(rate <= -1.0 for rate in growth_rates):
        raise ValueError("every annual growth rate must be greater than -100%")

    fcff_by_year = []
    fcff = STARTING_FCFF
    for growth_rate in growth_rates:
        fcff *= 1.0 + growth_rate
        fcff_by_year.append(fcff)

    pv_explicit_fcff = sum(
        yearly_fcff / (1.0 + wacc) ** year
        for year, yearly_fcff in enumerate(fcff_by_year, start=1)
    )
    terminal_value_year_5 = (
        fcff_by_year[-1] * (1.0 + terminal_growth)
        / (wacc - terminal_growth)
    )
    pv_terminal_value = terminal_value_year_5 / (1.0 + wacc) ** 5
    enterprise_value = pv_explicit_fcff + pv_terminal_value
    equity_value = enterprise_value + NON_OPERATING_CASH - DEBT
    value_per_share = equity_value / DILUTED_SHARES
    terminal_value_share = pv_terminal_value / enterprise_value

    return {
        "fcff_by_year": fcff_by_year,
        "pv_explicit_fcff": pv_explicit_fcff,
        "terminal_value_year_5": terminal_value_year_5,
        "pv_terminal_value": pv_terminal_value,
        "enterprise_value": enterprise_value,
        "equity_value": equity_value,
        "value_per_share": value_per_share,
        "terminal_value_share": terminal_value_share,
    }


def print_twelve_lines(result):
    """Print the required twelve-line DCF output."""
    lines = [
        *(f"FCFF Year {year}: {value:,.4f}"
          for year, value in enumerate(result["fcff_by_year"], 1)),
        f"PV of explicit FCFF: {result['pv_explicit_fcff']:,.4f}",
        f"Terminal value, Year 5: {result['terminal_value_year_5']:,.4f}",
        f"PV of terminal value: {result['pv_terminal_value']:,.4f}",
        f"Enterprise value: {result['enterprise_value']:,.4f}",
        f"Equity value: {result['equity_value']:,.4f}",
        f"Value per diluted share: {result['value_per_share']:,.4f}",
        f"PV of TV / enterprise value: {result['terminal_value_share']:.4f}",
    ]
    print("\n".join(lines))


def print_sensitivity_grid():
    """Print value per share for each WACC and terminal-growth pair."""
    print("\nSensitivity grid: value per diluted share")
    header = "WACC \\ terminal growth".ljust(24)
    header += "".join(f"{rate:>12.1%}" for rate in TERMINAL_GROWTH_SENSITIVITY)
    print(header)

    for wacc in WACC_SENSITIVITY:
        row = f"{wacc:.1%}".ljust(24)
        for terminal_growth in TERMINAL_GROWTH_SENSITIVITY:
            if terminal_growth >= wacc:
                cell = "invalid"
            else:
                cell = f"{calculate_dcf(GROWTH_RATES, wacc, terminal_growth)['value_per_share']:.2f}"
            row += f"{cell:>12}"
        print(row)


def value_for_shift(shift):
    shifted_growth_rates = [rate + shift for rate in GROWTH_RATES]
    if any(rate <= -1.0 for rate in shifted_growth_rates):
        raise ValueError("shift pushes an annual growth rate to -100% or below")
    return calculate_dcf(
        shifted_growth_rates, WACC, TERMINAL_GROWTH
    )["value_per_share"]


def solve_reverse_dcf():
    """Solve for a uniform shift to all five growth rates using bisection."""
    lower = SHIFT_LOWER_BOUND
    upper = SHIFT_UPPER_BOUND
    lower_value = value_for_shift(lower)
    upper_value = value_for_shift(upper)

    if not min(lower_value, upper_value) <= TARGET_SHARE_PRICE <= max(
        lower_value, upper_value
    ):
        return None

    increasing = upper_value > lower_value
    for _ in range(BISECTION_MAX_ITERATIONS):
        midpoint = (lower + upper) / 2.0
        midpoint_value = value_for_shift(midpoint)
        if abs(midpoint_value - TARGET_SHARE_PRICE) <= BISECTION_TOLERANCE:
            return midpoint
        if (midpoint_value < TARGET_SHARE_PRICE) == increasing:
            lower = midpoint
        else:
            upper = midpoint
    return (lower + upper) / 2.0


def print_reverse_dcf():
    shift = solve_reverse_dcf()
    print("\nReverse DCF")
    print(f"Target share price: ${TARGET_SHARE_PRICE:.2f}")
    if shift is None:
        print(
            "Solved uniform growth shift: no solution in "
            f"[{SHIFT_LOWER_BOUND:+.2%}, {SHIFT_UPPER_BOUND:+.2%}]"
        )
    else:
        shifted_rates = [rate + shift for rate in GROWTH_RATES]
        print(f"Solved uniform growth shift: {shift:+.4%}")
        print("Implied growth rates: " + ", ".join(f"{rate:.2%}" for rate in shifted_rates))
    print(
        "Held fixed: starting FCFF, WACC, terminal growth, cash, debt, "
        "and diluted shares."
    )


def main() -> None:
    if len(GROWTH_RATES) != 5:
        raise SystemExit("Error: GROWTH_RATES must contain exactly five rates.")
    if TERMINAL_GROWTH >= WACC:
        raise SystemExit(
            "Error: terminal growth must be less than WACC for the "
            "Gordon-growth formula."
        )
    if DILUTED_SHARES <= 0.0:
        raise SystemExit("Error: diluted shares must be greater than zero.")
    if SHIFT_LOWER_BOUND >= SHIFT_UPPER_BOUND:
        raise SystemExit("Error: the lower shift bound must be below the upper bound.")

    try:
        base_result = calculate_dcf(GROWTH_RATES, WACC, TERMINAL_GROWTH)
        value_for_shift(SHIFT_LOWER_BOUND)
        value_for_shift(SHIFT_UPPER_BOUND)
    except ValueError as error:
        raise SystemExit(f"Error: {error}") from error

    print_twelve_lines(base_result)
    print_sensitivity_grid()
    print_reverse_dcf()


if __name__ == "__main__":
    main()
