import ctypes

uint8_t = ctypes.c_uint8
uint16_t = ctypes.c_uint16
uint32_t = ctypes.c_uint32

MRAM_SIZE = 2048

# *****************************************************************************
# Register Address Sections
# *****************************************************************************
REG_SPI_CONFIG = 0x0000
REG_DEV_CONFIG = 0x0800
REG_MCAN = 0x1000
REG_MRAM = 0x8000

# *****************************************************************************
# SPI Registers and Device ID Register Addresses: 	0x0000 Prefix
# *****************************************************************************
REG_SPI_DEVICE_ID0 = 0x0000
REG_SPI_DEVICE_ID1 = 0x0004
REG_SPI_REVISION = 0x0008
REG_SPI_STATUS = 0x000C
REG_SPI_ERROR_STATUS_MASK = 0x0010

# *****************************************************************************
# Device Configuration Register Addresses: 	0x0800 Prefix
# *****************************************************************************
REG_DEV_MODES_AND_PINS = 0x0800
REG_DEV_TIMESTAMP_PRESCALER = 0x0804
REG_DEV_TEST_REGISTERS = 0x0808
REG_DEV_IR = 0x0820
REG_DEV_IE = 0x0830

# *****************************************************************************
# MCAN Register Addresses: 	0x1000 Prefix
# *****************************************************************************
REG_MCAN_CREL = 0x1000
REG_MCAN_ENDN = 0x1004
REG_MCAN_CUST = 0x1008
REG_MCAN_DBTP = 0x100C
REG_MCAN_TEST = 0x1010
REG_MCAN_RWD = 0x1014
REG_MCAN_CCCR = 0x1018
REG_MCAN_NBTP = 0x101C
REG_MCAN_TSCC = 0x1020
REG_MCAN_TSCV = 0x1024
REG_MCAN_TOCC = 0x1028
REG_MCAN_TOCV = 0x102C
REG_MCAN_ECR = 0x1040
REG_MCAN_PSR = 0x1044
REG_MCAN_TDCR = 0x1048
REG_MCAN_IR = 0x1050
REG_MCAN_IE = 0x1054
REG_MCAN_ILS = 0x1058
REG_MCAN_ILE = 0x105C
REG_MCAN_GFC = 0x1080
REG_MCAN_SIDFC = 0x1084
REG_MCAN_XIDFC = 0x1088
REG_MCAN_XIDAM = 0x1090
REG_MCAN_HPMS = 0x1094
REG_MCAN_NDAT1 = 0x1098
REG_MCAN_NDAT2 = 0x109C
REG_MCAN_RXF0C = 0x10A0
REG_MCAN_RXF0S = 0x10A4
REG_MCAN_RXF0A = 0x10A8
REG_MCAN_RXBC = 0x10AC
REG_MCAN_RXF1C = 0x10B0
REG_MCAN_RXF1S = 0x10B4
REG_MCAN_RXF1A = 0x10B8
REG_MCAN_RXESC = 0x10BC
REG_MCAN_TXBC = 0x10C0
REG_MCAN_TXFQS = 0x10C4
REG_MCAN_TXESC = 0x10C8
REG_MCAN_TXBRP = 0x10CC
REG_MCAN_TXBAR = 0x10D0
REG_MCAN_TXBCR = 0x10D4
REG_MCAN_TXBTO = 0x10D8
REG_MCAN_TXBCF = 0x10DC
REG_MCAN_TXBTIE = 0x10E0
REG_MCAN_TXBCIE = 0x10E4
REG_MCAN_TXEFC = 0x10F0
REG_MCAN_TXEFS = 0x10F4
REG_MCAN_TXEFA = 0x10F8
# *****************************************************************************

# *****************************************************************************
# DLC Value Defines: Used for RX and TX elements. The DLC[3:0] bit field
# *****************************************************************************
MCAN_DLC_0B = 0x00000000
MCAN_DLC_1B = 0x00000001
MCAN_DLC_2B = 0x00000002
MCAN_DLC_3B = 0x00000003
MCAN_DLC_4B = 0x00000004
MCAN_DLC_5B = 0x00000005
MCAN_DLC_6B = 0x00000006
MCAN_DLC_7B = 0x00000007
MCAN_DLC_8B = 0x00000008
MCAN_DLC_12B = 0x00000009
MCAN_DLC_16B = 0x0000000A
MCAN_DLC_20B = 0x0000000B
MCAN_DLC_24B = 0x0000000C
MCAN_DLC_32B = 0x0000000D
MCAN_DLC_48B = 0x0000000E
MCAN_DLC_64B = 0x0000000F
# *****************************************************************************

# *****************************************************************************
# MCAN Register Bit Field Defines
# *****************************************************************************

# DBTP
REG_BITS_MCAN_DBTP_TDC_EN = 0x00800000

# TEST
REG_BITS_MCAN_TEST_RX_DOM = 0x00000000
REG_BITS_MCAN_TEST_RX_REC = 0x00000080
REG_BITS_MCAN_TEST_TX_SP = 0x00000020
REG_BITS_MCAN_TEST_TX_DOM = 0x00000040
REG_BITS_MCAN_TEST_TX_REC = 0x00000060
REG_BITS_MCAN_TEST_LOOP_BACK = 0x00000010

# CCCR
REG_BITS_MCAN_CCCR_RESERVED_MASK = 0xFFFF0C00
REG_BITS_MCAN_CCCR_NISO_ISO = 0x00000000
REG_BITS_MCAN_CCCR_NISO_BOSCH = 0x00008000
REG_BITS_MCAN_CCCR_TXP = 0x00004000
REG_BITS_MCAN_CCCR_EFBI = 0x00002000
REG_BITS_MCAN_CCCR_PXHD_DIS = 0x00001000
REG_BITS_MCAN_CCCR_BRSE = 0x00000200
REG_BITS_MCAN_CCCR_FDOE = 0x00000100
REG_BITS_MCAN_CCCR_TEST = 0x00000080
REG_BITS_MCAN_CCCR_DAR_DIS = 0x00000040
REG_BITS_MCAN_CCCR_MON = 0x00000020
REG_BITS_MCAN_CCCR_CSR = 0x00000010
REG_BITS_MCAN_CCCR_CSA = 0x00000008
REG_BITS_MCAN_CCCR_ASM = 0x00000004
REG_BITS_MCAN_CCCR_CCE = 0x00000002
REG_BITS_MCAN_CCCR_INIT = 0x00000001

# IE
REG_BITS_MCAN_IE_ARAE = 0x20000000
REG_BITS_MCAN_IE_PEDE = 0x10000000
REG_BITS_MCAN_IE_PEAE = 0x08000000
REG_BITS_MCAN_IE_WDIE = 0x04000000
REG_BITS_MCAN_IE_BOE = 0x02000000
REG_BITS_MCAN_IE_EWE = 0x01000000
REG_BITS_MCAN_IE_EPE = 0x00800000
REG_BITS_MCAN_IE_ELOE = 0x00400000
REG_BITS_MCAN_IE_BEUE = 0x00200000
REG_BITS_MCAN_IE_BECE = 0x00100000
REG_BITS_MCAN_IE_DRXE = 0x00080000
REG_BITS_MCAN_IE_TOOE = 0x00040000
REG_BITS_MCAN_IE_MRAFE = 0x00020000
REG_BITS_MCAN_IE_TSWE = 0x00010000
REG_BITS_MCAN_IE_TEFLE = 0x00008000
REG_BITS_MCAN_IE_TEFFE = 0x00004000
REG_BITS_MCAN_IE_TEFWE = 0x00002000
REG_BITS_MCAN_IE_TEFNE = 0x00001000
REG_BITS_MCAN_IE_TFEE = 0x00000800
REG_BITS_MCAN_IE_TCFE = 0x00000400
REG_BITS_MCAN_IE_TCE = 0x00000200
REG_BITS_MCAN_IE_HPME = 0x00000100
REG_BITS_MCAN_IE_RF1LE = 0x00000080
REG_BITS_MCAN_IE_RF1FE = 0x00000040
REG_BITS_MCAN_IE_RF1WE = 0x00000020
REG_BITS_MCAN_IE_RF1NE = 0x00000010
REG_BITS_MCAN_IE_RF0LE = 0x00000008
REG_BITS_MCAN_IE_RF0FE = 0x00000004
REG_BITS_MCAN_IE_RF0WE = 0x00000002
REG_BITS_MCAN_IE_RF0NE = 0x00000001

# IR
REG_BITS_MCAN_IR_ARA = 0x20000000
REG_BITS_MCAN_IR_PED = 0x10000000
REG_BITS_MCAN_IR_PEA = 0x08000000
REG_BITS_MCAN_IR_WDI = 0x04000000
REG_BITS_MCAN_IR_BO = 0x02000000
REG_BITS_MCAN_IR_EW = 0x01000000
REG_BITS_MCAN_IR_EP = 0x00800000
REG_BITS_MCAN_IR_ELO = 0x00400000
REG_BITS_MCAN_IR_BEU = 0x00200000
REG_BITS_MCAN_IR_BEC = 0x00100000
REG_BITS_MCAN_IR_DRX = 0x00080000
REG_BITS_MCAN_IR_TOO = 0x00040000
REG_BITS_MCAN_IR_MRAF = 0x00020000
REG_BITS_MCAN_IR_TSW = 0x00010000
REG_BITS_MCAN_IR_TEFL = 0x00008000
REG_BITS_MCAN_IR_TEFF = 0x00004000
REG_BITS_MCAN_IR_TEFW = 0x00002000
REG_BITS_MCAN_IR_TEFN = 0x00001000
REG_BITS_MCAN_IR_TFE = 0x00000800
REG_BITS_MCAN_IR_TCF = 0x00000400
REG_BITS_MCAN_IR_TC = 0x00000200
REG_BITS_MCAN_IR_HPM = 0x00000100
REG_BITS_MCAN_IR_RF1L = 0x00000080
REG_BITS_MCAN_IR_RF1F = 0x00000040
REG_BITS_MCAN_IR_RF1W = 0x00000020
REG_BITS_MCAN_IR_RF1N = 0x00000010
REG_BITS_MCAN_IR_RF0L = 0x00000008
REG_BITS_MCAN_IR_RF0F = 0x00000004
REG_BITS_MCAN_IR_RF0W = 0x00000002
REG_BITS_MCAN_IR_RF0N = 0x00000001

# ILS
REG_BITS_MCAN_IE_ARAL = 0x20000000
REG_BITS_MCAN_IE_PEDL = 0x10000000
REG_BITS_MCAN_IE_PEAL = 0x08000000
REG_BITS_MCAN_IE_WDIL = 0x04000000
REG_BITS_MCAN_IE_BOL = 0x02000000
REG_BITS_MCAN_IE_EWL = 0x01000000
REG_BITS_MCAN_IE_EPL = 0x00800000
REG_BITS_MCAN_IE_ELOL = 0x00400000
REG_BITS_MCAN_IE_BEUL = 0x00200000
REG_BITS_MCAN_IE_BECL = 0x00100000
REG_BITS_MCAN_IE_DRXL = 0x00080000
REG_BITS_MCAN_IE_TOOL = 0x00040000
REG_BITS_MCAN_IE_MRAFL = 0x00020000
REG_BITS_MCAN_IE_TSWL = 0x00010000
REG_BITS_MCAN_IE_TEFLL = 0x00008000
REG_BITS_MCAN_IE_TEFFL = 0x00004000
REG_BITS_MCAN_IE_TEFWL = 0x00002000
REG_BITS_MCAN_IE_TEFNL = 0x00001000
REG_BITS_MCAN_IE_TFEL = 0x00000800
REG_BITS_MCAN_IE_TCFL = 0x00000400
REG_BITS_MCAN_IE_TCL = 0x00000200
REG_BITS_MCAN_IE_HPML = 0x00000100
REG_BITS_MCAN_IE_RF1LL = 0x00000080
REG_BITS_MCAN_IE_RF1FL = 0x00000040
REG_BITS_MCAN_IE_RF1WL = 0x00000020
REG_BITS_MCAN_IE_RF1NL = 0x00000010
REG_BITS_MCAN_IE_RF0LL = 0x00000008
REG_BITS_MCAN_IE_RF0FL = 0x00000004
REG_BITS_MCAN_IE_RF0WL = 0x00000002
REG_BITS_MCAN_IE_RF0NL = 0x00000001

# ILE
REG_BITS_MCAN_ILE_EINT1 = 0x00000002
REG_BITS_MCAN_ILE_EINT0 = 0x00000001

# GFC
REG_BITS_MCAN_GFC_ANFS_FIFO0 = 0x00000000
REG_BITS_MCAN_GFC_ANFS_FIFO1 = 0x00000010
REG_BITS_MCAN_GFC_ANFE_FIFO0 = 0x00000000
REG_BITS_MCAN_GFC_ANFE_FIFO1 = 0x00000004
REG_BITS_MCAN_GFC_RRFS = 0x00000002
REG_BITS_MCAN_GFC_RRFE = 0x00000001
REG_BITS_MCAN_GFC_MASK = 0x0000003F

# NDAT1

# NDAT2

# RXF0C
REG_BITS_MCAN_RXF0C_F0OM_OVERWRITE = 0x80000000

# RXESC
REG_BITS_MCAN_RXESC_RBDS_8B = 0x00000000
REG_BITS_MCAN_RXESC_RBDS_12B = 0x00000100
REG_BITS_MCAN_RXESC_RBDS_16B = 0x00000200
REG_BITS_MCAN_RXESC_RBDS_20B = 0x00000300
REG_BITS_MCAN_RXESC_RBDS_24B = 0x00000400
REG_BITS_MCAN_RXESC_RBDS_32B = 0x00000500
REG_BITS_MCAN_RXESC_RBDS_48B = 0x00000600
REG_BITS_MCAN_RXESC_RBDS_64B = 0x00000700
REG_BITS_MCAN_RXESC_F1DS_8B = 0x00000000
REG_BITS_MCAN_RXESC_F1DS_12B = 0x00000010
REG_BITS_MCAN_RXESC_F1DS_16B = 0x00000020
REG_BITS_MCAN_RXESC_F1DS_20B = 0x00000030
REG_BITS_MCAN_RXESC_F1DS_24B = 0x00000040
REG_BITS_MCAN_RXESC_F1DS_32B = 0x00000050
REG_BITS_MCAN_RXESC_F1DS_48B = 0x00000060
REG_BITS_MCAN_RXESC_F1DS_64B = 0x00000070
REG_BITS_MCAN_RXESC_F0DS_8B = 0x00000000
REG_BITS_MCAN_RXESC_F0DS_12B = 0x00000001
REG_BITS_MCAN_RXESC_F0DS_16B = 0x00000002
REG_BITS_MCAN_RXESC_F0DS_20B = 0x00000003
REG_BITS_MCAN_RXESC_F0DS_24B = 0x00000004
REG_BITS_MCAN_RXESC_F0DS_32B = 0x00000005
REG_BITS_MCAN_RXESC_F0DS_48B = 0x00000006
REG_BITS_MCAN_RXESC_F0DS_64B = 0x00000007

# TXBC
REG_BITS_MCAN_TXBC_TFQM = 0x40000000

# TXESC
REG_BITS_MCAN_TXESC_TBDS_8 = 0x00000000
REG_BITS_MCAN_TXESC_TBDS_12 = 0x00000001
REG_BITS_MCAN_TXESC_TBDS_16 = 0x00000002
REG_BITS_MCAN_TXESC_TBDS_20 = 0x00000003
REG_BITS_MCAN_TXESC_TBDS_24 = 0x00000004
REG_BITS_MCAN_TXESC_TBDS_32 = 0x00000005
REG_BITS_MCAN_TXESC_TBDS_48 = 0x00000006
REG_BITS_MCAN_TXESC_TBDS_64 = 0x00000007

# TSCC
REG_BITS_MCAN_TSCC_PRESCALER_MASK = 0x000F0000
REG_BITS_MCAN_TSCC_COUNTER_ALWAYS_0 = 0x00000000
REG_BITS_MCAN_TSCC_COUNTER_USE_TCP = 0x00000001
REG_BITS_MCAN_TSCC_COUNTER_EXTERNAL = 0x00000002

# TXBAR
REG_BITS_MCAN_TXBAR_AR31 = 0x80000000
REG_BITS_MCAN_TXBAR_AR30 = 0x40000000
REG_BITS_MCAN_TXBAR_AR29 = 0x20000000
REG_BITS_MCAN_TXBAR_AR28 = 0x10000000
REG_BITS_MCAN_TXBAR_AR27 = 0x08000000
REG_BITS_MCAN_TXBAR_AR26 = 0x04000000
REG_BITS_MCAN_TXBAR_AR25 = 0x02000000
REG_BITS_MCAN_TXBAR_AR24 = 0x01000000
REG_BITS_MCAN_TXBAR_AR23 = 0x00800000
REG_BITS_MCAN_TXBAR_AR22 = 0x00400000
REG_BITS_MCAN_TXBAR_AR21 = 0x00200000
REG_BITS_MCAN_TXBAR_AR20 = 0x00100000
REG_BITS_MCAN_TXBAR_AR19 = 0x00080000
REG_BITS_MCAN_TXBAR_AR18 = 0x00040000
REG_BITS_MCAN_TXBAR_AR17 = 0x00020000
REG_BITS_MCAN_TXBAR_AR16 = 0x00010000
REG_BITS_MCAN_TXBAR_AR15 = 0x00008000
REG_BITS_MCAN_TXBAR_AR14 = 0x00004000
REG_BITS_MCAN_TXBAR_AR13 = 0x00002000
REG_BITS_MCAN_TXBAR_AR12 = 0x00001000
REG_BITS_MCAN_TXBAR_AR11 = 0x00000800
REG_BITS_MCAN_TXBAR_AR10 = 0x00000400
REG_BITS_MCAN_TXBAR_AR9 = 0x00000200
REG_BITS_MCAN_TXBAR_AR8 = 0x00000100
REG_BITS_MCAN_TXBAR_AR7 = 0x00000080
REG_BITS_MCAN_TXBAR_AR6 = 0x00000040
REG_BITS_MCAN_TXBAR_AR5 = 0x00000020
REG_BITS_MCAN_TXBAR_AR4 = 0x00000010
REG_BITS_MCAN_TXBAR_AR3 = 0x00000008
REG_BITS_MCAN_TXBAR_AR2 = 0x00000004
REG_BITS_MCAN_TXBAR_AR1 = 0x00000002
REG_BITS_MCAN_TXBAR_AR0 = 0x00000001

# TXBCR
REG_BITS_MCAN_TXBCR_CR31 = 0x80000000
REG_BITS_MCAN_TXBCR_CR30 = 0x40000000
REG_BITS_MCAN_TXBCR_CR29 = 0x20000000
REG_BITS_MCAN_TXBCR_CR28 = 0x10000000
REG_BITS_MCAN_TXBCR_CR27 = 0x08000000
REG_BITS_MCAN_TXBCR_CR26 = 0x04000000
REG_BITS_MCAN_TXBCR_CR25 = 0x02000000
REG_BITS_MCAN_TXBCR_CR24 = 0x01000000
REG_BITS_MCAN_TXBCR_CR23 = 0x00800000
REG_BITS_MCAN_TXBCR_CR22 = 0x00400000
REG_BITS_MCAN_TXBCR_CR21 = 0x00200000
REG_BITS_MCAN_TXBCR_CR20 = 0x00100000
REG_BITS_MCAN_TXBCR_CR19 = 0x00080000
REG_BITS_MCAN_TXBCR_CR18 = 0x00040000
REG_BITS_MCAN_TXBCR_CR17 = 0x00020000
REG_BITS_MCAN_TXBCR_CR16 = 0x00010000
REG_BITS_MCAN_TXBCR_CR15 = 0x00008000
REG_BITS_MCAN_TXBCR_CR14 = 0x00004000
REG_BITS_MCAN_TXBCR_CR13 = 0x00002000
REG_BITS_MCAN_TXBCR_CR12 = 0x00001000
REG_BITS_MCAN_TXBCR_CR11 = 0x00000800
REG_BITS_MCAN_TXBCR_CR10 = 0x00000400
REG_BITS_MCAN_TXBCR_CR9 = 0x00000200
REG_BITS_MCAN_TXBCR_CR8 = 0x00000100
REG_BITS_MCAN_TXBCR_CR7 = 0x00000080
REG_BITS_MCAN_TXBCR_CR6 = 0x00000040
REG_BITS_MCAN_TXBCR_CR5 = 0x00000020
REG_BITS_MCAN_TXBCR_CR4 = 0x00000010
REG_BITS_MCAN_TXBCR_CR3 = 0x00000008
REG_BITS_MCAN_TXBCR_CR2 = 0x00000004
REG_BITS_MCAN_TXBCR_CR1 = 0x00000002
REG_BITS_MCAN_TXBCR_CR0 = 0x00000001

# TXBTIE
REG_BITS_MCAN_TXBTIE_TIE31 = 0x80000000
REG_BITS_MCAN_TXBTIE_TIE30 = 0x40000000
REG_BITS_MCAN_TXBTIE_TIE29 = 0x20000000
REG_BITS_MCAN_TXBTIE_TIE28 = 0x10000000
REG_BITS_MCAN_TXBTIE_TIE27 = 0x08000000
REG_BITS_MCAN_TXBTIE_TIE26 = 0x04000000
REG_BITS_MCAN_TXBTIE_TIE25 = 0x02000000
REG_BITS_MCAN_TXBTIE_TIE24 = 0x01000000
REG_BITS_MCAN_TXBTIE_TIE23 = 0x00800000
REG_BITS_MCAN_TXBTIE_TIE22 = 0x00400000
REG_BITS_MCAN_TXBTIE_TIE21 = 0x00200000
REG_BITS_MCAN_TXBTIE_TIE20 = 0x00100000
REG_BITS_MCAN_TXBTIE_TIE19 = 0x00080000
REG_BITS_MCAN_TXBTIE_TIE18 = 0x00040000
REG_BITS_MCAN_TXBTIE_TIE17 = 0x00020000
REG_BITS_MCAN_TXBTIE_TIE16 = 0x00010000
REG_BITS_MCAN_TXBTIE_TIE15 = 0x00008000
REG_BITS_MCAN_TXBTIE_TIE14 = 0x00004000
REG_BITS_MCAN_TXBTIE_TIE13 = 0x00002000
REG_BITS_MCAN_TXBTIE_TIE12 = 0x00001000
REG_BITS_MCAN_TXBTIE_TIE11 = 0x00000800
REG_BITS_MCAN_TXBTIE_TIE10 = 0x00000400
REG_BITS_MCAN_TXBTIE_TIE9 = 0x00000200
REG_BITS_MCAN_TXBTIE_TIE8 = 0x00000100
REG_BITS_MCAN_TXBTIE_TIE7 = 0x00000080
REG_BITS_MCAN_TXBTIE_TIE6 = 0x00000040
REG_BITS_MCAN_TXBTIE_TIE5 = 0x00000020
REG_BITS_MCAN_TXBTIE_TIE4 = 0x00000010
REG_BITS_MCAN_TXBTIE_TIE3 = 0x00000008
REG_BITS_MCAN_TXBTIE_TIE2 = 0x00000004
REG_BITS_MCAN_TXBTIE_TIE1 = 0x00000002
REG_BITS_MCAN_TXBTIE_TIE0 = 0x00000001

# TXBCIE
REG_BITS_MCAN_TXBCIE_CFIE31 = 0x80000000
REG_BITS_MCAN_TXBCIE_CFIE30 = 0x40000000
REG_BITS_MCAN_TXBCIE_CFIE29 = 0x20000000
REG_BITS_MCAN_TXBCIE_CFIE28 = 0x10000000
REG_BITS_MCAN_TXBCIE_CFIE27 = 0x08000000
REG_BITS_MCAN_TXBCIE_CFIE26 = 0x04000000
REG_BITS_MCAN_TXBCIE_CFIE25 = 0x02000000
REG_BITS_MCAN_TXBCIE_CFIE24 = 0x01000000
REG_BITS_MCAN_TXBCIE_CFIE23 = 0x00800000
REG_BITS_MCAN_TXBCIE_CFIE22 = 0x00400000
REG_BITS_MCAN_TXBCIE_CFIE21 = 0x00200000
REG_BITS_MCAN_TXBCIE_CFIE20 = 0x00100000
REG_BITS_MCAN_TXBCIE_CFIE19 = 0x00080000
REG_BITS_MCAN_TXBCIE_CFIE18 = 0x00040000
REG_BITS_MCAN_TXBCIE_CFIE17 = 0x00020000
REG_BITS_MCAN_TXBCIE_CFIE16 = 0x00010000
REG_BITS_MCAN_TXBCIE_CFIE15 = 0x00008000
REG_BITS_MCAN_TXBCIE_CFIE14 = 0x00004000
REG_BITS_MCAN_TXBCIE_CFIE13 = 0x00002000
REG_BITS_MCAN_TXBCIE_CFIE12 = 0x00001000
REG_BITS_MCAN_TXBCIE_CFIE11 = 0x00000800
REG_BITS_MCAN_TXBCIE_CFIE10 = 0x00000400
REG_BITS_MCAN_TXBCIE_CFIE9 = 0x00000200
REG_BITS_MCAN_TXBCIE_CFIE8 = 0x00000100
REG_BITS_MCAN_TXBCIE_CFIE7 = 0x00000080
REG_BITS_MCAN_TXBCIE_CFIE6 = 0x00000040
REG_BITS_MCAN_TXBCIE_CFIE5 = 0x00000020
REG_BITS_MCAN_TXBCIE_CFIE4 = 0x00000010
REG_BITS_MCAN_TXBCIE_CFIE3 = 0x00000008
REG_BITS_MCAN_TXBCIE_CFIE2 = 0x00000004
REG_BITS_MCAN_TXBCIE_CFIE1 = 0x00000002
REG_BITS_MCAN_TXBCIE_CFIE0 = 0x00000001
# *****************************************************************************

# *****************************************************************************
# Device Register Bit Field Defines
# *****************************************************************************

# Modes of Operation and Pin Configuration Registers (0x0800)
# Generic masks
REG_BITS_DEVICE_MODE_FORCED_SET_BITS = 0x00000020

# Wake pin
REG_BITS_DEVICE_MODE_WAKE_PIN_MASK = 0xC0000000
REG_BITS_DEVICE_MODE_WAKE_PIN_DIS = 0x00000000
REG_BITS_DEVICE_MODE_WAKE_PIN_RISING = 0x40000000
REG_BITS_DEVICE_MODE_WAKE_PIN_FALLING = 0x80000000
REG_BITS_DEVICE_MODE_WAKE_PIN_BOTHEDGES = 0xC0000000

# WD_Timer (If applicable)
REG_BITS_DEVICE_MODE_WD_TIMER_MASK = 0x30000000
REG_BITS_DEVICE_MODE_WD_TIMER_60MS = 0x00000000
REG_BITS_DEVICE_MODE_WD_TIMER_600MS = 0x10000000
REG_BITS_DEVICE_MODE_WD_TIMER_3S = 0x20000000
REG_BITS_DEVICE_MODE_WD_TIMER_6S = 0x30000000

# WD_TIMER_CLK_REF
REG_BITS_DEVICE_MODE_WD_CLK_MASK = 0x08000000
REG_BITS_DEVICE_MODE_WD_CLK_20MHZ = 0x00000000
REG_BITS_DEVICE_MODE_WD_CLK_40MHZ = 0x08000000

# GPO2 Pin Configuration
REG_BITS_DEVICE_MODE_GPO2_MASK = 0x00C00000
REG_BITS_DEVICE_MODE_GPO2_CAN_FAULT = 0x00000000
REG_BITS_DEVICE_MODE_GPO2_MCAN_INT0 = 0x00400000
REG_BITS_DEVICE_MODE_GPO2_WDT = 0x00800000
REG_BITS_DEVICE_MODE_GPO2_NINT = 0x00C00000

# Test Mode Enable Bit
REG_BITS_DEVICE_MODE_TESTMODE_ENMASK = 0x00200000
REG_BITS_DEVICE_MODE_TESTMODE_EN = 0x00200000
REG_BITS_DEVICE_MODE_TESTMODE_DIS = 0x00000000

# nWKRQ Pin GPO Voltage Rail Configuration
REG_BITS_DEVICE_MODE_NWKRQ_VOLT_MASK = 0x00080000
REG_BITS_DEVICE_MODE_NWKRQ_VOLT_INTERNAL = 0x00000000
REG_BITS_DEVICE_MODE_NWKRQ_VOLT_VIO = 0x00080000

# WD_BIT
REG_BITS_DEVICE_MODE_WDT_RESET_BIT = 0x00040000

# WD_ACTION
REG_BITS_DEVICE_MODE_WDT_ACTION_MASK = 0x00020000
REG_BITS_DEVICE_MODE_WDT_ACTION_INT = 0x00000000
REG_BITS_DEVICE_MODE_WDT_ACTION_INH_PULSE = 0x00010000
REG_BITS_DEVICE_MODE_WDT_ACTION_WDT_PULSE = 0x00020000

# CLKOUT/GPO1 Pin Mode Select
REG_BITS_DEVICE_MODE_GPO1_MODE_MASK = 0x0000C000
REG_BITS_DEVICE_MODE_GPO1_MODE_GPO = 0x00000000
REG_BITS_DEVICE_MODE_GPO1_MODE_CLKOUT = 0x00004000
REG_BITS_DEVICE_MODE_GPO1_MODE_GPI = 0x00008000

# Fail Safe Enable
REG_BITS_DEVICE_MODE_FAIL_SAFE_MASK = 0x00002000
REG_BITS_DEVICE_MODE_FAIL_SAFE_EN = 0x00002000
REG_BITS_DEVICE_MODE_FAIL_SAFE_DIS = 0x00000000

# CLKOUT Prescaler
REG_BITS_DEVICE_MODE_CLKOUT_MASK = 0x00001000
REG_BITS_DEVICE_MODE_CLKOUT_DIV1 = 0x00000000
REG_BITS_DEVICE_MODE_CLKOUT_DIV2 = 0x00001000

# GPO1 Function Select
REG_BITS_DEVICE_MODE_GPO1_FUNC_MASK = 0x00000C00
REG_BITS_DEVICE_MODE_GPO1_FUNC_SPI_INT = 0x00000000
REG_BITS_DEVICE_MODE_GPO1_FUNC_MCAN_INT1 = 0x00000400
REG_BITS_DEVICE_MODE_GPO1_FUNC_UVLO_THERM = 0x00000800

# INH Pin Disable
REG_BITS_DEVICE_MODE_INH_MASK = 0x00000200
REG_BITS_DEVICE_MODE_INH_DIS = 0x00000200
REG_BITS_DEVICE_MODE_INH_EN = 0x00000000

# nWKRQ Pin Configuration
REG_BITS_DEVICE_MODE_NWKRQ_CONFIG_MASK = 0x00000100
REG_BITS_DEVICE_MODE_NWKRQ_CONFIG_INH = 0x00000000
REG_BITS_DEVICE_MODE_NWKRQ_CONFIG_WKRQ = 0x00000100

# Mode of Operation
REG_BITS_DEVICE_MODE_DEVICEMODE_MASK = 0x000000C0
REG_BITS_DEVICE_MODE_DEVICEMODE_SLEEP = 0x00000000
REG_BITS_DEVICE_MODE_DEVICEMODE_STANDBY = 0x00000040
REG_BITS_DEVICE_MODE_DEVICEMODE_NORMAL = 0x00000080

# WDT_EN
REG_BITS_DEVICE_MODE_WDT_MASK = 0x00000008
REG_BITS_DEVICE_MODE_WDT_EN = 0x00000008
REG_BITS_DEVICE_MODE_WDT_DIS = 0x00000000

# Dev Reset
REG_BITS_DEVICE_MODE_DEVICE_RESET = 0x00000004

# SWE_DIS: Sleep Wake Error Disable
REG_BITS_DEVICE_MODE_SWE_MASK = 0x00000002
REG_BITS_DEVICE_MODE_SWE_DIS = 0x00000002
REG_BITS_DEVICE_MODE_SWE_EN = 0x00000000

# Test Mode Configuration
REG_BITS_DEVICE_MODE_TESTMODE_MASK = 0x00000001
REG_BITS_DEVICE_MODE_TESTMODE_PHY = 0x00000000
REG_BITS_DEVICE_MODE_TESTMODE_CONTROLLER = 0x00000001

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Device Interrupt Register values (0x0820)
REG_BITS_DEVICE_IR_CANLGND = 0x08000000
REG_BITS_DEVICE_IR_CANBUSOPEN = 0x04000000
REG_BITS_DEVICE_IR_CANBUSGND = 0x02000000
REG_BITS_DEVICE_IR_CANBUSBAT = 0x01000000
# Reserved											0x00800000
REG_BITS_DEVICE_IR_UVSUP = 0x00400000
REG_BITS_DEVICE_IR_UVIO = 0x00200000
REG_BITS_DEVICE_IR_PWRON = 0x00100000
REG_BITS_DEVICE_IR_TSD = 0x00080000
REG_BITS_DEVICE_IR_WDTO = 0x00040000
# Reserved											0x00020000
REG_BITS_DEVICE_IR_ECCERR = 0x00010000
REG_BITS_DEVICE_IR_CANINT = 0x00008000
REG_BITS_DEVICE_IR_LWU = 0x00004000
REG_BITS_DEVICE_IR_WKERR = 0x00002000
REG_BITS_DEVICE_IR_FRAME_OVF = 0x00001000
# Reserved											0x00000800
REG_BITS_DEVICE_IR_CANSLNT = 0x00000400
# Reserved											0x00000200
REG_BITS_DEVICE_IR_CANDOM = 0x00000100
REG_BITS_DEVICE_IR_GLOBALERR = 0x00000080
REG_BITS_DEVICE_IR_nWKRQ = 0x00000040
REG_BITS_DEVICE_IR_CANERR = 0x00000020
REG_BITS_DEVICE_IR_CANBUSFAULT = 0x00000010
REG_BITS_DEVICE_IR_SPIERR = 0x00000008
REG_BITS_DEVICE_IR_SWERR = 0x00000004
REG_BITS_DEVICE_IR_M_CAN_INT = 0x00000002
REG_BITS_DEVICE_IR_VTWD = 0x00000001

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Device Interrupt Enable Values (0x0830)
REG_BITS_DEVICE_IE_UVCCOUT = 0x00800000
REG_BITS_DEVICE_IE_UVSUP = 0x00400000
REG_BITS_DEVICE_IE_UVIO = 0x00200000
REG_BITS_DEVICE_IE_PWRON = 0x00100000
REG_BITS_DEVICE_IE_TSD = 0x00080000
REG_BITS_DEVICE_IE_WDTO = 0x00040000
# Reserved
REG_BITS_DEVICE_IE_ECCERR = 0x00010000
REG_BITS_DEVICE_IE_CANINT = 0x00008000
REG_BITS_DEVICE_IE_LWU = 0x00004000
REG_BITS_DEVICE_IE_WKERR = 0x00002000
REG_BITS_DEVICE_IE_FRAME_OVF = 0x00001000
# Reserved											0x00000800
REG_BITS_DEVICE_IE_CANSLNT = 0x00000400
# Reserved											0x00000200
REG_BITS_DEVICE_IE_CANDOM = 0x00000100
# Reserved											0x80-00
REG_BITS_DEVICE_IE_MASK = 0x7F69D700  # ! This mask is the bitwise-inverse of the 0x0830 IE register's reserved bits. A reserved bit is read as high always. This masks the reserved bits out.


class TCAN4x5x_Device_Mode_Enum:
    (TCAN4x5x_DEVICE_MODE_NORMAL, TCAN4x5x_DEVICE_MODE_STANDBY, TCAN4x5x_DEVICE_MODE_SLEEP) = map(uint8_t, range(3))


class TCAN4x5x_DEV_CONFIG_GPO1_CONFIG:
    (TCAN4x5x_DEV_CONFIG_GPO1_SPI_FAULT_INT,
     TCAN4x5x_DEV_CONFIG_GPO1_MCAN_INT1,
     TCAN4x5x_DEV_CONFIG_GPO1_UNDER_VOLTAGE_OR_THERMAL_INT) = map(uint8_t, range(3))


class TCAN4x5x_DEV_CONFIG_WDT_ACTION:
    (TCAN4x5x_DEV_CONFIG_WDT_ACTION_nINT,
     TCAN4x5x_DEV_CONFIG_WDT_ACTION_PULSE_INH,
     TCAN4x5x_DEV_CONFIG_WDT_ACTION_PULSE_WDT_OUTPUT) = map(uint8_t, range(3))


class TCAN4x5x_DEV_CONFIG_GPIO1_CONFIG:
    (TCAN4x5x_DEV_CONFIG_GPIO1_CONFIG_GPO,
     reserved,
     TCAN4x5x_DEV_CONFIG_GPIO1_CONFIG_WATCHDOG_INPUT) = map(uint8_t, range(3))


class TCAN4x5x_DEV_CONFIG_GPO2_CONFIG:
    (TCAN4x5x_DEV_CONFIG_GPO2_NO_ACTION,
     TCAN4x5x_DEV_CONFIG_GPO2_MCAN_INT0,
     TCAN4x5x_DEV_CONFIG_GPO2_WATCHDOG,
     TCAN4x5x_DEV_CONFIG_GPO2_MIRROR_INT) = map(uint8_t, range(4))


class TCAN4x5x_DEV_CONFIG_WAKE_CONFIG:
    (TCAN4x5x_DEV_CONFIG_WAKE_DISABLED,
     TCAN4x5x_DEV_CONFIG_WAKE_RISING_EDGE,
     TCAN4x5x_DEV_CONFIG_WAKE_FALLING_EDGE,
     TCAN4x5x_DEV_CONFIG_WAKE_BOTH_EDGES) = map(uint8_t, range(4))


class TCAN4x5x_GFC_NO_MATCH_BEHAVIOR:  # No Comments provided in original file
    (TCAN4x5x_GFC_ACCEPT_INTO_RXFIFO0,
     TCAN4x5x_GFC_ACCEPT_INTO_RXFIFO1,
     TCAN4x5x_GFC_REJECT) = map(uint8_t, range(3))


class TCAN4x5x_XID_EFT_Values:
    (  # Range filter from EFID1 to EFID2
        TCAN4x5x_XID_EFT_RANGE,

        # Dual ID filter matches if the incoming ID matches EFID1 or EFID2
        TCAN4x5x_XID_EFT_DUALID,

        # Classic Filter, EFID1 is the ID/filter, and EFID2 is the mask
        TCAN4x5x_XID_EFT_CLASSIC,

        # Range filter from EFID1 to EFID2, The XIDAM mask is not applied
        TCAN4x5x_XID_EFT_RANGENOMASK) = map(uint8_t, range(4))


class TCAN4x5x_XID_EFEC_Values:
    (  # Disabled filter. This filter will do nothing if it matches a packet
        TCAN4x5x_XID_EFEC_DISABLED,

        # Store in RX FIFO 0 if the filter matches the incoming message
        TCAN4x5x_XID_EFEC_STORERX0,

        # Store in RX FIFO 1 if the filter matches the incoming message
        TCAN4x5x_XID_EFEC_STORERX1,

        # Reject the packet (do not store, do not notify MCU) if the filter matches the incoming message
        TCAN4x5x_XID_EFEC_REJECTMATCH,

        # Store in default location but set a high priority message interrupt if the filter matches the incoming message
        TCAN4x5x_XID_EFEC_PRIORITY,

        # Store in RX FIFO 0 and set a high priority message interrupt if the filter matches the incoming message
        TCAN4x5x_XID_EFEC_PRIORITYSTORERX0,

        # Store in RX FIFO 1 and set a high priority message interrupt if the filter matches the incoming message
        TCAN4x5x_XID_EFEC_PRIORITYSTORERX1,

        # Store in RX Buffer for debug if the filter matches the incoming message.
        TCAN4x5x_XID_EFEC_STORERXBUFORDEBUG) = map(uint8_t, range(8))


class TCAN4x5x_MRAM_Element_Data_Size:
    (  # 8 bytes of data payload
        MRAM_8_Byte_Data,

        # 12 bytes of data payload
        MRAM_12_Byte_Data,

        # 16 bytes of data payload
        MRAM_16_Byte_Data,

        # 20 bytes of data payload
        MRAM_20_Byte_Data,

        # 24 bytes of data payload
        MRAM_24_Byte_Data,

        # 32 bytes of data payload
        MRAM_32_Byte_Data,

        # 48 bytes of data payload
        MRAM_48_Byte_Data,

        # 64 bytes of data payload
        MRAM_64_Byte_Data) = map(uint8_t, range(8))


class TCAN4x5x_SID_SFEC_Values:
    (  # Disabled filter. This filter will do nothing if it matches a packet
        TCAN4x5x_SID_SFEC_DISABLED,

        # Store in RX FIFO 0 if the filter matches the incoming message
        TCAN4x5x_SID_SFEC_STORERX0,

        # Store in RX FIFO 1 if the filter matches the incoming message
        TCAN4x5x_SID_SFEC_STORERX1,

        # Reject the packet (do not store, do not notify MCU) if the filter matches the incoming message
        TCAN4x5x_SID_SFEC_REJECTMATCH,

        # Store in default location but set a high priority message interrupt if the filter matches the incoming message
        TCAN4x5x_SID_SFEC_PRIORITY,

        # Store in RX FIFO 0 and set a high priority message interrupt if the filter matches the incoming message
        TCAN4x5x_SID_SFEC_PRIORITYSTORERX0,

        # Store in RX FIFO 1 and set a high priority message interrupt if the filter matches the incoming message
        TCAN4x5x_SID_SFEC_PRIORITYSTORERX1,

        # Store in RX Buffer for debug if the filter matches the incoming message. SFT is ignored if this is selected.
        TCAN4x5x_SID_SFEC_STORERXBUFORDEBUG) = map(uint8_t, range(7))


class TCAN4x5x_SID_SFT_Values:
    (  # Range Filter. SFID1 holds the start address, and SFID2 holds the end address. Any address in between will match
        TCAN4x5x_SID_SFT_RANGE,

        # Dual ID filter, where both SFID1 and SFID2 hold IDs that can match (must match exactly)
        TCAN4x5x_SID_SFT_DUALID,

        # Classic filter with SFID1 as the ID to match, and SFID2 as the bit mask that applies to SFID1
        TCAN4x5x_SID_SFT_CLASSIC,

        # Disabled filter. This filter will match nothing
        TCAN4x5x_SID_SFT_DISABLED) = map(uint8_t, range(4))


# END ENUMS
#
# Structs
#
class TCAN4x5x_MCAN_SID_Filter_bits(ctypes.Structure):
    _fields_ = [
        # @brief SFID2[10:0]
        ("SFID2", uint16_t, 11),

        # @brief Reserved
        ("reserved", uint8_t, 5),

        # @brief SFID1[10:0]
        ("SFID1", uint16_t, 11),

        # @brief SFEC[2:0]   Standard filter element configuration
        ("SFEC", TCAN4x5x_SID_SFEC_Values, 3),

        # @brief SFT Standard Filter Type
        ("SFT", TCAN4x5x_SID_SFT_Values, 2)
    ]


class TCAN4x5x_MCAN_SID_Filter(ctypes.Union):
    _fields_ = [("b", TCAN4x5x_MCAN_SID_Filter_bits),
                ("word", uint32_t)]


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

        # IE[18] TOOE: Time out occurred
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
        ("CANHCANL", uint8_t, 1),

        # DEV_IR[30] : CANBUSTERMOPEN, CAN Bus has termination point open
        ("CANBUSTERMOPEN", uint8_t, 1),

        # DEV_IR[31] : CANBUSNORM, CAN Bus is normal flag
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
        ("RRFE", uint8_t, 1),

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


# @brief Extended ID filter struct
class TCAN4x5x_MCAN_XID_Filter(ctypes.Structure):
    _fields_ = [
        # @brief EFID2[28:0]
        ("EFID2", uint32_t, 29),

        # @brief Reserved
        ("reserved", uint8_t, 1),

        # @brief EFT[1:0]
        ("EFT", TCAN4x5x_XID_EFT_Values, 2),

        # EFID1[28:0]
        ("EFID1", uint32_t, 29),

        # @brief SFT Standard Filter Type
        ("EFEC", TCAN4x5x_XID_EFEC_Values, 3)
    ]


class TCAN4x5x_DEV_CONFIG_bits(ctypes.Structure):
    _fields_ = [
        # @brief DEV_MODE_PINS[0] : Test mode configuration. Reserved in this struct
        # It is recommended to use the test mode function to enable or disable test mode rather than this struct
        ("RESERVED0", uint8_t, 1),

        # @brief DEV_MODE_PINS[1] : Sleep wake error disable.
        # Setting this to 1 will disable the 4 minute timer that puts the part back to sleep if no activity is detected
        ("SWE_DIS", uint8_t, 1),

        # @brief DEV_MODE_PINS[2] : Device reset. Write a 1 to perform a reset on the part
        ("DEVICE_RESET", uint8_t, 1),

        # @brief DEV_MODE_PINS[3] : Watchdog Enable. Use the watchdog functions to control enabling the watchdog
        ("WD_EN", uint8_t, 1),

        # @brief Reserved
        # @brief DEV_MODE_PINS[7:6] : Mode Selection. Use the mode functions to change the mode
        ("RESERVED1", uint8_t, 4),

        # @brief DEV_MODE_PINS[8] : nWKRQ Configuration
        # 0: Mirrors INH function
        # 1: Wake request interrupt
        ("nWKRQ_CONFIG", uint8_t, 1),

        # @brief DEV_MODE_PINS[9] : Inhibit pin disable
        ("INH_DIS", uint8_t, 1),

        # @brief DEV_MODE_PINS[11:10] : GPIO1 pin as a GPO function configuration
        # Configures the behavior of GPIO1 if it is configured to be a GPO
        # Available values are:
        # TCAN4x5x_DEV_CONFIG_GPO1_SPI_FAULT_INT : Active low output for a SPIERR
        # TCAN4x5x_DEV_CONFIG_GPO1_MCAN_INT1 : Active low output for MCAN_INT1 output (See MCAN ILE and ILS registers to use)
        # TCAN4x5x_DEV_CONFIG_GPO1_UNDER_VOLTAGE_OR_THERMAL_INT : Active low output for any under voltage or over temp interrupt
        ("GPIO1_GPO_CONFIG", TCAN4x5x_DEV_CONFIG_GPO1_CONFIG, 2),

        # @brief Reserved
        ("RESERVED2", uint8_t, 1),

        # @brief DEV_MODE_PINS[13] : Fail safe mode enable. Excludes power up fail safe
        ("FAIL_SAFE_EN", uint8_t, 1),

        # @brief DEV_MODE_PINS[15:14] : GPIO1 configuration
        # Configures the mode of the GPIO1 pin as an input or output
        # Available values are:
        # TCAN4x5x_DEV_CONFIG_GPIO1_CONFIG_GPO : Sets GPIO1 as an output. Be sure to see GPIO1_GPO_CONFIG field to set the behavior
        # TCAN4x5x_DEV_CONFIG_GPIO1_CONFIG_WATCHDOG_INPUT : Sets GPIO1 as an input for the watchdog timer. Watchdog will need to be enabled
        ("GPIO1_CONFIG", TCAN4x5x_DEV_CONFIG_GPIO1_CONFIG, 2),

        # @brief DEV_MODE_PINS[17:16] : Watchdog action. Defines the behavior of the watchdog timer when it times out
        # Sets the behavior of the watchdog when it times out
        # Available values are:
        # TCAN4x5x_DEV_CONFIG_WDT_ACTION_nINT : Sets an interrupt flag and the interrupt pin will be pulled low
        # TCAN4x5x_DEV_CONFIG_WDT_ACTION_PULSE_INH : Pulse INH low for ~300 ms then high
        # TCAN4x5x_DEV_CONFIG_WDT_ACTION_PULSE_WDT_OUTPUT : Pulse the watchdog output pin low for ~300 ms and high
        ("WD_ACTION", TCAN4x5x_DEV_CONFIG_WDT_ACTION, 2),

        # @brief DEV_MODE_PINS[18] : Watchdog reset bit
        # Write a 1 to reset the watchdog timer. It's recommended to use the other watchdog functions for this behavior
        ("WD_BIT_RESET", uint8_t, 1),

        # @brief DEV_MODE_PINS[19] : nWKRQ_VOLTAGE, set the voltage rail used by the nWKRQ pin
        # Available values are:
        # 0 [default] : Internal Voltage rail
        # 1           : VIO Voltage rail
        ("nWKRQ_VOLTAGE", uint8_t, 1),

        # @brief DEV_MODE_PINS[21:20] : RESERVED. Use test mode functions to enable test modes
        ("RESERVED3", uint8_t, 2),

        # @brief DEV_MODE_PINS[23:22] : nWKRQ_VOLTAGE, set the voltage rail used by the nWKRQ pin
        # Available values are:
        # TCAN4x5x_DEV_CONFIG_GPO2_NO_ACTION  [default] : No action for GPO2
        # TCAN4x5x_DEV_CONFIG_GPO2_MCAN_INT0 : Used as an output for MCAN INT0
        # TCAN4x5x_DEV_CONFIG_GPO2_WATCHDOG : Used as a watchdog output
        # TCAN4x5x_DEV_CONFIG_GPO2_MIRROR_INT : Mirror nINT pin
        ("GPO2_CONFIG", TCAN4x5x_DEV_CONFIG_GPO2_CONFIG, 2),

        # @brief DEV_MODE_PINS[26:24] : RESERVED
        ("RESERVED4", uint8_t, 3),

        # @brief DEV_MODE_PINS[27] : CLK_REF, used to tell the device what the input clock/crystal frequency is
        # Available values are:
        # 0           : 20 MHz
        # 1 [default] : 40 MHz
        ("CLK_REF", uint8_t, 1),

        # @brief DEV_MODE_PINS[29:28] : RESERVED. Use watchdog functions to set watchdog parameters
        ("RESERVED5", uint8_t, 2),

        # brief DEV_MODE_PINS[31:30] : WAKE_CONFIG, used to configure the direction required to wake a part up
        # Available values are:
        # TCAN4x5x_DEV_CONFIG_WAKE_DISABLED             : Disabled. Wake pin is not used
        # TCAN4x5x_DEV_CONFIG_WAKE_RISING_EDGE          : Low to high transition will wake the part
        # TCAN4x5x_DEV_CONFIG_WAKE_FALLING_EDGE         : High to low transition will wake the part
        # TCAN4x5x_DEV_CONFIG_WAKE_BOTH_EDGES [default] : Either transition will wake the part
        ("WAKE_CONFIG", TCAN4x5x_DEV_CONFIG_WAKE_CONFIG, 2)
    ]


class TCAN4x5x_DEV_CONFIG(ctypes.Union):
    _fields_ = [("b", TCAN4x5x_DEV_CONFIG_bits),
                ("word", uint32_t)]
