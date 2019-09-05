
from rest_framework import generics
# from rest_framework import viewsets
# from rest_framework.decorators import action
# from rest_framework.response import Response

from collect.models import HistoricalData
from collect.serializers import HistoricalDataSerializer

# from datatosql import history


class HistoryViewSet(generics.ListAPIView):
    serializer_class = HistoricalDataSerializer

    def get_queryset(self):
        # ticker = 'historical_data"."' + self.kwargs['ticker'].lower()
        ticker = self.kwargs['ticker'].lower()
        return HistoricalData.with_tickers(ticker)

    # history.dataToSQL('AAPL', 'history')
