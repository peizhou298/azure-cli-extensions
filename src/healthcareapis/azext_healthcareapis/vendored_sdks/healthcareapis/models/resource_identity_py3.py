# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class ResourceIdentity(Model):
    """Setting indicating whether the service has a managed identity associated
    with it.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar principal_id: The principal ID of the resource identity.
    :vartype principal_id: str
    :ivar tenant_id: The tenant ID of the resource.
    :vartype tenant_id: str
    :param type: Type of identity being specified, currently SystemAssigned
     and None are allowed. Possible values include: 'SystemAssigned', 'None'
    :type type: str or
     ~azure.mgmt.healthcareapis.models.ManagedServiceIdentityType
    """

    _validation = {
        'principal_id': {'readonly': True},
        'tenant_id': {'readonly': True},
    }

    _attribute_map = {
        'principal_id': {'key': 'principalId', 'type': 'str'},
        'tenant_id': {'key': 'tenantId', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
    }

    def __init__(self, *, type=None, **kwargs) -> None:
        super(ResourceIdentity, self).__init__(**kwargs)
        self.principal_id = None
        self.tenant_id = None
        self.type = type
