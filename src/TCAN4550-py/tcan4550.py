import ctypes
uint8_t = ctypes.c_uint8
uint32_t = ctypes.c_uint32

class TCAN4550:

    def __init__(self) -> None:

        self.dev_ie = TCAN4550_device_interrupt_enable()
        self.dev_ie = 0x0
        # Begin by clearing any potential SPI errors
        self.TCAN_clearSPIerr()

        self.TCAN_configure_interrupt_enable(self.dev_ie)


    def TCAN_clearSPIerr(self) -> None:
        pass
    
    def TCAN_configure_interrupt_enable(self, ie) -> bool:
        return True

    def TCAN_write_32(self, address, data) -> None:
        pass
    
    def TCAN_write_word(self, data, address, no_words) -> None:
        pass


    def TCAN_read_32(self, address, data) -> uint32_t:
        return 0
      
    def TCAN_read(self,address, data, no_words) -> uint32_t:
        return 0
    








        

class TCAN4550_device_interrupt_enable_bits(ctypes.LittleEndianStructure):
    _fields_ = [
        # @brief DEV_IE[0:7] : RESERVED
        ("RESERVED1", uint8_t , 8),

        # @brief DEV_IE[8] : CANDOM, Can bus stuck dominant
        ("CANDOMEN", uint8_t , 1),

        # @brief DEV_IE[9] : RESERVED
        ("RESERVED2", uint8_t , 1),

        # @brief DEV_IE[10] : CANTO, CAN Timeout
        ("CANTOEN", uint8_t , 1),
        
        # @brief DEV_IE[11] : RESERVED
        ("RESERVED3", uint8_t , 1),

        # @brief DEV_IE[12] : FRAME_OVF, Frame Error Overflow (If Selective Wake is equipped)
        ("FRAME_OVFEN", uint8_t , 1),

        # @brief DEV_IE[13] : WKERR, Wake Error
        ("WKERREN", uint8_t , 1),

        # @brief DEV_IE[14] : LWU, Local Wake Up
        ("LWUEN", uint8_t , 1),

        # @brief DEV_IE[15] : CANINT, CAN Bus Wake Up Interrupt
        ("CANINTEN", uint8_t , 1),

        # @brief DEV_IE[16] : ECCERR, MRAM ECC Error
        ("ECCERREN", uint8_t , 1),

        # @brief DEV_IE[17] : Reserved
        ("RESERVED4", uint8_t , 1),

        # @brief DEV_IE[18] : WDTO, Watchdog Time Out
        ("WDTOEN", uint8_t , 1),

        # @brief DEV_IE[19] : TSD, Thermal Shut Down
        ("TSDEN", uint8_t , 1),

        # @brief DEV_IE[20] : PWRON, Power On Interrupt
        ("PWRONEN", uint8_t , 1),

        # @brief DEV_IE[21] : UVIO, Undervoltage on UVIO
        ("UVIOEN", uint8_t , 1),

        # @brief DEV_IE[22] : UVSUP, Undervoltage on VSUP and VCCOUT
        ("UVSUPEN", uint8_t , 1),

        # @brief DEV_IE[23] : SMS, Sleep Mode Status Flag. Set when sleep mode is entered due to WKERR, UVIO, or TSD faults
        ("SMSEN", uint8_t , 1),

        # @brief DEV_IE[24] : CANBUSBAT, CAN Shorted to VBAT
        ("CANBUSBATEN", uint8_t , 1),

        # @brief DEV_IE[25] : CANBUSGND, CAN Shorted to GND
        ("CANBUSGNDEN", uint8_t , 1),

        # @brief DEV_IE[26] : CANBUSOPEN, CAN Open fault
        ("CANBUSOPENEN", uint8_t , 1),

        # @brief DEV_IE[27] : CANLGND, CANL GND
        ("CANLGNDEN", uint8_t , 1),

        # @brief DEV_IE[28] : CANHBAT, CANH to VBAT
        ("CANHBATEN", uint8_t , 1),

        # @brief DEV_IE[29] : CANHCANL, CANH and CANL shorted
        ("CANHCANLEN", uint8_t , 1),

        # @brief DEV_IE[30] : CANBUSTERMOPEN, CAN Bus has termination point open
        ("CANBUSTERMOPENEN", uint8_t , 1),

        # @brief DEV_IE[31] : CANBUSNOM, CAN Bus is normal flag
        ("CANBUSNORMEN", uint8_t , 1)
    ]

class TCAN4550_device_interrupt_enable(ctypes.Union):
    _fields_ = [("b", TCAN4550_device_interrupt_enable_bits),
                ("word", uint32_t)]