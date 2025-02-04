from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .number import Number

# Create your views here.

class LandingView(APIView):
    """
    LandingView is a class-based view that handles GET requests to the API.
    Methods:
        get(request):
    """
    def get(self, request):
        """
        Handles GET requests to the API.
        Args:
            request: The HTTP request object.
        Returns:
            Response: A JSON response containing a welcome message, author information, 
                      and available endpoints.
        """

        return Response({
            "message": "Welcome to the Number Classifier API",
            "author": "tha_orakkle",
            "endpoints": {
                "classify-numbers": "/api/classify-number?number=<number>",
            }
        })


class NumberView(APIView):
    """
    NumberView API to return interesting mathematical properties about a number.

    Methods
        get(request): Expects a 'number' parameter in the query string.

    """

    def get(self, request):
        """
        Returns:
            A JSON response containing:
            - "number": The input number.
            - "is_prime": Boolean indicating if the number is prime.
            - "is_perfect": Boolean indicating if the number is perfect.
            - "properties": A list of properties of the number.
            - "digit_sum": The sum of the digits of the number.
            - "fun_fact": A fun fact about the number.
            If the 'number' parameter is missing or invalid, returns an error message with status 400.
        """
        num = request.GET.get('number', None)
        if num is None:
            return Response({"error": "number is required"}, status=400)
        try:
            num = int(num)
        except:
            return Response({
                "number": "alphabet",
                "error": "true"
            }, status=400)
        number = Number(num)
        return Response({
            "number": number.number,
            "is_prime": number.is_prime(),
            "is_perfect": number.is_perfect(),
            "properties": number.properties(),
            "digit_sum": number.digit_sum(),
            "fun_fact": number.fun_fact()
        })
        