import logging

from .const import (
    DOMAIN,
    EERO_SESSION_COOKIE_FILE,
)

from .eero import (
    CookieStore,
    Eero,
)

_LOGGER = logging.getLogger(__name__)

class EeroServiceHandler:
    def __init__(self):
        self.session = CookieStore(EERO_SESSION_COOKIE_FILE)
        self.eero = Eero(self.session)

    def disable_internet(self):
        _LOGGER.debug("Disabling internet!")
        _LOGGER.debug(self.eero.account())

    def enable_internet(self):
        _LOGGER.debug("Enabling internet!")
        _LOGGER.debug(self.eero.account())
