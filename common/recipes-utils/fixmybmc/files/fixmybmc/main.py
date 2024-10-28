#!/usr/bin/env python3
# (c) Meta Platforms, Inc. and affiliates. Confidential and proprietary.

import sys
from typing import Dict, List

from fixmybmc import status

from fixmybmc.bmccheck import _checks, BmcCheck, load_checks
from fixmybmc.remediation import Remediation
from fixmybmc.utils import (
    bold,
    clear_line,
    color,
    color_bg,
    indent,
    overwrite_print,
    styled,
)


def main() -> int:
    load_checks()
    overwrite_print(f"Loaded {len(_checks)} checks")

    overwrite_print("Running checks...")
    statuses = run_checks(_checks)
    auto_remediations = get_auto_remediations(_checks.values())
    manual_remediations = get_manual_remediations(_checks.values())

    show_result_summary(_checks.values())
    show_remediations(auto_remediations, manual_remediations)
    run_remediations(auto_remediations)

    return all(isinstance(s, status.Ok) for s in statuses)


def run_checks(checks: Dict[str, BmcCheck]) -> List[status.Status]:
    results: List[status.Status] = []
    for name, check in checks.items():
        overwrite_print(f"Checking: {name}")
        check.run()
        results.append(check.result)
    clear_line()
    return results


def run_remediations(auto_remediations: List[Remediation]) -> None:
    if len(auto_remediations) == 0:
        return
    print()
    remediation_names = [r.name for r in auto_remediations]
    should_run = input(
        f"Run the recommended remediations? [{','.join(remediation_names)}][y/N] "
    )
    if should_run.lower() == "y":
        for r in auto_remediations:
            print("-----")
            print(indent(f"Running {r.name}"))
            r.run()
            print(indent(f"Finished running {r.name}"))
            print("-----")
    else:
        print("Skipping remediations")


def show_result_summary(checks: List[BmcCheck]) -> None:
    print(f"Ran {len(checks)} checks")
    print("-----")
    passed = [check for check in checks if isinstance(check.result, status.Ok)]
    problems = [check for check in checks if isinstance(check.result, status.Problem)]
    errors = [check for check in checks if isinstance(check.result, status.Error)]
    print("Result summary:")
    if len(passed) > 0:
        print(indent(styled(f"Passed: {len(passed)}", color(status.Ok.color), bold())))
        print(indent(", ".join([check.name for check in passed]), level=2))
    if len(problems) > 0:
        print(
            indent(
                styled(
                    f"Problems: {len(problems)}", color(status.Problem.color), bold()
                )
            )
        )
    if len(errors) > 0:
        print(
            indent(styled(f"Errors: {len(errors)}", color(status.Error.color), bold()))
        )
    print("-----")

    for check in problems + errors:
        print_res_name = styled(
            f"[  {check.result.name}  ]", color_bg(check.result.color), bold()
        )
        print(f"{print_res_name} {check.name}")
        print(f"{indent(str(check.result))}")


def show_remediations(
    auto_remediations: List[Remediation], manual_remediations: List[Remediation]
) -> None:
    if len(manual_remediations) == 0 and len(auto_remediations) == 0:
        print("No remediations available")
        return

    print("Remediations:")
    for r in manual_remediations:
        print(indent(f"Manual remediation recommended: {r.name}"))
        print(indent(r.description, level=2))

    for r in auto_remediations:
        print(indent(f"Auto remediation available: {r.name}"))
        print(indent(r.description, level=2))


def get_manual_remediations(checks: List[BmcCheck]) -> List[str]:
    problems = [check for check in checks if isinstance(check.result, status.Problem)]
    return [
        problem.result.manual_remediation
        for problem in problems
        if problem.result.has_manual_remediation
    ]


def get_auto_remediations(checks: List[BmcCheck]) -> List[Remediation]:
    problems = [check for check in checks if isinstance(check.result, status.Problem)]
    return [
        problem.result.remediation
        for problem in problems
        if problem.result.has_auto_remediation
    ]


if __name__ == "__main__":
    sys.exit(main())
