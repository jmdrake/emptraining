# -*- coding: utf-8 -*-
### required - do no delete
def user(): return dict(form=auth())
def download(): return response.download(request,db)
def call(): return service()
### end requires
def index():
    return dict()

def error():
    return dict()

@auth.requires_login()
def employee_manage():
    form = SQLFORM.smartgrid(db.t_employee,onupdate=auth.archive)
    return locals()

@auth.requires_login()
def course_manage():
    form = SQLFORM.smartgrid(db.t_course,onupdate=auth.archive)
    return locals()

@auth.requires_login()
def document_manage():
    form = SQLFORM.smartgrid(db.t_document,onupdate=auth.archive)
    return locals()

@auth.requires_login()
def doctype_manage():
    form = SQLFORM.smartgrid(db.t_doctype,onupdate=auth.archive)
    return locals()

@auth.requires_login()
def session_manage():
    form = SQLFORM.smartgrid(db.t_session,onupdate=auth.archive)
    return locals()

@auth.requires_login()
def attendance_manage():
    form = SQLFORM.smartgrid(db.t_attendance,onupdate=auth.archive)
    return locals()

@auth.requires_login()
def certification_manage():
    form = SQLFORM.smartgrid(db.t_certification,onupdate=auth.archive)
    return locals()

@auth.requires_login()
def empcert_manage():
    form = SQLFORM.smartgrid(db.t_empcert,onupdate=auth.archive)
    return locals()

