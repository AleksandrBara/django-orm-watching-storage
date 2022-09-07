from datacenter.models import get_duration, format_duration, Passcard, Visit, is_visit_long
from django.shortcuts import get_list_or_404, get_object_or_404, render


def passcard_info_view(request, passcode):
    passcard = Passcard.objects.all()
    this_passcard_visits = []
    card_onwer_name = get_object_or_404(Passcard,
                                   passcode=passcode)
    passcard_visits = get_list_or_404(Visit,
                                            passcard=card_onwer_name)
    for visit in passcard_visits:
        visit_info = {
            'entered_at': visit.entered_at,
            'duration': format_duration(get_duration(visit)),
            'is_strange': is_visit_long(visit)
        }
        this_passcard_visits.append(visit_info)
    context = {
        'passcard': passcard,
        'this_passcard_visits': this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)
