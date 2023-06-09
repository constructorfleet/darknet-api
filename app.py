# web imports
import os
from enum import Enum

import voluptuous as vol
from flask import Flask
from flask_executor import Executor
from flask_shell2http import Shell2HTTP


class Method(Enum):
    GET = "GET"
    POST = "POST"
    DELETE = "DELETE"
    PUT = "PUT"


class FieldType(Enum):
    INT = "INT"
    FLOAT = "FLOAT"
    STRING = "STRING",
    FILE = "FILE"


CONF_BASE_URL = "base_url"
CONF_ENDPOINT = "endpoint"
CONF_METHOD = "method"
CONF_NAME = "name"
CONF_COMMAND = "command"
CONF_CALLBACK_FN = "callback"
CONF_PARAMS = "params"
CONF_TYPE = "type"
CONF_CONTEXT = "context"

PARAM_SCHEMA = vol.Schema({
    vol.Required(vol.Coerce(str)): vol.All(vol.In(FieldType))
})

COMMAND_SCHEMA = vol.Schema({
    vol.Required(vol.Coerce(str)): {
        vol.Required(CONF_ENDPOINT): vol.urlparse,
        vol.Required(CONF_COMMAND): vol.Coerce(str),
        vol.Optional(CONF_CALLBACK_FN): vol.Coerce(str),
        vol.Optional(CONF_CONTEXT): vol.Schema({}),
        # vol.Optional(CONF_CALLBACK_FN): CALLBACK_SCHEMA,
        vol.Optional(CONF_PARAMS, default={}): PARAM_SCHEMA,
    }})

SCHEMA_PARAM = vol.Schema({
    vol.Required(vol.Coerce(str)): COMMAND_SCHEMA
})

# Flask application instance
app = Flask(__name__)

# application factory
executor = Executor(app)
shell2http = Shell2HTTP(app, executor)


async def configure_endpoint(name, config):
    end_point = config[CONF_ENDPOINT]
    command = config[CONF_COMMAND]
    callback = config[CONF_CALLBACK_FN]
    context = config[CONF_CONTEXT]


async def load_configs():
    app_config = __import__("config",
                            fromlist=os.environ["SERVER_CONFIG"] or "demo.py")
    valid_conf = COMMAND_SCHEMA(app_config)

    for command_name, command_def in valid_conf.items():
        shell2http.register_command(
            endpoint=command_def[CONF_ENDPOINT],
            command_name=command_def[CONF_COMMAND],
            callback_fn=command_def[CONF_CALLBACK_FN],
        )

app.run(os.environ["HOST"], int(os.environ["PORT"]))
