
import unittest
import wymiot


class DoesDoSth(unittest.TestCase):

    def test_nothing(self):
        path_to_nothing = '../examples/nothing/'
        result = wymiot.Wymiot.run_program(path_to_nothing, 'nothing', '')

        self.assertEquals(result, 'nothing\n')

    def test_read_files(self):
        path_to_test_dir = '../examples/fib/tests/'
        result = wymiot.Wymiot.list_input_files(path_to_test_dir)

        self.assertListEqual(result, [('test01.in', 'test01.out')])

    def ignore_test_do_sth0(self):
        path_to_fib = '../examples/fib/'
        result = wymiot.Wymiot.run_program(path_to_fib, 'fib', 'tests/test01.in')
        expected = '1 13 233'
        self.assertEquals(result, expected)

def main():
    unittest.main()

if __name__ == '__main__':
    main()