import pathlib
import sys
import unittest

if __name__ == "__main__":
    tests_path = pathlib.Path(__file__).parent
    root_path = tests_path.parent
    test_suite = unittest.defaultTestLoader.discover(
        start_dir=str(tests_path), top_level_dir=str(root_path)
    )
    test_runner = unittest.runner.TextTestRunner(verbosity=2)
    result = test_runner.run(test_suite)
    sys.exit(0 if result.wasSuccessful() else 1)
