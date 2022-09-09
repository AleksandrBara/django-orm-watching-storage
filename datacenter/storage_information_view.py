from django.shortcuts import render
from datacenter.models import get_duration, format_duration, Visit


def storage_information_view(request):
    who_inside = []
    unfinished_visits = Visit.objects.filter(leaved_at__isnull=True)
    for visit in unfinished_visits:
        visit_info = {
            'who_entered': visit.passcard.owner_name,
            'entered_at': visit.entered_at,
            'duration': format_duration(get_duration(visit)),
        }
        who_inside.append(visit_info)
    context = {
        'non_closed_visits': who_inside,
    }
    return render(request, 'storage_information.html', context)
