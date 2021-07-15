import pika, json

from main import Job, db

params = pika.URLParameters('amqps://ldskdlgk:ghW99nsOB1ASfMqSWJNZOrs-7wbfSruw@baboon.rmq.cloudamqp.com/ldskdlgk')

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='main')


def callback(ch, method, properties, body):
    print('Received in main')
    data = json.loads(body)
    print(data)

    if properties.content_type == 'job_created':
        job = Job(id=data['id'], job_title=data['job_title'],
         job_type = data['job_type'],job_description=data['job_description'])
        db.session.add(job)
        db.session.commit()
        print('Job Created')

    elif properties.content_type == 'job_updated':
        job = Job.query.get(data['id'])
        job.job_title = data['job_title']
        job.job_type = data['job_type']
        job.job_description = data['job_description']
        db.session.commit()
        print('Job Updated')

    elif properties.content_type == 'job_deleted':
        job = Job.query.get(data)
        db.session.delete(job)
        db.session.commit()
        print('Job Deleted')


channel.basic_consume(queue='main', on_message_callback=callback, auto_ack=True)

print('Started Consuming')

channel.start_consuming()

channel.close()