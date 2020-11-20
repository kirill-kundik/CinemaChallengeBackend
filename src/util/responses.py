from flask import jsonify, make_response


def render_resource(resource):
    return make_response(jsonify({'success': True, 'data': resource}), 200)


def render_error(errors, status=400):
    if not isinstance(errors, list):
        errors = [errors]
    return make_response(jsonify({'success': False, 'errors': errors}), status)
