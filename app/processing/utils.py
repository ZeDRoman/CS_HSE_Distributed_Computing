from flask import current_app

from processing.debug_messages import log_form_validation_error, production_form_data


def checkIsNumber(elem, elem_type):
    if isinstance(elem, int):
        return True

    if elem is None or not isinstance(elem, str) or not elem.isdigit():
        current_app.logger.info(elem_type + ' not a number, value: ' + str(elem))
        return False
    return True


def formIsValid(form):
    if not form.validate():
        app.logger.info(log_form_validation_error(production_form_data(), form))
        return False
    return True
