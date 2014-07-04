"""
These are integration tests. Tests the simulator on
several platypus programs with varied inputs
"""

from platypus.frontend.grammar import get_ast
from platypus.cfg.ast_to_cfg import get_cfg
from platypus.simulator.simulator import get_ir
from nose.tools import assert_equals

class TestSimulation:

    def setup(self):
        pass

    def teardown(self):
        pass

    def _get_ir(self, source_filepath):
        source_file = open(source_filepath, 'r')
        source = ""
        for line in source_file:
            source += line
        func_ast = get_ast(source)
        func_cfg = get_cfg(func_ast)
        func_ir = get_ir(func_cfg)
        try:
            os.remove("parser.out")
            os.remove("parsetab.py")
            os.remove("parsetab.pyc")
        except:
            pass
        return func_ir

    def test_sum_till_n(self):
        func_ir = self._get_ir("tests/examples/sum_till_n.platypus")
        argument = [10]
        expected_output = [45]
        output = func_ir.execute(argument)
        assert_equals(output, expected_output)

    def test_arith(self):
        func_ir = self._get_ir("tests/examples/arith.platypus")
        argument = [1, 23, 10]
        expected_output = [23, 10, 33]
        output = func_ir.execute(argument)
        assert_equals(output, expected_output)

        argument = [2, 23, 10]
        expected_output = [23, 10, 230]
        output = func_ir.execute(argument)
        assert_equals(output, expected_output)

        argument = [3, 23, 10]
        expected_output = [23, 10, 13]
        output = func_ir.execute(argument)
        assert_equals(output, expected_output)

        argument = [4, 23, 10]
        expected_output = [23, 10, 2]
        output = func_ir.execute(argument)
        assert_equals(output, expected_output)

    def test_greater(self):
        func_ir = self._get_ir("tests/examples/greater.platypus")
        argument = [1, 23, 10]
        expected_output = [23]
        output = func_ir.execute(argument)
        assert_equals(output, expected_output)

    def test_sum(self):
        func_ir = self._get_ir("tests/examples/fibo_sum.platypus")
        argument = [1, 1, 10]
        expected_output = [55, 143]
        output = func_ir.execute(argument)
        assert_equals(output, expected_output)
