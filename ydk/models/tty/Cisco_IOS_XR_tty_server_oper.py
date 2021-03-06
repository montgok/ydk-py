""" Cisco_IOS_XR_tty_server_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR tty\-server package operational data.

This module contains definitions
for the following management objects\:
  tty\: TTY Line Configuration

Copyright (c) 2013\-2015 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYDataValidationError


from ydk.models.tty.Cisco_IOS_XR_tty_management_datatypes import TtyTransportProtocolEnum
from ydk.models.tty.Cisco_IOS_XR_tty_management_datatypes import TtyTransportProtocolSelectEnum
from ydk.models.tty.Cisco_IOS_XR_tty_management_oper import HostAfIdBase_Identity
from ydk.models.tty.Cisco_IOS_XR_tty_management_oper import TransportServiceEnum

class LineStateEnum(Enum):
    """
    LineStateEnum

    Line state

    .. data:: NONE = 0

    	Line not connected

    .. data:: REGISTERED = 1

    	Line registered

    .. data:: IN_USE = 2

    	Line active and in use

    """

    NONE = 0

    REGISTERED = 1

    IN_USE = 2


    @staticmethod
    def _meta_info():
        from ydk.models.tty._meta import _Cisco_IOS_XR_tty_server_oper as meta
        return meta._meta_table['LineStateEnum']


class SessionOperationEnum(Enum):
    """
    SessionOperationEnum

    Session operation

    .. data:: NONE = 0

    	No sessions on the line

    .. data:: SETUP = 1

    	Session getting set up

    .. data:: SHELL = 2

    	Session active with a shell

    .. data:: TRANSITIONING = 3

    	Session in transitioning phase

    .. data:: PACKET = 4

    	Session ready to receive packets

    """

    NONE = 0

    SETUP = 1

    SHELL = 2

    TRANSITIONING = 3

    PACKET = 4


    @staticmethod
    def _meta_info():
        from ydk.models.tty._meta import _Cisco_IOS_XR_tty_server_oper as meta
        return meta._meta_table['SessionOperationEnum']



class Tty(object):
    """
    TTY Line Configuration
    
    .. attribute:: console_nodes
    
    	List of Nodes for console
    	**type**\: :py:class:`ConsoleNodes <ydk.models.tty.Cisco_IOS_XR_tty_server_oper.Tty.ConsoleNodes>`
    
    .. attribute:: vty_lines
    
    	List of VTY lines
    	**type**\: :py:class:`VtyLines <ydk.models.tty.Cisco_IOS_XR_tty_server_oper.Tty.VtyLines>`
    
    .. attribute:: auxiliary_nodes
    
    	List of Nodes attached with an auxiliary line
    	**type**\: :py:class:`AuxiliaryNodes <ydk.models.tty.Cisco_IOS_XR_tty_server_oper.Tty.AuxiliaryNodes>`
    
    

    """

    _prefix = 'tty-server-oper'
    _revision = '2015-07-30'

    def __init__(self):
        self.console_nodes = Tty.ConsoleNodes()
        self.console_nodes.parent = self
        self.vty_lines = Tty.VtyLines()
        self.vty_lines.parent = self
        self.auxiliary_nodes = Tty.AuxiliaryNodes()
        self.auxiliary_nodes.parent = self


    class ConsoleNodes(object):
        """
        List of Nodes for console
        
        .. attribute:: console_node
        
        	Console line configuration on a node
        	**type**\: list of :py:class:`ConsoleNode <ydk.models.tty.Cisco_IOS_XR_tty_server_oper.Tty.ConsoleNodes.ConsoleNode>`
        
        

        """

        _prefix = 'tty-server-oper'
        _revision = '2015-07-30'

        def __init__(self):
            self.parent = None
            self.console_node = YList()
            self.console_node.parent = self
            self.console_node.name = 'console_node'


        class ConsoleNode(object):
            """
            Console line configuration on a node
            
            .. attribute:: id  <key>
            
            	Node ID
            	**type**\: str
            
            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
            
            .. attribute:: console_line
            
            	Console line
            	**type**\: :py:class:`ConsoleLine <ydk.models.tty.Cisco_IOS_XR_tty_server_oper.Tty.ConsoleNodes.ConsoleNode.ConsoleLine>`
            
            

            """

            _prefix = 'tty-server-oper'
            _revision = '2015-07-30'

            def __init__(self):
                self.parent = None
                self.id = None
                self.console_line = Tty.ConsoleNodes.ConsoleNode.ConsoleLine()
                self.console_line.parent = self


            class ConsoleLine(object):
                """
                Console line
                
                .. attribute:: console_statistics
                
                	Statistics of the console line
                	**type**\: :py:class:`ConsoleStatistics <ydk.models.tty.Cisco_IOS_XR_tty_server_oper.Tty.ConsoleNodes.ConsoleNode.ConsoleLine.ConsoleStatistics>`
                
                .. attribute:: state
                
                	Line state information
                	**type**\: :py:class:`State <ydk.models.tty.Cisco_IOS_XR_tty_server_oper.Tty.ConsoleNodes.ConsoleNode.ConsoleLine.State>`
                
                .. attribute:: configuration
                
                	Configuration information of the line
                	**type**\: :py:class:`Configuration <ydk.models.tty.Cisco_IOS_XR_tty_server_oper.Tty.ConsoleNodes.ConsoleNode.ConsoleLine.Configuration>`
                
                

                """

                _prefix = 'tty-server-oper'
                _revision = '2015-07-30'

                def __init__(self):
                    self.parent = None
                    self.console_statistics = Tty.ConsoleNodes.ConsoleNode.ConsoleLine.ConsoleStatistics()
                    self.console_statistics.parent = self
                    self.state = Tty.ConsoleNodes.ConsoleNode.ConsoleLine.State()
                    self.state.parent = self
                    self.configuration = Tty.ConsoleNodes.ConsoleNode.ConsoleLine.Configuration()
                    self.configuration.parent = self


                class ConsoleStatistics(object):
                    """
                    Statistics of the console line
                    
                    .. attribute:: rs232
                    
                    	RS232 statistics of console line
                    	**type**\: :py:class:`Rs232 <ydk.models.tty.Cisco_IOS_XR_tty_server_oper.Tty.ConsoleNodes.ConsoleNode.ConsoleLine.ConsoleStatistics.Rs232>`
                    
                    .. attribute:: general_statistics
                    
                    	General statistics of line
                    	**type**\: :py:class:`GeneralStatistics <ydk.models.tty.Cisco_IOS_XR_tty_server_oper.Tty.ConsoleNodes.ConsoleNode.ConsoleLine.ConsoleStatistics.GeneralStatistics>`
                    
                    .. attribute:: exec_
                    
                    	Exec related statistics
                    	**type**\: :py:class:`Exec <ydk.models.tty.Cisco_IOS_XR_tty_server_oper.Tty.ConsoleNodes.ConsoleNode.ConsoleLine.ConsoleStatistics.Exec>`
                    
                    .. attribute:: aaa
                    
                    	AAA related statistics
                    	**type**\: :py:class:`Aaa <ydk.models.tty.Cisco_IOS_XR_tty_server_oper.Tty.ConsoleNodes.ConsoleNode.ConsoleLine.ConsoleStatistics.Aaa>`
                    
                    

                    """

                    _prefix = 'tty-server-oper'
                    _revision = '2015-07-30'

                    def __init__(self):
                        self.parent = None
                        self.rs232 = Tty.ConsoleNodes.ConsoleNode.ConsoleLine.ConsoleStatistics.Rs232()
                        self.rs232.parent = self
                        self.general_statistics = Tty.ConsoleNodes.ConsoleNode.ConsoleLine.ConsoleStatistics.GeneralStatistics()
                        self.general_statistics.parent = self
                        self.exec_ = Tty.ConsoleNodes.ConsoleNode.ConsoleLine.ConsoleStatistics.Exec()
                        self.exec_.parent = self
                        self.aaa = Tty.ConsoleNodes.ConsoleNode.ConsoleLine.ConsoleStatistics.Aaa()
                        self.aaa.parent = self


                    class Rs232(object):
                        """
                        RS232 statistics of console line
                        
                        .. attribute:: data_bits
                        
                        	Number of databits
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: exec_disabled
                        
                        	Exec disabled on TTY
                        	**type**\: bool
                        
                        .. attribute:: hardware_flow_control_status
                        
                        	Hardware flow control status
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: parity_status
                        
                        	Parity status
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: baud_rate
                        
                        	Inbound/Outbound baud rate in bps
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: stop_bits
                        
                        	Number of stopbits
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: overrun_error_count
                        
                        	Overrun error count
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: framing_error_count
                        
                        	Framing error count
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: parity_error_count
                        
                        	Parity error count
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'tty-server-oper'
                        _revision = '2015-07-30'

                        def __init__(self):
                            self.parent = None
                            self.data_bits = None
                            self.exec_disabled = None
                            self.hardware_flow_control_status = None
                            self.parity_status = None
                            self.baud_rate = None
                            self.stop_bits = None
                            self.overrun_error_count = None
                            self.framing_error_count = None
                            self.parity_error_count = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-tty-server-oper:rs232'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.data_bits is not None:
                                return True

                            if self.exec_disabled is not None:
                                return True

                            if self.hardware_flow_control_status is not None:
                                return True

                            if self.parity_status is not None:
                                return True

                            if self.baud_rate is not None:
                                return True

                            if self.stop_bits is not None:
                                return True

                            if self.overrun_error_count is not None:
                                return True

                            if self.framing_error_count is not None:
                                return True

                            if self.parity_error_count is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.tty._meta import _Cisco_IOS_XR_tty_server_oper as meta
                            return meta._meta_table['Tty.ConsoleNodes.ConsoleNode.ConsoleLine.ConsoleStatistics.Rs232']['meta_info']


                    class GeneralStatistics(object):
                        """
                        General statistics of line
                        
                        .. attribute:: terminal_length
                        
                        	Terminal length
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: terminal_width
                        
                        	Line width
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: async_interface
                        
                        	Usable as async interface
                        	**type**\: bool
                        
                        .. attribute:: flow_control_start_character
                        
                        	Software flow control start char
                        	**type**\: int
                        
                        	**range:** \-128..127
                        
                        .. attribute:: flow_control_stop_character
                        
                        	Software flow control stop char
                        	**type**\: int
                        
                        	**range:** \-128..127
                        
                        .. attribute:: domain_lookup_enabled
                        
                        	DNS resolution enabled
                        	**type**\: bool
                        
                        .. attribute:: motd_banner_enabled
                        
                        	MOTD banner enabled
                        	**type**\: bool
                        
                        .. attribute:: private_flag
                        
                        	TTY private flag
                        	**type**\: bool
                        
                        .. attribute:: terminal_type
                        
                        	Terminal type
                        	**type**\: str
                        
                        .. attribute:: absolute_timeout
                        
                        	Absolute timeout period
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: idle_time
                        
                        	TTY idle time
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'tty-server-oper'
                        _revision = '2015-07-30'

                        def __init__(self):
                            self.parent = None
                            self.terminal_length = None
                            self.terminal_width = None
                            self.async_interface = None
                            self.flow_control_start_character = None
                            self.flow_control_stop_character = None
                            self.domain_lookup_enabled = None
                            self.motd_banner_enabled = None
                            self.private_flag = None
                            self.terminal_type = None
                            self.absolute_timeout = None
                            self.idle_time = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-tty-server-oper:general-statistics'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.terminal_length is not None:
                                return True

                            if self.terminal_width is not None:
                                return True

                            if self.async_interface is not None:
                                return True

                            if self.flow_control_start_character is not None:
                                return True

                            if self.flow_control_stop_character is not None:
                                return True

                            if self.domain_lookup_enabled is not None:
                                return True

                            if self.motd_banner_enabled is not None:
                                return True

                            if self.private_flag is not None:
                                return True

                            if self.terminal_type is not None:
                                return True

                            if self.absolute_timeout is not None:
                                return True

                            if self.idle_time is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.tty._meta import _Cisco_IOS_XR_tty_server_oper as meta
                            return meta._meta_table['Tty.ConsoleNodes.ConsoleNode.ConsoleLine.ConsoleStatistics.GeneralStatistics']['meta_info']


                    class Exec(object):
                        """
                        Exec related statistics
                        
                        .. attribute:: time_stamp_enabled
                        
                        	Specifies whether timestamp is enabled or not
                        	**type**\: bool
                        
                        

                        """

                        _prefix = 'tty-server-oper'
                        _revision = '2015-07-30'

                        def __init__(self):
                            self.parent = None
                            self.time_stamp_enabled = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-tty-server-oper:exec'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.time_stamp_enabled is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.tty._meta import _Cisco_IOS_XR_tty_server_oper as meta
                            return meta._meta_table['Tty.ConsoleNodes.ConsoleNode.ConsoleLine.ConsoleStatistics.Exec']['meta_info']


                    class Aaa(object):
                        """
                        AAA related statistics
                        
                        .. attribute:: user_name
                        
                        	The authenticated username
                        	**type**\: str
                        
                        

                        """

                        _prefix = 'tty-server-oper'
                        _revision = '2015-07-30'

                        def __init__(self):
                            self.parent = None
                            self.user_name = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-tty-server-oper:aaa'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.user_name is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.tty._meta import _Cisco_IOS_XR_tty_server_oper as meta
                            return meta._meta_table['Tty.ConsoleNodes.ConsoleNode.ConsoleLine.ConsoleStatistics.Aaa']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-tty-server-oper:console-statistics'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.rs232 is not None and self.rs232._has_data():
                            return True

                        if self.general_statistics is not None and self.general_statistics._has_data():
                            return True

                        if self.exec_ is not None and self.exec_._has_data():
                            return True

                        if self.aaa is not None and self.aaa._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.tty._meta import _Cisco_IOS_XR_tty_server_oper as meta
                        return meta._meta_table['Tty.ConsoleNodes.ConsoleNode.ConsoleLine.ConsoleStatistics']['meta_info']


                class State(object):
                    """
                    Line state information
                    
                    .. attribute:: template
                    
                    	Information related to template applied to the line
                    	**type**\: :py:class:`Template <ydk.models.tty.Cisco_IOS_XR_tty_server_oper.Tty.ConsoleNodes.ConsoleNode.ConsoleLine.State.Template>`
                    
                    .. attribute:: general
                    
                    	General information
                    	**type**\: :py:class:`General <ydk.models.tty.Cisco_IOS_XR_tty_server_oper.Tty.ConsoleNodes.ConsoleNode.ConsoleLine.State.General>`
                    
                    

                    """

                    _prefix = 'tty-server-oper'
                    _revision = '2015-07-30'

                    def __init__(self):
                        self.parent = None
                        self.template = Tty.ConsoleNodes.ConsoleNode.ConsoleLine.State.Template()
                        self.template.parent = self
                        self.general = Tty.ConsoleNodes.ConsoleNode.ConsoleLine.State.General()
                        self.general.parent = self


                    class Template(object):
                        """
                        Information related to template applied to the
                        line
                        
                        .. attribute:: name
                        
                        	Name of the template
                        	**type**\: str
                        
                        

                        """

                        _prefix = 'tty-server-oper'
                        _revision = '2015-07-30'

                        def __init__(self):
                            self.parent = None
                            self.name = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-tty-server-oper:template'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.name is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.tty._meta import _Cisco_IOS_XR_tty_server_oper as meta
                            return meta._meta_table['Tty.ConsoleNodes.ConsoleNode.ConsoleLine.State.Template']['meta_info']


                    class General(object):
                        """
                        General information
                        
                        .. attribute:: operation
                        
                        	application running of on the tty line
                        	**type**\: :py:class:`SessionOperationEnum <ydk.models.tty.Cisco_IOS_XR_tty_server_oper.SessionOperationEnum>`
                        
                        .. attribute:: general_state
                        
                        	State of the line
                        	**type**\: :py:class:`LineStateEnum <ydk.models.tty.Cisco_IOS_XR_tty_server_oper.LineStateEnum>`
                        
                        

                        """

                        _prefix = 'tty-server-oper'
                        _revision = '2015-07-30'

                        def __init__(self):
                            self.parent = None
                            self.operation = None
                            self.general_state = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-tty-server-oper:general'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.operation is not None:
                                return True

                            if self.general_state is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.tty._meta import _Cisco_IOS_XR_tty_server_oper as meta
                            return meta._meta_table['Tty.ConsoleNodes.ConsoleNode.ConsoleLine.State.General']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-tty-server-oper:state'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.template is not None and self.template._has_data():
                            return True

                        if self.general is not None and self.general._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.tty._meta import _Cisco_IOS_XR_tty_server_oper as meta
                        return meta._meta_table['Tty.ConsoleNodes.ConsoleNode.ConsoleLine.State']['meta_info']


                class Configuration(object):
                    """
                    Configuration information of the line
                    
                    .. attribute:: connection_configuration
                    
                    	Conection configuration information
                    	**type**\: :py:class:`ConnectionConfiguration <ydk.models.tty.Cisco_IOS_XR_tty_server_oper.Tty.ConsoleNodes.ConsoleNode.ConsoleLine.Configuration.ConnectionConfiguration>`
                    
                    

                    """

                    _prefix = 'tty-server-oper'
                    _revision = '2015-07-30'

                    def __init__(self):
                        self.parent = None
                        self.connection_configuration = Tty.ConsoleNodes.ConsoleNode.ConsoleLine.Configuration.ConnectionConfiguration()
                        self.connection_configuration.parent = self


                    class ConnectionConfiguration(object):
                        """
                        Conection configuration information
                        
                        .. attribute:: transport_input
                        
                        	Protocols to use when connecting to the terminal server
                        	**type**\: :py:class:`TransportInput <ydk.models.tty.Cisco_IOS_XR_tty_server_oper.Tty.ConsoleNodes.ConsoleNode.ConsoleLine.Configuration.ConnectionConfiguration.TransportInput>`
                        
                        .. attribute:: acl_out
                        
                        	ACL for outbound traffic
                        	**type**\: str
                        
                        .. attribute:: acl_in
                        
                        	ACL for inbound traffic
                        	**type**\: str
                        
                        

                        """

                        _prefix = 'tty-server-oper'
                        _revision = '2015-07-30'

                        def __init__(self):
                            self.parent = None
                            self.transport_input = Tty.ConsoleNodes.ConsoleNode.ConsoleLine.Configuration.ConnectionConfiguration.TransportInput()
                            self.transport_input.parent = self
                            self.acl_out = None
                            self.acl_in = None


                        class TransportInput(object):
                            """
                            Protocols to use when connecting to the
                            terminal server
                            
                            .. attribute:: select
                            
                            	Choose transport protocols
                            	**type**\: :py:class:`TtyTransportProtocolSelectEnum <ydk.models.tty.Cisco_IOS_XR_tty_management_datatypes.TtyTransportProtocolSelectEnum>`
                            
                            .. attribute:: protocol1
                            
                            	Transport protocol1
                            	**type**\: :py:class:`TtyTransportProtocolEnum <ydk.models.tty.Cisco_IOS_XR_tty_management_datatypes.TtyTransportProtocolEnum>`
                            
                            .. attribute:: protocol2
                            
                            	Transport protocol2
                            	**type**\: :py:class:`TtyTransportProtocolEnum <ydk.models.tty.Cisco_IOS_XR_tty_management_datatypes.TtyTransportProtocolEnum>`
                            
                            .. attribute:: none
                            
                            	Not used
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            

                            """

                            _prefix = 'tty-server-oper'
                            _revision = '2015-07-30'

                            def __init__(self):
                                self.parent = None
                                self.select = None
                                self.protocol1 = None
                                self.protocol2 = None
                                self.none = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-tty-server-oper:transport-input'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.select is not None:
                                    return True

                                if self.protocol1 is not None:
                                    return True

                                if self.protocol2 is not None:
                                    return True

                                if self.none is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.tty._meta import _Cisco_IOS_XR_tty_server_oper as meta
                                return meta._meta_table['Tty.ConsoleNodes.ConsoleNode.ConsoleLine.Configuration.ConnectionConfiguration.TransportInput']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-tty-server-oper:connection-configuration'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.transport_input is not None and self.transport_input._has_data():
                                return True

                            if self.acl_out is not None:
                                return True

                            if self.acl_in is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.tty._meta import _Cisco_IOS_XR_tty_server_oper as meta
                            return meta._meta_table['Tty.ConsoleNodes.ConsoleNode.ConsoleLine.Configuration.ConnectionConfiguration']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-tty-server-oper:configuration'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.connection_configuration is not None and self.connection_configuration._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.tty._meta import _Cisco_IOS_XR_tty_server_oper as meta
                        return meta._meta_table['Tty.ConsoleNodes.ConsoleNode.ConsoleLine.Configuration']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-tty-server-oper:console-line'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.console_statistics is not None and self.console_statistics._has_data():
                        return True

                    if self.state is not None and self.state._has_data():
                        return True

                    if self.configuration is not None and self.configuration._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.tty._meta import _Cisco_IOS_XR_tty_server_oper as meta
                    return meta._meta_table['Tty.ConsoleNodes.ConsoleNode.ConsoleLine']['meta_info']

            @property
            def _common_path(self):
                if self.id is None:
                    raise YPYDataValidationError('Key property id is None')

                return '/Cisco-IOS-XR-tty-server-oper:tty/Cisco-IOS-XR-tty-server-oper:console-nodes/Cisco-IOS-XR-tty-server-oper:console-node[Cisco-IOS-XR-tty-server-oper:id = ' + str(self.id) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.id is not None:
                    return True

                if self.console_line is not None and self.console_line._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.tty._meta import _Cisco_IOS_XR_tty_server_oper as meta
                return meta._meta_table['Tty.ConsoleNodes.ConsoleNode']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-tty-server-oper:tty/Cisco-IOS-XR-tty-server-oper:console-nodes'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.console_node is not None:
                for child_ref in self.console_node:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.tty._meta import _Cisco_IOS_XR_tty_server_oper as meta
            return meta._meta_table['Tty.ConsoleNodes']['meta_info']


    class VtyLines(object):
        """
        List of VTY lines
        
        .. attribute:: vty_line
        
        	VTY Line
        	**type**\: list of :py:class:`VtyLine <ydk.models.tty.Cisco_IOS_XR_tty_server_oper.Tty.VtyLines.VtyLine>`
        
        

        """

        _prefix = 'tty-server-oper'
        _revision = '2015-07-30'

        def __init__(self):
            self.parent = None
            self.vty_line = YList()
            self.vty_line.parent = self
            self.vty_line.name = 'vty_line'


        class VtyLine(object):
            """
            VTY Line
            
            .. attribute:: line_number  <key>
            
            	VTY Line number
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: vty_statistics
            
            	Statistics of the VTY line
            	**type**\: :py:class:`VtyStatistics <ydk.models.tty.Cisco_IOS_XR_tty_server_oper.Tty.VtyLines.VtyLine.VtyStatistics>`
            
            .. attribute:: state
            
            	Line state information
            	**type**\: :py:class:`State <ydk.models.tty.Cisco_IOS_XR_tty_server_oper.Tty.VtyLines.VtyLine.State>`
            
            .. attribute:: configuration
            
            	Configuration information of the line
            	**type**\: :py:class:`Configuration <ydk.models.tty.Cisco_IOS_XR_tty_server_oper.Tty.VtyLines.VtyLine.Configuration>`
            
            .. attribute:: sessions
            
            	Outgoing sessions
            	**type**\: :py:class:`Sessions <ydk.models.tty.Cisco_IOS_XR_tty_server_oper.Tty.VtyLines.VtyLine.Sessions>`
            
            

            """

            _prefix = 'tty-server-oper'
            _revision = '2015-07-30'

            def __init__(self):
                self.parent = None
                self.line_number = None
                self.vty_statistics = Tty.VtyLines.VtyLine.VtyStatistics()
                self.vty_statistics.parent = self
                self.state = Tty.VtyLines.VtyLine.State()
                self.state.parent = self
                self.configuration = Tty.VtyLines.VtyLine.Configuration()
                self.configuration.parent = self
                self.sessions = Tty.VtyLines.VtyLine.Sessions()
                self.sessions.parent = self


            class VtyStatistics(object):
                """
                Statistics of the VTY line
                
                .. attribute:: connection
                
                	Connection related statistics
                	**type**\: :py:class:`Connection <ydk.models.tty.Cisco_IOS_XR_tty_server_oper.Tty.VtyLines.VtyLine.VtyStatistics.Connection>`
                
                .. attribute:: general_statistics
                
                	General statistics of line
                	**type**\: :py:class:`GeneralStatistics <ydk.models.tty.Cisco_IOS_XR_tty_server_oper.Tty.VtyLines.VtyLine.VtyStatistics.GeneralStatistics>`
                
                .. attribute:: exec_
                
                	Exec related statistics
                	**type**\: :py:class:`Exec <ydk.models.tty.Cisco_IOS_XR_tty_server_oper.Tty.VtyLines.VtyLine.VtyStatistics.Exec>`
                
                .. attribute:: aaa
                
                	AAA related statistics
                	**type**\: :py:class:`Aaa <ydk.models.tty.Cisco_IOS_XR_tty_server_oper.Tty.VtyLines.VtyLine.VtyStatistics.Aaa>`
                
                

                """

                _prefix = 'tty-server-oper'
                _revision = '2015-07-30'

                def __init__(self):
                    self.parent = None
                    self.connection = Tty.VtyLines.VtyLine.VtyStatistics.Connection()
                    self.connection.parent = self
                    self.general_statistics = Tty.VtyLines.VtyLine.VtyStatistics.GeneralStatistics()
                    self.general_statistics.parent = self
                    self.exec_ = Tty.VtyLines.VtyLine.VtyStatistics.Exec()
                    self.exec_.parent = self
                    self.aaa = Tty.VtyLines.VtyLine.VtyStatistics.Aaa()
                    self.aaa.parent = self


                class Connection(object):
                    """
                    Connection related statistics
                    
                    .. attribute:: incoming_host_address
                    
                    	Incoming host address(max)
                    	**type**\: str
                    
                    	**range:** 0..46
                    
                    .. attribute:: host_address_family
                    
                    	Incoming host address family
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: service
                    
                    	Input transport
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'tty-server-oper'
                    _revision = '2015-07-30'

                    def __init__(self):
                        self.parent = None
                        self.incoming_host_address = None
                        self.host_address_family = None
                        self.service = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-tty-server-oper:connection'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.incoming_host_address is not None:
                            return True

                        if self.host_address_family is not None:
                            return True

                        if self.service is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.tty._meta import _Cisco_IOS_XR_tty_server_oper as meta
                        return meta._meta_table['Tty.VtyLines.VtyLine.VtyStatistics.Connection']['meta_info']


                class GeneralStatistics(object):
                    """
                    General statistics of line
                    
                    .. attribute:: terminal_length
                    
                    	Terminal length
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: terminal_width
                    
                    	Line width
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: async_interface
                    
                    	Usable as async interface
                    	**type**\: bool
                    
                    .. attribute:: flow_control_start_character
                    
                    	Software flow control start char
                    	**type**\: int
                    
                    	**range:** \-128..127
                    
                    .. attribute:: flow_control_stop_character
                    
                    	Software flow control stop char
                    	**type**\: int
                    
                    	**range:** \-128..127
                    
                    .. attribute:: domain_lookup_enabled
                    
                    	DNS resolution enabled
                    	**type**\: bool
                    
                    .. attribute:: motd_banner_enabled
                    
                    	MOTD banner enabled
                    	**type**\: bool
                    
                    .. attribute:: private_flag
                    
                    	TTY private flag
                    	**type**\: bool
                    
                    .. attribute:: terminal_type
                    
                    	Terminal type
                    	**type**\: str
                    
                    .. attribute:: absolute_timeout
                    
                    	Absolute timeout period
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: idle_time
                    
                    	TTY idle time
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'tty-server-oper'
                    _revision = '2015-07-30'

                    def __init__(self):
                        self.parent = None
                        self.terminal_length = None
                        self.terminal_width = None
                        self.async_interface = None
                        self.flow_control_start_character = None
                        self.flow_control_stop_character = None
                        self.domain_lookup_enabled = None
                        self.motd_banner_enabled = None
                        self.private_flag = None
                        self.terminal_type = None
                        self.absolute_timeout = None
                        self.idle_time = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-tty-server-oper:general-statistics'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.terminal_length is not None:
                            return True

                        if self.terminal_width is not None:
                            return True

                        if self.async_interface is not None:
                            return True

                        if self.flow_control_start_character is not None:
                            return True

                        if self.flow_control_stop_character is not None:
                            return True

                        if self.domain_lookup_enabled is not None:
                            return True

                        if self.motd_banner_enabled is not None:
                            return True

                        if self.private_flag is not None:
                            return True

                        if self.terminal_type is not None:
                            return True

                        if self.absolute_timeout is not None:
                            return True

                        if self.idle_time is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.tty._meta import _Cisco_IOS_XR_tty_server_oper as meta
                        return meta._meta_table['Tty.VtyLines.VtyLine.VtyStatistics.GeneralStatistics']['meta_info']


                class Exec(object):
                    """
                    Exec related statistics
                    
                    .. attribute:: time_stamp_enabled
                    
                    	Specifies whether timestamp is enabled or not
                    	**type**\: bool
                    
                    

                    """

                    _prefix = 'tty-server-oper'
                    _revision = '2015-07-30'

                    def __init__(self):
                        self.parent = None
                        self.time_stamp_enabled = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-tty-server-oper:exec'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.time_stamp_enabled is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.tty._meta import _Cisco_IOS_XR_tty_server_oper as meta
                        return meta._meta_table['Tty.VtyLines.VtyLine.VtyStatistics.Exec']['meta_info']


                class Aaa(object):
                    """
                    AAA related statistics
                    
                    .. attribute:: user_name
                    
                    	The authenticated username
                    	**type**\: str
                    
                    

                    """

                    _prefix = 'tty-server-oper'
                    _revision = '2015-07-30'

                    def __init__(self):
                        self.parent = None
                        self.user_name = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-tty-server-oper:aaa'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.user_name is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.tty._meta import _Cisco_IOS_XR_tty_server_oper as meta
                        return meta._meta_table['Tty.VtyLines.VtyLine.VtyStatistics.Aaa']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-tty-server-oper:vty-statistics'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.connection is not None and self.connection._has_data():
                        return True

                    if self.general_statistics is not None and self.general_statistics._has_data():
                        return True

                    if self.exec_ is not None and self.exec_._has_data():
                        return True

                    if self.aaa is not None and self.aaa._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.tty._meta import _Cisco_IOS_XR_tty_server_oper as meta
                    return meta._meta_table['Tty.VtyLines.VtyLine.VtyStatistics']['meta_info']


            class State(object):
                """
                Line state information
                
                .. attribute:: template
                
                	Information related to template applied to the line
                	**type**\: :py:class:`Template <ydk.models.tty.Cisco_IOS_XR_tty_server_oper.Tty.VtyLines.VtyLine.State.Template>`
                
                .. attribute:: general
                
                	General information
                	**type**\: :py:class:`General <ydk.models.tty.Cisco_IOS_XR_tty_server_oper.Tty.VtyLines.VtyLine.State.General>`
                
                

                """

                _prefix = 'tty-server-oper'
                _revision = '2015-07-30'

                def __init__(self):
                    self.parent = None
                    self.template = Tty.VtyLines.VtyLine.State.Template()
                    self.template.parent = self
                    self.general = Tty.VtyLines.VtyLine.State.General()
                    self.general.parent = self


                class Template(object):
                    """
                    Information related to template applied to the
                    line
                    
                    .. attribute:: name
                    
                    	Name of the template
                    	**type**\: str
                    
                    

                    """

                    _prefix = 'tty-server-oper'
                    _revision = '2015-07-30'

                    def __init__(self):
                        self.parent = None
                        self.name = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-tty-server-oper:template'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.name is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.tty._meta import _Cisco_IOS_XR_tty_server_oper as meta
                        return meta._meta_table['Tty.VtyLines.VtyLine.State.Template']['meta_info']


                class General(object):
                    """
                    General information
                    
                    .. attribute:: operation
                    
                    	application running of on the tty line
                    	**type**\: :py:class:`SessionOperationEnum <ydk.models.tty.Cisco_IOS_XR_tty_server_oper.SessionOperationEnum>`
                    
                    .. attribute:: general_state
                    
                    	State of the line
                    	**type**\: :py:class:`LineStateEnum <ydk.models.tty.Cisco_IOS_XR_tty_server_oper.LineStateEnum>`
                    
                    

                    """

                    _prefix = 'tty-server-oper'
                    _revision = '2015-07-30'

                    def __init__(self):
                        self.parent = None
                        self.operation = None
                        self.general_state = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-tty-server-oper:general'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.operation is not None:
                            return True

                        if self.general_state is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.tty._meta import _Cisco_IOS_XR_tty_server_oper as meta
                        return meta._meta_table['Tty.VtyLines.VtyLine.State.General']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-tty-server-oper:state'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.template is not None and self.template._has_data():
                        return True

                    if self.general is not None and self.general._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.tty._meta import _Cisco_IOS_XR_tty_server_oper as meta
                    return meta._meta_table['Tty.VtyLines.VtyLine.State']['meta_info']


            class Configuration(object):
                """
                Configuration information of the line
                
                .. attribute:: connection_configuration
                
                	Conection configuration information
                	**type**\: :py:class:`ConnectionConfiguration <ydk.models.tty.Cisco_IOS_XR_tty_server_oper.Tty.VtyLines.VtyLine.Configuration.ConnectionConfiguration>`
                
                

                """

                _prefix = 'tty-server-oper'
                _revision = '2015-07-30'

                def __init__(self):
                    self.parent = None
                    self.connection_configuration = Tty.VtyLines.VtyLine.Configuration.ConnectionConfiguration()
                    self.connection_configuration.parent = self


                class ConnectionConfiguration(object):
                    """
                    Conection configuration information
                    
                    .. attribute:: transport_input
                    
                    	Protocols to use when connecting to the terminal server
                    	**type**\: :py:class:`TransportInput <ydk.models.tty.Cisco_IOS_XR_tty_server_oper.Tty.VtyLines.VtyLine.Configuration.ConnectionConfiguration.TransportInput>`
                    
                    .. attribute:: acl_out
                    
                    	ACL for outbound traffic
                    	**type**\: str
                    
                    .. attribute:: acl_in
                    
                    	ACL for inbound traffic
                    	**type**\: str
                    
                    

                    """

                    _prefix = 'tty-server-oper'
                    _revision = '2015-07-30'

                    def __init__(self):
                        self.parent = None
                        self.transport_input = Tty.VtyLines.VtyLine.Configuration.ConnectionConfiguration.TransportInput()
                        self.transport_input.parent = self
                        self.acl_out = None
                        self.acl_in = None


                    class TransportInput(object):
                        """
                        Protocols to use when connecting to the
                        terminal server
                        
                        .. attribute:: select
                        
                        	Choose transport protocols
                        	**type**\: :py:class:`TtyTransportProtocolSelectEnum <ydk.models.tty.Cisco_IOS_XR_tty_management_datatypes.TtyTransportProtocolSelectEnum>`
                        
                        .. attribute:: protocol1
                        
                        	Transport protocol1
                        	**type**\: :py:class:`TtyTransportProtocolEnum <ydk.models.tty.Cisco_IOS_XR_tty_management_datatypes.TtyTransportProtocolEnum>`
                        
                        .. attribute:: protocol2
                        
                        	Transport protocol2
                        	**type**\: :py:class:`TtyTransportProtocolEnum <ydk.models.tty.Cisco_IOS_XR_tty_management_datatypes.TtyTransportProtocolEnum>`
                        
                        .. attribute:: none
                        
                        	Not used
                        	**type**\: int
                        
                        	**range:** \-2147483648..2147483647
                        
                        

                        """

                        _prefix = 'tty-server-oper'
                        _revision = '2015-07-30'

                        def __init__(self):
                            self.parent = None
                            self.select = None
                            self.protocol1 = None
                            self.protocol2 = None
                            self.none = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-tty-server-oper:transport-input'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.select is not None:
                                return True

                            if self.protocol1 is not None:
                                return True

                            if self.protocol2 is not None:
                                return True

                            if self.none is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.tty._meta import _Cisco_IOS_XR_tty_server_oper as meta
                            return meta._meta_table['Tty.VtyLines.VtyLine.Configuration.ConnectionConfiguration.TransportInput']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-tty-server-oper:connection-configuration'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.transport_input is not None and self.transport_input._has_data():
                            return True

                        if self.acl_out is not None:
                            return True

                        if self.acl_in is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.tty._meta import _Cisco_IOS_XR_tty_server_oper as meta
                        return meta._meta_table['Tty.VtyLines.VtyLine.Configuration.ConnectionConfiguration']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-tty-server-oper:configuration'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.connection_configuration is not None and self.connection_configuration._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.tty._meta import _Cisco_IOS_XR_tty_server_oper as meta
                    return meta._meta_table['Tty.VtyLines.VtyLine.Configuration']['meta_info']


            class Sessions(object):
                """
                Outgoing sessions
                
                .. attribute:: outgoing_connection
                
                	List of outgoing sessions
                	**type**\: list of :py:class:`OutgoingConnection <ydk.models.tty.Cisco_IOS_XR_tty_server_oper.Tty.VtyLines.VtyLine.Sessions.OutgoingConnection>`
                
                

                """

                _prefix = 'tty-management-oper'
                _revision = '2015-01-07'

                def __init__(self):
                    self.parent = None
                    self.outgoing_connection = YList()
                    self.outgoing_connection.parent = self
                    self.outgoing_connection.name = 'outgoing_connection'


                class OutgoingConnection(object):
                    """
                    List of outgoing sessions
                    
                    .. attribute:: host_address
                    
                    	Host address
                    	**type**\: :py:class:`HostAddress <ydk.models.tty.Cisco_IOS_XR_tty_server_oper.Tty.VtyLines.VtyLine.Sessions.OutgoingConnection.HostAddress>`
                    
                    .. attribute:: connection_id
                    
                    	Connection ID [1\-20]
                    	**type**\: int
                    
                    	**range:** 0..255
                    
                    .. attribute:: host_name
                    
                    	Host name
                    	**type**\: str
                    
                    .. attribute:: transport_protocol
                    
                    	Session transport protocol
                    	**type**\: :py:class:`TransportServiceEnum <ydk.models.tty.Cisco_IOS_XR_tty_management_oper.TransportServiceEnum>`
                    
                    .. attribute:: is_last_active_session
                    
                    	True indicates last active session
                    	**type**\: bool
                    
                    .. attribute:: idle_time
                    
                    	Elapsed time since session was suspended (in seconds)
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'tty-management-oper'
                    _revision = '2015-01-07'

                    def __init__(self):
                        self.parent = None
                        self.host_address = Tty.VtyLines.VtyLine.Sessions.OutgoingConnection.HostAddress()
                        self.host_address.parent = self
                        self.connection_id = None
                        self.host_name = None
                        self.transport_protocol = None
                        self.is_last_active_session = None
                        self.idle_time = None


                    class HostAddress(object):
                        """
                        Host address
                        
                        .. attribute:: af_name
                        
                        	AFName
                        	**type**\: :py:class:`HostAfIdBase_Identity <ydk.models.tty.Cisco_IOS_XR_tty_management_oper.HostAfIdBase_Identity>`
                        
                        .. attribute:: ipv4_address
                        
                        	IPv4 address
                        	**type**\: str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: ipv6_address
                        
                        	IPv6 address
                        	**type**\: str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        

                        """

                        _prefix = 'tty-management-oper'
                        _revision = '2015-01-07'

                        def __init__(self):
                            self.parent = None
                            self.af_name = None
                            self.ipv4_address = None
                            self.ipv6_address = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-tty-management-oper:host-address'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.af_name is not None:
                                return True

                            if self.ipv4_address is not None:
                                return True

                            if self.ipv6_address is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.tty._meta import _Cisco_IOS_XR_tty_server_oper as meta
                            return meta._meta_table['Tty.VtyLines.VtyLine.Sessions.OutgoingConnection.HostAddress']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-tty-management-oper:outgoing-connection'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.host_address is not None and self.host_address._has_data():
                            return True

                        if self.connection_id is not None:
                            return True

                        if self.host_name is not None:
                            return True

                        if self.transport_protocol is not None:
                            return True

                        if self.is_last_active_session is not None:
                            return True

                        if self.idle_time is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.tty._meta import _Cisco_IOS_XR_tty_server_oper as meta
                        return meta._meta_table['Tty.VtyLines.VtyLine.Sessions.OutgoingConnection']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-tty-management-oper:sessions'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.outgoing_connection is not None:
                        for child_ref in self.outgoing_connection:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.tty._meta import _Cisco_IOS_XR_tty_server_oper as meta
                    return meta._meta_table['Tty.VtyLines.VtyLine.Sessions']['meta_info']

            @property
            def _common_path(self):
                if self.line_number is None:
                    raise YPYDataValidationError('Key property line_number is None')

                return '/Cisco-IOS-XR-tty-server-oper:tty/Cisco-IOS-XR-tty-server-oper:vty-lines/Cisco-IOS-XR-tty-server-oper:vty-line[Cisco-IOS-XR-tty-server-oper:line-number = ' + str(self.line_number) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.line_number is not None:
                    return True

                if self.vty_statistics is not None and self.vty_statistics._has_data():
                    return True

                if self.state is not None and self.state._has_data():
                    return True

                if self.configuration is not None and self.configuration._has_data():
                    return True

                if self.sessions is not None and self.sessions._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.tty._meta import _Cisco_IOS_XR_tty_server_oper as meta
                return meta._meta_table['Tty.VtyLines.VtyLine']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-tty-server-oper:tty/Cisco-IOS-XR-tty-server-oper:vty-lines'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.vty_line is not None:
                for child_ref in self.vty_line:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.tty._meta import _Cisco_IOS_XR_tty_server_oper as meta
            return meta._meta_table['Tty.VtyLines']['meta_info']


    class AuxiliaryNodes(object):
        """
        List of Nodes attached with an auxiliary line
        
        .. attribute:: auxiliary_node
        
        	Line configuration on a node
        	**type**\: list of :py:class:`AuxiliaryNode <ydk.models.tty.Cisco_IOS_XR_tty_server_oper.Tty.AuxiliaryNodes.AuxiliaryNode>`
        
        

        """

        _prefix = 'tty-server-oper'
        _revision = '2015-07-30'

        def __init__(self):
            self.parent = None
            self.auxiliary_node = YList()
            self.auxiliary_node.parent = self
            self.auxiliary_node.name = 'auxiliary_node'


        class AuxiliaryNode(object):
            """
            Line configuration on a node
            
            .. attribute:: id  <key>
            
            	Node ID
            	**type**\: str
            
            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
            
            .. attribute:: auxiliary_line
            
            	Auxiliary line
            	**type**\: :py:class:`AuxiliaryLine <ydk.models.tty.Cisco_IOS_XR_tty_server_oper.Tty.AuxiliaryNodes.AuxiliaryNode.AuxiliaryLine>`
            
            

            """

            _prefix = 'tty-server-oper'
            _revision = '2015-07-30'

            def __init__(self):
                self.parent = None
                self.id = None
                self.auxiliary_line = Tty.AuxiliaryNodes.AuxiliaryNode.AuxiliaryLine()
                self.auxiliary_line.parent = self


            class AuxiliaryLine(object):
                """
                Auxiliary line
                
                .. attribute:: auxiliary_statistics
                
                	Statistics of the auxiliary line
                	**type**\: :py:class:`AuxiliaryStatistics <ydk.models.tty.Cisco_IOS_XR_tty_server_oper.Tty.AuxiliaryNodes.AuxiliaryNode.AuxiliaryLine.AuxiliaryStatistics>`
                
                .. attribute:: state
                
                	Line state information
                	**type**\: :py:class:`State <ydk.models.tty.Cisco_IOS_XR_tty_server_oper.Tty.AuxiliaryNodes.AuxiliaryNode.AuxiliaryLine.State>`
                
                .. attribute:: configuration
                
                	Configuration information of the line
                	**type**\: :py:class:`Configuration <ydk.models.tty.Cisco_IOS_XR_tty_server_oper.Tty.AuxiliaryNodes.AuxiliaryNode.AuxiliaryLine.Configuration>`
                
                

                """

                _prefix = 'tty-server-oper'
                _revision = '2015-07-30'

                def __init__(self):
                    self.parent = None
                    self.auxiliary_statistics = Tty.AuxiliaryNodes.AuxiliaryNode.AuxiliaryLine.AuxiliaryStatistics()
                    self.auxiliary_statistics.parent = self
                    self.state = Tty.AuxiliaryNodes.AuxiliaryNode.AuxiliaryLine.State()
                    self.state.parent = self
                    self.configuration = Tty.AuxiliaryNodes.AuxiliaryNode.AuxiliaryLine.Configuration()
                    self.configuration.parent = self


                class AuxiliaryStatistics(object):
                    """
                    Statistics of the auxiliary line
                    
                    .. attribute:: rs232
                    
                    	RS232 statistics of console line
                    	**type**\: :py:class:`Rs232 <ydk.models.tty.Cisco_IOS_XR_tty_server_oper.Tty.AuxiliaryNodes.AuxiliaryNode.AuxiliaryLine.AuxiliaryStatistics.Rs232>`
                    
                    .. attribute:: general_statistics
                    
                    	General statistics of line
                    	**type**\: :py:class:`GeneralStatistics <ydk.models.tty.Cisco_IOS_XR_tty_server_oper.Tty.AuxiliaryNodes.AuxiliaryNode.AuxiliaryLine.AuxiliaryStatistics.GeneralStatistics>`
                    
                    .. attribute:: exec_
                    
                    	Exec related statistics
                    	**type**\: :py:class:`Exec <ydk.models.tty.Cisco_IOS_XR_tty_server_oper.Tty.AuxiliaryNodes.AuxiliaryNode.AuxiliaryLine.AuxiliaryStatistics.Exec>`
                    
                    .. attribute:: aaa
                    
                    	AAA related statistics
                    	**type**\: :py:class:`Aaa <ydk.models.tty.Cisco_IOS_XR_tty_server_oper.Tty.AuxiliaryNodes.AuxiliaryNode.AuxiliaryLine.AuxiliaryStatistics.Aaa>`
                    
                    

                    """

                    _prefix = 'tty-server-oper'
                    _revision = '2015-07-30'

                    def __init__(self):
                        self.parent = None
                        self.rs232 = Tty.AuxiliaryNodes.AuxiliaryNode.AuxiliaryLine.AuxiliaryStatistics.Rs232()
                        self.rs232.parent = self
                        self.general_statistics = Tty.AuxiliaryNodes.AuxiliaryNode.AuxiliaryLine.AuxiliaryStatistics.GeneralStatistics()
                        self.general_statistics.parent = self
                        self.exec_ = Tty.AuxiliaryNodes.AuxiliaryNode.AuxiliaryLine.AuxiliaryStatistics.Exec()
                        self.exec_.parent = self
                        self.aaa = Tty.AuxiliaryNodes.AuxiliaryNode.AuxiliaryLine.AuxiliaryStatistics.Aaa()
                        self.aaa.parent = self


                    class Rs232(object):
                        """
                        RS232 statistics of console line
                        
                        .. attribute:: data_bits
                        
                        	Number of databits
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: exec_disabled
                        
                        	Exec disabled on TTY
                        	**type**\: bool
                        
                        .. attribute:: hardware_flow_control_status
                        
                        	Hardware flow control status
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: parity_status
                        
                        	Parity status
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: baud_rate
                        
                        	Inbound/Outbound baud rate in bps
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: stop_bits
                        
                        	Number of stopbits
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: overrun_error_count
                        
                        	Overrun error count
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: framing_error_count
                        
                        	Framing error count
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: parity_error_count
                        
                        	Parity error count
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'tty-server-oper'
                        _revision = '2015-07-30'

                        def __init__(self):
                            self.parent = None
                            self.data_bits = None
                            self.exec_disabled = None
                            self.hardware_flow_control_status = None
                            self.parity_status = None
                            self.baud_rate = None
                            self.stop_bits = None
                            self.overrun_error_count = None
                            self.framing_error_count = None
                            self.parity_error_count = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-tty-server-oper:rs232'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.data_bits is not None:
                                return True

                            if self.exec_disabled is not None:
                                return True

                            if self.hardware_flow_control_status is not None:
                                return True

                            if self.parity_status is not None:
                                return True

                            if self.baud_rate is not None:
                                return True

                            if self.stop_bits is not None:
                                return True

                            if self.overrun_error_count is not None:
                                return True

                            if self.framing_error_count is not None:
                                return True

                            if self.parity_error_count is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.tty._meta import _Cisco_IOS_XR_tty_server_oper as meta
                            return meta._meta_table['Tty.AuxiliaryNodes.AuxiliaryNode.AuxiliaryLine.AuxiliaryStatistics.Rs232']['meta_info']


                    class GeneralStatistics(object):
                        """
                        General statistics of line
                        
                        .. attribute:: terminal_length
                        
                        	Terminal length
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: terminal_width
                        
                        	Line width
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: async_interface
                        
                        	Usable as async interface
                        	**type**\: bool
                        
                        .. attribute:: flow_control_start_character
                        
                        	Software flow control start char
                        	**type**\: int
                        
                        	**range:** \-128..127
                        
                        .. attribute:: flow_control_stop_character
                        
                        	Software flow control stop char
                        	**type**\: int
                        
                        	**range:** \-128..127
                        
                        .. attribute:: domain_lookup_enabled
                        
                        	DNS resolution enabled
                        	**type**\: bool
                        
                        .. attribute:: motd_banner_enabled
                        
                        	MOTD banner enabled
                        	**type**\: bool
                        
                        .. attribute:: private_flag
                        
                        	TTY private flag
                        	**type**\: bool
                        
                        .. attribute:: terminal_type
                        
                        	Terminal type
                        	**type**\: str
                        
                        .. attribute:: absolute_timeout
                        
                        	Absolute timeout period
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: idle_time
                        
                        	TTY idle time
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'tty-server-oper'
                        _revision = '2015-07-30'

                        def __init__(self):
                            self.parent = None
                            self.terminal_length = None
                            self.terminal_width = None
                            self.async_interface = None
                            self.flow_control_start_character = None
                            self.flow_control_stop_character = None
                            self.domain_lookup_enabled = None
                            self.motd_banner_enabled = None
                            self.private_flag = None
                            self.terminal_type = None
                            self.absolute_timeout = None
                            self.idle_time = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-tty-server-oper:general-statistics'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.terminal_length is not None:
                                return True

                            if self.terminal_width is not None:
                                return True

                            if self.async_interface is not None:
                                return True

                            if self.flow_control_start_character is not None:
                                return True

                            if self.flow_control_stop_character is not None:
                                return True

                            if self.domain_lookup_enabled is not None:
                                return True

                            if self.motd_banner_enabled is not None:
                                return True

                            if self.private_flag is not None:
                                return True

                            if self.terminal_type is not None:
                                return True

                            if self.absolute_timeout is not None:
                                return True

                            if self.idle_time is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.tty._meta import _Cisco_IOS_XR_tty_server_oper as meta
                            return meta._meta_table['Tty.AuxiliaryNodes.AuxiliaryNode.AuxiliaryLine.AuxiliaryStatistics.GeneralStatistics']['meta_info']


                    class Exec(object):
                        """
                        Exec related statistics
                        
                        .. attribute:: time_stamp_enabled
                        
                        	Specifies whether timestamp is enabled or not
                        	**type**\: bool
                        
                        

                        """

                        _prefix = 'tty-server-oper'
                        _revision = '2015-07-30'

                        def __init__(self):
                            self.parent = None
                            self.time_stamp_enabled = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-tty-server-oper:exec'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.time_stamp_enabled is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.tty._meta import _Cisco_IOS_XR_tty_server_oper as meta
                            return meta._meta_table['Tty.AuxiliaryNodes.AuxiliaryNode.AuxiliaryLine.AuxiliaryStatistics.Exec']['meta_info']


                    class Aaa(object):
                        """
                        AAA related statistics
                        
                        .. attribute:: user_name
                        
                        	The authenticated username
                        	**type**\: str
                        
                        

                        """

                        _prefix = 'tty-server-oper'
                        _revision = '2015-07-30'

                        def __init__(self):
                            self.parent = None
                            self.user_name = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-tty-server-oper:aaa'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.user_name is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.tty._meta import _Cisco_IOS_XR_tty_server_oper as meta
                            return meta._meta_table['Tty.AuxiliaryNodes.AuxiliaryNode.AuxiliaryLine.AuxiliaryStatistics.Aaa']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-tty-server-oper:auxiliary-statistics'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.rs232 is not None and self.rs232._has_data():
                            return True

                        if self.general_statistics is not None and self.general_statistics._has_data():
                            return True

                        if self.exec_ is not None and self.exec_._has_data():
                            return True

                        if self.aaa is not None and self.aaa._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.tty._meta import _Cisco_IOS_XR_tty_server_oper as meta
                        return meta._meta_table['Tty.AuxiliaryNodes.AuxiliaryNode.AuxiliaryLine.AuxiliaryStatistics']['meta_info']


                class State(object):
                    """
                    Line state information
                    
                    .. attribute:: template
                    
                    	Information related to template applied to the line
                    	**type**\: :py:class:`Template <ydk.models.tty.Cisco_IOS_XR_tty_server_oper.Tty.AuxiliaryNodes.AuxiliaryNode.AuxiliaryLine.State.Template>`
                    
                    .. attribute:: general
                    
                    	General information
                    	**type**\: :py:class:`General <ydk.models.tty.Cisco_IOS_XR_tty_server_oper.Tty.AuxiliaryNodes.AuxiliaryNode.AuxiliaryLine.State.General>`
                    
                    

                    """

                    _prefix = 'tty-server-oper'
                    _revision = '2015-07-30'

                    def __init__(self):
                        self.parent = None
                        self.template = Tty.AuxiliaryNodes.AuxiliaryNode.AuxiliaryLine.State.Template()
                        self.template.parent = self
                        self.general = Tty.AuxiliaryNodes.AuxiliaryNode.AuxiliaryLine.State.General()
                        self.general.parent = self


                    class Template(object):
                        """
                        Information related to template applied to the
                        line
                        
                        .. attribute:: name
                        
                        	Name of the template
                        	**type**\: str
                        
                        

                        """

                        _prefix = 'tty-server-oper'
                        _revision = '2015-07-30'

                        def __init__(self):
                            self.parent = None
                            self.name = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-tty-server-oper:template'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.name is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.tty._meta import _Cisco_IOS_XR_tty_server_oper as meta
                            return meta._meta_table['Tty.AuxiliaryNodes.AuxiliaryNode.AuxiliaryLine.State.Template']['meta_info']


                    class General(object):
                        """
                        General information
                        
                        .. attribute:: operation
                        
                        	application running of on the tty line
                        	**type**\: :py:class:`SessionOperationEnum <ydk.models.tty.Cisco_IOS_XR_tty_server_oper.SessionOperationEnum>`
                        
                        .. attribute:: general_state
                        
                        	State of the line
                        	**type**\: :py:class:`LineStateEnum <ydk.models.tty.Cisco_IOS_XR_tty_server_oper.LineStateEnum>`
                        
                        

                        """

                        _prefix = 'tty-server-oper'
                        _revision = '2015-07-30'

                        def __init__(self):
                            self.parent = None
                            self.operation = None
                            self.general_state = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-tty-server-oper:general'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.operation is not None:
                                return True

                            if self.general_state is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.tty._meta import _Cisco_IOS_XR_tty_server_oper as meta
                            return meta._meta_table['Tty.AuxiliaryNodes.AuxiliaryNode.AuxiliaryLine.State.General']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-tty-server-oper:state'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.template is not None and self.template._has_data():
                            return True

                        if self.general is not None and self.general._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.tty._meta import _Cisco_IOS_XR_tty_server_oper as meta
                        return meta._meta_table['Tty.AuxiliaryNodes.AuxiliaryNode.AuxiliaryLine.State']['meta_info']


                class Configuration(object):
                    """
                    Configuration information of the line
                    
                    .. attribute:: connection_configuration
                    
                    	Conection configuration information
                    	**type**\: :py:class:`ConnectionConfiguration <ydk.models.tty.Cisco_IOS_XR_tty_server_oper.Tty.AuxiliaryNodes.AuxiliaryNode.AuxiliaryLine.Configuration.ConnectionConfiguration>`
                    
                    

                    """

                    _prefix = 'tty-server-oper'
                    _revision = '2015-07-30'

                    def __init__(self):
                        self.parent = None
                        self.connection_configuration = Tty.AuxiliaryNodes.AuxiliaryNode.AuxiliaryLine.Configuration.ConnectionConfiguration()
                        self.connection_configuration.parent = self


                    class ConnectionConfiguration(object):
                        """
                        Conection configuration information
                        
                        .. attribute:: transport_input
                        
                        	Protocols to use when connecting to the terminal server
                        	**type**\: :py:class:`TransportInput <ydk.models.tty.Cisco_IOS_XR_tty_server_oper.Tty.AuxiliaryNodes.AuxiliaryNode.AuxiliaryLine.Configuration.ConnectionConfiguration.TransportInput>`
                        
                        .. attribute:: acl_out
                        
                        	ACL for outbound traffic
                        	**type**\: str
                        
                        .. attribute:: acl_in
                        
                        	ACL for inbound traffic
                        	**type**\: str
                        
                        

                        """

                        _prefix = 'tty-server-oper'
                        _revision = '2015-07-30'

                        def __init__(self):
                            self.parent = None
                            self.transport_input = Tty.AuxiliaryNodes.AuxiliaryNode.AuxiliaryLine.Configuration.ConnectionConfiguration.TransportInput()
                            self.transport_input.parent = self
                            self.acl_out = None
                            self.acl_in = None


                        class TransportInput(object):
                            """
                            Protocols to use when connecting to the
                            terminal server
                            
                            .. attribute:: select
                            
                            	Choose transport protocols
                            	**type**\: :py:class:`TtyTransportProtocolSelectEnum <ydk.models.tty.Cisco_IOS_XR_tty_management_datatypes.TtyTransportProtocolSelectEnum>`
                            
                            .. attribute:: protocol1
                            
                            	Transport protocol1
                            	**type**\: :py:class:`TtyTransportProtocolEnum <ydk.models.tty.Cisco_IOS_XR_tty_management_datatypes.TtyTransportProtocolEnum>`
                            
                            .. attribute:: protocol2
                            
                            	Transport protocol2
                            	**type**\: :py:class:`TtyTransportProtocolEnum <ydk.models.tty.Cisco_IOS_XR_tty_management_datatypes.TtyTransportProtocolEnum>`
                            
                            .. attribute:: none
                            
                            	Not used
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            

                            """

                            _prefix = 'tty-server-oper'
                            _revision = '2015-07-30'

                            def __init__(self):
                                self.parent = None
                                self.select = None
                                self.protocol1 = None
                                self.protocol2 = None
                                self.none = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-tty-server-oper:transport-input'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.select is not None:
                                    return True

                                if self.protocol1 is not None:
                                    return True

                                if self.protocol2 is not None:
                                    return True

                                if self.none is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.tty._meta import _Cisco_IOS_XR_tty_server_oper as meta
                                return meta._meta_table['Tty.AuxiliaryNodes.AuxiliaryNode.AuxiliaryLine.Configuration.ConnectionConfiguration.TransportInput']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-tty-server-oper:connection-configuration'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.transport_input is not None and self.transport_input._has_data():
                                return True

                            if self.acl_out is not None:
                                return True

                            if self.acl_in is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.tty._meta import _Cisco_IOS_XR_tty_server_oper as meta
                            return meta._meta_table['Tty.AuxiliaryNodes.AuxiliaryNode.AuxiliaryLine.Configuration.ConnectionConfiguration']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-tty-server-oper:configuration'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.connection_configuration is not None and self.connection_configuration._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.tty._meta import _Cisco_IOS_XR_tty_server_oper as meta
                        return meta._meta_table['Tty.AuxiliaryNodes.AuxiliaryNode.AuxiliaryLine.Configuration']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-tty-server-oper:auxiliary-line'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.auxiliary_statistics is not None and self.auxiliary_statistics._has_data():
                        return True

                    if self.state is not None and self.state._has_data():
                        return True

                    if self.configuration is not None and self.configuration._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.tty._meta import _Cisco_IOS_XR_tty_server_oper as meta
                    return meta._meta_table['Tty.AuxiliaryNodes.AuxiliaryNode.AuxiliaryLine']['meta_info']

            @property
            def _common_path(self):
                if self.id is None:
                    raise YPYDataValidationError('Key property id is None')

                return '/Cisco-IOS-XR-tty-server-oper:tty/Cisco-IOS-XR-tty-server-oper:auxiliary-nodes/Cisco-IOS-XR-tty-server-oper:auxiliary-node[Cisco-IOS-XR-tty-server-oper:id = ' + str(self.id) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.id is not None:
                    return True

                if self.auxiliary_line is not None and self.auxiliary_line._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.tty._meta import _Cisco_IOS_XR_tty_server_oper as meta
                return meta._meta_table['Tty.AuxiliaryNodes.AuxiliaryNode']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-tty-server-oper:tty/Cisco-IOS-XR-tty-server-oper:auxiliary-nodes'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.auxiliary_node is not None:
                for child_ref in self.auxiliary_node:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.tty._meta import _Cisco_IOS_XR_tty_server_oper as meta
            return meta._meta_table['Tty.AuxiliaryNodes']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-tty-server-oper:tty'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if not self.is_config():
            return False
        if self.console_nodes is not None and self.console_nodes._has_data():
            return True

        if self.vty_lines is not None and self.vty_lines._has_data():
            return True

        if self.auxiliary_nodes is not None and self.auxiliary_nodes._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.tty._meta import _Cisco_IOS_XR_tty_server_oper as meta
        return meta._meta_table['Tty']['meta_info']


