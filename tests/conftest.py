from datetime import timedelta
from unittest import mock

import pytest

from custom_components.vaillantcloud.coordinator import (
    SystemCoordinator,
    DailyDataCoordinator,
)
from myVaillant.api import MyVaillantAPI
from myVaillant.const import DEFAULT_BRAND
from myVaillant.models import Circuit, DomesticHotWater, System, Zone
from myVaillant.tests.utils import _mocked_api, _myvaillant_aioresponses
from polyfactory.factories import DataclassFactory

from custom_components.vaillantcloud.const import (
    DEFAULT_COUNTRY,
    DOMAIN,
    OPTION_BRAND,
    OPTION_COUNTRY,
    OPTION_REFRESH_DELAY,
    OPTION_UPDATE_INTERVAL,
    OPTION_FETCH_RTS,
    OPTION_FETCH_MPC,
)

TEST_OPTIONS = {
    OPTION_COUNTRY: DEFAULT_COUNTRY,
    OPTION_BRAND: DEFAULT_BRAND,
    OPTION_REFRESH_DELAY: 0,
    OPTION_UPDATE_INTERVAL: 1,
    OPTION_FETCH_RTS: True,
    OPTION_FETCH_MPC: True,
}


class AsyncMock(mock.MagicMock):
    async def __call__(self, *args, **kwargs):
        return super().__call__(*args, **kwargs)


@pytest.fixture(scope="session", autouse=True)
def asyncio_sleep_mock():
    """
    Disable sleep in asyncio to avoid delays in test execution
    """
    with mock.patch(
        "asyncio.sleep",
        new_callable=AsyncMock,
    ) as _fixture:
        yield _fixture


@pytest.fixture(autouse=True)
def auto_enable_custom_integrations(enable_custom_integrations):
    """Enable custom integrations in all tests."""
    yield


class SystemFactory(DataclassFactory):
    __model__ = System


class ZoneFactory(DataclassFactory):
    __model__ = Zone


class CircuitFactory(DataclassFactory):
    __model__ = Circuit


class DomesticHotWaterFactory(DataclassFactory):
    __model__ = DomesticHotWater


@pytest.fixture
def myvaillant_aioresponses():
    return _myvaillant_aioresponses()


@pytest.fixture
async def mocked_api() -> MyVaillantAPI:
    return await _mocked_api()


@pytest.fixture
async def system_coordinator_mock(hass, mocked_api) -> SystemCoordinator:
    with mock.patch(
        "homeassistant.config_entries.ConfigEntry",
        new_callable=mock.PropertyMock,
        return_value="mockid",
    ) as entry:
        entry.options = TEST_OPTIONS
        hass.data = {DOMAIN: {entry.entry_id: {}}}
        coordinator = SystemCoordinator(hass, mocked_api, entry, update_interval=None)
        yield coordinator
        
        # Clean up background tasks after test completion
        if hasattr(coordinator, '_debounced_refresh') and coordinator._debounced_refresh:
            coordinator._debounced_refresh.async_cancel()


@pytest.fixture
async def daily_data_coordinator_mock(hass, mocked_api) -> DailyDataCoordinator:
    with mock.patch(
        "homeassistant.config_entries.ConfigEntry",
        new_callable=mock.PropertyMock,
        return_value="mockid",
    ) as entry:
        hass.data = {DOMAIN: {entry.entry_id: {}}}
        return DailyDataCoordinator(hass, mocked_api, entry, timedelta(seconds=10))
