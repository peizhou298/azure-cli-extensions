# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# pylint: disable=line-too-long
# pylint: disable=too-many-statements
# pylint: disable=too-many-lines
# pylint: disable=too-many-locals
# pylint: disable=unused-argument

import json


def create_managednetwork(cmd, client,
                          resource_group,
                          name,
                          location=None,
                          tags=None,
                          scope=None):
    return client.create_or_update(resource_group_name=resource_group, managed_network_name=name)


def update_managednetwork(cmd, client, body,
                          resource_group,
                          name,
                          location=None,
                          tags=None,
                          scope=None):
    return client.create_or_update(resource_group_name=resource_group, managed_network_name=name)


def list_managednetwork(cmd, client,
                        resource_group):
    if resource_group is not None:
        return client.list_by_resource_group(resource_group_name=resource_group)
    return client.list_by_subscription()


def create_managednetwork_scope_assignment(cmd, client,
                                           name,
                                           scope=None,
                                           location=None,
                                           assigned_managed_network=None):
    body = {}
    body['location'] = location  # str
    body['assigned_managed_network'] = assigned_managed_network  # str
    return client.create_or_update(parameters=body, scope=scope, scope_assignment_name=name)


def update_managednetwork_scope_assignment(cmd, client, body,
                                           name,
                                           scope=None,
                                           location=None,
                                           assigned_managed_network=None):
    body = client.get(scope=scope, scope_assignment_name=name).as_dict()
    body.location = location  # str
    body.assigned_managed_network = assigned_managed_network  # str
    return client.create_or_update(parameters=body, scope=scope, scope_assignment_name=name)


def list_managednetwork_scope_assignment(cmd, client,
                                         scope=None):
    return client.list(scope=scope)


def create_managednetwork_managed_network_group(cmd, client,
                                                resource_group,
                                                managed_network_name,
                                                name,
                                                location=None,
                                                management_groups=None,
                                                subscriptions=None,
                                                virtual_networks=None,
                                                subnets=None,
                                                kind=None):
    return client.create_or_update(resource_group_name=resource_group, managed_network_name=managed_network_name, managed_network_group_name=name)


def update_managednetwork_managed_network_group(cmd, client, body,
                                                resource_group,
                                                managed_network_name,
                                                name,
                                                location=None,
                                                management_groups=None,
                                                subscriptions=None,
                                                virtual_networks=None,
                                                subnets=None,
                                                kind=None):
    return client.create_or_update(resource_group_name=resource_group, managed_network_name=managed_network_name, managed_network_group_name=name)


def list_managednetwork_managed_network_group(cmd, client,
                                              resource_group,
                                              managed_network_name):
    return client.list_by_managed_network(resource_group_name=resource_group, managed_network_name=managed_network_name)


def create_managednetwork_managed_network_peering_policy(cmd, client,
                                                         resource_group,
                                                         managed_network_name,
                                                         name,
                                                         _type,
                                                         location=None,
                                                         hub=None,
                                                         spokes=None,
                                                         mesh=None):
    return client.create_or_update(resource_group_name=resource_group, managed_network_name=managed_network_name, managed_network_peering_policy_name=name)


def update_managednetwork_managed_network_peering_policy(cmd, client, body,
                                                         resource_group,
                                                         managed_network_name,
                                                         name,
                                                         _type,
                                                         location=None,
                                                         hub=None,
                                                         spokes=None,
                                                         mesh=None):
    return client.create_or_update(resource_group_name=resource_group, managed_network_name=managed_network_name, managed_network_peering_policy_name=name)


def list_managednetwork_managed_network_peering_policy(cmd, client,
                                                       resource_group,
                                                       managed_network_name):
    return client.list_by_managed_network(resource_group_name=resource_group, managed_network_name=managed_network_name)
