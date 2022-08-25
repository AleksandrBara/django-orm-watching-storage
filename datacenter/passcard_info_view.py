from datacenter.models import is_visit_long
from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from django.utils.timezone import localtime
from datacenter.models import get_duration
from datacenter.models import format_duration
from django.shortcuts import get_list_or_404
from django.shortcuts import get_object_or_404


def passcard_info_view(request, passcode):
    passcard = Passcard.objects.all()[0]
    this_passcard_visits = []
    onwer_name = get_object_or_404(Passcard, passcode=passcode)
    one_person_all_visits = get_list_or_404(Visit, passcard=onwer_name)
    for visit in one_person_all_visits:
        entered_date = localtime(visit.entered_at).date()
        entered_time = localtime(visit.entered_at).time()
        entered_at = f'дата: {entered_date}   время: {entered_time}'
        visit_duration = get_duration(visit)
        visit_format_duration = format_duration(visit_duration)
        visit_chek = is_visit_long(visit)
        visit_info = {
            'entered_at': entered_at,
            'duration': visit_format_duration,
            'is_strange': visit_chek
        }
        this_passcard_visits.append(visit_info)
    context = {
        'passcard': passcard,
        'this_passcard_visits': this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)
