# Ragdoll - UserBot

"""
Exceptions which can be raised by py-Ragdoll Itself.
"""


class pyUltroidError(Exception):
    ...


class DependencyMissingError(ImportError):
    ...


class RunningAsFunctionLibError(pyUltroidError):
    ...
