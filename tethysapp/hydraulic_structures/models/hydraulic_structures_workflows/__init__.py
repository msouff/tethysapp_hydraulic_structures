"""
********************************************************************************
* Name: __init__.py
* Author: msouffront
* Created On: January 07, 2022
* Copyright: (c) Aquaveo 2022
********************************************************************************
"""
from .prepare_query import PrepareQueryWorkflow  # noqa:F401, E501

HYDRAULICSTRUCTURES_WORKFLOWS = {
    PrepareQueryWorkflow.TYPE: PrepareQueryWorkflow,
}
