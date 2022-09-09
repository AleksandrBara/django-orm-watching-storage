from datacenter.models import get_duration, format_duration, Passcard, Visit, is_visit_long
from django.shortcuts import get_list_or_404, get_object_or_404, render


def passcard_info_view(request, passcode):
    this_passcard_visits = []
    owner_name = get_object_or_404(Passcard,
                                   passcode=passcode)
    one_person_all_visits = get_list_or_404(Visit,
                                            passcard=owner_name)
    for visit in one_person_all_visits:
        visit_info = {
            'entered_at': visit.entered_at,
            'duration': format_duration(get_duration(visit)),
            'is_strange': is_visit_long(visit)
        }
        this_passcard_visits.append(visit_info)
    context = {
        'passcard': owner_name,
        'this_passcard_visits': this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)
