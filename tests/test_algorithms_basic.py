"""
Moduł testujący funkcjonalność głównego algorytmu poszukiwającego par.
"""

import pytest

from data_ops.algorithms.basic import PairAnalyzer

test_data = [
    (
        [1, 5, 3, 7, 9, 6, 10, 2, 12, 0, 4, 8, 0, 4, 12],
        12,
        [[5, 7], [3, 9], [2, 10], [0, 12], [0, 12], [4, 8]],
    ),
    ([1, 11, 11], 12, [[1, 11]]),
    ([], 12, []),
]


@pytest.mark.parametrize("indata,value_sum,output", test_data)
def test_find_pairs(indata, value_sum, output):
    pairanalyzer = PairAnalyzer(indata=indata)
    result = pairanalyzer.find_pairs(value_sum)
    assert result == output
