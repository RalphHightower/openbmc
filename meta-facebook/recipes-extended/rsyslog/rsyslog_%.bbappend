FILESEXTRAPATHS:prepend:openbmc-fb := "${THISDIR}/files:"

SRC_URI:append:openbmc-fb = "\
    file://rsyslog.conf \
    file://rotate_emmc \
    file://rotate_logfile \
    file://rotate_cri_sel \
    file://rotate_console_log \
    file://rsyslog.logrotate \
    file://rsyslog-emmc.conf \
    file://rsyslog-mterm.conf \
    file://rsyslog-remote.conf \
    "

MTERM_LOG_FILES ?= "mTerm_${MACHINE}"

do_install:append:openbmc-fb() {
  dst="${D}/usr/local/fbpackages/rotate"
  rsysconf="${D}${sysconfdir}/rsyslog.d"
  install -d $dst
  install -d ${rsysconf}
  install -m 755 ${UNPACKDIR}/rotate_logfile ${dst}/logfile
  install -m 755 ${UNPACKDIR}/rotate_cri_sel ${dst}/cri_sel
  install -m 755 ${UNPACKDIR}/rotate_console_log ${dst}/console_log

  install -m 644 ${UNPACKDIR}/rsyslog.conf ${D}${sysconfdir}/rsyslog.conf
  sed -i "s/__OPENBMC_VERSION__/${OPENBMC_VERSION}/g" ${D}${sysconfdir}/rsyslog.conf

  install -m 644 ${UNPACKDIR}/rsyslog-remote.conf ${rsysconf}/remote.conf

  for mterm_logfile in ${MTERM_LOG_FILES}; do
    conf=${rsysconf}/$mterm_logfile.conf
    install -m 644 ${UNPACKDIR}/rsyslog-mterm.conf ${conf}
    sed -i "s/__MTERM_LOG_FILE__/${mterm_logfile}/g;" ${conf}
  done

  if ! echo ${MACHINE_FEATURES} | awk "/emmc/ {exit 1}"; then
    install -m 644 ${UNPACKDIR}/rsyslog-emmc.conf ${rsysconf}/emmc.conf
    install -m 644 ${UNPACKDIR}/rotate_emmc ${D}${sysconfdir}/logrotate.d/emmc
  fi

  # Replaces the syslog or logrotate.rsyslog file from the package with our
  # custom config (filename depends on upstream package).
  rm -f ${D}${sysconfdir}/logrotate.d/logrotate.rsyslog
  install -m 644 ${UNPACKDIR}/rsyslog.logrotate ${D}${sysconfdir}/logrotate.d/syslog
}

FILES:${PN} += "/usr/local/fbpackages/rotate"
