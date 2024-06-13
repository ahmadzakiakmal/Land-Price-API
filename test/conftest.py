import csv

def read_csv(file_path):
    with open(file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        data = [row for row in reader]
    return data

def pytest_runtest_logreport(report):
    """Display the test name and custom messages based on test outcome."""
    if report.when == 'call':
        if report.passed:
            print(f"\nTest Passed: {report.nodeid}")
        elif report.failed:
            print(f"\nTest Failed: {report.nodeid}")
        elif report.skipped:
            print(f"\nTest Skipped: {report.nodeid}")

def pytest_terminal_summary(terminalreporter, exitstatus, config):
    """Display a summary at the end of the test session."""
    total = terminalreporter._numcollected
    passed = len(terminalreporter.stats.get('passed', []))
    failed = len(terminalreporter.stats.get('failed', []))
    skipped = len(terminalreporter.stats.get('skipped', []))

    terminalreporter.write_sep("=", "Summary")
    terminalreporter.write_line(f"Total tests run: {total}")
    terminalreporter.write_line(f"Tests passed: {passed}")
    terminalreporter.write_line(f"Tests failed: {failed}")
    terminalreporter.write_line(f"Tests skipped: {skipped}")

def pytest_sessionstart(session):
    """Display a start message."""
    print("\nStarting the test session...\n")

def pytest_sessionfinish(session, exitstatus):
    """Display a finish message."""
    print(f"\nTest session finished. Total tests run: {session.testscollected}\n")

