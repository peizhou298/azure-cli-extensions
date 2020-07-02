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


class AnonymizedViewsProperties(Model):
    """The properties of an anonymized view.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar provisioning_state: The provisioning state. Possible values include:
     'Deleting', 'Succeeded', 'Creating', 'Accepted', 'Verifying', 'Updating',
     'Failed', 'Canceled', 'Deprovisioned'
    :vartype provisioning_state: str or
     ~azure.mgmt.healthcareapis.models.ProvisioningState
    :param anonymized_view_config: The configuration of an anonymized view.
    :type anonymized_view_config: object
    """

    _validation = {
        'provisioning_state': {'readonly': True},
    }

    _attribute_map = {
        'provisioning_state': {'key': 'provisioningState', 'type': 'str'},
        'anonymized_view_config': {'key': 'anonymizedViewConfig', 'type': 'object'},
    }

    def __init__(self, **kwargs):
        super(AnonymizedViewsProperties, self).__init__(**kwargs)
        self.provisioning_state = None
        self.anonymized_view_config = kwargs.get('anonymized_view_config', None)
