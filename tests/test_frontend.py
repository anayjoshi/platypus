from platypus.frontend.grammar import get_ast

class TestFrontend:

    def setup(self):
        pass

    def teardown(self):
        pass

    def test_correct_simple(self):
        program = \
                """
                function (a b)
                {
                # some summary #
                    ans = a + b
                    return (ans)
                }
                """
        func_ast = get_ast(program)

    def test_correct_if(self):
        program = \
                """
                function (a)
                {
                # summary #
                    if (a > 3)
                    {
                        result = 1
                    }
                return (result)
                }
                """
        func_ast = get_ast(program)
