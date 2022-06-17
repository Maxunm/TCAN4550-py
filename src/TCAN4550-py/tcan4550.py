import ctypes
from enum import Enum

uint8_t = ctypes.c_uint8
uint16_t = ctypes.c_uint16
uint32_t = ctypes.c_uint32
import spidev


class TCAN4550:

    def __init__(self, bus: int, device: int) -> None:
        # SPI initialization
        self.spi = spidev.SpiDev(bus, device)
        self.spi.max_speed_hz = 2000000
        self.spi.lsbfirst = False
        self.spi.mode = 0b00
        self.spi.cshigh = True

        # TCAN device initialization

        # Begin by clearing any potential SPI errors
        self.TCAN_clearSPIerr()

        self.dev_ie = TCAN4x5x_device_interrupt_enable()
        self.dev_ie = 0x0  # Initialize to 0 to all bits are set to 0.
        self.TCAN_configure_interrupt_enable(self.dev_ie)  # Disable all non-MCAN related interrupts for simplicity

        self.dev_ir = TCAN4x5x_Device_Interrupts()
        self.dev_ir = 0x0  # Setup a new MCAN IR object for easy interrupt checking
        self.TCAN_read_interrupts(
            self.dev_ir)  # Request that the struct be updated with current DEVICE (not MCAN) interrupt values

        if self.dev_ir.b.PWRON:
            self.TCAN4x5x_Device_ClearInterrupts(self.dev_ir)

        # Configure the CAN bus speeds
        self.TCANNomTiming = TCAN4x5x_MCAN_Nominal_Timing_Simple()  # 500k arbitration with a 40 MHz crystal ((40E6 / 2) / (32 + 8) = 500E3)
        self.TCANNomTiming = 0x0
        self.TCANNomTiming.NominalBitRatePrescaler = 2
        self.TCANNomTiming.NominalTqBeforeSamplePoint = 32
        self.TCANNomTiming.NominalTqAfterSamplePoint = 8

        self.TCANDataTiming = TCAN4x5x_MCAN_Nominal_Timing_Simple()  # 2 Mbps CAN FD with a 40 MHz crystal (40E6 / (15 + 5) = 2E6)
        self.TCANDataTiming = 0x0
        self.TCANDataTiming.DataBitRatePrescaler = 1
        self.TCANDataTiming.DataTqBeforeSamplePoint = 15
        self.TCANDataTiming.DataTqAfterSamplePoint = 5

        # Configure the MCAN core settings
        self.cccrConfig = TCAN4x5x_MCAN_CCCR_Config()
        self.cccrConfig = 0x0  # Remember to initialize to 0, or you'll get random garbage!
        self.cccrConfig.b.FDOE = 1  # CAN FD mode enable
        self.cccrConfig.b.BRSE = 1  # CAN FD Bit rate switch enable

        # Configure the default CAN packet filtering settings
        self.gfc = TCAN4x5x_MCAN_Global_Filter_Configuration()
        self.gfc.b.RRFE = 1  # Reject remote frames (TCAN4x5x doesn't support this)
        self.gfc.b.RRFS = 1  # Reject remote frames (TCAN4x5x doesn't support this)
        self.gfc.b.ANFE = TCAN4x5x_GFC_NO_MATCH_BEHAVIOR.TCAN4x5x_GFC_ACCEPT_INTO_RXFIFO0.value  # Default behavior if incoming message doesn't match a filter is to accept into RXFIO0 for extended ID messages (29 bit IDs)
        self.gfc.b.ANFS = TCAN4x5x_GFC_NO_MATCH_BEHAVIOR.TCAN4x5x_GFC_ACCEPT_INTO_RXFIFO0.value  # Default behavior if incoming message doesn't match a filter is to accept into RXFIO0 for standard ID messages (11 bit IDs)

        '''
        In the next configuration block, we will set the MCAN core up to have:
          - 1 SID filter element
          - 1 XID Filter element
          - 5 RX FIFO 0 elements
          - RX FIFO 0 supports data payloads up to 64 bytes
          - RX FIFO 1 and RX Buffer will not have any elements, but we still set their data payload sizes, even though it's not required
          - No TX Event FIFOs
          - 2 Transmit buffers supporting up to 64 bytes of data payload
        '''
        self.MRAMConfiguration = TCAN4x5x_MRAM_Config()
        self.MRAMConfiguration = 0x0
        self.MRAMConfiguration.XIDNumElements = 1						# Extended ID number of elements, you MUST have a filter written to MRAM for each element defined
        self.MRAMConfiguration.SIDNumElements = 1						# Standard ID number of elements, you MUST have a filter written to MRAM for each element defined
        self.MRAMConfiguration.Rx0NumElements = 5						# RX0 Number of elements
        self.MRAMConfiguration.Rx0ElementSize = TCAN4x5x_MRAM_Element_Data_Size.MRAM_64_Byte_Data		# RX0 data payload size
        self.MRAMConfiguration.Rx1NumElements = 0						# RX1 number of elements
        self.MRAMConfiguration.Rx1ElementSize = TCAN4x5x_MRAM_Element_Data_Size.MRAM_64_Byte_Data		# RX1 data payload size
        self.MRAMConfiguration.RxBufNumElements = 0						# RX buffer number of elements
        self.MRAMConfiguration.RxBufElementSize = TCAN4x5x_MRAM_Element_Data_Size.MRAM_64_Byte_Data		# RX buffer data payload size
        self.MRAMConfiguration.TxEventFIFONumElements = 0				# TX Event FIFO number of elements
        self.MRAMConfiguration.TxBufferNumElements = 2					# TX buffer number of elements
        self.MRAMConfiguration.TxBufferElementSize = TCAN4x5x_MRAM_Element_Data_Size.MRAM_64_Byte_Data	# TX buffer data payload size

    def TCAN4x5x_Device_ClearInterrupts(self, ir):
        pass

    def TCAN_clearSPIerr(self) -> None:
        pass

    def TCAN_configure_interrupt_enable(self, ie) -> bool:
        return True

    def TCAN_read_interrupts(self, ir) -> bool:
        return True

    def TCAN_write_32(self, address, data) -> None:
        pass

    def TCAN_write(self, data, address, no_words) -> None:
        pass

    def TCAN_read_32(self, address, data) -> uint32_t:
        return 0

    def TCAN_read(self, address, data, no_words) -> uint32_t:
        return 0


class TCAN4x5x_GFC_NO_MATCH_BEHAVIOR(Enum):  # No Comments provided in original file
    TCAN4x5x_GFC_ACCEPT_INTO_RXFIFO0 = 0,
    TCAN4x5x_GFC_ACCEPT_INTO_RXFIFO1 = 1,
    TCAN4x5x_GFC_REJECT = 2


class TCAN4x5x_MRAM_Element_Data_Size(Enum):
    # 8 bytes of data payload
    MRAM_8_Byte_Data = 0,

    # 12 bytes of data payload
    MRAM_12_Byte_Data = 0x1,

    # 16 bytes of data payload
    MRAM_16_Byte_Data = 0x2,

    # 20 bytes of data payload
    MRAM_20_Byte_Data = 0x3,

    # 24 bytes of data payload
    MRAM_24_Byte_Data = 0x4,

    # 32 bytes of data payload
    MRAM_32_Byte_Data = 0x5,

    # 48 bytes of data payload
    MRAM_48_Byte_Data = 0x6,

    # 64 bytes of data payload
    MRAM_64_Byte_Data = 0x7


class TCAN4x5x_MCAN_Data_Timing_Simple(ctypes.Structure):
    _fields_ = [
        #  Prescaler value, interpreted as 1:x
        #  Valid range is: 1 to 32
        ("DataBitRatePrescaler", uint8_t, 6),

        #  DTQBSP: Number of time quanta before sample point
        #  Valid values are: 2 to 33
        ("DataTqBeforeSamplePoint", uint8_t, 6),

        # DTQASP: Number of time quanta after sample point
        # Valid values are: 1 to 16
        ("DataTqAfterSamplePoint", uint8_t, 5)
    ]


class TCAN4x5x_MCAN_Data_Timing_Raw(ctypes.Structure):
    _fields_ = [
        # DBRP: The prescaler value from the MCAN system clock. Interpreted by MCAN as the value is this field + 1
        # Valid range is: 0 to 31
        ("DataBitRatePrescaler", uint8_t, 5),

        # DTSEG1: Data time segment 1 + prop segment value. Interpreted by MCAN as the value in this field + 1
        # Valid values are: 0 to 31
        ("DataTimeSeg1andProp", uint8_t, 5),

        # DTSEG2: Data time segment 2. Interpreted by MCAN as the value is this field + 1
        # Valid values are: 0 to 15
        ("DataTimeSeg2", uint8_t, 4),

        # DSJW: Data Resynchronization jump width. Interpreted by MCAN as the value is this field + 1
        # Valid values are: 0 to 15
        ("DataSyncJumpWidth", uint8_t, 4),

        # TDCO: Transmitter delay compensation offset
        # Valid values are 0 to 127 mtq
        ("TDCOffset", uint8_t, 7),

        # TDCFilter: Transmitter delay compensation Filter Window Length
        # Valid values are 0 to 127 mtq
        ("TDCFilter", uint8_t, 7)
    ]


class TCAN4x5x_MCAN_Nominal_Timing_Simple(ctypes.Structure):
    _fields_ = [
        # NBRP: The prescaler value from the MCAN system clock. Value interpreted as 1:x
        # Valid range is: 1 to 512
        ("NominalBitRatePrescaler", uint16_t, 10),

        # NTQBSP: The total number of time quanta prior to sample point
        # Valid values are: 2 to 257
        ("NominalTqBeforeSamplePoint", uint16_t, 9),

        # NTQASP: The total number of time quanta after the sample point
        # Valid values are: 2 to 128
        ("NominalTqAfterSamplePoint", uint8_t, 8)
    ]


class TCAN4x5x_MCAN_Nominal_Timing_Raw(ctypes.Structure):
    _fields_ = [
        # NBRP: The prescaler value from the MCAN system clock. Interpreted by MCAN as the value is this field + 1
        # Valid range is: 0 to 511
        ("NominalBitRatePrescaler", uint16_t, 9),

        # NTSEG1: Data time segment 1 + prop segment value. Interpreted by MCAN as the value is this field + 1
        # Valid values are: 0 to 255
        ("NominalTimeSeg1andProp", uint8_t, 8),

        # NTSEG2: Data time segment 2. Interpreted by MCAN as the value is this field + 1
        # Valid values are: 0 to 127
        ("NominalTimeSeg2", uint8_t, 7),

        # NSJW: Nominal time Resynchronization jump width. Interpreted by MCAN as the value is this field + 1
        # Valid values are: 0 to 127
        ("NominalSyncJumpWidth", uint8_t, 7)
    ]


class TCAN4x5x_MRAM_Config(ctypes.Structure):
    _fields_ = [
        #  ************************
        #    Filter Elements   *
        #  ************************
        # Standard ID Number of Filter Elements: The number of 11-bit filters the user would like
        # Valid range is: 0 to 128
        ("SIDNumElements", uint8_t, 8),

        # Extended ID Number of Filter Elements: The number of 29-bit filters the user would like
        # Valid range is: 0 to 64
        ("XIDNumElements", uint8_t, 7),

        # /************************
        # RX FIFO Elements    *
        # ************************/

        # RX FIFO 0 number of elements: The number of elements for the RX FIFO 0
        # Valid range is: 0 to 64
        ("Rx0NumElements", uint8_t, 7),

        # RX FIFO 0 element size: The number of bytes for the RX 0 FIFO (data payload)
        ("Rx0ElementSize", TCAN4x5x_MRAM_Element_Data_Size, 3),

        # RX FIFO 1 number of elements: The number of elements for the RX FIFO 1
        # Valid range is: 0 to 64
        ("Rx1NumElements", uint8_t, 7),

        # RX FIFO 1 element size: The number of bytes for the RX 1 FIFO (data payload)
        ("Rx1ElementSize", TCAN4x5x_MRAM_Element_Data_Size, 3),

        # RX Buffers number of elements: The number of elements for the RX Buffers (Not the FIFO)
        # Valid range is: 0 to 64
        ("RxBufNumElements", uint8_t, 7),

        # RX Buffers element size: The number of bytes for the RX Buffers (data payload), not the FIFO
        ("RxBufElementSize", TCAN4x5x_MRAM_Element_Data_Size, 3),

        # /************************
        # TX Buffer Elements  *
        # ************************/

        # TX Event FIFO number of elements: The number of elements for the TX Event FIFO
        # Valid range is: 0 to 32
        ("TxEventFIFONumElements", uint8_t, 6),

        # TX Buffers number of elements: The number of elements for the TX Buffers
        # Valid range is: 0 to 32
        ("TxBufferNumElements", uint8_t, 6),

        # TX Buffers element size: The number of bytes for the TX Buffers (data payload)
        ("TxBufferElementSize", TCAN4x5x_MRAM_Element_Data_Size, 3)

    ]


class TCAN4x5x_MCAN_Interrupt_Enable_bits(ctypes.Structure):
    _fields_ = [
        # IE[0] RF0NE: Rx FIFO 0 new message
        ("RF0NE", uint8_t, 1),

        # IE[1] RF0WE: Rx FIFO 0 watermark reached
        ("RF0WE", uint8_t, 1),

        # IE[2] RF0FE: Rx FIFO 0 full
        ("RF0FE", uint8_t, 1),

        # IE[3] RF0LE: Rx FIFO 0 message lost
        ("RF0LE", uint8_t, 1),

        # IE[4] RF1NE: Rx FIFO 1 new message
        ("RF1NE", uint8_t, 1),

        # IE[5]  RF1WE: RX FIFO 1 watermark reached
        ("RF1WE", uint8_t, 1),

        # IE[6] RF1FE: Rx FIFO 1 full
        ("RF1FE", uint8_t, 1),

        # IE[7] RF1LE: Rx FIFO 1 message lost
        ("RF1LE", uint8_t, 1),

        # IE[8] HPME: High priority message
        ("HPME", uint8_t, 1),

        # IE[9] TCE: Transmission completed
        ("TCE", uint8_t, 1),

        # IE[10] TCFE: Transmission cancellation finished
        ("TCFE", uint8_t, 1),

        # IE[11] TFEE: Tx FIFO Empty
        ("TFEE", uint8_t, 1),

        # IE[12] TEFNE: Tx Event FIFO new entry
        ("TEFNE", uint8_t, 1),

        # IE[13] TEFWE: Tx Event FIFO watermark reached
        ("TEFWE", uint8_t, 1),

        # IE[14] TEFFE: Tx Event FIFO full
        ("TEFFE", uint8_t, 1),

        # IE[15] TEFLE: Tx Event FIFO element lost
        ("TEFLE", uint8_t, 1),

        # IE[16] TSWE: Timestamp wraparound
        ("TSWE", uint8_t, 1),

        # IE[17] MRAFE: Message RAM access failure
        ("MRAFE", uint8_t, 1),

        # IE[18] TOOE: Time out occured
        ("TOOE", uint8_t, 1),

        # IE[19] DRXE: Message stored to dedicated RX buffer
        ("DRXE", uint8_t, 1),

        # IE[20] BECE: MRAM Bit error corrected
        ("BECE", uint8_t, 1),

        # IE[21] BEUE: MRAM Bit error uncorrected
        ("BEUE", uint8_t, 1),

        # IE[22] ELOE: Error logging overflow
        ("ELOE", uint8_t, 1),

        # IE[23] EPE: Error_passive status changed
        ("EPE", uint8_t, 1),

        # IE[24] EWE: Error_warning status changed
        ("EWE", uint8_t, 1),

        # IE[25] BOE: Bus_off status changed
        ("BOE", uint8_t, 1),

        # IE[26] WDIE: MRAM Watchdog Interrupt
        ("WDIE", uint8_t, 1),

        # IE[27] PEAE Protocol Error in arbitration phase (nominal bit time used)
        ("PEAE", uint8_t, 1),

        # IE[28] PEDE: Protocol error in data phase (data bit time is used)
        ("PEDE", uint8_t, 1),

        # IE[29] ARAE: Access to reserved address
        ("ARAE", uint8_t, 1),

        # IE[30:31] Reserved, not writable
        ("reserved", uint8_t, 2)
    ]


class TCAN4x5x_MCAN_Interrupt_Enable(ctypes.Union):
    _fields_ = [("b", TCAN4x5x_MCAN_Interrupt_Enable_bits),
                ("word", uint32_t)]


class TCAN4x5x_MCAN_Interrupts_bits(ctypes.Structure):
    _fields_ = [
        # IR[0] RF0N: Rx FIFO 0 new message
        ("RF0N", uint8_t, 1),

        # IR[1] RF0W: Rx FIFO 0 watermark reached
        ("RF0W", uint8_t, 1),

        # IR[2] RF0F: Rx FIFO 0 full
        ("RF0F", uint8_t, 1),

        # IR[3] RF0L: Rx FIFO 0 message lost
        ("RF0L", uint8_t, 1),

        # IR[4] RF1N: Rx FIFO 1 new message
        ("RF1N", uint8_t, 1),

        # IR[5]  RF1W: RX FIFO 1 watermark reached
        ("RF1W", uint8_t, 1),

        # IR[6] RF1F: Rx FIFO 1 full
        ("RF1F", uint8_t, 1),

        # IR[7] RF1L: Rx FIFO 1 message lost
        ("RF1L", uint8_t, 1),

        # IR[8] HPM: High priority message
        ("HPM", uint8_t, 1),

        # IR[9] TC: Transmission completed
        ("TC", uint8_t, 1),

        # IR[10] TCF: Transmission cancellation finished
        ("TCF", uint8_t, 1),

        # IR[11] TFE: Tx FIFO Empty
        ("TFE", uint8_t, 1),

        # IR[12] TEFN: Tx Event FIFO new entry
        ("TEFN", uint8_t, 1),

        # IR[13] TEFW: Tx Event FIFO water mark reached
        ("TEFW", uint8_t, 1),

        # IR[14] TEFF: Tx Event FIFO full
        ("TEFF", uint8_t, 1),

        # IR[15] TEFL: Tx Event FIFO element lost
        ("TEFL", uint8_t, 1),

        # IR[16] TSW: Timestamp wrapped around
        ("TSW", uint8_t, 1),

        # IR[17] MRAF: Message RAM access failure
        ("MRAF", uint8_t, 1),

        # IR[18] TOO: Time out occurred
        ("TOO", uint8_t, 1),

        # IR[19] DRX: Message stored to dedicated RX buffer
        ("DRX", uint8_t, 1),

        # IR[20] BEC: MRAM Bit error corrected
        ("BEC", uint8_t, 1),

        # IR[21] BEU: MRAM Bit error uncorrected
        ("BEU", uint8_t, 1),

        # IR[22] ELO: Error logging overflow
        ("ELO", uint8_t, 1),

        # IR[23] EP: Error_passive status changed
        ("EP", uint8_t, 1),

        # IR[24] EW: Error_warning status changed
        ("EW", uint8_t, 1),

        # IR[25] BO: Bus_off status changed
        ("BO", uint8_t, 1),

        # IR[26] WDI: MRAM Watchdog Interrupt
        ("WDI", uint8_t, 1),

        # IR[27] PEA Protocol Error in arbitration phase (nominal bit time used)
        ("PEA", uint8_t, 1),

        # IR[28] PED: Protocol error in data phase (data bit time is used)
        ("PED", uint8_t, 1),

        # IR[29] ARA: Access to reserved address
        ("ARA", uint8_t, 1),

        # IR[30:31] Reserved, not writable
        ("reserved", uint8_t, 1)
    ]


class TCAN4x5x_MCAN_Interrupts(ctypes.Union):
    _fields_ = [("b", TCAN4x5x_MCAN_Interrupts_bits),
                ("words", uint32_t)]


class TCAN4x5x_MCAN_RX_Header(ctypes.Structure):
    _fields_ = [
        # CAN ID received
        ("ID", uint32_t, 29),

        # Remote Transmission Request flag
        ("RTR", uint8_t, 1),

        # Extended Identifier flag
        ("XTD", uint8_t, 1),

        # Error state indicator flag
        ("ESI", uint8_t, 1),

        # Receive time stamp
        ("RXTS", uint16_t, 16),

        # Data length code
        ("DLC", uint8_t, 4),

        # Bit rate switch used flag
        ("BRS", uint8_t, 1),

        # CAN FD Format flag
        ("FDF", uint8_t, 1),

        # Reserved (0)
        ("reserved", uint8_t, 2),

        # Filter index that this message matched
        ("FIDX", uint8_t, 7),

        # Accepted non matching frame flag
        ("ANMF", uint8_t, 1)
    ]


class TCAN4x5x_Device_Interrupts_bits(ctypes.Structure):
    _fields_ = {
        # DEV_IR[0] VTWD: Global Voltage, Temp, or Watchdog (if equipped) Interrupt
        ("VTWD", uint8_t, 1),

        # DEV_IR[1] M_CAN_INT: There are MCAN interrupts pending
        ("M_CAN_INT", uint8_t, 1),

        # DEV_IR[2] : Selective Wake Error (If equipped)
        ("SWERR", uint8_t, 1),

        # DEV_IR[3] : SPI Error
        ("SPIERR", uint8_t, 1),

        # DEV_IR[4] : CBF, CAN Bus Fault
        ("CBF", uint8_t, 1),

        # DEV_IR[5] : CANERR, CAN Error
        ("CANERR", uint8_t, 1),

        # DEV_IR[6] : WKRQ, Wake Request
        ("WKRQ", uint8_t, 1),

        # DEV_IR[7] : GLOBALERR, Global Error. Is the OR output of all interrupts
        ("GLOBALERR", uint8_t, 1),

        # DEV_IR[8] : CANDOM, Can bus stuck dominant
        ("CANDOM", uint8_t, 1),

        # DEV_IR[9] : RESERVED
        ("RESERVED", uint8_t, 1),

        # DEV_IR[10] : CANTO, CAN Timeout
        ("CANTO", uint8_t, 1),

        # DEV_IR[11] : RESERVED
        ("RESERVED2", uint8_t, 1),

        # DEV_IR[12] : FRAME_OVF, Frame Error Overflow (If Selective Wake is equipped)
        ("FRAME_OVF", uint8_t, 1),

        # DEV_IR[13] : WKERR, Wake Error
        ("WKERR", uint8_t, 1),

        # DEV_IR[14] : LWU, Local Wake Up
        ("LWU", uint8_t, 1),

        # DEV_IR[15] : CANINT, CAN Bus Wake Up Interrupt
        ("CANINT", uint8_t, 1),

        # DEV_IR[16] : ECCERR, MRAM ECC Error
        ("ECCERR", uint8_t, 1),

        # DEV_IR[17] : Reserved
        ("RESERVED3", uint8_t, 1),

        # DEV_IR[18] : WDTO, Watchdog Time Out
        ("WDTO", uint8_t, 1),

        # DEV_IR[19] : TSD, Thermal Shut Down
        ("TSD", uint8_t, 1),

        # DEV_IR[20] : PWRON, Power On Interrupt
        ("PWRON", uint8_t, 1),

        # DEV_IR[21] : UVIO, Undervoltage on UVIO
        ("UVIO", uint8_t, 1),

        # DEV_IR[22] : UVSUP, Undervoltage on VSUP and VCCOUT
        ("UVSUP", uint8_t, 1),

        # DEV_IR[23] : SMS, Sleep Mode Status Flag. Set when sleep mode is entered due to WKERR, UVIO, or TSD faults
        ("SMS", uint8_t, 1),

        # DEV_IR[24] : CANBUSBAT, CAN Shorted to VBAT
        ("CANBUSBAT", uint8_t, 1),

        # DEV_IR[25] : CANBUSGND, CAN Shorted to GND
        ("CANBUSGND", uint8_t, 1),

        # DEV_IR[26] : CANBUSOPEN, CAN Open fault
        ("CANBUSOPEN", uint8_t, 1),

        # DEV_IR[27] : CANLGND, CANL GND
        ("CANLGND", uint8_t, 1),

        # DEV_IR[28] : CANHBAT, CANH to VBAT
        ("CANHBAT", uint8_t, 1),

        # DEV_IR[29] : CANHCANL, CANH and CANL shorted
        ("CANHCANL", uint8_t, 1)

        # DEV_IR[30] : CANBUSTERMOPEN, CAN Bus has termination point open
        ("CANBUSTERMOPEN", uint8_t, 1)

        # DEV_IR[31] : CANBUSNOM, CAN Bus is normal flag
        ("CANBUSNORM", uint8_t, 1)
    }


class TCAN4x5x_Device_Interrupts(ctypes.Union):
    _fields_ = [("b", TCAN4x5x_Device_Interrupts_bits),
                ("word", uint32_t)]


class TCAN4x5x_MCAN_CCCR_Config_bits(ctypes.Structure):
    _fields_ = [
        # Reserved (0)
        ("reserved", uint8_t, 2),

        # ASM: Restricted Operation Mode. The device can only listen to CAN traffic and acknowledge, but not send anything.
        ("ASM", uint8_t, 1),

        # Reserved (0)
        ("reserved2", uint8_t, 1),

        # CSR: Clock stop request
        ("CSR", uint8_t, 1),

        # MON: Bus monitoring mode. The device may only listen to CAN traffic, and is not allowed to acknowledge or send error frames.
        ("MON", uint8_t, 1),

        # DAR: Disable automatic retransmission. If a transmission errors, gets a NACK, or loses arbitration, the MCAN controller will NOT try to transmit again
        ("DAR", uint8_t, 1),

        # TEST: MCAN Test mode enable
        ("TEST", uint8_t, 1),

        # FDOE: Can FD mode enabled, master enable for CAN FD support
        ("FDOE", uint8_t, 1),

        # BRSE: Bit rate switch enabled for can FD. Master enable for bit rate switching support
        ("BRSE", uint8_t, 1),

        # Reserved (0)
        ("reserved3", uint8_t, 1),

        # PXHD: Protocol exception handling disable
        # 0 = Protocol exception handling enabled [default]
        # 1 = protocol exception handling disabled
        ("PXHD", uint8_t, 1),

        # EFBI: Edge filtering during bus integration. 0 Disables this [default]
        ("EFBI", uint8_t, 1),

        # TXP: Transmit Pause Enable: Pause for 2 can bit times before next transmission
        ("TXP", uint8_t, 1),

        # NSIO: Non Iso Operation
        # 0: CAN FD frame format according to ISO 11898-1:2015 [default]
        # 1: CAN FD frame format according to Bosch CAN FD Spec v1
        ("NISO", uint8_t, 1)
    ]


class TCAN4x5x_MCAN_CCCR_Config(ctypes.Union):
    _fields_ = [("b", TCAN4x5x_MCAN_CCCR_Config_bits),
                ("word", uint32_t)]


class TCAN4x5x_MCAN_Global_Filter_Configuration_bits(ctypes.Structure):
    _fields_ = [
        # GFC[0] :  Reject Remote Frames for Extended IDs
        ("RRFE", uint8_t, 1)

        # GFC[1] :  Reject Remote Frames for Standard IDs
        ("RRFS", uint8_t, 1),

        # GFC[3:2] :  Accept Non-matching Frames Extended
        # Valid values:
        # TCAN4x5x_GFC_ACCEPT_INTO_RXFIFO0 : Accept into RXFIFO0
        # TCAN4x5x_GFC_ACCEPT_INTO_RXFIFO1 : Accept into RXFIFO1
        # TCAN4x5x_GFC_REJECT              : Reject
        ("ANFE", TCAN4x5x_GFC_NO_MATCH_BEHAVIOR, 2),

        # GFC[5:4] :  Accept Non-matching Frames Standard
        # Valid values:
        # TCAN4x5x_GFC_ACCEPT_INTO_RXFIFO0 : Accept into RXFIFO0
        # TCAN4x5x_GFC_ACCEPT_INTO_RXFIFO1 : Accept into RXFIFO1
        # TCAN4x5x_GFC_REJECT              : Reject
        ("ANFS", TCAN4x5x_GFC_NO_MATCH_BEHAVIOR, 2),

        # Reserved
        ("reserved", uint32_t, 26)
    ]


class TCAN4x5x_MCAN_Global_Filter_Configuration(ctypes.Union):
    _fields_ = [("b", TCAN4x5x_MCAN_Global_Filter_Configuration_bits),
                ("word", uint32_t)]


class TCAN4x5x_device_interrupt_enable_bits(ctypes.BigEndianStructure):
    _fields_ = [
        # @brief DEV_IE[0:7] : RESERVED
        ("RESERVED1", uint8_t, 8),

        # @brief DEV_IE[8] : CANDOM, Can bus stuck dominant
        ("CANDOMEN", uint8_t, 1),

        # @brief DEV_IE[9] : RESERVED
        ("RESERVED2", uint8_t, 1),

        # @brief DEV_IE[10] : CANTO, CAN Timeout
        ("CANTOEN", uint8_t, 1),

        # @brief DEV_IE[11] : RESERVED
        ("RESERVED3", uint8_t, 1),

        # @brief DEV_IE[12] : FRAME_OVF, Frame Error Overflow (If Selective Wake is equipped)
        ("FRAME_OVFEN", uint8_t, 1),

        # @brief DEV_IE[13] : WKERR, Wake Error
        ("WKERREN", uint8_t, 1),

        # @brief DEV_IE[14] : LWU, Local Wake Up
        ("LWUEN", uint8_t, 1),

        # @brief DEV_IE[15] : CANINT, CAN Bus Wake Up Interrupt
        ("CANINTEN", uint8_t, 1),

        # @brief DEV_IE[16] : ECCERR, MRAM ECC Error
        ("ECCERREN", uint8_t, 1),

        # @brief DEV_IE[17] : Reserved
        ("RESERVED4", uint8_t, 1),

        # @brief DEV_IE[18] : WDTO, Watchdog Time Out
        ("WDTOEN", uint8_t, 1),

        # @brief DEV_IE[19] : TSD, Thermal Shut Down
        ("TSDEN", uint8_t, 1),

        # @brief DEV_IE[20] : PWRON, Power On Interrupt
        ("PWRONEN", uint8_t, 1),

        # @brief DEV_IE[21] : UVIO, Undervoltage on UVIO
        ("UVIOEN", uint8_t, 1),

        # @brief DEV_IE[22] : UVSUP, Undervoltage on VSUP and VCCOUT
        ("UVSUPEN", uint8_t, 1),

        # @brief DEV_IE[23] : SMS, Sleep Mode Status Flag. Set when sleep mode is entered due to WKERR, UVIO, or TSD faults
        ("SMSEN", uint8_t, 1),

        # @brief DEV_IE[24] : CANBUSBAT, CAN Shorted to VBAT
        ("CANBUSBATEN", uint8_t, 1),

        # @brief DEV_IE[25] : CANBUSGND, CAN Shorted to GND
        ("CANBUSGNDEN", uint8_t, 1),

        # @brief DEV_IE[26] : CANBUSOPEN, CAN Open fault
        ("CANBUSOPENEN", uint8_t, 1),

        # @brief DEV_IE[27] : CANLGND, CANL GND
        ("CANLGNDEN", uint8_t, 1),

        # @brief DEV_IE[28] : CANHBAT, CANH to VBAT
        ("CANHBATEN", uint8_t, 1),

        # @brief DEV_IE[29] : CANHCANL, CANH and CANL shorted
        ("CANHCANLEN", uint8_t, 1),

        # @brief DEV_IE[30] : CANBUSTERMOPEN, CAN Bus has termination point open
        ("CANBUSTERMOPENEN", uint8_t, 1),

        # @brief DEV_IE[31] : CANBUSNOM, CAN Bus is normal flag
        ("CANBUSNORMEN", uint8_t, 1)
    ]


class TCAN4x5x_device_interrupt_enable(ctypes.Union):
    _fields_ = [("b", TCAN4x5x_device_interrupt_enable_bits),
                ("word", uint32_t)]
