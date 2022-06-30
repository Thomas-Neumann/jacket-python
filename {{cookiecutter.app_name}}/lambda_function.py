#!/usr/bin/env python3
"""
{{cookiecutter.description}}

this is the entrypoint for an AWS Lambda function

required IAM permissions:
    <specify all required IAM permissions>
"""

# standard imports
import logging
import os
import sys

# extra imports (make sure to add them to requirements.txt!)
# <add extra imports here, e.g. 'boto3' 'requests'>

from typing import Dict, Optional

sys.path.insert(0, os.path.dirname(__file__) + "/src")

# pylint: disable=wrong-import-position
import {{cookiecutter.pypackage_name}}

LH = logging.getLogger()


def lambda_handler(event: Dict, context: Dict) -> Optional[Dict]:
    """
    called by AWS Lambda
    """
    # <this is just an example - replace as needed>
    LH.setLevel(logging.INFO)
    LH.debug("event:   %s", event)
    LH.debug("context: %s", context)

    values = os.environ.get('VALUES', [])
    result = {{cookiecutter.pypackage_name}}.{{cookiecutter.main_function}}(values)
    # </this is just an example - replace as needed>
    return result
