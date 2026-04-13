import unittest
from typing import Callable

from cs6515_almost_k_sat import (
    input_transformation,
    output_transformation,
    verify_solution,
)

from npc.types import CNF, Assignment


class TestAlmostKSat(unittest.TestCase):
    def test_base_case_1(self):
        cnf = [
            {"x1", "x2", "x3"},
            {"x1", "!x2", "!x3"},
            {"!x1", "!x3", "!x4"},
            {"!x1", "x2", "!x4"},
            {"!x1", "!x2", "x4"},
            {"!x1", "!x2", "!x4"},
            {"x2", "x3", "x4"},
            {"!x2", "x3", "!x4"},
            {"!x1", "!x2", "!x3"},
            {"x1", "!x3", "x4"},
        ]

        variables = {"x1", "x2", "x3", "x4"}

        self.assertTrue(verify_solution(cnf, variables, 3))

    def test_base_case_2(self):
        cnf = [
            {"x1", "x2", "x3"},
            {"x1", "!x2", "!x3"},
            {"!x1", "!x3", "!x4"},
            {"!x1", "x2", "!x4"},
            {"!x1", "!x2", "x4"},
            {"!x1", "!x2", "!x4"},
            {"x2", "x3", "x4"},
            {"!x2", "x3", "!x4"},
            {"!x1", "!x2", "!x3"},
            {"x1", "!x3", "x4"},
        ]

        variables = {"x1", "x2", "x3", "x4"}

        self.assertFalse(verify_solution(cnf, variables, 4))


def sat(cnf: CNF, almost_k_sat: Callable[[CNF, int], Assignment]) -> Assignment | None:
    """
    SAT solver that uses almost_k_sat as a black box. This function is passed in and hidden from you.
    """
    # This is how we will run your functions for testing.
    return output_transformation(almost_k_sat(*input_transformation(cnf)))


if __name__ == "__main__":
    unittest.main()
