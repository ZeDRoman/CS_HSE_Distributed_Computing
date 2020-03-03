from flask import request


def production_form_data():
    return F"id: {request.form.get('id')}, name: {request.form.get('id')}, category: {request.form.get('id')}"


def log_form_validation_error(request_form, form):
    return ' '.join(['validation_error', str(form.__class__.__name__), request_form, str(form.errors)])


def log_db_error(request_form, db_error):
    return ' '.join(['db_error', request_form, str(db_error)])