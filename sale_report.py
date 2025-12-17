from odoo import api, models

class SaleOrderReport(models.AbstractModel):
    _name = 'report.fsz_sale_report_override.custom_sale_report'
    _description = 'Custom Sale Order Report'

    @api.model
    def _get_report_values(self, docids, data=None):
        docs = self.env['sale.order'].browse(docids)
        return {
            'doc_ids': docids,
            'doc_model': 'sale.order',
            'docs': docs,
        }
