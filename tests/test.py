import sys
from pathlib import Path
import pytest
import numpy as np

parent_dir = str(Path(__file__).parent.parent)
print(parent_dir)
sys.path.insert(0, parent_dir)



# test edilecek odevi importla

from odev import rectangle


# otomatik verilerin yuklenmesi

@pytest.fixture
def get_test_data():
   test_a = np.loadtxt("tests/test_a.csv", delimiter=",")
   test_b = np.loadtxt("tests/test_b.csv", delimiter=",")
   test_circumference = np.loadtxt("tests/test_circumference.csv", delimiter=",")
   test_area = np.loadtxt("tests/num_area.csv", delimiter=",")

   tested_circumference, tested_area = rectangle(test_a, test_b)
   return test_a, test_b, test_circumference, test_area, tested_circumference, tested_area


# testlerin tanimlari

def test1(get_test_data):
    # test the circumference computation
    test_a = get_test_data[0]
    test_b = get_test_data[1]
    test_circumference = get_test_data[2]
    tested_circumference = get_test_data[4]

    np.testing.assert_allclose(test_circumference, tested_circumference)


def test2(get_test_data):
    # test the area computation
    test_a = get_test_data[0]
    test_b = get_test_data[1]
    test_area = get_test_data[3]
    tested_area = get_test_data[5]

    np.testing.assert_allclose(test_area, tested_area)
