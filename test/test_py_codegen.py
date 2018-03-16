from __future__ import division, with_statement, absolute_import

import pytest  # noqa
import pytools
import pytools.py_codegen as codegen
import sys


def test_pickling_with_module_import():
    cg = codegen.PythonCodeGenerator()
    cg("import pytools.py_codegen")
    cg("import math as m")

    import pickle
    mod = pickle.loads(pickle.dumps(cg.get_picklable_module()))

    assert mod.mod_globals["pytools"] is pytools
    assert mod.mod_globals["pytools"].py_codegen is pytools.py_codegen

    import math
    assert mod.mod_globals["m"] is math


def test_picklable_function():
    cg = codegen.PythonFunctionGenerator("f", args=())
    cg("return 1")

    import pickle
    f = pickle.loads(pickle.dumps(cg.get_picklable_function()))

    assert f() == 1


if __name__ == "__main__":
    if len(sys.argv) > 1:
        exec(sys.argv[1])
    else:
        from py.test import main
        main([__file__])
