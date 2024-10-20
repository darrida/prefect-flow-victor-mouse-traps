"""Models module."""

from datetime import datetime
from typing import Any

from pydantic import BaseModel, Field


class Activity(BaseModel):  # pylint: disable=too-many-instance-attributes
    """Activity data class."""

    id: int  # pylint: disable=invalid-name
    url: str
    trap: str
    trap_name: str
    time_stamp: datetime
    time_stamp_unix: datetime
    sequence_number: int
    activity_type: int
    activity_type_text: str
    kills_present: int
    total_kills_reported: int
    battery_level: int
    wireless_network_rssi: int
    firmware_version_string: str
    temperature: int
    board_type: str
    error_code: int
    active: bool
    is_rat_kill: bool = Field(..., alias="isRatKill")
    sex_kill_detail: Any | None = Field(..., alias="sexKillDetail")
    age_kill_detail: Any | None = Field(..., alias="ageKillDetail")
    species_kill_detail: Any | None = Field(..., alias="speciesKillDetail")
    replaced_attractant: bool = Field(..., alias="replacedAttractant")
    replaced_battery: bool = Field(..., alias="replacedBattery")
    cleaned_trap: bool = Field(..., alias="cleanedTrap")
    note: Any | None = None
    site_id: Any | None = None
    building_id: Any | None = None
    floor_id: Any | None = None
    floor_plan_x: Any | None = None
    floor_plan_y: Any | None = None
    trap_type_text: str

    @property
    def temperature_celcius(self) -> float:
        """Get temperature in celcius."""
        return round(self.temperature / 20, 1)


class MobileApp(BaseModel):  # pylint: disable=too-many-instance-attributes
    """Mobile app data class."""

    url: str
    min_android_version: int
    ideal_android_version: int
    min_ios_version: str
    ideal_ios_version: str
    commercial_min_android_version: int
    commercial_ideal_android_version: int
    commercial_min_ios_version: str
    commercial_ideal_ios_version: str


class ProfileTermsAndConditions(BaseModel):
    """Profile terms- and condtions data class."""

    id: int  # pylint: disable=invalid-name
    time_stamp: datetime
    profile_id: int
    term_id: int
    terms_version: str


class Profile(BaseModel):  # pylint: disable=too-many-instance-attributes
    """Profile data class."""

    id: int  # pylint: disable=invalid-name
    url: str
    user: str
    name: str | None = None
    operator: str | None = None
    operator_name: str | None = None
    client: str | None = None
    client_name: str | None = None
    telephone_number: str | None = None
    phone_names: Any | None = Field(..., alias="phoneNames")
    phone_numbers: Any | None = Field(..., alias="phoneNumbers")
    email_addresses: Any | None = Field(..., alias="emailAddresses")
    email_notifications_enabled: bool
    notifications_enabled: bool
    terms_version: int
    notify_wifi_connection: bool
    notify_low_battery: bool
    notify_kill_alerts: bool
    notify_new_products: bool
    text_notifications_enabled: bool
    notify_empty_trap: bool
    fcm_tokens: Any | None = Field(..., alias="fcmTokens")
    apns_tokens: Any | None = Field(..., alias="apnsTokens")
    fcm_arns: Any | None = Field(..., alias="fcmARNs")
    apns_arns: Any | None = Field(..., alias="apnsARNs")
    fcm_tokens_pro: Any | None = Field(..., alias="fcmTokensPro")
    apns_tokens_pro: Any | None = Field(..., alias="apnsTokensPro")
    fcm_arns_pro: Any | None = Field(..., alias="fcmARNsPro")
    apns_arns_pro: Any | None = Field(..., alias="apnsARNsPro")
    favorite_sites: Any | None = None
    notify_false_trigger: bool
    accepted_terms_and_conditions: list[ProfileTermsAndConditions] | None = None


class User(BaseModel):  # pylint: disable=too-many-instance-attributes
    """User data class."""

    id: int  # pylint: disable=invalid-name
    url: str
    username: str
    password: str | None = None
    email: str
    groups: list[str]
    group_names: list[str]
    date_joined: datetime
    last_login: datetime
    first_name: str
    last_name: str
    profile: Profile


class OperatorTermsAndConditions(BaseModel):
    """Operator terms- and condtions data class."""

    id: int  # pylint: disable=invalid-name
    operator_id: int
    time_stamp: datetime
    terms_and_conditions: str
    terms_version: str


class Operator(BaseModel):  # pylint: disable=too-many-instance-attributes
    """Operator data class."""

    id: int  # pylint: disable=invalid-name
    url: str
    account_number: str
    name: str
    address: str
    type: int
    number_sites: int
    number_buildings: int
    number_traps: int
    terms_version: int
    terms: str
    contact: User
    terms_and_conditions: list[OperatorTermsAndConditions] | None = None


class TrapStatistics(BaseModel):  # pylint: disable=too-many-instance-attributes
    """Trap statistics data class."""

    id: int  # pylint: disable=invalid-name
    url: str
    trap: str
    trap_name: str
    kills_present: int
    install_date: datetime | None = None
    owner_name: str
    owner_email: str
    last_report_date: datetime
    last_kill_date: datetime | None = None
    temperature: int | None = None
    battery_level: int
    total_kills: int | None = None
    total_escapes: int | None = None
    rx_power_level: int
    firmware_version: str
    trap_provisioned: bool
    last_sequence_number: int | None = None
    total_retreats: int | None = None
    wireless_network_rssi: int
    error_code: int
    send_conn_lost_nt: bool
    send_empty_trap_nt: bool
    board_type: str
    last_maintenance_date: str | datetime
    bait_level: Any | None = None
    current_bait: Any | None = None
    last_bait_quantity: int | None = None

    @property
    def temperature_celcius(self) -> float | None:
        """Get temperature in celcius."""
        return round(self.temperature / 20, 1) if self.temperature else None


class Trap(BaseModel):  # pylint: disable=too-many-instance-attributes
    """Trap data class."""

    id: int  # pylint: disable=invalid-name
    url: str
    corruption_status: int
    corruption_status_options: list[tuple[int, str]] | None = None
    operator: str | None = None
    operator_name: str | None = None
    name: str
    ssid: str
    serial_number: str
    auto_upgrade: bool
    status: int
    location: str | None = None
    lat: float | None = None
    long: float | None = None
    upgrade_firmware: str | None = None
    commercial_gateway: str | None = None
    commercial_monitor_mode_enabled: bool
    lorawan_app_key: str
    site_name: str | None = None
    floor_plan_x: int | None = None
    floor_plan_y: int | None = None
    building_name: str | None = None
    floor_name: str | None = None
    room: str | None = None
    room_name: str | None = None
    trap_type: int
    trap_type_verbose: str
    alerts: int
    trapstatistics: TrapStatistics

    @property
    def corruption_status_verbose(self) -> str | None:
        """Get description of corruption_status code."""
        if self.corruption_status_options:
            return next(
                item[1]
                for item in self.corruption_status_options
                if item[0] == self.corruption_status
            )
        return None
