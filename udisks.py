from __future__ import annotations

from typing import Any, Dict, List, Tuple

from sdbus import (
    DbusDeprecatedFlag,
    DbusInterfaceCommonAsync,
    DbusNoReplyFlag,
    DbusPropertyConstFlag,
    DbusPropertyEmitsChangeFlag,
    DbusPropertyEmitsInvalidationFlag,
    DbusPropertyExplicitFlag,
    DbusUnprivilegedFlag,
    dbus_method_async,
    dbus_property_async,
    dbus_signal_async,
)


class OrgFreedesktopUDisks2ManagerInterface(
    DbusInterfaceCommonAsync,
    interface_name="org.freedesktop.UDisks2.Manager",
):
    @dbus_method_async(
        input_signature="s",
        result_signature="(bs)",
    )
    async def can_format(
        self,
        type: str,
    ) -> Tuple[bool, str]:
        raise NotImplementedError

    @dbus_method_async(
        input_signature="s",
        result_signature="(bts)",
    )
    async def can_resize(
        self,
        type: str,
    ) -> Tuple[bool, int, str]:
        raise NotImplementedError

    @dbus_method_async(
        input_signature="s",
        result_signature="(bs)",
    )
    async def can_check(
        self,
        type: str,
    ) -> Tuple[bool, str]:
        raise NotImplementedError

    @dbus_method_async(
        input_signature="s",
        result_signature="(bs)",
    )
    async def can_repair(
        self,
        type: str,
    ) -> Tuple[bool, str]:
        raise NotImplementedError

    @dbus_method_async(
        input_signature="ha{sv}",
        result_signature="o",
    )
    async def loop_setup(
        self,
        fd: int,
        options: Dict[str, Tuple[str, Any]],
    ) -> str:
        raise NotImplementedError

    @dbus_method_async(
        input_signature="aossta{sv}",
        result_signature="o",
    )
    async def mdraid_create(
        self,
        blocks: List[str],
        level: str,
        name: str,
        chunk: int,
        options: Dict[str, Tuple[str, Any]],
    ) -> str:
        raise NotImplementedError

    @dbus_method_async(
        input_signature="b",
        flags=DbusDeprecatedFlag,
    )
    async def enable_modules(
        self,
        enable: bool,
    ) -> None:
        raise NotImplementedError

    @dbus_method_async(
        input_signature="sb",
    )
    async def enable_module(
        self,
        name: str,
        enable: bool,
    ) -> None:
        raise NotImplementedError

    @dbus_method_async(
        input_signature="a{sv}",
        result_signature="ao",
    )
    async def get_block_devices(
        self,
        options: Dict[str, Tuple[str, Any]],
    ) -> List[str]:
        raise NotImplementedError

    @dbus_method_async(
        input_signature="a{sv}a{sv}",
        result_signature="ao",
    )
    async def resolve_device(
        self,
        devspec: Dict[str, Tuple[str, Any]],
        options: Dict[str, Tuple[str, Any]],
    ) -> List[str]:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="s",
    )
    def version(self) -> str:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="as",
    )
    def supported_filesystems(self) -> List[str]:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="as",
    )
    def supported_encryption_types(self) -> List[str]:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="s",
    )
    def default_encryption_type(self) -> str:
        raise NotImplementedError


class OrgFreedesktopUDisks2ManagerNVMeInterface(
    DbusInterfaceCommonAsync,
    interface_name="org.freedesktop.UDisks2.Manager.NVMe",
):
    @dbus_method_async(
        input_signature="aya{sv}",
    )
    async def set_host_nqn(
        self,
        hostnqn: bytes,
        options: Dict[str, Tuple[str, Any]],
    ) -> None:
        raise NotImplementedError

    @dbus_method_async(
        input_signature="aya{sv}",
    )
    async def set_host_id(
        self,
        hostid: bytes,
        options: Dict[str, Tuple[str, Any]],
    ) -> None:
        raise NotImplementedError

    @dbus_method_async(
        input_signature="ayssa{sv}",
        result_signature="o",
    )
    async def connect(
        self,
        subsysnqn: bytes,
        transport: str,
        transport_addr: str,
        options: Dict[str, Tuple[str, Any]],
    ) -> str:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="ay",
    )
    def host_nqn(self) -> bytes:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="ay",
    )
    def host_id(self) -> bytes:
        raise NotImplementedError


class OrgFreedesktopUDisks2DriveInterface(
    DbusInterfaceCommonAsync,
    interface_name="org.freedesktop.UDisks2.Drive",
):
    @dbus_method_async(
        input_signature="a{sv}",
    )
    async def eject(
        self,
        options: Dict[str, Tuple[str, Any]],
    ) -> None:
        raise NotImplementedError

    @dbus_method_async(
        input_signature="a{sv}a{sv}",
    )
    async def set_configuration(
        self,
        value: Dict[str, Tuple[str, Any]],
        options: Dict[str, Tuple[str, Any]],
    ) -> None:
        raise NotImplementedError

    @dbus_method_async(
        input_signature="a{sv}",
    )
    async def power_off(
        self,
        options: Dict[str, Tuple[str, Any]],
    ) -> None:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="s",
    )
    def vendor(self) -> str:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="s",
    )
    def model(self) -> str:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="s",
    )
    def revision(self) -> str:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="s",
    )
    def serial(self) -> str:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="s",
    )
    def wwn(self) -> str:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="s",
    )
    def id(self) -> str:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="a{sv}",
    )
    def configuration(self) -> Dict[str, Tuple[str, Any]]:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="s",
    )
    def media(self) -> str:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="as",
    )
    def media_compatibility(self) -> List[str]:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="b",
    )
    def media_removable(self) -> bool:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="b",
    )
    def media_available(self) -> bool:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="b",
    )
    def media_change_detected(self) -> bool:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="t",
    )
    def size(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="t",
    )
    def time_detected(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="t",
    )
    def time_media_detected(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="b",
    )
    def optical(self) -> bool:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="b",
    )
    def optical_blank(self) -> bool:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="u",
    )
    def optical_num_tracks(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="u",
    )
    def optical_num_audio_tracks(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="u",
    )
    def optical_num_data_tracks(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="u",
    )
    def optical_num_sessions(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="i",
    )
    def rotation_rate(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="s",
    )
    def connection_bus(self) -> str:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="s",
    )
    def seat(self) -> str:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="b",
    )
    def removable(self) -> bool:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="b",
    )
    def ejectable(self) -> bool:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="s",
    )
    def sort_key(self) -> str:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="b",
    )
    def can_power_off(self) -> bool:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="s",
    )
    def sibling_id(self) -> str:
        raise NotImplementedError


class OrgFreedesktopUDisks2DriveAtaInterface(
    DbusInterfaceCommonAsync,
    interface_name="org.freedesktop.UDisks2.Drive.Ata",
):
    @dbus_method_async(
        input_signature="a{sv}",
    )
    async def smart_update(
        self,
        options: Dict[str, Tuple[str, Any]],
    ) -> None:
        raise NotImplementedError

    @dbus_method_async(
        input_signature="a{sv}",
        result_signature="a(ysqiiixia{sv})",
    )
    async def smart_get_attributes(
        self,
        options: Dict[str, Tuple[str, Any]],
    ) -> List[Tuple[int, str, int, int, int, int, int, int, Dict[str, Tuple[str, Any]]]]:
        raise NotImplementedError

    @dbus_method_async(
        input_signature="sa{sv}",
    )
    async def smart_selftest_start(
        self,
        type: str,
        options: Dict[str, Tuple[str, Any]],
    ) -> None:
        raise NotImplementedError

    @dbus_method_async(
        input_signature="a{sv}",
    )
    async def smart_selftest_abort(
        self,
        options: Dict[str, Tuple[str, Any]],
    ) -> None:
        raise NotImplementedError

    @dbus_method_async(
        input_signature="ba{sv}",
    )
    async def smart_set_enabled(
        self,
        value: bool,
        options: Dict[str, Tuple[str, Any]],
    ) -> None:
        raise NotImplementedError

    @dbus_method_async(
        input_signature="a{sv}",
        result_signature="y",
    )
    async def pm_get_state(
        self,
        options: Dict[str, Tuple[str, Any]],
    ) -> int:
        raise NotImplementedError

    @dbus_method_async(
        input_signature="a{sv}",
    )
    async def pm_standby(
        self,
        options: Dict[str, Tuple[str, Any]],
    ) -> None:
        raise NotImplementedError

    @dbus_method_async(
        input_signature="a{sv}",
    )
    async def pm_wakeup(
        self,
        options: Dict[str, Tuple[str, Any]],
    ) -> None:
        raise NotImplementedError

    @dbus_method_async(
        input_signature="a{sv}",
    )
    async def security_erase_unit(
        self,
        options: Dict[str, Tuple[str, Any]],
    ) -> None:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="b",
    )
    def smart_supported(self) -> bool:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="b",
    )
    def smart_enabled(self) -> bool:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="t",
    )
    def smart_updated(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="b",
    )
    def smart_failing(self) -> bool:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="t",
    )
    def smart_power_on_seconds(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="d",
    )
    def smart_temperature(self) -> float:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="i",
    )
    def smart_num_attributes_failing(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="i",
    )
    def smart_num_attributes_failed_in_the_past(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="x",
    )
    def smart_num_bad_sectors(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="s",
    )
    def smart_selftest_status(self) -> str:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="i",
    )
    def smart_selftest_percent_remaining(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="b",
    )
    def pm_supported(self) -> bool:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="b",
    )
    def pm_enabled(self) -> bool:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="b",
    )
    def apm_supported(self) -> bool:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="b",
    )
    def apm_enabled(self) -> bool:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="b",
    )
    def aam_supported(self) -> bool:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="b",
    )
    def aam_enabled(self) -> bool:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="i",
    )
    def aam_vendor_recommended_value(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="b",
    )
    def write_cache_supported(self) -> bool:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="b",
    )
    def write_cache_enabled(self) -> bool:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="b",
    )
    def read_lookahead_supported(self) -> bool:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="b",
    )
    def read_lookahead_enabled(self) -> bool:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="i",
    )
    def security_erase_unit_minutes(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="i",
    )
    def security_enhanced_erase_unit_minutes(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="b",
    )
    def security_frozen(self) -> bool:
        raise NotImplementedError


class OrgFreedesktopUDisks2NVMeControllerInterface(
    DbusInterfaceCommonAsync,
    interface_name="org.freedesktop.UDisks2.NVMe.Controller",
):
    @dbus_method_async(
        input_signature="a{sv}",
    )
    async def smart_update(
        self,
        options: Dict[str, Tuple[str, Any]],
    ) -> None:
        raise NotImplementedError

    @dbus_method_async(
        input_signature="a{sv}",
        result_signature="a{sv}",
    )
    async def smart_get_attributes(
        self,
        options: Dict[str, Tuple[str, Any]],
    ) -> Dict[str, Tuple[str, Any]]:
        raise NotImplementedError

    @dbus_method_async(
        input_signature="sa{sv}",
    )
    async def smart_selftest_start(
        self,
        type: str,
        options: Dict[str, Tuple[str, Any]],
    ) -> None:
        raise NotImplementedError

    @dbus_method_async(
        input_signature="a{sv}",
    )
    async def smart_selftest_abort(
        self,
        options: Dict[str, Tuple[str, Any]],
    ) -> None:
        raise NotImplementedError

    @dbus_method_async(
        input_signature="sa{sv}",
    )
    async def sanitize_start(
        self,
        action: str,
        options: Dict[str, Tuple[str, Any]],
    ) -> None:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="s",
    )
    def state(self) -> str:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="q",
    )
    def controller_id(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="ay",
    )
    def subsystem_nqn(self) -> bytes:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="s",
    )
    def fguid(self) -> str:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="s",
    )
    def nvme_revision(self) -> str:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="t",
    )
    def unallocated_capacity(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="t",
    )
    def smart_updated(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="as",
    )
    def smart_critical_warning(self) -> List[str]:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="t",
    )
    def smart_power_on_hours(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="q",
    )
    def smart_temperature(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="s",
    )
    def smart_selftest_status(self) -> str:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="i",
    )
    def smart_selftest_percent_remaining(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="s",
    )
    def sanitize_status(self) -> str:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="i",
    )
    def sanitize_percent_remaining(self) -> int:
        raise NotImplementedError


class OrgFreedesktopUDisks2NVMeNamespaceInterface(
    DbusInterfaceCommonAsync,
    interface_name="org.freedesktop.UDisks2.NVMe.Namespace",
):
    @dbus_method_async(
        input_signature="a{sv}",
    )
    async def format_namespace(
        self,
        options: Dict[str, Tuple[str, Any]],
    ) -> None:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="u",
    )
    def nsid(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="s",
    )
    def nguid(self) -> str:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="s",
    )
    def eui64(self) -> str:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="s",
    )
    def uuid(self) -> str:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="s",
    )
    def wwn(self) -> str:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="a(qqy)",
    )
    def lbaformats(self) -> List[Tuple[int, int, int]]:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="(qqy)",
    )
    def formatted_lbasize(self) -> Tuple[int, int, int]:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="t",
    )
    def namespace_size(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="t",
    )
    def namespace_capacity(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="t",
    )
    def namespace_utilization(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="i",
    )
    def format_percent_remaining(self) -> int:
        raise NotImplementedError


class OrgFreedesktopUDisks2NVMeFabricsInterface(
    DbusInterfaceCommonAsync,
    interface_name="org.freedesktop.UDisks2.NVMe.Fabrics",
):
    @dbus_method_async(
        input_signature="a{sv}",
    )
    async def disconnect(
        self,
        options: Dict[str, Tuple[str, Any]],
    ) -> None:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="ay",
    )
    def host_nqn(self) -> bytes:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="ay",
    )
    def host_id(self) -> bytes:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="s",
    )
    def transport(self) -> str:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="ay",
    )
    def transport_address(self) -> bytes:
        raise NotImplementedError


class OrgFreedesktopUDisks2BlockInterface(
    DbusInterfaceCommonAsync,
    interface_name="org.freedesktop.UDisks2.Block",
):
    @dbus_method_async(
        input_signature="(sa{sv})a{sv}",
    )
    async def add_configuration_item(
        self,
        item: Tuple[str, Dict[str, Tuple[str, Any]]],
        options: Dict[str, Tuple[str, Any]],
    ) -> None:
        raise NotImplementedError

    @dbus_method_async(
        input_signature="(sa{sv})a{sv}",
    )
    async def remove_configuration_item(
        self,
        item: Tuple[str, Dict[str, Tuple[str, Any]]],
        options: Dict[str, Tuple[str, Any]],
    ) -> None:
        raise NotImplementedError

    @dbus_method_async(
        input_signature="(sa{sv})(sa{sv})a{sv}",
    )
    async def update_configuration_item(
        self,
        old_item: Tuple[str, Dict[str, Tuple[str, Any]]],
        new_item: Tuple[str, Dict[str, Tuple[str, Any]]],
        options: Dict[str, Tuple[str, Any]],
    ) -> None:
        raise NotImplementedError

    @dbus_method_async(
        input_signature="a{sv}",
        result_signature="a(sa{sv})",
    )
    async def get_secret_configuration(
        self,
        options: Dict[str, Tuple[str, Any]],
    ) -> List[Tuple[str, Dict[str, Tuple[str, Any]]]]:
        raise NotImplementedError

    @dbus_method_async(
        input_signature="sa{sv}",
    )
    async def format(
        self,
        type: str,
        options: Dict[str, Tuple[str, Any]],
    ) -> None:
        raise NotImplementedError

    @dbus_method_async(
        input_signature="a{sv}",
        result_signature="h",
    )
    async def open_for_backup(
        self,
        options: Dict[str, Tuple[str, Any]],
    ) -> int:
        raise NotImplementedError

    @dbus_method_async(
        input_signature="a{sv}",
        result_signature="h",
    )
    async def open_for_restore(
        self,
        options: Dict[str, Tuple[str, Any]],
    ) -> int:
        raise NotImplementedError

    @dbus_method_async(
        input_signature="a{sv}",
        result_signature="h",
    )
    async def open_for_benchmark(
        self,
        options: Dict[str, Tuple[str, Any]],
    ) -> int:
        raise NotImplementedError

    @dbus_method_async(
        input_signature="sa{sv}",
        result_signature="h",
    )
    async def open_device(
        self,
        mode: str,
        options: Dict[str, Tuple[str, Any]],
    ) -> int:
        raise NotImplementedError

    @dbus_method_async(
        input_signature="a{sv}",
    )
    async def rescan(
        self,
        options: Dict[str, Tuple[str, Any]],
    ) -> None:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="ay",
    )
    def device(self) -> bytes:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="ay",
    )
    def preferred_device(self) -> bytes:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="aay",
    )
    def symlinks(self) -> List[bytes]:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="t",
    )
    def device_number(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="s",
    )
    def id(self) -> str:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="t",
    )
    def size(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="b",
    )
    def read_only(self) -> bool:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="o",
    )
    def drive(self) -> str:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="o",
    )
    def mdraid(self) -> str:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="o",
    )
    def mdraid_member(self) -> str:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="s",
    )
    def id_usage(self) -> str:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="s",
    )
    def id_type(self) -> str:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="s",
    )
    def id_version(self) -> str:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="s",
    )
    def id_label(self) -> str:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="s",
    )
    def id_uuid(self) -> str:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="a(sa{sv})",
    )
    def configuration(self) -> List[Tuple[str, Dict[str, Tuple[str, Any]]]]:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="o",
    )
    def crypto_backing_device(self) -> str:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="b",
    )
    def hint_partitionable(self) -> bool:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="b",
    )
    def hint_system(self) -> bool:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="b",
    )
    def hint_ignore(self) -> bool:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="b",
    )
    def hint_auto(self) -> bool:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="s",
    )
    def hint_name(self) -> str:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="s",
    )
    def hint_icon_name(self) -> str:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="s",
    )
    def hint_symbolic_icon_name(self) -> str:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="as",
    )
    def userspace_mount_options(self) -> List[str]:
        raise NotImplementedError


class OrgFreedesktopUDisks2PartitionTableInterface(
    DbusInterfaceCommonAsync,
    interface_name="org.freedesktop.UDisks2.PartitionTable",
):
    @dbus_method_async(
        input_signature="ttssa{sv}",
        result_signature="o",
    )
    async def create_partition(
        self,
        offset: int,
        size: int,
        type: str,
        name: str,
        options: Dict[str, Tuple[str, Any]],
    ) -> str:
        raise NotImplementedError

    @dbus_method_async(
        input_signature="ttssa{sv}sa{sv}",
        result_signature="o",
    )
    async def create_partition_and_format(
        self,
        offset: int,
        size: int,
        type: str,
        name: str,
        options: Dict[str, Tuple[str, Any]],
        format_type: str,
        format_options: Dict[str, Tuple[str, Any]],
    ) -> str:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="ao",
    )
    def partitions(self) -> List[str]:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="s",
    )
    def type(self) -> str:
        raise NotImplementedError


class OrgFreedesktopUDisks2PartitionInterface(
    DbusInterfaceCommonAsync,
    interface_name="org.freedesktop.UDisks2.Partition",
):
    @dbus_method_async(
        input_signature="sa{sv}",
    )
    async def set_type(
        self,
        type: str,
        options: Dict[str, Tuple[str, Any]],
    ) -> None:
        raise NotImplementedError

    @dbus_method_async(
        input_signature="sa{sv}",
    )
    async def set_name(
        self,
        name: str,
        options: Dict[str, Tuple[str, Any]],
    ) -> None:
        raise NotImplementedError

    @dbus_method_async(
        input_signature="sa{sv}",
    )
    async def set_uuid(
        self,
        uuid: str,
        options: Dict[str, Tuple[str, Any]],
    ) -> None:
        raise NotImplementedError

    @dbus_method_async(
        input_signature="ta{sv}",
    )
    async def set_flags(
        self,
        flags: int,
        options: Dict[str, Tuple[str, Any]],
    ) -> None:
        raise NotImplementedError

    @dbus_method_async(
        input_signature="ta{sv}",
    )
    async def resize(
        self,
        size: int,
        options: Dict[str, Tuple[str, Any]],
    ) -> None:
        raise NotImplementedError

    @dbus_method_async(
        input_signature="a{sv}",
    )
    async def delete(
        self,
        options: Dict[str, Tuple[str, Any]],
    ) -> None:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="u",
    )
    def number(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="s",
    )
    def type(self) -> str:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="t",
    )
    def flags(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="t",
    )
    def offset(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="t",
    )
    def size(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="s",
    )
    def name(self) -> str:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="s",
    )
    def uuid(self) -> str:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="o",
    )
    def table(self) -> str:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="b",
    )
    def is_container(self) -> bool:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="b",
    )
    def is_contained(self) -> bool:
        raise NotImplementedError


class OrgFreedesktopUDisks2FilesystemInterface(
    DbusInterfaceCommonAsync,
    interface_name="org.freedesktop.UDisks2.Filesystem",
):
    @dbus_method_async(
        input_signature="sa{sv}",
    )
    async def set_label(
        self,
        label: str,
        options: Dict[str, Tuple[str, Any]],
    ) -> None:
        raise NotImplementedError

    @dbus_method_async(
        input_signature="sa{sv}",
    )
    async def set_uuid(
        self,
        uuid: str,
        options: Dict[str, Tuple[str, Any]],
    ) -> None:
        raise NotImplementedError

    @dbus_method_async(
        input_signature="a{sv}",
        result_signature="s",
    )
    async def mount(
        self,
        options: Dict[str, Tuple[str, Any]],
    ) -> str:
        raise NotImplementedError

    @dbus_method_async(
        input_signature="a{sv}",
    )
    async def unmount(
        self,
        options: Dict[str, Tuple[str, Any]],
    ) -> None:
        raise NotImplementedError

    @dbus_method_async(
        input_signature="ta{sv}",
    )
    async def resize(
        self,
        size: int,
        options: Dict[str, Tuple[str, Any]],
    ) -> None:
        raise NotImplementedError

    @dbus_method_async(
        input_signature="a{sv}",
        result_signature="b",
    )
    async def check(
        self,
        options: Dict[str, Tuple[str, Any]],
    ) -> bool:
        raise NotImplementedError

    @dbus_method_async(
        input_signature="a{sv}",
        result_signature="b",
    )
    async def repair(
        self,
        options: Dict[str, Tuple[str, Any]],
    ) -> bool:
        raise NotImplementedError

    @dbus_method_async(
        input_signature="a{sv}",
    )
    async def take_ownership(
        self,
        options: Dict[str, Tuple[str, Any]],
    ) -> None:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="aay",
    )
    def mount_points(self) -> List[bytes]:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="t",
    )
    def size(self) -> int:
        raise NotImplementedError


class OrgFreedesktopUDisks2SwapspaceInterface(
    DbusInterfaceCommonAsync,
    interface_name="org.freedesktop.UDisks2.Swapspace",
):
    @dbus_method_async(
        input_signature="a{sv}",
    )
    async def start(
        self,
        options: Dict[str, Tuple[str, Any]],
    ) -> None:
        raise NotImplementedError

    @dbus_method_async(
        input_signature="a{sv}",
    )
    async def stop(
        self,
        options: Dict[str, Tuple[str, Any]],
    ) -> None:
        raise NotImplementedError

    @dbus_method_async(
        input_signature="sa{sv}",
    )
    async def set_label(
        self,
        label: str,
        options: Dict[str, Tuple[str, Any]],
    ) -> None:
        raise NotImplementedError

    @dbus_method_async(
        input_signature="sa{sv}",
    )
    async def set_uuid(
        self,
        uuid: str,
        options: Dict[str, Tuple[str, Any]],
    ) -> None:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="b",
    )
    def active(self) -> bool:
        raise NotImplementedError


class OrgFreedesktopUDisks2EncryptedInterface(
    DbusInterfaceCommonAsync,
    interface_name="org.freedesktop.UDisks2.Encrypted",
):
    @dbus_method_async(
        input_signature="sa{sv}",
        result_signature="o",
    )
    async def unlock(
        self,
        passphrase: str,
        options: Dict[str, Tuple[str, Any]],
    ) -> str:
        raise NotImplementedError

    @dbus_method_async(
        input_signature="a{sv}",
    )
    async def lock(
        self,
        options: Dict[str, Tuple[str, Any]],
    ) -> None:
        raise NotImplementedError

    @dbus_method_async(
        input_signature="ssa{sv}",
    )
    async def change_passphrase(
        self,
        passphrase: str,
        new_passphrase: str,
        options: Dict[str, Tuple[str, Any]],
    ) -> None:
        raise NotImplementedError

    @dbus_method_async(
        input_signature="ta{sv}",
    )
    async def resize(
        self,
        size: int,
        options: Dict[str, Tuple[str, Any]],
    ) -> None:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="a(sa{sv})",
    )
    def child_configuration(self) -> List[Tuple[str, Dict[str, Tuple[str, Any]]]]:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="s",
    )
    def hint_encryption_type(self) -> str:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="t",
    )
    def metadata_size(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="o",
    )
    def cleartext_device(self) -> str:
        raise NotImplementedError


class OrgFreedesktopUDisks2LoopInterface(
    DbusInterfaceCommonAsync,
    interface_name="org.freedesktop.UDisks2.Loop",
):
    @dbus_method_async(
        input_signature="a{sv}",
    )
    async def delete(
        self,
        options: Dict[str, Tuple[str, Any]],
    ) -> None:
        raise NotImplementedError

    @dbus_method_async(
        input_signature="ba{sv}",
    )
    async def set_autoclear(
        self,
        value: bool,
        options: Dict[str, Tuple[str, Any]],
    ) -> None:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="ay",
    )
    def backing_file(self) -> bytes:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="b",
    )
    def autoclear(self) -> bool:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="u",
    )
    def setup_by_uid(self) -> int:
        raise NotImplementedError


class OrgFreedesktopUDisks2MDRaidInterface(
    DbusInterfaceCommonAsync,
    interface_name="org.freedesktop.UDisks2.MDRaid",
):
    @dbus_method_async(
        input_signature="a{sv}",
    )
    async def start(
        self,
        options: Dict[str, Tuple[str, Any]],
    ) -> None:
        raise NotImplementedError

    @dbus_method_async(
        input_signature="a{sv}",
    )
    async def stop(
        self,
        options: Dict[str, Tuple[str, Any]],
    ) -> None:
        raise NotImplementedError

    @dbus_method_async(
        input_signature="oa{sv}",
    )
    async def remove_device(
        self,
        device: str,
        options: Dict[str, Tuple[str, Any]],
    ) -> None:
        raise NotImplementedError

    @dbus_method_async(
        input_signature="oa{sv}",
    )
    async def add_device(
        self,
        device: str,
        options: Dict[str, Tuple[str, Any]],
    ) -> None:
        raise NotImplementedError

    @dbus_method_async(
        input_signature="aya{sv}",
    )
    async def set_bitmap_location(
        self,
        value: bytes,
        options: Dict[str, Tuple[str, Any]],
    ) -> None:
        raise NotImplementedError

    @dbus_method_async(
        input_signature="sa{sv}",
    )
    async def request_sync_action(
        self,
        sync_action: str,
        options: Dict[str, Tuple[str, Any]],
    ) -> None:
        raise NotImplementedError

    @dbus_method_async(
        input_signature="a{sv}",
    )
    async def delete(
        self,
        options: Dict[str, Tuple[str, Any]],
    ) -> None:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="s",
    )
    def uuid(self) -> str:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="s",
    )
    def name(self) -> str:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="s",
    )
    def level(self) -> str:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="u",
    )
    def num_devices(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="t",
    )
    def size(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="s",
    )
    def sync_action(self) -> str:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="d",
    )
    def sync_completed(self) -> float:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="t",
    )
    def sync_rate(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="t",
    )
    def sync_remaining_time(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="u",
    )
    def degraded(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="ay",
    )
    def bitmap_location(self) -> bytes:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="t",
    )
    def chunk_size(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="a(oiasta{sv})",
    )
    def active_devices(self) -> List[Tuple[str, int, List[str], int, Dict[str, Tuple[str, Any]]]]:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="a(sa{sv})",
    )
    def child_configuration(self) -> List[Tuple[str, Dict[str, Tuple[str, Any]]]]:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="b",
    )
    def running(self) -> bool:
        raise NotImplementedError


class OrgFreedesktopUDisks2JobInterface(
    DbusInterfaceCommonAsync,
    interface_name="org.freedesktop.UDisks2.Job",
):
    @dbus_method_async(
        input_signature="a{sv}",
    )
    async def cancel(
        self,
        options: Dict[str, Tuple[str, Any]],
    ) -> None:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="s",
    )
    def operation(self) -> str:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="d",
    )
    def progress(self) -> float:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="b",
    )
    def progress_valid(self) -> bool:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="t",
    )
    def bytes(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="t",
    )
    def rate(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="t",
    )
    def start_time(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="t",
    )
    def expected_end_time(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="ao",
    )
    def objects(self) -> List[str]:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="u",
    )
    def started_by_uid(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="b",
    )
    def cancelable(self) -> bool:
        raise NotImplementedError

    @dbus_signal_async(
        signal_signature="bs",
    )
    def completed(self) -> Tuple[bool, str]:
        raise NotImplementedError
