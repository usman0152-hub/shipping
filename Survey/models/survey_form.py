from odoo import fields, models


class SurveyModel(models.Model):
    _name = "survey.model"
    _description = "Survey Form"

    job = fields.Char('Job #')
    nature = fields.Char('Nature', required=True)
    console_of = fields.Selection(
        string='Console Of :',
        selection=[('LCL', 'LCL'), ('FCL', 'FCL'), ('Air', 'Air'), ('Sea', 'Sea')], )
    job_date = fields.Char('Job Date:')
    job_type = fields.Char('Job Type/Sub Type:')
    cost_center = fields.Char('Job Type/Sub Type:', required=True)
    console_id = fields.Char('Console ID:')
    job_kind = fields.Char('Job Kind:')
    customer_ref = fields.Char('Customer Refrence:')
    job_status = fields.Char('Job Status:')
    shipt_status = fields.Char('Shipt Status:')
    shipt_date = fields.Date('Shipt Date:')
    type_of_bl = fields.Char('Type of BL:')
    freight_type = fields.Char('Freight Type:')
    nomination = fields.Char('Nomination:')
    file = fields.Char('File:')
    tax_distribution = fields.Char('Tax Distribution:')
    hbl_number = fields.Char('HBL #', required=True )
    hbl_date = fields.Date('Hbl Date:')
    mbl_number = fields.Char('MBL:', required=True)
    mbl_date = fields.Date('MBL Date:')
    total_container = fields.Char('Total Container:')
    tariff_applied = fields.Char('Tariff Applied:')
    client = fields.Char('Client:', required=True )
    consignee = fields.Char('Consignee:')
    shipper = fields.Char('Shipper:' )
    commodity = fields.Char('Commodity:', required=True)
    port_of_loading = fields.Char('Port of Loading:', required=True)
    port_of_discharge = fields.Char('Port of Discharge:')
    final_destination = fields.Char('Final Destination:')
    custom_clearance = fields.Char('Custom Clearance:')
    transportation = fields.Char('Transportation:')
    forwarder_coloader = fields.Char('Forwarder/Coloader:')
    sales_representative = fields.Char('Sales Representative:')
    sline_carrier = fields.Char('Sline/Carrier:')
    local_vendor = fields.Char('Local Vendor:')
    overseas_agent = fields.Char('Overseas Agent:')
    vessel = fields.Char('Vessel:', required=True)
    voyage = fields.Char('Voyage:', required=True)
    etd = fields.Date('ETD:')
    eta = fields.Date('ETA:')
    cbkg_ed = fields.Char('C/BKG/ED:')
    weight = fields.Char('Weight:')
    volume = fields.Char('Vol:')
    container = fields.Char('Container:')
    teu = fields.Char('TEU:')
    pcs = fields.Char('PCS:')
    quotation = fields.Char('Quoatations:')
    tracking_notes = fields.Text('Tracking Notes:')



