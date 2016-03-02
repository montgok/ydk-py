""" CISCO_SESS_BORDER_CTRLR_STATS_MIB 

The main purpose of this MIB is to define the statistics
information for Session Border Controller application. This MIB
categorizes the statistics information into following types\:
1. RADIUS Messages Statistics \- Represents statistics of
   various RADIUS messages for RADIUS servers with which the
   client (SBC) shares a secret.

2. Rf Billing Statistics\- Represents Rf billing statistics 
   information which monitors the messages sent per\-realm over
   IMS Rx interface by Rf billing manager(SBC).

3. SIP Statistics \- Represents SIP requests and various SIP
   responses on a SIP adjacency in a given interval.

The Session Border Controller (SBC) enables direct IP\-to\-IP
interconnect between multiple administrative domains for
session\-based services providing protocol inter\-working,
security, and admission control and management. The SBC is a
voice over IP (VoIP) device that sits on the border of a 
network and controls call admission to that network. 

The primary purpose of an SBC is to protect the interior of the
network from excessive call load and malicious traffic.
Additional functions provided by the SBC include media bridging
and billing services. 

Periodic Statistics \- Represents the SBC call statistics 
information for a particular time interval. E.g. you can 
specify that you want to retrieve statistics for a summary 
period of the current or previous 5 minutes, 15 minutes, hour, 
or day. The statistics for 5 minutes are divided into five 
minute intervals past the hour \- that is, at 0 minutes, 5 
minutes, 10 minutes... past the hour.  When you retrieve 
statistics for the current five minute period, you will be 
given statistics from the start of the interval to the current
time. When you retrieve statistics for the previous five 
minutes, you will be given the statistics for the entirety of 
the previous interval. For example, if it is currently 12\:43
\-  the current 5 minute statistics cover 12\:40 \- 12\:43

\-  the previous 5 minute statistics cover 12\:35 \- 12\:40

The other intervals work similarly.  15 minute statistics are 
divided into 15 minute intervals past the hour (0 minutes, 15 
minutes, 30 minutes, 45 minutes).  Hourly statistics are divided
into intervals on the hour. Daily statistics are divided into
intervals at 0\:00 each day. Therefore, if you retrieve the 
statistics at 12\:43 for each of these intervals, the periods
covered are as follows.  
\-     current 15 minutes\: 12\:30 \- 12\:43

\-     previous 15 minutes\: 12\:15 \- 12\:30

\-     current hour\: 12\:00 \- 12\:43

\-     last hour\: 11\:00 \- 12\:00

\-     current day\: 00\:00 \- 12\:43

\-     last day\: 00\:00 (the day before) \- 00\:00.


GLOSSARY
SBC\: Session Border Controller

CSB\: CISCO Session Border Controller

Adjacency\: An adjacency contains the system information to be
transmitted to next HOP.

ACR\: Accounting Request

ACA\: Accounting Accept

AVP\: Attribute\-Value Pairs

REFERENCES
1. CISCO Session Border Controller Documents and FAQ
http\://zed.cisco.com/confluence/display/SBC/SBC

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYDataValidationError


from ydk.models.sess.CISCO_SESS_BORDER_CTRLR_CALL_STATS_MIB import CiscoSbcPeriodicStatsInterval_Enum

class CiscoSbcRadiusClientType_Enum(Enum):
    """
    CiscoSbcRadiusClientType_Enum

    This textual convention represents the type of RADIUS client.

    """

    AUTHENTICATION = 1

    ACCOUNTING = 2


    @staticmethod
    def _meta_info():
        from ydk.models.sess._meta import _CISCO_SESS_BORDER_CTRLR_STATS_MIB as meta
        return meta._meta_table['CiscoSbcRadiusClientType_Enum']


class CiscoSbcSIPMethod_Enum(Enum):
    """
    CiscoSbcSIPMethod_Enum

    This textual convention represents the various SIP Methods.

    """

    UNKNOWN = 1

    ACK = 2

    BYE = 3

    CANCEL = 4

    INFO = 5

    INVITE = 6

    MESSAGE = 7

    NOTIFY = 8

    OPTIONS = 9

    PRACK = 10

    REFER = 11

    REGISTER = 12

    SUBSCRIBE = 13

    UPDATE = 14


    @staticmethod
    def _meta_info():
        from ydk.models.sess._meta import _CISCO_SESS_BORDER_CTRLR_STATS_MIB as meta
        return meta._meta_table['CiscoSbcSIPMethod_Enum']



class CISCOSESSBORDERCTRLRSTATSMIB(object):
    """
    
    
    .. attribute:: csbradiusstatstable
    
    	This table has the reporting statistics of various RADIUS messages for RADIUS servers with which the client (SBC) shares a secret. Each entry in this table is identified by a  value of csbRadiusStatsEntIndex. The other indices of this table are csbCallStatsInstanceIndex defined in  csbCallStatsInstanceTable and csbCallStatsServiceIndex defined in csbCallStatsTable
    	**type**\: :py:class:`CsbRadiusStatsTable <ydk.models.sess.CISCO_SESS_BORDER_CTRLR_STATS_MIB.CISCOSESSBORDERCTRLRSTATSMIB.CsbRadiusStatsTable>`
    
    .. attribute:: csbrfbillrealmstatstable
    
    	This table describes the Rf billing statistics information which monitors the messages sent per\-realm by Rf billing  manager(SBC). SBC sends Rf billing data using Diameter as a transport protocol. Rf billing uses only ACR and ACA Diameter messages for the transport of billing data. The Accounting\-Record\-Type AVP on the ACR message labels the type  of the accounting request. The following types are used by Rf billing. 1.   For session\-based charging, the types Start (session begins), Interim (session is modified) and Stop (session ends) are used. 2.   For event\-based charging, the type Event is used when a chargeable event occurs outside the scope of a session.  Each row of this table is identified by a value of csbRfBillRealmStatsIndex and csbRfBillRealmStatsRealmName. The other indices of this table are csbCallStatsInstanceIndex defined in csbCallStatsInstanceTable and  csbCallStatsServiceIndex defined in csbCallStatsTable
    	**type**\: :py:class:`CsbRfBillRealmStatsTable <ydk.models.sess.CISCO_SESS_BORDER_CTRLR_STATS_MIB.CISCOSESSBORDERCTRLRSTATSMIB.CsbRfBillRealmStatsTable>`
    
    .. attribute:: csbsipmthdcurrentstatstable
    
    	This table reports count of SIP request and various SIP responses  for each SIP method on a SIP adjacency in a given interval. Each entry in this table represents a SIP method, its incoming and outgoing count, individual incoming and outgoing  count of various SIP responses for this method on a SIP adjacency in a given interval. To understand the meaning of  interval please refer <Periodic Statistics> section in  description of ciscoSbcStatsMIB.   This table is indexed on csbSIPMthdCurrentStatsAdjName, csbSIPMthdCurrentStatsMethod and  csbSIPMthdCurrentStatsInterval. The other indices of this table are csbCallStatsInstanceIndex defined in  csbCallStatsInstanceTable and csbCallStatsServiceIndex defined in csbCallStatsTable
    	**type**\: :py:class:`CsbSIPMthdCurrentStatsTable <ydk.models.sess.CISCO_SESS_BORDER_CTRLR_STATS_MIB.CISCOSESSBORDERCTRLRSTATSMIB.CsbSIPMthdCurrentStatsTable>`
    
    .. attribute:: csbsipmthdhistorystatstable
    
    	This table provide historical count of SIP request and various SIP responses for each SIP method on a SIP adjacency in various interval length defined by the csbSIPMthdHistoryStatsInterval object. Each entry in this table represents a SIP method, its incoming and outgoing count, individual incoming and outgoing  count of various SIP responses for this method on a SIP adjacency in a given interval. The possible values of interval will be previous 5 minutes, previous 15 minutes, previous 1 hour and previous day. To understand the meaning of interval please refer <Periodic Statistics> description of ciscoSbcStatsMIB. This table is indexed on csbSIPMthdHistoryStatsAdjName, csbSIPMthdHistoryStatsMethod and  csbSIPMthdHistoryStatsInterval. The other indices of this table are csbCallStatsInstanceIndex defined in  csbCallStatsInstanceTable and csbCallStatsServiceIndex defined in csbCallStatsTable
    	**type**\: :py:class:`CsbSIPMthdHistoryStatsTable <ydk.models.sess.CISCO_SESS_BORDER_CTRLR_STATS_MIB.CISCOSESSBORDERCTRLRSTATSMIB.CsbSIPMthdHistoryStatsTable>`
    
    .. attribute:: csbsipmthdrccurrentstatstable
    
    	This table reports SIP method request and response code statistics for each method and response code combination on given SIP adjacency in a given interval. To understand the  meaning of interval please refer <Periodic Statistics> section in description of ciscoSbcStatsMIB. An exact lookup will return a row only  if \- 1) detailed response code statistics are turned on in SBC 2) response code  messages sent or received is non zero for     given SIP adjacency, method and interval. Also an inexact lookup will only return rows for messages with non\-zero counts, to protect the user from large numbers of rows  for response codes which have not been received or sent
    	**type**\: :py:class:`CsbSIPMthdRCCurrentStatsTable <ydk.models.sess.CISCO_SESS_BORDER_CTRLR_STATS_MIB.CISCOSESSBORDERCTRLRSTATSMIB.CsbSIPMthdRCCurrentStatsTable>`
    
    .. attribute:: csbsipmthdrchistorystatstable
    
    	This table reports historical data for SIP method request and response code statistics for each method and response code  combination in a given past interval. The possible values of  interval will be previous 5 minutes, previous 15 minutes,  previous 1 hour and previous day. To understand the  meaning of interval please refer <Periodic Statistics> section in description of ciscoSbcStatsMIB. An exact lookup will return a row only  if \- 1) detailed response code statistics are turned on in SBC 2) response code  messages sent or received is non zero for     given SIP adjacency, method and interval. Also an inexact lookup will only return rows for messages with non\-zero counts, to protect the user from large numbers of rows for response codes which have not been received or sent
    	**type**\: :py:class:`CsbSIPMthdRCHistoryStatsTable <ydk.models.sess.CISCO_SESS_BORDER_CTRLR_STATS_MIB.CISCOSESSBORDERCTRLRSTATSMIB.CsbSIPMthdRCHistoryStatsTable>`
    
    

    """

    _prefix = 'cisco-sess-border'
    _revision = '2010-09-15'

    def __init__(self):
        self.csbradiusstatstable = CISCOSESSBORDERCTRLRSTATSMIB.CsbRadiusStatsTable()
        self.csbradiusstatstable.parent = self
        self.csbrfbillrealmstatstable = CISCOSESSBORDERCTRLRSTATSMIB.CsbRfBillRealmStatsTable()
        self.csbrfbillrealmstatstable.parent = self
        self.csbsipmthdcurrentstatstable = CISCOSESSBORDERCTRLRSTATSMIB.CsbSIPMthdCurrentStatsTable()
        self.csbsipmthdcurrentstatstable.parent = self
        self.csbsipmthdhistorystatstable = CISCOSESSBORDERCTRLRSTATSMIB.CsbSIPMthdHistoryStatsTable()
        self.csbsipmthdhistorystatstable.parent = self
        self.csbsipmthdrccurrentstatstable = CISCOSESSBORDERCTRLRSTATSMIB.CsbSIPMthdRCCurrentStatsTable()
        self.csbsipmthdrccurrentstatstable.parent = self
        self.csbsipmthdrchistorystatstable = CISCOSESSBORDERCTRLRSTATSMIB.CsbSIPMthdRCHistoryStatsTable()
        self.csbsipmthdrchistorystatstable.parent = self


    class CsbRadiusStatsTable(object):
        """
        This table has the reporting statistics of various RADIUS
        messages for RADIUS servers with which the client (SBC) shares a
        secret. Each entry in this table is identified by a 
        value of csbRadiusStatsEntIndex. The other indices of this table
        are csbCallStatsInstanceIndex defined in 
        csbCallStatsInstanceTable and csbCallStatsServiceIndex defined
        in csbCallStatsTable.
        
        .. attribute:: csbradiusstatsentry
        
        	A conceptual row in the csbRadiusStatsTable. There is an entry in this table for each RADIUS server, as identified by a  value of csbRadiusStatsEntIndex. The other indices of this  table are csbCallStatsInstanceIndex defined in  csbCallStatsInstanceTable and csbCallStatsServiceIndex defined in csbCallStatsTable
        	**type**\: list of :py:class:`CsbRadiusStatsEntry <ydk.models.sess.CISCO_SESS_BORDER_CTRLR_STATS_MIB.CISCOSESSBORDERCTRLRSTATSMIB.CsbRadiusStatsTable.CsbRadiusStatsEntry>`
        
        

        """

        _prefix = 'cisco-sess-border'
        _revision = '2010-09-15'

        def __init__(self):
            self.parent = None
            self.csbradiusstatsentry = YList()
            self.csbradiusstatsentry.parent = self
            self.csbradiusstatsentry.name = 'csbradiusstatsentry'


        class CsbRadiusStatsEntry(object):
            """
            A conceptual row in the csbRadiusStatsTable. There is an
            entry in this table for each RADIUS server, as identified by a 
            value of csbRadiusStatsEntIndex. The other indices of this 
            table are csbCallStatsInstanceIndex defined in 
            csbCallStatsInstanceTable and csbCallStatsServiceIndex defined
            in csbCallStatsTable.
            
            .. attribute:: csbcallstatsinstanceindex
            
            	
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: csbcallstatsserviceindex
            
            	
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: csbradiusstatsentindex
            
            	This object indicates the index of the RADIUS client entity that this server is configured on. This index is assigned  arbitrarily by the engine and is not saved over reboots
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: csbradiusstatsacsaccpts
            
            	This object indicates the number of RADIUS Access\-Accept packets (valid or invalid) received from this server
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: csbradiusstatsacschalls
            
            	This object indicates the number of RADIUS Access\-Challenge packets (valid or invalid) received from this server
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: csbradiusstatsacsrejects
            
            	This object indicates the number of RADIUS Access\-Reject packets (valid or invalid) received from this server
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: csbradiusstatsacsreqs
            
            	This object indicates the number of RADIUS Access\-Request packets sent to this server.  This does not include retransmissions
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: csbradiusstatsacsrtrns
            
            	This object indicates the number of RADIUS Access\-Request packets retransmitted to this RADIUS server
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: csbradiusstatsactreqs
            
            	This object indicates the number of RADIUS Accounting\-Request packets sent to this server. This does not include retransmissions
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: csbradiusstatsactretrans
            
            	This object indicates the number of RADIUS Accounting\-Request packets retransmitted to this RADIUS server
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: csbradiusstatsactrsps
            
            	This object indicates the number of RADIUS Accounting\-Response packets (valid or invalid) received from this server
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: csbradiusstatsbadauths
            
            	This object indicates the number of RADIUS response packets containing invalid authenticators or Signature attributes received from this server
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: csbradiusstatsclientname
            
            	This object indicates the client name of the RADIUS client to which that these statistics apply
            	**type**\: str
            
            	**range:** 0..255
            
            .. attribute:: csbradiusstatsclienttype
            
            	This object indicates the type(authentication or accounting) of the RADIUS clients configured on SBC
            	**type**\: :py:class:`CiscoSbcRadiusClientType_Enum <ydk.models.sess.CISCO_SESS_BORDER_CTRLR_STATS_MIB.CiscoSbcRadiusClientType_Enum>`
            
            .. attribute:: csbradiusstatsdropped
            
            	This object indicates the number of RADIUS packets which were received from this server and dropped for some other reason
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: csbradiusstatsmalformedrsps
            
            	This object indicates the number of malformed RADIUS response packets received from this server.  Malformed packets include packets with an invalid length. Bad authenticators, Signature attributes and unknown types are not included as malformed access responses
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: csbradiusstatspending
            
            	This object indicates the number of RADIUS request packets destined for this server that have not yet timed out or received a response. This variable is incremented when a request is sent and decremented on receipt of the response or on a timeout or retransmission
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: csbradiusstatssrvrname
            
            	This object indicates the server name of the RADIUS server to which that these statistics apply
            	**type**\: str
            
            	**range:** 0..255
            
            .. attribute:: csbradiusstatstimeouts
            
            	This object indicates the number of RADIUS request timeouts to this server.  After a timeout the client may retry to a different server or give up. A retry to a different server is counted as a request as well as a timeout
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: csbradiusstatsunknowntype
            
            	This object indicates the number of RADIUS packets of unknown type which were received from this server
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            

            """

            _prefix = 'cisco-sess-border'
            _revision = '2010-09-15'

            def __init__(self):
                self.parent = None
                self.csbcallstatsinstanceindex = None
                self.csbcallstatsserviceindex = None
                self.csbradiusstatsentindex = None
                self.csbradiusstatsacsaccpts = None
                self.csbradiusstatsacschalls = None
                self.csbradiusstatsacsrejects = None
                self.csbradiusstatsacsreqs = None
                self.csbradiusstatsacsrtrns = None
                self.csbradiusstatsactreqs = None
                self.csbradiusstatsactretrans = None
                self.csbradiusstatsactrsps = None
                self.csbradiusstatsbadauths = None
                self.csbradiusstatsclientname = None
                self.csbradiusstatsclienttype = None
                self.csbradiusstatsdropped = None
                self.csbradiusstatsmalformedrsps = None
                self.csbradiusstatspending = None
                self.csbradiusstatssrvrname = None
                self.csbradiusstatstimeouts = None
                self.csbradiusstatsunknowntype = None

            @property
            def _common_path(self):
                if self.csbcallstatsinstanceindex is None:
                    raise YPYDataValidationError('Key property csbcallstatsinstanceindex is None')
                if self.csbcallstatsserviceindex is None:
                    raise YPYDataValidationError('Key property csbcallstatsserviceindex is None')
                if self.csbradiusstatsentindex is None:
                    raise YPYDataValidationError('Key property csbradiusstatsentindex is None')

                return '/CISCO-SESS-BORDER-CTRLR-STATS-MIB:CISCO-SESS-BORDER-CTRLR-STATS-MIB/CISCO-SESS-BORDER-CTRLR-STATS-MIB:csbRadiusStatsTable/CISCO-SESS-BORDER-CTRLR-STATS-MIB:csbRadiusStatsEntry[CISCO-SESS-BORDER-CTRLR-STATS-MIB:csbCallStatsInstanceIndex = ' + str(self.csbcallstatsinstanceindex) + '][CISCO-SESS-BORDER-CTRLR-STATS-MIB:csbCallStatsServiceIndex = ' + str(self.csbcallstatsserviceindex) + '][CISCO-SESS-BORDER-CTRLR-STATS-MIB:csbRadiusStatsEntIndex = ' + str(self.csbradiusstatsentindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.csbcallstatsinstanceindex is not None:
                    return True

                if self.csbcallstatsserviceindex is not None:
                    return True

                if self.csbradiusstatsentindex is not None:
                    return True

                if self.csbradiusstatsacsaccpts is not None:
                    return True

                if self.csbradiusstatsacschalls is not None:
                    return True

                if self.csbradiusstatsacsrejects is not None:
                    return True

                if self.csbradiusstatsacsreqs is not None:
                    return True

                if self.csbradiusstatsacsrtrns is not None:
                    return True

                if self.csbradiusstatsactreqs is not None:
                    return True

                if self.csbradiusstatsactretrans is not None:
                    return True

                if self.csbradiusstatsactrsps is not None:
                    return True

                if self.csbradiusstatsbadauths is not None:
                    return True

                if self.csbradiusstatsclientname is not None:
                    return True

                if self.csbradiusstatsclienttype is not None:
                    return True

                if self.csbradiusstatsdropped is not None:
                    return True

                if self.csbradiusstatsmalformedrsps is not None:
                    return True

                if self.csbradiusstatspending is not None:
                    return True

                if self.csbradiusstatssrvrname is not None:
                    return True

                if self.csbradiusstatstimeouts is not None:
                    return True

                if self.csbradiusstatsunknowntype is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.sess._meta import _CISCO_SESS_BORDER_CTRLR_STATS_MIB as meta
                return meta._meta_table['CISCOSESSBORDERCTRLRSTATSMIB.CsbRadiusStatsTable.CsbRadiusStatsEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-SESS-BORDER-CTRLR-STATS-MIB:CISCO-SESS-BORDER-CTRLR-STATS-MIB/CISCO-SESS-BORDER-CTRLR-STATS-MIB:csbRadiusStatsTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.csbradiusstatsentry is not None:
                for child_ref in self.csbradiusstatsentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.sess._meta import _CISCO_SESS_BORDER_CTRLR_STATS_MIB as meta
            return meta._meta_table['CISCOSESSBORDERCTRLRSTATSMIB.CsbRadiusStatsTable']['meta_info']


    class CsbRfBillRealmStatsTable(object):
        """
        This table describes the Rf billing statistics information
        which monitors the messages sent per\-realm by Rf billing 
        manager(SBC). SBC sends Rf billing data using Diameter as a
        transport protocol. Rf billing uses only ACR and ACA Diameter
        messages for the transport of billing data. The
        Accounting\-Record\-Type AVP on the ACR message labels the type 
        of the accounting request. The following types are used by Rf
        billing.
        1.   For session\-based charging, the types Start (session
        begins), Interim (session is modified) and Stop (session ends)
        are used.
        2.   For event\-based charging, the type Event is used when a
        chargeable event occurs outside the scope of a session.
        
        Each row of this table is identified by a value of
        csbRfBillRealmStatsIndex and csbRfBillRealmStatsRealmName.
        The other indices of this table are csbCallStatsInstanceIndex
        defined in csbCallStatsInstanceTable and 
        csbCallStatsServiceIndex defined in csbCallStatsTable.
        
        .. attribute:: csbrfbillrealmstatsentry
        
        	A conceptual row in the csbRfBillRealmStatsTable. There is an entry in this table for each realm, as identified by a  value of csbRfBillRealmStatsIndex and  csbRfBillRealmStatsRealmName. The other indices of this table are csbCallStatsInstanceIndex defined in csbCallStatsInstanceTable and csbCallStatsServiceIndex defined in csbCallStatsTable
        	**type**\: list of :py:class:`CsbRfBillRealmStatsEntry <ydk.models.sess.CISCO_SESS_BORDER_CTRLR_STATS_MIB.CISCOSESSBORDERCTRLRSTATSMIB.CsbRfBillRealmStatsTable.CsbRfBillRealmStatsEntry>`
        
        

        """

        _prefix = 'cisco-sess-border'
        _revision = '2010-09-15'

        def __init__(self):
            self.parent = None
            self.csbrfbillrealmstatsentry = YList()
            self.csbrfbillrealmstatsentry.parent = self
            self.csbrfbillrealmstatsentry.name = 'csbrfbillrealmstatsentry'


        class CsbRfBillRealmStatsEntry(object):
            """
            A conceptual row in the csbRfBillRealmStatsTable. There
            is an entry in this table for each realm, as identified by a 
            value of csbRfBillRealmStatsIndex and 
            csbRfBillRealmStatsRealmName. The other indices of this
            table are csbCallStatsInstanceIndex defined in
            csbCallStatsInstanceTable and csbCallStatsServiceIndex defined
            in csbCallStatsTable.
            
            .. attribute:: csbcallstatsinstanceindex
            
            	
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: csbcallstatsserviceindex
            
            	
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: csbrfbillrealmstatsindex
            
            	This object indicates the billing method instance index. The range of valid values for this field is 0 \- 31
            	**type**\: int
            
            	**range:** 0..31
            
            .. attribute:: csbrfbillrealmstatsrealmname
            
            	This object indicates the realm for which these statistics are collected. The length of this object is zero when value is not assigned to it
            	**type**\: str
            
            	**range:** 0..255
            
            .. attribute:: csbrfbillrealmstatsfaileventacrs
            
            	This object indicates the total number of failed Event ACRs since start of day or the last time the statistics were reset
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: csbrfbillrealmstatsfailinterimacrs
            
            	This object indicates the total number of failed Interim ACRs since start of day or the last time the statistics were reset
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: csbrfbillrealmstatsfailstartacrs
            
            	This object indicates the total number of failed Start ACRs since start of day or the last time the statistics were reset
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: csbrfbillrealmstatsfailstopacrs
            
            	This object indicates the total number of failed Stop ACRs since start of day or the last time the statistics were reset
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: csbrfbillrealmstatssucceventacrs
            
            	This object indicates the total number of successful Event ACRs since start of day or the last time the statistics were reset
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: csbrfbillrealmstatssuccinterimacrs
            
            	This object indicates the total number of successful Interim ACRs since start of day or the last time the statistics were reset
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: csbrfbillrealmstatssuccstartacrs
            
            	This object indicates the total number of successful Start ACRs since start of day or the last time the statistics were reset
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: csbrfbillrealmstatssuccstopacrs
            
            	This object indicates the total number of successful Stop ACRs since start of day or the last time the statistics were reset
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: csbrfbillrealmstatstotaleventacrs
            
            	This object indicates the combined sum of successful and failed Event ACRs since start of day or the last time the statistics were reset
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: csbrfbillrealmstatstotalinterimacrs
            
            	This object indicates the combined sum of successful and failed Interim ACRs since start of day or the last time the statistics were reset
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: csbrfbillrealmstatstotalstartacrs
            
            	This object indicates the combined sum of successful and failed Start ACRs since start of day or the last time the statistics were reset
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: csbrfbillrealmstatstotalstopacrs
            
            	This object indicates the combined sum of successful and failed Stop ACRs since start of day or the last time the statistics were reset
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'cisco-sess-border'
            _revision = '2010-09-15'

            def __init__(self):
                self.parent = None
                self.csbcallstatsinstanceindex = None
                self.csbcallstatsserviceindex = None
                self.csbrfbillrealmstatsindex = None
                self.csbrfbillrealmstatsrealmname = None
                self.csbrfbillrealmstatsfaileventacrs = None
                self.csbrfbillrealmstatsfailinterimacrs = None
                self.csbrfbillrealmstatsfailstartacrs = None
                self.csbrfbillrealmstatsfailstopacrs = None
                self.csbrfbillrealmstatssucceventacrs = None
                self.csbrfbillrealmstatssuccinterimacrs = None
                self.csbrfbillrealmstatssuccstartacrs = None
                self.csbrfbillrealmstatssuccstopacrs = None
                self.csbrfbillrealmstatstotaleventacrs = None
                self.csbrfbillrealmstatstotalinterimacrs = None
                self.csbrfbillrealmstatstotalstartacrs = None
                self.csbrfbillrealmstatstotalstopacrs = None

            @property
            def _common_path(self):
                if self.csbcallstatsinstanceindex is None:
                    raise YPYDataValidationError('Key property csbcallstatsinstanceindex is None')
                if self.csbcallstatsserviceindex is None:
                    raise YPYDataValidationError('Key property csbcallstatsserviceindex is None')
                if self.csbrfbillrealmstatsindex is None:
                    raise YPYDataValidationError('Key property csbrfbillrealmstatsindex is None')
                if self.csbrfbillrealmstatsrealmname is None:
                    raise YPYDataValidationError('Key property csbrfbillrealmstatsrealmname is None')

                return '/CISCO-SESS-BORDER-CTRLR-STATS-MIB:CISCO-SESS-BORDER-CTRLR-STATS-MIB/CISCO-SESS-BORDER-CTRLR-STATS-MIB:csbRfBillRealmStatsTable/CISCO-SESS-BORDER-CTRLR-STATS-MIB:csbRfBillRealmStatsEntry[CISCO-SESS-BORDER-CTRLR-STATS-MIB:csbCallStatsInstanceIndex = ' + str(self.csbcallstatsinstanceindex) + '][CISCO-SESS-BORDER-CTRLR-STATS-MIB:csbCallStatsServiceIndex = ' + str(self.csbcallstatsserviceindex) + '][CISCO-SESS-BORDER-CTRLR-STATS-MIB:csbRfBillRealmStatsIndex = ' + str(self.csbrfbillrealmstatsindex) + '][CISCO-SESS-BORDER-CTRLR-STATS-MIB:csbRfBillRealmStatsRealmName = ' + str(self.csbrfbillrealmstatsrealmname) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.csbcallstatsinstanceindex is not None:
                    return True

                if self.csbcallstatsserviceindex is not None:
                    return True

                if self.csbrfbillrealmstatsindex is not None:
                    return True

                if self.csbrfbillrealmstatsrealmname is not None:
                    return True

                if self.csbrfbillrealmstatsfaileventacrs is not None:
                    return True

                if self.csbrfbillrealmstatsfailinterimacrs is not None:
                    return True

                if self.csbrfbillrealmstatsfailstartacrs is not None:
                    return True

                if self.csbrfbillrealmstatsfailstopacrs is not None:
                    return True

                if self.csbrfbillrealmstatssucceventacrs is not None:
                    return True

                if self.csbrfbillrealmstatssuccinterimacrs is not None:
                    return True

                if self.csbrfbillrealmstatssuccstartacrs is not None:
                    return True

                if self.csbrfbillrealmstatssuccstopacrs is not None:
                    return True

                if self.csbrfbillrealmstatstotaleventacrs is not None:
                    return True

                if self.csbrfbillrealmstatstotalinterimacrs is not None:
                    return True

                if self.csbrfbillrealmstatstotalstartacrs is not None:
                    return True

                if self.csbrfbillrealmstatstotalstopacrs is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.sess._meta import _CISCO_SESS_BORDER_CTRLR_STATS_MIB as meta
                return meta._meta_table['CISCOSESSBORDERCTRLRSTATSMIB.CsbRfBillRealmStatsTable.CsbRfBillRealmStatsEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-SESS-BORDER-CTRLR-STATS-MIB:CISCO-SESS-BORDER-CTRLR-STATS-MIB/CISCO-SESS-BORDER-CTRLR-STATS-MIB:csbRfBillRealmStatsTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.csbrfbillrealmstatsentry is not None:
                for child_ref in self.csbrfbillrealmstatsentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.sess._meta import _CISCO_SESS_BORDER_CTRLR_STATS_MIB as meta
            return meta._meta_table['CISCOSESSBORDERCTRLRSTATSMIB.CsbRfBillRealmStatsTable']['meta_info']


    class CsbSIPMthdCurrentStatsTable(object):
        """
        This table reports count of SIP request and various SIP
        responses  for each SIP method on a SIP adjacency in a given
        interval. Each entry in this table represents a SIP method, its
        incoming and outgoing count, individual incoming and outgoing 
        count of various SIP responses for this method on a SIP
        adjacency in a given interval. To understand the meaning of 
        interval please refer <Periodic Statistics> section in 
        description of ciscoSbcStatsMIB.  
        This table is indexed on csbSIPMthdCurrentStatsAdjName,
        csbSIPMthdCurrentStatsMethod and 
        csbSIPMthdCurrentStatsInterval. The other indices of this
        table are csbCallStatsInstanceIndex defined in 
        csbCallStatsInstanceTable and csbCallStatsServiceIndex defined
        in csbCallStatsTable.
        
        .. attribute:: csbsipmthdcurrentstatsentry
        
        	A conceptual row in the csbSIPMthdCurrentStatsTable. Each row describes a SIP method and various responses count for this method on a given SIP adjacency and given interval. This table is indexed on csbSIPMthdCurrentStatsAdjName, csbSIPMthdCurrentStatsMethod and  csbSIPMthdCurrentStatsInterval. The other indices of this table are csbCallStatsInstanceIndex defined in  csbCallStatsInstanceTable and csbCallStatsServiceIndex defined in csbCallStatsTable
        	**type**\: list of :py:class:`CsbSIPMthdCurrentStatsEntry <ydk.models.sess.CISCO_SESS_BORDER_CTRLR_STATS_MIB.CISCOSESSBORDERCTRLRSTATSMIB.CsbSIPMthdCurrentStatsTable.CsbSIPMthdCurrentStatsEntry>`
        
        

        """

        _prefix = 'cisco-sess-border'
        _revision = '2010-09-15'

        def __init__(self):
            self.parent = None
            self.csbsipmthdcurrentstatsentry = YList()
            self.csbsipmthdcurrentstatsentry.parent = self
            self.csbsipmthdcurrentstatsentry.name = 'csbsipmthdcurrentstatsentry'


        class CsbSIPMthdCurrentStatsEntry(object):
            """
            A conceptual row in the csbSIPMthdCurrentStatsTable. Each row
            describes a SIP method and various responses count for this
            method on a given SIP adjacency and given interval. This table
            is indexed on csbSIPMthdCurrentStatsAdjName,
            csbSIPMthdCurrentStatsMethod and 
            csbSIPMthdCurrentStatsInterval. The other indices of this
            table are csbCallStatsInstanceIndex defined in 
            csbCallStatsInstanceTable and csbCallStatsServiceIndex defined
            in csbCallStatsTable.
            
            .. attribute:: csbcallstatsinstanceindex
            
            	
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: csbcallstatsserviceindex
            
            	
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: csbsipmthdcurrentstatsadjname
            
            	This object indicates the name of the SIP adjacency for which stats related with SIP request and all kind of corresponding SIP responses are reported. The object acts as an index of the table
            	**type**\: str
            
            	**range:** 0..255
            
            .. attribute:: csbsipmthdcurrentstatsinterval
            
            	This object indicates the interval for which the periodic statistics information is to be displayed. The interval values can be 5 minutes, 15 minutes, 1 hour , 1 Day. This  object acts as an index for the table
            	**type**\: :py:class:`CiscoSbcPeriodicStatsInterval_Enum <ydk.models.sess.CISCO_SESS_BORDER_CTRLR_CALL_STATS_MIB.CiscoSbcPeriodicStatsInterval_Enum>`
            
            .. attribute:: csbsipmthdcurrentstatsmethod
            
            	This object indicates the SIP method Request. The object acts as an index of the table
            	**type**\: :py:class:`CiscoSbcSIPMethod_Enum <ydk.models.sess.CISCO_SESS_BORDER_CTRLR_STATS_MIB.CiscoSbcSIPMethod_Enum>`
            
            .. attribute:: csbsipmthdcurrentstatsmethodname
            
            	This object indicates the text representation of the SIP method request. E.g. INVITE, ACK, BYE etc
            	**type**\: str
            
            	**range:** 0..255
            
            .. attribute:: csbsipmthdcurrentstatsreqin
            
            	This object indicates the total incoming SIP message requests of this type on this SIP adjacency
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: csbsipmthdcurrentstatsreqout
            
            	This object indicates the total outgoing SIP message requests of this type on this SIP adjacency
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: csbsipmthdcurrentstatsresp1xxin
            
            	This object indicates the total 1xx responses for this method received on this SIP adjacency
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: csbsipmthdcurrentstatsresp1xxout
            
            	This object indicates the total 1xx responses for this method sent on this SIP adjacency
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: csbsipmthdcurrentstatsresp2xxin
            
            	This object indicates the total 2xx responses for this method received on this SIP adjacency
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: csbsipmthdcurrentstatsresp2xxout
            
            	This object indicates the total 2xx responses for this method sent on this SIP adjacency
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: csbsipmthdcurrentstatsresp3xxin
            
            	This object indicates the total 3xx responses for this method received on this SIP adjacency
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: csbsipmthdcurrentstatsresp3xxout
            
            	This object indicates the total 3xx responses for this method sent on this SIP adjacency
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: csbsipmthdcurrentstatsresp4xxin
            
            	This object indicates the total 4xx responses for this method received on this SIP adjacency
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: csbsipmthdcurrentstatsresp4xxout
            
            	This object indicates the total 4xx responses for this method sent on this SIP adjacency
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: csbsipmthdcurrentstatsresp5xxin
            
            	This object indicates the total 5xx responses for this method received on this SIP adjacency
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: csbsipmthdcurrentstatsresp5xxout
            
            	This object indicates the total 5xx responses for this method sent on this SIP adjacency
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: csbsipmthdcurrentstatsresp6xxin
            
            	This object indicates the total 6xx responses for this method received on this SIP adjacency
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: csbsipmthdcurrentstatsresp6xxout
            
            	This object indicates the total 6xx responses for this method sent on this SIP adjacency
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'cisco-sess-border'
            _revision = '2010-09-15'

            def __init__(self):
                self.parent = None
                self.csbcallstatsinstanceindex = None
                self.csbcallstatsserviceindex = None
                self.csbsipmthdcurrentstatsadjname = None
                self.csbsipmthdcurrentstatsinterval = None
                self.csbsipmthdcurrentstatsmethod = None
                self.csbsipmthdcurrentstatsmethodname = None
                self.csbsipmthdcurrentstatsreqin = None
                self.csbsipmthdcurrentstatsreqout = None
                self.csbsipmthdcurrentstatsresp1xxin = None
                self.csbsipmthdcurrentstatsresp1xxout = None
                self.csbsipmthdcurrentstatsresp2xxin = None
                self.csbsipmthdcurrentstatsresp2xxout = None
                self.csbsipmthdcurrentstatsresp3xxin = None
                self.csbsipmthdcurrentstatsresp3xxout = None
                self.csbsipmthdcurrentstatsresp4xxin = None
                self.csbsipmthdcurrentstatsresp4xxout = None
                self.csbsipmthdcurrentstatsresp5xxin = None
                self.csbsipmthdcurrentstatsresp5xxout = None
                self.csbsipmthdcurrentstatsresp6xxin = None
                self.csbsipmthdcurrentstatsresp6xxout = None

            @property
            def _common_path(self):
                if self.csbcallstatsinstanceindex is None:
                    raise YPYDataValidationError('Key property csbcallstatsinstanceindex is None')
                if self.csbcallstatsserviceindex is None:
                    raise YPYDataValidationError('Key property csbcallstatsserviceindex is None')
                if self.csbsipmthdcurrentstatsadjname is None:
                    raise YPYDataValidationError('Key property csbsipmthdcurrentstatsadjname is None')
                if self.csbsipmthdcurrentstatsinterval is None:
                    raise YPYDataValidationError('Key property csbsipmthdcurrentstatsinterval is None')
                if self.csbsipmthdcurrentstatsmethod is None:
                    raise YPYDataValidationError('Key property csbsipmthdcurrentstatsmethod is None')

                return '/CISCO-SESS-BORDER-CTRLR-STATS-MIB:CISCO-SESS-BORDER-CTRLR-STATS-MIB/CISCO-SESS-BORDER-CTRLR-STATS-MIB:csbSIPMthdCurrentStatsTable/CISCO-SESS-BORDER-CTRLR-STATS-MIB:csbSIPMthdCurrentStatsEntry[CISCO-SESS-BORDER-CTRLR-STATS-MIB:csbCallStatsInstanceIndex = ' + str(self.csbcallstatsinstanceindex) + '][CISCO-SESS-BORDER-CTRLR-STATS-MIB:csbCallStatsServiceIndex = ' + str(self.csbcallstatsserviceindex) + '][CISCO-SESS-BORDER-CTRLR-STATS-MIB:csbSIPMthdCurrentStatsAdjName = ' + str(self.csbsipmthdcurrentstatsadjname) + '][CISCO-SESS-BORDER-CTRLR-STATS-MIB:csbSIPMthdCurrentStatsInterval = ' + str(self.csbsipmthdcurrentstatsinterval) + '][CISCO-SESS-BORDER-CTRLR-STATS-MIB:csbSIPMthdCurrentStatsMethod = ' + str(self.csbsipmthdcurrentstatsmethod) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.csbcallstatsinstanceindex is not None:
                    return True

                if self.csbcallstatsserviceindex is not None:
                    return True

                if self.csbsipmthdcurrentstatsadjname is not None:
                    return True

                if self.csbsipmthdcurrentstatsinterval is not None:
                    return True

                if self.csbsipmthdcurrentstatsmethod is not None:
                    return True

                if self.csbsipmthdcurrentstatsmethodname is not None:
                    return True

                if self.csbsipmthdcurrentstatsreqin is not None:
                    return True

                if self.csbsipmthdcurrentstatsreqout is not None:
                    return True

                if self.csbsipmthdcurrentstatsresp1xxin is not None:
                    return True

                if self.csbsipmthdcurrentstatsresp1xxout is not None:
                    return True

                if self.csbsipmthdcurrentstatsresp2xxin is not None:
                    return True

                if self.csbsipmthdcurrentstatsresp2xxout is not None:
                    return True

                if self.csbsipmthdcurrentstatsresp3xxin is not None:
                    return True

                if self.csbsipmthdcurrentstatsresp3xxout is not None:
                    return True

                if self.csbsipmthdcurrentstatsresp4xxin is not None:
                    return True

                if self.csbsipmthdcurrentstatsresp4xxout is not None:
                    return True

                if self.csbsipmthdcurrentstatsresp5xxin is not None:
                    return True

                if self.csbsipmthdcurrentstatsresp5xxout is not None:
                    return True

                if self.csbsipmthdcurrentstatsresp6xxin is not None:
                    return True

                if self.csbsipmthdcurrentstatsresp6xxout is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.sess._meta import _CISCO_SESS_BORDER_CTRLR_STATS_MIB as meta
                return meta._meta_table['CISCOSESSBORDERCTRLRSTATSMIB.CsbSIPMthdCurrentStatsTable.CsbSIPMthdCurrentStatsEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-SESS-BORDER-CTRLR-STATS-MIB:CISCO-SESS-BORDER-CTRLR-STATS-MIB/CISCO-SESS-BORDER-CTRLR-STATS-MIB:csbSIPMthdCurrentStatsTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.csbsipmthdcurrentstatsentry is not None:
                for child_ref in self.csbsipmthdcurrentstatsentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.sess._meta import _CISCO_SESS_BORDER_CTRLR_STATS_MIB as meta
            return meta._meta_table['CISCOSESSBORDERCTRLRSTATSMIB.CsbSIPMthdCurrentStatsTable']['meta_info']


    class CsbSIPMthdHistoryStatsTable(object):
        """
        This table provide historical count of SIP request and various
        SIP responses for each SIP method on a SIP adjacency in various
        interval length defined by the csbSIPMthdHistoryStatsInterval
        object. Each entry in this table represents a SIP method, its
        incoming and outgoing count, individual incoming and outgoing 
        count of various SIP responses for this method on a SIP
        adjacency in a given interval. The possible values of interval
        will be previous 5 minutes, previous 15 minutes, previous 1 hour
        and previous day. To understand the meaning of interval please
        refer <Periodic Statistics> description of ciscoSbcStatsMIB.
        This table is indexed on csbSIPMthdHistoryStatsAdjName,
        csbSIPMthdHistoryStatsMethod and 
        csbSIPMthdHistoryStatsInterval. The other indices of this
        table are csbCallStatsInstanceIndex defined in 
        csbCallStatsInstanceTable and csbCallStatsServiceIndex defined
        in csbCallStatsTable.
        
        .. attribute:: csbsipmthdhistorystatsentry
        
        	A conceptual row in the csbSIPMthdHistoryStatsTable. The entries in this table are updated as interval completes in the csbSIPMthdCurrentStatsTable table and the data is  moved from that table to this one. This table is indexed on csbSIPMthdHistoryStatsAdjName, csbSIPMthdHistoryStatsMethod and csbSIPMthdHistoryStatsInterval. The other indices of this  table are csbCallStatsInstanceIndex defined in csbCallStatsInstanceTable and csbCallStatsServiceIndex defined in csbCallStatsTable
        	**type**\: list of :py:class:`CsbSIPMthdHistoryStatsEntry <ydk.models.sess.CISCO_SESS_BORDER_CTRLR_STATS_MIB.CISCOSESSBORDERCTRLRSTATSMIB.CsbSIPMthdHistoryStatsTable.CsbSIPMthdHistoryStatsEntry>`
        
        

        """

        _prefix = 'cisco-sess-border'
        _revision = '2010-09-15'

        def __init__(self):
            self.parent = None
            self.csbsipmthdhistorystatsentry = YList()
            self.csbsipmthdhistorystatsentry.parent = self
            self.csbsipmthdhistorystatsentry.name = 'csbsipmthdhistorystatsentry'


        class CsbSIPMthdHistoryStatsEntry(object):
            """
            A conceptual row in the csbSIPMthdHistoryStatsTable. The
            entries in this table are updated as interval completes in
            the csbSIPMthdCurrentStatsTable table and the data is 
            moved from that table to this one.
            This table is indexed on csbSIPMthdHistoryStatsAdjName,
            csbSIPMthdHistoryStatsMethod and
            csbSIPMthdHistoryStatsInterval. The other indices of this 
            table are csbCallStatsInstanceIndex defined in
            csbCallStatsInstanceTable and csbCallStatsServiceIndex
            defined in csbCallStatsTable.
            
            .. attribute:: csbcallstatsinstanceindex
            
            	
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: csbcallstatsserviceindex
            
            	
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: csbsipmthdhistorystatsadjname
            
            	This object indicates the name of the SIP adjacency for which stats related with SIP request and all kind of corresponding SIP responses are reported. The object acts as an index of the table
            	**type**\: str
            
            	**range:** 0..255
            
            .. attribute:: csbsipmthdhistorystatsinterval
            
            	This object indicates the interval for which the historical statistics information is to be displayed. The interval values can be previous 5 minutes, previous 15 minutes,  previous 1 hour and previous 1 Day. This object acts as an  index for the table
            	**type**\: :py:class:`CiscoSbcPeriodicStatsInterval_Enum <ydk.models.sess.CISCO_SESS_BORDER_CTRLR_CALL_STATS_MIB.CiscoSbcPeriodicStatsInterval_Enum>`
            
            .. attribute:: csbsipmthdhistorystatsmethod
            
            	This object indicates the SIP method Request. The object acts as an index of the table
            	**type**\: :py:class:`CiscoSbcSIPMethod_Enum <ydk.models.sess.CISCO_SESS_BORDER_CTRLR_STATS_MIB.CiscoSbcSIPMethod_Enum>`
            
            .. attribute:: csbsipmthdhistorystatsmethodname
            
            	This object indicates the text representation of the SIP method request. E.g. INVITE, ACK, BYE etc
            	**type**\: str
            
            	**range:** 0..255
            
            .. attribute:: csbsipmthdhistorystatsreqin
            
            	This object indicates the total incoming SIP message requests of this type on this SIP adjacency
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: csbsipmthdhistorystatsreqout
            
            	This object indicates the total outgoing SIP message requests of this type on this SIP adjacency
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: csbsipmthdhistorystatsresp1xxin
            
            	This object indicates the total 1xx responses for this method received on this SIP adjacency
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: csbsipmthdhistorystatsresp1xxout
            
            	This object indicates the total 1xx responses for this method sent on this SIP adjacency
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: csbsipmthdhistorystatsresp2xxin
            
            	This object indicates the total 2xx responses for this method received on this SIP adjacency
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: csbsipmthdhistorystatsresp2xxout
            
            	This object indicates the total 2xx responses for this method sent on this SIP adjacency
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: csbsipmthdhistorystatsresp3xxin
            
            	This object indicates the total 3xx responses for this method received on this SIP adjacency
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: csbsipmthdhistorystatsresp3xxout
            
            	This object indicates the total 3xx responses for this method sent on this SIP adjacency
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: csbsipmthdhistorystatsresp4xxin
            
            	This object indicates the total 4xx responses for this method received on this SIP adjacency
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: csbsipmthdhistorystatsresp4xxout
            
            	This object indicates the total 4xx responses for this method sent on this SIP adjacency
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: csbsipmthdhistorystatsresp5xxin
            
            	This object indicates the total 5xx responses for this method received on this SIP adjacency
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: csbsipmthdhistorystatsresp5xxout
            
            	This object indicates the total 5xx responses for this method sent on this SIP adjacency
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: csbsipmthdhistorystatsresp6xxin
            
            	This object indicates the total 6xx responses for this method received on this SIP adjacency
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: csbsipmthdhistorystatsresp6xxout
            
            	This object indicates the total 6xx responses for this method sent on this SIP adjacency
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'cisco-sess-border'
            _revision = '2010-09-15'

            def __init__(self):
                self.parent = None
                self.csbcallstatsinstanceindex = None
                self.csbcallstatsserviceindex = None
                self.csbsipmthdhistorystatsadjname = None
                self.csbsipmthdhistorystatsinterval = None
                self.csbsipmthdhistorystatsmethod = None
                self.csbsipmthdhistorystatsmethodname = None
                self.csbsipmthdhistorystatsreqin = None
                self.csbsipmthdhistorystatsreqout = None
                self.csbsipmthdhistorystatsresp1xxin = None
                self.csbsipmthdhistorystatsresp1xxout = None
                self.csbsipmthdhistorystatsresp2xxin = None
                self.csbsipmthdhistorystatsresp2xxout = None
                self.csbsipmthdhistorystatsresp3xxin = None
                self.csbsipmthdhistorystatsresp3xxout = None
                self.csbsipmthdhistorystatsresp4xxin = None
                self.csbsipmthdhistorystatsresp4xxout = None
                self.csbsipmthdhistorystatsresp5xxin = None
                self.csbsipmthdhistorystatsresp5xxout = None
                self.csbsipmthdhistorystatsresp6xxin = None
                self.csbsipmthdhistorystatsresp6xxout = None

            @property
            def _common_path(self):
                if self.csbcallstatsinstanceindex is None:
                    raise YPYDataValidationError('Key property csbcallstatsinstanceindex is None')
                if self.csbcallstatsserviceindex is None:
                    raise YPYDataValidationError('Key property csbcallstatsserviceindex is None')
                if self.csbsipmthdhistorystatsadjname is None:
                    raise YPYDataValidationError('Key property csbsipmthdhistorystatsadjname is None')
                if self.csbsipmthdhistorystatsinterval is None:
                    raise YPYDataValidationError('Key property csbsipmthdhistorystatsinterval is None')
                if self.csbsipmthdhistorystatsmethod is None:
                    raise YPYDataValidationError('Key property csbsipmthdhistorystatsmethod is None')

                return '/CISCO-SESS-BORDER-CTRLR-STATS-MIB:CISCO-SESS-BORDER-CTRLR-STATS-MIB/CISCO-SESS-BORDER-CTRLR-STATS-MIB:csbSIPMthdHistoryStatsTable/CISCO-SESS-BORDER-CTRLR-STATS-MIB:csbSIPMthdHistoryStatsEntry[CISCO-SESS-BORDER-CTRLR-STATS-MIB:csbCallStatsInstanceIndex = ' + str(self.csbcallstatsinstanceindex) + '][CISCO-SESS-BORDER-CTRLR-STATS-MIB:csbCallStatsServiceIndex = ' + str(self.csbcallstatsserviceindex) + '][CISCO-SESS-BORDER-CTRLR-STATS-MIB:csbSIPMthdHistoryStatsAdjName = ' + str(self.csbsipmthdhistorystatsadjname) + '][CISCO-SESS-BORDER-CTRLR-STATS-MIB:csbSIPMthdHistoryStatsInterval = ' + str(self.csbsipmthdhistorystatsinterval) + '][CISCO-SESS-BORDER-CTRLR-STATS-MIB:csbSIPMthdHistoryStatsMethod = ' + str(self.csbsipmthdhistorystatsmethod) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.csbcallstatsinstanceindex is not None:
                    return True

                if self.csbcallstatsserviceindex is not None:
                    return True

                if self.csbsipmthdhistorystatsadjname is not None:
                    return True

                if self.csbsipmthdhistorystatsinterval is not None:
                    return True

                if self.csbsipmthdhistorystatsmethod is not None:
                    return True

                if self.csbsipmthdhistorystatsmethodname is not None:
                    return True

                if self.csbsipmthdhistorystatsreqin is not None:
                    return True

                if self.csbsipmthdhistorystatsreqout is not None:
                    return True

                if self.csbsipmthdhistorystatsresp1xxin is not None:
                    return True

                if self.csbsipmthdhistorystatsresp1xxout is not None:
                    return True

                if self.csbsipmthdhistorystatsresp2xxin is not None:
                    return True

                if self.csbsipmthdhistorystatsresp2xxout is not None:
                    return True

                if self.csbsipmthdhistorystatsresp3xxin is not None:
                    return True

                if self.csbsipmthdhistorystatsresp3xxout is not None:
                    return True

                if self.csbsipmthdhistorystatsresp4xxin is not None:
                    return True

                if self.csbsipmthdhistorystatsresp4xxout is not None:
                    return True

                if self.csbsipmthdhistorystatsresp5xxin is not None:
                    return True

                if self.csbsipmthdhistorystatsresp5xxout is not None:
                    return True

                if self.csbsipmthdhistorystatsresp6xxin is not None:
                    return True

                if self.csbsipmthdhistorystatsresp6xxout is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.sess._meta import _CISCO_SESS_BORDER_CTRLR_STATS_MIB as meta
                return meta._meta_table['CISCOSESSBORDERCTRLRSTATSMIB.CsbSIPMthdHistoryStatsTable.CsbSIPMthdHistoryStatsEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-SESS-BORDER-CTRLR-STATS-MIB:CISCO-SESS-BORDER-CTRLR-STATS-MIB/CISCO-SESS-BORDER-CTRLR-STATS-MIB:csbSIPMthdHistoryStatsTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.csbsipmthdhistorystatsentry is not None:
                for child_ref in self.csbsipmthdhistorystatsentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.sess._meta import _CISCO_SESS_BORDER_CTRLR_STATS_MIB as meta
            return meta._meta_table['CISCOSESSBORDERCTRLRSTATSMIB.CsbSIPMthdHistoryStatsTable']['meta_info']


    class CsbSIPMthdRCCurrentStatsTable(object):
        """
        This table reports SIP method request and response code
        statistics for each method and response code combination on
        given SIP adjacency in a given interval. To understand the 
        meaning of interval please refer <Periodic Statistics> section
        in description of ciscoSbcStatsMIB. An exact lookup will return
        a row only  if \-
        1) detailed response code statistics are turned on in SBC
        2) response code  messages sent or received is non zero for 
           given SIP adjacency, method and interval.
        Also an inexact lookup will only return rows for messages with
        non\-zero counts, to protect the user from large numbers of rows 
        for response codes which have not been received or sent.
        
        .. attribute:: csbsipmthdrccurrentstatsentry
        
        	A conceptual row in the csbSIPMthdRCCurrentStatsTable. Each entry in this table represents a method and response code combination. Each entry in this table is identified by a value of csbSIPMthdRCCurrentStatsAdjName, csbSIPMthdRCCurrentStatsMethod, csbSIPMthdRCCurrentStatsRespCode and csbSIPMthdRCCurrentStatsInterval. The other indices of this table are csbCallStatsInstanceIndex defined in csbCallStatsInstanceTable and csbCallStatsServiceIndex defined in csbCallStatsTable
        	**type**\: list of :py:class:`CsbSIPMthdRCCurrentStatsEntry <ydk.models.sess.CISCO_SESS_BORDER_CTRLR_STATS_MIB.CISCOSESSBORDERCTRLRSTATSMIB.CsbSIPMthdRCCurrentStatsTable.CsbSIPMthdRCCurrentStatsEntry>`
        
        

        """

        _prefix = 'cisco-sess-border'
        _revision = '2010-09-15'

        def __init__(self):
            self.parent = None
            self.csbsipmthdrccurrentstatsentry = YList()
            self.csbsipmthdrccurrentstatsentry.parent = self
            self.csbsipmthdrccurrentstatsentry.name = 'csbsipmthdrccurrentstatsentry'


        class CsbSIPMthdRCCurrentStatsEntry(object):
            """
            A conceptual row in the csbSIPMthdRCCurrentStatsTable. Each
            entry in this table represents a method and response code
            combination. Each entry in this table is identified by a value
            of csbSIPMthdRCCurrentStatsAdjName,
            csbSIPMthdRCCurrentStatsMethod,
            csbSIPMthdRCCurrentStatsRespCode and
            csbSIPMthdRCCurrentStatsInterval. The other indices of this
            table are csbCallStatsInstanceIndex defined in
            csbCallStatsInstanceTable and csbCallStatsServiceIndex defined
            in csbCallStatsTable.
            
            .. attribute:: csbcallstatsinstanceindex
            
            	
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: csbcallstatsserviceindex
            
            	
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: csbsipmthdrccurrentstatsadjname
            
            	This identifies the name of the adjacency for which statistics are reported. This object acts as an index for the table
            	**type**\: str
            
            	**range:** 0..255
            
            .. attribute:: csbsipmthdrccurrentstatsinterval
            
            	This object identifies the interval for which the periodic statistics information is to be displayed. The interval values can be 5 min, 15 mins, 1 hour , 1 Day. This object acts as an index for the table
            	**type**\: :py:class:`CiscoSbcPeriodicStatsInterval_Enum <ydk.models.sess.CISCO_SESS_BORDER_CTRLR_CALL_STATS_MIB.CiscoSbcPeriodicStatsInterval_Enum>`
            
            .. attribute:: csbsipmthdrccurrentstatsmethod
            
            	This object indicates the SIP method request. This object acts as an index for the table
            	**type**\: :py:class:`CiscoSbcSIPMethod_Enum <ydk.models.sess.CISCO_SESS_BORDER_CTRLR_STATS_MIB.CiscoSbcSIPMethod_Enum>`
            
            .. attribute:: csbsipmthdrccurrentstatsrespcode
            
            	This object indicates the response code for the SIP message request. The range of valid values for SIP response codes is 100 \- 999. This object acts as an index for the table
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: csbsipmthdrccurrentstatsmethodname
            
            	This object indicates the text representation of the SIP method request. E.g. INVITE, ACK, BYE etc
            	**type**\: str
            
            	**range:** 0..255
            
            .. attribute:: csbsipmthdrccurrentstatsrespin
            
            	This object indicates the total SIP messages with this response code this method received on this SIP adjacency
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: csbsipmthdrccurrentstatsrespout
            
            	This object indicates the total SIP messages with this response code for this method sent on this SIP adjacency
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'cisco-sess-border'
            _revision = '2010-09-15'

            def __init__(self):
                self.parent = None
                self.csbcallstatsinstanceindex = None
                self.csbcallstatsserviceindex = None
                self.csbsipmthdrccurrentstatsadjname = None
                self.csbsipmthdrccurrentstatsinterval = None
                self.csbsipmthdrccurrentstatsmethod = None
                self.csbsipmthdrccurrentstatsrespcode = None
                self.csbsipmthdrccurrentstatsmethodname = None
                self.csbsipmthdrccurrentstatsrespin = None
                self.csbsipmthdrccurrentstatsrespout = None

            @property
            def _common_path(self):
                if self.csbcallstatsinstanceindex is None:
                    raise YPYDataValidationError('Key property csbcallstatsinstanceindex is None')
                if self.csbcallstatsserviceindex is None:
                    raise YPYDataValidationError('Key property csbcallstatsserviceindex is None')
                if self.csbsipmthdrccurrentstatsadjname is None:
                    raise YPYDataValidationError('Key property csbsipmthdrccurrentstatsadjname is None')
                if self.csbsipmthdrccurrentstatsinterval is None:
                    raise YPYDataValidationError('Key property csbsipmthdrccurrentstatsinterval is None')
                if self.csbsipmthdrccurrentstatsmethod is None:
                    raise YPYDataValidationError('Key property csbsipmthdrccurrentstatsmethod is None')
                if self.csbsipmthdrccurrentstatsrespcode is None:
                    raise YPYDataValidationError('Key property csbsipmthdrccurrentstatsrespcode is None')

                return '/CISCO-SESS-BORDER-CTRLR-STATS-MIB:CISCO-SESS-BORDER-CTRLR-STATS-MIB/CISCO-SESS-BORDER-CTRLR-STATS-MIB:csbSIPMthdRCCurrentStatsTable/CISCO-SESS-BORDER-CTRLR-STATS-MIB:csbSIPMthdRCCurrentStatsEntry[CISCO-SESS-BORDER-CTRLR-STATS-MIB:csbCallStatsInstanceIndex = ' + str(self.csbcallstatsinstanceindex) + '][CISCO-SESS-BORDER-CTRLR-STATS-MIB:csbCallStatsServiceIndex = ' + str(self.csbcallstatsserviceindex) + '][CISCO-SESS-BORDER-CTRLR-STATS-MIB:csbSIPMthdRCCurrentStatsAdjName = ' + str(self.csbsipmthdrccurrentstatsadjname) + '][CISCO-SESS-BORDER-CTRLR-STATS-MIB:csbSIPMthdRCCurrentStatsInterval = ' + str(self.csbsipmthdrccurrentstatsinterval) + '][CISCO-SESS-BORDER-CTRLR-STATS-MIB:csbSIPMthdRCCurrentStatsMethod = ' + str(self.csbsipmthdrccurrentstatsmethod) + '][CISCO-SESS-BORDER-CTRLR-STATS-MIB:csbSIPMthdRCCurrentStatsRespCode = ' + str(self.csbsipmthdrccurrentstatsrespcode) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.csbcallstatsinstanceindex is not None:
                    return True

                if self.csbcallstatsserviceindex is not None:
                    return True

                if self.csbsipmthdrccurrentstatsadjname is not None:
                    return True

                if self.csbsipmthdrccurrentstatsinterval is not None:
                    return True

                if self.csbsipmthdrccurrentstatsmethod is not None:
                    return True

                if self.csbsipmthdrccurrentstatsrespcode is not None:
                    return True

                if self.csbsipmthdrccurrentstatsmethodname is not None:
                    return True

                if self.csbsipmthdrccurrentstatsrespin is not None:
                    return True

                if self.csbsipmthdrccurrentstatsrespout is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.sess._meta import _CISCO_SESS_BORDER_CTRLR_STATS_MIB as meta
                return meta._meta_table['CISCOSESSBORDERCTRLRSTATSMIB.CsbSIPMthdRCCurrentStatsTable.CsbSIPMthdRCCurrentStatsEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-SESS-BORDER-CTRLR-STATS-MIB:CISCO-SESS-BORDER-CTRLR-STATS-MIB/CISCO-SESS-BORDER-CTRLR-STATS-MIB:csbSIPMthdRCCurrentStatsTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.csbsipmthdrccurrentstatsentry is not None:
                for child_ref in self.csbsipmthdrccurrentstatsentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.sess._meta import _CISCO_SESS_BORDER_CTRLR_STATS_MIB as meta
            return meta._meta_table['CISCOSESSBORDERCTRLRSTATSMIB.CsbSIPMthdRCCurrentStatsTable']['meta_info']


    class CsbSIPMthdRCHistoryStatsTable(object):
        """
        This table reports historical data for SIP method request and
        response code statistics for each method and response code 
        combination in a given past interval. The possible values of 
        interval will be previous 5 minutes, previous 15 minutes, 
        previous 1 hour and previous day. To understand the 
        meaning of interval please refer <Periodic Statistics> section
        in description of ciscoSbcStatsMIB. An exact lookup will return
        a row only  if \-
        1) detailed response code statistics are turned on in SBC
        2) response code  messages sent or received is non zero for 
           given SIP adjacency, method and interval.
        Also an inexact lookup will only return rows for messages with
        non\-zero counts, to protect the user from large numbers of rows
        for response codes which have not been received or sent.
        
        .. attribute:: csbsipmthdrchistorystatsentry
        
        	A conceptual row in the csbSIPMthdRCHistoryStatsTable. The entries in this table are updated as interval completes in the csbSIPMthdRCCurrentStatsTable table and the data is  moved from that table to this one. Each entry in this table  is identified by a value of csbSIPMthdRCHistoryStatsAdjName,  csbSIPMthdRCHistoryStatsMethod, csbSIPMthdRCHistoryStatsRespCode and csbSIPMthdRCHistoryStatsInterval. The other indices of this table are csbCallStatsInstanceIndex defined in csbCallStatsInstanceTable and csbCallStatsServiceIndex defined in csbCallStatsTable
        	**type**\: list of :py:class:`CsbSIPMthdRCHistoryStatsEntry <ydk.models.sess.CISCO_SESS_BORDER_CTRLR_STATS_MIB.CISCOSESSBORDERCTRLRSTATSMIB.CsbSIPMthdRCHistoryStatsTable.CsbSIPMthdRCHistoryStatsEntry>`
        
        

        """

        _prefix = 'cisco-sess-border'
        _revision = '2010-09-15'

        def __init__(self):
            self.parent = None
            self.csbsipmthdrchistorystatsentry = YList()
            self.csbsipmthdrchistorystatsentry.parent = self
            self.csbsipmthdrchistorystatsentry.name = 'csbsipmthdrchistorystatsentry'


        class CsbSIPMthdRCHistoryStatsEntry(object):
            """
            A conceptual row in the csbSIPMthdRCHistoryStatsTable. The
            entries in this table are updated as interval completes in
            the csbSIPMthdRCCurrentStatsTable table and the data is 
            moved from that table to this one. Each entry in this table 
            is identified by a value of csbSIPMthdRCHistoryStatsAdjName, 
            csbSIPMthdRCHistoryStatsMethod,
            csbSIPMthdRCHistoryStatsRespCode and
            csbSIPMthdRCHistoryStatsInterval. The other indices of this
            table are csbCallStatsInstanceIndex defined in
            csbCallStatsInstanceTable and csbCallStatsServiceIndex defined
            in csbCallStatsTable.
            
            .. attribute:: csbcallstatsinstanceindex
            
            	
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: csbcallstatsserviceindex
            
            	
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: csbsipmthdrchistorystatsadjname
            
            	This identifies the name of the adjacency for which statistics are reported. This object acts as an index for the table
            	**type**\: str
            
            	**range:** 0..255
            
            .. attribute:: csbsipmthdrchistorystatsinterval
            
            	This object identifies the interval for which the periodic statistics information is to be displayed. The interval values can be previous 5 min, previous 15 mins, previous 1  hour , previous 1 Day. This object acts as an index for the table
            	**type**\: :py:class:`CiscoSbcPeriodicStatsInterval_Enum <ydk.models.sess.CISCO_SESS_BORDER_CTRLR_CALL_STATS_MIB.CiscoSbcPeriodicStatsInterval_Enum>`
            
            .. attribute:: csbsipmthdrchistorystatsmethod
            
            	This object indicates the SIP method request. This object acts as an index for the table
            	**type**\: :py:class:`CiscoSbcSIPMethod_Enum <ydk.models.sess.CISCO_SESS_BORDER_CTRLR_STATS_MIB.CiscoSbcSIPMethod_Enum>`
            
            .. attribute:: csbsipmthdrchistorystatsrespcode
            
            	This object indicates the response code for the SIP message request. The range of valid values for SIP response codes is 100 \- 999. This object acts as an index for the table
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: csbsipmthdrchistorystatsmethodname
            
            	This object indicates the text representation of the SIP method request. E.g. INVITE, ACK, BYE etc
            	**type**\: str
            
            	**range:** 0..255
            
            .. attribute:: csbsipmthdrchistorystatsrespin
            
            	This object indicates the total SIP messages with this response code this method received on this SIP adjacency
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: csbsipmthdrchistorystatsrespout
            
            	This object indicates the total SIP messages with this response code for this method sent on this SIP adjacency
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'cisco-sess-border'
            _revision = '2010-09-15'

            def __init__(self):
                self.parent = None
                self.csbcallstatsinstanceindex = None
                self.csbcallstatsserviceindex = None
                self.csbsipmthdrchistorystatsadjname = None
                self.csbsipmthdrchistorystatsinterval = None
                self.csbsipmthdrchistorystatsmethod = None
                self.csbsipmthdrchistorystatsrespcode = None
                self.csbsipmthdrchistorystatsmethodname = None
                self.csbsipmthdrchistorystatsrespin = None
                self.csbsipmthdrchistorystatsrespout = None

            @property
            def _common_path(self):
                if self.csbcallstatsinstanceindex is None:
                    raise YPYDataValidationError('Key property csbcallstatsinstanceindex is None')
                if self.csbcallstatsserviceindex is None:
                    raise YPYDataValidationError('Key property csbcallstatsserviceindex is None')
                if self.csbsipmthdrchistorystatsadjname is None:
                    raise YPYDataValidationError('Key property csbsipmthdrchistorystatsadjname is None')
                if self.csbsipmthdrchistorystatsinterval is None:
                    raise YPYDataValidationError('Key property csbsipmthdrchistorystatsinterval is None')
                if self.csbsipmthdrchistorystatsmethod is None:
                    raise YPYDataValidationError('Key property csbsipmthdrchistorystatsmethod is None')
                if self.csbsipmthdrchistorystatsrespcode is None:
                    raise YPYDataValidationError('Key property csbsipmthdrchistorystatsrespcode is None')

                return '/CISCO-SESS-BORDER-CTRLR-STATS-MIB:CISCO-SESS-BORDER-CTRLR-STATS-MIB/CISCO-SESS-BORDER-CTRLR-STATS-MIB:csbSIPMthdRCHistoryStatsTable/CISCO-SESS-BORDER-CTRLR-STATS-MIB:csbSIPMthdRCHistoryStatsEntry[CISCO-SESS-BORDER-CTRLR-STATS-MIB:csbCallStatsInstanceIndex = ' + str(self.csbcallstatsinstanceindex) + '][CISCO-SESS-BORDER-CTRLR-STATS-MIB:csbCallStatsServiceIndex = ' + str(self.csbcallstatsserviceindex) + '][CISCO-SESS-BORDER-CTRLR-STATS-MIB:csbSIPMthdRCHistoryStatsAdjName = ' + str(self.csbsipmthdrchistorystatsadjname) + '][CISCO-SESS-BORDER-CTRLR-STATS-MIB:csbSIPMthdRCHistoryStatsInterval = ' + str(self.csbsipmthdrchistorystatsinterval) + '][CISCO-SESS-BORDER-CTRLR-STATS-MIB:csbSIPMthdRCHistoryStatsMethod = ' + str(self.csbsipmthdrchistorystatsmethod) + '][CISCO-SESS-BORDER-CTRLR-STATS-MIB:csbSIPMthdRCHistoryStatsRespCode = ' + str(self.csbsipmthdrchistorystatsrespcode) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.csbcallstatsinstanceindex is not None:
                    return True

                if self.csbcallstatsserviceindex is not None:
                    return True

                if self.csbsipmthdrchistorystatsadjname is not None:
                    return True

                if self.csbsipmthdrchistorystatsinterval is not None:
                    return True

                if self.csbsipmthdrchistorystatsmethod is not None:
                    return True

                if self.csbsipmthdrchistorystatsrespcode is not None:
                    return True

                if self.csbsipmthdrchistorystatsmethodname is not None:
                    return True

                if self.csbsipmthdrchistorystatsrespin is not None:
                    return True

                if self.csbsipmthdrchistorystatsrespout is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.sess._meta import _CISCO_SESS_BORDER_CTRLR_STATS_MIB as meta
                return meta._meta_table['CISCOSESSBORDERCTRLRSTATSMIB.CsbSIPMthdRCHistoryStatsTable.CsbSIPMthdRCHistoryStatsEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-SESS-BORDER-CTRLR-STATS-MIB:CISCO-SESS-BORDER-CTRLR-STATS-MIB/CISCO-SESS-BORDER-CTRLR-STATS-MIB:csbSIPMthdRCHistoryStatsTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.csbsipmthdrchistorystatsentry is not None:
                for child_ref in self.csbsipmthdrchistorystatsentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.sess._meta import _CISCO_SESS_BORDER_CTRLR_STATS_MIB as meta
            return meta._meta_table['CISCOSESSBORDERCTRLRSTATSMIB.CsbSIPMthdRCHistoryStatsTable']['meta_info']

    @property
    def _common_path(self):

        return '/CISCO-SESS-BORDER-CTRLR-STATS-MIB:CISCO-SESS-BORDER-CTRLR-STATS-MIB'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if not self.is_config():
            return False
        if self.is_presence():
            return True
        if self.csbradiusstatstable is not None and self.csbradiusstatstable._has_data():
            return True

        if self.csbradiusstatstable is not None and self.csbradiusstatstable.is_presence():
            return True

        if self.csbrfbillrealmstatstable is not None and self.csbrfbillrealmstatstable._has_data():
            return True

        if self.csbrfbillrealmstatstable is not None and self.csbrfbillrealmstatstable.is_presence():
            return True

        if self.csbsipmthdcurrentstatstable is not None and self.csbsipmthdcurrentstatstable._has_data():
            return True

        if self.csbsipmthdcurrentstatstable is not None and self.csbsipmthdcurrentstatstable.is_presence():
            return True

        if self.csbsipmthdhistorystatstable is not None and self.csbsipmthdhistorystatstable._has_data():
            return True

        if self.csbsipmthdhistorystatstable is not None and self.csbsipmthdhistorystatstable.is_presence():
            return True

        if self.csbsipmthdrccurrentstatstable is not None and self.csbsipmthdrccurrentstatstable._has_data():
            return True

        if self.csbsipmthdrccurrentstatstable is not None and self.csbsipmthdrccurrentstatstable.is_presence():
            return True

        if self.csbsipmthdrchistorystatstable is not None and self.csbsipmthdrchistorystatstable._has_data():
            return True

        if self.csbsipmthdrchistorystatstable is not None and self.csbsipmthdrchistorystatstable.is_presence():
            return True

        return False

    def is_presence(self):
        ''' Returns True if this instance represents presence container else returns False '''
        return False

    @staticmethod
    def _meta_info():
        from ydk.models.sess._meta import _CISCO_SESS_BORDER_CTRLR_STATS_MIB as meta
        return meta._meta_table['CISCOSESSBORDERCTRLRSTATSMIB']['meta_info']

