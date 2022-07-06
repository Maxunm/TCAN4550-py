from TCAN4x5x_Data_Structs import *  # This imports all the types & Data structures
import spidev


class TCAN4550:

    def __init__(self, bus: int, device: int, verify_writes: bool) -> None:
        # Verify Writes variable
        self.TCAN4x5x_DEVICE_VERIFY_CONFIGURATION_WRITES = verify_writes
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
        self.dev_ie.word = 0x0  # Initialize to 0 to all bits are set to 0.
        self.TCAN4x5x_Device_ConfigureInterruptEnable(self.dev_ie)  # Disable all non-MCAN related interrupts for simplicity

        self.dev_ir = TCAN4x5x_Device_Interrupts()
        self.dev_ir.word = 0x0  # Setup a new MCAN IR object for easy interrupt checking
        dev_ir = self.TCAN4x5x_Device_ReadInterrupts()  # Request that the struct be updated with current DEVICE (not MCAN) interrupt values

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
        self.cccrConfig.word = 0x0  # Remember to initialize to 0, or you'll get random garbage!
        self.cccrConfig.b.FDOE = 1  # CAN FD mode enable
        self.cccrConfig.b.BRSE = 1  # CAN FD Bit rate switch enable

        # Configure the default CAN packet filtering settings
        self.gfc = TCAN4x5x_MCAN_Global_Filter_Configuration()
        self.gfc.word = 0x0
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
        self.MRAMConfiguration.word = 0x0
        self.MRAMConfiguration.b.XIDNumElements = 1  # Extended ID number of elements, you MUST have a filter written to MRAM for each element defined
        self.MRAMConfiguration.b.SIDNumElements = 1  # Standard ID number of elements, you MUST have a filter written to MRAM for each element defined
        self.MRAMConfiguration.b.Rx0NumElements = 5  # RX0 Number of elements
        self.MRAMConfiguration.b.Rx0ElementSize = TCAN4x5x_MRAM_Element_Data_Size.MRAM_64_Byte_Data  # RX0 data payload size
        self.MRAMConfiguration.b.Rx1NumElements = 0  # RX1 number of elements
        self.MRAMConfiguration.b.Rx1ElementSize = TCAN4x5x_MRAM_Element_Data_Size.MRAM_64_Byte_Data  # RX1 data payload size
        self.MRAMConfiguration.b.RxBufNumElements = 0  # RX buffer number of elements
        self.MRAMConfiguration.b.RxBufElementSize = TCAN4x5x_MRAM_Element_Data_Size.MRAM_64_Byte_Data  # RX buffer data payload size
        self.MRAMConfiguration.b.TxEventFIFONumElements = 0  # TX Event FIFO number of elements
        self.MRAMConfiguration.b.TxBufferNumElements = 2  # TX buffer number of elements
        self.MRAMConfiguration.b.TxBufferElementSize = TCAN4x5x_MRAM_Element_Data_Size.MRAM_64_Byte_Data  # TX buffer data payload size

        # Configure the MCAN core with the settings above, the changes in this block are write protected registers,      #
        # so it makes the most sense to do them all at once, so we only unlock and lock once                             #/

        self.TCAN4x5x_MCAN_EnableProtectedRegisters()  # Start by making protected registers accessible
        self.TCAN4x5x_MCAN_ConfigureCCCRRegister(self.cccrConfig)  # Enable FD mode and Bit rate switching
        self.TCAN4x5x_MCAN_ConfigureGlobalFilter(
            self.gfc)  # Configure the global filter configuration (Default CAN message behavior)
        self.TCAN4x5x_MCAN_ConfigureNominalTiming_Simple(self.TCANNomTiming)  # Setup nominal/arbitration bit timing
        self.TCAN4x5x_MCAN_ConfigureDataTiming_Simple(self.TCANDataTiming)  # Setup CAN FD timing
        self.TCAN4x5x_MRAM_Clear()  # Clear all of MRAM (Writes 0's to all of it)
        self.TCAN4x5x_MRAM_Configure(
            self.MRAMConfiguration)  # Set up the applicable registers related to MRAM configuration
        self.TCAN4x5x_MCAN_DisableProtectedRegisters()  # Disable protected write and take device out of INIT mode

        # Set the interrupts we want to enable for MCAN #/
        self.mcan_ie = TCAN4x5x_MCAN_Interrupt_Enable()  # Remember to initialize to 0, or you'll get random garbage!
        self.mcan_ie.word = 0x0
        self.mcan_ie.b.RF0NE = 1  # RX FIFO 0 new message interrupt enable

        self.TCAN4x5x_MCAN_ConfigureInterruptEnable(self.mcan_ie)  # Enable the appropriate registers

        # Setup filters, this filter will mark any message with ID 0x055 as a priority message #/
        self.SID_ID = TCAN4x5x_MCAN_SID_Filter()
        self.SID_ID.word = 0x0
        self.SID_ID.b.SFT = TCAN4x5x_SID_SFT_Values.TCAN4x5x_SID_SFT_CLASSIC  # SFT: Standard filter type. Configured as a classic filter
        self.SID_ID.b.SFEC = TCAN4x5x_SID_SFEC_Values.TCAN4x5x_SID_SFEC_PRIORITYSTORERX0  # Standard filter element configuration, store it in RX fifo 0 as a priority message
        self.SID_ID.b.SFID1 = 0x055  # SFID1 (Classic mode Filter)
        self.SID_ID.b.SFID2 = 0x7FF  # SFID2 (Classic mode Mask)
        self.TCAN4x5x_MCAN_WriteSIDFilter(0, self.SID_ID)  # Write to the MRAM

        # Store ID 0x12345678 as a priority message #/
        self.XID_ID = TCAN4x5x_MCAN_XID_Filter()
        self.XID_ID = 0x0
        self.XID_ID.EFT = TCAN4x5x_XID_EFT_Values.TCAN4x5x_XID_EFT_CLASSIC  # EFT
        self.XID_ID.EFEC = TCAN4x5x_XID_EFEC_Values.TCAN4x5x_XID_EFEC_PRIORITYSTORERX0  # EFEC
        self.XID_ID.EFID1 = 0x12345678  # EFID1 (Classic mode filter)
        self.XID_ID.EFID2 = 0x1FFFFFFF  # EFID2 (Classic mode mask)
        self.TCAN4x5x_MCAN_WriteXIDFilter(0, self.XID_ID)  # Write to the MRAM

        # Configure the TCAN4550 Non-CAN-related functions #/
        self.devConfig = TCAN4x5x_DEV_CONFIG()  # Remember to initialize to 0, or you'll get random garbage!
        self.devConfig.word = 0x0
        self.devConfig.b.SWE_DIS = 0  # Keep Sleep Wake Error Enabled (it's a disable bit, not an enable)
        self.devConfig.b.DEVICE_RESET = 0  # Not requesting a software reset
        self.devConfig.b.WD_EN = 0  # Watchdog disabled
        self.devConfig.b.nWKRQ_CONFIG = 0  # Mirror INH function (default)
        self.devConfig.b.INH_DIS = 0  # INH enabled (default)
        self.devConfig.b.GPIO1_GPO_CONFIG = TCAN4x5x_DEV_CONFIG_GPO1_CONFIG.TCAN4x5x_DEV_CONFIG_GPO1_MCAN_INT1  # MCAN nINT 1 (default)
        self.devConfig.b.FAIL_SAFE_EN = 0  # Failsafe disabled (default)
        self.devConfig.b.GPIO1_CONFIG = TCAN4x5x_DEV_CONFIG_GPIO1_CONFIG.TCAN4x5x_DEV_CONFIG_GPIO1_CONFIG_GPO  # GPIO set as GPO (Default)
        self.devConfig.b.WD_ACTION = TCAN4x5x_DEV_CONFIG_WDT_ACTION.TCAN4x5x_DEV_CONFIG_WDT_ACTION_nINT  # Watchdog set an interrupt (default)
        self.devConfig.b.WD_BIT_RESET = 0  # Don't reset the watchdog
        self.devConfig.b.nWKRQ_VOLTAGE = 0  # Set nWKRQ to internal voltage rail (default)
        self.devConfig.b.GPO2_CONFIG = TCAN4x5x_DEV_CONFIG_GPO2_CONFIG.TCAN4x5x_DEV_CONFIG_GPO2_NO_ACTION  # GPO2 has no behavior (default)
        self.devConfig.b.CLK_REF = 1  # Input crystal is a 40 MHz crystal (default)
        self.devConfig.b.WAKE_CONFIG = TCAN4x5x_DEV_CONFIG_WAKE_CONFIG.TCAN4x5x_DEV_CONFIG_WAKE_BOTH_EDGES  # Wake pin can be triggered by either edge (default)
        self.TCAN4x5x_Device_Configure(self.devConfig)  # Configure the device with the above configuration
        self.TCAN4x5x_Device_SetMode(
            TCAN4x5x_Device_Mode_Enum.TCAN4x5x_DEVICE_MODE_NORMAL)  # Set to normal mode, since configuration is done. This line turns on the transceiver
        self.TCAN4x5x_MCAN_ClearInterruptsAll()  # Resets all MCAN interrupts (does NOT include any SPIERR interrupts)

    def TCAN4x5x_Device_ClearInterrupts(self, ir):
        """Clear the device interrupts

        Will attempt to clear any interrupts that are marked as a '1' in the passed **TCAN4x5x_Device_Interrupts** struct
        :param
            ir: is a **TCAN4x5x_Device_Interrupts** struct containing the interrupt bit fields that will be updated
        """
        self.AHB_WRITE_32(REG_DEV_IR, ir.word)

    def TCAN_clearSPIerr(self) -> None:
        """Clear a SPIERR flag that may be set"""
        self.AHB_WRITE_32(REG_SPI_STATUS, 0xFFFFFFFF)

    def TCAN4x5x_Device_ConfigureInterruptEnable(self, ie) -> bool:
        """Configures the device interrupt enable register

        Configures the device interrupt enable register based on the passed **TCAN4x5x_Device_Interrupt_Enable** struct

        :param 
            ie: is a **TCAN4x5x_Device_Interrupt_Enable** struct containing the desired enable interrupt bits
            
        :return: True if configuration successfully done, False if not
        """
        self.AHB_WRITE_32(REG_DEV_IE, ie.word)
        if self.TCAN4x5x_DEVICE_VERIFY_CONFIGURATION_WRITES:
            # Check to see if the write was successful.
            readValue = self.AHB_READ_32(REG_DEV_IE)  # Read value
            readValue = readValue.value & REG_BITS_DEVICE_IE_MASK  # Apply mask to ignore reserved
            if readValue != (ie.word.value & REG_BITS_DEVICE_IE_MASK):
                return False
        return True

    def TCAN4x5x_Device_ReadInterrupts(self) -> TCAN4x5x_Device_Interrupts:
        """Read the device interrupts
        
        Reads the device interrupts and updates a **TCAN4x5x_Device_Interrupts** struct that is passed to the function
        
        :param
            ir: is a pointer to a **TCAN4x5x_Device_Interrupts** struct containing the interrupt bit fields that will be updated
        """
        ir = TCAN4x5x_Device_Interrupts()
        ir.word = self.AHB_READ_32(REG_DEV_IR)
        return ir

    def AHB_WRITE_32(self, address, data) -> None:
        """Single word write

         :param
            address A 16-bit address of the destination register
         
         :param
            data A 32-bit word of data to write to the destination register

        """
        self.TCAN_write(data, address, 1)

    def TCAN_write(self, data, address, no_words) -> None:
        pass

    def AHB_READ_32(self, address) -> uint32_t:
        """Single word read

         :param
            address A 16-bit address of the source register

         :return
            Returns 32-bit word of data from source register

        """
        return self.TCAN_read(address, 1)

    def TCAN_read(self, address, no_words) -> uint32_t:
        return uint32_t(0)

    def TCAN4x5x_MCAN_EnableProtectedRegisters(self) -> bool:
        """ Enable Protected MCAN Registers

        Attempts to enable CCR.CCE and CCR.INIT to allow writes to protected registers, needed for MCAN configuration

        Returns:
            bool: True if successfully enabled, otherwise return False
        """
        pass

    def TCAN4x5x_MCAN_ConfigureCCCRRegister(self, cccrConfig):
        """Configure the MCAN CCCR Register
        
        Configures the bits of the CCCR register to match the CCCR config struct
        
        warning:: This function writes to protected MCAN registers
        
        note:: Requires that protected registers have been unlocked using **TCAN4x5x_MCAN_EnableProtectedRegisters()** and **TCAN4x5x_MCAN_DisableProtectedRegisters()** be used to lock the registers after configuration

        :param
            *cccrConfig is a pointer to a **TCAN4x5x_MCAN_CCCR_Config** struct containing the configuration bits
        returns:
            true if successfully enabled, otherwise return false
        """
        pass

    def TCAN4x5x_MCAN_ConfigureGlobalFilter(self, gfc):
        """Configures the MCAN global filter configuration register, using the passed Global Filter Configuration struct.
 
        Configures the default behavior of the MCAN controller when receiving messages. This can include accepting or rejecting CAN messages by default.

        warning:: This function writes to protected MCAN registers
        
        note:: Requires that protected registers have been unlocked using **TCAN4x5x_MCAN_EnableProtectedRegisters()** and **TCAN4x5x_MCAN_DisableProtectedRegisters()** be used to lock the registers after configuration

        :param 
            *gfc: is a pointer of a **TCAN4x5x_MCAN_Global_Filter_Configuration** struct containing the register values

        return:
            true if successfully enabled, otherwise return false
        """
        pass

    def TCAN4x5x_MCAN_ConfigureNominalTiming_Simple(self, TCANNomTiming):
        """Writes the MCAN nominal timing settings, using the simple nominal timing struct
        
         * Writes the data timing information to MCAN using the input from the ***nomTiming** pointer
         
         warning::This function writes to protected MCAN registers
         
         note::Requires that protected registers have been unlocked using **TCAN4x5x_MCAN_EnableProtectedRegisters()** and **TCAN4x5x_MCAN_DisableProtectedRegisters()** be used to lock the registers after configuration
         
         :param
            *nomTiming is a pointer of a **TCAN4x5x_MCAN_Nominal_Timing_Simple** struct containing the simplified nominal timing information
        return:
            ** true** if successfully enabled, otherwise return false
        """
        pass

    def TCAN4x5x_MCAN_ConfigureDataTiming_Simple(self, TCANDataTiming):
        """Writes the MCAN data time settings, using the simple data timing struct
        
         Writes the data timing information to MCAN using the input from the ***dataTiming** pointer
         
         warning:: This function writes to protected MCAN registers
         
         note::Requires that protected registers have been unlocked using **TCAN4x5x_MCAN_EnableProtectedRegisters()** and  **TCAN4x5x_MCAN_DisableProtectedRegisters()** be used to lock the registers after configuration

        :param
            *dataTiming is a pointer of a **TCAN4x5x_MCAN_Data_Timing_Simple** struct containing the simplified data timing information
            
        :return
            true if successfully enabled, otherwise return false

        """
        pass

    def TCAN4x5x_MRAM_Clear(self):
        """Clear (Zero-fill) the contents of MRAM
        
         Write 0s to every address in MRAM. Useful for initializing the MRAM to known values during initial configuration so that accidental ECC errors do not happen

        """
        pass

    def TCAN4x5x_MRAM_Configure(self, MRAMConfiguration):
        """Configures the MRAM registers

         Uses the ***MRAMConfig** pointer to set up the various sections of the MRAM memory space.
         There are several different elements that may be configured in the MRAM, including their number of elements, as well as size of elements.
         This function will automatically generate the start addresses for each of the appropriate MRAM sections, attempting to place them immediately back-to-back.
         This function will check for over allocated memory conditions, and return false if this is found to be the case.

         warning:: This function writes to protected MCAN registers
         
         note:: Requires that protected registers have been unlocked using **TCAN4x5x_MCAN_EnableProtectedRegisters()** and **TCAN4x5x_MCAN_DisableProtectedRegisters()** be used to lock the registers after configuration

         :param
            *MRAMConfig is a pointer of a **TCAN4x5x_MRAM_Config** struct containing the desired MRAM configuration
         
         :return
            true if successful, otherwise return false

        Args:
            MRAMConfiguration (_type_): _description_
        """
        pass

    def TCAN4x5x_MCAN_DisableProtectedRegisters(self):
        """Disable Protected MCAN Registers

         Attempts to disable CCCR.CCE and CCCR.INIT to disallow writes to protected registers

         :return
            true if successfully enabled, otherwise return false
        """
        pass

    def TCAN4x5x_MCAN_ConfigureInterruptEnable(self, mcan_ie):
        """ Configures the MCAN interrupt enable register

        Configures the MCAN interrupt enable register based on the passed **TCAN4x5x_MCAN_Interrupt_Enable** struct
        Also enables MCAN interrupts out to the INT1 pin.

        :param
            *ie: is a pointer to a **TCAN4x5x_MCAN_Interrupt_Enable** struct containing the desired enabled interrupt bits

        """
        pass

    def TCAN4x5x_MCAN_WriteSIDFilter(self, param, SID_ID):
        """ Write MCAN Standard ID filter into MRAM

         This function will write a standard ID MCAN filter to a specified filter element

         :param
            filterIndex is the SID filter index in MRAM to write to (starts at 0)
         
         :param
            *filter is a pointer to a **TCAN4x5x_MCAN_SID_Filter** struct containing the MCAN filter information

         :return
            true if write was successful, false if not

        """
        pass

    def TCAN4x5x_MCAN_WriteXIDFilter(self, param, XID_ID):
        """Write MCAN Extended ID filter into MRAM

         This function will write an extended ID MCAN filter to a specified filter element

         :param
            filterIndex is the XID filter index in MRAM to write to (starts at 0)
         
         :param
            *filter is a pointer to a **TCAN4x5x_MCAN_XID_Filter** struct containing the MCAN filter information

         @:return
            true if write was successful, false if not
            
        """
        pass

    def TCAN4x5x_Device_Configure(self, devConfig):
        """ Configures the device mode and pin register

         Configures the device mode and pin register based on the passed **TCAN4x5x_DEV_CONFIG** struct, but will mask out the reserved bits on a write

         :param
            *devCfg is a pointer to a **TCAN4x5x_DEV_CONFIG** struct containing the desired device mode and pin register values

         :return
            true if configuration successfully done, false if not

        """
        pass

    def TCAN4x5x_MCAN_ClearInterruptsAll(self):
        """Clear all MCAN interrupts

        Clears all MCAN interrupts
        """
        pass

    def TCAN4x5x_Device_SetMode(self, TCAN4x5x_DEVICE_MODE):
        """Sets the TCAN4x5x device mode

         Sets the TCAN4x5x device mode based on the input **modeDefine** enum

         :param
            modeDefine is an **TCAN4x5x_Device_Mode_Enum** enum

         :return
            true if configuration successfully done, false if not

        """
        pass


