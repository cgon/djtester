from django.db import models

class Receipt(models.Model):
	date = models.DateField()
	amount = models.DecimalField(max_digits=7, decimal_places=2)


class ReturnReceipt(Receipt):
	class Meta:
		proxy = True

	def return_status(self):
		pass


class ReturnsLedger(models.Model):
	return_receipt = models.ForeignKey(ReturnReceipt)
