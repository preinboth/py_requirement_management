from requ_man import RequirementManagement


requirements = [
    ">=1.2.0,<3.0.0",
    "==1.5.0",
    "~=1.2.3",
    "==1.2.3,~=1.2.0,>=2.0.0,<3.0.0",
]
requ_man = RequirementManagement()

for requirement in requirements:
    requ_man.get_min_max_version(requirement)
