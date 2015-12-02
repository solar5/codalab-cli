"""
This module exports some simple names used throughout the CodaLab bundle system:
  - The various CodaLab error classes, with documentation for each.
  - The State class, an enumeration of all legal bundle states.
  - precondition, a utility method that check's a function's input preconditions.
"""

# Increment this on the develop branch when develop is merged into master.
# http://semver.org/
CODALAB_VERSION = '0.1.0'

class IntegrityError(ValueError):
    """
    Raised by the model when there is a database integrity issue.

    Indicates a serious error that either means that there was a bug in the model
    code that left the database in a bad state, or that there was an out-of-band
    database edit with the same result.
    """


class PreconditionViolation(ValueError):
    """
    Raised when a value generated by one module fails to satisfy a precondition
    required by another module.

    This class of error is serious and should indicate a problem in code, but it
    it is not an AssertionError because it is not local to a single module.
    """


class UsageError(ValueError):
    """
    Raised when user input causes an exception. This error is the only one for
    which the command-line client suppresses output.
    """


class AuthorizationError(UsageError):
    """
    Raised when access to a resource is refused because authentication is required
    and has not been provided. Similar to HTTP status 401.
    """


class PermissionError(UsageError):
    """
    Raised when access to a resource is refused because the user does not have
    necessary permissions. Similar to HTTP status 403.
    """


class State(object):
    """
    An enumeration of states that a bundle can be in.
    """
    CREATED = 'created'   # Just created
    STAGED = 'staged'     # All the dependencies are met
    QUEUED = 'queued'     # Submitted to the queue (and possibly copying files around)
    RUNNING = 'running'   # Actually running
    READY = 'ready'       # Done running and succeeded
    FAILED = 'failed'     # Done running and failed

    OPTIONS = {CREATED, STAGED, RUNNING, READY, FAILED}
    FINAL_STATES = {READY, FAILED}


def precondition(condition, message):
    if not condition:
        raise PreconditionViolation(message)
