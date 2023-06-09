COMMAND_SCHEMA = vol.Schema({
    vol.Required(vol.Coerce(str)): {
        vol.Required(CONF_ENDPOINT): vol.urlparse,
        vol.Required(CONF_COMMAND): vol.Coerce(str),
        vol.Optional(CONF_CALLBACK_FN): vol.Coerce(str),
        vol.Optional(CONF_CONTEXT): vol.Schema({}),
        # vol.Optional(CONF_CALLBACK_FN): CALLBACK_SCHEMA,
        vol.Optional(CONF_PARAMS, default={}): PARAM_SCHEMA,
    }})

config = {
    "test": {
        "endpoint": "/",
        "command": "echp 'hello",
    }
}