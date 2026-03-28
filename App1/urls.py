from django.urls import path,include
from.import views


urlpatterns = [

    path('',views.base,name='base'),
    path('home',views.home,name='home'),
    path('branch',views.branch,name='branch'),
#----change Company------#
    path('changecompony',views.changecompony,name='changecompony'),
    path('createcompony',views.createcompony,name='createcompony'),
    path('crtcompony',views.crtecompony,name='crtecompony'),
    path('selectcompony',views.selectcompony,name='selectcompony'),



#-----Create Currency-------#
    path('currency',views.currency,name='currency'),
    path('currency_alter/<int:pk>',views.currency_alter,name='currency_alter'),
    path('save_currency_data',views.save_currency_data,name="save_currency_data"),
    path('load_create_currency',views.load_create_currency,name='load_create_currency'),
    path('create_currency',views.create_currency,name='create_currency'),
    path('update_currency/<int:pk>',views.update_currency,name='update_currency'),

#-----Create Voucher--------#   
    path('voucher',views.voucher,name='voucher'),
    # path('vouchpage',views.vouchpage,name='vouchpage'),
    path('load_create_vouchertyp',views.load_create_vouchertyp,name='load_create_vouchertyp'),
    path('create_voucher',views.create_voucher,name="create_voucher"),
    path('update_voucher/<int:pk>',views.update_voucher,name="update_voucher"),
    path('save_voucher/<int:pk>',views.save_voucher,name="save_voucher"),

#-----Create Group----------#
    path('group',views.group,name='group'),
    path('branch',views.branch,name='branch'),
    path('load_create_group1',views.load_create_group1,name='load_create_group1'),
    path('load_create_groups',views.load_create_groups,name="load_create_groups"),
    path('create_group',views.create_group,name="create_group"),
    path('update_grp/<int:pk>',views.update_grp,name="update_grp"),

#-----Create Ledger---------#   
    path('ledger',views.ledger,name='ledger'),
    path('ledgerpage',views.ledgerpage,name='ledgerpage'),
    path('load_create_ledgertype',views.load_create_ledgertyp,name='load_create_ledgertyp'),
    path('create_ledger',views.create_ledger,name="create_ledger"),
    path('update_ledger/<int:pk>',views.update_ledger,name="update_ledger"),
    path('save_ledger/<int:pk>',views.save_ledger,name="save_ledger"),

    path('accounting_vouchers',views.accounting_vouchers,name='accounting_vouchers'),
    path('daybook',views.daybook,name='daybook'),
    path('balancesheet',views.balancesheet,name='balancesheet'),
    path('profitloss',views.profitloss,name='profitloss'),
    path('stocksummary',views.stocksummary,name='stocksummary'),
    path('ratioanalysis',views.ratioanalysis,name='ratioanalysis'),
    path('displaymorereports',views.displaymorereports,name='displaymorereports'),
    path('trialbalance',views.trialbalance,name='trialbalance'),
    path('cashflow',views.cashflow,name='cashflow'),

#-----Update Company------#
    path('updatecompony',views.updatecompony,name='updatecompony'),

#-----Feature Pages: Data------#
    path('feature/backup',views.feature_backup,name='feature_backup'),
    path('feature/restore',views.feature_restore,name='feature_restore'),
    path('feature/split-data',views.feature_split,name='feature_split'),
    path('feature/data-path',views.feature_data_path,name='feature_data_path'),

#-----Feature Pages: Exchange------#
    path('feature/data-sync',views.feature_data_sync,name='feature_data_sync'),
    path('feature/exchange-config',views.feature_exchange_config,name='feature_exchange_config'),
    path('feature/online-access',views.feature_online_access,name='feature_online_access'),

#-----Feature Pages: Import------#
    path('feature/import-masters',views.feature_import_masters,name='feature_import_masters'),
    path('feature/import-transactions',views.feature_import_transactions,name='feature_import_transactions'),
    path('feature/import-bank',views.feature_import_bank,name='feature_import_bank'),
    path('feature/import-manage',views.feature_import_manage,name='feature_import_manage'),
    path('feature/import-config',views.feature_import_config,name='feature_import_config'),

#-----Feature Pages: Export------#
    path('feature/export-current',views.feature_export_current,name='feature_export_current'),
    path('feature/export-others',views.feature_export_others,name='feature_export_others'),
    path('feature/export-masters',views.feature_export_masters,name='feature_export_masters'),
    path('feature/export-transactions',views.feature_export_transactions,name='feature_export_transactions'),
    path('feature/export-config',views.feature_export_config,name='feature_export_config'),

#-----Feature Pages: Share------#
    path('feature/share-current',views.feature_share_current,name='feature_share_current'),
    path('feature/share-others',views.feature_share_others,name='feature_share_others'),
    path('feature/share-config',views.feature_share_config,name='feature_share_config'),

#-----Feature Pages: Print------#
    path('feature/print-current',views.feature_print_current,name='feature_print_current'),
    path('feature/print-others',views.feature_print_others,name='feature_print_others'),
    path('feature/print-config',views.feature_print_config,name='feature_print_config'),

#-----Feature Pages: Help------#
    path('feature/help-docs',views.feature_help_docs,name='feature_help_docs'),
    path('feature/help-updates',views.feature_help_updates,name='feature_help_updates'),
    path('feature/help-release-notes',views.feature_help_release_notes,name='feature_help_release_notes'),
    path('feature/help-about',views.feature_help_about,name='feature_help_about'),
    path('feature/help-license',views.feature_help_license,name='feature_help_license'),

#-----Generic Stubs for Unimplemented Features------#
    path('budget', views.generic_stub, {'feature_name': 'Budget'}, name='budget'),
    path('scenario', views.generic_stub, {'feature_name': 'Scenario'}, name='scenario'),
    path('creditlimits', views.generic_stub, {'feature_name': 'Credit Limits'}, name='creditlimits'),
    path('stockgroup', views.generic_stub, {'feature_name': 'Stock Group'}, name='stockgroup'),
    path('stockcategory', views.generic_stub, {'feature_name': 'Stock Category'}, name='stockcategory'),
    path('stockitem', views.generic_stub, {'feature_name': 'Stock Item'}, name='stockitem'),
    path('unit', views.generic_stub, {'feature_name': 'Unit'}, name='unit'),
    path('godown', views.generic_stub, {'feature_name': 'Godown'}, name='godown'),
    path('gstdetails', views.generic_stub, {'feature_name': 'GST Details'}, name='gstdetails'),
    path('pancindetails', views.generic_stub, {'feature_name': 'PAN/CIN Details'}, name='pancindetails'),
    path('reconciliation', views.generic_stub, {'feature_name': 'Reconciliation'}, name='reconciliation'),
    path('banking_stub', views.generic_stub, {'feature_name': 'Banking'}, name='banking_stub'),

]