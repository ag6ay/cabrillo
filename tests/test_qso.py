"""Test the QSO class."""
from datetime import datetime

import pytest

from cabrillo import QSO
from cabrillo.errors import InvalidQSOException


def test_yarc():
    """Test the QSO class with YARC QSO Party exchanges."""
    qso = QSO('14313', 'PH',
              datetime.strptime('May 30 2018 10:10PM', '%b %d %Y %I:%M%p'),
              'KX0XXX', '59', 'KX9XXX', '44',
              de_exch=['10', 'CO'], dx_exch=['20', 'IN'], t=None)
    assert qso.freq == '14313'
    assert qso.mo == 'PH'
    assert qso.date == datetime.strptime('May 30 2018 10:10PM',
                                         '%b %d %Y %I:%M%p')
    assert qso.de_call == 'KX0XXX'
    assert qso.dx_call == 'KX9XXX'
    assert qso.de_rst == '59'
    assert qso.dx_rst == '44'
    assert qso.de_exch == ['10', 'CO']
    assert qso.dx_exch == ['20', 'IN']
    assert qso.t is None
    assert str(qso) == '14313 PH 2018-05-30 2210 KX0XXX 59 10 CO KX9XXX 44 ' \
                       '20 IN'


def test_with_xmtr():
    """Test the QSO class with a transmitter designation."""
    qso = QSO('241G', 'PH',
              datetime.strptime('May 30 2018 10:10PM', '%b %d %Y %I:%M%p'),
              'KX0XXX', '59', 'KX9XXX', '44',
              de_exch=['CO'], dx_exch=['IL'], t=1)
    assert qso.freq == '241G'
    assert qso.mo == 'PH'
    assert qso.date == datetime.strptime('May 30 2018 10:10PM',
                                         '%b %d %Y %I:%M%p')
    assert qso.de_call == 'KX0XXX'
    assert qso.dx_call == 'KX9XXX'
    assert qso.de_rst == '59'
    assert qso.dx_rst == '44'
    assert qso.de_exch == ['CO']
    assert qso.dx_exch == ['IL']
    assert qso.t == 1
    assert str(qso) == '241G PH 2018-05-30 2210 KX0XXX 59 CO KX9XXX 44 ' \
                       'IL 1'


def test_invalid_mode():
    """Test the QSO class with invalid modes."""
    with pytest.raises(InvalidQSOException) as _:
        QSO('LIGHT', 'MCW', datetime.now(), 'KX0XXX', '59',
            'KX9XXX', '59')


def test_automatic_list():
    """Test automatic creation of lists for exchanges."""
    qso = QSO('LIGHT', 'CW', datetime.now(), 'KX0XXX', '59',
              'KX9XXX', '59')
    assert qso.de_exch == []
    assert qso.dx_exch == []