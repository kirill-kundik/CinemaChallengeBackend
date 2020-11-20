from flask import jsonify, make_response


def render_resource(resource):
    if isinstance(resource, list):
        output = []
        for r in resource:
            if hasattr(r, 'json'):
                output.append(r.json)
            else:
                output.append(r)
        resource = output
    else:
        if hasattr(resource, 'json'):
            resource = resource.json

    return make_response(
        jsonify({'success': True, 'data': resource}), 200
    )


def render_error(errors, status=400):
    if not isinstance(errors, list):
        errors = [errors]
    return make_response(jsonify({'success': False, 'errors': errors}), status)
