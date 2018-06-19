from flask_restplus import Api
from flask import Blueprint

blueprint = Blueprint('api', __name__)

from .cats import api as ns1
from .dogs import api as ns2

api = Api(
    blueprint
)

api.add_namespace(ns1)
api.add_namespace(ns2)