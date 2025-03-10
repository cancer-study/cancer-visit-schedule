from dateutil.relativedelta import relativedelta
from edc_visit_schedule import Schedule, Visit

from .crfs import crf
from .requisitions import requisitions

# schedule for new participants 6 months intervals for visits
schedule2 = Schedule(
    name='schedule_6months',
    verbose_name='Cancer (6months)',
    onschedule_model='cancer_subject.onschedule6months',
    offschedule_model='cancer_prn.subjectoffstudy',
    consent_model='cancer_subject.subjectconsent',
    appointment_model='cancer_subject.appointment')

visit0 = Visit(
    code='1000',
    title='Enrollment Visit',
    timepoint=0,
    rbase=relativedelta(days=0),
    rlower=relativedelta(days=0),
    rupper=relativedelta(days=0),
    requisitions=requisitions,
    crfs=crf.get(1000),
    facility_name='5-day clinic')

visit1 = Visit(
    code='1600',
    title='Follow-up Visit 6 months',
    timepoint=2,
    rbase=relativedelta(months=6),
    rlower=relativedelta(days=0),
    rupper=relativedelta(days=0),
    requisitions=requisitions,
    crfs=crf.get(1600),
    facility_name='5-day clinic')

visit2 = Visit(
    code='2200',
    title='Follow-up Visit 12 months',
    timepoint=4,
    rbase=relativedelta(months=12),
    rlower=relativedelta(days=0),
    rupper=relativedelta(days=0),
    requisitions=requisitions,
    crfs=crf.get(2200),
    facility_name='5-day clinic')

visit3 = Visit(
    code='2800',
    title='Follow-up Visit 18 months',
    timepoint=6,
    rbase=relativedelta(months=18),
    rlower=relativedelta(days=0),
    rupper=relativedelta(days=0),
    requisitions=requisitions,
    crfs=crf.get(2800),
    facility_name='5-day clinic')

visit4 = Visit(
    code='3400',
    title='Follow-up Visit 24 months',
    timepoint=8,
    rbase=relativedelta(months=24),
    rlower=relativedelta(days=0),
    rupper=relativedelta(days=0),
    requisitions=requisitions,
    crfs=crf.get(3400),
    facility_name='5-day clinic')

visit5 = Visit(
    code='4000',
    title='Follow-up Visit 30 months',
    timepoint=10,
    rbase=relativedelta(months=30),
    rlower=relativedelta(days=0),
    rupper=relativedelta(days=0),
    requisitions=requisitions,
    crfs=crf.get(4000),
    facility_name='5-day clinic')

visit6 = Visit(
    code='4600',
    title='Follow-up Visit 36 months',
    timepoint=12,
    rbase=relativedelta(months=36),
    rlower=relativedelta(days=0),
    rupper=relativedelta(days=0),
    requisitions=requisitions,
    crfs=crf.get(4600),
    facility_name='5-day clinic')

visit7 = Visit(
    code='5200',
    title='Follow-up Visit 42 months',
    timepoint=14,
    rbase=relativedelta(months=42),
    rlower=relativedelta(days=0),
    rupper=relativedelta(days=0),
    requisitions=requisitions,
    crfs=crf.get(5200),
    facility_name='5-day clinic')

visit8 = Visit(
    code='5800',
    title='Follow-up Visit 48 months',
    timepoint=16,
    rbase=relativedelta(months=48),
    rlower=relativedelta(days=0),
    rupper=relativedelta(days=0),
    requisitions=requisitions,
    crfs=crf.get(5800),
    facility_name='5-day clinic')

visit9 = Visit(
    code='6400',
    title='Follow-up Visit 54 months',
    timepoint=18,
    rbase=relativedelta(months=54),
    rlower=relativedelta(days=0),
    rupper=relativedelta(days=0),
    requisitions=requisitions,
    crfs=crf.get(6400),
    facility_name='5-day clinic')

visit10 = Visit(
    code='7000',
    title='Follow-up Visit 60 months',
    timepoint=20,
    rbase=relativedelta(months=60),
    rlower=relativedelta(days=0),
    rupper=relativedelta(days=0),
    requisitions=requisitions,
    crfs=crf.get(7000),
    facility_name='5-day clinic')

schedule2.add_visit(visit=visit0)
schedule2.add_visit(visit=visit1)
schedule2.add_visit(visit=visit2)
schedule2.add_visit(visit=visit3)
schedule2.add_visit(visit=visit4)
schedule2.add_visit(visit=visit5)
schedule2.add_visit(visit=visit6)
schedule2.add_visit(visit=visit7)
schedule2.add_visit(visit=visit8)
schedule2.add_visit(visit=visit9)
schedule2.add_visit(visit=visit10)
