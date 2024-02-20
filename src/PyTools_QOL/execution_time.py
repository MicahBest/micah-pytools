import time


def print_execution_time(start_time) -> None:
    """
    Prints the time it took to run a program after execution.

    Args:
        - start_time (float) : start time of the program (`start_time = time.time()`)

    Returns:
        - None
    """
    assert isinstance(start_time, float)
    exec_time = time.time() - start_time

    nseconds = exec_time % 60
    nminutes = exec_time // 60
    nhours = exec_time // (60 * 60)
    ndays = exec_time // (60 * 60 * 24)

    if ndays:
        print(f"Program executed in {ndays:.0f} days, {nhours:.0f} hours, {nminutes:.0f} minutes, {nseconds:.0f} seconds.")
    elif nhours:
        print(f"Program executed in {nhours:.0f} hours, {nminutes:.0f} minutes, {nseconds:.0f} seconds.")
    elif nminutes:
        print(f"Program executed in {nminutes:.0f} minutes, {nseconds:.0f} seconds.")
    else:
        print(f"Program executed in {nseconds:.0f} seconds.")
