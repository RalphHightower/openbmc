# ",/usr/bin/env python,
# ,
# Copyright 2018-present Facebook. All Rights Reserved.,
# ,
# This program file is free software; you can redistribute it and/or modify it,
# under the terms of the GNU General Public License as published by the,
# Free Software Foundation; version 2 of the License.,
# ,
# This program is distributed in the hope that it will be useful, but WITHOUT,
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or,
# FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License,
# for more details.,
# ,
# You should have received a copy of the GNU General Public License,
# along with this program in a file named COPYING; if not, write to the,
# Free Software Foundation, Inc.,,
# 51 Franklin Street, Fifth Floor,,
# Boston, MA 02110-1301 USA,
# ,

REST_END_POINTS = {
    "/api": ["version", "Description"],
    "/api/bmc": [
        "load-15",
        "open-fds",
        "Uptime",
        "OpenBMC Version",
        "uptime",
        "Description",
        "kernel version",
        "SPI0 Vendor",
        "Secondary Boot Triggered",
        "load-5",
        "u-boot version",
        "SPI1 Vendor",
        "load-1",
        "Memory Usage",
        "TPM FW version",
        "Reset Reason",
        "TPM TCG version",
        "CPU Usage",
        "MAC Addr",
        "MTD Parts",
        "At-Scale-Debug Running",
        "vboot",
        "memory",
    ],
    "/api/fans": [
        "Fan 0 Speed",
        "Fan 1 Speed",
        "Fan Mode",
        "FSCD Driver",
        "Sensor Fail",
        "Fan Fail",
        "Platform Specific",
    ],
    "/api/logs": ["Logs"],
    "/api/mezz": ["Description"],
    "/api/mezz/fruid": [
        "Product FRU ID",
        "Product Manufacturer",
        "Product Name",
        "Product Version",
        "Product Custom Data 1",
        "Board Mfg Date",
        "Board Product",
        "Product Asset Tag",
        "Board FRU ID",
        "Product Custom Data 2",
        "Board Part Number",
        "Product Serial",
        "Product Custom Data 3",
        "Board Serial",
        "Board Custom Data 3",
        "Board Custom Data 2",
        "Board Custom Data 1",
        "Product Part Number",
        "Board Mfg",
    ],
    "/api/mezz/logs": ["Logs"],
    "/api/mezz/sensors": ["MEZZ_SENSOR_TEMP"],
    "/api/sensors": [
        "PVCCSA VR Pout",
        "SP_HSC_TEMP",
        "SP_HSC_IN_VOLT",
        "SOC DIMMA0 Temp",
        "SP_HSC_OUT_CURR",
        "SP_P3V3",
        "PVDDQ_AB",
        "SP_FAN1_PWM",
        "PVCCIO VR Pout",
        "SP_P1V8_STBY",
        "PVDDQ_AB VR Temp",
        "SP_FAN0_TACH",
        "PVDDQ_DE VR Pout",
        "SYSTEM_AIRFLOW",
        "SP_HSC_PEAK_PIN",
        "HOST_BOOT_TEMP",
        "PVDDQ_DE VR Curr",
        "INA230 Voltage",
        "SOC DIMMD1 Temp",
        "SP_OUTLET_TEMP",
        "PVCCIO VR Vol",
        "PVCCIN VR Temp",
        "P1V05PCH VR Temp",
        "SOC DIMMD0 Temp",
        "SOC DIMMA1 Temp",
        "P12V_STBY_MB",
        "MB Outlet Temp_B",
        "PVNN_PCH VR Temp",
        "SP_P5V",
        "NVMe2 CTemp",
        "SOC Package Pwr",
        "PVDDQ_AB VR Curr",
        "MB Outlet Temp_T",
        "SP_HSC_IN_POWERAVG",
        "INA230 Power",
        "PVDDQ_DE VR Vol",
        "P1V05_PCH",
        "MB Inlet Temp",
        "SP_INLET_TEMP",
        "SP_HSC_PEAK_IOUT",
        "SP_SENSOR_P2V5_BMC_STBY",
        "PVDDQ_AB VR Vol",
        "P3V3_STBY_MB",
        "PVDDQ_AB VR Pout",
        "SP_P3V3_STBY",
        "P1V05PCH VR Vol",
        "P1V05PCH VR Pout",
        "PVCCSA VR Vol",
        "PVCCIN VR Pout",
        "SP_FAN1_TACH",
        "NVMe1 CTemp",
        "PVCCSA VR Curr",
        "SOC DIMMB1 Temp",
        "PVNN_PCH VR Curr",
        "SP_P12V",
        "SOC Therm Margin",
        "SP_FAN0_PWM",
        "SP_P12V_SLOT4",
        "SOC Tjmax",
        "SP_SENSOR_P1V2_BMC_STBY",
        "SP_P12V_SLOT1",
        "SP_P12V_SLOT2",
        "SP_P12V_SLOT3",
        "SP_SENSOR_P1V15_BMC_STBY",
        "PVCCIO VR Temp",
        "PVNNPCH",
        "PV_BAT",
        "PCH Temp",
        "SOC DIMME1 Temp",
        "MEZZ_SENSOR_TEMP",
        "PVCCSA VR Temp",
        "PVDDQ_DE VR Temp",
        "SOC Temp",
        "PVCCIN VR Vol",
        "P1V05PCH VR Curr",
        "SP_HSC_IN_POWER",
        "SOC DIMMB0 Temp",
        "PVNN_PCH VR Pout",
        "SOC DIMME0 Temp",
        "P3V3_MB",
        "PVCCIO VR Curr",
        "PVDDQ_DE",
        "PVCCIN VR Curr",
    ],
    "/api/server1": ["Power status", "BIC_ok"],
    "/api/server1/bios": ["Description"],
    "/api/server1/bios/boot-order": ["Description"],
    "/api/server1/bios/boot-order/boot_mode": [
        "Note #1: Actions Format:",
        "Boot Mode",
        "Note #2: Boot Mode No.",
    ],
    "/api/server1/bios/boot-order/boot_order": [
        "Boot Order",
        "Note #2: Boot Order No.",
        "Note #1: Actions Format:",
    ],
    "/api/server1/bios/boot-order/clear_cmos": ["Clear CMOS Function"],
    "/api/server1/bios/boot-order/force_boot_bios_setup": [
        "Force Boot to BIOS Setup Function"
    ],
    "/api/server1/bios/plat-info": ["Platform Information"],
    "/api/server1/bios/postcode": ["POST Code"],
    "/api/server1/config": [
        "slot1_trigger_hpr",
        "sysfw_ver_slot1",
        "slot1_sel_error",
        "slot1_boot_order",
        "slot1_sensor_health",
        "pwr_server1_last_state",
        "identify_slot1",
        "slot1_cpu_ppin",
        "slot1_por_cfg",
    ],
    "/api/server1/fruid": [
        "Product Name",
        "Product Version",
        "Product Manufacturer",
        "Board Mfg Date",
        "Product Custom Data 1",
        "Board FRU ID",
        "Product Custom Data 2",
        "Board Part Number",
        "Product Serial",
        "Chassis Custom Data 1",
        "Board Product",
        "Board Serial",
        "Product FRU ID",
        "Board Custom Data 1",
        "Product Part Number",
        "Board Mfg",
        "Chassis Type",
    ],
    "/api/server1/logs": ["Logs"],
    "/api/server1/sensors": [
        "PVNN_PCH VR Curr",
        "PVCCSA VR Pout",
        "PVCCIO VR Temp",
        "PVDDQ_AB",
        "PVCCIO VR Pout",
        "P12V_STBY_MB",
        "PVDDQ_DE VR Vol",
        "PVDDQ_DE VR Pout",
        "HOST_BOOT_TEMP",
        "PVDDQ_AB VR Curr",
        "SOC DIMMD1 Temp",
        "INA230 Voltage",
        "PVCCIN VR Temp",
        "P1V05PCH VR Temp",
        "SOC DIMMA1 Temp",
        "MB Outlet Temp_B",
        "SOC DIMME1 Temp",
        "SOC DIMMD0 Temp",
        "NVMe2 CTemp",
        "SOC Package Pwr",
        "PVDDQ_DE VR Curr",
        "MB Outlet Temp_T",
        "INA230 Power",
        "P1V05_PCH",
        "MB Inlet Temp",
        "PVDDQ_AB VR Vol",
        "P3V3_STBY_MB",
        "PVDDQ_AB VR Pout",
        "P1V05PCH VR Vol",
        "P1V05PCH VR Pout",
        "PVCCSA VR Vol",
        "PVCCIN VR Pout",
        "NVMe1 CTemp",
        "PVCCSA VR Curr",
        "PVDDQ_DE",
        "SOC DIMMA0 Temp",
        "SOC Therm Margin",
        "SOC Tjmax",
        "PVCCIO VR Vol",
        "SOC DIMMB1 Temp",
        "PVNNPCH",
        "PV_BAT",
        "PCH Temp",
        "PVNN_PCH VR Temp",
        "PVCCSA VR Temp",
        "PVDDQ_DE VR Temp",
        "SOC Temp",
        "PVCCIN VR Vol",
        "P1V05PCH VR Curr",
        "SOC DIMMB0 Temp",
        "PVNN_PCH VR Pout",
        "SOC DIMME0 Temp",
        "P3V3_MB",
        "PVCCIO VR Curr",
        "PVDDQ_AB VR Temp",
        "PVCCIN VR Curr",
    ],
    "/api/server2": ["Power status", "BIC_ok"],
    "/api/server2/bios": ["Description"],
    "/api/server2/bios/boot-order": ["Description"],
    "/api/server2/bios/boot-order/boot_mode": [
        "Note #1: Actions Format:",
        "Boot Mode",
        "Note #2: Boot Mode No.",
    ],
    "/api/server2/bios/boot-order/boot_order": [
        "Boot Order",
        "Note #2: Boot Order No.",
        "Note #1: Actions Format:",
    ],
    "/api/server2/bios/boot-order/clear_cmos": ["Clear CMOS Function"],
    "/api/server2/bios/boot-order/force_boot_bios_setup": [
        "Force Boot to BIOS Setup Function"
    ],
    "/api/server2/bios/plat-info": ["Platform Information"],
    "/api/server2/bios/postcode": ["POST Code"],
    "/api/server2/config": [
        "pwr_server2_last_state",
        "sysfw_ver_slot2",
        "slot2_sel_error",
        "slot2_por_cfg",
        "slot2_trigger_hpr",
        "slot2_boot_order",
        "slot2_sensor_health",
        "identify_slot2",
        "slot2_cpu_ppin",
    ],
    "/api/server2/fruid": [
        "Product Name",
        "Product Version",
        "Product Manufacturer",
        "Board Mfg Date",
        "Product Custom Data 1",
        "Board FRU ID",
        "Product Custom Data 2",
        "Board Part Number",
        "Product Serial",
        "Chassis Custom Data 1",
        "Board Product",
        "Board Serial",
        "Product FRU ID",
        "Board Custom Data 1",
        "Product Part Number",
        "Board Mfg",
        "Chassis Type",
    ],
    "/api/server2/logs": ["Logs"],
    "/api/server2/sensors": [
        "PVNN_PCH VR Curr",
        "PVCCSA VR Pout",
        "PVCCIO VR Temp",
        "PVDDQ_AB",
        "PVCCIO VR Pout",
        "P12V_STBY_MB",
        "PVDDQ_DE VR Vol",
        "PVDDQ_DE VR Pout",
        "HOST_BOOT_TEMP",
        "PVDDQ_AB VR Curr",
        "SOC DIMMD1 Temp",
        "INA230 Voltage",
        "PVCCIN VR Temp",
        "P1V05PCH VR Temp",
        "SOC DIMMA1 Temp",
        "MB Outlet Temp_B",
        "SOC DIMME1 Temp",
        "SOC DIMMD0 Temp",
        "NVMe2 CTemp",
        "SOC Package Pwr",
        "PVDDQ_DE VR Curr",
        "MB Outlet Temp_T",
        "INA230 Power",
        "P1V05_PCH",
        "MB Inlet Temp",
        "PVDDQ_AB VR Vol",
        "P3V3_STBY_MB",
        "PVDDQ_AB VR Pout",
        "P1V05PCH VR Vol",
        "P1V05PCH VR Pout",
        "PVCCSA VR Vol",
        "PVCCIN VR Pout",
        "NVMe1 CTemp",
        "PVCCSA VR Curr",
        "PVDDQ_DE",
        "SOC DIMMA0 Temp",
        "SOC Therm Margin",
        "SOC Tjmax",
        "PVCCIO VR Vol",
        "SOC DIMMB1 Temp",
        "PVNNPCH",
        "PV_BAT",
        "PCH Temp",
        "PVNN_PCH VR Temp",
        "PVCCSA VR Temp",
        "PVDDQ_DE VR Temp",
        "SOC Temp",
        "PVCCIN VR Vol",
        "P1V05PCH VR Curr",
        "SOC DIMMB0 Temp",
        "PVNN_PCH VR Pout",
        "SOC DIMME0 Temp",
        "P3V3_MB",
        "PVCCIO VR Curr",
        "PVDDQ_AB VR Temp",
        "PVCCIN VR Curr",
    ],
    "/api/server3": ["Power status", "BIC_ok"],
    "/api/server3/bios": ["Description"],
    "/api/server3/bios/boot-order": ["Description"],
    "/api/server3/bios/boot-order/boot_mode": [
        "Note #1: Actions Format:",
        "Boot Mode",
        "Note #2: Boot Mode No.",
    ],
    "/api/server3/bios/boot-order/boot_order": [
        "Boot Order",
        "Note #2: Boot Order No.",
        "Note #1: Actions Format:",
    ],
    "/api/server3/bios/boot-order/clear_cmos": ["Clear CMOS Function"],
    "/api/server3/bios/boot-order/force_boot_bios_setup": [
        "Force Boot to BIOS Setup Function"
    ],
    "/api/server3/bios/plat-info": ["Platform Information"],
    "/api/server3/bios/postcode": ["POST Code"],
    "/api/server3/config": [
        "pwr_server3_last_state",
        "slot3_por_cfg",
        "sysfw_ver_slot3",
        "slot3_sel_error",
        "slot3_trigger_hpr",
        "slot3_boot_order",
        "slot3_cpu_ppin",
        "slot3_sensor_health",
        "identify_slot3",
    ],
    "/api/server3/fruid": [
        "Product Name",
        "Product Version",
        "Product Manufacturer",
        "Board Mfg Date",
        "Product Custom Data 1",
        "Board FRU ID",
        "Product Custom Data 2",
        "Board Part Number",
        "Product Serial",
        "Chassis Custom Data 1",
        "Board Product",
        "Board Serial",
        "Product FRU ID",
        "Board Custom Data 1",
        "Product Part Number",
        "Board Mfg",
        "Chassis Type",
    ],
    "/api/server3/logs": ["Logs"],
    "/api/server3/sensors": [
        "PVNN_PCH VR Curr",
        "PVCCSA VR Pout",
        "PVCCIO VR Temp",
        "PVDDQ_AB",
        "PVCCIO VR Pout",
        "P12V_STBY_MB",
        "PVDDQ_DE VR Vol",
        "PVDDQ_DE VR Pout",
        "HOST_BOOT_TEMP",
        "PVDDQ_AB VR Curr",
        "SOC DIMMD1 Temp",
        "INA230 Voltage",
        "PVCCIN VR Temp",
        "P1V05PCH VR Temp",
        "SOC DIMMA1 Temp",
        "MB Outlet Temp_B",
        "SOC DIMME1 Temp",
        "SOC DIMMD0 Temp",
        "NVMe2 CTemp",
        "SOC Package Pwr",
        "PVDDQ_DE VR Curr",
        "MB Outlet Temp_T",
        "INA230 Power",
        "P1V05_PCH",
        "MB Inlet Temp",
        "PVDDQ_AB VR Vol",
        "P3V3_STBY_MB",
        "PVDDQ_AB VR Pout",
        "P1V05PCH VR Vol",
        "P1V05PCH VR Pout",
        "PVCCSA VR Vol",
        "PVCCIN VR Pout",
        "NVMe1 CTemp",
        "PVCCSA VR Curr",
        "PVDDQ_DE",
        "SOC DIMMA0 Temp",
        "SOC Therm Margin",
        "SOC Tjmax",
        "PVCCIO VR Vol",
        "SOC DIMMB1 Temp",
        "PVNNPCH",
        "PV_BAT",
        "PCH Temp",
        "PVNN_PCH VR Temp",
        "PVCCSA VR Temp",
        "PVDDQ_DE VR Temp",
        "SOC Temp",
        "PVCCIN VR Vol",
        "P1V05PCH VR Curr",
        "SOC DIMMB0 Temp",
        "PVNN_PCH VR Pout",
        "SOC DIMME0 Temp",
        "P3V3_MB",
        "PVCCIO VR Curr",
        "PVDDQ_AB VR Temp",
        "PVCCIN VR Curr",
    ],
    "/api/server4": ["Power status", "BIC_ok"],
    "/api/server4/bios": ["Description"],
    "/api/server4/bios/boot-order": ["Description"],
    "/api/server4/bios/boot-order/boot_mode": [
        "Note #1: Actions Format:",
        "Boot Mode",
        "Note #2: Boot Mode No.",
    ],
    "/api/server4/bios/boot-order/boot_order": [
        "Boot Order",
        "Note #2: Boot Order No.",
        "Note #1: Actions Format:",
    ],
    "/api/server4/bios/boot-order/clear_cmos": ["Clear CMOS Function"],
    "/api/server4/bios/boot-order/force_boot_bios_setup": [
        "Force Boot to BIOS Setup Function"
    ],
    "/api/server4/bios/plat-info": ["Platform Information"],
    "/api/server4/bios/postcode": ["POST Code"],
    "/api/server4/config": [
        "pwr_server4_last_state",
        "slot4_por_cfg",
        "slot4_boot_order",
        "sysfw_ver_slot4",
        "slot4_cpu_ppin",
        "slot4_sensor_health",
        "identify_slot4",
        "slot4_sel_error",
        "slot4_trigger_hpr",
    ],
    "/api/server4/fruid": [
        "Product Name",
        "Product Version",
        "Product Manufacturer",
        "Board Mfg Date",
        "Product Custom Data 1",
        "Board FRU ID",
        "Product Custom Data 2",
        "Board Part Number",
        "Product Serial",
        "Chassis Custom Data 1",
        "Board Product",
        "Board Serial",
        "Product FRU ID",
        "Board Custom Data 1",
        "Product Part Number",
        "Board Mfg",
        "Chassis Type",
    ],
    "/api/server4/logs": ["Logs"],
    "/api/server4/sensors": [
        "PVNN_PCH VR Curr",
        "PVCCSA VR Pout",
        "PVCCIO VR Temp",
        "PVDDQ_AB",
        "PVCCIO VR Pout",
        "P12V_STBY_MB",
        "PVDDQ_DE VR Vol",
        "PVDDQ_DE VR Pout",
        "HOST_BOOT_TEMP",
        "PVDDQ_AB VR Curr",
        "SOC DIMMD1 Temp",
        "INA230 Voltage",
        "PVCCIN VR Temp",
        "P1V05PCH VR Temp",
        "SOC DIMMA1 Temp",
        "MB Outlet Temp_B",
        "SOC DIMME1 Temp",
        "SOC DIMMD0 Temp",
        "NVMe2 CTemp",
        "SOC Package Pwr",
        "PVDDQ_DE VR Curr",
        "MB Outlet Temp_T",
        "INA230 Power",
        "P1V05_PCH",
        "MB Inlet Temp",
        "PVDDQ_AB VR Vol",
        "P3V3_STBY_MB",
        "PVDDQ_AB VR Pout",
        "P1V05PCH VR Vol",
        "P1V05PCH VR Pout",
        "PVCCSA VR Vol",
        "PVCCIN VR Pout",
        "NVMe1 CTemp",
        "PVCCSA VR Curr",
        "PVDDQ_DE",
        "SOC DIMMA0 Temp",
        "SOC Therm Margin",
        "SOC Tjmax",
        "PVCCIO VR Vol",
        "SOC DIMMB1 Temp",
        "PVNNPCH",
        "PV_BAT",
        "PCH Temp",
        "PVNN_PCH VR Temp",
        "PVCCSA VR Temp",
        "PVDDQ_DE VR Temp",
        "SOC Temp",
        "PVCCIN VR Vol",
        "P1V05PCH VR Curr",
        "SOC DIMMB0 Temp",
        "PVNN_PCH VR Pout",
        "SOC DIMME0 Temp",
        "P3V3_MB",
        "PVCCIO VR Curr",
        "PVDDQ_AB VR Temp",
        "PVCCIN VR Curr",
    ],
    "/api/spb": ["Description"],
    "/api/spb/bmc": [
        "load-15",
        "open-fds",
        "Uptime",
        "OpenBMC Version",
        "uptime",
        "Description",
        "kernel version",
        "SPI0 Vendor",
        "Secondary Boot Triggered",
        "load-5",
        "u-boot version",
        "SPI1 Vendor",
        "load-1",
        "Memory Usage",
        "TPM FW version",
        "Reset Reason",
        "TPM TCG version",
        "CPU Usage",
        "MAC Addr",
        "MTD Parts",
        "At-Scale-Debug Running",
        "vboot",
        "memory",
    ],
    "/api/spb/fans": [
        "Fan 0 Speed",
        "Fan 1 Speed",
        "Fan Mode",
        "FSCD Driver",
        "Sensor Fail",
        "Fan Fail",
        "Platform Specific",
    ],
    "/api/spb/fruid": [
        "Product Manufacturer",
        "Product Name",
        "Board Serial",
        "Product Version",
        "Product Custom Data 1",
        "Board Mfg Date",
        "Product Asset Tag",
        "Board FRU ID",
        "Product Custom Data 2",
        "Board Part Number",
        "Product Serial",
        "Board Product",
        "Chassis Part Number",
        "Product FRU ID",
        "Board Custom Data 1",
        "Product Part Number",
        "Board Mfg",
        "Chassis Type",
        "Chassis Serial Number",
    ],
    "/api/spb/logs": ["Logs"],
    "/api/spb/sensors": [
        "SP_SENSOR_P2V5_BMC_STBY",
        "SP_P1V8_STBY",
        "SP_HSC_TEMP",
        "SP_P3V3_STBY",
        "SP_HSC_IN_VOLT",
        "SP_HSC_OUT_CURR",
        "SP_HSC_IN_POWERAVG",
        "SP_FAN0_TACH",
        "SP_FAN1_PWM",
        "SP_P12V_SLOT4",
        "SP_P12V",
        "SP_HSC_PEAK_PIN",
        "SP_FAN0_PWM",
        "SP_FAN1_TACH",
        "SP_SENSOR_P1V2_BMC_STBY",
        "SP_P5V",
        "SP_P12V_SLOT1",
        "SP_P12V_SLOT2",
        "SP_P12V_SLOT3",
        "SP_SENSOR_P1V15_BMC_STBY",
        "SP_INLET_TEMP",
        "SP_OUTLET_TEMP",
        "SP_P3V3",
        "SP_HSC_IN_POWER",
        "SP_HSC_PEAK_IOUT",
    ],
}
