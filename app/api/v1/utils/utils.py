"""Utility functions for the app."""
from flask import request, jsonify
from flask_jwt import jwt
from instance.config import key


def requires_token(route_method):
    """Initialize a decorator function for token required endpoints."""
    def wrapp(*args, **kwargs):
        token = None
        if 'X-API-KEY' in request.headers:
            token = request.headers['X-API-KEY']
        if not token:
            return jsonify({
                "status": "error",
                "message": "Token is missing!"
            }), 401
        try:
            data = jwt.decode(token, key)
        except Exception:
            return jsonify({
                "status": "error",
                "message": "Token is Invalid"
            }), 401
        return route_method(*args, **kwargs)

    return wrapp
