from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import loader
from account.models import *

# Create your views here.
# def login(request):
#     return render(request,'login.html')

def amount(request):
    # JournalEntry.objects.all().delete()
    if request.POST:
        description=request.POST['dcn']
        amount=request.POST['amount']
        date=request.POST['date']
        ttype=request.POST['transaction_type']
        amtentry=JournalEntry(particulars=description,date=date,amount=amount,ttype=ttype)
        amtentry.save()
    return render(request,'amount_debit_credit.html')

def journal_entry_list(request):
    search_date = request.GET.get('search_date', None)
    entries = JournalEntry.objects.all().order_by('date')

    if search_date:
        entries = entries.filter(date=search_date)

    total_debit = 0
    total_credit = 0
    balance = 0

    for entry in entries:
        if entry.ttype == 1:  # Debit
            total_debit += entry.amount
            balance -= entry.amount
        elif entry.ttype == 0:  # Credit
            total_credit += entry.amount
            balance += entry.amount

        entry.balance = balance

    return render(request, 'journal_entry_list.html', {
        'entries': entries,
        'current_balance': balance,
        'total_debit': total_debit,
        'total_credit': total_credit,
        'search_date': search_date,  # Pass search_date to the template for displaying in the UI
    })