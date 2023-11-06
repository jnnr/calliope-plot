def pytest_exception_interact(node, call, report):
    # Adopted from https://stackoverflow.com/questions/56807698/how-to-run-script-as-pytest-test
    excinfo = call.excinfo
    if "script" in node.funcargs:
        excinfo.traceback = excinfo.traceback.cut(path=node.funcargs["script"])
    report.longrepr = node.repr_failure(excinfo)
