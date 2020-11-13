# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

try:
    from ._models_py3 import CheckNameAvailabilityParameters
    from ._models_py3 import ErrorDetails
    from ._models_py3 import ErrorDetailsInternal
    from ._models_py3 import Operation
    from ._models_py3 import OperationDisplay
    from ._models_py3 import OperationListResult
    from ._models_py3 import OperationResultsDescription
    from ._models_py3 import Resource
    from ._models_py3 import ResourceIdentity
    from ._models_py3 import ServiceAccessPolicyEntry
    from ._models_py3 import ServiceAuthenticationConfigurationInfo
    from ._models_py3 import ServiceCorsConfigurationInfo
    from ._models_py3 import ServiceCosmosDBConfigurationInfo
    from ._models_py3 import ServiceExportConfigurationInfo
    from ._models_py3 import ServiceAcrConfigurationInfo
    from ._models_py3 import ServicesDescription
    from ._models_py3 import ServicesDescriptionListResult
    from ._models_py3 import ServicesNameAvailabilityInfo
    from ._models_py3 import ServicesPatchDescription
    from ._models_py3 import ServicesProperties
except (SyntaxError, ImportError):
    from ._models import CheckNameAvailabilityParameters  # type: ignore
    from ._models import ErrorDetails  # type: ignore
    from ._models import ErrorDetailsInternal  # type: ignore
    from ._models import Operation  # type: ignore
    from ._models import OperationDisplay  # type: ignore
    from ._models import OperationListResult  # type: ignore
    from ._models import OperationResultsDescription  # type: ignore
    from ._models import Resource  # type: ignore
    from ._models import ResourceIdentity  # type: ignore
    from ._models import ServiceAccessPolicyEntry  # type: ignore
    from ._models import ServiceAuthenticationConfigurationInfo  # type: ignore
    from ._models import ServiceCorsConfigurationInfo  # type: ignore
    from ._models import ServiceCosmosDBConfigurationInfo  # type: ignore
    from ._models import ServiceExportConfigurationInfo  # type: ignore
    from ._models import ServiceAcrConfigurationInfo 
    from ._models import ServicesDescription  # type: ignore
    from ._models import ServicesDescriptionListResult  # type: ignore
    from ._models import ServicesNameAvailabilityInfo  # type: ignore
    from ._models import ServicesPatchDescription  # type: ignore
    from ._models import ServicesProperties  # type: ignore

from ._healthcare_apis_management_client_enums import (
    Kind,
    ManagedServiceIdentityType,
    OperationResultStatus,
    ProvisioningState,
    ServiceNameUnavailabilityReason,
)

__all__ = [
    'CheckNameAvailabilityParameters',
    'ErrorDetails',
    'ErrorDetailsInternal',
    'Operation',
    'OperationDisplay',
    'OperationListResult',
    'OperationResultsDescription',
    'Resource',
    'ResourceIdentity',
    'ServiceAccessPolicyEntry',
    'ServiceAuthenticationConfigurationInfo',
    'ServiceCorsConfigurationInfo',
    'ServiceCosmosDBConfigurationInfo',
    'ServiceExportConfigurationInfo',
     'ServiceAcrConfigurationInfo',
    'ServicesDescription',
    'ServicesDescriptionListResult',
    'ServicesNameAvailabilityInfo',
    'ServicesPatchDescription',
    'ServicesProperties',
    'Kind',
    'ManagedServiceIdentityType',
    'OperationResultStatus',
    'ProvisioningState',
    'ServiceNameUnavailabilityReason',
]
