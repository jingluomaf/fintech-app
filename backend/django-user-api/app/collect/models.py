from django.db import models
# from datatosql.history import histricalDataToSQL


# class HistoricalDataManager(models.Manager):


class HistoricalData(models.Model):
    # objects = HistoricalDataManager()

    date = models.DateField(primary_key=True)
    open = models.FloatField(null=True)
    high = models.FloatField(null=True)
    low = models.FloatField(null=True)
    close = models.FloatField(null=True)
    volume = models.BigIntegerField(null=True)
    dividends = models.FloatField(null=True)
    splits = models.FloatField(null=True)

    class Meta:
        managed = False
        # db_table = 'historical_data"."'+'aapl'
        # ordering = ['-date']

    def with_tickers(self):
        from django.db import connection
        from django.db.utils import ProgrammingError
        from django.http import Http404
        with connection.cursor() as cursor:
            try:
                cursor.execute("SELECT * FROM historical_data." + self)
            except (ProgrammingError, NameError):
                raise Http404
            result_list = []
            for row in cursor.fetchall():
                p = HistoricalData.objects.model(
                    date=row[0],
                    open=row[1],
                    high=row[2],
                    low=row[3],
                    close=row[4],
                    volume=row[5],
                    dividends=row[6],
                    splits=row[7],
                )
                result_list.insert(0, p)
        return result_list


# def fabric(names, baseclass=HistoricalData):

#     for name in names:
#         # histricalDataToSQL(name)

#         class Meta:
#             db_table = '%s_historical_data' % name.lower()
#         attrs = {'__module__': baseclass.__module__, 'Meta': Meta}
#         # specify any other class attributes here
#         # E.g. you can specify extra fields:
#         # attrs.update({'my_field': models.CharField(max_length=100)})
#         # newclass = type(str(name), (baseclass,), attrs)
#         # globals()[name] = newclass


# fabric(['MTGE',
#         'CENX',
#         'ASPS',
#         'AMRN',
#         'AMPE',
#         'AMAG',
#         ])
