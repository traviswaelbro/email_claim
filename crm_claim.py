from openerp.osv import fields,osv

class crm_claim(osv.osv):
    _inherit = 'crm.claim'
    
    def email_claim(self, cr, uid, ids, vals, context=None):
    	""" Open a window to compose an email to the current claim's linked partner.
    	""" 
        assert len(ids) == 1, 'This option should only be used for a single id at a time.'
        ir_model_data = self.pool.get('ir.model.data')
        try:
            compose_form_id = ir_model_data.get_object_reference(cr, uid, 'mail', 'email_compose_message_wizard_form')[1]
        except ValueError:
            compose_form_id = False 

        # res_partner_data = res_partner_create.browse(cr,SUPERUSER_ID,ids[0],context=context)
        res_partner_data = self.browse(cr,uid,ids)

        ctx = dict()
        ctx.update({
            # 'default_model': 'res.partner',
            # 'default_res_id': res_partner_data.id,
            # 'default_use_template': bool(template_id),
            # 'default_template_id': template_id,
            'default_use_template': True,
            'default_template_id': 32,
            'default_composition_mode': 'comment',
        })
        return {
            'type': 'ir.actions.act_window',
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'mail.compose.message',
            'views': [(compose_form_id, 'form')],
            'view_id': compose_form_id,
            'target': 'new',
            'context': ctx,
        }