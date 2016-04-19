""" Cisco_IOS_XR_ethernet_cfm_datatypes 

This module contains a collection of generally useful
derived YANG data types.

Copyright (c) 2013\-2015 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYDataValidationError



class BandwidthNotificationStateEnum(Enum):
    """
    BandwidthNotificationStateEnum

    Bandwidth notification state

    .. data:: OK = 1

    	Link is not degraded

    .. data:: DEGRADED = 2

    	Link is in degraded state

    """

    OK = 1

    DEGRADED = 2


    @staticmethod
    def _meta_info():
        from ydk.models.ethernet._meta import _Cisco_IOS_XR_ethernet_cfm_datatypes as meta
        return meta._meta_table['BandwidthNotificationStateEnum']


class CfmAisIntervalEnum(Enum):
    """
    CfmAisIntervalEnum

    Cfm ais interval

    .. data:: Y_1S = 4

    	1s

    .. data:: Y_1M = 6

    	1m

    """

    Y_1S = 4

    Y_1M = 6


    @staticmethod
    def _meta_info():
        from ydk.models.ethernet._meta import _Cisco_IOS_XR_ethernet_cfm_datatypes as meta
        return meta._meta_table['CfmAisIntervalEnum']


class CfmCcmIntervalEnum(Enum):
    """
    CfmCcmIntervalEnum

    Cfm ccm interval

    .. data:: Y_3__DOT__3MS = 1

    	3.3ms

    .. data:: Y_10MS = 2

    	10ms

    .. data:: Y_100MS = 3

    	100ms

    .. data:: Y_1S = 4

    	1s

    .. data:: Y_10S = 5

    	10s

    .. data:: Y_1M = 6

    	1m

    .. data:: Y_10M = 7

    	10m

    """

    Y_3__DOT__3MS = 1

    Y_10MS = 2

    Y_100MS = 3

    Y_1S = 4

    Y_10S = 5

    Y_1M = 6

    Y_10M = 7


    @staticmethod
    def _meta_info():
        from ydk.models.ethernet._meta import _Cisco_IOS_XR_ethernet_cfm_datatypes as meta
        return meta._meta_table['CfmCcmIntervalEnum']


class CfmMepDirEnum(Enum):
    """
    CfmMepDirEnum

    Cfm mep dir

    .. data:: UP = 0

    	Up MEP

    .. data:: DOWN = 1

    	Down MEP

    """

    UP = 0

    DOWN = 1


    @staticmethod
    def _meta_info():
        from ydk.models.ethernet._meta import _Cisco_IOS_XR_ethernet_cfm_datatypes as meta
        return meta._meta_table['CfmMepDirEnum']



