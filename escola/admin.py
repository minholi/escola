from django.contrib.admin import AdminSite

class EscolaAdminSite(AdminSite):
    site_header = 'Escola'

admin_site = EscolaAdminSite(name='escolaadmin')