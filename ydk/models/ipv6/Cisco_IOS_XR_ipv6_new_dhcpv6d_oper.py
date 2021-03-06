""" Cisco_IOS_XR_ipv6_new_dhcpv6d_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR ipv6\-new\-dhcpv6d package operational data.

This module contains definitions
for the following management objects\:
  dhcpv6\: IPV6 DHCPD operational data

Copyright (c) 2013\-2015 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYDataValidationError



class BagDhcpv6DFsmStateEnum(Enum):
    """
    BagDhcpv6DFsmStateEnum

    Bag dhcpv6d fsm state

    .. data:: SERVER_INITIALIZING = 0

    	Server initializing state for client binding

    .. data:: SERVER_WAITING_DPM = 1

    	Server waiting on DPM to validate subscriber

    .. data:: SERVER_WAITING_DAPS = 2

    	Server waiting on DAPS to assign/free

    	addr/prefix

    .. data:: SERVER_WAITING_CLIENT = 3

    	Server waiting for a request from the client

    .. data:: SERVER_WAITING_SUBSCRIBER = 4

    	Server waiting for iedge response for the

    	session

    .. data:: SERVER_WAITING_RIB = 5

    	Server waiting for RIB response for route add

    .. data:: SERVER_BOUND_CLIENT = 6

    	Server bound state to the client

    .. data:: PROXY_INITIALIZING = 10

    	Proxy initializing state for client binding

    .. data:: PROXY_WAITING_DPM = 11

    	Proxy waiting on DPM to validate subscriber

    .. data:: PROXY_WAITING_DAPS = 12

    	Proxy waiting on DAPS to assign/free prefix(ND)

    .. data:: PROXY_WAITING_CLIENT_SERVER = 13

    	Proxy waiting for a msg from the client/srv

    .. data:: PROXY_WAITING_SUBSCRIBER = 14

    	Proxy waiting on iedge to sub session resp

    .. data:: PROXY_WAITING_RIB = 15

    	Proxy waiting on RIB response

    .. data:: PROXY_BOUND_CLIENT = 16

    	Proxy bound state to the client

    """

    SERVER_INITIALIZING = 0

    SERVER_WAITING_DPM = 1

    SERVER_WAITING_DAPS = 2

    SERVER_WAITING_CLIENT = 3

    SERVER_WAITING_SUBSCRIBER = 4

    SERVER_WAITING_RIB = 5

    SERVER_BOUND_CLIENT = 6

    PROXY_INITIALIZING = 10

    PROXY_WAITING_DPM = 11

    PROXY_WAITING_DAPS = 12

    PROXY_WAITING_CLIENT_SERVER = 13

    PROXY_WAITING_SUBSCRIBER = 14

    PROXY_WAITING_RIB = 15

    PROXY_BOUND_CLIENT = 16


    @staticmethod
    def _meta_info():
        from ydk.models.ipv6._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_oper as meta
        return meta._meta_table['BagDhcpv6DFsmStateEnum']


class BagDhcpv6DIaIdEnum(Enum):
    """
    BagDhcpv6DIaIdEnum

    Bag dhcpv6d ia id

    .. data:: IANA = 0

    	Non-temporary Addresses assigned 

    .. data:: IAPD = 1

    	Prefix delegeated to client      

    .. data:: IATA = 2

    	Temporary Addresses - not supported 

    """

    IANA = 0

    IAPD = 1

    IATA = 2


    @staticmethod
    def _meta_info():
        from ydk.models.ipv6._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_oper as meta
        return meta._meta_table['BagDhcpv6DIaIdEnum']



class Dhcpv6(object):
    """
    IPV6 DHCPD operational data
    
    .. attribute:: database
    
    	DHCP database
    	**type**\: :py:class:`Database <ydk.models.ipv6.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Database>`
    
    .. attribute:: nodes
    
    	IPv6 DHCP list of nodes
    	**type**\: :py:class:`Nodes <ydk.models.ipv6.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes>`
    
    

    """

    _prefix = 'ipv6-new-dhcpv6d-oper'
    _revision = '2015-11-09'

    def __init__(self):
        self.database = Dhcpv6.Database()
        self.database.parent = self
        self.nodes = Dhcpv6.Nodes()
        self.nodes.parent = self


    class Database(object):
        """
        DHCP database
        
        .. attribute:: configured
        
        	Database feature configured
        	**type**\: bool
        
        .. attribute:: version
        
        	Current file version
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: full_file_write_interval
        
        	Full file write interval in minutes
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: last_full_write_file_name
        
        	Last full write file name
        	**type**\: str
        
        	**range:** 0..64
        
        .. attribute:: last_full_write_time
        
        	Last full write time since epoch
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: full_file_write_count
        
        	Full file write count
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: failed_full_file_write_count
        
        	Failed full file write count
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: full_file_record_count
        
        	Full file record count
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: last_full_file_write_error_timestamp
        
        	Last full file write error timestamp since epoch
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: incremental_file_write_interval
        
        	Incremental file write interval in minutes
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: last_incremental_write_file_name
        
        	Last incremental write file name
        	**type**\: str
        
        	**range:** 0..64
        
        .. attribute:: last_incremental_write_time
        
        	Last incremental write time since epoch
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: incremental_file_write_count
        
        	Incremental file write count
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: failed_incremental_file_write_count
        
        	Failed incremental file write count
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: incremental_file_record_count
        
        	Incremental file record count
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: last_incremental_file_write_error_timestamp
        
        	Last incremental file write error timestamp since epoch
        	**type**\: int
        
        	**range:** 0..4294967295
        
        

        """

        _prefix = 'ipv6-new-dhcpv6d-oper'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.configured = None
            self.version = None
            self.full_file_write_interval = None
            self.last_full_write_file_name = None
            self.last_full_write_time = None
            self.full_file_write_count = None
            self.failed_full_file_write_count = None
            self.full_file_record_count = None
            self.last_full_file_write_error_timestamp = None
            self.incremental_file_write_interval = None
            self.last_incremental_write_file_name = None
            self.last_incremental_write_time = None
            self.incremental_file_write_count = None
            self.failed_incremental_file_write_count = None
            self.incremental_file_record_count = None
            self.last_incremental_file_write_error_timestamp = None

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-ipv6-new-dhcpv6d-oper:dhcpv6/Cisco-IOS-XR-ipv6-new-dhcpv6d-oper:database'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.configured is not None:
                return True

            if self.version is not None:
                return True

            if self.full_file_write_interval is not None:
                return True

            if self.last_full_write_file_name is not None:
                return True

            if self.last_full_write_time is not None:
                return True

            if self.full_file_write_count is not None:
                return True

            if self.failed_full_file_write_count is not None:
                return True

            if self.full_file_record_count is not None:
                return True

            if self.last_full_file_write_error_timestamp is not None:
                return True

            if self.incremental_file_write_interval is not None:
                return True

            if self.last_incremental_write_file_name is not None:
                return True

            if self.last_incremental_write_time is not None:
                return True

            if self.incremental_file_write_count is not None:
                return True

            if self.failed_incremental_file_write_count is not None:
                return True

            if self.incremental_file_record_count is not None:
                return True

            if self.last_incremental_file_write_error_timestamp is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.ipv6._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_oper as meta
            return meta._meta_table['Dhcpv6.Database']['meta_info']


    class Nodes(object):
        """
        IPv6 DHCP list of nodes
        
        .. attribute:: node
        
        	IPv6 DHCP particular node name
        	**type**\: list of :py:class:`Node <ydk.models.ipv6.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node>`
        
        

        """

        _prefix = 'ipv6-new-dhcpv6d-oper'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.node = YList()
            self.node.parent = self
            self.node.name = 'node'


        class Node(object):
            """
            IPv6 DHCP particular node name
            
            .. attribute:: node_name  <key>
            
            	Node name
            	**type**\: str
            
            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
            
            .. attribute:: proxy
            
            	IPv6 DHCP proxy operational data
            	**type**\: :py:class:`Proxy <ydk.models.ipv6.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Proxy>`
            
            .. attribute:: server
            
            	IPv6 DHCP server operational data
            	**type**\: :py:class:`Server <ydk.models.ipv6.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Server>`
            
            .. attribute:: relay
            
            	IPv6 DHCP relay operational data
            	**type**\: :py:class:`Relay <ydk.models.ipv6.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Relay>`
            
            

            """

            _prefix = 'ipv6-new-dhcpv6d-oper'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.node_name = None
                self.proxy = Dhcpv6.Nodes.Node.Proxy()
                self.proxy.parent = self
                self.server = Dhcpv6.Nodes.Node.Server()
                self.server.parent = self
                self.relay = Dhcpv6.Nodes.Node.Relay()
                self.relay.parent = self


            class Proxy(object):
                """
                IPv6 DHCP proxy operational data
                
                .. attribute:: vrfs
                
                	DHCPV6 proxy list of VRF names
                	**type**\: :py:class:`Vrfs <ydk.models.ipv6.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Proxy.Vrfs>`
                
                .. attribute:: profiles
                
                	IPv6 DHCP proxy profile
                	**type**\: :py:class:`Profiles <ydk.models.ipv6.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Proxy.Profiles>`
                
                .. attribute:: statistics
                
                	DHCPv6 proxy statistics
                	**type**\: :py:class:`Statistics <ydk.models.ipv6.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Proxy.Statistics>`
                
                .. attribute:: binding
                
                	DHCPV6 proxy bindings
                	**type**\: :py:class:`Binding <ydk.models.ipv6.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Proxy.Binding>`
                
                

                """

                _prefix = 'ipv6-new-dhcpv6d-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.vrfs = Dhcpv6.Nodes.Node.Proxy.Vrfs()
                    self.vrfs.parent = self
                    self.profiles = Dhcpv6.Nodes.Node.Proxy.Profiles()
                    self.profiles.parent = self
                    self.statistics = Dhcpv6.Nodes.Node.Proxy.Statistics()
                    self.statistics.parent = self
                    self.binding = Dhcpv6.Nodes.Node.Proxy.Binding()
                    self.binding.parent = self


                class Vrfs(object):
                    """
                    DHCPV6 proxy list of VRF names
                    
                    .. attribute:: vrf
                    
                    	IPv6 DHCP proxy VRF name
                    	**type**\: list of :py:class:`Vrf <ydk.models.ipv6.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Proxy.Vrfs.Vrf>`
                    
                    

                    """

                    _prefix = 'ipv6-new-dhcpv6d-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.vrf = YList()
                        self.vrf.parent = self
                        self.vrf.name = 'vrf'


                    class Vrf(object):
                        """
                        IPv6 DHCP proxy VRF name
                        
                        .. attribute:: vrf_name  <key>
                        
                        	VRF name
                        	**type**\: str
                        
                        	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                        
                        .. attribute:: statistics
                        
                        	IPv6 DHCP proxy statistics
                        	**type**\: :py:class:`Statistics <ydk.models.ipv6.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Proxy.Vrfs.Vrf.Statistics>`
                        
                        

                        """

                        _prefix = 'ipv6-new-dhcpv6d-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.vrf_name = None
                            self.statistics = Dhcpv6.Nodes.Node.Proxy.Vrfs.Vrf.Statistics()
                            self.statistics.parent = self


                        class Statistics(object):
                            """
                            IPv6 DHCP proxy statistics
                            
                            .. attribute:: solicit
                            
                            	DHCPV6 solicit packets
                            	**type**\: :py:class:`Solicit <ydk.models.ipv6.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.Solicit>`
                            
                            .. attribute:: advertise
                            
                            	DHCPV6 advertise packets
                            	**type**\: :py:class:`Advertise <ydk.models.ipv6.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.Advertise>`
                            
                            .. attribute:: request
                            
                            	DHCPV6 request packets
                            	**type**\: :py:class:`Request <ydk.models.ipv6.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.Request>`
                            
                            .. attribute:: reply
                            
                            	DHCPV6 reply packets
                            	**type**\: :py:class:`Reply <ydk.models.ipv6.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.Reply>`
                            
                            .. attribute:: confirm
                            
                            	DHCPV6 confirm packets
                            	**type**\: :py:class:`Confirm <ydk.models.ipv6.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.Confirm>`
                            
                            .. attribute:: decline
                            
                            	DHCPV6 decline packets
                            	**type**\: :py:class:`Decline <ydk.models.ipv6.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.Decline>`
                            
                            .. attribute:: renew
                            
                            	DHCPV6 renew packets
                            	**type**\: :py:class:`Renew <ydk.models.ipv6.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.Renew>`
                            
                            .. attribute:: rebind
                            
                            	DHCPV6 rebind packets
                            	**type**\: :py:class:`Rebind <ydk.models.ipv6.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.Rebind>`
                            
                            .. attribute:: release
                            
                            	DHCPV6 release packets
                            	**type**\: :py:class:`Release <ydk.models.ipv6.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.Release>`
                            
                            .. attribute:: reconfig
                            
                            	DHCPV6 reconfig packets
                            	**type**\: :py:class:`Reconfig <ydk.models.ipv6.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.Reconfig>`
                            
                            .. attribute:: inform
                            
                            	DHCPV6 inform packets
                            	**type**\: :py:class:`Inform <ydk.models.ipv6.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.Inform>`
                            
                            .. attribute:: relay_forward
                            
                            	DHCPV6 relay forward packets
                            	**type**\: :py:class:`RelayForward <ydk.models.ipv6.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.RelayForward>`
                            
                            .. attribute:: relay_reply
                            
                            	DHCPV6 relay reply packets
                            	**type**\: :py:class:`RelayReply <ydk.models.ipv6.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.RelayReply>`
                            
                            .. attribute:: lease_query
                            
                            	DHCPV6 lease query packets
                            	**type**\: :py:class:`LeaseQuery <ydk.models.ipv6.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.LeaseQuery>`
                            
                            .. attribute:: lease_query_reply
                            
                            	DHCPV6 lease query reply packets
                            	**type**\: :py:class:`LeaseQueryReply <ydk.models.ipv6.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.LeaseQueryReply>`
                            
                            .. attribute:: lease_query_done
                            
                            	DHCPV6 lease query done packets
                            	**type**\: :py:class:`LeaseQueryDone <ydk.models.ipv6.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.LeaseQueryDone>`
                            
                            .. attribute:: lease_query_data
                            
                            	DHCPV6 lease query data packets
                            	**type**\: :py:class:`LeaseQueryData <ydk.models.ipv6.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.LeaseQueryData>`
                            
                            

                            """

                            _prefix = 'ipv6-new-dhcpv6d-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.solicit = Dhcpv6.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.Solicit()
                                self.solicit.parent = self
                                self.advertise = Dhcpv6.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.Advertise()
                                self.advertise.parent = self
                                self.request = Dhcpv6.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.Request()
                                self.request.parent = self
                                self.reply = Dhcpv6.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.Reply()
                                self.reply.parent = self
                                self.confirm = Dhcpv6.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.Confirm()
                                self.confirm.parent = self
                                self.decline = Dhcpv6.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.Decline()
                                self.decline.parent = self
                                self.renew = Dhcpv6.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.Renew()
                                self.renew.parent = self
                                self.rebind = Dhcpv6.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.Rebind()
                                self.rebind.parent = self
                                self.release = Dhcpv6.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.Release()
                                self.release.parent = self
                                self.reconfig = Dhcpv6.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.Reconfig()
                                self.reconfig.parent = self
                                self.inform = Dhcpv6.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.Inform()
                                self.inform.parent = self
                                self.relay_forward = Dhcpv6.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.RelayForward()
                                self.relay_forward.parent = self
                                self.relay_reply = Dhcpv6.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.RelayReply()
                                self.relay_reply.parent = self
                                self.lease_query = Dhcpv6.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.LeaseQuery()
                                self.lease_query.parent = self
                                self.lease_query_reply = Dhcpv6.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.LeaseQueryReply()
                                self.lease_query_reply.parent = self
                                self.lease_query_done = Dhcpv6.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.LeaseQueryDone()
                                self.lease_query_done.parent = self
                                self.lease_query_data = Dhcpv6.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.LeaseQueryData()
                                self.lease_query_data.parent = self


                            class Solicit(object):
                                """
                                DHCPV6 solicit packets
                                
                                .. attribute:: received_packets
                                
                                	Received packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: transmitted_packets
                                
                                	Transmitted packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: dropped_packets
                                
                                	Dropped packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                

                                """

                                _prefix = 'ipv6-new-dhcpv6d-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.received_packets = None
                                    self.transmitted_packets = None
                                    self.dropped_packets = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ipv6-new-dhcpv6d-oper:solicit'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.received_packets is not None:
                                        return True

                                    if self.transmitted_packets is not None:
                                        return True

                                    if self.dropped_packets is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.ipv6._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_oper as meta
                                    return meta._meta_table['Dhcpv6.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.Solicit']['meta_info']


                            class Advertise(object):
                                """
                                DHCPV6 advertise packets
                                
                                .. attribute:: received_packets
                                
                                	Received packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: transmitted_packets
                                
                                	Transmitted packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: dropped_packets
                                
                                	Dropped packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                

                                """

                                _prefix = 'ipv6-new-dhcpv6d-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.received_packets = None
                                    self.transmitted_packets = None
                                    self.dropped_packets = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ipv6-new-dhcpv6d-oper:advertise'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.received_packets is not None:
                                        return True

                                    if self.transmitted_packets is not None:
                                        return True

                                    if self.dropped_packets is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.ipv6._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_oper as meta
                                    return meta._meta_table['Dhcpv6.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.Advertise']['meta_info']


                            class Request(object):
                                """
                                DHCPV6 request packets
                                
                                .. attribute:: received_packets
                                
                                	Received packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: transmitted_packets
                                
                                	Transmitted packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: dropped_packets
                                
                                	Dropped packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                

                                """

                                _prefix = 'ipv6-new-dhcpv6d-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.received_packets = None
                                    self.transmitted_packets = None
                                    self.dropped_packets = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ipv6-new-dhcpv6d-oper:request'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.received_packets is not None:
                                        return True

                                    if self.transmitted_packets is not None:
                                        return True

                                    if self.dropped_packets is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.ipv6._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_oper as meta
                                    return meta._meta_table['Dhcpv6.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.Request']['meta_info']


                            class Reply(object):
                                """
                                DHCPV6 reply packets
                                
                                .. attribute:: received_packets
                                
                                	Received packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: transmitted_packets
                                
                                	Transmitted packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: dropped_packets
                                
                                	Dropped packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                

                                """

                                _prefix = 'ipv6-new-dhcpv6d-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.received_packets = None
                                    self.transmitted_packets = None
                                    self.dropped_packets = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ipv6-new-dhcpv6d-oper:reply'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.received_packets is not None:
                                        return True

                                    if self.transmitted_packets is not None:
                                        return True

                                    if self.dropped_packets is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.ipv6._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_oper as meta
                                    return meta._meta_table['Dhcpv6.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.Reply']['meta_info']


                            class Confirm(object):
                                """
                                DHCPV6 confirm packets
                                
                                .. attribute:: received_packets
                                
                                	Received packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: transmitted_packets
                                
                                	Transmitted packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: dropped_packets
                                
                                	Dropped packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                

                                """

                                _prefix = 'ipv6-new-dhcpv6d-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.received_packets = None
                                    self.transmitted_packets = None
                                    self.dropped_packets = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ipv6-new-dhcpv6d-oper:confirm'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.received_packets is not None:
                                        return True

                                    if self.transmitted_packets is not None:
                                        return True

                                    if self.dropped_packets is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.ipv6._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_oper as meta
                                    return meta._meta_table['Dhcpv6.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.Confirm']['meta_info']


                            class Decline(object):
                                """
                                DHCPV6 decline packets
                                
                                .. attribute:: received_packets
                                
                                	Received packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: transmitted_packets
                                
                                	Transmitted packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: dropped_packets
                                
                                	Dropped packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                

                                """

                                _prefix = 'ipv6-new-dhcpv6d-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.received_packets = None
                                    self.transmitted_packets = None
                                    self.dropped_packets = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ipv6-new-dhcpv6d-oper:decline'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.received_packets is not None:
                                        return True

                                    if self.transmitted_packets is not None:
                                        return True

                                    if self.dropped_packets is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.ipv6._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_oper as meta
                                    return meta._meta_table['Dhcpv6.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.Decline']['meta_info']


                            class Renew(object):
                                """
                                DHCPV6 renew packets
                                
                                .. attribute:: received_packets
                                
                                	Received packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: transmitted_packets
                                
                                	Transmitted packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: dropped_packets
                                
                                	Dropped packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                

                                """

                                _prefix = 'ipv6-new-dhcpv6d-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.received_packets = None
                                    self.transmitted_packets = None
                                    self.dropped_packets = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ipv6-new-dhcpv6d-oper:renew'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.received_packets is not None:
                                        return True

                                    if self.transmitted_packets is not None:
                                        return True

                                    if self.dropped_packets is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.ipv6._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_oper as meta
                                    return meta._meta_table['Dhcpv6.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.Renew']['meta_info']


                            class Rebind(object):
                                """
                                DHCPV6 rebind packets
                                
                                .. attribute:: received_packets
                                
                                	Received packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: transmitted_packets
                                
                                	Transmitted packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: dropped_packets
                                
                                	Dropped packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                

                                """

                                _prefix = 'ipv6-new-dhcpv6d-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.received_packets = None
                                    self.transmitted_packets = None
                                    self.dropped_packets = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ipv6-new-dhcpv6d-oper:rebind'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.received_packets is not None:
                                        return True

                                    if self.transmitted_packets is not None:
                                        return True

                                    if self.dropped_packets is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.ipv6._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_oper as meta
                                    return meta._meta_table['Dhcpv6.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.Rebind']['meta_info']


                            class Release(object):
                                """
                                DHCPV6 release packets
                                
                                .. attribute:: received_packets
                                
                                	Received packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: transmitted_packets
                                
                                	Transmitted packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: dropped_packets
                                
                                	Dropped packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                

                                """

                                _prefix = 'ipv6-new-dhcpv6d-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.received_packets = None
                                    self.transmitted_packets = None
                                    self.dropped_packets = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ipv6-new-dhcpv6d-oper:release'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.received_packets is not None:
                                        return True

                                    if self.transmitted_packets is not None:
                                        return True

                                    if self.dropped_packets is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.ipv6._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_oper as meta
                                    return meta._meta_table['Dhcpv6.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.Release']['meta_info']


                            class Reconfig(object):
                                """
                                DHCPV6 reconfig packets
                                
                                .. attribute:: received_packets
                                
                                	Received packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: transmitted_packets
                                
                                	Transmitted packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: dropped_packets
                                
                                	Dropped packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                

                                """

                                _prefix = 'ipv6-new-dhcpv6d-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.received_packets = None
                                    self.transmitted_packets = None
                                    self.dropped_packets = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ipv6-new-dhcpv6d-oper:reconfig'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.received_packets is not None:
                                        return True

                                    if self.transmitted_packets is not None:
                                        return True

                                    if self.dropped_packets is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.ipv6._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_oper as meta
                                    return meta._meta_table['Dhcpv6.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.Reconfig']['meta_info']


                            class Inform(object):
                                """
                                DHCPV6 inform packets
                                
                                .. attribute:: received_packets
                                
                                	Received packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: transmitted_packets
                                
                                	Transmitted packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: dropped_packets
                                
                                	Dropped packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                

                                """

                                _prefix = 'ipv6-new-dhcpv6d-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.received_packets = None
                                    self.transmitted_packets = None
                                    self.dropped_packets = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ipv6-new-dhcpv6d-oper:inform'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.received_packets is not None:
                                        return True

                                    if self.transmitted_packets is not None:
                                        return True

                                    if self.dropped_packets is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.ipv6._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_oper as meta
                                    return meta._meta_table['Dhcpv6.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.Inform']['meta_info']


                            class RelayForward(object):
                                """
                                DHCPV6 relay forward packets
                                
                                .. attribute:: received_packets
                                
                                	Received packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: transmitted_packets
                                
                                	Transmitted packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: dropped_packets
                                
                                	Dropped packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                

                                """

                                _prefix = 'ipv6-new-dhcpv6d-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.received_packets = None
                                    self.transmitted_packets = None
                                    self.dropped_packets = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ipv6-new-dhcpv6d-oper:relay-forward'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.received_packets is not None:
                                        return True

                                    if self.transmitted_packets is not None:
                                        return True

                                    if self.dropped_packets is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.ipv6._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_oper as meta
                                    return meta._meta_table['Dhcpv6.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.RelayForward']['meta_info']


                            class RelayReply(object):
                                """
                                DHCPV6 relay reply packets
                                
                                .. attribute:: received_packets
                                
                                	Received packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: transmitted_packets
                                
                                	Transmitted packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: dropped_packets
                                
                                	Dropped packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                

                                """

                                _prefix = 'ipv6-new-dhcpv6d-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.received_packets = None
                                    self.transmitted_packets = None
                                    self.dropped_packets = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ipv6-new-dhcpv6d-oper:relay-reply'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.received_packets is not None:
                                        return True

                                    if self.transmitted_packets is not None:
                                        return True

                                    if self.dropped_packets is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.ipv6._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_oper as meta
                                    return meta._meta_table['Dhcpv6.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.RelayReply']['meta_info']


                            class LeaseQuery(object):
                                """
                                DHCPV6 lease query packets
                                
                                .. attribute:: received_packets
                                
                                	Received packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: transmitted_packets
                                
                                	Transmitted packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: dropped_packets
                                
                                	Dropped packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                

                                """

                                _prefix = 'ipv6-new-dhcpv6d-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.received_packets = None
                                    self.transmitted_packets = None
                                    self.dropped_packets = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ipv6-new-dhcpv6d-oper:lease-query'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.received_packets is not None:
                                        return True

                                    if self.transmitted_packets is not None:
                                        return True

                                    if self.dropped_packets is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.ipv6._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_oper as meta
                                    return meta._meta_table['Dhcpv6.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.LeaseQuery']['meta_info']


                            class LeaseQueryReply(object):
                                """
                                DHCPV6 lease query reply packets
                                
                                .. attribute:: received_packets
                                
                                	Received packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: transmitted_packets
                                
                                	Transmitted packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: dropped_packets
                                
                                	Dropped packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                

                                """

                                _prefix = 'ipv6-new-dhcpv6d-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.received_packets = None
                                    self.transmitted_packets = None
                                    self.dropped_packets = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ipv6-new-dhcpv6d-oper:lease-query-reply'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.received_packets is not None:
                                        return True

                                    if self.transmitted_packets is not None:
                                        return True

                                    if self.dropped_packets is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.ipv6._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_oper as meta
                                    return meta._meta_table['Dhcpv6.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.LeaseQueryReply']['meta_info']


                            class LeaseQueryDone(object):
                                """
                                DHCPV6 lease query done packets
                                
                                .. attribute:: received_packets
                                
                                	Received packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: transmitted_packets
                                
                                	Transmitted packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: dropped_packets
                                
                                	Dropped packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                

                                """

                                _prefix = 'ipv6-new-dhcpv6d-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.received_packets = None
                                    self.transmitted_packets = None
                                    self.dropped_packets = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ipv6-new-dhcpv6d-oper:lease-query-done'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.received_packets is not None:
                                        return True

                                    if self.transmitted_packets is not None:
                                        return True

                                    if self.dropped_packets is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.ipv6._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_oper as meta
                                    return meta._meta_table['Dhcpv6.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.LeaseQueryDone']['meta_info']


                            class LeaseQueryData(object):
                                """
                                DHCPV6 lease query data packets
                                
                                .. attribute:: received_packets
                                
                                	Received packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: transmitted_packets
                                
                                	Transmitted packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: dropped_packets
                                
                                	Dropped packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                

                                """

                                _prefix = 'ipv6-new-dhcpv6d-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.received_packets = None
                                    self.transmitted_packets = None
                                    self.dropped_packets = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ipv6-new-dhcpv6d-oper:lease-query-data'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.received_packets is not None:
                                        return True

                                    if self.transmitted_packets is not None:
                                        return True

                                    if self.dropped_packets is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.ipv6._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_oper as meta
                                    return meta._meta_table['Dhcpv6.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.LeaseQueryData']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-ipv6-new-dhcpv6d-oper:statistics'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.solicit is not None and self.solicit._has_data():
                                    return True

                                if self.advertise is not None and self.advertise._has_data():
                                    return True

                                if self.request is not None and self.request._has_data():
                                    return True

                                if self.reply is not None and self.reply._has_data():
                                    return True

                                if self.confirm is not None and self.confirm._has_data():
                                    return True

                                if self.decline is not None and self.decline._has_data():
                                    return True

                                if self.renew is not None and self.renew._has_data():
                                    return True

                                if self.rebind is not None and self.rebind._has_data():
                                    return True

                                if self.release is not None and self.release._has_data():
                                    return True

                                if self.reconfig is not None and self.reconfig._has_data():
                                    return True

                                if self.inform is not None and self.inform._has_data():
                                    return True

                                if self.relay_forward is not None and self.relay_forward._has_data():
                                    return True

                                if self.relay_reply is not None and self.relay_reply._has_data():
                                    return True

                                if self.lease_query is not None and self.lease_query._has_data():
                                    return True

                                if self.lease_query_reply is not None and self.lease_query_reply._has_data():
                                    return True

                                if self.lease_query_done is not None and self.lease_query_done._has_data():
                                    return True

                                if self.lease_query_data is not None and self.lease_query_data._has_data():
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.ipv6._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_oper as meta
                                return meta._meta_table['Dhcpv6.Nodes.Node.Proxy.Vrfs.Vrf.Statistics']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')
                            if self.vrf_name is None:
                                raise YPYDataValidationError('Key property vrf_name is None')

                            return self.parent._common_path +'/Cisco-IOS-XR-ipv6-new-dhcpv6d-oper:vrf[Cisco-IOS-XR-ipv6-new-dhcpv6d-oper:vrf-name = ' + str(self.vrf_name) + ']'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.vrf_name is not None:
                                return True

                            if self.statistics is not None and self.statistics._has_data():
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.ipv6._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_oper as meta
                            return meta._meta_table['Dhcpv6.Nodes.Node.Proxy.Vrfs.Vrf']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ipv6-new-dhcpv6d-oper:vrfs'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.vrf is not None:
                            for child_ref in self.vrf:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.ipv6._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_oper as meta
                        return meta._meta_table['Dhcpv6.Nodes.Node.Proxy.Vrfs']['meta_info']


                class Profiles(object):
                    """
                    IPv6 DHCP proxy profile
                    
                    .. attribute:: profile
                    
                    	IPv6 DHCP proxy profile
                    	**type**\: list of :py:class:`Profile <ydk.models.ipv6.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Proxy.Profiles.Profile>`
                    
                    

                    """

                    _prefix = 'ipv6-new-dhcpv6d-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.profile = YList()
                        self.profile.parent = self
                        self.profile.name = 'profile'


                    class Profile(object):
                        """
                        IPv6 DHCP proxy profile
                        
                        .. attribute:: profile_name  <key>
                        
                        	Profile name
                        	**type**\: str
                        
                        	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                        
                        .. attribute:: throttle_infos
                        
                        	DHCPV6 throttle table
                        	**type**\: :py:class:`ThrottleInfos <ydk.models.ipv6.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Proxy.Profiles.Profile.ThrottleInfos>`
                        
                        .. attribute:: info
                        
                        	IPv6 DHCP proxy profile Info
                        	**type**\: :py:class:`Info <ydk.models.ipv6.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Proxy.Profiles.Profile.Info>`
                        
                        

                        """

                        _prefix = 'ipv6-new-dhcpv6d-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.profile_name = None
                            self.throttle_infos = Dhcpv6.Nodes.Node.Proxy.Profiles.Profile.ThrottleInfos()
                            self.throttle_infos.parent = self
                            self.info = Dhcpv6.Nodes.Node.Proxy.Profiles.Profile.Info()
                            self.info.parent = self


                        class ThrottleInfos(object):
                            """
                            DHCPV6 throttle table
                            
                            .. attribute:: throttle_info
                            
                            	IPv6 DHCP proxy profile Throttle Info
                            	**type**\: list of :py:class:`ThrottleInfo <ydk.models.ipv6.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Proxy.Profiles.Profile.ThrottleInfos.ThrottleInfo>`
                            
                            

                            """

                            _prefix = 'ipv6-new-dhcpv6d-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.throttle_info = YList()
                                self.throttle_info.parent = self
                                self.throttle_info.name = 'throttle_info'


                            class ThrottleInfo(object):
                                """
                                IPv6 DHCP proxy profile Throttle Info
                                
                                .. attribute:: mac_address  <key>
                                
                                	MAC address
                                	**type**\: str
                                
                                	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                                
                                .. attribute:: binding_chaddr
                                
                                	Client MAC address
                                	**type**\: str
                                
                                	**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
                                
                                .. attribute:: ifname
                                
                                	DHCP access interface
                                	**type**\: str
                                
                                	**range:** 0..65
                                
                                .. attribute:: state
                                
                                	State of entry
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: time_left
                                
                                	Time Left in secs
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'ipv6-new-dhcpv6d-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.mac_address = None
                                    self.binding_chaddr = None
                                    self.ifname = None
                                    self.state = None
                                    self.time_left = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYDataValidationError('parent is not set . Cannot derive path.')
                                    if self.mac_address is None:
                                        raise YPYDataValidationError('Key property mac_address is None')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ipv6-new-dhcpv6d-oper:throttle-info[Cisco-IOS-XR-ipv6-new-dhcpv6d-oper:mac-address = ' + str(self.mac_address) + ']'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.mac_address is not None:
                                        return True

                                    if self.binding_chaddr is not None:
                                        return True

                                    if self.ifname is not None:
                                        return True

                                    if self.state is not None:
                                        return True

                                    if self.time_left is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.ipv6._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_oper as meta
                                    return meta._meta_table['Dhcpv6.Nodes.Node.Proxy.Profiles.Profile.ThrottleInfos.ThrottleInfo']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-ipv6-new-dhcpv6d-oper:throttle-infos'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.throttle_info is not None:
                                    for child_ref in self.throttle_info:
                                        if child_ref._has_data():
                                            return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.ipv6._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_oper as meta
                                return meta._meta_table['Dhcpv6.Nodes.Node.Proxy.Profiles.Profile.ThrottleInfos']['meta_info']


                        class Info(object):
                            """
                            IPv6 DHCP proxy profile Info
                            
                            .. attribute:: interface_id_references
                            
                            	Interface id references
                            	**type**\: :py:class:`InterfaceIdReferences <ydk.models.ipv6.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Proxy.Profiles.Profile.Info.InterfaceIdReferences>`
                            
                            .. attribute:: vrf_references
                            
                            	VRF references
                            	**type**\: :py:class:`VrfReferences <ydk.models.ipv6.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Proxy.Profiles.Profile.Info.VrfReferences>`
                            
                            .. attribute:: interface_references
                            
                            	Interface references
                            	**type**\: :py:class:`InterfaceReferences <ydk.models.ipv6.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Proxy.Profiles.Profile.Info.InterfaceReferences>`
                            
                            .. attribute:: profile_name
                            
                            	Proxy profile name
                            	**type**\: str
                            
                            	**range:** 0..65
                            
                            .. attribute:: remote_id
                            
                            	Remote id
                            	**type**\: str
                            
                            	**range:** 0..257
                            
                            .. attribute:: profile_link_address
                            
                            	Link address
                            	**type**\: str
                            
                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: profile_helper_address
                            
                            	Helper addresses
                            	**type**\: list of str
                            
                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: vrf_name
                            
                            	VRF names
                            	**type**\: list of str
                            
                            	**range:** 0..33
                            
                            .. attribute:: interface_name
                            
                            	Interface names
                            	**type**\: list of str
                            
                            	**range:** 0..65
                            
                            

                            """

                            _prefix = 'ipv6-new-dhcpv6d-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.interface_id_references = Dhcpv6.Nodes.Node.Proxy.Profiles.Profile.Info.InterfaceIdReferences()
                                self.interface_id_references.parent = self
                                self.vrf_references = Dhcpv6.Nodes.Node.Proxy.Profiles.Profile.Info.VrfReferences()
                                self.vrf_references.parent = self
                                self.interface_references = Dhcpv6.Nodes.Node.Proxy.Profiles.Profile.Info.InterfaceReferences()
                                self.interface_references.parent = self
                                self.profile_name = None
                                self.remote_id = None
                                self.profile_link_address = None
                                self.profile_helper_address = YLeafList()
                                self.profile_helper_address.parent = self
                                self.profile_helper_address.name = 'profile_helper_address'
                                self.vrf_name = YLeafList()
                                self.vrf_name.parent = self
                                self.vrf_name.name = 'vrf_name'
                                self.interface_name = YLeafList()
                                self.interface_name.parent = self
                                self.interface_name.name = 'interface_name'


                            class InterfaceIdReferences(object):
                                """
                                Interface id references
                                
                                .. attribute:: ipv6_dhcpv6d_proxy_iid_reference
                                
                                	ipv6 dhcpv6d proxy iid reference
                                	**type**\: list of :py:class:`Ipv6Dhcpv6DProxyIidReference <ydk.models.ipv6.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Proxy.Profiles.Profile.Info.InterfaceIdReferences.Ipv6Dhcpv6DProxyIidReference>`
                                
                                

                                """

                                _prefix = 'ipv6-new-dhcpv6d-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.ipv6_dhcpv6d_proxy_iid_reference = YList()
                                    self.ipv6_dhcpv6d_proxy_iid_reference.parent = self
                                    self.ipv6_dhcpv6d_proxy_iid_reference.name = 'ipv6_dhcpv6d_proxy_iid_reference'


                                class Ipv6Dhcpv6DProxyIidReference(object):
                                    """
                                    ipv6 dhcpv6d proxy iid reference
                                    
                                    .. attribute:: proxy_iid_interface_name
                                    
                                    	Interface name for interface id
                                    	**type**\: str
                                    
                                    	**range:** 0..65
                                    
                                    .. attribute:: proxy_interface_id
                                    
                                    	Interface id
                                    	**type**\: str
                                    
                                    	**range:** 0..257
                                    
                                    

                                    """

                                    _prefix = 'ipv6-new-dhcpv6d-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.proxy_iid_interface_name = None
                                        self.proxy_interface_id = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-ipv6-new-dhcpv6d-oper:ipv6-dhcpv6d-proxy-iid-reference'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        if not self.is_config():
                                            return False
                                        if self.proxy_iid_interface_name is not None:
                                            return True

                                        if self.proxy_interface_id is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.ipv6._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_oper as meta
                                        return meta._meta_table['Dhcpv6.Nodes.Node.Proxy.Profiles.Profile.Info.InterfaceIdReferences.Ipv6Dhcpv6DProxyIidReference']['meta_info']

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ipv6-new-dhcpv6d-oper:interface-id-references'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.ipv6_dhcpv6d_proxy_iid_reference is not None:
                                        for child_ref in self.ipv6_dhcpv6d_proxy_iid_reference:
                                            if child_ref._has_data():
                                                return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.ipv6._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_oper as meta
                                    return meta._meta_table['Dhcpv6.Nodes.Node.Proxy.Profiles.Profile.Info.InterfaceIdReferences']['meta_info']


                            class VrfReferences(object):
                                """
                                VRF references
                                
                                .. attribute:: ipv6_dhcpv6d_proxy_vrf_reference
                                
                                	ipv6 dhcpv6d proxy vrf reference
                                	**type**\: list of :py:class:`Ipv6Dhcpv6DProxyVrfReference <ydk.models.ipv6.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Proxy.Profiles.Profile.Info.VrfReferences.Ipv6Dhcpv6DProxyVrfReference>`
                                
                                

                                """

                                _prefix = 'ipv6-new-dhcpv6d-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.ipv6_dhcpv6d_proxy_vrf_reference = YList()
                                    self.ipv6_dhcpv6d_proxy_vrf_reference.parent = self
                                    self.ipv6_dhcpv6d_proxy_vrf_reference.name = 'ipv6_dhcpv6d_proxy_vrf_reference'


                                class Ipv6Dhcpv6DProxyVrfReference(object):
                                    """
                                    ipv6 dhcpv6d proxy vrf reference
                                    
                                    .. attribute:: proxy_reference_vrf_name
                                    
                                    	VRF name
                                    	**type**\: str
                                    
                                    	**range:** 0..33
                                    
                                    

                                    """

                                    _prefix = 'ipv6-new-dhcpv6d-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.proxy_reference_vrf_name = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-ipv6-new-dhcpv6d-oper:ipv6-dhcpv6d-proxy-vrf-reference'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        if not self.is_config():
                                            return False
                                        if self.proxy_reference_vrf_name is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.ipv6._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_oper as meta
                                        return meta._meta_table['Dhcpv6.Nodes.Node.Proxy.Profiles.Profile.Info.VrfReferences.Ipv6Dhcpv6DProxyVrfReference']['meta_info']

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ipv6-new-dhcpv6d-oper:vrf-references'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.ipv6_dhcpv6d_proxy_vrf_reference is not None:
                                        for child_ref in self.ipv6_dhcpv6d_proxy_vrf_reference:
                                            if child_ref._has_data():
                                                return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.ipv6._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_oper as meta
                                    return meta._meta_table['Dhcpv6.Nodes.Node.Proxy.Profiles.Profile.Info.VrfReferences']['meta_info']


                            class InterfaceReferences(object):
                                """
                                Interface references
                                
                                .. attribute:: ipv6_dhcpv6d_proxy_interface_reference
                                
                                	ipv6 dhcpv6d proxy interface reference
                                	**type**\: list of :py:class:`Ipv6Dhcpv6DProxyInterfaceReference <ydk.models.ipv6.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Proxy.Profiles.Profile.Info.InterfaceReferences.Ipv6Dhcpv6DProxyInterfaceReference>`
                                
                                

                                """

                                _prefix = 'ipv6-new-dhcpv6d-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.ipv6_dhcpv6d_proxy_interface_reference = YList()
                                    self.ipv6_dhcpv6d_proxy_interface_reference.parent = self
                                    self.ipv6_dhcpv6d_proxy_interface_reference.name = 'ipv6_dhcpv6d_proxy_interface_reference'


                                class Ipv6Dhcpv6DProxyInterfaceReference(object):
                                    """
                                    ipv6 dhcpv6d proxy interface reference
                                    
                                    .. attribute:: proxy_reference_interface_name
                                    
                                    	Interface name
                                    	**type**\: str
                                    
                                    	**range:** 0..65
                                    
                                    

                                    """

                                    _prefix = 'ipv6-new-dhcpv6d-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.proxy_reference_interface_name = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-ipv6-new-dhcpv6d-oper:ipv6-dhcpv6d-proxy-interface-reference'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        if not self.is_config():
                                            return False
                                        if self.proxy_reference_interface_name is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.ipv6._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_oper as meta
                                        return meta._meta_table['Dhcpv6.Nodes.Node.Proxy.Profiles.Profile.Info.InterfaceReferences.Ipv6Dhcpv6DProxyInterfaceReference']['meta_info']

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ipv6-new-dhcpv6d-oper:interface-references'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.ipv6_dhcpv6d_proxy_interface_reference is not None:
                                        for child_ref in self.ipv6_dhcpv6d_proxy_interface_reference:
                                            if child_ref._has_data():
                                                return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.ipv6._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_oper as meta
                                    return meta._meta_table['Dhcpv6.Nodes.Node.Proxy.Profiles.Profile.Info.InterfaceReferences']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-ipv6-new-dhcpv6d-oper:info'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.interface_id_references is not None and self.interface_id_references._has_data():
                                    return True

                                if self.vrf_references is not None and self.vrf_references._has_data():
                                    return True

                                if self.interface_references is not None and self.interface_references._has_data():
                                    return True

                                if self.profile_name is not None:
                                    return True

                                if self.remote_id is not None:
                                    return True

                                if self.profile_link_address is not None:
                                    return True

                                if self.profile_helper_address is not None:
                                    for child in self.profile_helper_address:
                                        if child is not None:
                                            return True

                                if self.vrf_name is not None:
                                    for child in self.vrf_name:
                                        if child is not None:
                                            return True

                                if self.interface_name is not None:
                                    for child in self.interface_name:
                                        if child is not None:
                                            return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.ipv6._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_oper as meta
                                return meta._meta_table['Dhcpv6.Nodes.Node.Proxy.Profiles.Profile.Info']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')
                            if self.profile_name is None:
                                raise YPYDataValidationError('Key property profile_name is None')

                            return self.parent._common_path +'/Cisco-IOS-XR-ipv6-new-dhcpv6d-oper:profile[Cisco-IOS-XR-ipv6-new-dhcpv6d-oper:profile-name = ' + str(self.profile_name) + ']'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.profile_name is not None:
                                return True

                            if self.throttle_infos is not None and self.throttle_infos._has_data():
                                return True

                            if self.info is not None and self.info._has_data():
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.ipv6._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_oper as meta
                            return meta._meta_table['Dhcpv6.Nodes.Node.Proxy.Profiles.Profile']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ipv6-new-dhcpv6d-oper:profiles'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.profile is not None:
                            for child_ref in self.profile:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.ipv6._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_oper as meta
                        return meta._meta_table['Dhcpv6.Nodes.Node.Proxy.Profiles']['meta_info']


                class Statistics(object):
                    """
                    DHCPv6 proxy statistics
                    
                    .. attribute:: ipv6_dhcpv6d_proxy_stat
                    
                    	ipv6 dhcpv6d proxy stat
                    	**type**\: list of :py:class:`Ipv6Dhcpv6DProxyStat <ydk.models.ipv6.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Proxy.Statistics.Ipv6Dhcpv6DProxyStat>`
                    
                    

                    """

                    _prefix = 'ipv6-new-dhcpv6d-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.ipv6_dhcpv6d_proxy_stat = YList()
                        self.ipv6_dhcpv6d_proxy_stat.parent = self
                        self.ipv6_dhcpv6d_proxy_stat.name = 'ipv6_dhcpv6d_proxy_stat'


                    class Ipv6Dhcpv6DProxyStat(object):
                        """
                        ipv6 dhcpv6d proxy stat
                        
                        .. attribute:: statistics
                        
                        	Proxy statistics
                        	**type**\: :py:class:`Statistics <ydk.models.ipv6.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Proxy.Statistics.Ipv6Dhcpv6DProxyStat.Statistics>`
                        
                        .. attribute:: vrf_name
                        
                        	DHCPv6 L3 VRF name
                        	**type**\: str
                        
                        	**range:** 0..33
                        
                        

                        """

                        _prefix = 'ipv6-new-dhcpv6d-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.statistics = Dhcpv6.Nodes.Node.Proxy.Statistics.Ipv6Dhcpv6DProxyStat.Statistics()
                            self.statistics.parent = self
                            self.vrf_name = None


                        class Statistics(object):
                            """
                            Proxy statistics
                            
                            .. attribute:: received_packets
                            
                            	Received packets
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: transmitted_packets
                            
                            	Transmitted packets
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: dropped_packets
                            
                            	Dropped packets
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            

                            """

                            _prefix = 'ipv6-new-dhcpv6d-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.received_packets = None
                                self.transmitted_packets = None
                                self.dropped_packets = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-ipv6-new-dhcpv6d-oper:statistics'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.received_packets is not None:
                                    return True

                                if self.transmitted_packets is not None:
                                    return True

                                if self.dropped_packets is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.ipv6._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_oper as meta
                                return meta._meta_table['Dhcpv6.Nodes.Node.Proxy.Statistics.Ipv6Dhcpv6DProxyStat.Statistics']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-ipv6-new-dhcpv6d-oper:ipv6-dhcpv6d-proxy-stat'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.statistics is not None and self.statistics._has_data():
                                return True

                            if self.vrf_name is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.ipv6._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_oper as meta
                            return meta._meta_table['Dhcpv6.Nodes.Node.Proxy.Statistics.Ipv6Dhcpv6DProxyStat']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ipv6-new-dhcpv6d-oper:statistics'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.ipv6_dhcpv6d_proxy_stat is not None:
                            for child_ref in self.ipv6_dhcpv6d_proxy_stat:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.ipv6._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_oper as meta
                        return meta._meta_table['Dhcpv6.Nodes.Node.Proxy.Statistics']['meta_info']


                class Binding(object):
                    """
                    DHCPV6 proxy bindings
                    
                    .. attribute:: clients
                    
                    	DHCPV6 proxy client bindings
                    	**type**\: :py:class:`Clients <ydk.models.ipv6.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Proxy.Binding.Clients>`
                    
                    .. attribute:: summary
                    
                    	DHCPV6 proxy binding summary
                    	**type**\: :py:class:`Summary <ydk.models.ipv6.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Proxy.Binding.Summary>`
                    
                    

                    """

                    _prefix = 'ipv6-new-dhcpv6d-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.clients = Dhcpv6.Nodes.Node.Proxy.Binding.Clients()
                        self.clients.parent = self
                        self.summary = Dhcpv6.Nodes.Node.Proxy.Binding.Summary()
                        self.summary.parent = self


                    class Clients(object):
                        """
                        DHCPV6 proxy client bindings
                        
                        .. attribute:: client
                        
                        	Single DHCPV6 proxy binding
                        	**type**\: list of :py:class:`Client <ydk.models.ipv6.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Proxy.Binding.Clients.Client>`
                        
                        

                        """

                        _prefix = 'ipv6-new-dhcpv6d-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.client = YList()
                            self.client.parent = self
                            self.client.name = 'client'


                        class Client(object):
                            """
                            Single DHCPV6 proxy binding
                            
                            .. attribute:: client_id  <key>
                            
                            	Client ID
                            	**type**\: str
                            
                            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                            
                            .. attribute:: ia_id_pd
                            
                            	List of DHCPv6 IA\_ID/PDs
                            	**type**\: :py:class:`IaIdPd <ydk.models.ipv6.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Proxy.Binding.Clients.Client.IaIdPd>`
                            
                            .. attribute:: duid
                            
                            	Client DUID
                            	**type**\: str
                            
                            .. attribute:: client_flag
                            
                            	DHCPV6 client flag
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: subscriber_label
                            
                            	DHCPV6 subscriber label
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: vrf_name
                            
                            	DHCPVV6 client/subscriber VRF name
                            	**type**\: str
                            
                            	**range:** 0..33
                            
                            .. attribute:: mac_address
                            
                            	Client MAC address
                            	**type**\: str
                            
                            .. attribute:: ia_id_p_ds
                            
                            	Number of ia\_id/pd
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: interface_name
                            
                            	DHCPV6 access interface to client
                            	**type**\: str
                            
                            	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                            
                            .. attribute:: access_vrf_name
                            
                            	DHCPV6 access VRF name to client
                            	**type**\: str
                            
                            	**range:** 0..33
                            
                            .. attribute:: proxy_binding_tags
                            
                            	DHCPV6 VLAN tag count
                            	**type**\: int
                            
                            	**range:** 0..255
                            
                            .. attribute:: proxy_binding_outer_tag
                            
                            	DHCPV6 VLAN Outer VLAN
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: proxy_binding_inner_tag
                            
                            	DHCPV6 VLAN Inner VLAN
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: class_name
                            
                            	DHCPV6 class name
                            	**type**\: str
                            
                            	**range:** 0..64
                            
                            .. attribute:: pool_name
                            
                            	DHCPV6 pool name
                            	**type**\: str
                            
                            	**range:** 0..64
                            
                            .. attribute:: rx_remote_id
                            
                            	DHCPV6 received Remote ID
                            	**type**\: str
                            
                            	**range:** 0..771
                            
                            .. attribute:: tx_remote_id
                            
                            	DHCPV6 transmitted Remote ID
                            	**type**\: str
                            
                            	**range:** 0..771
                            
                            .. attribute:: rx_interface_id
                            
                            	DHCPV6 received Interface ID
                            	**type**\: str
                            
                            	**range:** 0..771
                            
                            .. attribute:: tx_interface_id
                            
                            	DHCPV6 transmitted Interface ID
                            	**type**\: str
                            
                            	**range:** 0..771
                            
                            .. attribute:: server_ipv6_address
                            
                            	DHCPV6 server IPv6 address
                            	**type**\: str
                            
                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: profile_name
                            
                            	DHCPV6 profile name
                            	**type**\: str
                            
                            	**range:** 0..65
                            
                            .. attribute:: framed_ipv6_prefix
                            
                            	DHCPV6 framed ipv6 addess used by ND
                            	**type**\: str
                            
                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: framed_prefix_length
                            
                            	DHCPV6 framed ipv6 prefix length used by ND
                            	**type**\: int
                            
                            	**range:** 0..255
                            
                            .. attribute:: is_nak_next_renew
                            
                            	Is true if DHCP next renew from client will be NAK'd
                            	**type**\: bool
                            
                            .. attribute:: srg_state
                            
                            	DHCPV6 SRG state
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: srg_intf_role
                            
                            	DHCPV6 SRG Intf Role
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'ipv6-new-dhcpv6d-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.client_id = None
                                self.ia_id_pd = Dhcpv6.Nodes.Node.Proxy.Binding.Clients.Client.IaIdPd()
                                self.ia_id_pd.parent = self
                                self.duid = None
                                self.client_flag = None
                                self.subscriber_label = None
                                self.vrf_name = None
                                self.mac_address = None
                                self.ia_id_p_ds = None
                                self.interface_name = None
                                self.access_vrf_name = None
                                self.proxy_binding_tags = None
                                self.proxy_binding_outer_tag = None
                                self.proxy_binding_inner_tag = None
                                self.class_name = None
                                self.pool_name = None
                                self.rx_remote_id = None
                                self.tx_remote_id = None
                                self.rx_interface_id = None
                                self.tx_interface_id = None
                                self.server_ipv6_address = None
                                self.profile_name = None
                                self.framed_ipv6_prefix = None
                                self.framed_prefix_length = None
                                self.is_nak_next_renew = None
                                self.srg_state = None
                                self.srg_intf_role = None


                            class IaIdPd(object):
                                """
                                List of DHCPv6 IA\_ID/PDs
                                
                                .. attribute:: bag_dhcpv6d_ia_id_pd_info
                                
                                	bag dhcpv6d ia id pd info
                                	**type**\: list of :py:class:`BagDhcpv6DIaIdPdInfo <ydk.models.ipv6.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Proxy.Binding.Clients.Client.IaIdPd.BagDhcpv6DIaIdPdInfo>`
                                
                                

                                """

                                _prefix = 'ipv6-new-dhcpv6d-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.bag_dhcpv6d_ia_id_pd_info = YList()
                                    self.bag_dhcpv6d_ia_id_pd_info.parent = self
                                    self.bag_dhcpv6d_ia_id_pd_info.name = 'bag_dhcpv6d_ia_id_pd_info'


                                class BagDhcpv6DIaIdPdInfo(object):
                                    """
                                    bag dhcpv6d ia id pd info
                                    
                                    .. attribute:: addresses
                                    
                                    	List of addresses in this IA
                                    	**type**\: :py:class:`Addresses <ydk.models.ipv6.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Proxy.Binding.Clients.Client.IaIdPd.BagDhcpv6DIaIdPdInfo.Addresses>`
                                    
                                    .. attribute:: ia_type
                                    
                                    	IA type
                                    	**type**\: :py:class:`BagDhcpv6DIaIdEnum <ydk.models.ipv6.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.BagDhcpv6DIaIdEnum>`
                                    
                                    .. attribute:: ia_id
                                    
                                    	IA\_ID of this IA
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: flags
                                    
                                    	FSM Flag for this IA
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: total_address
                                    
                                    	Total address in this IA
                                    	**type**\: int
                                    
                                    	**range:** 0..65535
                                    
                                    .. attribute:: state
                                    
                                    	State
                                    	**type**\: :py:class:`BagDhcpv6DFsmStateEnum <ydk.models.ipv6.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.BagDhcpv6DFsmStateEnum>`
                                    
                                    

                                    """

                                    _prefix = 'ipv6-new-dhcpv6d-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.addresses = Dhcpv6.Nodes.Node.Proxy.Binding.Clients.Client.IaIdPd.BagDhcpv6DIaIdPdInfo.Addresses()
                                        self.addresses.parent = self
                                        self.ia_type = None
                                        self.ia_id = None
                                        self.flags = None
                                        self.total_address = None
                                        self.state = None


                                    class Addresses(object):
                                        """
                                        List of addresses in this IA
                                        
                                        .. attribute:: bag_dhcpv6d_addr_attrb
                                        
                                        	bag dhcpv6d addr attrb
                                        	**type**\: list of :py:class:`BagDhcpv6DAddrAttrb <ydk.models.ipv6.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Proxy.Binding.Clients.Client.IaIdPd.BagDhcpv6DIaIdPdInfo.Addresses.BagDhcpv6DAddrAttrb>`
                                        
                                        

                                        """

                                        _prefix = 'ipv6-new-dhcpv6d-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            self.parent = None
                                            self.bag_dhcpv6d_addr_attrb = YList()
                                            self.bag_dhcpv6d_addr_attrb.parent = self
                                            self.bag_dhcpv6d_addr_attrb.name = 'bag_dhcpv6d_addr_attrb'


                                        class BagDhcpv6DAddrAttrb(object):
                                            """
                                            bag dhcpv6d addr attrb
                                            
                                            .. attribute:: prefix
                                            
                                            	IPv6 prefix
                                            	**type**\: str
                                            
                                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                            
                                            .. attribute:: prefix_length
                                            
                                            	Prefix length
                                            	**type**\: int
                                            
                                            	**range:** 0..255
                                            
                                            .. attribute:: lease_time
                                            
                                            	Lease time in seconds
                                            	**type**\: int
                                            
                                            	**range:** 0..4294967295
                                            
                                            .. attribute:: remaining_lease_time
                                            
                                            	Remaining lease time in seconds
                                            	**type**\: int
                                            
                                            	**range:** 0..4294967295
                                            
                                            

                                            """

                                            _prefix = 'ipv6-new-dhcpv6d-oper'
                                            _revision = '2015-11-09'

                                            def __init__(self):
                                                self.parent = None
                                                self.prefix = None
                                                self.prefix_length = None
                                                self.lease_time = None
                                                self.remaining_lease_time = None

                                            @property
                                            def _common_path(self):
                                                if self.parent is None:
                                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                                return self.parent._common_path +'/Cisco-IOS-XR-ipv6-new-dhcpv6d-oper:bag-dhcpv6d-addr-attrb'

                                            def is_config(self):
                                                ''' Returns True if this instance represents config data else returns False '''
                                                return False

                                            def _has_data(self):
                                                if not self.is_config():
                                                    return False
                                                if self.prefix is not None:
                                                    return True

                                                if self.prefix_length is not None:
                                                    return True

                                                if self.lease_time is not None:
                                                    return True

                                                if self.remaining_lease_time is not None:
                                                    return True

                                                return False

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.ipv6._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_oper as meta
                                                return meta._meta_table['Dhcpv6.Nodes.Node.Proxy.Binding.Clients.Client.IaIdPd.BagDhcpv6DIaIdPdInfo.Addresses.BagDhcpv6DAddrAttrb']['meta_info']

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/Cisco-IOS-XR-ipv6-new-dhcpv6d-oper:addresses'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return False

                                        def _has_data(self):
                                            if not self.is_config():
                                                return False
                                            if self.bag_dhcpv6d_addr_attrb is not None:
                                                for child_ref in self.bag_dhcpv6d_addr_attrb:
                                                    if child_ref._has_data():
                                                        return True

                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.ipv6._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_oper as meta
                                            return meta._meta_table['Dhcpv6.Nodes.Node.Proxy.Binding.Clients.Client.IaIdPd.BagDhcpv6DIaIdPdInfo.Addresses']['meta_info']

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-ipv6-new-dhcpv6d-oper:bag-dhcpv6d-ia-id-pd-info'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        if not self.is_config():
                                            return False
                                        if self.addresses is not None and self.addresses._has_data():
                                            return True

                                        if self.ia_type is not None:
                                            return True

                                        if self.ia_id is not None:
                                            return True

                                        if self.flags is not None:
                                            return True

                                        if self.total_address is not None:
                                            return True

                                        if self.state is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.ipv6._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_oper as meta
                                        return meta._meta_table['Dhcpv6.Nodes.Node.Proxy.Binding.Clients.Client.IaIdPd.BagDhcpv6DIaIdPdInfo']['meta_info']

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ipv6-new-dhcpv6d-oper:ia-id-pd'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.bag_dhcpv6d_ia_id_pd_info is not None:
                                        for child_ref in self.bag_dhcpv6d_ia_id_pd_info:
                                            if child_ref._has_data():
                                                return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.ipv6._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_oper as meta
                                    return meta._meta_table['Dhcpv6.Nodes.Node.Proxy.Binding.Clients.Client.IaIdPd']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')
                                if self.client_id is None:
                                    raise YPYDataValidationError('Key property client_id is None')

                                return self.parent._common_path +'/Cisco-IOS-XR-ipv6-new-dhcpv6d-oper:client[Cisco-IOS-XR-ipv6-new-dhcpv6d-oper:client-id = ' + str(self.client_id) + ']'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.client_id is not None:
                                    return True

                                if self.ia_id_pd is not None and self.ia_id_pd._has_data():
                                    return True

                                if self.duid is not None:
                                    return True

                                if self.client_flag is not None:
                                    return True

                                if self.subscriber_label is not None:
                                    return True

                                if self.vrf_name is not None:
                                    return True

                                if self.mac_address is not None:
                                    return True

                                if self.ia_id_p_ds is not None:
                                    return True

                                if self.interface_name is not None:
                                    return True

                                if self.access_vrf_name is not None:
                                    return True

                                if self.proxy_binding_tags is not None:
                                    return True

                                if self.proxy_binding_outer_tag is not None:
                                    return True

                                if self.proxy_binding_inner_tag is not None:
                                    return True

                                if self.class_name is not None:
                                    return True

                                if self.pool_name is not None:
                                    return True

                                if self.rx_remote_id is not None:
                                    return True

                                if self.tx_remote_id is not None:
                                    return True

                                if self.rx_interface_id is not None:
                                    return True

                                if self.tx_interface_id is not None:
                                    return True

                                if self.server_ipv6_address is not None:
                                    return True

                                if self.profile_name is not None:
                                    return True

                                if self.framed_ipv6_prefix is not None:
                                    return True

                                if self.framed_prefix_length is not None:
                                    return True

                                if self.is_nak_next_renew is not None:
                                    return True

                                if self.srg_state is not None:
                                    return True

                                if self.srg_intf_role is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.ipv6._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_oper as meta
                                return meta._meta_table['Dhcpv6.Nodes.Node.Proxy.Binding.Clients.Client']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-ipv6-new-dhcpv6d-oper:clients'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.client is not None:
                                for child_ref in self.client:
                                    if child_ref._has_data():
                                        return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.ipv6._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_oper as meta
                            return meta._meta_table['Dhcpv6.Nodes.Node.Proxy.Binding.Clients']['meta_info']


                    class Summary(object):
                        """
                        DHCPV6 proxy binding summary
                        
                        .. attribute:: iana
                        
                        	IANA proxy binding summary
                        	**type**\: :py:class:`Iana <ydk.models.ipv6.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Proxy.Binding.Summary.Iana>`
                        
                        .. attribute:: iapd
                        
                        	IAPD proxy binding summary
                        	**type**\: :py:class:`Iapd <ydk.models.ipv6.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Proxy.Binding.Summary.Iapd>`
                        
                        .. attribute:: clients
                        
                        	Total number of clients
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'ipv6-new-dhcpv6d-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.iana = Dhcpv6.Nodes.Node.Proxy.Binding.Summary.Iana()
                            self.iana.parent = self
                            self.iapd = Dhcpv6.Nodes.Node.Proxy.Binding.Summary.Iapd()
                            self.iapd.parent = self
                            self.clients = None


                        class Iana(object):
                            """
                            IANA proxy binding summary
                            
                            .. attribute:: initializing_clients
                            
                            	Number of clients in init state
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: dpm_waiting_clients
                            
                            	Number of clients waiting on DPM to validate subscriber
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: daps_waiting_clients
                            
                            	Number of clients waiting on DAPS to assign/free prefix(ND)
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: msg_waiting_clients
                            
                            	Number of clients waiting for a message from the client/server
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: iedge_waiting_clients
                            
                            	Number of clients waiting on iedge to subscriber session
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: rib_waiting_clients
                            
                            	Number of clients in waiting on RIB response
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: bound_clients
                            
                            	Number of clients in bound state
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'ipv6-new-dhcpv6d-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.initializing_clients = None
                                self.dpm_waiting_clients = None
                                self.daps_waiting_clients = None
                                self.msg_waiting_clients = None
                                self.iedge_waiting_clients = None
                                self.rib_waiting_clients = None
                                self.bound_clients = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-ipv6-new-dhcpv6d-oper:iana'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.initializing_clients is not None:
                                    return True

                                if self.dpm_waiting_clients is not None:
                                    return True

                                if self.daps_waiting_clients is not None:
                                    return True

                                if self.msg_waiting_clients is not None:
                                    return True

                                if self.iedge_waiting_clients is not None:
                                    return True

                                if self.rib_waiting_clients is not None:
                                    return True

                                if self.bound_clients is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.ipv6._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_oper as meta
                                return meta._meta_table['Dhcpv6.Nodes.Node.Proxy.Binding.Summary.Iana']['meta_info']


                        class Iapd(object):
                            """
                            IAPD proxy binding summary
                            
                            .. attribute:: initializing_clients
                            
                            	Number of clients in init state
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: dpm_waiting_clients
                            
                            	Number of clients waiting on DPM to validate subscriber
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: daps_waiting_clients
                            
                            	Number of clients waiting on DAPS to assign/free prefix(ND)
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: msg_waiting_clients
                            
                            	Number of clients waiting for a message from the client/server
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: iedge_waiting_clients
                            
                            	Number of clients waiting on iedge to subscriber session
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: rib_waiting_clients
                            
                            	Number of clients in waiting on RIB response
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: bound_clients
                            
                            	Number of clients in bound state
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'ipv6-new-dhcpv6d-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.initializing_clients = None
                                self.dpm_waiting_clients = None
                                self.daps_waiting_clients = None
                                self.msg_waiting_clients = None
                                self.iedge_waiting_clients = None
                                self.rib_waiting_clients = None
                                self.bound_clients = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-ipv6-new-dhcpv6d-oper:iapd'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.initializing_clients is not None:
                                    return True

                                if self.dpm_waiting_clients is not None:
                                    return True

                                if self.daps_waiting_clients is not None:
                                    return True

                                if self.msg_waiting_clients is not None:
                                    return True

                                if self.iedge_waiting_clients is not None:
                                    return True

                                if self.rib_waiting_clients is not None:
                                    return True

                                if self.bound_clients is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.ipv6._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_oper as meta
                                return meta._meta_table['Dhcpv6.Nodes.Node.Proxy.Binding.Summary.Iapd']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-ipv6-new-dhcpv6d-oper:summary'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.iana is not None and self.iana._has_data():
                                return True

                            if self.iapd is not None and self.iapd._has_data():
                                return True

                            if self.clients is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.ipv6._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_oper as meta
                            return meta._meta_table['Dhcpv6.Nodes.Node.Proxy.Binding.Summary']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ipv6-new-dhcpv6d-oper:binding'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.clients is not None and self.clients._has_data():
                            return True

                        if self.summary is not None and self.summary._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.ipv6._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_oper as meta
                        return meta._meta_table['Dhcpv6.Nodes.Node.Proxy.Binding']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-ipv6-new-dhcpv6d-oper:proxy'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.vrfs is not None and self.vrfs._has_data():
                        return True

                    if self.profiles is not None and self.profiles._has_data():
                        return True

                    if self.statistics is not None and self.statistics._has_data():
                        return True

                    if self.binding is not None and self.binding._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.ipv6._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_oper as meta
                    return meta._meta_table['Dhcpv6.Nodes.Node.Proxy']['meta_info']


            class Server(object):
                """
                IPv6 DHCP server operational data
                
                .. attribute:: binding
                
                	DHCPV6 server bindings
                	**type**\: :py:class:`Binding <ydk.models.ipv6.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Server.Binding>`
                
                .. attribute:: vrfs
                
                	DHCPV6 server list of VRF names
                	**type**\: :py:class:`Vrfs <ydk.models.ipv6.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Server.Vrfs>`
                
                .. attribute:: profiles
                
                	IPv6 DHCP server profile
                	**type**\: :py:class:`Profiles <ydk.models.ipv6.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Server.Profiles>`
                
                .. attribute:: statistics
                
                	DHCPv6 server statistics
                	**type**\: :py:class:`Statistics <ydk.models.ipv6.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Server.Statistics>`
                
                

                """

                _prefix = 'ipv6-new-dhcpv6d-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.binding = Dhcpv6.Nodes.Node.Server.Binding()
                    self.binding.parent = self
                    self.vrfs = Dhcpv6.Nodes.Node.Server.Vrfs()
                    self.vrfs.parent = self
                    self.profiles = Dhcpv6.Nodes.Node.Server.Profiles()
                    self.profiles.parent = self
                    self.statistics = Dhcpv6.Nodes.Node.Server.Statistics()
                    self.statistics.parent = self


                class Binding(object):
                    """
                    DHCPV6 server bindings
                    
                    .. attribute:: summary
                    
                    	DHCPV6 server binding summary
                    	**type**\: :py:class:`Summary <ydk.models.ipv6.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Server.Binding.Summary>`
                    
                    .. attribute:: clients
                    
                    	DHCPV6 server client bindings
                    	**type**\: :py:class:`Clients <ydk.models.ipv6.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Server.Binding.Clients>`
                    
                    

                    """

                    _prefix = 'ipv6-new-dhcpv6d-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.summary = Dhcpv6.Nodes.Node.Server.Binding.Summary()
                        self.summary.parent = self
                        self.clients = Dhcpv6.Nodes.Node.Server.Binding.Clients()
                        self.clients.parent = self


                    class Summary(object):
                        """
                        DHCPV6 server binding summary
                        
                        .. attribute:: iana
                        
                        	IANA server binding summary
                        	**type**\: :py:class:`Iana <ydk.models.ipv6.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Server.Binding.Summary.Iana>`
                        
                        .. attribute:: iapd
                        
                        	IAPD server binding summary
                        	**type**\: :py:class:`Iapd <ydk.models.ipv6.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Server.Binding.Summary.Iapd>`
                        
                        .. attribute:: clients
                        
                        	Total number of clients
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'ipv6-new-dhcpv6d-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.iana = Dhcpv6.Nodes.Node.Server.Binding.Summary.Iana()
                            self.iana.parent = self
                            self.iapd = Dhcpv6.Nodes.Node.Server.Binding.Summary.Iapd()
                            self.iapd.parent = self
                            self.clients = None


                        class Iana(object):
                            """
                            IANA server binding summary
                            
                            .. attribute:: initializing_clients
                            
                            	Number of clients in init state
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: dpm_waiting_clients
                            
                            	Number of clients waiting on DPM to validate subscriber
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: daps_waiting_clients
                            
                            	Number of clients waiting on DAPS to assign/free addr/prefix
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: request_waiting_clients
                            
                            	Number of clients waiting for a request from the client
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: iedge_waiting_clients
                            
                            	Number of clients waiting for iedge for the session
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: rib_waiting_clients
                            
                            	Number of clients in waiting for RIB response
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: bound_clients
                            
                            	Number of clients in bound state
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'ipv6-new-dhcpv6d-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.initializing_clients = None
                                self.dpm_waiting_clients = None
                                self.daps_waiting_clients = None
                                self.request_waiting_clients = None
                                self.iedge_waiting_clients = None
                                self.rib_waiting_clients = None
                                self.bound_clients = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-ipv6-new-dhcpv6d-oper:iana'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.initializing_clients is not None:
                                    return True

                                if self.dpm_waiting_clients is not None:
                                    return True

                                if self.daps_waiting_clients is not None:
                                    return True

                                if self.request_waiting_clients is not None:
                                    return True

                                if self.iedge_waiting_clients is not None:
                                    return True

                                if self.rib_waiting_clients is not None:
                                    return True

                                if self.bound_clients is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.ipv6._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_oper as meta
                                return meta._meta_table['Dhcpv6.Nodes.Node.Server.Binding.Summary.Iana']['meta_info']


                        class Iapd(object):
                            """
                            IAPD server binding summary
                            
                            .. attribute:: initializing_clients
                            
                            	Number of clients in init state
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: dpm_waiting_clients
                            
                            	Number of clients waiting on DPM to validate subscriber
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: daps_waiting_clients
                            
                            	Number of clients waiting on DAPS to assign/free addr/prefix
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: request_waiting_clients
                            
                            	Number of clients waiting for a request from the client
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: iedge_waiting_clients
                            
                            	Number of clients waiting for iedge for the session
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: rib_waiting_clients
                            
                            	Number of clients in waiting for RIB response
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: bound_clients
                            
                            	Number of clients in bound state
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'ipv6-new-dhcpv6d-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.initializing_clients = None
                                self.dpm_waiting_clients = None
                                self.daps_waiting_clients = None
                                self.request_waiting_clients = None
                                self.iedge_waiting_clients = None
                                self.rib_waiting_clients = None
                                self.bound_clients = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-ipv6-new-dhcpv6d-oper:iapd'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.initializing_clients is not None:
                                    return True

                                if self.dpm_waiting_clients is not None:
                                    return True

                                if self.daps_waiting_clients is not None:
                                    return True

                                if self.request_waiting_clients is not None:
                                    return True

                                if self.iedge_waiting_clients is not None:
                                    return True

                                if self.rib_waiting_clients is not None:
                                    return True

                                if self.bound_clients is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.ipv6._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_oper as meta
                                return meta._meta_table['Dhcpv6.Nodes.Node.Server.Binding.Summary.Iapd']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-ipv6-new-dhcpv6d-oper:summary'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.iana is not None and self.iana._has_data():
                                return True

                            if self.iapd is not None and self.iapd._has_data():
                                return True

                            if self.clients is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.ipv6._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_oper as meta
                            return meta._meta_table['Dhcpv6.Nodes.Node.Server.Binding.Summary']['meta_info']


                    class Clients(object):
                        """
                        DHCPV6 server client bindings
                        
                        .. attribute:: client
                        
                        	Single DHCPV6 server binding
                        	**type**\: list of :py:class:`Client <ydk.models.ipv6.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Server.Binding.Clients.Client>`
                        
                        

                        """

                        _prefix = 'ipv6-new-dhcpv6d-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.client = YList()
                            self.client.parent = self
                            self.client.name = 'client'


                        class Client(object):
                            """
                            Single DHCPV6 server binding
                            
                            .. attribute:: client_id  <key>
                            
                            	Client ID
                            	**type**\: str
                            
                            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                            
                            .. attribute:: ia_id_pd
                            
                            	List of DHCPv6 IA\_ID/PDs
                            	**type**\: :py:class:`IaIdPd <ydk.models.ipv6.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Server.Binding.Clients.Client.IaIdPd>`
                            
                            .. attribute:: duid
                            
                            	Client DUID
                            	**type**\: str
                            
                            .. attribute:: client_id_xr
                            
                            	Client unique identifier
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: client_flag
                            
                            	DHCPV6 client flag
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: subscriber_label
                            
                            	DHCPV6 subscriber label
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: vrf_name
                            
                            	DHCPVV6 client/subscriber VRF name
                            	**type**\: str
                            
                            	**range:** 0..33
                            
                            .. attribute:: mac_address
                            
                            	Client MAC address
                            	**type**\: str
                            
                            .. attribute:: ia_id_p_ds
                            
                            	Number of ia\_id/pd
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: link_local_address
                            
                            	DHCPV6 IPv6 client link local address
                            	**type**\: str
                            
                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: interface_name
                            
                            	DHCPV6 access interface to client
                            	**type**\: str
                            
                            	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                            
                            .. attribute:: access_vrf_name
                            
                            	DHCPV6 access VRF name to client
                            	**type**\: str
                            
                            	**range:** 0..33
                            
                            .. attribute:: server_binding_tags
                            
                            	DHCPV6 VLAN tag count
                            	**type**\: int
                            
                            	**range:** 0..255
                            
                            .. attribute:: server_binding_outer_tag
                            
                            	DHCPV6 VLAN Outer VLAN
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: server_binding_inner_tag
                            
                            	DHCPV6 VLAN Inner VLAN
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: pool_name
                            
                            	DHCPV6 pool name
                            	**type**\: str
                            
                            	**range:** 0..64
                            
                            .. attribute:: profile_name
                            
                            	DHCPV6 profile name
                            	**type**\: str
                            
                            	**range:** 0..64
                            
                            .. attribute:: framed_ipv6_prefix
                            
                            	DHCPV6 framed ipv6 addess used by ND
                            	**type**\: str
                            
                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: framed_prefix_length
                            
                            	DHCPV6 framed ipv6 prefix length used by ND
                            	**type**\: int
                            
                            	**range:** 0..255
                            
                            .. attribute:: class_name
                            
                            	DHCPV6 class name
                            	**type**\: str
                            
                            	**range:** 0..64
                            
                            .. attribute:: rx_remote_id
                            
                            	DHCPV6 received Remote ID
                            	**type**\: str
                            
                            	**range:** 0..771
                            
                            .. attribute:: rx_interface_id
                            
                            	DHCPV6 received Interface ID
                            	**type**\: str
                            
                            	**range:** 0..771
                            
                            .. attribute:: prefix_pool_name
                            
                            	DHCPV6 server prefix pool name
                            	**type**\: str
                            
                            	**range:** 0..64
                            
                            .. attribute:: address_pool_name
                            
                            	DHCPV6 server address pool name
                            	**type**\: str
                            
                            	**range:** 0..64
                            
                            .. attribute:: dns_server_count
                            
                            	DNS server count
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: is_nak_next_renew
                            
                            	Is true if DHCPv6 next renew from client will be NAK'd
                            	**type**\: bool
                            
                            .. attribute:: srg_state
                            
                            	DHCPV6 SRG state
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: srg_intf_role
                            
                            	DHCPV6 SRG Intf Role
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'ipv6-new-dhcpv6d-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.client_id = None
                                self.ia_id_pd = Dhcpv6.Nodes.Node.Server.Binding.Clients.Client.IaIdPd()
                                self.ia_id_pd.parent = self
                                self.duid = None
                                self.client_id_xr = None
                                self.client_flag = None
                                self.subscriber_label = None
                                self.vrf_name = None
                                self.mac_address = None
                                self.ia_id_p_ds = None
                                self.link_local_address = None
                                self.interface_name = None
                                self.access_vrf_name = None
                                self.server_binding_tags = None
                                self.server_binding_outer_tag = None
                                self.server_binding_inner_tag = None
                                self.pool_name = None
                                self.profile_name = None
                                self.framed_ipv6_prefix = None
                                self.framed_prefix_length = None
                                self.class_name = None
                                self.rx_remote_id = None
                                self.rx_interface_id = None
                                self.prefix_pool_name = None
                                self.address_pool_name = None
                                self.dns_server_count = None
                                self.is_nak_next_renew = None
                                self.srg_state = None
                                self.srg_intf_role = None


                            class IaIdPd(object):
                                """
                                List of DHCPv6 IA\_ID/PDs
                                
                                .. attribute:: bag_dhcpv6d_ia_id_pd_info
                                
                                	bag dhcpv6d ia id pd info
                                	**type**\: list of :py:class:`BagDhcpv6DIaIdPdInfo <ydk.models.ipv6.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Server.Binding.Clients.Client.IaIdPd.BagDhcpv6DIaIdPdInfo>`
                                
                                

                                """

                                _prefix = 'ipv6-new-dhcpv6d-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.bag_dhcpv6d_ia_id_pd_info = YList()
                                    self.bag_dhcpv6d_ia_id_pd_info.parent = self
                                    self.bag_dhcpv6d_ia_id_pd_info.name = 'bag_dhcpv6d_ia_id_pd_info'


                                class BagDhcpv6DIaIdPdInfo(object):
                                    """
                                    bag dhcpv6d ia id pd info
                                    
                                    .. attribute:: addresses
                                    
                                    	List of addresses in this IA
                                    	**type**\: :py:class:`Addresses <ydk.models.ipv6.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Server.Binding.Clients.Client.IaIdPd.BagDhcpv6DIaIdPdInfo.Addresses>`
                                    
                                    .. attribute:: ia_type
                                    
                                    	IA type
                                    	**type**\: :py:class:`BagDhcpv6DIaIdEnum <ydk.models.ipv6.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.BagDhcpv6DIaIdEnum>`
                                    
                                    .. attribute:: ia_id
                                    
                                    	IA\_ID of this IA
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: flags
                                    
                                    	FSM Flag for this IA
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: total_address
                                    
                                    	Total address in this IA
                                    	**type**\: int
                                    
                                    	**range:** 0..65535
                                    
                                    .. attribute:: state
                                    
                                    	State
                                    	**type**\: :py:class:`BagDhcpv6DFsmStateEnum <ydk.models.ipv6.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.BagDhcpv6DFsmStateEnum>`
                                    
                                    

                                    """

                                    _prefix = 'ipv6-new-dhcpv6d-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.addresses = Dhcpv6.Nodes.Node.Server.Binding.Clients.Client.IaIdPd.BagDhcpv6DIaIdPdInfo.Addresses()
                                        self.addresses.parent = self
                                        self.ia_type = None
                                        self.ia_id = None
                                        self.flags = None
                                        self.total_address = None
                                        self.state = None


                                    class Addresses(object):
                                        """
                                        List of addresses in this IA
                                        
                                        .. attribute:: bag_dhcpv6d_addr_attrb
                                        
                                        	bag dhcpv6d addr attrb
                                        	**type**\: list of :py:class:`BagDhcpv6DAddrAttrb <ydk.models.ipv6.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Server.Binding.Clients.Client.IaIdPd.BagDhcpv6DIaIdPdInfo.Addresses.BagDhcpv6DAddrAttrb>`
                                        
                                        

                                        """

                                        _prefix = 'ipv6-new-dhcpv6d-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            self.parent = None
                                            self.bag_dhcpv6d_addr_attrb = YList()
                                            self.bag_dhcpv6d_addr_attrb.parent = self
                                            self.bag_dhcpv6d_addr_attrb.name = 'bag_dhcpv6d_addr_attrb'


                                        class BagDhcpv6DAddrAttrb(object):
                                            """
                                            bag dhcpv6d addr attrb
                                            
                                            .. attribute:: prefix
                                            
                                            	IPv6 prefix
                                            	**type**\: str
                                            
                                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                            
                                            .. attribute:: prefix_length
                                            
                                            	Prefix length
                                            	**type**\: int
                                            
                                            	**range:** 0..255
                                            
                                            .. attribute:: lease_time
                                            
                                            	Lease time in seconds
                                            	**type**\: int
                                            
                                            	**range:** 0..4294967295
                                            
                                            .. attribute:: remaining_lease_time
                                            
                                            	Remaining lease time in seconds
                                            	**type**\: int
                                            
                                            	**range:** 0..4294967295
                                            
                                            

                                            """

                                            _prefix = 'ipv6-new-dhcpv6d-oper'
                                            _revision = '2015-11-09'

                                            def __init__(self):
                                                self.parent = None
                                                self.prefix = None
                                                self.prefix_length = None
                                                self.lease_time = None
                                                self.remaining_lease_time = None

                                            @property
                                            def _common_path(self):
                                                if self.parent is None:
                                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                                return self.parent._common_path +'/Cisco-IOS-XR-ipv6-new-dhcpv6d-oper:bag-dhcpv6d-addr-attrb'

                                            def is_config(self):
                                                ''' Returns True if this instance represents config data else returns False '''
                                                return False

                                            def _has_data(self):
                                                if not self.is_config():
                                                    return False
                                                if self.prefix is not None:
                                                    return True

                                                if self.prefix_length is not None:
                                                    return True

                                                if self.lease_time is not None:
                                                    return True

                                                if self.remaining_lease_time is not None:
                                                    return True

                                                return False

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.ipv6._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_oper as meta
                                                return meta._meta_table['Dhcpv6.Nodes.Node.Server.Binding.Clients.Client.IaIdPd.BagDhcpv6DIaIdPdInfo.Addresses.BagDhcpv6DAddrAttrb']['meta_info']

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/Cisco-IOS-XR-ipv6-new-dhcpv6d-oper:addresses'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return False

                                        def _has_data(self):
                                            if not self.is_config():
                                                return False
                                            if self.bag_dhcpv6d_addr_attrb is not None:
                                                for child_ref in self.bag_dhcpv6d_addr_attrb:
                                                    if child_ref._has_data():
                                                        return True

                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.ipv6._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_oper as meta
                                            return meta._meta_table['Dhcpv6.Nodes.Node.Server.Binding.Clients.Client.IaIdPd.BagDhcpv6DIaIdPdInfo.Addresses']['meta_info']

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-ipv6-new-dhcpv6d-oper:bag-dhcpv6d-ia-id-pd-info'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        if not self.is_config():
                                            return False
                                        if self.addresses is not None and self.addresses._has_data():
                                            return True

                                        if self.ia_type is not None:
                                            return True

                                        if self.ia_id is not None:
                                            return True

                                        if self.flags is not None:
                                            return True

                                        if self.total_address is not None:
                                            return True

                                        if self.state is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.ipv6._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_oper as meta
                                        return meta._meta_table['Dhcpv6.Nodes.Node.Server.Binding.Clients.Client.IaIdPd.BagDhcpv6DIaIdPdInfo']['meta_info']

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ipv6-new-dhcpv6d-oper:ia-id-pd'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.bag_dhcpv6d_ia_id_pd_info is not None:
                                        for child_ref in self.bag_dhcpv6d_ia_id_pd_info:
                                            if child_ref._has_data():
                                                return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.ipv6._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_oper as meta
                                    return meta._meta_table['Dhcpv6.Nodes.Node.Server.Binding.Clients.Client.IaIdPd']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')
                                if self.client_id is None:
                                    raise YPYDataValidationError('Key property client_id is None')

                                return self.parent._common_path +'/Cisco-IOS-XR-ipv6-new-dhcpv6d-oper:client[Cisco-IOS-XR-ipv6-new-dhcpv6d-oper:client-id = ' + str(self.client_id) + ']'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.client_id is not None:
                                    return True

                                if self.ia_id_pd is not None and self.ia_id_pd._has_data():
                                    return True

                                if self.duid is not None:
                                    return True

                                if self.client_id_xr is not None:
                                    return True

                                if self.client_flag is not None:
                                    return True

                                if self.subscriber_label is not None:
                                    return True

                                if self.vrf_name is not None:
                                    return True

                                if self.mac_address is not None:
                                    return True

                                if self.ia_id_p_ds is not None:
                                    return True

                                if self.link_local_address is not None:
                                    return True

                                if self.interface_name is not None:
                                    return True

                                if self.access_vrf_name is not None:
                                    return True

                                if self.server_binding_tags is not None:
                                    return True

                                if self.server_binding_outer_tag is not None:
                                    return True

                                if self.server_binding_inner_tag is not None:
                                    return True

                                if self.pool_name is not None:
                                    return True

                                if self.profile_name is not None:
                                    return True

                                if self.framed_ipv6_prefix is not None:
                                    return True

                                if self.framed_prefix_length is not None:
                                    return True

                                if self.class_name is not None:
                                    return True

                                if self.rx_remote_id is not None:
                                    return True

                                if self.rx_interface_id is not None:
                                    return True

                                if self.prefix_pool_name is not None:
                                    return True

                                if self.address_pool_name is not None:
                                    return True

                                if self.dns_server_count is not None:
                                    return True

                                if self.is_nak_next_renew is not None:
                                    return True

                                if self.srg_state is not None:
                                    return True

                                if self.srg_intf_role is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.ipv6._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_oper as meta
                                return meta._meta_table['Dhcpv6.Nodes.Node.Server.Binding.Clients.Client']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-ipv6-new-dhcpv6d-oper:clients'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.client is not None:
                                for child_ref in self.client:
                                    if child_ref._has_data():
                                        return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.ipv6._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_oper as meta
                            return meta._meta_table['Dhcpv6.Nodes.Node.Server.Binding.Clients']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ipv6-new-dhcpv6d-oper:binding'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.summary is not None and self.summary._has_data():
                            return True

                        if self.clients is not None and self.clients._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.ipv6._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_oper as meta
                        return meta._meta_table['Dhcpv6.Nodes.Node.Server.Binding']['meta_info']


                class Vrfs(object):
                    """
                    DHCPV6 server list of VRF names
                    
                    .. attribute:: vrf
                    
                    	IPv6 DHCP server VRF name
                    	**type**\: list of :py:class:`Vrf <ydk.models.ipv6.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Server.Vrfs.Vrf>`
                    
                    

                    """

                    _prefix = 'ipv6-new-dhcpv6d-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.vrf = YList()
                        self.vrf.parent = self
                        self.vrf.name = 'vrf'


                    class Vrf(object):
                        """
                        IPv6 DHCP server VRF name
                        
                        .. attribute:: vrf_name  <key>
                        
                        	VRF name
                        	**type**\: str
                        
                        	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                        
                        .. attribute:: statistics
                        
                        	IPv6 DHCP server statistics
                        	**type**\: :py:class:`Statistics <ydk.models.ipv6.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Server.Vrfs.Vrf.Statistics>`
                        
                        

                        """

                        _prefix = 'ipv6-new-dhcpv6d-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.vrf_name = None
                            self.statistics = Dhcpv6.Nodes.Node.Server.Vrfs.Vrf.Statistics()
                            self.statistics.parent = self


                        class Statistics(object):
                            """
                            IPv6 DHCP server statistics
                            
                            .. attribute:: solicit
                            
                            	DHCPV6 solicit packets
                            	**type**\: :py:class:`Solicit <ydk.models.ipv6.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Server.Vrfs.Vrf.Statistics.Solicit>`
                            
                            .. attribute:: advertise
                            
                            	DHCPV6 advertise packets
                            	**type**\: :py:class:`Advertise <ydk.models.ipv6.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Server.Vrfs.Vrf.Statistics.Advertise>`
                            
                            .. attribute:: request
                            
                            	DHCPV6 request packets
                            	**type**\: :py:class:`Request <ydk.models.ipv6.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Server.Vrfs.Vrf.Statistics.Request>`
                            
                            .. attribute:: reply
                            
                            	DHCPV6 reply packets
                            	**type**\: :py:class:`Reply <ydk.models.ipv6.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Server.Vrfs.Vrf.Statistics.Reply>`
                            
                            .. attribute:: confirm
                            
                            	DHCPV6 confirm packets
                            	**type**\: :py:class:`Confirm <ydk.models.ipv6.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Server.Vrfs.Vrf.Statistics.Confirm>`
                            
                            .. attribute:: decline
                            
                            	DHCPV6 decline packets
                            	**type**\: :py:class:`Decline <ydk.models.ipv6.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Server.Vrfs.Vrf.Statistics.Decline>`
                            
                            .. attribute:: renew
                            
                            	DHCPV6 renew packets
                            	**type**\: :py:class:`Renew <ydk.models.ipv6.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Server.Vrfs.Vrf.Statistics.Renew>`
                            
                            .. attribute:: rebind
                            
                            	DHCPV6 rebind packets
                            	**type**\: :py:class:`Rebind <ydk.models.ipv6.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Server.Vrfs.Vrf.Statistics.Rebind>`
                            
                            .. attribute:: release
                            
                            	DHCPV6 release packets
                            	**type**\: :py:class:`Release <ydk.models.ipv6.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Server.Vrfs.Vrf.Statistics.Release>`
                            
                            .. attribute:: reconfig
                            
                            	DHCPV6 reconfig packets
                            	**type**\: :py:class:`Reconfig <ydk.models.ipv6.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Server.Vrfs.Vrf.Statistics.Reconfig>`
                            
                            .. attribute:: inform
                            
                            	DHCPV6 inform packets
                            	**type**\: :py:class:`Inform <ydk.models.ipv6.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Server.Vrfs.Vrf.Statistics.Inform>`
                            
                            .. attribute:: relay_forward
                            
                            	DHCPV6 relay forward packets
                            	**type**\: :py:class:`RelayForward <ydk.models.ipv6.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Server.Vrfs.Vrf.Statistics.RelayForward>`
                            
                            .. attribute:: relay_reply
                            
                            	DHCPV6 relay reply packets
                            	**type**\: :py:class:`RelayReply <ydk.models.ipv6.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Server.Vrfs.Vrf.Statistics.RelayReply>`
                            
                            .. attribute:: lease_query
                            
                            	DHCPV6 lease query packets
                            	**type**\: :py:class:`LeaseQuery <ydk.models.ipv6.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Server.Vrfs.Vrf.Statistics.LeaseQuery>`
                            
                            .. attribute:: lease_query_reply
                            
                            	DHCPV6 lease query reply packets
                            	**type**\: :py:class:`LeaseQueryReply <ydk.models.ipv6.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Server.Vrfs.Vrf.Statistics.LeaseQueryReply>`
                            
                            .. attribute:: lease_query_done
                            
                            	DHCPV6 lease query done packets
                            	**type**\: :py:class:`LeaseQueryDone <ydk.models.ipv6.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Server.Vrfs.Vrf.Statistics.LeaseQueryDone>`
                            
                            .. attribute:: lease_query_data
                            
                            	DHCPV6 lease query data packets
                            	**type**\: :py:class:`LeaseQueryData <ydk.models.ipv6.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Server.Vrfs.Vrf.Statistics.LeaseQueryData>`
                            
                            

                            """

                            _prefix = 'ipv6-new-dhcpv6d-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.solicit = Dhcpv6.Nodes.Node.Server.Vrfs.Vrf.Statistics.Solicit()
                                self.solicit.parent = self
                                self.advertise = Dhcpv6.Nodes.Node.Server.Vrfs.Vrf.Statistics.Advertise()
                                self.advertise.parent = self
                                self.request = Dhcpv6.Nodes.Node.Server.Vrfs.Vrf.Statistics.Request()
                                self.request.parent = self
                                self.reply = Dhcpv6.Nodes.Node.Server.Vrfs.Vrf.Statistics.Reply()
                                self.reply.parent = self
                                self.confirm = Dhcpv6.Nodes.Node.Server.Vrfs.Vrf.Statistics.Confirm()
                                self.confirm.parent = self
                                self.decline = Dhcpv6.Nodes.Node.Server.Vrfs.Vrf.Statistics.Decline()
                                self.decline.parent = self
                                self.renew = Dhcpv6.Nodes.Node.Server.Vrfs.Vrf.Statistics.Renew()
                                self.renew.parent = self
                                self.rebind = Dhcpv6.Nodes.Node.Server.Vrfs.Vrf.Statistics.Rebind()
                                self.rebind.parent = self
                                self.release = Dhcpv6.Nodes.Node.Server.Vrfs.Vrf.Statistics.Release()
                                self.release.parent = self
                                self.reconfig = Dhcpv6.Nodes.Node.Server.Vrfs.Vrf.Statistics.Reconfig()
                                self.reconfig.parent = self
                                self.inform = Dhcpv6.Nodes.Node.Server.Vrfs.Vrf.Statistics.Inform()
                                self.inform.parent = self
                                self.relay_forward = Dhcpv6.Nodes.Node.Server.Vrfs.Vrf.Statistics.RelayForward()
                                self.relay_forward.parent = self
                                self.relay_reply = Dhcpv6.Nodes.Node.Server.Vrfs.Vrf.Statistics.RelayReply()
                                self.relay_reply.parent = self
                                self.lease_query = Dhcpv6.Nodes.Node.Server.Vrfs.Vrf.Statistics.LeaseQuery()
                                self.lease_query.parent = self
                                self.lease_query_reply = Dhcpv6.Nodes.Node.Server.Vrfs.Vrf.Statistics.LeaseQueryReply()
                                self.lease_query_reply.parent = self
                                self.lease_query_done = Dhcpv6.Nodes.Node.Server.Vrfs.Vrf.Statistics.LeaseQueryDone()
                                self.lease_query_done.parent = self
                                self.lease_query_data = Dhcpv6.Nodes.Node.Server.Vrfs.Vrf.Statistics.LeaseQueryData()
                                self.lease_query_data.parent = self


                            class Solicit(object):
                                """
                                DHCPV6 solicit packets
                                
                                .. attribute:: received_packets
                                
                                	Received packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: transmitted_packets
                                
                                	Transmitted packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: dropped_packets
                                
                                	Dropped packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                

                                """

                                _prefix = 'ipv6-new-dhcpv6d-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.received_packets = None
                                    self.transmitted_packets = None
                                    self.dropped_packets = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ipv6-new-dhcpv6d-oper:solicit'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.received_packets is not None:
                                        return True

                                    if self.transmitted_packets is not None:
                                        return True

                                    if self.dropped_packets is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.ipv6._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_oper as meta
                                    return meta._meta_table['Dhcpv6.Nodes.Node.Server.Vrfs.Vrf.Statistics.Solicit']['meta_info']


                            class Advertise(object):
                                """
                                DHCPV6 advertise packets
                                
                                .. attribute:: received_packets
                                
                                	Received packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: transmitted_packets
                                
                                	Transmitted packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: dropped_packets
                                
                                	Dropped packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                

                                """

                                _prefix = 'ipv6-new-dhcpv6d-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.received_packets = None
                                    self.transmitted_packets = None
                                    self.dropped_packets = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ipv6-new-dhcpv6d-oper:advertise'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.received_packets is not None:
                                        return True

                                    if self.transmitted_packets is not None:
                                        return True

                                    if self.dropped_packets is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.ipv6._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_oper as meta
                                    return meta._meta_table['Dhcpv6.Nodes.Node.Server.Vrfs.Vrf.Statistics.Advertise']['meta_info']


                            class Request(object):
                                """
                                DHCPV6 request packets
                                
                                .. attribute:: received_packets
                                
                                	Received packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: transmitted_packets
                                
                                	Transmitted packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: dropped_packets
                                
                                	Dropped packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                

                                """

                                _prefix = 'ipv6-new-dhcpv6d-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.received_packets = None
                                    self.transmitted_packets = None
                                    self.dropped_packets = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ipv6-new-dhcpv6d-oper:request'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.received_packets is not None:
                                        return True

                                    if self.transmitted_packets is not None:
                                        return True

                                    if self.dropped_packets is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.ipv6._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_oper as meta
                                    return meta._meta_table['Dhcpv6.Nodes.Node.Server.Vrfs.Vrf.Statistics.Request']['meta_info']


                            class Reply(object):
                                """
                                DHCPV6 reply packets
                                
                                .. attribute:: received_packets
                                
                                	Received packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: transmitted_packets
                                
                                	Transmitted packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: dropped_packets
                                
                                	Dropped packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                

                                """

                                _prefix = 'ipv6-new-dhcpv6d-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.received_packets = None
                                    self.transmitted_packets = None
                                    self.dropped_packets = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ipv6-new-dhcpv6d-oper:reply'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.received_packets is not None:
                                        return True

                                    if self.transmitted_packets is not None:
                                        return True

                                    if self.dropped_packets is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.ipv6._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_oper as meta
                                    return meta._meta_table['Dhcpv6.Nodes.Node.Server.Vrfs.Vrf.Statistics.Reply']['meta_info']


                            class Confirm(object):
                                """
                                DHCPV6 confirm packets
                                
                                .. attribute:: received_packets
                                
                                	Received packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: transmitted_packets
                                
                                	Transmitted packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: dropped_packets
                                
                                	Dropped packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                

                                """

                                _prefix = 'ipv6-new-dhcpv6d-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.received_packets = None
                                    self.transmitted_packets = None
                                    self.dropped_packets = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ipv6-new-dhcpv6d-oper:confirm'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.received_packets is not None:
                                        return True

                                    if self.transmitted_packets is not None:
                                        return True

                                    if self.dropped_packets is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.ipv6._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_oper as meta
                                    return meta._meta_table['Dhcpv6.Nodes.Node.Server.Vrfs.Vrf.Statistics.Confirm']['meta_info']


                            class Decline(object):
                                """
                                DHCPV6 decline packets
                                
                                .. attribute:: received_packets
                                
                                	Received packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: transmitted_packets
                                
                                	Transmitted packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: dropped_packets
                                
                                	Dropped packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                

                                """

                                _prefix = 'ipv6-new-dhcpv6d-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.received_packets = None
                                    self.transmitted_packets = None
                                    self.dropped_packets = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ipv6-new-dhcpv6d-oper:decline'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.received_packets is not None:
                                        return True

                                    if self.transmitted_packets is not None:
                                        return True

                                    if self.dropped_packets is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.ipv6._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_oper as meta
                                    return meta._meta_table['Dhcpv6.Nodes.Node.Server.Vrfs.Vrf.Statistics.Decline']['meta_info']


                            class Renew(object):
                                """
                                DHCPV6 renew packets
                                
                                .. attribute:: received_packets
                                
                                	Received packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: transmitted_packets
                                
                                	Transmitted packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: dropped_packets
                                
                                	Dropped packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                

                                """

                                _prefix = 'ipv6-new-dhcpv6d-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.received_packets = None
                                    self.transmitted_packets = None
                                    self.dropped_packets = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ipv6-new-dhcpv6d-oper:renew'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.received_packets is not None:
                                        return True

                                    if self.transmitted_packets is not None:
                                        return True

                                    if self.dropped_packets is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.ipv6._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_oper as meta
                                    return meta._meta_table['Dhcpv6.Nodes.Node.Server.Vrfs.Vrf.Statistics.Renew']['meta_info']


                            class Rebind(object):
                                """
                                DHCPV6 rebind packets
                                
                                .. attribute:: received_packets
                                
                                	Received packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: transmitted_packets
                                
                                	Transmitted packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: dropped_packets
                                
                                	Dropped packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                

                                """

                                _prefix = 'ipv6-new-dhcpv6d-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.received_packets = None
                                    self.transmitted_packets = None
                                    self.dropped_packets = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ipv6-new-dhcpv6d-oper:rebind'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.received_packets is not None:
                                        return True

                                    if self.transmitted_packets is not None:
                                        return True

                                    if self.dropped_packets is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.ipv6._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_oper as meta
                                    return meta._meta_table['Dhcpv6.Nodes.Node.Server.Vrfs.Vrf.Statistics.Rebind']['meta_info']


                            class Release(object):
                                """
                                DHCPV6 release packets
                                
                                .. attribute:: received_packets
                                
                                	Received packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: transmitted_packets
                                
                                	Transmitted packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: dropped_packets
                                
                                	Dropped packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                

                                """

                                _prefix = 'ipv6-new-dhcpv6d-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.received_packets = None
                                    self.transmitted_packets = None
                                    self.dropped_packets = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ipv6-new-dhcpv6d-oper:release'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.received_packets is not None:
                                        return True

                                    if self.transmitted_packets is not None:
                                        return True

                                    if self.dropped_packets is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.ipv6._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_oper as meta
                                    return meta._meta_table['Dhcpv6.Nodes.Node.Server.Vrfs.Vrf.Statistics.Release']['meta_info']


                            class Reconfig(object):
                                """
                                DHCPV6 reconfig packets
                                
                                .. attribute:: received_packets
                                
                                	Received packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: transmitted_packets
                                
                                	Transmitted packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: dropped_packets
                                
                                	Dropped packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                

                                """

                                _prefix = 'ipv6-new-dhcpv6d-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.received_packets = None
                                    self.transmitted_packets = None
                                    self.dropped_packets = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ipv6-new-dhcpv6d-oper:reconfig'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.received_packets is not None:
                                        return True

                                    if self.transmitted_packets is not None:
                                        return True

                                    if self.dropped_packets is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.ipv6._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_oper as meta
                                    return meta._meta_table['Dhcpv6.Nodes.Node.Server.Vrfs.Vrf.Statistics.Reconfig']['meta_info']


                            class Inform(object):
                                """
                                DHCPV6 inform packets
                                
                                .. attribute:: received_packets
                                
                                	Received packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: transmitted_packets
                                
                                	Transmitted packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: dropped_packets
                                
                                	Dropped packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                

                                """

                                _prefix = 'ipv6-new-dhcpv6d-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.received_packets = None
                                    self.transmitted_packets = None
                                    self.dropped_packets = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ipv6-new-dhcpv6d-oper:inform'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.received_packets is not None:
                                        return True

                                    if self.transmitted_packets is not None:
                                        return True

                                    if self.dropped_packets is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.ipv6._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_oper as meta
                                    return meta._meta_table['Dhcpv6.Nodes.Node.Server.Vrfs.Vrf.Statistics.Inform']['meta_info']


                            class RelayForward(object):
                                """
                                DHCPV6 relay forward packets
                                
                                .. attribute:: received_packets
                                
                                	Received packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: transmitted_packets
                                
                                	Transmitted packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: dropped_packets
                                
                                	Dropped packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                

                                """

                                _prefix = 'ipv6-new-dhcpv6d-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.received_packets = None
                                    self.transmitted_packets = None
                                    self.dropped_packets = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ipv6-new-dhcpv6d-oper:relay-forward'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.received_packets is not None:
                                        return True

                                    if self.transmitted_packets is not None:
                                        return True

                                    if self.dropped_packets is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.ipv6._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_oper as meta
                                    return meta._meta_table['Dhcpv6.Nodes.Node.Server.Vrfs.Vrf.Statistics.RelayForward']['meta_info']


                            class RelayReply(object):
                                """
                                DHCPV6 relay reply packets
                                
                                .. attribute:: received_packets
                                
                                	Received packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: transmitted_packets
                                
                                	Transmitted packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: dropped_packets
                                
                                	Dropped packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                

                                """

                                _prefix = 'ipv6-new-dhcpv6d-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.received_packets = None
                                    self.transmitted_packets = None
                                    self.dropped_packets = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ipv6-new-dhcpv6d-oper:relay-reply'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.received_packets is not None:
                                        return True

                                    if self.transmitted_packets is not None:
                                        return True

                                    if self.dropped_packets is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.ipv6._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_oper as meta
                                    return meta._meta_table['Dhcpv6.Nodes.Node.Server.Vrfs.Vrf.Statistics.RelayReply']['meta_info']


                            class LeaseQuery(object):
                                """
                                DHCPV6 lease query packets
                                
                                .. attribute:: received_packets
                                
                                	Received packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: transmitted_packets
                                
                                	Transmitted packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: dropped_packets
                                
                                	Dropped packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                

                                """

                                _prefix = 'ipv6-new-dhcpv6d-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.received_packets = None
                                    self.transmitted_packets = None
                                    self.dropped_packets = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ipv6-new-dhcpv6d-oper:lease-query'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.received_packets is not None:
                                        return True

                                    if self.transmitted_packets is not None:
                                        return True

                                    if self.dropped_packets is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.ipv6._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_oper as meta
                                    return meta._meta_table['Dhcpv6.Nodes.Node.Server.Vrfs.Vrf.Statistics.LeaseQuery']['meta_info']


                            class LeaseQueryReply(object):
                                """
                                DHCPV6 lease query reply packets
                                
                                .. attribute:: received_packets
                                
                                	Received packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: transmitted_packets
                                
                                	Transmitted packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: dropped_packets
                                
                                	Dropped packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                

                                """

                                _prefix = 'ipv6-new-dhcpv6d-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.received_packets = None
                                    self.transmitted_packets = None
                                    self.dropped_packets = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ipv6-new-dhcpv6d-oper:lease-query-reply'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.received_packets is not None:
                                        return True

                                    if self.transmitted_packets is not None:
                                        return True

                                    if self.dropped_packets is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.ipv6._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_oper as meta
                                    return meta._meta_table['Dhcpv6.Nodes.Node.Server.Vrfs.Vrf.Statistics.LeaseQueryReply']['meta_info']


                            class LeaseQueryDone(object):
                                """
                                DHCPV6 lease query done packets
                                
                                .. attribute:: received_packets
                                
                                	Received packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: transmitted_packets
                                
                                	Transmitted packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: dropped_packets
                                
                                	Dropped packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                

                                """

                                _prefix = 'ipv6-new-dhcpv6d-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.received_packets = None
                                    self.transmitted_packets = None
                                    self.dropped_packets = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ipv6-new-dhcpv6d-oper:lease-query-done'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.received_packets is not None:
                                        return True

                                    if self.transmitted_packets is not None:
                                        return True

                                    if self.dropped_packets is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.ipv6._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_oper as meta
                                    return meta._meta_table['Dhcpv6.Nodes.Node.Server.Vrfs.Vrf.Statistics.LeaseQueryDone']['meta_info']


                            class LeaseQueryData(object):
                                """
                                DHCPV6 lease query data packets
                                
                                .. attribute:: received_packets
                                
                                	Received packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: transmitted_packets
                                
                                	Transmitted packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: dropped_packets
                                
                                	Dropped packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                

                                """

                                _prefix = 'ipv6-new-dhcpv6d-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.received_packets = None
                                    self.transmitted_packets = None
                                    self.dropped_packets = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ipv6-new-dhcpv6d-oper:lease-query-data'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.received_packets is not None:
                                        return True

                                    if self.transmitted_packets is not None:
                                        return True

                                    if self.dropped_packets is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.ipv6._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_oper as meta
                                    return meta._meta_table['Dhcpv6.Nodes.Node.Server.Vrfs.Vrf.Statistics.LeaseQueryData']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-ipv6-new-dhcpv6d-oper:statistics'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.solicit is not None and self.solicit._has_data():
                                    return True

                                if self.advertise is not None and self.advertise._has_data():
                                    return True

                                if self.request is not None and self.request._has_data():
                                    return True

                                if self.reply is not None and self.reply._has_data():
                                    return True

                                if self.confirm is not None and self.confirm._has_data():
                                    return True

                                if self.decline is not None and self.decline._has_data():
                                    return True

                                if self.renew is not None and self.renew._has_data():
                                    return True

                                if self.rebind is not None and self.rebind._has_data():
                                    return True

                                if self.release is not None and self.release._has_data():
                                    return True

                                if self.reconfig is not None and self.reconfig._has_data():
                                    return True

                                if self.inform is not None and self.inform._has_data():
                                    return True

                                if self.relay_forward is not None and self.relay_forward._has_data():
                                    return True

                                if self.relay_reply is not None and self.relay_reply._has_data():
                                    return True

                                if self.lease_query is not None and self.lease_query._has_data():
                                    return True

                                if self.lease_query_reply is not None and self.lease_query_reply._has_data():
                                    return True

                                if self.lease_query_done is not None and self.lease_query_done._has_data():
                                    return True

                                if self.lease_query_data is not None and self.lease_query_data._has_data():
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.ipv6._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_oper as meta
                                return meta._meta_table['Dhcpv6.Nodes.Node.Server.Vrfs.Vrf.Statistics']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')
                            if self.vrf_name is None:
                                raise YPYDataValidationError('Key property vrf_name is None')

                            return self.parent._common_path +'/Cisco-IOS-XR-ipv6-new-dhcpv6d-oper:vrf[Cisco-IOS-XR-ipv6-new-dhcpv6d-oper:vrf-name = ' + str(self.vrf_name) + ']'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.vrf_name is not None:
                                return True

                            if self.statistics is not None and self.statistics._has_data():
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.ipv6._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_oper as meta
                            return meta._meta_table['Dhcpv6.Nodes.Node.Server.Vrfs.Vrf']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ipv6-new-dhcpv6d-oper:vrfs'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.vrf is not None:
                            for child_ref in self.vrf:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.ipv6._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_oper as meta
                        return meta._meta_table['Dhcpv6.Nodes.Node.Server.Vrfs']['meta_info']


                class Profiles(object):
                    """
                    IPv6 DHCP server profile
                    
                    .. attribute:: profile
                    
                    	IPv6 DHCP server profile
                    	**type**\: list of :py:class:`Profile <ydk.models.ipv6.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Server.Profiles.Profile>`
                    
                    

                    """

                    _prefix = 'ipv6-new-dhcpv6d-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.profile = YList()
                        self.profile.parent = self
                        self.profile.name = 'profile'


                    class Profile(object):
                        """
                        IPv6 DHCP server profile
                        
                        .. attribute:: profile_name  <key>
                        
                        	Profile name
                        	**type**\: str
                        
                        	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                        
                        .. attribute:: info
                        
                        	IPv6 DHCP server profile Info
                        	**type**\: :py:class:`Info <ydk.models.ipv6.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Server.Profiles.Profile.Info>`
                        
                        .. attribute:: throttle_infos
                        
                        	DHCPV6 throttle table
                        	**type**\: :py:class:`ThrottleInfos <ydk.models.ipv6.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Server.Profiles.Profile.ThrottleInfos>`
                        
                        

                        """

                        _prefix = 'ipv6-new-dhcpv6d-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.profile_name = None
                            self.info = Dhcpv6.Nodes.Node.Server.Profiles.Profile.Info()
                            self.info.parent = self
                            self.throttle_infos = Dhcpv6.Nodes.Node.Server.Profiles.Profile.ThrottleInfos()
                            self.throttle_infos.parent = self


                        class Info(object):
                            """
                            IPv6 DHCP server profile Info
                            
                            .. attribute:: lease
                            
                            	Server lease time
                            	**type**\: :py:class:`Lease <ydk.models.ipv6.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Server.Profiles.Profile.Info.Lease>`
                            
                            .. attribute:: interface_references
                            
                            	Interface references
                            	**type**\: :py:class:`InterfaceReferences <ydk.models.ipv6.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Server.Profiles.Profile.Info.InterfaceReferences>`
                            
                            .. attribute:: profile_name
                            
                            	Server profile name
                            	**type**\: str
                            
                            	**range:** 0..65
                            
                            .. attribute:: domain_name
                            
                            	Server domain name
                            	**type**\: str
                            
                            	**range:** 0..65
                            
                            .. attribute:: profile_dns
                            
                            	DNS address count
                            	**type**\: int
                            
                            	**range:** 0..255
                            
                            .. attribute:: aftr_name
                            
                            	Server aftr name
                            	**type**\: str
                            
                            	**range:** 0..65
                            
                            .. attribute:: framed_addr_pool_name
                            
                            	Server framed address pool name
                            	**type**\: str
                            
                            	**range:** 0..65
                            
                            .. attribute:: delegated_prefix_pool_name
                            
                            	Server delegated prefix pool name
                            	**type**\: str
                            
                            	**range:** 0..65
                            
                            .. attribute:: rapid_commit
                            
                            	Rapid Commit
                            	**type**\: bool
                            
                            .. attribute:: profile_dns_address
                            
                            	DNS addresses
                            	**type**\: list of str
                            
                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            

                            """

                            _prefix = 'ipv6-new-dhcpv6d-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.lease = Dhcpv6.Nodes.Node.Server.Profiles.Profile.Info.Lease()
                                self.lease.parent = self
                                self.interface_references = Dhcpv6.Nodes.Node.Server.Profiles.Profile.Info.InterfaceReferences()
                                self.interface_references.parent = self
                                self.profile_name = None
                                self.domain_name = None
                                self.profile_dns = None
                                self.aftr_name = None
                                self.framed_addr_pool_name = None
                                self.delegated_prefix_pool_name = None
                                self.rapid_commit = None
                                self.profile_dns_address = YLeafList()
                                self.profile_dns_address.parent = self
                                self.profile_dns_address.name = 'profile_dns_address'


                            class Lease(object):
                                """
                                Server lease time
                                
                                .. attribute:: seconds
                                
                                	DHCPV6 client lease in seconds
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: time
                                
                                	Time in format HH\:MM\:SS
                                	**type**\: str
                                
                                	**range:** 0..10
                                
                                

                                """

                                _prefix = 'ipv6-new-dhcpv6d-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.seconds = None
                                    self.time = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ipv6-new-dhcpv6d-oper:lease'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.seconds is not None:
                                        return True

                                    if self.time is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.ipv6._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_oper as meta
                                    return meta._meta_table['Dhcpv6.Nodes.Node.Server.Profiles.Profile.Info.Lease']['meta_info']


                            class InterfaceReferences(object):
                                """
                                Interface references
                                
                                .. attribute:: ipv6_dhcpv6d_server_interface_reference
                                
                                	ipv6 dhcpv6d server interface reference
                                	**type**\: list of :py:class:`Ipv6Dhcpv6DServerInterfaceReference <ydk.models.ipv6.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Server.Profiles.Profile.Info.InterfaceReferences.Ipv6Dhcpv6DServerInterfaceReference>`
                                
                                

                                """

                                _prefix = 'ipv6-new-dhcpv6d-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.ipv6_dhcpv6d_server_interface_reference = YList()
                                    self.ipv6_dhcpv6d_server_interface_reference.parent = self
                                    self.ipv6_dhcpv6d_server_interface_reference.name = 'ipv6_dhcpv6d_server_interface_reference'


                                class Ipv6Dhcpv6DServerInterfaceReference(object):
                                    """
                                    ipv6 dhcpv6d server interface reference
                                    
                                    .. attribute:: server_reference_interface_name
                                    
                                    	Interface name
                                    	**type**\: str
                                    
                                    	**range:** 0..65
                                    
                                    

                                    """

                                    _prefix = 'ipv6-new-dhcpv6d-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.server_reference_interface_name = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-ipv6-new-dhcpv6d-oper:ipv6-dhcpv6d-server-interface-reference'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        if not self.is_config():
                                            return False
                                        if self.server_reference_interface_name is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.ipv6._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_oper as meta
                                        return meta._meta_table['Dhcpv6.Nodes.Node.Server.Profiles.Profile.Info.InterfaceReferences.Ipv6Dhcpv6DServerInterfaceReference']['meta_info']

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ipv6-new-dhcpv6d-oper:interface-references'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.ipv6_dhcpv6d_server_interface_reference is not None:
                                        for child_ref in self.ipv6_dhcpv6d_server_interface_reference:
                                            if child_ref._has_data():
                                                return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.ipv6._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_oper as meta
                                    return meta._meta_table['Dhcpv6.Nodes.Node.Server.Profiles.Profile.Info.InterfaceReferences']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-ipv6-new-dhcpv6d-oper:info'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.lease is not None and self.lease._has_data():
                                    return True

                                if self.interface_references is not None and self.interface_references._has_data():
                                    return True

                                if self.profile_name is not None:
                                    return True

                                if self.domain_name is not None:
                                    return True

                                if self.profile_dns is not None:
                                    return True

                                if self.aftr_name is not None:
                                    return True

                                if self.framed_addr_pool_name is not None:
                                    return True

                                if self.delegated_prefix_pool_name is not None:
                                    return True

                                if self.rapid_commit is not None:
                                    return True

                                if self.profile_dns_address is not None:
                                    for child in self.profile_dns_address:
                                        if child is not None:
                                            return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.ipv6._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_oper as meta
                                return meta._meta_table['Dhcpv6.Nodes.Node.Server.Profiles.Profile.Info']['meta_info']


                        class ThrottleInfos(object):
                            """
                            DHCPV6 throttle table
                            
                            .. attribute:: throttle_info
                            
                            	IPv6 DHCP server profile Throttle Info
                            	**type**\: list of :py:class:`ThrottleInfo <ydk.models.ipv6.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Server.Profiles.Profile.ThrottleInfos.ThrottleInfo>`
                            
                            

                            """

                            _prefix = 'ipv6-new-dhcpv6d-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.throttle_info = YList()
                                self.throttle_info.parent = self
                                self.throttle_info.name = 'throttle_info'


                            class ThrottleInfo(object):
                                """
                                IPv6 DHCP server profile Throttle Info
                                
                                .. attribute:: mac_address  <key>
                                
                                	MAC address
                                	**type**\: str
                                
                                	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                                
                                .. attribute:: binding_chaddr
                                
                                	Client MAC address
                                	**type**\: str
                                
                                	**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
                                
                                .. attribute:: ifname
                                
                                	DHCP access interface
                                	**type**\: str
                                
                                	**range:** 0..65
                                
                                .. attribute:: state
                                
                                	State of entry
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: time_left
                                
                                	Time Left in secs
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'ipv6-new-dhcpv6d-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.mac_address = None
                                    self.binding_chaddr = None
                                    self.ifname = None
                                    self.state = None
                                    self.time_left = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYDataValidationError('parent is not set . Cannot derive path.')
                                    if self.mac_address is None:
                                        raise YPYDataValidationError('Key property mac_address is None')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ipv6-new-dhcpv6d-oper:throttle-info[Cisco-IOS-XR-ipv6-new-dhcpv6d-oper:mac-address = ' + str(self.mac_address) + ']'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.mac_address is not None:
                                        return True

                                    if self.binding_chaddr is not None:
                                        return True

                                    if self.ifname is not None:
                                        return True

                                    if self.state is not None:
                                        return True

                                    if self.time_left is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.ipv6._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_oper as meta
                                    return meta._meta_table['Dhcpv6.Nodes.Node.Server.Profiles.Profile.ThrottleInfos.ThrottleInfo']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-ipv6-new-dhcpv6d-oper:throttle-infos'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.throttle_info is not None:
                                    for child_ref in self.throttle_info:
                                        if child_ref._has_data():
                                            return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.ipv6._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_oper as meta
                                return meta._meta_table['Dhcpv6.Nodes.Node.Server.Profiles.Profile.ThrottleInfos']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')
                            if self.profile_name is None:
                                raise YPYDataValidationError('Key property profile_name is None')

                            return self.parent._common_path +'/Cisco-IOS-XR-ipv6-new-dhcpv6d-oper:profile[Cisco-IOS-XR-ipv6-new-dhcpv6d-oper:profile-name = ' + str(self.profile_name) + ']'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.profile_name is not None:
                                return True

                            if self.info is not None and self.info._has_data():
                                return True

                            if self.throttle_infos is not None and self.throttle_infos._has_data():
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.ipv6._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_oper as meta
                            return meta._meta_table['Dhcpv6.Nodes.Node.Server.Profiles.Profile']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ipv6-new-dhcpv6d-oper:profiles'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.profile is not None:
                            for child_ref in self.profile:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.ipv6._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_oper as meta
                        return meta._meta_table['Dhcpv6.Nodes.Node.Server.Profiles']['meta_info']


                class Statistics(object):
                    """
                    DHCPv6 server statistics
                    
                    .. attribute:: ipv6_dhcpv6d_server_stat
                    
                    	ipv6 dhcpv6d server stat
                    	**type**\: list of :py:class:`Ipv6Dhcpv6DServerStat <ydk.models.ipv6.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Server.Statistics.Ipv6Dhcpv6DServerStat>`
                    
                    

                    """

                    _prefix = 'ipv6-new-dhcpv6d-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.ipv6_dhcpv6d_server_stat = YList()
                        self.ipv6_dhcpv6d_server_stat.parent = self
                        self.ipv6_dhcpv6d_server_stat.name = 'ipv6_dhcpv6d_server_stat'


                    class Ipv6Dhcpv6DServerStat(object):
                        """
                        ipv6 dhcpv6d server stat
                        
                        .. attribute:: statistics
                        
                        	Server statistics
                        	**type**\: :py:class:`Statistics <ydk.models.ipv6.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Server.Statistics.Ipv6Dhcpv6DServerStat.Statistics>`
                        
                        .. attribute:: vrf_name
                        
                        	DHCPv6 L3 VRF name
                        	**type**\: str
                        
                        	**range:** 0..33
                        
                        

                        """

                        _prefix = 'ipv6-new-dhcpv6d-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.statistics = Dhcpv6.Nodes.Node.Server.Statistics.Ipv6Dhcpv6DServerStat.Statistics()
                            self.statistics.parent = self
                            self.vrf_name = None


                        class Statistics(object):
                            """
                            Server statistics
                            
                            .. attribute:: received_packets
                            
                            	Received packets
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: transmitted_packets
                            
                            	Transmitted packets
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: dropped_packets
                            
                            	Dropped packets
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            

                            """

                            _prefix = 'ipv6-new-dhcpv6d-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.received_packets = None
                                self.transmitted_packets = None
                                self.dropped_packets = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-ipv6-new-dhcpv6d-oper:statistics'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.received_packets is not None:
                                    return True

                                if self.transmitted_packets is not None:
                                    return True

                                if self.dropped_packets is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.ipv6._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_oper as meta
                                return meta._meta_table['Dhcpv6.Nodes.Node.Server.Statistics.Ipv6Dhcpv6DServerStat.Statistics']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-ipv6-new-dhcpv6d-oper:ipv6-dhcpv6d-server-stat'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.statistics is not None and self.statistics._has_data():
                                return True

                            if self.vrf_name is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.ipv6._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_oper as meta
                            return meta._meta_table['Dhcpv6.Nodes.Node.Server.Statistics.Ipv6Dhcpv6DServerStat']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ipv6-new-dhcpv6d-oper:statistics'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.ipv6_dhcpv6d_server_stat is not None:
                            for child_ref in self.ipv6_dhcpv6d_server_stat:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.ipv6._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_oper as meta
                        return meta._meta_table['Dhcpv6.Nodes.Node.Server.Statistics']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-ipv6-new-dhcpv6d-oper:server'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.binding is not None and self.binding._has_data():
                        return True

                    if self.vrfs is not None and self.vrfs._has_data():
                        return True

                    if self.profiles is not None and self.profiles._has_data():
                        return True

                    if self.statistics is not None and self.statistics._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.ipv6._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_oper as meta
                    return meta._meta_table['Dhcpv6.Nodes.Node.Server']['meta_info']


            class Relay(object):
                """
                IPv6 DHCP relay operational data
                
                .. attribute:: statistics
                
                	DHCPv6 relay statistics
                	**type**\: :py:class:`Statistics <ydk.models.ipv6.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Relay.Statistics>`
                
                .. attribute:: binding
                
                	DHCPV6 relay bindings
                	**type**\: :py:class:`Binding <ydk.models.ipv6.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Relay.Binding>`
                
                .. attribute:: vrfs
                
                	DHCPV6 relay list of VRF names
                	**type**\: :py:class:`Vrfs <ydk.models.ipv6.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Relay.Vrfs>`
                
                

                """

                _prefix = 'ipv6-new-dhcpv6d-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.statistics = Dhcpv6.Nodes.Node.Relay.Statistics()
                    self.statistics.parent = self
                    self.binding = Dhcpv6.Nodes.Node.Relay.Binding()
                    self.binding.parent = self
                    self.vrfs = Dhcpv6.Nodes.Node.Relay.Vrfs()
                    self.vrfs.parent = self


                class Statistics(object):
                    """
                    DHCPv6 relay statistics
                    
                    .. attribute:: ipv6_dhcpv6d_relay_stat
                    
                    	ipv6 dhcpv6d relay stat
                    	**type**\: list of :py:class:`Ipv6Dhcpv6DRelayStat <ydk.models.ipv6.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Relay.Statistics.Ipv6Dhcpv6DRelayStat>`
                    
                    

                    """

                    _prefix = 'ipv6-new-dhcpv6d-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.ipv6_dhcpv6d_relay_stat = YList()
                        self.ipv6_dhcpv6d_relay_stat.parent = self
                        self.ipv6_dhcpv6d_relay_stat.name = 'ipv6_dhcpv6d_relay_stat'


                    class Ipv6Dhcpv6DRelayStat(object):
                        """
                        ipv6 dhcpv6d relay stat
                        
                        .. attribute:: statistics
                        
                        	Relay statistics
                        	**type**\: :py:class:`Statistics <ydk.models.ipv6.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Relay.Statistics.Ipv6Dhcpv6DRelayStat.Statistics>`
                        
                        .. attribute:: vrf_name
                        
                        	DHCPv6 L3 VRF name
                        	**type**\: str
                        
                        	**range:** 0..33
                        
                        

                        """

                        _prefix = 'ipv6-new-dhcpv6d-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.statistics = Dhcpv6.Nodes.Node.Relay.Statistics.Ipv6Dhcpv6DRelayStat.Statistics()
                            self.statistics.parent = self
                            self.vrf_name = None


                        class Statistics(object):
                            """
                            Relay statistics
                            
                            .. attribute:: received_packets
                            
                            	Received packets
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: transmitted_packets
                            
                            	Transmitted packets
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: dropped_packets
                            
                            	Dropped packets
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            

                            """

                            _prefix = 'ipv6-new-dhcpv6d-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.received_packets = None
                                self.transmitted_packets = None
                                self.dropped_packets = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-ipv6-new-dhcpv6d-oper:statistics'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.received_packets is not None:
                                    return True

                                if self.transmitted_packets is not None:
                                    return True

                                if self.dropped_packets is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.ipv6._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_oper as meta
                                return meta._meta_table['Dhcpv6.Nodes.Node.Relay.Statistics.Ipv6Dhcpv6DRelayStat.Statistics']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-ipv6-new-dhcpv6d-oper:ipv6-dhcpv6d-relay-stat'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.statistics is not None and self.statistics._has_data():
                                return True

                            if self.vrf_name is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.ipv6._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_oper as meta
                            return meta._meta_table['Dhcpv6.Nodes.Node.Relay.Statistics.Ipv6Dhcpv6DRelayStat']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ipv6-new-dhcpv6d-oper:statistics'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.ipv6_dhcpv6d_relay_stat is not None:
                            for child_ref in self.ipv6_dhcpv6d_relay_stat:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.ipv6._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_oper as meta
                        return meta._meta_table['Dhcpv6.Nodes.Node.Relay.Statistics']['meta_info']


                class Binding(object):
                    """
                    DHCPV6 relay bindings
                    
                    .. attribute:: summary
                    
                    	DHCPV6 relay binding summary
                    	**type**\: :py:class:`Summary <ydk.models.ipv6.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Relay.Binding.Summary>`
                    
                    .. attribute:: clients
                    
                    	DHCPV6 relay client bindings
                    	**type**\: :py:class:`Clients <ydk.models.ipv6.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Relay.Binding.Clients>`
                    
                    

                    """

                    _prefix = 'ipv6-new-dhcpv6d-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.summary = Dhcpv6.Nodes.Node.Relay.Binding.Summary()
                        self.summary.parent = self
                        self.clients = Dhcpv6.Nodes.Node.Relay.Binding.Clients()
                        self.clients.parent = self


                    class Summary(object):
                        """
                        DHCPV6 relay binding summary
                        
                        .. attribute:: clients
                        
                        	Total number of clients
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'ipv6-new-dhcpv6d-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.clients = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-ipv6-new-dhcpv6d-oper:summary'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.clients is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.ipv6._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_oper as meta
                            return meta._meta_table['Dhcpv6.Nodes.Node.Relay.Binding.Summary']['meta_info']


                    class Clients(object):
                        """
                        DHCPV6 relay client bindings
                        
                        .. attribute:: client
                        
                        	Single DHCPV6 relay binding
                        	**type**\: list of :py:class:`Client <ydk.models.ipv6.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Relay.Binding.Clients.Client>`
                        
                        

                        """

                        _prefix = 'ipv6-new-dhcpv6d-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.client = YList()
                            self.client.parent = self
                            self.client.name = 'client'


                        class Client(object):
                            """
                            Single DHCPV6 relay binding
                            
                            .. attribute:: client_id  <key>
                            
                            	Client ID
                            	**type**\: str
                            
                            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                            
                            .. attribute:: duid
                            
                            	Client DUID
                            	**type**\: str
                            
                            .. attribute:: client_id_xr
                            
                            	Client unique identifier
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: prefix_length
                            
                            	length of prefix
                            	**type**\: int
                            
                            	**range:** 0..255
                            
                            .. attribute:: prefix
                            
                            	DHCPV6 IPv6 Prefix allotted to client
                            	**type**\: str
                            
                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: vrf_name
                            
                            	DHCPv6 client/subscriber Vrf name
                            	**type**\: str
                            
                            	**range:** 0..33
                            
                            .. attribute:: lifetime
                            
                            	Client route lifetime
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: rem_life_time
                            
                            	Client route remaining lifetime
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: interface_name
                            
                            	Interface name
                            	**type**\: str
                            
                            	**range:** 0..65
                            
                            .. attribute:: next_hop_addr
                            
                            	Next hop is our address
                            	**type**\: str
                            
                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: ia_id
                            
                            	IA\_ID of this IA
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: relay_profile_name
                            
                            	Relay Profile name
                            	**type**\: str
                            
                            	**range:** 0..65
                            
                            

                            """

                            _prefix = 'ipv6-new-dhcpv6d-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.client_id = None
                                self.duid = None
                                self.client_id_xr = None
                                self.prefix_length = None
                                self.prefix = None
                                self.vrf_name = None
                                self.lifetime = None
                                self.rem_life_time = None
                                self.interface_name = None
                                self.next_hop_addr = None
                                self.ia_id = None
                                self.relay_profile_name = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')
                                if self.client_id is None:
                                    raise YPYDataValidationError('Key property client_id is None')

                                return self.parent._common_path +'/Cisco-IOS-XR-ipv6-new-dhcpv6d-oper:client[Cisco-IOS-XR-ipv6-new-dhcpv6d-oper:client-id = ' + str(self.client_id) + ']'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.client_id is not None:
                                    return True

                                if self.duid is not None:
                                    return True

                                if self.client_id_xr is not None:
                                    return True

                                if self.prefix_length is not None:
                                    return True

                                if self.prefix is not None:
                                    return True

                                if self.vrf_name is not None:
                                    return True

                                if self.lifetime is not None:
                                    return True

                                if self.rem_life_time is not None:
                                    return True

                                if self.interface_name is not None:
                                    return True

                                if self.next_hop_addr is not None:
                                    return True

                                if self.ia_id is not None:
                                    return True

                                if self.relay_profile_name is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.ipv6._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_oper as meta
                                return meta._meta_table['Dhcpv6.Nodes.Node.Relay.Binding.Clients.Client']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-ipv6-new-dhcpv6d-oper:clients'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.client is not None:
                                for child_ref in self.client:
                                    if child_ref._has_data():
                                        return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.ipv6._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_oper as meta
                            return meta._meta_table['Dhcpv6.Nodes.Node.Relay.Binding.Clients']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ipv6-new-dhcpv6d-oper:binding'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.summary is not None and self.summary._has_data():
                            return True

                        if self.clients is not None and self.clients._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.ipv6._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_oper as meta
                        return meta._meta_table['Dhcpv6.Nodes.Node.Relay.Binding']['meta_info']


                class Vrfs(object):
                    """
                    DHCPV6 relay list of VRF names
                    
                    .. attribute:: vrf
                    
                    	IPv6 DHCP relay VRF name
                    	**type**\: list of :py:class:`Vrf <ydk.models.ipv6.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Relay.Vrfs.Vrf>`
                    
                    

                    """

                    _prefix = 'ipv6-new-dhcpv6d-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.vrf = YList()
                        self.vrf.parent = self
                        self.vrf.name = 'vrf'


                    class Vrf(object):
                        """
                        IPv6 DHCP relay VRF name
                        
                        .. attribute:: vrf_name  <key>
                        
                        	VRF name
                        	**type**\: str
                        
                        	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                        
                        .. attribute:: statistics
                        
                        	IPv6 DHCP relay statistics
                        	**type**\: :py:class:`Statistics <ydk.models.ipv6.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Relay.Vrfs.Vrf.Statistics>`
                        
                        

                        """

                        _prefix = 'ipv6-new-dhcpv6d-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.vrf_name = None
                            self.statistics = Dhcpv6.Nodes.Node.Relay.Vrfs.Vrf.Statistics()
                            self.statistics.parent = self


                        class Statistics(object):
                            """
                            IPv6 DHCP relay statistics
                            
                            .. attribute:: solicit
                            
                            	DHCPV6 solicit packets
                            	**type**\: :py:class:`Solicit <ydk.models.ipv6.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Relay.Vrfs.Vrf.Statistics.Solicit>`
                            
                            .. attribute:: advertise
                            
                            	DHCPV6 advertise packets
                            	**type**\: :py:class:`Advertise <ydk.models.ipv6.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Relay.Vrfs.Vrf.Statistics.Advertise>`
                            
                            .. attribute:: request
                            
                            	DHCPV6 request packets
                            	**type**\: :py:class:`Request <ydk.models.ipv6.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Relay.Vrfs.Vrf.Statistics.Request>`
                            
                            .. attribute:: reply
                            
                            	DHCPV6 reply packets
                            	**type**\: :py:class:`Reply <ydk.models.ipv6.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Relay.Vrfs.Vrf.Statistics.Reply>`
                            
                            .. attribute:: confirm
                            
                            	DHCPV6 confirm packets
                            	**type**\: :py:class:`Confirm <ydk.models.ipv6.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Relay.Vrfs.Vrf.Statistics.Confirm>`
                            
                            .. attribute:: decline
                            
                            	DHCPV6 decline packets
                            	**type**\: :py:class:`Decline <ydk.models.ipv6.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Relay.Vrfs.Vrf.Statistics.Decline>`
                            
                            .. attribute:: renew
                            
                            	DHCPV6 renew packets
                            	**type**\: :py:class:`Renew <ydk.models.ipv6.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Relay.Vrfs.Vrf.Statistics.Renew>`
                            
                            .. attribute:: rebind
                            
                            	DHCPV6 rebind packets
                            	**type**\: :py:class:`Rebind <ydk.models.ipv6.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Relay.Vrfs.Vrf.Statistics.Rebind>`
                            
                            .. attribute:: release
                            
                            	DHCPV6 release packets
                            	**type**\: :py:class:`Release <ydk.models.ipv6.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Relay.Vrfs.Vrf.Statistics.Release>`
                            
                            .. attribute:: reconfig
                            
                            	DHCPV6 reconfig packets
                            	**type**\: :py:class:`Reconfig <ydk.models.ipv6.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Relay.Vrfs.Vrf.Statistics.Reconfig>`
                            
                            .. attribute:: inform
                            
                            	DHCPV6 inform packets
                            	**type**\: :py:class:`Inform <ydk.models.ipv6.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Relay.Vrfs.Vrf.Statistics.Inform>`
                            
                            .. attribute:: relay_forward
                            
                            	DHCPV6 relay forward packets
                            	**type**\: :py:class:`RelayForward <ydk.models.ipv6.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Relay.Vrfs.Vrf.Statistics.RelayForward>`
                            
                            .. attribute:: relay_reply
                            
                            	DHCPV6 relay reply packets
                            	**type**\: :py:class:`RelayReply <ydk.models.ipv6.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Relay.Vrfs.Vrf.Statistics.RelayReply>`
                            
                            .. attribute:: lease_query
                            
                            	DHCPV6 lease query packets
                            	**type**\: :py:class:`LeaseQuery <ydk.models.ipv6.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Relay.Vrfs.Vrf.Statistics.LeaseQuery>`
                            
                            .. attribute:: lease_query_reply
                            
                            	DHCPV6 lease query reply packets
                            	**type**\: :py:class:`LeaseQueryReply <ydk.models.ipv6.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Relay.Vrfs.Vrf.Statistics.LeaseQueryReply>`
                            
                            .. attribute:: lease_query_done
                            
                            	DHCPV6 lease query done packets
                            	**type**\: :py:class:`LeaseQueryDone <ydk.models.ipv6.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Relay.Vrfs.Vrf.Statistics.LeaseQueryDone>`
                            
                            .. attribute:: lease_query_data
                            
                            	DHCPV6 lease query data packets
                            	**type**\: :py:class:`LeaseQueryData <ydk.models.ipv6.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Relay.Vrfs.Vrf.Statistics.LeaseQueryData>`
                            
                            

                            """

                            _prefix = 'ipv6-new-dhcpv6d-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.solicit = Dhcpv6.Nodes.Node.Relay.Vrfs.Vrf.Statistics.Solicit()
                                self.solicit.parent = self
                                self.advertise = Dhcpv6.Nodes.Node.Relay.Vrfs.Vrf.Statistics.Advertise()
                                self.advertise.parent = self
                                self.request = Dhcpv6.Nodes.Node.Relay.Vrfs.Vrf.Statistics.Request()
                                self.request.parent = self
                                self.reply = Dhcpv6.Nodes.Node.Relay.Vrfs.Vrf.Statistics.Reply()
                                self.reply.parent = self
                                self.confirm = Dhcpv6.Nodes.Node.Relay.Vrfs.Vrf.Statistics.Confirm()
                                self.confirm.parent = self
                                self.decline = Dhcpv6.Nodes.Node.Relay.Vrfs.Vrf.Statistics.Decline()
                                self.decline.parent = self
                                self.renew = Dhcpv6.Nodes.Node.Relay.Vrfs.Vrf.Statistics.Renew()
                                self.renew.parent = self
                                self.rebind = Dhcpv6.Nodes.Node.Relay.Vrfs.Vrf.Statistics.Rebind()
                                self.rebind.parent = self
                                self.release = Dhcpv6.Nodes.Node.Relay.Vrfs.Vrf.Statistics.Release()
                                self.release.parent = self
                                self.reconfig = Dhcpv6.Nodes.Node.Relay.Vrfs.Vrf.Statistics.Reconfig()
                                self.reconfig.parent = self
                                self.inform = Dhcpv6.Nodes.Node.Relay.Vrfs.Vrf.Statistics.Inform()
                                self.inform.parent = self
                                self.relay_forward = Dhcpv6.Nodes.Node.Relay.Vrfs.Vrf.Statistics.RelayForward()
                                self.relay_forward.parent = self
                                self.relay_reply = Dhcpv6.Nodes.Node.Relay.Vrfs.Vrf.Statistics.RelayReply()
                                self.relay_reply.parent = self
                                self.lease_query = Dhcpv6.Nodes.Node.Relay.Vrfs.Vrf.Statistics.LeaseQuery()
                                self.lease_query.parent = self
                                self.lease_query_reply = Dhcpv6.Nodes.Node.Relay.Vrfs.Vrf.Statistics.LeaseQueryReply()
                                self.lease_query_reply.parent = self
                                self.lease_query_done = Dhcpv6.Nodes.Node.Relay.Vrfs.Vrf.Statistics.LeaseQueryDone()
                                self.lease_query_done.parent = self
                                self.lease_query_data = Dhcpv6.Nodes.Node.Relay.Vrfs.Vrf.Statistics.LeaseQueryData()
                                self.lease_query_data.parent = self


                            class Solicit(object):
                                """
                                DHCPV6 solicit packets
                                
                                .. attribute:: received_packets
                                
                                	Received packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: transmitted_packets
                                
                                	Transmitted packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: dropped_packets
                                
                                	Dropped packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                

                                """

                                _prefix = 'ipv6-new-dhcpv6d-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.received_packets = None
                                    self.transmitted_packets = None
                                    self.dropped_packets = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ipv6-new-dhcpv6d-oper:solicit'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.received_packets is not None:
                                        return True

                                    if self.transmitted_packets is not None:
                                        return True

                                    if self.dropped_packets is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.ipv6._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_oper as meta
                                    return meta._meta_table['Dhcpv6.Nodes.Node.Relay.Vrfs.Vrf.Statistics.Solicit']['meta_info']


                            class Advertise(object):
                                """
                                DHCPV6 advertise packets
                                
                                .. attribute:: received_packets
                                
                                	Received packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: transmitted_packets
                                
                                	Transmitted packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: dropped_packets
                                
                                	Dropped packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                

                                """

                                _prefix = 'ipv6-new-dhcpv6d-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.received_packets = None
                                    self.transmitted_packets = None
                                    self.dropped_packets = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ipv6-new-dhcpv6d-oper:advertise'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.received_packets is not None:
                                        return True

                                    if self.transmitted_packets is not None:
                                        return True

                                    if self.dropped_packets is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.ipv6._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_oper as meta
                                    return meta._meta_table['Dhcpv6.Nodes.Node.Relay.Vrfs.Vrf.Statistics.Advertise']['meta_info']


                            class Request(object):
                                """
                                DHCPV6 request packets
                                
                                .. attribute:: received_packets
                                
                                	Received packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: transmitted_packets
                                
                                	Transmitted packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: dropped_packets
                                
                                	Dropped packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                

                                """

                                _prefix = 'ipv6-new-dhcpv6d-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.received_packets = None
                                    self.transmitted_packets = None
                                    self.dropped_packets = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ipv6-new-dhcpv6d-oper:request'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.received_packets is not None:
                                        return True

                                    if self.transmitted_packets is not None:
                                        return True

                                    if self.dropped_packets is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.ipv6._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_oper as meta
                                    return meta._meta_table['Dhcpv6.Nodes.Node.Relay.Vrfs.Vrf.Statistics.Request']['meta_info']


                            class Reply(object):
                                """
                                DHCPV6 reply packets
                                
                                .. attribute:: received_packets
                                
                                	Received packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: transmitted_packets
                                
                                	Transmitted packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: dropped_packets
                                
                                	Dropped packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                

                                """

                                _prefix = 'ipv6-new-dhcpv6d-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.received_packets = None
                                    self.transmitted_packets = None
                                    self.dropped_packets = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ipv6-new-dhcpv6d-oper:reply'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.received_packets is not None:
                                        return True

                                    if self.transmitted_packets is not None:
                                        return True

                                    if self.dropped_packets is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.ipv6._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_oper as meta
                                    return meta._meta_table['Dhcpv6.Nodes.Node.Relay.Vrfs.Vrf.Statistics.Reply']['meta_info']


                            class Confirm(object):
                                """
                                DHCPV6 confirm packets
                                
                                .. attribute:: received_packets
                                
                                	Received packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: transmitted_packets
                                
                                	Transmitted packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: dropped_packets
                                
                                	Dropped packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                

                                """

                                _prefix = 'ipv6-new-dhcpv6d-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.received_packets = None
                                    self.transmitted_packets = None
                                    self.dropped_packets = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ipv6-new-dhcpv6d-oper:confirm'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.received_packets is not None:
                                        return True

                                    if self.transmitted_packets is not None:
                                        return True

                                    if self.dropped_packets is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.ipv6._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_oper as meta
                                    return meta._meta_table['Dhcpv6.Nodes.Node.Relay.Vrfs.Vrf.Statistics.Confirm']['meta_info']


                            class Decline(object):
                                """
                                DHCPV6 decline packets
                                
                                .. attribute:: received_packets
                                
                                	Received packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: transmitted_packets
                                
                                	Transmitted packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: dropped_packets
                                
                                	Dropped packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                

                                """

                                _prefix = 'ipv6-new-dhcpv6d-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.received_packets = None
                                    self.transmitted_packets = None
                                    self.dropped_packets = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ipv6-new-dhcpv6d-oper:decline'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.received_packets is not None:
                                        return True

                                    if self.transmitted_packets is not None:
                                        return True

                                    if self.dropped_packets is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.ipv6._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_oper as meta
                                    return meta._meta_table['Dhcpv6.Nodes.Node.Relay.Vrfs.Vrf.Statistics.Decline']['meta_info']


                            class Renew(object):
                                """
                                DHCPV6 renew packets
                                
                                .. attribute:: received_packets
                                
                                	Received packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: transmitted_packets
                                
                                	Transmitted packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: dropped_packets
                                
                                	Dropped packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                

                                """

                                _prefix = 'ipv6-new-dhcpv6d-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.received_packets = None
                                    self.transmitted_packets = None
                                    self.dropped_packets = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ipv6-new-dhcpv6d-oper:renew'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.received_packets is not None:
                                        return True

                                    if self.transmitted_packets is not None:
                                        return True

                                    if self.dropped_packets is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.ipv6._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_oper as meta
                                    return meta._meta_table['Dhcpv6.Nodes.Node.Relay.Vrfs.Vrf.Statistics.Renew']['meta_info']


                            class Rebind(object):
                                """
                                DHCPV6 rebind packets
                                
                                .. attribute:: received_packets
                                
                                	Received packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: transmitted_packets
                                
                                	Transmitted packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: dropped_packets
                                
                                	Dropped packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                

                                """

                                _prefix = 'ipv6-new-dhcpv6d-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.received_packets = None
                                    self.transmitted_packets = None
                                    self.dropped_packets = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ipv6-new-dhcpv6d-oper:rebind'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.received_packets is not None:
                                        return True

                                    if self.transmitted_packets is not None:
                                        return True

                                    if self.dropped_packets is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.ipv6._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_oper as meta
                                    return meta._meta_table['Dhcpv6.Nodes.Node.Relay.Vrfs.Vrf.Statistics.Rebind']['meta_info']


                            class Release(object):
                                """
                                DHCPV6 release packets
                                
                                .. attribute:: received_packets
                                
                                	Received packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: transmitted_packets
                                
                                	Transmitted packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: dropped_packets
                                
                                	Dropped packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                

                                """

                                _prefix = 'ipv6-new-dhcpv6d-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.received_packets = None
                                    self.transmitted_packets = None
                                    self.dropped_packets = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ipv6-new-dhcpv6d-oper:release'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.received_packets is not None:
                                        return True

                                    if self.transmitted_packets is not None:
                                        return True

                                    if self.dropped_packets is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.ipv6._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_oper as meta
                                    return meta._meta_table['Dhcpv6.Nodes.Node.Relay.Vrfs.Vrf.Statistics.Release']['meta_info']


                            class Reconfig(object):
                                """
                                DHCPV6 reconfig packets
                                
                                .. attribute:: received_packets
                                
                                	Received packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: transmitted_packets
                                
                                	Transmitted packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: dropped_packets
                                
                                	Dropped packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                

                                """

                                _prefix = 'ipv6-new-dhcpv6d-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.received_packets = None
                                    self.transmitted_packets = None
                                    self.dropped_packets = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ipv6-new-dhcpv6d-oper:reconfig'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.received_packets is not None:
                                        return True

                                    if self.transmitted_packets is not None:
                                        return True

                                    if self.dropped_packets is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.ipv6._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_oper as meta
                                    return meta._meta_table['Dhcpv6.Nodes.Node.Relay.Vrfs.Vrf.Statistics.Reconfig']['meta_info']


                            class Inform(object):
                                """
                                DHCPV6 inform packets
                                
                                .. attribute:: received_packets
                                
                                	Received packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: transmitted_packets
                                
                                	Transmitted packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: dropped_packets
                                
                                	Dropped packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                

                                """

                                _prefix = 'ipv6-new-dhcpv6d-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.received_packets = None
                                    self.transmitted_packets = None
                                    self.dropped_packets = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ipv6-new-dhcpv6d-oper:inform'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.received_packets is not None:
                                        return True

                                    if self.transmitted_packets is not None:
                                        return True

                                    if self.dropped_packets is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.ipv6._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_oper as meta
                                    return meta._meta_table['Dhcpv6.Nodes.Node.Relay.Vrfs.Vrf.Statistics.Inform']['meta_info']


                            class RelayForward(object):
                                """
                                DHCPV6 relay forward packets
                                
                                .. attribute:: received_packets
                                
                                	Received packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: transmitted_packets
                                
                                	Transmitted packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: dropped_packets
                                
                                	Dropped packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                

                                """

                                _prefix = 'ipv6-new-dhcpv6d-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.received_packets = None
                                    self.transmitted_packets = None
                                    self.dropped_packets = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ipv6-new-dhcpv6d-oper:relay-forward'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.received_packets is not None:
                                        return True

                                    if self.transmitted_packets is not None:
                                        return True

                                    if self.dropped_packets is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.ipv6._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_oper as meta
                                    return meta._meta_table['Dhcpv6.Nodes.Node.Relay.Vrfs.Vrf.Statistics.RelayForward']['meta_info']


                            class RelayReply(object):
                                """
                                DHCPV6 relay reply packets
                                
                                .. attribute:: received_packets
                                
                                	Received packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: transmitted_packets
                                
                                	Transmitted packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: dropped_packets
                                
                                	Dropped packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                

                                """

                                _prefix = 'ipv6-new-dhcpv6d-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.received_packets = None
                                    self.transmitted_packets = None
                                    self.dropped_packets = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ipv6-new-dhcpv6d-oper:relay-reply'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.received_packets is not None:
                                        return True

                                    if self.transmitted_packets is not None:
                                        return True

                                    if self.dropped_packets is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.ipv6._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_oper as meta
                                    return meta._meta_table['Dhcpv6.Nodes.Node.Relay.Vrfs.Vrf.Statistics.RelayReply']['meta_info']


                            class LeaseQuery(object):
                                """
                                DHCPV6 lease query packets
                                
                                .. attribute:: received_packets
                                
                                	Received packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: transmitted_packets
                                
                                	Transmitted packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: dropped_packets
                                
                                	Dropped packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                

                                """

                                _prefix = 'ipv6-new-dhcpv6d-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.received_packets = None
                                    self.transmitted_packets = None
                                    self.dropped_packets = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ipv6-new-dhcpv6d-oper:lease-query'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.received_packets is not None:
                                        return True

                                    if self.transmitted_packets is not None:
                                        return True

                                    if self.dropped_packets is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.ipv6._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_oper as meta
                                    return meta._meta_table['Dhcpv6.Nodes.Node.Relay.Vrfs.Vrf.Statistics.LeaseQuery']['meta_info']


                            class LeaseQueryReply(object):
                                """
                                DHCPV6 lease query reply packets
                                
                                .. attribute:: received_packets
                                
                                	Received packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: transmitted_packets
                                
                                	Transmitted packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: dropped_packets
                                
                                	Dropped packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                

                                """

                                _prefix = 'ipv6-new-dhcpv6d-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.received_packets = None
                                    self.transmitted_packets = None
                                    self.dropped_packets = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ipv6-new-dhcpv6d-oper:lease-query-reply'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.received_packets is not None:
                                        return True

                                    if self.transmitted_packets is not None:
                                        return True

                                    if self.dropped_packets is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.ipv6._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_oper as meta
                                    return meta._meta_table['Dhcpv6.Nodes.Node.Relay.Vrfs.Vrf.Statistics.LeaseQueryReply']['meta_info']


                            class LeaseQueryDone(object):
                                """
                                DHCPV6 lease query done packets
                                
                                .. attribute:: received_packets
                                
                                	Received packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: transmitted_packets
                                
                                	Transmitted packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: dropped_packets
                                
                                	Dropped packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                

                                """

                                _prefix = 'ipv6-new-dhcpv6d-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.received_packets = None
                                    self.transmitted_packets = None
                                    self.dropped_packets = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ipv6-new-dhcpv6d-oper:lease-query-done'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.received_packets is not None:
                                        return True

                                    if self.transmitted_packets is not None:
                                        return True

                                    if self.dropped_packets is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.ipv6._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_oper as meta
                                    return meta._meta_table['Dhcpv6.Nodes.Node.Relay.Vrfs.Vrf.Statistics.LeaseQueryDone']['meta_info']


                            class LeaseQueryData(object):
                                """
                                DHCPV6 lease query data packets
                                
                                .. attribute:: received_packets
                                
                                	Received packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: transmitted_packets
                                
                                	Transmitted packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: dropped_packets
                                
                                	Dropped packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                

                                """

                                _prefix = 'ipv6-new-dhcpv6d-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.received_packets = None
                                    self.transmitted_packets = None
                                    self.dropped_packets = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ipv6-new-dhcpv6d-oper:lease-query-data'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.received_packets is not None:
                                        return True

                                    if self.transmitted_packets is not None:
                                        return True

                                    if self.dropped_packets is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.ipv6._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_oper as meta
                                    return meta._meta_table['Dhcpv6.Nodes.Node.Relay.Vrfs.Vrf.Statistics.LeaseQueryData']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-ipv6-new-dhcpv6d-oper:statistics'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.solicit is not None and self.solicit._has_data():
                                    return True

                                if self.advertise is not None and self.advertise._has_data():
                                    return True

                                if self.request is not None and self.request._has_data():
                                    return True

                                if self.reply is not None and self.reply._has_data():
                                    return True

                                if self.confirm is not None and self.confirm._has_data():
                                    return True

                                if self.decline is not None and self.decline._has_data():
                                    return True

                                if self.renew is not None and self.renew._has_data():
                                    return True

                                if self.rebind is not None and self.rebind._has_data():
                                    return True

                                if self.release is not None and self.release._has_data():
                                    return True

                                if self.reconfig is not None and self.reconfig._has_data():
                                    return True

                                if self.inform is not None and self.inform._has_data():
                                    return True

                                if self.relay_forward is not None and self.relay_forward._has_data():
                                    return True

                                if self.relay_reply is not None and self.relay_reply._has_data():
                                    return True

                                if self.lease_query is not None and self.lease_query._has_data():
                                    return True

                                if self.lease_query_reply is not None and self.lease_query_reply._has_data():
                                    return True

                                if self.lease_query_done is not None and self.lease_query_done._has_data():
                                    return True

                                if self.lease_query_data is not None and self.lease_query_data._has_data():
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.ipv6._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_oper as meta
                                return meta._meta_table['Dhcpv6.Nodes.Node.Relay.Vrfs.Vrf.Statistics']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')
                            if self.vrf_name is None:
                                raise YPYDataValidationError('Key property vrf_name is None')

                            return self.parent._common_path +'/Cisco-IOS-XR-ipv6-new-dhcpv6d-oper:vrf[Cisco-IOS-XR-ipv6-new-dhcpv6d-oper:vrf-name = ' + str(self.vrf_name) + ']'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.vrf_name is not None:
                                return True

                            if self.statistics is not None and self.statistics._has_data():
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.ipv6._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_oper as meta
                            return meta._meta_table['Dhcpv6.Nodes.Node.Relay.Vrfs.Vrf']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ipv6-new-dhcpv6d-oper:vrfs'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.vrf is not None:
                            for child_ref in self.vrf:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.ipv6._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_oper as meta
                        return meta._meta_table['Dhcpv6.Nodes.Node.Relay.Vrfs']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-ipv6-new-dhcpv6d-oper:relay'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.statistics is not None and self.statistics._has_data():
                        return True

                    if self.binding is not None and self.binding._has_data():
                        return True

                    if self.vrfs is not None and self.vrfs._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.ipv6._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_oper as meta
                    return meta._meta_table['Dhcpv6.Nodes.Node.Relay']['meta_info']

            @property
            def _common_path(self):
                if self.node_name is None:
                    raise YPYDataValidationError('Key property node_name is None')

                return '/Cisco-IOS-XR-ipv6-new-dhcpv6d-oper:dhcpv6/Cisco-IOS-XR-ipv6-new-dhcpv6d-oper:nodes/Cisco-IOS-XR-ipv6-new-dhcpv6d-oper:node[Cisco-IOS-XR-ipv6-new-dhcpv6d-oper:node-name = ' + str(self.node_name) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.node_name is not None:
                    return True

                if self.proxy is not None and self.proxy._has_data():
                    return True

                if self.server is not None and self.server._has_data():
                    return True

                if self.relay is not None and self.relay._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.ipv6._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_oper as meta
                return meta._meta_table['Dhcpv6.Nodes.Node']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-ipv6-new-dhcpv6d-oper:dhcpv6/Cisco-IOS-XR-ipv6-new-dhcpv6d-oper:nodes'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.node is not None:
                for child_ref in self.node:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.ipv6._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_oper as meta
            return meta._meta_table['Dhcpv6.Nodes']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-ipv6-new-dhcpv6d-oper:dhcpv6'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if not self.is_config():
            return False
        if self.database is not None and self.database._has_data():
            return True

        if self.nodes is not None and self.nodes._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.ipv6._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_oper as meta
        return meta._meta_table['Dhcpv6']['meta_info']


