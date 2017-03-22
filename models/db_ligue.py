# -*- coding: utf-8 -*-

db.define_table('discipline',
                Field('libelle','string',requires=IS_NOT_EMPTY()),
                Field('olympique','string',requires=IS_IN_SET(['OUI','NON']))
                ,migrate = True
               )

db.define_table('ligue',
             Field('nom','string',requires=IS_NOT_EMPTY()),
             Field('adresseRue','string',requires=IS_NOT_EMPTY()),
             Field('ville','string',requires=IS_NOT_EMPTY()),
             Field('cp','string',requires=IS_NOT_EMPTY()),
             Field('tel','string',requires=IS_NOT_EMPTY()),
             Field('URLSiteWeb','string'),
             Field('emailContact','string'),
             Field('idDiscipline','reference discipline',requires =IS_IN_DB(db,db.discipline.id,'%(libelle)s'))
            ,migrate = True
                )
