__author__ = 'harrison'

import pytz
from datetime import datetime
from datetime import timedelta
from datetime import tzinfo
from dateutil.relativedelta import relativedelta
from django.utils.timezone import utc
from django.utils.timezone import localtime
from django.utils.timezone import now
from django.utils.timezone import is_aware
from django.utils.timezone import is_naive
from django.utils.timezone import get_default_timezone
from django.utils.timezone import get_default_timezone_name


if __name__ == "__main__":
    from django.conf import settings
    settings.configure(USE_TZ=True, TIME_ZONE='Asia/Shanghai')


class TimeZone(object):
    # <DstTzInfo 'Asia/Shanghai' LMT+8:00:00 STD>
    # actutal is <DstTzInfo 'Asia/Shanghai' LMT+8:06:00 STD>
    DEFAULT_TIMEZONE = get_default_timezone()

    @classmethod
    def navie_to_aware(cls, naive_datetime, tz=DEFAULT_TIMEZONE):
        """

        :param naive_datetime:
        :param tz:
        :return:
        """
        # return +08:06
        # return naive_datetime.replace(tzinfo=tz)

        # return +08:00
        return tz.localize(naive_datetime)

    @classmethod
    def datetime_to_timezone(cls, d, tz=utc):
        if is_naive(d):
            # change to local aware datetime
            d = cls.navie_to_aware(d)
        return localtime(d, timezone=tz)

    @classmethod
    def datetime_to_utc(cls, d):
        """

        :param d:
        :return:
        """
        return cls.datetime_to_timezone(d, tz=utc)

    @classmethod
    def utc_to_local(cls, utc_datetime):
        return cls.utc_to_timezone(utc_datetime)

    @staticmethod
    def utc_to_timezone(utc_datetime, tz=DEFAULT_TIMEZONE):
        if is_naive(utc_datetime):
            utc_datetime = utc_datetime.replace(tzinfo=utc)
        return localtime(utc_datetime, timezone=tz)

    @staticmethod
    def utc_now():
        return now()

    @classmethod
    def local_now(cls):
        return cls.DEFAULT_TIMEZONE.localize(datetime.now())

    @staticmethod
    def increate_months(cur_datetime, n=1):
        assert n >= 0
        return cur_datetime + relativedelta(months=n)

    @staticmethod
    def decreate_months(cur_datetime, n=1):
        assert n >= 0
        return cur_datetime - relativedelta(months=n)

    @staticmethod
    def month_range(year, month, tz=utc):
        assert year >= 0
        assert 12 >= month >= 1
        start_date = datetime(year, month, 1)
        end_date = TimeZone.increate_months(start_date)
        return TimeZone.datetime_to_timezone(start_date, tz), TimeZone.datetime_to_timezone(end_date, tz)


if __name__ == "__main__":
    local_now = datetime.now()
    print 'local_time: %s' % TimeZone.navie_to_aware(local_now, pytz.timezone(pytz.country_timezones('cn')[0]))
    print 'local_time: %s' % TimeZone.navie_to_aware(local_now)
    print 'utc_time: %s' % TimeZone.datetime_to_utc(local_now)
    print 'utc_now: %s' % TimeZone.utc_now()
    print 'local_now: %s' % TimeZone.local_now()

    print 'first in 2014-08 in utc: %s' % TimeZone.datetime_to_utc(datetime(2014, 8, 1))
    print 'last  in 2014-08 in utc: %s' % TimeZone.datetime_to_utc(datetime(2014, 9, 1))

    local_d1 = datetime(2014, 9, 15, 23, 22, 10)
    assert TimeZone.navie_to_aware(local_d1) == TimeZone.utc_to_local(TimeZone.datetime_to_utc(local_d1))

    print '2013-12: (%s~%s)' % (TimeZone.month_range(2013, 12))
    print '2014-01: (%s~%s)' % (TimeZone.month_range(2014, 1))
