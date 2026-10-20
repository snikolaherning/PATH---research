"""Lab 08: UiPath P/E reference using the saved Lab 07 calculator.

Uses only Python's standard library. Edit the target and peer inputs below to
run another case. Prices and diluted EPS are in USD per share.
"""

from statistics import median


# ============================== EDITABLE INPUTS ==============================

# Prices: September 9, 2026 close, USD. Information cutoff: September 10, 2026.
# Sources and remaining comparability qualifications: lab08-uipath-comps.md.
TARGET = {
    "name": "UiPath", "ticker": "PATH", "price": 13.57, "diluted_eps": 0.52,
    "fiscal_year_end": "2026-01-31", "eps_publication_date": "2026-03-11",
}

PEERS = [
    {
        "name": "Pegasystems", "ticker": "PEGA", "price": 35.03,
        "diluted_eps": 2.13, "decision": "qualify",
        "fiscal_year_end": "2025-12-31", "eps_publication_date": "2026-02-10",
    },
]
# Appian is a qualified business comparable but excluded from P/E by the student.
# Its reported FY2025 diluted EPS is $0.02. No revenue/ARR valuation is substituted.

# ============================================================================


def positive_number(value):
    """Return True only for positive int/float inputs; booleans are rejected."""
    return isinstance(value, (int, float)) and not isinstance(value, bool) and value > 0


def normalized_ticker(company):
    """Return a normalized ticker used for target exclusion and deduplication."""
    ticker = company.get("ticker")
    if not isinstance(ticker, str):
        return ""
    return ticker.strip().upper()


def prepare_peers(target, peers):
    """Deduplicate peers by ticker and exclude the target company."""
    target_ticker = normalized_ticker(target)
    seen_tickers = set()
    prepared = []

    for peer in peers:
        ticker = normalized_ticker(peer)
        if ticker == target_ticker:
            continue
        if ticker and ticker in seen_tickers:
            continue
        if ticker:
            seen_tickers.add(ticker)
        prepared.append(peer)

    return prepared


def peer_multiple(peer):
    """Return a peer's P/E or None when price or diluted EPS is not meaningful."""
    price = peer.get("price")
    diluted_eps = peer.get("diluted_eps")
    if not positive_number(price) or not positive_number(diluted_eps):
        return None
    return price / diluted_eps


def valid_peer_results(peers):
    """Return (peer, full-precision P/E) pairs for peers with meaningful inputs."""
    results = []
    for peer in peers:
        multiple = peer_multiple(peer)
        if multiple is not None:
            results.append((peer, multiple))
    return results


def implied_price(multiple, target_eps):
    """Apply a P/E multiple to target EPS, or return None if not meaningful."""
    if multiple is None or not positive_number(target_eps):
        return None
    return multiple * target_eps


def company_label(company):
    name = company.get("name") or "Unnamed company"
    ticker = normalized_ticker(company)
    return f"{name} ({ticker})" if ticker else name


def format_price(value):
    return "not meaningful" if value is None else f"${value:,.2f}"


def format_dollar_change(value):
    sign = "+" if value >= 0 else "-"
    return f"{sign}${abs(value):,.2f}"


def main(validate=False):
    target_eps = TARGET.get("diluted_eps")
    peers = prepare_peers(TARGET, PEERS)
    results = valid_peer_results(peers)

    print(f"Target: {company_label(TARGET)}")
    print(f"Target diluted EPS: {format_price(target_eps if positive_number(target_eps) else None)}")
    print("\nPeer P/E multiples")

    for peer in peers:
        multiple = peer_multiple(peer)
        if multiple is None:
            print(f"{company_label(peer)}: not meaningful")
        else:
            print(f"{company_label(peer)}: {multiple:.6f}x")

    if not results:
        print("\nPeer valuation: no usable peers")
        print("\nLeave-one-out analysis: no usable peers")
        return

    multiples = [multiple for _, multiple in results]
    median_multiple = median(multiples)
    full_peer_estimate = implied_price(median_multiple, target_eps)

    print(f"\nValid peer count: {len(results)}")
    print(f"Peer median P/E: {median_multiple:.6f}x")

    if full_peer_estimate is None:
        print("Target valuation: not meaningful because target diluted EPS is missing or nonpositive")
    elif len(results) == 1:
        only_multiple = results[0][1]
        print(f"Reference estimate: {format_price(implied_price(only_multiple, target_eps))}")
        print("Peer-implied range: not available with one valid peer")
    else:
        minimum_price = implied_price(min(multiples), target_eps)
        maximum_price = implied_price(max(multiples), target_eps)
        print(f"Peer-implied minimum price: {format_price(minimum_price)}")
        print(f"Peer-implied median price: {format_price(full_peer_estimate)}")
        print(f"Peer-implied maximum price: {format_price(maximum_price)}")
        print(f"Peer-implied range: {format_price(minimum_price)} to {format_price(maximum_price)}")

    if not validate:
        return

    print("\nLeave-one-out analysis")
    for removed_peer, _ in results:
        removed_ticker = normalized_ticker(removed_peer)
        remaining = [
            (peer, multiple)
            for peer, multiple in results
            if normalized_ticker(peer) != removed_ticker
        ]
        if not remaining:
            print(f"Remove {company_label(removed_peer)}: no estimate")
            continue

        remaining_median = median(multiple for _, multiple in remaining)
        remaining_estimate = implied_price(remaining_median, target_eps)
        if remaining_estimate is None or full_peer_estimate is None:
            print(f"Remove {company_label(removed_peer)}: not meaningful")
            continue

        change = remaining_estimate - full_peer_estimate
        print(
            f"Remove {company_label(removed_peer)}: "
            f"remaining median-implied price {format_price(remaining_estimate)}; "
            f"change {format_dollar_change(change)}"
        )


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--validate", action="store_true", help="Show peer-removal check after recording your prediction")
    main(validate=parser.parse_args().validate)
