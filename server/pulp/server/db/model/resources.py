from mongoengine import Document, StringField


class ReservedResource(Document):
    """
    Instances of this class represent resources that have been reserved.

    :ivar task_id:       The uuid of the task associated with this reservation
    :type task_id:       basestring
    :ivar worker_name:   The name of the worker associated with this reservation.
    :type worker_name:   basestring
    :ivar resource_id:   The name of the resource reserved for the task.
    :type resource_id:   basestring
    """
    task_id = StringField(db_field='_id', primary_key=True)
    worker_name = StringField()
    resource_id = StringField()

    # For backward compatibility
    _ns = StringField(default='reserved_resources')

    meta = {'collection': 'reserved_resources',
            'indexes': ['-worker_name', '-resource_id'],
            'allow_inheritance': False}
