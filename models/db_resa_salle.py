# -*- coding: utf-8 -*-
db.define_table('categorie',
                Field('nom','string'),
                Field('admin_email','string'),
                Field('heureOuverture','integer'),
                Field('heureOuvertureMinutes','integer'),
                Field('heureFermeture','integer'),
                Field('heureFermetureMinutes','integer'),
                migrate=True)

db.define_table('salle',
                Field('nom','string'),
                Field('capacite','integer'),
                Field('disponible','integer',default=1),
                Field('categorie_id',db.categorie,requires=IS_IN_DB(db,db.categorie.id,'%(nom)s')),
                migrate=True)

db.define_table('reservation',
                Field('etat','integer',writable=False,default=1),
                Field('dateDebut','datetime',writable=False,requires = IS_DATETIME(format=T('%d-%m-%Y %H:%M'),error_message='doit être au format DD-MM-YYYY HH:MM!')),
                Field('dateFin','datetime',writable=False,requires = IS_DATETIME(format=T('%d-%m-%Y %H:%M'),error_message='doit être au format DD-MM-YYYY HH:MM!')),
                Field('salle_id',db.salle,writable=False,requires=IS_IN_DB(db,db.salle.id,'%(nom)s')),
                migrate=True)
