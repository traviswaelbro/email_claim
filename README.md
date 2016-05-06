# email_claim

_email_claim_ is a module that adds an _Email_ button to Odoo's _Claim_ form. 

The email button will open the compose dialog. Currently, it uses a hard-coded template ID, which must be created manually by you. 

##### Example Values for email template:

- From: ```${object.user_id.email or object.company_id.email}```
- To: ```${object.partner_id.email}```
- Subject: ```${object.name or 'RMA'} Authorization```

##### To Do:

- Remove crm_claim_sale_services dependency, in favor of generic crm_claim dependency
  - Convert view inheritance
- Create default template
- Allow selecting template from Odoo settings
