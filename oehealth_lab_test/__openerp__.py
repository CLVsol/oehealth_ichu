# -*- encoding: utf-8 -*-
################################################################################
#                                                                              #
# Copyright (C) 2012  Carlos Eduardo Vercelino - CLVsol.net                    #
#                                                                              #
# This program is free software: you can redistribute it and/or modify         #
# it under the terms of the GNU Affero General Public License as published by  #
# the Free Software Foundation, either version 3 of the License, or            #
# (at your option) any later version.                                          #
#                                                                              #
# This program is distributed in the hope that it will be useful,              #
# but WITHOUT ANY WARRANTY; without even the implied warranty of               #
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the                #
# GNU Affero General Public License for more details.                          #
#                                                                              #
# You should have received a copy of the GNU Affero General Public License     #
# along with this program.  If not, see <http://www.gnu.org/licenses/>.        #
################################################################################

{
    'name': 'OeHealth: Laboratory Tests',
    'version': '1.0.0',
    'author': 'Carlos Eduardo Vercelino - CLVsol',
    'category': 'Generic Modules/Others',
    'license': 'AGPL-3',
    'website': 'http://CLVsol.net',
    'description': '''
    ''',
    'depends': [
                'oehealth_patient'
                ]
                ,
    'data': [
             'security/ir.model.access.csv',
             ],
    'init_xml': [
                 'security/oehealth_lab_test_security.xml',
                 'oehealth_lab_test_view.xml',
                 'wizard/create_lab_test.xml'
                 ],
    'test': [],
    'update_xml': [
                   'data/oehealth_lab_test_sequences.xml',
                  ],
    'installable': True,
    'active': False,
}