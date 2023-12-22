"""Support custom filters for jinja2 templating"""
import logging

from homeassistant.helpers import template

_LOGGER = logging.getLogger(__name__)

_TemplateEnvironment = template.TemplateEnvironment

## -- MAP ATTRIBUTES
def mapattributes(self, list_of_dicts, list_of_keys):
    l = []
    for di in list_of_dicts:
      newdi = { }
      for key in list_of_keys:
        newdi[key] = di[key]
      l.append(newdi)
    return l

def init(*args):
    """Initialize filters"""
    env = _TemplateEnvironment(*args)
    env.filters["mapattributes"] = mapattributes
    env.globals["mapattributes"] = mapattributes
    return env

template.TemplateEnvironment = init
template._NO_HASS_ENV.filters["mapattributes"] = mapattributes

async def async_setup(hass, hass_config):
    tpl = template.Template("", template._NO_HASS_ENV.hass)
    tpl._env.globals = mapattributes
    return True
