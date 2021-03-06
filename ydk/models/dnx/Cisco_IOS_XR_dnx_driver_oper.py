""" Cisco_IOS_XR_dnx_driver_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR dnx\-driver package operational data.

This module contains definitions
for the following management objects\:
  fia\: FIA driver operational data

Copyright (c) 2013\-2015 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYDataValidationError




class Fia(object):
    """
    FIA driver operational data
    
    .. attribute:: nodes
    
    	FIA driver operational data for available nodes
    	**type**\: :py:class:`Nodes <ydk.models.dnx.Cisco_IOS_XR_dnx_driver_oper.Fia.Nodes>`
    
    

    """

    _prefix = 'dnx-driver-oper'
    _revision = '2015-11-09'

    def __init__(self):
        self.nodes = Fia.Nodes()
        self.nodes.parent = self


    class Nodes(object):
        """
        FIA driver operational data for available nodes
        
        .. attribute:: node
        
        	FIA operational data for a particular node
        	**type**\: list of :py:class:`Node <ydk.models.dnx.Cisco_IOS_XR_dnx_driver_oper.Fia.Nodes.Node>`
        
        

        """

        _prefix = 'dnx-driver-oper'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.node = YList()
            self.node.parent = self
            self.node.name = 'node'


        class Node(object):
            """
            FIA operational data for a particular node
            
            .. attribute:: node_name  <key>
            
            	Node ID
            	**type**\: str
            
            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
            
            .. attribute:: rx_link_information
            
            	FIA link rx information
            	**type**\: :py:class:`RxLinkInformation <ydk.models.dnx.Cisco_IOS_XR_dnx_driver_oper.Fia.Nodes.Node.RxLinkInformation>`
            
            .. attribute:: driver_information
            
            	FIA driver information
            	**type**\: :py:class:`DriverInformation <ydk.models.dnx.Cisco_IOS_XR_dnx_driver_oper.Fia.Nodes.Node.DriverInformation>`
            
            .. attribute:: clear_statistics
            
            	Clear statistics information
            	**type**\: :py:class:`ClearStatistics <ydk.models.dnx.Cisco_IOS_XR_dnx_driver_oper.Fia.Nodes.Node.ClearStatistics>`
            
            .. attribute:: tx_link_information
            
            	FIA link TX information
            	**type**\: :py:class:`TxLinkInformation <ydk.models.dnx.Cisco_IOS_XR_dnx_driver_oper.Fia.Nodes.Node.TxLinkInformation>`
            
            .. attribute:: register_dump
            
            	FIA register dump information
            	**type**\: :py:class:`RegisterDump <ydk.models.dnx.Cisco_IOS_XR_dnx_driver_oper.Fia.Nodes.Node.RegisterDump>`
            
            .. attribute:: diag_shell
            
            	FIA diag shell information
            	**type**\: :py:class:`DiagShell <ydk.models.dnx.Cisco_IOS_XR_dnx_driver_oper.Fia.Nodes.Node.DiagShell>`
            
            .. attribute:: oir_history
            
            	FIA operational data of oir history
            	**type**\: :py:class:`OirHistory <ydk.models.dnx.Cisco_IOS_XR_dnx_driver_oper.Fia.Nodes.Node.OirHistory>`
            
            .. attribute:: asic_statistics
            
            	FIA asic statistics information
            	**type**\: :py:class:`AsicStatistics <ydk.models.dnx.Cisco_IOS_XR_dnx_driver_oper.Fia.Nodes.Node.AsicStatistics>`
            
            

            """

            _prefix = 'dnx-driver-oper'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.node_name = None
                self.rx_link_information = Fia.Nodes.Node.RxLinkInformation()
                self.rx_link_information.parent = self
                self.driver_information = Fia.Nodes.Node.DriverInformation()
                self.driver_information.parent = self
                self.clear_statistics = Fia.Nodes.Node.ClearStatistics()
                self.clear_statistics.parent = self
                self.tx_link_information = Fia.Nodes.Node.TxLinkInformation()
                self.tx_link_information.parent = self
                self.register_dump = Fia.Nodes.Node.RegisterDump()
                self.register_dump.parent = self
                self.diag_shell = Fia.Nodes.Node.DiagShell()
                self.diag_shell.parent = self
                self.oir_history = Fia.Nodes.Node.OirHistory()
                self.oir_history.parent = self
                self.asic_statistics = Fia.Nodes.Node.AsicStatistics()
                self.asic_statistics.parent = self


            class RxLinkInformation(object):
                """
                FIA link rx information
                
                .. attribute:: link_options
                
                	Option table for link rx information
                	**type**\: :py:class:`LinkOptions <ydk.models.dnx.Cisco_IOS_XR_dnx_driver_oper.Fia.Nodes.Node.RxLinkInformation.LinkOptions>`
                
                

                """

                _prefix = 'dnx-driver-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.link_options = Fia.Nodes.Node.RxLinkInformation.LinkOptions()
                    self.link_options.parent = self


                class LinkOptions(object):
                    """
                    Option table for link rx information
                    
                    .. attribute:: link_option
                    
                    	Option \: topo , flag , stats
                    	**type**\: list of :py:class:`LinkOption <ydk.models.dnx.Cisco_IOS_XR_dnx_driver_oper.Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption>`
                    
                    

                    """

                    _prefix = 'dnx-driver-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.link_option = YList()
                        self.link_option.parent = self
                        self.link_option.name = 'link_option'


                    class LinkOption(object):
                        """
                        Option \: topo , flag , stats
                        
                        .. attribute:: option  <key>
                        
                        	Link option
                        	**type**\: str
                        
                        	**pattern:** (flap)\|(topo)
                        
                        .. attribute:: rx_asic_instances
                        
                        	Instance table for rx information
                        	**type**\: :py:class:`RxAsicInstances <ydk.models.dnx.Cisco_IOS_XR_dnx_driver_oper.Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances>`
                        
                        

                        """

                        _prefix = 'dnx-driver-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.option = None
                            self.rx_asic_instances = Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances()
                            self.rx_asic_instances.parent = self


                        class RxAsicInstances(object):
                            """
                            Instance table for rx information
                            
                            .. attribute:: rx_asic_instance
                            
                            	Instance number for rx link information
                            	**type**\: list of :py:class:`RxAsicInstance <ydk.models.dnx.Cisco_IOS_XR_dnx_driver_oper.Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances.RxAsicInstance>`
                            
                            

                            """

                            _prefix = 'dnx-driver-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.rx_asic_instance = YList()
                                self.rx_asic_instance.parent = self
                                self.rx_asic_instance.name = 'rx_asic_instance'


                            class RxAsicInstance(object):
                                """
                                Instance number for rx link information
                                
                                .. attribute:: instance  <key>
                                
                                	Receive instance
                                	**type**\: int
                                
                                	**range:** 0..16
                                
                                .. attribute:: rx_links
                                
                                	Link table class for rx information
                                	**type**\: :py:class:`RxLinks <ydk.models.dnx.Cisco_IOS_XR_dnx_driver_oper.Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances.RxAsicInstance.RxLinks>`
                                
                                

                                """

                                _prefix = 'dnx-driver-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.instance = None
                                    self.rx_links = Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances.RxAsicInstance.RxLinks()
                                    self.rx_links.parent = self


                                class RxLinks(object):
                                    """
                                    Link table class for rx information
                                    
                                    .. attribute:: rx_link
                                    
                                    	Link number for rx link information
                                    	**type**\: list of :py:class:`RxLink <ydk.models.dnx.Cisco_IOS_XR_dnx_driver_oper.Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances.RxAsicInstance.RxLinks.RxLink>`
                                    
                                    

                                    """

                                    _prefix = 'dnx-driver-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.rx_link = YList()
                                        self.rx_link.parent = self
                                        self.rx_link.name = 'rx_link'


                                    class RxLink(object):
                                        """
                                        Link number for rx link information
                                        
                                        .. attribute:: start_number
                                        
                                        	Start number
                                        	**type**\: int
                                        
                                        	**range:** 0..35
                                        
                                        .. attribute:: end_number
                                        
                                        	End number
                                        	**type**\: int
                                        
                                        	**range:** 0..35
                                        
                                        .. attribute:: status_option
                                        
                                        	RX link status option
                                        	**type**\: str
                                        
                                        	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                                        
                                        .. attribute:: rx_link
                                        
                                        	Single link information
                                        	**type**\: list of :py:class:`RxLink <ydk.models.dnx.Cisco_IOS_XR_dnx_driver_oper.Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances.RxAsicInstance.RxLinks.RxLink.RxLink>`
                                        
                                        

                                        """

                                        _prefix = 'dnx-driver-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            self.parent = None
                                            self.start_number = None
                                            self.end_number = None
                                            self.status_option = None
                                            self.rx_link = YList()
                                            self.rx_link.parent = self
                                            self.rx_link.name = 'rx_link'


                                        class RxLink(object):
                                            """
                                            Single link information
                                            
                                            .. attribute:: link  <key>
                                            
                                            	Single link
                                            	**type**\: int
                                            
                                            	**range:** \-2147483648..2147483647
                                            
                                            .. attribute:: this_link
                                            
                                            	this link
                                            	**type**\: :py:class:`ThisLink <ydk.models.dnx.Cisco_IOS_XR_dnx_driver_oper.Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances.RxAsicInstance.RxLinks.RxLink.RxLink.ThisLink>`
                                            
                                            .. attribute:: far_end_link
                                            
                                            	far end link
                                            	**type**\: :py:class:`FarEndLink <ydk.models.dnx.Cisco_IOS_XR_dnx_driver_oper.Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances.RxAsicInstance.RxLinks.RxLink.RxLink.FarEndLink>`
                                            
                                            .. attribute:: far_end_link_in_hw
                                            
                                            	far end link in hw
                                            	**type**\: :py:class:`FarEndLinkInHw <ydk.models.dnx.Cisco_IOS_XR_dnx_driver_oper.Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances.RxAsicInstance.RxLinks.RxLink.RxLink.FarEndLinkInHw>`
                                            
                                            .. attribute:: history
                                            
                                            	history
                                            	**type**\: :py:class:`History <ydk.models.dnx.Cisco_IOS_XR_dnx_driver_oper.Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances.RxAsicInstance.RxLinks.RxLink.RxLink.History>`
                                            
                                            .. attribute:: speed
                                            
                                            	speed
                                            	**type**\: int
                                            
                                            	**range:** 0..4294967295
                                            
                                            .. attribute:: stage
                                            
                                            	stage
                                            	**type**\: int
                                            
                                            	**range:** 0..255
                                            
                                            .. attribute:: is_link_valid
                                            
                                            	is link valid
                                            	**type**\: bool
                                            
                                            .. attribute:: is_conf_pending
                                            
                                            	is conf pending
                                            	**type**\: bool
                                            
                                            .. attribute:: admin_state
                                            
                                            	admin state
                                            	**type**\: int
                                            
                                            	**range:** 0..255
                                            
                                            .. attribute:: oper_state
                                            
                                            	oper state
                                            	**type**\: int
                                            
                                            	**range:** 0..255
                                            
                                            .. attribute:: error_state
                                            
                                            	error state
                                            	**type**\: int
                                            
                                            	**range:** 0..255
                                            
                                            .. attribute:: flags
                                            
                                            	flags
                                            	**type**\: str
                                            
                                            .. attribute:: flap_cnt
                                            
                                            	flap cnt
                                            	**type**\: int
                                            
                                            	**range:** 0..4294967295
                                            
                                            .. attribute:: num_admin_shuts
                                            
                                            	num admin shuts
                                            	**type**\: int
                                            
                                            	**range:** 0..4294967295
                                            
                                            

                                            """

                                            _prefix = 'dnx-driver-oper'
                                            _revision = '2015-11-09'

                                            def __init__(self):
                                                self.parent = None
                                                self.link = None
                                                self.this_link = Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances.RxAsicInstance.RxLinks.RxLink.RxLink.ThisLink()
                                                self.this_link.parent = self
                                                self.far_end_link = Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances.RxAsicInstance.RxLinks.RxLink.RxLink.FarEndLink()
                                                self.far_end_link.parent = self
                                                self.far_end_link_in_hw = Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances.RxAsicInstance.RxLinks.RxLink.RxLink.FarEndLinkInHw()
                                                self.far_end_link_in_hw.parent = self
                                                self.history = Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances.RxAsicInstance.RxLinks.RxLink.RxLink.History()
                                                self.history.parent = self
                                                self.speed = None
                                                self.stage = None
                                                self.is_link_valid = None
                                                self.is_conf_pending = None
                                                self.admin_state = None
                                                self.oper_state = None
                                                self.error_state = None
                                                self.flags = None
                                                self.flap_cnt = None
                                                self.num_admin_shuts = None


                                            class ThisLink(object):
                                                """
                                                this link
                                                
                                                .. attribute:: asic_id
                                                
                                                	asic id
                                                	**type**\: :py:class:`AsicId <ydk.models.dnx.Cisco_IOS_XR_dnx_driver_oper.Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances.RxAsicInstance.RxLinks.RxLink.RxLink.ThisLink.AsicId>`
                                                
                                                .. attribute:: link_type
                                                
                                                	link type
                                                	**type**\: int
                                                
                                                	**range:** 0..255
                                                
                                                .. attribute:: link_stage
                                                
                                                	link stage
                                                	**type**\: int
                                                
                                                	**range:** 0..255
                                                
                                                .. attribute:: link_num
                                                
                                                	link num
                                                	**type**\: int
                                                
                                                	**range:** 0..4294967295
                                                
                                                .. attribute:: phy_link_num
                                                
                                                	phy link num
                                                	**type**\: int
                                                
                                                	**range:** 0..4294967295
                                                
                                                

                                                """

                                                _prefix = 'dnx-driver-oper'
                                                _revision = '2015-11-09'

                                                def __init__(self):
                                                    self.parent = None
                                                    self.asic_id = Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances.RxAsicInstance.RxLinks.RxLink.RxLink.ThisLink.AsicId()
                                                    self.asic_id.parent = self
                                                    self.link_type = None
                                                    self.link_stage = None
                                                    self.link_num = None
                                                    self.phy_link_num = None


                                                class AsicId(object):
                                                    """
                                                    asic id
                                                    
                                                    .. attribute:: rack_type
                                                    
                                                    	rack type
                                                    	**type**\: int
                                                    
                                                    	**range:** 0..4294967295
                                                    
                                                    .. attribute:: asic_type
                                                    
                                                    	asic type
                                                    	**type**\: int
                                                    
                                                    	**range:** 0..255
                                                    
                                                    .. attribute:: rack_num
                                                    
                                                    	rack num
                                                    	**type**\: int
                                                    
                                                    	**range:** 0..4294967295
                                                    
                                                    .. attribute:: slot_num
                                                    
                                                    	slot num
                                                    	**type**\: int
                                                    
                                                    	**range:** 0..4294967295
                                                    
                                                    .. attribute:: asic_instance
                                                    
                                                    	asic instance
                                                    	**type**\: int
                                                    
                                                    	**range:** 0..4294967295
                                                    
                                                    

                                                    """

                                                    _prefix = 'dnx-driver-oper'
                                                    _revision = '2015-11-09'

                                                    def __init__(self):
                                                        self.parent = None
                                                        self.rack_type = None
                                                        self.asic_type = None
                                                        self.rack_num = None
                                                        self.slot_num = None
                                                        self.asic_instance = None

                                                    @property
                                                    def _common_path(self):
                                                        if self.parent is None:
                                                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                                        return self.parent._common_path +'/Cisco-IOS-XR-dnx-driver-oper:asic-id'

                                                    def is_config(self):
                                                        ''' Returns True if this instance represents config data else returns False '''
                                                        return False

                                                    def _has_data(self):
                                                        if not self.is_config():
                                                            return False
                                                        if self.rack_type is not None:
                                                            return True

                                                        if self.asic_type is not None:
                                                            return True

                                                        if self.rack_num is not None:
                                                            return True

                                                        if self.slot_num is not None:
                                                            return True

                                                        if self.asic_instance is not None:
                                                            return True

                                                        return False

                                                    @staticmethod
                                                    def _meta_info():
                                                        from ydk.models.dnx._meta import _Cisco_IOS_XR_dnx_driver_oper as meta
                                                        return meta._meta_table['Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances.RxAsicInstance.RxLinks.RxLink.RxLink.ThisLink.AsicId']['meta_info']

                                                @property
                                                def _common_path(self):
                                                    if self.parent is None:
                                                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                                    return self.parent._common_path +'/Cisco-IOS-XR-dnx-driver-oper:this-link'

                                                def is_config(self):
                                                    ''' Returns True if this instance represents config data else returns False '''
                                                    return False

                                                def _has_data(self):
                                                    if not self.is_config():
                                                        return False
                                                    if self.asic_id is not None and self.asic_id._has_data():
                                                        return True

                                                    if self.link_type is not None:
                                                        return True

                                                    if self.link_stage is not None:
                                                        return True

                                                    if self.link_num is not None:
                                                        return True

                                                    if self.phy_link_num is not None:
                                                        return True

                                                    return False

                                                @staticmethod
                                                def _meta_info():
                                                    from ydk.models.dnx._meta import _Cisco_IOS_XR_dnx_driver_oper as meta
                                                    return meta._meta_table['Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances.RxAsicInstance.RxLinks.RxLink.RxLink.ThisLink']['meta_info']


                                            class FarEndLink(object):
                                                """
                                                far end link
                                                
                                                .. attribute:: asic_id
                                                
                                                	asic id
                                                	**type**\: :py:class:`AsicId <ydk.models.dnx.Cisco_IOS_XR_dnx_driver_oper.Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances.RxAsicInstance.RxLinks.RxLink.RxLink.FarEndLink.AsicId>`
                                                
                                                .. attribute:: link_type
                                                
                                                	link type
                                                	**type**\: int
                                                
                                                	**range:** 0..255
                                                
                                                .. attribute:: link_stage
                                                
                                                	link stage
                                                	**type**\: int
                                                
                                                	**range:** 0..255
                                                
                                                .. attribute:: link_num
                                                
                                                	link num
                                                	**type**\: int
                                                
                                                	**range:** 0..4294967295
                                                
                                                .. attribute:: phy_link_num
                                                
                                                	phy link num
                                                	**type**\: int
                                                
                                                	**range:** 0..4294967295
                                                
                                                

                                                """

                                                _prefix = 'dnx-driver-oper'
                                                _revision = '2015-11-09'

                                                def __init__(self):
                                                    self.parent = None
                                                    self.asic_id = Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances.RxAsicInstance.RxLinks.RxLink.RxLink.FarEndLink.AsicId()
                                                    self.asic_id.parent = self
                                                    self.link_type = None
                                                    self.link_stage = None
                                                    self.link_num = None
                                                    self.phy_link_num = None


                                                class AsicId(object):
                                                    """
                                                    asic id
                                                    
                                                    .. attribute:: rack_type
                                                    
                                                    	rack type
                                                    	**type**\: int
                                                    
                                                    	**range:** 0..4294967295
                                                    
                                                    .. attribute:: asic_type
                                                    
                                                    	asic type
                                                    	**type**\: int
                                                    
                                                    	**range:** 0..255
                                                    
                                                    .. attribute:: rack_num
                                                    
                                                    	rack num
                                                    	**type**\: int
                                                    
                                                    	**range:** 0..4294967295
                                                    
                                                    .. attribute:: slot_num
                                                    
                                                    	slot num
                                                    	**type**\: int
                                                    
                                                    	**range:** 0..4294967295
                                                    
                                                    .. attribute:: asic_instance
                                                    
                                                    	asic instance
                                                    	**type**\: int
                                                    
                                                    	**range:** 0..4294967295
                                                    
                                                    

                                                    """

                                                    _prefix = 'dnx-driver-oper'
                                                    _revision = '2015-11-09'

                                                    def __init__(self):
                                                        self.parent = None
                                                        self.rack_type = None
                                                        self.asic_type = None
                                                        self.rack_num = None
                                                        self.slot_num = None
                                                        self.asic_instance = None

                                                    @property
                                                    def _common_path(self):
                                                        if self.parent is None:
                                                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                                        return self.parent._common_path +'/Cisco-IOS-XR-dnx-driver-oper:asic-id'

                                                    def is_config(self):
                                                        ''' Returns True if this instance represents config data else returns False '''
                                                        return False

                                                    def _has_data(self):
                                                        if not self.is_config():
                                                            return False
                                                        if self.rack_type is not None:
                                                            return True

                                                        if self.asic_type is not None:
                                                            return True

                                                        if self.rack_num is not None:
                                                            return True

                                                        if self.slot_num is not None:
                                                            return True

                                                        if self.asic_instance is not None:
                                                            return True

                                                        return False

                                                    @staticmethod
                                                    def _meta_info():
                                                        from ydk.models.dnx._meta import _Cisco_IOS_XR_dnx_driver_oper as meta
                                                        return meta._meta_table['Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances.RxAsicInstance.RxLinks.RxLink.RxLink.FarEndLink.AsicId']['meta_info']

                                                @property
                                                def _common_path(self):
                                                    if self.parent is None:
                                                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                                    return self.parent._common_path +'/Cisco-IOS-XR-dnx-driver-oper:far-end-link'

                                                def is_config(self):
                                                    ''' Returns True if this instance represents config data else returns False '''
                                                    return False

                                                def _has_data(self):
                                                    if not self.is_config():
                                                        return False
                                                    if self.asic_id is not None and self.asic_id._has_data():
                                                        return True

                                                    if self.link_type is not None:
                                                        return True

                                                    if self.link_stage is not None:
                                                        return True

                                                    if self.link_num is not None:
                                                        return True

                                                    if self.phy_link_num is not None:
                                                        return True

                                                    return False

                                                @staticmethod
                                                def _meta_info():
                                                    from ydk.models.dnx._meta import _Cisco_IOS_XR_dnx_driver_oper as meta
                                                    return meta._meta_table['Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances.RxAsicInstance.RxLinks.RxLink.RxLink.FarEndLink']['meta_info']


                                            class FarEndLinkInHw(object):
                                                """
                                                far end link in hw
                                                
                                                .. attribute:: asic_id
                                                
                                                	asic id
                                                	**type**\: :py:class:`AsicId <ydk.models.dnx.Cisco_IOS_XR_dnx_driver_oper.Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances.RxAsicInstance.RxLinks.RxLink.RxLink.FarEndLinkInHw.AsicId>`
                                                
                                                .. attribute:: link_type
                                                
                                                	link type
                                                	**type**\: int
                                                
                                                	**range:** 0..255
                                                
                                                .. attribute:: link_stage
                                                
                                                	link stage
                                                	**type**\: int
                                                
                                                	**range:** 0..255
                                                
                                                .. attribute:: link_num
                                                
                                                	link num
                                                	**type**\: int
                                                
                                                	**range:** 0..4294967295
                                                
                                                .. attribute:: phy_link_num
                                                
                                                	phy link num
                                                	**type**\: int
                                                
                                                	**range:** 0..4294967295
                                                
                                                

                                                """

                                                _prefix = 'dnx-driver-oper'
                                                _revision = '2015-11-09'

                                                def __init__(self):
                                                    self.parent = None
                                                    self.asic_id = Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances.RxAsicInstance.RxLinks.RxLink.RxLink.FarEndLinkInHw.AsicId()
                                                    self.asic_id.parent = self
                                                    self.link_type = None
                                                    self.link_stage = None
                                                    self.link_num = None
                                                    self.phy_link_num = None


                                                class AsicId(object):
                                                    """
                                                    asic id
                                                    
                                                    .. attribute:: rack_type
                                                    
                                                    	rack type
                                                    	**type**\: int
                                                    
                                                    	**range:** 0..4294967295
                                                    
                                                    .. attribute:: asic_type
                                                    
                                                    	asic type
                                                    	**type**\: int
                                                    
                                                    	**range:** 0..255
                                                    
                                                    .. attribute:: rack_num
                                                    
                                                    	rack num
                                                    	**type**\: int
                                                    
                                                    	**range:** 0..4294967295
                                                    
                                                    .. attribute:: slot_num
                                                    
                                                    	slot num
                                                    	**type**\: int
                                                    
                                                    	**range:** 0..4294967295
                                                    
                                                    .. attribute:: asic_instance
                                                    
                                                    	asic instance
                                                    	**type**\: int
                                                    
                                                    	**range:** 0..4294967295
                                                    
                                                    

                                                    """

                                                    _prefix = 'dnx-driver-oper'
                                                    _revision = '2015-11-09'

                                                    def __init__(self):
                                                        self.parent = None
                                                        self.rack_type = None
                                                        self.asic_type = None
                                                        self.rack_num = None
                                                        self.slot_num = None
                                                        self.asic_instance = None

                                                    @property
                                                    def _common_path(self):
                                                        if self.parent is None:
                                                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                                        return self.parent._common_path +'/Cisco-IOS-XR-dnx-driver-oper:asic-id'

                                                    def is_config(self):
                                                        ''' Returns True if this instance represents config data else returns False '''
                                                        return False

                                                    def _has_data(self):
                                                        if not self.is_config():
                                                            return False
                                                        if self.rack_type is not None:
                                                            return True

                                                        if self.asic_type is not None:
                                                            return True

                                                        if self.rack_num is not None:
                                                            return True

                                                        if self.slot_num is not None:
                                                            return True

                                                        if self.asic_instance is not None:
                                                            return True

                                                        return False

                                                    @staticmethod
                                                    def _meta_info():
                                                        from ydk.models.dnx._meta import _Cisco_IOS_XR_dnx_driver_oper as meta
                                                        return meta._meta_table['Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances.RxAsicInstance.RxLinks.RxLink.RxLink.FarEndLinkInHw.AsicId']['meta_info']

                                                @property
                                                def _common_path(self):
                                                    if self.parent is None:
                                                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                                    return self.parent._common_path +'/Cisco-IOS-XR-dnx-driver-oper:far-end-link-in-hw'

                                                def is_config(self):
                                                    ''' Returns True if this instance represents config data else returns False '''
                                                    return False

                                                def _has_data(self):
                                                    if not self.is_config():
                                                        return False
                                                    if self.asic_id is not None and self.asic_id._has_data():
                                                        return True

                                                    if self.link_type is not None:
                                                        return True

                                                    if self.link_stage is not None:
                                                        return True

                                                    if self.link_num is not None:
                                                        return True

                                                    if self.phy_link_num is not None:
                                                        return True

                                                    return False

                                                @staticmethod
                                                def _meta_info():
                                                    from ydk.models.dnx._meta import _Cisco_IOS_XR_dnx_driver_oper as meta
                                                    return meta._meta_table['Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances.RxAsicInstance.RxLinks.RxLink.RxLink.FarEndLinkInHw']['meta_info']


                                            class History(object):
                                                """
                                                history
                                                
                                                .. attribute:: histnum
                                                
                                                	histnum
                                                	**type**\: int
                                                
                                                	**range:** 0..255
                                                
                                                .. attribute:: start_index
                                                
                                                	start index
                                                	**type**\: int
                                                
                                                	**range:** 0..255
                                                
                                                .. attribute:: hist
                                                
                                                	hist
                                                	**type**\: list of :py:class:`Hist <ydk.models.dnx.Cisco_IOS_XR_dnx_driver_oper.Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances.RxAsicInstance.RxLinks.RxLink.RxLink.History.Hist>`
                                                
                                                

                                                """

                                                _prefix = 'dnx-driver-oper'
                                                _revision = '2015-11-09'

                                                def __init__(self):
                                                    self.parent = None
                                                    self.histnum = None
                                                    self.start_index = None
                                                    self.hist = YList()
                                                    self.hist.parent = self
                                                    self.hist.name = 'hist'


                                                class Hist(object):
                                                    """
                                                    hist
                                                    
                                                    .. attribute:: admin_state
                                                    
                                                    	admin state
                                                    	**type**\: int
                                                    
                                                    	**range:** \-128..127
                                                    
                                                    .. attribute:: oper_state
                                                    
                                                    	oper state
                                                    	**type**\: int
                                                    
                                                    	**range:** \-128..127
                                                    
                                                    .. attribute:: error_state
                                                    
                                                    	error state
                                                    	**type**\: int
                                                    
                                                    	**range:** \-128..127
                                                    
                                                    .. attribute:: timestamp
                                                    
                                                    	timestamp
                                                    	**type**\: int
                                                    
                                                    	**range:** 0..18446744073709551615
                                                    
                                                    .. attribute:: reasons
                                                    
                                                    	reasons
                                                    	**type**\: str
                                                    
                                                    

                                                    """

                                                    _prefix = 'dnx-driver-oper'
                                                    _revision = '2015-11-09'

                                                    def __init__(self):
                                                        self.parent = None
                                                        self.admin_state = None
                                                        self.oper_state = None
                                                        self.error_state = None
                                                        self.timestamp = None
                                                        self.reasons = None

                                                    @property
                                                    def _common_path(self):
                                                        if self.parent is None:
                                                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                                        return self.parent._common_path +'/Cisco-IOS-XR-dnx-driver-oper:hist'

                                                    def is_config(self):
                                                        ''' Returns True if this instance represents config data else returns False '''
                                                        return False

                                                    def _has_data(self):
                                                        if not self.is_config():
                                                            return False
                                                        if self.admin_state is not None:
                                                            return True

                                                        if self.oper_state is not None:
                                                            return True

                                                        if self.error_state is not None:
                                                            return True

                                                        if self.timestamp is not None:
                                                            return True

                                                        if self.reasons is not None:
                                                            return True

                                                        return False

                                                    @staticmethod
                                                    def _meta_info():
                                                        from ydk.models.dnx._meta import _Cisco_IOS_XR_dnx_driver_oper as meta
                                                        return meta._meta_table['Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances.RxAsicInstance.RxLinks.RxLink.RxLink.History.Hist']['meta_info']

                                                @property
                                                def _common_path(self):
                                                    if self.parent is None:
                                                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                                    return self.parent._common_path +'/Cisco-IOS-XR-dnx-driver-oper:history'

                                                def is_config(self):
                                                    ''' Returns True if this instance represents config data else returns False '''
                                                    return False

                                                def _has_data(self):
                                                    if not self.is_config():
                                                        return False
                                                    if self.histnum is not None:
                                                        return True

                                                    if self.start_index is not None:
                                                        return True

                                                    if self.hist is not None:
                                                        for child_ref in self.hist:
                                                            if child_ref._has_data():
                                                                return True

                                                    return False

                                                @staticmethod
                                                def _meta_info():
                                                    from ydk.models.dnx._meta import _Cisco_IOS_XR_dnx_driver_oper as meta
                                                    return meta._meta_table['Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances.RxAsicInstance.RxLinks.RxLink.RxLink.History']['meta_info']

                                            @property
                                            def _common_path(self):
                                                if self.parent is None:
                                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')
                                                if self.link is None:
                                                    raise YPYDataValidationError('Key property link is None')

                                                return self.parent._common_path +'/Cisco-IOS-XR-dnx-driver-oper:rx-link[Cisco-IOS-XR-dnx-driver-oper:link = ' + str(self.link) + ']'

                                            def is_config(self):
                                                ''' Returns True if this instance represents config data else returns False '''
                                                return False

                                            def _has_data(self):
                                                if not self.is_config():
                                                    return False
                                                if self.link is not None:
                                                    return True

                                                if self.this_link is not None and self.this_link._has_data():
                                                    return True

                                                if self.far_end_link is not None and self.far_end_link._has_data():
                                                    return True

                                                if self.far_end_link_in_hw is not None and self.far_end_link_in_hw._has_data():
                                                    return True

                                                if self.history is not None and self.history._has_data():
                                                    return True

                                                if self.speed is not None:
                                                    return True

                                                if self.stage is not None:
                                                    return True

                                                if self.is_link_valid is not None:
                                                    return True

                                                if self.is_conf_pending is not None:
                                                    return True

                                                if self.admin_state is not None:
                                                    return True

                                                if self.oper_state is not None:
                                                    return True

                                                if self.error_state is not None:
                                                    return True

                                                if self.flags is not None:
                                                    return True

                                                if self.flap_cnt is not None:
                                                    return True

                                                if self.num_admin_shuts is not None:
                                                    return True

                                                return False

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.dnx._meta import _Cisco_IOS_XR_dnx_driver_oper as meta
                                                return meta._meta_table['Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances.RxAsicInstance.RxLinks.RxLink.RxLink']['meta_info']

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/Cisco-IOS-XR-dnx-driver-oper:rx-link'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return False

                                        def _has_data(self):
                                            if not self.is_config():
                                                return False
                                            if self.start_number is not None:
                                                return True

                                            if self.end_number is not None:
                                                return True

                                            if self.status_option is not None:
                                                return True

                                            if self.rx_link is not None:
                                                for child_ref in self.rx_link:
                                                    if child_ref._has_data():
                                                        return True

                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.dnx._meta import _Cisco_IOS_XR_dnx_driver_oper as meta
                                            return meta._meta_table['Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances.RxAsicInstance.RxLinks.RxLink']['meta_info']

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-dnx-driver-oper:rx-links'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        if not self.is_config():
                                            return False
                                        if self.rx_link is not None:
                                            for child_ref in self.rx_link:
                                                if child_ref._has_data():
                                                    return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.dnx._meta import _Cisco_IOS_XR_dnx_driver_oper as meta
                                        return meta._meta_table['Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances.RxAsicInstance.RxLinks']['meta_info']

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYDataValidationError('parent is not set . Cannot derive path.')
                                    if self.instance is None:
                                        raise YPYDataValidationError('Key property instance is None')

                                    return self.parent._common_path +'/Cisco-IOS-XR-dnx-driver-oper:rx-asic-instance[Cisco-IOS-XR-dnx-driver-oper:instance = ' + str(self.instance) + ']'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.instance is not None:
                                        return True

                                    if self.rx_links is not None and self.rx_links._has_data():
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.dnx._meta import _Cisco_IOS_XR_dnx_driver_oper as meta
                                    return meta._meta_table['Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances.RxAsicInstance']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-dnx-driver-oper:rx-asic-instances'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.rx_asic_instance is not None:
                                    for child_ref in self.rx_asic_instance:
                                        if child_ref._has_data():
                                            return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.dnx._meta import _Cisco_IOS_XR_dnx_driver_oper as meta
                                return meta._meta_table['Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')
                            if self.option is None:
                                raise YPYDataValidationError('Key property option is None')

                            return self.parent._common_path +'/Cisco-IOS-XR-dnx-driver-oper:link-option[Cisco-IOS-XR-dnx-driver-oper:option = ' + str(self.option) + ']'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.option is not None:
                                return True

                            if self.rx_asic_instances is not None and self.rx_asic_instances._has_data():
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.dnx._meta import _Cisco_IOS_XR_dnx_driver_oper as meta
                            return meta._meta_table['Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-dnx-driver-oper:link-options'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.link_option is not None:
                            for child_ref in self.link_option:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.dnx._meta import _Cisco_IOS_XR_dnx_driver_oper as meta
                        return meta._meta_table['Fia.Nodes.Node.RxLinkInformation.LinkOptions']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-dnx-driver-oper:rx-link-information'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.link_options is not None and self.link_options._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.dnx._meta import _Cisco_IOS_XR_dnx_driver_oper as meta
                    return meta._meta_table['Fia.Nodes.Node.RxLinkInformation']['meta_info']


            class DriverInformation(object):
                """
                FIA driver information
                
                .. attribute:: drv_version
                
                	drv version
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: coeff_major_rev
                
                	coeff major rev
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: coeff_minor_rev
                
                	coeff minor rev
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: functional_role
                
                	functional role
                	**type**\: int
                
                	**range:** 0..255
                
                .. attribute:: issu_role
                
                	issu role
                	**type**\: int
                
                	**range:** 0..255
                
                .. attribute:: rack_name
                
                	rack name
                	**type**\: str
                
                .. attribute:: rack_type
                
                	rack type
                	**type**\: int
                
                	**range:** \-2147483648..2147483647
                
                .. attribute:: rack_num
                
                	rack num
                	**type**\: int
                
                	**range:** 0..255
                
                .. attribute:: is_driver_ready
                
                	is driver ready
                	**type**\: bool
                
                .. attribute:: card_avail_mask
                
                	card avail mask
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: asic_avail_mask
                
                	asic avail mask
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: exp_asic_avail_mask
                
                	exp asic avail mask
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: ucmc_ratio
                
                	ucmc ratio
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: asic_oper_notify_to_fsdb_pending_bmap
                
                	asic oper notify to fsdb pending bmap
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: is_full_fgid_download_req
                
                	is full fgid download req
                	**type**\: bool
                
                .. attribute:: is_fgid_download_in_progress
                
                	is fgid download in progress
                	**type**\: bool
                
                .. attribute:: is_fgid_download_completed
                
                	is fgid download completed
                	**type**\: bool
                
                .. attribute:: fsdb_conn_active
                
                	fsdb conn active
                	**type**\: bool
                
                .. attribute:: fgid_conn_active
                
                	fgid conn active
                	**type**\: bool
                
                .. attribute:: issu_mgr_conn_active
                
                	issu mgr conn active
                	**type**\: bool
                
                .. attribute:: fsdb_reg_active
                
                	fsdb reg active
                	**type**\: bool
                
                .. attribute:: fgid_reg_active
                
                	fgid reg active
                	**type**\: bool
                
                .. attribute:: issu_mgr_reg_active
                
                	issu mgr reg active
                	**type**\: bool
                
                .. attribute:: num_pm_conn_reqs
                
                	num pm conn reqs
                	**type**\: int
                
                	**range:** 0..255
                
                .. attribute:: num_fsdb_conn_reqs
                
                	num fsdb conn reqs
                	**type**\: int
                
                	**range:** 0..255
                
                .. attribute:: num_fgid_conn_reqs
                
                	num fgid conn reqs
                	**type**\: int
                
                	**range:** 0..255
                
                .. attribute:: num_fstats_conn_reqs
                
                	num fstats conn reqs
                	**type**\: int
                
                	**range:** 0..255
                
                .. attribute:: num_cm_conn_reqs
                
                	num cm conn reqs
                	**type**\: int
                
                	**range:** 0..255
                
                .. attribute:: num_issu_mgr_conn_reqs
                
                	num issu mgr conn reqs
                	**type**\: int
                
                	**range:** 0..255
                
                .. attribute:: num_peer_fia_conn_reqs
                
                	num peer fia conn reqs
                	**type**\: int
                
                	**range:** 0..255
                
                .. attribute:: is_gaspp_registered
                
                	is gaspp registered
                	**type**\: bool
                
                .. attribute:: is_cih_registered
                
                	is cih registered
                	**type**\: bool
                
                .. attribute:: offset_time_nsec
                
                	offset time nsec
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: drvr_startup_timestamp
                
                	drvr startup timestamp
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: num_intf_ports
                
                	num intf ports
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: uc_weight
                
                	uc weight
                	**type**\: int
                
                	**range:** 0..255
                
                .. attribute:: respawn_count
                
                	respawn count
                	**type**\: int
                
                	**range:** 0..255
                
                .. attribute:: total_asics
                
                	total asics
                	**type**\: int
                
                	**range:** 0..255
                
                .. attribute:: issu_ready_ntfy_pending
                
                	issu ready ntfy pending
                	**type**\: bool
                
                .. attribute:: issu_abort_sent
                
                	issu abort sent
                	**type**\: bool
                
                .. attribute:: issu_abort_rcvd
                
                	issu abort rcvd
                	**type**\: bool
                
                .. attribute:: fc_mode
                
                	fc mode
                	**type**\: int
                
                	**range:** 0..255
                
                .. attribute:: board_rev_id
                
                	board rev id
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: device_info
                
                	device info
                	**type**\: list of :py:class:`DeviceInfo <ydk.models.dnx.Cisco_IOS_XR_dnx_driver_oper.Fia.Nodes.Node.DriverInformation.DeviceInfo>`
                
                .. attribute:: card_info
                
                	card info
                	**type**\: list of :py:class:`CardInfo <ydk.models.dnx.Cisco_IOS_XR_dnx_driver_oper.Fia.Nodes.Node.DriverInformation.CardInfo>`
                
                

                """

                _prefix = 'dnx-driver-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.drv_version = None
                    self.coeff_major_rev = None
                    self.coeff_minor_rev = None
                    self.functional_role = None
                    self.issu_role = None
                    self.rack_name = None
                    self.rack_type = None
                    self.rack_num = None
                    self.is_driver_ready = None
                    self.card_avail_mask = None
                    self.asic_avail_mask = None
                    self.exp_asic_avail_mask = None
                    self.ucmc_ratio = None
                    self.asic_oper_notify_to_fsdb_pending_bmap = None
                    self.is_full_fgid_download_req = None
                    self.is_fgid_download_in_progress = None
                    self.is_fgid_download_completed = None
                    self.fsdb_conn_active = None
                    self.fgid_conn_active = None
                    self.issu_mgr_conn_active = None
                    self.fsdb_reg_active = None
                    self.fgid_reg_active = None
                    self.issu_mgr_reg_active = None
                    self.num_pm_conn_reqs = None
                    self.num_fsdb_conn_reqs = None
                    self.num_fgid_conn_reqs = None
                    self.num_fstats_conn_reqs = None
                    self.num_cm_conn_reqs = None
                    self.num_issu_mgr_conn_reqs = None
                    self.num_peer_fia_conn_reqs = None
                    self.is_gaspp_registered = None
                    self.is_cih_registered = None
                    self.offset_time_nsec = None
                    self.drvr_startup_timestamp = None
                    self.num_intf_ports = None
                    self.uc_weight = None
                    self.respawn_count = None
                    self.total_asics = None
                    self.issu_ready_ntfy_pending = None
                    self.issu_abort_sent = None
                    self.issu_abort_rcvd = None
                    self.fc_mode = None
                    self.board_rev_id = None
                    self.device_info = YList()
                    self.device_info.parent = self
                    self.device_info.name = 'device_info'
                    self.card_info = YList()
                    self.card_info.parent = self
                    self.card_info.name = 'card_info'


                class DeviceInfo(object):
                    """
                    device info
                    
                    .. attribute:: asic_id
                    
                    	asic id
                    	**type**\: :py:class:`AsicId <ydk.models.dnx.Cisco_IOS_XR_dnx_driver_oper.Fia.Nodes.Node.DriverInformation.DeviceInfo.AsicId>`
                    
                    .. attribute:: is_valid
                    
                    	is valid
                    	**type**\: bool
                    
                    .. attribute:: fapid
                    
                    	fapid
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: hotplug_event
                    
                    	hotplug event
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: slice_state
                    
                    	slice state
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: admin_state
                    
                    	admin state
                    	**type**\: int
                    
                    	**range:** 0..255
                    
                    .. attribute:: oper_state
                    
                    	oper state
                    	**type**\: int
                    
                    	**range:** 0..255
                    
                    .. attribute:: asic_state
                    
                    	asic state
                    	**type**\: int
                    
                    	**range:** 0..255
                    
                    .. attribute:: last_init_cause
                    
                    	last init cause
                    	**type**\: int
                    
                    	**range:** 0..255
                    
                    .. attribute:: num_pon_resets
                    
                    	num pon resets
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: num_hard_resets
                    
                    	num hard resets
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: last_pon_reset_timestamp
                    
                    	last pon reset timestamp
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: last_hard_reset_timestamp
                    
                    	last hard reset timestamp
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: local_switch_state
                    
                    	local switch state
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'dnx-driver-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.asic_id = Fia.Nodes.Node.DriverInformation.DeviceInfo.AsicId()
                        self.asic_id.parent = self
                        self.is_valid = None
                        self.fapid = None
                        self.hotplug_event = None
                        self.slice_state = None
                        self.admin_state = None
                        self.oper_state = None
                        self.asic_state = None
                        self.last_init_cause = None
                        self.num_pon_resets = None
                        self.num_hard_resets = None
                        self.last_pon_reset_timestamp = None
                        self.last_hard_reset_timestamp = None
                        self.local_switch_state = None


                    class AsicId(object):
                        """
                        asic id
                        
                        .. attribute:: rack_type
                        
                        	rack type
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: asic_type
                        
                        	asic type
                        	**type**\: int
                        
                        	**range:** 0..255
                        
                        .. attribute:: rack_num
                        
                        	rack num
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: slot_num
                        
                        	slot num
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: asic_instance
                        
                        	asic instance
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'dnx-driver-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.rack_type = None
                            self.asic_type = None
                            self.rack_num = None
                            self.slot_num = None
                            self.asic_instance = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-dnx-driver-oper:asic-id'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.rack_type is not None:
                                return True

                            if self.asic_type is not None:
                                return True

                            if self.rack_num is not None:
                                return True

                            if self.slot_num is not None:
                                return True

                            if self.asic_instance is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.dnx._meta import _Cisco_IOS_XR_dnx_driver_oper as meta
                            return meta._meta_table['Fia.Nodes.Node.DriverInformation.DeviceInfo.AsicId']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-dnx-driver-oper:device-info'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.asic_id is not None and self.asic_id._has_data():
                            return True

                        if self.is_valid is not None:
                            return True

                        if self.fapid is not None:
                            return True

                        if self.hotplug_event is not None:
                            return True

                        if self.slice_state is not None:
                            return True

                        if self.admin_state is not None:
                            return True

                        if self.oper_state is not None:
                            return True

                        if self.asic_state is not None:
                            return True

                        if self.last_init_cause is not None:
                            return True

                        if self.num_pon_resets is not None:
                            return True

                        if self.num_hard_resets is not None:
                            return True

                        if self.last_pon_reset_timestamp is not None:
                            return True

                        if self.last_hard_reset_timestamp is not None:
                            return True

                        if self.local_switch_state is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.dnx._meta import _Cisco_IOS_XR_dnx_driver_oper as meta
                        return meta._meta_table['Fia.Nodes.Node.DriverInformation.DeviceInfo']['meta_info']


                class CardInfo(object):
                    """
                    card info
                    
                    .. attribute:: oir_circular_buffer
                    
                    	oir circular buffer
                    	**type**\: :py:class:`OirCircularBuffer <ydk.models.dnx.Cisco_IOS_XR_dnx_driver_oper.Fia.Nodes.Node.DriverInformation.CardInfo.OirCircularBuffer>`
                    
                    .. attribute:: card_type
                    
                    	card type
                    	**type**\: int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: card_name
                    
                    	card name
                    	**type**\: str
                    
                    .. attribute:: slot_no
                    
                    	slot no
                    	**type**\: int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: card_flag
                    
                    	card flag
                    	**type**\: int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: evt_flag
                    
                    	evt flag
                    	**type**\: int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: reg_flag
                    
                    	reg flag
                    	**type**\: int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: instance
                    
                    	instance
                    	**type**\: int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: card_state
                    
                    	card state
                    	**type**\: int
                    
                    	**range:** 0..255
                    
                    .. attribute:: exp_num_asics
                    
                    	exp num asics
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: exp_num_asics_per_fsdb
                    
                    	exp num asics per fsdb
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: is_powered
                    
                    	is powered
                    	**type**\: bool
                    
                    .. attribute:: cxp_avail_bitmap
                    
                    	cxp avail bitmap
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: num_ilkns_per_asic
                    
                    	num ilkns per asic
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: num_local_ports_per_ilkn
                    
                    	num local ports per ilkn
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: num_cos_per_port
                    
                    	num cos per port
                    	**type**\: int
                    
                    	**range:** 0..255
                    
                    

                    """

                    _prefix = 'dnx-driver-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.oir_circular_buffer = Fia.Nodes.Node.DriverInformation.CardInfo.OirCircularBuffer()
                        self.oir_circular_buffer.parent = self
                        self.card_type = None
                        self.card_name = None
                        self.slot_no = None
                        self.card_flag = None
                        self.evt_flag = None
                        self.reg_flag = None
                        self.instance = None
                        self.card_state = None
                        self.exp_num_asics = None
                        self.exp_num_asics_per_fsdb = None
                        self.is_powered = None
                        self.cxp_avail_bitmap = None
                        self.num_ilkns_per_asic = None
                        self.num_local_ports_per_ilkn = None
                        self.num_cos_per_port = None


                    class OirCircularBuffer(object):
                        """
                        oir circular buffer
                        
                        .. attribute:: count
                        
                        	count
                        	**type**\: int
                        
                        	**range:** \-2147483648..2147483647
                        
                        .. attribute:: start
                        
                        	start
                        	**type**\: int
                        
                        	**range:** \-2147483648..2147483647
                        
                        .. attribute:: end
                        
                        	end
                        	**type**\: int
                        
                        	**range:** \-2147483648..2147483647
                        
                        .. attribute:: fia_oir_info
                        
                        	fia oir info
                        	**type**\: list of :py:class:`FiaOirInfo <ydk.models.dnx.Cisco_IOS_XR_dnx_driver_oper.Fia.Nodes.Node.DriverInformation.CardInfo.OirCircularBuffer.FiaOirInfo>`
                        
                        

                        """

                        _prefix = 'dnx-driver-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.count = None
                            self.start = None
                            self.end = None
                            self.fia_oir_info = YList()
                            self.fia_oir_info.parent = self
                            self.fia_oir_info.name = 'fia_oir_info'


                        class FiaOirInfo(object):
                            """
                            fia oir info
                            
                            .. attribute:: card_flag
                            
                            	card flag
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: card_type
                            
                            	card type
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: reg_flag
                            
                            	reg flag
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: evt_flag
                            
                            	evt flag
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: rack_num
                            
                            	rack num
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: instance
                            
                            	instance
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: cur_card_state
                            
                            	cur card state
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            

                            """

                            _prefix = 'dnx-driver-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.card_flag = None
                                self.card_type = None
                                self.reg_flag = None
                                self.evt_flag = None
                                self.rack_num = None
                                self.instance = None
                                self.cur_card_state = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-dnx-driver-oper:fia-oir-info'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.card_flag is not None:
                                    return True

                                if self.card_type is not None:
                                    return True

                                if self.reg_flag is not None:
                                    return True

                                if self.evt_flag is not None:
                                    return True

                                if self.rack_num is not None:
                                    return True

                                if self.instance is not None:
                                    return True

                                if self.cur_card_state is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.dnx._meta import _Cisco_IOS_XR_dnx_driver_oper as meta
                                return meta._meta_table['Fia.Nodes.Node.DriverInformation.CardInfo.OirCircularBuffer.FiaOirInfo']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-dnx-driver-oper:oir-circular-buffer'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.count is not None:
                                return True

                            if self.start is not None:
                                return True

                            if self.end is not None:
                                return True

                            if self.fia_oir_info is not None:
                                for child_ref in self.fia_oir_info:
                                    if child_ref._has_data():
                                        return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.dnx._meta import _Cisco_IOS_XR_dnx_driver_oper as meta
                            return meta._meta_table['Fia.Nodes.Node.DriverInformation.CardInfo.OirCircularBuffer']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-dnx-driver-oper:card-info'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.oir_circular_buffer is not None and self.oir_circular_buffer._has_data():
                            return True

                        if self.card_type is not None:
                            return True

                        if self.card_name is not None:
                            return True

                        if self.slot_no is not None:
                            return True

                        if self.card_flag is not None:
                            return True

                        if self.evt_flag is not None:
                            return True

                        if self.reg_flag is not None:
                            return True

                        if self.instance is not None:
                            return True

                        if self.card_state is not None:
                            return True

                        if self.exp_num_asics is not None:
                            return True

                        if self.exp_num_asics_per_fsdb is not None:
                            return True

                        if self.is_powered is not None:
                            return True

                        if self.cxp_avail_bitmap is not None:
                            return True

                        if self.num_ilkns_per_asic is not None:
                            return True

                        if self.num_local_ports_per_ilkn is not None:
                            return True

                        if self.num_cos_per_port is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.dnx._meta import _Cisco_IOS_XR_dnx_driver_oper as meta
                        return meta._meta_table['Fia.Nodes.Node.DriverInformation.CardInfo']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-dnx-driver-oper:driver-information'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.drv_version is not None:
                        return True

                    if self.coeff_major_rev is not None:
                        return True

                    if self.coeff_minor_rev is not None:
                        return True

                    if self.functional_role is not None:
                        return True

                    if self.issu_role is not None:
                        return True

                    if self.rack_name is not None:
                        return True

                    if self.rack_type is not None:
                        return True

                    if self.rack_num is not None:
                        return True

                    if self.is_driver_ready is not None:
                        return True

                    if self.card_avail_mask is not None:
                        return True

                    if self.asic_avail_mask is not None:
                        return True

                    if self.exp_asic_avail_mask is not None:
                        return True

                    if self.ucmc_ratio is not None:
                        return True

                    if self.asic_oper_notify_to_fsdb_pending_bmap is not None:
                        return True

                    if self.is_full_fgid_download_req is not None:
                        return True

                    if self.is_fgid_download_in_progress is not None:
                        return True

                    if self.is_fgid_download_completed is not None:
                        return True

                    if self.fsdb_conn_active is not None:
                        return True

                    if self.fgid_conn_active is not None:
                        return True

                    if self.issu_mgr_conn_active is not None:
                        return True

                    if self.fsdb_reg_active is not None:
                        return True

                    if self.fgid_reg_active is not None:
                        return True

                    if self.issu_mgr_reg_active is not None:
                        return True

                    if self.num_pm_conn_reqs is not None:
                        return True

                    if self.num_fsdb_conn_reqs is not None:
                        return True

                    if self.num_fgid_conn_reqs is not None:
                        return True

                    if self.num_fstats_conn_reqs is not None:
                        return True

                    if self.num_cm_conn_reqs is not None:
                        return True

                    if self.num_issu_mgr_conn_reqs is not None:
                        return True

                    if self.num_peer_fia_conn_reqs is not None:
                        return True

                    if self.is_gaspp_registered is not None:
                        return True

                    if self.is_cih_registered is not None:
                        return True

                    if self.offset_time_nsec is not None:
                        return True

                    if self.drvr_startup_timestamp is not None:
                        return True

                    if self.num_intf_ports is not None:
                        return True

                    if self.uc_weight is not None:
                        return True

                    if self.respawn_count is not None:
                        return True

                    if self.total_asics is not None:
                        return True

                    if self.issu_ready_ntfy_pending is not None:
                        return True

                    if self.issu_abort_sent is not None:
                        return True

                    if self.issu_abort_rcvd is not None:
                        return True

                    if self.fc_mode is not None:
                        return True

                    if self.board_rev_id is not None:
                        return True

                    if self.device_info is not None:
                        for child_ref in self.device_info:
                            if child_ref._has_data():
                                return True

                    if self.card_info is not None:
                        for child_ref in self.card_info:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.dnx._meta import _Cisco_IOS_XR_dnx_driver_oper as meta
                    return meta._meta_table['Fia.Nodes.Node.DriverInformation']['meta_info']


            class ClearStatistics(object):
                """
                Clear statistics information
                
                .. attribute:: asic_instances
                
                	Instance table for clear statistics information
                	**type**\: :py:class:`AsicInstances <ydk.models.dnx.Cisco_IOS_XR_dnx_driver_oper.Fia.Nodes.Node.ClearStatistics.AsicInstances>`
                
                

                """

                _prefix = 'dnx-driver-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.asic_instances = Fia.Nodes.Node.ClearStatistics.AsicInstances()
                    self.asic_instances.parent = self


                class AsicInstances(object):
                    """
                    Instance table for clear statistics
                    information
                    
                    .. attribute:: asic_instance
                    
                    	Asic instance to be cleared
                    	**type**\: list of :py:class:`AsicInstance <ydk.models.dnx.Cisco_IOS_XR_dnx_driver_oper.Fia.Nodes.Node.ClearStatistics.AsicInstances.AsicInstance>`
                    
                    

                    """

                    _prefix = 'dnx-driver-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.asic_instance = YList()
                        self.asic_instance.parent = self
                        self.asic_instance.name = 'asic_instance'


                    class AsicInstance(object):
                        """
                        Asic instance to be cleared
                        
                        .. attribute:: asic_instance  <key>
                        
                        	Asic instance
                        	**type**\: int
                        
                        	**range:** 0..16
                        
                        .. attribute:: instance
                        
                        	Clear value
                        	**type**\: int
                        
                        	**range:** \-2147483648..2147483647
                        
                        

                        """

                        _prefix = 'dnx-driver-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.asic_instance = None
                            self.instance = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')
                            if self.asic_instance is None:
                                raise YPYDataValidationError('Key property asic_instance is None')

                            return self.parent._common_path +'/Cisco-IOS-XR-dnx-driver-oper:asic-instance[Cisco-IOS-XR-dnx-driver-oper:asic-instance = ' + str(self.asic_instance) + ']'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.asic_instance is not None:
                                return True

                            if self.instance is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.dnx._meta import _Cisco_IOS_XR_dnx_driver_oper as meta
                            return meta._meta_table['Fia.Nodes.Node.ClearStatistics.AsicInstances.AsicInstance']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-dnx-driver-oper:asic-instances'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.asic_instance is not None:
                            for child_ref in self.asic_instance:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.dnx._meta import _Cisco_IOS_XR_dnx_driver_oper as meta
                        return meta._meta_table['Fia.Nodes.Node.ClearStatistics.AsicInstances']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-dnx-driver-oper:clear-statistics'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.asic_instances is not None and self.asic_instances._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.dnx._meta import _Cisco_IOS_XR_dnx_driver_oper as meta
                    return meta._meta_table['Fia.Nodes.Node.ClearStatistics']['meta_info']


            class TxLinkInformation(object):
                """
                FIA link TX information
                
                .. attribute:: tx_status_option_table
                
                	Link table for tx information
                	**type**\: :py:class:`TxStatusOptionTable <ydk.models.dnx.Cisco_IOS_XR_dnx_driver_oper.Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable>`
                
                

                """

                _prefix = 'dnx-driver-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.tx_status_option_table = Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable()
                    self.tx_status_option_table.parent = self


                class TxStatusOptionTable(object):
                    """
                    Link table for tx information
                    
                    .. attribute:: tx_status_option
                    
                    	Option\: data, ctrl, all\- for now none
                    	**type**\: :py:class:`TxStatusOption <ydk.models.dnx.Cisco_IOS_XR_dnx_driver_oper.Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable.TxStatusOption>`
                    
                    

                    """

                    _prefix = 'dnx-driver-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.tx_status_option = Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable.TxStatusOption()
                        self.tx_status_option.parent = self


                    class TxStatusOption(object):
                        """
                        Option\: data, ctrl, all\- for now none
                        
                        .. attribute:: tx_asic_instances
                        
                        	Instance table for tx information
                        	**type**\: :py:class:`TxAsicInstances <ydk.models.dnx.Cisco_IOS_XR_dnx_driver_oper.Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable.TxStatusOption.TxAsicInstances>`
                        
                        

                        """

                        _prefix = 'dnx-driver-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.tx_asic_instances = Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable.TxStatusOption.TxAsicInstances()
                            self.tx_asic_instances.parent = self


                        class TxAsicInstances(object):
                            """
                            Instance table for tx information
                            
                            .. attribute:: tx_asic_instance
                            
                            	Instance number for tx link information
                            	**type**\: list of :py:class:`TxAsicInstance <ydk.models.dnx.Cisco_IOS_XR_dnx_driver_oper.Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable.TxStatusOption.TxAsicInstances.TxAsicInstance>`
                            
                            

                            """

                            _prefix = 'dnx-driver-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.tx_asic_instance = YList()
                                self.tx_asic_instance.parent = self
                                self.tx_asic_instance.name = 'tx_asic_instance'


                            class TxAsicInstance(object):
                                """
                                Instance number for tx link information
                                
                                .. attribute:: instance  <key>
                                
                                	Transmit instance
                                	**type**\: int
                                
                                	**range:** 0..16
                                
                                .. attribute:: tx_links
                                
                                	Link table for tx information
                                	**type**\: :py:class:`TxLinks <ydk.models.dnx.Cisco_IOS_XR_dnx_driver_oper.Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable.TxStatusOption.TxAsicInstances.TxAsicInstance.TxLinks>`
                                
                                

                                """

                                _prefix = 'dnx-driver-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.instance = None
                                    self.tx_links = Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable.TxStatusOption.TxAsicInstances.TxAsicInstance.TxLinks()
                                    self.tx_links.parent = self


                                class TxLinks(object):
                                    """
                                    Link table for tx information
                                    
                                    .. attribute:: tx_link
                                    
                                    	Link number for tx link information
                                    	**type**\: list of :py:class:`TxLink <ydk.models.dnx.Cisco_IOS_XR_dnx_driver_oper.Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable.TxStatusOption.TxAsicInstances.TxAsicInstance.TxLinks.TxLink>`
                                    
                                    

                                    """

                                    _prefix = 'dnx-driver-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.tx_link = YList()
                                        self.tx_link.parent = self
                                        self.tx_link.name = 'tx_link'


                                    class TxLink(object):
                                        """
                                        Link number for tx link information
                                        
                                        .. attribute:: start_number
                                        
                                        	Start number
                                        	**type**\: int
                                        
                                        	**range:** 0..35
                                        
                                        .. attribute:: end_number
                                        
                                        	End number
                                        	**type**\: int
                                        
                                        	**range:** 0..35
                                        
                                        .. attribute:: tx_link
                                        
                                        	Single link information
                                        	**type**\: list of :py:class:`TxLink <ydk.models.dnx.Cisco_IOS_XR_dnx_driver_oper.Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable.TxStatusOption.TxAsicInstances.TxAsicInstance.TxLinks.TxLink.TxLink>`
                                        
                                        

                                        """

                                        _prefix = 'dnx-driver-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            self.parent = None
                                            self.start_number = None
                                            self.end_number = None
                                            self.tx_link = YList()
                                            self.tx_link.parent = self
                                            self.tx_link.name = 'tx_link'


                                        class TxLink(object):
                                            """
                                            Single link information
                                            
                                            .. attribute:: link  <key>
                                            
                                            	Single Link
                                            	**type**\: int
                                            
                                            	**range:** \-2147483648..2147483647
                                            
                                            .. attribute:: this_link
                                            
                                            	this link
                                            	**type**\: :py:class:`ThisLink <ydk.models.dnx.Cisco_IOS_XR_dnx_driver_oper.Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable.TxStatusOption.TxAsicInstances.TxAsicInstance.TxLinks.TxLink.TxLink.ThisLink>`
                                            
                                            .. attribute:: far_end_link
                                            
                                            	far end link
                                            	**type**\: :py:class:`FarEndLink <ydk.models.dnx.Cisco_IOS_XR_dnx_driver_oper.Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable.TxStatusOption.TxAsicInstances.TxAsicInstance.TxLinks.TxLink.TxLink.FarEndLink>`
                                            
                                            .. attribute:: stats
                                            
                                            	stats
                                            	**type**\: :py:class:`Stats <ydk.models.dnx.Cisco_IOS_XR_dnx_driver_oper.Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable.TxStatusOption.TxAsicInstances.TxAsicInstance.TxLinks.TxLink.TxLink.Stats>`
                                            
                                            .. attribute:: history
                                            
                                            	history
                                            	**type**\: :py:class:`History <ydk.models.dnx.Cisco_IOS_XR_dnx_driver_oper.Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable.TxStatusOption.TxAsicInstances.TxAsicInstance.TxLinks.TxLink.TxLink.History>`
                                            
                                            .. attribute:: speed
                                            
                                            	speed
                                            	**type**\: int
                                            
                                            	**range:** 0..4294967295
                                            
                                            .. attribute:: stage
                                            
                                            	stage
                                            	**type**\: int
                                            
                                            	**range:** 0..255
                                            
                                            .. attribute:: is_link_valid
                                            
                                            	is link valid
                                            	**type**\: bool
                                            
                                            .. attribute:: is_conf_pending
                                            
                                            	is conf pending
                                            	**type**\: bool
                                            
                                            .. attribute:: is_power_enabled
                                            
                                            	is power enabled
                                            	**type**\: bool
                                            
                                            .. attribute:: coeff1
                                            
                                            	coeff1
                                            	**type**\: int
                                            
                                            	**range:** 0..4294967295
                                            
                                            .. attribute:: coeff2
                                            
                                            	coeff2
                                            	**type**\: int
                                            
                                            	**range:** 0..4294967295
                                            
                                            .. attribute:: admin_state
                                            
                                            	admin state
                                            	**type**\: int
                                            
                                            	**range:** 0..255
                                            
                                            .. attribute:: oper_state
                                            
                                            	oper state
                                            	**type**\: int
                                            
                                            	**range:** 0..255
                                            
                                            .. attribute:: error_state
                                            
                                            	error state
                                            	**type**\: int
                                            
                                            	**range:** 0..255
                                            
                                            .. attribute:: num_admin_shuts
                                            
                                            	num admin shuts
                                            	**type**\: int
                                            
                                            	**range:** 0..4294967295
                                            
                                            

                                            """

                                            _prefix = 'dnx-driver-oper'
                                            _revision = '2015-11-09'

                                            def __init__(self):
                                                self.parent = None
                                                self.link = None
                                                self.this_link = Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable.TxStatusOption.TxAsicInstances.TxAsicInstance.TxLinks.TxLink.TxLink.ThisLink()
                                                self.this_link.parent = self
                                                self.far_end_link = Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable.TxStatusOption.TxAsicInstances.TxAsicInstance.TxLinks.TxLink.TxLink.FarEndLink()
                                                self.far_end_link.parent = self
                                                self.stats = Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable.TxStatusOption.TxAsicInstances.TxAsicInstance.TxLinks.TxLink.TxLink.Stats()
                                                self.stats.parent = self
                                                self.history = Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable.TxStatusOption.TxAsicInstances.TxAsicInstance.TxLinks.TxLink.TxLink.History()
                                                self.history.parent = self
                                                self.speed = None
                                                self.stage = None
                                                self.is_link_valid = None
                                                self.is_conf_pending = None
                                                self.is_power_enabled = None
                                                self.coeff1 = None
                                                self.coeff2 = None
                                                self.admin_state = None
                                                self.oper_state = None
                                                self.error_state = None
                                                self.num_admin_shuts = None


                                            class ThisLink(object):
                                                """
                                                this link
                                                
                                                .. attribute:: asic_id
                                                
                                                	asic id
                                                	**type**\: :py:class:`AsicId <ydk.models.dnx.Cisco_IOS_XR_dnx_driver_oper.Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable.TxStatusOption.TxAsicInstances.TxAsicInstance.TxLinks.TxLink.TxLink.ThisLink.AsicId>`
                                                
                                                .. attribute:: link_type
                                                
                                                	link type
                                                	**type**\: int
                                                
                                                	**range:** 0..255
                                                
                                                .. attribute:: link_stage
                                                
                                                	link stage
                                                	**type**\: int
                                                
                                                	**range:** 0..255
                                                
                                                .. attribute:: link_num
                                                
                                                	link num
                                                	**type**\: int
                                                
                                                	**range:** 0..4294967295
                                                
                                                .. attribute:: phy_link_num
                                                
                                                	phy link num
                                                	**type**\: int
                                                
                                                	**range:** 0..4294967295
                                                
                                                

                                                """

                                                _prefix = 'dnx-driver-oper'
                                                _revision = '2015-11-09'

                                                def __init__(self):
                                                    self.parent = None
                                                    self.asic_id = Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable.TxStatusOption.TxAsicInstances.TxAsicInstance.TxLinks.TxLink.TxLink.ThisLink.AsicId()
                                                    self.asic_id.parent = self
                                                    self.link_type = None
                                                    self.link_stage = None
                                                    self.link_num = None
                                                    self.phy_link_num = None


                                                class AsicId(object):
                                                    """
                                                    asic id
                                                    
                                                    .. attribute:: rack_type
                                                    
                                                    	rack type
                                                    	**type**\: int
                                                    
                                                    	**range:** 0..4294967295
                                                    
                                                    .. attribute:: asic_type
                                                    
                                                    	asic type
                                                    	**type**\: int
                                                    
                                                    	**range:** 0..255
                                                    
                                                    .. attribute:: rack_num
                                                    
                                                    	rack num
                                                    	**type**\: int
                                                    
                                                    	**range:** 0..4294967295
                                                    
                                                    .. attribute:: slot_num
                                                    
                                                    	slot num
                                                    	**type**\: int
                                                    
                                                    	**range:** 0..4294967295
                                                    
                                                    .. attribute:: asic_instance
                                                    
                                                    	asic instance
                                                    	**type**\: int
                                                    
                                                    	**range:** 0..4294967295
                                                    
                                                    

                                                    """

                                                    _prefix = 'dnx-driver-oper'
                                                    _revision = '2015-11-09'

                                                    def __init__(self):
                                                        self.parent = None
                                                        self.rack_type = None
                                                        self.asic_type = None
                                                        self.rack_num = None
                                                        self.slot_num = None
                                                        self.asic_instance = None

                                                    @property
                                                    def _common_path(self):
                                                        if self.parent is None:
                                                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                                        return self.parent._common_path +'/Cisco-IOS-XR-dnx-driver-oper:asic-id'

                                                    def is_config(self):
                                                        ''' Returns True if this instance represents config data else returns False '''
                                                        return False

                                                    def _has_data(self):
                                                        if not self.is_config():
                                                            return False
                                                        if self.rack_type is not None:
                                                            return True

                                                        if self.asic_type is not None:
                                                            return True

                                                        if self.rack_num is not None:
                                                            return True

                                                        if self.slot_num is not None:
                                                            return True

                                                        if self.asic_instance is not None:
                                                            return True

                                                        return False

                                                    @staticmethod
                                                    def _meta_info():
                                                        from ydk.models.dnx._meta import _Cisco_IOS_XR_dnx_driver_oper as meta
                                                        return meta._meta_table['Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable.TxStatusOption.TxAsicInstances.TxAsicInstance.TxLinks.TxLink.TxLink.ThisLink.AsicId']['meta_info']

                                                @property
                                                def _common_path(self):
                                                    if self.parent is None:
                                                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                                    return self.parent._common_path +'/Cisco-IOS-XR-dnx-driver-oper:this-link'

                                                def is_config(self):
                                                    ''' Returns True if this instance represents config data else returns False '''
                                                    return False

                                                def _has_data(self):
                                                    if not self.is_config():
                                                        return False
                                                    if self.asic_id is not None and self.asic_id._has_data():
                                                        return True

                                                    if self.link_type is not None:
                                                        return True

                                                    if self.link_stage is not None:
                                                        return True

                                                    if self.link_num is not None:
                                                        return True

                                                    if self.phy_link_num is not None:
                                                        return True

                                                    return False

                                                @staticmethod
                                                def _meta_info():
                                                    from ydk.models.dnx._meta import _Cisco_IOS_XR_dnx_driver_oper as meta
                                                    return meta._meta_table['Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable.TxStatusOption.TxAsicInstances.TxAsicInstance.TxLinks.TxLink.TxLink.ThisLink']['meta_info']


                                            class FarEndLink(object):
                                                """
                                                far end link
                                                
                                                .. attribute:: asic_id
                                                
                                                	asic id
                                                	**type**\: :py:class:`AsicId <ydk.models.dnx.Cisco_IOS_XR_dnx_driver_oper.Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable.TxStatusOption.TxAsicInstances.TxAsicInstance.TxLinks.TxLink.TxLink.FarEndLink.AsicId>`
                                                
                                                .. attribute:: link_type
                                                
                                                	link type
                                                	**type**\: int
                                                
                                                	**range:** 0..255
                                                
                                                .. attribute:: link_stage
                                                
                                                	link stage
                                                	**type**\: int
                                                
                                                	**range:** 0..255
                                                
                                                .. attribute:: link_num
                                                
                                                	link num
                                                	**type**\: int
                                                
                                                	**range:** 0..4294967295
                                                
                                                .. attribute:: phy_link_num
                                                
                                                	phy link num
                                                	**type**\: int
                                                
                                                	**range:** 0..4294967295
                                                
                                                

                                                """

                                                _prefix = 'dnx-driver-oper'
                                                _revision = '2015-11-09'

                                                def __init__(self):
                                                    self.parent = None
                                                    self.asic_id = Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable.TxStatusOption.TxAsicInstances.TxAsicInstance.TxLinks.TxLink.TxLink.FarEndLink.AsicId()
                                                    self.asic_id.parent = self
                                                    self.link_type = None
                                                    self.link_stage = None
                                                    self.link_num = None
                                                    self.phy_link_num = None


                                                class AsicId(object):
                                                    """
                                                    asic id
                                                    
                                                    .. attribute:: rack_type
                                                    
                                                    	rack type
                                                    	**type**\: int
                                                    
                                                    	**range:** 0..4294967295
                                                    
                                                    .. attribute:: asic_type
                                                    
                                                    	asic type
                                                    	**type**\: int
                                                    
                                                    	**range:** 0..255
                                                    
                                                    .. attribute:: rack_num
                                                    
                                                    	rack num
                                                    	**type**\: int
                                                    
                                                    	**range:** 0..4294967295
                                                    
                                                    .. attribute:: slot_num
                                                    
                                                    	slot num
                                                    	**type**\: int
                                                    
                                                    	**range:** 0..4294967295
                                                    
                                                    .. attribute:: asic_instance
                                                    
                                                    	asic instance
                                                    	**type**\: int
                                                    
                                                    	**range:** 0..4294967295
                                                    
                                                    

                                                    """

                                                    _prefix = 'dnx-driver-oper'
                                                    _revision = '2015-11-09'

                                                    def __init__(self):
                                                        self.parent = None
                                                        self.rack_type = None
                                                        self.asic_type = None
                                                        self.rack_num = None
                                                        self.slot_num = None
                                                        self.asic_instance = None

                                                    @property
                                                    def _common_path(self):
                                                        if self.parent is None:
                                                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                                        return self.parent._common_path +'/Cisco-IOS-XR-dnx-driver-oper:asic-id'

                                                    def is_config(self):
                                                        ''' Returns True if this instance represents config data else returns False '''
                                                        return False

                                                    def _has_data(self):
                                                        if not self.is_config():
                                                            return False
                                                        if self.rack_type is not None:
                                                            return True

                                                        if self.asic_type is not None:
                                                            return True

                                                        if self.rack_num is not None:
                                                            return True

                                                        if self.slot_num is not None:
                                                            return True

                                                        if self.asic_instance is not None:
                                                            return True

                                                        return False

                                                    @staticmethod
                                                    def _meta_info():
                                                        from ydk.models.dnx._meta import _Cisco_IOS_XR_dnx_driver_oper as meta
                                                        return meta._meta_table['Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable.TxStatusOption.TxAsicInstances.TxAsicInstance.TxLinks.TxLink.TxLink.FarEndLink.AsicId']['meta_info']

                                                @property
                                                def _common_path(self):
                                                    if self.parent is None:
                                                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                                    return self.parent._common_path +'/Cisco-IOS-XR-dnx-driver-oper:far-end-link'

                                                def is_config(self):
                                                    ''' Returns True if this instance represents config data else returns False '''
                                                    return False

                                                def _has_data(self):
                                                    if not self.is_config():
                                                        return False
                                                    if self.asic_id is not None and self.asic_id._has_data():
                                                        return True

                                                    if self.link_type is not None:
                                                        return True

                                                    if self.link_stage is not None:
                                                        return True

                                                    if self.link_num is not None:
                                                        return True

                                                    if self.phy_link_num is not None:
                                                        return True

                                                    return False

                                                @staticmethod
                                                def _meta_info():
                                                    from ydk.models.dnx._meta import _Cisco_IOS_XR_dnx_driver_oper as meta
                                                    return meta._meta_table['Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable.TxStatusOption.TxAsicInstances.TxAsicInstance.TxLinks.TxLink.TxLink.FarEndLink']['meta_info']


                                            class Stats(object):
                                                """
                                                stats
                                                
                                                .. attribute:: dummy
                                                
                                                	dummy
                                                	**type**\: int
                                                
                                                	**range:** 0..4294967295
                                                
                                                

                                                """

                                                _prefix = 'dnx-driver-oper'
                                                _revision = '2015-11-09'

                                                def __init__(self):
                                                    self.parent = None
                                                    self.dummy = None

                                                @property
                                                def _common_path(self):
                                                    if self.parent is None:
                                                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                                    return self.parent._common_path +'/Cisco-IOS-XR-dnx-driver-oper:stats'

                                                def is_config(self):
                                                    ''' Returns True if this instance represents config data else returns False '''
                                                    return False

                                                def _has_data(self):
                                                    if not self.is_config():
                                                        return False
                                                    if self.dummy is not None:
                                                        return True

                                                    return False

                                                @staticmethod
                                                def _meta_info():
                                                    from ydk.models.dnx._meta import _Cisco_IOS_XR_dnx_driver_oper as meta
                                                    return meta._meta_table['Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable.TxStatusOption.TxAsicInstances.TxAsicInstance.TxLinks.TxLink.TxLink.Stats']['meta_info']


                                            class History(object):
                                                """
                                                history
                                                
                                                .. attribute:: histnum
                                                
                                                	histnum
                                                	**type**\: int
                                                
                                                	**range:** 0..255
                                                
                                                .. attribute:: start_index
                                                
                                                	start index
                                                	**type**\: int
                                                
                                                	**range:** 0..255
                                                
                                                .. attribute:: hist
                                                
                                                	hist
                                                	**type**\: list of :py:class:`Hist <ydk.models.dnx.Cisco_IOS_XR_dnx_driver_oper.Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable.TxStatusOption.TxAsicInstances.TxAsicInstance.TxLinks.TxLink.TxLink.History.Hist>`
                                                
                                                

                                                """

                                                _prefix = 'dnx-driver-oper'
                                                _revision = '2015-11-09'

                                                def __init__(self):
                                                    self.parent = None
                                                    self.histnum = None
                                                    self.start_index = None
                                                    self.hist = YList()
                                                    self.hist.parent = self
                                                    self.hist.name = 'hist'


                                                class Hist(object):
                                                    """
                                                    hist
                                                    
                                                    .. attribute:: admin_state
                                                    
                                                    	admin state
                                                    	**type**\: int
                                                    
                                                    	**range:** \-128..127
                                                    
                                                    .. attribute:: oper_state
                                                    
                                                    	oper state
                                                    	**type**\: int
                                                    
                                                    	**range:** \-128..127
                                                    
                                                    .. attribute:: error_state
                                                    
                                                    	error state
                                                    	**type**\: int
                                                    
                                                    	**range:** \-128..127
                                                    
                                                    .. attribute:: timestamp
                                                    
                                                    	timestamp
                                                    	**type**\: int
                                                    
                                                    	**range:** 0..18446744073709551615
                                                    
                                                    .. attribute:: reasons
                                                    
                                                    	reasons
                                                    	**type**\: str
                                                    
                                                    

                                                    """

                                                    _prefix = 'dnx-driver-oper'
                                                    _revision = '2015-11-09'

                                                    def __init__(self):
                                                        self.parent = None
                                                        self.admin_state = None
                                                        self.oper_state = None
                                                        self.error_state = None
                                                        self.timestamp = None
                                                        self.reasons = None

                                                    @property
                                                    def _common_path(self):
                                                        if self.parent is None:
                                                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                                        return self.parent._common_path +'/Cisco-IOS-XR-dnx-driver-oper:hist'

                                                    def is_config(self):
                                                        ''' Returns True if this instance represents config data else returns False '''
                                                        return False

                                                    def _has_data(self):
                                                        if not self.is_config():
                                                            return False
                                                        if self.admin_state is not None:
                                                            return True

                                                        if self.oper_state is not None:
                                                            return True

                                                        if self.error_state is not None:
                                                            return True

                                                        if self.timestamp is not None:
                                                            return True

                                                        if self.reasons is not None:
                                                            return True

                                                        return False

                                                    @staticmethod
                                                    def _meta_info():
                                                        from ydk.models.dnx._meta import _Cisco_IOS_XR_dnx_driver_oper as meta
                                                        return meta._meta_table['Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable.TxStatusOption.TxAsicInstances.TxAsicInstance.TxLinks.TxLink.TxLink.History.Hist']['meta_info']

                                                @property
                                                def _common_path(self):
                                                    if self.parent is None:
                                                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                                    return self.parent._common_path +'/Cisco-IOS-XR-dnx-driver-oper:history'

                                                def is_config(self):
                                                    ''' Returns True if this instance represents config data else returns False '''
                                                    return False

                                                def _has_data(self):
                                                    if not self.is_config():
                                                        return False
                                                    if self.histnum is not None:
                                                        return True

                                                    if self.start_index is not None:
                                                        return True

                                                    if self.hist is not None:
                                                        for child_ref in self.hist:
                                                            if child_ref._has_data():
                                                                return True

                                                    return False

                                                @staticmethod
                                                def _meta_info():
                                                    from ydk.models.dnx._meta import _Cisco_IOS_XR_dnx_driver_oper as meta
                                                    return meta._meta_table['Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable.TxStatusOption.TxAsicInstances.TxAsicInstance.TxLinks.TxLink.TxLink.History']['meta_info']

                                            @property
                                            def _common_path(self):
                                                if self.parent is None:
                                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')
                                                if self.link is None:
                                                    raise YPYDataValidationError('Key property link is None')

                                                return self.parent._common_path +'/Cisco-IOS-XR-dnx-driver-oper:tx-link[Cisco-IOS-XR-dnx-driver-oper:link = ' + str(self.link) + ']'

                                            def is_config(self):
                                                ''' Returns True if this instance represents config data else returns False '''
                                                return False

                                            def _has_data(self):
                                                if not self.is_config():
                                                    return False
                                                if self.link is not None:
                                                    return True

                                                if self.this_link is not None and self.this_link._has_data():
                                                    return True

                                                if self.far_end_link is not None and self.far_end_link._has_data():
                                                    return True

                                                if self.stats is not None and self.stats._has_data():
                                                    return True

                                                if self.history is not None and self.history._has_data():
                                                    return True

                                                if self.speed is not None:
                                                    return True

                                                if self.stage is not None:
                                                    return True

                                                if self.is_link_valid is not None:
                                                    return True

                                                if self.is_conf_pending is not None:
                                                    return True

                                                if self.is_power_enabled is not None:
                                                    return True

                                                if self.coeff1 is not None:
                                                    return True

                                                if self.coeff2 is not None:
                                                    return True

                                                if self.admin_state is not None:
                                                    return True

                                                if self.oper_state is not None:
                                                    return True

                                                if self.error_state is not None:
                                                    return True

                                                if self.num_admin_shuts is not None:
                                                    return True

                                                return False

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.dnx._meta import _Cisco_IOS_XR_dnx_driver_oper as meta
                                                return meta._meta_table['Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable.TxStatusOption.TxAsicInstances.TxAsicInstance.TxLinks.TxLink.TxLink']['meta_info']

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/Cisco-IOS-XR-dnx-driver-oper:tx-link'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return False

                                        def _has_data(self):
                                            if not self.is_config():
                                                return False
                                            if self.start_number is not None:
                                                return True

                                            if self.end_number is not None:
                                                return True

                                            if self.tx_link is not None:
                                                for child_ref in self.tx_link:
                                                    if child_ref._has_data():
                                                        return True

                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.dnx._meta import _Cisco_IOS_XR_dnx_driver_oper as meta
                                            return meta._meta_table['Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable.TxStatusOption.TxAsicInstances.TxAsicInstance.TxLinks.TxLink']['meta_info']

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-dnx-driver-oper:tx-links'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        if not self.is_config():
                                            return False
                                        if self.tx_link is not None:
                                            for child_ref in self.tx_link:
                                                if child_ref._has_data():
                                                    return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.dnx._meta import _Cisco_IOS_XR_dnx_driver_oper as meta
                                        return meta._meta_table['Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable.TxStatusOption.TxAsicInstances.TxAsicInstance.TxLinks']['meta_info']

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYDataValidationError('parent is not set . Cannot derive path.')
                                    if self.instance is None:
                                        raise YPYDataValidationError('Key property instance is None')

                                    return self.parent._common_path +'/Cisco-IOS-XR-dnx-driver-oper:tx-asic-instance[Cisco-IOS-XR-dnx-driver-oper:instance = ' + str(self.instance) + ']'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.instance is not None:
                                        return True

                                    if self.tx_links is not None and self.tx_links._has_data():
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.dnx._meta import _Cisco_IOS_XR_dnx_driver_oper as meta
                                    return meta._meta_table['Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable.TxStatusOption.TxAsicInstances.TxAsicInstance']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-dnx-driver-oper:tx-asic-instances'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.tx_asic_instance is not None:
                                    for child_ref in self.tx_asic_instance:
                                        if child_ref._has_data():
                                            return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.dnx._meta import _Cisco_IOS_XR_dnx_driver_oper as meta
                                return meta._meta_table['Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable.TxStatusOption.TxAsicInstances']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-dnx-driver-oper:tx-status-option'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.tx_asic_instances is not None and self.tx_asic_instances._has_data():
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.dnx._meta import _Cisco_IOS_XR_dnx_driver_oper as meta
                            return meta._meta_table['Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable.TxStatusOption']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-dnx-driver-oper:tx-status-option-table'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.tx_status_option is not None and self.tx_status_option._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.dnx._meta import _Cisco_IOS_XR_dnx_driver_oper as meta
                        return meta._meta_table['Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-dnx-driver-oper:tx-link-information'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.tx_status_option_table is not None and self.tx_status_option_table._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.dnx._meta import _Cisco_IOS_XR_dnx_driver_oper as meta
                    return meta._meta_table['Fia.Nodes.Node.TxLinkInformation']['meta_info']


            class RegisterDump(object):
                """
                FIA register dump information
                
                .. attribute:: register_dump_units
                
                	Unit table for register dump
                	**type**\: :py:class:`RegisterDumpUnits <ydk.models.dnx.Cisco_IOS_XR_dnx_driver_oper.Fia.Nodes.Node.RegisterDump.RegisterDumpUnits>`
                
                

                """

                _prefix = 'dnx-driver-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.register_dump_units = Fia.Nodes.Node.RegisterDump.RegisterDumpUnits()
                    self.register_dump_units.parent = self


                class RegisterDumpUnits(object):
                    """
                    Unit table for register dump
                    
                    .. attribute:: register_dump_unit
                    
                    	Unit number for register dump
                    	**type**\: list of :py:class:`RegisterDumpUnit <ydk.models.dnx.Cisco_IOS_XR_dnx_driver_oper.Fia.Nodes.Node.RegisterDump.RegisterDumpUnits.RegisterDumpUnit>`
                    
                    

                    """

                    _prefix = 'dnx-driver-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.register_dump_unit = YList()
                        self.register_dump_unit.parent = self
                        self.register_dump_unit.name = 'register_dump_unit'


                    class RegisterDumpUnit(object):
                        """
                        Unit number for register dump
                        
                        .. attribute:: unit  <key>
                        
                        	Unit number
                        	**type**\: int
                        
                        	**range:** \-2147483648..2147483647
                        
                        .. attribute:: output
                        
                        	output
                        	**type**\: str
                        
                        

                        """

                        _prefix = 'dnx-driver-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.unit = None
                            self.output = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')
                            if self.unit is None:
                                raise YPYDataValidationError('Key property unit is None')

                            return self.parent._common_path +'/Cisco-IOS-XR-dnx-driver-oper:register-dump-unit[Cisco-IOS-XR-dnx-driver-oper:unit = ' + str(self.unit) + ']'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.unit is not None:
                                return True

                            if self.output is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.dnx._meta import _Cisco_IOS_XR_dnx_driver_oper as meta
                            return meta._meta_table['Fia.Nodes.Node.RegisterDump.RegisterDumpUnits.RegisterDumpUnit']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-dnx-driver-oper:register-dump-units'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.register_dump_unit is not None:
                            for child_ref in self.register_dump_unit:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.dnx._meta import _Cisco_IOS_XR_dnx_driver_oper as meta
                        return meta._meta_table['Fia.Nodes.Node.RegisterDump.RegisterDumpUnits']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-dnx-driver-oper:register-dump'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.register_dump_units is not None and self.register_dump_units._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.dnx._meta import _Cisco_IOS_XR_dnx_driver_oper as meta
                    return meta._meta_table['Fia.Nodes.Node.RegisterDump']['meta_info']


            class DiagShell(object):
                """
                FIA diag shell information
                
                .. attribute:: diag_shell_units
                
                	Unit table for diag shell
                	**type**\: :py:class:`DiagShellUnits <ydk.models.dnx.Cisco_IOS_XR_dnx_driver_oper.Fia.Nodes.Node.DiagShell.DiagShellUnits>`
                
                

                """

                _prefix = 'dnx-driver-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.diag_shell_units = Fia.Nodes.Node.DiagShell.DiagShellUnits()
                    self.diag_shell_units.parent = self


                class DiagShellUnits(object):
                    """
                    Unit table for diag shell
                    
                    .. attribute:: diag_shell_unit
                    
                    	Unit number for diag shell statistics
                    	**type**\: list of :py:class:`DiagShellUnit <ydk.models.dnx.Cisco_IOS_XR_dnx_driver_oper.Fia.Nodes.Node.DiagShell.DiagShellUnits.DiagShellUnit>`
                    
                    

                    """

                    _prefix = 'dnx-driver-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.diag_shell_unit = YList()
                        self.diag_shell_unit.parent = self
                        self.diag_shell_unit.name = 'diag_shell_unit'


                    class DiagShellUnit(object):
                        """
                        Unit number for diag shell statistics
                        
                        .. attribute:: unit  <key>
                        
                        	Unit number
                        	**type**\: int
                        
                        	**range:** 0..15
                        
                        .. attribute:: commands
                        
                        	Command table for diag shell
                        	**type**\: :py:class:`Commands <ydk.models.dnx.Cisco_IOS_XR_dnx_driver_oper.Fia.Nodes.Node.DiagShell.DiagShellUnits.DiagShellUnit.Commands>`
                        
                        

                        """

                        _prefix = 'dnx-driver-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.unit = None
                            self.commands = Fia.Nodes.Node.DiagShell.DiagShellUnits.DiagShellUnit.Commands()
                            self.commands.parent = self


                        class Commands(object):
                            """
                            Command table for diag shell
                            
                            .. attribute:: command
                            
                            	Command for diag shell statistics
                            	**type**\: list of :py:class:`Command <ydk.models.dnx.Cisco_IOS_XR_dnx_driver_oper.Fia.Nodes.Node.DiagShell.DiagShellUnits.DiagShellUnit.Commands.Command>`
                            
                            

                            """

                            _prefix = 'dnx-driver-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.command = YList()
                                self.command.parent = self
                                self.command.name = 'command'


                            class Command(object):
                                """
                                Command for diag shell statistics
                                
                                .. attribute:: cmd  <key>
                                
                                	Shell command
                                	**type**\: str
                                
                                .. attribute:: output
                                
                                	Added to support datalist
                                	**type**\: list of :py:class:`Output <ydk.models.dnx.Cisco_IOS_XR_dnx_driver_oper.Fia.Nodes.Node.DiagShell.DiagShellUnits.DiagShellUnit.Commands.Command.Output>`
                                
                                

                                """

                                _prefix = 'dnx-driver-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.cmd = None
                                    self.output = YList()
                                    self.output.parent = self
                                    self.output.name = 'output'


                                class Output(object):
                                    """
                                    Added to support datalist
                                    
                                    .. attribute:: output  <key>
                                    
                                    	First line
                                    	**type**\: str
                                    
                                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                                    
                                    .. attribute:: output_xr
                                    
                                    	output xr
                                    	**type**\: str
                                    
                                    

                                    """

                                    _prefix = 'dnx-driver-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.output = None
                                        self.output_xr = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYDataValidationError('parent is not set . Cannot derive path.')
                                        if self.output is None:
                                            raise YPYDataValidationError('Key property output is None')

                                        return self.parent._common_path +'/Cisco-IOS-XR-dnx-driver-oper:output[Cisco-IOS-XR-dnx-driver-oper:output = ' + str(self.output) + ']'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        if not self.is_config():
                                            return False
                                        if self.output is not None:
                                            return True

                                        if self.output_xr is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.dnx._meta import _Cisco_IOS_XR_dnx_driver_oper as meta
                                        return meta._meta_table['Fia.Nodes.Node.DiagShell.DiagShellUnits.DiagShellUnit.Commands.Command.Output']['meta_info']

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYDataValidationError('parent is not set . Cannot derive path.')
                                    if self.cmd is None:
                                        raise YPYDataValidationError('Key property cmd is None')

                                    return self.parent._common_path +'/Cisco-IOS-XR-dnx-driver-oper:command[Cisco-IOS-XR-dnx-driver-oper:cmd = ' + str(self.cmd) + ']'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.cmd is not None:
                                        return True

                                    if self.output is not None:
                                        for child_ref in self.output:
                                            if child_ref._has_data():
                                                return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.dnx._meta import _Cisco_IOS_XR_dnx_driver_oper as meta
                                    return meta._meta_table['Fia.Nodes.Node.DiagShell.DiagShellUnits.DiagShellUnit.Commands.Command']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-dnx-driver-oper:commands'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.command is not None:
                                    for child_ref in self.command:
                                        if child_ref._has_data():
                                            return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.dnx._meta import _Cisco_IOS_XR_dnx_driver_oper as meta
                                return meta._meta_table['Fia.Nodes.Node.DiagShell.DiagShellUnits.DiagShellUnit.Commands']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')
                            if self.unit is None:
                                raise YPYDataValidationError('Key property unit is None')

                            return self.parent._common_path +'/Cisco-IOS-XR-dnx-driver-oper:diag-shell-unit[Cisco-IOS-XR-dnx-driver-oper:unit = ' + str(self.unit) + ']'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.unit is not None:
                                return True

                            if self.commands is not None and self.commands._has_data():
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.dnx._meta import _Cisco_IOS_XR_dnx_driver_oper as meta
                            return meta._meta_table['Fia.Nodes.Node.DiagShell.DiagShellUnits.DiagShellUnit']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-dnx-driver-oper:diag-shell-units'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.diag_shell_unit is not None:
                            for child_ref in self.diag_shell_unit:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.dnx._meta import _Cisco_IOS_XR_dnx_driver_oper as meta
                        return meta._meta_table['Fia.Nodes.Node.DiagShell.DiagShellUnits']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-dnx-driver-oper:diag-shell'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.diag_shell_units is not None and self.diag_shell_units._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.dnx._meta import _Cisco_IOS_XR_dnx_driver_oper as meta
                    return meta._meta_table['Fia.Nodes.Node.DiagShell']['meta_info']


            class OirHistory(object):
                """
                FIA operational data of oir history
                
                .. attribute:: flags
                
                	Flag table for history
                	**type**\: :py:class:`Flags <ydk.models.dnx.Cisco_IOS_XR_dnx_driver_oper.Fia.Nodes.Node.OirHistory.Flags>`
                
                

                """

                _prefix = 'dnx-driver-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.flags = Fia.Nodes.Node.OirHistory.Flags()
                    self.flags.parent = self


                class Flags(object):
                    """
                    Flag table for history
                    
                    .. attribute:: flag
                    
                    	Flag value for physical location
                    	**type**\: list of :py:class:`Flag <ydk.models.dnx.Cisco_IOS_XR_dnx_driver_oper.Fia.Nodes.Node.OirHistory.Flags.Flag>`
                    
                    

                    """

                    _prefix = 'dnx-driver-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.flag = YList()
                        self.flag.parent = self
                        self.flag.name = 'flag'


                    class Flag(object):
                        """
                        Flag value for physical location
                        
                        .. attribute:: flag  <key>
                        
                        	Flag value
                        	**type**\: int
                        
                        	**range:** \-2147483648..2147483647
                        
                        .. attribute:: slots
                        
                        	Slot table for history
                        	**type**\: :py:class:`Slots <ydk.models.dnx.Cisco_IOS_XR_dnx_driver_oper.Fia.Nodes.Node.OirHistory.Flags.Flag.Slots>`
                        
                        

                        """

                        _prefix = 'dnx-driver-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.flag = None
                            self.slots = Fia.Nodes.Node.OirHistory.Flags.Flag.Slots()
                            self.slots.parent = self


                        class Slots(object):
                            """
                            Slot table for history
                            
                            .. attribute:: slot
                            
                            	Slot number for getting history
                            	**type**\: list of :py:class:`Slot <ydk.models.dnx.Cisco_IOS_XR_dnx_driver_oper.Fia.Nodes.Node.OirHistory.Flags.Flag.Slots.Slot>`
                            
                            

                            """

                            _prefix = 'dnx-driver-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.slot = YList()
                                self.slot.parent = self
                                self.slot.name = 'slot'


                            class Slot(object):
                                """
                                Slot number for getting history
                                
                                .. attribute:: slot  <key>
                                
                                	Slot number
                                	**type**\: int
                                
                                	**range:** \-2147483648..2147483647
                                
                                .. attribute:: drv_version
                                
                                	drv version
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: coeff_major_rev
                                
                                	coeff major rev
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: coeff_minor_rev
                                
                                	coeff minor rev
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: functional_role
                                
                                	functional role
                                	**type**\: int
                                
                                	**range:** 0..255
                                
                                .. attribute:: issu_role
                                
                                	issu role
                                	**type**\: int
                                
                                	**range:** 0..255
                                
                                .. attribute:: rack_name
                                
                                	rack name
                                	**type**\: str
                                
                                .. attribute:: rack_type
                                
                                	rack type
                                	**type**\: int
                                
                                	**range:** \-2147483648..2147483647
                                
                                .. attribute:: rack_num
                                
                                	rack num
                                	**type**\: int
                                
                                	**range:** 0..255
                                
                                .. attribute:: is_driver_ready
                                
                                	is driver ready
                                	**type**\: bool
                                
                                .. attribute:: card_avail_mask
                                
                                	card avail mask
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: asic_avail_mask
                                
                                	asic avail mask
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: exp_asic_avail_mask
                                
                                	exp asic avail mask
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: ucmc_ratio
                                
                                	ucmc ratio
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: asic_oper_notify_to_fsdb_pending_bmap
                                
                                	asic oper notify to fsdb pending bmap
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: is_full_fgid_download_req
                                
                                	is full fgid download req
                                	**type**\: bool
                                
                                .. attribute:: is_fgid_download_in_progress
                                
                                	is fgid download in progress
                                	**type**\: bool
                                
                                .. attribute:: is_fgid_download_completed
                                
                                	is fgid download completed
                                	**type**\: bool
                                
                                .. attribute:: fsdb_conn_active
                                
                                	fsdb conn active
                                	**type**\: bool
                                
                                .. attribute:: fgid_conn_active
                                
                                	fgid conn active
                                	**type**\: bool
                                
                                .. attribute:: issu_mgr_conn_active
                                
                                	issu mgr conn active
                                	**type**\: bool
                                
                                .. attribute:: fsdb_reg_active
                                
                                	fsdb reg active
                                	**type**\: bool
                                
                                .. attribute:: fgid_reg_active
                                
                                	fgid reg active
                                	**type**\: bool
                                
                                .. attribute:: issu_mgr_reg_active
                                
                                	issu mgr reg active
                                	**type**\: bool
                                
                                .. attribute:: num_pm_conn_reqs
                                
                                	num pm conn reqs
                                	**type**\: int
                                
                                	**range:** 0..255
                                
                                .. attribute:: num_fsdb_conn_reqs
                                
                                	num fsdb conn reqs
                                	**type**\: int
                                
                                	**range:** 0..255
                                
                                .. attribute:: num_fgid_conn_reqs
                                
                                	num fgid conn reqs
                                	**type**\: int
                                
                                	**range:** 0..255
                                
                                .. attribute:: num_fstats_conn_reqs
                                
                                	num fstats conn reqs
                                	**type**\: int
                                
                                	**range:** 0..255
                                
                                .. attribute:: num_cm_conn_reqs
                                
                                	num cm conn reqs
                                	**type**\: int
                                
                                	**range:** 0..255
                                
                                .. attribute:: num_issu_mgr_conn_reqs
                                
                                	num issu mgr conn reqs
                                	**type**\: int
                                
                                	**range:** 0..255
                                
                                .. attribute:: num_peer_fia_conn_reqs
                                
                                	num peer fia conn reqs
                                	**type**\: int
                                
                                	**range:** 0..255
                                
                                .. attribute:: is_gaspp_registered
                                
                                	is gaspp registered
                                	**type**\: bool
                                
                                .. attribute:: is_cih_registered
                                
                                	is cih registered
                                	**type**\: bool
                                
                                .. attribute:: offset_time_nsec
                                
                                	offset time nsec
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: drvr_startup_timestamp
                                
                                	drvr startup timestamp
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: num_intf_ports
                                
                                	num intf ports
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: uc_weight
                                
                                	uc weight
                                	**type**\: int
                                
                                	**range:** 0..255
                                
                                .. attribute:: respawn_count
                                
                                	respawn count
                                	**type**\: int
                                
                                	**range:** 0..255
                                
                                .. attribute:: total_asics
                                
                                	total asics
                                	**type**\: int
                                
                                	**range:** 0..255
                                
                                .. attribute:: issu_ready_ntfy_pending
                                
                                	issu ready ntfy pending
                                	**type**\: bool
                                
                                .. attribute:: issu_abort_sent
                                
                                	issu abort sent
                                	**type**\: bool
                                
                                .. attribute:: issu_abort_rcvd
                                
                                	issu abort rcvd
                                	**type**\: bool
                                
                                .. attribute:: fc_mode
                                
                                	fc mode
                                	**type**\: int
                                
                                	**range:** 0..255
                                
                                .. attribute:: board_rev_id
                                
                                	board rev id
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: device_info
                                
                                	device info
                                	**type**\: list of :py:class:`DeviceInfo <ydk.models.dnx.Cisco_IOS_XR_dnx_driver_oper.Fia.Nodes.Node.OirHistory.Flags.Flag.Slots.Slot.DeviceInfo>`
                                
                                .. attribute:: card_info
                                
                                	card info
                                	**type**\: list of :py:class:`CardInfo <ydk.models.dnx.Cisco_IOS_XR_dnx_driver_oper.Fia.Nodes.Node.OirHistory.Flags.Flag.Slots.Slot.CardInfo>`
                                
                                

                                """

                                _prefix = 'dnx-driver-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.slot = None
                                    self.drv_version = None
                                    self.coeff_major_rev = None
                                    self.coeff_minor_rev = None
                                    self.functional_role = None
                                    self.issu_role = None
                                    self.rack_name = None
                                    self.rack_type = None
                                    self.rack_num = None
                                    self.is_driver_ready = None
                                    self.card_avail_mask = None
                                    self.asic_avail_mask = None
                                    self.exp_asic_avail_mask = None
                                    self.ucmc_ratio = None
                                    self.asic_oper_notify_to_fsdb_pending_bmap = None
                                    self.is_full_fgid_download_req = None
                                    self.is_fgid_download_in_progress = None
                                    self.is_fgid_download_completed = None
                                    self.fsdb_conn_active = None
                                    self.fgid_conn_active = None
                                    self.issu_mgr_conn_active = None
                                    self.fsdb_reg_active = None
                                    self.fgid_reg_active = None
                                    self.issu_mgr_reg_active = None
                                    self.num_pm_conn_reqs = None
                                    self.num_fsdb_conn_reqs = None
                                    self.num_fgid_conn_reqs = None
                                    self.num_fstats_conn_reqs = None
                                    self.num_cm_conn_reqs = None
                                    self.num_issu_mgr_conn_reqs = None
                                    self.num_peer_fia_conn_reqs = None
                                    self.is_gaspp_registered = None
                                    self.is_cih_registered = None
                                    self.offset_time_nsec = None
                                    self.drvr_startup_timestamp = None
                                    self.num_intf_ports = None
                                    self.uc_weight = None
                                    self.respawn_count = None
                                    self.total_asics = None
                                    self.issu_ready_ntfy_pending = None
                                    self.issu_abort_sent = None
                                    self.issu_abort_rcvd = None
                                    self.fc_mode = None
                                    self.board_rev_id = None
                                    self.device_info = YList()
                                    self.device_info.parent = self
                                    self.device_info.name = 'device_info'
                                    self.card_info = YList()
                                    self.card_info.parent = self
                                    self.card_info.name = 'card_info'


                                class DeviceInfo(object):
                                    """
                                    device info
                                    
                                    .. attribute:: asic_id
                                    
                                    	asic id
                                    	**type**\: :py:class:`AsicId <ydk.models.dnx.Cisco_IOS_XR_dnx_driver_oper.Fia.Nodes.Node.OirHistory.Flags.Flag.Slots.Slot.DeviceInfo.AsicId>`
                                    
                                    .. attribute:: is_valid
                                    
                                    	is valid
                                    	**type**\: bool
                                    
                                    .. attribute:: fapid
                                    
                                    	fapid
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: hotplug_event
                                    
                                    	hotplug event
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: slice_state
                                    
                                    	slice state
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: admin_state
                                    
                                    	admin state
                                    	**type**\: int
                                    
                                    	**range:** 0..255
                                    
                                    .. attribute:: oper_state
                                    
                                    	oper state
                                    	**type**\: int
                                    
                                    	**range:** 0..255
                                    
                                    .. attribute:: asic_state
                                    
                                    	asic state
                                    	**type**\: int
                                    
                                    	**range:** 0..255
                                    
                                    .. attribute:: last_init_cause
                                    
                                    	last init cause
                                    	**type**\: int
                                    
                                    	**range:** 0..255
                                    
                                    .. attribute:: num_pon_resets
                                    
                                    	num pon resets
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: num_hard_resets
                                    
                                    	num hard resets
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: last_pon_reset_timestamp
                                    
                                    	last pon reset timestamp
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: last_hard_reset_timestamp
                                    
                                    	last hard reset timestamp
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: local_switch_state
                                    
                                    	local switch state
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    

                                    """

                                    _prefix = 'dnx-driver-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.asic_id = Fia.Nodes.Node.OirHistory.Flags.Flag.Slots.Slot.DeviceInfo.AsicId()
                                        self.asic_id.parent = self
                                        self.is_valid = None
                                        self.fapid = None
                                        self.hotplug_event = None
                                        self.slice_state = None
                                        self.admin_state = None
                                        self.oper_state = None
                                        self.asic_state = None
                                        self.last_init_cause = None
                                        self.num_pon_resets = None
                                        self.num_hard_resets = None
                                        self.last_pon_reset_timestamp = None
                                        self.last_hard_reset_timestamp = None
                                        self.local_switch_state = None


                                    class AsicId(object):
                                        """
                                        asic id
                                        
                                        .. attribute:: rack_type
                                        
                                        	rack type
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: asic_type
                                        
                                        	asic type
                                        	**type**\: int
                                        
                                        	**range:** 0..255
                                        
                                        .. attribute:: rack_num
                                        
                                        	rack num
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: slot_num
                                        
                                        	slot num
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: asic_instance
                                        
                                        	asic instance
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        

                                        """

                                        _prefix = 'dnx-driver-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            self.parent = None
                                            self.rack_type = None
                                            self.asic_type = None
                                            self.rack_num = None
                                            self.slot_num = None
                                            self.asic_instance = None

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/Cisco-IOS-XR-dnx-driver-oper:asic-id'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return False

                                        def _has_data(self):
                                            if not self.is_config():
                                                return False
                                            if self.rack_type is not None:
                                                return True

                                            if self.asic_type is not None:
                                                return True

                                            if self.rack_num is not None:
                                                return True

                                            if self.slot_num is not None:
                                                return True

                                            if self.asic_instance is not None:
                                                return True

                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.dnx._meta import _Cisco_IOS_XR_dnx_driver_oper as meta
                                            return meta._meta_table['Fia.Nodes.Node.OirHistory.Flags.Flag.Slots.Slot.DeviceInfo.AsicId']['meta_info']

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-dnx-driver-oper:device-info'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        if not self.is_config():
                                            return False
                                        if self.asic_id is not None and self.asic_id._has_data():
                                            return True

                                        if self.is_valid is not None:
                                            return True

                                        if self.fapid is not None:
                                            return True

                                        if self.hotplug_event is not None:
                                            return True

                                        if self.slice_state is not None:
                                            return True

                                        if self.admin_state is not None:
                                            return True

                                        if self.oper_state is not None:
                                            return True

                                        if self.asic_state is not None:
                                            return True

                                        if self.last_init_cause is not None:
                                            return True

                                        if self.num_pon_resets is not None:
                                            return True

                                        if self.num_hard_resets is not None:
                                            return True

                                        if self.last_pon_reset_timestamp is not None:
                                            return True

                                        if self.last_hard_reset_timestamp is not None:
                                            return True

                                        if self.local_switch_state is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.dnx._meta import _Cisco_IOS_XR_dnx_driver_oper as meta
                                        return meta._meta_table['Fia.Nodes.Node.OirHistory.Flags.Flag.Slots.Slot.DeviceInfo']['meta_info']


                                class CardInfo(object):
                                    """
                                    card info
                                    
                                    .. attribute:: oir_circular_buffer
                                    
                                    	oir circular buffer
                                    	**type**\: :py:class:`OirCircularBuffer <ydk.models.dnx.Cisco_IOS_XR_dnx_driver_oper.Fia.Nodes.Node.OirHistory.Flags.Flag.Slots.Slot.CardInfo.OirCircularBuffer>`
                                    
                                    .. attribute:: card_type
                                    
                                    	card type
                                    	**type**\: int
                                    
                                    	**range:** \-2147483648..2147483647
                                    
                                    .. attribute:: card_name
                                    
                                    	card name
                                    	**type**\: str
                                    
                                    .. attribute:: slot_no
                                    
                                    	slot no
                                    	**type**\: int
                                    
                                    	**range:** \-2147483648..2147483647
                                    
                                    .. attribute:: card_flag
                                    
                                    	card flag
                                    	**type**\: int
                                    
                                    	**range:** \-2147483648..2147483647
                                    
                                    .. attribute:: evt_flag
                                    
                                    	evt flag
                                    	**type**\: int
                                    
                                    	**range:** \-2147483648..2147483647
                                    
                                    .. attribute:: reg_flag
                                    
                                    	reg flag
                                    	**type**\: int
                                    
                                    	**range:** \-2147483648..2147483647
                                    
                                    .. attribute:: instance
                                    
                                    	instance
                                    	**type**\: int
                                    
                                    	**range:** \-2147483648..2147483647
                                    
                                    .. attribute:: card_state
                                    
                                    	card state
                                    	**type**\: int
                                    
                                    	**range:** 0..255
                                    
                                    .. attribute:: exp_num_asics
                                    
                                    	exp num asics
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: exp_num_asics_per_fsdb
                                    
                                    	exp num asics per fsdb
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: is_powered
                                    
                                    	is powered
                                    	**type**\: bool
                                    
                                    .. attribute:: cxp_avail_bitmap
                                    
                                    	cxp avail bitmap
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: num_ilkns_per_asic
                                    
                                    	num ilkns per asic
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: num_local_ports_per_ilkn
                                    
                                    	num local ports per ilkn
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: num_cos_per_port
                                    
                                    	num cos per port
                                    	**type**\: int
                                    
                                    	**range:** 0..255
                                    
                                    

                                    """

                                    _prefix = 'dnx-driver-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.oir_circular_buffer = Fia.Nodes.Node.OirHistory.Flags.Flag.Slots.Slot.CardInfo.OirCircularBuffer()
                                        self.oir_circular_buffer.parent = self
                                        self.card_type = None
                                        self.card_name = None
                                        self.slot_no = None
                                        self.card_flag = None
                                        self.evt_flag = None
                                        self.reg_flag = None
                                        self.instance = None
                                        self.card_state = None
                                        self.exp_num_asics = None
                                        self.exp_num_asics_per_fsdb = None
                                        self.is_powered = None
                                        self.cxp_avail_bitmap = None
                                        self.num_ilkns_per_asic = None
                                        self.num_local_ports_per_ilkn = None
                                        self.num_cos_per_port = None


                                    class OirCircularBuffer(object):
                                        """
                                        oir circular buffer
                                        
                                        .. attribute:: count
                                        
                                        	count
                                        	**type**\: int
                                        
                                        	**range:** \-2147483648..2147483647
                                        
                                        .. attribute:: start
                                        
                                        	start
                                        	**type**\: int
                                        
                                        	**range:** \-2147483648..2147483647
                                        
                                        .. attribute:: end
                                        
                                        	end
                                        	**type**\: int
                                        
                                        	**range:** \-2147483648..2147483647
                                        
                                        .. attribute:: fia_oir_info
                                        
                                        	fia oir info
                                        	**type**\: list of :py:class:`FiaOirInfo <ydk.models.dnx.Cisco_IOS_XR_dnx_driver_oper.Fia.Nodes.Node.OirHistory.Flags.Flag.Slots.Slot.CardInfo.OirCircularBuffer.FiaOirInfo>`
                                        
                                        

                                        """

                                        _prefix = 'dnx-driver-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            self.parent = None
                                            self.count = None
                                            self.start = None
                                            self.end = None
                                            self.fia_oir_info = YList()
                                            self.fia_oir_info.parent = self
                                            self.fia_oir_info.name = 'fia_oir_info'


                                        class FiaOirInfo(object):
                                            """
                                            fia oir info
                                            
                                            .. attribute:: card_flag
                                            
                                            	card flag
                                            	**type**\: int
                                            
                                            	**range:** \-2147483648..2147483647
                                            
                                            .. attribute:: card_type
                                            
                                            	card type
                                            	**type**\: int
                                            
                                            	**range:** \-2147483648..2147483647
                                            
                                            .. attribute:: reg_flag
                                            
                                            	reg flag
                                            	**type**\: int
                                            
                                            	**range:** \-2147483648..2147483647
                                            
                                            .. attribute:: evt_flag
                                            
                                            	evt flag
                                            	**type**\: int
                                            
                                            	**range:** \-2147483648..2147483647
                                            
                                            .. attribute:: rack_num
                                            
                                            	rack num
                                            	**type**\: int
                                            
                                            	**range:** \-2147483648..2147483647
                                            
                                            .. attribute:: instance
                                            
                                            	instance
                                            	**type**\: int
                                            
                                            	**range:** \-2147483648..2147483647
                                            
                                            .. attribute:: cur_card_state
                                            
                                            	cur card state
                                            	**type**\: int
                                            
                                            	**range:** \-2147483648..2147483647
                                            
                                            

                                            """

                                            _prefix = 'dnx-driver-oper'
                                            _revision = '2015-11-09'

                                            def __init__(self):
                                                self.parent = None
                                                self.card_flag = None
                                                self.card_type = None
                                                self.reg_flag = None
                                                self.evt_flag = None
                                                self.rack_num = None
                                                self.instance = None
                                                self.cur_card_state = None

                                            @property
                                            def _common_path(self):
                                                if self.parent is None:
                                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                                return self.parent._common_path +'/Cisco-IOS-XR-dnx-driver-oper:fia-oir-info'

                                            def is_config(self):
                                                ''' Returns True if this instance represents config data else returns False '''
                                                return False

                                            def _has_data(self):
                                                if not self.is_config():
                                                    return False
                                                if self.card_flag is not None:
                                                    return True

                                                if self.card_type is not None:
                                                    return True

                                                if self.reg_flag is not None:
                                                    return True

                                                if self.evt_flag is not None:
                                                    return True

                                                if self.rack_num is not None:
                                                    return True

                                                if self.instance is not None:
                                                    return True

                                                if self.cur_card_state is not None:
                                                    return True

                                                return False

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.dnx._meta import _Cisco_IOS_XR_dnx_driver_oper as meta
                                                return meta._meta_table['Fia.Nodes.Node.OirHistory.Flags.Flag.Slots.Slot.CardInfo.OirCircularBuffer.FiaOirInfo']['meta_info']

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/Cisco-IOS-XR-dnx-driver-oper:oir-circular-buffer'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return False

                                        def _has_data(self):
                                            if not self.is_config():
                                                return False
                                            if self.count is not None:
                                                return True

                                            if self.start is not None:
                                                return True

                                            if self.end is not None:
                                                return True

                                            if self.fia_oir_info is not None:
                                                for child_ref in self.fia_oir_info:
                                                    if child_ref._has_data():
                                                        return True

                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.dnx._meta import _Cisco_IOS_XR_dnx_driver_oper as meta
                                            return meta._meta_table['Fia.Nodes.Node.OirHistory.Flags.Flag.Slots.Slot.CardInfo.OirCircularBuffer']['meta_info']

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-dnx-driver-oper:card-info'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        if not self.is_config():
                                            return False
                                        if self.oir_circular_buffer is not None and self.oir_circular_buffer._has_data():
                                            return True

                                        if self.card_type is not None:
                                            return True

                                        if self.card_name is not None:
                                            return True

                                        if self.slot_no is not None:
                                            return True

                                        if self.card_flag is not None:
                                            return True

                                        if self.evt_flag is not None:
                                            return True

                                        if self.reg_flag is not None:
                                            return True

                                        if self.instance is not None:
                                            return True

                                        if self.card_state is not None:
                                            return True

                                        if self.exp_num_asics is not None:
                                            return True

                                        if self.exp_num_asics_per_fsdb is not None:
                                            return True

                                        if self.is_powered is not None:
                                            return True

                                        if self.cxp_avail_bitmap is not None:
                                            return True

                                        if self.num_ilkns_per_asic is not None:
                                            return True

                                        if self.num_local_ports_per_ilkn is not None:
                                            return True

                                        if self.num_cos_per_port is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.dnx._meta import _Cisco_IOS_XR_dnx_driver_oper as meta
                                        return meta._meta_table['Fia.Nodes.Node.OirHistory.Flags.Flag.Slots.Slot.CardInfo']['meta_info']

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYDataValidationError('parent is not set . Cannot derive path.')
                                    if self.slot is None:
                                        raise YPYDataValidationError('Key property slot is None')

                                    return self.parent._common_path +'/Cisco-IOS-XR-dnx-driver-oper:slot[Cisco-IOS-XR-dnx-driver-oper:slot = ' + str(self.slot) + ']'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.slot is not None:
                                        return True

                                    if self.drv_version is not None:
                                        return True

                                    if self.coeff_major_rev is not None:
                                        return True

                                    if self.coeff_minor_rev is not None:
                                        return True

                                    if self.functional_role is not None:
                                        return True

                                    if self.issu_role is not None:
                                        return True

                                    if self.rack_name is not None:
                                        return True

                                    if self.rack_type is not None:
                                        return True

                                    if self.rack_num is not None:
                                        return True

                                    if self.is_driver_ready is not None:
                                        return True

                                    if self.card_avail_mask is not None:
                                        return True

                                    if self.asic_avail_mask is not None:
                                        return True

                                    if self.exp_asic_avail_mask is not None:
                                        return True

                                    if self.ucmc_ratio is not None:
                                        return True

                                    if self.asic_oper_notify_to_fsdb_pending_bmap is not None:
                                        return True

                                    if self.is_full_fgid_download_req is not None:
                                        return True

                                    if self.is_fgid_download_in_progress is not None:
                                        return True

                                    if self.is_fgid_download_completed is not None:
                                        return True

                                    if self.fsdb_conn_active is not None:
                                        return True

                                    if self.fgid_conn_active is not None:
                                        return True

                                    if self.issu_mgr_conn_active is not None:
                                        return True

                                    if self.fsdb_reg_active is not None:
                                        return True

                                    if self.fgid_reg_active is not None:
                                        return True

                                    if self.issu_mgr_reg_active is not None:
                                        return True

                                    if self.num_pm_conn_reqs is not None:
                                        return True

                                    if self.num_fsdb_conn_reqs is not None:
                                        return True

                                    if self.num_fgid_conn_reqs is not None:
                                        return True

                                    if self.num_fstats_conn_reqs is not None:
                                        return True

                                    if self.num_cm_conn_reqs is not None:
                                        return True

                                    if self.num_issu_mgr_conn_reqs is not None:
                                        return True

                                    if self.num_peer_fia_conn_reqs is not None:
                                        return True

                                    if self.is_gaspp_registered is not None:
                                        return True

                                    if self.is_cih_registered is not None:
                                        return True

                                    if self.offset_time_nsec is not None:
                                        return True

                                    if self.drvr_startup_timestamp is not None:
                                        return True

                                    if self.num_intf_ports is not None:
                                        return True

                                    if self.uc_weight is not None:
                                        return True

                                    if self.respawn_count is not None:
                                        return True

                                    if self.total_asics is not None:
                                        return True

                                    if self.issu_ready_ntfy_pending is not None:
                                        return True

                                    if self.issu_abort_sent is not None:
                                        return True

                                    if self.issu_abort_rcvd is not None:
                                        return True

                                    if self.fc_mode is not None:
                                        return True

                                    if self.board_rev_id is not None:
                                        return True

                                    if self.device_info is not None:
                                        for child_ref in self.device_info:
                                            if child_ref._has_data():
                                                return True

                                    if self.card_info is not None:
                                        for child_ref in self.card_info:
                                            if child_ref._has_data():
                                                return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.dnx._meta import _Cisco_IOS_XR_dnx_driver_oper as meta
                                    return meta._meta_table['Fia.Nodes.Node.OirHistory.Flags.Flag.Slots.Slot']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-dnx-driver-oper:slots'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.slot is not None:
                                    for child_ref in self.slot:
                                        if child_ref._has_data():
                                            return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.dnx._meta import _Cisco_IOS_XR_dnx_driver_oper as meta
                                return meta._meta_table['Fia.Nodes.Node.OirHistory.Flags.Flag.Slots']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')
                            if self.flag is None:
                                raise YPYDataValidationError('Key property flag is None')

                            return self.parent._common_path +'/Cisco-IOS-XR-dnx-driver-oper:flag[Cisco-IOS-XR-dnx-driver-oper:flag = ' + str(self.flag) + ']'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.flag is not None:
                                return True

                            if self.slots is not None and self.slots._has_data():
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.dnx._meta import _Cisco_IOS_XR_dnx_driver_oper as meta
                            return meta._meta_table['Fia.Nodes.Node.OirHistory.Flags.Flag']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-dnx-driver-oper:flags'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.flag is not None:
                            for child_ref in self.flag:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.dnx._meta import _Cisco_IOS_XR_dnx_driver_oper as meta
                        return meta._meta_table['Fia.Nodes.Node.OirHistory.Flags']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-dnx-driver-oper:oir-history'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.flags is not None and self.flags._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.dnx._meta import _Cisco_IOS_XR_dnx_driver_oper as meta
                    return meta._meta_table['Fia.Nodes.Node.OirHistory']['meta_info']


            class AsicStatistics(object):
                """
                FIA asic statistics information
                
                .. attribute:: statistics_asic_instances
                
                	Instance table for statistics
                	**type**\: :py:class:`StatisticsAsicInstances <ydk.models.dnx.Cisco_IOS_XR_dnx_driver_oper.Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances>`
                
                

                """

                _prefix = 'dnx-driver-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.statistics_asic_instances = Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances()
                    self.statistics_asic_instances.parent = self


                class StatisticsAsicInstances(object):
                    """
                    Instance table for statistics
                    
                    .. attribute:: statistics_asic_instance
                    
                    	Asic instance for statistics
                    	**type**\: list of :py:class:`StatisticsAsicInstance <ydk.models.dnx.Cisco_IOS_XR_dnx_driver_oper.Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance>`
                    
                    

                    """

                    _prefix = 'dnx-driver-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.statistics_asic_instance = YList()
                        self.statistics_asic_instance.parent = self
                        self.statistics_asic_instance.name = 'statistics_asic_instance'


                    class StatisticsAsicInstance(object):
                        """
                        Asic instance for statistics
                        
                        .. attribute:: instance  <key>
                        
                        	Asic instance
                        	**type**\: int
                        
                        	**range:** 0..16
                        
                        .. attribute:: pbc_statistics
                        
                        	Packet Byte Counter for a Asic
                        	**type**\: :py:class:`PbcStatistics <ydk.models.dnx.Cisco_IOS_XR_dnx_driver_oper.Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.PbcStatistics>`
                        
                        .. attribute:: fmac_statistics
                        
                        	Statistics of FMAC
                        	**type**\: :py:class:`FmacStatistics <ydk.models.dnx.Cisco_IOS_XR_dnx_driver_oper.Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.FmacStatistics>`
                        
                        

                        """

                        _prefix = 'dnx-driver-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.instance = None
                            self.pbc_statistics = Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.PbcStatistics()
                            self.pbc_statistics.parent = self
                            self.fmac_statistics = Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.FmacStatistics()
                            self.fmac_statistics.parent = self


                        class PbcStatistics(object):
                            """
                            Packet Byte Counter for a Asic
                            
                            .. attribute:: pbc_stats
                            
                            	PBC stats bag
                            	**type**\: :py:class:`PbcStats <ydk.models.dnx.Cisco_IOS_XR_dnx_driver_oper.Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.PbcStatistics.PbcStats>`
                            
                            

                            """

                            _prefix = 'dnx-driver-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.pbc_stats = Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.PbcStatistics.PbcStats()
                                self.pbc_stats.parent = self


                            class PbcStats(object):
                                """
                                PBC stats bag
                                
                                .. attribute:: stats_info
                                
                                	stats info
                                	**type**\: :py:class:`StatsInfo <ydk.models.dnx.Cisco_IOS_XR_dnx_driver_oper.Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.PbcStatistics.PbcStats.StatsInfo>`
                                
                                .. attribute:: valid
                                
                                	valid
                                	**type**\: bool
                                
                                .. attribute:: rack_no
                                
                                	rack no
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: slot_no
                                
                                	slot no
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: asic_instance
                                
                                	asic instance
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: chip_ver
                                
                                	chip ver
                                	**type**\: int
                                
                                	**range:** 0..65535
                                
                                

                                """

                                _prefix = 'dnx-driver-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.stats_info = Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.PbcStatistics.PbcStats.StatsInfo()
                                    self.stats_info.parent = self
                                    self.valid = None
                                    self.rack_no = None
                                    self.slot_no = None
                                    self.asic_instance = None
                                    self.chip_ver = None


                                class StatsInfo(object):
                                    """
                                    stats info
                                    
                                    .. attribute:: num_blocks
                                    
                                    	Num Blocks
                                    	**type**\: int
                                    
                                    	**range:** 0..255
                                    
                                    .. attribute:: block_info
                                    
                                    	block info
                                    	**type**\: list of :py:class:`BlockInfo <ydk.models.dnx.Cisco_IOS_XR_dnx_driver_oper.Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.PbcStatistics.PbcStats.StatsInfo.BlockInfo>`
                                    
                                    

                                    """

                                    _prefix = 'dnx-driver-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.num_blocks = None
                                        self.block_info = YList()
                                        self.block_info.parent = self
                                        self.block_info.name = 'block_info'


                                    class BlockInfo(object):
                                        """
                                        block info
                                        
                                        .. attribute:: block_name
                                        
                                        	Block Name
                                        	**type**\: str
                                        
                                        	**range:** 0..11
                                        
                                        .. attribute:: num_fields
                                        
                                        	Num Fields
                                        	**type**\: int
                                        
                                        	**range:** 0..255
                                        
                                        .. attribute:: field_info
                                        
                                        	field info
                                        	**type**\: list of :py:class:`FieldInfo <ydk.models.dnx.Cisco_IOS_XR_dnx_driver_oper.Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.PbcStatistics.PbcStats.StatsInfo.BlockInfo.FieldInfo>`
                                        
                                        

                                        """

                                        _prefix = 'dnx-driver-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            self.parent = None
                                            self.block_name = None
                                            self.num_fields = None
                                            self.field_info = YList()
                                            self.field_info.parent = self
                                            self.field_info.name = 'field_info'


                                        class FieldInfo(object):
                                            """
                                            field info
                                            
                                            .. attribute:: field_name
                                            
                                            	Field Name
                                            	**type**\: str
                                            
                                            	**range:** 0..51
                                            
                                            .. attribute:: field_value
                                            
                                            	Field Value
                                            	**type**\: int
                                            
                                            	**range:** 0..18446744073709551615
                                            
                                            .. attribute:: is_ovf
                                            
                                            	Is Ovf
                                            	**type**\: bool
                                            
                                            

                                            """

                                            _prefix = 'dnx-driver-oper'
                                            _revision = '2015-11-09'

                                            def __init__(self):
                                                self.parent = None
                                                self.field_name = None
                                                self.field_value = None
                                                self.is_ovf = None

                                            @property
                                            def _common_path(self):
                                                if self.parent is None:
                                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                                return self.parent._common_path +'/Cisco-IOS-XR-dnx-driver-oper:field-info'

                                            def is_config(self):
                                                ''' Returns True if this instance represents config data else returns False '''
                                                return False

                                            def _has_data(self):
                                                if not self.is_config():
                                                    return False
                                                if self.field_name is not None:
                                                    return True

                                                if self.field_value is not None:
                                                    return True

                                                if self.is_ovf is not None:
                                                    return True

                                                return False

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.dnx._meta import _Cisco_IOS_XR_dnx_driver_oper as meta
                                                return meta._meta_table['Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.PbcStatistics.PbcStats.StatsInfo.BlockInfo.FieldInfo']['meta_info']

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/Cisco-IOS-XR-dnx-driver-oper:block-info'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return False

                                        def _has_data(self):
                                            if not self.is_config():
                                                return False
                                            if self.block_name is not None:
                                                return True

                                            if self.num_fields is not None:
                                                return True

                                            if self.field_info is not None:
                                                for child_ref in self.field_info:
                                                    if child_ref._has_data():
                                                        return True

                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.dnx._meta import _Cisco_IOS_XR_dnx_driver_oper as meta
                                            return meta._meta_table['Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.PbcStatistics.PbcStats.StatsInfo.BlockInfo']['meta_info']

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-dnx-driver-oper:stats-info'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        if not self.is_config():
                                            return False
                                        if self.num_blocks is not None:
                                            return True

                                        if self.block_info is not None:
                                            for child_ref in self.block_info:
                                                if child_ref._has_data():
                                                    return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.dnx._meta import _Cisco_IOS_XR_dnx_driver_oper as meta
                                        return meta._meta_table['Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.PbcStatistics.PbcStats.StatsInfo']['meta_info']

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-dnx-driver-oper:pbc-stats'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.stats_info is not None and self.stats_info._has_data():
                                        return True

                                    if self.valid is not None:
                                        return True

                                    if self.rack_no is not None:
                                        return True

                                    if self.slot_no is not None:
                                        return True

                                    if self.asic_instance is not None:
                                        return True

                                    if self.chip_ver is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.dnx._meta import _Cisco_IOS_XR_dnx_driver_oper as meta
                                    return meta._meta_table['Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.PbcStatistics.PbcStats']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-dnx-driver-oper:pbc-statistics'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.pbc_stats is not None and self.pbc_stats._has_data():
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.dnx._meta import _Cisco_IOS_XR_dnx_driver_oper as meta
                                return meta._meta_table['Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.PbcStatistics']['meta_info']


                        class FmacStatistics(object):
                            """
                            Statistics of FMAC
                            
                            .. attribute:: fmac_links
                            
                            	Link table for statistics
                            	**type**\: :py:class:`FmacLinks <ydk.models.dnx.Cisco_IOS_XR_dnx_driver_oper.Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.FmacStatistics.FmacLinks>`
                            
                            

                            """

                            _prefix = 'dnx-driver-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.fmac_links = Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.FmacStatistics.FmacLinks()
                                self.fmac_links.parent = self


                            class FmacLinks(object):
                                """
                                Link table for statistics
                                
                                .. attribute:: fmac_link
                                
                                	Link number for statistics
                                	**type**\: list of :py:class:`FmacLink <ydk.models.dnx.Cisco_IOS_XR_dnx_driver_oper.Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.FmacStatistics.FmacLinks.FmacLink>`
                                
                                

                                """

                                _prefix = 'dnx-driver-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.fmac_link = YList()
                                    self.fmac_link.parent = self
                                    self.fmac_link.name = 'fmac_link'


                                class FmacLink(object):
                                    """
                                    Link number for statistics
                                    
                                    .. attribute:: link  <key>
                                    
                                    	Link number
                                    	**type**\: int
                                    
                                    	**range:** \-2147483648..2147483647
                                    
                                    .. attribute:: fmac_asic
                                    
                                    	Single aisc information
                                    	**type**\: list of :py:class:`FmacAsic <ydk.models.dnx.Cisco_IOS_XR_dnx_driver_oper.Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.FmacStatistics.FmacLinks.FmacLink.FmacAsic>`
                                    
                                    

                                    """

                                    _prefix = 'dnx-driver-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.link = None
                                        self.fmac_asic = YList()
                                        self.fmac_asic.parent = self
                                        self.fmac_asic.name = 'fmac_asic'


                                    class FmacAsic(object):
                                        """
                                        Single aisc information
                                        
                                        .. attribute:: asic  <key>
                                        
                                        	Single asic
                                        	**type**\: int
                                        
                                        	**range:** \-2147483648..2147483647
                                        
                                        .. attribute:: aggr_stats
                                        
                                        	aggr stats
                                        	**type**\: :py:class:`AggrStats <ydk.models.dnx.Cisco_IOS_XR_dnx_driver_oper.Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.FmacStatistics.FmacLinks.FmacLink.FmacAsic.AggrStats>`
                                        
                                        .. attribute:: incr_stats
                                        
                                        	incr stats
                                        	**type**\: :py:class:`IncrStats <ydk.models.dnx.Cisco_IOS_XR_dnx_driver_oper.Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.FmacStatistics.FmacLinks.FmacLink.FmacAsic.IncrStats>`
                                        
                                        .. attribute:: valid
                                        
                                        	valid
                                        	**type**\: bool
                                        
                                        .. attribute:: rack_no
                                        
                                        	rack no
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: slot_no
                                        
                                        	slot no
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: asic_instance
                                        
                                        	asic instance
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: link_no
                                        
                                        	link no
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: link_valid
                                        
                                        	link valid
                                        	**type**\: bool
                                        
                                        

                                        """

                                        _prefix = 'dnx-driver-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            self.parent = None
                                            self.asic = None
                                            self.aggr_stats = Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.FmacStatistics.FmacLinks.FmacLink.FmacAsic.AggrStats()
                                            self.aggr_stats.parent = self
                                            self.incr_stats = Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.FmacStatistics.FmacLinks.FmacLink.FmacAsic.IncrStats()
                                            self.incr_stats.parent = self
                                            self.valid = None
                                            self.rack_no = None
                                            self.slot_no = None
                                            self.asic_instance = None
                                            self.link_no = None
                                            self.link_valid = None


                                        class AggrStats(object):
                                            """
                                            aggr stats
                                            
                                            .. attribute:: link_error_status
                                            
                                            	link error status
                                            	**type**\: :py:class:`LinkErrorStatus <ydk.models.dnx.Cisco_IOS_XR_dnx_driver_oper.Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.FmacStatistics.FmacLinks.FmacLink.FmacAsic.AggrStats.LinkErrorStatus>`
                                            
                                            .. attribute:: link_counters
                                            
                                            	link counters
                                            	**type**\: :py:class:`LinkCounters <ydk.models.dnx.Cisco_IOS_XR_dnx_driver_oper.Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.FmacStatistics.FmacLinks.FmacLink.FmacAsic.AggrStats.LinkCounters>`
                                            
                                            .. attribute:: ovf_status
                                            
                                            	ovf status
                                            	**type**\: :py:class:`OvfStatus <ydk.models.dnx.Cisco_IOS_XR_dnx_driver_oper.Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.FmacStatistics.FmacLinks.FmacLink.FmacAsic.AggrStats.OvfStatus>`
                                            
                                            

                                            """

                                            _prefix = 'dnx-driver-oper'
                                            _revision = '2015-11-09'

                                            def __init__(self):
                                                self.parent = None
                                                self.link_error_status = Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.FmacStatistics.FmacLinks.FmacLink.FmacAsic.AggrStats.LinkErrorStatus()
                                                self.link_error_status.parent = self
                                                self.link_counters = Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.FmacStatistics.FmacLinks.FmacLink.FmacAsic.AggrStats.LinkCounters()
                                                self.link_counters.parent = self
                                                self.ovf_status = Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.FmacStatistics.FmacLinks.FmacLink.FmacAsic.AggrStats.OvfStatus()
                                                self.ovf_status.parent = self


                                            class LinkErrorStatus(object):
                                                """
                                                link error status
                                                
                                                .. attribute:: link_crc_error
                                                
                                                	link crc error
                                                	**type**\: int
                                                
                                                	**range:** 0..4294967295
                                                
                                                .. attribute:: link_size_error
                                                
                                                	link size error
                                                	**type**\: int
                                                
                                                	**range:** 0..4294967295
                                                
                                                .. attribute:: link_mis_align_error
                                                
                                                	link mis align error
                                                	**type**\: int
                                                
                                                	**range:** 0..4294967295
                                                
                                                .. attribute:: link_code_group_error
                                                
                                                	link code group error
                                                	**type**\: int
                                                
                                                	**range:** 0..4294967295
                                                
                                                .. attribute:: link_no_sig_lock_error
                                                
                                                	link no sig lock error
                                                	**type**\: int
                                                
                                                	**range:** 0..4294967295
                                                
                                                .. attribute:: link_no_sig_accept_error
                                                
                                                	link no sig accept error
                                                	**type**\: int
                                                
                                                	**range:** 0..4294967295
                                                
                                                .. attribute:: link_tokens_error
                                                
                                                	link tokens error
                                                	**type**\: int
                                                
                                                	**range:** 0..4294967295
                                                
                                                .. attribute:: error_token_count
                                                
                                                	error token count
                                                	**type**\: int
                                                
                                                	**range:** 0..4294967295
                                                
                                                

                                                """

                                                _prefix = 'dnx-driver-oper'
                                                _revision = '2015-11-09'

                                                def __init__(self):
                                                    self.parent = None
                                                    self.link_crc_error = None
                                                    self.link_size_error = None
                                                    self.link_mis_align_error = None
                                                    self.link_code_group_error = None
                                                    self.link_no_sig_lock_error = None
                                                    self.link_no_sig_accept_error = None
                                                    self.link_tokens_error = None
                                                    self.error_token_count = None

                                                @property
                                                def _common_path(self):
                                                    if self.parent is None:
                                                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                                    return self.parent._common_path +'/Cisco-IOS-XR-dnx-driver-oper:link-error-status'

                                                def is_config(self):
                                                    ''' Returns True if this instance represents config data else returns False '''
                                                    return False

                                                def _has_data(self):
                                                    if not self.is_config():
                                                        return False
                                                    if self.link_crc_error is not None:
                                                        return True

                                                    if self.link_size_error is not None:
                                                        return True

                                                    if self.link_mis_align_error is not None:
                                                        return True

                                                    if self.link_code_group_error is not None:
                                                        return True

                                                    if self.link_no_sig_lock_error is not None:
                                                        return True

                                                    if self.link_no_sig_accept_error is not None:
                                                        return True

                                                    if self.link_tokens_error is not None:
                                                        return True

                                                    if self.error_token_count is not None:
                                                        return True

                                                    return False

                                                @staticmethod
                                                def _meta_info():
                                                    from ydk.models.dnx._meta import _Cisco_IOS_XR_dnx_driver_oper as meta
                                                    return meta._meta_table['Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.FmacStatistics.FmacLinks.FmacLink.FmacAsic.AggrStats.LinkErrorStatus']['meta_info']


                                            class LinkCounters(object):
                                                """
                                                link counters
                                                
                                                .. attribute:: tx_control_cells_counter
                                                
                                                	TX Control cells counter
                                                	**type**\: int
                                                
                                                	**range:** 0..18446744073709551615
                                                
                                                .. attribute:: tx_data_cell_counter
                                                
                                                	TX Data cell counter
                                                	**type**\: int
                                                
                                                	**range:** 0..18446744073709551615
                                                
                                                .. attribute:: tx_data_byte_counter
                                                
                                                	TX Data byte counter
                                                	**type**\: int
                                                
                                                	**range:** 0..18446744073709551615
                                                
                                                .. attribute:: rx_crc_errors_counter
                                                
                                                	RX CRC errors counter
                                                	**type**\: int
                                                
                                                	**range:** 0..18446744073709551615
                                                
                                                .. attribute:: rx_lfec_fec_correctable_error
                                                
                                                	RX LFEC FEC correctable error
                                                	**type**\: int
                                                
                                                	**range:** 0..18446744073709551615
                                                
                                                .. attribute:: rx_8b_10b_disparity_errors
                                                
                                                	RX 8b 10b disparity errors
                                                	**type**\: int
                                                
                                                	**range:** 0..18446744073709551615
                                                
                                                .. attribute:: rx_control_cells_counter
                                                
                                                	RX Control cells counter
                                                	**type**\: int
                                                
                                                	**range:** 0..18446744073709551615
                                                
                                                .. attribute:: rx_data_cell_counter
                                                
                                                	RX Data cell counter
                                                	**type**\: int
                                                
                                                	**range:** 0..18446744073709551615
                                                
                                                .. attribute:: rx_data_byte_counter
                                                
                                                	RX Data byte counter
                                                	**type**\: int
                                                
                                                	**range:** 0..18446744073709551615
                                                
                                                .. attribute:: rx_dropped_retransmitted_control
                                                
                                                	RX dropped retransmitted control
                                                	**type**\: int
                                                
                                                	**range:** 0..18446744073709551615
                                                
                                                .. attribute:: tx_asyn_fifo_rate
                                                
                                                	TX Asyn fifo rate
                                                	**type**\: int
                                                
                                                	**range:** 0..18446744073709551615
                                                
                                                .. attribute:: rx_asyn_fifo_rate
                                                
                                                	RX Asyn fifo rate
                                                	**type**\: int
                                                
                                                	**range:** 0..18446744073709551615
                                                
                                                .. attribute:: rx_lfec_fec_uncorrectable_errors
                                                
                                                	RX LFEC FEC uncorrectable errors
                                                	**type**\: int
                                                
                                                	**range:** 0..18446744073709551615
                                                
                                                .. attribute:: rx_8b_10b_code_errors
                                                
                                                	RX 8b 10b code errors
                                                	**type**\: int
                                                
                                                	**range:** 0..18446744073709551615
                                                
                                                

                                                """

                                                _prefix = 'dnx-driver-oper'
                                                _revision = '2015-11-09'

                                                def __init__(self):
                                                    self.parent = None
                                                    self.tx_control_cells_counter = None
                                                    self.tx_data_cell_counter = None
                                                    self.tx_data_byte_counter = None
                                                    self.rx_crc_errors_counter = None
                                                    self.rx_lfec_fec_correctable_error = None
                                                    self.rx_8b_10b_disparity_errors = None
                                                    self.rx_control_cells_counter = None
                                                    self.rx_data_cell_counter = None
                                                    self.rx_data_byte_counter = None
                                                    self.rx_dropped_retransmitted_control = None
                                                    self.tx_asyn_fifo_rate = None
                                                    self.rx_asyn_fifo_rate = None
                                                    self.rx_lfec_fec_uncorrectable_errors = None
                                                    self.rx_8b_10b_code_errors = None

                                                @property
                                                def _common_path(self):
                                                    if self.parent is None:
                                                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                                    return self.parent._common_path +'/Cisco-IOS-XR-dnx-driver-oper:link-counters'

                                                def is_config(self):
                                                    ''' Returns True if this instance represents config data else returns False '''
                                                    return False

                                                def _has_data(self):
                                                    if not self.is_config():
                                                        return False
                                                    if self.tx_control_cells_counter is not None:
                                                        return True

                                                    if self.tx_data_cell_counter is not None:
                                                        return True

                                                    if self.tx_data_byte_counter is not None:
                                                        return True

                                                    if self.rx_crc_errors_counter is not None:
                                                        return True

                                                    if self.rx_lfec_fec_correctable_error is not None:
                                                        return True

                                                    if self.rx_8b_10b_disparity_errors is not None:
                                                        return True

                                                    if self.rx_control_cells_counter is not None:
                                                        return True

                                                    if self.rx_data_cell_counter is not None:
                                                        return True

                                                    if self.rx_data_byte_counter is not None:
                                                        return True

                                                    if self.rx_dropped_retransmitted_control is not None:
                                                        return True

                                                    if self.tx_asyn_fifo_rate is not None:
                                                        return True

                                                    if self.rx_asyn_fifo_rate is not None:
                                                        return True

                                                    if self.rx_lfec_fec_uncorrectable_errors is not None:
                                                        return True

                                                    if self.rx_8b_10b_code_errors is not None:
                                                        return True

                                                    return False

                                                @staticmethod
                                                def _meta_info():
                                                    from ydk.models.dnx._meta import _Cisco_IOS_XR_dnx_driver_oper as meta
                                                    return meta._meta_table['Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.FmacStatistics.FmacLinks.FmacLink.FmacAsic.AggrStats.LinkCounters']['meta_info']


                                            class OvfStatus(object):
                                                """
                                                ovf status
                                                
                                                .. attribute:: tx_control_cells_counter
                                                
                                                	TX Control cells counter
                                                	**type**\: str
                                                
                                                	**range:** 0..6
                                                
                                                .. attribute:: tx_data_cell_counter
                                                
                                                	TX Data cell counter
                                                	**type**\: str
                                                
                                                	**range:** 0..6
                                                
                                                .. attribute:: tx_data_byte_counter
                                                
                                                	TX Data byte counter
                                                	**type**\: str
                                                
                                                	**range:** 0..6
                                                
                                                .. attribute:: rx_crc_errors_counter
                                                
                                                	RX CRC errors counter
                                                	**type**\: str
                                                
                                                	**range:** 0..6
                                                
                                                .. attribute:: rx_lfec_fec_correctable_error
                                                
                                                	RX LFEC FEC correctable error
                                                	**type**\: str
                                                
                                                	**range:** 0..6
                                                
                                                .. attribute:: rx_8b_10b_disparity_errors
                                                
                                                	RX 8b 10b disparity errors
                                                	**type**\: str
                                                
                                                	**range:** 0..6
                                                
                                                .. attribute:: rx_control_cells_counter
                                                
                                                	RX Control cells counter
                                                	**type**\: str
                                                
                                                	**range:** 0..6
                                                
                                                .. attribute:: rx_data_cell_counter
                                                
                                                	RX Data cell counter
                                                	**type**\: str
                                                
                                                	**range:** 0..6
                                                
                                                .. attribute:: rx_data_byte_counter
                                                
                                                	RX Data byte counter
                                                	**type**\: str
                                                
                                                	**range:** 0..6
                                                
                                                .. attribute:: rx_dropped_retransmitted_control
                                                
                                                	RX dropped retransmitted control
                                                	**type**\: str
                                                
                                                	**range:** 0..6
                                                
                                                .. attribute:: tx_asyn_fifo_rate
                                                
                                                	TX Asyn fifo rate
                                                	**type**\: str
                                                
                                                	**range:** 0..6
                                                
                                                .. attribute:: rx_asyn_fifo_rate
                                                
                                                	RX Asyn fifo rate
                                                	**type**\: str
                                                
                                                	**range:** 0..6
                                                
                                                .. attribute:: rx_lfec_fec_uncorrectable_errors
                                                
                                                	RX LFEC FEC uncorrectable errors
                                                	**type**\: str
                                                
                                                	**range:** 0..6
                                                
                                                .. attribute:: rx_8b_10b_code_errors
                                                
                                                	RX 8b 10b code errors
                                                	**type**\: str
                                                
                                                	**range:** 0..6
                                                
                                                

                                                """

                                                _prefix = 'dnx-driver-oper'
                                                _revision = '2015-11-09'

                                                def __init__(self):
                                                    self.parent = None
                                                    self.tx_control_cells_counter = None
                                                    self.tx_data_cell_counter = None
                                                    self.tx_data_byte_counter = None
                                                    self.rx_crc_errors_counter = None
                                                    self.rx_lfec_fec_correctable_error = None
                                                    self.rx_8b_10b_disparity_errors = None
                                                    self.rx_control_cells_counter = None
                                                    self.rx_data_cell_counter = None
                                                    self.rx_data_byte_counter = None
                                                    self.rx_dropped_retransmitted_control = None
                                                    self.tx_asyn_fifo_rate = None
                                                    self.rx_asyn_fifo_rate = None
                                                    self.rx_lfec_fec_uncorrectable_errors = None
                                                    self.rx_8b_10b_code_errors = None

                                                @property
                                                def _common_path(self):
                                                    if self.parent is None:
                                                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                                    return self.parent._common_path +'/Cisco-IOS-XR-dnx-driver-oper:ovf-status'

                                                def is_config(self):
                                                    ''' Returns True if this instance represents config data else returns False '''
                                                    return False

                                                def _has_data(self):
                                                    if not self.is_config():
                                                        return False
                                                    if self.tx_control_cells_counter is not None:
                                                        return True

                                                    if self.tx_data_cell_counter is not None:
                                                        return True

                                                    if self.tx_data_byte_counter is not None:
                                                        return True

                                                    if self.rx_crc_errors_counter is not None:
                                                        return True

                                                    if self.rx_lfec_fec_correctable_error is not None:
                                                        return True

                                                    if self.rx_8b_10b_disparity_errors is not None:
                                                        return True

                                                    if self.rx_control_cells_counter is not None:
                                                        return True

                                                    if self.rx_data_cell_counter is not None:
                                                        return True

                                                    if self.rx_data_byte_counter is not None:
                                                        return True

                                                    if self.rx_dropped_retransmitted_control is not None:
                                                        return True

                                                    if self.tx_asyn_fifo_rate is not None:
                                                        return True

                                                    if self.rx_asyn_fifo_rate is not None:
                                                        return True

                                                    if self.rx_lfec_fec_uncorrectable_errors is not None:
                                                        return True

                                                    if self.rx_8b_10b_code_errors is not None:
                                                        return True

                                                    return False

                                                @staticmethod
                                                def _meta_info():
                                                    from ydk.models.dnx._meta import _Cisco_IOS_XR_dnx_driver_oper as meta
                                                    return meta._meta_table['Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.FmacStatistics.FmacLinks.FmacLink.FmacAsic.AggrStats.OvfStatus']['meta_info']

                                            @property
                                            def _common_path(self):
                                                if self.parent is None:
                                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                                return self.parent._common_path +'/Cisco-IOS-XR-dnx-driver-oper:aggr-stats'

                                            def is_config(self):
                                                ''' Returns True if this instance represents config data else returns False '''
                                                return False

                                            def _has_data(self):
                                                if not self.is_config():
                                                    return False
                                                if self.link_error_status is not None and self.link_error_status._has_data():
                                                    return True

                                                if self.link_counters is not None and self.link_counters._has_data():
                                                    return True

                                                if self.ovf_status is not None and self.ovf_status._has_data():
                                                    return True

                                                return False

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.dnx._meta import _Cisco_IOS_XR_dnx_driver_oper as meta
                                                return meta._meta_table['Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.FmacStatistics.FmacLinks.FmacLink.FmacAsic.AggrStats']['meta_info']


                                        class IncrStats(object):
                                            """
                                            incr stats
                                            
                                            .. attribute:: link_error_status
                                            
                                            	link error status
                                            	**type**\: :py:class:`LinkErrorStatus <ydk.models.dnx.Cisco_IOS_XR_dnx_driver_oper.Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.FmacStatistics.FmacLinks.FmacLink.FmacAsic.IncrStats.LinkErrorStatus>`
                                            
                                            .. attribute:: link_counters
                                            
                                            	link counters
                                            	**type**\: :py:class:`LinkCounters <ydk.models.dnx.Cisco_IOS_XR_dnx_driver_oper.Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.FmacStatistics.FmacLinks.FmacLink.FmacAsic.IncrStats.LinkCounters>`
                                            
                                            .. attribute:: ovf_status
                                            
                                            	ovf status
                                            	**type**\: :py:class:`OvfStatus <ydk.models.dnx.Cisco_IOS_XR_dnx_driver_oper.Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.FmacStatistics.FmacLinks.FmacLink.FmacAsic.IncrStats.OvfStatus>`
                                            
                                            

                                            """

                                            _prefix = 'dnx-driver-oper'
                                            _revision = '2015-11-09'

                                            def __init__(self):
                                                self.parent = None
                                                self.link_error_status = Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.FmacStatistics.FmacLinks.FmacLink.FmacAsic.IncrStats.LinkErrorStatus()
                                                self.link_error_status.parent = self
                                                self.link_counters = Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.FmacStatistics.FmacLinks.FmacLink.FmacAsic.IncrStats.LinkCounters()
                                                self.link_counters.parent = self
                                                self.ovf_status = Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.FmacStatistics.FmacLinks.FmacLink.FmacAsic.IncrStats.OvfStatus()
                                                self.ovf_status.parent = self


                                            class LinkErrorStatus(object):
                                                """
                                                link error status
                                                
                                                .. attribute:: link_crc_error
                                                
                                                	link crc error
                                                	**type**\: int
                                                
                                                	**range:** 0..4294967295
                                                
                                                .. attribute:: link_size_error
                                                
                                                	link size error
                                                	**type**\: int
                                                
                                                	**range:** 0..4294967295
                                                
                                                .. attribute:: link_mis_align_error
                                                
                                                	link mis align error
                                                	**type**\: int
                                                
                                                	**range:** 0..4294967295
                                                
                                                .. attribute:: link_code_group_error
                                                
                                                	link code group error
                                                	**type**\: int
                                                
                                                	**range:** 0..4294967295
                                                
                                                .. attribute:: link_no_sig_lock_error
                                                
                                                	link no sig lock error
                                                	**type**\: int
                                                
                                                	**range:** 0..4294967295
                                                
                                                .. attribute:: link_no_sig_accept_error
                                                
                                                	link no sig accept error
                                                	**type**\: int
                                                
                                                	**range:** 0..4294967295
                                                
                                                .. attribute:: link_tokens_error
                                                
                                                	link tokens error
                                                	**type**\: int
                                                
                                                	**range:** 0..4294967295
                                                
                                                .. attribute:: error_token_count
                                                
                                                	error token count
                                                	**type**\: int
                                                
                                                	**range:** 0..4294967295
                                                
                                                

                                                """

                                                _prefix = 'dnx-driver-oper'
                                                _revision = '2015-11-09'

                                                def __init__(self):
                                                    self.parent = None
                                                    self.link_crc_error = None
                                                    self.link_size_error = None
                                                    self.link_mis_align_error = None
                                                    self.link_code_group_error = None
                                                    self.link_no_sig_lock_error = None
                                                    self.link_no_sig_accept_error = None
                                                    self.link_tokens_error = None
                                                    self.error_token_count = None

                                                @property
                                                def _common_path(self):
                                                    if self.parent is None:
                                                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                                    return self.parent._common_path +'/Cisco-IOS-XR-dnx-driver-oper:link-error-status'

                                                def is_config(self):
                                                    ''' Returns True if this instance represents config data else returns False '''
                                                    return False

                                                def _has_data(self):
                                                    if not self.is_config():
                                                        return False
                                                    if self.link_crc_error is not None:
                                                        return True

                                                    if self.link_size_error is not None:
                                                        return True

                                                    if self.link_mis_align_error is not None:
                                                        return True

                                                    if self.link_code_group_error is not None:
                                                        return True

                                                    if self.link_no_sig_lock_error is not None:
                                                        return True

                                                    if self.link_no_sig_accept_error is not None:
                                                        return True

                                                    if self.link_tokens_error is not None:
                                                        return True

                                                    if self.error_token_count is not None:
                                                        return True

                                                    return False

                                                @staticmethod
                                                def _meta_info():
                                                    from ydk.models.dnx._meta import _Cisco_IOS_XR_dnx_driver_oper as meta
                                                    return meta._meta_table['Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.FmacStatistics.FmacLinks.FmacLink.FmacAsic.IncrStats.LinkErrorStatus']['meta_info']


                                            class LinkCounters(object):
                                                """
                                                link counters
                                                
                                                .. attribute:: tx_control_cells_counter
                                                
                                                	TX Control cells counter
                                                	**type**\: int
                                                
                                                	**range:** 0..18446744073709551615
                                                
                                                .. attribute:: tx_data_cell_counter
                                                
                                                	TX Data cell counter
                                                	**type**\: int
                                                
                                                	**range:** 0..18446744073709551615
                                                
                                                .. attribute:: tx_data_byte_counter
                                                
                                                	TX Data byte counter
                                                	**type**\: int
                                                
                                                	**range:** 0..18446744073709551615
                                                
                                                .. attribute:: rx_crc_errors_counter
                                                
                                                	RX CRC errors counter
                                                	**type**\: int
                                                
                                                	**range:** 0..18446744073709551615
                                                
                                                .. attribute:: rx_lfec_fec_correctable_error
                                                
                                                	RX LFEC FEC correctable error
                                                	**type**\: int
                                                
                                                	**range:** 0..18446744073709551615
                                                
                                                .. attribute:: rx_8b_10b_disparity_errors
                                                
                                                	RX 8b 10b disparity errors
                                                	**type**\: int
                                                
                                                	**range:** 0..18446744073709551615
                                                
                                                .. attribute:: rx_control_cells_counter
                                                
                                                	RX Control cells counter
                                                	**type**\: int
                                                
                                                	**range:** 0..18446744073709551615
                                                
                                                .. attribute:: rx_data_cell_counter
                                                
                                                	RX Data cell counter
                                                	**type**\: int
                                                
                                                	**range:** 0..18446744073709551615
                                                
                                                .. attribute:: rx_data_byte_counter
                                                
                                                	RX Data byte counter
                                                	**type**\: int
                                                
                                                	**range:** 0..18446744073709551615
                                                
                                                .. attribute:: rx_dropped_retransmitted_control
                                                
                                                	RX dropped retransmitted control
                                                	**type**\: int
                                                
                                                	**range:** 0..18446744073709551615
                                                
                                                .. attribute:: tx_asyn_fifo_rate
                                                
                                                	TX Asyn fifo rate
                                                	**type**\: int
                                                
                                                	**range:** 0..18446744073709551615
                                                
                                                .. attribute:: rx_asyn_fifo_rate
                                                
                                                	RX Asyn fifo rate
                                                	**type**\: int
                                                
                                                	**range:** 0..18446744073709551615
                                                
                                                .. attribute:: rx_lfec_fec_uncorrectable_errors
                                                
                                                	RX LFEC FEC uncorrectable errors
                                                	**type**\: int
                                                
                                                	**range:** 0..18446744073709551615
                                                
                                                .. attribute:: rx_8b_10b_code_errors
                                                
                                                	RX 8b 10b code errors
                                                	**type**\: int
                                                
                                                	**range:** 0..18446744073709551615
                                                
                                                

                                                """

                                                _prefix = 'dnx-driver-oper'
                                                _revision = '2015-11-09'

                                                def __init__(self):
                                                    self.parent = None
                                                    self.tx_control_cells_counter = None
                                                    self.tx_data_cell_counter = None
                                                    self.tx_data_byte_counter = None
                                                    self.rx_crc_errors_counter = None
                                                    self.rx_lfec_fec_correctable_error = None
                                                    self.rx_8b_10b_disparity_errors = None
                                                    self.rx_control_cells_counter = None
                                                    self.rx_data_cell_counter = None
                                                    self.rx_data_byte_counter = None
                                                    self.rx_dropped_retransmitted_control = None
                                                    self.tx_asyn_fifo_rate = None
                                                    self.rx_asyn_fifo_rate = None
                                                    self.rx_lfec_fec_uncorrectable_errors = None
                                                    self.rx_8b_10b_code_errors = None

                                                @property
                                                def _common_path(self):
                                                    if self.parent is None:
                                                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                                    return self.parent._common_path +'/Cisco-IOS-XR-dnx-driver-oper:link-counters'

                                                def is_config(self):
                                                    ''' Returns True if this instance represents config data else returns False '''
                                                    return False

                                                def _has_data(self):
                                                    if not self.is_config():
                                                        return False
                                                    if self.tx_control_cells_counter is not None:
                                                        return True

                                                    if self.tx_data_cell_counter is not None:
                                                        return True

                                                    if self.tx_data_byte_counter is not None:
                                                        return True

                                                    if self.rx_crc_errors_counter is not None:
                                                        return True

                                                    if self.rx_lfec_fec_correctable_error is not None:
                                                        return True

                                                    if self.rx_8b_10b_disparity_errors is not None:
                                                        return True

                                                    if self.rx_control_cells_counter is not None:
                                                        return True

                                                    if self.rx_data_cell_counter is not None:
                                                        return True

                                                    if self.rx_data_byte_counter is not None:
                                                        return True

                                                    if self.rx_dropped_retransmitted_control is not None:
                                                        return True

                                                    if self.tx_asyn_fifo_rate is not None:
                                                        return True

                                                    if self.rx_asyn_fifo_rate is not None:
                                                        return True

                                                    if self.rx_lfec_fec_uncorrectable_errors is not None:
                                                        return True

                                                    if self.rx_8b_10b_code_errors is not None:
                                                        return True

                                                    return False

                                                @staticmethod
                                                def _meta_info():
                                                    from ydk.models.dnx._meta import _Cisco_IOS_XR_dnx_driver_oper as meta
                                                    return meta._meta_table['Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.FmacStatistics.FmacLinks.FmacLink.FmacAsic.IncrStats.LinkCounters']['meta_info']


                                            class OvfStatus(object):
                                                """
                                                ovf status
                                                
                                                .. attribute:: tx_control_cells_counter
                                                
                                                	TX Control cells counter
                                                	**type**\: str
                                                
                                                	**range:** 0..6
                                                
                                                .. attribute:: tx_data_cell_counter
                                                
                                                	TX Data cell counter
                                                	**type**\: str
                                                
                                                	**range:** 0..6
                                                
                                                .. attribute:: tx_data_byte_counter
                                                
                                                	TX Data byte counter
                                                	**type**\: str
                                                
                                                	**range:** 0..6
                                                
                                                .. attribute:: rx_crc_errors_counter
                                                
                                                	RX CRC errors counter
                                                	**type**\: str
                                                
                                                	**range:** 0..6
                                                
                                                .. attribute:: rx_lfec_fec_correctable_error
                                                
                                                	RX LFEC FEC correctable error
                                                	**type**\: str
                                                
                                                	**range:** 0..6
                                                
                                                .. attribute:: rx_8b_10b_disparity_errors
                                                
                                                	RX 8b 10b disparity errors
                                                	**type**\: str
                                                
                                                	**range:** 0..6
                                                
                                                .. attribute:: rx_control_cells_counter
                                                
                                                	RX Control cells counter
                                                	**type**\: str
                                                
                                                	**range:** 0..6
                                                
                                                .. attribute:: rx_data_cell_counter
                                                
                                                	RX Data cell counter
                                                	**type**\: str
                                                
                                                	**range:** 0..6
                                                
                                                .. attribute:: rx_data_byte_counter
                                                
                                                	RX Data byte counter
                                                	**type**\: str
                                                
                                                	**range:** 0..6
                                                
                                                .. attribute:: rx_dropped_retransmitted_control
                                                
                                                	RX dropped retransmitted control
                                                	**type**\: str
                                                
                                                	**range:** 0..6
                                                
                                                .. attribute:: tx_asyn_fifo_rate
                                                
                                                	TX Asyn fifo rate
                                                	**type**\: str
                                                
                                                	**range:** 0..6
                                                
                                                .. attribute:: rx_asyn_fifo_rate
                                                
                                                	RX Asyn fifo rate
                                                	**type**\: str
                                                
                                                	**range:** 0..6
                                                
                                                .. attribute:: rx_lfec_fec_uncorrectable_errors
                                                
                                                	RX LFEC FEC uncorrectable errors
                                                	**type**\: str
                                                
                                                	**range:** 0..6
                                                
                                                .. attribute:: rx_8b_10b_code_errors
                                                
                                                	RX 8b 10b code errors
                                                	**type**\: str
                                                
                                                	**range:** 0..6
                                                
                                                

                                                """

                                                _prefix = 'dnx-driver-oper'
                                                _revision = '2015-11-09'

                                                def __init__(self):
                                                    self.parent = None
                                                    self.tx_control_cells_counter = None
                                                    self.tx_data_cell_counter = None
                                                    self.tx_data_byte_counter = None
                                                    self.rx_crc_errors_counter = None
                                                    self.rx_lfec_fec_correctable_error = None
                                                    self.rx_8b_10b_disparity_errors = None
                                                    self.rx_control_cells_counter = None
                                                    self.rx_data_cell_counter = None
                                                    self.rx_data_byte_counter = None
                                                    self.rx_dropped_retransmitted_control = None
                                                    self.tx_asyn_fifo_rate = None
                                                    self.rx_asyn_fifo_rate = None
                                                    self.rx_lfec_fec_uncorrectable_errors = None
                                                    self.rx_8b_10b_code_errors = None

                                                @property
                                                def _common_path(self):
                                                    if self.parent is None:
                                                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                                    return self.parent._common_path +'/Cisco-IOS-XR-dnx-driver-oper:ovf-status'

                                                def is_config(self):
                                                    ''' Returns True if this instance represents config data else returns False '''
                                                    return False

                                                def _has_data(self):
                                                    if not self.is_config():
                                                        return False
                                                    if self.tx_control_cells_counter is not None:
                                                        return True

                                                    if self.tx_data_cell_counter is not None:
                                                        return True

                                                    if self.tx_data_byte_counter is not None:
                                                        return True

                                                    if self.rx_crc_errors_counter is not None:
                                                        return True

                                                    if self.rx_lfec_fec_correctable_error is not None:
                                                        return True

                                                    if self.rx_8b_10b_disparity_errors is not None:
                                                        return True

                                                    if self.rx_control_cells_counter is not None:
                                                        return True

                                                    if self.rx_data_cell_counter is not None:
                                                        return True

                                                    if self.rx_data_byte_counter is not None:
                                                        return True

                                                    if self.rx_dropped_retransmitted_control is not None:
                                                        return True

                                                    if self.tx_asyn_fifo_rate is not None:
                                                        return True

                                                    if self.rx_asyn_fifo_rate is not None:
                                                        return True

                                                    if self.rx_lfec_fec_uncorrectable_errors is not None:
                                                        return True

                                                    if self.rx_8b_10b_code_errors is not None:
                                                        return True

                                                    return False

                                                @staticmethod
                                                def _meta_info():
                                                    from ydk.models.dnx._meta import _Cisco_IOS_XR_dnx_driver_oper as meta
                                                    return meta._meta_table['Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.FmacStatistics.FmacLinks.FmacLink.FmacAsic.IncrStats.OvfStatus']['meta_info']

                                            @property
                                            def _common_path(self):
                                                if self.parent is None:
                                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                                return self.parent._common_path +'/Cisco-IOS-XR-dnx-driver-oper:incr-stats'

                                            def is_config(self):
                                                ''' Returns True if this instance represents config data else returns False '''
                                                return False

                                            def _has_data(self):
                                                if not self.is_config():
                                                    return False
                                                if self.link_error_status is not None and self.link_error_status._has_data():
                                                    return True

                                                if self.link_counters is not None and self.link_counters._has_data():
                                                    return True

                                                if self.ovf_status is not None and self.ovf_status._has_data():
                                                    return True

                                                return False

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.dnx._meta import _Cisco_IOS_XR_dnx_driver_oper as meta
                                                return meta._meta_table['Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.FmacStatistics.FmacLinks.FmacLink.FmacAsic.IncrStats']['meta_info']

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYDataValidationError('parent is not set . Cannot derive path.')
                                            if self.asic is None:
                                                raise YPYDataValidationError('Key property asic is None')

                                            return self.parent._common_path +'/Cisco-IOS-XR-dnx-driver-oper:fmac-asic[Cisco-IOS-XR-dnx-driver-oper:asic = ' + str(self.asic) + ']'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return False

                                        def _has_data(self):
                                            if not self.is_config():
                                                return False
                                            if self.asic is not None:
                                                return True

                                            if self.aggr_stats is not None and self.aggr_stats._has_data():
                                                return True

                                            if self.incr_stats is not None and self.incr_stats._has_data():
                                                return True

                                            if self.valid is not None:
                                                return True

                                            if self.rack_no is not None:
                                                return True

                                            if self.slot_no is not None:
                                                return True

                                            if self.asic_instance is not None:
                                                return True

                                            if self.link_no is not None:
                                                return True

                                            if self.link_valid is not None:
                                                return True

                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.dnx._meta import _Cisco_IOS_XR_dnx_driver_oper as meta
                                            return meta._meta_table['Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.FmacStatistics.FmacLinks.FmacLink.FmacAsic']['meta_info']

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYDataValidationError('parent is not set . Cannot derive path.')
                                        if self.link is None:
                                            raise YPYDataValidationError('Key property link is None')

                                        return self.parent._common_path +'/Cisco-IOS-XR-dnx-driver-oper:fmac-link[Cisco-IOS-XR-dnx-driver-oper:link = ' + str(self.link) + ']'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        if not self.is_config():
                                            return False
                                        if self.link is not None:
                                            return True

                                        if self.fmac_asic is not None:
                                            for child_ref in self.fmac_asic:
                                                if child_ref._has_data():
                                                    return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.dnx._meta import _Cisco_IOS_XR_dnx_driver_oper as meta
                                        return meta._meta_table['Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.FmacStatistics.FmacLinks.FmacLink']['meta_info']

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-dnx-driver-oper:fmac-links'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.fmac_link is not None:
                                        for child_ref in self.fmac_link:
                                            if child_ref._has_data():
                                                return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.dnx._meta import _Cisco_IOS_XR_dnx_driver_oper as meta
                                    return meta._meta_table['Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.FmacStatistics.FmacLinks']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-dnx-driver-oper:fmac-statistics'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.fmac_links is not None and self.fmac_links._has_data():
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.dnx._meta import _Cisco_IOS_XR_dnx_driver_oper as meta
                                return meta._meta_table['Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.FmacStatistics']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')
                            if self.instance is None:
                                raise YPYDataValidationError('Key property instance is None')

                            return self.parent._common_path +'/Cisco-IOS-XR-dnx-driver-oper:statistics-asic-instance[Cisco-IOS-XR-dnx-driver-oper:instance = ' + str(self.instance) + ']'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.instance is not None:
                                return True

                            if self.pbc_statistics is not None and self.pbc_statistics._has_data():
                                return True

                            if self.fmac_statistics is not None and self.fmac_statistics._has_data():
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.dnx._meta import _Cisco_IOS_XR_dnx_driver_oper as meta
                            return meta._meta_table['Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-dnx-driver-oper:statistics-asic-instances'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.statistics_asic_instance is not None:
                            for child_ref in self.statistics_asic_instance:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.dnx._meta import _Cisco_IOS_XR_dnx_driver_oper as meta
                        return meta._meta_table['Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-dnx-driver-oper:asic-statistics'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.statistics_asic_instances is not None and self.statistics_asic_instances._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.dnx._meta import _Cisco_IOS_XR_dnx_driver_oper as meta
                    return meta._meta_table['Fia.Nodes.Node.AsicStatistics']['meta_info']

            @property
            def _common_path(self):
                if self.node_name is None:
                    raise YPYDataValidationError('Key property node_name is None')

                return '/Cisco-IOS-XR-dnx-driver-oper:fia/Cisco-IOS-XR-dnx-driver-oper:nodes/Cisco-IOS-XR-dnx-driver-oper:node[Cisco-IOS-XR-dnx-driver-oper:node-name = ' + str(self.node_name) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.node_name is not None:
                    return True

                if self.rx_link_information is not None and self.rx_link_information._has_data():
                    return True

                if self.driver_information is not None and self.driver_information._has_data():
                    return True

                if self.clear_statistics is not None and self.clear_statistics._has_data():
                    return True

                if self.tx_link_information is not None and self.tx_link_information._has_data():
                    return True

                if self.register_dump is not None and self.register_dump._has_data():
                    return True

                if self.diag_shell is not None and self.diag_shell._has_data():
                    return True

                if self.oir_history is not None and self.oir_history._has_data():
                    return True

                if self.asic_statistics is not None and self.asic_statistics._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.dnx._meta import _Cisco_IOS_XR_dnx_driver_oper as meta
                return meta._meta_table['Fia.Nodes.Node']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-dnx-driver-oper:fia/Cisco-IOS-XR-dnx-driver-oper:nodes'

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
            from ydk.models.dnx._meta import _Cisco_IOS_XR_dnx_driver_oper as meta
            return meta._meta_table['Fia.Nodes']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-dnx-driver-oper:fia'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if not self.is_config():
            return False
        if self.nodes is not None and self.nodes._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.dnx._meta import _Cisco_IOS_XR_dnx_driver_oper as meta
        return meta._meta_table['Fia']['meta_info']


