#include "fw-util.h"
#include <cstdio>
#include <cstring>
#include "server.h"
#include <openbmc/pal.h>
#include <facebook/bic.h>
#include <syslog.h>

using namespace std;

class VrComponent : public Component {
  uint8_t slot_id = 0;
  Server server;
  public:
  VrComponent(const string& fru, const string& comp, uint8_t _slot_id)
    : Component(fru, comp), slot_id(_slot_id), server(_slot_id, fru) {}
  int print_version() {
    uint8_t ver[32] = {0};
#if defined(CONFIG_FBY2_RC) || defined(CONFIG_FBY2_EP)
    int ret;
    uint8_t server_type = 0xFF;
    ret = minilaketb_get_server_type(slot_id, &server_type);
    if (ret) {
      syslog(LOG_ERR, "%s, Get server type failed\n", __func__);
    }
    switch (server_type) {
      case SERVER_TYPE_RC:
        try {
          server.ready();
          // Print VDD_APC_CBF VR Version
          if (bic_get_fw_ver(slot_id, FW_VDD_APC_CBF_VR, ver)){
            printf("VDD_APC_CBF VR Version: NA\n");
          }
          else {
            printf("VDD_APC_CBF VR Version: 0x%02x%02x%02x%02x%02x\n", ver[0], ver[1], ver[2], ver[3], ver[4]);
          }

          // Print DDR510 VR Version Version
          if (bic_get_fw_ver(slot_id, FW_DDR510_VR, ver)){
            printf("DDR510 VR Version: NA\n");
          }
          else {
            printf("DDR510 VR Version: 0x%02x%02x%02x%02x%02x\n", ver[0], ver[1], ver[2], ver[3], ver[4]);
          }

          // Print DDR423 VR Version Version
          if (bic_get_fw_ver(slot_id, FW_DDR423_VR, ver)){
            printf("DDR423 VR Version: NA\n");
          }
          else {
            printf("DDR423 VR Version: 0x%02x%02x%02x%02x%02x\n", ver[0], ver[1], ver[2], ver[3], ver[4]);
          }
        } catch (string err) {
            printf("VDD_APC_CBF VR Version: NA (%s)\n", err.c_str());
            printf("DDR510 VR Version: NA (%s)\n", err.c_str());
            printf("DDR423 VR Version: NA (%s)\n", err.c_str());
        }
        break;

      case SERVER_TYPE_EP:
        try {
          server.ready();
          // Print VDD_CORE VR Version
          if (bic_get_fw_ver(slot_id, FW_VDD_CORE_VR, ver)) {
            printf("VDD_CORE VR Version: NA\n");
          }
          else {
            printf("VDD_CORE VR Version: 0x%02x%02x, 0x%02x%02x\n", ver[0], ver[1], ver[2], ver[3]);
          }

          // Print VDD_SRAM VR Version
          if (bic_get_fw_ver(slot_id, FW_VDD_SRAM_VR, ver)) {
            printf("VDD_SRAM VR Version: NA\n");
          }
          else {
            printf("VDD_SRAM VR Version: 0x%02x%02x, 0x%02x%02x\n", ver[0], ver[1], ver[2], ver[3]);
          }

          // Print VDD_MEM VR Version
          if (bic_get_fw_ver(slot_id, FW_VDD_MEM_VR, ver)) {
            printf("VDD_MEM VR Version: NA\n");
          }
          else {
            printf("VDD_MEM VR Version: 0x%02x%02x, 0x%02x%02x\n", ver[0], ver[1], ver[2], ver[3]);
          }

          // Print VDD_SOC VR Version
          if (bic_get_fw_ver(slot_id, FW_VDD_SOC_VR, ver)) {
            printf("VDD_SOC VR Version: NA\n");
          }
          else {
            printf("VDD_SOC VR Version: 0x%02x%02x, 0x%02x%02x\n", ver[0], ver[1], ver[2], ver[3]);
          }

          // Print DDR_AG VR Version
          if (bic_get_fw_ver(slot_id, FW_DDR_AG_VR, ver)) {
            printf("DDR_AG VR Version: NA\n");
          }
          else {
            printf("DDR_AG VR Version: 0x%02x%02x, 0x%02x%02x\n", ver[0], ver[1], ver[2], ver[3]);
          }

          // Print DDR_BH VR Version
          if (bic_get_fw_ver(slot_id, FW_DDR_BH_VR, ver)) {
            printf("DDR_BH VR Version: NA\n");
          }
          else {
            printf("DDR_BH VR Version: 0x%02x%02x, 0x%02x%02x\n", ver[0], ver[1], ver[2], ver[3]);
          }
        } catch (string err) {
            printf("VDD_CORE VR Version: NA (%s)\n", err.c_str());
            printf("VDD_SRAM VR Version: NA (%s)\n", err.c_str());
            printf("VDD_MEM VR Version: NA (%s)\n", err.c_str());
            printf("VDD_SOC VR Version: NA (%s)\n", err.c_str());
            printf("DDR_AG VR Version: NA (%s)\n", err.c_str());
            printf("DDR_BH VR Version: NA (%s)\n", err.c_str());
        }
        break;

      case SERVER_TYPE_TL:
      default:
        try {
          server.ready();

          // Print PVCCIN VR Version
          if (bic_get_fw_ver(slot_id, FW_PVCCIN_VR, ver)) {
            printf("PVCCIN VR Version: NA\n");
          }
          else {
            printf("PVCCIN VR Version: 0x%02x%02x, 0x%02x%02x\n", ver[0], ver[1], ver[2], ver[3]);
          }

          // Print DDRAB VR Version
          if (bic_get_fw_ver(slot_id, FW_DDRAB_VR, ver)) {
            printf("DDRAB VR Version: NA\n");
          }
          else {
            printf("DDRAB VR Version: 0x%02x%02x, 0x%02x%02x\n", ver[0], ver[1], ver[2], ver[3]);
          }


          // Print P1V05 VR Version
          if (bic_get_fw_ver(slot_id, FW_P1V05_VR, ver)) {
            printf("P1V05 VR Version: NA\n");
          }
          else {
            printf("P1V05 VR Version: 0x%02x%02x, 0x%02x%02x\n", ver[0], ver[1], ver[2], ver[3]);
          }
        } catch (string err) {
            printf("PVCCIO VR Version: NA (%s)\n", err.c_str());
            printf("PVCCIN VR Version: NA (%s)\n", err.c_str());
            printf("DDRAB VR Version: NA (%s)\n", err.c_str());
            printf("PVNNPCH VR Version: NA (%s)\n", err.c_str());
            printf("P1V05 VR Version: NA (%s)\n", err.c_str());
        }
        break;
    }
#else
    try {
      server.ready();

      // Print PVCCIN VR Version
      if (bic_get_fw_ver(slot_id, FW_PVCCIN_VR, ver)){
        printf("PVCCIN VR Version: NA\n");
      }
      else {
        printf("PVCCIN VR Version: 0x%02x%02x, 0x%02x%02x\n", ver[0], ver[1], ver[2], ver[3]);
      }

      // Print DDRAB VR Version
      if (bic_get_fw_ver(slot_id, FW_DDRAB_VR, ver)){
        printf("DDRAB VR Version: NA\n");
      }
      else {
        printf("DDRAB VR Version: 0x%02x%02x, 0x%02x%02x\n", ver[0], ver[1], ver[2], ver[3]);
      }

      // Print P1V05 VR Version
      if (bic_get_fw_ver(slot_id, FW_P1V05_VR, ver)){
        printf("P1V05 VR Version: NA\n");
      }
      else {
        printf("P1V05 VR Version: 0x%02x%02x, 0x%02x%02x\n", ver[0], ver[1], ver[2], ver[3]);
      }
    } catch (string err) {
        printf("PVCCIN VR Version: NA (%s)\n", err.c_str());
        printf("DDRAB VR Version: NA (%s)\n", err.c_str());
        printf("PVNNPCH VR Version: NA (%s)\n", err.c_str());
        printf("P1V05 VR Version: NA (%s)\n", err.c_str());
    }
#endif
    return 0;
  }

  int update(const string& image) {
    int ret;
    try {
      server.ready();
      ret = bic_update_fw(slot_id, UPDATE_VR, (char *)image.c_str());
    } catch(string err) {
      ret = FW_STATUS_NOT_SUPPORTED;
    }
    return ret;
  }
};

VrComponent vr1("slot1", "vr", 1);
