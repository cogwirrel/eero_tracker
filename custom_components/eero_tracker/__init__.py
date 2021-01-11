import logging

from .const import (
    DOMAIN,
    SERVICE_DISABLE_INTERNET,
    SERVICE_ENABLE_INTERNET,
)

from .services import (
    EeroServiceHandler,
)

_LOGGER = logging.getLogger(__name__)

async def async_setup(hass, config):
    return True

async def async_setup_entry(hass, config_entry):
    _LOGGER.debug("Setting up Eero config entry", hass, config_entry)
    service_handler = EeroServiceHandler()

    def enable_internet(service):
        service_handler.enable_internet()

    def disable_internet(service):
        service_handler.disable_internet()

    hass.services.async_register(DOMAIN, SERVICE_ENABLE_INTERNET, enable_internet)
    hass.services.async_register(DOMAIN, SERVICE_DISABLE_INTERNET, disable_internet)

    return True
