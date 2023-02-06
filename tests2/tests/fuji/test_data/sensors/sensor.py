# ",/usr/bin/env python,
# ,
# Copyright 2020-present Facebook. All Rights Reserved.,
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

SENSORS = []

SCM_SENSORS = [
    "SCM_OUTLET_U7_TEMP",
    "SCM_INLET_U8_TEMP",
    "SCM_INPUT_VOLTAGE",
    "SCM_SENSOR_POWER_VOLTAGE",
    "SCM_CURRENT",
    "SCM_POWER",
    "BMC_LM75_U9_TEMP",
    "MB_OUTLET_TEMP",
    "MB_INLET_TEMP",
    "PCH_TEMP",
    "VCCIN_VR_TEMP",
    "1V05MIX_VR_TEMP",
    "SOC_TEMP",
    # "SOC_THERM_MARGIN_TEMP",
    "VDDR_VR_TEMP",
    "SOC_DIMMA0_TEMP",
    "SOC_DIMMB0_TEMP",
    "SOC_PACKAGE_POWER",
    "VCCIN_VR_OUT_POWER",
    "VDDR_VR_OUT_POWER",
    # "SOC_TJMAX_TEMP",
    "P3V3_MB_VOLT",
    "P12V_MB_VOLT",
    "P1V05_PCH_VOLT",
    "P3V3_STBY_MB_VOLT",
    "P5V_STBY_MB_VOLT",
    "PV_BAT_VOLT",
    "PVDDR_VOLT",
    "P1V05_MIX_VOLT",
    "1V05MIX_VR_CURR",
    "VDDR_VR_CURR",
    "VCCIN_VR_CURR",
    "VCCIN_VR_VOLT",
    "VDDR_VR_VOLT",
    "1V05MIX_VR_VOLT",
    "1V05MIX_VR_OUT_POWER",
    "INA230_POWER",
    "INA230_VOLT",
]

PIM1_SENSORS_16Q = [
    "PIM1_LM75_U37_TEMP_BASE",
    "PIM1_LM75_U26_TEMP",
    "PIM1_LM75_U37_TEMP_MEZZ",
    "PIM1_QSFP_TEMP",
    "PIM1_INPUT_VOLTAGE",
    "PIM1_POWER_VOLTAGE",
    "PIM1_CURRENT",
    "PIM1_POWER",
    "PIM1_XP3R3V",
    "PIM1_XP3R3V_EARLY",
    "PIM1_XP2R5V_EARLY",
    "PIM1_TXDRV_PHY",
    "PIM1_XP0R8V_PHY",
    "PIM1_XP1R1V_EARLY",
    "PIM1_DVDD_PHY4",
    "PIM1_DVDD_PHY3",
    "PIM1_DVDD_PHY2",
    "PIM1_DVDD_PHY1",
    "PIM1_XP1R8V_EARLY",
    "PIM1_XP1R8V_PHYIO",
    "PIM1_XP1R8V_PHYAVDD",
    "PIM1_MP2975_INPUT_VOLTAGE",
    "PIM1_MP2975_OUTPUT_VOL_XP0R8V",
    "PIM1_MP2975_OUTPUT_CURR_XP0R8V",
    "PIM1_MP2975_OUTPUT_VOL_XP3R3V",
    "PIM1_MP2975_OUTPUT_CURR_XP3R3V",
]

PIM1_SENSORS_16O = [
    "PIM1_LM75_4A",
    "PIM1_LM75_U27_TEMP_FRONT",
    "PIM1_LM75_U28_TEMP_REAR",
    "PIM1_QSFP_TEMP",
    "PIM1_INPUT_VOLTAGE",
    "PIM1_POWER_VOLTAGE",
    "PIM1_CURRENT",
    "PIM1_POWER",
    "PIM1_XP3R3V",
    "PIM1_XP2R5V",
    "PIM1_XP1R1V",
    "PIM1_XP1R8V",
    "PIM1_XP3R3V_OBO",
    "PIM1_XP8R0V_OBO",
    "PIM1_XP0R65V_OBO",
    "PIM1_XP0R94V_OBO",
    "PIM1_XP1R15V_OBO",
    "PIM1_XP1R8V_OBO",
    "PIM1_XP2R0V_OBO",
    "PIM1_XP3R6V_OBO",
    "PIM1_UCD90160_VOLT13",
    "PIM1_MP2975_INPUT_VOLTAGE",
    "PIM1_MP2975_OUTPUT_VOL_XP0R8V",
    "PIM1_MP2975_OUTPUT_CURR_XP0R8V",
    "PIM1_MP2975_OUTPUT_VOL_XP3R3V",
    "PIM1_MP2975_OUTPUT_CURR_XP3R3V",
]


PIM2_SENSORS_16Q = [
    "PIM2_LM75_U37_TEMP_BASE",
    "PIM2_LM75_U26_TEMP",
    "PIM2_LM75_U37_TEMP_MEZZ",
    "PIM2_QSFP_TEMP",
    "PIM2_INPUT_VOLTAGE",
    "PIM2_POWER_VOLTAGE",
    "PIM2_CURRENT",
    "PIM2_POWER",
    "PIM2_XP3R3V",
    "PIM2_XP3R3V_EARLY",
    "PIM2_XP2R5V_EARLY",
    "PIM2_TXDRV_PHY",
    "PIM2_XP0R8V_PHY",
    "PIM2_XP1R1V_EARLY",
    "PIM2_DVDD_PHY4",
    "PIM2_DVDD_PHY3",
    "PIM2_DVDD_PHY2",
    "PIM2_DVDD_PHY1",
    "PIM2_XP1R8V_EARLY",
    "PIM2_XP1R8V_PHYIO",
    "PIM2_XP1R8V_PHYAVDD",
    "PIM2_MP2975_INPUT_VOLTAGE",
    "PIM2_MP2975_OUTPUT_VOL_XP0R8V",
    "PIM2_MP2975_OUTPUT_CURR_XP0R8V",
    "PIM2_MP2975_OUTPUT_VOL_XP3R3V",
    "PIM2_MP2975_OUTPUT_CURR_XP3R3V",
]

PIM2_SENSORS_16O = [
    "PIM2_LM75_4A",
    "PIM2_LM75_U27_TEMP_FRONT",
    "PIM2_LM75_U28_TEMP_REAR",
    "PIM2_QSFP_TEMP",
    "PIM2_INPUT_VOLTAGE",
    "PIM2_POWER_VOLTAGE",
    "PIM2_CURRENT",
    "PIM2_POWER",
    "PIM2_XP3R3V",
    "PIM2_XP2R5V",
    "PIM2_XP1R1V",
    "PIM2_XP1R8V",
    "PIM2_XP3R3V_OBO",
    "PIM2_XP8R0V_OBO",
    "PIM2_XP0R65V_OBO",
    "PIM2_XP0R94V_OBO",
    "PIM2_XP1R15V_OBO",
    "PIM2_XP1R8V_OBO",
    "PIM2_XP2R0V_OBO",
    "PIM2_XP3R6V_OBO",
    "PIM2_UCD90160_VOLT13",
    "PIM2_MP2975_INPUT_VOLTAGE",
    "PIM2_MP2975_OUTPUT_VOL_XP0R8V",
    "PIM2_MP2975_OUTPUT_CURR_XP0R8V",
    "PIM2_MP2975_OUTPUT_VOL_XP3R3V",
    "PIM2_MP2975_OUTPUT_CURR_XP3R3V",
]


PIM3_SENSORS_16Q = [
    "PIM3_LM75_U37_TEMP_BASE",
    "PIM3_LM75_U26_TEMP",
    "PIM3_LM75_U37_TEMP_MEZZ",
    "PIM3_QSFP_TEMP",
    "PIM3_INPUT_VOLTAGE",
    "PIM3_POWER_VOLTAGE",
    "PIM3_CURRENT",
    "PIM3_POWER",
    "PIM3_XP3R3V",
    "PIM3_XP3R3V_EARLY",
    "PIM3_XP2R5V_EARLY",
    "PIM3_TXDRV_PHY",
    "PIM3_XP0R8V_PHY",
    "PIM3_XP1R1V_EARLY",
    "PIM3_DVDD_PHY4",
    "PIM3_DVDD_PHY3",
    "PIM3_DVDD_PHY2",
    "PIM3_DVDD_PHY1",
    "PIM3_XP1R8V_EARLY",
    "PIM3_XP1R8V_PHYIO",
    "PIM3_XP1R8V_PHYAVDD",
    "PIM3_MP2975_INPUT_VOLTAGE",
    "PIM3_MP2975_OUTPUT_VOL_XP0R8V",
    "PIM3_MP2975_OUTPUT_CURR_XP0R8V",
    "PIM3_MP2975_OUTPUT_VOL_XP3R3V",
    "PIM3_MP2975_OUTPUT_CURR_XP3R3V",
]

PIM3_SENSORS_16O = [
    "PIM3_LM75_4A",
    "PIM3_LM75_U27_TEMP_FRONT",
    "PIM3_LM75_U28_TEMP_REAR",
    "PIM3_QSFP_TEMP",
    "PIM3_INPUT_VOLTAGE",
    "PIM3_POWER_VOLTAGE",
    "PIM3_CURRENT",
    "PIM3_POWER",
    "PIM3_XP3R3V",
    "PIM3_XP2R5V",
    "PIM3_XP1R1V",
    "PIM3_XP1R8V",
    "PIM3_XP3R3V_OBO",
    "PIM3_XP8R0V_OBO",
    "PIM3_XP0R65V_OBO",
    "PIM3_XP0R94V_OBO",
    "PIM3_XP1R15V_OBO",
    "PIM3_XP1R8V_OBO",
    "PIM3_XP2R0V_OBO",
    "PIM3_XP3R6V_OBO",
    "PIM3_UCD90160_VOLT13",
    "PIM3_MP2975_INPUT_VOLTAGE",
    "PIM3_MP2975_OUTPUT_VOL_XP0R8V",
    "PIM3_MP2975_OUTPUT_CURR_XP0R8V",
    "PIM3_MP2975_OUTPUT_VOL_XP3R3V",
    "PIM3_MP2975_OUTPUT_CURR_XP3R3V",
]


PIM4_SENSORS_16Q = [
    "PIM4_LM75_U37_TEMP_BASE",
    "PIM4_LM75_U26_TEMP",
    "PIM4_LM75_U37_TEMP_MEZZ",
    "PIM4_QSFP_TEMP",
    "PIM4_INPUT_VOLTAGE",
    "PIM4_POWER_VOLTAGE",
    "PIM4_CURRENT",
    "PIM4_POWER",
    "PIM4_XP3R3V",
    "PIM4_XP3R3V_EARLY",
    "PIM4_XP2R5V_EARLY",
    "PIM4_TXDRV_PHY",
    "PIM4_XP0R8V_PHY",
    "PIM4_XP1R1V_EARLY",
    "PIM4_DVDD_PHY4",
    "PIM4_DVDD_PHY3",
    "PIM4_DVDD_PHY2",
    "PIM4_DVDD_PHY1",
    "PIM4_XP1R8V_EARLY",
    "PIM4_XP1R8V_PHYIO",
    "PIM4_XP1R8V_PHYAVDD",
    "PIM4_MP2975_INPUT_VOLTAGE",
    "PIM4_MP2975_OUTPUT_VOL_XP0R8V",
    "PIM4_MP2975_OUTPUT_CURR_XP0R8V",
    "PIM4_MP2975_OUTPUT_VOL_XP3R3V",
    "PIM4_MP2975_OUTPUT_CURR_XP3R3V",
]

PIM4_SENSORS_16O = [
    "PIM4_LM75_4A",
    "PIM4_LM75_U27_TEMP_FRONT",
    "PIM4_LM75_U28_TEMP_REAR",
    "PIM4_QSFP_TEMP",
    "PIM4_INPUT_VOLTAGE",
    "PIM4_POWER_VOLTAGE",
    "PIM4_CURRENT",
    "PIM4_POWER",
    "PIM4_XP3R3V",
    "PIM4_XP2R5V",
    "PIM4_XP1R1V",
    "PIM4_XP1R8V",
    "PIM4_XP3R3V_OBO",
    "PIM4_XP8R0V_OBO",
    "PIM4_XP0R65V_OBO",
    "PIM4_XP0R94V_OBO",
    "PIM4_XP1R15V_OBO",
    "PIM4_XP1R8V_OBO",
    "PIM4_XP2R0V_OBO",
    "PIM4_XP3R6V_OBO",
    "PIM4_UCD90160_VOLT13",
    "PIM4_MP2975_INPUT_VOLTAGE",
    "PIM4_MP2975_OUTPUT_VOL_XP0R8V",
    "PIM4_MP2975_OUTPUT_CURR_XP0R8V",
    "PIM4_MP2975_OUTPUT_VOL_XP3R3V",
    "PIM4_MP2975_OUTPUT_CURR_XP3R3V",
]


PIM5_SENSORS_16Q = [
    "PIM5_LM75_U37_TEMP_BASE",
    "PIM5_LM75_U26_TEMP",
    "PIM5_LM75_U37_TEMP_MEZZ",
    "PIM5_QSFP_TEMP",
    "PIM5_INPUT_VOLTAGE",
    "PIM5_POWER_VOLTAGE",
    "PIM5_CURRENT",
    "PIM5_POWER",
    "PIM5_XP3R3V",
    "PIM5_XP3R3V_EARLY",
    "PIM5_XP2R5V_EARLY",
    "PIM5_TXDRV_PHY",
    "PIM5_XP0R8V_PHY",
    "PIM5_XP1R1V_EARLY",
    "PIM5_DVDD_PHY4",
    "PIM5_DVDD_PHY3",
    "PIM5_DVDD_PHY2",
    "PIM5_DVDD_PHY1",
    "PIM5_XP1R8V_EARLY",
    "PIM5_XP1R8V_PHYIO",
    "PIM5_XP1R8V_PHYAVDD",
    "PIM5_MP2975_INPUT_VOLTAGE",
    "PIM5_MP2975_OUTPUT_VOL_XP0R8V",
    "PIM5_MP2975_OUTPUT_CURR_XP0R8V",
    "PIM5_MP2975_OUTPUT_VOL_XP3R3V",
    "PIM5_MP2975_OUTPUT_CURR_XP3R3V",
]

PIM5_SENSORS_16O = [
    "PIM5_LM75_4A",
    "PIM5_LM75_U27_TEMP_FRONT",
    "PIM5_LM75_U28_TEMP_REAR",
    "PIM5_QSFP_TEMP",
    "PIM5_INPUT_VOLTAGE",
    "PIM5_POWER_VOLTAGE",
    "PIM5_CURRENT",
    "PIM5_POWER",
    "PIM5_XP3R3V",
    "PIM5_XP2R5V",
    "PIM5_XP1R1V",
    "PIM5_XP1R8V",
    "PIM5_XP3R3V_OBO",
    "PIM5_XP8R0V_OBO",
    "PIM5_XP0R65V_OBO",
    "PIM5_XP0R94V_OBO",
    "PIM5_XP1R15V_OBO",
    "PIM5_XP1R8V_OBO",
    "PIM5_XP2R0V_OBO",
    "PIM5_XP3R6V_OBO",
    "PIM5_UCD90160_VOLT13",
    "PIM5_MP2975_INPUT_VOLTAGE",
    "PIM5_MP2975_OUTPUT_VOL_XP0R8V",
    "PIM5_MP2975_OUTPUT_CURR_XP0R8V",
    "PIM5_MP2975_OUTPUT_VOL_XP3R3V",
    "PIM5_MP2975_OUTPUT_CURR_XP3R3V",
]


PIM6_SENSORS_16Q = [
    "PIM6_LM75_U37_TEMP_BASE",
    "PIM6_LM75_U26_TEMP",
    "PIM6_LM75_U37_TEMP_MEZZ",
    "PIM6_QSFP_TEMP",
    "PIM6_INPUT_VOLTAGE",
    "PIM6_POWER_VOLTAGE",
    "PIM6_CURRENT",
    "PIM6_POWER",
    "PIM6_XP3R3V",
    "PIM6_XP3R3V_EARLY",
    "PIM6_XP2R5V_EARLY",
    "PIM6_TXDRV_PHY",
    "PIM6_XP0R8V_PHY",
    "PIM6_XP1R1V_EARLY",
    "PIM6_DVDD_PHY4",
    "PIM6_DVDD_PHY3",
    "PIM6_DVDD_PHY2",
    "PIM6_DVDD_PHY1",
    "PIM6_XP1R8V_EARLY",
    "PIM6_XP1R8V_PHYIO",
    "PIM6_XP1R8V_PHYAVDD",
    "PIM6_MP2975_INPUT_VOLTAGE",
    "PIM6_MP2975_OUTPUT_VOL_XP0R8V",
    "PIM6_MP2975_OUTPUT_CURR_XP0R8V",
    "PIM6_MP2975_OUTPUT_VOL_XP3R3V",
    "PIM6_MP2975_OUTPUT_CURR_XP3R3V",
]

PIM6_SENSORS_16O = [
    "PIM6_LM75_4A",
    "PIM6_LM75_U27_TEMP_FRONT",
    "PIM6_LM75_U28_TEMP_REAR",
    "PIM6_QSFP_TEMP",
    "PIM6_INPUT_VOLTAGE",
    "PIM6_POWER_VOLTAGE",
    "PIM6_CURRENT",
    "PIM6_POWER",
    "PIM6_XP3R3V",
    "PIM6_XP2R5V",
    "PIM6_XP1R1V",
    "PIM6_XP1R8V",
    "PIM6_XP3R3V_OBO",
    "PIM6_XP8R0V_OBO",
    "PIM6_XP0R65V_OBO",
    "PIM6_XP0R94V_OBO",
    "PIM6_XP1R15V_OBO",
    "PIM6_XP1R8V_OBO",
    "PIM6_XP2R0V_OBO",
    "PIM6_XP3R6V_OBO",
    "PIM6_UCD90160_VOLT13",
    "PIM6_MP2975_INPUT_VOLTAGE",
    "PIM6_MP2975_OUTPUT_VOL_XP0R8V",
    "PIM6_MP2975_OUTPUT_CURR_XP0R8V",
    "PIM6_MP2975_OUTPUT_VOL_XP3R3V",
    "PIM6_MP2975_OUTPUT_CURR_XP3R3V",
]


PIM7_SENSORS_16Q = [
    "PIM7_LM75_U37_TEMP_BASE",
    "PIM7_LM75_U26_TEMP",
    "PIM7_LM75_U37_TEMP_MEZZ",
    "PIM7_QSFP_TEMP",
    "PIM7_INPUT_VOLTAGE",
    "PIM7_POWER_VOLTAGE",
    "PIM7_CURRENT",
    "PIM7_POWER",
    "PIM7_XP3R3V",
    "PIM7_XP3R3V_EARLY",
    "PIM7_XP2R5V_EARLY",
    "PIM7_TXDRV_PHY",
    "PIM7_XP0R8V_PHY",
    "PIM7_XP1R1V_EARLY",
    "PIM7_DVDD_PHY4",
    "PIM7_DVDD_PHY3",
    "PIM7_DVDD_PHY2",
    "PIM7_DVDD_PHY1",
    "PIM7_XP1R8V_EARLY",
    "PIM7_XP1R8V_PHYIO",
    "PIM7_XP1R8V_PHYAVDD",
    "PIM7_MP2975_INPUT_VOLTAGE",
    "PIM7_MP2975_OUTPUT_VOL_XP0R8V",
    "PIM7_MP2975_OUTPUT_CURR_XP0R8V",
    "PIM7_MP2975_OUTPUT_VOL_XP3R3V",
    "PIM7_MP2975_OUTPUT_CURR_XP3R3V",
]

PIM7_SENSORS_16O = [
    "PIM7_LM75_4A",
    "PIM7_LM75_U27_TEMP_FRONT",
    "PIM7_LM75_U28_TEMP_REAR",
    "PIM7_QSFP_TEMP",
    "PIM7_INPUT_VOLTAGE",
    "PIM7_POWER_VOLTAGE",
    "PIM7_CURRENT",
    "PIM7_POWER",
    "PIM7_XP3R3V",
    "PIM7_XP2R5V",
    "PIM7_XP1R1V",
    "PIM7_XP1R8V",
    "PIM7_XP3R3V_OBO",
    "PIM7_XP8R0V_OBO",
    "PIM7_XP0R65V_OBO",
    "PIM7_XP0R94V_OBO",
    "PIM7_XP1R15V_OBO",
    "PIM7_XP1R8V_OBO",
    "PIM7_XP2R0V_OBO",
    "PIM7_XP3R6V_OBO",
    "PIM7_UCD90160_VOLT13",
    "PIM7_MP2975_INPUT_VOLTAGE",
    "PIM7_MP2975_OUTPUT_VOL_XP0R8V",
    "PIM7_MP2975_OUTPUT_CURR_XP0R8V",
    "PIM7_MP2975_OUTPUT_VOL_XP3R3V",
    "PIM7_MP2975_OUTPUT_CURR_XP3R3V",
]


PIM8_SENSORS_16Q = [
    "PIM8_LM75_U37_TEMP_BASE",
    "PIM8_LM75_U26_TEMP",
    "PIM8_LM75_U37_TEMP_MEZZ",
    "PIM8_QSFP_TEMP",
    "PIM8_INPUT_VOLTAGE",
    "PIM8_POWER_VOLTAGE",
    "PIM8_CURRENT",
    "PIM8_POWER",
    "PIM8_XP3R3V",
    "PIM8_XP3R3V_EARLY",
    "PIM8_XP2R5V_EARLY",
    "PIM8_TXDRV_PHY",
    "PIM8_XP0R8V_PHY",
    "PIM8_XP1R1V_EARLY",
    "PIM8_DVDD_PHY4",
    "PIM8_DVDD_PHY3",
    "PIM8_DVDD_PHY2",
    "PIM8_DVDD_PHY1",
    "PIM8_XP1R8V_EARLY",
    "PIM8_XP1R8V_PHYIO",
    "PIM8_XP1R8V_PHYAVDD",
    "PIM8_MP2975_INPUT_VOLTAGE",
    "PIM8_MP2975_OUTPUT_VOL_XP0R8V",
    "PIM8_MP2975_OUTPUT_CURR_XP0R8V",
    "PIM8_MP2975_OUTPUT_VOL_XP3R3V",
    "PIM8_MP2975_OUTPUT_CURR_XP3R3V",
]

PIM8_SENSORS_16O = [
    "PIM8_LM75_4A",
    "PIM8_LM75_U27_TEMP_FRONT",
    "PIM8_LM75_U28_TEMP_REAR",
    "PIM8_QSFP_TEMP",
    "PIM8_INPUT_VOLTAGE",
    "PIM8_POWER_VOLTAGE",
    "PIM8_CURRENT",
    "PIM8_POWER",
    "PIM8_XP3R3V",
    "PIM8_XP2R5V",
    "PIM8_XP1R1V",
    "PIM8_XP1R8V",
    "PIM8_XP3R3V_OBO",
    "PIM8_XP8R0V_OBO",
    "PIM8_XP0R65V_OBO",
    "PIM8_XP0R94V_OBO",
    "PIM8_XP1R15V_OBO",
    "PIM8_XP1R8V_OBO",
    "PIM8_XP2R0V_OBO",
    "PIM8_XP3R6V_OBO",
    "PIM8_UCD90160_VOLT13",
    "PIM8_MP2975_INPUT_VOLTAGE",
    "PIM8_MP2975_OUTPUT_VOL_XP0R8V",
    "PIM8_MP2975_OUTPUT_CURR_XP0R8V",
    "PIM8_MP2975_OUTPUT_VOL_XP3R3V",
    "PIM8_MP2975_OUTPUT_CURR_XP3R3V",
]


PSU1_SENSORS = [
    "PSU1_IN_VOLT",
    "PSU1_12V_VOLT",
    "PSU1_STBY_VOLT",
    "PSU1_IN_CURR",
    "PSU1_12V_CURR",
    "PSU1_STBY_CURR",
    "PSU1_IN_POWER",
    "PSU1_12V_POWER",
    "PSU1_STBY_POWER",
    "PSU1_FAN_SPEED",
    "PSU1_TEMP1",
    "PSU1_TEMP2",
    "PSU1_TEMP3",
]

PSU2_SENSORS = [
    "PSU2_IN_VOLT",
    "PSU2_12V_VOLT",
    "PSU2_STBY_VOLT",
    "PSU2_IN_CURR",
    "PSU2_12V_CURR",
    "PSU2_STBY_CURR",
    "PSU2_IN_POWER",
    "PSU2_12V_POWER",
    "PSU2_STBY_POWER",
    "PSU2_FAN_SPEED",
    "PSU2_TEMP1",
    "PSU2_TEMP2",
    "PSU2_TEMP3",
]

PSU3_SENSORS = [
    "PSU3_IN_VOLT",
    "PSU3_12V_VOLT",
    "PSU3_STBY_VOLT",
    "PSU3_IN_CURR",
    "PSU3_12V_CURR",
    "PSU3_STBY_CURR",
    "PSU3_IN_POWER",
    "PSU3_12V_POWER",
    "PSU3_STBY_POWER",
    "PSU3_FAN_SPEED",
    "PSU3_TEMP1",
    "PSU3_TEMP2",
    "PSU3_TEMP3",
]

PSU4_SENSORS = [
    "PSU4_IN_VOLT",
    "PSU4_12V_VOLT",
    "PSU4_STBY_VOLT",
    "PSU4_IN_CURR",
    "PSU4_12V_CURR",
    "PSU4_STBY_CURR",
    "PSU4_IN_POWER",
    "PSU4_12V_POWER",
    "PSU4_STBY_POWER",
    "PSU4_FAN_SPEED",
    "PSU4_TEMP1",
    "PSU4_TEMP2",
    "PSU4_TEMP3",
]

SMB_SENSORS = [
    "SMB_XP3R3V_BMC",
    "SMB_XP2R5V_BMC",
    "SMB_XP1R8V_BMC",
    "SMB_XP1R2V_BMC",
    "SMB_XP1R0V_FPGA",
    "SMB_XP3R3V_USB",
    "SMB_XP5R0V",
    "SMB_XP3R3V_EARLY",
    "SMB_LM57_VTEMP",
    "SMB_XP1R8",
    "SMB_XP1R2",
    "SMB_VDDC_SW",
    "SMB_XP3R3V",
    "SMB_XP1R8V_AVDD",
    "SMB_XP1R2V_TVDD",
    "SMB_XP0R75V_1_PVDD",
    "SMB_XP0R75V_2_PVDD",
    "SMB_XP0R75V_3_PVDD",
    "SMB_VDD_PCIE",
    "SMB_XP0R84V_DCSU",
    "SMB_XP0R84V_CSU",
    "SMB_XP1R8V_CSU",
    "SMB_XP3R3V_TCXO",
    "SMB_OUTPUT_VOLTAGE_XP0R75V_1",
    "SMB_OUTPUT_CURRENT_XP0R75V_1",
    "SMB_INPUT_VOLTAGE_1",
    "SMB_OUTPUT_VOLTAGE_XP1R2V",
    "SMB_OUTPUT_CURRENT_XP1R2V",
    "SMB_OUTPUT_VOLTAGE_XP0R75V_2",
    "SMB_OUTPUT_CURRENT_XP0R75V_2",
    "SMB_INPUT_VOLTAGE_2",
    "SIM_LM75_U1_TEMP",
    "SMB_LM75B_U51_1_TEMP",
    "SMB_LM75B_U57_TEMP",
    "SMB_LM75B_U39_TEMP",
    "SMB_VDDC_SW_TEMP",
    "SMB_XP12R0V_VDDC_SW_IN",
    "SMB_VDDC_SW_IN_SENS",
    "SMB_VDDC_SW_POWER_IN",
    "SMB_VDDC_SW_POWER_OUT",
    "SMB_VDDC_SW_CURR_IN",
    "SMB_VDDC_SW_CURR_OUT",
    "PDB_L_TMP75_U2_TEMP",
    "PDB_L_TMP75_U3_TEMP",
    "PDB_R_TMP75_U2_TEMP",
    "PDB_R_TMP75_U3_TEMP",
    "FCB_FCM1_TMP75_U1_TEMP",
    "FCB_FCM1_TMP75_U2_TEMP",
    "FCB_FCM2_TMP75_U1_TEMP",
    "FCB_FCM2_TMP75_U2_TEMP",
    "FCM-T_CHIP_INPUT_VOLTAGE",
    "FCM-T_POWER_CURRENT",
    "FCM-T_POWER_VOLTAGE",
    "FCM-B_CHIP_INPUT_VOLTAGE",
    "FCM-B_POWER_CURRENT",
    "FCM-B_POWER_VOLTAGE",
    "FAN1_FRONT_SPEED",
    "FAN1_REAR_SPEED",
    "FAN2_FRONT_SPEED",
    "FAN2_REAR_SPEED",
    "FAN3_FRONT_SPEED",
    "FAN3_REAR_SPEED",
    "FAN4_FRONT_SPEED",
    "FAN4_REAR_SPEED",
    "FAN5_FRONT_SPEED",
    "FAN5_REAR_SPEED",
    "FAN6_FRONT_SPEED",
    "FAN6_REAR_SPEED",
    "FAN7_FRONT_SPEED",
    "FAN7_REAR_SPEED",
    "FAN8_FRONT_SPEED",
    "FAN8_REAR_SPEED",
]
