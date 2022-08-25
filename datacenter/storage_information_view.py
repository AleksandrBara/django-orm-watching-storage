from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from django.utils.timezone import localtime
from datacenter.models import get_duration
from datacenter.models import format_duration


def storage_information_view(request):
    not_closed_visits = []
    not_end_visits = Visit.objects.filter(leaved_at=None)
    for visit in not_end_visits:
        duration = get_duration(visit)
        formatted_duration = format_duration(duration)
        moscow_entered_time = f'дата: {localtime(visit.entered_at).date()}   время: {localtime(visit.entered_at).time()} '
        visit_info = {
            'who_entered': '{}'.format(visit.passcard.owner_name),
            'entered_at': '{}'.format(moscow_entered_time),
            'duration': '{}'.format(formatted_duration),
        }
        not_closed_visits.append(visit_info)
    context = {
        'non_closed_visits': not_closed_visits,
    }
    return render(request, 'storage_information.html', context)
