# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'Survey Form',
    'version': '14.0.1.0.0',
    'author': 'Muhammad Usman',
    'summary': 'Survey Form',
    'sequence': 12,
    'description': """user freindly interface for Survey Form""",
    'category': 'Sales',
    'website': 'https://www.odoo.com/page/billing',
    'depends': ['base'],
    'data': ['security/ir.model.access.csv','security/security.xml','data/survey_data.xml', 'views/survey_form_vews.xml', 'views/manifiest_form_vews.xml'],
    'demo': [
    ],
    'qweb': [
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
