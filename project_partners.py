from openerp.osv import fields, osv
import openerp.addons.decimal_precision as dp
from lxml import etree as ET


class project_partners_partners(osv.Model):
    _inherit = 'res.partner'

    _columns = {
        'project_partners_projects': fields.many2many(
            'project.project',
            'rel_partners_projects',
            'partners',
            'project_partners_projects',
            'Projects'),
        'project_partners_tasks': fields.many2many(
            'project.project',
            'rel_partners_tasks',
            'partners',
            'project_partners_tasks',
            'Tasks'),
    }

class project_partners_project(osv.Model):
    _inherit = 'project.project'

    _columns = {
        'partners': fields.many2many(
            'res.partner',
            'rel_partners_projects',
            'project_partners_projects',
            'partners',
            'Partners'),
    }


class project_partners_task(osv.osv):
    _inherit = 'project.task'

    _columns = {
        'partners': fields.many2many(
            'res.partner',
            'rel_partners_tasks',
            'project_partners_tasks',
            'partners',
            'Partners'),
    }
