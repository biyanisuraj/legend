import collections
from .metrics_schema import (
    mysql_ec2_schema,
    pgsql_rds_schema,
    mysql_56_rds_schema,
    sqs_schema,
    springboot_schema,
    rabbitmq_schema,
    jmx_schema,
    haproxy_schema,
    elb_schema,
    django_schema,
    couchdb_schema,
    consul_schema,
    promtail_schema,
    celery_schema,
    platform_k8s_deployment_schema,
    redis_schema,
    systemcore_ec2_schema,
    s3_schema
)


def md(x, y):
    z = x.copy()
    z.update(y)
    return z


url_regex = '^(http:\/\/www\.|https:\/\/www\.|http:\/\/|https:\/\/)?[a-z0-9]+([\-\.]{1}[a-z0-9]+)*\.[a-z]{2,5}(:[0-9]{1,5})?(\/.*)?$'

panels_in_row_schema = {
    'panels_in_row': {'type': 'integer', 'required': False}
}

additional_panels_schema = {
    'panels': {'type': 'list', 'schema': {'type': 'dict', 'schema': {
        'title': {'type': 'string', 'required': True},
        'type': {'type': 'string', 'required': False, 'allowed': ['Graph']},
        'description': {'type': 'string', 'required': False}, 
        'targets': {'type': 'list', 'schema': {'type': 'dict', 'schema': {
            'metric': {'type': 'string', 'required': True},
            'legend': {'type': 'string', 'required': False},
            'ref_no': {'type': 'integer', 'coerce': int, 'required': False},
        }}},
        'alert_config': {'type': 'dict', 'required': False, 'schema':{
            'priority': {'type': 'string', 'required': True, 'allowed': ['P1','P2','P3','P4','P5']},
            'message': {'type': 'string', 'required': False},
            'rule': {'type': 'dict', 'required': False, 'schema': {
                'for_duration': {'type': 'string', 'required': True},
                'evaluate_every': {'type': 'string', 'required': True},
            }},
            'condition_query': {'type': 'list', 'required': True},
        }}
    }}}
}

default_panels_schema = md(panels_in_row_schema, additional_panels_schema)

schema = {
    'title': {'type': 'string', 'required': True, 'empty': False},
    'grafana_folder': {'type': 'string', 'required': True, 'empty': False},
    'alert_channels': {'type': 'list', 'schema': {'type': 'string'}, 'required': True},
    'service': {'type': 'string', 'required': True, 'empty': False},
    'environment': {'type': 'string', 'required': True, 'empty': False},
    'description': {'type': 'string', 'required': True, 'empty': False},
    'references': {
            'type': 'dict',
            'required': True,
            'schema': {
                'deployment': {'type': 'string', 'regex': url_regex, 'required': True, 'empty': False},
                'documentation': {'type': 'string', 'regex': url_regex, 'required': True, 'empty': False},
                'metrics_definition': {'type': 'string', 'regex': url_regex, 'required': True, 'empty': False},
            },
    },
    'tags': {'type': 'list', 'schema': {'type': 'string'}, 'required': True, 'empty': False},
    'components':{
        'type': 'dict',
        'required': False,
        'schema': {
            'celery': {'type': 'dict', 'schema':  md(default_panels_schema, celery_schema), 'required': False},
            'promtail': {'type': 'dict', 'schema':  md(default_panels_schema, promtail_schema), 'required': False},
            'platform_k8s_deployment': {'type': 'dict', 'schema': md(default_panels_schema, platform_k8s_deployment_schema), 'required': False},
            'redis': {'type': 'dict', 'schema':  md(default_panels_schema, redis_schema), 'required': False},
            'systemcore_ec2': {'type': 'dict', 'schema':  md(default_panels_schema, systemcore_ec2_schema), 'required': False},
            's3': {'type': 'dict', 'schema': md(default_panels_schema, s3_schema), 'required': False},
            'consul': {'type': 'dict', 'schema':  md(default_panels_schema, consul_schema), 'required': False},
            'couchdb': {'type': 'dict', 'schema':  md(default_panels_schema, couchdb_schema), 'required': False},
            'django': {'type': 'dict', 'schema':  md(default_panels_schema, django_schema), 'required': False},
            'elb': {'type': 'dict', 'schema':  md(default_panels_schema, elb_schema), 'required': False},
            'haproxy': {'type': 'dict', 'schema':  md(default_panels_schema, haproxy_schema), 'required': False},
            'jmx': {'type': 'dict', 'schema':  md(default_panels_schema, jmx_schema), 'required': False},
            'rabbitmq': {'type': 'dict', 'schema':  md(default_panels_schema, rabbitmq_schema), 'required': False},
            'springboot': {'type': 'dict', 'schema':  md(default_panels_schema, springboot_schema), 'required': False},
            'sqs': {'type': 'dict', 'schema':  md(default_panels_schema, sqs_schema), 'required': False},
            'mysql_56_rds': {'type': 'dict', 'schema':  md(default_panels_schema, mysql_56_rds_schema), 'required': False},
            'mysql_ec2': {'type': 'dict', 'schema':  md(default_panels_schema, mysql_ec2_schema), 'required': False},
            'pgsql_rds': {'type': 'dict', 'schema':  md(default_panels_schema, pgsql_rds_schema), 'required': False},
            }
      }
}
