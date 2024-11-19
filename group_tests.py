import unittest
from group import groups_of_3


class TestGroupsOf3(unittest.TestCase):
    def test_perfect_groups(self):
        """Test when input length is divisible by 3"""
        self.assertEqual(
            groups_of_3([1, 2, 3, 4, 5, 6, 7, 8, 9]),
            [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        )

    def test_incomplete_final_group(self):
        """Test when input length is not divisible by 3"""
        self.assertEqual(
            groups_of_3([1, 2, 3, 4, 5, 6, 7, 8]),
            [[1, 2, 3], [4, 5, 6], [7, 8]]
        )

    def test_small_list(self):
        """Test with list smaller than 3 elements"""
        self.assertEqual(
            groups_of_3([1, 2]),
            [[1, 2]]
        )

    def test_empty_list(self):
        """Test with empty list"""
        self.assertEqual(
            groups_of_3([]),
            []
        )


if __name__ == '__main__':
    unittest.main()

"""


from group import groups_of_3

def test_groups_of_3():
    assert groups_of_3([1, 2, 3, 4, 5, 6, 7, 8, 9]) == [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    assert groups_of_3([1, 2, 3, 4, 5, 6, 7, 8]) == [[1, 2, 3], [4, 5, 6], [7, 8]]
    assert groups_of_3([]) == []
    assert groups_of_3([1]) == [[1]]
    assert groups_of_3([1, 2]) == [[1, 2]]
    assert groups_of_3([1, 2, 3]) == [[1, 2, 3]]

print(groups_of_3([3, 1, 4, 5, 3, 1, 3, 2, 2, 5, 6, 7, 9, 8, 7]))

"""