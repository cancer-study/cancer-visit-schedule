from edc_visit_schedule import VisitSchedule, site_visit_schedules

from .schedule import schedule1

visit_schedule1 = VisitSchedule(
    name='visit_schedule1',
    verbose_name='Cancer',
    offstudy_model='cancer_subject.subjectoffstudy',
    locator_model='cancer_subject.subject_locator',
    death_report_model='cancer_subject.af005',
    previous_visit_schedule=None)

visit_schedule1.add_schedule(schedule1)

site_visit_schedules.register(visit_schedule1)
