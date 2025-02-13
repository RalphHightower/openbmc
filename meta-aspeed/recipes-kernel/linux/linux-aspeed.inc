DESCRIPTION = "Linux Kernel for Aspeed"
SECTION = "kernel"
LICENSE = "GPL-2.0-only"

COMPATIBLE_MACHINE = "aspeed"

do_compile[depends] = "libgcc:do_populate_sysroot"

inherit kernel

# linux-yocto.inc attempts to add kernel metadata, which we do not use.
# remove it to avoid the KERNEL_DANGLING_FEATURES warning.
KERNEL_FEATURES:remove = "cfg/fs/vfat.scc"

# Do not install kernel in rootfs
do_install[postfuncs] += "remove_kernel_image_from_rootfs"
remove_kernel_image_from_rootfs() {
    rm -rf ${D}/boot/${KERNEL_IMAGETYPE}*
}

pkg_postinst:kernel-image() {
}
