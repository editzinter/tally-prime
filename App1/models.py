from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse
from django.contrib.auth.models import User
from locale import currency
from unicodedata import decimal

# Create your models here.

class crtcompony(models.Model):
    componyname = models.CharField(max_length=50)
    mailingname = models.CharField(max_length=50, blank=True, default='')
    address = models.CharField(max_length=50, blank=True, default='')
    state = models.CharField(max_length=50, blank=True, default='')
    country = models.CharField(max_length=50, blank=True, default='India')
    pincode = models.CharField(max_length=10, blank=True, default='')
    telphone = models.CharField(max_length=10, blank=True, default='')
    mobile = models.CharField(max_length=10, blank=True, default='')
    fax = models.CharField(max_length=10, blank=True, default='')
    email = models.EmailField(blank=True, default='')
    website = models.CharField(max_length=100, blank=True, default='')
    fyearbgn = models.DateField(null=True, blank=True)
    booksbgn = models.DateField(null=True, blank=True)
    curncysymbl = models.CharField(max_length=10, blank=True, default='₹')
    crncyname = models.CharField(max_length=10, blank=True, default='INR')

    def __str__(self):
        return self.name


class VoucherModels(models.Model):
    voucher_name = models.CharField(max_length=225)
    alias = models.CharField(max_length=225)
    voucher_type = models.CharField(max_length=225)
    abbreviation = models.CharField(max_length=225)
    active_this_voucher_type =  models.CharField(max_length=225)
    method_voucher_numbering = models.CharField(max_length=225)
    use_adv_conf = models.CharField(max_length=225,blank=True)
    prvnt_duplictes = models.CharField(max_length=225,default="Null",blank=True)
    use_effective_date =  models.CharField(max_length=225,default="Null")
    allow_zero_value_trns =  models.CharField(max_length=225)
    allow_naration_in_voucher =  models.CharField(max_length=225)
    make_optional =  models.CharField(max_length=225)
    provide_naration =  models.CharField(max_length=225)
    print_voucher = models.CharField(max_length=225)
  
    def __str__(self):
        return self.name

class CreateCurrency(models.Model):
    symbol =models.CharField(max_length=225)
    formal_name=models.CharField(max_length=225)
    ISO_code=models.CharField(max_length=225)
    decimal_places= models.CharField(max_length=225,default=2)
    show_in_millions =  models.CharField(max_length=225)
    suffix_to_amount=  models.CharField(max_length=225)
    space_symbol_amount = models.CharField(max_length=225)
    word_after_decimal = models.CharField(max_length=225)
    decimal_no_in_words = models.CharField(max_length=225)

    def __str__(self):
        return self.name

class CurrencyAlter(models.Model):
    cname= models.ForeignKey( CreateCurrency,on_delete=models.CASCADE,default=1)
    slno = models.CharField(max_length=225)
    currencys = models.CharField(max_length=225)
    stdrate =models.CharField(max_length=225)
    lastvrate =models.CharField(max_length=225)
    specirate =models.CharField(max_length=225)
    lastvrate2 =models.CharField(max_length=225)
    specirate2 =models.CharField(max_length=225)
    
    def __str__(self):
        return self.name

class GroupModel(models.Model):
    name =  models.CharField(max_length=225,default="Null",blank=True)
    alias =  models.CharField(max_length=225,default="Null",blank=True)
    under =models.CharField(max_length=225,default="Null",blank=True)
    nature_of_group = models.CharField(max_length=225,default="Null",blank=True)
    does_it_affect =models.CharField(max_length=225,default="Null",blank=True)
    gp_behaves_like_sub_ledger =  models.CharField(max_length=225,default="Null",blank=True)
    nett_debit_credit_bal_reporting =  models.CharField(max_length=225,default="Null",blank=True)
    used_for_calculation =  models.CharField(max_length=225,default="Null",blank=True)
    method_to_allocate_usd_purchase =  models.CharField(max_length=225,default="Null",blank=True)

    def __str__(self):
        return self.name



class LedgerModels(models.Model):
    ledger_name = models.CharField(max_length=225)
    alias = models.CharField(max_length=225)
    under = models.CharField(max_length=225)
    mail_name = models.CharField(max_length=225)
    mail_address =  models.CharField(max_length=225)
    mail_state = models.CharField(max_length=225)
    mail_country = models.CharField(max_length=225,blank=True)
    mail_pincode = models.CharField(max_length=225,default="Null",blank=True)
    bank_details =  models.CharField(max_length=225,default="Null")
    pan_no =  models.CharField(max_length=225)
    registration_type =  models.CharField(max_length=225)
    gst_in =  models.CharField(max_length=225)
    alter_gst =  models.CharField(max_length=225)
  
    def __str__(self):
        return self.ledger_name


class PrintConfig(models.Model):
    printer_name = models.CharField(max_length=225, default='Microsoft Print to PDF')
    paper_size = models.CharField(max_length=50, default='a4')
    orientation = models.CharField(max_length=50, default='portrait')
    print_preview = models.CharField(max_length=10, default='yes')
    copy_marking = models.CharField(max_length=50, default='none')
    num_copies = models.IntegerField(default=1)
    show_company_name = models.CharField(max_length=10, default='yes')
    show_company_address = models.CharField(max_length=10, default='no')
    show_company_logo = models.CharField(max_length=10, default='no')
    report_title = models.CharField(max_length=225, default='Auto (from report)', blank=True)
    report_subtitle = models.CharField(max_length=225, default='', blank=True)
    margin_top = models.IntegerField(default=10)
    margin_bottom = models.IntegerField(default=10)
    margin_left = models.IntegerField(default=15)
    margin_right = models.IntegerField(default=15)

    def __str__(self):
        return f'PrintConfig #{self.pk}'


class ExportConfig(models.Model):
    default_format = models.CharField(max_length=50, default='excel')
    destination_folder = models.CharField(max_length=500, default='')
    open_after_export = models.CharField(max_length=10, default='yes')
    include_logo = models.CharField(max_length=10, default='yes')

    def __str__(self):
        return f'ExportConfig #{self.pk}'


class ImportConfig(models.Model):
    default_format = models.CharField(max_length=50, default='xml')
    default_master_type = models.CharField(max_length=50, default='ledgers')
    duplicate_handling = models.CharField(max_length=50, default='ignore')

    def __str__(self):
        return f'ImportConfig #{self.pk}'


class BackupLog(models.Model):
    company_names = models.TextField(default='')
    file_path = models.CharField(max_length=500)
    file_size = models.CharField(max_length=50, default='0 KB')
    backup_format = models.CharField(max_length=10, default='zip')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Backup {self.created_at}'


class AppSetting(models.Model):
    key = models.CharField(max_length=225, unique=True)
    value = models.TextField(default='', blank=True)

    def __str__(self):
        return self.key


class ImportTemplate(models.Model):
    name = models.CharField(max_length=225)
    file_format = models.CharField(max_length=50, default='csv')
    master_type = models.CharField(max_length=50, default='ledgers')
    field_mappings = models.TextField(default='{}')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Transaction(models.Model):
    date = models.DateField()
    voucher_type = models.CharField(max_length=100)
    voucher_number = models.IntegerField()
    narration = models.TextField(blank=True, null=True)
    company = models.ForeignKey(crtcompony, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.voucher_type} - {self.voucher_number} ({self.date})"

class TransactionEntry(models.Model):
    transaction = models.ForeignKey(Transaction, on_delete=models.CASCADE, related_name='entries')
    ledger = models.ForeignKey(LedgerModels, on_delete=models.CASCADE)
    entry_type = models.CharField(max_length=2, choices=[('Dr', 'Debit'), ('Cr', 'Credit')])
    amount = models.DecimalField(max_digits=15, decimal_places=2)

    def __str__(self):
        return f"{self.transaction.voucher_type} {self.entry_type} {self.amount} - {self.ledger.ledger_name}"       