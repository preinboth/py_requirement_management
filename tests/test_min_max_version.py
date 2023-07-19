import unittest

from requ_man import RequirementManagement


class TestMinMaxVersion(unittest.TestCase):
    def setUp(self):
        self.requ_man = RequirementManagement()

    def test_exact_match(self):
        requirements = "==1.5.0"
        min_version, max_version = self.requ_man.get_min_max_version(requirements)
        self.assertEqual(min_version, "1.5.0")
        self.assertEqual(max_version, "1.5.0")

    def test_minimum_version(self):
        requirements = ">=1.2.0"
        min_version, max_version = self.requ_man.get_min_max_version(requirements)
        self.assertEqual(min_version, "1.2.0")
        # self.assertIsNone(max_version)

    def test_maximum_version(self):
        requirements = "<=2.0.0"
        min_version, max_version = self.requ_man.get_min_max_version(requirements)
        # self.assertIsNone(min_version)
        self.assertEqual(max_version, "2.0.0")

    def test_tilde_operator(self):
        requirements = "~=1.2.3"
        min_version, max_version = self.requ_man.get_min_max_version(requirements)
        self.assertEqual(min_version, "1.2.3")
        self.assertEqual(max_version, "1.3.0")

    def test_greater_than_operator(self):
        requirements = ">1.3.0"
        min_version, max_version = self.requ_man.get_min_max_version(requirements)
        self.assertEqual(min_version, "2.0.0")
        self.assertIsNone(max_version)

    def test_less_than_operator(self):
        requirements = "<1.2.3"
        min_version, max_version = self.requ_man.get_min_max_version(requirements)
        self.assertIsNone(min_version)
        self.assertEqual(max_version, "1.2.3")
    
    def test_caret_operator(self):
        requirements = "^1.2.0"
        min_version, max_version = self.requ_man.get_min_max_version(requirements)
        self.assertEqual(min_version, "1.2.0")
        self.assertEqual(max_version, "1.9.9")

if __name__ == "__main__":
    unittest.main()
