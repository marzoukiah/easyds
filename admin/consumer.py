import pika, json, os, django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "admin.settings")
django.setup()

from jobs.models import Job

params = pika.URLParameters('amqps://ldskdlgk:ghW99nsOB1ASfMqSWJNZOrs-7wbfSruw@baboon.rmq.cloudamqp.com/ldskdlgk')

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='admin')


def callback(ch, method, properties, body):
    print('Received in admin')
    id = json.loads(body)
    print(id)
    job = Job.objects.get(id=id)
    job.type = "done"
    job.save()
    print('Job likes increased!')


channel.basic_consume(queue='admin', on_message_callback=callback, auto_ack=True)

print('Started Consuming')

channel.start_consuming()

channel.close()