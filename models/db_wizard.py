### we prepend t_ to tablenames and f_ to fieldnames for disambiguity


########################################
db.define_table('t_employee',
    Field('f_name', type='string',
          label=T('Name')),
    Field('f_address', type='string',
          label=T('Address')),
    Field('f_phone', type='string',
          label=T('Phone')),
    Field('f_email', type='string',
          label=T('Email')),
    auth.signature,
    format='%(f_name)s',
    migrate=settings.migrate)

db.define_table('t_employee_archive',db.t_employee,Field('current_record','reference t_employee',readable=False,writable=False))

########################################
db.define_table('t_course',
    Field('f_title_string', type='string',
          label=T('Title String')),
    Field('f_description', type='text',
          label=T('Description')),
    auth.signature,
    format='%(f_title_string)s',
    migrate=settings.migrate)

db.define_table('t_course_archive',db.t_course,Field('current_record','reference t_course',readable=False,writable=False))

########################################
db.define_table('t_session',
    Field('f_course_id_reference', type='reference t_course',
          label=T('Course Id Reference')),
    Field('f_date', type='date',
          label=T('Date')),
    auth.signature,
    format='%(f_course_id_reference)s',
    migrate=settings.migrate)

db.define_table('t_session_archive',db.t_session,Field('current_record','reference t_session',readable=False,writable=False))

########################################
db.define_table('t_attendance',
    Field('f_emp_id_reference', type='reference t_employee',
          label=T('Emp Id Reference')),
    Field('f_session_id_reference', type='reference t_session',
          label=T('Session Id Reference')),
    auth.signature,
    format='%(f_emp_id_reference)s',
    migrate=settings.migrate)

db.define_table('t_attendance_archive',db.t_attendance,Field('current_record','reference t_attendance',readable=False,writable=False))

########################################
db.define_table('t_certification',
    Field('f_name_string', type='string',
          label=T('Name String')),
    Field('f_description', type='text',
          label=T('Description')),
    auth.signature,
    format='%(f_name_string)s',
    migrate=settings.migrate)

db.define_table('t_certification_archive',db.t_certification,Field('current_record','reference t_certification',readable=False,writable=False))

########################################
db.define_table('t_empcert',
    Field('f_emp_id_reference', type='reference t_employee',
          label=T('Emp Id Reference')),
    Field('f_cert_id_reference', type='reference t_certification',
          label=T('Cert Id Reference')),
    Field('f_expires', type='date',
          label=T('Expires')),
    auth.signature,
    format='%(f_emp_id_reference)s',
    migrate=settings.migrate)

db.define_table('t_empcert_archive',db.t_empcert,Field('current_record','reference t_empcert',readable=False,writable=False))

########################################
db.define_table('t_doctype',
    Field('f_name_string', type='string',
          label=T('Name String')),
    Field('f_description', type='text',
          label=T('Description')),
    auth.signature,
    format='%(f_name_string)s',
    migrate=settings.migrate)

db.define_table('t_doctype_archive',db.t_doctype,Field('current_record','reference t_doctype',readable=False,writable=False))

########################################
db.define_table('t_document',
    Field('f_title_string', type='string',
          label=T('Title String')),
    Field('f_description', type='text',
          label=T('Description')),
    Field('f_course_id_reference', type='reference t_course',
          label=T('Course Id Reference')),
    Field('f_doctype_id_reference', type='reference t_doctype',
          label=T('Doctype Id Reference')),
    Field('f_document', 'upload', default='/home/john'),
    auth.signature,
    format='%(f_title_string)s',
    migrate=settings.migrate)

db.define_table('t_document_archive',db.t_document,Field('current_record','reference t_document',readable=False,writable=False))
