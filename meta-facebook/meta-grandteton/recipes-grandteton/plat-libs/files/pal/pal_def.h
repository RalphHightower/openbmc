#ifndef __PAL_DEF_COMMON_H__
#define __PAL_DEF_COMMON_H__
#include <openbmc/misc-utils.h>
#include "pal_def_cover.h"

#define MAX_PATH_LEN           (128)
#define MAX_TXBUF_SIZE         (255)
#define MAX_RXBUF_SIZE         (255)
#define MAX_I2C_TXBUF_SIZE     (16)
#define MAX_I2C_RXBUF_SIZE     (16)

//GPIO EVENT Common
#define FM_UARTSW_LSB_N          "FM_UARTSW_LSB_N"
#define FM_UARTSW_MSB_N          "FM_UARTSW_MSB_N"
#define FM_POST_CARD_PRES_N      "FM_DEBUG_PORT_PRSNT_N_IN"
#define FM_CPU_CATERR_N          "H_CPU_CATERR_LVC2_R2_N"
#define BIOS_TPM_PRESENT_IN      "FM_BIOS_TPM_PRSNT_IN"
#define BIOS_TPM_PRESENT_OUT     "FM_BIOS_TPM_PRSNT_OUT"
#define IRQ_BIOS_TPM_SPI_IN      "IRQ_PCH_TPM_SPI_IN"
#define IRQ_BIOS_TPM_SPI_OUT     "IRQ_BIOS_TPM_SPI_OUT"

//GPIO Power Control Common
#define FP_RST_BTN_IN_N          "ID_RST_BTN_BMC_IN"
#define FP_PWR_BTN_IN_N          "SYS_BMC_PWRBTN_IN"
#define FP_PWR_BTN_OUT_N         "SYS_BMC_PWRBTN_OUT"
#define FP_RST_BTN_OUT_N         "RST_BMC_RSTBTN_OUT_R_N"

//GPIO SWB
#define BIC_READY                "FM_SWB_BIC_READY_ISO_R_N"

//GPIO HGX
#define HMC_PRESENCE             "GPU_HMC_PRSNT_ISO_R_N"
#define HMC_READY                "GPU_BASE_HMC_READY_ISO_R"
#define GPU_FPGA_READY           "GPU_FPGA_READY_ISO_R"
#define GPU_FPGA_RST_N           "GPU_FPGA_RST_N"

// GPIO FAN_BP PRSNT
#define FAN_BP1_PRSNT      "FAN_BP1_PRSNT_N"
#define FAN_BP2_PRSNT      "FAN_BP2_PRSNT_N"

// GPIO HPDB PRSNT
#define HPDB_PRSNT         "HPDB_PRESENT"

//GPIO FAN PRSNT
#define  FAN0_PRSNT        "FAN0_PRESENT"
#define  FAN1_PRSNT        "FAN1_PRESENT"
#define  FAN2_PRSNT        "FAN2_PRESENT"
#define  FAN3_PRSNT        "FAN3_PRESENT"
#define  FAN4_PRSNT        "FAN4_PRESENT"
#define  FAN5_PRSNT        "FAN5_PRESENT"
#define  FAN6_PRSNT        "FAN6_PRESENT"
#define  FAN7_PRSNT        "FAN7_PRESENT"
#define  FAN8_PRSNT        "FAN8_PRESENT"
#define  FAN9_PRSNT        "FAN9_PRESENT"
#define  FAN10_PRSNT       "FAN10_PRESENT"
#define  FAN11_PRSNT       "FAN11_PRESENT"
#define  FAN12_PRSNT       "FAN12_PRESENT"
#define  FAN13_PRSNT       "FAN13_PRESENT"
#define  FAN14_PRSNT       "FAN14_PRESENT"
#define  FAN15_PRSNT       "FAN15_PRESENT"

//GPIO SWB CABLE PRESENT
#define CABLE_PRSNT_G     "SWB_CABLE_PRSNT_G_N"
#define CABLE_PRSNT_F     "SWB_CABLE_PRSNT_F_N"
#define CABLE_PRSNT_C     "SWB_CABLE_PRSNT_C_N"
#define CABLE_PRSNT_B     "SWB_CABLE_PRSNT_B_N"

//GPIO GPU CABLE PRESENT
#define CABLE_PRSNT_A     "GPU_CABLE_PRSNT_A_N"
#define CABLE_PRSNT_D     "GPU_CABLE_PRSNT_D_N"
#define CABLE_PRSNT_E     "GPU_CABLE_PRSNT_E_N"
#define CABLE_PRSNT_H     "GPU_CABLE_PRSNT_H_N"

//GPIO PDB BUSBAR PRESENT
#define FM_HS1_EN_BUSBAR_BUF  "FM_HS1_EN_BUSBAR_BUF"
#define FM_HS2_EN_BUSBAR_BUF  "FM_HS2_EN_BUSBAR_BUF"

#define GPU_FPGA_THERM_OVERT   "GPU_FPGA_THERM_OVERT_ISO_R_N"
#define GPU_FPGA_DEVIC_OVERT   "GPU_FPGA_OVERT_ISO_R_N"

#define CPLD_POWER_FAIL_ALERT  "CPLD_POWER_FAIL_ALERT"

#define FM_SMB_1_ALERT_GPU     "FM_SMB_1_ALERT_GPU_ISO_N"
#define FM_SMB_2_ALERT_GPU     "FM_SMB_2_ALERT_GPU_ISO_N"

//AC POWER BUTTON
#define FP_AC_PWR_BMC_BTN  "AC_PWR_BMC_BTN_N"

#define BMC_DEF_SLAVE_ADDR (0x10)

#define PWR_OPTION_LIST "status, graceful-shutdown, off, on, reset, cycle"

#define FRU_EEPROM "/sys/class/i2c-dev/i2c-%d/device/%d-00%x/eeprom"
#define MAX_NUM_FRUS    (FRU_CNT-1)
#define MAX_NODES       (2)

#define LARGEST_DEVICE_NAME (120)
#define UNIT_DIV            (1000)
#define ERR_NOT_READY       (-2)

#define PAGE_SIZE  0x1000
#define PREPARE_FW_UPDATE_CLEAR (0x00)
#define PREPARE_FW_UPDATE_SET   (0x01)

#define READING_SKIP    (1)
#define READING_NA      (-2)

//NM Device Info
#define NM_IPMB_BUS_ID             (I2C_BUS_6)
#define NM_SLAVE_ADDR              (0x2C)

//SWB Device Info
#define SWB_BIC_EID    (0x0A)
#define SWB_BUS_ID     (3)
#define SWB_UART_ID    (5)

#define MAX_CPU_CNT    (2)

/* Artemis */
// ACB Device Info
#define GTA_BIC_UART_ID 5
#define ACB_BIC_BUS 3
#define ACB_BIC_ADDR 0x20
#define ACB_BIC_EID 0x0A

// MEB Device Info
#define MEB_BIC_BUS 9
#define MEB_BIC_ADDR 0x20
#define MEB_BIC_EID 0x0A

#define ACB_VR_BUS_ID   (1)
#define CXL_VR_BUS_ID   (2)

#define CXL_VR_NUM      (3)

// JCN1,2,3,4,9,10,11,12 can plug CXL or E1.S
// JCN5,6,7,8 plugs E1.S
#define MAX_CXL_NUM 8
#define MAX_DEV_NAME 32
#define MAX_FRU_NAME 32
#define MAX_FRUID_NAME 64
#define MAX_FRUID_PATH_LEN 64

#define GTA_FRUID_DEV_PATH "/tmp/fruid_%s_dev%d.bin"

#define KV_KEY_LAST_POWER_GOOD "last_power_good_sec"

typedef struct {
  uint8_t fru_prsnt;
  uint8_t fru_type;
} fru_status;
/* Artemis End */

#define GPION_COMMON_SOURCE_OFFSET   (0xE0)
#define AST_GPIO_BASE                (0x1e780000)

/*  GTI  */
#define MB_CPLD_BUS               (I2C_BUS_7)
#define MB_CPLD_ADDR              (0x46)

#define SWB_CPLD_BUS              (I2C_BUS_32)
#define SWB_CPLD_ADDR             (0x26)

enum {
  DIMM_ID0 = 0,
  DIMM_ID1,
  DIMM_ID2,
  DIMM_ID3,
  DIMM_ID4,
  DIMM_ID5,
  DIMM_ID6,
  DIMM_ID7,
  DIMM_ID8,
  DIMM_ID9,
  DIMM_ID10,
  DIMM_ID11,
  DIMM_ID12,
  DIMM_ID13,
  DIMM_ID14,
  DIMM_ID15,
  DIMM_ID16,
  DIMM_ID17,
  DIMM_ID18,
  DIMM_ID19,
  DIMM_ID20,
  DIMM_ID21,
  DIMM_ID22,
  DIMM_ID23,
  DIMM_ID24,
  DIMM_ID25,
  DIMM_ID26,
  DIMM_ID27,
  DIMM_ID28,
  DIMM_ID29,
  DIMM_ID30,
  DIMM_ID31,
};

enum {
  DIMM_CPU0_CRPA = 0,
  DIMM_CPU0_CRPB,
  DIMM_CPU0_CRPC,
  DIMM_CPU0_CRPD,
  DIMM_CPU0_CRPE,
  DIMM_CPU0_CRPF,
  DIMM_CPU0_CRPG,
  DIMM_CPU0_CRPH,
  DIMM_CPU1_CRPA,
  DIMM_CPU1_CRPB,
  DIMM_CPU1_CRPC,
  DIMM_CPU1_CRPD,
  DIMM_CPU1_CRPE,
  DIMM_CPU1_CRPF,
  DIMM_CPU1_CRPG,
  DIMM_CPU1_CRPH,
};

enum {
  VR0_COMP,
  VR1_COMP,
  BIC_COMP,
  PEX0_COMP,
  PEX1_COMP,
  PEX2_COMP,
  PEX3_COMP,
  CPLD_COMP,
  NIC0_COMP,
  NIC1_COMP,
  NIC2_COMP,
  NIC3_COMP,
  NIC4_COMP,
  NIC5_COMP,
  NIC6_COMP,
  NIC7_COMP,
  //Artemis Meb CXL
  CXL1_COMP,
  CXL2_COMP,
  CXL3_COMP,
  CXL4_COMP,
  CXL5_COMP,
  CXL6_COMP,
  CXL7_COMP,
  CXL8_COMP,
  CXL1_VR_P089A_COMP,
  CXL1_VR_P0V8D_PVDDQ_AB_COMP,
  CXL1_VR_PVDDQ_CD_COMP,
  CXL2_VR_P089A_COMP,
  CXL2_VR_P0V8D_PVDDQ_AB_COMP,
  CXL2_VR_PVDDQ_CD_COMP,
  CXL3_VR_P089A_COMP,
  CXL3_VR_P0V8D_PVDDQ_AB_COMP,
  CXL3_VR_PVDDQ_CD_COMP,
  CXL4_VR_P089A_COMP,
  CXL4_VR_P0V8D_PVDDQ_AB_COMP,
  CXL4_VR_PVDDQ_CD_COMP,
  CXL5_VR_P089A_COMP,
  CXL5_VR_P0V8D_PVDDQ_AB_COMP,
  CXL5_VR_PVDDQ_CD_COMP,
  CXL6_VR_P089A_COMP,
  CXL6_VR_P0V8D_PVDDQ_AB_COMP,
  CXL6_VR_PVDDQ_CD_COMP,
  CXL7_VR_P089A_COMP,
  CXL7_VR_P0V8D_PVDDQ_AB_COMP,
  CXL7_VR_PVDDQ_CD_COMP,
  CXL8_VR_P089A_COMP,
  CXL8_VR_P0V8D_PVDDQ_AB_COMP,
  CXL8_VR_PVDDQ_CD_COMP,
};

enum DEVICE_COMP {
  DEV_BASE_COMP = 8,
  CB_ACCL1_DEV1_COMP = 8,
  CB_ACCL1_DEV2_COMP,
  CB_ACCL2_DEV1_COMP,
  CB_ACCL2_DEV2_COMP,
  CB_ACCL3_DEV1_COMP,
  CB_ACCL3_DEV2_COMP,
  CB_ACCL4_DEV1_COMP,
  CB_ACCL4_DEV2_COMP,
  CB_ACCL5_DEV1_COMP,
  CB_ACCL5_DEV2_COMP,
  CB_ACCL6_DEV1_COMP,
  CB_ACCL6_DEV2_COMP,
  CB_ACCL7_DEV1_COMP,
  CB_ACCL7_DEV2_COMP,
  CB_ACCL8_DEV1_COMP,
  CB_ACCL8_DEV2_COMP,
  CB_ACCL9_DEV1_COMP,
  CB_ACCL9_DEV2_COMP,
  CB_ACCL10_DEV1_COMP,
  CB_ACCL10_DEV2_COMP,
  CB_ACCL11_DEV1_COMP,
  CB_ACCL11_DEV2_COMP,
  CB_ACCL12_DEV1_COMP,
  CB_ACCL12_DEV2_COMP,
};

enum FW_RESP_LENGTH {
  MEB_CXL_FW_RESP_LEN = 16,
};

enum {
  FRU_ALL = 0,
  FRU_MB,
  FRU_SWB,
  FRU_HGX,
  FRU_NIC0,
  FRU_NIC1,
  FRU_OCPDBG,
  FRU_BMC,
  FRU_SCM,
  FRU_VPDB,
  FRU_HPDB,
  FRU_FAN_BP1,
  FRU_FAN_BP2,
  FRU_FIO,
  FRU_HSC,
  FRU_SHSC,
  // Artemis FRU ID
  FRU_ACB,
  FRU_MEB,
  FRU_ACB_ACCL1,
  FRU_ACB_ACCL2,
  FRU_ACB_ACCL3,
  FRU_ACB_ACCL4,
  FRU_ACB_ACCL5,
  FRU_ACB_ACCL6,
  FRU_ACB_ACCL7,
  FRU_ACB_ACCL8,
  FRU_ACB_ACCL9,
  FRU_ACB_ACCL10,
  FRU_ACB_ACCL11,
  FRU_ACB_ACCL12,
  // Artemis MEB CXL/NIC/E1.S board
  FRU_MEB_JCN1,
  FRU_MEB_JCN2,
  FRU_MEB_JCN3,
  FRU_MEB_JCN4,
  FRU_MEB_JCN5,
  FRU_MEB_JCN6,
  FRU_MEB_JCN7,
  FRU_MEB_JCN8,
  FRU_MEB_JCN9,
  FRU_MEB_JCN10,
  FRU_MEB_JCN11,
  FRU_MEB_JCN12,
  FRU_MEB_JCN13,
  FRU_MEB_JCN14,
  FRU_UBB,
  FRU_HMC,
  FRU_CX7,
  FRU_CNT,
  FRU_AGGREGATE = 0xff,
};

enum FRU_DEV_COUNT {
  FRU_ACB_ACCL_CNT = 12,
  FRU_MEB_JCN_CNT = 14,
};

enum {
  REV_PO = 0,
  REV_EVT,
  REV_DVT,
  REV_PVT,
  REV_MP,
};

enum {
  PDB_REV_PO             = 0,
  PDB_REV_EVT            = 1,
  PDB_REV_EVT2           = 2,
  PDB_REV_DVT            = 3,
  VPDB_DISCRETE_REV_PVT  = 3,
  PDB_REV_DVT2           = 4,
  PDB_REV_PVT            = 5,
  PDB_REV_PVT2           = 6,
  VPDB_DISCRETE_REV_MP   = 6,
};
// Sensors Under Side Plane
enum {
  MB_SENSOR_TBD,
};

enum{
  MEZZ_SENSOR_TBD,
};

enum {
  BOOT_DEVICE_USB      = 0x0,
  BOOT_DEVICE_IPV4     = 0x1,
  BOOT_DEVICE_HDD      = 0x2,
  BOOT_DEVICE_CDROM    = 0x3,
  BOOT_DEVICE_OTHERS   = 0x4,
  BOOT_DEVICE_IPV6     = 0x9,
  BOOT_DEVICE_RESERVED = 0xff,
};

enum {
  IPMI_CHANNEL_0 = 0,
  IPMI_CHANNEL_1,
  IPMI_CHANNEL_2,
  IPMI_CHANNEL_3,
  IPMI_CHANNEL_4,
  IPMI_CHANNEL_5,
  IPMI_CHANNEL_6,
  IPMI_CHANNEL_7,
  IPMI_CHANNEL_8,
  IPMI_CHANNEL_9,
  IPMI_CHANNEL_A,
  IPMI_CHANNEL_B,
  IPMI_CHANNEL_C,
  IPMI_CHANNEL_D,
  IPMI_CHANNEL_E,
  IPMI_CHANNEL_F,
};

enum {
  I2C_BUS_0 = 0,
  I2C_BUS_1,
  I2C_BUS_2,
  I2C_BUS_3,
  I2C_BUS_4,
  I2C_BUS_5,
  I2C_BUS_6,
  I2C_BUS_7,
  I2C_BUS_8,
  I2C_BUS_9,
  I2C_BUS_10,
  I2C_BUS_11,
  I2C_BUS_12,
  I2C_BUS_13,
  I2C_BUS_14,
  I2C_BUS_15,
  I2C_BUS_16,
  I2C_BUS_17,
  I2C_BUS_18,
  I2C_BUS_19,
  I2C_BUS_20,
  I2C_BUS_21,
  I2C_BUS_22,
  I2C_BUS_23,
  I2C_BUS_24,
  I2C_BUS_25,
  I2C_BUS_26,
  I2C_BUS_27,
  I2C_BUS_28,
  I2C_BUS_29,
  I2C_BUS_30,
  I2C_BUS_31,
  I2C_BUS_32,
  I2C_BUS_33,
  I2C_BUS_34,
  I2C_BUS_35,
  I2C_BUS_36,
  I2C_BUS_37,
  I2C_BUS_38,
  I2C_BUS_39,
  I2C_BUS_40,
  I2C_BUS_41,
  I2C_BUS_42,
  I2C_BUS_43,
  I2C_BUS_44,
  I2C_BUS_45,
  I2C_BUS_46,
  I2C_BUS_47,
  I2C_BUS_48,
  I2C_BUS_49,
  I2C_BUS_50,
  I2C_BUS_51,
  I2C_BUS_52,
  I2C_BUS_53,
  I2C_BUS_54,
  I2C_BUS_55,
  I2C_BUS_56,
  I2C_BUS_57,
  I2C_BUS_58,
  I2C_BUS_59,
  I2C_BUS_60,
  I2C_BUS_61,
  I2C_BUS_62,
  I2C_BUS_63,
  I2C_BUS_64,
  I2C_BUS_65,
  I2C_BUS_66,
  I2C_BUS_67,
  I2C_BUS_68,
  I2C_BUS_69,
};

enum {
  POSTCODE_BY_BMC,
  POSTCODE_BY_HOST,
};

enum {
  CC_OEM_DEVICE_NOT_PRESENT = 0x30,
  CC_OEM_DEVICE_INFO_ERR = 0x31,
  CC_OEM_DEVICE_DESTINATION_ERR = 0x32,
  CC_OEM_DEVICE_SEND_SLAVE_RESTORE_POWER_POLICY_FAIL =0x33,
  CC_OEM_GET_SELF_ADDRESS_ERR = 0x34,
  CC_OEM_ONLY_SUPPORT_MASTER = 0x35,
};

enum PLDM_FRU_ID {
  PLDM_FRU_NOT_SUPPORT = -1,
  PLDM_FRU_SWB = 0,
  PLDM_FRU_FIO = 1,
  PLDM_FRU_SHSC = 2,
};

enum FRU_PRESENT {
  FRU_NOT_PRSNT,
  FRU_PRSNT,
};

enum FRU_PATH_TYPE {
  FRU_PATH_NONE,
  FRU_PATH_EEPROM,
  FRU_PATH_PLDM,
};

enum VR_VENDOR {
  VR_RENESAS = 0,
  VR_TI,
  VR_INFINEON,
  VR_VISHAY,
  VR_ONSEMI,
  VR_MPS,
};

/* Artemis */
enum ARTEMIS_OEM_COMMAND {
  CMD_OEM_1S_GET_ASIC_CARD_STATUS = 0x76,
  CMD_OEM_1S_GET_SENSOR_READING = 0x77,
  CMD_OEM_1S_ACTIVE_CXL         = 0x78,
};

// JCN can plug dual or single devices
enum MEB_JCN_LOCATION {
  JCN_0_1 = 0, // dual device on location 0 and 1
  JCN_0, // single device on location 0
  JCN_1, // single device on location 1
};

enum MEB_JCN_TYPE {
  E1S_CARD,
  E1S_0_CARD,
  E1S_1_CARD,
  E1S_0_1_CARD,
  NIC_CARD,
  CXL_CARD,
  UNKNOWN_CARD = 0xff,
};

enum GTA_SKU_ID {
  GTA_CONFIG_1 = 1,
  GTA_CONFIG_8 = 8,
  GTA_CONFIG_9 = 9,
  GTA_CONFIG_12 = 12,
  GTA_CONFIG_13 = 13,
};

enum DEVICES_NUMBER {
  ACCL_DEV_NUM = 2,
  MC_DEV_NUM = 4,
  CB_DEV_NUM = 24,
};

enum DEVICE_ID {
  DEV_ID1 = 1,
  DEV_ID2,
};

// Component ID
enum CB_FRU_COMPONENT {
  // CB Devices
  DEV_ID_BASE  = 0x1E,
  FAC1_DEV1_FRU_ID = 0x1E,
  FAC1_DEV2_FRU_ID,
  FAC2_DEV1_FRU_ID,
  FAC2_DEV2_FRU_ID,
  FAC3_DEV1_FRU_ID,
  FAC3_DEV2_FRU_ID,
  FAC4_DEV1_FRU_ID,
  FAC4_DEV2_FRU_ID,
  FAC5_DEV1_FRU_ID,
  FAC5_DEV2_FRU_ID,
  FAC6_DEV1_FRU_ID,
  FAC6_DEV2_FRU_ID,
  FAC7_DEV1_FRU_ID,
  FAC7_DEV2_FRU_ID,
  FAC8_DEV1_FRU_ID,
  FAC8_DEV2_FRU_ID,
  FAC9_DEV1_FRU_ID,
  FAC9_DEV2_FRU_ID,
  FAC10_DEV1_FRU_ID,
  FAC10_DEV2_FRU_ID,
  FAC11_DEV1_FRU_ID,
  FAC11_DEV2_FRU_ID,
  FAC12_DEV1_FRU_ID,
  FAC12_DEV2_FRU_ID,
};

/* BMC to MB CPLD ADDR*/
enum GTA_MB_BMC_CPLD_INFO {
  MB_STBY_PWR_FAULT_OFFSET = 0x52,
  MB_STBY_PWR_FAULT_TIMEOUE_OFFSET = 0x53,
  MB_NORMAL_PWR_FAULT_A_OFFSET = 0x54,
  MB_NORMAL_PWR_FAULT_B_OFFSET = 0x55,
  MB_NORMAL_PWR_FAULT_TIMEOUT_A_OFFSET = 0x56,
  MB_NORMAL_PWR_FAULT_TIMEOUT_B_OFFSET = 0x57,
};

/* BMC to MC CPLD ADDR */
enum GTA_MC_BMC_CPLD_INFO {
  MC_CPLD_ADDR = 0xC0,
  MC_PWR_FAULT_OFFSET = 0x0D,
  MC_PWR_FAULT_TIMEOUT_OFFSET = 0x0E,
  MC_STBY_POWER_OFFSET = 0x01,
};

/* BMC to CB CPLD ADDR */
enum GTA_CB_BMC_CPLD_INFO {
  CB_CPLD_ADDR = 0xB8,
  CB_PWR_FAULT_A_OFFSET = 0x0D,
  CB_PWR_FAULT_B_OFFSET = 0x0E,
  CB_PWR_FAULT_TIMEOUT_A_OFFSET = 0x5D,
  CB_PWR_FAULT_TIMEOUT_B_OFFSET = 0x5E,
};

enum DEVIC_NVME_READY {
  NVME_READY = 0,
  NVME_NOT_READY = 1,
};

enum DEVICE_IDENTIFIER_SUPPORT {
  IDENTIFIER_SUPPORT = 0,
  IDENTIFIER_NOT_SUPPORT = 1,
};

enum GTA_MB_CPLD {
  GTA_MB_CPLD_ADDR = 0x46,
  MC_PWR_FAULT_MASK = 0x01,
  CB_PWR_FAULT_MASK = 0x02,
  MC_PWR_TRAY_REMOVE_MASK = 0x04,
  CB_PWR_TRAY_REMOVE_MASK = 0x08,
  MB_NORMAL_PWR_FAULT_MASK = 0x10,
  MB_STBY_PWR_FAULT_MASK = 0x20,
};

enum GTA_MB_CPLD_OFFSET {
  HSC_EN_R_OFFSET = 0x01,
  EXP_BOARD_PWR_FAULT_OFFSET = 0x0D,
  EXP_BOARD_PWR_GOOD_DROP_OFFSET = 0x10,
  EXP_BOARD_NO_PWR_GOOD_OFFSET = 0x14,
};

enum GTA_MB_CPLD_BIT {
  GPU_HSC_EN_R_BIT = 6,
};

enum GTA_MB_CPLD_ASSERTED_VALUE {
  GPU_HSC_EN_ASSERTED_VALUE = 0,
};

enum GTA_MB_CPLD_CB_POWER_FAULT_BIT {
  CB_NORMAL_PG_FAULT = 0,
  CB_STBY_PG_FAULT,
  HPDB_PG_FAULT,
};

enum GTA_MB_REV_ID {
  GTA_DVT_STAGE = 4,
};

enum GTA_EXMAX_CABLE {
  GTA_EXMAX_CABLE_A = 1,
  GTA_EXMAX_CABLE_B,
  GTA_EXMAX_CABLE_C,
  GTA_EXMAX_CABLE_D,
  GTA_EXMAX_CABLE_E,
  GTA_EXMAX_CABLE_F,
};

enum GTA_POWER_FAULT_STATUS {
  POWER_GOOD_DROP = 0,
  NO_POWER_GOOD   = 1,
};

enum GTA_MB_POWER_FAULT_LOCATION {
  MB_PWR_FAULT_A_LOCATION = 0,
  MB_PWR_FAULT_B_LOCATION = 1,
};

enum GTA_CB_POWER_FAULT_LOCATION {
  CB_POWER_FAULT_A_LOCATION = 0,
  CB_POWER_FAULT_B_LOCATION = 1,
};

/* Artemis End */

#endif
