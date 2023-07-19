import re
from typing import List, Tuple


class RequirementManagement:
    def __init__(self):
        self._operators: List[str] = ["==", ">=", "<=", "<", ">", "~=", "^"]

    def get_min_max_version(self, requirements):
        min_version: str = None
        max_version: str = None

        requirements_list: List[Tuple[str, str]] = re.findall(
            r"([<>=~^!]*)([\d+\.]+|\d+)", requirements
        )
        for op, version in requirements_list:
            if op not in self._operators:
                raise ValueError(f"invalid operator: {op}")
            elif op == "==":
                # exact version
                min_version = version
                max_version = version
            elif op == ">=":
                # minimum version
                min_version = version
            elif op == "<=":
                # maximum version
                max_version = version
            elif op == ">":
                # greater_than_operator
                major, minor, patch = version.split(".")
                next_major_version = int(major) + 1
                min_version = f"{next_major_version}.0.0"
                max_version = None  # No upper bound
            elif op == "<":
                # less_than_operator
                max_version = version
            elif op == "~=":
                # tilde_operator
                major, minor, _ = version.split(".")
                min_version = version
                max_version = f"{major}.{int(minor) + 1}.0"
            elif op == "^":
                # caret operator
                major, minor, patch = version.split(".")
                next_major_version = int(major) + 1
                min_version = f"{major}.{minor}.0"
                max_version = f"{next_major_version - 1}.9.9"
    
        return min_version, max_version


