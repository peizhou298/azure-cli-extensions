# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

import argparse
import antlr4

from azure.cli.command_modules.monitor.util import (
    get_aggregation_map, get_operator_map, get_autoscale_operator_map,
    get_autoscale_aggregation_map, get_autoscale_scale_direction_map)

from knack.util import CLIError


# pylint: disable=protected-access
class PeeringAddDirectConnection(argparse._AppendAction):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        super(PeeringAddDirectConnection, self).__call__(parser, namespace, action, option_string)

    def get_action(self, values, option_string):  # pylint: disable=no-self-use
        try:
            properties = dict(x.split('=', 1) for x in values)
        except ValueError:
            raise CLIError('usage error: {} [KEY=VALUE ...]'.format(option_string))
        d = {}
        for x in properties:
            k = x[0].lower()
            v = x[1]
            if k == 'bandwithdinmbps':
                d['bandwidthInMbps'] = v
            elif k == 'sessionaddressprovider':
                d['sessionAddressProvider'] = v
            elif k == 'useforpeeringservice':
                d['useForPeeringService'] = v
            elif k == 'peeringdbfacilityid':
                d['peeringDBFacilityId'] = v
            elif k == 'sessionprefixv4':
                d.setdefault('bgpSession', {})['sessionPrefixV4'] = v
            elif k == 'sessionprefixv6':
                d.setdefault('bgpSession', {})['sessionPrefixV6'] = v
            elif k == 'maxprefixesadvertisedv4':
                d.setdefault('bgpSession', {})['maxPrefixesAdvertisedV4'] = v
            elif k == 'maxprefixesadvertisedv6':
                d.setdefault('bgpSession', {})['maxPrefixesAdvertisedV6'] = v
            elif k == 'md5authenticationkey':
                d.setdefault('bgpSession', {})['md5AuthenticationKey'] = v
            elif k == 'connectionidentifier':
                d['connectionIdentifier'] = v
            else:
                raise CLIError('usage error: {} is invalid'.format(x))
        return d


# pylint: disable=protected-access
class PeeringAddExchangeConnection(argparse._AppendAction):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        super(PeeringAddExchangeConnection, self).__call__(parser, namespace, action, option_string)

    def get_action(self, values, option_string):  # pylint: disable=no-self-use
        #_type = values[0].lower()

        # iterate through values
        return {}
        #raise CLIError('usage error: {} TYPE KEY [ARGS]'.format(option_string))
