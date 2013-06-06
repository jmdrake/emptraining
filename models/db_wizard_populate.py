from gluon.contrib.populate import populate
if db(db.auth_user).isempty():
     populate(db.auth_user,10)
     populate(db.t_employee,10)
     populate(db.t_course,10)
     populate(db.t_session,10)
     populate(db.t_attendance,10)
     populate(db.t_certification,10)
     populate(db.t_empcert,10)
     populate(db.t_doctype,10)
     populate(db.t_certtype,10)
     populate(db.t_document,10)
