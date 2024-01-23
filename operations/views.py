from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from security.security_middleware import check_role
from .models import Bank, Branch, Gender
from .serializers import BankSerializer, BranchSerializer, GenderSerializer


@api_view(['POST'])
@check_role('Bank - Maker')
def bank_create(request):
    serializer = BankSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)


@api_view(['GET'])
@check_role('Bank - Read')
def bank_list(request):
    banks = Bank.objects.all()
    serializer = BankSerializer(banks, many=True)
    return Response(serializer.data)


# @api_view(['GET'])
# @check_role('Bank - Read')
# def bank_detail(request, pk):
#     try:
#         bank = Bank.objects.get(pk=pk)
#     except Bank.DoesNotExist:
#         return Response(status=404)

#     serializer = BankSerializer(bank)
#     return Response(serializer.data)


@api_view(['PUT'])
@check_role('Bank - Checker')
def bank_update(request, pk):
    try:
        bank = Bank.objects.get(pk=pk)
    except Bank.DoesNotExist:
        return Response(status=404)

    serializer = BankSerializer(bank, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)


@api_view(['DELETE'])
@check_role('Bank - Deleter')
def bank_delete(request, pk):
    try:
        bank = Bank.objects.get(pk=pk)
    except Bank.DoesNotExist:
        return Response(status=404)

    bank.delete()
    return Response(status=204)





