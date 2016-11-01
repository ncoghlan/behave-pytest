import sys

import py

def install_pytest_asserts():
    try:
        import ast  # noqa
    except ImportError as e:
        print('Can not use py.test asserts - import ast failed!')
        return
    else:
        # Both Jython and CPython 2.6.0 have AST bugs that make the
        # assertion rewriting hook malfunction.
        if (sys.platform.startswith('java') or
                sys.version_info[:3] == (2, 6, 0)):
            print('Can not use py.test asserts - no compatible python interpreter')
            return

    from _pytest.assertion import rewrite  # noqa

    hook = rewrite.AssertionRewritingHook()  # noqa
    sys.meta_path.insert(0, hook)
