import os
import sys

# This file makes the project root importable by pytest,
# so tests in tests/ can do `from logic_utils import ...`.
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
