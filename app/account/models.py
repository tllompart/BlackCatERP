from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

from ..base.views.sequence import get_next_value

from app.base.models.basemodel import ERPBase
from app.base.models.tax import Tax
from app.base.models.company import Company


class AccountYear(ERPBase):
    name = models.CharField(max_length=255, blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    # slug         = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.name


ACCOUNT_PLAN_TYPE = (
    ("To Charge", _("To Charge")),
    ("To Pay", _("To Pay")),
    ("Bank and Cashier", _("Bank and Cashier")),
    ("Credit Card", _("Credit Card")),
    ("Current Assets", _("Current Assets")),
    ("Non-current Assets", _("Non-current Assets")),
    ("Pre-payments", _("Pre-payments")),
    ("Fixed Assets", _("Fixed Assets")),
    ("Current Liability", _("Current Liability")),
    ("Non-current Liabilities", _("Non-current Liabilities")),
    ("Capital", _("Capital")),
    ("Current Year Earnings", _("Current Year Earnings")),
    ("Other Income", _("Other Income")),
    ("Income", _("Income")),
    ("Depreciation", _("Depreciation")),
    ("Expenses", _("Expenses")),
    ("Direct Cost of Sales", _("Direct Cost of Sales")),
    ("Unclassified Accounts", _("Unclassified Accounts")),
)


# ========================================================================== #
class AccountPlan(ERPBase):
    code = models.CharField(_('Code'), max_length=80)
    name = models.CharField(_('Name'), max_length=80)
    type = models.CharField(
        choices=ACCOUNT_PLAN_TYPE,
        max_length=64,
        default='active'
    )
    tax_id = models.ManyToManyField(Tax, verbose_name=_('Tax'), blank=True)
    reconcile = models.BooleanField(_("Reconcile"), default=False)


JOURNAL_TYPE = (
    ("sale", _("Sale")),
    ("purchase", _("Purchase")),
    ("cash", _("Cash")),
    ("bank", _("bank")),
    ("miscellaneous", _("Miscellaneous")),
)


# ========================================================================== #
class Journal(ERPBase):
    name = models.CharField(_("Name"), max_length=80)
    type = models.CharField(
        choices=JOURNAL_TYPE,
        max_length=13,
        default='Sale'
    )
    short_code = models.CharField(max_length=6)
    default_credit_account = models.ForeignKey(
        AccountPlan,
        verbose_name=_("Default Credit Account"),
        null=True,
        blank=True,
        on_delete=models.PROTECT,
        related_name='credit_acount'
    )
    default_debit_account = models.ForeignKey(
        AccountPlan,
        verbose_name=_("Default Debit Account"),
        null=True,
        blank=True,
        on_delete=models.PROTECT,
        related_name='debit_account'
    )

    def __str__(self):
        return "{}".format(self.name)


ACCOUNT_MOVE_STATE = (
    (0, _('No asentado')),
    (1, _('Validated')),
    (2, _('canceled')),
    (3, _('confirmed'))
)


# ========================================================================== #
class AccountMove(ERPBase):
    name = models.CharField(_('Name'), max_length=80)
    state = models.IntegerField(
        _('Status'),
        choices=ACCOUNT_MOVE_STATE,
        default=0
    )
    journal_id = models.ForeignKey(Journal, on_delete=models.PROTECT)
    date_move = models.DateField(default=timezone.now)
    company_move = models.ForeignKey(
        Company,
        on_delete=models.PROTECT,
        null=True,
        blank=True
    )
    reference = models.CharField(
        _('Reference'),
        max_length=80,
        null=True,
        blank=True
    )

    amount = models.DecimalField(
        _('Total'),
        max_digits=10,
        decimal_places=2,
        default=0
    )
    debit = models.DecimalField(
        _('debit'),
        max_digits=10,
        decimal_places=2,
        default=0
    )
    credit = models.DecimalField(
        _('credit'),
        max_digits=10,
        decimal_places=2,
        default=0
    )

    def save(self, *args, **kwargs):
        self.name = get_next_value(self._meta.object_name, 'ACC')

        if not self.date_move or self.date_move == "":
            self.date_move = timezone.now
        super().save(*args, **kwargs)
