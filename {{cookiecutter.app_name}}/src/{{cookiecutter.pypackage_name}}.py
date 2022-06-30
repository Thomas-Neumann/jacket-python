#!/usr/bin/env python3
"""
implementation of {{cookiecutter.pypackage_name}}

{{cookiecutter.description}}
"""

# standard imports
import logging

# extra imports (make sure to add them to requirements.txt!)
# <add extra imports here, e.g. 'boto3' 'requests'>

LH = logging.getLogger(__name__)

VERSIONSTRING = '0.1.0-alpha1'


def {{cookiecutter.main_function}}(values):
    """
    application logic
    """
    # <this is just an example - replace as needed>
    LH.info("[%s] Logging something.", __name__)
    for value in values:
        print(f" - '{value}'")
    # </this is just an example - replace as needed>
    return "Got {} arguments".format(len(values))
